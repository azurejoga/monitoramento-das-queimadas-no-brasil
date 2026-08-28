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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c11552e0-93e7-31c5-8e5d-9dd9a5bdcf8f | -5.7616 | -57.5612 | 2026-08-28 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| add507c7-ab9d-3ebb-88c8-c33ef3fbec04 | -8.8031 | -70.8217 | 2026-08-28 18:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 28303e2e-30c7-36ce-bedb-c18516049061 | -6.2538 | -55.4109 | 2026-08-28 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f0c30a65-b967-31de-bff2-39aca660daf3 | -8.8184 | -49.6308 | 2026-08-28 18:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| cddc209e-38a3-3056-a03f-5f5490882667 | -6.2537 | -55.4308 | 2026-08-28 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 42e088ba-56af-3a44-a42a-11e2adb47e02 | -14.2402 | -51.7576 | 2026-08-28 18:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| dec484a8-71a6-33ad-b7d5-adf46402fa5b | -6.8386 | -59.4379 | 2026-08-28 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 89255fad-00cd-3ace-b7dc-11204b1388e2 | -6.605 | -55.4337 | 2026-08-28 18:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 2efaf96c-2e9f-30bc-8582-6730f0a43767 | -2.74 | -47.04 | 2026-08-28 18:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2181b21f-0563-3e83-87ee-753e1af1b6b0 | -2.71 | -47.04 | 2026-08-28 18:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bff423e-6f73-3f19-93b1-8c68a0272551 | -6.8019 | -59.4008 | 2026-08-28 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 04b2e216-9f84-37cd-a254-4b36896d07f3 | -11.2128 | -53.9976 | 2026-08-28 18:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| d0b190f3-fd6e-3330-a27e-b5c5aaf5bf66 | -8.8761 | -71.2607 | 2026-08-28 18:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 76ed5e4e-cb4e-391c-8b30-f4b4df2a7d90 | -6.5865 | -55.4346 | 2026-08-28 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 94296cca-a4c4-37ed-889f-aa15bde5b26e | -7.4735 | -61.3846 | 2026-08-28 18:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 7bf698e0-b08d-391e-9ebe-b70b54530f8e | -14.1838 | -52.8245 | 2026-08-28 18:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 2e4a8878-a241-3383-95b9-dfb5b17c9cab | -6.7698 | -55.6844 | 2026-08-28 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 3c731be1-f855-3ead-8aa6-50456dce9b89 | -8.0928 | -45.8354 | 2026-08-28 18:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 413a302b-fbbd-3d6a-81ef-890ea09e06da | -10.0596 | -46.9477 | 2026-08-28 18:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| d8f6f15e-c592-36b0-8243-44990d9192b7 | -15.6554 | -53.856 | 2026-08-28 18:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| cb422463-5d66-3b1d-9323-320d51753ab7 | -6.2027 | -57.7583 | 2026-08-28 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 45c9d1bc-f52f-30ea-9753-bd87f4d0657f | -3.2361 | -61.2359 | 2026-08-28 18:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| a779bf67-8ef7-326e-a983-22323fd8dac7 | -6.1984 | -55.4135 | 2026-08-28 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 39763295-41de-3e4e-8faf-7d73b7ced049 | -8.0737 | -45.8598 | 2026-08-28 18:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| a71b3aab-1dc9-3450-9710-98405a5785cc | -9.1713 | -49.9622 | 2026-08-28 18:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 399beb54-1a7f-3b1e-b410-46720a68c971 | -8.5781 | -54.797 | 2026-08-28 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 189.6 |
| 4bacb243-7bb7-32c3-b48e-231b586129ae | -11.697 | -54.5876 | 2026-08-28 18:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f3494d2b-2ff4-37fb-b6d6-21d671fbfb41 | -7.5852 | -61.2089 | 2026-08-28 18:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2f1e5208-5c5a-3b38-b00e-7f0f4823cb25 | -6.7279 | -59.4423 | 2026-08-28 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| ab10771f-df67-36d0-99e7-d2a60869cbdd | -10.9364 | -50.5545 | 2026-08-28 18:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| c775b0f4-8bd7-392a-9721-17bd2b66c0af | -9.1895 | -59.6364 | 2026-08-28 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| f66eb344-4897-3d7b-8605-d7b0e81f7446 | -9.7874 | -43.5742 | 2026-08-28 18:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f0194059-6a8c-3e5e-b68d-739920cf9c32 | -8.9511 | -70.7279 | 2026-08-28 18:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 86.7 |
| efc9a48a-a78b-307f-87b4-f79de09d7df1 | -9.1711 | -49.9835 | 2026-08-28 18:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 1d0a390c-faee-37e4-a800-525636f1b02b | -9.4331 | -51.6716 | 2026-08-28 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 1c28accc-7ef1-30ae-9be9-1b36f1e0ab02 | -6.8756 | -59.4171 | 2026-08-28 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 4b055694-6c98-3de8-9ff3-37c0bbfa7450 | -8.631 | -66.5473 | 2026-08-28 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 9cf05d51-acea-38bb-880f-7839a052d171 | -7.5478 | -61.3056 | 2026-08-28 18:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| e04ce0c9-a715-3976-88df-1411d752c6b5 | -10.3898 | -61.1925 | 2026-08-28 18:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 44f6a129-bdd4-31cc-ae0d-419f998272fe | -6.1841 | -57.7786 | 2026-08-28 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 8ef01b57-6f19-3208-a791-47dd13206ab5 | -15.6139 | -56.4103 | 2026-08-28 18:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 6fff775f-c78c-3bec-867d-e2e41f64e874 | -6.1657 | -57.7793 | 2026-08-28 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 193.8 |
| 9cf7567d-5886-37fc-9ed6-6c7f95e3854a | -11.843 | -47.2152 | 2026-08-28 18:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 5c0ae286-6756-3d3c-ab03-8fd87019464f | -9.1709 | -59.6374 | 2026-08-28 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 53197f79-4bdf-36cf-b97b-9198700ecc76 | -6.7832 | -59.4401 | 2026-08-28 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| e9c85ccb-62b6-3f80-944d-c1d7aae03675 | -8.87 | -66.8935 | 2026-08-28 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| b9b1a93e-e02c-302a-b671-ab74cfe7efd7 | -10.498 | -64.5193 | 2026-08-28 18:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 84.0 |
| cfa563ac-a52a-3209-b6d8-66d35dd0db6a | -15.1058 | -47.9983 | 2026-08-28 18:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8ddd9d6e-0a2d-3f53-960e-a22c5c249aae | -6.8957 | -43.6368 | 2026-08-28 18:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 46cad7c0-b632-372f-ac5d-8fb5069874f8 | -7.4734 | -61.4037 | 2026-08-28 18:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| dcf6a855-5eac-35de-a0a0-394e1ce4d756 | -8.6694 | -49.5369 | 2026-08-28 18:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 7d879378-cbad-3fe9-90e5-6181a707513e | -10.5166 | -64.5186 | 2026-08-28 18:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 3438313f-bb76-3634-885a-6fe59fc83ab2 | -4.3022 | -59.4634 | 2026-08-28 18:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 40a259b4-a26f-3203-9e23-1ed729bbb78d | -8.5779 | -54.8172 | 2026-08-28 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 40cf06b6-141f-321a-abcc-6999f43c59de | -8.87 | -66.9121 | 2026-08-28 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 1ee6299a-4a61-3e65-81b2-f052b96d22a5 | -8.776 | -50.0616 | 2026-08-28 18:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 2784bdb0-7a95-3f26-86ce-3c8fa049889d | -9.1525 | -49.9639 | 2026-08-28 18:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 172.0 |
| 6fcdce26-89af-317f-894c-49f982d3b068 | -9.4329 | -51.6926 | 2026-08-28 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 7c37fca1-351c-3332-b67e-44f365f4cf08 | -9.1978 | -61.0809 | 2026-08-28 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c19af539-b13c-3d44-b10c-f3c862e23782 | -5.9996 | -57.8249 | 2026-08-28 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 79f4239c-5a57-3353-a172-d267f5990d6e | -11.5984 | -65.1338 | 2026-08-28 18:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 810351de-a0e1-307f-8cae-9ad028c10732 | -4.3021 | -59.4826 | 2026-08-28 18:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 200266ab-d4d1-3462-8ce4-205f69e0fafa | -9.7878 | -43.5506 | 2026-08-28 18:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| d44758b1-e4b3-3b4d-bf78-60b204e75681 | -10.3897 | -61.2118 | 2026-08-28 18:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| eca9bad4-0d56-3c05-8dd2-264ef466d5b4 | -10.4981 | -64.5005 | 2026-08-28 18:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 87c6fcb4-0311-3cb6-be9a-882d89099d95 | -10.3391 | -49.9762 | 2026-08-28 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 65d95e50-f077-3573-bdb6-54ae26dc7552 | -6.8757 | -59.3978 | 2026-08-28 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 10a52862-c461-3eae-b495-002bb3f1dac0 | -8.6311 | -66.5287 | 2026-08-28 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| fc80c4c0-943b-30ab-b23f-7594bfadaae3 | -14.8817 | -52.6293 | 2026-08-28 18:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 227.5 |
| 1bedda5c-9423-315c-9313-ff88a5819093 | -9.9708 | -53.9419 | 2026-08-28 18:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 4818fa10-f2c7-33fa-8b99-7f4f3551ce5f | -5.7616 | -57.5612 | 2026-08-28 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| abba3b0c-6301-3b8c-aab1-26e28b6491f8 | -14.8814 | -52.6505 | 2026-08-28 18:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 355f05db-9a70-34e6-82a0-a1e7beda9ba0 | -10.0731 | -48.6868 | 2026-08-28 18:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 290ffbc4-1aa1-3c76-9098-5f02110811d3 | -11.7167 | -54.5244 | 2026-08-28 18:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 135.7 |
| b4f551f5-c50b-3280-b849-079922a31cbf | -6.8569 | -59.4564 | 2026-08-28 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 1c383601-2902-3273-8446-8d2825d5643c | -6.1473 | -57.78 | 2026-08-28 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 5070bc99-f252-3c29-b31f-3b0b8446ee5e | -14.8627 | -52.6106 | 2026-08-28 18:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 06b35aff-18d4-359b-bd37-dc03c3300d8e | -8.0739 | -45.8372 | 2026-08-28 18:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 092dc2c1-e992-3450-b476-2a76d2b8f0c0 | -11.006 | -49.6461 | 2026-08-28 18:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 8b41cc7c-3c7b-31ad-a07a-dbb44d052d0c | -5.9995 | -57.8444 | 2026-08-28 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| dd08683c-6f6a-3429-b245-4de0dc381d3c | -8.5971 | -54.7553 | 2026-08-28 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 553bf9ab-380d-3757-b485-13058c4d7663 | -9.4517 | -51.6909 | 2026-08-28 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 68e6fbbd-282c-3a05-86f4-e8c29350ab9a | -8.8184 | -49.6308 | 2026-08-28 18:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 4009913c-557f-318e-822f-a456cdd61fba | -15.5576 | -56.2938 | 2026-08-28 18:20:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| beac774f-e917-39f5-8e6d-98bf817feeab | -8.5975 | -54.715 | 2026-08-28 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 71c08de0-98a3-397b-af5e-ca7de885f4f0 | -6.82 | -59.4579 | 2026-08-28 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 48c664d1-9e8e-3dd6-bb31-7b352cb18e88 | -8.5977 | -54.6948 | 2026-08-28 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| d4b67264-4b9a-3479-bd6f-3284e75c0518 | -6.2538 | -55.4109 | 2026-08-28 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 6de92735-3885-322a-8e2d-940a5021bc1e | -12.9244 | -59.8843 | 2026-08-28 18:20:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 1162c687-2d37-33a2-85d3-fa83e4597eac | -14.6024 | -53.1508 | 2026-08-28 18:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| ef12d38c-6f1b-310d-985f-9c9243752b6d | -9.1714 | -59.5793 | 2026-08-28 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 0c54faa6-dd3e-3445-b702-914782bf488b | -8.3785 | -70.8456 | 2026-08-28 18:20:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 83.1 |
| dec6f18c-1e3e-38cb-b1cd-e07b954e2d29 | -9.1976 | -61.1 | 2026-08-28 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 9880b8ef-c47e-381c-ad42-297671c29156 | -13.3254 | -46.9333 | 2026-08-28 18:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 1c61cc3c-6ceb-3338-ae0b-bc3d11b49c5e | -14.1645 | -52.8269 | 2026-08-28 18:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 570385e4-015d-35a4-950c-aa176185ef4f | -6.894 | -59.4164 | 2026-08-28 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| e7973cc9-44b7-3cde-b2f7-b422bd3f4c5e | -14.8821 | -52.608 | 2026-08-28 18:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 247.8 |
| 50352ac1-9403-3097-8061-ec9094b0408d | -6.7645 | -59.4794 | 2026-08-28 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 8163830c-aad4-3530-b788-fd0cfcbafa97 | -9.4705 | -51.6893 | 2026-08-28 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 1740beca-9806-3e60-bb80-2fb9cdc9ad25 | -8.5783 | -54.7768 | 2026-08-28 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 153.4 |


[Clique aqui para ver as próximas entradas](README159.md)
