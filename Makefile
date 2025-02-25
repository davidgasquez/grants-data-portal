.DEFAULT_GOAL := all

.PHONY: .uv
.uv:
	@uv --version || echo 'Please install uv: https://docs.astral.sh/uv/getting-started/installation/'

.PHONY: install
install: .uv
	uv sync --frozen

.PHONY: dev
dev:
	uv run dagster dev
