"""LEC09: play every Sonic animation from the sprite sheet."""

from pathlib import Path
from typing import NamedTuple

from pico2d import (
    SDL_KEYDOWN,
    SDL_QUIT,
    SDLK_ESCAPE,
    clear_canvas,
    close_canvas,
    delay,
    get_events,
    load_image,
    open_canvas,
    update_canvas,
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


class Animation(NamedTuple):
    name: str
    frames: tuple[Frame, ...]


ANIMATIONS = (
    Animation("1행 동작", (
        Frame(1, 39, 29, 39),
        Frame(31, 40, 26, 38),
        Frame(58, 39, 29, 39),
        Frame(87, 40, 29, 38),
        Frame(118, 40, 30, 38),
        Frame(150, 40, 30, 38),
        Frame(182, 40, 30, 38),
        Frame(212, 39, 29, 38),
        Frame(241, 39, 28, 38),
        Frame(270, 45, 24, 32),
        Frame(302, 51, 29, 26),
    )),
    # 다음 동작
)


def draw_frame(sprite, frame: Frame) -> None:
    scale = 4
    sprite.clip_draw(
        frame.x,
        frame.bottom(sprite.h),
        frame.width,
        frame.height,
        CANVAS_WIDTH // 2,
        CANVAS_HEIGHT // 2,
        frame.width * scale,
        frame.height * scale,
    )


def main():
    if not SPRITE_PATH.is_file():
        raise FileNotFoundError(f"스프라이트 시트를 찾을 수 없습니다: {SPRITE_PATH}")

    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sprite = load_image(str(SPRITE_PATH))
        running = True
        while running:
            clear_canvas()
            draw_frame(sprite, FIRST_FRAME)
            update_canvas()
            for event in get_events():
                if event.type == SDL_QUIT or (
                    event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
                ):
                    running = False
            delay(1 / 60)
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
