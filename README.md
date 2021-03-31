# Simple Mandarin Ruby

Basic Anki addon for annotating Chinese characters with pinyin [ruby text](https://en.wikipedia.org/wiki/Ruby_character) in an ad-hoc manner.

Uses [pypinyin](https://github.com/mozillazg/python-pinyin) with a more comprehensive phrase dictionary to try and get better results.

In early stages so functionality is very basic:

- Designed to work only on plain, unformatted text. May remove or mess up existing formatting.
- Ruby markup is character by character, which has the side-effect of making multi-character word selection a pain.
- No customization options like numbered tones / bopomofo / colours / bracketed output.
- No included functionality for overwriting/removing existing ruby. Anki's built-in undo should at least work though.
- Only tested on Anki 2.1.40.
- Not available on AnkiWeb.

## Installation

### Requirements

- Python >= 3.3 with pip
- `curl` in `PATH`
    - Windows users: should already be present in recent versions of Windows 10 (`curl.exe`)

### Building

Note: Currently only one build dependency needs installing ([`vendorize`](https://pypi.org/project/vendorize/)), but you may prefer to create and activate a Python virtual environment first anyway.

From the repo's root directory run the appropriate commands:

#### Windows command prompt
```
py -m pip install -r requirements-dev.txt
build.cmd
```

#### Bash / Linux shell
```
python -m pip install -r requirements-dev.txt
./build
```

### Copying

Assuming the build succeeds, copy (or symlink) the `src` directory to your Anki addon directory and rename it to `simple-mandarin-ruby` or something else appropriate.

## Licenses

This project's code is [licensed under GPLv3](./LICENSE).

### Dependencies

pypinyin code is [licensed under the MIT License](https://github.com/mozillazg/python-pinyin/blob/master/LICENSE.txt).

[Character pinyin data](https://github.com/mozillazg/pinyin-data) is partially derived from the [Unihan Database](http://www.unicode.org/charts/unihan.html) ([license](https://www.unicode.org/license.html)) and [ZDIC](https://www.zdic.net/) ([public domain / CC0](https://www.zdic.net/aboutus/copyright/)).
  
[Phrase pinyin data](https://github.com/mozillazg/phrase-pinyin-data) is partially derived from [CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cc-cedict) ([licensed under CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)) and ZDIC.

[`ruby.svg` (the Ruby logo)](https://commons.wikimedia.org/wiki/File:Ruby_logo.svg) is [licensed under CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/).