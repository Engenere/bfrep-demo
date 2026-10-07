"""Exemplos da demo: XMLs para quem não tem um XML em mãos.

Os XMLs ficam em examples/<id>.xml e só contêm dados fictícios. O id do
primeiro exemplo de cada documento é o próprio nome do documento, então
?exemplo=danfe abre o exemplo padrão do DANFE.
"""

from dataclasses import dataclass, field
from pathlib import Path

EXAMPLES_DIR = Path(__file__).resolve().parent / "examples"


@dataclass(frozen=True)
class Example:
    id: str
    doc: str
    label: str
    description: str
    # Valores com que a barra lateral abre neste exemplo, pela chave de cada
    # widget: ligam as opções que mostram o que o XML tem de especial.
    options: dict = field(default_factory=dict)

    @property
    def file_name(self) -> str:
        return f"{self.id}.xml"

    def read(self) -> bytes:
        return (EXAMPLES_DIR / self.file_name).read_bytes()


EXAMPLES = [
    Example(
        id="danfe",
        doc="DANFE",
        label="Nota simples",
        description="NF-e de homologação com um único item.",
    ),
    Example(
        id="danfe-fatura",
        doc="DANFE",
        label="Fatura e transporte",
        description="NF-e com duplicatas, transportadora e informações "
        "complementares separadas por ';', impressa com o canhoto da "
        "transportadora e com cada ';' virando uma quebra de linha.",
        options={"danfe_carrier_receipt": True, "danfe_semicolon": True},
    ),
    Example(
        id="danfe-multipagina",
        doc="DANFE",
        label="Várias páginas",
        description="NF-e com 29 itens, que ocupam mais de uma página.",
    ),
    Example(
        id="danfe-anp",
        doc="DANFE",
        label="Combustível (ANP)",
        description="Item de combustível com o grupo comb, impresso com o "
        "código e a descrição ANP.",
        options={"danfe_anp": True},
    ),
    Example(
        id="danfe-anvisa",
        doc="DANFE",
        label="Medicamento (ANVISA)",
        description="Item de medicamento com os grupos med e rastro, impresso "
        "com o código ANVISA e os lotes.",
        options={"danfe_anvisa": True, "danfe_branch": True},
    ),
    Example(
        id="danfce",
        doc="DANFCe",
        label="Cupom autorizado",
        description="NFC-e autorizada, com três itens e consumidor "
        "identificado por CNPJ.",
    ),
    Example(
        id="danfce-homologacao",
        doc="DANFCe",
        label="Homologação",
        description="NFC-e de homologação ainda sem protocolo: o cupom traz "
        "os avisos de sem valor fiscal e de pendente de autorização.",
    ),
    Example(
        id="danfce-muitos-itens",
        doc="DANFCe",
        label="Muitos itens",
        description="NFC-e com 36 itens. O cupom sai numa única página com a "
        "altura do conteúdo, como na bobina contínua.",
    ),
    Example(
        id="dacte",
        doc="DACTE",
        label="Rodoviário",
        description="CT-e do modal rodoviário.",
    ),
    Example(
        id="dacte-aereo",
        doc="DACTE",
        label="Aéreo",
        description="CT-e do modal aéreo.",
    ),
    Example(
        id="dacte-ibs-cbs",
        doc="DACTE",
        label="Reforma tributária (IBS/CBS)",
        description="CT-e com o grupo IBSCBS da reforma tributária, impresso "
        "com a coluna IBS/CBS no quadro de impostos.",
        options={"dacte_ibs_cbs": True},
    ),
    Example(
        id="dacte-multipagina",
        doc="DACTE",
        label="Várias páginas",
        description="CT-e com 29 NF-es transportadas, que ocupam mais de uma "
        "página.",
    ),
    Example(
        id="damdfe",
        doc="DAMDFE",
        label="Rodoviário",
        description="MDF-e do modal rodoviário.",
    ),
    Example(
        id="damdfe-municipios",
        doc="DAMDFE",
        label="Vários municípios",
        description="MDF-e rodoviário com dois municípios de descarregamento, "
        "impresso com a origem e o destino da prestação no percurso.",
        options={"damdfe_origem_destino": True},
    ),
    Example(
        id="damdfe-aereo",
        doc="DAMDFE",
        label="Aéreo",
        description="MDF-e do modal aéreo.",
    ),
    Example(
        id="damdfe-aquaviario",
        doc="DAMDFE",
        label="Aquaviário",
        description="MDF-e do modal aquaviário.",
    ),
    Example(
        id="dacce",
        doc="DACCe",
        label="Carta de correção",
        description="Evento de CC-e de uma NF-e. O XML do evento não traz os "
        "dados do emitente, por isso a barra lateral já vem preenchida com "
        "dados fictícios.",
        options={
            "dacce_nome": "EMPRESA EXEMPLO LTDA",
            "dacce_end": "AV. EXEMPLO, 100",
            "dacce_bairro": "CENTRO",
            "dacce_cidade": "SÃO PAULO",
            "dacce_uf": "SP",
            "dacce_fone": "(11) 1234-5678",
        },
    ),
    Example(
        id="danfse",
        doc="DANFSE",
        label="Produção",
        description="NFS-e nacional emitida em produção.",
    ),
    Example(
        id="danfse-homologacao",
        doc="DANFSE",
        label="Homologação",
        description='NFS-e de homologação, com a expressão "NFS-e SEM '
        'VALIDADE JURÍDICA" no cabeçalho.',
    ),
    Example(
        id="danfse-intermediario",
        doc="DANFSE",
        label="Com intermediário",
        description="NFS-e com o intermediário do serviço identificado.",
    ),
    Example(
        id="danfse-ibs-cbs",
        doc="DANFSE",
        label="Reforma tributária (IBS/CBS)",
        description="NFS-e com o grupo IBSCBS da reforma tributária.",
    ),
]

EXAMPLES_BY_ID = {example.id: example for example in EXAMPLES}
