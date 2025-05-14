---

# 🧠 AI Document Grabber

A simple Flask-based REST API that downloads AI-generated or shared documents from a provided URL and saves them to your local system. Useful for integrating with AI assistants or bots that return document links, or just grabbing files via an API.

---

## 📂 Project Structure

```
ai_document_grabber/
│
├── ai_document_grabber/
│   └── downloader.py         # Main logic for downloading documents
│
├── tests/
│   └── test_downloader.py    # Pytest test case for downloader function
│
├── app.py                    # Flask API for handling download requests
├── README.md                 # This file
└── requirements.txt          # List of required packages
```

---

## 🚀 Features

* 🔽 Download documents via a simple API
* ✅ JSON-based POST request
* 🧪 Includes unit tests using `pytest`
* ⚙️ Headers added for secure and successful downloads
* 🧰 Ready for Postman testing

---

## 📦 Requirements

* Python 3.10+
* Flask
* Requests
* Pytest (for testing)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔧 Usage

### 1. Run the Flask app:

```bash
python app.py
```

It starts on `http://127.0.0.1:5000`

---

### 2. Test with Postman

#### ➤ POST Request

**URL**: `http://127.0.0.1:5000/download`
**Method**: `POST`
**Headers**:
`Content-Type: application/json`

**Body** (raw JSON):

```json
{
  "url": "https://raw.githubusercontent.com/github/gitignore/main/README.md",
  "filename": "README.md"
}
```

#### ➤ GET Request

**URL**: `http://127.0.0.1:5000/download`
**Method**: `GET`

This is just for a simple confirmation response like:

```json
{
  "message": "Welcome to the AI Document Grabber API!"
}
```

---

## 🧪 Running Tests

```bash
pytest
```

This runs the downloader test to ensure the URL is valid and the file downloads correctly.

---

## 🛡 Error Handling

* Returns a `400` if URL or filename is missing
* Returns a `500` if the file could not be downloaded (e.g. invalid URL or headers issue)

---

## 🧠 Motivation

This project helps automate the process of receiving and downloading documents from AI tools. Instead of clicking links manually, just post the URL to the API and let it handle it.

---

## 📌 Future Improvements

* Add support for saving to a specific folder
* Add file extension/type validation
* Deploy to a cloud platform (like Render or Heroku)
* Add authentication (e.g., API keys)
* Log successful and failed downloads

---

## 🤝 Contributing

Feel free to fork and open a PR! Bug fixes, improvements, and new features are welcome.

---

## 📝 License

This project is open-source under the [MIT License](LICENSE).

---


