#!/bin/bash

STUBS=./stubs-tmp/

python3 -m venv venv && \
. ./venv/bin/activate && \
pip install litestar[standard] msgspec black mypy numpy
black -q demo/ && \
mkdir -p $STUBS && \
cp ./demo/client/pyscript.pyi $STUBS && \
MYPYPATH=$STUBS mypy demo && \
uvicorn demo.server:app --host 0.0.0.0
