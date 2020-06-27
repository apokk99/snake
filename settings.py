class Settings:
    def __init__(self):
        # screen_width and screen_height must be multiple of 2 * cube_side
        self.screen_width = 600
        self.screen_height = 400
        self.cube_side = 20

        self.columns = self.screen_width // self.cube_side
        self.rows = self.screen_height // self.cube_side
        self.total_cubes = self.columns * self.rows

        self.bg_color = (230, 230, 230)
        self.grid_color = (210, 210, 210)
        self.head_color = (38, 128, 62)
        self.apple_color = (163, 46, 50)
        self.part_color = (46, 184, 64)

    # Get every possible coordinate on map
    def get_map_coord(self):
        map_coords = []
        for x in range(0, self.screen_width, self.cube_side):
            for y in range(0, self.screen_height, self.cube_side):
                map_coords.append((x, y))
        return map_coords