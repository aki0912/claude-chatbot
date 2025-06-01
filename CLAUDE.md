# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flask-based web chatbot application that provides a web interface for interacting with Claude AI via the Anthropic API. The application maintains conversation history in Flask sessions and provides a clean, responsive chat interface.

## Architecture

- **app.py**: Main Flask application with three routes:
  - `/` - Serves the chat interface (index.html)
  - `/chat` - POST endpoint that handles user messages and returns Claude responses
  - `/clear` - POST endpoint to clear conversation history
- **claude_api.py**: ClaudeAPI wrapper class that handles Anthropic API communication
- **templates/index.html**: Single-page chat interface with embedded CSS and JavaScript

## Development Commands

```bash
# Install dependencies with uv
uv sync

# Run the application
uv run python app.py

# Or activate the virtual environment and run directly
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
python app.py

# The app runs on http://localhost:5000
```

## Environment Setup

Copy `.env.example` to `.env` and configure:
- `ANTHROPIC_API_KEY`: Your Anthropic API key
- `SECRET_KEY`: Flask session secret key

## Key Implementation Details

- Conversation history is stored in Flask sessions (session['conversation'])
- Uses Claude 3.5 Sonnet model (claude-3-5-sonnet-20241022) with 1000 max tokens
- Frontend uses vanilla JavaScript with fetch API for AJAX communication
- Chat interface auto-scrolls and includes typing indicators
- Error handling returns JSON responses with status and error messages