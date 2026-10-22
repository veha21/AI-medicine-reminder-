from sklearn.tree import DecisionTreeClassifier

# Training Data
# [Sleep Late, Busy Schedule]

X = [
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0]
]

# 1 = Missed Medicine
# 0 = Took Medicine

y = [1, 1, 0, 0]

# Create AI Model
model = DecisionTreeClassifier()

# Train Model
model.fit(X, y)

# Predict

sleep_late = int(input("Sleep Late? (1=yes, 0=no): "))
busy = int(input("Busy Schedule? (1=yes, 0=no): "))

prediction = model.predict([[sleep_late, busy]])

if prediction[0] == 1:
    print("⚠ User may MISS medicine")
else:
    print("✅ User likely to take medicine")
    