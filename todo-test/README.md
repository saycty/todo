## Installation

To get started with MyApp, you'll need to have Python 3.8 or above installed. Then, follow these steps:

1. Clone the repository.

2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application, use the following command:

```bash
uvicorn main:app --reload
```

This will start the server on `http://127.0.0.1:8000`. You can visit this URL in your browser to interact with the app.

### API Documentation

You can access the API documentation at `http://127.0.0.1:8000/docs` once the server is running.
