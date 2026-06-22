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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6237a90-206b-3913-b2b3-74105eab781e | -9.07818 | -44.7549 | 2026-06-22 04:23:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2d8fbe1-eb18-374d-bca2-e0afe27435d0 | -6.24109 | -48.53353 | 2026-06-22 04:23:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 576a62d9-4d86-3fe8-ac28-3cc8866b4a29 | -8.87465 | -46.9535 | 2026-06-22 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2c63222-acf6-3dd4-8a3f-a4f56beef98e | -7.95742 | -47.41393 | 2026-06-22 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f43637a-0471-3bf1-aaea-bbeba1cf3889 | -7.31938 | -46.55376 | 2026-06-22 04:23:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e09c3575-7d5c-3095-8015-8b07ea1f3566 | -4.27981 | -48.65958 | 2026-06-22 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1d7c1af-2610-3fbc-9540-590b8da7e1a4 | -7.96718 | -47.41955 | 2026-06-22 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c9d1d9cc-9c81-3cbb-91bb-72fc7a1b9405 | -6.23733 | -48.53304 | 2026-06-22 04:23:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b44d15d-dfa7-3c28-b67b-87d60741a288 | -8.87583 | -46.94617 | 2026-06-22 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49b1f6fe-7487-3a7a-aba5-f5154969e1de | -8.61913 | -47.79481 | 2026-06-22 04:23:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bdb19189-996d-3cb7-a0b4-b342fca6185e | -9.49904 | -42.99431 | 2026-06-22 04:23:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cf197fac-9da5-3c3d-82a3-0c711f3a057a | -8.87524 | -46.94983 | 2026-06-22 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f10de6c-aac4-37ab-a1af-812202bfca16 | -8.81169 | -43.93185 | 2026-06-22 04:23:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a51f2d09-150b-3286-a467-ae6ff38d33de | -6.50538 | -44.69824 | 2026-06-22 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0bf49f6e-52a5-36bf-b79d-b0248de31a5d | -8.87682 | -46.94593 | 2026-06-22 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1651e08a-2580-3d4e-b9ca-e5188acce271 | -8.88139 | -46.93925 | 2026-06-22 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cf4b36c-4290-3a8c-9e44-ae3d2a1003b6 | -8.7017 | -47.97813 | 2026-06-22 04:23:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 297e85be-a4ed-3b35-a3cc-238f7f989e61 | -7.32217 | -46.55795 | 2026-06-22 04:23:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e763459-3caf-32dd-9812-b1f0c5d93d18 | -7.96309 | -47.42271 | 2026-06-22 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0fff5ea1-3d44-3e56-a328-57d5599f866b | -8.87801 | -46.93869 | 2026-06-22 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| beb34dcd-3a80-378e-afb3-ada542544972 | -7.27692 | -44.09063 | 2026-06-22 04:23:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a10c04c-2874-3cdf-836e-94daddfc485a | -6.50593 | -44.69478 | 2026-06-22 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0fa7ad93-17e4-39e7-9cc5-670e8b1a01bc | -7.96372 | -47.41891 | 2026-06-22 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 32722153-129b-33c4-adf5-a1b6a20269d7 | -7.95615 | -47.42163 | 2026-06-22 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9232837e-9549-39b2-b547-540fcf64a656 | -9.03777 | -47.26908 | 2026-06-22 04:23:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a69a8726-9a11-383f-90ea-255b25781410 | -7.95962 | -47.42216 | 2026-06-22 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13f9f2aa-f36c-30ec-8351-f2489e1ebaa2 | -4.25341 | -48.54451 | 2026-06-22 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82089b93-7398-3fb7-9c72-a6b24b720e7a | -6.24181 | -48.52921 | 2026-06-22 04:23:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08c95e9a-497c-34a7-a2f4-1ae2c6cf72ab | -6.50705 | -42.21774 | 2026-06-22 04:23:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 88f65e4a-daa6-368c-8b55-6687ebceb923 | -6.23804 | -48.5288 | 2026-06-22 04:23:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a5adf201-f5bd-3ff4-afc3-bb118b5ae192 | -8.8808 | -46.94287 | 2026-06-22 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba218740-99b3-396d-b5c4-d1b89b8d6449 | -6.50263 | -44.69426 | 2026-06-22 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0bffa4fb-5b1e-372e-b1d0-630a99f4a1d8 | -5.86288 | -46.25129 | 2026-06-22 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc04e034-fd89-3147-b7ae-52f779a37269 | -6.69604 | -47.43105 | 2026-06-22 04:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97694ebb-491d-3fed-8f52-3b62b5163349 | -11.0598 | -52.47829 | 2026-06-22 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1233a85b-517c-35b5-968e-55a9b24c456b | -14.98273 | -45.44647 | 2026-06-22 04:25:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b0a22ce-c9bc-326f-aee0-070ee88057ee | -11.11402 | -54.14571 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3db191f1-7c35-3ba0-b022-9b11895f10d9 | -13.51923 | -52.1646 | 2026-06-22 04:25:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67ee8f2d-1c85-343f-9da5-434f55904a89 | -10.16959 | -51.6618 | 2026-06-22 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1c8796e9-5f6b-30f3-83e8-7ca38f715e6e | -14.10504 | -49.88248 | 2026-06-22 04:25:00 | NOAA-20 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd0338b6-0688-3dc1-bfab-5b77a9790804 | -14.91633 | -52.00316 | 2026-06-22 04:25:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6da8fbf6-894e-3bf4-a3a6-0e3ca5b08022 | -17.22212 | -43.67745 | 2026-06-22 04:25:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 64d5c565-58eb-3202-a4a1-a55b148d9737 | -14.10578 | -49.87819 | 2026-06-22 04:25:00 | NOAA-20 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 198cbb80-1654-35e4-9572-6b96ced60f23 | -10.56195 | -46.24199 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d46ed909-ddac-36f3-b91c-723ae580038c | -10.17461 | -51.65847 | 2026-06-22 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88dad5dc-9fc9-3461-b4a3-0c8ae518619c | -11.05089 | -52.47671 | 2026-06-22 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4603b9c4-0934-3f34-b08d-340fb6e0afd0 | -10.60344 | -47.45824 | 2026-06-22 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b34f97fa-e9d8-3505-8abb-70a2713fa00e | -10.25117 | -49.59998 | 2026-06-22 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42f28496-e6cb-3e36-a385-88a0191542a0 | -12.43456 | -58.40455 | 2026-06-22 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05a35a34-2d3a-35b6-8837-7503945c8cde | -12.06507 | -48.42878 | 2026-06-22 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3946696e-7ddf-39c9-a88c-5469e30cf245 | -10.5542 | -46.24793 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 110c3399-8bd7-3148-9634-f4b8f32f6eba | -10.90962 | -46.32106 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e99dde88-5dfd-3388-834b-4e91da1704d7 | -10.9374 | -46.42247 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 465acb76-a05c-3ea7-88be-f1babf33d114 | -12.45717 | -46.52456 | 2026-06-22 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69a2049b-d439-3c1c-8a60-2c914830c43f | -16.30762 | -47.6263 | 2026-06-22 04:25:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 530cdcc1-3969-3009-81a6-a12f105f4387 | -11.04642 | -52.47596 | 2026-06-22 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e78452df-0cbc-33f0-9e30-01ba10882380 | -16.02506 | -43.41971 | 2026-06-22 04:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82d2ca3b-8573-365e-be49-657920405e17 | -13.29053 | -45.19048 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 495428d9-0f98-3ec5-a1ed-431200d2179f | -10.55808 | -46.24495 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61a9addb-1652-38bd-9c6e-e7490e6accb6 | -12.0692 | -48.42547 | 2026-06-22 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b7ca89c-ee96-3ec3-9927-5e2adf2c9093 | -10.94735 | -46.4241 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4b89e69-eb9c-351d-be0c-038ea7bf0624 | -13.2967 | -45.21741 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d8c9b64-61e5-35dc-97a1-7181aa0b563b | -11.11016 | -54.13991 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f39d8b62-7d0c-31a2-91cf-91b3ce6764cd | -10.54068 | -47.7127 | 2026-06-22 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dea1fc9b-7fbf-38b0-9fc8-97b4c6feddcf | -11.11012 | -54.13887 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b4b1032-8995-361e-8cd1-60b39f808a4c | -14.87854 | -54.54938 | 2026-06-22 04:25:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 171f4866-8969-38dc-8214-a3dd548e49fc | -11.9076 | -43.41127 | 2026-06-22 04:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 069644e6-acad-3a11-af13-7d4aec869527 | -11.90409 | -43.41075 | 2026-06-22 04:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52ff79ac-ac58-34f6-8690-a7614d05e521 | -10.76978 | -54.11049 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9745d588-8c83-327a-be88-3d8a637d72d5 | -11.10411 | -54.14362 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 458d2b21-e24d-3cc9-8089-5be0a086793b | -13.28718 | -45.18995 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09646620-0cb1-3f0a-8b46-f78d12f7b744 | -10.90687 | -46.31701 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75841626-dccf-3f9b-ba2f-c0b7cf001f56 | -14.10867 | -49.88311 | 2026-06-22 04:25:00 | NOAA-20 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b8d7d08-9457-3b4c-8700-c1c0a9585c37 | -11.10024 | -54.13789 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69a47c8a-591d-3545-934a-82fda22a412f | -10.56251 | -46.23847 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62247c72-4e93-3be9-bc6d-d8896692523c | -10.53477 | -47.72719 | 2026-06-22 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdd4a961-7dc1-3a16-9c9e-e015e01f2380 | -10.56639 | -46.2355 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72d9bd67-0931-3663-bbc4-f8bd292ce060 | -11.10517 | -54.13782 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bab7f798-d2da-385d-87f4-935208f80487 | -10.53758 | -47.73153 | 2026-06-22 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fc2ba97-422b-3cb2-85f3-8c059cd42cfb | -15.38807 | -40.82307 | 2026-06-22 04:25:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0f9d209e-18d7-3702-9f80-60e1918afd4d | -10.17888 | -51.65923 | 2026-06-22 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb380316-d171-3e0d-83a9-0f759e7f9d7c | -14.97825 | -45.45325 | 2026-06-22 04:25:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f1a78d6-6cb2-3bda-a5e8-029c30c8224d | -12.42625 | -54.17512 | 2026-06-22 04:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f8cff28-a9e3-3130-8539-cc24ee4dbcda | -11.09915 | -54.1426 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89e61625-1816-3579-90fa-926c5c8a30e1 | -10.60623 | -47.46252 | 2026-06-22 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd7f8170-e26f-36b1-b20e-8a2d10721941 | -13.51504 | -52.16383 | 2026-06-22 04:25:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad7f76d6-b819-39d8-a4d7-01c5e9aa8446 | -11.10906 | -54.14569 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d6ec7b46-ae72-3f02-8fc3-da91fda45727 | -13.30228 | -45.22572 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cbc8239-e04a-397c-96dd-45902d93eeac | -12.46953 | -55.13306 | 2026-06-22 04:25:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbf9c29d-c176-35b3-aaa2-a504f2c53e2f | -11.20346 | -46.77536 | 2026-06-22 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 374b700d-045e-3fea-b0ee-6355dbc4dea8 | -13.29501 | -45.20604 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5af04062-e637-3ff0-9f9d-fb011b14550e | -10.94071 | -46.42301 | 2026-06-22 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d30fb0f-1dfd-3d80-82d1-607d9d87431f | -11.05535 | -52.47748 | 2026-06-22 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c19e7f8-3150-31f5-828b-9e2e723ef9c0 | -13.30059 | -45.21434 | 2026-06-22 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3999eb47-1a1a-3f33-871d-67123ca193d7 | -11.05615 | -52.47298 | 2026-06-22 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2bd397c4-0d8e-313b-bdc9-da12922e915f | -12.45386 | -46.52401 | 2026-06-22 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 546b8081-6074-3260-acee-025ab3a4eff1 | -11.05818 | -52.48735 | 2026-06-22 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0041da4-edda-3e7e-80e3-1b6597f9b3da | -11.10021 | -54.13684 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a39aeac0-69d9-3107-abd8-fd0a8dbdce88 | -12.43207 | -58.40827 | 2026-06-22 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9e3f86a7-b57f-3b9c-a6c4-60de8808fed8 | -11.09419 | -54.14162 | 2026-06-22 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README6.md)
