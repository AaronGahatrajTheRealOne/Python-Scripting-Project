import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIR_PATHERN = "game"

def find_all_game_paths(source):
    game_paths = []
    
    for root, dirs ,files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATHERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)
                
        break
    
    return game_paths
    
def get_name_from_paths(paths, to_strip):
    new_names = []    
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip, "")
        new_names.append(new_dir_name)
    
def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)
    
    game_paths = find_all_game_paths(source_path)
    new_game_dirs = get_name_from_paths(game_paths, "game")
    
    create_dir(target_path)
    
    for src, dest in zip(game_paths, new_game_dirs):
        dest_path = os.path.join(target_path,dest)
        copy_and_overwrite(src, dest_path) 

def copy_and_overwrite(source, dest):
    if os.path.exist(dest):
        shutil.rmtree(dest)
    shutil.copytree(source,dest)

if __name__ == "__main__":
    args = sys.argv
    print(args)
    if len(args) > 3: 
        raise Exception("You must pass a sourse and target directory only." )
    source, target = args[1:]
    main(source, target)