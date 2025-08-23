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
| 0a25fc61-f708-3d15-bc2d-9236d2c3e442 | -6.18045 | -45.43145 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 056462f1-5814-32d1-b0c9-6bfc4e55e310 | -9.02715 | -59.01542 | 2025-08-23 04:51:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97ed830a-ff8f-3f3c-8a41-3c40fd244d61 | -10.19258 | -46.84254 | 2025-08-23 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d897602-9d02-375f-8f8e-435bad201af1 | -6.43527 | -53.38878 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0fb81cf-f4af-39be-9948-ed265b63f089 | -7.43064 | -45.41795 | 2025-08-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3342d97-cc77-3dc9-aa6d-417ec0140596 | -5.83829 | -52.07265 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f24e48d-2a0c-391a-ad9d-9cd4824d3886 | -9.20593 | -59.46084 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0fdaabcb-d5e2-3162-a2a4-28d24b194027 | -6.38968 | -45.52372 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 202393b9-64e0-3f3f-8d7f-b93174d55879 | -9.22895 | -59.7609 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8acb66c4-afd8-33ad-bdd1-aab2334139dc | -11.13707 | -44.7565 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee692f2f-0ca2-372c-a808-30026fa227ee | -9.19605 | -59.45066 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 62b7eb5f-10dc-3273-b6a8-2d3108de9b43 | -9.15837 | -59.59281 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4135f6f-71f8-3b7e-8d82-e2ee0eeb073a | -9.37272 | -48.25183 | 2025-08-23 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9aeee4ef-f5e5-31bd-99c5-7f23a65d87c1 | -6.60263 | -44.56541 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| acbf256b-e424-30b2-8810-a489404d62af | -8.85745 | -52.04722 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96cd6b52-8b21-38fe-a772-4e5650b7bd1e | -7.64558 | -45.23969 | 2025-08-23 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 71cdecea-8b61-3b5d-8253-03c22938d9cf | -3.51529 | -47.20729 | 2025-08-23 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e760459-313b-3464-aaee-e47e072dbee0 | -5.80323 | -59.21523 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3eb62540-b723-354f-bf7c-70ca84f21392 | -7.73069 | -67.0742 | 2025-08-23 04:51:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7980c0d2-013d-3c96-abf0-f39091ca9c3e | -5.78034 | -46.28864 | 2025-08-23 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 633a36f5-a018-3970-8203-4d547030a5ba | -9.18076 | -59.6523 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d8ac6ea-c7d0-37f1-b6b8-f0d045b5df96 | -6.12285 | -44.4103 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d0e58536-6411-31f2-9fbb-eec952ac38a9 | -5.76217 | -57.60212 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08259d9d-e92a-3024-a90a-735352de5803 | -9.20658 | -59.482 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e8e0cce-a604-3f60-8649-c889944d0747 | -4.18194 | -47.20743 | 2025-08-23 04:51:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd657717-352a-326f-91e9-f9f03c1f9994 | -8.85464 | -52.0431 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0e6ce4bd-61df-3fe1-8b05-c1f868366971 | -5.88215 | -53.61613 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f12e99f-5c41-340d-abc7-a93cebefac85 | -7.7353 | -67.06851 | 2025-08-23 04:51:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 319f12e4-abce-3dcc-b4a7-8c442b03b20b | -8.60203 | -62.62495 | 2025-08-23 04:51:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 166059e2-4f81-389e-93dc-c72084ff48e3 | -9.20032 | -59.45144 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e8204de-4890-3469-b41e-4573f9d03112 | -7.84146 | -46.97129 | 2025-08-23 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f229241-a8f6-384f-b434-636a10d37535 | -9.19889 | -59.65084 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 240c8dda-e24c-3724-a1f3-51e6ea605c64 | -4.59545 | -48.95931 | 2025-08-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb3c2dca-b3fa-329b-beec-c71c941367ad | -9.19381 | -59.6543 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a229877a-d70b-3d82-9525-73b74a2e6115 | -8.07936 | -43.68333 | 2025-08-23 04:51:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c887cc02-cd61-3a38-aa7b-79c4d098189b | -7.08177 | -60.06302 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b337d3ce-a95f-3885-a0ca-e147db347f65 | -10.68754 | -50.12259 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b08c467f-c6b0-3f55-93a0-f6c3206a2c1c | -7.50592 | -63.83662 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a2d02fb-b716-3d5f-b91c-81c4a9a69f07 | -6.37483 | -45.54414 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 7fe4c955-949a-3bda-995f-17615d4d62a8 | -7.31835 | -59.61483 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05ae8d1f-f2cd-3ac9-9ba0-1df7bac9055f | -4.13894 | -46.46154 | 2025-08-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5944b13-5f72-3c9d-bfda-42560f9dd615 | -7.81464 | -63.55937 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f7497ee-4f93-3371-864e-751b9901605d | -5.1103 | -43.21864 | 2025-08-23 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c7b3872e-8a91-31f4-8704-71ceaad9d568 | -9.5986 | -55.35222 | 2025-08-23 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 42d2cc8c-0bef-3165-840f-d0af420fd8d9 | -10.64931 | -50.12591 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca7cf1f0-6bb0-3a19-b612-680a7f84901a | -10.71141 | -48.21432 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed6deb7f-0b9b-3a74-965b-0ad1917e2115 | -10.63696 | -50.13309 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2346241-fd2a-3ba3-bb79-e4ebfc3a5fb7 | -6.52883 | -43.87009 | 2025-08-23 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78431d6f-96b7-344a-b613-9ac699a54b98 | -5.75933 | -57.5945 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acd7027f-62de-3703-8481-95695b9a7eb6 | -4.34575 | -46.46631 | 2025-08-23 04:51:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 34.8 |
| aab875de-d1b3-3701-9008-e7a19fa63861 | -5.73297 | -57.60455 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e47b058-0cef-344f-95b5-941fbf5f3b80 | -9.22458 | -59.76013 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52c0a563-ad97-39d2-ae62-8fb6dbcd19e7 | -6.32046 | -43.75192 | 2025-08-23 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 03fd0440-c81c-385b-94a4-6e8873ad0c3e | -7.17423 | -48.42126 | 2025-08-23 04:51:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ddf7260f-18ad-3d42-9403-26fdf75284ac | -4.13391 | -49.36179 | 2025-08-23 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d0c1f98-77e7-37ce-9df6-d7d04c292a56 | -6.23834 | -47.31448 | 2025-08-23 04:51:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fbb43fb-6eb9-3e5b-a30d-d7397b035f2b | -10.74666 | -48.24985 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2cfbd70b-3fbb-300e-be98-a3e2347bda3f | -5.44078 | -60.17985 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4979757-835f-35f5-abbe-4a3314a61f52 | -9.20101 | -59.44738 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 31ce7e6a-c0e1-3b64-91ca-3d0b5e8eeaa3 | -6.586 | -59.87553 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 22850c37-81f9-31b0-ac49-2540100e171b | -5.87435 | -57.75499 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a81ea521-17de-332e-a857-f627b1223e8d | -8.90773 | -51.04693 | 2025-08-23 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20e4df7c-b5df-372d-b1f7-5e3410c59cca | -7.21059 | -45.31267 | 2025-08-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77be9666-7518-31b2-afd1-01f915f34bd3 | -6.05497 | -53.87839 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1b4826d-664e-34d2-a30f-83799333ac3c | -8.534 | -48.86008 | 2025-08-23 04:51:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de9f6d1d-c97a-32a2-9f6e-5915506ab48a | -8.29184 | -47.26379 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4953a56-c28f-3e33-ba74-283e86910bd1 | -7.81241 | -63.56807 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d47b4aab-3576-3e57-9b8b-29ea439904dc | -6.27516 | -52.82841 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d93a04a9-52ea-394b-ba2b-7b575e3f15e3 | -6.77362 | -44.31943 | 2025-08-23 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 574a8030-b76e-356f-a751-0f172216afdc | -8.44552 | -53.7784 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21c610f5-cddb-3196-8c6c-ce949a1819b1 | -5.74733 | -57.59249 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 33cf5d72-cf45-34a8-8ac6-8d217d609169 | -6.28285 | -52.82254 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8aa26b1d-fce9-348f-9e28-e72c3daee74f | -9.1888 | -59.63215 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bada345-f372-3f1b-ad0a-6ed01fd83761 | -7.56288 | -61.37944 | 2025-08-23 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ec45491-794a-3346-a1d5-bfc421ed2981 | -5.15063 | -44.93882 | 2025-08-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bcb578e-412c-32c3-9979-5244026e60c5 | -9.21119 | -59.63173 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ef73f3f6-9bd0-3d63-989c-ab706a973c93 | -7.8031 | -63.55377 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f5e8ad80-0496-3314-9285-f5ed5c551bc1 | -7.3044 | -43.67318 | 2025-08-23 04:51:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 73fc85db-a6e1-3d73-8ff8-9433b0799ff9 | -6.15919 | -45.03451 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a947379-2276-3707-915e-aae94f9bbb90 | -7.54978 | -63.85264 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 64507a56-f32f-31a8-a46a-0b93e0d2654b | -9.18298 | -59.63977 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc2be63f-5372-3b72-9313-d8680ddc61ca | -6.65278 | -58.81985 | 2025-08-23 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f5fea8d-0c27-36d9-9dc2-e3d02c1a051e | -7.61703 | -46.26206 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecb64952-fba5-36e8-bc84-501cd43ea47b | -6.76842 | -44.31927 | 2025-08-23 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c111747a-5c9a-3f4b-b095-5358b8d54676 | -9.19606 | -59.64159 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71f43499-b17f-397e-895c-194b69b90bc2 | -6.77055 | -44.32231 | 2025-08-23 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84765087-9b50-3804-a93a-823bb323e71c | -6.25761 | -53.67221 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce5092b2-2b55-3300-9ccb-fc02d9bd9b06 | -5.75475 | -57.59729 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2c03a41-1201-3e79-af26-0cdee900eeb3 | -7.29817 | -59.62539 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2473956f-f930-332c-b96f-bc35f808e394 | -5.87993 | -53.6302 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d255ac5-bfc5-37d0-9955-0f062f8ff060 | -9.20181 | -59.46852 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d389641f-3863-3739-a4d9-55f80b5acb7b | -10.75379 | -48.24447 | 2025-08-23 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76f91f23-7f1c-3534-ae80-bd2f51ae3984 | -9.19893 | -59.4596 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4a20d622-2b78-35ef-872f-6ad821648934 | -11.05525 | -44.59749 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 808813ae-9dec-3d76-b56b-d03fc179746a | -7.29741 | -59.62987 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 446a6695-ddbf-3c66-95f5-a77d258b2d18 | -5.49001 | -42.15955 | 2025-08-23 04:51:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e8420b09-3963-3211-91be-3f9f0bda808f | -7.02673 | -44.64173 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bfd89613-58e0-3350-8138-3559d52d942d | -7.62418 | -63.48737 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74ab528f-a97a-386c-bc26-11d8d2147eaa | -7.60602 | -44.37445 | 2025-08-23 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 256f139a-c1c5-3710-b689-82876d64b7cc | -6.37554 | -45.5392 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |


[Clique aqui para ver as próximas entradas](README42.md)
