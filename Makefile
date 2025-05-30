.DEFAULT_GOAL := all

.PHONY: .uv
.uv:
	@uv --version || echo 'Please install uv: https://docs.astral.sh/uv/getting-started/installation/'

.PHONY: setup
setup: .uv
	uv sync --frozen

.PHONY: dev
dev:
	uv run dg dev

.PHONY: run
run:
	uv run dg launch --assets '*'

.PHONY: web
web:
	uv run python -m http.server 8000 -d web
