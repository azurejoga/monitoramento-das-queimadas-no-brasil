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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 133432a2-6cad-3832-8689-8e714819c7fe | -8.9874 | -65.4192 | 2025-08-26 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 8a575846-01b9-3475-b808-50406477c52e | -11.1587 | -44.7627 | 2025-08-26 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 462.9 |
| 83070fa9-7f97-3a11-b2b6-39f4d38819a5 | -8.8364 | -62.4321 | 2025-08-26 05:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f620deef-1542-3f1a-b558-8de96731308f | -11.1396 | -44.7654 | 2025-08-26 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 42e9247b-4d98-375c-8222-f6db62d4355d | -8.855 | -62.4313 | 2025-08-26 05:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 069b781f-9e16-392d-a04b-74e782d36b46 | -13.5715 | -48.196 | 2025-08-26 05:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 65306439-f4a8-39cf-b46e-f1d14a1e4075 | -9.006 | -65.4 | 2025-08-26 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 8f3b3e7f-54e9-34b4-89cd-219e6fd83f17 | -6.8229 | -58.956 | 2025-08-26 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 2e31d0a1-8a03-3976-a9ba-da77f1227e4d | -8.8734 | -62.4495 | 2025-08-26 05:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 214ae8c4-03e2-3593-a566-2254a1d58751 | -6.7819 | -59.6711 | 2025-08-26 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 3f2840b7-a702-30ed-af34-1e65c41ca51b | -8.8363 | -62.451 | 2025-08-26 05:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 96.4 |
| dc0afe2c-b6cd-306e-85c4-e9282546efa9 | -11.1583 | -44.7859 | 2025-08-26 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| bc058ff4-fa1c-3bdb-aec7-1ad932e2268c | -6.8228 | -58.9753 | 2025-08-26 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 73b96fc9-f307-3ed4-ab1e-789d12ee5581 | -7.3854 | -64.3475 | 2025-08-26 05:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2fa1dfa1-201b-33b7-9b9f-f8fa4ad9c030 | -6.7635 | -59.6718 | 2025-08-26 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 8f4bd5c5-5a22-3fff-87e9-5d733b9ad20a | -8.8548 | -62.4503 | 2025-08-26 05:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 164.5 |
| 3c8599e3-98c0-3aa7-b7ae-b4849150d084 | -11.1779 | -44.76 | 2025-08-26 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 7b31b968-e399-36ad-8976-6ae4d6c742f4 | -6.8413 | -58.9552 | 2025-08-26 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| e0da5f36-f276-3805-ae2e-29e0e7fc63b0 | -9.1715 | -59.5599 | 2025-08-26 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| a89affc7-2ef4-3cd3-bd9f-8e366e35e301 | -7.3854 | -64.3475 | 2025-08-26 05:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 382c40fa-db65-388c-8694-018eeea76d38 | -9.1903 | -59.5395 | 2025-08-26 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 57db32fa-3db3-3650-940e-ec7f526f0b2a | -11.1583 | -44.7859 | 2025-08-26 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| c464b575-140a-3921-a250-a2c48d67d5c7 | -8.855 | -62.4313 | 2025-08-26 05:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 67146b83-bc1f-3d3b-85a1-5317036c7de9 | -8.9874 | -65.4192 | 2025-08-26 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| f38f3874-4e60-3d71-9062-61d341cc72cf | -8.8734 | -62.4495 | 2025-08-26 05:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 9a5c0513-86c2-34a0-bed6-7e19ad314b57 | -11.1591 | -44.7395 | 2025-08-26 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 197.4 |
| 354bfbbc-4f99-3cd9-a6d3-6c57a27df3c1 | -11.1779 | -44.76 | 2025-08-26 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| b1c9ce21-6af3-3029-a2c4-41feee738943 | -11.1587 | -44.7627 | 2025-08-26 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 867.4 |
| a2ff7792-536f-3402-83a3-f731cd5ca3cf | -6.2459 | -60.0174 | 2025-08-26 05:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| b7af971f-fa02-3186-a0fa-acfca8070b5f | -9.1722 | -59.4629 | 2025-08-26 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 5a19e31c-15a4-37ba-ba48-28d00b9f8bdc | -9.1717 | -59.5405 | 2025-08-26 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| b03da385-bad9-38bd-8a82-87aa6215254c | -11.1396 | -44.7654 | 2025-08-26 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 6464d3ab-2bbe-3efe-a4a1-479de0faf41e | -6.7635 | -59.6718 | 2025-08-26 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 07f2accc-1c76-390f-a3f3-3216b5702624 | -9.1718 | -59.5211 | 2025-08-26 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 9fe4f452-a28b-360a-939e-0e7e353f3741 | -8.8548 | -62.4503 | 2025-08-26 05:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 162.1 |
| ce5d48dc-bc2f-3784-bf26-a9c32940ef7c | -11.6273 | -46.4126 | 2025-08-26 05:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 4784f871-38fa-3bb9-8bcb-8c59be509ac8 | -9.1904 | -59.5201 | 2025-08-26 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 59fcde8f-f5c6-3948-9be3-c739f30c94ef | -8.8364 | -62.4321 | 2025-08-26 05:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| ff5525c9-ffbd-3e41-97b8-5c744289184f | -4.9605 | -55.8226 | 2025-08-26 05:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 09c16bfc-708d-3f16-9cea-b36b01bbfa6b | -8.8363 | -62.451 | 2025-08-26 05:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 7b30d710-5150-3db2-b3b6-17bd34968162 | -2.93326 | -53.6924 | 2025-08-26 05:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d401f7f-5566-3c1e-a6db-60260736ffa3 | -2.93222 | -53.69939 | 2025-08-26 05:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3736776f-41fc-39fe-856e-784a33202a1f | -2.92731 | -53.69506 | 2025-08-26 05:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da241205-647b-391d-b461-80bfcaa5ff52 | -2.92679 | -53.69856 | 2025-08-26 05:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21421f89-d3c3-303c-bca2-2427ae420d7a | -2.92782 | -53.69157 | 2025-08-26 05:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e45d4658-3677-31c3-b575-8ef444851ec2 | -8.11226 | -62.876 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6541d58-c8cd-3ba0-846d-ad5ad47184a8 | -6.83937 | -58.96014 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4067f80-89e1-35f6-bfd5-5d772b84a5cc | -4.96258 | -55.81354 | 2025-08-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 2ab9a634-5c89-3793-bc40-55101b807867 | -6.94176 | -59.64746 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97fb98ef-8d84-317c-97bc-0834d2957800 | -7.39404 | -64.35525 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 879383bf-fb5a-3498-a62a-5c26e44b873c | -7.361 | -59.66327 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad9f0828-b623-3b0c-a3d8-75b254dcf1ca | -7.54228 | -63.84353 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d56222fc-bea1-325f-8827-93ce6ce5ae0f | -7.87757 | -63.0122 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7319c184-1705-310d-91e9-2755ab193d01 | -7.44348 | -63.163 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80be9887-da8b-3f29-b2cb-8fcb2573d8e7 | -7.81117 | -62.33728 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a99c3867-7e9c-3ed7-9439-143fa2bf50f8 | -7.54666 | -63.83711 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecfd3d9d-4fe9-3e5a-bd37-9003dfd93150 | -5.5328 | -60.21155 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e182a5a8-4447-3e24-b8c2-6aa522f5c7a2 | -7.47869 | -61.3485 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b4ca9e4-4c2f-3bac-9188-696958931aec | -8.11562 | -62.87652 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 745c4b77-1cfa-392a-a506-5308b2f6a8a4 | -6.35683 | -55.80328 | 2025-08-26 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5295823-a825-34cb-85fe-976291ad4541 | -6.25666 | -60.01421 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5b623d8-0155-323a-80ec-448073f643a3 | -6.31111 | -59.87803 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7aa19229-9564-3466-9adf-2330b1ece209 | -5.31752 | -60.19979 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73169866-0585-3ad4-ab3f-ecd9b208ecd4 | -8.56317 | -55.26083 | 2025-08-26 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5235b3a4-46cd-3658-9363-c78b840e041c | -7.38852 | -64.34729 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e2fcd5f-dc89-38bc-8ed7-197585a434af | -7.5605 | -63.85703 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d7079e9-1679-33f8-93f0-57fcc463874e | -7.38467 | -64.35023 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 046ea1fa-dacc-3f4f-9075-2fadeb3dbc3d | -6.25883 | -60.01683 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83bfe093-6c13-3410-98a0-9ac287f56c68 | -7.37973 | -64.36009 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4ad5991a-a7a3-3aed-b966-f7c3b54e70fd | -6.25203 | -60.01117 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37d472a6-73fc-30c1-9d99-0a0735f4e496 | -8.1128 | -62.87239 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fadc410c-ebc1-36a5-a935-5163619b3ca5 | -6.24522 | -60.00562 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c34a5663-f873-3a2e-95de-6571ded948e3 | -5.44386 | -60.156 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1903b482-58f1-3176-8b72-4d34301954da | -6.94689 | -60.08181 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d04f4f0-5071-3a5a-8cd3-6116f3ff8832 | -5.4039 | -60.172 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ab7c684-587b-3640-a5c6-d83993e0d746 | -4.96182 | -55.81889 | 2025-08-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6383ec42-18cf-33b3-9c4a-78c8cf4e5832 | -6.26105 | -60.0103 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ce9f8fd-2f34-3d11-ba3c-9bf9d221f7a0 | -6.83885 | -58.96367 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2369c213-9ee9-3013-80be-05f2a3977f26 | -8.12052 | -61.46005 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72380909-ae51-3fe0-81f8-4367a112b892 | -6.25577 | -60.01174 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d76d21c-815c-34d2-883e-ac977087f78d | -5.45186 | -60.15278 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f0889fb-330b-32ac-937d-083efce24605 | -6.5766 | -60.06751 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c937ed11-0d97-3a35-a36a-012e29e69c85 | -5.42354 | -60.16616 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a65b7ce6-56f4-37f6-a9f1-1f204e940a39 | -8.12111 | -61.45603 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1821180-25ea-39bf-b560-812956bfe30a | -6.24148 | -60.00507 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4c1cff67-e3cf-3957-9a81-2b54c75ee67d | -6.78519 | -59.68029 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a5eb77ec-357d-38e4-b76f-8c2cad1a3d8f | -6.78204 | -59.67493 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 014d8360-d69d-3484-8606-5444fa9586b5 | -7.62503 | -61.04021 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6475fb20-df0c-37d9-aae5-c084748bb038 | -5.29857 | -60.20129 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce3947d0-8419-365b-b179-ba8868b0b023 | -7.65703 | -63.51955 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52aea9bb-caa1-3663-bf03-92e4cb857f74 | -5.53044 | -60.20235 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac4a815b-6359-3729-ae79-dff09205824c | -6.23773 | -60.0045 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e805fcdd-8b18-3700-b952-a021e0930f5e | -6.7726 | -59.65883 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4e99d82-bc57-3251-a386-de01166c5064 | -6.70908 | -58.56846 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66f19ee7-7639-3e79-b788-133f32f907e3 | -6.57703 | -59.88566 | 2025-08-26 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee33d9fd-1f77-37a3-99e7-1e45cfac917f | -7.62384 | -61.0367 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 263bd2e8-3298-32b4-a3da-68e98aa71c09 | -6.25271 | -60.00672 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14f3ea80-7752-3733-a69a-75a6ba36cc2c | -7.47634 | -61.33991 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8e6628ff-f550-354e-a224-8758798d0c61 | -6.23706 | -60.00899 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f047cd5f-be22-39c6-98cb-7cb5bdbf326f | -7.61899 | -61.04446 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README76.md)
