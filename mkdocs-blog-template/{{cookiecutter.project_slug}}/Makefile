.PHONY: serve build clean help

serve:
	poetry run mkdocs serve

build:
	poetry run mkdocs build

clean:
	rm -rf site/

help:
	@echo "Available commands:"
	@echo "  make serve  - Start local development server"
	@echo "  make build  - Build static site"
	@echo "  make clean  - Remove built site files"
