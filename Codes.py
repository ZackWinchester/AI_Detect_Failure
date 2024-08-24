import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv ("pump_sensor_data.csv")

data['timestamp'] = pd.to_datetime(data['timestamp'])

fr = data.groupby('pump_id')['failure'].mean().sort_values(ascending=False)

print("Failure rates by pump:")
print(fr)

plt.figure(figsize=(12, 6))
fr.plot(kind='bar')
plt.title('Failure Rates by Pump')
plt.xlabel('Pump ID')
plt.ylabel('Failure Rate')
plt.tight_layout()
plt.show()

problematic_pump = fr.index[0]

print(f"\Most problematic pump: {problematic_pump}")

problematic_pump_data = data[data['pump_id'] == problematic_pump]

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
