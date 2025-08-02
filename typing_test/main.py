import argparse

from blessed import Terminal
from rich.console import Console

from reference_text import ReferenceText
from modes import timed_mode
from modes import perfect_mode
import settings

# TODO: create a new arg or an optional add on to the --timed-mode arg to
# override the time duration of timed mode


def parse_args() -> argparse.Namespace:
    """Parses command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--word-count", "-w", type=int, help="overrides word count for the current run"
    )
    parser.add_argument(
        "--difficulty",
        "-d",
        choices=["easy", "medium", "hard", "veryHard"],
        help="overrides difficulty for the current run",
    )
    parser.add_argument(
        "--show-config",
        action="store_true",
        help="opens settings.json in text editor to edit it",
    )
    parser.add_argument(
        "--timed-mode",
        action="store_true",
        help="overrides config and sets timed mode for current run",
    )
    parser.add_argument(
        "--perf-mode",
        action="store_true",
        help="overrides config and sets perfect mode for current run",
    )
    return parser.parse_args()


def main():
    # Parsing args first to bypass potential config errors
    args = parse_args()
    # and handling `--show-config` before reading the config as well so
    # it can be edited this way even if it's throwing errors
    if args.show_config:
        settings.show_config_file()
        return

    # Create_default_settings will only create a default JSON if one
    # does not already exist
    settings.create_default_settings()
    # Configuration is the programs copy of the JSON once its read, so
    # can be temporarily overwritten for the runtime of the program
    configuration = settings.read_settings()
    settings.check_settings_validity(configuration)

    # Handling remaining args

    # Validating conflicts before applying valid args
    if args.timed_mode and args.perf_mode:
        raise ValueError("You cannot enable both timed and perfect mode")
    if args.timed_mode and args.word_count:
        raise ValueError("Timed mode and word-count are incompatible settings")

    if args.word_count:
        configuration["word_count"] = args.word_count
    if args.difficulty:
        configuration["difficulty"] = args.difficulty
    if args.timed_mode:
        configuration["mode"] = "timed"
    if args.perf_mode:
        configuration["mode"] = "perfect"

    term = Terminal()
    console = Console()

    if configuration["mode"] == "perfect":
        rf = ReferenceText(configuration["word_count"], configuration["difficulty"])
        reference_text = rf.get_selected_chars()
        perfect_mode.run_perfect_mode(term, console, reference_text)
    elif configuration["mode"] == "timed":
        rf = ReferenceText(None, configuration["difficulty"])
        reference_text = rf.get_selected_chars()
        # TODO: pull existing duration settings from JSON item `timer`
        timed_mode.run_timed_mode(term, console, rf, reference_text, duration_sec=60)


if __name__ == "__main__":
    main()
