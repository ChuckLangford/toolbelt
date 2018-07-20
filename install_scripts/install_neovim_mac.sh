#!/bin/sh

brew install neovim

# automate steps to use .vimrc
mkdir -p ~/.config/nvim && cd $_ && touch init.vim
printf "set runtimepath^=~/.vim runtimepath+=~/.vim/after\nlet &packpath = &runtimepath\nsource ~/.vimrc" >> init.vim
