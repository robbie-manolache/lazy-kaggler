
import os
import json
import subprocess

def gen_dataset_metafile(local_path, user, title, 
                         subtitle=None, description=None,
                         url_path=None, licenses=[{"name": "CC0-1.0"}],
                         resources=None, keywords=None):
    """
    Generates dataset-metadata.json file required for uploading via Kaggle datasets API.
    """
    
    if url_path is None:
        url_path = title.replace(" ", "-")
    
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

def upload_dataset(local_path, new_version=False,
                   version_notes=None):
    """
    """
    
    if os.path.exists(os.path.join(local_path, "dataset-metadata.json")):
        pass
    else:
        print("Must generate metadata prior to uploading!"+
              "\nYou can use gen_dataset_metafile() function for this.")
        return
    
    if new_version:
        cmd = "kaggle datasets version -p \"%s\" -m \"%s\""%(local_path, 
                                                             version_notes)   
    else:
        cmd = "kaggle datasets create -p \"%s\""%local_path
        
    subprocess.run(cmd)      
