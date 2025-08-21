"""
TyStyle - Beautiful terminal styling with gradients and animations
Complete library in a single file for easy distribution and use.
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__description__ = "Beautiful terminal styling with gradients and animations"

import os
import time
import threading
import random
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.box import Box

# Enable Windows color support
os.system('color')
os.environ['FORCE_COLOR'] = '1'
os.environ['COLORTERM'] = 'truecolor'

console = Console()

class CustomGradients:
    """Custom gradient system with ANSI and Rich support"""
    
    GRADIENTS = {
        # === Two-color gradients ===
        "red_to_blue":      [(255, 0, 0), (0, 0, 255)],
        "green_to_purple":  [(0, 255, 0), (128, 0, 128)],
        "cyan_to_pink":     [(0, 255, 255), (255, 192, 203)],
        "orange_to_teal":   [(255, 165, 0), (0, 128, 128)],
        "yellow_to_red":    [(255, 255, 0), (255, 0, 0)],
        "pink_to_blue":     [(255, 105, 180), (0, 191, 255)],

        # === Fire/warm colors ===
        "fire":             [(139, 0, 0), (255, 69, 0), (255, 165, 0), (255, 255, 0)],
        "sunset":           [(255, 94, 77), (255, 154, 0), (255, 206, 84)],
        "lava":             [(128, 0, 0), (255, 0, 0), (255, 140, 0)],
        "ember":            [(205, 92, 92), (255, 160, 122), (255, 218, 185)],

        # === Cool/ocean colors ===
        "ocean":            [(0, 0, 139), (0, 191, 255), (173, 216, 230)],
        "ice":              [(176, 224, 230), (173, 216, 230), (240, 248, 255)],
        "arctic":           [(72, 61, 139), (106, 90, 205), (147, 112, 219)],
        "deep_sea":         [(0, 0, 128), (0, 100, 139), (0, 191, 255)],

        # === Nature colors ===
        "forest":           [(34, 139, 34), (50, 205, 50), (144, 238, 144)],
        "jungle":           [(0, 100, 0), (34, 139, 34), (107, 142, 35)],
        "autumn":           [(139, 69, 19), (205, 133, 63), (255, 165, 0)],
        "spring":           [(154, 205, 50), (124, 252, 0), (173, 255, 47)],

        # === Neon/cyberpunk ===
        "neon_green":       [(0, 255, 0), (0, 255, 127), (127, 255, 212)],
        "neon_blue":        [(0, 191, 255), (30, 144, 255), (173, 216, 230)],
        "neon_pink":        [(255, 20, 147), (255, 105, 180), (255, 182, 193)],
        "cyberpunk":        [(255, 0, 255), (0, 255, 255), (0, 255, 0)],
        "matrix":           [(0, 255, 0), (0, 128, 0), (0, 64, 0)],

        # === Rainbow variations ===
        "rainbow":          [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (128, 0, 128)],
        "rainbow_soft":     [(255, 182, 193), (255, 218, 185), (255, 255, 224), (144, 238, 144), (173, 216, 230), (221, 160, 221)],
        "pride":            [(228, 3, 3), (255, 140, 0), (255, 237, 0), (0, 128, 38), (0, 77, 255), (117, 7, 135)],

        # === Monochrome ===
        "black_to_white":   [(0, 0, 0), (255, 255, 255)],
        "white_to_black":   [(255, 255, 255), (0, 0, 0)],
        "grey_to_white":    [(128, 128, 128), (255, 255, 255)],
        "grey_to_black":    [(128, 128, 128), (0, 0, 0)],
        "grey_scale":       [(0, 0, 0), (128, 128, 128), (255, 255, 255)],

        # === Black blends ===
        "black_to_red":     [(0, 0, 0), (139, 0, 0), (255, 0, 0)],
        "black_to_blue":    [(0, 0, 0), (0, 0, 139), (0, 0, 255)],
        "black_to_green":   [(0, 0, 0), (0, 100, 0), (0, 255, 0)],
        "black_to_yellow":  [(0, 0, 0), (139, 139, 0), (255, 255, 0)],
        "black_to_purple":  [(0, 0, 0), (75, 0, 130), (128, 0, 128)],
        "black_to_orange":  [(0, 0, 0), (139, 69, 0), (255, 165, 0)],
        "black_to_pink":    [(0, 0, 0), (139, 69, 19), (255, 105, 180)],
        "black_to_cyan":    [(0, 0, 0), (0, 139, 139), (0, 255, 255)],
        "black_to_gold":    [(0, 0, 0), (184, 134, 11), (255, 215, 0)],
        "black_to_silver":  [(0, 0, 0), (128, 128, 128), (192, 192, 192)],

        # === White blends ===
        "white_to_red":     [(255, 255, 255), (255, 182, 193), (255, 0, 0)],
        "white_to_blue":    [(255, 255, 255), (173, 216, 230), (0, 0, 255)],
        "white_to_green":   [(255, 255, 255), (144, 238, 144), (0, 255, 0)],
        "white_to_yellow":  [(255, 255, 255), (255, 255, 224), (255, 255, 0)],
        "white_to_purple":  [(255, 255, 255), (221, 160, 221), (128, 0, 128)],
        "white_to_orange":  [(255, 255, 255), (255, 218, 185), (255, 165, 0)],
        "white_to_pink":    [(255, 255, 255), (255, 192, 203), (255, 105, 180)],
        "white_to_cyan":    [(255, 255, 255), (224, 255, 255), (0, 255, 255)],
        "white_to_gold":    [(255, 255, 255), (255, 248, 220), (255, 215, 0)],

        # === Dark to light blends ===
        "midnight_to_dawn": [(25, 25, 112), (70, 130, 180), (255, 218, 185)],
        "shadow_to_light":  [(47, 79, 79), (128, 128, 128), (245, 245, 245)],
        "charcoal_to_cream":[(54, 54, 54), (169, 169, 169), (255, 253, 208)],
        "obsidian_to_pearl":[(41, 36, 33), (105, 105, 105), (240, 234, 214)],
        "slate_to_ivory":   [(47, 79, 79), (112, 128, 144), (255, 255, 240)],

        # === Gradient variations ===
        "red_shades":       [(139, 0, 0), (220, 20, 60), (255, 99, 71)],
        "blue_shades":      [(0, 0, 139), (65, 105, 225), (135, 206, 235)],
        "purple_shades":    [(75, 0, 130), (138, 43, 226), (221, 160, 221)],
        "green_shades":     [(0, 100, 0), (34, 139, 34), (144, 238, 144)],
        "orange_shades":    [(139, 69, 0), (255, 140, 0), (255, 218, 185)],
        "pink_shades":      [(139, 69, 19), (255, 20, 147), (255, 182, 193)],

        # === Special effects ===
        "gold":             [(255, 215, 0), (255, 223, 0), (255, 255, 224)],
        "silver":           [(192, 192, 192), (211, 211, 211), (245, 245, 245)],
        "copper":           [(184, 115, 51), (205, 127, 50), (210, 180, 140)],
        "plasma":           [(128, 0, 128), (255, 0, 255), (255, 105, 180), (255, 255, 0)],
        "aurora":           [(0, 255, 127), (64, 224, 208), (138, 43, 226)],
        "galaxy":           [(25, 25, 112), (72, 61, 139), (123, 104, 238), (255, 20, 147)],
    }

    @staticmethod
    def _interpolate(c1, c2, t):
        return (
            int(c1[0] + (c2[0] - c1[0]) * t),
            int(c1[1] + (c2[1] - c1[1]) * t),
            int(c1[2] + (c2[2] - c1[2]) * t),
        )

    @classmethod
    def horizontal(cls, colors, text):
        if not colors or not text: return text
        result, text_len, num_colors = "", len(text), len(colors)
        for i, char in enumerate(text):
            pos = i / max(text_len - 1, 1)
            seg_size = 1.0 / max(num_colors - 1, 1)
            seg = min(int(pos / seg_size), num_colors - 2)
            local = (pos - seg * seg_size) / seg_size
            r, g, b = cls._interpolate(colors[seg], colors[seg + 1], local)
            result += f"\033[38;2;{r};{g};{b}m{char}"
        return result + "\033[0m"

    @classmethod
    def vertical(cls, colors, text):
        lines = text.split("\n")
        if len(lines) <= 1:
            return cls.horizontal(colors, text)
        result_lines = []
        for i, line in enumerate(lines):
            pos = i / (len(lines) - 1)
            seg = min(int(pos * (len(colors) - 1)), len(colors) - 2)
            local = (pos * (len(colors) - 1)) - seg
            r, g, b = cls._interpolate(colors[seg], colors[seg + 1], local)
            result_lines.append(f"\033[38;2;{r};{g};{b}m{line}\033[0m")
        return "\n".join(result_lines)

    @classmethod
    def to_rich_text(cls, colors, text, direction="horizontal"):
        if not colors or not text: 
            return Text(text)

        if direction == "vertical":
            lines = text.split("\n")
            if len(lines) == 1:
                return cls.to_rich_text(colors, text, direction="horizontal")

            rich_text = Text()
            for i, line in enumerate(lines):
                pos = i / max(len(lines) - 1, 1)
                seg = min(int(pos * (len(colors) - 1)), len(colors) - 2)
                local = (pos * (len(colors) - 1)) - seg
                r, g, b = cls._interpolate(colors[seg], colors[seg + 1], local)
                rich_text.append(line, style=f"rgb({r},{g},{b})")
                if i < len(lines) - 1:
                    rich_text.append("\n")
            return rich_text
        else:
            rich_text = Text()
            text_len, num_colors = len(text), len(colors)
            for i, char in enumerate(text):
                pos = i / max(text_len - 1, 1)
                seg_size = 1.0 / max(num_colors - 1, 1)
                seg = min(int(pos / seg_size), num_colors - 2)
                local = (pos - seg * seg_size) / seg_size
                r, g, b = cls._interpolate(colors[seg], colors[seg + 1], local)
                rich_text.append(char, style=f"rgb({r},{g},{b})")
            return rich_text

    @classmethod
    def get(cls, gradient_name, text, direction="horizontal", rich=False):
        if gradient_name not in cls.GRADIENTS:
            return text
        colors = cls.GRADIENTS[gradient_name]
        return cls.to_rich_text(colors, text, direction) if rich else (
            cls.vertical(colors, text) if direction == "vertical" else cls.horizontal(colors, text)
        )


class Animations:
    """Animation system for terminal text effects"""
    
    @staticmethod
    def clear_line():
        print('\r' + ' ' * 80 + '\r', end='', flush=True)
    
    @staticmethod
    def hide_cursor():
        print('\033[?25l', end='', flush=True)
    
    @staticmethod
    def show_cursor():
        print('\033[?25h', end='', flush=True)

    @classmethod
    def typewriter(cls, text, delay=0.05, gradient_name=None):
        cls.hide_cursor()
        try:
            for i in range(len(text) + 1):
                cls.clear_line()
                current_text = text[:i]
                if gradient_name and gradient_name in CustomGradients.GRADIENTS:
                    colored_text = CustomGradients.get(gradient_name, current_text)
                    print(colored_text, end='', flush=True)
                else:
                    print(current_text, end='', flush=True)
                time.sleep(delay)
            print()
        finally:
            cls.show_cursor()

    @classmethod
    def wave_animation(cls, text, cycles=3, delay=0.1, gradient_name="ocean"):
        cls.hide_cursor()
        try:
            for cycle in range(cycles):
                for offset in range(len(text)):
                    cls.clear_line()
                    animated_text = ""
                    for i, char in enumerate(text):
                        if (i + offset) % 4 == 0:
                            animated_text += char.upper()
                        else:
                            animated_text += char.lower()
                    
                    if gradient_name and gradient_name in CustomGradients.GRADIENTS:
                        colored_text = CustomGradients.get(gradient_name, animated_text)
                        print(colored_text, end='', flush=True)
                    else:
                        print(animated_text, end='', flush=True)
                    time.sleep(delay)
            print()
        finally:
            cls.show_cursor()

    @classmethod
    def rainbow_cycle(cls, text, cycles=5, delay=0.2):
        cls.hide_cursor()
        rainbow_gradients = ["red_to_blue", "fire", "sunset", "ocean", "forest", "cyberpunk"]
        try:
            for cycle in range(cycles):
                for gradient_name in rainbow_gradients:
                    cls.clear_line()
                    colored_text = CustomGradients.get(gradient_name, text)
                    print(colored_text, end='', flush=True)
                    time.sleep(delay)
            print()
        finally:
            cls.show_cursor()

    @classmethod
    def blink(cls, text, blinks=5, delay=0.5, gradient_name=None):
        cls.hide_cursor()
        try:
            for _ in range(blinks):
                if gradient_name and gradient_name in CustomGradients.GRADIENTS:
                    colored_text = CustomGradients.get(gradient_name, text)
                    print(colored_text, end='', flush=True)
                else:
                    print(text, end='', flush=True)
                time.sleep(delay)
                
                cls.clear_line()
                time.sleep(delay)
            
            if gradient_name and gradient_name in CustomGradients.GRADIENTS:
                colored_text = CustomGradients.get(gradient_name, text)
                print(colored_text)
            else:
                print(text)
        finally:
            cls.show_cursor()

    @classmethod
    def slide_in(cls, text, direction="left", delay=0.05, gradient_name=None):
        cls.hide_cursor()
        try:
            text_len = len(text)
            
            if direction == "left":
                for i in range(text_len + 1):
                    cls.clear_line()
                    spaces = " " * (text_len - i)
                    current_text = spaces + text[:i]
                    
                    if gradient_name and gradient_name in CustomGradients.GRADIENTS:
                        colored_text = CustomGradients.get(gradient_name, current_text)
                        print(colored_text, end='', flush=True)
                    else:
                        print(current_text, end='', flush=True)
                    time.sleep(delay)
                    
            elif direction == "right":
                for i in range(text_len + 1):
                    cls.clear_line()
                    current_text = text[-i:] if i > 0 else ""
                    spaces = " " * (text_len - len(current_text))
                    display_text = current_text + spaces
                    
                    if gradient_name and gradient_name in CustomGradients.GRADIENTS:
                        colored_text = CustomGradients.get(gradient_name, display_text)
                        print(colored_text, end='', flush=True)
                    else:
                        print(display_text, end='', flush=True)
                    time.sleep(delay)
            print()
        finally:
            cls.show_cursor()

    @classmethod
    def matrix_rain(cls, text, duration=3, gradient_name="matrix"):
        cls.hide_cursor()
        try:
            chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            iterations = int(duration / 0.1)
            
            for _ in range(iterations):
                cls.clear_line()
                random_text = ''.join(random.choice(chars) for _ in range(len(text)))
                
                if gradient_name and gradient_name in CustomGradients.GRADIENTS:
                    colored_text = CustomGradients.get(gradient_name, random_text)
                    print(colored_text, end='', flush=True)
                else:
                    print(random_text, end='', flush=True)
                time.sleep(0.1)
            
            cls.clear_line()
            if gradient_name and gradient_name in CustomGradients.GRADIENTS:
                final_text = CustomGradients.get(gradient_name, text)
                print(final_text)
            else:
                print(text)
                
        finally:
            cls.show_cursor()


class Effects:
    """Additional text effects and styling utilities"""
    
    @staticmethod
    def shadow(text, gradient_name="black_to_white", offset=2):
        lines = text.split('\n')
        result = []
        
        for line in lines:
            shadow_line = ' ' * offset + '░' * len(line)
            result.append(shadow_line)
        
        for i, line in enumerate(lines):
            if gradient_name and gradient_name in CustomGradients.GRADIENTS:
                colored_line = CustomGradients.get(gradient_name, line)
                result[i] = colored_line + '\n' + result[i]
            else:
                result[i] = line + '\n' + result[i]
        
        return '\n'.join(result)
    
    @staticmethod
    def outline(text, gradient_name="white_to_black", char='█'):
        lines = text.split('\n')
        if not lines:
            return text
        
        max_len = max(len(line) for line in lines)
        
        top_border = char * (max_len + 4)
        
        content_lines = []
        for line in lines:
            padded_line = line.ljust(max_len)
            if gradient_name and gradient_name in CustomGradients.GRADIENTS:
                colored_line = CustomGradients.get(gradient_name, padded_line)
                content_lines.append(f"{char} {colored_line} {char}")
            else:
                content_lines.append(f"{char} {padded_line} {char}")
        
        bottom_border = char * (max_len + 4)
        
        return top_border + '\n' + '\n'.join(content_lines) + '\n' + bottom_border
    
    @staticmethod
    def glow(text, gradient_name="neon_blue", intensity=3):
        if gradient_name not in CustomGradients.GRADIENTS:
            return text
        
        result = []
        colors = CustomGradients.GRADIENTS[gradient_name]
        
        for layer in range(intensity, 0, -1):
            spaces = ' ' * layer
            layer_text = spaces + text + spaces
            if len(colors) > 1:
                layer_color = colors[-1] if layer == 1 else colors[0]
                faded_color = tuple(int(c * (0.3 + 0.7 * (intensity - layer) / intensity)) for c in layer_color)
                layer_gradient = [faded_color, layer_color] if layer > 1 else colors
                colored_layer = CustomGradients.horizontal(layer_gradient, layer_text)
                result.append(colored_layer)
        
        main_text = CustomGradients.get(gradient_name, text)
        return '\n'.join(result) + '\n' + main_text
    
    @staticmethod
    def box(text, gradient_name=None, title="", style="rounded"):
        if gradient_name and gradient_name in CustomGradients.GRADIENTS:
            rich_text = CustomGradients.to_rich_text(CustomGradients.GRADIENTS[gradient_name], text)
        else:
            rich_text = Text(text)
        
        box_style = Box.ROUNDED if style == "rounded" else Box.SQUARE
        panel = Panel(rich_text, title=title, box=box_style)
        
        with console.capture() as capture:
            console.print(panel)
        
        return capture.get()
    
    @classmethod
    def banner(cls, text, gradient_name="fire", width=60, char='='):
        lines = text.split('\n')
        max_len = max(len(line) for line in lines) if lines else 0
        banner_width = max(width, max_len + 4)
        
        top_border = char * banner_width
        
        content = []
        for line in lines:
            padding = (banner_width - len(line) - 2) // 2
            padded_line = f"{char}{' ' * padding}{line}{' ' * (banner_width - len(line) - padding - 2)}{char}"
            
            if gradient_name and gradient_name in CustomGradients.GRADIENTS:
                colored_line = CustomGradients.get(gradient_name, padded_line)
                content.append(colored_line)
            else:
                content.append(padded_line)
        
        bottom_border = char * banner_width
        
        return top_border + '\n' + '\n'.join(content) + '\n' + bottom_border


# Helper functions
def gradient(name, text, direction="horizontal"): 
    return CustomGradients.get(name, text, direction, rich=False)

def gradient_rich(name, text, direction="horizontal"): 
    return CustomGradients.get(name, text, direction, rich=True)

def animate(effect, text, **kwargs):
    if hasattr(Animations, effect):
        getattr(Animations, effect)(text, **kwargs)
    else:
        print(f"Animation '{effect}' not found. Available: typewriter, wave_animation, rainbow_cycle, blink, slide_in, matrix_rain")

# Auto-create direct-call functions for all gradients
def _register_gradient_functions():
    for name in CustomGradients.GRADIENTS.keys():
        globals()[name] = lambda text, n=name: gradient(n, text)
        globals()[f"{name}_rich"] = lambda text, n=name: gradient_rich(n, text)

_register_gradient_functions()

# Export everything for easy imports
__all__ = [
    'CustomGradients', 'Animations', 'Effects',
    'gradient', 'gradient_rich', 'animate', 'console'
] + list(CustomGradients.GRADIENTS.keys()) + [f"{name}_rich" for name in CustomGradients.GRADIENTS.keys()]