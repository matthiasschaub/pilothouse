# Pilothouse

A pilothouse to command the fleet of ships in your harbor.

## Prerequisites

Pilothouse is tailored to me and not yet configurable at all. This means to
make it run following requirements have to be met:

- Urbit binary in path.
- Harbor at `$HOME/projects/urbit/harbor`.
- Fake ships and backups (e.g. `zod.bk`) in your harbor.
- Alacrity as terminal.

If somebody is interested in making this a more stable and general tool, please
reach out to me on the network (`~talfus-ladds`).

## Installation

```bash
pipx install https://git.sr.ht/~talfus-laddus/pilothouse
```

## Usage

```
Usage: pilothouse [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  chain  Chain of command: New, init and sync.
  init   Merge, mount, sync, commit and install desk.
  new    Recreate ship in harbor.
  run    Run ship from harbor.
  sync   Continuously synchronize desks between Earth and Mars.
```

Workflow:
```bash
pilothouse new zod
pilothouse init zod my-desk/
pilothouse sync
```

Or simply:
```
pilothouse chain zod my-desk
```
