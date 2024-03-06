from src.capture import capture
from src.preprocessing import preprocessing

def test_preprocessing() -> None:
    sound = capture()
    processed_sound = preprocessing(sound)
    assert isinstance(processed_sound, list)
    assert all(isinstance(_, float) for _ in processed_sound)
