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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99a2c466-ce4b-3ae4-a4b2-712bc9f34eb2 | -13.73142 | -54.7289 | 2025-09-30 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c287b2ce-2904-3801-a92e-99907297d9e6 | -12.44521 | -54.47315 | 2025-09-30 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fa21064-8796-3f38-b97d-b34f3f05acc7 | -13.20326 | -50.94288 | 2025-09-30 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81025abe-999e-3e96-a737-de0b63b2c6cd | -13.20392 | -50.93711 | 2025-09-30 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec0ddad3-d5e0-3b22-b3ba-c7519cdeb259 | -10.62664 | -53.69694 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1097241b-2cd2-3303-8b81-cccc1cc9121f | -11.14404 | -54.12676 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc8404e9-234d-38ac-81f3-1f1500e58a52 | -10.89339 | -53.74969 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3593b63a-a0be-3512-ac81-e28c412c75b3 | -11.30383 | -53.96278 | 2025-09-30 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 957b5f2d-760f-365f-93c9-0581d432c31d | -11.16594 | -54.12284 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a4950dd2-33b7-322e-b940-c02fe9a5bb79 | -11.1493 | -54.12746 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 9483f888-246d-3f24-a9ec-f7de721f62d1 | -14.68149 | -59.84722 | 2025-09-30 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3417dc83-5988-3776-a19a-96c545b28c20 | -11.39347 | -55.0873 | 2025-09-30 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecf97d77-fa6d-3580-916c-39fd57a0d4a4 | -13.22309 | -50.92973 | 2025-09-30 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0fd4f41d-ef84-3b78-b087-6518604480b2 | -10.63449 | -53.69979 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5910412c-db07-346f-b177-ec0e4bb113d2 | -7.00637 | -71.62351 | 2025-09-30 05:29:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c8b5380-9cb9-395e-9d16-f522e013312c | -14.80865 | -59.70768 | 2025-09-30 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37c0563e-cb25-3311-a9e1-e909e4734985 | -16.06115 | -51.03224 | 2025-09-30 05:29:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6579138-4cd9-3001-a503-9e27b76ed1b6 | -10.62706 | -53.69355 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00175109-1d08-31af-887c-2f02e3c99d3e | -10.88349 | -53.7416 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee5cba1f-f13c-3884-a4c3-74786eb71875 | -10.03153 | -52.10821 | 2025-09-30 05:29:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e39f4b0-af5d-397b-b9c4-f21610d1fe51 | -10.6436 | -53.69241 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76dd34ac-b037-35a2-9223-0d204ce8f0ab | -10.63739 | -53.69836 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b692594-9ef4-313a-bfe1-530126b3898e | -11.15457 | -54.12813 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 9fe096b3-a786-36c8-9402-4c38082494b6 | -13.22971 | -50.93048 | 2025-09-30 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03ff8724-1750-390f-9aac-4b448dcdeffd | -13.75234 | -54.7317 | 2025-09-30 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af10b6f9-4d1f-3dee-992d-a9c1b5c41262 | -11.41001 | -55.06489 | 2025-09-30 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b78584a8-a78a-34a2-bef1-378c9622a071 | -13.73102 | -54.73227 | 2025-09-30 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 91750a1b-90b3-338e-9938-6c8db581aeed | -11.13962 | -54.11945 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e842d36-6a7a-3580-9418-31ac46a44dad | -10.63581 | -53.68979 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 149b087d-118a-3d0b-987b-7a2389fc7938 | -11.15498 | -54.12488 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 1397e3e9-ed8b-3515-81e8-ffb161dba511 | -14.85222 | -54.76194 | 2025-09-30 05:29:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8797b360-8cad-3656-aa83-31aa80d2e779 | -10.663 | -53.71186 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8763b708-c092-31a9-895f-a89d977c775c | -11.14972 | -54.12422 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 5726ea5c-c1d9-30e3-bd65-f915269c00ae | -6.93666 | -71.50389 | 2025-09-30 05:29:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f2befa6-8238-3dbe-8572-535eeb5c4d73 | -9.70612 | -58.19741 | 2025-09-30 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70d9d79f-0dbc-3dca-a985-337339ee380b | -10.62956 | -53.69571 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36283307-16a2-3fa2-be2f-da4666af1a91 | -10.63823 | -53.6917 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 705351d3-61fe-3fc0-a7ed-562da3b7acf6 | -13.21584 | -50.93478 | 2025-09-30 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 912dc89b-e45f-36c8-ac3d-6c9289ed3c11 | -13.22907 | -50.9363 | 2025-09-30 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 385a0276-8d3c-3501-a307-cbfe8bac66e6 | -10.63537 | -53.6931 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e39b24d-bd93-3c50-a276-4c98e36fd2fc | -10.63864 | -53.68839 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb1a54c4-b63e-33d0-8979-3942d3fec75d | -10.63202 | -53.69765 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f09bf371-9531-34bd-a81a-c19548ffbc4c | -10.89471 | -53.73933 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b4affc5-5c0e-3e3a-85ba-d7c7abe3ccd3 | -13.73706 | -54.7262 | 2025-09-30 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c7d191e4-1294-3460-bb41-a48aafe17b0a | -10.62911 | -53.69909 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7728bf38-712f-3900-a851-530f4517294e | -7.00699 | -71.62004 | 2025-09-30 05:29:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb2f8f4e-eff3-31ef-8166-597a2c772839 | -10.188 | -52.55201 | 2025-09-30 05:29:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bc0893e-ebc1-32f2-87c2-0eb659039741 | -10.0854 | -50.21059 | 2025-09-30 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 1e3fba07-3121-3c8e-ac91-9cc86f1b8022 | -11.4296 | -55.04044 | 2025-09-30 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4db77eb4-60d1-3dce-ab50-7308112124b2 | -10.63493 | -53.69643 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1c2deae-85c7-3553-84c0-b05e7f47bb26 | -16.06734 | -51.03903 | 2025-09-30 05:29:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71e0c6cd-45a1-376f-aff6-89bae4e1524a | -15.2498 | -56.83535 | 2025-09-30 05:29:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 90043de5-5e0f-3760-847d-b6e3c89afd17 | -11.43457 | -55.04103 | 2025-09-30 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ce8d37a-9cfe-3971-af01-632ae15c9bb1 | -10.99917 | -57.05276 | 2025-09-30 05:29:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| edff062a-69e2-31cd-9f0f-9faa649ef494 | -13.73182 | -54.72554 | 2025-09-30 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a6a3212c-d5e6-3593-a30f-0bcb5e3dfd19 | -15.2559 | -56.83259 | 2025-09-30 05:29:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 464edb95-2f74-33d7-8804-6228538fa414 | -11.14889 | -54.1307 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a9d696ee-8213-3448-b29c-d15e0be25a1b | -9.91346 | -58.56234 | 2025-09-30 05:29:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 246862b6-ae65-379a-a7bb-d8fe7fb48bc8 | -11.16551 | -54.12619 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| eeb77311-eeb7-3944-8a26-95ef4191b2f3 | -13.20923 | -50.93401 | 2025-09-30 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 718b5478-4803-38e9-b54e-94fdc0a619a6 | -11.14529 | -54.11693 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f41b9bb-9e6e-3bdd-9ac7-e852120a94ab | -13.23327 | -61.1932 | 2025-09-30 05:29:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee0a2fee-0031-3d5e-9098-391f9c55949e | -13.23386 | -61.18927 | 2025-09-30 05:29:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a198c37e-1ac0-30a0-b6e6-3ea0faf8984e | -11.15013 | -54.12098 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8df5e469-f715-3e71-ab9b-eade8e73f359 | -10.07807 | -50.21558 | 2025-09-30 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 01dd826c-f6cb-3de6-99fa-dfe7eb2ec894 | -11.16025 | -54.1255 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 08b84f37-3f16-392d-92a8-15f1ebb80c84 | -11.15539 | -54.12163 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 70b8089a-87e0-379e-89a6-2a5574d93952 | -10.19326 | -52.55674 | 2025-09-30 05:29:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcf2f72e-4702-3591-81d1-41128050004e | -11.15983 | -54.12881 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 53703777-19fc-3eaf-bff8-4cb26a33e187 | -13.75756 | -54.73244 | 2025-09-30 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56ce3082-fe5f-3cde-9c56-9a84b465371b | -9.24096 | -57.6097 | 2025-09-30 05:29:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17472375-445d-317c-848a-2927a12e8e44 | -14.8131 | -59.70369 | 2025-09-30 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11223d5f-7a28-3552-bd83-3b8197a4eec2 | -9.24146 | -57.60614 | 2025-09-30 05:29:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b73a818-9352-36e0-9e93-64f3a79b182d | -11.16109 | -54.11893 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 0917a7c0-b570-393b-9b52-5a7b39b0ff1b | -12.39489 | -57.58256 | 2025-09-30 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cfed23d-f16f-39f8-a588-4affb796dfac | -10.63781 | -53.69503 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 099f774f-a7ac-3ddf-8377-e08691f6985e | -14.81373 | -59.69916 | 2025-09-30 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7f65c16-be7d-3baf-ad62-1a340089cacc | -10.63159 | -53.70103 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 002bbd3a-f52a-30ab-9c6a-94e638b7c5ea | -11.41114 | -55.06683 | 2025-09-30 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc8d35ab-745e-3320-8367-bb323bf77a11 | -12.39912 | -57.58316 | 2025-09-30 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64d3aac9-ac3f-3eed-9528-6d369b4052e0 | -11.15415 | -54.1314 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 722c0bf3-4e16-3e9e-8259-a043d4ac461f | -11.30426 | -53.95942 | 2025-09-30 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06910292-cc36-3b40-9b41-e53ce22e3aa5 | -9.34547 | -57.42914 | 2025-09-30 05:29:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6834c991-3c6c-35c5-9b74-955c25a8004f | -10.63244 | -53.69428 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 126a013a-a41a-3c0f-97b3-16e033b13257 | -10.88393 | -53.73809 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17aa15d7-eac7-3691-9452-ab65dc8b2736 | -11.33075 | -61.58059 | 2025-09-30 05:29:00 | NOAA-20 | MINISTRO ANDREAZZA | RONDÔNIA | Brasil | 1101203 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b50b523-f6d5-31c9-96b1-c3f82eee5df1 | -10.08473 | -50.21642 | 2025-09-30 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 612f59b5-473e-340d-b454-37ab10ab0994 | -13.73223 | -54.72218 | 2025-09-30 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 59bf0f2a-e6ae-36dc-a6c1-1e652a0b24a1 | -13.2086 | -50.93982 | 2025-09-30 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81ee4ec4-fabd-3b8c-a1af-2d1d866aefa9 | -15.25451 | -56.83525 | 2025-09-30 05:29:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| df2697c5-3997-329c-9685-833baa06f19d | -14.80481 | -59.70728 | 2025-09-30 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 255a14b5-ba5c-3ace-a706-9276b80f4932 | -11.41495 | -55.06562 | 2025-09-30 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9477a945-096c-3d7c-996e-5cf2a032e1fe | -12.44479 | -54.47641 | 2025-09-30 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c89aced-35d6-39d7-ac55-b3671e3c4062 | -11.1615 | -54.11571 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d2f3bff8-c15c-3d40-be7e-658d82bfeb31 | -11.16067 | -54.1222 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 70735983-f8f2-3b7e-b3e2-b7bec72c7c5b | -12.79515 | -56.96109 | 2025-09-30 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8c204f0-b38b-3079-acac-5ba2b0ce785b | -12.44543 | -54.47338 | 2025-09-30 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b05c841d-50e1-3e9f-ba15-56d421ce3141 | -13.73746 | -54.72282 | 2025-09-30 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0412a498-2473-3190-b71c-de860c2e58c2 | -14.85709 | -54.76614 | 2025-09-30 05:29:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38c16454-e631-3e7d-924d-1b5933148e4d | -10.1875 | -52.55598 | 2025-09-30 05:29:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README105.md)
