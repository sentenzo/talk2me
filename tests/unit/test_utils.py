import pytest

from talk2me.utils import audio_to_text
from tests.conftest import AUDIO_FILES, seq_similarity

SEQ_SIM_THRESHOLD = 0.9  # in interval [0, 1]
seq_similarity


@pytest.mark.parametrize(
    "audio_file_name",
    list(AUDIO_FILES),
)
def test_audio_to_text(audio_file_name):
    path_to_audio = AUDIO_FILES[audio_file_name]["path"]
    t_expected = AUDIO_FILES[audio_file_name]["transcription"]
    t_received = audio_to_text(path_to_audio)
    seq_sim = seq_similarity(t_expected, t_received)
    print("t_received:", t_received)
    print("seq_sim:", seq_sim)
    assert seq_sim >= SEQ_SIM_THRESHOLD
