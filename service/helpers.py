from django.conf import settings

def gen_decode_this_url(vin, api_key, response_format):
    return settings.DECODE_THIS_URL % (
        vin,
        api_key,
        response_format,
    )

def get_response_from_transport():
    pass