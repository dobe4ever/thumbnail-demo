import streamlit as st
from auto_thoombnail import upload_photo, auto_thumbnail


# Main app layout
st.image("templates\logo.png", width=300)
st.title("Auto Thumbnail")

# Form for user input
photo = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])
num = st.number_input("Episode number", min_value=0)
l1 = st.text_input("Title line 1")
l2 = st.text_input("Title line 2 (optional)")

if photo:
    uploaded_photo = upload_photo(photo)
    st.image(uploaded_photo)

# Submit button
if st.button("Submit"):
    if uploaded_photo is not None:
        auto_thumbnail(episode_num=num, line1=l1, line2=l2)

        # Display the processed image
        st.subheader("New thumbnail")
        st.image("uploads/new_thumbnail.png")
    else:
        st.error("Please upload an image.")

