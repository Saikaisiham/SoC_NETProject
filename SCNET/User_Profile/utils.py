import uuid
import base64


def generate_code():
    code = str(uuid.uuid4()).replace('-','')[:12]
    return code
