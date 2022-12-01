import logging

from ongaku import ongaku

from .loop import loop_,reset_bio

logging.basicConfig(level=logging.ERROR)


if __name__ == "__main__":
    try:
        ongaku.run(loop_())
    except KeyboardInterrupt:
        ongaku.run(reset_bio())
        print("\nOngaku: Stopped")
