import hmac
import hashlib


def is_valid_signature(x_hub_signature, data, private_key):

    """
    Validates Github webhook. Webhook detects a repository merge and requests
    push authorization from the deployment. This function verifies the signature
    of the request.

    :param x_hub_signature: String value of the x-hub-signature-256 hash
    :param data: Request data/payload
    :param private_key: Private key stored at deployment as env var
    :return:
    """

    if x_hub_signature is None:
        return 'x_hub_signature is None'

    # Splits the x-hub-signature into it's key and value
    hash_algorithm, github_signature = x_hub_signature.split('=', 1)

    # Instantiates the hash algorithm type defined by the key of
    # x-hub-signature
    algorithm = hashlib.__dict__.get(hash_algorithm)

    # Encodes the application private key for comparison to request
    # <str>.encode() should also work
    encoded_key = bytes(private_key, 'latin-1')

    # Creates an hmac object using the encoded private key and payload/data
    # using the algorithm type supplied by x-hub-signature
    mac = hmac.new(encoded_key, msg=data, digestmod=algorithm)

    # Return boolean value of key comparison result
    return hmac.compare_digest(mac.hexdigest(), github_signature)
