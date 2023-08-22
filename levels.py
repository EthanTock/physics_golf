from game_assets.wall_box import WallBox
from game_assets.button import Button
from level import Level

# DEBUG = Level(
#     name="debug",
#     colorset="neon_city",
#     unnamed_wall_boxes=[
#         WallBox((2, 2), (3, 20))
#     ],
#     named_wall_boxes={
#         "w0": WallBox((10, 10), (7, 9), "w0", "horizontal")
#     },
#     buttons={
#         Button((5, 5), (2, 2), "b0", action=print, action_args=["this is a Button. "], action_kwargs={"end": "dear God.\n"})
#     },
#     start_point=(150, 150),
#     hole=(500, 200)
# )
EMPTY = Level(
    name="empty",
    colorset="grayscale",
    start_point=(0, 0),
)

LEVELS = {
    # DEBUG.name: DEBUG,
    EMPTY.name: EMPTY
}
