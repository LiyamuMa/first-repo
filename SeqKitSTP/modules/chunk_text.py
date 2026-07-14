import logging  
logger = logging.getLogger(__name__)


def chunk_string(query_sequence, chunk_by):

    logger.info("Chunking sequence into blocks of {}".format(chunk_by))

    my_list = []

    try:
        while query_sequence:
            my_list.append(query_sequence[:chunk_by])
            query_sequence = query_sequence[chunk_by:]
    except TypeError as e:
        logger.error("Chunking failed with exception: {}".format(e))
        raise

    return my_list


def chunk_string_to_blocks(query_sequence, chunk_by, num_blocks, return_lowercase=True):

    logger.info(
        "Chunking sequence into rows of {} blocks of {}".format(
            num_blocks, chunk_by
        )
    )

    if not isinstance(chunk_by, int) or not isinstance(num_blocks, int):
        raise TypeError(
            f"chunk_by {chunk_by} and num_blocks {num_blocks} must be integers."
        )

    try:
        query_sequence = "".join(query_sequence.split())

        if return_lowercase:
            query_sequence = query_sequence.lower()

        flat_chunks = chunk_string(query_sequence, chunk_by)

        full_list = [
            flat_chunks[i:i + num_blocks]
            for i in range(0, len(flat_chunks), num_blocks)
        ]

    except TypeError as e:
        logger.error("Chunking to blocks failed with exception: {}".format(e))
        raise

    return full_list