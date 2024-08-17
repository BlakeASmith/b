#!/usr/bin/env python3
from subprocess import run
from shutil import which
from pathlib import Path

# Expecting a directory structure like
#├── <program>
    #├── <platform1>
    #│   └── bootstrap.sh
    #│   └── check_install.sh
    #├─── <platform2>
    #│   └── bootstrap.sh
    #│   └── check_install.sh
    #├── default
    #│   └── check_install.sh
    #│   └── bootstrap.sh


def detect_platform():
    arch = which("pacman")
    deb = which("apt")
    mac = which("brew")

    if arch:
        return "arch"
    if deb:
        return "debian"
    if mac:
        return "mac"

    raise RuntimeError("Unspported platform :(")

platform = detect_platform()
print(f"detected platform {platform}")

here = Path(__file__).parent
dirs = [here/"pipx", here/"ansible"]

for d in dirs:
    program = d.name
    platforms = {_d.name: _d for _d in d.glob("*") if _d.is_dir()}
    p = platforms.get(platform, None)
    default = platforms.get("default", None)

    if p is None and default is None:
        raise RuntimeError(f"Must define configuration for platform {platform} or add default")

    if p is None:
        p = default

    assert p is not None
    assert default is not None

    bootstrap = p/"bootstrap.sh"
    if not bootstrap.exists():
        bootstrap = default/"bootstrap.sh"

    check_exists = p/"check_exists.sh"
    if not check_exists.exists():
        check_exists = default/"check_exists.sh"

    result = run([str(check_exists.absolute())])
    if result.returncode != 0:
        print(f"{program} is installed. Running {bootstrap}")
        _ = run([str(bootstrap.absolute())])
    else:
        print(f"{program} is installed")
