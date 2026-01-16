def test_plc_start_and_stop(plc_connection):
    """Unit test: PLC can start and stop correctly"""
    plc_connection.start_cycle()
    assert plc_connection.started is True

    plc_connection.stop()
    assert plc_connection.started is False
