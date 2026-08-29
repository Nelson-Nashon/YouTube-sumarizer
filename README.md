# 🎬 YouTube Video Summarizer

A mini LLM-powered app that fetches a YouTube video's transcript and generates a summary using Google's Gemini API. Built with Python and Streamlit.

## Features

- Paste any YouTube video URL (with captions/subtitles available)
- Automatically fetches the video's transcript
- Generates a summary using Gemini (`gemini-3.6-flash`)
- Choose summary style: concise, detailed, or bullet points
- Simple, clean Streamlit web interface

## Tech Stack

- Python
- [Streamlit](https://streamlit.io/) — web UI
- [Google Gemini API](https://ai.google.dev/) — summarization
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) — transcript fetching

## Setup

1. Clone the repo:
git clone https://github.com/Nelson-Nashon/YouTube-sumarizer.git
cd youtube-sumarizer

2. Create a virtual environment and install dependencies:
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

3. Create a `.env` file in the project root with your Gemini API key:
GEMINI_API_KEY=your_key_here

4. Run the app:
python -m streamlit run main.py

## How It Works

1. User pastes a YouTube URL.
2. `transcript.py` extracts the video ID and fetches the transcript via `youtube-transcript-api`.
3. `summarizer.py` sends the transcript to Gemini with a prompt asking for the main topic, key points, and a takeaway.
4. The summary is displayed in the Streamlit UI.

## Future Improvements

- Chunk very long transcripts instead of truncating them
- Deploy live on Streamlit Community Cloud
- Support multiple languages
