"""
Response is JSON, top level is list of businesses, each business is a dictionary
Price: on scale of 1 to 4 $, with 4 being the most expensive
Attributes cost money, not in free tier but would be cool.
Basic Data:  id, name, price, rating, review_count
Category Data:  1 to Many, alias and title

Note:  This search only returns 87 total restaurants, but there is ~3000 in Delaware
Not2:  Changing search to "wilmington, de" returns 2100 restaurants, "dover, de" returns 337
Note3: If we can get long, lat and radius to cover all DE, then filter results for only restaurants with state = DE it might work.
Note4: Note3 seems overcomplicated, maybe we just do Wilmington, DE and advert is a "NomNomNavigator for Wilmington"
"""
import requests
import json
from config import bearer_token

# Max limit is 50 per Yelp API Docs, but maybe I can get more, nope its 50
url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "authorization": bearer_token,
    "accept": "application/json"
}

# Going to build two json files - one for basic details, one that is a list of 1 to many categories for each.
# Initializes the lists to store restaurant categories and details
restaurants = []
restaurant_categories = []

# Try to call the API 2x, get all the restaurants from each call
# Loop to make API requests; with range being the number of API requests to make
for i in range(0, 2):
    if i == 0:
        new_offset = "0"
    else:
        new_offset = str((50 * i) + 1)
    # Parameters for the API
    params = {
        "location": "Delaware",
        "limit": "50",
        "offset": new_offset
    }
    # This code makes the API request
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
            "image_url": image_url
        }
        # Append the details of restaurant to the list named restaurant
        restaurants.append(r_details)
        # Process restaurant categories
        c_id = r["id"]
        restaurants.append(r_details)
        for cat in r['categories']:
            r_cat = {
                "id": c_id,
                "alias": cat["alias"],
                "title": cat["title"]
            }
            restaurant_categories.append(r_cat)

tot_r = len(restaurants)
print(tot_r)

with open('fetched_data/restaurants.json', 'w') as f:
    json.dump(restaurants, f, indent=2)

with open('fetched_data/restaurant_categories.json', 'w') as f:
    json.dump(restaurant_categories, f, indent=2)
