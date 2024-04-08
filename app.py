import streamlit as st
import pandas as pd

def main():
    # Set page configuration
    st.set_page_config(page_title="My Professional Portfolio", page_icon="🚀", layout="wide")

    # Display title and introduction
    st.title("My Professional Portfolio")
    st.write("Welcome to my portfolio! Explore below to learn more about me.")

    # Display photo
    st.image("./photo.jpeg",width=100)

    # My Info section
    st.markdown("---")
    st.header("My Info")
    st.write("Name:  Aditya Gupta")
    st.write("Location:  Uttar Pradesh, India")
    st.write("Occupation:  Data Scientist")

    st.write("Connect with me:")
    st.write("[Instagram](https://www.instagram.com/aditya_gupta06/)")
    st.write("[GitHub](https://github.com/AdityaGupta63)")

    # My Skills section
    st.markdown("---")
    st.header("My Skills")
    st.subheader("Technical Skills:")
    st.write("- Python [Advane level]")
    st.write("- UI Designer")
    st.write("- HTML/CSS")
    st.subheader("Soft Skills:")
    st.write("- Communication")
    st.write("- Teamwork")
    st.write("- Problem-solving")

    # About Me section
    st.markdown("---")
    st.header("About Me")
    st.write("""
    I am a passionate and enthusiastic individual with a strong background in software development and a keen interest in emerging technologies. 
    I enjoy working on challenging projects and collaborating with teams to create innovative solutions.
    """)

    # Contact Me section
    st.markdown("---")
    st.header("Contact Me")
    st.write("Feel free to reach out to me at modanwaladicode@gmail.com")

    data = pd.DataFrame({
    'latitude': [26.84670880],
    'longitude': [80.94615920]
})
    
    st.map(data)

if __name__ == "__main__":
    main()
