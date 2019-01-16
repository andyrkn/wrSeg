import sys
import image_processors
import dragndrop

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        dragndrop.drop(sys.argv[1], image_processors.pixalate)