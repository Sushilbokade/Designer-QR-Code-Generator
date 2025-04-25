# Artistic QR Code Generator

A web application that generates beautiful, artistic QR codes with various patterns and styles. Create unique QR codes that are both functional and visually appealing.

## Table of Contents
- [Features](#features)
- [Technical Overview](#technical-overview)
- [System Architecture](#system-architecture)
- [Component Details](#component-details)
- [API Documentation](#api-documentation)
- [Development Guide](#development-guide)
- [Deployment Guide](#deployment-guide)
- [Performance & Security](#performance--security)
- [Maintenance & Troubleshooting](#maintenance--troubleshooting)
- [License](#license)

## Features

- Multiple artistic patterns (circles, diamonds, flowers, stars, hexagons, rounded)
- Beautiful color combinations
- High error correction for reliable scanning
- Easy-to-use web interface
- Instant preview and download options

## Technical Overview

### Technology Stack
- **Backend**: Python 3.11+ with Flask framework
- **Frontend**: HTML5, JavaScript, TailwindCSS
- **Image Processing**: PIL (Python Imaging Library), qrcode library
- **Deployment**: Render.com (Cloud Platform)
- **Version Control**: Git

### Project Structure
```
├── app.py                 # Flask application server
├── qr_generator.py        # Core QR code generation logic
├── demo.py               # Demonstration script
├── requirements.txt      # Python dependencies
├── render.yaml           # Render deployment configuration
├── Procfile             # Process file for web servers
├── templates/
│   └── index.html       # Frontend user interface
└── static/
    └── generated/       # Generated QR code storage
```

## System Architecture

### Architecture Diagram
```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Web Browser   │────▶│   Flask Server   │────▶│  QR Generator   │
│   (Frontend)    │◀────│   (Backend API)  │◀────│     Engine      │
└─────────────────┘     └──────────────────┘     └─────────────────┘
        ▲                        │                        │
        │                        ▼                        ▼
        │                ┌──────────────────┐    ┌─────────────────┐
        └───────────────│  Static Assets    │    │   File System   │
                       │  (Generated QRs)   │    │    Storage      │
                       └──────────────────┘     └─────────────────┘
```

### Data Flow
1. User inputs text and selects style
2. Frontend sends POST request to /generate
3. Backend validates input and generates QR code
4. QR code is saved to static/generated/
5. Frontend displays and enables download

## Component Details

### Core QR Generation Engine
The QR code generation is handled by two main classes:

#### ArtisticQRCode Class
- Custom pattern styles implementation
- Dual-color scheme support
- Configurable parameters
- High-quality anti-aliased output

**Pattern Styles:**
1. **Circles**
   - Alternating circle sizes
   - Enhanced contrast through size variation
   
2. **Diamonds**
   - Rotated square patterns
   - Mathematical precision in angles
   
3. **Flowers**
   - Six-petal design
   - Overlapping petals with centered dots
   
4. **Stars**
   - Eight-point star design
   - Inner/outer radius variation
   
5. **Hexagons**
   - Nested patterns with contrast
   - Geometric precision
   
6. **Rounded**
   - Soft-cornered squares
   - Nested design with padding

#### AIQRCodeGenerator Class
- Handles high-level QR generation
- Manages color schemes
- Implements error correction
- Handles file operations

## API Documentation

### Endpoints

#### GET /
- **Purpose**: Main application interface
- **Response**: HTML page
- **Error Codes**: 404, 500

#### POST /generate
- **Purpose**: QR code generation
- **Request Body**:
  ```json
  {
    "text": "string",
    "style": "circles|diamonds|flowers|stars|hexagons|rounded"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "image_url": "string",
    "download_name": "string"
  }
  ```
- **Error Codes**: 400, 500

## Development Guide

### Prerequisites
- Python 3.11+
- pip package manager
- Git (optional)

### Local Development Setup

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

### Environment Variables
- `PORT`: Server port (default: 5000)
- `MAX_CONTENT_LENGTH`: Max file size (default: 16MB)

## Deployment Guide

### Deploying to Render.com

1. Create a free account at [Render.com](https://render.com)
2. Connect your GitHub repository
3. In Render Dashboard, click "New +" and select "Web Service"
4. Choose your repository
5. Configure the service:
   - Name: artistic-qr-generator (or preferred name)
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Python Version: 3.11
6. Click "Create Web Service"

### Post-Deployment Checklist
- [ ] Verify all QR styles work
- [ ] Test error handling
- [ ] Monitor performance
- [ ] Check file cleanup

## Performance & Security

### Performance Optimizations
- Optimized drawing algorithms
- Memory-efficient image handling
- Automatic file cleanup
- Responsive UI design

### Security Measures
1. **File System Security**
   - Controlled file paths
   - Automatic cleanup
   - Size limitations

2. **Input Validation**
   - Request validation
   - Content type checking
   - Error boundaries

3. **Output Safety**
   - Secure file serving
   - Unique filenames
   - Content-Type headers

## Maintenance & Troubleshooting

### Regular Maintenance
1. Monitor disk usage
2. Check error logs
3. Verify file cleanup
4. Update dependencies

### Common Issues & Solutions

1. **QR Generation Fails**
   - Check input text length
   - Verify style parameter
   - Check disk space

2. **Performance Issues**
   - Monitor memory usage
   - Check file cleanup
   - Verify concurrent requests

3. **Deployment Issues**
   - Check Python version
   - Verify dependencies
   - Check environment variables

## License

MIT License - Feel free to use and modify  
Copyright (c) 2025 Sushil Bokade
