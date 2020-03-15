from subprocess import run, PIPE
from os.path import abspath, split, join, sep


def runner(result):
    # Executable path
    LOCALDIR = abspath(split(__file__)[0])
    CALC = join(LOCALDIR + sep, "calc.exe")

    # Run the executable file
    exe = [CALC, result]
    completed_process = run(exe, stdout=PIPE, stderr=PIPE)

    try:
        res = "Result: " + str(completed_process.stdout).split("\\r\\n")[-2]
    except Exception as e:
        try:
            err = "Error: " + str(completed_process.stderr)
        except Exception:
            err = "Error: " + e
