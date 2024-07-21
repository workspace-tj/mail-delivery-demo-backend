from uuid import uuid4


def generate_id():
    """
    Generate a unique ID using UUID4 without hyphens.
    """
    return str(uuid4()).replace("-", "")
