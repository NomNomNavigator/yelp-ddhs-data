import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Will need to create a DF from cleaned data.
# One file with all restaurants from both cities with IDs, city and common attributes as columns
# Note:  City will need to be set as "Philadelphia" or "Wilmington" regardless of actual city in yelp results.

# Need to extract features for Philadelphia and Wilmingotn restaurants to train the model on
philly_restaurants = df[df['city'] == 'Philadelphia'].set_index('business_ID').drop('Philadelphia', axis=1)
wilmington_restaurants = df[df['city'] == 'Wilmington'].set_index('Product ID').drop('Wilmington', axis=1)

# Figure out the type of model to train, some sort of comparison or collaborative filtering (K-means, cosine sim, etc)
# How do we get a trained model to act as an API we can hit?  Better to have it in the project?
reco_model = cosine_similarity(philly_restaurants, wilmington_restaurants)


# Create a function to get restaurant recommendations from the model
# Should this actually be in a different file?  Going to want to use this often?
# What data gets passed to the model?  What is used for rules?
def get_recommendations(liked_restaurants, city, cuisine, rating, price, ambiance):

    # Get the uses's liked restaurants, and disliked restaurants
    # Send them to the model, along with city and their values for the common attributes
    


    # Calculate similarity between users liked restaurants in one city and those of another city
    similarity_scores = cosine_similarity([user_profile], company_features)

    # Create a DataFrame with Product IDs and their similarity scores
    recommendations = pd.DataFrame({'business_ID': restaurants.index, 'Similarity Score': similarity_scores[0]})

    # Sort products by similarity score in descending order
    recommendations = recommendations.sort_values(by='Similarity Score', ascending=False)

    # Display top recommended products
    top_recommendations = recommendations.head(5)
    return top_recommendations

# Example usage:
user_liked_restaurants = ['3489u34r8y3983ur', '34ru3894ru398y2r', '389ry29j9u498y2489r']  # Replace with actual Product IDs
restaurant_recos = get_recommendations(user_likes_company1, model, company2_features)
print(recommendations_company2)
