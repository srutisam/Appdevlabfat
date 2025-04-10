# Appdevlabfat
22mic0132


.github/workflows/main.yml

name: CI/CD Pipeline for Python Web Application

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  linting:
    name: Static Code Analysis
    runs-on: ubuntu-latest

    steps:
    # Check out the code
    - name: Checkout code
      uses: actions/checkout@v3

    # Set up Python
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    # Install dependencies
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    # Run Flake8 for Python code linting
    - name: Run Python Linter (flake8)
      run: |
        flake8 .

  style-check:
    name: Style Checks
    runs-on: ubuntu-latest

    steps:
    # Check out the code
    - name: Checkout code
      uses: actions/checkout@v3

    # Run Stylelint for CSS/SCSS files
    - name: Run Stylelint
      uses: actions/stylelint@v3
      with:
        args: "**/*.css **/*.scss"
