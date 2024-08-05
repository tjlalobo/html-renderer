# HTML Renderer

Infrastructure for Rendering dynamic (and, static) html content in a headless chromium environment.

## Building the project

**Requirement**: Docker Desktop version=4.x installation.

```bash
$ git clone https://github.com/tjlalobo/html-renderer.git
$ cd html-renderer
$ docker build -t html-renderer .
```

## Usage

Run the below command passing in the url of the html to render as an argument.

```bash
$ docker run -it --rm html-renderer render-html <url>
```

## License

[MIT](https://choosealicense.com/licenses/mit/)