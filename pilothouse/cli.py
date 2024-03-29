import click
from pathlib import Path
from pilothouse import pilothouse as ph


@click.group()
def cli():
    pass


@cli.command("run")
@click.argument("pier", type=str)
def run(pier):
    """Run ship from harbor."""
    ph.run(pier)


@cli.command("new")
@click.argument("pier", type=str)
def new(pier):
    """Recreate ship in harbor."""
    ph.new(pier)


@cli.command("sync")
@click.argument("pier", type=str)
@click.argument(
    "desk",
    type=click.Path(
        exists=True,
        dir_okay=True,
        file_okay=False,
        path_type=Path,
    ),
)
def sync(pier, desk):
    """Continuously synchronize desks between Earth and Mars."""
    ph.rsync(pier, desk, True)


@cli.command("init")
@click.argument("pier", type=str)
@click.argument(
    "desk",
    type=click.Path(
        exists=True,
        dir_okay=True,
        file_okay=False,
        path_type=Path,
    ),
)
@click.option("--argo", is_flag=True, help="Install %argo")
def init(pier, desk, argo):
    """Merge, mount, sync, commit and install desk."""
    ph.init(pier, desk, argo)


@cli.command("commit")
@click.argument("pier", type=str)
@click.argument(
    "desk",
    type=click.Path(
        exists=True,
        dir_okay=True,
        file_okay=False,
        path_type=Path,
    ),
)
def commit(pier, desk):
    """Commit desk."""
    ph.commit(pier, desk)


@cli.command("autocommit")
@click.argument("pier", type=str)
@click.argument(
    "desk",
    type=click.Path(
        exists=True,
        dir_okay=True,
        file_okay=False,
        path_type=Path,
    ),
)
def autocommit(pier, desk):
    """Autocommit desk."""
    ph.autocommit(pier, desk)


@cli.command("chain")
@click.argument("pier", type=str)
@click.argument(
    "desk",
    type=click.Path(
        exists=True,
        dir_okay=True,
        file_okay=False,
        path_type=Path,
    ),
)
@click.option("--argo", is_flag=True, help="Install %argo")
def chain(pier, desk, argo):
    """Chain of command: New, init and sync."""
    ph.chain(pier, desk, argo)
