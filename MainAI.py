import streamlit as st
import tensorflow as tf
from PIL import Image

# Load the pre-trained model
model = tf.keras.applications.ResNet50(weights='imagenet')

# Create a function to generate AI-generated photos
def generate_photos():
    photos = []
    for _ in range(3):
        # Generate a random image
        random_image = tf.random.uniform((224, 224, 3), minval=0, maxval=255, dtype=tf.uint8)
        # Preprocess the image
        preprocessed_image = tf.keras.applications.resnet50.preprocess_input(random_image)
        # Make predictions using the pre-trained model
        predictions = model.predict(tf.expand_dims(preprocessed_image, axis=0))
        # Get the predicted label
        predicted_label = tf.keras.applications.resnet50.decode_predictions(predictions, top=1)[0][0][1]
        # Create an image with the predicted label as text
        image = Image.fromarray(random_image.numpy())
        image = image.convert("RGB")
        image = image.resize((300, 300))
        image = image.filter(ImageFilter.GaussianBlur(radius=2))
        draw = ImageDraw.Draw(image)
        draw.text((10, 10), predicted_label, fill=(255, 255, 255))
        photos.append(image)
    return photos

# Create the Streamlit app
def main():
    st.title("AI Picture Generator")
    st.write("Welcome to the AI Picture Generator app!")
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