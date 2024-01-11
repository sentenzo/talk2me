from pathlib import Path

from .utils import audio_to_text

AUDIO_FILES = ["en_123.wav", "en_chunk.wav", "en_news.wav"]
AUDIO_FILE_PATHS = {
    file_name: (
        Path(__file__).parent.parent / "tests" / "audio_samples" / file_name
    ).as_posix()
    for file_name in AUDIO_FILES
}

if __name__ == "__main__":
    for file_name in AUDIO_FILE_PATHS:
        print("###", file_name)
        print(audio_to_text(AUDIO_FILE_PATHS[file_name]))
        print()
