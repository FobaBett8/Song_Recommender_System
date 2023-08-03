import streamlit as st
import requests
import ast
import pickle

def main():
    st.title("Song Recommender")
    input = st.text_input(label="Enter a song: ")
    if st.button("Recommend"):
        response = requests.get('http://127.0.0.1:8000/item_based?input={}'.format(input))
        data_temp = response.content.decode('UTF-8')
        data = ast.literal_eval(data_temp)

        for i in data['song']:
            st.write(data['song'][i])
    

if __name__ == "__main__":
    main()