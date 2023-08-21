import streamlit as st
import email
# from cloud import subscribe
from models import Podcast, SubscriptionModel
import modal

# Set page config for wider layout
st.set_page_config(
    layout="wide",
    page_title="Podcast Newsletter",
    page_icon="🎧",
    initial_sidebar_state="collapsed",
)

# Streamlit UI
st.title("Personalized Podcast Newsletter")
st.markdown("---")


# Allow user to input a list of RSS feeds
st.subheader("Enter Podcast RSS Feeds (One per line)")
rss_feeds = st.text_area("Paste RSS feeds here:", height=150)

subscribe_newsletter = st.checkbox("Subscribe to Newsletter")
if subscribe_newsletter:
    email = st.text_input("Enter your email:")
    receive_suggestions = st.checkbox(
        "Receive Podcast Suggestions",
        help="By selecting this option, you'll receive personalized podcast suggestions.",
    )
    
    if st.button("Subscribe"):
        if email:
            # Send subscription request to backend
            podcasts = [Podcast(rss=x) for x in rss_feeds]
            model = SubscriptionModel(
                user_email=email, podcasts=podcasts, receive_suggestions=receive_suggestions
            )
            f = modal.Function.lookup("podcast-app", "subscribe")
            subscription_response = f.remote(model)
            if subscription_response is not None:
                # st.success("Subscription successful!")
                st.text(subscription_response)
            else:
                st.error("Subscription failed. Please try again.")
        else:
            st.warning("Please enter your email.")


# Add a footer with additional information
st.markdown("---")
st.info(
    "Powered by Streamlit | Learn more at [Streamlit Docs](https://docs.streamlit.io)"
)
