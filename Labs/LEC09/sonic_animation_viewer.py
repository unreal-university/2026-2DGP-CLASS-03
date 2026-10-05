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
    Animation("2행 동작", (
        Frame(8, 80, 26, 37),
        Frame(37, 80, 27, 37),
        Frame(65, 80, 31, 38),
        Frame(97, 80, 37, 37),
        Frame(135, 80, 32, 35),
        Frame(170, 79, 32, 38),
        Frame(206, 79, 26, 38),
        Frame(238, 80, 24, 37),
        Frame(263, 80, 30, 37),
        Frame(295, 80, 36, 37),
        Frame(334, 80, 32, 36),
        Frame(370, 79, 29, 38),
    )),
    Animation("3행 동작", (
        Frame(1, 124, 33, 40),
        Frame(39, 124, 35, 39),
        Frame(89, 125, 35, 38),
        Frame(130, 121, 34, 42),
        Frame(181, 122, 34, 41),
        Frame(228, 122, 33, 40),
    )),
    Animation("4행 동작", (
        Frame(1, 169, 29, 30),
        Frame(35, 167, 29, 31),
        Frame(67, 169, 30, 29),
        Frame(98, 169, 31, 29),
        Frame(131, 168, 29, 30),
        Frame(162, 168, 29, 31),
        Frame(193, 170, 30, 29),
        Frame(230, 170, 31, 29),
        Frame(268, 170, 30, 30),
    )),
    Animation("5행 동작", (
        Frame(1, 206, 30, 27),
        Frame(36, 206, 29, 27),
        Frame(70, 206, 29, 27),
        Frame(105, 206, 29, 27),
        Frame(139, 206, 29, 27),
        Frame(174, 206, 29, 27),
    )),
    Animation("6행 동작", (
        Frame(1, 239, 29, 35),
        Frame(36, 239, 30, 35),
        Frame(74, 239, 31, 35),
        Frame(111, 238, 31, 36),
        Frame(149, 239, 30, 35),
        Frame(186, 238, 31, 36),
    )),
    Animation("7행 동작", (
        Frame(1, 283, 29, 35),
        Frame(36, 283, 30, 35),
        Frame(72, 286, 39, 31),
        Frame(123, 285, 39, 32),
        Frame(172, 286, 39, 31),
        Frame(218, 285, 38, 32),
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
