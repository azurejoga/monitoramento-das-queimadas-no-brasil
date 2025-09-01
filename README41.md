# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66ef70c7-dca6-36a5-b2a9-5e57f6476d47 | -12.59784 | -48.21166 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a6a843cc-e162-3ab0-b37a-a95b64cd4cff | -10.87865 | -55.76878 | 2025-09-01 04:12:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84fcc866-90d0-33a2-b03d-4955f4e86e33 | -15.71495 | -49.0022 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2152d171-f9a7-32dc-a7cc-b5f8ceb6cd2b | -13.17261 | -45.28349 | 2025-09-01 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| acc8d1a4-c9fd-35ba-a2e8-0def6da1f56f | -15.08203 | -48.11953 | 2025-09-01 04:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6db80eb6-a607-36a7-ac99-92bea4c5ed53 | -15.58546 | -48.33529 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3576c7ed-a59d-33cc-9d07-854cacc6f1f9 | -12.97446 | -48.11274 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 76c8f94b-3dab-313e-b78f-be01c21cfc74 | -12.59739 | -48.22266 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4578fc58-0b4b-395d-8c0f-7e3b0e125817 | -15.75694 | -47.75845 | 2025-09-01 04:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c545233a-b428-3e33-8a1f-0b2752bfda10 | -14.77088 | -46.7705 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d07d8cfc-c0c4-3b98-b418-056f4b765fd2 | -14.7433 | -46.73402 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fb3181c-756d-3a13-828f-c3643e419cbf | -15.72318 | -49.00349 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| bbeb4b44-4e18-3c6b-9480-897d2a70df6a | -13.47313 | -46.93773 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c204902-26bf-3f8f-93eb-f8a0cee77ee7 | -14.02528 | -44.47832 | 2025-09-01 04:12:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e0f1d79-21f5-3268-8b85-3002bde87002 | -12.57473 | -48.20705 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2cd1de5c-cfca-3715-9212-992e0e6e92d1 | -15.70287 | -48.9133 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f8e8f498-a191-3df1-ab3f-bba96396718d | -13.51336 | -46.99529 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a744cd3-6ea0-3bb8-82f4-19fc8f11977c | -12.57817 | -48.21152 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f7392f60-c98a-3470-bb0e-295c83f5715d | -15.7157 | -48.99816 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5816fa6c-4324-30c4-91df-ff46aec07f57 | -14.82207 | -46.73325 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 933baf0c-5cec-33bc-8581-b660046df80c | -15.77669 | -47.80209 | 2025-09-01 04:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 499ab4e0-ac81-3213-9d4c-41c1503c1449 | -14.74696 | -46.7346 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d57e8b1-40d8-3555-a73b-729a50bb9cec | -14.79152 | -46.73779 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1b8c83f-2aa1-3bab-9d90-03e89d255447 | -13.16565 | -45.28229 | 2025-09-01 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 11785c55-b4a8-3078-b50d-28c35e9403dc | -15.58642 | -48.32985 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ac474c9f-9001-30e1-93fa-376d66aa7b03 | -14.77243 | -46.76146 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0464e354-715f-3c47-9639-88d42bfd80f8 | -14.03322 | -44.47217 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 562a91bc-5c9d-32ea-9443-768fe4788e98 | -15.59443 | -48.35351 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e610db14-74b5-35f4-ad2c-aa06499f3e1a | -12.87824 | -48.16335 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1dae63ee-1d18-31bc-b2a6-c0ed4a442ebd | -16.97287 | -49.309 | 2025-09-01 04:12:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 32576720-c84b-3b5d-a9c2-5221d2d15a93 | -14.74107 | -46.74686 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e603b80-721c-33c1-a3e8-e4779ef97d0a | -13.37432 | -46.94775 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 70606546-e63d-30e7-a624-04ebdebe220f | -12.55837 | -44.78903 | 2025-09-01 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0372a07d-d0a1-3df2-92c6-74e184c73548 | -12.97642 | -54.7603 | 2025-09-01 04:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 983cb115-0db0-38e4-a967-f027da55600a | -15.31485 | -46.07964 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a04e7776-b350-3f1d-9fed-7a224be1a5fd | -14.85011 | -47.09688 | 2025-09-01 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 870f8796-efc8-3ee2-8ee4-6ac09f6dc35a | -14.49374 | -52.98684 | 2025-09-01 04:12:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 241ff940-9d71-3430-88c3-debf9da30e15 | -12.59581 | -48.22283 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 61fbb854-8bee-38ff-adbc-bbf05226b05d | -12.79583 | -48.08657 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8288302-0ff3-3098-94bd-26113a0466cd | -15.71856 | -48.89618 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1fb3ff74-8a3e-32f2-9a8a-35ca30c188f1 | -15.63044 | -46.81598 | 2025-09-01 04:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7a58705-2287-3963-961c-df17d496a7f0 | -14.03262 | -44.47583 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3d71cb5-6963-3bfd-8565-c6608a27052e | -13.49086 | -46.99089 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c88752cf-d0aa-3e72-b40d-0ca99c711115 | -13.34621 | -47.04614 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 139a6032-219e-384d-9f22-600f97207949 | -15.58657 | -48.35189 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 7b62ec6a-3284-3ad0-a920-5cb828b09e3e | -12.56932 | -48.21372 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 964ad986-4aeb-35c5-802a-a86ce3b1c7e8 | -14.78422 | -46.71456 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7888c07-d9ae-3da3-9a10-df370d4f61c8 | -13.47668 | -46.98338 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd63787a-badb-34ba-8330-932cc821f4f4 | -15.69926 | -48.88674 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f040dae8-a16f-3cf3-84a4-1baa32f6e12f | -12.5987 | -48.21518 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8de28e4e-2ea3-3a6b-9c5b-c1db09fc8bae | -13.3348 | -46.97647 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b721ed0-9645-35ea-a85b-9b403ed0af1e | -15.6973 | -48.92084 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73d524d0-91cc-3bda-9caa-7d92ec2ee147 | -13.17157 | -47.20241 | 2025-09-01 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 650e4c71-92b5-382e-bd5e-c5e66b26dbf7 | -14.77895 | -46.76733 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52f8420b-d4eb-3585-9101-c92596c8f411 | -12.59649 | -48.21909 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 5b4c14f9-4b28-34b7-aff9-597d4492be82 | -12.60522 | -48.17778 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 185ceef0-b5fe-3998-9c25-72bad6e08c57 | -16.29599 | -52.94213 | 2025-09-01 04:12:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3bbd206-7837-3009-9528-8c2eea4c0e54 | -15.70972 | -48.89859 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e68dad81-dd09-3c1f-8b5b-fa046c0aefdc | -12.85766 | -48.0678 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 91ca11f6-50f9-3db1-bbac-7ae914a61b7d | -14.81622 | -46.72377 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 252b7963-ddb7-3ba8-9b7e-74c55e5b1032 | -11.92925 | -50.62953 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 662cbb10-1d53-3be4-a7d5-9a9a8b5a3e71 | -15.6987 | -48.91307 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2a4ca5ec-b271-3251-9f39-bdaedeea9079 | -14.79947 | -46.73523 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cd8d4a8-a7cd-354d-90f8-cc2b5bb5605b | -13.58275 | -46.92966 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47fd5da8-f711-3fe2-a291-1fc8f67192e6 | -16.29537 | -52.94521 | 2025-09-01 04:12:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e980dfc1-9b00-3dfd-9942-2865dd63859c | -15.71449 | -48.8954 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1e14372-7213-31ad-abbb-900ac1011b79 | -15.22646 | -53.79616 | 2025-09-01 04:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4625f489-bad7-3d9b-9c37-d9dbd4367b6e | -14.85089 | -47.09235 | 2025-09-01 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 84428d6f-3e7f-3410-a3f4-33624a98f036 | -12.62567 | -57.00841 | 2025-09-01 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 421a429c-e2e6-3dbf-9884-a8ec3b833e92 | -13.33534 | -46.86093 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97bf7044-0b39-36ed-8da2-fe45c55b5af9 | -14.04701 | -44.55766 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71128af1-105b-36c3-a6fd-5f5e2ebfaf7e | -13.33857 | -46.97714 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ca25193-a74d-3b3d-b546-bb43a6a27ffa | -18.12039 | -48.53813 | 2025-09-01 04:12:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6f657ec1-e51d-3c83-8719-803dd92915cd | -13.66677 | -46.93439 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 93eec360-b105-3143-a69d-9ef423c70fa9 | -13.98876 | -44.52907 | 2025-09-01 04:12:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31d59af8-9b42-3ebf-aca1-7a98ddb512b2 | -16.96953 | -49.30424 | 2025-09-01 04:12:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ecf8172-6283-3194-af5f-34fbe143fec8 | -14.1591 | -43.67308 | 2025-09-01 04:12:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 05e0e2d1-281a-3f5f-995b-d1b33cef4dbd | -12.60395 | -48.17811 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcf843e3-55ad-36c5-8496-fb4da8b736a9 | -13.1663 | -45.27838 | 2025-09-01 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a2ede7ab-d462-3c6a-bead-3e93eaed33ad | -14.79658 | -46.73018 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cc33d7f-4091-3697-8710-84729d8362fb | -15.69799 | -48.917 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78d296e9-91b1-3e90-97af-1c0f8cddf3a3 | -15.61827 | -47.85989 | 2025-09-01 04:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55d1135c-481d-3599-831e-a26f2f7c658d | -13.47315 | -46.93538 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad6f0343-9472-3566-86dc-5e68508a6fd6 | -13.32028 | -46.85888 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e13f966-f3cc-3bfa-928d-a5e86e2d3619 | -17.84907 | -44.31581 | 2025-09-01 04:12:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dab5bb5a-e78e-388c-bb5d-4c28959a260e | -12.57647 | -44.80776 | 2025-09-01 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c639f3cb-6d0e-326f-915c-0e4ea1636a1d | -16.13301 | -49.04794 | 2025-09-01 04:12:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d025037d-0d71-3e00-8632-b3da757998f4 | -12.6074 | -48.20568 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4312a3f3-fa69-3212-a01b-664298a9b058 | -15.22449 | -53.79225 | 2025-09-01 04:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 983668ac-e875-3590-ad50-b1ddae735df7 | -13.70319 | -46.90118 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae391ed3-a7bf-3214-9815-15d8d3f466fd | -13.70779 | -46.92402 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de23381c-df3f-37e3-989b-db114e0884ac | -13.49259 | -46.98104 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 04e01594-ddf8-31a1-b158-11e5642b6d47 | -16.15099 | -49.63787 | 2025-09-01 04:12:00 | NPP-375D | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4bbe561d-722a-3738-8f85-600581ca6321 | -12.87736 | -48.09779 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c74cb154-a5f3-345e-9cc5-abb0d3ee447f | -14.02925 | -44.47525 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57d24102-5a0e-3982-be12-dc6c5b3a061e | -13.50961 | -46.99455 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5cc64c47-b0d3-3e32-966f-46864028de9f | -11.51877 | -54.47291 | 2025-09-01 04:12:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4699128f-d3f7-3e70-ac74-f58b1ee174ad | -13.68979 | -46.9169 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc910f77-375d-3c3a-ada7-6a250cb6eca0 | -14.78869 | -46.73232 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c7d8d9c-24f8-380a-b11a-96836317f21d | -12.61762 | -48.19593 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README42.md)
