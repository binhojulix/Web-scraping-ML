#!/bin/shell

echo "-----------------------------------------"
echo "*** Web scrapping ml ***"

DIR="/venv/"
if [ -d "$DIR" ]; then
  # Take action if $DIR exists. #
  echo "criando venv ${DIR}..."
  python3 -m venv venv
fi


