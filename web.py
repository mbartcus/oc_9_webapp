import streamlit as st
import requests
#import pandas as pd




st.title('Books recommandation')
st.subheader('Filtering Recommandation System')

#all_clicks_df = pd.read_parquet('results/usr_clicks.gzip')
#users = all_clicks_df.user_id.unique()

with st.form(key='recommandation_form', clear_on_submit=True):
    user_id = st.text_input('Select user')

    #recommandation_type = st.selectbox(
    #'Select the recommandation type',
    #('collaborative-recommandation', 'filtering-recommandation'))

    #user_id = st.selectbox(
    #'Select the user',
    #users)

    submit_button = st.form_submit_button('Submit')

if submit_button:
    with st.spinner('Wait for it...'):
        st.info(f'Your user is :  {user_id}')
        st.info(f'Your recommandationtype is :  {recommandation_type}')

        #if recommandation_type == 'collaborative-recommandation':
        article_score = requests.get("https://oc9.azurewebsites.net/api/HttpTriggerRecommand", params={"clientId":"blobs_extension", "user_id": user_id}).json()
        #else:
        #article_score = requests.get("https://oc9.azurewebsites.net/api/HttpTriggerFillterRecom", params={"clientId":"blobs_extension", "user_id": user_id}).json()
        st.text(type(article_score))
        st.json(article_score)
        #for i, article in enumerate(article_score):
        #    st.text('{0}/{1}:{2}'.format(i+1, article, article_score[article]))
