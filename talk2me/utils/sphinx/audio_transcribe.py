import logging

import speech_recognition as sr


def a2t(path_to_audio):
    r = sr.Recognizer()
    with sr.AudioFile(path_to_audio) as source:
        audio = r.record(source)  # read the entire audio file
    return r.recognize_sphinx(audio)
