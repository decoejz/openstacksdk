import openstack

# Initialize and turn on debug logging
openstack.enable_logging(debug=False)

# Initialize connection
# Cloud configs are read with openstack.config
conn = openstack.connect(cloud='openstack')

print('\n\n\nVai DELETAR')
conn.delete_server('decomanu')
print('DELETOU\n\n\n')