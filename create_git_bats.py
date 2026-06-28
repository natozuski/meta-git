import os
import sys
import argparse

def create_bat_files(desktop_path, folder_names):
    """
    Creates .bat files for each git folder:
    - folder.bat: navigates to the folder
    - folder_git.bat: navigates to the folder and runs git status and git pull
    """
    
    # Validate desktop path
    if not os.path.exists(desktop_path):
        print(f"Error: Desktop path '{desktop_path}' does not exist.")
        return False
    
    # Validate each folder exists
    valid_folders = []
    for folder in folder_names:
        folder_path = os.path.join(desktop_path, folder)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            valid_folders.append(folder)
        else:
            print(f"Warning: Folder '{folder}' not found at '{desktop_path}'. Skipping...")
    
    if not valid_folders:
        print("No valid folders found. Exiting...")
        return False
    
    # Create bat files for each valid folder
    for folder in valid_folders:
        folder_path = os.path.join(desktop_path, folder)
        
        # Create folder.bat (just navigates to the folder)
        bat_content = f'cd "{folder_path}"\n\npause'
        bat_filename = f"{folder}.bat"
        
        with open(bat_filename, 'w') as f:
            f.write(bat_content)
        print(f"Created: {bat_filename}")
        
        # Create folder_git.bat (navigates and runs git commands)
        git_bat_content = f'cd "{folder_path}"\ngit status\ngit pull\n\npause'
        git_bat_filename = f"{folder}_git.bat"
        
        with open(git_bat_filename, 'w') as f:
            f.write(git_bat_content)
        print(f"Created: {git_bat_filename}")
    
    return True

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Create .bat files for git folders on desktop')
    parser.add_argument('desktop_path', help='Path to your desktop directory')
    parser.add_argument('folders', nargs='+', help='Names of git folders on your desktop')
    
    args = parser.parse_args()
    
    # Create the bat files
    success = create_bat_files(args.desktop_path, args.folders)
    
    if success:
        print("\nAll .bat files created successfully!")
    else:
        print("\nFailed to create .bat files.")
        sys.exit(1)

if __name__ == "__main__":
    main()