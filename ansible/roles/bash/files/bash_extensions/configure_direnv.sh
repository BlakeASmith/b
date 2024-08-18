# load direnv hook if exists, if it doesn't then skip running this file
$(which direnv &>/dev/null) && eval "$(direnv hook bash)" &>/dev/null || return


function mkvenv() {
    python3 -m venv "$PWD/.venv"
    echo "export VIRTUAL_ENV=$PWD/.venv" >> .envrc
    echo "export PATH=$PWD/.venv/bin:$PATH" >> .envrc
    direnv allow "$PWD"
}






