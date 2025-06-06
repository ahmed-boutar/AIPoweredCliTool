import click
from watcher import start_watching

@click.command()
def watch_folder():
    """Watches 'input/' for new .txt files and summarizes them."""
    start_watching()

if __name__ == "__main__":
    watch_folder()
