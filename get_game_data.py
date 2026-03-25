import os
import sys

GAME_DIR_PATHERN = "game"

def find_all_game_path(source):
    game_paths = []

    for root, dirs, fileName in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATHERN in directory.lower():
                paths = os.path.join(source, directory)
                game_paths.append(paths)

    return game_paths

def get_names_from_paths(paths, to_remove):
    new_names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_remove, "")
        new_names.append(new_dir_name)

def create_target_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def main(source, target):
    cwd = os.getcwd()
    
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)
    
    game_paths = find_all_game_path(source_path)
    new_game_dirs = get_names_from_paths(game_paths, "game")
    
    create_target_dir(target_path)

if __name__ == "__main__":
    arguments = sys.argv
    if (len(arguments) > 3):
        raise Exception("You need to add source and the target dirName..")
    source, target = arguments[1:]
    main(source, target)
    