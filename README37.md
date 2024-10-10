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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a350aae-809b-39d2-abd7-4200a88e66f8 | -2.6532 | -53.3708 | 2024-10-10 02:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 1d068b38-a123-3f3f-8bdb-47dd11c6fa2f | -4.0814 | -51.0292 | 2024-10-10 02:45:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| b8b19bea-22ee-3a17-85d9-70b78d44d9c7 | -4.0961 | -48.2739 | 2024-10-10 02:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 158.9 |
| 13d6fcbb-56e3-3ff6-b95d-4646d5e73868 | -4.0962 | -48.2523 | 2024-10-10 02:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 570fe7f7-4e80-306d-b4e1-8044181d7758 | -4.1146 | -48.2731 | 2024-10-10 02:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 191.2 |
| ef652122-dfdf-3462-9b05-8bd694d7db8b | -4.1148 | -48.2515 | 2024-10-10 02:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 87994fe6-6df9-38da-ad81-f6ae4a9c3c6d | -6.5218 | -60.0649 | 2024-10-10 02:45:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 0b8bd6ee-c4d9-3402-99fc-c3031835891d | -6.7654 | -59.3252 | 2024-10-10 02:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| d8b8a17d-c469-3bdb-beb8-776a06dbaa59 | -6.7655 | -59.3059 | 2024-10-10 02:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| d3b77418-f325-38fe-9eba-2e8a518c0eb3 | -6.7839 | -59.3245 | 2024-10-10 02:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 5767c729-4bbc-3b61-9e05-407136610f2f | -6.784 | -59.3052 | 2024-10-10 02:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 91b0ea4d-2720-3600-880a-b5190883c344 | -9.027 | -61.6244 | 2024-10-10 02:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 95680f62-e9e9-3732-893e-da20b354a13a | -9.0271 | -61.6053 | 2024-10-10 02:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 53fb33d8-c95d-3974-997e-0df39b218f9b | -9.0656 | -61.3934 | 2024-10-10 02:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| d4d1e343-e7f0-3558-adad-4d37279c8823 | -9.0841 | -61.4117 | 2024-10-10 02:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 14884a44-d243-36e6-978b-161066cae1fb | -9.0842 | -61.3925 | 2024-10-10 02:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 4fc852a3-af80-334d-a435-0892cc474e8e | -9.1035 | -61.2769 | 2024-10-10 02:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 1565cf4b-ab29-34ff-b0cb-217f3748867e | -9.122 | -61.2951 | 2024-10-10 02:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 7000c845-637f-3c6f-8c37-95d36b83edca | -9.1221 | -61.276 | 2024-10-10 02:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 188.0 |
| 4748133e-18ac-3381-b03f-b0c1965251cd | -10.4287 | -60.9979 | 2024-10-10 02:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 52bd76bc-9339-3e5f-bd94-87128358d326 | -11.0254 | -57.2237 | 2024-10-10 02:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 123.4 |
| afd46329-8f12-33a1-9dd2-74c7e7812808 | -11.0256 | -57.2038 | 2024-10-10 02:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 765aa66c-a1f3-3be3-af9a-5c3cf55f31cb | -11.0441 | -57.2421 | 2024-10-10 02:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 18e2be76-7fde-31e8-a69a-d685600934c3 | -11.0443 | -57.2222 | 2024-10-10 02:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 156.8 |
| 024de01f-5ed5-330e-87ce-411174764afd | -11.0445 | -57.2023 | 2024-10-10 02:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 39df762b-914f-3f2d-8700-da7f39bdad06 | -11.2582 | -60.4079 | 2024-10-10 02:46:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| f3378f14-9cf7-31e7-8e03-b4fae3167f9c | -11.277 | -60.4067 | 2024-10-10 02:46:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 9c1c0d3a-0408-3367-a120-d60ffe1ac188 | -11.8188 | -58.8459 | 2024-10-10 02:46:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 968fc706-398d-36f5-b555-0586225c30da | -12.2893 | -43.7258 | 2024-10-10 02:46:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 4537581a-a06f-3d9e-a462-285b964878ff | -12.2888 | -43.7495 | 2024-10-10 02:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 9cd356e2-b3d4-3748-971f-ddd6a8995cf3 | -12.3065 | -59.1838 | 2024-10-10 02:46:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| a0b4280f-a8a2-3780-ade1-5fa599bb1d3a | -12.3067 | -59.1641 | 2024-10-10 02:46:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 979cac19-e1aa-3be5-b833-f1ed0f82b774 | -12.7056 | -63.0606 | 2024-10-10 02:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 6d137d1d-7823-3f51-9342-8a2bb052642c | -12.7058 | -63.0414 | 2024-10-10 02:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 17207da3-6dc1-35d2-8ba3-579d43cfc384 | -12.7247 | -63.0403 | 2024-10-10 02:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 6acee3d1-56b5-3ee5-a1ec-de4bb5fd15a1 | -12.9255 | -51.1361 | 2024-10-10 02:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| d6596b32-3647-32e7-9d17-5383f04d3f82 | -12.9447 | -51.1337 | 2024-10-10 02:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 246.0 |
| b786328c-f324-3d02-9258-c545b4746949 | -12.9451 | -51.1123 | 2024-10-10 02:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 14653a46-f8cd-3b43-8efc-9a25d4e75633 | -12.973 | -46.216 | 2024-10-10 02:46:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 14b95078-2894-3bcc-af26-f8d8dc1fefbc | -13.1845 | -51.7004 | 2024-10-10 02:46:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 95a75078-409f-3cfe-9e2a-0d35b5b11a7f | -13.7346 | -60.6079 | 2024-10-10 02:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 7a41fc23-e2ac-3e00-808e-649a904ea971 | -17.6668 | -56.3059 | 2024-10-10 02:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.5 |
| e2367153-4fc0-3f54-84f2-cbb25701049d | -2.6533 | -53.3506 | 2024-10-10 02:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| fc20523d-f988-3445-bb37-d0fbb9e0cbdb | -2.6716 | -53.3704 | 2024-10-10 02:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| c63954fb-1b38-3b97-ac02-33390a2cdb9b | -2.6716 | -53.3502 | 2024-10-10 02:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 339.7 |
| 56b8dd1e-2144-3f61-8238-9bac1cfdb4f8 | -2.6717 | -53.3299 | 2024-10-10 02:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| aa146a7f-465c-34ca-bd2d-d698402e524a | -2.69 | -53.3497 | 2024-10-10 02:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| b78c738f-017f-3f42-92cd-5f90216282d4 | -4.0961 | -48.2739 | 2024-10-10 02:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| b18abfc6-f075-3c1d-9d88-31e108e4f817 | -4.0962 | -48.2523 | 2024-10-10 02:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 2076712e-6e8b-3935-8dac-2acca5a7a9bd | -4.1146 | -48.2731 | 2024-10-10 02:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 224.2 |
| 14186d0e-e8b6-3301-9a53-fa60d6530415 | -4.1148 | -48.2515 | 2024-10-10 02:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| c19e3f0e-7549-3bbc-a2fe-ccefb5cb996e | -6.5218 | -60.0649 | 2024-10-10 02:55:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 64380cde-593a-3709-8679-74894ff7c86f | -6.747 | -59.3259 | 2024-10-10 02:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| bdbbafa2-70e8-3f3c-8264-1facf848c818 | -6.7654 | -59.3252 | 2024-10-10 02:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| e3a7835d-d87c-3c1b-a8cf-981637e25fb7 | -6.7655 | -59.3059 | 2024-10-10 02:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| d7769ba7-6940-3cba-aea6-d0e560cc21c8 | -6.7839 | -59.3245 | 2024-10-10 02:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 1307804e-9b28-3a8b-bd57-c84f65548c68 | -6.784 | -59.3052 | 2024-10-10 02:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 7e2cf858-ea36-391e-9881-4ebe5c311e5a | -8.1475 | -42.9717 | 2024-10-10 02:55:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.1 |
| 2f0e7a0a-6b48-3ada-98e0-ad27b6972cb0 | -8.1478 | -42.9481 | 2024-10-10 02:55:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.2 |
| f312b93a-bd71-3976-9c5c-ae9011c357ba | -9.027 | -61.6244 | 2024-10-10 02:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 7623f437-d457-36e5-b21a-137fbb8efb48 | -9.0656 | -61.3934 | 2024-10-10 02:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 16e8b838-9df4-3b74-a18b-99a6061debc0 | -9.0841 | -61.4117 | 2024-10-10 02:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 5394ccac-7e46-3e08-a2cb-5c447dd4b637 | -9.0842 | -61.3925 | 2024-10-10 02:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 22f6920b-0ca1-3993-bda7-bbfa76950903 | -9.1035 | -61.2769 | 2024-10-10 02:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 57168771-a410-35cd-8478-135d568bc2bd | -9.1223 | -61.2569 | 2024-10-10 02:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0d3641a3-3c77-3ca2-a6ea-6da24eb5a779 | -9.1407 | -61.2751 | 2024-10-10 02:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 34977eb2-011a-3edf-bf3d-2ccbc71edc69 | -9.122 | -61.2951 | 2024-10-10 02:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 086e2c05-3078-3773-96a3-923b70fbb68f | -9.1221 | -61.276 | 2024-10-10 02:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 191.6 |
| cd28e8fc-1d4b-3156-9a56-ed362fd7f620 | -11.0252 | -57.2436 | 2024-10-10 02:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| cfd4cf9b-832a-35d2-8268-2ca0b6629809 | -11.0254 | -57.2237 | 2024-10-10 02:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| c561c492-170c-30a2-a470-f32d8fce5136 | -11.0256 | -57.2038 | 2024-10-10 02:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 270e20be-3211-319e-b257-3c5fde72debe | -11.0443 | -57.2222 | 2024-10-10 02:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 9df5af2e-e099-3e2d-aac9-f4c9042cf843 | -11.0445 | -57.2023 | 2024-10-10 02:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 74aa0c95-55de-3291-a9d3-1bd793c86b0c | -12.3065 | -59.1838 | 2024-10-10 02:56:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 8b316fde-ff81-39aa-8b77-195a3b20d7b5 | -12.3067 | -59.1641 | 2024-10-10 02:56:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 2f43088a-8600-3846-bd7e-4a4e0edf5986 | -12.7056 | -63.0606 | 2024-10-10 02:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| aad7a7a6-f297-38e6-a286-4a702d4ded08 | -12.9447 | -51.1337 | 2024-10-10 02:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.6 |
| b2b450b6-64c3-3cd7-9673-378a59601eb3 | -12.9451 | -51.1123 | 2024-10-10 02:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 275b219f-14a1-334b-9133-5871f1c1fbe0 | -12.973 | -46.216 | 2024-10-10 02:56:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 3d9351dd-b782-31e0-9e29-6febd54b5ed1 | -13.1845 | -51.7004 | 2024-10-10 02:56:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 93a9803c-aafc-3a45-a76b-eccce7f99aaf | -7.12789 | -35.13101 | 2024-10-10 03:02:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 56a48c33-87ca-3fc9-b941-0c0d2a7d5715 | -7.12729 | -35.13441 | 2024-10-10 03:02:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| cd60da50-f3d5-3c1c-b747-1a0d3e7d9ef4 | -6.4521 | -38.84857 | 2024-10-10 03:02:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 19096abb-b8cc-3d15-8f51-3abd84b1890c | -6.44401 | -38.85404 | 2024-10-10 03:02:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f49f9757-5442-3a67-b40f-6196a9e06cc1 | -8.51037 | -35.06792 | 2024-10-10 03:04:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ce5d52c1-cabd-3e67-a259-9c0152a75eec | -8.50979 | -35.0711 | 2024-10-10 03:04:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 032f825b-5509-358c-ab0f-b75aefd6e6ec | -2.67 | -53.35 | 2024-10-10 03:05:13 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6983500-b87c-3af2-ab12-12cb0ff4a22c | -2.6533 | -53.3506 | 2024-10-10 03:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 8b6bd24c-ddbc-3089-ad2c-2847b3b1a11d | -2.6716 | -53.3704 | 2024-10-10 03:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 698f4845-b7c4-3fd3-bf4b-b76ff5c9f322 | -2.6716 | -53.3502 | 2024-10-10 03:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 310.1 |
| fbab7c50-c1b8-3c2c-9c3e-2284a5dcdcf6 | -2.6717 | -53.3299 | 2024-10-10 03:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 83019442-109b-3f94-87d0-a36accced4d3 | -2.69 | -53.3497 | 2024-10-10 03:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| ad20713f-b7f0-363d-b623-b53144cccc45 | -4.0961 | -48.2739 | 2024-10-10 03:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 2d706718-ed05-3cb6-bddd-52e4d08b480a | -4.0962 | -48.2523 | 2024-10-10 03:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| accf1da8-0743-38e6-a322-e3bd552ee9d3 | -4.1146 | -48.2731 | 2024-10-10 03:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 223.1 |
| e6b6ce75-c39c-3a5d-97e1-f2c9c2539677 | -4.1148 | -48.2515 | 2024-10-10 03:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| bd9ffc86-75f7-3bdd-8467-217c17d804ba | -6.7654 | -59.3252 | 2024-10-10 03:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| f4060404-be23-38a3-babb-19c6330611b5 | -6.7655 | -59.3059 | 2024-10-10 03:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 848c6adf-9a22-3ff5-8b2d-f9a91d62e83e | -6.7839 | -59.3245 | 2024-10-10 03:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 09993fba-8ae1-3839-b797-09559bf86d30 | -6.784 | -59.3052 | 2024-10-10 03:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |


[Clique aqui para ver as próximas entradas](README38.md)
