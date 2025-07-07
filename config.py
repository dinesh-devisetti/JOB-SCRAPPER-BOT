import os

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")  # TODO: Define this in GitHub Secrets
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # TODO: Define this in GitHub Secrets

if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    raise ValueError("Please set EMAIL_ADDRESS and EMAIL_PASSWORD environment variables.")
