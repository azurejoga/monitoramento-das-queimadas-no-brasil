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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3af099e8-a8c9-3728-9738-6dd84ba3b38c | -6.12547 | -57.69306 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1983d1d5-d873-3202-af6f-e06ef6083f49 | -7.58066 | -61.35658 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6593e3d-48f0-3b2d-90b8-908bea6cf52d | -7.72766 | -60.98119 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 869ba3d2-8f1c-3f40-81c3-5e3323ba21e1 | -7.29146 | -56.68673 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 711a94d8-07d8-3be9-a762-b5b922d4f696 | -7.73608 | -55.22163 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2187f965-b5b6-3edd-b95e-96e7b04afc3e | -6.16049 | -52.63482 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a16a863f-f04b-3d53-9d82-cdf72e1462c9 | -7.58664 | -61.34638 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03f10ae6-5144-39f3-b168-a7d209a09ade | -6.86584 | -59.46885 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8caf6057-9204-3620-b4f2-9a045cfdb99b | -5.88404 | -57.76645 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0edbd24b-bf6c-30ee-b81d-2ad93de77cc1 | -8.797 | -62.51352 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bba24c14-22f6-3ea9-bcc8-e5e2732fda5b | -7.63319 | -55.29629 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b1b8b73-3753-3ec8-ab4d-898759c0d6be | -3.90623 | -59.65413 | 2026-09-01 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecaa7d1a-ce3d-35ab-b7e7-0751aa081018 | -10.68875 | -46.25869 | 2026-09-01 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0c8ea34-e1cb-35af-8cdf-240670577ff0 | -7.53225 | -61.37476 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f655e57f-fc46-3d3a-86c1-6bdba89f340f | -7.03983 | -59.2282 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30155fac-9552-3ca8-a2ac-74b66af31b7f | -3.13317 | -61.18025 | 2026-09-01 05:16:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c21c6f11-781a-3ecd-a5a3-e781a83ef024 | -7.29423 | -56.69078 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c600d43-36c6-3dec-8d1f-a0db3090c652 | -2.91326 | -54.1184 | 2026-09-01 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b4dcd9b-dd39-3683-adec-07c22c4708ec | -9.13409 | -61.09591 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e021165-53f2-38f7-a68b-db84cb55daa0 | -10.7554 | -47.98838 | 2026-09-01 05:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c0bdacf-834c-3752-ac22-d13a15ed4b8c | -4.96151 | -55.84798 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4f02b0c-6ea5-3d3f-b5a7-525bb3522f43 | -6.18583 | -57.73343 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cfa277af-d310-3990-bad6-a557c4250052 | -6.3107 | -53.54562 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb0ac7d6-4322-30bd-bb25-0f62fc0add57 | -5.94774 | -57.69163 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aac837a9-5d1d-331f-b94a-5ae8e424571d | -9.46536 | -57.02225 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7500eb60-ac76-3e8c-b137-82e6ba2b1eba | -11.21511 | -46.09028 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc079e8b-7571-33d9-bb16-8c4073a03a71 | -5.95359 | -57.67732 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a00c178b-5747-3635-8cc9-750ebeea1f3a | -6.62253 | -53.17663 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7f8acc2-bb7b-39aa-a83b-f3694216d5cb | -5.94491 | -57.68736 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 150ca710-9d63-32ad-8f40-e543a71a6db2 | -10.75111 | -47.98041 | 2026-09-01 05:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19f5e758-0a92-3958-8e88-5a75ade62162 | -8.59056 | -54.77165 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 481bc206-0c28-3449-87d8-e41353d076b5 | -7.28243 | -48.12386 | 2026-09-01 05:16:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4385433-d4b2-3cae-b0be-8a754bbd60d6 | -7.34179 | -60.58018 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ffd50eb1-8d53-319c-ace9-5a5434bad6cb | -5.60259 | -44.00014 | 2026-09-01 05:16:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d558bf98-c375-37af-b1ae-675485492124 | -8.12854 | -54.96116 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1b2b39d5-4da7-3ec1-9d29-01d605720984 | -9.01987 | -57.53777 | 2026-09-01 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 416ae00c-b3fe-3e9f-bb8c-fd4d02512eb8 | -10.36268 | -50.00922 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 36e7a228-1724-350c-8847-a237e11300b4 | -11.00696 | -48.38499 | 2026-09-01 05:16:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6adb0947-e12e-3ebf-b422-8e4478c124fc | -6.75776 | -59.44385 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e01d5a0-88c5-3c71-b3b6-dd2f182fc2b4 | -9.17612 | -59.63607 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52228373-2c27-3512-8263-7a8062926493 | -7.32126 | -61.14626 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8c73871-8d07-34b1-abc3-7b1e8a10004f | -8.13809 | -54.96642 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dae74b4-827c-3dbf-b5a4-259d0f9227bc | -7.7325 | -60.9767 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 973807b3-dec3-3e46-a73a-93ee959b0150 | -6.11786 | -57.68115 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b865053-eb89-3a5e-8656-8adc1c82b9e5 | -6.93579 | -55.64585 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8cbf019-0245-3fe5-8f1b-56b9849c11b6 | -9.15129 | -60.94862 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bb60fa96-dcd5-3383-bb20-5dec6478ff4e | -3.62368 | -60.56232 | 2026-09-01 05:16:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59582527-7a2a-3198-a60b-d14eaf06fa53 | -6.82208 | -58.87644 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 47713283-e134-3be2-8d2e-0716ea1e0a40 | -7.68115 | -55.33999 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a87cb775-9b23-364f-a6fd-80441e52bb67 | -3.61057 | -59.07434 | 2026-09-01 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51b4943f-2d45-37f1-8a2b-13fbf09e0e0d | -6.94906 | -55.62656 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e606c7e-565e-3345-949a-637fb0d446b0 | -4.15037 | -60.69262 | 2026-09-01 05:16:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8927642d-7ebb-3cd4-bfd5-8f231cb33e16 | -9.15211 | -60.94374 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 03e54d73-4859-3332-b62b-14e8c75d1dc2 | -8.71469 | -52.36316 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04ad4f8c-9a9f-3fa2-9d4d-d331d780d152 | -6.59501 | -58.59388 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9e8d54c-d204-32a5-8329-70a116045036 | -8.79269 | -62.51272 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc6cefcf-fa62-32dc-9155-6718521fb89f | -7.45727 | -59.93446 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e3aaea7-951d-38d9-9d4f-75256adc19d7 | -7.33789 | -60.57948 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1d1e434f-0cb1-3113-82c0-78353fa82dd7 | -7.85884 | -61.14438 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7babc06b-7f24-3bee-b076-1fd4ff0a2c7e | -11.32079 | -45.17392 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3085aa5-af81-3bca-8816-aad7a2cb4d78 | -7.19623 | -60.68116 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d7efb00-123e-3ea1-8130-8e2a6b4ac920 | -7.5813 | -61.35295 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7f66e7e-aa44-3004-8754-4f9c9c025e33 | -8.13472 | -54.96587 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 26ef4f0e-87bd-34c0-990a-7ef16cd5e244 | -6.90863 | -59.48492 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da8eacb7-1eb8-33bf-9e9e-bc27916e0665 | -6.81177 | -59.09482 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7dcc2229-df33-3bd7-beff-9ecdbc04ed48 | -8.59282 | -54.75695 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f4f034e-d216-3a1f-a485-270ed97393e1 | -7.29972 | -60.56784 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab1ca1dc-1498-3f18-8225-de31b90db9a7 | -4.96041 | -55.8549 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e228911-7ba3-3214-86ef-e7543074de00 | -7.56333 | -61.36519 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca478745-8c05-3259-ad80-8864995a9ba0 | -6.80482 | -59.43377 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fd99069-90c9-30f7-acfa-2ed3ed24ab5b | -6.26288 | -53.64797 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ab54b7c-7b6c-30a4-a0a5-99d6af127e96 | -6.25006 | -55.42712 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e85ac54c-2385-3553-a314-2717699ea590 | -9.46958 | -51.57763 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d312e41-6db9-3c3a-8ed5-7e968263986e | -11.21021 | -46.08081 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5672bcfd-0a02-3274-a748-4f64e4242f97 | -6.11846 | -57.67744 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d5a01be-1670-357a-85d0-b2bf64ccb23e | -4.84944 | -55.83048 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39c7d4df-91e3-3c69-bcd7-5da13cd10fc0 | -5.94834 | -57.68793 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4380e18d-000a-35e1-9581-81ac03f48d13 | -9.17825 | -59.62354 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 117e2cc7-04c0-3c05-a437-f7b87b3cdbd2 | -6.84813 | -59.46149 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3db8531-0767-38a8-b2a4-df0e050a7bcc | -7.03396 | -59.21852 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6f05ef22-59c7-3c91-a08c-1f6fbed1e942 | -4.79579 | -55.97474 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 574f32e3-48cb-30e0-bf5d-4fb0dfeafee8 | -10.83817 | -50.70878 | 2026-09-01 05:16:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d597f27-eb69-3a49-8d22-b07fef333067 | -8.93909 | -62.37358 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8866b7fd-c4cd-3504-886d-5f5c35ede611 | -8.59509 | -54.71964 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d195834-0ac4-34ab-bc12-f6264ce1d2d2 | -6.97987 | -59.59369 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe7945f6-2da6-3960-941a-3be135bfbcd3 | -9.48144 | -57.02846 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38870f56-5660-38d8-b27b-174e9a3929f2 | -4.96538 | -55.84505 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fec81fca-9c37-300b-a7ab-69645092a5a1 | -5.25248 | -55.91162 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed245a58-3426-371a-afd8-70377afd2062 | -7.57292 | -60.46875 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7ce9e78c-c1c5-3e65-ad59-d3e447244e57 | -8.93981 | -62.36955 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12fa3fec-afbe-3864-ae08-8f6d19e671e2 | -6.69921 | -55.41216 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74583d8b-d576-35b2-83b0-9fb82eefa593 | -5.96088 | -57.69758 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07f80365-93db-3e33-9655-9c61cdbf710a | -3.12815 | -58.99978 | 2026-09-01 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f3bccad-e960-3dad-a39d-0a11c94e87b9 | -5.8846 | -52.07606 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec0e1464-25f2-3cf9-b059-34eadbd8f8df | -6.29373 | -53.5862 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4b71b12-fe3f-3634-912f-0d107a508fea | -10.34514 | -50.00203 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2ad226f-d3ce-32dc-a99d-a8b6bf486f9e | -11.00734 | -48.38205 | 2026-09-01 05:16:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c967552a-c054-399c-8da8-95fdade049e0 | -6.27856 | -53.33425 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5fef976-a0d8-3ff3-af92-00c3b7210601 | -5.24916 | -55.91109 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b25d67b-22c4-33ed-a224-25eb4f6a816b | -10.34906 | -50.00729 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |


[Clique aqui para ver as próximas entradas](README64.md)
