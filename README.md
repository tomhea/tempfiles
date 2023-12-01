# tempf - TempFiles

[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/tomhea/tempfiles)](https://github.com/tomhea/tempfiles)
[![GitHub](https://img.shields.io/github/license/tomhea/flip-jump)](LICENSE)
[![PyPI - Version](https://img.shields.io/pypi/v/tempf)](https://pypi.org/project/tempf/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/tempf)](https://pypi.org/project/tempf/)


Multiple temporary files in 1 line of code. 

TempFiles(X) returns a tuple of X non-used paths.

```python
from tempf import TempFiles

with TempFiles(3) as (path1, path2, path3):
    with path1.open('w') as file1:
        file1.write('See how easy it is?')
```


## Install
```
>>> pip install tempf
```


## Example
Compilation process:

```python
from pathlib import Path
from tempf import TempFiles


def compile_run_and_check_output(code_path: Path, expected_output: str) -> bool:
    """
    Compile the code, run it, and assert the output is as expected.
    :param code_path: The path to the code to compile.
    :param expected_output: The expected output from running the code.
    :returns: True if compilation and run went successful, and the run outputted the expected output. 
    """
    with TempFiles(4) as (compile_log_path, run_log_path, executable_path, run_output_path):
        compile_file(code_path, log=compile_log_path, compiled=executable_path)
        if not is_compile_log_ok(compile_log_path):
            return False

        run_compiled(executable_path, log=run_log_path, run_output=run_output_path)
        if not is_run_log_ok(run_log_path):
            return False

        with run_output_path.open('r') as output_file:
            return expected_output == output_file.read()
```
