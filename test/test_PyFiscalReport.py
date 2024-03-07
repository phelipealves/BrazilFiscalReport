import os
import unittest

from PyFiscalReport import pdf_docs


class TestPynfedance(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def test_format_cpf_cnpj(self):
        nfedanfe_instance = pdf_docs
        cpf = nfedanfe_instance.format_cpf_cnpj("76586507812")
        self.assertEqual("765.865.078-12", cpf)

    def test_format_number(self):
        nfedanfe_instance = pdf_docs
        number = nfedanfe_instance.format_number("19500")
        self.assertEqual("19.500", number)

    def test_create_danfe_pdf(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))

        xml_file_path = os.path.join(current_dir, "data", "NFe_teste_cee.xml")
        with open(xml_file_path, "r", encoding="utf8") as f:
            xmls = [f.read()]
        pdf = pdf_docs.Danfe(
            xmls=xmls, image=None, cfg_layout="ICMS_ST", receipt_pos="top"
        )
        pdf.output("danfe.pdf")

        self.assertTrue(os.path.isfile("danfe.pdf"))


if __name__ == "__main__":
    unittest.main()
