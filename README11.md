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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7356269d-1006-38c1-ae6a-8b4d8cacdc43 | -7.72409 | -44.39642 | 2025-09-20 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81c579bf-da0f-3b0e-8ac7-74079b2e6854 | -5.76253 | -42.77906 | 2025-09-20 04:25:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5c165761-fa02-3fd9-8ba6-36de39823012 | -6.38885 | -43.32328 | 2025-09-20 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d60dc067-5759-3aef-9fbe-d471ca2b70af | -7.37917 | -47.03978 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e551c95b-3a23-3423-9e71-1037289e5bd1 | -7.71831 | -44.38774 | 2025-09-20 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d665b6d-4c9f-3a10-ab87-42337203803e | -0.91232 | -47.55065 | 2025-09-20 04:25:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b18ff73e-26a9-3f24-ab5d-7908d65d2673 | -3.98705 | -51.05735 | 2025-09-20 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4f1c190-8c26-30a0-a474-6c7e2d83ac0e | -5.67384 | -43.16895 | 2025-09-20 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b546a2bc-a397-3cd1-a113-20dcbf71f9e6 | -8.05554 | -48.16219 | 2025-09-20 04:25:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19047c2e-8e41-3071-93b4-c1dcbe450c6a | -7.38854 | -47.04481 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 23854584-021f-3891-abc9-55fd99b198a8 | -7.25321 | -45.48998 | 2025-09-20 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| af13262c-0303-38dd-bccc-76a08213a341 | -2.2647 | -47.84535 | 2025-09-20 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55e8a4eb-dd4e-3494-8f12-12b65fac037c | -6.09633 | -42.8245 | 2025-09-20 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e3aaf815-d355-3093-8fd1-6663ab3ac34e | -5.57333 | -43.44852 | 2025-09-20 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6caa81e7-f21f-30e1-a0c6-e7db8b786475 | -6.38099 | -43.3514 | 2025-09-20 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0be2c4fe-60a2-3bd9-9b28-71ef6cdfdbbd | -6.64139 | -49.78214 | 2025-09-20 04:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f25563e-4833-3b8a-8e7c-f69deb93538d | -6.46837 | -45.68374 | 2025-09-20 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b77c1588-3c20-3373-b021-d43fb5141bb8 | -7.58123 | -45.50106 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc048dc5-df40-3c9d-82c6-a884ed48e0bd | -6.09661 | -42.8224 | 2025-09-20 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4311b2d0-674d-3b59-bc77-3de911757b65 | -5.8362 | -45.91832 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6fdc86e-7690-3ca3-a2a1-6ce6c8cd3bf8 | -5.55123 | -42.15394 | 2025-09-20 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 51b8ed6b-7882-3ba5-b6e0-ae0869b728e9 | -7.04837 | -46.65755 | 2025-09-20 04:25:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8374de2a-a9df-3cda-9b68-edbe411d3cd9 | -5.79576 | -43.633 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4630ee50-aedb-3720-a59f-99874bcc2a2e | -2.82911 | -48.65919 | 2025-09-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bb04365-5aab-34f5-8cca-7cebdc08a96b | -6.80937 | -47.86687 | 2025-09-20 04:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0833a3dd-aac0-3905-a6d8-f11a713e5232 | -6.77824 | -46.94718 | 2025-09-20 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db5c8eac-d4a9-396a-90fa-475365490f57 | -6.38159 | -43.34739 | 2025-09-20 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5a93d51-b5aa-302d-95db-a2d444a68a32 | -6.80994 | -47.86325 | 2025-09-20 04:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aafe33f1-0ee7-3325-be8b-c7c48c59768a | -5.98674 | -43.80786 | 2025-09-20 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eeae05f1-d0cd-3ee2-b957-0547c3f415c2 | -3.51143 | -52.75088 | 2025-09-20 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ef67a1a9-8943-35c5-907c-71dc40cede78 | -4.87304 | -46.83262 | 2025-09-20 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a66a869-3185-3767-ad08-679cb552a832 | -5.91248 | -45.07676 | 2025-09-20 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a662678-35ec-340a-87c2-cd24e46098c1 | -5.48086 | -42.95961 | 2025-09-20 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| be37e001-525e-3c81-a258-9b3caffba09b | -5.79868 | -43.63746 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25d7de23-2f96-3fdd-9618-0dbac2b89ef2 | -5.78409 | -42.78492 | 2025-09-20 04:25:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cf667401-315a-3099-8bcb-42d3b756d1cb | -3.35018 | -48.395 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6616aded-0ef1-3aa6-aa97-b4b3bce85088 | -7.8358 | -45.6381 | 2025-09-20 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c18dbb72-8a6d-3704-8788-455ec9acd0f4 | -5.60497 | -52.14945 | 2025-09-20 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae4aa392-dcdf-376e-aa13-7ae95f997200 | -7.25934 | -45.49455 | 2025-09-20 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20a25c30-4546-355e-90c8-7ed74ffd848f | -7.58566 | -45.49446 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b16d473c-b324-3fd7-8a72-bebc2eda8f08 | -6.59084 | -43.49827 | 2025-09-20 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 456dd723-dc71-332e-ad2d-c93f405f2436 | -7.59289 | -45.49197 | 2025-09-20 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efceaa25-cecd-3067-ac56-00a7b569d091 | -5.84045 | -46.28564 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a96ade1-4879-3cc8-90fb-c775b5e2cda0 | -4.66495 | -49.33128 | 2025-09-20 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a934ba27-089b-3313-9158-c9d46c7e3e46 | -2.14499 | -53.65147 | 2025-09-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4877280e-261c-362f-9e4c-2a595c06fa79 | -3.983 | -51.05657 | 2025-09-20 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea74aa22-f7de-3eab-8e77-5b4866ebd6bd | -5.55811 | -42.15977 | 2025-09-20 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ef272be4-7715-3a74-8eca-994dc279e755 | -4.92111 | -38.67992 | 2025-09-20 04:25:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a8162050-e488-3ad7-9a8d-d03575c2ca90 | -5.79048 | -43.64424 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf6344be-6bd2-3862-98c9-8c33c99e66fb | -5.79458 | -43.64084 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83679670-965e-3994-ad36-7304c43bb907 | -2.98683 | -49.29108 | 2025-09-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6c408226-151c-3cb5-8db6-584292970a1a | -5.82515 | -45.90248 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d1b5984-b377-34fb-85bc-9a97a8bab212 | -3.45715 | -51.21152 | 2025-09-20 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b141db07-3cdb-3988-804f-9ec426e4c327 | -6.81166 | -47.85245 | 2025-09-20 04:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de446b62-0de1-3439-8741-e69ba112e459 | -5.6313 | -45.94931 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb6c4d8f-1cd1-3bd9-a476-c3715fa2365c | -5.80753 | -53.43976 | 2025-09-20 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 172542df-f2bb-309d-bc3a-5a2e83b46968 | -5.55051 | -42.15665 | 2025-09-20 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7524ec1c-02c6-3731-8d44-7cbf18087332 | -3.23012 | -47.13023 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99049e26-2acd-31f3-a0ea-e7726fd8c2b3 | -4.72046 | -46.13288 | 2025-09-20 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ab171c4-a6e8-3563-8462-cbc83dd8aeb0 | -7.9528 | -43.87986 | 2025-09-20 04:25:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fb4edb5-500f-357e-8a85-0373b718c717 | -3.97392 | -49.96755 | 2025-09-20 04:25:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dbf1050-8c61-3594-abc8-4449adfae257 | -2.79476 | -47.15113 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9367270a-a1af-34b8-a0fb-515d0af66600 | -5.69039 | -46.35393 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0f371f8-fe6d-399b-9d48-8436f82622a0 | -6.09507 | -40.89423 | 2025-09-20 04:25:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 46b94a19-19c0-3eb3-9b5f-9011e573caae | -7.08209 | -47.32725 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e754eed-fc92-3155-850b-570e5c20cfdf | -8.14019 | -43.62162 | 2025-09-20 04:25:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28302d26-ad88-399e-be66-3b248b294bce | -3.81669 | -41.01091 | 2025-09-20 04:25:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 01b04310-624a-3c99-a9b0-20da9a58306a | -7.18251 | -44.40965 | 2025-09-20 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30064991-8fae-361d-b5e4-dcc5797751d1 | -1.27086 | -47.87048 | 2025-09-20 04:25:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45db1036-1f85-3a7f-8b8e-a9a7752938b9 | -6.21361 | -42.64351 | 2025-09-20 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| df4a7609-ae8b-3af1-ac31-3f877a37744f | -6.37741 | -43.35086 | 2025-09-20 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ab66ac4-a317-3492-a379-d686c1d2bf54 | -5.49546 | -45.11318 | 2025-09-20 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38ef9cee-2ad0-37f9-b126-635f657308a8 | -3.98242 | -51.06009 | 2025-09-20 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21fc38b8-932d-36cb-ae77-cd369eb8dbad | -5.88892 | -45.99705 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f4804cc-c13e-355c-aeaa-fd94e5d8bec8 | -2.98967 | -52.62986 | 2025-09-20 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5f4c8f7-1f3c-37a6-b10a-2f2971c70577 | -6.10265 | -47.85432 | 2025-09-20 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98d502d9-9bbd-35da-a344-597d6a9cfab4 | -5.82738 | -45.9099 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc490bfb-996f-3934-95d4-dc9ea66180f6 | -5.85668 | -45.90024 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5529b11-a4df-3441-a25d-3cc96a110403 | -6.00842 | -43.71148 | 2025-09-20 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be3e42e6-486b-3f13-86f7-98d2be3b4f56 | -3.72984 | -51.35502 | 2025-09-20 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c1e83bd-f5e3-3a84-b53a-e1ebee2d5f4a | -5.63237 | -45.94241 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c7ef0c6-89b4-3143-a8d2-fd1bae0ab412 | -5.35772 | -43.00667 | 2025-09-20 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| de380bcb-668e-34fb-8d4d-b0c9a6b0d50e | -2.8327 | -48.65975 | 2025-09-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9002eaf4-1dbd-3b65-a5a7-669adbd39564 | -3.5675 | -38.8928 | 2025-09-20 04:25:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 12396d11-c1dd-38cc-b8d1-92da7b148133 | -5.55056 | -42.15858 | 2025-09-20 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 998a3ce5-a688-324c-9a99-e43664ff4e91 | -5.30455 | -45.57642 | 2025-09-20 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55207cdc-5bbb-366d-9099-8774355e0452 | -3.07721 | -48.81475 | 2025-09-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3ada611-7da2-39af-b2bb-fcb64e787d05 | -7.16964 | -39.76855 | 2025-09-20 04:25:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| acbc123f-1dbb-313c-8cc8-ab3300abd3ab | -5.83661 | -46.28857 | 2025-09-20 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e48fdd0e-708d-395b-9c34-cabc722b9640 | -6.05586 | -42.69376 | 2025-09-20 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6b26dde0-54de-369c-a596-be53ac3911a4 | -5.78471 | -42.7807 | 2025-09-20 04:25:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b8b06a3d-7752-382b-bcab-fcb148d97236 | -5.48023 | -42.96379 | 2025-09-20 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c80cd840-1954-36bf-b214-7dbbae235ce4 | -7.08762 | -47.33526 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb836dd4-7951-30ed-99b2-7fe5619ac0f0 | -5.09363 | -41.13897 | 2025-09-20 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d5142294-c007-3d02-8e3e-c3c283f104b1 | -3.15917 | -49.4784 | 2025-09-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13f22731-5920-33ee-b05a-d9091f8a94a4 | -3.45361 | -47.63017 | 2025-09-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8480266f-933d-340c-a132-d0678a68e971 | -5.61803 | -43.46608 | 2025-09-20 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffaf8f75-cc7a-3b99-8cc6-1a5424e3ed4f | -7.38578 | -47.04082 | 2025-09-20 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ab46b5f3-7e51-3c57-842a-9cd9fb780232 | -5.04977 | -47.9086 | 2025-09-20 04:25:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a537dac-9eeb-3086-a337-622c63dbacf2 | -5.55358 | -42.16187 | 2025-09-20 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README12.md)
