# Projeto DevOps: dupla-17

Site: https://vlourez.github.io/projeto-devops-Dupla-17/ (status em /status.html)
Imagem: ghcr.io/vlourez/projeto-devops-dupla-17

## O fluxo completo
1. Um `git push` na `main` dispara o CI (testes e construção da imagem) e o fluxo "Publicar site com status".
2. O fluxo do site roda os testes; só se passarem ele gera o `status.html` e publica no GitHub Pages.
3. Uma tag `v*` (`git push origin v1`) dispara o fluxo "Publicar imagem", que testa de novo e faz login no ghcr.io.
4. A imagem é construída com `--build-arg APP_VERSION=<tag>` e enviada para `ghcr.io/vlourez/projeto-devops-dupla-17:<tag>`.
5. No Codespace: `docker pull`, `docker run -p 5017:5017` e `curl http://localhost:5017/saude` devolve a `versao`.

## Linha do tempo
- v1 (`13a0568`): Dockerfile com `ARG`/`ENV APP_VERSION` e o fluxo `publicar-imagem.yml`; a API responde na porta 5017.
- v2 (`e0aef84`): a última linha do `app.py` passou a usar `port=5018`. Os testes passaram e a imagem foi publicada, mas o contêiner não respondia na 5017.
- v3 (`eda6f34`): `git revert` do commit da v2, voltando para `port=PORTA`. Depois, um revert aplicado no commit errado (`a578663`) trouxe a 5018 de volta para a main e foi desfeito em `ee5544d`.

## O que os testes não pegaram
Os testes usam `app.test_client()`, que chama as rotas sem abrir porta de rede, então a porta errada passou. Para pegar isso, o pipeline poderia subir o contêiner (`docker run -p 5017:5017`), esperar alguns segundos e fazer `curl http://localhost:5017/saude`, falhando se não houver resposta.

## Quem fez o quê
João (Vlourez, aluno A): página de status no `pages.yml`, verificação da visibilidade da imagem, `git revert` da v2 e tag v3, README e o revert que corrigiu a main depois do "Reapply".

Robert (Robert-739, aluno B): Dockerfile com a versão, fluxo `publicar-imagem.yml`, tags v1 e v2 (a falha simulada na porta) e o próprio parágrafo do README.