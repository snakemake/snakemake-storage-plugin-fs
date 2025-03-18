# from https://stackoverflow.com/a/1392549
import os
from pathlib import Path
import shutil


def get_query_size(query_path: Path) -> int:
    if query_path.is_dir():
        return sum(f.stat().st_size for f in query_path.glob("**/*") if f.is_file())
    else:
        return query_path.stat().st_size