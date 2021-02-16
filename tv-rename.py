#tv-rename
import argparse, os, sys
from os.path import isfile, join

CWD = os.getcwd()
FILE_FORMATS = ['avi', 'm4v', 'mkv', 'mov', 'mp4', 'mpg', 'mpeg']

def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")

def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Renames files in a directory to conform with Plex TV show naming conventions.')
    
    parser.add_argument('Title',
        metavar='title',
        type=str,
        help='title of TV show')
    
    parser.add_argument('Season',
        metavar='season',
        type=int,
        help='season number')
    
    parser.add_argument('-d',
        '--directory',
        action='store',
        nargs='?',
        type=dir_path,
        default=CWD,
        help='the directory to read and rename files in')
    
    parser.add_argument('-f',
        '--first',
        action='store',
        type=int,
        nargs='?',
        default=1,
        help='episode number to start renaming from')

    parser.add_argument('-r',
        '--readonly',
        action='store_true',
        help='run the program in readonly mode (whatif mode)')
    
    return parser

def main():
    parser = init_parser()
    args = parser.parse_args()
    season = args.Season
    title = args.Title
    directory = args.directory
    readonly = args.readonly

    if readonly:
        print("Running in readonly mode. No files will be renamed")

    files = [f for f in os.listdir(args.directory) if isfile(join(args.directory, f))]
    if len(files) == 0:
        print("Directory does not contain any files, exiting")
        sys.exit()
        # TODO: throw error

    video_files = [f for f in files if f.split('.')[-1] in FILE_FORMATS]
    if len(video_files) == 0:
        print("Directory does not contain any supported video files, exiting")
        sys.exit()
        # TODO: throw error

    for video in video_files:
        extension = video.split('.')[-1]
        i = video_files.index(video) + 1

        if season < 10:
            season_str = f'0{season}'
        else:
            season_str = f'{season}'
        
        if i < 10:
            episode = f'0{i}'
        else:
            episode = f'{i}'
        
        name = f'{title} - S{season_str}E{episode}.{extension}'
        full_path = join(directory, video)
        destination = join(directory, name)

        if readonly:
            print(f'Program would rename {video} to {name}')
        else:
            print(f'Renaming {video} to {name}')
            os.rename(full_path, destination)        

if __name__ == '__main__':
    main()