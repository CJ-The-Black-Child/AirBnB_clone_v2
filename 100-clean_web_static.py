#!/usr/bin/python3
"""
Deletes out-of-date archives, using the function do_clean
"""


import os
from datetime import datetime
from fabric.api import env, run, local, runs_once

env.hosts = ['34.237.91.196', '3.89.146.172']
env.user = 'ubuntu'


@runs_once
def do_pack():
    """Archives the static files"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")

    cur_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            cur_time.year,
            cur_time.month,
            cur_time.day,
            cur_time.hour,
            cur_time.minute,
            cur_time.second
            )

    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archive_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archive_size))
    except Exception:
        output = None
    return output


def do_deploy(archive_path):
    """
    Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False

    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False

    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s  {} /data/web_static/current".format(folder_path))
        print('New version is now LIVE!')
        success = True
    except Exception:
        success = False
    return success


def deploy():
    """
    Archives and deploys the static files to the host_servers.
    """
    archive_path = do_pack()

    if archive_path:
        return do_deploy(archive_path)

    else:
        return False


def do_clear(number=0):
    """
    Delets out-of date arhives of the static files
    Args:
        number(Any): The number of archives to keep.
    """
    if int(number) < 2:
        number = 1
    else:
        number = int(number) + 1
    local("ls -1t versions/ | tail -n +{} | xargs -I {{}} rm versions/{{}}".format(number))
    run("ls -1t /data/web_static/releases/ | tail -n {} | xargs -I {{}} rm -rf /data/web_static/releases/{{}})".format(number))
    run("find /data/web_static/releases/ -mindepth 1 -type d -exec rmdir {{}} \;")
    run("rm -rf /data/web_static/current")
    print("Deleted out-of-date archives")

if __name__ == "__main__":
    do_clean()
