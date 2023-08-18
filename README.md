Having a .dockerignore is crucial for the docker build otherwise it copies the local .venv over into the image and breaks the virtual environment

When installing optional dependencies for python packages in zsh you need to wrap it in single quotes because zsh uses square brackets for pattern matching