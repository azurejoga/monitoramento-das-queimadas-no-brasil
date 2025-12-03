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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32125307-9626-386b-97f2-fe5863586473 | -3.23347 | -45.54759 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 425f4405-d026-3c5a-9101-18ed7cb01135 | -3.38645 | -50.003 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9f5ca3d-d81d-36a7-9309-b4bc67ec2f73 | -2.91032 | -48.72542 | 2025-12-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e684fc9-4e51-3def-9b7f-0cf8b3a38fbd | -2.32063 | -48.57964 | 2025-12-03 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b5adb91-c77d-37de-8208-a1fb55861055 | -3.53423 | -49.98967 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba1ae430-fb18-317f-8bac-5898b94dd572 | -2.4514 | -48.505 | 2025-12-03 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a46f63be-184b-3c8c-a7eb-3a502fa6d937 | -2.85525 | -46.73674 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 7a3ac6df-235a-35aa-aaaf-c6e8a674ad12 | -3.28933 | -50.08196 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b89c474-650c-30a0-87ea-8dd996e8dc48 | -2.45505 | -49.32853 | 2025-12-03 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 367a798d-faa7-3d51-810c-37b21af7e7de | -1.86707 | -48.02266 | 2025-12-03 04:38:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0f1c90d-7c56-3a6c-bc9d-0adc9b40628b | -2.72314 | -47.39994 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a9e68b1-6c0f-3e93-b4e6-a81abf0e981a | -3.32249 | -42.49388 | 2025-12-03 04:38:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 078210d3-53c5-37bb-b665-5c9932b376f4 | -3.23746 | -45.56945 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 98e5727a-331e-3097-bbc6-f9b93bf9cd4f | -2.96749 | -49.53007 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd70e4c3-5da1-31c6-9c55-ff7ef0cc0384 | -3.22346 | -46.87177 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84451e34-f193-335b-9e4e-7789c0ef1094 | -2.24384 | -45.62043 | 2025-12-03 04:38:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5b91c3d5-1527-3955-ba21-341e51ad3070 | -3.2194 | -45.5622 | 2025-12-03 04:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 2fb602c4-f0f5-3bb4-8aa1-c6b9c30ccd0c | -3.2379 | -45.5615 | 2025-12-03 04:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 2a713d68-ca5d-360b-af48-d12227ce9639 | -3.2565 | -45.5607 | 2025-12-03 04:40:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 89f45fea-96a4-33dd-8c03-ebd90793161d | -3.2378 | -45.5839 | 2025-12-03 04:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 02d7aeed-c436-36e7-a07f-5367e0fc5536 | -3.238 | -45.539 | 2025-12-03 04:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| a592ae14-0076-3ada-bbbf-db14df3f21d3 | -11.12374 | -53.95331 | 2025-12-03 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdf9606f-c384-3920-b5d3-d03c1cb6a7e4 | -13.6465 | -49.40458 | 2025-12-03 04:40:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82c707c4-e735-3aaa-9484-c8d536a43085 | -10.76397 | -52.42802 | 2025-12-03 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e09ff006-9a04-3b6d-a22c-23c712dea1c6 | -8.16757 | -43.22371 | 2025-12-03 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7d300ecb-2d2e-3219-a300-fd54d93a9574 | -11.2783 | -52.46259 | 2025-12-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3435853b-f974-3bb8-b7cf-2ec5b21dd4a0 | -11.27489 | -52.46202 | 2025-12-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 741cef13-2b21-3106-8bc9-0ca4179a4dc0 | -9.6721 | -48.52422 | 2025-12-03 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75d6acd0-70b6-3ae0-8398-016ee4f03f45 | -8.1693 | -43.17807 | 2025-12-03 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c28efe9a-aa9e-34a1-b185-2daf7620516c | -10.22938 | -48.08267 | 2025-12-03 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2343ce4b-9826-3615-8522-dad0fef87126 | -11.27147 | -52.46144 | 2025-12-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8380e2f-88f6-3c05-8a7e-1a375688f828 | -9.29862 | -40.36519 | 2025-12-03 04:40:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 71befe27-cb4b-337e-9ff6-dd8ba84428c4 | -12.85052 | -52.51946 | 2025-12-03 04:40:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4b6dce9-2ea4-3075-8b36-78378810a78a | -11.12446 | -53.94901 | 2025-12-03 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7b864b24-e91d-3352-a44a-f41dba05657a | -8.17205 | -43.22433 | 2025-12-03 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2f30c796-db7f-326d-b158-8f00b3123a01 | -11.1281 | -53.94965 | 2025-12-03 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4f07551f-01cb-3e79-9f14-bc6673b22c56 | -11.27428 | -52.46578 | 2025-12-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c202202c-830f-3b0f-8cc1-1d774c3687e3 | -11.27769 | -52.46636 | 2025-12-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d98cd958-fdf9-3dba-8bd7-fb78fcdaf75b | -11.12738 | -53.95394 | 2025-12-03 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60ee7ab5-f9f4-3b71-8225-0765705f066c | -10.22593 | -48.08215 | 2025-12-03 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8aa45946-b789-36e4-b3eb-668b47d0c337 | -8.99094 | -48.0919 | 2025-12-03 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74d0a157-449a-3abb-91fb-b9f93915d6f3 | -10.19943 | -48.09371 | 2025-12-03 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1253c51e-7e4d-3312-bebc-ac39d5aaa9d9 | -10.22535 | -48.08597 | 2025-12-03 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a590331b-35b9-3c3d-a48c-9880bf6ffe64 | -11.13246 | -53.94598 | 2025-12-03 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c0b9c7e-2e0e-3d20-bd94-e41484128e9b | -9.58078 | -44.60641 | 2025-12-03 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dee5b87-230a-37ad-9b3d-58208ac664f9 | -11.12882 | -53.94536 | 2025-12-03 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d55b7d2e-016a-3be4-b8a2-957c76e44fd6 | -7.8671 | -38.73045 | 2025-12-03 04:40:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e745b401-6481-3c68-b3ee-60724df8f0ac | -11.13174 | -53.95028 | 2025-12-03 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8b7a095-c674-3489-8910-0c6382e34808 | -11.12518 | -53.94472 | 2025-12-03 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d2237c6-b74d-3e39-bd44-c46fc383fd97 | -9.11086 | -50.52614 | 2025-12-03 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75667b64-0e6c-3ade-a0bb-833446f65047 | -10.19598 | -48.09317 | 2025-12-03 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4407bd3-970b-3bcd-aee6-546895481e83 | -7.86481 | -38.73212 | 2025-12-03 04:40:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 467ff1e4-3370-3bb8-81e7-c75f4d99e7c4 | -14.94445 | -53.05961 | 2025-12-03 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 589fd01c-e34d-32c9-88a8-73a7ab001323 | -20.3057 | -47.35042 | 2025-12-03 04:42:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b293a990-9bb4-3b16-9abd-79fb53f161af | -15.12301 | -52.95222 | 2025-12-03 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcd9ac1b-8b6e-32ce-8b7b-df55224a98b0 | -16.32919 | -48.87645 | 2025-12-03 04:42:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 063285c5-d43a-3fa7-96c1-ac416eef81bc | -14.96599 | -53.05561 | 2025-12-03 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 914b8d2c-862e-321c-9dd9-2624f43b56e5 | -14.94783 | -53.0602 | 2025-12-03 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a6654c8-8479-3956-995f-5101d9faf7c3 | -15.76495 | -53.13877 | 2025-12-03 04:42:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c527f2d0-7bc4-3e93-9aee-f5ab9521cf52 | -16.79305 | -47.32093 | 2025-12-03 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10b3e069-023a-3181-98ba-042c84cbf41b | -16.51559 | -51.20395 | 2025-12-03 04:42:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 43e7f506-26de-32f2-8517-a59b2503a47f | -15.12361 | -52.94852 | 2025-12-03 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54bc779b-a15c-35d6-b4f2-7dece4eb663e | -15.12084 | -52.94424 | 2025-12-03 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a02656e6-bf6a-35df-9810-ea74c388a2c1 | -15.11963 | -52.95164 | 2025-12-03 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 302d5d8a-f1d8-306e-908f-271f0b8073eb | -15.11686 | -52.94737 | 2025-12-03 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1fdbd1d6-2304-3b32-9447-957cefb7ffe5 | -15.11747 | -52.94366 | 2025-12-03 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3553b181-5a88-329c-94e7-7c6f1f5f5e96 | -18.16103 | -39.65572 | 2025-12-03 04:42:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| c6eb6e9e-e9f8-3df8-a5a7-d024d5cc49f6 | -20.30168 | -47.3496 | 2025-12-03 04:42:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d16260c7-c17a-39ed-a1c3-04860f6d495e | -15.12421 | -52.94482 | 2025-12-03 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3b02374-9bc5-3d43-8b12-1ebc6773f385 | -18.69917 | -47.59497 | 2025-12-03 04:42:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2402dbbe-ac41-3488-b8c6-88e89791bf38 | -15.11903 | -52.95536 | 2025-12-03 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5138c2de-1d56-3c6e-b3c2-688bb2238033 | -18.16157 | -39.65012 | 2025-12-03 04:42:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 29351413-1cbb-35da-94ae-a0143f13f351 | -15.5778 | -39.02979 | 2025-12-03 04:42:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 77a79333-5289-3955-ae74-71f49e52f419 | -20.30121 | -47.35347 | 2025-12-03 04:42:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3ff7363-9229-3215-81cc-ee3d5645b208 | -15.12024 | -52.94794 | 2025-12-03 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 79ed1476-d589-33eb-abf7-ec8d526745e3 | -17.15171 | -48.08851 | 2025-12-03 04:42:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 167039d9-4b04-3c67-9233-5783167681fd | -18.16231 | -39.65173 | 2025-12-03 04:42:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| af45b8ac-84e9-3142-80ad-15a6147a4e65 | -18.15586 | -39.65097 | 2025-12-03 04:42:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| cfd08b5c-0bdd-3410-ac33-129d9f40fd00 | -21.3245 | -55.78423 | 2025-12-03 04:44:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28e22372-fe42-3429-8063-19e3549b3797 | -22.73067 | -49.3541 | 2025-12-03 04:44:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce740d62-73b1-3fd9-a78c-ac8fee85d967 | -28.06289 | -48.6722 | 2025-12-03 04:44:00 | NOAA-21 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cc84d46f-ef92-3e68-a5d5-3f3e0f77565d | -21.19018 | -49.55839 | 2025-12-03 04:44:00 | NOAA-21 | MENDONÇA | SÃO PAULO | Brasil | 3529500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7849c4bc-8552-33aa-b483-c9dee1217c3b | -21.62404 | -56.13089 | 2025-12-03 04:44:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 279af5ba-9c46-3423-a3a3-d8d03b145867 | -22.7313 | -49.34941 | 2025-12-03 04:44:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bf48cc3-758c-324f-ae3a-bc8b1d9d2ba9 | -22.72887 | -49.35078 | 2025-12-03 04:44:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1abf690d-3ad6-31b2-86c2-699639bfd3a0 | -23.31604 | -49.42402 | 2025-12-03 04:44:00 | NOAA-21 | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e86dd141-5a8d-3445-8393-9fb3ce57ca16 | -21.18963 | -49.55604 | 2025-12-03 04:44:00 | NOAA-21 | MENDONÇA | SÃO PAULO | Brasil | 3529500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bfc7af55-e22d-376e-99ec-85908b1adb99 | -21.62684 | -56.13588 | 2025-12-03 04:44:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5c1a6f80-e665-3811-bd5d-f8c360fb8ae0 | -21.62328 | -56.13517 | 2025-12-03 04:44:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d82987f9-75e6-38f9-83c3-75ca29f999ae | -20.88883 | -49.89926 | 2025-12-03 04:44:00 | NOAA-21 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2ad0a32f-961b-3430-bd4b-4c0244b79a4c | -24.30441 | -51.74067 | 2025-12-03 04:44:00 | NOAA-21 | IVAIPORÃ | PARANÁ | Brasil | 4111506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 00e45353-3526-3d75-b9e3-21af1113d6d8 | -22.95875 | -48.69241 | 2025-12-03 04:44:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a51ec3a7-187d-3dc4-aae0-9ed13077207b | -20.8919 | -48.30267 | 2025-12-03 04:44:00 | NOAA-21 | VIRADOURO | SÃO PAULO | Brasil | 3556800 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb5245f4-b7eb-374f-afa9-fd6f545b1a63 | -30.51354 | -52.80419 | 2025-12-03 04:46:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 7d0aa2ed-99dc-3477-80d0-a16cdf935ecf | -30.51413 | -52.7999 | 2025-12-03 04:46:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| b33efaf2-a995-3289-99e5-a11c4656639b | -3.2379 | -45.5615 | 2025-12-03 04:50:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 154.2 |
| 6ae264b7-7430-3214-bd3a-fa8a80090284 | -3.2565 | -45.5607 | 2025-12-03 04:50:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 0cc10f4e-7738-3b54-9f25-b31921d71ae0 | -3.2378 | -45.5839 | 2025-12-03 04:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 77831366-2b8e-31e5-80a0-9891e4af0024 | -3.238 | -45.539 | 2025-12-03 04:50:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |
| ae7b9a20-cdba-3363-abfa-80a6b2d71cdf | -3.2194 | -45.5622 | 2025-12-03 04:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 86.5 |


[Clique aqui para ver as próximas entradas](README16.md)
