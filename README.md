Simple Python-based webserver that simply mirrors the browser HTTP headers back to the browser.

```bash
docker run --rm --network=host deanturpin/http
```

Hit the server with your browser: `http://localhost:8080`

And you will be presented with the browser heads included in the `GET` request.

```bash
MIRROR BROWSER HEADERS - 2025-02-24 13:00:42.639989

accept-language en-GB,en-US;q=0.9,en;q=0.8
accept-encoding gzip, deflate, br, zstd
sec-fetch-site none
connection keep-alive
accept text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
```
