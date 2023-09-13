import streamlit as st
import openai
from PIL import Image

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Create a function to generate AI-generated photos
def generate_photos():
    photos = []
    for _ in range(3):
        # Generate an image using OpenAI API
        response = openai.Completion.create(
            engine="davinci",
            prompt="Generate an image of a random object.",
            max_tokens=50,
            temperature=0.7
        )
        image_url = response.choices[0].text.strip()

        # Load and display the generated image
        image = Image.open(requests.get(image_url, stream=True).raw)
        photos.append(image)
    return photos

# Create the Streamlit app
def main():
    st.title("OpenAI Picture Generator")
    st.write("Welcome to the OpenAI Picture Generator app!")
    st.write("Click the button below to generate three AI-generated photos.")

    if st.button("Generate"):
        # Generate three AI-generated photos
        generated_photos = generate_photos()

        # Display the generated photos
        for photo in generated_photos:
            st.image(photo, use_column_width=True)

# Run the app
if __name__ == "__main__":
    main()
