class FileNotExistError(Exception):
    """
FileNotExistError indicates that the file corresponding to the provided sha256 hash could not be found. This error occurs when the server fails to locate the file based on the provided SHA256 hash.
    This error is uncommon and typically indicates a server-side issue. It may occur due to a server outage, network issues, or a corrupted file on the server.
    This error is unexpected and should be reported to the server administrator for further investigation. It may indicate a problem with the server or the file storage mechanism.
    """

    pass


class FileRequiredError(Exception):
    """
FileRequiredError indicates that BinaryAI requires the original file, but it is not being provided. This error occurs when the original file is not provided along with the SHA256 hash.
    This error might occur when only the hash is provided to BinaryAI without the original file. Please ensure that the original file is provided along with the hash.
    This error might occur when only the hash is provided to BinaryAI without the original file. Please ensure that the original file is provided along with the hash.
    """

    pass
