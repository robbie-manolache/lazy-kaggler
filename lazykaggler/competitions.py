import subprocess
import pandas as pd
from io import StringIO

def competition_list(group = "general", category = "all", 
                     sort_by = "latestDeadline", search_for = None):
    """
    """

    # Argument checks - must be one of the valid options from Kaggle API
    # TBC

    # Set up command
    cmd = "kaggle competitions list"
    cmd = " ".join([cmd, "--group", group, "--category", category, 
                    "--sort-by", sort_by])
    if search_for is not None:
        cmd = " ".join([cmd, "search", search_for])
    else:
        pass
    cmd = cmd + " -v --csv"

    # run command and get output
    x = subprocess.run(cmd, capture_output=True)
    df = pd.read_csv(StringIO(x.stdout.decode("utf-8")))

    return df

def competition_files(competiton):
    """
    """

    # Set up command
    cmd = " ".join(["kaggle competitions files", competiton, "-v -csv"])

    # run command and get output
    x = subprocess.run(cmd, capture_output=True)
    df = pd.read_csv(StringIO(x.stdout.decode("utf-8")))

    return df