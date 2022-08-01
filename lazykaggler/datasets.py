
# |-+]=[+-||-+]=[+-||-+]=[+-||-+]=[+-||-+]=[+-||-+]=[+-||-+]=[+-||-+]=[+-||-+]=[
# Kaggle Datasets ]=[+-||-+]=[+-||-+]=[+-||-+]=[+-||-+]=[+-||-+]=[+-||-+]=[+-||-
# |-+]=[+-||-+]=[+-||-+]=[+-||-+]=[+-||-+]=[+-||-+]=[+-||-+]=[+-||-+]=[+-||-+]=[


import os
import json
import subprocess


def gen_dataset_metafile(local_path: str,
                         user: str,
                         title: str,
                         subtitle: str = None,
                         description: str = None,
                         url_path: str = None,
                         licenses: list = None,
                         resources: str = None,
                         keywords: str = None):
    """
    Generates dataset-metadata.json file required for uploading via Kaggle 
    Datasets API.

    Parameters
    ----------
    local_path: str
        Path of local directory where data is located. The dataset-metadata.json 
        file will be created here.
    user: str
        Your Kaggle username.
    title: str
        Title of the dataset.
    subtitle: str, optional, default=None
        Subtitle for the dataset.
    description: str, optional, default=None
        Dataset description.
    url_path: str, optional, default=None
        TBC
    licenses: list, optional, default=None
        TBC
    resources: str, optional, default=None
        TBC
    keywords: str, optional, default=None
        TBC

    """

    if url_path is None:
        url_path = title.replace(" ", "-")

    if licenses is None:
        licenses = [{"name": "CC0-1.0"}]

    meta = {
        "title": title,
        "id": user + "/" + url_path,
        "licenses": licenses
    }

    if subtitle is not None:
        meta["subtitle"] = subtitle

    if description is not None:
        meta["description"] = description

    if resources is not None:
        meta["resources"] = resources

    if keywords is not None:
        meta["keywords"] = keywords

    with open(os.path.join(local_path, "dataset-metadata.json"), "w") as wf:
        json.dump(meta, wf)


def upload_dataset(local_path: str,
                   new_version: bool = False,
                   version_notes: str = None):
    """
    Upload data to Kaggle Datasets via the API.

    Parameters
    ----------
    local_path: str
        Path of local folder where data is located. Must contain a file named 
        dataset-metadata.json.
    new_version: bool, default=False
        TBC
    version_notes: str, optional, default=None
        TBC

    """

    if os.path.exists(os.path.join(local_path, "dataset-metadata.json")):
        pass
    else:
        print("Must generate metadata prior to uploading!" +
              "\nYou can use gen_dataset_metafile() function for this.")
        return

    if new_version:
        cmd = "kaggle datasets version -p \"%s\" -m \"%s\"" % (local_path,
                                                               version_notes)
    else:
        cmd = "kaggle datasets create -p \"%s\"" % local_path

    subprocess.run(cmd)
