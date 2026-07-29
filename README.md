# RAC (Art Club)

A Django web application, deployed on Vercel.

🔗 **Live site:** [rac-fawn.vercel.app](https://rac-fawn.vercel.app)

## Tech Stack

- **Backend:** Django 6.0
- **Static files:** WhiteNoise
- **Deployment:** Vercel (serverless, `@vercel/python`)

## Project Structure

```
rac/
├── artclub/
│   ├── artclub/        # Django project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── club/            # Django app
│   └── manage.py
├── requirements.txt      # Python dependencies (used by Vercel build)
├── vercel.json            # Vercel build & routing config
└── README.md
```

## Getting Started (Local Development)

1. **Clone the repo**
   ```bash
   git clone https://github.com/ariful-riane/rac.git
   cd rac/artclub
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server**
   ```bash
   python manage.py runserver
   ```

5. Visit `http://127.0.0.1:8000` in your browser.

## Deployment

This project is deployed on [Vercel](https://vercel.com) using the `@vercel/python` builder. Configuration lives in `vercel.json` at the repo root, which points to `artclub/artclub/wsgi.py` as the entry point.

Any push to the `master` branch triggers an automatic redeploy.

## License

This project currently has no license specified.
