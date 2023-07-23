
import src.config.config_defaults as cf
from src.wrapper.rate_wrapper import RateDownloaderWrapper


if __name__ == "__main__":
    RateDownloaderWrapper(threads=cf.THREADS_NUMBER).call()
