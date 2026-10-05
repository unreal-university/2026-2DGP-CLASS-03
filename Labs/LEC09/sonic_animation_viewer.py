"""LEC09: play every Sonic animation from the sprite sheet."""

from pathlib import Path

from pico2d import close_canvas, load_image, open_canvas


CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
SPRITE_PATH = Path(__file__).with_name("sonic-sprite.png")


def main():
    if not SPRITE_PATH.is_file():
        raise FileNotFoundError(f"스프라이트 시트를 찾을 수 없습니다: {SPRITE_PATH}")

    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sprite = load_image(str(SPRITE_PATH))
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
