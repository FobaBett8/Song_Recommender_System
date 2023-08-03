from fastapi import FastAPI
import Recommenders
import pandas as pandas
app = FastAPI()

@app.get('/item_based')
def recommender(input):
    song_df_1 = pandas.read_csv('triplets_file.csv')
    song_df_2 = pandas.read_csv('song_data.csv')
    song_df = pandas.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on ='song_id', how = 'left')
    song_df['song'] = song_df['title'] + ' - ' + song_df['artist_name']
    song_df = song_df.head(10000)
    ir = Recommenders.item_similarity_recommender_py()
    ir.create(song_df, 'user_id', 'song')
    user_items = ir.get_user_items(song_df['user_id'][100])
    ir.recommend(song_df['user_id'][100])
    input = [input]
    return ir.get_similar_items(input)

