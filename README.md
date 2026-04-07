# QA Automation Test – SignSetu

## 👨‍💻 Candidate

Darshan S

---

## 📌 Project Overview

This project implements an automated test suite for the SignSetu backend API (Video Caption Processing Pipeline).

The main objectives were to:

- Automate the complete API workflow
- Handle asynchronous processing effectively
- Validate responses and data integrity
- Identify and document real-world bugs

---

## ⚙️ Tech Stack

- Python
- Pytest
- Requests

---

## 🔄 Test Workflow Covered

1. **Authentication**
   - POST `/api/auth`
   - Retrieves session token

2. **Create Video**
   - POST `/api/videos`
   - Creates a new video record

3. **Trigger Caption Processing**
   - POST `/api/videos/{id}/process-captions`
   - Starts asynchronous caption generation

4. **Fetch Captions**
   - GET `/api/captions?videoId={id}`
   - Implemented polling to handle async processing

5. **Cleanup**
   - DELETE `/api/videos/{id}`

---

## 🔁 Async Handling Strategy

Caption generation is asynchronous. To handle this reliably:

- Implemented polling with retry logic
- Added delays between requests
- Validated response availability before assertions

---

## 🧪 Test Strategy

- End-to-end workflow validation
- Negative testing (invalid inputs, missing headers)
- Edge case testing (duplicate requests, invalid IDs)
- Repeatability testing (multiple test executions)

---

## 🐞 Bugs & Observations

### 1. State Collision in Authentication

- Error: `This X-Candidate-ID is already active`
- Cause: Reuse of the same candidate ID
- Impact: Breaks test repeatability
- Suggestion: Allow multiple sessions or reset state

---

### 2. Inconsistent Status Codes

- Example: Invalid video ID returns `401` instead of `404`
- Impact: Misleading API behavior
- Suggestion: Use appropriate HTTP status codes

---

### 3. Caption Generation Instability

- Issue: Captions are not consistently generated after processing
- Impact: Flaky asynchronous behavior
- Suggestion: Improve processing reliability or provide status tracking

---

### 4. Duplicate Processing Allowed

- Same video can trigger caption processing multiple times
- Expected behavior: Prevent duplicate processing requests

---

### 5. Missing Header Validation

- API does not strictly validate missing `X-Candidate-ID`
- Impact: Potential design/security issue

---

## 📸 Screenshots

Included:

- Test execution results (pytest output)
- Failed test cases (bug evidence)
- Code implementation

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
pytest -v
```

---

## ✅ Key Highlights

- End-to-end API automation implemented
- Asynchronous workflow handled using polling
- Multiple real-world bugs identified
- Tests designed for reliability and repeatability

---

## 🎯 Conclusion

This test suite not only validates API functionality but also highlights critical issues in system behavior.
The approach focuses on real-world QA practices including robustness, edge case handling, and bug discovery.
