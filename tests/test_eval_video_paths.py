from pathlib import Path

from dataloader.video_paths import (
    benchmark_video_dir,
    eval_video_root,
    task_video_dir,
)


def test_eval_video_root_uses_checkpoint_file_directory(tmp_path):
    checkpoint_dir = tmp_path / "logs" / "run_001" / "checkpoints"
    checkpoint_dir.mkdir(parents=True)
    checkpoint_file = checkpoint_dir / "final_model.pth"
    checkpoint_file.write_bytes(b"checkpoint")

    assert Path(eval_video_root(str(checkpoint_file), str(tmp_path / "unused"))) == checkpoint_dir / "eval_videos"


def test_eval_video_root_uses_checkpoint_directory_when_directory_is_provided(tmp_path):
    checkpoint_dir = tmp_path / "logs" / "run_001" / "checkpoints"
    checkpoint_dir.mkdir(parents=True)

    assert Path(eval_video_root(str(checkpoint_dir), str(tmp_path / "unused"))) == checkpoint_dir / "eval_videos"


def test_eval_video_root_uses_current_run_checkpoints_for_training_eval(tmp_path):
    checkpoints_dir = tmp_path / "logs" / "run_001" / "checkpoints"

    assert Path(eval_video_root(None, str(checkpoints_dir))) == checkpoints_dir / "eval_videos"


def test_task_video_dir_does_not_add_extra_videos_folder(tmp_path):
    root = tmp_path / "checkpoints" / "eval_videos"

    path = Path(task_video_dir(str(root), "libero_object_swap", "pick_up_the_bowl"))

    assert path == root / "libero_object_swap" / "pick_up_the_bowl"
    assert "videos" not in path.relative_to(root).parts


def test_benchmark_video_dir_uses_active_benchmark_name(tmp_path):
    root = tmp_path / "checkpoints" / "eval_videos"

    assert Path(benchmark_video_dir(str(root), "libero_object")) == root / "libero_object"
    assert Path(benchmark_video_dir(str(root), "libero_object_swap")) == root / "libero_object_swap"
