from loguru import logger


def check_name(data):
    try:
        if data:
            return data
    except Exception as error:
        logger.error(f"Error: {error}")

