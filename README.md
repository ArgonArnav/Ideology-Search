# Ideology-Search

A domain-specific “Ideologies” search engine featuring a high-performance Python-based asyncio/aiohttp crawler that gathered & deduplicated 100K+ English pages, extracted metadata & hyperlink graphs for an inverted TF-IDF, PageRank & HITS index. This project develops the full crawling → indexing → UI pipeline and benchmarks its semantic precision & contextual relevance against Google & Bing.

---

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

---

## Features

- **Asyncio/Aiohttp Crawler:** High-performance web crawler for large-scale data collection.
- **Deduplication:** Cleans and deduplicates crawled data.
- **Metadata & Hyperlink Extraction:** Builds metadata and hyperlink graphs for downstream indexing.
- **Indexing:** Inverted index using TF-IDF, PageRank, and HITS algorithms (scikit-learn based).
- **Full-stack Pipeline:** Seamless integration from crawling to search UI.
- **Semantic Benchmarking:** Compare and benchmark results against Google and Bing for precision and relevance.

---

## Architecture

```
frontend/ (React)
   |
   v
backend/ (Flask, Asyncio, Sklearn, Crawler)
   |
   v
Crawling → Deduplication → Indexing → Search API → UI
```

---

## Backend Setup

The backend is a Python (Flask) app with async crawling and indexing.

### Prerequisites

- Python 3.8+
- `pip`

### Installation

1. Navigate to the backend directory:

   ```sh
   cd backend
   ```

2. (Optional but recommended) Create a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:

   ```sh
   pip install -r requirements.txt
   ```

   **Requirements include:**
   - flask
   - flask-cors
   - scikit-learn
   - requests
   - beautifulsoup4
   - googlesearch-python
   - serpapi

### Running the Backend Server

```sh
python app.py
```

The backend will start (by default) at `http://127.0.0.1:5000`.

---

## Frontend Setup

The frontend is built using React.

### Prerequisites

- Node.js (v18+ recommended)
- npm (comes with Node.js)

### Installation

1. Navigate to the frontend directory:

   ```sh
   cd frontend
   ```

2. Install frontend dependencies:

   ```sh
   npm install
   ```

### Running the Frontend

```sh
npm start
```

This will start the frontend (typically at `http://localhost:3000`) and proxy API requests to the backend.

---

## Usage

1. **Start the backend server** (see above).
2. **Start the frontend UI** (see above).
3. Open your browser at `http://localhost:3000` to use the Ideology search engine.

---

## Project Structure

```
backend/
  ├── app.py               # Flask API server
  ├── crawler.py           # Asyncio/Aiohttp web crawler
  ├── conver_pkl.py        # Utility for pickle conversion
  ├── prepare_sklearn_index.py # Index preparation scripts
  ├── search_engine.py     # Main search engine logic
  ├── sklearn_indexer.py   # Sklearn-based indexing
  ├── requirements.txt     # Python dependencies
  └── terms.json           # Domain-specific terms

frontend/
  ├── README.md
  ├── package.json         # React/NPM dependencies
  ├── public/
  └── src/                 # React source code
```

---

## License

This project is MIT license. Please contact the repository owner for usage terms.

---

## Author

- [ArgonArnav](https://github.com/ArgonArnav)

---
