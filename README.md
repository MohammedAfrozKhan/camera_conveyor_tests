# Tiny Implementation: Battery Module Test Cell

## Project Structure

app/ # Application logic (vision, PLC, system)
tests/ # pytest tests (unit, E2E, UI)

## How to Run Tests

1. Make sure Python 3.14+ is installed.
2. Install dependencies: 
python -m pip install pytest selenium webdriver-manager
3. Run all tests: 
python -m pytest

## Test Types

- **Unit Tests:** `test_vision_unit.py`, `test_plc_unit.py`  
- **E2E Tests:** `test_e2e_happy_path.py`, `test_e2e_edge_cases.py`  
- **UI Smoke Test:** `test_ui_smoke.py`

## Assumptions

- No real hardware needed.
- Camera, belt, and manipulator are faked/mocked.
- Logging simulates module detection and movement.
- CI/CD: unit/component tests on every push, E2E tests nightly or on main.

## Artifacts

- Logs printed in console.
- Can be extended to save captured images or cycle logs.

