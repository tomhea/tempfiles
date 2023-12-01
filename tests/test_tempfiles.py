from tempf import TempFiles


# noinspection PyUnusedLocal
def test_sanity() -> None:
    """
    Test that TempFiles(3) actually parses.
    """
    with TempFiles(3) as (a, b, c):
        pass


def test_read_write_multiple_lengths() -> None:
    """
    Test TempFiles with different number of temp-files.
    For each case, test that each temp-file actually responds to the standard 'w'/'a'/'r' openings,
     and to the write()/read() functions.
    """
    for num_of_files in range(10):
        with TempFiles(num_of_files) as paths:
            for path in paths:
                with path.open('w') as file:
                    file.write('0')
                with path.open('w') as file:
                    file.write('1')

                with path.open('a') as file:
                    file.write('2')
                with path.open('a') as file:
                    file.write('3')

                with path.open('r') as file:
                    assert '123' == file.read()

