from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Tuple


class TempFiles:
    """
    Returns a tuple of temporary files' paths. These files share the lifetime of the `with` statement.

    Example:
        with TempFiles(4) as (path1, path2, path3, log_file_path):
            configure_logger(output_log_path=log_file_path)
            with path1.open('w') as file1:
                file1.write("See how easy it is?")
    """
    def __init__(self, number_of_files: int) -> None:
        self._number_of_files = number_of_files

    def __enter__(self) -> Tuple[Path]:
        """
        Creates a temporary directory, and files under that directory.
        :returns: The tuple of the files temporary paths.
        """
        self._temporary_directory = TemporaryDirectory(prefix='tom')  # A bit of temporary credit to myself :)
        directory_path = Path(self._temporary_directory.__enter__())

        return tuple(directory_path / 'file{}'.format(file_index) for file_index in range(self._number_of_files))

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Exits the temporary directory (will make all the files disappear).
        """
        self._temporary_directory.__exit__(exc_type, exc_val, exc_tb)
