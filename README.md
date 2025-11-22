# Look It Up: Analysing Internal Web Search Capabilities of Modern LLMs
## Abstract

Modern large language models integrate web search to provide real-time answers, yet it remains unclear whether they are efficiently calibrated to use search when it is actually needed. We introduce a benchmark evaluating both the necessity and effectiveness of web access across commercial models with no access to internal states or parameters. The dataset includes a static split of 783 temporally anchored questions answerable from pre-cutoff knowledge, aimed at testing whether models invoke search based on low internal confidence, and a dynamic split of 288 post-cutoff queries designed to test whether models recognise when search is required and retrieve updated information. Web access substantially improves static accuracy for GPT-5-mini and Claude Haiku 4.5, though confidence calibration worsens. On dynamic queries, both models frequently invoke search yet remain below 70 percent accuracy due to weak query formulation. Costs per accuracy-improving call remain low, but returns diminish once initial retrieval fails. Selective invocation helps, but models become overconfident and inconsistent after search. Overall, built-in web search meaningfully improves factual accuracy and can be invoked selectively, yet models remain overconfident, skip retrieval when it is essential, and falter once initial search queries underperform. Taken together, internal web search works better as a good low-latency verification layer than a reliable analytical tool, with clear room for improvement.

<div align="center">
  <img width="500" alt="Web_Img1" src="https://github.com/user-attachments/assets/f4c5841d-b8aa-45f5-b3fa-e2bcb7c1e095" />
</div>
</br>
*End-to-end evaluation pipeline covering uncertainty assessment, query issuance, retrieval outcomes, and accuracy transitions.*

## Overview

This repository accompanies our paper evaluating how closed-source LLMs decide when to invoke built-in web search, whether retrieval yields correct answers, and how cost scales with accuracy improvements.

## Method:

- Static split: evaluates selective invocation based on internal confidence when retrieval is unnecessary.
- Dynamic split: evaluates whether models detect information staleness and fetch updated answers.
- Metrics: accuracy, calibration impact, routing behavior, cost per improvement, and query efficiency.
- Models tested: Claude 4.5 Haiku and GPT-5-mini.


## Repository Status

Code, dataset, and benchmark scripts will be released upon acceptance.
If you need early access for reproducibility or collaboration, please open an issue.

## Citation

A BibTeX entry will be added after acceptance!
