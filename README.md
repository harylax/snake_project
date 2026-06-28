# Snake Project

A simple Snake game written in Python using the MiniLibX Python bindings.

## Features

* Classic Snake gameplay
* Random apple generation
* Score display
* Game Over screen
* Restart the game by pressing **Enter**

## Requirements

* Python 3
* MiniLibX Python wheel (`mlx-2.2-py3-none-any.whl`)

## Installation

```bash
make install
```

## Run

```bash
make run
```

## Controls

* **↑** : Move up
* **↓** : Move down
* **←** : Move left
* **→** : Move right
* **Enter** : Restart after Game Over
* **Esc** : Quit the game

## Clean

Remove cache files:

```bash
make clean
```

Remove the virtual environment:

```bash
make fclean
```

## Project Structure

```
.
├── snake.py
├── Makefile
├── mlx-2.2-py3-none-any.whl
└── README.md
```
