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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22b39b9d-d47b-3191-9130-b2bd1b4f1437 | -17.93631 | -48.91779 | 2025-07-01 05:16:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63b4c28d-aa92-3caa-8a90-7b28e7790a43 | -24.7426 | -53.8099 | 2025-07-01 05:18:00 | NPP-375D | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 461f27ee-25b9-3b3b-9b81-204fd3181fb2 | -24.74261 | -53.81047 | 2025-07-01 05:18:00 | NPP-375D | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3eb31032-c87d-31e2-8e8e-bcf78c19a046 | -6.2943 | -43.6891 | 2025-07-01 05:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 734683a1-6688-3596-bda9-2c1bec2ae644 | -6.2945 | -43.6659 | 2025-07-01 05:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 79be1baf-6005-3e75-8ff7-021b62d15c55 | -6.2945 | -43.6659 | 2025-07-01 05:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 1bdecd8e-2ed3-39eb-a4eb-0d6cf1937f05 | -6.2943 | -43.6891 | 2025-07-01 05:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 96420710-2911-3006-bafa-953d55690b99 | 2.75375 | -60.36633 | 2025-07-01 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b563d669-1808-303d-94ec-cedd574592d7 | 2.7504 | -60.36685 | 2025-07-01 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 835b74bd-77ec-31cd-9f29-6ad026b57ec9 | -6.54179 | -54.97516 | 2025-07-01 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef38b17a-be27-3093-8034-387aa7a42b80 | -6.54748 | -54.9727 | 2025-07-01 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8d5934b-ba85-3eea-8cb1-f7357abb3137 | -6.54269 | -54.96874 | 2025-07-01 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fe3386d-f130-3330-8942-f27a224c5d6c | -6.54224 | -54.97195 | 2025-07-01 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6153fa23-4f3a-3a82-819c-3af64ec6b81c | -9.28582 | -56.24564 | 2025-07-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47dbaa7f-55ad-3064-8b50-a52e1210c2f8 | -9.25204 | -58.75203 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4af2a75a-ee3f-335e-99d7-713351ba3916 | -12.6239 | -54.21176 | 2025-07-01 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3968e8c2-499e-3035-a893-05fa01cdbf44 | -11.1238 | -55.44731 | 2025-07-01 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85371872-df20-3c01-a106-f3e581adab40 | -9.11361 | -59.0547 | 2025-07-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52e6e042-0150-3496-aeb1-e76235f8b4ef | -9.23577 | -58.7457 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a9126af-0ac1-3afe-80d8-7ba055858134 | -13.00605 | -53.42294 | 2025-07-01 05:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e227112-b707-3aff-92c2-99313e1729dd | -12.62885 | -54.2213 | 2025-07-01 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a56cb145-9b79-3d40-8714-d1c105241eac | -9.70241 | -56.18184 | 2025-07-01 05:36:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 389817e2-debf-3ee2-b11d-4ba36d463b22 | -11.57791 | -54.57255 | 2025-07-01 05:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99bb8531-f352-38ae-ae2f-16080cfed059 | -10.12309 | -57.77457 | 2025-07-01 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a33e494a-336b-3285-adc9-2564f769058b | -9.39107 | -57.52269 | 2025-07-01 05:36:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98608079-ce68-3851-a9f2-eebaf07f08bc | -10.88045 | -56.45238 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17da96b1-3dda-39e3-81a8-20bbf7be3700 | -8.68948 | -63.77755 | 2025-07-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72b5a0a1-3076-3bd9-a0ed-79ead7a7b45c | -10.28184 | -52.83617 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa303421-18e5-362a-8659-68f89e0961f7 | -10.87807 | -53.7376 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9c5fe2cd-affc-3876-8dd9-f26f6a943894 | -11.57841 | -54.56853 | 2025-07-01 05:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a0b13be-2c9e-3c77-8529-3eb347ea850f | -11.83001 | -62.77229 | 2025-07-01 05:36:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 407042e8-8ed8-3d93-97d7-b11484d12913 | -8.67487 | -51.47213 | 2025-07-01 05:36:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f6ceefd-ac5a-3619-9626-d4a2c21aeec0 | -13.00662 | -53.41782 | 2025-07-01 05:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6be371c1-a5db-3f6f-a62f-f5c28aba5f45 | -12.63535 | -54.21761 | 2025-07-01 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7d24a986-0701-39df-8b46-437272b83dcc | -10.29816 | -57.12548 | 2025-07-01 05:36:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc8f4bec-e46e-3c31-a6b8-1c5bc17a3cc0 | -10.87659 | -56.44278 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 446cbfad-9329-3504-b4a7-cdc5173476c2 | -11.20149 | -55.91963 | 2025-07-01 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf376bb5-9d33-3045-97b5-d6ade6fa1a47 | -9.70202 | -56.18479 | 2025-07-01 05:36:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6fb01174-6320-3ac1-b7f0-57b5bc225901 | -9.17265 | -61.40376 | 2025-07-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6eead32d-7b67-3590-95dd-8c2f27054f86 | -10.87698 | -56.43983 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62025970-5126-312f-8ead-6c0332e625f5 | -9.23157 | -58.74508 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ed19a49-bba7-3af3-9199-97954f3a57e1 | -9.40024 | -63.26295 | 2025-07-01 05:36:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3356b79c-b4e9-318e-b364-17a84e5491c5 | -10.28571 | -52.83504 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7a94a35-ba8a-3376-a07e-23de2577d355 | -10.87502 | -56.45465 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19ad5737-3a26-3a9c-b925-35c61cc1a36f | -9.92647 | -59.93884 | 2025-07-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed07250f-4313-3c8b-9d8b-a982adbd0427 | -9.23998 | -58.74633 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0fbdda9-5fec-3c6a-b3f4-d1c5ac509396 | -9.24674 | -58.7592 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77c7749f-4401-3b1f-9b0f-dbbdaf0a9bf7 | -10.12778 | -52.34813 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 170285ae-975b-35e5-9394-5ba221ff5511 | -9.23212 | -58.74117 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5953fcb8-a6b2-3832-937a-e18ecb4e600d | -10.29747 | -57.13073 | 2025-07-01 05:36:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 149d1ff7-c37c-3777-af3a-1b10e92931cc | -12.62339 | -54.21614 | 2025-07-01 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 886f62a3-942d-3f2d-b120-648220a273ce | -11.12334 | -55.45086 | 2025-07-01 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4af01774-725e-36d6-ad1f-d828fc08c702 | -9.24564 | -58.76696 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd376e8e-765c-323b-ad71-07aa1d6ee715 | -9.242 | -58.76242 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d5b7d02-9c3f-3711-8120-0ae48afa3a41 | -10.88186 | -53.75663 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 735790e1-ab44-313c-9c37-9a070e0288c8 | -10.07494 | -52.74347 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 09c18d9f-4907-3313-b37f-068bbfc6fb39 | -9.24309 | -58.7547 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34401299-4798-3c3f-bffe-8aa385c67abc | -11.20674 | -55.92034 | 2025-07-01 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd5f7a3f-a741-3b2f-9ad8-bfbdfab43a42 | -11.57924 | -54.56713 | 2025-07-01 05:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04f96be3-8e1d-3339-8e78-64fece31f95f | -11.19625 | -55.91881 | 2025-07-01 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 58486f06-6421-3ede-a7e0-9b23f2241edb | -10.87619 | -56.44574 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 86f1ca78-df60-3c0e-ac66-ea700f9d8553 | -10.12713 | -52.3537 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 37ed3f78-7539-3935-a3ff-7fcec396eeea | -10.02074 | -54.323 | 2025-07-01 05:36:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bb9c217-e0a5-3fdc-99f7-60157ef5d0ad | -10.07787 | -52.75278 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1bf9a0b7-b9a9-3466-a07f-4c1713c943ee | -10.30294 | -57.12613 | 2025-07-01 05:36:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77d32f6e-a585-3f5b-99b5-ed6fa75ed70b | -8.68562 | -63.78053 | 2025-07-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fd9dbb2-7542-30a9-86da-77c098605d2e | -12.62936 | -54.21692 | 2025-07-01 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 234f435e-fd08-3e67-9e97-715c190621ce | -10.08763 | -52.7452 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5c766e8-edd5-343a-8652-97a9f87a739e | -9.23103 | -58.74897 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3624c05e-a2a3-386c-bcf4-6631a28f2423 | -9.24729 | -58.75532 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0a48a8a-71fa-3d20-add3-ee5dbb01d19d | -10.87462 | -56.45766 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8df1eb2d-635d-39e8-a01c-110ceab5b80a | -10.87146 | -53.74154 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a8ec4a6-c589-300b-9158-a1a9053c279c | -10.08008 | -52.75453 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32584790-69e5-3c5b-8f1a-a7adc075ebe0 | -9.23687 | -58.73789 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1b1dc9a-a2f6-364b-99db-a79cede816eb | -9.08546 | -59.47639 | 2025-07-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3da260e-41bb-3e40-8aa4-fa8cb9946748 | -9.71754 | -56.18401 | 2025-07-01 05:36:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdb1c5e1-a240-349f-9b51-63bc3ca9aa12 | -9.25039 | -58.76371 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f2b25e2-523b-3c74-a531-b28c33e27424 | -10.08613 | -52.73833 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2afef39f-06b4-3cd3-a91b-5d5b90811783 | -10.08549 | -52.74344 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f9a2693b-da3e-3f22-b52f-979599043784 | -10.07914 | -52.74261 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f65d8266-4aaf-3680-8fff-ecf5ab91de3c | -10.87116 | -56.445 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4bc4a41-0e13-3995-9ab3-25435f4bcf34 | -9.2862 | -56.24278 | 2025-07-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1838f58-16ef-3e37-ad73-2e0ec6de207b | -10.8676 | -53.77319 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 233d79c9-69ee-3d4e-bb11-618486a5fdfa | -9.25514 | -58.76043 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0628021-5570-3a1e-9182-c01333176a4b | -9.25149 | -58.75594 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae62df94-b70a-385b-a8fe-e4696850016f | -9.70666 | -56.1885 | 2025-07-01 05:36:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f9f40d6b-4141-31d3-8cc9-e21645f83f6a | -9.25569 | -58.75653 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e654935c-b089-34ec-b7dc-f1333521fc9d | -10.87541 | -56.45168 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f5bfd11-5495-3dd8-a8a4-07d8d4a6f21e | -9.08946 | -59.47697 | 2025-07-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4391bd6b-5e40-36f2-b43e-35722c169dbc | -10.86706 | -53.7776 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57be8d9e-f518-308b-ab24-35934da898d7 | -10.88163 | -56.44347 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b8f1e3a-68be-3fdb-89e4-ceb69671f2ab | -9.24839 | -58.74753 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0252d831-de34-3854-b589-e5753e903387 | -10.93348 | -55.32394 | 2025-07-01 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd78526d-1e55-3866-b1cf-224b31a44529 | -10.88123 | -56.44648 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| de5caa9c-e185-3c6c-91f8-5f3b4aebedb8 | -11.60294 | -65.14587 | 2025-07-01 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63160b85-f498-38fc-b2f6-50cf3b3604cf | -9.25094 | -58.75983 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b0facca-cb5a-3e04-a4d7-11b8670c544d | -9.24894 | -58.7436 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02455631-6fe6-39a7-adb1-257d448e7883 | -7.89359 | -61.47562 | 2025-07-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0376e5c9-197b-328f-9646-fc665c1c4629 | -10.88667 | -56.44415 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e266832b-9eb1-377e-aa56-96c8ade83bbf | -10.87203 | -53.73686 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README18.md)
