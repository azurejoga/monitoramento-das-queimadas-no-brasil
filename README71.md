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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 395803dd-aee4-3bb4-a8df-31b15b5410c1 | -15.14986 | -52.3346 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac85165e-6069-303b-931f-51433c203beb | -12.90788 | -56.93739 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 50b4bea7-8b8c-3abe-8a54-5a476c98a1d8 | -13.74239 | -46.93318 | 2025-09-04 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6454cdef-5be2-3be2-a5f8-4dacac77116c | -12.89717 | -56.93554 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96a1acc7-8366-3530-bdd8-e78ed7a474d2 | -11.59317 | -47.75992 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 283986e8-c5bb-38c8-a407-ef50e7e13f71 | -15.57765 | -50.32021 | 2025-09-04 04:55:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b95a649-73a8-3f98-b59d-ea1ed740d701 | -11.95712 | -45.77635 | 2025-09-04 04:55:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53cf7117-f96a-3526-8cff-a1b7f0a921e4 | -17.15514 | -46.24385 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad272473-ddec-376c-ac68-833457416eff | -13.9473 | -53.98594 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 817bf62d-5f4d-3b30-9893-c04dbf8bbc1c | -15.5507 | -48.40582 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52346015-7028-3e51-abec-6b3217aa0ba8 | -12.86667 | -48.01768 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| db070067-1b38-3e68-8820-90fef97afe1e | -11.03718 | -52.0428 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e810f926-f037-3fa1-be29-b1b230bbada7 | -14.90965 | -49.62719 | 2025-09-04 04:55:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7927404-3f5f-3ef6-aed5-e26f2cd8310f | -12.94235 | -56.98515 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6edbd0b8-3ed9-3df9-b09c-e24b4c92dc30 | -11.83896 | -51.42514 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dafd3f4b-9db2-37bc-8793-1513684cb49d | -11.8801 | -51.53932 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7186fe9-75b8-3d31-bbc3-09fb35699189 | -11.63313 | -52.20506 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1d82360b-9023-3180-a4c2-aeeb4ba6ac0f | -14.81432 | -48.20439 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20a2f84b-7a82-35f3-86aa-9a2ee3360d04 | -13.81814 | -56.61179 | 2025-09-04 04:55:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 178d2622-f48b-3f3e-a002-a71afda4ad27 | -16.47287 | -46.86885 | 2025-09-04 04:55:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebec197e-5be5-333a-925f-78843d9cad55 | -12.48452 | -53.82867 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b14b2b8-dfa6-33d9-954a-1c714a479663 | -11.65007 | -54.52815 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 246163c5-c5e6-34e7-b4cd-1ad28c478596 | -14.53789 | -48.07139 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ad9a9e4d-36b6-3653-b938-1a17a247af26 | -12.88793 | -56.94675 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a0b32c2-1582-39d0-8784-3f0d4a26d3ea | -14.5679 | -48.04737 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8edc7897-f413-307c-9080-8ecf4baf1236 | -11.43884 | -46.91945 | 2025-09-04 04:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 578c562c-82c8-3ce7-93da-b07fc5fa2604 | -10.97135 | -49.75268 | 2025-09-04 04:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 435d87bd-acea-3a43-a3f5-936b7fcaa9b8 | -11.19805 | -55.01201 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b0a1c81-470c-3652-800e-9bb38f9206ea | -15.17675 | -52.35463 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 663b47ab-4e26-3487-a95f-8f65e5392a4a | -11.65285 | -54.53227 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 82b8728a-8eeb-3b32-bd2e-0406a2bf09f5 | -11.61834 | -52.18821 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07a2eda9-a479-344b-bf6b-706f05d9cc59 | -10.2476 | -61.77477 | 2025-09-04 04:55:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13022262-9c46-3210-8d3f-352dae4bf826 | -14.75909 | -48.08366 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a70b06cf-ff65-38b7-baff-0e1f05023913 | -11.64674 | -52.20716 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4efa7ec1-f094-353a-a004-2979b7d2c5e6 | -11.63536 | -52.19027 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fa792ab-28b9-37e8-a94f-d13123950b43 | -12.89307 | -48.02882 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 659f1319-85b1-31b4-b5f4-67629b6b1384 | -11.1001 | -52.04141 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 820c0360-f5af-3d60-91cc-669c099777c3 | -12.91398 | -57.01115 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5619844-f8d9-3e70-a60b-da1e2bd01358 | -13.09038 | -57.12098 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93079b6a-c25c-3b82-abeb-9fb34f04b8d1 | -12.96696 | -54.77065 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c1af295-2b86-3479-96b0-94226b24c98d | -15.04177 | -50.04736 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0815d85a-5a7a-3613-b06c-025e74482ae1 | -13.31131 | -51.76324 | 2025-09-04 04:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8917edb9-e738-35c8-b0bb-02d35a1f4d06 | -12.96915 | -54.77836 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed1621f6-e9f7-398b-81b3-03f87192f699 | -12.64312 | -57.0049 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11470a7e-830b-348b-abcc-3e74f982c581 | -11.58147 | -52.15598 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a624f6e9-8eb1-31c7-b811-2b6082851a5b | -12.24127 | -50.14724 | 2025-09-04 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ae5f7d3-0210-3292-b2ed-8fdaedc7b446 | -12.18756 | -53.89292 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2de7b824-016d-3e88-9bdb-6d93f62f58bb | -14.55543 | -48.07395 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 239356d9-1966-371b-815e-7182f5dcd2d1 | -14.98928 | -59.38916 | 2025-09-04 04:55:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e69db96-673c-3978-914a-1e2a4f2d936e | -12.99888 | -48.07347 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 875ff21a-60b7-3b96-a75c-2d34ec898044 | -10.49105 | -53.647 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ac9e8e6-4701-3922-8caa-067cf0df53f9 | -12.49006 | -53.83683 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74488b2f-246d-33d9-a0ff-b9c26afac699 | -14.20149 | -48.08302 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbd5e949-f609-3c8e-9791-e57f6ef906f5 | -11.88417 | -51.53597 | 2025-09-04 04:55:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b50c416-5de4-312c-b4f7-e04527b61e01 | -12.89439 | -56.95212 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b7478129-a9d3-3639-b6a5-b5e6eac46d33 | -10.45059 | -53.62247 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5f89dbd-f648-37a6-9607-4f6c061f9f32 | -17.97206 | -46.90696 | 2025-09-04 04:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d0eb412-ed43-33cf-80ab-e92c710bf927 | -10.61388 | -55.39953 | 2025-09-04 04:55:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2d24b70-b279-34c7-be71-3c38b60665b2 | -12.98989 | -54.75613 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c445b02-fd66-30b0-b10b-c9f30bd9cc4c | -12.81176 | -47.66798 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec895a81-e0dc-36cd-a777-9975af73869d | -14.75417 | -48.08708 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55cfab56-38f1-3434-8ce6-322e03969c59 | -15.01691 | -50.08355 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe9d381f-f5b8-35e9-980d-d8c6e6231c0b | -15.02923 | -50.08046 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ae7cb3c-faca-382e-a9a8-fdefe5ac3b37 | -13.30635 | -51.76688 | 2025-09-04 04:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea341890-d0ad-3deb-95d7-2cfa67806636 | -16.30598 | -45.6974 | 2025-09-04 04:55:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d12b3f61-1e6a-3fe5-9941-aafe86f03791 | -15.04092 | -50.08191 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aaf047f4-913d-3903-9b28-e183eb84c36f | -14.81998 | -48.331 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 154d2b47-4e22-3563-9d62-f606db7d7988 | -13.86309 | -47.98 | 2025-09-04 04:55:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 000e5eac-d439-34ca-9435-d861ac453de1 | -11.95619 | -51.34206 | 2025-09-04 04:55:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dac10eff-2ac0-3c9b-b0d5-8dec1ce26da3 | -11.73674 | -47.74934 | 2025-09-04 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7c5a08f2-448c-37d1-893f-dd9ee1d1500e | -13.85437 | -47.97851 | 2025-09-04 04:55:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5cd20260-07fc-38c4-b7ad-6eaf99f706a7 | -15.30239 | -52.73366 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d548b532-938b-3cd4-8861-dcccb1e618ed | -12.91179 | -57.00216 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fd79e889-84f8-38ba-9ecb-0f9cd4c28c9b | -12.61298 | -57.00812 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4c2eea0-0c29-3d64-9340-401894d43913 | -11.62117 | -52.19244 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7311c732-17fd-3a50-811d-4c613e782e49 | -12.93668 | -48.06266 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 213967e2-5135-318a-8cee-efb3b5e64c49 | -11.09274 | -52.02128 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c4dcc8a-2ead-340a-abdf-c66b78f5c8df | -11.95551 | -58.7297 | 2025-09-04 04:55:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7a14add-c596-30b7-b370-887b6b12edb7 | -11.73618 | -47.75338 | 2025-09-04 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 67ed5b49-09ea-3e78-bd19-18bac15ae782 | -10.48053 | -53.6273 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb04fb0a-58ae-3f20-bfb9-f1b984eadc1e | -13.75004 | -46.94769 | 2025-09-04 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d531ea04-e33d-3d5d-9c36-a0bf0c4d9014 | -13.08679 | -57.12035 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c4d10b0-9945-38f3-80ca-7f70d15c5caf | -14.57213 | -54.5525 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25a5e8da-3ecf-3ad9-8444-988cb2f73e1c | -10.94874 | -51.00103 | 2025-09-04 04:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 389d1d20-9278-3092-83c3-438f85d11a0b | -12.51781 | -53.83409 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e61c2dfc-1626-35a9-a5f1-91a51314ab16 | -16.30145 | -45.69019 | 2025-09-04 04:55:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cbb2bd1f-c3d1-31ef-9b66-6eafdf16dbb7 | -12.90857 | -56.93327 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 65c7a588-12e2-3543-8d7d-b784c384d225 | -12.97745 | -54.79077 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cbfb4d0-bb3d-36d5-ace3-dbab5e56bf4d | -14.59496 | -48.01259 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a6eca2d-f35c-3a0e-aecb-8ce956731d48 | -10.45503 | -53.61599 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35c796ac-2a0b-305a-85fd-f80c51925ead | -14.61601 | -54.5342 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b66c36a7-518b-31da-bf22-eef11a627e2f | -14.78352 | -48.13559 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f3054a9-f3f6-356f-8309-abc8f55e4ab2 | -16.51546 | -55.03048 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c385102-db69-3bd8-acc1-9374d0934b69 | -14.90804 | -49.62347 | 2025-09-04 04:55:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04815611-5d49-3f85-9f3f-7d078a747a0d | -10.48772 | -53.64647 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7561498-c4f1-3bdc-8408-8454f47192b7 | -12.47953 | -48.08007 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 792c05e6-1402-33ff-8468-660208381cf0 | -11.19407 | -55.0151 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f7391fd-2b5b-3745-a208-73db232eeb8c | -11.63085 | -52.19714 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8c66626-635a-338a-8c20-809532850ec1 | -14.88473 | -59.50362 | 2025-09-04 04:55:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c36376f2-ec9a-3dc8-a742-be28f5d5b1c3 | -13.26956 | -51.84556 | 2025-09-04 04:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README72.md)
