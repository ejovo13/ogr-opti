FROM rust

RUN apt-get update
RUN apt-get install -y python3 python3-pip curl fish python3-full pipx

RUN pipx install ogr-py

ENV PATH="${PATH}:/root/.local/bin"
CMD fish