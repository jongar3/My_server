""""""

from natsort import natsorted
from pathlib import Path
import os
import re

current_dir = Path(os.getcwd()) 

def fix_format_serie(renmame_episodes=False):
    SERIE_NAME = str(current_dir).split("/")[-1]
    print(SERIE_NAME)

    for path in current_dir.iterdir():
        if not path.is_dir() or path.name.startswith('.'):
            continue
        
        try:
            season_number = int(path.name.split(" ")[-1]) # Get the number of the seasons
        except (ValueError, IndexError):
            continue
      
        episode_number = 0 # Usually the episodes would be ordered with iterdir()
        if season_number>0:
            print(f"Renaming season {season_number:02d}")
            for episode in natsorted(path.iterdir()):
                episode_number += 1
                episode_name = str(episode).split("/")[-1]
                #print(episode_name)
                numbers= re.findall(r'E\d{2}', episode_name) # If we have a E01, E02... This should be the episode number
                if len(numbers) == 1:
                    episode_number = int(numbers [0][1:]) # Get the number after E
                new_name = f"{SERIE_NAME} S{season_number:02d}E{episode_number:02d}{episode.suffix}"
                if episode.name == new_name:
                    continue
                    
                print(f"  [OK] {episode.name} -> {new_name}")
                if renmame_episodes:
                    episode.rename(path / new_name)



if __name__ == "__main__":
    fix_format_serie()
    confirmation= input("ARE THE CHANGES OK? pls press y to confirm...")
    if confirmation.lower() == 'y':
        fix_format_serie(renmame_episodes=True)
    else:
        print("No changes were made.")