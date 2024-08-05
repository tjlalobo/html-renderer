# HTML Renderer

Infrastructure for rendering html content (dynamic and static) in a headless chromium environment.

## Building the project

**Requirement**: Docker Desktop version=4.x installation.

```bash
$ git clone https://github.com/tjlalobo/html-renderer.git
$ cd html-renderer
$ docker build -t html-renderer .
```

## Usage

Run the below command passing in the url of the html page to render as an argument.

```bash
$ docker run -it --rm html-renderer render-html \
> https://toscrape.com/ > scraping_sandbox.html
```

## License

[MIT](https://choosealicense.com/licenses/mit/)