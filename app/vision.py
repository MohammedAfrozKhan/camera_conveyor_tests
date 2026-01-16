def detect_modules(frame):
    """
    Fake vision logic: returns True if at least one battery module is detected.
    frame: dict with key 'modules' (int)
    """
    return frame.get("modules", 0) >= 1