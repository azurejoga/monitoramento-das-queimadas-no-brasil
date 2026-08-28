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

## Dados Diários - Página 171

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b79b8f8-10e9-36e7-8325-bd0733a51a41 | -12.9052 | -59.9053 | 2026-08-28 19:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| d6aacd82-177c-300e-abff-85ce4f36d885 | -8.6486 | -62.8565 | 2026-08-28 19:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| b583f8ee-f073-322f-affc-54668719d674 | -6.8941 | -59.3971 | 2026-08-28 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 76aa43e3-6880-39a8-8b58-9f9f49d4e2e5 | -8.0928 | -45.8354 | 2026-08-28 19:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 0b932df4-ac95-3d92-9c1d-c8b644746ffe | -9.1711 | -49.9835 | 2026-08-28 19:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| bbeeb2e1-5e00-3e85-86d8-e93b7391dcc6 | -6.7645 | -59.4794 | 2026-08-28 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| ca749606-1b98-3a48-994b-68ad3fcc4e4c | -6.857 | -59.4371 | 2026-08-28 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| e9a719d9-9d69-30df-9169-4b5f147d2d85 | -9.874 | -60.2762 | 2026-08-28 19:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1441af8a-e160-3e72-b705-4adef895b458 | -6.7647 | -59.4601 | 2026-08-28 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| ad375e6c-55c0-30d5-92aa-90f593630eeb | -6.8384 | -59.4571 | 2026-08-28 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| a01f3819-a47d-3399-ac56-b9beaed6cfd1 | -6.9521 | -58.9506 | 2026-08-28 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 3a43b578-1793-3831-8088-22645b9fdd74 | -14.1835 | -52.8456 | 2026-08-28 19:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 5203fa64-82af-39dd-8db8-1ffb5d418fe0 | -9.1525 | -49.9639 | 2026-08-28 19:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 0feca9f2-5d55-37af-a687-15ccc5dc8e8b | -8.5969 | -54.7755 | 2026-08-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 237.3 |
| dcef6cf5-5473-3622-b633-43390fdded81 | -14.8817 | -52.6293 | 2026-08-28 19:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 230.6 |
| 486330dc-7154-3f5d-92f9-f11b50b84ce6 | -6.5865 | -55.4346 | 2026-08-28 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 173.4 |
| b6f53082-c4bf-387d-b0d3-b854201387af | -6.8955 | -43.6601 | 2026-08-28 19:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 9cef548c-15ce-32f0-9a07-9bcaf46080a9 | -9.1713 | -49.9622 | 2026-08-28 19:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| d9e88ad2-5751-3ada-906b-bb1e062a336d | -14.9008 | -52.6479 | 2026-08-28 19:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 8d7324eb-fe73-30fa-87a4-45bdcfbaa0e0 | -9.1714 | -59.5793 | 2026-08-28 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 6d3e8714-1ff3-3652-b63b-1887f4de0da9 | -8.5971 | -54.7553 | 2026-08-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 176.7 |
| 298b81c4-3a4e-336c-9177-86d9401f0e0a | -14.3569 | -51.6995 | 2026-08-28 19:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 164.2 |
| d28e6b21-ef9c-3a3b-b3c8-0290fc8cf58b | -6.8957 | -43.6368 | 2026-08-28 19:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| adbe6aa6-e6ab-390d-88f4-9541c0d1b1b4 | -8.87 | -66.8935 | 2026-08-28 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 969c4b73-d636-3d6e-9cab-5444b118381f | -6.8569 | -59.4564 | 2026-08-28 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 7c71bd04-ccaa-37d3-8855-8ae8750b5c91 | -8.7757 | -50.083 | 2026-08-28 19:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 44771d0c-dea9-37e7-904c-52710ea5e6d0 | -7.4953 | -55.2862 | 2026-08-28 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| f259f41e-1b54-3604-925d-ae25bf1976d6 | -7.3663 | -55.1734 | 2026-08-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 355c128c-85c0-3cc9-bce5-e0ad118bb130 | -8.0551 | -45.839 | 2026-08-28 19:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 46c58788-6502-3ba7-8892-79c0affccab0 | -8.8576 | -71.3159 | 2026-08-28 19:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 03d8e6d9-7191-3bab-9d85-4b2da392885d | -6.1657 | -57.7793 | 2026-08-28 19:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 2672500c-a19a-303a-998e-7918ab654f79 | -4.1696 | -42.4346 | 2026-08-28 19:10:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 110.6 |
| 641fbc10-ffc0-3bb3-8f7d-848ea3c273b6 | -9.1978 | -61.0809 | 2026-08-28 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| d58fbff7-8a67-3983-b6c8-3bcbce801261 | -8.1432 | -64.0053 | 2026-08-28 19:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 266c2712-52c9-3438-9c66-c41e78e37826 | -4.3205 | -59.4821 | 2026-08-28 19:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| eea3bd21-aab4-3030-8f83-f3e796a39a8e | -9.4825 | -66.6347 | 2026-08-28 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d34d03b3-277e-30b1-b48f-ae5e2d0ff4ed | -8.5781 | -54.797 | 2026-08-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 452e6158-9393-3442-b2af-9d2e7fcb1ae0 | -6.7831 | -59.4594 | 2026-08-28 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 4874fcfe-c82e-3818-a0f9-54bf0fa6d93c | -6.7648 | -59.4408 | 2026-08-28 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 4748d94f-f6f3-35d0-b149-b5845192e785 | -14.8814 | -52.6505 | 2026-08-28 19:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 2619752d-e0ec-3cce-840d-3edcde54d89d | -7.3478 | -55.1744 | 2026-08-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| ef7b9a26-9bcd-39d3-bdb9-11c9cb25c093 | -9.02 | -57.5377 | 2026-08-28 19:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| d2f8ffee-5eab-3dce-800a-e505d035a0e8 | -8.0737 | -45.8598 | 2026-08-28 19:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 876099d0-6960-320d-a850-bbfd0bdae282 | -9.1895 | -59.6364 | 2026-08-28 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 8190f55f-a3fb-3e3c-acf1-f35abff2605c | -12.9054 | -59.8857 | 2026-08-28 19:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 3d194fb8-7439-3363-993d-bbc7f5ad7d1c | -12.0921 | -47.1812 | 2026-08-28 19:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 407753e3-c5e9-31c8-8ce0-fd9e3c53948e | -7.6031 | -61.3225 | 2026-08-28 19:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 0d28c66a-514b-3046-9b1e-e013fd068bd0 | -8.8576 | -71.2976 | 2026-08-28 19:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 9f78a81e-6b3b-3cd4-bf86-a82103a7385a | -9.0012 | -57.5585 | 2026-08-28 19:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 31a74b98-09dd-3b8e-a554-6f9a8f2223e2 | -8.0739 | -45.8372 | 2026-08-28 19:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| a7f620c8-c826-3cce-9c79-ff1a474f9342 | -9.8065 | -43.5717 | 2026-08-28 19:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 34a627a4-ebc4-30f7-ae12-fcd16ff1ee74 | -10.9377 | -46.6168 | 2026-08-28 19:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 178.4 |
| b350a5c8-8c64-3f99-b127-968f391aef09 | -10.3202 | -49.9782 | 2026-08-28 19:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 24af5ad4-1ec9-3994-9eb6-8c42c6999312 | -13.5991 | -45.772 | 2026-08-28 19:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| bbfbb95e-7ef0-38fe-91c8-ca30b64495c4 | -10.3205 | -49.9567 | 2026-08-28 19:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 723ff2ad-d1fb-3582-b006-df9f33a0c7d0 | -6.9336 | -58.9514 | 2026-08-28 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 167.0 |
| 4c40b479-75f7-3322-ac5b-43c3ff5222ea | -7.5478 | -61.3056 | 2026-08-28 19:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 202.7 |
| fc4bb4b6-e137-39b3-b00c-cab39512b89f | -7.80768 | -73.10345 | 2026-08-28 19:10:00 | NPP-375 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 23f1ccce-b54b-3003-a590-5629aad3c2ac | -7.29963 | -72.84634 | 2026-08-28 19:10:00 | NPP-375 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 78fad037-d857-3bde-8b31-f459b506a06e | -6.92226 | -69.99548 | 2026-08-28 19:10:00 | NPP-375 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| c6dcb4c5-8e20-3b3c-bc07-057911a26704 | -7.22609 | -72.43414 | 2026-08-28 19:10:00 | NPP-375 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 863d668c-92af-3920-80bf-4f93c4323202 | -7.15651 | -73.22025 | 2026-08-28 19:10:00 | NPP-375 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bcde6e9c-a6e8-3cd7-b878-f07a0f85fa2d | -7.66077 | -72.49538 | 2026-08-28 19:10:00 | NPP-375 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76f15ccc-3097-3f5f-8830-535f3074abae | -7.68348 | -72.43259 | 2026-08-28 19:10:00 | NPP-375 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 13f315f6-fc1a-3d87-b87b-55f0a76f9b0d | -7.34241 | -73.26987 | 2026-08-28 19:10:00 | NPP-375 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 28f3b2d1-c456-3ead-baa4-df5b7c02be02 | -7.58941 | -73.26735 | 2026-08-28 19:10:00 | NPP-375 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ce5ae8e8-d71b-3d2d-8a25-d3ab5fb58300 | -7.72256 | -73.08189 | 2026-08-28 19:10:00 | NPP-375 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 14.2 |
| c921136c-990c-311b-a831-c70ae3598ef7 | -7.73612 | -72.66616 | 2026-08-28 19:10:00 | NPP-375 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 076b6535-48cd-3b64-8f33-89a42422c8ad | -7.719 | -73.08509 | 2026-08-28 19:10:00 | NPP-375 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a3079a4b-e580-32d3-ad35-04a3ce7361f7 | -7.72427 | -73.08421 | 2026-08-28 19:10:00 | NPP-375 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5dbee98c-d91b-3708-9137-ee19d62392b8 | -6.92912 | -69.9926 | 2026-08-28 19:10:00 | NPP-375 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 62f75349-7947-3b3a-ada5-ad8949a17451 | -7.22762 | -73.1058 | 2026-08-28 19:10:00 | NPP-375 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| c40b4f74-3372-3ef5-9f85-30af4c35e74a | -7.23228 | -72.43686 | 2026-08-28 19:10:00 | NPP-375 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d6bb7421-3324-34cd-b673-4fb546e1ca65 | -7.64692 | -72.44997 | 2026-08-28 19:10:00 | NPP-375 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa1638e5-daa6-39e8-8152-6e065534f987 | -7.68745 | -73.30323 | 2026-08-28 19:10:00 | NPP-375 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 047d88aa-df35-3b2b-9c10-516100d05a27 | -7.71901 | -72.75767 | 2026-08-28 19:10:00 | NPP-375 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 285c86e1-0cc9-3c5f-b894-61ad42b4f4ad | -7.23164 | -72.43324 | 2026-08-28 19:10:00 | NPP-375 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d09f77ce-9ed1-31f5-9e0a-aad93b81b582 | -7.34438 | -72.9431 | 2026-08-28 19:10:00 | NPP-375 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 20.6 |
| faccf6b5-8841-3678-9a4e-5de021f4234a | -7.22673 | -72.43775 | 2026-08-28 19:10:00 | NPP-375 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 44c94789-4cd7-32ab-bd90-6c218d50d715 | -6.92328 | -70.00088 | 2026-08-28 19:10:00 | NPP-375 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 899f8c4f-fa94-3d34-b978-b21d4002f833 | -6.92363 | -69.99924 | 2026-08-28 19:10:00 | NPP-375 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ad5c5226-b12a-3c8e-b86c-1565f8b78871 | -7.54132 | -73.48267 | 2026-08-28 19:10:00 | NPP-375 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87292d39-2078-3c9f-bfc5-0945a8e6405e | -7.22704 | -73.10249 | 2026-08-28 19:10:00 | NPP-375 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 26c6e6e1-f69c-365a-8b0c-d6d61f6ae69a | -7.29902 | -72.84293 | 2026-08-28 19:10:00 | NPP-375 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 6b5136f3-d98f-3e98-a054-ddc65e1257e2 | -7.37209 | -73.25488 | 2026-08-28 19:10:00 | NPP-375 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b22f6332-b4e5-3cc0-83d6-b3d3911eb83e | -7.65885 | -72.48475 | 2026-08-28 19:10:00 | NPP-375 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 2519905d-ea15-3ab4-99e1-70be09c5046f | -7.85339 | -73.42429 | 2026-08-28 19:10:00 | NPP-375 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a408699f-1a3a-333e-9bd0-037465c88389 | -6.69991 | -70.33827 | 2026-08-28 19:10:00 | NPP-375 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e2806cfb-573d-3848-b9ef-7d28e6c82628 | -7.84827 | -73.42524 | 2026-08-28 19:10:00 | NPP-375 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e5489a9-521f-35d0-b7d3-1b653ab74ff6 | -6.92872 | -69.99424 | 2026-08-28 19:10:00 | NPP-375 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 75091862-19d1-3c01-b0e1-d44a26cfaa11 | -6.92124 | -69.99012 | 2026-08-28 19:10:00 | NPP-375 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 9b3b54a7-8924-3a0b-bed2-4100e3881722 | -7.5305 | -73.48136 | 2026-08-28 19:10:00 | NPP-375 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccfe3124-7f67-3c2a-8069-65e08161f1b0 | -7.7237 | -73.08098 | 2026-08-28 19:10:00 | NPP-375 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 295db6d8-f3c9-3a51-ac73-a9f0f61afa1c | -7.72602 | -72.70345 | 2026-08-28 19:10:00 | NPP-375 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d4b9ec0a-d4a5-3c26-bfa3-9577c2bccd09 | -6.92265 | -69.99385 | 2026-08-28 19:10:00 | NPP-375 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 74093e3f-c3e3-310c-8ad7-47a06c6d2830 | -7.34497 | -72.94646 | 2026-08-28 19:10:00 | NPP-375 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ff01d283-6661-344e-a21b-939d6e3d3744 | -7.72315 | -73.08512 | 2026-08-28 19:10:00 | NPP-375 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 45d5809d-91ea-3b59-a4f8-8dce84b53156 | -7.80824 | -73.10666 | 2026-08-28 19:10:00 | NPP-375 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d07e228c-c0bd-3067-8913-feec7c3652df | -7.68411 | -72.43616 | 2026-08-28 19:10:00 | NPP-375 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1f57dc9a-5623-3c69-9c17-ebf7b442efcd | -7.34184 | -73.2667 | 2026-08-28 19:10:00 | NPP-375 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 20.6 |


[Clique aqui para ver as próximas entradas](README172.md)
