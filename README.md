# GridMaker-pip

A simple pip package to turn URLs of images to a stitched grid.

## Usage

1. Install the package:

    ```bash
    $ pip3 install gridmaker-pip
    ```

2. Create a JSON file/list in the following format:

    ```json
    [
        "https://url0.xyz/image0",
        "https://url1.xyz/image1",
        ...
    ]
    ```

3. Run the program:

    ```bash
    $ gridmaker

    === GridMaker 1.0 ===
    Location of the JSON list:  list.json
    Output file path (with the name of the file): grid.jpg
    Width of a single grid item (min 10): 100
    Height of a single grid item (min 10): 100
    Horizontal size of the grid image (min 2): 16
    Vertical size of the grid image (min 2): 9
    ```

### With Args

**Example:**

*Will generate an image grid made out of 17x17 images, each 200x200 big.*

```bash
$ gridmaker -i list.json -o grid.jpeg --width 200 --height 200 --vertical 17 --horizontal 17 --no-cache -v
```

```
usage: gridmaker [-h] [-i json_path] [-o image_path] [--no-cache] [--clear-cache] [--width width] [--height height] [--horizontal size] [--vertical size] [-v]

Turn image urls to a grid

optional arguments:
  -h, --help         show this help message and exit
  -v                 Output all steps

Input/Output:
  -i json_path       The input JSON file containing a list of URLs
  -o image_path      The output JPEG file

Cache:
  --no-cache         Do not use cache
  --clear-cache      Clear the cache

Size:
  --width width      The width of single images
  --height height    The height of single images
  --horizontal size  The number of images horizontally
  --vertical size    The number of images vertically
```

## Thanks

- *Thanks to [Nikolai Janakiev](https://gist.github.com/njanakiev) for sharing his [concat_images.py](https://gist.github.com/njanakiev/1932e0a450df6d121c05069d5f7d7d6f) GIST. It has saved me a lot of time :D.*

## [License](LICENSE.md)

[Apache License - Version 2.0 , January 2004](http://www.apache.org/licenses/)
