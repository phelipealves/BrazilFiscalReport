DAMDFE (Auxiliary Document of the Electronic Invoice for Retail) is a printed version of the Electronic Retail Invoice (NF-e) in Brazil. It contains key information about the transaction, such as the seller, buyer, and item details, and is used as proof of purchase.

## Using in Python Code 🐍

```python
from brazilfiscalreport.damdfe import Damdfe

# Path to the XML file
xml_file_path = 'damdfe.xml'

# Load XML Content
with open(xml_file_path, "r", encoding="utf8") as file:
    xml_content = file.read()

# Instantiate the DAMDFE object with the loaded XML content
damdfe = Damdfe(xml=xml_content)

# Save the generated PDF to a file
damdfe.output('damdfe.pdf')
```

## Using in CLI 💻

```
bfrep damdfe /path/to/cce_1.xml
```
## Customizing DAMDFE 🎨

This section describes how to customize the PDF output of the DAMDFE using the `DamdfeConfig` class. You can adjust various settings such as margins, fonts, and tax configurations according to your needs.

### Configuration Options ⚙️

Here is a breakdown of all the configuration options available in `DamdfeConfig`:

---

**Logo**

- **Type**: `str`, `BytesIO`, or `bytes`
- **Description**: Path to the logo file or binary image data to be included in the PDF. You can use a file path string or pass image data directly.
- **Example**:
    ```python
    config.logo = "path/to/logo.jpg"  # Using a file path
    ```
- **Default**: No logo.

---

**Margins**

- **Type**: `Margins`
- **Fields**: `top`, `right`, `bottom`, `left` (all of type `Number`)
- **Description**: Sets the page margins for the PDF document.
- **Example**:
    ```python
    config.margins = Margins(top=10, right=10, bottom=10, left=10)
    ```
- **Default**: top, right, bottom, and left are set to 5 mm.

---

**Font Type**

- **Type**: `FontType` (Enum)
- **Values**: `COURIER`, `TIMES`
- **Description**: Font style used throughout the PDF document.
- **Example**:
    ```python
    config.font_type = FontType.COURIER
    ```
- **Default**: `TIMES`

---

### Usage Example with Customization

Here’s how to set up a DamdfeConfig object with a full set of customizations:

```python
from brazilfiscalreport.damdfe import (
    Damdfe,
    DacteConfig,
    FontType,
    Margins,
)

# Path to the XML file
xml_file_path = 'mdf-e.xml'

# Load XML Content
with open(xml_file_path, "r", encoding="utf8") as file:
    xml_content = file.read()

# Create a configuration instance
config = DamdfeConfig(
    logo='path/to/logo.png',
    margins=Margins(top=10, right=10, bottom=10, left=10),
    font_type=FontType.TIMES
)

# Use this config when creating a Damdfe instance
damdfe = Damdfe(xml_content, config=config)
damdfe.output('output_dacte.pdf')
```
