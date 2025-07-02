import pandas as pd
import matplotlib.pyplot as plt

# 1. Load grouped summary
data = pd.read_csv('summary_report.csv')

# 2. Create a Subnet label
data['Subnet'] = data['Network Address'] + '/' + data['CIDR'].astype(str)

# 3. Sort by Usable Hosts for clearer bars
data = data.sort_values(by='Usable Hosts', ascending=False)

# 4. Plot
plt.figure(figsize=(12, 6))
plt.bar(data['Subnet'], data['Usable Hosts'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Subnet (Network/CIDR)')
plt.ylabel('Number of Usable Hosts')
plt.title('Number of Usable Hosts per Subnet')
plt.tight_layout()

# 5. Save chart
plt.savefig('network_plot.png')
print('Bar chart saved as network_plot.png')