import logging 
logger = logging.getLogger(__name__)

def create_genbank_style(chunk_list):
    counter = 0

    text_out = ""

    try:
        for line in chunk_list:
            counter += 1
            row = " ".join(line)
            text_out += f"{counter}\t{row}\n"
            counter += len("".join(row.split())) - 1

    except TypeError as e:
        logger.error(f"create_genbank_style failed with error: {e}")

    return text_out