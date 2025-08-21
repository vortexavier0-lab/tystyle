from tystyle import gradient, animate, Effects

# Simple gradient text
print(gradient("fire", "Hello World!"))
print(gradient("ocean", "Vertical gradient", direction="vertical"))

# Animations
animate("typewriter", "Typing effect...", delay=0.1)
animate("rainbow_cycle", "Rainbow colors!", cycles=3)

# Effects
print(Effects.glow("Glowing text", gradient_name="neon_blue"))
print(Effects.banner("WELCOME", gradient_name="cyberpunk"))