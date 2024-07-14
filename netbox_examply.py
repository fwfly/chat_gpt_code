import pynetbox
import csv

# 讀取 CSV 檔案
csv_file_path = 'your_file.csv'

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    # 將每一行轉換為字典並存入列表中
    data = [row for row in csvreader]

# 顯示資料
for item in data:
    print(item)


class RackManager:
    def __init__(self, netbox_url, token):
        self.nb = pynetbox.api(netbox_url, token=token)

    def get_or_create_site(self, site_name):
        sites = self.nb.dcim.sites.filter(name=site_name)
        if sites:
            return sites[0].id
        else:
            new_site = self.nb.dcim.sites.create(name=site_name, slug=site_name.lower().replace(" ", "-"))
            return new_site.id
    
    def get_or_create_rack(self, rack_name):
        racks = self.nb.dcim.racks.filter(name=rack_name)
        if racks:
            return racks[0].id
        else:
            new_rack = self.nb.dcim.racks.create(name=rack_name)
            return new_rack.id

    def get_or_create_device_role(self, role_name):
        roles = self.nb.dcim.device_roles.filter(name=role_name)
        if roles:
            return roles[0].id
        else:
            new_role = self.nb.dcim.device_roles.create(name=role_name, slug=role_name.lower().replace(" ", "-"))
            return new_role.id

    def get_or_create_device_type(self, device_type, manufacturer_name):
        manufacturers = self.nb.dcim.manufacturers.filter(name=manufacturer_name)
        if manufacturers:
            manufacturer_id = manufacturers[0].id
        else:
            new_manufacturer = self.nb.dcim.manufacturers.create(name=manufacturer_name, slug=manufacturer_name.lower().replace(" ", "-"))
            manufacturer_id = new_manufacturer.id

        device_types = self.nb.dcim.device_types.filter(model=device_type, manufacturer_id=manufacturer_id)
        if device_types:
            return device_types[0].id
        else:
            new_device_type = self.nb.dcim.device_types.create(model=device_type, manufacturer=manufacturer_id, slug=device_type.lower().replace(" ", "-"))
            return new_device_type.id

    def add_or_replace_device(self, rack_name, device_name, position, device_type, site_name, device_role, manufacturer_name):

        site_id = self.get_or_create_site(site_name)        
        rack_id = self.get_or_create_rack(rack_name)
        
        sites = self.nb.dcim.sites.filter(name=site_name)
        if not sites:
            new_site = self.nb.dcim.sites.create(name=site_name, slug=site_name.lower().replace(" ", "-"))
            site_id = new_site.id
        else:
            site_id = sites[0].id

        device_type_id = self.get_or_create_device_type(device_type, manufacturer_name)
        device_role_id = self.get_or_create_device_role(device_role)

        devices_in_rack = self.nb.dcim.devices.filter(rack_id=rack_id, position=position)
        if devices_in_rack:
            devices_in_rack[0].delete()

        new_device = self.nb.dcim.devices.create(
            name=device_name,
            device_type=device_type_id,
            rack=rack_id,
            position=position,
            site=site_id,
            device_role=device_role_id
        )
        return new_device.id

# 使用示例
if __name__ == "__main__":
    netbox_url = "http://your-netbox-instance.com"
    token = "your-api-token"
    
    rack_manager = RackManager(netbox_url, token)
    device_id = rack_manager.add_or_replace_device(
        rack_name="my-rack",
        device_name="my-device",
        position=1,
        device_type="device-model",
        site_name="my-site",
        device_role="server",
        manufacturer_name="my-manufacturer"
    )
    print(f"Device ID: {device_id}")
