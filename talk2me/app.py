from pathlib import Path


from utils.sphinx.audio_transcribe import a2t as sphinx_a2t
from utils.whisper.audio_transcribe import a2t as whisper_a2t


AUDIO_FILE = (Path(__file__).parent / "audio" / "en_news.wav").as_posix()

if __name__ == "__main__":
    print("Sphinx:\n", sphinx_a2t(AUDIO_FILE))
    print()
    print("Whisper:\n", whisper_a2t(AUDIO_FILE))
    print()
