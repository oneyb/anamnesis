# Description

Anamnesis is a clipboard manager. It stores all clipboard history and
offers an easy interface to do a full-text search of the items of its
history.


# Usage

I use `xbindkeys` to create a keyboard shortcut.

``` example
"anamnesis-browser"
Mod4 + c
```
That won't work on wayland, so use your distro's configuration options.

# Installing on Linux

## Easily

``` shell
# First install system dependencies (see Dependencies section below)
# Then:
pipx install --system-site-packages git+https://github.com/oneyb/anamnesis
```

## Manually

The recommended manual installation has three steps:

1.  copy the command-line to the system path
2.  install the anamnesis daemon in the session start-up
3.  create a keyboard shortcut to the graphic interface

Specifically:

1.  Create a symbolic link named 'anamnesis' in the system path,
    pointing to anamnesis.py, for example:

    ``` shell
    sudo ln -s /path/to/anamnesis.py /usr/bin/anamnesis
    ```

2.  Configure the following command to be executed on session start-up
    (System -\> Preferences -\> Session Apps):

    ``` shell
    anamnesis --start
    ```

3.  Configure a shortcut to the graphic interface (System -\>
    Preferences -\> Keyboard Shortcuts):

    ``` shell
    anamnesis --browse
    ```

# Command line

``` example
Usage: anamnesis [options]

Options:
  --version            show program's version number and exit
  -h, --help           show this help message and exit
  --start              starts anamnesis daemon
  --stop               stops anamnesis daemon
  --restart            restarts anamnesis daemon
  -b, --browser        opens anamnesis browser with clipboard history
  --cleanup            optimize database and limit the number of elements
  -l N, --list=N       prints the clipboard history last N values
  --filter=KEYWORDS    use keywords to filter the clips to be listed
  -a CLIP, --add=CLIP  adds a value to the clipboard
  --remove=ID          removes the clipboard element with the given id
  --brief              print only a brief version of long clipboard elements
```

## Examples:

Starts the graphical user interface:

``` shell
anamnesis --browser
# alternatively, if using easy installation
anamnesis-browser
```

Starts the anamnesis daemon:

``` shell
anamnesis --start
# alternatively, if using easy installation
anamnesis-daemon
```

Stops the anamnesis daemon:

``` shell
anamnesis --stop
```

List the last 20 clipboard items:

``` shell
anamnesis --list=20
```

List the last 5 items in the clipboard the has the keywords 'my' and
'search':

``` shell
anamnesis --list=5 --filter="my search"
```

Adds a clipboard item (same as copying to the clipboard if the daemon is
running):

``` shell
anamnesis --add="hello, clipboard!"
```

# Dependencies

-   python3 (>3.5)
-   sqlite3
-   python3-gi
-   gobject-introspection
-   libgirepository-2.0-dev

``` shell
# Debian 13 (maybe Ubuntu)
sudo apt install libgirepository-2.0-dev gobject-introspection

# Fedora/RHEL
sudo dnf install python3-gobject-devel gobject-introspection-devel gtk3-devel

# Arch
sudo pacman -S python-gobject gobject-introspection gtk3
```

# Configuration

Anamnesis will search for configuration files in the
$XDG<sub>DATADIRS</sub> and $XDG<sub>CONFIGHOME</sub> directories. It
defaults to:

-   `/usr/share/anamnesis/anamnesis.cfg`

-   `~/.config/anamnesis/anamnesis.cfg`

# Authors

Written by Fabio Guerra \<fabiowguerra@users.sourceforge.net\>

Ported to Python 3 by Brian Oney

# <span class="todo TODO">TODO</span> Issues

-   Configure GUI window to be pretty again
    -   [file:anamnesis/browser.py::#%20def%20apply_treeview_configuration(treeview):](anamnesis/browser.py::#%20def%20apply_treeview_configuration(treeview):)
