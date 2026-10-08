"""Testes da demo (streamlit_app.py), executada pelo AppTest do Streamlit."""

from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from catalog import EXAMPLES

APP = str(Path(__file__).resolve().parents[1] / "streamlit_app.py")
# Gerar o PDF dos exemplos maiores passa do timeout padrão de 3 s.
TIMEOUT = 60


def run_app(**query_params):
    at = AppTest.from_file(APP, default_timeout=TIMEOUT)
    at.query_params.update(query_params)
    return at.run()


def test_examples_have_unique_ids_and_existing_files():
    assert len({example.id for example in EXAMPLES}) == len(EXAMPLES)
    for example in EXAMPLES:
        assert example.read().startswith(b"<"), example.file_name


@pytest.mark.parametrize("example", EXAMPLES, ids=lambda example: example.id)
def test_example_generates_pdf(example):
    at = run_app(exemplo=example.id)
    assert not at.exception
    assert not at.error, [e.value for e in at.error]
    assert at.success[0].value == "1 PDF gerado com sucesso!"
    # O tipo detectado no XML tem de ser o documento do exemplo.
    row = f"📄 **{example.file_name}** · :gray-background[{example.doc}]"
    assert row in [markdown.value for markdown in at.markdown]
    assert at.query_params["exemplo"] == example.id


def test_document_id_opens_its_first_example():
    at = run_app(exemplo="danfce")
    assert at.session_state["example_doc"] == "DANFCe"
    assert at.session_state["example_DANFCe"] == "danfce"


def test_unknown_example_falls_back_to_upload():
    at = run_app(exemplo="nao-existe")
    assert not at.exception
    assert at.session_state["source"] == "upload"
    assert "exemplo" not in at.query_params
    assert not at.success


def test_switching_to_upload_clears_the_example_from_the_url():
    at = run_app(exemplo="danfe")
    at.segmented_control(key="source").set_value("upload").run()
    assert "exemplo" not in at.query_params
    assert not at.success


@pytest.mark.parametrize(
    "example",
    [example for example in EXAMPLES if example.options],
    ids=lambda example: example.id,
)
def test_example_opens_with_its_options(example):
    at = run_app(exemplo=example.id)
    for key, value in example.options.items():
        # get_by_key também falha se a chave não for de nenhum widget.
        assert at.get_by_key(key).value == value, key


def test_switching_example_resets_the_previous_options():
    at = run_app(exemplo="danfe-anp")
    assert at.toggle(key="danfe_anp").value is True
    at.pills(key="example_DANFE").set_value("danfe").run()
    assert at.toggle(key="danfe_anp").value is False


@pytest.mark.parametrize("example_id", ["danfe", "danfe-ibs-cbs"])
@pytest.mark.parametrize(
    "layout", ["NT 2026.010 (reforma tributária)", "MOC 7.0 (anterior)"]
)
def test_danfe_layout_can_be_forced(example_id, layout):
    at = run_app(exemplo=example_id)
    at.selectbox(key="danfe_layout").set_value(layout).run()
    assert not at.exception
    assert not at.error, [e.value for e in at.error]
    assert at.success[0].value == "1 PDF gerado com sucesso!"
