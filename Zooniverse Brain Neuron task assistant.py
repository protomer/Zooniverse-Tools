import pyautogui
import time

# === CONFIGURE THESE VALUES ===
TARGET_COLOR = (191, 191, 191)        # RGB color to find (e.g., grey)
# Or convert hex to RGB: #FF0000 -> (255, 0, 0)
REGION = (100, 100, 800, 600)     # (x, y, width, height) - region to search
CLICK_OFFSET = (0, 0)             # Optional: offset from detected pixel
SLEEP_DURATION = 1                # seconds between checks
# ===============================

def hex_to_rgb(hex_color):
    """Convert #RRGGBB to (R, G, B) tuple"""
    hex_color = hex_color.lstrip('#')  # Fixed lstrip
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Optional: Use hex string instead of RGB
# TARGET_COLOR = hex_to_rgb("#FF00FF")  # Example: magenta

print("Starting color detection script...")
time.sleep(1)
print(f"Looking for color {TARGET_COLOR} in region {REGION}")
print("Press Ctrl+C to stop.")

clicked_positions = set()

try:
    while True:
        # Take screenshot of the region
        screenshot = pyautogui.screenshot(region=REGION)
        
        # Get region coordinates
        left, top, width, height = REGION
        
        found = False
        for x in range(width):
            for y in range(height):
                pixel = screenshot.getpixel((x, y))
                if pixel == TARGET_COLOR:
                    # Convert local coords to screen coords
                    screen_x = left + x + CLICK_OFFSET[0]
                    screen_y = top + y + CLICK_OFFSET[1]
                    click_pos = (screen_x, screen_y)
                    
                    if click_pos in clicked_positions:
                        continue
                    
                    print(f"Color found at {click_pos} - Clicking!")
                    pyautogui.click(screen_x, screen_y)
                    clicked_positions.add(click_pos)
                    found = True
                    break  # Stop after first new match
            if found:
                break
        
        if not found:
            print(f"Color {TARGET_COLOR} not found in region or all positions already clicked. Retrying in {SLEEP_DURATION} seconds...")
        
        time.sleep(SLEEP_DURATION)

except KeyboardInterrupt:
    print("\nScript stopped by user.")