import time
import argparse

from blessed import Terminal
from rich.console import Console

from reference_text import ReferenceText
from modes import timed_mode
from modes import perfect_mode
import settings
import input_handler
import renderer
import metrics


def parse_args():
    """parses command line arguments"""
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
        "--timed-mode", action="store_true", help="switches test mode to timed test"
    )
    parser.add_argument(
        "--perf-mode", action="store_true", help="switches test mode to perfect test"
    )
    return parser.parse_args()


def main():
    # parsing args first to bypass potential config errors
    args = parse_args()
    # and handling show config before reading the config as well so it
    # can be edited this way even if its throwing errors
    if args.show_config:
        settings.show_config_file()
        return

    term = Terminal()
    console = Console()

    # create_default_settings will only create a default JSON if one
    # does not already exist
    settings.create_default_settings()
    # configuration is the programs copy of the JSON once its read, so
    # can be temporarily overwritten for the runtime of the program
    configuration = settings.read_settings()
    settings.check_settings_validity(configuration)

    # handling remaining args
    if args.word_count:
        configuration["word_count"] = args.word_count
    if args.difficulty:
        configuration["difficulty"] = args.difficulty
    if args.timed_mode and args.perf_mode:
        raise ValueError("You cannot enable both timed and perfect mode")
    if args.timed_mode:
        configuration["mode"] = "timed"
    if args.perf_mode:
        configuration["mode"] = "perfect"

    # TODO: generate enough text for the user to keep typing for the
    # entire duration in timed mode, either move this logic below to the
    # individual mode modules, or handle it here
    rf = ReferenceText(configuration["word_count"], configuration["difficulty"])
    reference_text = rf.get_selected_chars()

    if configuration["mode"] == "perfect":
        perfect_mode.run_perfect_mode(term, console, reference_text)
    elif configuration["mode"] == "timed":
        timed_mode.run_timed_mode(term, console, reference_text, duration_sec=10)


if __name__ == "__main__":
    main()
