FROM ubuntu:24.04

ADD https://github.com/astral-sh/uv/releases/download/0.13.1/uv-x86_64-unknown-linux-gnu.tar.gz /tmp/uv.tar.gz
RUN tar --strip-components=1 -xzf /tmp/uv.tar.gz -C /usr/bin
WORKDIR /usr/src/app
COPY . .
RUN uv sync
CMD ["uv", "run", "demo-repository-2"]
