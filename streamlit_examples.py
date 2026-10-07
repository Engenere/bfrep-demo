"""Exemplos do playground: XMLs de teste para quem não tem um XML em mãos.

Os arquivos vêm de tests/fixtures/ e só contêm dados fictícios. O id do
primeiro exemplo de cada documento é o próprio nome do documento, então
?exemplo=danfe abre o exemplo padrão do DANFE.
"""

from dataclasses import dataclass, field
from pathlib import Path

FIXTURES = Path(__file__).resolve().parent / "tests" / "fixtures"


@dataclass(frozen=True)
class Example:
    id: str
    doc: str
    label: str
    path: str
    description: str
    # Opção da barra lateral que vale a pena testar com este XML.
    tip: str | None = None
    # Dados cadastrais da CC-e, que o XML do evento não traz.
    emitente: dict = field(default_factory=dict)

    @property
    def file_name(self) -> str:
        return Path(self.path).name

    def read(self) -> bytes:
        return (FIXTURES / self.path).read_bytes()


EXAMPLES = [
    Example(
        id="danfe",
        doc="DANFE",
        label="Nota simples",
        path="danfe/nfe_test_1.xml",
        description="NF-e de homologação com um único item.",
    ),
    Example(
        id="danfe-fatura",
        doc="DANFE",
        label="Fatura e transporte",
        path="danfe/nfe_semicolon_line_break.xml",
        description="NF-e com duplicatas, transportadora, lotes e informações "
        "complementares separadas por ';'.",
        tip="Experimente **Canhoto de coleta para a transportadora**, "
        "**Exibição da fatura** e **Quebrar linha em ';' nas inf. "
        "complementares**.",
    ),
    Example(
        id="danfe-multipagina",
        doc="DANFE",
        label="Várias páginas",
        path="danfe/nfe_multi_page_products.xml",
        description="NF-e com 29 itens, que ocupam mais de uma página.",
        tip="Mude a **Orientação** para Paisagem ou o **Tamanho da fonte** "
        "para Grande.",
    ),
    Example(
        id="danfe-anp",
        doc="DANFE",
        label="Combustível (ANP)",
        path="danfe/nfe_test_anp.xml",
        description="Item de combustível com o grupo comb (código ANP).",
        tip="Ative **Exibir dados ANP (combustíveis)**.",
    ),
    Example(
        id="danfe-anvisa",
        doc="DANFE",
        label="Medicamento (ANVISA)",
        path="danfe/nfe_test_anvisa.xml",
        description="Item de medicamento com o grupo med e lotes de "
        "rastreabilidade.",
        tip="Ative **Exibir dados ANVISA (medicamentos)** e **Exibir lotes "
        "(rastreabilidade)**.",
    ),
    Example(
        id="danfce",
        doc="DANFCe",
        label="Cupom autorizado",
        path="danfce/danfce_default.xml",
        description="NFC-e autorizada, com três itens e consumidor "
        "identificado por CNPJ.",
        tip="Troque a **Largura da bobina** para 58 mm.",
    ),
    Example(
        id="danfce-homologacao",
        doc="DANFCe",
        label="Homologação",
        path="danfce/danfce_sem_valor_fiscal.xml",
        description="NFC-e de homologação ainda sem protocolo: o cupom traz "
        "os avisos de sem valor fiscal e de pendente de autorização.",
    ),
    Example(
        id="danfce-muitos-itens",
        doc="DANFCe",
        label="Muitos itens",
        path="danfce/danfce_many_items.xml",
        description="NFC-e com 36 itens. O cupom sai numa única página com a "
        "altura do conteúdo, como na bobina contínua.",
        tip="Ative **Quebrar em páginas** para paginar o cupom.",
    ),
    Example(
        id="dacte",
        doc="DACTE",
        label="Rodoviário",
        path="dacte/dacte_test_1.xml",
        description="CT-e do modal rodoviário.",
    ),
    Example(
        id="dacte-aereo",
        doc="DACTE",
        label="Aéreo",
        path="dacte/dacte_aereo_test.xml",
        description="CT-e do modal aéreo.",
    ),
    Example(
        id="dacte-ibs-cbs",
        doc="DACTE",
        label="Reforma tributária (IBS/CBS)",
        path="dacte/dacte_reforma_tributaria.xml",
        description="CT-e com o grupo IBSCBS da reforma tributária.",
        tip="Ative **Exibir IBS/CBS (reforma tributária)**.",
    ),
    Example(
        id="dacte-multipagina",
        doc="DACTE",
        label="Várias páginas",
        path="dacte/dacte_test_multi_pages.xml",
        description="CT-e com 29 NF-es transportadas, que ocupam mais de uma "
        "página.",
    ),
    Example(
        id="damdfe",
        doc="DAMDFE",
        label="Rodoviário",
        path="damdfe/mdf-e_test_1.xml",
        description="MDF-e do modal rodoviário.",
    ),
    Example(
        id="damdfe-municipios",
        doc="DAMDFE",
        label="Vários municípios",
        path="damdfe/mdf-e_test_multi_municipio.xml",
        description="MDF-e rodoviário com dois municípios de descarregamento.",
        tip="Ative **Exibir origem/destino da prestação**.",
    ),
    Example(
        id="damdfe-aereo",
        doc="DAMDFE",
        label="Aéreo",
        path="damdfe/mdf-e_test_aereo.xml",
        description="MDF-e do modal aéreo.",
    ),
    Example(
        id="damdfe-aquaviario",
        doc="DAMDFE",
        label="Aquaviário",
        path="damdfe/mdf-e_test_aquaviario.xml",
        description="MDF-e do modal aquaviário.",
    ),
    Example(
        id="dacce",
        doc="DACCe",
        label="Carta de correção",
        path="dacce/xml_cce_1.xml",
        description="Evento de CC-e de uma NF-e. O XML do evento não traz os "
        "dados do emitente, por isso a barra lateral já vem preenchida com "
        "dados fictícios.",
        emitente={
            "nome": "EMPRESA EXEMPLO LTDA",
            "end": "AV. EXEMPLO, 100",
            "bairro": "CENTRO",
            "cidade": "SÃO PAULO",
            "uf": "SP",
            "fone": "(11) 1234-5678",
        },
    ),
    Example(
        id="danfse",
        doc="DANFSE",
        label="Produção",
        path="danfse/nfse_test_prod.xml",
        description="NFS-e nacional emitida em produção.",
        tip="Ative o **Canhoto de cientificação**.",
    ),
    Example(
        id="danfse-homologacao",
        doc="DANFSE",
        label="Homologação",
        path="danfse/nfse_test_hom.xml",
        description='NFS-e de homologação, com a expressão "NFS-e SEM '
        'VALIDADE JURÍDICA" no cabeçalho.',
    ),
    Example(
        id="danfse-intermediario",
        doc="DANFSE",
        label="Com intermediário",
        path="danfse/nfse_test_interm.xml",
        description="NFS-e com o intermediário do serviço identificado.",
    ),
    Example(
        id="danfse-ibs-cbs",
        doc="DANFSE",
        label="Reforma tributária (IBS/CBS)",
        path="danfse/nfse_rtc_valid.xml",
        description="NFS-e com o grupo IBSCBS da reforma tributária.",
    ),
]

EXAMPLES_BY_ID = {example.id: example for example in EXAMPLES}
