#!/usr/bin/python3
""" use Fabric script to generate the .tgz archive """

from datetime import datetime
from fabric.api import local
from fabric.decorators import runs_once

@runs_once
def do_pack():
    """
    Generates the .tgx archive from the contents of the web_static folder
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)

    local("mkdir -p versions")
    result = local("tar -czvf {} web_static".format(archive_name))

    return archive_name if not result.failed else None
