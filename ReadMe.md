# X Post Generator with Gemini

Generate compelling X (Twitter) posts from your images using Google Gemini AI!  
This Streamlit app takes an uploaded image and (optionally) your description, then generates an engaging X post in your chosen tone, with options for hashtags and emojis.

---

## Features

- Upload an image (JPG, PNG)
- Choose tone: Casual, Professional, Funny, Inspirational, Provocative
- Optionally describe the image for better results
- Include/exclude hashtags and emojis
- Set maximum character count (up to 280)
- Copy or download the generated post
- Powered by Google Gemini API

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/x-post-generator.git
cd x-post-generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your environment variables

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run the app

```bash
streamlit run main.py
```

---

## Deploy on Streamlit Community Cloud

1. Push your code to a public GitHub repository.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Click **"New app"** and connect your GitHub repo.
4. Set your `GEMINI_API_KEY` as a **Secret** in the app's settings.
5. Deploy!

---

## Requirements

- Python 3.8+
- Streamlit
- Pillow
- python-dotenv
- google-generativeai

---

## License

MIT License

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Gemini API](https://ai.google.dev/)
