"""
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import graphviz

# Step 1: Data generation
credit_score = [500, 600, 700, 550, 750, 800, 650, 700, 600, 550]
income = [3000, 5000, 4000, 2000, 6000, 7000, 5500, 4000, 3000, 2000]
loan_amount = [10000, 20000, 15000, 5000, 25000, 30000, 18000, 15000, 10000, 8000]
loan_term = ['short-term', 'long-term', 'long-term', 'short-term', 'long-term',
             'long-term', 'short-term', 'long-term', 'short-term', 'short-term']
employment_status = ['employed', 'employed', 'self-employed', 'unemployed', 'employed',
                     'self-employed', 'employed', 'other', 'self-employed', 'employed']
previous_delinquencies = ['no', 'yes', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'no', 'yes']
loan_approval = ['yes', 'no', 'yes', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'no']

# Step 2: Data preprocessing
X = list(zip(credit_score, income, loan_amount, loan_term, employment_status, previous_delinquencies))
y = loan_approval

# Encoding categorical variables
X_encoded = []
for i in range(len(X)):
    encoded = []
    encoded.append(X[i][0])
    encoded.append(X[i][1])
    encoded.append(X[i][2])
    encoded.append(1 if X[i][3] == 'long-term' else 0)
    if X[i][4] == 'employed':
        encoded += [1, 0, 0]
    elif X[i][4] == 'self-employed':
        encoded += [0, 1, 0]
    elif X[i][4] == 'unemployed':
        encoded += [0, 0, 1]
    else:
        encoded += [0, 0, 0]
    encoded.append(1 if X[i][5] == 'yes' else 0)
    X_encoded.append(encoded)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Step 3: Build the decision tree classifier
classifier = DecisionTreeClassifier()

# Step 4: Train the model
classifier.fit(X_train, y_train)

# Step 5: Evaluate the classifier
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 6: Visualize the decision tree
dot_data = tree.export_graphviz(classifier, out_file=None,
                                feature_names=['Credit Score', 'Income', 'Loan Amount', 'Loan Term',
                                               'Employment Status: Employed', 'Employment Status: Self-Employed',
                                               'Employment Status: Unemployed', 'Previous Delinquencies: Yes'],
                                class_names=['Rejected', 'Approved'],
                                filled=True
)
"""
# Decision tree calculations
manufacturing_cost = 20
selling_price = 40
fixed_cost = 50000
estimated_demand = 10000

# Calculate the profit if the product is launched
launch_profit = (selling_price - manufacturing_cost) * min(estimated_demand, 10000)
launch_profit -= fixed_cost

# Calculate the profit if the product is not launched
no_launch_profit = 0

# Calculate the expected value
prob_launch = 0.5  # Assuming equal probabilities of launching and not launching
prob_no_launch = 0.5

expected_value = (prob_launch * launch_profit) + (prob_no_launch * no_launch_profit)

# Print the expected value
print("Expected Value of Launching the Product: $", expected_value)

# Recommendation to the boss
if expected_value > 0:
    recommendation = "Launch the product."
else:
    recommendation = "Do not launch the product."

print("Recommendation:", recommendation)



