import streamlit as st
from PIL import Image

# Basic page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# Header
st.title("👨‍💻 Welcome to My Portfolio!")
st.subheader("Hi, I'm [Your Name] 👋")
st.write("I'm a passionate developer who loves building cool stuff with Python!")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Projects", "Contact"])

# Home Page
if page == "Home":
    st.header("🏠 Home")
    st.write("Welcome to my personal website built with Streamlit!")

    # Profile Image
    img = Image.open("image/image.jpg")

    st.image(img, caption="That's me!", width=300)

# About Me Page
elif page == "About Me":
    st.header("📖 About Me")
    st.write("""
        - 💻 I'm a Python developer.
        - 📚 I love learning new technologies.
        - 🚀 Always ready for a new challenge!
    """)
    st.info("Fun fact: Streamlit makes web development easy!")

# Projects Page
elif page == "Projects":
    st.header("🛠 Projects")
    
    st.subheader("🔹 Project 1: Cool Web App")
    st.write("Description: A web application built with Streamlit and Python.")
    
    st.subheader("🔹 Project 2: Data Analysis")
    st.write("Description: A data analysis project using Pandas and Matplotlib.")

# Contact Page
elif page == "Contact":
    st.header("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submitted = st.form_submit_button("Send")

        if submitted:
            st.success(f"Thanks {name}! I'll get back to you at {email}.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
