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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b2db219-1192-35b6-9262-772cfe034cf1 | -2.61749 | -51.80844 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1e7dfc9-fe07-3d82-af0a-7a6aaaa0d890 | -2.9907 | -51.32914 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37e8b382-89ff-3e17-92e6-c6a1c8b7473f | -2.20671 | -52.09798 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a2223976-480f-3b4b-abca-da6065f9719e | -2.26712 | -53.47203 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 193bbdd4-19b4-3f54-b794-7065564afc2f | -3.69166 | -51.37031 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd018116-50e7-3630-8511-f7359425f824 | -2.55952 | -56.68718 | 2024-11-29 05:22:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d3d9ebb-2619-3850-b079-d01632c62a54 | -1.98811 | -50.67042 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1da1980f-5670-3dbb-bb1c-0ca345433539 | -3.49317 | -53.81127 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c3311e2-f700-3d56-9927-d7f10789dc3a | -2.65919 | -48.77683 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f1c5cbad-e2bb-3d58-a409-aa5287c00493 | -3.2516 | -53.63317 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| be5d35a8-0e9d-3072-b507-c9cbe9740602 | -3.24973 | -53.64576 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3e19131a-7654-3374-bd98-a5515b93c06b | -2.80398 | -51.58764 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 13347444-ba12-39c2-aa0a-7b318e7a8ebd | -3.06017 | -53.6828 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d25458a-267b-3959-aceb-0251dfe29a8a | -3.50303 | -53.80465 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4cf510b-a8ae-372c-bfe0-3b487a6ebff8 | -4.51761 | -59.80973 | 2024-11-29 05:22:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 055ec097-cd47-3bc7-9f25-ef161f2d49b5 | -1.68376 | -54.23215 | 2024-11-29 05:22:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90524455-9ae9-3697-93e9-4ec92188d974 | -2.7497 | -54.11184 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8084ee52-2c10-31c4-9bc7-6a5145395647 | -2.8359 | -54.10941 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a31ea7a-e0dd-3ed6-b933-2c7915fce633 | -1.76535 | -55.67504 | 2024-11-29 05:22:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 119102f5-32b8-3f6b-9c76-ee035777bf95 | -3.10314 | -53.82134 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec036a25-f6d8-3cc6-a599-cb4715ed715b | -2.31502 | -51.96233 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fa237e0-e515-3ce4-bd15-9897cf4378d0 | -1.35982 | -54.65519 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62ec1657-4481-392f-ba92-fc926ce3318f | -8.28173 | -48.03645 | 2024-11-29 05:22:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 241bce7e-48c4-387f-ba92-f60d0e59d4b9 | -3.49195 | -53.81928 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16e145b3-2850-309a-86ef-6026c898b09c | -3.49933 | -53.79989 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae8bc10f-c3bc-39d7-9277-d96f67e77a60 | -2.98664 | -53.27959 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d76126d5-7f7d-39c6-8638-d9a7db78f96f | -4.43604 | -46.57302 | 2024-11-29 05:22:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b639de6a-8a18-37d4-9df7-8e6829a503ef | -3.2422 | -53.93097 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ff81c42-2124-3d19-a37a-c124c112a6bd | -2.86219 | -53.9949 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 102b30dd-442e-3884-abce-d1611b7e2607 | -2.66311 | -48.78281 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 03186865-5156-3e11-91a1-5bef29a421ff | -8.1415 | -54.85157 | 2024-11-29 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c57eabdc-b400-308e-b25e-02aad897e128 | -3.67145 | -54.28336 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fcfa0e2b-1e9d-35d2-978e-ae7c9ccf859a | -3.86303 | -50.15501 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aa13c02e-cc1d-3955-8e12-a79652ded401 | -2.5901 | -53.97175 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4d7b6dc-bfaa-34f0-b91d-506dc0fa4598 | -2.1473 | -50.61263 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 686124fc-c901-3ef1-8dde-fe57aed955c3 | -2.60558 | -54.27171 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 322c5dd3-f35d-3b1b-9c85-08021df8a4b8 | -3.47016 | -50.52703 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23206765-dea3-3f1a-b48e-9757038a2fa0 | -2.87707 | -53.32203 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7777c88b-99bf-349f-965d-16a7f5be85fd | -4.1136 | -50.77757 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fda49fc7-2c41-37fd-9f5b-12e9b51d53e8 | -3.43309 | -54.12012 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc7203f8-0e77-39ca-8eb1-a7dcbb9fd1bd | -12.30692 | -56.6977 | 2024-11-29 05:22:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b97139bf-db3b-3f28-b99f-ba08f22732ab | -3.79298 | -51.2598 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a350211-b120-367d-b375-c8d9dd168dce | -2.49131 | -49.05052 | 2024-11-29 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44ac2051-5744-3082-a6fc-e47802c99f20 | -2.25823 | -53.74669 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80a967bb-0960-3bd0-afba-31a424a05b36 | -3.57741 | -50.3345 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2b02838-651e-3a87-a291-56b3edf99279 | -2.97135 | -53.2906 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 8ceea47d-f380-394e-9f94-d31d920f7086 | -2.66329 | -48.79096 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 7eda595c-d3f5-3dfc-bd2f-5a50ff0ca9ab | -1.58145 | -53.83735 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7db021ba-5bec-3351-8a20-5f0aea880ff3 | -3.09475 | -54.02374 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6d1acd37-38eb-3ba9-8dc8-27264f91f35e | -2.75751 | -54.11691 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0ed402b-c3bb-345e-b7c8-614d64ebe854 | -1.70986 | -52.63507 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 30ae4e3b-6d2b-3559-bbdb-61c7eae9fb0a | -3.72375 | -50.18488 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d2b7d01-3046-3c84-806d-e32f02d430c8 | -4.19499 | -48.56458 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a41ba209-fcb1-36a1-bc65-174899418b3d | -4.59469 | -49.56611 | 2024-11-29 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1c4325f-4448-35fd-91ac-ce19b8cc9bad | -1.67458 | -52.49596 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7eda7f08-ffb7-39c9-b3da-37e62085ccb2 | -2.98531 | -53.28853 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 7e1b9680-7a7a-3bb3-bdfe-0d8085ec8fe5 | -3.04411 | -54.04531 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dcafa19-3102-3357-b557-335df1ff549c | -4.218 | -54.76448 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c40f09b6-87bb-30a0-ad19-636fc5af2bf3 | -4.06987 | -47.02903 | 2024-11-29 05:22:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c15d6925-84c1-3d42-b5dd-09fcb6ebb14d | -2.95725 | -53.88425 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91c666a8-7a77-339f-ace2-63fa76ac4937 | -1.92326 | -52.88575 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b7c8ee6d-a477-3461-9861-5a97a3b7e21d | -3.5428 | -50.18498 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b103b09-950a-320e-a3a0-f7db5124900b | -4.34052 | -47.57454 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6c9764d8-e8bb-393f-9a00-ac3feb997478 | -3.11948 | -53.10698 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a454bdc-08e1-3350-b32c-72477b7bfa8c | -3.20167 | -46.56279 | 2024-11-29 05:22:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f71f6b1e-39dc-3f05-bd71-d30586c9ead7 | -3.22631 | -54.17731 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e0cb31d8-c22f-372a-9e45-4a614113506f | -2.65793 | -48.78558 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 7654436f-dacb-3147-b740-a8f3957c61f4 | -2.83412 | -54.12084 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 524ac3c1-d332-3d1e-a205-b90d51f4a6d5 | -1.52788 | -54.22442 | 2024-11-29 05:22:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8002abd5-40ce-33fb-9f7e-d72dbc6ac949 | -2.75332 | -54.11628 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 37c9f340-e6fc-3ced-a790-5466bf61043f | -3.47123 | -50.52636 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d216ec1e-140b-3e92-b7d9-8d214f90c2d6 | -2.57805 | -49.99767 | 2024-11-29 05:22:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f7fe5ea-9eee-3c49-b2d7-b089851d7552 | -3.50181 | -53.81266 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8bb46b3b-4a3d-342b-bfca-67f521e760b4 | -3.4499 | -52.007 | 2024-11-29 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b4bd8a5-fb12-3bf0-8f48-ebc0ea238aa2 | -3.27075 | -53.30526 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 363058cc-b44c-3ccd-ad89-edf66291522f | -2.1478 | -50.60937 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7bfd5e3-3a24-3c74-a992-999508846a0b | -3.59109 | -51.14165 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f2e2135-75de-3d9d-8a6d-ab48a9ed4538 | -3.12972 | -49.40713 | 2024-11-29 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3778697a-07da-3da6-a230-d3528dc49128 | -1.99068 | -53.28772 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19c71ef3-26c6-3796-baec-f1ed575b4f4e | -2.8329 | -54.10114 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f85ad7d3-2f7e-3349-b0bd-9a2d9edcfe12 | -3.71106 | -51.79467 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 08bdb83b-68e4-33fb-9b6f-a2106137799d | -1.58061 | -53.83822 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c330c037-a0bc-311c-b23d-2681d40bde7e | -3.39059 | -54.28729 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 345fd3bd-da7a-3189-a4e8-49be5ee760e9 | -1.69761 | -52.4481 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| b6195ae9-d2ea-3094-b5aa-8c0c1ca14ad4 | -2.84432 | -54.02791 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ae09c14-a711-3a86-aac9-35abebcae0cf | -1.62882 | -53.86431 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29e0e0a0-ee44-3b38-a419-651f1ea17e31 | -3.26581 | -49.89442 | 2024-11-29 05:22:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 902be548-9600-3212-9159-120b942d0537 | -3.23805 | -53.63305 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19346181-5967-3999-ac69-52bc84dc58c1 | -1.42598 | -55.27702 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c77cc734-14b2-321f-b753-bbef42956c18 | -2.36825 | -56.11496 | 2024-11-29 05:22:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ee0edb7-7c17-386b-82b9-93edcad60706 | -1.7221 | -52.49363 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b9f98f1-3626-3fb6-b01f-ddaf568c8251 | -4.78476 | -46.11525 | 2024-11-29 05:22:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e13b7fc9-7b7d-3aee-9385-4e6707803d90 | -2.29743 | -51.98104 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 98d5ad79-4a27-3248-a7fa-64175c8023c8 | -3.57098 | -53.02148 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3c26fe4d-154f-3004-9438-9917b3d064ce | -3.1134 | -54.47385 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6b1096a-def9-3626-a372-48c714ec4047 | -1.87952 | -52.65844 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de55ba56-d766-31c9-ad91-4e318c533ca8 | -3.09626 | -54.56071 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c8fc18a-9f47-3fb4-8363-6f33a695cea8 | -3.56736 | -53.26255 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c55628e-a68f-3f33-91b7-659ec9f4c51a | -3.53395 | -52.15795 | 2024-11-29 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8d4b23f-a5b3-3aac-ac7b-ed678a70f598 | -3.09767 | -53.72726 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README96.md)
