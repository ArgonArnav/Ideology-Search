from flask import Flask, request, jsonify
from flask_cors import CORS
from search_engine import (
    search_documents_vector_space,
    search_documents_pagerank,
    search_documents_hits,
    search_google_serpapi,
    search_bing_serpapi
)
import time

app = Flask(__name__)
CORS(app)

@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query', '')
    algorithm = data.get('ranking_algorithm', 'tfidf')

    # Custom Search Engine based on algorithm
    start_time = time.time()

    if algorithm == 'pagerank':
        custom_results = search_documents_pagerank(query)
        method_used = "PageRank"
    elif algorithm == 'hits':
        custom_results = search_documents_hits(query)
        method_used = "HITS"
    else:
        custom_results = search_documents_vector_space(query)
        method_used = "Vector Space"

    custom_time = time.time() - start_time
    print(f"[Custom Search - {method_used}]")
    print(f"Execution time: {custom_time:.4f} seconds")
    print(f"Number of results: {len(custom_results)}")
    print(f"Top result: {next(iter(custom_results)) if custom_results else 'None'}\n")

    # --- Google Search ---
    start_time = time.time()
    google_results = search_google_serpapi(query)
    google_time = time.time() - start_time

    print("[Google Search]")
    print(f"Execution time: {google_time:.4f} seconds")
    print(f"Number of results: {len(google_results)}")
    print(f"Top result: {google_results[0] if google_results else 'None'}\n")

    # --- Bing Search ---
    start_time = time.time()
    bing_results = search_bing_serpapi(query)
    bing_time = time.time() - start_time

    print("[Bing Search]")
    print(f"Execution time: {bing_time:.4f} seconds")
    print(f"Number of results: {len(bing_results)}")
    print(f"Top result: {bing_results[0] if bing_results else 'None'}\n")

    return jsonify({
        "custom": custom_results,
        "google": google_results,
        "bing": bing_results
    })

if __name__ == '__main__':
    app.run(debug=True)