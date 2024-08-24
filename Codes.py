import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('C:/Users/User/Desktop/Github/AI_Detect_Failure/Dataset/pump_sensor_data.csv')

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Group by pump_id and calculate failure rate
failure_rates = df.groupby('pump_id')['failure'].mean().sort_values(ascending=False)

print("Failure rates by pump:")
print(failure_rates)

# Plot failure rates
plt.figure(figsize=(12, 6))
failure_rates.plot(kind='bar')
plt.title('Failure Rates by Pump')
plt.xlabel('Pump ID')
plt.ylabel('Failure Rate')
plt.tight_layout()
plt.show()

# Identify the pump with the highest failure rate
problematic_pump = failure_rates.index[0]

print(f"\
Most problematic pump: {problematic_pump}")

# Analyze sensor readings for the problematic pump
problematic_pump_data = df[df['pump_id'] == problematic_pump]

# Plot sensor readings for the problematic pump
fig, axs = plt.subplots(3, 2, figsize=(15, 15))
fig.suptitle(f'Sensor Readings for Pump {problematic_pump}')

axs[0, 0].plot(problematic_pump_data['timestamp'], problematic_pump_data['pressure'])
axs[0, 0].set_title('Pressure')
axs[0, 0].set_xlabel('Timestamp')

axs[0, 1].plot(problematic_pump_data['timestamp'], problematic_pump_data['temperature'])
axs[0, 1].set_title('Temperature')
axs[0, 1].set_xlabel('Timestamp')

axs[1, 0].plot(problematic_pump_data['timestamp'], problematic_pump_data['flow_rate'])
axs[1, 0].set_title('Flow Rate')
axs[1, 0].set_xlabel('Timestamp')

axs[1, 1].plot(problematic_pump_data['timestamp'], problematic_pump_data['vibration'])
axs[1, 1].set_title('Vibration')
axs[1, 1].set_xlabel('Timestamp')

axs[2, 0].plot(problematic_pump_data['timestamp'], problematic_pump_data['power_consumption'])
axs[2, 0].set_title('Power Consumption')
axs[2, 0].set_xlabel('Timestamp')

axs[2, 1].plot(problematic_pump_data['timestamp'], problematic_pump_data['hours_since_maintenance'])
axs[2, 1].set_title('Hours Since Maintenance')
axs[2, 1].set_xlabel('Timestamp')

plt.tight_layout()
plt.show()

print("Analysis complete.")
