import requests
import json
from config import bearer_token

# Yelp API endpoint for searching businesses
url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "authorization": bearer_token,
    "accept": "application/json"
}


def fetch_and_save_data(location):
    # Lists to store restaurant details and categories
    restaurants = []
    restaurant_categories = []

    # Initial values for offset and limit
    offset = 0
    limit = 50  # Yelp API limit per request

    # Loop to fetch data until no more businesses are returned
    while True:
        # Parameters for the API request
        params = {
            "location": location,
            "limit": str(limit),
            "offset": str(offset)
        }

        # Make API request to Yelp
        response = requests.get(url, headers=headers, params=params)
        r_list = response.json()

        # Check if no more businesses are returned
        if not r_list['businesses']:
            break

        # Process each restaurant in the response
        for r in r_list['businesses']:
            # Extract the image URL from the response
            image_url = r.get("image_url", "")

            # Details of the restaurant
            r_details = {
                "id": r["id"],
                "name": r["name"],
                "review_count": r["review_count"],
                "rating": r["rating"],
                "price_range": r.get("price"),
                "location": {
                    "city": r.get("location", {}).get("city"),
                    "state": r.get("location", {}).get("state"),
                },
                "image_url": image_url,
                "alias": r["categories"][0]["alias"],
                "title": r["categories"][0]["title"]
            }

            # Append restaurant details to the list
            restaurants.append(r_details)

            # Process restaurant categories
            c_id = r["id"]
            for cat in r['categories']:
                r_cat = {
                    "id": c_id,
                    "alias": cat["alias"],
                    "title": cat["title"]
                }
                restaurant_categories.append(r_cat)

        # Increment offset for the next page of results
        offset += limit

    # Print the total number of restaurants fetched
    tot_r = len(restaurants)
    print(tot_r)

    # Save restaurant details and categories to JSON files
    with open(f'fetched_data/{location}_restaurants.json', 'w') as f:
        json.dump(restaurants, f, indent=2)

    with open(f'fetched_data/{location}_restaurant_categories.json', 'w') as f:
        json.dump(restaurant_categories, f, indent=2)


# Call the function for Wilmington Delaware
fetch_and_save_data("Wilmington, Delaware")

# Call the function for Philadelphia
fetch_and_save_data("Philadelphia")
