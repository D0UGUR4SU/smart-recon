# smart-recon

Para utilizar é necessário se atentar ao passo a passo:

---

1. Clone esse repositório em alguma pasta no seu linux ou mac (Não testado no WSL)
2. Gere a imagem do docker usando docker build -t kali-tools . (OBS: Nos scripts, é utilizado o kali-tools com a tag 2.0, então provavelmente pode ser necessário criar um commit da imagem com essa tag)
3. Libere as permissões para todas as pastas do projeto, com o comando: sudo chown 1000:1000 *
4. Agora já podemos rodar um docker-compose up para subir o nosso open_distro (Importante ter configurado o docker para não precisar rodar com sudo)
5. Confirme que o opendistro rodou certinho verificando se obteve esse retorno:

```
database-node1    | [2023-11-25T14:27:12,613][INFO ][c.a.o.s.c.ConfigurationRepository] [database-node1] Node 'database-node1' initialized
```
