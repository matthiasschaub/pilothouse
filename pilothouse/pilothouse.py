import click
import os
import requests
import shutil
import subprocess
from time import sleep
from pathlib import Path

harbor = Path.home() / "projects" / "urbit" / "harbor"
argo = harbor / "argo"  # language server


def new(pier):
    """Recreate ship in harbor."""
    pier = harbor / pier
    pier_bk = pier.with_suffix(".bk")
    if pier.exists():
        shutil.rmtree(pier)
    if pier_bk.exists():
        shutil.copytree(pier_bk, pier)
    run(pier)


def run(pier):
    pier = harbor / pier
    if not pier.exists():
        click.echo("Pier does not exists")
        return
    subprocess.Popen(["alacritty", "--command", "urbit", pier])


def init(pier, desk, argo):
    """Merge, mount, sync, commit and install desk."""
    if argo:
        dojo(pier, "merge %argo our %base")
        dojo(pier, "mount %argo")
        rsync(pier, argo, False)
        dojo(pier, "commit %argo")
        dojo(pier, "install our %argo")

    dojo(pier, "merge %{} our %base".format(desk.name))
    dojo(pier, "mount %{}".format(desk.name))
    rsync(pier, desk, False)
    dojo(pier, "commit %{}".format(desk.name))
    dojo(pier, "install our %{}".format(desk.name))
    dojo(pier, "start %dbug")


def rsync(pier, desk, watch):
    pier = harbor / pier
    desk_earth = desk
    desk_mars = pier / desk.name
    if not pier.exists():
        click.echo("Pier does not exists")
    # TODO: If syncing full desk this can be useful to keep destination dir clean
    # if desk_mars.exists():
    #     shutil.rmtree(desk_mars)
    if watch:
        os.system("watch rsync -r {}/ {}".format(desk_earth, desk_mars))
    else:
        os.system("rsync -r {}/ {}/".format(desk_earth, desk_mars))


def dojo(pier, cmd):
    with open(harbor / pier / ".http.ports") as f:
        words = f.read().split()
    port = int(words[0])
    url = "http://localhost:{}".format(port)
    data = {
        "source": {"dojo": "+hood/{}".format(cmd)},
        "sink": {"app": "hood"},
    }
    requests.post(url, json=data)


def chain(pier, desk, argo):
    new(pier)
    sleep(1)
    init(pier, desk, argo)
    rsync(pier, desk, True)
