"""
fix_sprites.py — Remove checkerboard backgrounds and add outlines to character sprites.

Uses flood-fill from image edges to detect and remove the checkerboard
transparency pattern that AI generators bake into images, then adds a
subtle outline so characters pop on any background.

Usage:  python fix_sprites.py
  (run from the EchoesOfSpring folder)
"""

from PIL import Image, ImageFilter, ImageChops
import os
from collections import deque

SPRITES_DIR = os.path.join("game", "images")
OUTLINE_COLOR = (40, 20, 60, 200)   # Dark purple, slightly transparent
OUTLINE_WIDTH = 3                    # Pixels of outline thickness

SPRITE_FILES = [
    "sakura happy.png",
    "sakura neutral.png",
    "sakura sad.png",
    "sakura surprise.png",
    "akira neutral.png",
    "akira happy.png",
    "akira sad.png",
    "akira surprise.png",
]

# Checkerboard block size (typically 8, 16, or 32 px in editors)
BLOCK_SIZES = [8, 10, 12, 16, 20, 24, 32]

FLOOD_TOLERANCE = 60     # How different a neighbour can be before we stop
CHECKER_TOLERANCE = 45   # Max diff between the two checkerboard colours
EDGE_SAMPLE = 0.05       # Sample 5% of edge pixels to detect checker colours


def color_dist(c1, c2):
    """Euclidean RGB distance."""
    return sum((a - b) ** 2 for a, b in zip(c1[:3], c2[:3])) ** 0.5


def detect_checker_colors(img):
    """Sample edge pixels to find the two dominant checkerboard colours."""
    w, h = img.size
    pixels = img.load()
    edge_pixels = []

    # Gather pixels from all 4 edges
    for x in range(w):
        edge_pixels.append(pixels[x, 0][:3])
        edge_pixels.append(pixels[x, h - 1][:3])
    for y in range(h):
        edge_pixels.append(pixels[0, y][:3])
        edge_pixels.append(pixels[w - 1, y][:3])

    # Find two most common colour clusters
    # Bucket by rounding to nearest 16
    buckets = {}
    for rgb in edge_pixels:
        key = (rgb[0] // 16, rgb[1] // 16, rgb[2] // 16)
        if key not in buckets:
            buckets[key] = []
        buckets[key].append(rgb)

    # Sort buckets by count, take top 2
    sorted_buckets = sorted(buckets.items(), key=lambda x: -len(x[1]))

    colors = []
    for key, pxs in sorted_buckets[:2]:
        avg = tuple(sum(c) // len(pxs) for c in zip(*pxs))
        colors.append(avg)

    if len(colors) < 2:
        colors.append(colors[0])

    return colors


def is_checker_like(r, g, b, checker_colors):
    """Check if a pixel matches either checkerboard colour."""
    rgb = (r, g, b)
    for cc in checker_colors:
        if color_dist(rgb, cc) < CHECKER_TOLERANCE:
            return True
    # Also catch generic grey/white checkerboard
    saturation = max(r, g, b) - min(r, g, b)
    if saturation < 30 and min(r, g, b) > 160:
        return True
    return False


def remove_checkerboard(img):
    """
    Flood-fill from all edges to remove the checkerboard background.
    Any pixel reachable from the edge that looks like the checker pattern
    gets made transparent.
    """
    img = img.convert("RGBA")
    w, h = img.size
    pixels = img.load()

    checker_colors = detect_checker_colors(img)
    print(f"    Detected checker colours: {checker_colors}")

    # Build a visited/transparent mask
    to_clear = set()
    visited = set()

    # Seed from all edge pixels that match the checker pattern
    queue = deque()
    for x in range(w):
        for y in [0, h - 1]:
            r, g, b, a = pixels[x, y]
            if is_checker_like(r, g, b, checker_colors):
                queue.append((x, y))
                visited.add((x, y))
    for y in range(h):
        for x in [0, w - 1]:
            if (x, y) not in visited:
                r, g, b, a = pixels[x, y]
                if is_checker_like(r, g, b, checker_colors):
                    queue.append((x, y))
                    visited.add((x, y))

    # BFS flood fill
    while queue:
        cx, cy = queue.popleft()
        to_clear.add((cx, cy))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                visited.add((nx, ny))
                r, g, b, a = pixels[nx, ny]
                if is_checker_like(r, g, b, checker_colors):
                    queue.append((nx, ny))

    # Clear all background pixels
    for (x, y) in to_clear:
        pixels[x, y] = (0, 0, 0, 0)

    # Clean up stray semi-transparent edge pixels (anti-alias the boundary)
    # Do a second pass: any remaining pixel where 3+ of 4 neighbours are transparent
    for y in range(h):
        for x in range(w):
            if (x, y) in to_clear:
                continue
            r, g, b, a = pixels[x, y]
            if a == 0:
                continue
            transparent_neighbours = 0
            total_neighbours = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1),
                           (-1, -1), (1, -1), (-1, 1), (1, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h:
                    total_neighbours += 1
                    if pixels[nx, ny][3] == 0:
                        transparent_neighbours += 1
            # If mostly surrounded by transparency and looks greyish, remove
            if total_neighbours > 0 and transparent_neighbours >= total_neighbours * 0.6:
                saturation = max(r, g, b) - min(r, g, b)
                if saturation < 40:
                    pixels[x, y] = (0, 0, 0, 0)

    print(f"    Cleared {len(to_clear)} background pixels")
    return img


def add_outline(img, color=OUTLINE_COLOR, width=OUTLINE_WIDTH):
    """Add a coloured outline around non-transparent pixels."""
    alpha = img.split()[3]

    dilated = alpha
    for _ in range(width):
        dilated = dilated.filter(ImageFilter.MaxFilter(3))

    outline_mask = ImageChops.subtract(dilated, alpha)

    outline_layer = Image.new("RGBA", img.size, color)
    outline_layer.putalpha(outline_mask)

    result = Image.new("RGBA", img.size, (0, 0, 0, 0))
    result = Image.alpha_composite(result, outline_layer)
    result = Image.alpha_composite(result, img)

    return result


def process_sprite(filepath):
    """Full pipeline: remove checkerboard → add outline → save."""
    print(f"  Processing: {os.path.basename(filepath)}")
    img = Image.open(filepath)
    img = remove_checkerboard(img)
    img = add_outline(img)
    img.save(filepath)
    print(f"    ✓ Saved ({img.size[0]}x{img.size[1]})")


def main():
    print("=" * 55)
    print("Sprite Fixer v2 — Flood-fill background removal")
    print("=" * 55)

    for name in SPRITE_FILES:
        path = os.path.join(SPRITES_DIR, name)
        if os.path.exists(path):
            process_sprite(path)
        else:
            print(f"  ⚠ Not found: {path}")

    print("\nDone! All sprites cleaned up.")


if __name__ == "__main__":
    main()
