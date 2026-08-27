FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

RUN curl -LsSf https://astral.sh/uv/0.10.11/install.sh | env UV_INSTALL_DIR=/usr/local/bin sh

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_INSTALL_DIR=/usr/local/share/uv/python \
    UV_PYTHON_PREFERENCE=only-managed

RUN mkdir -p /usr/local/share/uv/python \
    && uv python install 3.9
