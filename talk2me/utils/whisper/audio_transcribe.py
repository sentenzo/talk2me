import whisper


def a2t(path_to_audio):
    model = whisper.load_model("base")
    return model.transcribe(path_to_audio, fp16=False)["text"]
