import logging
from dotenv import load_dotenv
from os import getenv
from tests.path_transversal import file_path_traversal_simple_case


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Starting the program")

    load_dotenv()
    testing_url = getenv("TESTING_URL")
    logging.debug("Loaded configuration")

    file_path_traversal_simple_case()