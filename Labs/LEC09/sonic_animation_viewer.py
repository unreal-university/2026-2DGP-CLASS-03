"""LEC09: play every Sonic animation from the sprite sheet."""

from pathlib import Path
from typing import NamedTuple

from pico2d import (
    SDL_KEYDOWN,
    SDL_QUIT,
    SDLK_ESCAPE,
    close_canvas,
    get_events,
    load_image,
    open_canvas,
)


CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
SPRITE_PATH = Path(__file__).with_name("sonic-sprite.png")


class Frame(NamedTuple):
    """A crop rectangle measured from the sheet's top-left corner."""

    x: int
    y: int
    width: int
    height: int

    def bottom(self, image_height: int) -> int:
        return image_height - self.y - self.height


FIRST_FRAME = Frame(1, 39, 29, 39)


def main():
    if not SPRITE_PATH.is_file():
        raise FileNotFoundError(f"스프라이트 시트를 찾을 수 없습니다: {SPRITE_PATH}")

    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sprite = load_image(str(SPRITE_PATH))
        running = True
        while running:
            for event in get_events():
                if event.type == SDL_QUIT or (
                    event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
                ):
                    running = False
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
