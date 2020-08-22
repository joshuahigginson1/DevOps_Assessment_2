"""Serving as service 3's entry point."""

# Imports --------------------------------------------------------------

from src.service3 import service3

# Run our App ----------------------------------------------------------

if __name__ == "__main__":
    service3.run(host="0.0.0.0", port=5003)
