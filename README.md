# ppjson.py

## Installation
`pip install git+https://github.com/chris48s/ppjson.git`

## Usage

```
usage: ppjson.py [-h] [-i INDENT] [--header HEADER] url

Grab json from an API and format it nicely

positional arguments:
  url                           URL to grab json from

optional arguments:
  -h, --help                    show help
  -i INDENT, --indent INDENT    <Optional> Indent size
  -H HEADER, --header HEADER    <Optional> HTTP header (multiple -H arguments are allowed)
```

e.g:

`ppjson.py -i 4 -H "Accept: application/json" -H "Authorization: Bearer f00b42" "https://foo.bar/ugly.json" > pretty.json`
