from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import streamlit as st

# Custom CSS
# Set page config first
st.set_page_config(page_title="My Webpage", page_icon=":gem:", layout="wide")


def methodology_tab():
    st.header("Our Methodology")
    st.subheader("OracleOfTheCourt uses multiple databases of Advanced Statistics used by NBA Front-Offices And Machine Learning Algorithms To Determine the best candidate for each accolade.")

    # Add the image below the subheader with a smaller size
    image_path = "C:/Users/Shant B/Desktop/NBA Advanced Stats and Data/StreamlitImages/NonAbsolute Data.png"
    image = Image.open(image_path)
    
    # Create a column to center the image and control its width
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(image, caption="Our Data Graph", use_column_width=True)

    # Rest of your methodology content
    col1, col2, col3 = st.columns(3)

    with col1:
        st.title("Our Benchmarks For Our Algorithm are as follows:")
        st.subheader("""
        Accuracy of predicting the actual MVP: 1.0000
        Model Performance Metrics:
        Accuracy: 1.0000
        Precision: 1.0000
        Recall: 1.0000
        F1-Score: 1.0000
        R-squared: 0.8347
        Mean Absolute Error: 0.0757
        Spearman's Rank Correlation: 0.9091
        ROC AUC Score: 0.9960
        """)

    with col2:
        st.title("Our Past Predictions (Last 3 Years):")
        st.subheader("""
        Top 5 MVP candidates for 2024 season:
        Nikola Jokic - Predicted MVP Score: 0.9746, Actual MVP Rank: 1
        Shai Gilgeous Alexander - Predicted MVP Score: 0.6128, Actual MVP Rank: 3
        Joel Embiid - Predicted MVP Score: 0.4957, Actual MVP Rank: 2
        Luka Doncic - Predicted MVP Score: 0.3415, Actual MVP Rank: 4
        Giannis Antetokounmpo - Predicted MVP Score: 0.2693, Actual MVP Rank: 5

        Top 5 MVP candidates for 2023 season:
        Joel Embiid - Predicted MVP Score: 0.8477, Actual MVP Rank: 1
        Nikola Jokic - Predicted MVP Score: 0.5563, Actual MVP Rank: 2
        Giannis Antetokounmpo - Predicted MVP Score: 0.3359, Actual MVP Rank: 3
        Jayson Tatum - Predicted MVP Score: 0.2402, Actual MVP Rank: 4
        Shai Gilgeous Alexander - Predicted MVP Score: 0.2216, Actual MVP Rank: 5

        Top 5 MVP candidates for 2022 season:
        Nikola Jokic - Predicted MVP Score: 0.9428, Actual MVP Rank: 1
        Giannis Antetokounmpo - Predicted MVP Score: 0.7942, Actual MVP Rank: 3
        Joel Embiid - Predicted MVP Score: 0.5043, Actual MVP Rank: 2
        Luka Doncic - Predicted MVP Score: 0.2437, Actual MVP Rank: 5
        Devin Booker - Predicted MVP Score: 0.2242, Actual MVP Rank: 4
        """)

    with col3:
        st.title("DISCLAIMER")
        st.subheader("""
        This website is not affiliated, associated, authorized, endorsed by, sponsored, authored, contributed to, or in any way officially or unofficially connected with the NBA or any national or local basketball teams, any of their direct and indirect subsidiaries, affiliates, controlled companies, distributors, licensees, representatives, successors, assigns, and agents.
        """)

# Custom CSS
st.markdown("""
<style>
    body {
        background-color: ##262730;  /* Dark Blue */
    }
    .stApp {
        background-color: ##262730;  /* Dark Blue */
    }
    h1, h2, h3 {
        color: #ffffff !important;  /* Hot Pink */
        font-weight: bold !important;
    }
    p, .stMarkdown, .stText {
        color: #ff524d !important;  /* Bright Red */
    }
</style>
""", unsafe_allow_html=True)

# Rest of your code...

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Tracker", "Methodology"])

    if page == "Tracker":
        show_home_page()
    elif page == "Methodology":
        methodology_tab()

def show_home_page():
    # Move all your existing content (everything after the CSS) into this function
    # Start from the line: def load_lottieurl(url):
    # and include everything up to the end of your current script

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    #LOAD IMAGES / ASSETS
    #LOTTIE FILE:
    lottie_coding = load_lottieurl("https://lottie.host/75afdd30-1b92-41de-a2c0-918b7bd40321/pKw1dYCNai.json")
    img_contact_form = Image.open("C:/Users/Shant B/Desktop/NBA Advanced Stats and Data/StreamlitImages/NBAGannChart.png")
    img_lottie_animation = Image.open("C:/Users/Shant B/Desktop/NBA Advanced Stats and Data/StreamlitImages/RenTech Resized.webp")

    #HEADER
    st.subheader("Hi, Im Shawn :wave:")
    st.title("A passionate College Student For NBA")
    st.write("I love researching about NBA Advanced Statistics")
    st.markdown("<a href='https://youtube.com' style='color: #00fffb;'>Learn More ></a>", unsafe_allow_html=True)


    # What I do
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
                """
    I am an aspiring Data Science and Quant. I have insane
    Share Ratios and performance, real shit. My sportsbetting
    MVP predictor is the best in the market.

    If this sounds interesting to you, dm me.
    """
            )
            st.markdown("<a href='https://linkedin.com' style='color: #00fffb;'>My LinkedIn ></a>", unsafe_allow_html=True)
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

    ## Projects
    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_lottie_animation)
        with text_column:
            st.subheader("INtegrate Lottie Animations Inside Your Streamlit App")
            st.write(
                """
                Learn How To Do Data Science
                With NBA Advanced Stats.
                This is the most accurate model in the world btw"""
            )
            st.markdown("[Watch Video...](https://radixtrading.co/)")
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_form)
    ## Contact:
    with st.container():
        st.write("---")
        st.header("Get my contact info")
        st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/your@email.com" method="POST" style="color: #00fffb;">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required style="color: #FF0000;">
    <input type="email" name="email" placeholder="Your email" required style="color: #FF0000;">
    <textarea name="message" placeholder="Your message here" required style="color: #FF0000;"></textarea>
    <button type="submit" style="color: #FF0000;">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

if __name__ == "__main__":
    main()