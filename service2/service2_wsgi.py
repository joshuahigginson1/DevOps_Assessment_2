"""Serving as service 2's entry point."""

# Imports --------------------------------------------------------------

from src.service2 import service2

# Run our App ----------------------------------------------------------

if __name__ == "__main__":
    service2.run(host="0.0.0.0", port=5002)
