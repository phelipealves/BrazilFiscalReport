DACCe (Auxiliary Document of the Electronic Bill of Lading) is a printed version of the Electronic Bill of Lading (BL-e) used in Brazil. It simplifies the information from the electronic document, providing details like sender, receiver, cargo, and transportation.

## Using in Python Code 🐍

```python
from brazilfiscalreport.dacce import DaCCe

# Path to the XML file
xml_file_path = 'cce.xml'

# Load XML Content
with open(xml_file_path, "r", encoding="utf8") as file:
    xml_content = file.read()

# Instantiate the CC-e PDF object with the loaded XML content
cce = DaCCe(xml=xml_content)

# Save the generated PDF to a file
cce.output('cce.pdf')
```

## Using in CLI 💻

```
bfrep dacce /path/to/cce_1.xml
```
