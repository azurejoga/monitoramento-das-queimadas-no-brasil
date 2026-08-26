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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54a22579-f05f-3669-835a-940c9402ba7a | -7.07035 | -59.22365 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 6e931aa4-a143-3606-8dc5-efcb6fb1345e | -6.64377 | -58.51562 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 119757fe-a718-38d8-9823-68ee3363f880 | -6.7472 | -56.33637 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7998ff55-1ad6-33b8-af76-9eb80ba5cb6c | -6.14345 | -59.92843 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c61f0ce9-72f2-3df4-bf6e-dfcc087edf7d | -7.07477 | -59.22434 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e05b1a60-48bf-34b1-9e15-f4405c51b06f | -6.26483 | -53.36962 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7e872fe-07f2-32f9-9d5f-bea93eda895c | -6.86255 | -56.5752 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ced1813-d586-3852-8482-8e7fa9b1c63f | -6.80455 | -59.68686 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9da016d-ca61-385b-8a31-77898f4e2a81 | -7.31912 | -64.69561 | 2026-08-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77980c89-8caf-3fcd-9d25-263a5ceb40e7 | -9.45216 | -60.53314 | 2026-08-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff567adf-0226-383e-a6cd-c8f72891a602 | -6.62944 | -58.48411 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b94a162a-9f7d-385c-b8a9-8d72714d32c6 | -6.16549 | -57.80206 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4c03ab47-a19d-3305-8a21-a6ac1a47f3b2 | -6.9684 | -59.08842 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de7cb519-5ed0-3b92-8ac1-08db5aabda3d | -6.95438 | -59.09085 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 860b3a33-7705-309f-b679-bfcb3a3f2719 | -6.02825 | -58.04345 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce57b70e-3429-3f8c-bbfd-08b4b7d21f73 | -9.29016 | -60.91328 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 965060c4-34b8-3bc8-9259-151e5be76d48 | -6.86915 | -59.40543 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17b81937-d229-3f3a-a00e-025c3d3de7c6 | -9.38941 | -60.57566 | 2026-08-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ceb8399f-1f38-3575-a4f2-643ad4b4192f | -6.17918 | -57.70575 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23e55cb7-11ac-3726-9ae5-38fee2498e52 | -7.7947 | -62.39318 | 2026-08-26 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11eb7c4a-d541-3e10-ba8a-fa4ac7423011 | -6.50712 | -55.22598 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a9389cc-6e62-3535-b383-18699f89f1be | -6.79506 | -59.60255 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40e826af-e54c-3b9a-918a-74bca15798a8 | -9.60929 | -55.11147 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| e4d1f41d-2a5a-3db7-844b-27f6ed447889 | -6.14662 | -59.92572 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 08b62a1e-5ea1-3c3f-ba5f-82a43965bcc9 | -7.20651 | -60.61718 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2e87dd4-e074-3816-b3e5-1618a89b314e | -6.14013 | -57.84431 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8ab8e31b-6c73-34bd-bccb-8445fa7596d1 | -6.9878 | -59.26604 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e788f48a-0d9c-3765-bb54-2f1a636e92f1 | -6.12804 | -57.82652 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3ea4e0fa-0cb4-3f29-a00f-5aa5c0f2e3cd | -7.11125 | -56.55886 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23c18fd1-f0b6-3751-b1dc-bb27fba00355 | -7.03749 | -59.23215 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e34d53da-872d-3767-bfd2-497d5862cec6 | -8.22346 | -55.00474 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f7a96bd-f899-3fd6-b5b2-7a6560761205 | -6.80483 | -59.59579 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a824632a-6bfb-3cea-ac86-ceb3fcffa2a0 | -9.09983 | -60.90931 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33dc38b2-166b-3f9d-aeaa-52efde61c28c | -7.38173 | -59.98876 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f1f72ce-e310-300b-a708-123df4564442 | -6.63199 | -58.4992 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f643ff95-6e61-3d8c-90d9-96f0557de96e | -6.63592 | -58.50468 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c756565c-3e2f-396a-aea4-abeb91f745b0 | -8.81416 | -62.33533 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 964408b2-61b8-35ff-b09c-4d1190dba524 | -9.67373 | -55.09889 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac73ef05-5884-323b-9e5c-b370d1462610 | -6.11768 | -57.83019 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 59a2a40b-8cd1-3342-97ce-b9dd8b5f8750 | -8.26128 | -63.99355 | 2026-08-26 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56db9f21-fb35-3a14-86c2-ee07863ffb23 | -6.7238 | -59.44219 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d815feaa-e22d-3066-b7f0-b8fa7a209055 | -7.47526 | -61.37073 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6729b1ae-d66c-3a4f-b7f0-9f7cf8cede1a | -6.14687 | -57.69909 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d4d974fe-f181-3ac0-a2cd-b42f405a9420 | -7.48236 | -55.27644 | 2026-08-26 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| abc62a0a-910d-38f6-ba1b-b1ba76fb4ae4 | -7.3804 | -55.15475 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0c9e6ae6-d74d-319b-8a1f-1b1d3dbe6024 | -8.57542 | -55.28236 | 2026-08-26 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c71e3385-c714-3e85-ba1c-03d0ee733c5e | -8.81184 | -62.31414 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d9a0e6ac-1110-37fb-918f-44b78491c403 | -7.55595 | -61.41235 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62c5fbe0-89db-397b-999d-3eb7ff9adb54 | -9.59536 | -60.52492 | 2026-08-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad25e23e-b6a3-3f55-a532-ff2bb5b4c862 | -6.77874 | -59.4407 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a251db15-2f73-3f04-a49a-5fcbd239d226 | -6.22928 | -55.61599 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b54548ae-54a8-3606-817e-8658096a442b | -6.6373 | -58.49512 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a99d039-d9d9-3cd5-8a02-7bfea01d0174 | -6.93934 | -62.88654 | 2026-08-26 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbb397b3-cafb-326b-9ec5-585bd427f8ed | -7.21109 | -60.61419 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d449effe-f099-3f7a-8759-3779b5778df8 | -8.82596 | -62.33256 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25d98c61-9c3a-3587-94e5-d45386c9e9cf | -9.16496 | -58.3317 | 2026-08-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 23d7333a-2fc9-3a18-a43e-5dc1a6d64fd9 | -6.22814 | -55.47441 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d310c26d-95c1-30b9-a668-aa2e57bf7aed | -7.8108 | -63.26271 | 2026-08-26 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 235349a8-747e-3c25-a096-2a4f29c42506 | -6.83143 | -59.94366 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed17d4f5-c733-370a-b6c2-654ce44b43e1 | -9.46002 | -60.53815 | 2026-08-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5933b58-516a-36be-b290-2260020c03ee | -7.21162 | -60.61063 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48bfbcb0-2b59-3760-b7a7-dc7879c1dc00 | -6.79472 | -59.81178 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29df1ae2-067b-3067-be83-cd1b5f1e5688 | -6.93609 | -58.94895 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d094228d-9ced-31ad-ab07-cc29a1e5c1a5 | -6.80053 | -59.59513 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dc909c2-a056-36ab-acbf-ad7cdce180be | -6.15079 | -59.92625 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f69b7564-5fc2-3161-8be6-be09cc6b1ce8 | -9.6024 | -55.1078 | 2026-08-26 05:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 7f983c5c-9b0b-3fae-af00-443b394cbcbc | -10.7596 | -54.0384 | 2026-08-26 05:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| f80796bb-7497-3510-b738-107472352455 | -13.3034 | -51.4517 | 2026-08-26 05:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 209.6 |
| d9ba8636-4598-3141-850d-bf81f4ce27b4 | -13.3226 | -51.4493 | 2026-08-26 05:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 761bdc51-ac15-3eac-a0e4-691d165146eb | -13.2842 | -51.4541 | 2026-08-26 05:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 4734f05b-a772-3a49-8b81-4b288b756f00 | -7.5104 | -61.3832 | 2026-08-26 05:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| ea3d6112-13d6-312f-802a-5b0702062fab | -12.6836 | -48.4116 | 2026-08-26 05:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 4e6a1354-6c33-3756-b709-d7c1438425d4 | -13.3031 | -51.4731 | 2026-08-26 05:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| dfdcca38-8cb3-30cc-a510-a9421030c3da | -6.641 | -58.4987 | 2026-08-26 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 954d649b-32df-3393-a10d-adf6603297ad | -12.0354 | -46.0374 | 2026-08-26 05:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| ca2fa561-8c70-33c8-9c29-11351c395eee | -6.2676 | -53.3768 | 2026-08-26 05:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 4d2111c7-9002-3a40-9358-c9d6c2c275bd | -7.5289 | -61.3825 | 2026-08-26 05:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 226122bd-f3d0-305a-85cb-3d38ea6cf6cf | -13.2448 | -51.5229 | 2026-08-26 05:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 41c8b5c8-53b3-3d3e-a88f-c3c0f8e64022 | -6.6409 | -58.5181 | 2026-08-26 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 838cdf38-0af7-36bd-ac73-5ac627564f48 | -7.5288 | -61.4015 | 2026-08-26 05:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| d4eb6e7b-b51a-3023-9d53-a8b53ea329e1 | -12.0546 | -46.0346 | 2026-08-26 05:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| a37adf8c-2ad7-3da5-a23f-40f2c9ab7d42 | -13.8627 | -54.06158 | 2026-08-26 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa2c9017-807b-3d27-afbc-25fe8cb833f1 | -13.86868 | -54.08938 | 2026-08-26 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6789d2f-8593-3988-b19e-3430fcafc44f | -10.0689 | -60.49957 | 2026-08-26 05:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9be04050-92db-306f-bbfc-e2c94088576c | -10.7539 | -54.01841 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0dab4902-40ba-3f6f-b172-66ffe0cc388a | -13.86085 | -54.03243 | 2026-08-26 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de201d9f-f879-3f3e-a2bd-75f2f63da149 | -13.85828 | -54.05719 | 2026-08-26 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76d0e7ba-e504-3ec0-a2bf-5e3efe8aadbd | -10.42481 | -61.22349 | 2026-08-26 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 409e2821-98f9-3f12-abbc-7d8e575816ac | -12.08248 | -64.24529 | 2026-08-26 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abf46ab7-cf08-36bc-a728-381a239269d4 | -10.77004 | -54.03879 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 602395f4-0c4b-3522-839d-d5c3d4163c5a | -10.7591 | -54.03057 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bf97b83f-bcab-3633-8042-12dfcc96d784 | -10.76478 | -54.02649 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9f3aab56-8a33-3a00-a6c9-f27ccd8bed81 | -10.77135 | -54.02737 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 01b3cd8b-409a-3611-85c9-96daeadbff38 | -10.42583 | -61.2162 | 2026-08-26 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2edf2dab-e29d-3005-ab64-b18d06be6ba3 | -10.76347 | -54.03799 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| db8bcf7b-04a7-3f14-9ab5-3bb5e7b216af | -13.8565 | -54.05536 | 2026-08-26 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ac650f0-31c9-3cbd-b0b2-1c3b5622259c | -10.65167 | -57.25122 | 2026-08-26 05:50:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 560da21c-9f29-3b66-a15d-5b824b23e137 | -10.98498 | -60.79189 | 2026-08-26 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42d527ff-6a12-3737-aa66-884d8c3e7bed | -10.76046 | -54.01936 | 2026-08-26 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2a910dde-8fe9-3301-977c-5b6b2de6e0f2 | -10.07869 | -58.54135 | 2026-08-26 05:50:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README73.md)
