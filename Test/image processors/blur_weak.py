import sys
import image_processors
import dragndrop

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        dragndrop.drop(sys.argv[1], lambda x: image_processors.blur(x, 5))