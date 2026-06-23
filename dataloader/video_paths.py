"""Path helpers for evaluation video outputs."""

import os
from typing import Optional


def checkpoint_dir(checkpoint_path: str) -> str:
    """Return the directory that contains a checkpoint path."""
    normalized_path = os.path.normpath(checkpoint_path)
    if os.path.isfile(normalized_path):
        return os.path.dirname(normalized_path)
    return normalized_path


def eval_video_root(checkpoint_path: Optional[str], checkpoints_dir: str) -> str:
    """Return the root directory for evaluation videos."""
    base_dir = checkpoint_dir(checkpoint_path) if checkpoint_path is not None else os.path.normpath(checkpoints_dir)
    return os.path.join(base_dir, "eval_videos")


def benchmark_video_dir(save_video_dir: str, benchmark_type: str) -> str:
    """Return the directory for a benchmark's evaluation videos."""
    return os.path.join(save_video_dir, benchmark_type)


def task_video_dir(save_video_dir: str, benchmark_type: str, task_name: str) -> str:
    """Return the directory for a task's evaluation videos."""
    return os.path.join(benchmark_video_dir(save_video_dir, benchmark_type), task_name)
