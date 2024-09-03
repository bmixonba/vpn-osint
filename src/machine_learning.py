import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler

# Generate some chaotic time series data (e.g., Lorenz system)
def generate_chaotic_data(n_points):
    data = np.zeros((n_points, 3))
    # Initialization
    x, y, z = 0.1, 0, 0
    dt = 0.01
    for i in range(n_points):
        x_dot = 10 * (y - x)
        y_dot = x * (28 - z) - y
        z_dot = x * y - 8/3 * z
        x += x_dot * dt
        y += y_dot * dt
        z += z_dot * dt
        data[i] = [x, y, z]
    return data

data = generate_chaotic_data(10000)

# Normalize data
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

# Prepare data for LSTM
def create_dataset(data, time_steps=1):
    X, y = [], []
    for i in range(len(data) - time_steps):
        X.append(data[i:(i + time_steps), :])
        y.append(data[i + time_steps, :])
    return np.array(X), np.array(y)

time_steps = 10
X, y = create_dataset(data_scaled, time_steps)

# Split into train and test sets
train_size = int(len(X) * 0.67)
test_size = len(X) - train_size
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Build LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(time_steps, 3)))
model.add(LSTM(50))
model.add(Dense(3))
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=20, batch_size=64, validation_data=(X_test, y_test))

# Predict and inverse transform the data
predicted = model.predict(X_test)
predicted = scaler.inverse_transform(predicted)

# Plot the results
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.plot(predicted[:, 0], label='Predicted X')
plt.plot(data[train_size+time_steps:, 0], label='True X')
plt.legend()
plt.show()
