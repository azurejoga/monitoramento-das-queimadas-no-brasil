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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c855325-3748-3296-b18c-d2ecb69fcc56 | -20.85685 | -54.95649 | 2025-08-03 05:21:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3681d21-e5d9-3ea1-a8f1-ccc5b4262be5 | -23.83529 | -52.95409 | 2025-08-03 05:21:00 | NOAA-20 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 473f79b3-e750-3715-94fb-59893217c481 | -6.6144 | -59.9656 | 2025-08-03 05:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 20e1b020-4e2a-3416-b1aa-02a780e6e649 | -4.5684 | -44.2036 | 2025-08-03 05:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 0cc9e31e-03db-3e95-acbd-11778157b7cf | -8.0126 | -43.1749 | 2025-08-03 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 153.4 |
| 8f1c25e4-d80a-345a-b2bd-b6d3ef82a01a | -8.0129 | -43.1513 | 2025-08-03 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 229.0 |
| 5f4c49d4-58a9-3237-8e91-1a208994e843 | -7.9937 | -43.1769 | 2025-08-03 05:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 115.7 |
| d4714b8c-99f6-3571-8c30-234eddd72cae | -7.994 | -43.1534 | 2025-08-03 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 131.2 |
| 3c0597fe-a9d1-30d2-bcf7-5dffd58645da | -8.0318 | -43.1493 | 2025-08-03 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| c3a5c385-c960-3c0d-bb5e-eeb4e004e8c6 | -6.6329 | -59.9649 | 2025-08-03 05:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 046e83de-03c3-3f82-ad02-5b8d1ffdb34c | -7.9937 | -43.1769 | 2025-08-03 05:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 560ce223-b83d-3b45-9d58-fe71b0ef45ed | -8.0129 | -43.1513 | 2025-08-03 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 231.1 |
| 54d1d4e6-3ba6-39c5-ad22-8c8789a3751e | -8.0132 | -43.1278 | 2025-08-03 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| fddb238d-9a35-35e1-929e-38166e262db0 | -8.0126 | -43.1749 | 2025-08-03 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 145.6 |
| 35d962d3-69f9-3a6e-8cc5-a55790ae35d0 | -8.0318 | -43.1493 | 2025-08-03 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| fb66ee71-cc79-38bf-8984-48872ec08b77 | -4.5684 | -44.2036 | 2025-08-03 05:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 0fc47247-55b0-3d4c-af78-edb483b1819c | -7.994 | -43.1534 | 2025-08-03 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 8f092b4f-86b9-39be-b77f-ed2f105d267d | -8.0126 | -43.1749 | 2025-08-03 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 173.4 |
| a81053d5-866c-3f84-9be9-963c95b22d45 | -7.994 | -43.1534 | 2025-08-03 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| 0c3be6f9-1883-3065-b560-c84ee576c0f1 | -8.0129 | -43.1513 | 2025-08-03 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 286.6 |
| 570bf3d3-06c6-3915-b105-bdb21ad917a5 | -7.9937 | -43.1769 | 2025-08-03 05:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 15ac1757-5533-3802-9db4-c1389a290fb2 | -8.0132 | -43.1278 | 2025-08-03 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| f8f7719b-c5c0-3bfa-815e-bbfc81c9e935 | -7.994 | -43.1534 | 2025-08-03 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 125.3 |
| 1cbe2262-d789-3f5b-8594-63cb7d9cfb2e | -8.0132 | -43.1278 | 2025-08-03 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 7925b7e3-1631-34e8-abff-1a5463b0db38 | -8.0126 | -43.1749 | 2025-08-03 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 174.8 |
| e7b2a919-1939-3755-8720-7e0fc5af47a7 | -7.9937 | -43.1769 | 2025-08-03 06:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 90f90960-c031-3651-a30f-089a27e8f230 | -8.0129 | -43.1513 | 2025-08-03 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 301.8 |
| 9249fc3d-7c40-3e34-a6a7-ec20bbdacc0e | -4.5497 | -44.2047 | 2025-08-03 06:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 363567f1-cd54-33ea-9832-3974baa396b9 | -6.73074 | -59.17066 | 2025-08-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 65619f0e-6fb5-3bec-a61b-f835aec79ac2 | -6.67042 | -59.16243 | 2025-08-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6af11eb-7689-3687-8cf9-0d2034edc68d | -6.67628 | -59.16991 | 2025-08-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bd41f281-9646-3b85-b8f5-e72d639f9612 | -6.67711 | -59.16339 | 2025-08-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 91eab6b4-6961-3f1f-9e4e-136e564fcaf7 | -6.64735 | -59.1057 | 2025-08-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 26620ddf-6ead-3ade-b56d-f9b866d65733 | -6.67951 | -59.17186 | 2025-08-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 41ffd065-3b92-391e-80ea-36176e01f674 | -6.67369 | -59.16438 | 2025-08-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 80228205-fc17-352d-a7a2-32dac666a2e4 | -6.65407 | -59.10662 | 2025-08-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1bde016a-5307-3221-9872-80d8715546ff | -6.67284 | -59.17078 | 2025-08-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bd6b29a1-09fd-3f60-ba60-cc272e2fd66f | -6.68037 | -59.16545 | 2025-08-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 97d08077-1a41-3ead-aa63-7fad0d8821af | -6.66961 | -59.16876 | 2025-08-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9835f1a5-b215-35d7-9a73-c1b6172a8fb3 | -6.65326 | -59.11277 | 2025-08-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4646de08-3a1c-3d51-81f3-81e1c5d982a8 | -6.8168 | -59.27055 | 2025-08-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6c313fb-021e-3b04-813a-6712f21f2501 | -8.45534 | -70.14557 | 2025-08-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e48cfb4-4f5d-35cf-88ae-16adf40fc884 | -6.64654 | -59.11184 | 2025-08-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 58895461-bd95-3fa4-ba58-bf334430df08 | -8.0126 | -43.1749 | 2025-08-03 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 134.8 |
| 4f5936a1-e1de-32d9-82a5-9bf242b5d439 | -7.9937 | -43.1769 | 2025-08-03 06:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 100.4 |
| 53a5b3f5-f59b-3cfa-b807-9d93a961d1be | -8.0129 | -43.1513 | 2025-08-03 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 321.9 |
| 7ed8860c-8778-319e-98a4-43464c5055e1 | -7.994 | -43.1534 | 2025-08-03 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.8 |
| 1960d35a-9b67-3c9a-99d4-fa672d35867b | -6.6144 | -59.9656 | 2025-08-03 06:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 487f0869-f42f-365d-bc4d-88cd7c3b85ec | -8.0132 | -43.1278 | 2025-08-03 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 15bfe7c9-d820-3f5c-9486-9de595e830f1 | -8.0318 | -43.1493 | 2025-08-03 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| 2b4bfe92-fa68-345b-83f4-f47dd455ac73 | -6.64912 | -59.10887 | 2025-08-03 06:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| ceb4e2d3-4c05-3b58-8db0-123f8d96a03a | -6.67146 | -59.15712 | 2025-08-03 06:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 89061a03-7a9d-33a0-ae6d-bbeee8a99d4c | -7.01878 | -59.82759 | 2025-08-03 06:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 090b6d0e-322a-3899-9508-65c12d4385ba | -6.61692 | -59.9645 | 2025-08-03 06:29:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 72378be5-1a74-3227-aaf1-a1ce0356ae00 | -6.61889 | -59.95213 | 2025-08-03 06:29:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bf4006e5-d27d-3201-998e-bc3a22a0e8ec | -6.65082 | -59.09808 | 2025-08-03 06:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 67b63d34-0425-36fa-aed2-ae27e75c43a1 | -6.66977 | -59.16798 | 2025-08-03 06:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 7e69d171-602c-37ba-9f81-9d4c511713d0 | -2.90305 | -54.15411 | 2025-08-03 06:29:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 64aaf2d2-f0b4-3002-a91c-12538541a70c | -6.73227 | -59.17237 | 2025-08-03 06:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cb298ba1-9c85-309a-b882-c1bd1464b8e4 | -7.9937 | -43.1769 | 2025-08-03 06:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 6490abdc-3d34-3b2a-b8eb-6776c31e6f14 | -8.0129 | -43.1513 | 2025-08-03 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 334.1 |
| abc8aef3-f96a-31b1-9594-a4dffa6d88d4 | -7.994 | -43.1534 | 2025-08-03 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.6 |
| d669f5f4-addb-3606-b6f7-3e6513f7f98a | -8.0126 | -43.1749 | 2025-08-03 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 155.1 |
| 6bc94dcc-fd15-39eb-aba2-43239c143f68 | -8.0132 | -43.1278 | 2025-08-03 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| e704ca95-db05-3aca-b292-a4ee08d4da30 | -8.0129 | -43.1513 | 2025-08-03 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 352.0 |
| bf3fda58-018a-3c88-be51-f14a553d786f | -7.9937 | -43.1769 | 2025-08-03 06:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 123.9 |
| 465db600-bba0-30ce-9c44-3731fa55eaa1 | -8.0318 | -43.1493 | 2025-08-03 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.2 |
| 7df84d4b-1f71-3dfd-a933-9ff4882c91d8 | -6.6144 | -59.9656 | 2025-08-03 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 2fa1c60e-f548-3804-a646-b2cbb619a07f | -8.0126 | -43.1749 | 2025-08-03 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 163.3 |
| 4550a018-3e87-31b8-96ec-3ae7dbfb4e23 | -7.994 | -43.1534 | 2025-08-03 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 172.7 |
| ed72f4e5-8d6f-3ad0-a84e-821ff6b7537e | -8.0132 | -43.1278 | 2025-08-03 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 1a447777-a28d-3c00-8557-660f34ac5fb6 | -8.0132 | -43.1278 | 2025-08-03 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 0a51024a-87fe-3f30-a72d-8f7974feacc3 | -18.5824 | -51.1708 | 2025-08-03 06:50:00 | GOES-19 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 2b1fbcbd-da6a-3b27-a713-afb0a12aebb3 | -8.0318 | -43.1493 | 2025-08-03 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 4b59d1ba-892a-3441-84ba-8134eeb9b76f | -7.994 | -43.1534 | 2025-08-03 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 495.3 |
| 6bf2d401-97b3-3d61-ba93-885bd8f15e53 | -8.0126 | -43.1749 | 2025-08-03 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 219.8 |
| f24afb37-5ada-364e-855b-1d06622abf83 | -8.0129 | -43.1513 | 2025-08-03 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 521.9 |
| 955c6002-e1cc-3d05-874b-d474eacbd8c8 | -7.9937 | -43.1769 | 2025-08-03 06:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 232.9 |
| 29942a64-c435-3d2d-9054-9aca412c90c1 | -18.5824 | -51.1708 | 2025-08-03 07:00:00 | GOES-19 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 77203481-1a61-3e83-a8ea-6327fa11be65 | -18.5829 | -51.1487 | 2025-08-03 07:00:00 | GOES-19 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 56.1 |
| 1a4d6a62-f8cf-3999-bfd9-e8d8aa6d5efd | -4.5684 | -44.2036 | 2025-08-03 07:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| c52949a6-afff-3339-8f8a-193dc8ce33f6 | -7.9937 | -43.1769 | 2025-08-03 07:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| a33254f3-552e-3cef-82cc-dfccae03a940 | -8.0318 | -43.1493 | 2025-08-03 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 51f1cd60-bf0c-3293-a19e-24ff978b6a21 | -7.994 | -43.1534 | 2025-08-03 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.1 |
| 17cd611e-b8cf-3835-92d4-6d697a765d7b | -8.0132 | -43.1278 | 2025-08-03 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| c648ff92-b1ad-39a3-bcea-95542a276629 | -8.0126 | -43.1749 | 2025-08-03 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 379abb65-36ea-358e-bcac-61d5e208366e | -8.0129 | -43.1513 | 2025-08-03 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 204.4 |
| 63f07c07-e25e-3a2d-be51-046342f3b591 | -8.0126 | -43.1749 | 2025-08-03 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 5761ef8d-f233-3436-a17e-3a9154bdb365 | -8.0129 | -43.1513 | 2025-08-03 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 221.0 |
| 0b5a02a0-0bd4-3632-b95e-b2094455b260 | -7.9937 | -43.1769 | 2025-08-03 07:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 58.0 |
| 1bcb60f5-1fc6-36c6-a271-d10dd1432f8c | -7.994 | -43.1534 | 2025-08-03 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| 067bceef-1c23-3ebe-b848-8fb780b10710 | -8.0132 | -43.1278 | 2025-08-03 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 091d9ca3-9415-3c76-8dba-d79303ae87b3 | -7.9937 | -43.1769 | 2025-08-03 08:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| e10bb2a2-1546-3ca9-a252-ab43ad32a238 | -8.0126 | -43.1749 | 2025-08-03 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| e778c5b8-3c17-33f5-845e-1594517fa695 | -8.0129 | -43.1513 | 2025-08-03 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 171.5 |
| 09462deb-9fb1-3a87-bfa7-914736fb4d1f | -8.0318 | -43.1493 | 2025-08-03 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.4 |
| 444af94b-42d7-3bea-87eb-48af02dbef42 | -7.994 | -43.1534 | 2025-08-03 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.2 |
| b181b5bb-9ff1-3f01-9ae1-a7b30b1105a9 | -8.0132 | -43.1278 | 2025-08-03 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.3 |
| de502e84-cfbf-3528-a46d-62bae3360f40 | -8.0132 | -43.1278 | 2025-08-03 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| f5ba4cf2-a68f-3ae0-b95d-b6da70fa81c8 | -7.994 | -43.1534 | 2025-08-03 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |


[Clique aqui para ver as próximas entradas](README31.md)
