import streamlit as st
from pytube import YouTube
import random

emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼"]
def random_emoji():
    st.session_state.emoji = random.choice(emojis)
    return st.session_state.emoji


"""
# Youtube Video Downloader
"""
url = st.text_input('Please enter Video URL')
st.write('Your entered URL', url)

path = st.text_input('Give path to store')
st.write('Your entered Path', path)

if st.button('Download Video'):
    video=YouTube(url)
    stream=video.streams.get_highest_resolution()
    st.write('downloading..please wait!',random_emoji())
    stream.download(path)
    st.write('Hurrah!! Video downloaded!',random_emoji())