#!/usr/bin/python3
"""
Fabric script that distributes an archive the web servers,
using the function do_deploy
"""


import os
from fabric.api import env, put, run

""" Define server Ip addresses """
env.hosts = ['34.237.91.196', '3.89.146.172']


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
    archive_path = "versions/web_static_20230923191314.tgz"
    if do_deploy(archive_path):
        """ Deploy the archuve to the servers """
        print("Deployment successful")
    else:
        print("Deployment failed")
