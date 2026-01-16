from app.system import run_cycle

def test_no_module_cycle(plc_connection):
    """E2E test: no module present, system handles gracefully"""
    frame = {"modules": 0}
    result = run_cycle(plc_connection, frame)

    assert result == "NO_MODULE"
    assert plc_connection.started is True
    assert plc_connection.module_out is False
