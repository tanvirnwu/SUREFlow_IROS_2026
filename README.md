<h4 align="center"><strong><a href="https://2026.ieee-iros.org/">Accepted at IEEE/RSJ International Conference on Intelligent Robots & Systems (IROS) 2026, Pittsburgh, PA, USA</a></strong></h4>
<h2 align="center"><strong>SUREFlow: State-space Uncertainty-aware REsidual Flow Matching for Robust Robot Manipulation</a></strong> (<strong><a href="https://arxiv.org/pdf/2607.10504">Paper</a>)</h2>
<h6 align="center">Md Tanvir Islam, Sai Navaneet Peddapalli, Sangmoon Lee, Sangtae Ahn<sup>*</sup></h6>
<h6 align="center">Kyungpook National University, Daegu 41566, Republic of Korea | *Corresponding Author</h6> 
<hr>

## SUREFlow Architecture
Our SUREFlow is a mamba based lightweight (179M) vision-language-action model for Robot Manipulation.

![](./assets/SUREFlow_IROS_2026.jpg)


## LIBERO Benchmark Results
| Method | Venue | Spatial | Object | Goal | Long | Average |
|---|---|---:|---:|---:|---:|---:|
| Octo [13] | RSS'24 | 78.9 | 85.7 | 84.6 | 51.1 | 75.1 |
| QueST [16] | NeurIPS'24 | 89.0 | 90.0 | 88.4 | 87.0 | 88.6 |
| MAIL [3] | CoRL'24 | 53.8 | 81.5 | 56.3 | 41.7 | 58.3 |
| TraceVLA [17] | ICLR'25 | 84.6 | 85.2 | 75.1 | 54.1 | 74.8 |
| **SUREFlow (Ours)** | **IROS'26** | **94.8** | **91.0** | **93.8** | **90.2** | **92.5** |

## LIBERO-PRO Benchmark Results
**TABLE II**

**LIBERO-PRO model leaderboard showing normalized success rates under five perturbation types across four benchmarks.**

| Model | Goal Obj | Goal Pos | Goal Sem | Goal Task | Goal Env | Spatial Obj | Spatial Pos | Spatial Sem | Spatial Task | Spatial Env | LIBERO-10 Obj | LIBERO-10 Pos | LIBERO-10 Sem | LIBERO-10 Task | LIBERO-10 Env | Object Obj | Object Pos | Object Sem | Object Task | Object Env | Average SR ↑ | Params ↓ |
|:------|---------:|---------:|---------:|----------:|---------:|------------:|------------:|------------:|-------------:|------------:|--------------:|--------------:|--------------:|---------------:|--------------:|-----------:|-----------:|-----------:|------------:|-----------:|-------------:|---------:|
| OpenVLA [12] | 0.96 | 0.00 | 0.98 | 0.00 | 0.98 | 0.97 | 0.00 | 0.97 | 0.00 | 0.89 | 0.81 | 0.00 | 0.96 | 0.00 | 0.85 | 0.98 | 0.00 | 0.98 | 0.00 | 0.00 | 0.52 | 7B |
| π0 [28] | 0.94 | 0.00 | 0.93 | 0.00 | 0.39 | 0.95 | 0.00 | 0.97 | 0.00 | 0.60 | 0.79 | 0.00 | 0.82 | 0.00 | 0.27 | 0.94 | 0.00 | 0.90 | 0.00 | 0.29 | 0.44 | 3B |
| π0.5 [15] | 0.97 | 0.38 | 0.97 | 0.00 | 0.46 | 0.97 | 0.20 | 0.97 | 0.01 | 0.46 | 0.92 | 0.08 | 0.93 | 0.01 | 0.46 | 0.98 | 0.17 | 0.96 | 0.01 | 0.73 | **0.53** | 3B |
| **SUREFlow (Ours)** | 0.93 | 0.00 | 0.89 | 0.00 | 0.93 | 0.92 | 0.00 | 0.90 | 0.00 | 0.93 | 0.21 | 0.00 | 0.78 | 0.00 | 0.74 | 0.68 | 0.00 | 0.94 | 0.00 | 0.91 | 0.49 | **179.1M** |

# SUREFlow

SUREFlow supports training on LIBERO suites and evaluating a trained checkpoint on either:
- the same vanilla LIBERO suite, or
- a LIBERO-PRO variant of that suite.

This is done by decoupling:
- **train suite**: dataset + training language embeddings
- **eval suite**: simulator benchmark + evaluation language embeddings


When `--eval_suite` is set, simulator benchmark becomes:
`<train_suite>_<eval_suite>`

Examples:
- `train_suite=libero_goal`, `eval_suite=object` -> sim benchmark `libero_goal_object`

## Training
Train on a vanilla LIBERO suite:

```bash
python run.py --train_suite libero_spatial
```
Supported `--train_suite` values: `libero_object`, `libero_spatial`, `libero_goal`, `libero_90`, `libero_10`
  
## Evaluation with a checkpoint
### 1) Vanilla LIBERO evaluation
Evaluate a checkpoint on the same vanilla suite:

```bash
python run.py --train_suite libero_spatial --checkpoint_path /path/to/ckpt.pth
```

### 2) LIBERO-PRO evaluation on the same checkpoint
Evaluate the same checkpoint on a LIBERO-PRO suite:

```bash
python run.py --train_suite libero_spatial --eval_suite object --checkpoint_path /path/to/ckpt.pth
```

#### Eval suites (LIBERO-PRO suffixes)
Optional `--eval_suite` values: `object`, `swap`, `lan`, `task`, `temp`

In this mode:
- dataset benchmark remains `libero_goal`
- simulator benchmark is `libero_goal_object`
- evaluation embeddings are loaded from `language_embeddings/libero_goal_object.pkl`



## Repository notes
The public package is `SUREFlow`. The original Mamba implementation is kept under `SUREFlow/mamba/` so the backbone code remains easy to compare with the upstream block implementation.


```bibtex
@article{islam2026sureflow,
  title={SUREFlow: State-space Uncertainty-aware REsidual Flow Matching for Robust Robot Manipulation},
  author={Islam, Md Tanvir and Peddapalli, Sai Navaneet and Lee, Sangmoon and Ahn, Sangtae},
  journal={arXiv preprint arXiv:2607.10504},
  year={2026}
}
