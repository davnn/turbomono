# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "typer>=0.12.5",
# ]
# ///
import typer

app = typer.Typer()


def return_zero():
    return 0


@app.command()
def hello(name: str):
    print(f"Hello {name} from script!")


if __name__ == "__main__":
    app()
