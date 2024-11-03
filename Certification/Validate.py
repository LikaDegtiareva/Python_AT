import logging

def validate_status_200(response, error_message):
    if response.status_code != 200:
        logging.error(error_message)
        raise Exception(error_message)