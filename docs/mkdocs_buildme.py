import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[0]))
sys.path.append(str(Path(__file__).resolve().parents[1]))
sys.path.append(str(Path(__file__).resolve().parents[2]))
sys.path.append(str(Path(__file__).resolve().parents[3]))
sys.path.append(str(Path(__file__).resolve().parents[4]))
sys.path.append(str(Path(__file__).resolve().parents[5]))

from vicmil_pip.packages.pyMkDocs import *

def zip_to_tree_link(zip_url: str) -> str:
    """
    Converts a GitHub ZIP archive URL of a branch to the corresponding tree URL.

    Example:
    https://github.com/user/repo/archive/refs/heads/branch.zip
    => https://github.com/user/repo/tree/branch
    """
    import re

    pattern = r"(https://github\.com/[^/]+/[^/]+)/archive/refs/heads/([^.]+)\.zip"
    match = re.match(pattern, zip_url)

    if match:
        base_url, branch = match.groups()
        return f"{base_url}/tree/{branch}"
    else:
        raise ValueError("Invalid GitHub ZIP branch URL format.")

def build_package_index():
    """
    Update the package index with the latest information about all the packages
    """
    from vicmil_pip import installer
    packages = installer.get_packages()

    file_contents = "# List of packages\n\n"
    package_counter = 0
    for package in packages.keys():
        package_counter += 1
        file_contents += f"## {package_counter}. {packages[package].name}" + "\n\n"
        file_contents += packages[package].description + "\n\n"

        if hasattr(packages[package], 'github_repo') and packages[package].github_repo:
            tree_link = zip_to_tree_link(packages[package].github_repo)
            file_contents += f"github_repo: [{tree_link}]({tree_link})" + "\n\n"

        if len(packages[package].dependencies) > 0:
            file_contents += f"dependencies: {packages[package].dependencies}" + "\n\n"

        file_contents += "\n"

        package_info_file = installer.get_directory_path(__file__, 0) + "/docs/docs/package_info.md"

        with open(package_info_file, "w+") as file:
            file.write(file_contents)


if __name__ == "__main__":
    build_package_index()
    compile_mkdocs(get_directory_path(__file__) + "/docs")