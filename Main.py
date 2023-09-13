import streamlit as st
import random
from PIL import Image

# Define the Tarot card deck
tarot_deck = [
    {"name": "The Fool", "image": "fool.jpg"},
    {"name": "The Magician", "image": "magician.jpg"},
    {"name": "The High Priestess", "image": "high_priestess.jpg"},
    # Add more Tarot cards with their respective images
]

# Create a function to predict a random Tarot card
def predict_tarot_card():
    return random.choice(tarot_deck)

# Create the Streamlit app
def main():
    st.title("AI Predict Future with Tarot Cards")
    st.write("Welcome to the AI Predict Future with Tarot Cards app!")
    st.write("Click the button below to get a prediction for your future.")

    if st.button("Predict"):
        # Generate three random Tarot cards
        predictions = [predict_tarot_card() for _ in range(3)]

        # Display the Tarot card photos
        for prediction in predictions:
            image = Image.open(prediction["image"])
            st.image(image, caption=prediction["name"], use_column_width=True)

        # Display the prediction statement
        st.write("Your future prediction is:", ", ".join([prediction["name"] for prediction in predictions]))

# Run the app
if __name__ == "__main__":
    main()
