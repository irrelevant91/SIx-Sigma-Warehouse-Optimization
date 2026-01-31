import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df_metrics = pd.read_excel('raw_metrics.xlsx', sheet_name='Daily_Metrics')
df_pareto = pd.read_excel('raw_metrics.xlsx', sheet_name='Pareto_Causes')

# 1. Generate Control Chart
plt.figure(figsize=(12, 6))
plt.plot(df_metrics['Date'], df_metrics['Avg Discrepancy Rate'], marker='o', label='Discrepancy Rate')
plt.axhline(y=df_metrics['Mean'][0], color='g', linestyle='--', label='Mean')
plt.axhline(y=df_metrics['UCL'][0], color='r', linestyle='--', label='UCL')
plt.title('Process Control Chart: Inventory Discrepancies')
plt.xlabel('Date')
plt.ylabel('Rate (%)')
plt.legend()
plt.savefig('control_chart.png')

# 2. Generate Pareto Chart
df_pareto = df_pareto.sort_values('Count', ascending=False)
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(df_pareto['Cause'], df_pareto['Count'], color='steelblue')
ax1.set_ylabel('Frequency')
ax2 = ax1.twinx()
ax2.plot(df_pareto['Cause'], df_pareto['Cum_Pct'], color='red', marker='D')
ax2.set_ylabel('Cumulative %')
plt.title('Pareto Analysis of Root Causes')
plt.savefig('pareto_chart.png')