# 建立 Vagrant VM

```
mkdir my-vm && cd my-vm
vagrant init ubuntu/jammy64
```

這邊要改 dncp

vim Vagrantfile
```
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.network "private_network", type: "dhcp"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
  end
end
```

```
vagrant up
vagrant ssh
```

# 使用 provision 安裝 cephadm

```
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.network "private_network", type: "dhcp"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
  end
  config.vm.provision "shell", inline: <<-SHELL
    apt update
    apt install -y curl
    curl --fsSL https://raw.githubusercontent.com/ceph/ceph/main/src/cephadm/cephadm -o cephadm
    chmod +x cephadm
    mv cephadm /usr/local/bin/
  SHELL
end

```
vagrant up --provision

# 設定 vagrant with 靜態 IP

```
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.network "private_network", ip: "192.168.56.100"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL
    cat <<EOF > /etc/netplan/01-netcfg.yaml
    network:
      version: 2
      ethernets:
        ens3:
          addresses: [192.168.56.100/24]
          gateway4: 192.168.56.1
          nameservers:
            addresses: [8.8.8.8, 8.8.4.4]
    EOF
    netplan apply
  SHELL
end
```

# 設定多台 vm 用 static ip
```
Vagrant.configure("2") do |config|
  # 定義要建立的 VM
  nodes = [
    { name: "node1", ip: "192.168.56.101" },
    { name: "node2", ip: "192.168.56.102" },
    { name: "node3", ip: "192.168.56.103" }
  ]

  nodes.each do |node|
    config.vm.define node[:name] do |node_config|
      node_config.vm.box = "ubuntu/jammy64"  # Ubuntu 22.04 LTS

      # 設定 Private Network（靜態 IP）
      node_config.vm.network "private_network", ip: node[:ip]

      # 設定虛擬機資源
      node_config.vm.provider "virtualbox" do |vb|
        vb.memory = "2048"
        vb.cpus = 2
      end

      # 自動化設定（Provisioning）
      node_config.vm.provision "shell", inline: <<-SHELL
        echo "Provisioning #{node[:name]} with static IP: #{node[:ip]}"
        sudo apt update
      SHELL
    end
  end
end

```
