import os

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    raise ValueError("Please set EMAIL_ADDRESS and EMAIL_PASSWORD environment variables.")
