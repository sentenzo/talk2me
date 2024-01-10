from pathlib import Path

from .utils.whisper.audio_transcribe import a2t as whisper_a2t

AUDIO_FILE = (
    Path(__file__).parent.parent / "tests" / "audio_samples" / "en_news.wav"
).as_posix()

if __name__ == "__main__":
    print("Whisper:\n", whisper_a2t(AUDIO_FILE))
    print()
