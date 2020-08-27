"""This script creates our database schema."""

# Imports --------------------------------------------------------------

from src.service1_init import db
from src.service1_schema import Downloads

# Execute Code ---------------------------------------------------------

db.create_all()
