# test-scripts

## Work with python
### Install brew
```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Add the next line to the file `~/.zshrc`
```text
export PATH=/opt/homebrew/bin:$PATH
```

### Install pyenv
https://github.com/pyenv/pyenv#installation
```shell
brew update
brew install pyenv
```

### Install python 
```shell
pyenv install 3.11.0
pyenv global 3.12.0
```
Add the next line to the file `~/.zshrc`
```text
alias python="$(pyenv which python)"
alias pip="$(pyenv which pip)"
```

### Install poetry
https://python-poetry.org/docs/
```shell
brew install pipx
pipx ensurepath
pipx install poetry
```