# Phash Python Bindings

Python bindings to [libphash](http://www.phash.org/).

libphash paper: http://www.phash.org/docs/pubs/thesis_zauner.pdf

## Usage

Requirements
* ImageMagick (for generating the test image set)
* libphash (for hashing, duh)

```bash
./generate_images.sh
python test_hashing.py
```

TODO:
* Include textual hash functions in python bindings
* Include setup.py to make this package redistributable
