"""Serving as service 1's entry point."""

# Imports --------------------------------------------------------------

from src.service1_init import service1, db

# Build Database Schema ------------------------------------------------

from src.service1_schema import Downloads

db.create_all()

# Run our App ----------------------------------------------------------

if __name__ == "__main__":
    service1.run()
