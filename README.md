# ArxivSearch

ArxivSearch is a fast and convenient service designed to help you find scientific articles, save them, highlight key points, and create a network of research groups with similar research interests. This project leverages FastAPI for the backend, allowing efficient and scalable API interactions.

## Features

- **Search Scientific Articles**: Quickly find articles on arXiv using a keyword search.
- **Save Articles**: Save articles for future reference.
- **Highlight Text**: Highlight important parts of the articles.
- **Research Network**: Create a network of research groups with similar interests.

## API Endpoints
**GET /**: 
- **Description**: Renders the main search page.
**Response**: HTML page with a search form.
  
**POST /search**: 
- **Description**: Accepts a search term and returns the search results from arXiv.
- **Request Parameters**:
- **Response**: HTML page with a table of search results or JSON error message if no search term is provided.


## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ArxivSearch.git
   cd ArxivSearch
