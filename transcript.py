from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_video_id(url: str) -> str:
    match = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url)
    if not match:
        raise ValueError("Couldn't extract video ID from URL")
    return match.group(1)

def get_transcript(url: str) -> str:
    video_id = get_video_id(url)
    ytt_api = YouTubeTranscriptApi()
    fetched = ytt_api.fetch(video_id)
    return " ".join(snippet.text for snippet in fetched)