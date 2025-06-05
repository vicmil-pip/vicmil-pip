# List of packages

## 1. assetFonts

some fonts, free to use, supporting a wide range of languages

github_repo: [https://github.com/vicmil-pip/vicmil-pip-assets/tree/assetFonts](https://github.com/vicmil-pip/vicmil-pip-assets/tree/assetFonts)


## 2. assetsVitB

vitB is a ML model used by segment anything https://github.com/facebookresearch/segment-anything

github_repo: [https://github.com/vicmil-pip/vicmil-pip-assets/tree/vitB](https://github.com/vicmil-pip/vicmil-pip-assets/tree/vitB)


## 3. cppBasics

c++ utility files, only requiring a c++11 compiler. Also includes some utility files when compiling for the browser

github_repo: [https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppBasics](https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppBasics)

dependencies: ['cppBuild']


## 4. cppBinPacking

c++ utility files, and smol-atlas library for packing 2d rectangles on a 2d surface

github_repo: [https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppBinPacking](https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppBinPacking)

dependencies: ['cppBasics']


## 5. cppBindings

!unstable! utility files for building c++ bindings, especially to python

github_repo: [https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppBindings](https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppBindings)

dependencies: ['cppBasics']


## 6. cppBuild

Help tools for building c++ projects

github_repo: [https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppBuild](https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppBuild)

dependencies: ['pyUtil']


## 7. cppCompiler

!unstable! basic gcc compiler for windows or linux

github_repo: [https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppBasicCompiler](https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppBasicCompiler)

dependencies: ['pyUtil']


## 8. cppEigen

c++ utility files, and eigen library for various math operations

github_repo: [https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppEigen](https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppEigen)

dependencies: ['cppBasics']


## 9. cppEmsdk

emscripten, used for compiling c++ for the web

github_repo: [https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppEmsdk](https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppEmsdk)

dependencies: ['pyUtil']


## 10. cppGlm

c++ utility files, and glm library for math aimed at graphics and linear algebra

github_repo: [https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppGlm](https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppGlm)

dependencies: ['cppBasics']


## 11. cppMingwStdThreads

c++ files for fixing missing threads implementation in mingw compiler on windows

github_repo: [https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppMingwStdThreads](https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppMingwStdThreads)

dependencies: ['cppBasics']


## 12. cppMiniz

c++ utility files, and miniz library for zipping/unzipping files

github_repo: [https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppMiniz](https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppMiniz)

dependencies: ['cppBasics']


## 13. cppOpengl

c++ utility files, and opengl+sdl library for building graphics applications

github_repo: [https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppOpengl](https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppOpengl)

dependencies: ['cppBasics']


## 14. cppSocketIOClient

c++ utility files, and socket io client library for building networking apps

github_repo: [https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppSocketIOClient](https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppSocketIOClient)

dependencies: ['cppBasics']


## 15. cppStb

c++ utility files, and stb library for loading images and fonts in c++

github_repo: [https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppStb](https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppStb)

dependencies: ['cppBasics']


## 16. cppTinyObjLoader

c++ utility files, and tiny obj loader library for loading .obj files

github_repo: [https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppTinyObjLoader](https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppTinyObjLoader)

dependencies: ['cppBasics', 'cppMiniz']


## 17. cppVicmilGui

!unstable! c++ utility files for building cross-platform graphics applications in c++

github_repo: [https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppVicmilGui](https://github.com/vicmil-pip/vicmil-pip-cpp-packages/tree/cppVicmilGui)

dependencies: ['cppBasics', 'cppOpengl', 'cppStb', 'cppGlm', 'cppTinyObjLoader', 'cppBinPacking', 'assetFonts']


## 18. jsNvm

!unstable! python utility files, and nvm(node version manager), for building node applications, including react


## 19. pyCertBot

Automatically set up an ssl certificate for https traffic using certbot

github_repo: [https://github.com/vicmil-pip/vicmil-pip-python-packages/tree/pyCertBot](https://github.com/vicmil-pip/vicmil-pip-python-packages/tree/pyCertBot)

dependencies: ['pyUtil']


## 20. pyFlaskUtil

!unstable! python utility functions, and flask

github_repo: [https://github.com/vicmil-pip/vicmil-pip-python-packages/tree/pyFlaskUtil](https://github.com/vicmil-pip/vicmil-pip-python-packages/tree/pyFlaskUtil)

dependencies: ['pyUtil']


## 21. pyGitUtil

!unstable! python utility files, and flask to host documentation

dependencies: ['pyUtil']


## 22. pyMkDocs

python utility files, and mkdocs library or creating documentation

github_repo: [https://github.com/vicmil-pip/vicmil-pip-python-packages/tree/pyMkDocs](https://github.com/vicmil-pip/vicmil-pip-python-packages/tree/pyMkDocs)

dependencies: ['pyUtil']


## 23. pyUtil

python utility functions

github_repo: [https://github.com/vicmil-pip/vicmil-pip-python-packages/tree/pyUtil](https://github.com/vicmil-pip/vicmil-pip-python-packages/tree/pyUtil)


