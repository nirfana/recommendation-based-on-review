# Contents of `app2.py`
import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model

# Function to load the model
@st.cache_data
def load_sentiment_model():
    model = load_model('../model.keras')
    return model

# Function to make predictions
def predict_sentiment(review_text, model):
    # Perform prediction
    pred = model.predict([review_text])
    prediction = tf.where(pred >= 0.5, 1, 0)
    
    # Convert tensor to a list of 1s and 0s
    predictions_list = prediction.numpy().flatten().tolist()
    
    # Replace 1 with 'Recommending' and 0 with 'Not Recommending'
    predictions_recommended = ['The author recommending this product' if x == 1 else 'The author not recommending this product' for x in predictions_list]
    
    return predictions_recommended

# Streamlit app function
def app():
    st.title('Make Predictions')
    
    # Load the model
    model = load_sentiment_model()
    
    # Text input for user
    user_input = st.text_area("Enter your review:", "")
    
    if st.button("Predict"):
        if user_input:
            # Display a loading message while predicting
            with st.spinner('Predicting...'):
                # Perform prediction
                predictions = predict_sentiment(user_input, model)
                
                # Display the prediction result
                st.success(f'Prediction: {predictions[0]}')
        else:
            st.warning("Please enter a review.")

if __name__ == '__main__':
    app()
