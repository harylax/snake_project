from mlx import Mlx
import time


mlx = Mlx()
mlx_ptr = mlx.mlx_init()
win_ptr = mlx.mlx_new_window(mlx_ptr, 800, 600, 'Snake Project')
cell_size = 10
width = 800 // 10
height = 600 // 10


def draw_rect(x, y, w, h, color) -> None:
    for j in range(y, y + h):
        for i in range(x, x + w):
            mlx.mlx_pixel_put(mlx_ptr, win_ptr, i, j, color)


def draw_cell(pos: tuple[int, int], color: int) -> None:
    x, y = pos
    draw_rect(x * cell_size, y * cell_size, cell_size, cell_size, color)


class Snake:
    def __init__(self) -> None:
        self.position: tuple[int, int] = (width // 2, height // 2)
        self.running: bool = True
        self.direction: tuple[int, int] = (1, 0)

    def draw_snake(self) -> None:
        draw_cell(self.position, 0xFF00FF55)

    def animate(self, _) -> None:
        if not self.running:
            mlx.mlx_string_put(mlx_ptr, win_ptr, 365, 290, 0xFFFFFFFF, "GAME OVER")
            return
        mlx.mlx_clear_window(mlx_ptr, win_ptr)
        self.draw_snake()
        x, y = self.position
        dx, dy = self.direction
        nx, ny = x + dx, y + dy
        if not (0 <= nx < width and 0 <= ny < height):
            self.running = False
        self.position = nx, ny
        time.sleep(0.05)

    def key_hook(self, keycode: int, _) -> None:
        if keycode == 65307:
            mlx.mlx_loop_exit(mlx_ptr)
            return

        if keycode == 65361:
            self.direction = (-1, 0)
        if keycode == 65362:
            self.direction = (0, -1)
        if keycode == 65363:
            self.direction = (1, 0)
        if keycode == 65364:
            self.direction = (0, 1)

        if keycode == 65293:
            if self.running:
                return
            mlx.mlx_loop_hook(mlx_ptr, None, None)
            mlx.mlx_clear_window(mlx_ptr, win_ptr)
            self.position = width // 2, height // 2
            self.running = True
            mlx.mlx_loop_hook(mlx_ptr, self.animate, None)


def close_hook(_) -> None:
    mlx.mlx_loop_exit(mlx_ptr)


def run() -> None:
    snake = Snake()
    mlx.mlx_hook(win_ptr, 33, 0, close_hook, None)
    mlx.mlx_loop_hook(mlx_ptr, snake.animate, None)
    mlx.mlx_key_hook(win_ptr, snake.key_hook, None)
    mlx.mlx_loop(mlx_ptr)


def main() -> None:
    run()


if __name__ == "__main__":
    main()
