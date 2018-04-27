Use the following stackoverflow for instructions:
[Stackoverflow Question](https://unix.stackexchange.com/questions/33255/how-to-define-and-load-your-own-shell-function-in-zsh)

You'll need to source these functions in your .zshrc:
```
fpath=( ~/path/of/zshfunction/dir "${fpath[@]}" )
autoload -Uz dockercs
```

When more functions are added, update your autoload:
```
autoload -Uz dockercs function1 function 2
```
