
"""Serving as service 1's entry point."""

# Imports --------------------------------------------------------------

from service3.src.service3_init import service3

# Run our App ----------------------------------------------------------

if __name__ == "__main__":
    service3.run(port=5003)
