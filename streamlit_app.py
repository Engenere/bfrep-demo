import xml.etree.ElementTree as ET

import streamlit as st

from brazilfiscalreport.dacce import DaCCe
from brazilfiscalreport.dacte import Dacte
from brazilfiscalreport.damdfe import Damdfe
from brazilfiscalreport.danfe import Danfe

DOCUMENT_TYPES = {
    "nfeProc": ("DANFE", Danfe),
    "NFe": ("DANFE", Danfe),
    "cteProc": ("DACTE", Dacte),
    "CTe": ("DACTE", Dacte),
    "mdfeProc": ("DAMDFE", Damdfe),
    "MDFe": ("DAMDFE", Damdfe),
    "procEventoNFe": ("DACCe", DaCCe),
}

st.set_page_config(
    page_title="Conversor XML Fiscal para PDF", page_icon=":page_facing_up:"
)

st.title("Conversor de XML Fiscal para PDF")
st.markdown("Transforme seus XMLs fiscais em PDF de forma rápida e gratuita.")
st.markdown(
    "Documentos suportados: "
    ":gray-background[**DANFE** · NF-e] "
    ":gray-background[**DACTE** · CT-e] "
    ":gray-background[**DAMDFE** · MDF-e] "
    ":gray-background[**DACCe** · CC-e]"
)

uploaded_file = st.file_uploader("Envie o arquivo XML", type=["xml"])

if uploaded_file is not None:
    xml_content = uploaded_file.read().decode("utf-8")

    try:
        root = ET.fromstring(xml_content)
    except ET.ParseError:
        st.error("Arquivo XML inválido. Por favor, envie um XML fiscal válido.")
        st.stop()

    # Strip namespace to get the local tag name
    root_tag = root.tag.split("}")[-1] if "}" in root.tag else root.tag

    if root_tag not in DOCUMENT_TYPES:
        supported = ", ".join(f"`{t}`" for t in DOCUMENT_TYPES)
        st.error(
            f"Tipo de documento não reconhecido: `{root_tag}`. "
            f"Tags raiz suportadas: {supported}."
        )
        st.stop()

    doc_name, doc_class = DOCUMENT_TYPES[root_tag]
    st.info(f"Tipo de documento detectado: **{doc_name}**")

    try:
        if doc_class is DaCCe:
            emitente = {
                "nome": " ",
                "end": " ",
                "bairro": " ",
                "cep": " ",
                "cidade": " ",
                "uf": " ",
                "fone": " ",
            }
            instance = doc_class(xml=xml_content, emitente=emitente)
        else:
            instance = doc_class(xml=xml_content)
        pdf_bytes = bytes(instance.output())
    except Exception as e:
        st.error(f"Erro ao gerar o PDF: {e}")
        st.stop()

    file_name = uploaded_file.name.rsplit(".", 1)[0] + ".pdf"

    st.success("PDF gerado com sucesso!")
    st.download_button(
        label=f"Baixar {doc_name} em PDF",
        data=pdf_bytes,
        file_name=file_name,
        mime="application/pdf",
    )

st.divider()
st.caption(
    "Desenvolvido com "
    "[Brazil Fiscal Report](https://github.com/Engenere/BrazilFiscalReport)"
    " — biblioteca open source para geração de documentos fiscais em PDF."
)
