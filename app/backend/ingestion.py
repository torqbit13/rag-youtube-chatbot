from youtube_transcript_api import TranscriptsDisabled, YouTubeTranscriptApi


def fetch_transcript(video_id: str) -> str:
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
        return " ".join(chunk["text"] for chunk in transcript_list)
    except TranscriptsDisabled:
        raise ValueError("No captions available for this video.")
    except Exception as e:
        raise ValueError(f"An error occured during transcript fetching: {e}")