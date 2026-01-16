from app.vision import detect_modules
import logging

# Simple logging for QA/artifacts
logging.basicConfig(level=logging.INFO, format='%(message)s')

def run_cycle(plc, camera_frame):
    """
    Simulates a single conveyor cycle:
    start -> capture image -> module out
    """
    plc.start_cycle()
    logging.info("Cycle started")

    if detect_modules(camera_frame):
        plc.set_module_out()
        logging.info("Module detected, moved out")
        return "OK"

    logging.info("No module detected")
    return "NO_MODULE"
