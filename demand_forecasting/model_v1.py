# demand_forecasting/model_v1.py
import pandas as pd
from sklearn.linear_model import LinearRegression

# Fake sample data
data = {
    'week': [1, 2, 3, 4, 5],
    'demand': [200, 220, 250, 270, 300]
}
df = pd.DataFrame(data)

# Train model
X = df[['week']]
y = df['demand']
model = LinearRegression()
model.fit(X, y)

# Predict week 6
predicted = model.predict([[6]])
print(f"Predicted demand for week 6: {predicted[0]:.2f}")
