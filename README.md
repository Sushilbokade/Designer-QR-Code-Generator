# Artistic QR Code Generator

A web application that generates beautiful, artistic QR codes with various patterns and styles. Create unique QR codes that are both functional and visually appealing.

## Features

- Multiple artistic patterns (circles, diamonds, flowers, stars, hexagons, rounded)
- Beautiful color combinations
- High error correction for reliable scanning
- Easy-to-use web interface
- Instant preview and download options

## Live Demo

The application will be available after deployment. Follow the deployment instructions below to host your own instance.

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   venv\Scripts\activate     # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Visit `http://localhost:5000` in your browser

## Free Deployment to Render

1. Create a free account at [Render.com](https://render.com)
2. Connect your GitHub repository (first push your code to GitHub)
3. In Render Dashboard, click "New +" and select "Web Service"
4. Choose your repository
5. Fill in these details:
   - Name: artistic-qr-generator (or your preferred name)
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Click "Create Web Service"

Your application will be deployed and available at the URL provided by Render (usually something like `https://your-app-name.onrender.com`).

## Technologies Used

- Python/Flask
- qrcode library
- Pillow for image processing
- TailwindCSS for styling
- JavaScript for interactivity

## License

MIT License - Feel free to use and modify