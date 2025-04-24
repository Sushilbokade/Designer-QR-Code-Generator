# Artistic QR Code Generator

A web application that generates beautiful, artistic QR codes with various patterns and styles. Create unique QR codes that are both functional and visually appealing.

## Features

- Multiple artistic patterns (circles, diamonds, flowers, stars, hexagons, rounded)
- Beautiful color combinations
- High error correction for reliable scanning
- Easy-to-use web interface
- Instant preview and download options

## Live Demo

Visit [https://artistic-qr-generator.herokuapp.com](https://artistic-qr-generator.herokuapp.com) to try it out!

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

## Deployment to Heroku

1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Login to Heroku:
   ```bash
   heroku login
   ```
3. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```
4. Push to Heroku:
   ```bash
   git push heroku main
   ```

## Technologies Used

- Python/Flask
- qrcode library
- Pillow for image processing
- TailwindCSS for styling
- JavaScript for interactivity

## License

MIT License - Feel free to use and modify