from app import app


def test_aluno_nao_aceita_post():
    resposta = app.test_client().post("/aluno")
    assert resposta.status_code == 405
