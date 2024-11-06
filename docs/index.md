[![image](https://github.com/engenere/BrazilFiscalReport/workflows/tests/badge.svg)](https://github.com/Engenere/BrazilFiscalReport/actions)
[![image](https://codecov.io/gh/engenere/BrazilFiscalReport/branch/main/graph/badge.svg)](https://app.codecov.io/gh/Engenere/BrazilFiscalReport)
[![image](https://img.shields.io/github/languages/top/Engenere/brazilfiscalreport)](https://pypi.org/project/BrazilFiscalReport/)
[![image](https://img.shields.io/pypi/v/brazilfiscalreport.svg)](https://pypi.org/project/BrazilFiscalReport/)
[![image](https://img.shields.io/pypi/l/brazilfiscalreport)](https://github.com/Engenere/BrazilFiscalReport/blob/main/LICENSE)
![beta](https://img.shields.io/badge/status-beta-orange)
# Brazil Fiscal Report

Python library for generating Brazilian auxiliary fiscal documents in PDF from XML documents.

## Supported Documents 📄

- **DANFE** - Documento Auxiliar da Nota Fiscal Eletrônica (NF-e)
- **DACCe** - Documento Auxiliar da Carta de Correção Eletrônica (CC-e)
- **DACTE** - Documento Auxiliar do Conhecimento de Transporte Eletrônico (CT-e)
- **DAMDFE** - Documento Auxiliar do Manifesto Eletrônico de Documentos Fiscais (MDF-e)

## Usage Modes

### 1. CLI (Command Line)

For quick and easy PDF generation, use the CLI. After configuring the `config.yaml` file with the issuer details, margins, and logo, you can easily generate PDFs with a single command.

### 2. Python Code

For further customization and integration, use the library directly in Python code. This mode allows you to configure margins, fonts, receipt positions, and other options tailored to your needs.

## Beta Stage Notice 🚧

This library is currently in the beta stage of development. While it has many of the intended features implemented, it is still undergoing testing and improvements. Users should note that during this phase, functionality may change and some instability may occur. We welcome feedback on any issues or suggestions for enhancements. Use in production environments should be approached with caution.

## Dependencies 🛠️

- [FPDF2](https://github.com/py-pdf/fpdf2) - PDF creation library for Python
- phonenumbers
- python-barcode
- qrcode (only required for DACTE)

## To install 🔧

```bash
pip install brazilfiscalreport
```

## Installing DACTE with Dependencies
If you specifically need the DACTE functionality, you can install it along with its required dependencies using:

```bash
pip install brazilfiscalreport[dacte]
```

## Installing DAMDFE with Dependencies
If you specifically need the DAMDFE functionality, you can install it along with its required dependencies using:

```bash
pip install brazilfiscalreport[damdfe]
```

### Installing CLI with Dependencies
If you specifically need the CLI functionality, you can install it along with its required dependencies using:

```bash
pip install brazilfiscalreport[cli]
```
