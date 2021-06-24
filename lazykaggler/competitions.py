import os
import subprocess
import pandas as pd
from io import StringIO
from zipfile import ZipFile

def competition_list(group = None, category = None, 
                     sort_by = None, search_for = None):
    """
    """

    # Argument checks - must be one of the valid options from Kaggle API
    # TBC

    # arg dict
    arg_dict = {
        "group": group, "category": category, "sort_by": sort_by, "search_for": search_for
    }
    
    # set up command
    cmd = "kaggle competitions list"
    for k, v in arg_dict.items():
        if v is not None:
            cmd = cmd + " --" + k + " " + v
    cmd = cmd + " -v --csv"

    # run command and get output
    x = subprocess.run(cmd, capture_output=True)
    df = pd.read_csv(StringIO(x.stdout.decode("utf-8")))

    return df

def competition_files(competiton):
    """
    Issues
    - Not all files shown at once
    - there appears to be a limit of 500 for "smaller files"
      - e.g. the image data for OSIC PFP
    - may have to compile iteratively
    - unclear whether the 500 file names are extracted at random
    """

    # set up command
    cmd = " ".join(["kaggle competitions files", competiton, "-v -csv"])

    # run command and get output
    x = subprocess.run(cmd, capture_output=True)
    df = pd.read_csv(StringIO(x.stdout.decode("utf-8")))

    return df

def competition_download(competition, file_name = None, local_path = None,
                         re_download = False):
    """
    """

    # split file_name in case it is a directory path
    if file_name is None:
        file_name_parts = ""
    else:
        file_name_parts = file_name.split("/")

    # extend local path to mirror setup on Kaggle
    if len(file_name_parts) > 1:
        local_path = os.path.join(local_path, *file_name_parts[:-1])
        if not os.path.isdir(local_path):
            os.makedirs(local_path)

        # check that file has not been downloaded
        full_path = os.path.join(local_path, file_name_parts[-1])
        if os.path.exists(full_path) and not re_download:
            print("%s already downloaded"%file_name)
            return
        else:
            pass
    else:
        full_path = os.path.join(local_path, competition)

    # set up command
    cmd = " ".join(["kaggle competitions download", competition])
    if file_name is not None:
        cmd = cmd + " -f \"%s\""%file_name
    if local_path is not None:
        cmd = cmd + " -p \"%s\""%local_path
    
    # run command
    subprocess.run(cmd)

    # Check if file is zipped
    if os.path.exists(full_path+".zip"):
        with ZipFile(full_path+".zip") as zf:
            zf.extractall(local_path)
        os.remove(full_path+".zip")
        print("Successfully unzipped contents of %s"%(full_path+".zip"))
    else:
        if os.path.exists(full_path):
            print("%s downloaded successfully"%file_name)
        else:
            print("%s could not be downloaded"%file_name)
