import pynetbox

class NetBoxManager:
    def __init__(self, api_url, token):
        self.nb = pynetbox.api(api_url, token=token)
        
    def list_racks(self):
        """Lists all racks"""
        try:
            return self.nb.dcim.racks.all()
        except Exception as e:
            print(f"An error occurred while listing racks: {e}")
            return []

    def list_device_roles(self):
        """Lists all device roles"""
        try:
            return self.nb.dcim.device_roles.all()
        except Exception as e:
            print(f"An error occurred while listing device roles: {e}")
            return []

    def list_devices(self):
        """Lists all devices"""
        try:
            return self.nb.dcim.devices.all()
        except Exception as e:
            print(f"An error occurred while listing devices: {e}")
            return []

    def add_device(self, name, device_role, device_type, site, rack=None):
        """Adds a new device"""
        try:
            device_data = {
                "name": name,
                "device_role": device_role,
                "device_type": device_type,
                "site": site,
            }
            if rack:
                device_data["rack"] = rack
            
            return self.nb.dcim.devices.create(device_data)
        except Exception as e:
            print(f"An error occurred while adding the device: {e}")
            return None

# Usage example:
if __name__ == "__main__":
    api_url = "http://your-netbox-instance/api/"
    token = "your-api-token"

    nb_manager = NetBoxManager(api_url, token)
    
    racks = nb_manager.list_racks()
    print("Racks:", racks)
    
    device_roles = nb_manager.list_device_roles()
    print("Device Roles:", device_roles)
    
    devices = nb_manager.list_devices()
    print("Devices:", devices)
    
    new_device = nb_manager.add_device(
        name="New Device",
        device_role=1,  # Assuming 1 is the ID of the device role
        device_type=1,  # Assuming 1 is the ID of the device type
        site=1          # Assuming 1 is the ID of the site
    )
    print("New Device:", new_device)
