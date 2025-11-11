
name: Python Test are imports right

on:
  push:
    paths:
    - 'main.py'
    - 'eye_tracker.py.py'
    - 'camera_display.py'
    - 'spi_display.py'

jobs:
  build:
    strategy:
      # we should give github deside own speed max-parallel: 1
      matrix:
        python: [3.10.10, 3.11, 3.12]
        
        os: [ubuntu-20.04, ubuntu-latest] 
        exclude:
          - os: ubuntu-20.04
            python: 3.10.10
          - os: ubuntu-20.04
            python: 3.11
          - os: ubuntu-20.04
            python: 3.12
    runs-on: ${{ matrix.os }}


    steps:
    - uses: actions/checkout@v4
    - name: Setup Python
      uses: actions/setup-python@v6.0.0
      with:
        python-version: ${{ matrix.python }}
    - name: Install dependencies
      run: |
        python3 -m pip install --upgrade pip
        pip3 install -r requirements.txt
        pip3 install pytest pytest-cov
    - name: Test test_imports.py with pytest and run flake8 and then try compile it.
      run: |
        pytest test_imports.py
        flake8 .
        python -m py_compile *.py
