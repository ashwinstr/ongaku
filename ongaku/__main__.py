import logging

from ongaku import venom
from .song import reset_bio

logging.basicConfig(level=logging.ERROR)


if __name__ == "__main__":
    try:
        venom.run()
    except KeyboardInterrupt:
        venom.run(reset_bio())
        print("\nOngaku: Stopped")
