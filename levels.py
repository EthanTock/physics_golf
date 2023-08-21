from game_assets.wall_box import WallBox
from game_assets.button import Button
from level import Level

LEVEL_1 = Level(
    name="1",
    colorset="neon_city",
    wall_boxes=[
        WallBox((2, 2), (3, 20))
    ],
    named_wall_boxes={
        "w0": WallBox((10, 10), (7, 9), "w0", "horizontal")
    },
    buttons={
        Button((5, 5), (2, 2), "b0", action=print, action_args=["this is a Button. "], action_kwargs={"end": "dear God.\n"})
    },
    start_point=(150, 150),
    end_point=(500, 200)
)
EDITOR = Level(
    name="editor",
    colorset="grayscale",
    start_point=(0, 0),
    end_point=(100, 100)  # TODO change this to a hole object...
)

LEVELS = {
    LEVEL_1.name: LEVEL_1,
    EDITOR.name: EDITOR
}
