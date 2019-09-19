import openstack

# Initialize and turn on debug logging
openstack.enable_logging(debug=False)

# Initialize connection
# Cloud configs are read with openstack.config
conn = openstack.connect(cloud='openstack')

# Find a flavor with at least 512M of RAM
flavor = conn.get_flavor_by_ram(1024)

image = conn.get_image('bionic')

network = conn.get_network('1489179c-45b7-4973-9d51-17044fda6000')

# Boot a server, wait for it to boot, and then do whatever is needed
# to get a public ip for it.
print('\n\n\nVai CRIAR')
conn.create_server('decomanu', image=image, flavor=flavor, wait=True, auto_ip=True, network=network)
print('CRIOU\n\n\n')