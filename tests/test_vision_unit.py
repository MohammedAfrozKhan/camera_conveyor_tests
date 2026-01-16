from app.vision import detect_modules

def test_detects_module_present():
    """Unit test: detect_modules returns True if module is present"""
    frame = {"modules": 1}
    assert detect_modules(frame) is True

def test_detects_no_module():
    """Unit test: detect_modules returns False if no module is present"""
    frame = {"modules": 0}
    assert detect_modules(frame) is False
