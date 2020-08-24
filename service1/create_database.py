"""This file ports our SQL database schema to an SQL database."""

from src.service1_init import db
from src.service1_schema import Downloads

db.create_all()
