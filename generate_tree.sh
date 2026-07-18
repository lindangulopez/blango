#!/bin/bash

find . \
  -path "./.git" -prune -o \
  -path "./__pycache__" -prune -o \
  -path "./env" -prune -o \
  -path "./venv" -prune -o \
  -path "./.venv" -prune -o \
  -print | sort > REPO_TREE.txt

{
echo "# Repository Tree"
echo
echo '```'
cat REPO_TREE.txt
echo '```'
} > REPO_TREE.md

echo "Done! Repository tree saved to REPO_TREE.md"