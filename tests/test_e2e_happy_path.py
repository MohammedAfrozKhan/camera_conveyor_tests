from app.system import run_cycle

def test_happy_path_start_capture_module_out(plc_connection):
    """E2E test: module present, full cycle completes successfully"""
    frame = {"modules": 1}
    result = run_cycle(plc_connection, frame)

    assert result == "OK"
    assert plc_connection.started is True
    assert plc_connection.module_out is True
