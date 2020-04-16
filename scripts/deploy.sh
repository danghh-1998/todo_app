#!/usr/bin/env bash
eval $(ssh-agent -s)
if [ -d "todo_app" ]; then
  cd todo_app
  git pull origin master
else
  git clone "git@github.com:danghh-1998/todo_app.git"
fi
