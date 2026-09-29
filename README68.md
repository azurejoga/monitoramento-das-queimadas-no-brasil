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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6267107-82cc-30c2-a20b-042fe41d1cdd | -10.3939 | -61.23331 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c6aff38-38f0-384c-97dc-8fd48b895760 | -10.38583 | -61.2571 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 2b3d8bdf-dfa5-374d-8070-fc5e2e48cdbc | -10.39499 | -61.26507 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0951ce4b-7078-39ce-8ec5-170510fc7ae4 | -9.93106 | -60.72401 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf660d91-9efb-3bf7-8f39-a1652b857a42 | -10.4013 | -61.25584 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff184487-9839-333e-bf4b-d4b7045c245b | -10.40244 | -61.24675 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b42beb4-b287-3308-8adb-096173855be2 | -10.3929 | -61.24239 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 110e9da8-e6b5-393d-8de4-1db025b74046 | -10.39314 | -61.23935 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| efce277e-0254-3301-ae5b-0542cc6f082a | -8.91545 | -64.15086 | 2026-09-29 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d997dae3-8505-3b74-9a22-c9c2105f57b7 | -8.03195 | -71.25674 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c49a8106-e994-3dff-90f2-b19b02a39d8e | -10.26845 | -67.33592 | 2026-09-29 05:55:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af48a360-24bd-33ff-a55a-1df8813b1d0e | -9.17008 | -61.40485 | 2026-09-29 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| cff004a4-d8d2-3163-9ba1-913c88dfe63c | -6.93145 | -71.77888 | 2026-09-29 05:55:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0493890b-6144-350b-8e70-3d2811fd93d0 | -10.39713 | -61.24905 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62f8ec16-69b3-3dc4-a5c6-f9e62aa5a260 | -8.02298 | -70.82929 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a2bcd5b-3faa-377c-8275-ef6eb9ffaaf8 | -10.3828 | -61.24137 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34a8af2b-6c6e-31ef-a2f7-846de7e0c3d3 | -9.19417 | -67.74363 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6751672-f60d-310a-a8f1-66ff6d17fa74 | -9.9232 | -60.71617 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8dafc96-9799-35fd-b6d4-3b55c862a039 | -10.38161 | -61.2504 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f545e59-c263-386e-b4ef-495af86d6759 | -10.38906 | -61.23275 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43db60d6-f6b1-3446-9a7d-107f500516cf | -10.38707 | -61.24778 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 3858ca7c-5cd1-3f04-ba15-1b9edcd8f1f5 | -10.39428 | -61.23027 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e6053d6-c816-3b60-a13a-4fe992c5f612 | -9.11302 | -67.85768 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99fc8e36-9c2e-39ad-85bb-0d38fecd5b6f | -7.18507 | -69.88713 | 2026-09-29 05:55:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e9a62a9-04d3-39f3-b97d-f005a5fe7bc3 | -10.38746 | -61.2448 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 8d2db6e5-36d4-3ba3-84dd-26b4da66a10e | -7.38133 | -72.47026 | 2026-09-29 05:55:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9c31b2b4-4107-30f6-b8a3-f7a6892d49c8 | -10.39587 | -61.25844 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 7efb0b71-2a25-3395-8ef9-0742ecc79603 | -6.97464 | -71.7608 | 2026-09-29 05:55:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86b528fa-c0f9-3d79-8ed9-c3c943486eb2 | -10.39891 | -61.23414 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c57f253-df8a-3214-b4d5-338587851c4b | -10.38866 | -61.2358 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 656874e0-579e-36ef-8bbd-2e4416f10c44 | -10.11007 | -68.02065 | 2026-09-29 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12928d0e-30df-3e95-af89-c38cfc4eb302 | -9.38265 | -67.69739 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe3b3261-77f2-3fbb-b20d-2c539324b550 | -7.07018 | -55.48087 | 2026-09-29 05:55:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 03b19366-829f-39f4-bb65-695289579265 | -8.03541 | -71.25728 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b88c052b-33b2-3598-a001-00b13191ab85 | -10.40088 | -61.25919 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2eade46f-f456-3f49-981c-e51bd5a31fc6 | -10.3978 | -61.24303 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 50fae8d8-02ef-3b0f-b446-01bba90ee4d7 | -9.161 | -67.67917 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35ae56d9-b1ca-3a85-95fb-bd38acdc6980 | -10.38667 | -61.25075 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 96322cc3-6dea-3cdd-b83a-85689387c4be | -9.92758 | -60.72323 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 95a18ac0-f53a-3e97-b4ed-078461d87e7b | -10.39277 | -61.24231 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1c824c5-efd7-3d32-b766-b07a1b8d2813 | -6.9753 | -71.75671 | 2026-09-29 05:55:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4850af4f-46e7-3125-88cf-bac47d4b5411 | -9.16833 | -67.67655 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fc0802d0-93eb-3f01-bee3-79f40446e437 | -8.84671 | -70.62839 | 2026-09-29 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22f1b33c-9ffa-3dba-a44b-56be2885c0d8 | -9.16168 | -68.24971 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf25d4c9-c49b-3961-8b83-0e4f0286a274 | -8.75842 | -70.82275 | 2026-09-29 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7451008d-dccd-3df7-b6fa-c1597f6fba0a | -9.1377 | -67.93504 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 056abace-29cc-3acf-8842-adeb36f847e4 | -10.3987 | -61.23728 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 91b9d449-ecb9-330a-98cd-45908ff0b6a6 | -10.38123 | -61.25325 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c238c6b-4785-33b3-be98-c6a2608b20bc | -9.99116 | -67.57288 | 2026-09-29 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ddfae33-7880-3c85-bc1a-f847054f677b | -7.06281 | -55.48046 | 2026-09-29 05:55:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a010283-696e-3fa3-8264-2d1290e66dd9 | -9.34167 | -68.78233 | 2026-09-29 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dad4bea6-37e7-314a-a152-9aedb67a3df2 | -8.8894 | -71.34287 | 2026-09-29 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bebf87c-ba25-33f4-acb1-545cc5308491 | -10.39631 | -61.2552 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ecaf12e7-7212-30fd-9dfa-78ea2ef32c56 | -7.98886 | -70.93406 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e180ceb-5843-3189-85c9-912e591d02fd | 0.90927 | -59.62837 | 2026-09-29 05:55:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b7beffd-6859-361e-afff-cbe716c500dd | -10.39667 | -61.25202 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 8126dcc9-21de-38b4-a5ae-ff6b8dff188c | -10.3895 | -61.26796 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e29e5ace-351a-3a77-aa6c-06271cd6679e | -10.38882 | -61.27402 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 119626fc-180d-3310-986f-e2385b27859b | -7.89466 | -70.90739 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58f859d1-9bc7-309b-9627-3ca4e7642dd6 | -10.39753 | -61.24604 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 480e4fcd-12dd-302d-9c03-9816271a379e | -9.12195 | -67.84428 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 174003fa-857b-3151-bda5-1b4b7fa134f9 | -8.78555 | -70.80468 | 2026-09-29 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e08fc11-ee92-3ae9-8e09-7fe274b5baba | -7.06973 | -55.48156 | 2026-09-29 05:55:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 770ac942-6390-3313-bec3-4e1844083c96 | -10.39816 | -61.24012 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21d47156-d6ce-30a6-8162-e50db7ae77de | -10.38958 | -61.26794 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d283963-b644-3dfc-a710-f2e20ee7d4fd | -8.84729 | -70.62479 | 2026-09-29 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ac082ba-1904-3022-9a17-217c9b064d90 | -10.40254 | -61.24681 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 418070ca-6f99-3535-8860-2a1ddd00a98e | -9.92672 | -60.717 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 63a8623e-1b8e-3e68-8433-c340cb9c0139 | -10.38786 | -61.24181 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4b552a7c-1170-3047-8a09-387b93113ac9 | -10.39705 | -61.24899 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 22e9056f-5965-3dbc-ad23-99224f6c1ae4 | -10.39422 | -61.27162 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3da8cf2c-d46b-33d4-afe1-b0062f520087 | -10.39352 | -61.23634 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78c03090-1d99-3fc2-9bcc-6aeb0b0a700d | -6.67498 | -55.11118 | 2026-09-29 05:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4cfea220-962c-3cd7-a3b1-e88d1bf153d4 | -10.42988 | -69.76658 | 2026-09-29 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dba93362-4e3d-3a30-bfa3-f023f24307d9 | -9.16971 | -67.67632 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 93d38c0a-1aa5-3c06-afc4-354be172e8c7 | -10.38004 | -61.26227 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df8ec10f-3194-318e-a61c-5c371bfc84ff | -8.47263 | -70.87813 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c4ab3de-7bd1-3e9e-9008-9db862122311 | -9.16932 | -61.41052 | 2026-09-29 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6adbe5aa-9c12-33d2-932c-f14d41dc44fb | -7.79063 | -71.98713 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb0681cf-91ca-39b6-841c-a000335dd250 | -10.39587 | -61.25848 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3431d20-54ed-3a78-9fd6-88a1803632d3 | -10.38826 | -61.23882 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3d808817-30cf-34c7-b686-1e3badf32bc7 | -9.12532 | -67.8448 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8ffe127-18eb-3b4a-8806-f7bdba725a86 | -10.4017 | -61.25267 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e93525ba-4d33-3811-9181-d64bc080264e | -7.89125 | -70.90683 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4601f6ac-495d-3e7f-868d-0ca09edf8542 | -10.39628 | -61.25515 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 152.7 |
| d2459914-1368-30c5-93e2-0f6df4c7e7ee | -10.38199 | -61.24753 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b4ee746-fb79-395a-9dbf-991738385d74 | -10.62422 | -67.93012 | 2026-09-29 05:55:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a428e46f-67d8-326a-80a4-de3551312965 | -9.92798 | -60.72006 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1eaab58a-b8ae-366b-837b-48081ee526f4 | -10.39543 | -61.26178 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33213a9c-4fa0-3ba2-9473-d4f52c7c9808 | -8.83889 | -62.39278 | 2026-09-29 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44ccebda-7bd9-3e9d-856a-3ca78365fadb | -9.38385 | -67.69774 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb356de3-35e6-3011-960c-5b10136ff17c | -10.39743 | -61.24597 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 7cc4e21e-6f14-39dc-9a88-f40a127e9e2e | -9.93276 | -60.72393 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 123d5c6b-2855-3406-b520-6c057888b7b1 | -9.9319 | -60.71771 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d756d4a0-b5a6-3b95-a62b-b6a5d2a8d2b6 | -9.12439 | -67.94063 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 768224cc-9236-3799-8523-47742f7f67f7 | -10.39084 | -61.25787 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 38983220-6f39-3c27-839a-bf1377b7f82f | -10.39853 | -61.23717 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71517df7-452e-3c21-9f1b-3699edbfd86b | -9.16519 | -61.40426 | 2026-09-29 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| ca98d5dc-611b-3641-a996-4102906da5b9 | -10.38993 | -61.26474 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4120c69b-4093-31ca-ba95-c6716df7acfb | -10.39831 | -61.24021 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README69.md)
