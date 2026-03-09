import argparse
import logging
from src.pipeline import run_pipeline


def main():

    # -------------------------
    # Logging configuration
    # -------------------------
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # -------------------------
    # CLI arguments
    # -------------------------
    parser = argparse.ArgumentParser(
        description="Countries Data Engineering Pipeline"
    )

    parser.add_argument(
        "--output",
        default="sqlite",
        choices=["sqlite", "parquet"],
        help="Output target: sqlite or parquet"
    )

    args = parser.parse_args()

    # -------------------------
    # Run pipeline
    # -------------------------
    run_pipeline(args.output)


if __name__ == "__main__":
    main()