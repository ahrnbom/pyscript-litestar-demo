# pyscript-litestar-demo
Demonstration of how to use Pyscript and Litestar together, to run web software with Python on both frontend and backend

## Main points demonstrated
* The same `msgspec` models can be used across both server and client. This is similar to the workflow commonly used in Javascript libraries, where Javascript runs on both the server and the browser client, except you don't need all the wonk inherent to Javascript.
* Taking advantage of modern Python type hints. Open this project in VS Code, with the Python extension, and you will see that it fully understands the type of every variable in this project. Furthermore, `mypy` is used to statically analyze the code for type errors.
* A .pyi file is used to provide type hints for Pyscript, which would otherwise not be possible. This currently only support the precise functionality used in this demo project, but the concept could be expanded to cover all Web APIs provided.
* The somewhat strange design of the `fetch` function in Pyscript, which differs somewhat in its API from its Javascript counterpart.

## Instructions
`./run.sh`
Then visit `localhost:8000` in a browser