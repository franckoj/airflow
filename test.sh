#!/bin/bash

# Variables
DEST_FOLDER="dag_test"      # Name of the new folder
SOURCE_FOLDER="dags" # Name of the source folder to copy from

# Step 1: Create the destination folder if it doesn't exist
if [ ! -d "$DEST_FOLDER" ]; then
    echo "Creating destination folder: $DEST_FOLDER"
    mkdir "$DEST_FOLDER"
else
    echo "Folder $DEST_FOLDER already exists."
fi

# Step 2: Copy contents from the source folder to the destination folder
if [ -d "$SOURCE_FOLDER" ]; then
    echo "Copying contents from $SOURCE_FOLDER to $DEST_FOLDER" 
    cp -r "$SOURCE_FOLDER"/* "$DEST_FOLDER"/
else
    echo "Source folder $SOURCE_FOLDER does not exist. Exiting."
    exit 1
fi

# Step 3: Delete the source folder
echo "Deleting source folder: $SOURCE_FOLDER"
# rm -rf "$SOURCE_FOLDER"

# echo "Operation completed successfully."
