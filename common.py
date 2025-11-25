import logging

def setup_logging(level: int = logging.INFO) -> None:
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("advent_of_code.log"), logging.StreamHandler()],
    )

def read_input(inputfile: str) -> str:
    logging.info("Reading input file")
    try:
        with open(inputfile, "r") as f:
            return f.read()
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        raise
