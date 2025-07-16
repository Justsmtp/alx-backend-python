# 0x03. Unittests and Integration Tests

## Learning Objectives

- Understand the difference between unit tests and integration tests.
- Master common testing patterns such as mocking, parameterization, and fixtures.

## Technologies Used

- Python 3.7
- Pycodestyle 2.5
- unittest + parameterized

## Project Structure

- `utils.py`: Utility functions.
- `client.py`: Classes for HTTP interaction.
- `fixtures.py`: Static data for mocking responses.
- `test_utils.py`: Unit tests for `utils.py`.
- `test_client.py`: Unit and integration tests for `client.py`.

## Usage

To run tests:
```bash
python3 -m unittest test_utils.py
python3 -m unittest test_client.py

Ensure you have parameterized installed:

```bash
pip install parameterized


---

