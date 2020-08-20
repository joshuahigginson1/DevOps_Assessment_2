
"""Serving as service 1's entry point."""

# Imports --------------------------------------------------------------

from service4.src.service4_init import service4

# Run our App ----------------------------------------------------------

if __name__ == "__main__":
    service4.run(port=5004)