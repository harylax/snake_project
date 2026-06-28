.PHONY: install, run, clean, fclean

venv/.installed:
	python3 -m venv venv
	venv/bin/pip install mlx-2.2-py3-none-any.whl
	touch venv/.installed

install: venv/.installed

run:
	venv/bin/python3 snake.py

clean:
	rm -rf .mypy_cache

fclean: clean
	rm -rf venv
