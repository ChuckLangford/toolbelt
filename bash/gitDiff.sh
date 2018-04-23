#!/bin/sh

git diff $1 $2 ':(exclude)*.csproj' ':(exclude)*packages.config' ':(exclude)*package.json'
