from subprocess import check_call


def rundev() -> None:
    check_call(["uvicorn", "main:app", "--reload"])

