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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f19d347-bb94-3cac-b165-4eae07366d18 | -3.74271 | -50.76139 | 2025-12-10 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 087829cb-9c1f-37c3-af13-35b25e21208d | -2.65174 | -54.84594 | 2025-12-10 04:57:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bfe0e8b1-83bb-3b6c-a8fe-9550393a6344 | -3.41977 | -52.65139 | 2025-12-10 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9992b1c1-1fb8-36bd-b6cd-1a62006d9fa2 | -2.48912 | -47.77755 | 2025-12-10 04:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a1c554c5-3f81-3441-8057-1dc3ce80150f | -3.01841 | -52.3948 | 2025-12-10 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 187145cf-a015-39c7-a42a-be6c9f94a398 | -2.78737 | -54.41893 | 2025-12-10 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24c410bd-25be-3cea-9559-aa99207147ef | -8.66834 | -44.2224 | 2025-12-10 04:57:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df35a9ec-b3eb-3cc3-b752-a8c21e8898a0 | -3.68743 | -43.81971 | 2025-12-10 04:57:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16e72cbb-61ff-3c81-8585-2dd7f83ccf48 | -2.07165 | -49.0066 | 2025-12-10 04:57:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 41d0ec9c-0b2f-32da-bdb8-9f771bfb51c7 | -2.88287 | -45.24155 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 47e35881-321e-3e52-91ad-a51781181997 | -1.87781 | -54.68876 | 2025-12-10 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d4cf4c5-d376-3cc5-b296-75ae1d924f0d | -2.43978 | -45.60241 | 2025-12-10 04:57:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f922c68-fe44-37cb-bc50-46a55e39fab3 | -1.67078 | -54.58001 | 2025-12-10 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f2293ea-a53b-3b91-98f0-59a592a041dc | -3.42419 | -41.66202 | 2025-12-10 04:57:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 87d40b82-f87a-3f11-b880-d6a080429f07 | -3.68798 | -43.81596 | 2025-12-10 04:57:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15371bb8-9655-3967-8423-a9666aa3c33c | -2.42044 | -48.26928 | 2025-12-10 04:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e7cd07b-4fe4-3b69-9feb-afaf46028993 | -1.41377 | -54.29575 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 498679ed-5f8a-3feb-93f9-cf90b115dc1c | -2.26474 | -53.70843 | 2025-12-10 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6555b90-7b6f-37c0-bfd5-763c08a70c2c | -1.41821 | -54.28934 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da9939aa-9718-3a37-a2fe-bd249c3effd4 | -1.87838 | -54.68519 | 2025-12-10 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42ab7838-2a61-360c-b58b-975ac0ce6a07 | -1.47319 | -54.2013 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4325fff-389f-30c3-86f0-0e9e2a70dd90 | -3.27763 | -53.1241 | 2025-12-10 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb6cbd4c-4d92-33db-b6dd-cf9455d4227b | -2.82133 | -45.27803 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2400116-a5c7-3b76-a6b4-87a52bc67204 | -2.42283 | -45.84458 | 2025-12-10 04:57:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01a993d7-3455-3867-b9e3-fc5e48264fb9 | -3.17433 | -52.8736 | 2025-12-10 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30bb7867-95d5-3455-9688-d17545650d1c | -5.16037 | -44.10092 | 2025-12-10 04:57:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a8f85e1-bc3d-3426-b35e-917f0d1e1fa9 | -3.95578 | -41.52702 | 2025-12-10 04:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d6747e36-bd78-3ab3-98c1-0bd0baa227a0 | -1.57933 | -53.1216 | 2025-12-10 04:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2de0880b-32b5-3025-9621-81d02f4ad75e | -2.88377 | -45.23995 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 958d4a7d-12e6-37ed-9581-8a783bb2daf2 | -3.46385 | -42.02063 | 2025-12-10 04:57:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e1c10465-cce4-3f15-b924-fd74604378a1 | -3.46068 | -42.02178 | 2025-12-10 04:57:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5ad293ad-1e63-381b-8e30-1935e6228c40 | -2.85268 | -46.83205 | 2025-12-10 04:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96f12dd5-c569-3c4f-b73d-6e10381492f6 | -3.85821 | -54.39488 | 2025-12-10 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4de9223-3456-304a-934f-4ab8cec90921 | -2.07999 | -52.05439 | 2025-12-10 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d24b773f-760a-3b90-a87e-6bf30248b6f8 | -2.04336 | -56.62019 | 2025-12-10 04:57:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69b3f169-760b-3e5d-a447-e63e5e8e375f | -3.42032 | -52.6479 | 2025-12-10 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 822bbc84-78b2-359a-ba7f-c2714c07b29b | -4.91388 | -43.46502 | 2025-12-10 04:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78049e22-5ae7-324b-ad6d-74954aa9e498 | -2.74329 | -48.39062 | 2025-12-10 04:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51d49033-aeac-3288-a53b-36768dd626ca | -3.41698 | -52.64738 | 2025-12-10 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51410593-2e08-39d8-9e16-93d2c8147646 | -2.77395 | -54.52456 | 2025-12-10 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a0a5dc93-fef0-33c4-b6f1-152d51b3c628 | -2.11976 | -53.65711 | 2025-12-10 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98236581-4336-3e4b-89a8-3fcd23eb0f63 | -3.84431 | -50.96975 | 2025-12-10 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8d00288-c37c-37cc-98ac-e7476744f6a7 | -1.88069 | -55.26253 | 2025-12-10 04:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87ae6421-4d51-3f7a-aef2-84bb2f0ab165 | -1.72224 | -53.09863 | 2025-12-10 04:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cecfd78b-3add-3f02-886b-da3447d90a62 | -2.44467 | -45.60315 | 2025-12-10 04:57:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f11e917a-c761-3ebe-8f1b-1dacd0e0e997 | -1.18897 | -55.6862 | 2025-12-10 04:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5d2b1268-28c3-3e20-b739-aa6395fd97c1 | -5.32694 | -43.55979 | 2025-12-10 04:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a0c73971-ff10-3d11-82a9-6ed0ff49f4f8 | -3.39358 | -42.10605 | 2025-12-10 04:57:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f3502fe6-5001-36d9-89c2-7778cc8860e6 | -2.00631 | -54.13872 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f2c24b3-f238-325e-a652-c6a001dcab8a | -2.75119 | -45.40232 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddd0829a-d32a-3da5-98e9-fbda7dd1405e | -4.91328 | -43.46918 | 2025-12-10 04:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61c69451-1a88-3ace-b418-7eca54884898 | -2.08054 | -52.05083 | 2025-12-10 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2d125a18-2932-3dce-a022-9a727f2df62c | -2.74211 | -54.59525 | 2025-12-10 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6085235b-e197-3fbe-97b9-121d3d29a1ae | -2.81675 | -45.27437 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dcfb25da-8d63-3fbe-996e-95e5af96abf5 | -2.48431 | -47.78078 | 2025-12-10 04:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 250fa387-e30d-3ac1-94a8-de51885d730e | -1.19593 | -54.19039 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 642f9eda-f754-3537-831a-d26a3eb76692 | -3.70331 | -50.94479 | 2025-12-10 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 061ad7e7-4748-34d7-b6ba-c6b83015acd9 | -3.46487 | -52.75519 | 2025-12-10 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54358e40-d1b3-3389-a930-52109c091d03 | -1.36247 | -53.22494 | 2025-12-10 04:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2740b8ff-dac0-3007-b70c-0225be70790b | -2.82177 | -45.27516 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91465c65-d5a2-3156-8fd5-7dbef6849774 | -3.58963 | -41.6694 | 2025-12-10 04:57:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4838b973-25c6-3112-ae28-da6c625c33df | -4.47597 | -44.08263 | 2025-12-10 04:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3cd7cea-e223-3e7f-9575-1ab3c18249c2 | -3.51846 | -47.20948 | 2025-12-10 04:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 40b7aaa7-3198-3766-ba1c-4bc0c516a19b | -2.26301 | -47.86659 | 2025-12-10 04:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f9807716-5f18-301f-b62f-aad90a93e300 | -2.51577 | -45.43409 | 2025-12-10 04:57:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97aaa53e-51fd-3b82-9018-19d8af8806ce | -3.46635 | -52.83072 | 2025-12-10 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35ecd7e7-c233-354b-ab2a-48abb9894fed | -4.11996 | -54.22339 | 2025-12-10 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f127a17e-84f2-3210-b880-ae5aa09e6c42 | -1.88118 | -54.68929 | 2025-12-10 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b757338b-b2d5-393b-abdc-f9af0b5bc7b8 | -6.00035 | -40.37837 | 2025-12-10 04:57:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1cfca3a9-5103-3de6-8423-301a172b92f1 | -1.41711 | -54.2963 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71976ebb-49ca-3aee-b668-38ce2dfa0104 | -2.84731 | -45.27618 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f73f1bf-4d5a-3abd-9072-bd8103a0123e | -2.26143 | -53.70791 | 2025-12-10 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4dc43d37-d7e9-3ea3-97b5-25395cb037f7 | -6.89583 | -42.84381 | 2025-12-10 04:57:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bbf9f4fb-e72c-3fbc-a53a-3f23f5e90951 | -2.77672 | -54.5286 | 2025-12-10 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b66b206d-52f6-3c1f-970d-6cf94ef3625e | -2.79997 | -47.3514 | 2025-12-10 04:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c81055b-2aaa-3aeb-84a3-17a66b096d92 | -3.17101 | -52.87308 | 2025-12-10 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d2a2df5-9999-38f6-ad28-1156198c956a | -2.38677 | -56.05536 | 2025-12-10 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79438c6d-6d25-3aac-b561-2f12a549c933 | -1.47597 | -54.20533 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5cf4104-ac1f-3d44-8dd2-48f215896158 | -2.79687 | -47.3424 | 2025-12-10 04:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88b2bf67-358d-3968-8a7b-f6d50be82558 | -3.39669 | -42.46997 | 2025-12-10 04:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 346aee08-a934-308a-ac86-5537f3b27b81 | -2.35846 | -48.07404 | 2025-12-10 04:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0ab1478-0f18-36b1-8482-95635d46901b | -1.47931 | -54.20586 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4671c1c8-a34f-38fc-8074-079300468b5a | -2.34667 | -53.64021 | 2025-12-10 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee3772c0-7f59-350c-a10f-4304451a0927 | -2.25885 | -47.86593 | 2025-12-10 04:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b193f4c9-cd51-3da9-9dad-a158e7ea4490 | -2.48491 | -47.77696 | 2025-12-10 04:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 15883d59-7433-3011-a0ca-117f154b25d7 | -2.60213 | -51.937 | 2025-12-10 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bdf4fa3-3d4c-3bc6-8ee1-ac09f5d7ddcf | -3.08965 | -52.7863 | 2025-12-10 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d14da1f-dca4-398b-ad07-591a0c51c340 | -3.96229 | -41.52806 | 2025-12-10 04:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 99f3060c-9cfe-39e7-92b1-d7c4867cd631 | -2.85233 | -45.27696 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ba11c61a-39cc-39ae-8673-76689d43aee1 | -2.79935 | -47.35557 | 2025-12-10 04:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5045cc49-4db4-3f33-8a67-909da53946e4 | -3.23175 | -47.47031 | 2025-12-10 04:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b6e63194-94b3-357d-9583-60d07d868ea3 | -3.70269 | -50.94875 | 2025-12-10 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad6d7bb1-0758-3619-8d8a-4a36665f1584 | -8.09889 | -55.01315 | 2025-12-10 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c20fc74-1f0d-3be0-a5c9-ed950cda6cd4 | -3.18135 | -48.03149 | 2025-12-10 04:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 452783ea-3386-3604-9f35-94841726e9c5 | -1.19537 | -54.1939 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8b7e94d-e0df-346e-bcc8-1d13b2f1f10b | -6.00367 | -40.37459 | 2025-12-10 04:57:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ee33069c-e3f0-3e71-8e86-f9e4f397a0d2 | -1.41766 | -54.29281 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6d2b458-5014-3a23-9c59-bb0d598e807a | -3.5832 | -41.66847 | 2025-12-10 04:57:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cb3827a2-3f86-3ef3-baa5-e38442fe3bbd | -2.77728 | -54.5251 | 2025-12-10 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9a18c837-040e-39a0-b12f-22d0ef009d78 | -1.57549 | -53.12452 | 2025-12-10 04:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README14.md)
