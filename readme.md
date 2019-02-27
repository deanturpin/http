Simple Python-based webserver that mirrors the browser HTTP headers back to the
browser.

Launch server on common ports.
```bash
docker run --rm -d -p   80:8080 deanturpin/http
docker run --rm -d -p  443:8080 deanturpin/http
docker run --rm -d -p 8080:8080 deanturpin/http
```
