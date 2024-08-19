function scr() {
    [[ $# -eq 0 ]] && echo "usage: scr NAME" && return 1
    touch "$1"
    echo "#!/bin/bash" >> "$1"
    chmod +x "$1"
    vim "$1"
}
