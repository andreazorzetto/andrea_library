# Andrea_Library ;)

A versatile library designed to simplify the integration with Aqua APIs.

## Installation

It's recommended to create a Python virtual environment to manage dependencies effectively.

**Step 1:** Create a Virtual Environment

Use the following commands to create and activate a virtual environment:
```
python3 -m venv aquaenv
source aquaenv/bin/activate
```

**Step 2:** Install the Package

Navigate to the library's directory and install the package in editable mode:
```
cd andrea_library
pip install -e .
```

## Usage

Examples demonstrating the usage of Andrea_Library are available in the `examples` folder. These examples cover various scenarios to help you get started quickly.


## Testing
To ensure everything is working correctly, you can run the test suite included with the library. This can help verify that all functionalities are operating as expected.
### Running Tests
Navigate to the library's directory and use the following command to run the tests, for either mocked or real tests:
```bash
pytest tests/mock/
pytest tests/real/
```

The test results will provide feedback on the various components of the library, making it easier to identify and resolve any issues.

## Misc
### Install pytest
To install pytest on your MacBook, follow these steps:

**Step 1**: Following the test above to activate your Python Virtual Environment

**Step 2**: Install pytest

With your virtual environment activated, you can install pytest using pip. Open your terminal and run:
```bash
pip install pytest
```

**Step 3**: Verify the Installation

To ensure pytest was installed correctly, you can check its version:
```bash
pytest --version
```

**Upgrading**: 

To upgrade pytest to the latest version, you can run:
```bash
pip install --upgrade pytest
```

### Deactivate Python Virtual Environment
```bash
deactivate
```