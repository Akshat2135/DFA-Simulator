"""
DFA Simulator package.
Author: Akshat
"""

__version__ = "0.1.0"
__author__ = "Akshat"


def main() -> None:
    """Launch the DFA Simulator Streamlit web application."""
    import sys
    import subprocess
    from pathlib import Path

    app_file = Path(__file__).parent / "app.py"
    subprocess.run([sys.executable, "-m", "streamlit", "run", str(app_file)])


if __name__ == "__main__":
    main()
