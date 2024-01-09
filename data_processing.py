import pandas as pd


def process_data(location):
    # Load the data into a DataFrame
    df_restaurants = pd.read_json(f'fetched_data/{location}_restaurants.json')

    # Inspect the DataFrame
    print(df_restaurants.head())

    # Extract relevant information
    restaurant_names = df_restaurants["name"].tolist()
    cuisines = df_restaurants["alias"].tolist()
    review_counts = df_restaurants["review_count"].tolist()
    ratings = df_restaurants["rating"].tolist()
    price_ranges = df_restaurants["price_range"].tolist()
    image_urls = df_restaurants["image_url"].tolist()
    categories_aliases = df_restaurants["alias"].tolist()
    categories_titles = df_restaurants["title"].tolist()
    # Split the location dictionary into separate columns
    # pd.Series gets applied to each element expanding in the location column while expanding them into separate columns
    locations = df_restaurants["location"].apply(pd.Series)
    cities = locations["city"].tolist()
    states = locations["state"].tolist()

    # Data cleaning and structuring
    # Example: Convert price range to numerical representation
    df_restaurants["price_numerical"] = df_restaurants["price_range"].map({"$": 1, "$$": 2, "$$$": 3, "$$$$": 4})

    # Save processed data to CSV
    df_restaurants.to_csv(f'processed_data/{location}_processed_data.csv', index=False)


# The script is designed to process data fetched from Yelp API and transform it into a structured format.
# The DataFrame 'df_restaurants' is used to store the fetched data for further processing.

# Extracted information such as restaurant names, cuisines, review counts, ratings, price ranges, image URLs,
# and categories is stored in separate lists for analysis.

# The 'location' dictionary is split into separate columns 'cities' and 'states' for more detailed location information.

# Data cleaning and structuring steps are performed, for example, converting the price range to numerical
# representation.

# The processed data is saved to a CSV file for further analysis and visualization.

