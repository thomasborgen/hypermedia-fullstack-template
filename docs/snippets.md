# base64 encode a key to clipboard

```sh
openssl base64 -in key.json | tr -d '\n' | pbcopy
```
