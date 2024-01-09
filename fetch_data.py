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
    # Going to build two json files - one for basic details, one that is a list of 1 to many categories for each.
    # Initializes the lists to store restaurant categories and details
    restaurants = []
    restaurant_categories = []

    # Calculate the total number of API requests needed
    total_requests = 376
    requests_per_batch = 50

    # Loop to make API requests
    for i in range(total_requests // requests_per_batch + 1):
        if i == 0:
            new_offset = "0"
        else:
            new_offset = str((50 * i) + 1)
        # Parameters for the API
        params = {
            "location": location,
            "limit": "50",
            "offset": new_offset
        }

        # Make API request to Yelp using requests
        response = requests.get(url, headers=headers, params=params)
        r_list = response.json()
        print(r_list)

        # Process each restaurant in response
        for r in r_list['businesses']:
            # Extract the image URL directly from each response
            image_url = r.get("image_url", "")
            # This is the restaurant details
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
            # Append the details of the restaurant to the list named restaurants
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

    tot_r = len(restaurants)
    print(tot_r)

    with open(f'fetched_data/{location}_restaurants.json', 'w') as f:
        json.dump(restaurants, f, indent=2)

    with open(f'fetched_data/{location}_restaurant_categories.json', 'w') as f:
        json.dump(restaurant_categories, f, indent=2)


# Call the function for Wilmington Delaware
fetch_and_save_data("Wilmington, Delaware")

# Call the function for Philadelphia
fetch_and_save_data("Philadelphia")

