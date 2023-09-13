import streamlit as st
import random

# Define the Tarot card deck
tarot_deck = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
    "Judgment", "The World"
]

# Create a function to predict a random Tarot card
def predict_tarot_card():
    return random.choice(tarot_deck)

# Create the Streamlit app
def main():
    st.title("Tarot Card AI Prediction")
    st.write("Welcome to the Tarot Card AI Prediction app!")
    st.write("Click the button below to get a random Tarot card prediction.")

    if st.button("Predict"):
        prediction = predict_tarot_card()
        st.write("Your Tarot card prediction is:", prediction)


# Run the app
if __name__ == "__main__":
    main()
