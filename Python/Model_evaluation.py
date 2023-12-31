import numpy as np

# data
size = np.array([1000, 1500, 2000, 2500, 3000])
price = np.array([15000, 25000, 35000, 45000, 55000])
predicted_price = np.array([15500, 24000, 35000, 46000, 55500])# Predicted prices ---> regression model

mse = np.mean((price - predicted_price) ** 2)# How to calculate mean squared error
print("Mean Squared Error (MSE):", mse)

# How to calculate accuracy and error rate

acceptable_error_margin = 0.1  # 10% acceptable error margin
absolute_errors = np.abs(price - predicted_price)
accurate_predictions = np.sum(absolute_errors <= (acceptable_error_margin * price))
accuracy = accurate_predictions / len(price)
error_rate = 1 - accuracy

print("Accuracy:", accuracy)
print("Error Rate:", error_rate)
acceptable_error_margin = 0.1  # 10% acceptable error margin

if error_rate <= acceptable_error_margin:
    print("desired level of accuracy")
else:
    print("not desired level of accuracy")
                