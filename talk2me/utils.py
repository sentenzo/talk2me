import speech_recognition as sr

# https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py


def audio_to_text(path_to_audio, cached_recognizer=sr.Recognizer()):
    audio = None
    r = cached_recognizer
    with sr.AudioFile(path_to_audio) as source:
        audio = r.record(source)  # read the entire audio file
    text = r.recognize_whisper(audio, model="base")
    return text
