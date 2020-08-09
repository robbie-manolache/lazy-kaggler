import os
import subprocess

def kernel_output_download(user, kernel_name, local_path = None):
    """
    """

    # set kernel path
    kernel_path = "/".join([user, kernel_name])

    # set up command
    cmd = " ".join(["kaggle kernels output", kernel_path])
    if local_path is not None:
        cmd = cmd + " -p \"%s\""%local_path

    # run command
    subprocess.run(cmd)

    # check local path contents
    print(os.listdir(local_path))