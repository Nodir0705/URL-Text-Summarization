# URL Text Summarization

A small desktop app that downloads a news article from a URL and shows a short summary of it.

## What it does

You paste an article URL into the window and press **Summerize**. The app downloads the page, pulls out the article text, and picks the most important sentences. The summary is about 20% of the original sentences and opens in a new window.

## How it works

1. `newspaper3k` downloads the page and extracts the article text.
2. spaCy (`en_core_web_sm`) splits the text into words and sentences.
3. Each word that is not a stop word or punctuation gets a score: how often it appears, divided by the count of the most frequent word.
4. Each sentence gets the sum of its word scores.
5. The top 20% of sentences by score become the summary.

The window is built with Tkinter and a bundled copy of CustomTkinter 4.3.0.

## Quick start

There is no `requirements.txt`; these packages match the imports in `URLsummarization.py`.

```bash
git clone https://github.com/Nodir0705/URL-Text-Summarization.git
cd URL-Text-Summarization
pip install newspaper3k spacy "pillow<10" matplotlib
python -m spacy download en_core_web_sm
python URLsummarization.py
```

Run it from the repository folder, because the app loads `logo.png` and `icon.ico` by relative path.

## Project structure

- `URLsummarization.py` - the whole app: window, URL input, and the summarizer
- `customtkinter/` - bundled copy of the CustomTkinter library (version 4.3.0)
- `logo.png`, `icon.ico` - images used by the window

## Notes

- This is a 2022 university group project, kept as a learning example.
- The summary is extractive: it copies existing sentences and does not write new ones.
- `pillow<10` is needed because the code uses `Image.ANTIALIAS`, which newer Pillow removed.
- `app.iconbitmap('icon.ico')` works on Windows; on Linux or macOS you may need to remove that line.
- The text in the Help window was copied from another project and does not describe this app.
- Not tested with current package versions.
