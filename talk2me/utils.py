import speech_recognition as sr

# https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py


SR_RECOGNIZER = sr.Recognizer()


def audio_to_text(path_to_audio, cached_recognizer=SR_RECOGNIZER) -> str:
    audio = None
    r = cached_recognizer
    with sr.AudioFile(path_to_audio) as source:
        audio = r.record(source)  # read the entire audio file
    text = r.recognize_whisper(audio, model="base")
    return text


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
    return r.recognize_whisper(audio, model="base")


def mic_to_text_background(
    time_limit, mic_index=None, cached_recognizer=SR_RECOGNIZER
) -> str:
    r = cached_recognizer
    m = sr.Microphone(device_index=mic_index)
    with m as source:
        r.adjust_for_ambient_noise(source, duration=3)

    def callback(recognizer, audio):
        print("###")
        print(recognizer.recognize_whisper(audio, model="base"))

    stop_listening = r.listen_in_background(
        m, callback, phrase_time_limit=time_limit
    )

    return stop_listening
