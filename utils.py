import logging

import dill


def load_object(file_path: str):
    """
    Load file into python and return object.

    :param file_path: file location
    :return: object
    """
    try:
        with open(file_path, "rb") as f:
            obj = dill.load(file=f)
        return obj
    except Exception as e:
        logging.info(f"Error in load_object: {str(e)}")
        raise e
