Vagrant.configure(2) do |config|
  # Virtual machine parameters
  config.vm.box = "Samael500/insta"
  # config.vm.box = "chef/debian-7.8"
  config.vm.network "private_network", ip: "10.1.1.123"
  config.vm.synced_folder ".", "/home/vagrant/proj"
  config.vm.hostname = "insta"
  config.vm.post_up_message = "insta dev server successfuly started.
    Connect to host with:
    http://10.1.1.123/
    or over ssh with `vagrant ssh`

    Admin user credentials:
    login: root
    password: 123123
    "
  # Set box name
  config.vm.define :insta_vagrant do |t|
  end
  # Virtualbox specific parameters
  config.vm.provider "virtualbox" do |v|
    v.name = "insta_vagrant"
    v.memory = 1024
    v.cpus = 2
  end
  # Provisioning with Ansible
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision/playbook.dev.yml"
  end
end
