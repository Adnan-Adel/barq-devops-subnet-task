import pandas as pd
import ipaddress

# Load data
data = pd.read_excel('ip_data.xlsx')

cidrs = []
network_addresses = []
broadcast_addresses = []
usable_hosts = []
first_hosts = []
last_hosts = []

# Process each row
for index, row in data.iterrows():
    ip = row['IP Address']
    mask = row['Subnet Mask']

    # Calculate CIDR
    cidr = ipaddress.IPv4Network(f'0.0.0.0/{mask}').prefixlen
    cidrs.append(cidr)

    # Create network
    interface = ipaddress.IPv4Interface(f'{ip}/{mask}')
    network = interface.network

    # Network and broadcast
    network_addresses.append(str(network.network_address))
    broadcast_addresses.append(str(network.broadcast_address))

    # Usable hosts
    num_hosts = network.num_addresses - 2 if network.num_addresses > 2 else 0
    usable_hosts.append(num_hosts)

    if num_hosts > 0:
        first_hosts.append(str(network.network_address + 1))
        last_hosts.append(str(network.broadcast_address - 1))
    else:
        first_hosts.append(None)
        last_hosts.append(None)

# Add new columns
data['CIDR'] = cidrs
data['Network Address'] = network_addresses
data['Broadcast Address'] = broadcast_addresses
data['Usable Hosts'] = usable_hosts
data['First Host'] = first_hosts
data['Last Host'] = last_hosts

# Export full details
data.to_csv('subnet_report.csv', index=False)

# Group by CIDR and subnet
summary = data.groupby(['Network Address', 'CIDR']).agg({
    'Usable Hosts': 'sum',
    'IP Address': 'count'
}).reset_index()

summary = summary.rename(columns={'IP Address': 'IP Count'})

# Save grouped summary
summary.to_csv('summary_report.csv', index=False)

print('Analysis complete. Reports generated.')