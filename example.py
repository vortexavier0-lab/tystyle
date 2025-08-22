#!/usr/bin/env python3
"""
TyStyle Complete Demo Script
Showcases all features of the beautiful terminal styling library
"""

# Import the TyStyle library (assuming it's saved as tystyle.py)
from tystyle import *
import time
import random

def demo_header():
    """Display the demo header"""
    print("\n" * 2)
    header_text = "🎨 TYSTYLE COMPLETE DEMO 🎨"
    print(gradient("fire", "=" * 60))
    print(gradient("rainbow", header_text.center(60)))
    print(gradient("fire", "=" * 60))
    print(gradient("cyberpunk", "Beautiful terminal styling with gradients and animations".center(60)))
    print(gradient("fire", "=" * 60))
    print()

def demo_basic_gradients():
    """Demonstrate basic gradient functionality"""
    print(gradient("neon_blue", "\n🌈 BASIC GRADIENTS SHOWCASE"))
    print(gradient("silver", "-" * 40))
    
    sample_text = "Beautiful Gradient Text!"
    
    # Showcase various gradient categories
    categories = {
        "🔥 Fire/Warm": ["fire", "sunset", "lava", "ember", "inferno"],
        "🌊 Ocean/Cool": ["ocean", "ice", "arctic", "glacier", "frozen"],
        "🌿 Nature": ["forest", "jungle", "spring", "autumn", "meadow"],
        "⚡ Neon/Cyber": ["cyberpunk", "matrix", "synthwave", "electric", "holographic"],
        "🌈 Rainbow": ["rainbow", "pride", "vibrant_rainbow", "pastel_rainbow"],
        "💎 Gemstones": ["ruby", "emerald", "sapphire", "diamond", "amethyst"]
    }
    
    for category, gradients in categories.items():
        print(f"\n{gradient('gold', category)}")
        for grad_name in gradients:
            print(f"  {grad_name:15}: {gradient(grad_name, sample_text)}")
    
    time.sleep(2)

def demo_gradient_directions():
    """Demonstrate different gradient directions"""
    print(gradient("aurora", "\n🧭 GRADIENT DIRECTIONS"))
    print(gradient("silver", "-" * 40))
    
    multiline_text = """MULTI-LINE
GRADIENT
DEMO TEXT"""
    
    directions = [
        ("horizontal", "➡️ Horizontal"),
        ("vertical", "⬇️ Vertical"), 
        ("diagonal", "↘️ Diagonal"),
        ("radial", "🎯 Radial")
    ]
    
    for direction, label in directions:
        print(f"\n{gradient('neon_pink', label)}:")
        print(CustomGradients.get("sunset", multiline_text, direction))
        time.sleep(1.5)

def demo_animations():
    """Demonstrate various animation effects"""
    print(gradient("lightning", "\n⚡ ANIMATION SHOWCASE"))
    print(gradient("silver", "-" * 40))
    
    animations_to_demo = [
        ("typewriter", "Typewriter Effect", {"delay": 0.08, "gradient_name": "matrix"}),
        ("wave_animation", "Wave Animation", {"cycles": 2, "delay": 0.1, "gradient_name": "ocean"}),
        ("color_wave", "Color Wave", {"cycles": 2, "delay": 0.08, "gradient_name": "rainbow"}),
        ("rainbow_cycle", "Rainbow Cycle", {"cycles": 2, "delay": 0.3}),
        ("blink", "Blink Effect", {"blinks": 3, "delay": 0.4, "gradient_name": "neon_blue"}),
        ("slide_in", "Slide In", {"direction": "left", "delay": 0.05, "gradient_name": "cyberpunk"}),
        ("matrix_rain", "Matrix Rain", {"duration": 2, "gradient_name": "matrix"}),
        ("pulse", "Pulse Effect", {"pulses": 3, "delay": 0.4, "gradient_name": "neon_pink"}),
        ("sparkle", "Sparkle Effect", {"duration": 2, "gradient_name": "gold"}),
        ("zoom_in", "Zoom In", {"steps": 8, "delay": 0.1, "gradient_name": "fire"}),
        ("falling_letters", "Falling Letters", {"delay": 0.15, "gradient_name": "blue_shades"}),
        ("neon_flicker", "Neon Flicker", {"flickers": 8, "gradient_name": "neon_green"})
    ]
    
    for anim_name, description, kwargs in animations_to_demo:
        print(f"\n{gradient('gold', f'🎭 {description}:')}")
        animate(anim_name, "ANIMATED TEXT DEMO!", **kwargs)
        time.sleep(1)

def demo_effects():
    """Demonstrate visual effects"""
    print(gradient("plasma", "\n✨ VISUAL EFFECTS SHOWCASE"))
    print(gradient("silver", "-" * 40))
    
    demo_text = "STYLED TEXT"
    
    effects_to_demo = [
        ("shadow", "Shadow Effect", {"gradient_name": "blue_shades", "offset": 2}),
        ("outline", "Outline Effect", {"gradient_name": "gold", "char": "█"}),
        ("glow", "Glow Effect", {"gradient_name": "neon_pink", "intensity": 3}),
        ("banner", "Banner Effect", {"gradient_name": "cyberpunk", "width": 50}),
        ("double_vision", "Double Vision", {"gradient_name1": "red_shades", "gradient_name2": "blue_shades"}),
        ("mirror", "Mirror Effect", {"gradient_name": "silver", "vertical": False}),
        ("pixelate", "Pixelate Effect", {"gradient_name": "retro_neon"}),
        ("emboss", "Emboss Effect", {"gradient_name": "silver"}),
        ("distort", "Distort Effect", {"gradient_name": "cyberpunk", "intensity": 2})
    ]
    
    for effect_name, description, kwargs in effects_to_demo:
        print(f"\n{gradient('aurora', f'🎨 {description}:')}")
        result = effect(effect_name, demo_text, **kwargs)
        print(result)
        time.sleep(2)

def demo_patterns():
    """Demonstrate pattern effects"""
    print(gradient("galaxy", "\n🎯 PATTERN EFFECTS"))
    print(gradient("silver", "-" * 40))
    
    pattern_text = "PATTERN DEMO TEXT"
    
    patterns_to_demo = [
        ("checkerboard", "Checkerboard Pattern", {
            "gradient_name1": "black_to_white", 
            "gradient_name2": "white_to_black", 
            "size": 2
        }),
        ("zebra_stripes", "Zebra Stripes", {
            "gradient_name1": "black_to_white", 
            "gradient_name2": "gold"
        }),
        ("wave_pattern", "Wave Pattern", {
            "gradient_name": "ocean", 
            "frequency": 2
        })
    ]
    
    for pattern_name, description, kwargs in patterns_to_demo:
        print(f"\n{gradient('neon_blue', f'🌊 {description}:')}")
        result = pattern(pattern_name, pattern_text, **kwargs)
        print(result)
        time.sleep(2)

def demo_animated_patterns():
    """Demonstrate animated patterns"""
    print(gradient("holographic", "\n🌀 ANIMATED PATTERNS"))
    print(gradient("silver", "-" * 40))
    
    print(f"\n{gradient('cosmic', '💨 Breathing Text:')}")
    animate("breathing_text", "BREATHING DEMO", cycles=2, gradient_name="calm", delay=0.08)
    
    print(f"\n{gradient('cosmic', '🌀 Spiral Reveal:')}")
    spiral_text = "SPIRAL\nREVEAL\nDEMO"
    animate("spiral_reveal", spiral_text, delay=0.05, gradient_name="galaxy")

def demo_text_art():
    """Demonstrate text art utilities"""
    print(gradient("diamond", "\n🎨 TEXT ART UTILITIES"))
    print(gradient("silver", "-" * 40))
    
    art_text = "TEXT ART"
    
    # Borders
    print(f"\n{gradient('gold', '📦 Border Styles:')}")
    border_styles = ["single", "double", "rounded", "thick", "dotted"]
    for style in border_styles:
        print(f"\n{style.capitalize()} Border:")
        bordered = TextArt.create_border(f"{style.upper()} BORDER", style, "silver")
        print(bordered)
        time.sleep(1)
    
    # Title
    print(f"\n{gradient('gold', '👑 Fancy Title:')}")
    title = TextArt.create_title("AMAZING TITLE", "gold", 50)
    print(title)
    
    # Progress bars
    print(f"\n{gradient('gold', '📊 Progress Bars:')}")
    for i in range(0, 101, 20):
        bar = TextArt.progress_bar(i, 30, "green_shades")
        print(f"Progress: {bar}")
        time.sleep(0.3)

def demo_interactive_effects():
    """Demonstrate interactive effects"""
    print(gradient("electric", "\n⚡ INTERACTIVE EFFECTS"))
    print(gradient("silver", "-" * 40))
    
    print(f"\n{gradient('matrix', '⌨️ Typing Effect:')}")
    InteractiveEffects.typing_effect("Hello, this is a typing effect!", "matrix", 0.08)
    
    print(f"\n{gradient('fire', '⏱️ Countdown Timer:')}")
    InteractiveEffects.countdown(5, "fire", "Launch in:")

def demo_utility_functions():
    """Demonstrate utility functions"""
    print(gradient("cosmic", "\n🛠️ UTILITY FUNCTIONS"))
    print(gradient("silver", "-" * 40))
    
    demo_text = "UTILITY DEMO"
    
    print(f"\n{gradient('aurora', '🎲 Random Gradient:')}")
    for _ in range(5):
        print(random_gradient(demo_text))
        time.sleep(0.5)
    
    print(f"\n{gradient('aurora', '🎨 Blend Gradients:')}")
    blended = blend_gradients("fire", "ocean", demo_text, 0.5)
    print(f"Fire + Ocean: {blended}")
    
    print(f"\n{gradient('aurora', '⚡ Quick Gradient:')}")
    custom_colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255)]
    quick_grad = quick_gradient(demo_text, custom_colors)
    print(f"Custom colors: {quick_grad}")

def demo_rich_integration():
    """Demonstrate Rich library integration"""
    print(gradient("holographic", "\n📚 RICH INTEGRATION"))
    print(gradient("silver", "-" * 40))
    
    # Rich text examples
    rich_text = gradient_rich("sunset", "This text uses Rich formatting!")
    console.print(f"\nRich gradient: {rich_text}")
    
    # Rich panels and effects
    demo_text = "Rich Integration Demo"
    boxed = effect("box", demo_text, gradient_name="cyberpunk", title="Demo Box", style="rounded")
    print(f"\nRich Box Effect:")
    print(boxed)

def demo_comprehensive_showcase():
    """A comprehensive showcase combining multiple effects"""
    print(gradient("rainbow", "\n🎪 COMPREHENSIVE SHOWCASE"))
    print(gradient("silver", "-" * 50))
    
    # Create a complex demo
    title = "TYSTYLE MASTER DEMO"
    
    print(f"\n{gradient('fire', '🚀 Complex Animation Sequence:')}")
    
    # Step 1: Typewriter with matrix theme
    animate("typewriter", "Initializing TyStyle...", delay=0.05, gradient_name="matrix")
    
    # Step 2: Loading with sparkles
    animate("sparkle", "Loading effects...", duration=2, gradient_name="gold")
    
    # Step 3: Main title with glow
    glowing_title = effect("glow", title, gradient_name="neon_blue", intensity=3)
    print(f"\n{glowing_title}")
    
    # Step 4: Animated showcase
    animate("rainbow_cycle", "SUCCESS! All systems operational!", cycles=2)
    
    # Step 5: Final banner
    final_banner = effect("banner", "DEMO COMPLETE", gradient_name="holographic", width=60)
    print(f"\n{final_banner}")

def interactive_menu():
    """Interactive demo menu"""
    while True:
        print(gradient("aurora", "\n🎮 INTERACTIVE DEMO MENU"))
        print(gradient("silver", "-" * 40))
        
        options = [
            ("1", "Basic Gradients", demo_basic_gradients),
            ("2", "Gradient Directions", demo_gradient_directions),
            ("3", "Animations", demo_animations),
            ("4", "Visual Effects", demo_effects),
            ("5", "Pattern Effects", demo_patterns),
            ("6", "Animated Patterns", demo_animated_patterns),
            ("7", "Text Art", demo_text_art),
            ("8", "Interactive Effects", demo_interactive_effects),
            ("9", "Utility Functions", demo_utility_functions),
            ("10", "Rich Integration", demo_rich_integration),
            ("11", "Comprehensive Showcase", demo_comprehensive_showcase),
            ("12", "List All Gradients", list_gradients),
            ("13", "Built-in Demo", demo),
            ("0", "Exit", None)
        ]
        
        for key, description, _ in options:
            option_text = f"{key}. {description}"
            print(gradient("neon_green" if key != "0" else "red_shades", option_text))
        
        try:
            choice = input(f"\n{gradient('gold', 'Select option (0-13): ')}")
            
            if choice == "0":
                print(gradient("fire", "\n👋 Thanks for using TyStyle! Goodbye!"))
                break
            
            # Find and execute the selected option
            selected_option = next((opt for opt in options if opt[0] == choice), None)
            if selected_option and selected_option[2]:
                print("\n" + "="*60)
                selected_option[2]()
                print("\n" + "="*60)
                input(gradient("aurora", "\nPress Enter to continue..."))
            elif choice == "12":
                list_gradients()
                input(gradient("aurora", "\nPress Enter to continue..."))
            elif choice == "13":
                demo()
                input(gradient("aurora", "\nPress Enter to continue..."))
            else:
                print(gradient("red_shades", "Invalid option! Please try again."))
                
        except KeyboardInterrupt:
            print(gradient("fire", "\n\n👋 Demo interrupted. Goodbye!"))
            break
        except Exception as e:
            print(gradient("red_shades", f"\nError: {e}"))

def main():
    """Main demo function"""
    try:
        # Show header
        demo_header()
        
        # Ask user for demo type
        print(gradient("neon_blue", "Choose demo mode:"))
        print(gradient("gold", "1. Full Automatic Demo"))
        print(gradient("gold", "2. Interactive Menu"))
        print(gradient("gold", "3. Quick Showcase"))
        
        choice = input(gradient("aurora", "\nEnter choice (1-3): "))
        
        if choice == "1":
            # Full automatic demo
            print(gradient("fire", "\n🎬 Starting Full Automatic Demo...\n"))
            demo_basic_gradients()
            demo_gradient_directions() 
            demo_animations()
            demo_effects()
            demo_patterns()
            demo_animated_patterns()
            demo_text_art()
            demo_interactive_effects()
            demo_utility_functions()
            demo_rich_integration()
            demo_comprehensive_showcase()
            
        elif choice == "2":
            # Interactive menu
            interactive_menu()
            
        elif choice == "3":
            # Quick showcase
            print(gradient("cyberpunk", "\n⚡ Quick Showcase Mode\n"))
            demo_basic_gradients()
            demo_animations()
            demo_effects()
            demo_comprehensive_showcase()
            
        else:
            print(gradient("red_shades", "Invalid choice, starting quick showcase..."))
            demo_basic_gradients()
            demo_comprehensive_showcase()
        
        # Closing message
        closing_text = "🎨 Thanks for exploring TyStyle! 🎨"
        animate("rainbow_cycle", closing_text, cycles=2)
        
    except KeyboardInterrupt:
        print(gradient("fire", "\n\n👋 Demo interrupted. Goodbye!"))
    except Exception as e:
        print(gradient("red_shades", f"\nDemo error: {e}"))
        print(gradient("gold", "Make sure you have the TyStyle library (tystyle.py) in the same directory!"))

if __name__ == "__main__":
    main()
