from qr_generator import AIQRCodeGenerator

def main():
    # Initialize the QR code generator
    generator = AIQRCodeGenerator()
    
    # Test different artistic styles
    test_cases = [
        {
            "message": "Circles within circles, infinite patterns",
            "style": "circles",
            "filename": "qr_circles.png"
        },
        {
            "message": "Diamond light reflecting wisdom",
            "style": "diamonds",
            "filename": "qr_diamonds.png"
        },
        {
            "message": "A garden of digital flowers blooms",
            "style": "flowers",
            "filename": "qr_flowers.png"
        },
        {
            "message": "Starlight guiding through code",
            "style": "stars",
            "filename": "qr_stars.png"
        },
        {
            "message": "Hexagonal harmony in data",
            "style": "hexagons",
            "filename": "qr_hexagons.png"
        },
        {
            "message": "Smooth edges frame the future",
            "style": "rounded",
            "filename": "qr_rounded.png"
        }
    ]
    
    try:
        print("Generating artistic QR codes...\n")
        for case in test_cases:
            output_path = generator.generate_qr(
                text=case["message"],
                output_path=case["filename"],
                style=case["style"]
            )
            print(f"✨ Created {case['style']} style QR code: {output_path}")
            print(f"📝 Message: {case['message']}")
            print()
        
        print("\nAll QR codes generated successfully!")
        print("Each QR code features:")
        print("• Unique artistic patterns (circles, diamonds, flowers, stars, hexagons, rounded)")
        print("• Beautiful color combinations from a curated palette")
        print("• High error correction for reliable scanning")
        print("• Enhanced contrast for better visibility")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()