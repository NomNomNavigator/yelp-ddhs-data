"""
For a "cold-start" recommender, we could use a content based approach.
- Medium/Toward DS/Googling -> Not sure if a content based approach but regressors, nearest neighbors or k-means algos might fit.
Once we start collecting data, then some sort of collaborative filtering or hybrid could work
- Many sources seem to recommend an "alternating least squares" algorithm/training
"""

# Thinking we might want to use one or more of these packages/modules for model training
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

# I think we want to create a DF from cleaned data to use data for model training.
# One file with all restaurants from both cities with IDs, city and common attributes as columns.
# Note:  City will need to be set as "Philadelphia" or "Wilmington" regardless of actual city in yelp results.
df = pd.read_json('/wrangled_data/<some file>.json')

# It seems we might = need to extract features for Philadelphia and Wilmington restaurants to train the model
# Perhaps something like the below...
philly_restaurants = df[df['city'] == 'Philadelphia'].set_index('business_ID').drop('Philadelphia', axis=1)
wilmington_restaurants = df[df['city'] == 'Wilmington'].set_index('Product ID').drop('Wilmington', axis=1)

# Figure out the type of model to train, some sort of comparison or collaborative filtering (K-means, cosine sim, etc)
# How do we get a trained model to act as an API we can hit?  Better to have it in the project?
# Encode the 'City' column?? using Label Encoding
label_encoder = LabelEncoder()
df['city'] = label_encoder.fit_transform(df['city'])

# Split the data into training and testing sets
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Separate features and target variable
X_train = train_df.drop(['business_id', 'city'], axis=1)
y_train = train_df['city']

X_test = test_df.drop(['business_id', 'city'], axis=1)
y_test = test_df['city']

# Train a model: Can use different types, this example is RandomForestRegressor model
# Figure out random_state settings, why is it 42.
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Predict the similarity scores on the test set
y_pred = model.predict(X_test)

# Evaluate the model (optional)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')



# Create a function to get restaurant recommendations from the model
# Should this actually be in a different file?  Going to want to use this often?
# What data gets passed to the model?  What is used for rules?
def get_recommendations(liked_restaurants, city, cuisine, rating, price, ambiance):
    pass
