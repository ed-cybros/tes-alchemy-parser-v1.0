# The Elder Scrolls Alchemy Effects Parser

A Python-based data cleaning/transforming pipeline designed to scrape basic alchemy data (reagents and their effects) from the [Unofficial Elder Scrolls Pages (UESP)](https://en.uesp.net/wiki/Lore:Alchemy) and standardize inconsistent or equivalent effect names across multiple Elder Scrolls titles under a unified naming scheme.

## Motivation

Alchemy effects are represented differently across multiple Elder Scrolls game titles. This made practical use of cross-title alchemy data inconvenient and inefficient in a role-playing setting.

The goal of this project was to collect reagent-effect data from across the titles and standardize effect names under a unified naming scheme while preserving the association between reagents and their effects.

## Features

* **Automated Scraping:** Aggregates reagent data from UESP (A–Z).
* **Data Normalization:** Maps inconsistent and diverging effect names to a new, unified naming scheme.
* **Intelligent Cleaning:** Distinguishes between reagents and effects while removing duplicates and ensuring proper formatting.

## Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4B0082?style=for-the-badge&logo=python&logoColor=white)

## Folder Structure

```md
project_root/
│ main.py                  # Runs the pipeline
│ README.md
│ data/                    # Stores intermediate and final text files
│   ├ 01_parsed.txt
│   ├ 02_renamed.txt
│   └ 03_cleaned_(final).txt
│ scripts/
│   ├ script1_scrape.py
│   ├ script2_replace.py
│   └ script3_clean.py
│ notebooks/
│   └ alchemy_scraping_pipeline.ipynbsynonymous
```

## Requirements

* Python 3.x
* requests
* beautifulsoup4

## Install dependencies

`pip install requests beautifulsoup4`

## Usage

Ensure `data/` folder exists.

Run the main entry point to execute the full pipeline:

```bash

python main.py

```

## Detailed Overview

For a step-by-step visualization of the full process see the [Alchemy Parser Pipeline Notebook](notebooks/tes_alchemy_parser_2.0_overview.ipynb).

## Disclaimer

This project was made as part of a personal role-playing experience in The Elder Scrolls universe and is not actively maintained. New reagents or effects added to the website may not be captured or normalized correctly by the scripts.

## Why 2.0 exists?

Current project represents the first working implementation of the alchemy data collection pipeline. While it successfully scraped and standardized reagent-effect data, the final output was stored as a text file suitable mostly for manual lookup.

These limitations later became one of the motivations behind the development of [The Elder Scrolls Alchemy Parser 2.0](https://github.com/ed-cybros/tes-alchemy-parser-v2.0), where the data was restructured using JSON and SQLite to provide more flexible lookup capabilities, while also placing special emphasis on data validation and integrity checks.
