import numpy as np

# lat, lon = 45.7965772, -74.1137449
# lat, lon = 45.7965772, -74.1137449
lat, lon = 45.7894027, -74.0175779

print("Age;Latitude;Longitude")

for i in range(100):
    age = 18 + i // 20
    age_center = np.array([lat, lon]) + 0.01 * np.random.random((1, 2))
    print(f'{age};{age_center[0, 0]};{age_center[0, 1]}')

for i in range(75):
    age = 35 + i // 10
    age_center = np.array([lat + 0.005, lon + 0.015]) + 0.01 * np.random.random((1, 2))
    print(f'{age};{age_center[0, 0]};{age_center[0, 1]}')

for i in range(50):
    age = 65 + i // 5
    age_center = np.array([lat - 0.005, lon + 0.015]) + 0.01 * np.random.random((1, 2))
    print(f'{age};{age_center[0, 0]};{age_center[0, 1]}')
