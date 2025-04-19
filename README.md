<div align="center" style="font-size: 6em;">
  ࿂
</div>
<h1 align="center">Grants Data Portal</h1>

<div align="center">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/davidgasquez/grants-data-portal?style=flat-square">
  <img alt="GitHub" src="https://img.shields.io/github/license/davidgasquez/grants-data-portal?style=flat-square">
  <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/davidgasquez/grants-data-portal/run.yml?style=flat-square">
  <a href="https://www.drips.network/app/projects/github/davidgasquez/gitcoin-grants-data-portal" target="_blank"><img src="https://www.drips.network/api/embed/project/https%3A%2F%2Fgithub.com%2Fdavidgasquez%2Fgitcoin-grants-data-portal/support.png?background=light&style=github&text=project&stat=none" alt="Support gitcoin-grants-data-portal on drips.network" height="20"></a>
</div>


Open source, serverless, and local-first Data Platform for Public Goods Grants Data. This data hub improves data access and empower data scientists to conduct research that guides community driven analysis.

> [!IMPORTANT]
>
> The previous version of the portal (browse it [here](https://github.com/davidgasquez/grants-data-portal/tree/ea74827476e25fbc3f94aa052c15c7b681a2d183)) is **deprecated**. You can find better and more up to date data on [Open Source Observer](https://www.opensource.observer/). This new approach/version **focuses on curating Open Source Observer datasets with some smaller datasets** and distributing them.

## 📖 Overview

The repository contains code and artifacts to help process grants around the Public Goods Ecosystem. The portal is based on the principles of [Datadex](https://datadex.datonic.io/).

### 📦 Key Features

- **Open**: Code and data are open source and relies on open standards and formats.
- **Permissionless Collaboration**: Collaborate on data, models, and pipelines. Fork the repo and run the platform locally in minutes. No constraints or platform lock-ins.
- **Decentralization Options**: Runs on a laptop, server, CI runner, or even on decentralized compute networks like Bacalhau. No local setup required.
- **Data as Code**: Each commit generates and pushes all datasets as files to an Object Storage.
- **Modular Flexibility**: Replace, extend, or remove individual components. Compatible with tons of tools. At the end of the day, datasets are Parquet files.
- **Low Friction Data Usage**: Raw and processed data is available to anyone openly. Use whatever tool you want!
- **Modern Data Engineering**: Supports data engineering essentials such as typing, testing, materialized views, and development branches. Utilizes best practices, including declarative transformations, and utilizes state-of-the-art tools like DuckDB.

## ⚙️ Quick Start

Make sure you have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed. Clone the repository and install dependencies:

```bash
git clone https://github.com/davidgasquez/grants-data-portal.git
cd grants-data-portal
make setup
```

Run the Dagster UI:

```bash
make dev
```

You can now access the Dagster UI at [http://localhost:3000](http://localhost:3000)!

## 🛠️ Contributing

This project is in active development. You can help by giving ideas, answering questions, reporting bugs, proposing enhancements, improving the documentation, and fixing bugs.
Some ways you can contribute to this project:

- Adding new data sources.
- Improving the data quality of existing datasets.
- Adding tests to the data pipelines.

### 📄 License

[MIT](https://choosealicense.com/licenses/mit/).
