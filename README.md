# Minimalist Portfolio Website

A simple, minimalist portfolio website built with [Flask](https://flask.palletsprojects.com/) and ready to be hosted on Linux.

## Features

- Clean, minimalist design
- Built with Python and Flask
- Easy to deploy on any Linux server
- Ready for customization

## Getting Started

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd portfolio-site
   ```
2. **Create and activate a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```
3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```
4. **Run the Flask app**
    ```sh
    flask run
    ```

## Deployment
For production, use [Gunicorn](https://gunicorn.org/) as the WSGI server:
```sh
gunicorn -w 4 app:app
```