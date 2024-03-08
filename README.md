# BrazilFiscalReport

Python library for generating Brazilian auxiliary fiscal documents in PDF from XML documents.

## Supported Documents

DANFE - Documento Auxiliar da Nota Fiscal Eletrônica (NF-e)

DACCe - Documento Auxiliar da Carta de Correção Eletrônica (CC-e )

Dependencies:

- FPDF2
(pip install fpdf2)

Roadmap
-
- Unitary tests
- Implement DACTe
- Documentation



## Usage examples


```
from pdf_docs import Danfe, DaCCe

# DANFE
# cfg_layout -> 3 posibilidades de layout das colunas dos itens no modo retrato: 'ICMS_ST', 'ICMS_ST', 'ICMS_IPI'
# receipt_pos -> impressão do recibo de entrega no topo da DANFE ('top') ou no rodapé ('bottom')

xmls = [open( "xml_nfe.xml", "r", encoding="utf8").read()]
pdf = Danfe(xmls=xmls, image=None, cfg_layout='ICMS_ST', receipt_pos='top')
pdf.output('danfe.pdf', 'F')

# DaCCe
emitente = {'nome': 'COMPANY ME-EPP',
            'end': 'AV TEST, 00',
            'bairro' : 'TEST',
            'cep': '00000-000',
            'cidade': 'SÃO PAULO',
            'uf': 'SP',
            'fone': '(11) 1234-5678'}


xmls = [open( "xml_cce.xml", "r", encoding="utf8").read(),]
pdf_cce = DaCCe(xmls=xmls, emitente=emitente, image=None)
pdf_cce.output('cce.pdf', 'F')


```
## Running Tests

### Cloning the repository

```
git clone https://github.com/Engenere/PyFiscalReport.git
```
### Install the lib locally
```
pip install -e file:///path/to/your/package#egg=package_name
```
### Run the tests
```
python3 -m unittest test/test_PyFiscalReport.py
```

## Credits

This is a fork of the nfe_utils project
(https://github.com/edsonbernar/nfe_utils),
originally created by Edson Bernardino (https://github.com/edsonbernar).
