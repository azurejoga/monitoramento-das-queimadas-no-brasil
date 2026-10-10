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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c96d279-3089-3bc1-bc0f-99a5a4767a85 | -9.3165 | -47.3851 | 2026-10-10 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 8f038cfb-f6f9-3f36-b8d1-611deee9c464 | -6.4566 | -55.5008 | 2026-10-10 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| c347ab44-a124-307a-aada-c33bb4eaa683 | -7.9084 | -54.7396 | 2026-10-10 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| c62fe6ec-65a9-36d4-9ef7-63a252f415b1 | -11.0745 | -44.1003 | 2026-10-10 00:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 00e38236-4976-377f-9944-dfb93557068a | -3.1285 | -54.1657 | 2026-10-10 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 08e9a19d-a21a-32a9-ba2f-22e02fa32c25 | -4.36 | -54.77 | 2026-10-10 00:15:00 | MSG-03 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 713a37cd-4625-36d5-892b-f79da6880b73 | -14.46 | -43.99 | 2026-10-10 00:15:00 | MSG-03 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f8150aaa-9710-3c14-bd7a-3612295be0f5 | -14.46 | -43.95 | 2026-10-10 00:15:00 | MSG-03 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 64e02487-f57d-38a8-8bab-33cd24a5b230 | -7.54 | -45.31 | 2026-10-10 00:15:00 | MSG-03 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a14c16c-347a-3665-ae56-3f8ebe3e7f25 | -11.08 | -44.13 | 2026-10-10 00:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca8f7a48-664d-3ce4-9595-65a84984853d | -3.9729 | -59.3564 | 2026-10-10 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c68396af-b919-31b4-8655-c4272bbc8415 | -3.2737 | -54.6826 | 2026-10-10 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| f66fd19c-47c5-307c-bd19-608c5ac2ee85 | -9.2784 | -47.4112 | 2026-10-10 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 83be00d0-98d4-3435-8b26-97074e4bbbce | -4.4506 | -47.9329 | 2026-10-10 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 6d299189-b2af-39cc-bbeb-9b1c9cfbb6bb | -3.3139 | -59.4089 | 2026-10-10 00:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 15bf944f-4a42-3c8a-8ebd-0311e24e49f6 | -3.8573 | -55.7992 | 2026-10-10 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 65750968-bd7c-3e20-8a65-23d5930f3c9a | -12.2158 | -57.0887 | 2026-10-10 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| d8857cca-b51b-349d-b477-e07ef8e7fabd | -7.0225 | -47.6829 | 2026-10-10 00:20:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 060ce814-2cf9-36f5-a714-c3accd32d615 | -12.3067 | -63.351 | 2026-10-10 00:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 103.5 |
| fcda4b12-edaa-3bb9-a879-b09ec31d6c8d | -3.8574 | -55.7794 | 2026-10-10 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ce09d10c-7ab3-3a2b-acdf-987ce6b74730 | -7.4975 | -55.0055 | 2026-10-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| ac65ce0e-6970-3b6c-ac15-586e78b91e29 | -2.9267 | -54.0702 | 2026-10-10 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e2419cae-6b67-363b-8caf-06925777263f | -14.4535 | -43.9359 | 2026-10-10 00:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 4d656ea5-605c-3b7c-9a8d-cc8788326f7f | -4.3582 | -54.75 | 2026-10-10 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ac088e52-402f-3c0f-b0d8-3989c45ae953 | -5.7059 | -49.05 | 2026-10-10 00:20:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| e0eafcd4-b219-37ca-a717-25df2388020b | -3.5807 | -51.5039 | 2026-10-10 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| d807a85d-3c30-397d-b9a1-9825e177ca45 | -4.4025 | -49.7774 | 2026-10-10 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 6a4739f9-40d4-3b80-9568-a0e9155a2a31 | -3.9912 | -59.356 | 2026-10-10 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| ef799602-fa3f-3155-bd30-0918ac526290 | -3.839 | -55.7997 | 2026-10-10 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 4f82cea7-3d9c-34b3-8a6c-60d6f72d6176 | -7.5347 | -45.3233 | 2026-10-10 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 8b9d7bbf-c403-3c8e-a1a7-3fbc1f0167f5 | -3.5307 | -54.7356 | 2026-10-10 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 80b67db0-171b-350a-b45e-1da084ceb1f4 | -12.859 | -44.1504 | 2026-10-10 00:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 9a3cbdcb-0ef0-33b3-be30-c3cde69d6f0e | -7.9086 | -54.7194 | 2026-10-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 552b5dc3-66a0-32bf-b641-c51189667ab2 | -6.4566 | -55.5008 | 2026-10-10 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| dcd5a85f-175a-3e87-8763-269eb8202dfd | -3.1114 | -53.7839 | 2026-10-10 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 23df87e9-c1d5-3247-a4a4-4e4b96baf0cd | -6.4411 | -55.0424 | 2026-10-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| e072d63b-4076-3df8-8214-ec0220a17879 | -12.2879 | -63.352 | 2026-10-10 00:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.3 |
| eb496e69-0ad6-3bb7-9be5-c89bb0239aea | -9.809 | -64.4526 | 2026-10-10 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 5a6daecb-d4d4-35e1-8c20-22b2564de2c1 | -7.4977 | -54.9854 | 2026-10-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 3bcdf896-ef1e-3bc2-8961-474ef0d47516 | -7.927 | -54.7384 | 2026-10-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 7b633430-497b-3d06-bc42-61f38b00d036 | -6.9318 | -59.2605 | 2026-10-10 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 29bcd40a-3b8e-3a17-97cb-64a013508c61 | -3.1284 | -54.1857 | 2026-10-10 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9aec386c-7637-3eff-aeb9-2b4abf9d1933 | -4.3767 | -54.7493 | 2026-10-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| d1b93cba-60b2-3287-b640-8e89c54fd358 | -5.7378 | -45.1307 | 2026-10-10 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 84ee7038-20c7-3ecc-9bd4-d67c283262e2 | -4.5929 | -55.7168 | 2026-10-10 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6fb0e9cd-adcb-3fff-99ca-63bf0a783b67 | -4.812 | -56.0849 | 2026-10-10 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 3034ff39-d02f-3b4a-a7c9-598d0ef85520 | -12.2156 | -57.1087 | 2026-10-10 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 0705e9fd-f4f4-3719-ba8c-cda1b80eb18c | -3.875 | -55.9764 | 2026-10-10 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 7846b76f-be77-333a-bfaf-f114d52a0c0d | -14.4726 | -43.956 | 2026-10-10 00:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 334.2 |
| 98220e54-af54-3c1f-92a7-c7e894c54e6a | -12.2154 | -57.1287 | 2026-10-10 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 4591b2f5-d79f-3a70-86d2-61b13cbf76ab | -2.618 | -59.9938 | 2026-10-10 00:20:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| fa1cc3aa-03b6-33b2-840a-a2c3a1c379f0 | -6.6145 | -59.9464 | 2026-10-10 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 684028ce-4403-33e5-870c-8af3cfc2cab7 | -7.2011 | -52.6272 | 2026-10-10 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 4badd879-e376-3013-af5a-6c3474f86a1b | -5.7565 | -45.1293 | 2026-10-10 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| b3f7580c-a824-3147-978d-687ffc4724e5 | -3.9911 | -59.3752 | 2026-10-10 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 1e9de017-1271-39d9-beac-a087d1110f62 | -6.633 | -59.9457 | 2026-10-10 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 8c665952-9a03-3f48-bf53-c4c6b63c3c3f | -4.3582 | -54.77 | 2026-10-10 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| a8919610-e199-3346-ab0e-7a535afb2a5e | -3.6048 | -54.5936 | 2026-10-10 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 9928df6a-056f-37f9-941e-1d0e069c7b91 | -3.7494 | -60.6014 | 2026-10-10 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 215.4 |
| 28f4303c-a0cb-3048-adb4-a356292edb05 | -12.2877 | -63.3711 | 2026-10-10 00:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 139.5 |
| da1a9fc6-921b-3688-ae2a-fbf51a542262 | -12.3064 | -63.3893 | 2026-10-10 00:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 88.7 |
| e769782c-0a35-3308-8ccc-bcb4582a496e | -3.1101 | -54.1661 | 2026-10-10 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 2f8152a1-35e8-394e-b1d9-c81e1536e65f | -7.5162 | -54.9844 | 2026-10-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 425c8fa6-3ef3-3b06-9438-9367769a4837 | -6.478 | -55.0606 | 2026-10-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 0808b250-eda4-3165-ba10-c2c0a9e27593 | -6.4903 | -62.8554 | 2026-10-10 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| f1cecb35-d298-399f-969a-ecbf50f3f019 | -3.2204 | -49.4205 | 2026-10-10 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 0da0a6df-073f-3515-a103-6b8c04a3202b | -14.453 | -43.9598 | 2026-10-10 00:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 270.3 |
| 331262a7-6a4a-3afc-b0f8-5a868dd23545 | -4.4344 | -47.5421 | 2026-10-10 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d7678c59-f6e9-3c36-9bee-6a3cbaed22f9 | -3.7311 | -60.6018 | 2026-10-10 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 04dfc8e6-6283-34c6-afa4-8a89e97e80f5 | -12.2152 | -57.1488 | 2026-10-10 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 9f6a55eb-1513-3eb3-8a2a-b0d8f1adce1a | -12.8585 | -44.174 | 2026-10-10 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 7ebb0957-2fa5-33ec-870e-3a026a562199 | -3.2736 | -54.7025 | 2026-10-10 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 30cd4c93-8f10-31b2-8089-a83e59311087 | -14.4731 | -43.9322 | 2026-10-10 00:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 8be17139-35d8-3f30-a123-db26b82ae718 | -7.5161 | -55.0044 | 2026-10-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 1ce2ea2f-b5a9-312f-99d3-970499bd3b23 | -3.5491 | -54.7351 | 2026-10-10 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 9dc6e706-0f97-3333-9a56-6b3cdda73297 | -3.2553 | -54.683 | 2026-10-10 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| bdbbd486-1779-33ff-979e-092752bbcfef | -1.6225 | -54.4348 | 2026-10-10 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 2cb3595a-6b1b-31ae-a409-f9b93763c25f | -7.5162 | -45.3024 | 2026-10-10 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| a0e8617a-82cf-3abf-ab15-fd45208fc927 | -3.6397 | -60.6226 | 2026-10-10 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 16e721ae-49df-3c24-bae2-f9cd35572404 | -7.9231 | -63.6935 | 2026-10-10 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 13fe32ce-5769-3e5d-8bcd-cd1f654cd438 | -13.386 | -43.8945 | 2026-10-10 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 750a6369-9cc6-3881-b20b-d8cba1454fe3 | -5.2303 | -50.6856 | 2026-10-10 00:20:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 7a409bc2-cac2-3f8d-80c9-025c5208bd8f | -1.6408 | -54.4345 | 2026-10-10 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 9e735139-58a1-39ff-9cf7-04e4f542581e | -3.8749 | -55.9961 | 2026-10-10 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 66201406-78d0-3a62-8141-4363ecc30cce | -7.9272 | -54.7182 | 2026-10-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 517e16df-6a6f-332a-b27a-9d1bf8eb44cc | -7.1825 | -52.6283 | 2026-10-10 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 53e5f7f7-e711-3326-8acd-5901bd4e58f9 | -3.7346 | -59.4577 | 2026-10-10 00:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 174f3a17-5db6-3bcd-92c6-4c2b165a1364 | -3.6907 | -47.815 | 2026-10-10 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 0c58bf9f-a884-3131-bcdb-9fccd46ef4f0 | -12.2343 | -57.1271 | 2026-10-10 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 49e390f5-d21f-36c2-8e85-05dacebc54a8 | -3.2203 | -49.4417 | 2026-10-10 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| fb05277b-f4f8-33a5-8746-c4b48b811f68 | -2.618 | -59.9747 | 2026-10-10 00:20:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| e471612b-6ba3-3805-9e90-2e784bdb45d8 | -7.0228 | -47.661 | 2026-10-10 00:20:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 50438f7b-bdda-3d0d-9fa1-75467d77ab79 | -3.5676 | -54.6946 | 2026-10-10 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 2b4c3cc0-02a7-32c8-9dcc-b1cb0ff91efb | -3.7495 | -60.5824 | 2026-10-10 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| e1957aaf-9704-3727-8e31-aac787498875 | -6.4595 | -55.0615 | 2026-10-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f6443e57-106d-3530-b5da-5db24be7fa11 | -3.8391 | -55.7799 | 2026-10-10 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| cab64edb-3578-3e35-9cd6-e1dcba518d57 | -3.3138 | -59.4281 | 2026-10-10 00:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| ad337cf9-2ca4-3cc1-8ac8-278b4cef5d2e | -3.0375 | -53.8865 | 2026-10-10 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 1e9d8b7e-ae5f-3c2a-beef-2c34050626b0 | -12.2876 | -63.3903 | 2026-10-10 00:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 6db1e65c-b581-39ed-a1cd-f59fa31cb427 | -3.1285 | -54.1657 | 2026-10-10 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |


[Clique aqui para ver as próximas entradas](README11.md)
