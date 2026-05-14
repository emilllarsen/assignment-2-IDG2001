# `TERMINAL, CLI, ++`

```
Basic introduction

```

- Some terminology

- Command syntax

- Important commands

- Python args


- `CLI`

   - `Command Line Interface (not GUI)`

- `Console`

   - `The physical PC –` `sometimes… Historical terms`

- `Terminal`

   - `Program for CLI stuff: Windows Terminal, Terminal, iTerm2, CMD`

- `Shell`

   - `Programs which process commands. Like programming languages:`
```
   Bash, zsh, OhMyPosh, OhMyFish, PowerShell, CMD, Batch.
```

      - `Some programs has their own shells.`


- `Command structure: <command/program> <arguments ...>`

- `Parameters`

   - `-<single character parameter 1><... 2><... 3>...`

   - `--<multi character parameter>`

   - `Often support either (pip –U …, pip –upgrade …)`

- `Help: man`

- `Pipeing: | and redirection: > < >>`

   - `ls | grep '\.py$' | sort > file.txt`

   - `Pipe: Between programs/commands, redir: To/from file/stream`

- `Multiple actions in one command: &&`


- `… are executable programs, found in the $PATH or in some`
```
 specific folders somewhere (/bin/?)
```

- `We can also make and run our own shell scripts, and run them`

   - `My sync script for the repos: ./sync.sh`


- `Paths: (nothing) . .. ~ / \`

- `cd <path>`

- `ls <path>/<filter>`

- `tree <path>`

- `pwd`

- `mkdir` `<foldername>`

- `rmdir` `<foldername>`

- `rm <file/folder>`

- `touch <filename>`

- `open/ii <path>` _`(Unix/Win)`_

- `clear`

- `exit`

- `alias x=y`

- `chmod` `<mode> <file(s)>`




- `Important paths`

- `Change Directory`

- `List content/items (-la)`

- `List tree structure`

- `Print Working Directory (where am I?)`

- `Make Directory`

- `Remove Directory (empty)`

- `Remove (-rf)`

- `Make (empty) file`

- `Open file explorer/finder`

- `Clear terminal window`

- `Exit terminal`

- `Make new (temporary) command name`

- `Change Mode (allow script to run)`


- `./<script-name.sh>`

- `ssh`

- `git`

- `python`

- `echo`




          - `Run local (executable) script`

          - `SSH`

          - `Git`

          - `Run Python thingy`

          - `Print stuff`




- `apt, pacman*, brew, winget`

- `tar, zip`

- `grep, sed`

- `top, htop` `/ kill, pkill`




- `Package managers`

- `Compression`

- `String search stuff`

- `Task manager / end process`

```
                *I use Arch btw

```

- `Spaces`

- `$var`

- `sudo <command>`




- `Quotes "v 1.txt" or v\ 1.txt`

- `Variables`

- `Super User DO: Run with admin rights`


- `enter`

- `tab`

- `ctrl + c`

- `ctrl + z`

- `ctrl + a/e`




- `Run command`

- `Finish line`

- `End active + skip line`

- `Send active to background`

- `Home/end`


- `.bashrc, .zshrc, .zprofile`

   - `Ran every time you open a new shell`

   - `Things like aliases, shell setup, etc.`


```
import sys

args = sys.argv

print(args)

# ["file.py", "arg1", "arg2"]

```

- `Cons of CLI`

   - `Ugly, not user friends, scary, halp`

   - `Inefficient (sometimes)`


- `Pros of CLI`

   - `Repeatable, copyable, scriptable and automatable`

   - `Available when SSH-ing and similar`

   - `Fast (sometimes)`


