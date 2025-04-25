import qrcode
from qrcode.image.base import BaseImage
from qrcode.image.pure import PymagingImage
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageOps
import numpy as np
import random
import math
from typing import Tuple, Optional

class ArtisticQRCode:
    def __init__(self, border, width, box_size, style='circles', main_color='#000000', accent_color='#000000', back_color='white'):
        self.border = border
        self.width = width
        self.box_size = box_size
        self.style = style
        self.main_color = main_color
        self.accent_color = accent_color
        self.back_color = back_color
        self.img_size = (width + border * 2) * box_size
        self._img = Image.new('RGBA', (self.img_size, self.img_size), back_color)
        self._draw = ImageDraw.Draw(self._img)
        
    def draw_module(self, row, col, is_active):
        if not is_active:
            return

        x = (col + self.border) * self.box_size
        y = (row + self.border) * self.box_size
        box = [x, y, x + self.box_size, y + self.box_size]
        
        center_x = x + self.box_size // 2
        center_y = y + self.box_size // 2
        box_width = self.box_size
        box_height = self.box_size
        
        if self.style == 'circles':
            # Draw circular modules with varying sizes
            radius = min(box_width, box_height) // 2
            if (row + col) % 2 == 0:
                radius = int(radius * 0.8)  # Smaller circles for alternating pattern
            self._draw.ellipse([
                center_x - radius, center_y - radius,
                center_x + radius, center_y + radius
            ], fill=self.main_color if (row + col) % 2 == 0 else self.accent_color)
            
        elif self.style == 'diamonds':
            # Draw diamond shapes with slight rotation for variety
            angle = math.pi / 6 if (row + col) % 2 == 0 else -math.pi / 6
            radius = min(box_width, box_height) // 2
            points = []
            for i in range(4):
                base_angle = (2 * math.pi * i) / 4
                adjusted_angle = base_angle + angle
                x = center_x + radius * math.cos(adjusted_angle)
                y = center_y + radius * math.sin(adjusted_angle)
                points.append((x, y))
            self._draw.polygon(points, fill=self.main_color if (row + col) % 2 == 0 else self.accent_color)
            
        elif self.style == 'flowers':
            # Draw flower-like patterns with overlapping petals
            radius = min(box_width, box_height) // 3
            petals = 6
            # Draw outer petals
            for i in range(petals):
                angle = (2 * math.pi * i) / petals
                petal_x = center_x + radius * math.cos(angle)
                petal_y = center_y + radius * math.sin(angle)
                petal_size = radius * 0.8
                self._draw.ellipse([
                    petal_x - petal_size, petal_y - petal_size,
                    petal_x + petal_size, petal_y + petal_size
                ], fill=self.main_color if (row + col) % 2 == 0 else self.accent_color)
            # Draw center
            self._draw.ellipse([
                center_x - radius//2, center_y - radius//2,
                center_x + radius//2, center_y + radius//2
            ], fill=self.accent_color if (row + col) % 2 == 0 else self.main_color)
            
        elif self.style == 'stars':
            # Draw elegant star patterns
            outer_radius = min(box_width, box_height) // 2
            inner_radius = outer_radius // 2
            points = []
            num_points = 8
            # Create star shape with alternating inner and outer points
            for i in range(num_points * 2):
                angle = (2 * math.pi * i) / (num_points * 2)
                radius = outer_radius if i % 2 == 0 else inner_radius
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)
                points.append((x, y))
            self._draw.polygon(points, fill=self.main_color if (row + col) % 2 == 0 else self.accent_color)
            # Add center dot
            center_radius = inner_radius // 3
            self._draw.ellipse([
                center_x - center_radius, center_y - center_radius,
                center_x + center_radius, center_y + center_radius
            ], fill=self.accent_color if (row + col) % 2 == 0 else self.main_color)
            
        elif self.style == 'hexagons':
            # Draw hexagonal pattern with inner detail
            outer_radius = min(box_width, box_height) // 2
            inner_radius = outer_radius * 0.7
            # Draw outer hexagon
            points = []
            for i in range(6):
                angle = (2 * math.pi * i) / 6
                x = center_x + outer_radius * math.cos(angle)
                y = center_y + outer_radius * math.sin(angle)
                points.append((x, y))
            self._draw.polygon(points, fill=self.main_color if (row + col) % 2 == 0 else self.accent_color)
            # Draw inner hexagon
            inner_points = []
            for i in range(6):
                angle = (2 * math.pi * i) / 6
                x = center_x + inner_radius * math.cos(angle)
                y = center_y + inner_radius * math.sin(angle)
                inner_points.append((x, y))
            self._draw.polygon(inner_points, fill=self.accent_color if (row + col) % 2 == 0 else self.main_color)
            
        else:  # 'rounded' style
            # Draw rounded squares with inner rounded square
            outer_radius = min(box_width, box_height) // 4
            self._draw.rounded_rectangle(box, radius=outer_radius, 
                                      fill=self.main_color if (row + col) % 2 == 0 else self.accent_color)
            # Draw inner rounded square
            padding = box_width // 4
            inner_box = [x + padding, y + padding, x + box_width - padding, y + box_height - padding]
            inner_radius = outer_radius // 2
            self._draw.rounded_rectangle(inner_box, radius=inner_radius,
                                      fill=self.accent_color if (row + col) % 2 == 0 else self.main_color)
    
    def get_image(self):
        return self._img

class AIQRCodeGenerator:
    def __init__(self):
        pass
    
    def generate_qr(self, text: str, output_path: str, 
                   style: str = 'circles',
                   color_scheme: Optional[Tuple[str, str]] = None) -> str:
        """
        Generate an artistic QR code with custom patterns and colors.
        
        Args:
            text: The text to encode in the QR code
            output_path: Where to save the QR code image
            style: One of 'circles', 'diamonds', 'flowers', 'stars', 'hexagons', 'rounded'
            color_scheme: Tuple of (main_color, accent_color) in hex format
        """
        # Beautiful color schemes with good contrast
        color_schemes = [
            ('#1A237E', '#7986CB'),  # Deep blue theme
            ('#1B5E20', '#81C784'),  # Forest theme
            ('#311B92', '#9575CD'),  # Purple theme
            ('#B71C1C', '#EF9A9A'),  # Ruby theme
            ('#004D40', '#80CBC4'),  # Teal theme
            ('#E65100', '#FFB74D'),  # Orange theme
            ('#4A148C', '#BA68C8'),  # Royal purple theme
            ('#880E4F', '#F48FB1'),  # Pink theme
            ('#827717', '#C5E1A5'),  # Olive theme
            ('#01579B', '#81D4FA'),  # Ocean theme
        ]
        
        if not color_scheme:
            color_scheme = random.choice(color_schemes)
            
        # Create QR code with high error correction
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=15,  # Larger size for better pattern visibility
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        
        # Create artistic QR code image
        artistic_qr = ArtisticQRCode(
            border=qr.border,
            width=qr.modules_count,
            box_size=qr.box_size,
            style=style,
            main_color=color_scheme[0],
            accent_color=color_scheme[1],
            back_color='white'
        )
        
        # Draw QR code modules
        for row in range(qr.modules_count):
            for col in range(qr.modules_count):
                artistic_qr.draw_module(row, col, qr.modules[row][col])
        
        # Get the final image
        img = artistic_qr.get_image()
        
        # Apply final enhancements
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.2)
        
        # Save with high quality
        img.save(output_path, quality=100)
        return output_path