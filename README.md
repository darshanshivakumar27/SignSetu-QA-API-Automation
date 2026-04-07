# SignSetu QA API Automation

## Project Overview

SignSetu QA API Automation is a Python-based automated testing framework built using **Pytest** and **Requests** to validate REST APIs.
The project demonstrates automated API validation, asynchronous response handling, and bug detection through automated test cases.

This framework tests different API endpoints of the SignSetu platform and verifies responses, status codes, and expected outputs.

---

## Features

- Automated REST API testing
- Positive and negative test case validation
- Async API polling verification
- Bug detection and reporting
- Screenshot evidence for discovered issues

---

## Technologies Used

- Python
- Pytest
- Requests Library
- REST API Testing
- Automated QA Testing

---

## Project Structure

```
SignSetu-QA-API-Automation
│
├── test_api.py
├── test_bugs.py
├── utils.py
├── conftest.py
├── requirements.txt
├── screenshots
│     ├── bug_captions.png
│     ├── bug_invalid_id.png
│
└── README.md
```

### File Description

**test_api.py**
Contains automated API test cases for validating main API flows.

**test_bugs.py**
Contains test cases designed to detect bugs and unexpected API behavior.

**utils.py**
Helper functions used across the test framework.

**conftest.py**
Pytest fixtures and configuration setup.

**screenshots/**
Contains screenshot evidence of bugs discovered during testing.

---

## Installation

Clone the repository

```
git clone https://github.com/darshanshivakumar27/SignSetu-QA-API-Automation.git
```

Navigate to project folder

```
cd SignSetu-QA-API-Automation
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Running the Tests

Run all automated API tests using:

```
pytest -v
```

This will execute all test cases and display the results in the terminal.

---

## Bug Evidence

During automated testing, the following issues were identified:

**Invalid Video ID Bug**

Screenshot available in:

```
screenshots/bug_invalid_id.png
```

**Captions API Bug**

Screenshot available in:

```
screenshots/bug_captions.png
```

---

## Author

Darshan S
BE Computer Science & Data Science
PES College of Engineering, Mandya

GitHub
https://github.com/darshanshivakumar27
