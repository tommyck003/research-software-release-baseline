import pathlib
import tomllib  # Built-in in Python 3.11+

path = pathlib.Path(__file__).parent / "config1.toml"

with path.open(mode="rb") as fp:
    config1 = tomllib.load(fp)