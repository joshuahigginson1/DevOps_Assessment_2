
"""Serving as service 1's entry point."""

# Imports --------------------------------------------------------------

from service2.src.service2 import service2

# Run our App ----------------------------------------------------------

if __name__ == "__main__":
    service2.run(port=5002)
