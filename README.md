<div align="center">
  <img src="https://user-images.githubusercontent.com/1682202/271937380-10d6e036-5fe4-4ea6-b3b4-8e3001c21289.png" width="100" />
</div>
<h1 align="center">Grants Data Portal</h1>

<div align="center">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/davidgasquez/grants-data-portal?style=flat-square">
  <img alt="GitHub" src="https://img.shields.io/github/license/davidgasquez/grants-data-portal?style=flat-square">
  <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/davidgasquez/grants-data-portal/run.yml?style=flat-square">
  <a href="https://www.drips.network/app/projects/github/davidgasquez/gitcoin-grants-data-portal" target="_blank"><img src="https://www.drips.network/api/embed/project/https%3A%2F%2Fgithub.com%2Fdavidgasquez%2Fgitcoin-grants-data-portal/support.png?background=light&style=github&text=project&stat=none" alt="Support gitcoin-grants-data-portal on drips.network" height="20"></a>
</div>

Open source, serverless, and local-first Data Platform for Grants Data. This data hub improves data access and empower data scientists to conduct research that guides community driven analysis.

> [!WARNING]
>
> This repository is under active development. The datasets might not be fully up to date and the API might undergo breaking changes. Please use it with caution.

## 📖 Overview

This repository contains all the code and related artifacts to process funding data from diverse sources (on-chain and off-chain). You can go directly to the processed datasets or explore the different metrics and pipelines on this repository.

<div align="center">
  <a href="https://grantsdataportal.xyz/data" target="_blank">
      <img src="https://img.shields.io/badge/GET_THE_DATA-0090ff?style=for-the-badge" alt="GET THE DATA">
  </a>
</div>

![DAG](https://github.com/davidgasquez/gitcoin-grants-data-portal/assets/1682202/2095974c-f8c4-430b-9c93-dd2a0598127e)

## 📖 Overview

The repository contains code and artifacts to help process grants around the Public Goods Ecosystem. The portal is based on the principles of [Datadex](https://github.com/davidgasquez/datadex).

### 📦 Key Features

- **Open**: Code and data are open source and relies on open standards and formats.
- **Permissionless Collaboration**: Collaborate on data, models, and pipelines. Fork the repo and run the platform locally in mintures. No constraints or platform lock-ins.
- **Decentralization Options**: Runs on a laptop, server, CI runner, or even on decentralized compute networks like Bacalhau. No local setup required; it even works seamlessly in GitHub Codespaces.
- **Data as Code**: Each commit generates and pushes all table files to R2.
- **Modular Flexibility**: Replace, extend, or remove individual components. Compatible with tons of tools. At the end of the day, tables are Parquet files.
- **Low Friction Data Usage**: Raw and processed data is available to anyone openly. Use whatever tool you want!
- **Modern Data Engineering**: Supports data engineering essentials such as typing, testing, materialized views, and development branches. Utilizes best practices, including declarative transformations, and utilizes state-of-the-art tools like DuckDB.

## ⚙️ Quick Start

The fastest way to start working on the Data Portal is via [VSCode Remote Containers](https://code.visualstudio.com/docs/remote/containers). Once inside the develpment environment, you can run `make dev` to spin up the Dagster UI.

The development environment can also run in your browser thanks to GitHub Codespaces! Just click on the badge below to get started.

[![badge](https://github.com/codespaces/badge.svg)](https://codespaces.new/davidgasquez/gitcoin-grants-data-portal)

## 🛠️ Contributing

This project is in active development. You can help by giving ideas, answering questions, reporting bugs, proposing enhancements, improving the documentation, and fixing bugs. Feel free to open issues and pull requests!

Some ways you can contribute to this project:

- Adding new data sources.
- Improving the data quality of existing datasets.
- Adding tests to the data pipelines.

### 📄 License

[MIT](https://choosealicense.com/licenses/mit/).
