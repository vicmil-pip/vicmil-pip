"""
This is the installer that contains all information for how to install things
"""

import platform
import inspect
import zipfile
import os
import pathlib
import shutil
import importlib
import sys
import urllib.request
import subprocess
from typing import Dict
import time
sys.path.append(str(pathlib.Path(__file__).resolve().parents[0])) 

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
    

class GitPackage(Package):
    def __init__(self):
        self.github_repo = None

    def install(self):
        package_path = get_directory_path(__file__, 0) + "/packages/" + self.name
        tmp_zip = get_directory_path(__file__, 0) + "/temp.zip"
        download_github_repo_as_zip(self.github_repo, tmp_zip)
        unzip_without_top_dir(tmp_zip, package_path, delete_zip=True)
        if os.path.exists(f"{package_path}/setup.py"):
            run_command(f'"{sys.executable}" "{package_path}/setup.py"')


class Packages:
    class cppEmsdk(GitPackage):
        def __init__(self):
            self.name = "cppEmsdk"
            self.description = "emscripten, used for compiling c++ for the web"
            self.dependencies = ["pyUtil"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-cpp-packages/archive/refs/heads/cppEmsdk.zip"


    class cppCompiler(GitPackage):
        def __init__(self):
            self.name = "cppCompiler"
            self.description = "!unstable! basic gcc compiler for windows or linux"
            self.dependencies = ["pyUtil"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-cpp-packages/archive/refs/heads/cppBasicCompiler.zip"
            
            
    class cppBuild(GitPackage):
        def __init__(self):
            self.name = "cppBuild"
            self.description = "Help tools for building c++ projects"
            self.dependencies = ["pyUtil"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-cpp-packages/archive/refs/heads/cppBuild.zip"


    class cppBasics(GitPackage):
        def __init__(self):
            self.name = "cppBasics"
            self.description = "c++ utility files, only requiring a c++11 compiler. Also includes some utility files when compiling for the browser"
            self.dependencies = ["cppBuild"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-cpp-packages/archive/refs/heads/cppBasics.zip"
            

    class cppOpengl(GitPackage):
        def __init__(self):
            self.name = "cppOpengl"
            self.description = "c++ utility files, and opengl+sdl library for building graphics applications"
            self.dependencies = ["cppBasics"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-cpp-packages/archive/refs/heads/cppOpengl.zip"

    
    class cppStb(GitPackage):
        def __init__(self):
            self.name = "cppStb"
            self.description = "c++ utility files, and stb library for loading images and fonts in c++"
            self.dependencies = ["cppBasics"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-cpp-packages/archive/refs/heads/cppStb.zip"


    class cppGlm(GitPackage):
        def __init__(self):
            self.name = "cppGlm"
            self.description = "c++ utility files, and glm library for math aimed at graphics and linear algebra"
            self.dependencies = ["cppBasics"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-cpp-packages/archive/refs/heads/cppGlm.zip"


    class cppSocketIOClient(GitPackage):
        def __init__(self):
            self.name = "cppSocketIOClient"
            self.description = "c++ utility files, and socket io client library for building networking apps"
            self.dependencies = ["cppBasics"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-cpp-packages/archive/refs/heads/cppSocketIOClient.zip"

    
    class cppMiniz(GitPackage):
        def __init__(self):
            self.name = "cppMiniz"
            self.description = "c++ utility files, and miniz library for zipping/unzipping files"
            self.dependencies = ["cppBasics"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-cpp-packages/archive/refs/heads/cppMiniz.zip"

    
    class cppTinyObjLoader(GitPackage):
        def __init__(self):
            self.name = "cppTinyObjLoader"
            self.description = "c++ utility files, and tiny obj loader library for loading .obj files"
            self.dependencies = ["cppBasics", "cppMiniz"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-cpp-packages/archive/refs/heads/cppTinyObjLoader.zip"


    class cppBinPacking(GitPackage):
        def __init__(self):
            self.name = "cppBinPacking"
            self.description = "c++ utility files, and smol-atlas library for packing 2d rectangles on a 2d surface"
            self.dependencies = ["cppBasics"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-cpp-packages/archive/refs/heads/cppBinPacking.zip"

    
    class cppEigen(GitPackage):
        def __init__(self):
            self.name = "cppEigen"
            self.description = "c++ utility files, and eigen library for various math operations"
            self.dependencies = ["cppBasics"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-cpp-packages/archive/refs/heads/cppEigen.zip"

    
    class cppBindings(GitPackage):
        def __init__(self):
            self.name = "cppBindings"
            self.description = "!unstable! utility files for building c++ bindings, especially to python"
            self.dependencies = ["cppBasics"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-cpp-packages/archive/refs/heads/cppBindings.zip"


    class cppVicmilGui(GitPackage):
        def __init__(self):
            self.name = "cppVicmilGui"
            self.description = "!unstable! c++ utility files for building cross-platform graphics applications in c++"
            self.dependencies = [
                "cppBasics", 
                "cppOpengl", 
                "cppStb", 
                "cppGlm", 
                "cppTinyObjLoader", 
                "cppBinPacking",
                "assetFonts"
            ]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-cpp-packages/archive/refs/heads/cppVicmilGui.zip"

    
    class cppMingwStdThreads(GitPackage):
        def __init__(self):
            self.name = "cppMingwStdThreads"
            self.description = "c++ files for fixing missing threads implementation in mingw compiler on windows"
            self.dependencies = [
                "cppBasics"
            ]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-cpp-packages/archive/refs/heads/cppMingwStdThreads.zip"


    class assetFonts(GitPackage):
        def __init__(self):
            self.name = "assetFonts"
            self.description = "some fonts, free to use, supporting a wide range of languages"
            self.dependencies = []
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-assets/archive/refs/heads/assetFonts.zip"


    class assetVitB(GitPackage):
        def __init__(self):
            self.name = "assetsVitB"
            self.description = "vitB is a ML model used by segment anything https://github.com/facebookresearch/segment-anything"
            self.dependencies = []
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-assets/archive/refs/heads/vitB.zip"


    class jsNvm(GitPackage):
        def __init__(self):
            self.name = "jsNvm"
            self.description = "!unstable! python utility files, and nvm(node version manager), for building node applications, including react"
            self.dependencies = []
            self.github_repo: str = None

    
    class pyCertBot(GitPackage):
        def __init__(self):
            self.name = "pyCertBot"
            self.description = "Automatically set up an ssl certificate for https traffic using certbot"
            self.dependencies = ["pyUtil"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-python-packages/archive/refs/heads/pyCertBot.zip"

    
    class pyMkDocs(GitPackage):
        def __init__(self):
            self.name = "pyMkDocs"
            self.description = "python utility files, and mkdocs library or creating documentation"
            self.dependencies = ["pyUtil"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-python-packages/archive/refs/heads/pyMkDocs.zip"

    
    class pyGitUtil(GitPackage):
        def __init__(self):
            self.name = "pyGitUtil"
            self.description = "!unstable! python utility files, and flask to host documentation"
            self.dependencies = ["pyUtil"]
            self.github_repo: str = None


    class pyFlaskUtil(GitPackage):
        def __init__(self):
            self.name = "pyFlaskUtil"
            self.description = "!unstable! python utility functions, and flask"
            self.dependencies = ["pyUtil"]
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-python-packages/archive/refs/heads/pyFlaskUtil.zip"


    class pyUtil(GitPackage):
        def __init__(self):
            self.name = "pyUtil"
            self.description = "python utility functions"
            self.dependencies = []
            self.github_repo: str = "https://github.com/vicmil-pip/vicmil-pip-python-packages/archive/refs/heads/pyUtil.zip"


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
    dirs = os.listdir(get_directory_path(__file__, 0) + "/packages")
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


def get_directory_path(__file__in, up_directories=0):
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


def get_venv_pip_path(env_directory_path):
    if platform.system() == "Windows":
        return f'{env_directory_path}/Scripts/pip'
    else:
        return f'{env_directory_path}/bin/pip'
    

def pip_install_packages_in_virtual_environment(env_directory_path, packages):
    if not os.path.exists(env_directory_path):
        print("Invalid path")
        raise Exception("Invalid path")
    
    for package in packages:
        run_command(f'"{get_venv_pip_path(env_directory_path)}" install {package}')
             

def python_virtual_environment(env_directory_path):
    # Setup a python virtual environmet
    os.makedirs(env_directory_path, exist_ok=True) # Ensure directory exists
    run_command(f'"{sys.executable}" -m venv "{env_directory_path}"')


def run_command(command: str) -> None:
    """Run a command in the terminal"""
    if platform.system() == "Windows": # Windows
        win_command = None
        if command[0] != '"':
            win_command = f'powershell; {command}'
        else:
            win_command = f'powershell; &{command}'

        print("running command: ", f'{win_command}')
        os.system(win_command)
    else:
        print("running command: ", f'{command}')
        os.system(command)


def get_venv_site_packages_path(venv_path):
    """Returns the site-packages path for a given virtual environment."""
    python_version = f"python{sys.version_info.major}.{sys.version_info.minor}"
    
    # Construct the expected site-packages path
    if platform.system() == "Windows": # Windows
        # The site package path may vary on windows, so we check for both
        site_packages_path = os.path.join(venv_path, "Lib", "site-packages")
        if not os.path.exists(site_packages_path):
            site_packages_path = os.path.join(venv_path, "lib", python_version, "site-packages")
    else:  # macOS/Linux
        site_packages_path = os.path.join(venv_path, "lib", python_version, "site-packages")

    return site_packages_path if os.path.exists(site_packages_path) else None


def module_installed(module_name: str) -> bool:
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False
    

def include_other_venv(other_venv_path: str):
    site_package_path = get_venv_site_packages_path(other_venv_path)
    if not other_venv_path in sys.path:
        print("Updating sys.path with other venv", site_package_path)
        sys.path.append(site_package_path)  # Add other venv's site-packages to sys.path
    

class PipManager:
    def __init__(self):
        self._modules = list()
        self.venv_path = get_directory_path(__file__) + "/venv"
        self.installed_pip_packages = list()

    def add_module(self, module_name: str, pip_package_if_missing: str):
        self._modules.append((module_name, pip_package_if_missing))

    def add_pip_package(self, pip_package: str):
        self._modules.append((None, pip_package))

    def include_other_venv(self):
        include_other_venv(self.venv_path)

    def install_missing_modules(self):
        """
        [vmdoc:start]
        # PipManager.install_missing_modules()

        Tries to see if the module is available, 
            if it fails, it installs the missing pip packages inside self.venv_path
        [vmdoc:end]
        """
        missing_pip_packages = set()

        for module_name, pip_package in self._modules:
            if not module_name or not module_installed(module_name=module_name):
                if not pip_package in self.installed_pip_packages:
                    missing_pip_packages.add(pip_package)
                    self.installed_pip_packages.append(pip_package)

        if len(missing_pip_packages) > 0:
            if not os.path.exists(self.venv_path):
                python_virtual_environment(self.venv_path)

            missing_pip_packages = list(missing_pip_packages)
            pip_install_packages_in_virtual_environment(self.venv_path, missing_pip_packages)

            self.include_other_venv()


def download_github_repo_as_zip(zip_url: str, output_zip_file: str):
    """Downloads a GitHub repository as a ZIP file.
    
    Args:
        repo_url (str): The URL of the GitHub repository (e.g., "https://github.com/owner/repo").
        output_file (str): The name of the output ZIP file (e.g., "repo.zip").
    """
    try:
        pip_manager = PipManager()
        if not module_installed("requests"):
            pip_manager.add_pip_package("requests")
            pip_manager.install_missing_modules()

        import requests
        response = requests.get(zip_url, stream=True)
        response.raise_for_status()  # Raise an error for bad responses
        
        with open(output_zip_file, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        
        print(f"Download complete: {output_zip_file}")
    except Exception as e:
        print(f"Error: {e}")