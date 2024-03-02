from src.capture import capture

def test_capture() -> None:
    sound = capture()
    assert isinstance(sound, float)
    assert all(isinstance(_, float) for _ in sound)
