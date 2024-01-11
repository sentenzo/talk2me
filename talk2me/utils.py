import time
from queue import Queue

import speech_recognition as sr
from speech_recognition.audio import AudioData

# https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py


SR_RECOGNIZER = sr.Recognizer()
DEFAULT_MODEL = "tiny.en"  # tiny, base, small, medium, large


def audio_to_text(path_to_audio, cached_recognizer=SR_RECOGNIZER) -> str:
    audio = None
    r = cached_recognizer
    with sr.AudioFile(path_to_audio) as source:
        audio = r.record(source)  # read the entire audio file
    text = r.recognize_whisper(audio, model=DEFAULT_MODEL)
    return text


def mic_to_text_streem(mic_index=None, cached_recognizer=SR_RECOGNIZER):
    print("Say something!")
    r = cached_recognizer
    que_audio = Queue()
    acc_audio = None

    def record_callback(_, audio: AudioData) -> None:
        # data = audio.get_raw_data()
        que_audio.put(audio)

    source = sr.Microphone(mic_index)

    stop_listening = r.listen_in_background(source, record_callback, 1)
    try:
        while True:
            time.sleep(0.5)
            if que_audio.empty():
                continue

            audio = que_audio.get()

            if acc_audio:
                acc_audio.frame_data += audio.frame_data
            else:
                acc_audio = audio
            yield r.recognize_whisper(acc_audio, model=DEFAULT_MODEL)
    except KeyboardInterrupt:
        stop_listening(False)


def print_mic_list():
    print(*sr.Microphone.list_microphone_names(), sep="\n")
    print()
    print(*sr.Microphone.list_working_microphones().items(), sep="\n")
    print()


def mic_to_text(
    time_limit, mic_index=None, cached_recognizer=SR_RECOGNIZER
) -> str:
    r = cached_recognizer
    with sr.Microphone(mic_index) as source:
        print("Say something!")
        audio = r.listen(source, 5, time_limit)
    return r.recognize_whisper(audio, model=DEFAULT_MODEL)


def mic_to_text_background(
    time_limit, mic_index=None, cached_recognizer=SR_RECOGNIZER
) -> str:
    r = cached_recognizer
    m = sr.Microphone(device_index=mic_index)
    with m as source:
        r.adjust_for_ambient_noise(source, duration=3)

    def callback(recognizer, audio):
        print("###")
        print(recognizer.recognize_whisper(audio, model=DEFAULT_MODEL))

    stop_listening = r.listen_in_background(
        m, callback, phrase_time_limit=time_limit
    )

    return stop_listening
