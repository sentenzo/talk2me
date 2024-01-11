import time

from .utils import (
    audio_to_text,
    mic_to_text,
    mic_to_text_background,
    mic_to_text_streem,
    print_mic_list,
)

if __name__ == "__main__":
    # print_mic_list()

    # stop = mic_to_text_background(5)  # , mic_index=1)
    # time.sleep(10)
    # stop()

    # print(mic_to_text(5))

    for text in mic_to_text_streem():
        print(text, end="\r")
    print()
