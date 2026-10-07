# BrazilFiscalReport Demo

Demo online da [BrazilFiscalReport](https://github.com/Engenere/BrazilFiscalReport): converte XMLs fiscais em PDF direto no navegador, sem instalar nada.

**➡️ [brazilfiscalreport.streamlit.app](https://brazilfiscalreport.streamlit.app)**

- Envie XMLs de NF-e, NFC-e, CT-e, MDF-e, CC-e ou NFS-e nacional e baixe o DANFE, DANFCe, DACTE, DAMDFE, DACCe ou DANFSe.
- Não tem um XML? Use um dos exemplos prontos, todos com dados fictícios.
- A barra lateral expõe as opções de geração da biblioteca: logotipo, margens, fontes, marcas d'água e o que mais cada documento aceitar.

## Link direto para um exemplo

`?exemplo=<id>` abre a demo já com um exemplo carregado. Os ids estão em [`catalog.py`](catalog.py); o id do primeiro exemplo de cada documento é o próprio nome do documento:

- [brazilfiscalreport.streamlit.app/?exemplo=danfe](https://brazilfiscalreport.streamlit.app/?exemplo=danfe)
- [brazilfiscalreport.streamlit.app/?exemplo=danfce](https://brazilfiscalreport.streamlit.app/?exemplo=danfce)
- [brazilfiscalreport.streamlit.app/?exemplo=dacte-ibs-cbs](https://brazilfiscalreport.streamlit.app/?exemplo=dacte-ibs-cbs)

## Rodando localmente

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Testes

```bash
pip install pytest
pytest
```

Os testes abrem a demo com cada exemplo e conferem que o PDF é gerado e que o tipo de documento detectado é o esperado.

## Adicionando um exemplo

1. Salve o XML em `examples/<id>.xml`, só com dados fictícios.
2. Registre-o em `EXAMPLES`, no [`catalog.py`](catalog.py), com uma descrição curta. Se o XML existe para mostrar uma opção da barra lateral, ligue-a em `options`, pela chave do widget.

## Relação com a biblioteca

A demo instala a BrazilFiscalReport como dependência, pelo [`requirements.txt`](requirements.txt). Problemas no PDF gerado são da biblioteca: abra a issue [lá](https://github.com/Engenere/BrazilFiscalReport/issues). Quando uma versão nova da biblioteca trouxer uma opção de geração nova, ela entra na barra lateral aqui.

## Licença

[LGPL-3.0](LICENSE).
