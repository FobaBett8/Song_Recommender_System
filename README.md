# Song_Recommender_System

## Scenario:

You have been hired by a music streaming company. Your task is to read the dataset and create a recommender system which recommends users on what to listen to next based on their history. You must also use an API to then display this system with required UI to display it on a webpage.

## Project Objective:

To build a recommendation system based on user history and developing API and UI to display and give an interactive platform for the user to select songs and obtain recommendations.

- Recommenders.py: 
1. `popularity_recommender_py`:
   - This class implements a popularity-based recommender system. It does not personalize recommendations based on user preferences but instead recommends popular items based on their overall popularity in the training data.
   - The `create` method takes the training data, user ID, and item ID as inputs. It calculates the popularity score for each unique item (song) in the training data based on the number of times it appears in the data.
   - The top 10 popular items are stored in the `popularity_recommendations` attribute.
   - The `recommend` method takes a user ID as input and returns the top 10 popular recommendations for that user.

2. `item_similarity_recommender_py`:
   - This class implements an item similarity-based recommender system. It uses the co-occurrence matrix to find similar items based on the users who have interacted with them.
   - The `create` method takes the training data, user ID, and item ID as inputs.
   - The `get_user_items` method returns a list of unique items (songs) corresponding to a given user.
   - The `get_item_users` method returns a set of unique users for a given item (song).
   - The `get_all_items_train_data` method returns a list of all unique items (songs) in the training data.
   - The `construct_cooccurence_matrix` method calculates the co-occurrence matrix based on the interaction between items and users in the training data.
   - The `generate_top_recommendations` method generates top recommendations for a given user using the co-occurrence matrix.
   - The `recommend` method takes a user ID as input and returns the top 10 item similarity-based recommendations for that user.
   - The `get_similar_items` method takes a list of items as input and returns the top 10 item similarity-based recommendations for those items.

It's important to note that these recommenders have different approaches:
   - The Popularity-based recommender recommends popular items for all users, regardless of their preferences.
   - The Item Similarity-based recommender finds items that are similar to the ones a user has interacted with, personalized to that user's behavior.

- api.py: 

