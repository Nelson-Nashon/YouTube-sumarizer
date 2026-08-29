import streamlit as st
from transcript import get_transcript
from summarizer import summarize

st.set_page_config(page_title="YouTube Video Summarizer", page_icon="🎬")
st.title("🎬 YouTube Video Summarizer")

url = st.text_input("Paste a YouTube URL:")
style = st.selectbox("Summary style", ["concise", "detailed", "bullet points"])

if st.button("Summarize"):
    if not url:
        st.warning("Please paste a URL first.")
    else:
        with st.spinner("Fetching transcript..."):
            try:
                transcript = get_transcript(url)
            except Exception as e:
                st.error(f"Couldn't fetch transcript: {e}")
                st.stop()

        with st.spinner("Summarizing..."):
            try:
                summary = summarize(transcript, style)
            except Exception as e:
                st.error(f"Summarization failed: {e}")
                st.stop()

        st.subheader("Summary")
        st.write(summary)