import pytest
from app.plc import FakePLC

@pytest.fixture(scope="session")
def plc_connection():
    """
    Session-scoped fake PLC connection.
    Created once per test session and reused by all tests.
    """
    plc = FakePLC()
    yield plc
    plc.stop()
