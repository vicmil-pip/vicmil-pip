"""
This is the installer that contains all information for how to install things
"""

import platform
import inspect
import requests
import zipfile
import os
import pathlib
import shutil
import importlib
import sys
import urllib.request
from typing import Dict

"""
=============================================================================
                            List of Packages
=============================================================================
"""

class Package:
    def __init__(self):
        self.name: str = "no name has been added"
        self.description: str = "no description has been added"
        self.dependencies: list = []

    def install(self):
        raise Exception("No installer defined")


class Packages:
    class gcc(Package):
        def __init__(self):
            self.name = "gcc"
            self.description = "opens a webpage to show how to install gcc for your specific platform, gcc is a c/c++ compiler"
            self.dependencies = []
    
        def install(self):
            url = ""
            if platform.system() == "Windows":
                url = "https://code.visualstudio.com/docs/cpp/config-mingw"
                
            if platform.system() == "Linux":
                url = "https://medium.com/@adwalkz/demystifying-development-a-guide-to-build-essential-in-ubuntu-for-seamless-software-compilation-b590b5a298bb"
                
            go_to_url(url)
            package_path = get_directory_path(__file__, 0) + "/packages/" + self.name
            os.makedirs(package_path, exist_ok=True)
            with open(package_path + "/readme.md", "w") as file:
                file.write("this directory is intentionally left blank\n")
            

    class cppBuild(Package):
        def __init__(self):
            self.name = "cppBuild"
            self.description = "Help tools for building c++ projects"
            self.dependencies = []


    class cppBasics(Package):
        def __init__(self):
            self.name = "cppBasics"
            self.description = "c++ utility files, only requiring a c++11 compiler. Also includes some utility files when compiling for the browser"
            self.dependencies = ["cppBuild"]


    class cppOpenglSDL(Package):
        def __init__(self):
            self.name = "cppOpenglSDL"
            self.description = "c++ utility files, and opengl+sdl library for building graphics applications"
            self.dependencies = ["cppBasics"]

    
    class cppStb(Package):
        def __init__(self):
            self.name = "cppStb"
            self.description = "c++ utility files, and stb library for loading images and fonts in c++"
            self.dependencies = ["cppBasics"]


    class cppGlm(Package):
        def __init__(self):
            self.name = "cppGlm"
            self.description = "c++ utility files, and glm library for math aimed at graphics and linear algebra"
            self.dependencies = ["cppBasics"]


    class cppEmsdk(Package):
        def __init__(self):
            self.name = "emsdk"
            self.description = "emscripten, used for compiling c++ for the web"
            self.dependencies = []
        
        def install(self):
            install_emsdk(get_directory_path(__file__) + "/" + self.name)


    class cppSocketIOClient(Package):
        def __init__(self):
            self.name = "cppSocketIOClient"
            self.description = "c++ utility files, and socket io client library for building networking apps"
            self.dependencies = ["cppBasics"]

    
    class cppMiniz(Package):
        def __init__(self):
            self.name = "cppMiniz"
            self.description = "c++ utility files, and miniz library for zipping/unzipping files"
            self.dependencies = ["cppBasics"]

    
    class cppTinyObjLoader(Package):
        def __init__(self):
            self.name = "cppTinyObjLoader"
            self.description = "c++ utility files, and tiny obj loader library for loading .obj files"
            self.dependencies = ["cppBasics", "cppMiniz"]


    class cpp2DRectPack(Package):
        def __init__(self):
            self.name = "cpp2DRectPack"
            self.description = "c++ utility files, and smol-atlas library for packing 2d rectangles on a 2d surface"
            self.dependencies = ["cppBasics"]

    
    class cppEigen(Package):
        def __init__(self):
            self.name = "cppEigen"
            self.description = "c++ utility files, and eigen library for various math operations"
            self.dependencies = ["cppBasics"]


    class notoFonts(Package):
        def __init__(self):
            self.name = "notoFonts"
            self.description = "subset of noto fonts, free to use, supporting a wide range of languages. https://fonts.google.com/noto/fonts"
            self.dependencies = []


    class vitB(Package):
        def __init__(self):
            self.name = "vitB"
            self.description = "vitB is a ML model used by segment anything https://github.com/facebookresearch/segment-anything"
            self.dependencies = []


    class cppVicmilGui(Package):
        def __init__(self):
            self.name = "cppVicmilGui"
            self.description = "c++ utility files for building cross-platform graphics applications in c++"
            self.dependencies = [
                "cppBasics", 
                "cppOpenglSDL", 
                "cppStb", 
                "cppGlm", 
                "cppEmsdk", 
                "cppSocketIOClient", 
                "cppMiniz", 
                "cppTinyObjLoader", 
                "cpp2DRectPack",
                "notoFonts"
            ]

    class nvm(Package):
        def __init__(self):
            self.name = "nvm"
            self.description = "python utility files, and nvm(node version manager), for building node applications"
            self.dependencies = []

    
    class mkDocs(Package):
        def __init__(self):
            self.name = "mkDocs"
            self.description = "python utility files, and mkdocs library or creating documentation"
            self.dependencies = []


def get_packages():
    # Initialize an empty dictionary to hold package information
    package_dict = {}
    
    # Iterate through all the classes in the Packages class
    for name, obj in inspect.getmembers(Packages):
        # Check if the object is a subclass of Package (and not Package itself)
        if isinstance(obj, type) and issubclass(obj, Package) and obj is not Package:
            package_instance = obj()
            package_dict[package_instance.name] = package_instance
    
    return package_dict


packages: Dict[str, Package] = get_packages()


def print_all_packages():
    # List all the packages and print their description
    package_info = "Packages: \n"
    packages_sorted = list(packages.keys())
    packages_sorted.sort()
    for package_name in packages_sorted:
        package_info += packages[package_name].name.ljust(20, " ") + ": " + packages[package_name].description + "\n"

    print(package_info)


def print_installed_packages():
    # List all the packages and print their description
    dirs = os.listdir(get_directory_path(__file__, 0)) + "/packages"         
    folders = list()
    for f in dirs:
        if not os.path.isdir(os.path.join(get_directory_path(__file__, 0), f)):
            continue
        if f == "__pycache__":
            continue
        if f == "venv":
            continue
        folders.append(f)

    print(f"found {len(folders)} installed packages")
    print(folders)
        

def install_package(package_name: str):
    # Determine if the install is valid
    if not package_name in packages.keys():
        print("Could not find package in available packages")
        return

    package_path = get_directory_path(__file__, 0) + "/packages/" + package_name
    if os.path.exists(package_path):
        print(f"Package {package_name} path already exists")
        return

    # Create the package directory
    os.makedirs(package_path, exist_ok=True)

    # Start by installing dependencies
    if len(packages[package_name].dependencies) != 0:
        #print(f"Installing dependencies: {packages[package_name].dependencies}")
        for package_dep in packages[package_name].dependencies:
            install_package(package_dep)

    try:
        print(f"Installing package: {package_name}")
        packages[package_name].install()
    except Exception as e:
        print(f"{package_name} package install failed:", e)
        delete_folder_with_contents(package_path)


def remove_package(package_name: str):
    # Determine if the install is valid
    if not package_name in packages.keys():
        print("Could not find package in available packages")

    package_path = get_directory_path(__file__, 0) + "/packages/" + package_name
    if os.path.exists(package_path):
        delete_folder_with_contents(package_path)
        print(f"removed package {package_name}")


"""
=============================================================================
                            Utility functions
=============================================================================
"""


def get_directory_path(__file__in, up_directories):
    return str(pathlib.Path(__file__in).parents[up_directories].resolve()).replace("\\", "/")


def delete_file(file: str):
    if os.path.exists(file):
        os.remove(file)


def delete_folder_with_contents(file: str):
    if os.path.exists(file):
        shutil.rmtree(file)  # Deletes the folder and its contents


def unzip_file(zip_file_path: str, destination_folder: str, delete_zip=False):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)

    if delete_zip:
        delete_file(zip_file_path)


def unzip_without_top_dir(zip_file_path, destination_folder, delete_zip=False):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Get the list of file paths in the zip
        members = zip_ref.namelist()
        
        # Identify the top-level directory (assume first path element)
        top_level_dir = os.path.commonprefix(members).rstrip('/')
        
        for member in members:
            # Remove the top-level directory from the file path
            relative_path = os.path.relpath(member, top_level_dir)
            
            # Compute the final extraction path
            final_path = os.path.join(destination_folder, relative_path)

            if member.endswith('/'):  # Handle directories
                os.makedirs(final_path, exist_ok=True)
            else:  # Extract files
                os.makedirs(os.path.dirname(final_path), exist_ok=True)
                with zip_ref.open(member) as src, open(final_path, 'wb') as dst:
                    dst.write(src.read())

    if delete_zip:
        delete_file(zip_file_path)


def go_to_url(url: str):
    # Opens the webbrowser with the provided url
    import webbrowser
    webbrowser.open(url, new=0, autoraise=True)


def python_virtual_environment(env_directory_path):
    # Setup a python virtual environmet
    os.makedirs(env_directory_path, exist_ok=True) # Ensure directory exists
    os.system(f'{sys.executable} -m venv "{env_directory_path}"')


def pip_install_packages_in_virtual_environment(env_directory_path, packages):
    if not os.path.exists(env_directory_path):
        print("Invalid path")
        raise Exception("Invalid path")
  
    my_os = platform.system()
    for package in packages:
        if my_os == "Windows":
            os.system(f'powershell; &"{env_directory_path}/Scripts/pip" install {package}')
        else:
            os.system(f'"{env_directory_path}/bin/pip" install {package}')


def get_site_packages_path(venv_path):
    """Returns the site-packages path for a given virtual environment."""
    python_version = f"python{sys.version_info.major}.{sys.version_info.minor}"
    
    # Construct the expected site-packages path
    if os.name == "nt":  # Windows
        site_packages_path = os.path.join(venv_path, "Lib", "site-packages")
    else:  # macOS/Linux
        site_packages_path = os.path.join(venv_path, "lib", python_version, "site-packages")

    return site_packages_path if os.path.exists(site_packages_path) else None


def use_other_venv_if_missing(package_name, other_venv_path):
    try:
        importlib.import_module(package_name)
        print(f"{package_name} is already installed in the current environment.")
    except ImportError:
        print(f"{package_name} not found. Using the package from the other environment.")
        other_venv_path = get_site_packages_path(other_venv_path)
        print(other_venv_path)
        sys.path.insert(0, other_venv_path)  # Add other venv's site-packages to sys.path


def run_command(command: str) -> None:
    """Run a command in the terminal"""
    platform_name = platform.system()
    if platform_name == "Windows": # Windows
        print("running command: ", f'powershell; &{command}')
        if command[0] != '"':
            os.system(f'powershell; {command}')
        else:
            os.system(f'powershell; &{command}')
    else:
        print("running command: ", f'{command}')
        os.system(command)


def download_file_from_google_drive(drive_url: str, output_file: str):
    def _extract_id_from_url(self, url: str):
        url2 = url.split("drive.google.com/file/d/")[1]
        file_id = url2.split("/")[0]
        return file_id
    
    def _download_large_file_from_google_drive(id, destination):
        use_other_venv_if_missing("gdown", get_directory_path(__file__, 0) + "/venv")
        import gdown
        # Construct the direct URL
        url = f"https://drive.google.com/uc?id={id}"

        # Download the file
        gdown.download(url, destination, quiet=False)

    file_id = _extract_id_from_url(drive_url)
    _download_large_file_from_google_drive(file_id, output_file)


def download_github_repo_as_zip(zip_url: str, output_zip_file: str):
    """Downloads a GitHub repository as a ZIP file.
    
    Args:
        repo_url (str): The URL of the GitHub repository (e.g., "https://github.com/owner/repo").
        output_file (str): The name of the output ZIP file (e.g., "repo.zip").
    """
    try:
        response = requests.get(zip_url, stream=True)
        response.raise_for_status()  # Raise an error for bad responses
        
        with open(output_zip_file, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        
        print(f"Download complete: {output_zip_file}")
    except Exception as e:
        print(f"Error: {e}")


def install_emsdk(output_directory: str):
    my_os = platform.system()
    if my_os == "Linux":
        # Download emsdk from git
        emsdk_git_url = "https://github.com/emscripten-core/emsdk/archive/refs/heads/main.zip"
        tmp_zip = get_directory_path(__file__, 0) + "/emsdk_temp.zip"
        download_github_repo_as_zip(emsdk_git_url, tmp_zip)
        unzip_file(tmp_zip, output_directory, True)

        # Install emsdk
        emsdk_path = output_directory + "/emsdk/emsdk"
        run_command('chmod +x "' + emsdk_path + '"')
        run_command('"' + emsdk_path + '" install latest')
        run_command('"' + emsdk_path + '" activate latest')
    elif my_os == "Windows":
        tmp_zip = get_directory_path(__file__, 0) + "/emsdk_temp.zip"
        google_drive_path = "TODO"
        download_file_from_google_drive(google_drive_path, tmp_zip)
        unzip_without_top_dir(tmp_zip, output_directory, True)

        old_name = output_directory + "/emsdk-win"
        new_name = output_directory + "emsdk"
        os.rename(old_name, new_name)


def download_file_from_url(file_path: str, file_url: str):
    # Ensure that parent directory exists
    os.makedirs(get_directory_path(file_path, 0), exist_ok=True)

    # Iterate through files and download them
    with urllib.request.urlopen(file_url) as f:
        html = f.read().decode('utf-8')
        with open(file_path, "w") as install_file: # Create install file
            install_file.write(html)