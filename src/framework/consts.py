from pathlib import Path

SERVER_RUNNING_BANNER = """
+----------------------------------------+
|             SERVER WORKS!              |
+----------------------------------------+

Visit http://{host}:{port}

..........................................
"""
_this_file_path = Path(__file__).resolve()

dir_framework = _this_file_path.parent.resolve()

dir_src = dir_framework.parent.resolve()

dir_repo = dir_src.parent.resolve()

dir_static = (dir_src / "static").resolve()
