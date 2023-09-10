#!/usr/bin/python3
"""
Fabric script that distributes an archive the web servers,
using the function do_deploy
"""


import os
from datetime import datetime
from fabric.api import env, put, run, runs_once, local

""" Define server Ip addresses """
env.hosts = ['34.237.91.196', '3.89.146.172']


def pack_web_static():
    """
    Create and packs the web_static archive.
    Returns:
        The path to the created archive or None if there was an error.
    """

    if not os.path.isdir("versions"):
        os.mkdir("versions")

    """ Generate a uunique archive name based on the current timestamp """
    cur_time = datetime.now()
    archive_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            cur_time.year,
            cur_time.month,
            cur_time.day,
            cur_time.hour,
            cur_time.minute,
            cur_time.second
            )
    try:
        print("Packing web_static to {}".format(archive_name))
        local("tar -cvzf {} web_static".format(archive_name))
        archive_size = os.stat(archive_name).st_size
        print("web_static packed: {} -> {} Bytes".format(
            archive_name, archive_size
            )
            )
        return archive_name
    except Exception as e:
        print("Error packing web_static:", e)
        return None


@runs_once
def do_deploy(archive_path):
    """
    Deploys the static files to the host servers
    Args:
        archive_path (str): The path to the archived static files.
    Returns:
        True if deployment was successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return (False)

    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)

    try:
        """ Upload the archive to /tmp/ on the remote server """
        put(archive_path, "/tmp/{}".format(file_name))

        """ Create the release folder and extract the archive """
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))

        """ Remove the temporary archive on the remote server """
        run("rm -rf /tmp/{}".format(file_name))

        """ Move the contents to the correct location """
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))

        """ Update the symbolic link """
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))

        print('New version deployed!')
        return (True)

    except Exception as e:
        print("Error deploying:", e)
        return (False)


if __name__ == "__main__":
    """ Pack the web_static directory and get the archive path """
    archive_path = pack_web_static()
    if archive_path:
        """ Deploy the archuve to the servers """
        do_deploy(archive_path)
