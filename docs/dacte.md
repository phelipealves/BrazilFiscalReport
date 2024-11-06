DACTE (Auxiliary Document of the Electronic Transportation Bill) is a printed document used in Brazil to accompany the electronic transportation invoice (CT-e). It serves as a simplified version of the CT-e, providing key details about the shipment, such as cargo information, sender and receiver, and transport company data.

## Customizing DACTE 🎨

This section describes how to customize the PDF output of the DACTE using the `DacteConfig` class. You can adjust various settings such as margins, fonts, and tax configurations according to your needs.

## Using in Python Code 🐍

```python
from brazilfiscalreport.dacte import Dacte

# Path to the XML file
xml_file_path = 'cte.xml'

# Load XML Content
with open(xml_file_path, "r", encoding="utf8") as file:
    xml_content = file.read()

# Instantiate the DACTE object with the loaded XML content
dacte = Dacte(xml=xml_content)
dacte.output('output_dacte.pdf')
```
## Using in CLI 💻

```
bfrep dacte /path/to/dacte.xml
```

## Customizing DACTE 🎨

This section describes how to customize the PDF output of the DACTE using the `DacteConfig` class. You can adjust various settings such as margins, fonts, and tax configurations according to your needs.

### Configuration Options ⚙️

Here is a breakdown of all the configuration options available in `DacteConfig`:

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
    config.margins = Margins(top=5, right=5, bottom=5, left=5)
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

**Display PIS COFINS**

- **Type**: `Bool`
- **Values**: `True`, `False`
- **Description**: Whether or not to display PIS and COFINS taxes in the DACTE totals.
- **Example**:
    ```python
    config.display_pis_cofins = True
    ```
- **Default**: `False`

---

### Usage Example with Customization

Here’s how to set up a DacteConfig object with a full set of customizations:

```python
from brazilfiscalreport.dacte import (
    Dacte,
    DacteConfig,
    FontType,
    Margins,
)

# Path to the XML file
xml_file_path = 'cte.xml'

# Load XML Content
with open(xml_file_path, "r", encoding="utf8") as file:
    xml_content = file.read()

# Create a configuration instance
config = DacteConfig(
    logo='path/to/logo.png',
    margins=Margins(top=10, right=10, bottom=10, left=10),
    font_type=FontType.TIMES
)

# Use this config when creating a Dacte instance
dacte = Dacte(xml_content, config=config)
dacte.output('output_dacte.pdf')
```
