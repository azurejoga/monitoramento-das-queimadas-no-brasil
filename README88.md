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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fe40f05-890e-3147-91c4-48f7e15705b7 | -5.9819 | -57.6892 | 2026-08-30 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 95e820e7-f2eb-3d9f-b61b-014c9c50c771 | -5.4876 | -57.1416 | 2026-08-30 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 8d51b0b1-6a25-32eb-98cd-1497f2ce2272 | -9.9281 | -60.5242 | 2026-08-30 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| eb001451-8758-3f5f-944e-d7a2f20528e9 | -9.0615 | -65.4169 | 2026-08-30 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 370a558c-245d-3ba0-a37c-2ff60daf948d | -11.2294 | -45.099 | 2026-08-30 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 516092ff-4f36-3dbc-a29a-1a5648b0ad02 | -7.1121 | -42.7963 | 2026-08-30 14:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 148.2 |
| c9bc48f8-481e-3734-ac8d-1a668c491e26 | -9.0614 | -65.4355 | 2026-08-30 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 6b3c36a7-0453-33e1-84b7-ede9fdae7ac5 | -12.2277 | -50.5792 | 2026-08-30 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| d7bf4620-e74d-3f07-afbd-48a94c4cf172 | -3.4943 | -54.6567 | 2026-08-30 14:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| f48b3e82-24e8-374d-85e2-723de7728b18 | -11.1995 | -55.1008 | 2026-08-30 14:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 9f542a96-4adc-39da-9f82-6840508701e9 | -8.6154 | -54.7945 | 2026-08-30 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| a484c6ad-d56b-3490-9170-843433f31ec9 | -2.9488 | -43.7536 | 2026-08-30 14:50:00 | GOES-19 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 02a39683-fddf-37d1-86e7-5abb2c9fc28e | -12.9216 | -45.8812 | 2026-08-30 14:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| ed32b5f3-92ff-3f73-8ce4-0ad413281b92 | -6.5234 | -51.4279 | 2026-08-30 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 5bcefb96-fea7-3dde-a2cf-55b194ef2053 | -9.9284 | -60.4856 | 2026-08-30 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 60cff72c-4c9e-3456-a53e-f860a160058d | -8.5925 | -66.9564 | 2026-08-30 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 3deda8c3-79f2-396f-9551-bf4beba907a8 | -9.043 | -65.4175 | 2026-08-30 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| bdec5fac-7247-377b-bca2-db745f1c27c8 | -14.5627 | -52.077 | 2026-08-30 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 50de8a26-9a85-33d1-a8b6-1e6fc3f11a4d | -9.9282 | -60.5049 | 2026-08-30 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 438380b6-f622-3f2a-b27c-a978a0ad2637 | -3.2361 | -61.2548 | 2026-08-30 14:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 9bd603c3-b78b-3000-af02-885b3b4c65bb | -7.2932 | -60.6096 | 2026-08-30 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 02fe7fb3-02a6-31cb-94be-9f01c65520f5 | -14.7601 | -48.7467 | 2026-08-30 14:50:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 113.6 |
| ca438d67-9b9c-3cb5-a06e-e2f7b422fe15 | -6.4101 | -51.6634 | 2026-08-30 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 598174b5-9849-37e1-b92f-f253717c9404 | -15.2283 | -57.6517 | 2026-08-30 14:50:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 041afe88-c042-3c89-a72f-7b531c5b62a4 | -8.574 | -66.9569 | 2026-08-30 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 267d09a0-6666-3c8d-bbbe-df90d8eab55c | -10.7454 | -50.6812 | 2026-08-30 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 524d94ef-da46-3e74-b71c-dd2abf75e7cc | -11.0627 | -47.1385 | 2026-08-30 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 28bfad12-9d7f-352d-b78c-870e39c29da9 | -9.2262 | -65.8784 | 2026-08-30 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| c1429f68-3165-33a9-a104-cf7c73317e01 | -12.2281 | -50.5578 | 2026-08-30 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 14a6a809-4998-34b3-9cec-c5c58db255ca | -9.1532 | -59.5221 | 2026-08-30 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 0161b458-71a7-35c0-b032-a3d4755508dd | -14.1456 | -52.8082 | 2026-08-30 14:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 08fddf72-4369-378e-8406-a4082edc2dba | -11.2443 | -45.3497 | 2026-08-30 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.9 |
| 185444ea-6ea2-31b8-8425-23b4f7f6e090 | -11.2485 | -45.0963 | 2026-08-30 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 03de8084-dd3f-31bb-b52d-1bd1cf94810c | -6.861 | -41.6772 | 2026-08-30 14:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 354.3 |
| 9977c4b0-43d9-344a-badb-f7286e50f4ef | -7.1315 | -42.7472 | 2026-08-30 14:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 1765d569-c265-3056-93bb-6a5a2900352e | -9.874 | -60.2762 | 2026-08-30 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| f8c3a8ca-2c6c-3c35-a4dd-1950f8210c6d | -5.871 | -57.7715 | 2026-08-30 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 662c5095-6fc3-3a1a-b200-3c145ec057ce | -8.1534 | -45.4904 | 2026-08-30 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 17110aa3-bb77-361c-b353-27a61e38ef75 | -15.3849 | -52.6677 | 2026-08-30 14:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 878eac5d-4386-341c-884b-725712d5ab8d | -13.3422 | -51.4256 | 2026-08-30 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 618c2591-f398-3a3f-9bc6-a8c260c9a924 | -12.0921 | -47.1812 | 2026-08-30 14:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 498beaa9-fe7f-32d9-bfde-1942861b746d | -14.4387 | -52.56 | 2026-08-30 14:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| e6798e10-9f9f-3513-9cb1-43d236fa1932 | -4.1516 | -60.6878 | 2026-08-30 14:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 80e21c72-dd04-3ee8-af3d-eeebc06e1ecb | -7.2933 | -60.5905 | 2026-08-30 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.5 |
| cea8128c-1f24-3c9c-9912-07e86f8f0753 | -7.1312 | -42.7708 | 2026-08-30 14:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 245.3 |
| 55756dd7-da2d-346b-814e-d5410c729b94 | -9.0723 | -60.4148 | 2026-08-30 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 99cae401-1773-30b2-9cbf-c7943eefed76 | -8.739 | -45.3844 | 2026-08-30 14:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 7a2d1265-deaf-31e9-8e27-3b4af5264388 | -14.5631 | -52.0557 | 2026-08-30 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| a190a005-96e7-35a7-8b97-2fee02ea2804 | -11.3427 | -45.1751 | 2026-08-30 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d0c47e64-2358-30d7-b2fc-c9b7e24743c1 | -10.4794 | -64.5012 | 2026-08-30 14:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 34b2a2a3-104f-3598-b70d-c65fa09570ad | -13.8749 | -54.1361 | 2026-08-30 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| b6e3b5eb-b207-38e3-b180-907ffc397026 | -12.9221 | -45.8582 | 2026-08-30 14:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 0fa4002f-0f8b-3304-bd02-4e5f4d78d27f | -4.9605 | -55.8226 | 2026-08-30 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 82d498ba-d49c-3126-9f19-78e3151da2ab | -11.3619 | -45.1724 | 2026-08-30 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 954eb8f0-625b-323d-b90c-a0dadb958ab9 | -5.9635 | -57.6899 | 2026-08-30 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 182303f9-f265-311b-8e22-1ddd077e8e12 | -7.3294 | -55.1555 | 2026-08-30 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| e776fbc5-1c3a-3f38-bd8d-8f3da10b5d3d | -10.7647 | -50.6579 | 2026-08-30 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 565ed7e1-0f10-3d79-acda-65e3cae3d9d0 | -16.2729 | -42.59 | 2026-08-30 14:50:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 139.2 |
| b696611d-80ac-3e42-b67a-585ac3171921 | -10.7644 | -50.6792 | 2026-08-30 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 182.7 |
| b5c0f19d-2e4e-3e8c-83dc-156b336c3630 | -11.8021 | -51.0343 | 2026-08-30 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 1103e1fa-9e27-390f-98f4-e5f5a7088b03 | -11.0054 | -49.6893 | 2026-08-30 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c33d8f0d-a0bb-36db-943e-d4fcced44b43 | -10.7649 | -50.6366 | 2026-08-30 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 70645cf3-283e-333d-ab79-533c03858253 | -14.3175 | -51.7474 | 2026-08-30 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 42a059fb-b521-3ccb-a439-b97013bafb12 | -9.1523 | -59.6384 | 2026-08-30 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 701f6868-c873-367d-a66f-13b564534082 | -3.6399 | -60.5466 | 2026-08-30 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 7eac4b0a-b6e3-3f0f-96dd-9c69079d1cb8 | -8.1534 | -45.4904 | 2026-08-30 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 1e591fae-79c8-31fa-91fc-98fc879b5262 | -7.1309 | -42.7945 | 2026-08-30 15:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 104.9 |
| 938cad07-c2d6-37db-bcbc-e8ff8cc99e52 | -7.546 | -44.3395 | 2026-08-30 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 5a31e223-1eb3-30e5-9a6f-42dc8d189595 | -7.2932 | -60.6096 | 2026-08-30 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 5b28674b-875c-358f-95ea-20582b9c5318 | -14.1649 | -52.8058 | 2026-08-30 15:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 234.3 |
| 1da4a0a6-f0f3-387b-b0ba-da6a186f0e65 | -10.7409 | -54.0196 | 2026-08-30 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| f0cfbd8b-cf33-3076-86ab-375d53667c22 | -6.0 | -45.0889 | 2026-08-30 15:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| f739dcd2-5f5a-38cf-8031-455b6b9836fd | -4.9787 | -55.8615 | 2026-08-30 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| cdee92ea-6660-3a6f-b83d-311a34a6ab27 | -11.0057 | -49.6677 | 2026-08-30 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 0501c329-0612-3236-99bf-578e1873801e | -10.7867 | -45.3433 | 2026-08-30 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 241.0 |
| eebd415a-6c5c-3549-8200-8248a946fa72 | -10.8249 | -45.3382 | 2026-08-30 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 280.8 |
| 39849701-52d5-3456-a05d-0df9454f83af | -21.0172 | -57.8313 | 2026-08-30 15:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 5fd3fda4-fb3e-3639-9180-d0e8a0b90f95 | -10.1538 | -45.6982 | 2026-08-30 15:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 225.5 |
| 02314700-2a26-314c-801f-26328d0d6fe1 | -14.5627 | -52.077 | 2026-08-30 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 2af264e3-cd7e-3f18-91cf-f09ca5d40e0f | -4.9605 | -55.8226 | 2026-08-30 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 4e5248f9-ff2a-3abe-9af4-22ff11a61b33 | -10.7644 | -50.6792 | 2026-08-30 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 26ce8487-2e03-3925-858a-8306a6ee7a30 | -10.4794 | -64.5012 | 2026-08-30 15:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 917390cb-120b-3f70-b56c-19b7fc8f3ca3 | -7.5661 | -61.3239 | 2026-08-30 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 51ce42b3-e04d-3120-bac8-9215191b560d | -14.7601 | -48.7467 | 2026-08-30 15:00:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 90.3 |
| a5e8a531-5b82-35ec-84cd-3cdd5de6e9b0 | -11.2506 | -53.9941 | 2026-08-30 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| f843a36e-7a37-3b79-a768-4a6c460771ad | -9.874 | -60.2762 | 2026-08-30 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2a93a44b-3f81-37e5-b97c-97110d0b5731 | -14.1456 | -52.8082 | 2026-08-30 15:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 4f9ca57d-23b9-3a2e-b167-19a92507090f | -8.1345 | -45.4923 | 2026-08-30 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 31150e60-880b-350e-ae02-8a0738e6433f | -11.2128 | -53.9976 | 2026-08-30 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 211502f5-8623-3f26-8874-32595c4dd52b | -9.1525 | -59.619 | 2026-08-30 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 5621a8e6-0e64-33bc-b6fc-eadf58fd6ead | -11.0054 | -49.6893 | 2026-08-30 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 12013e19-93a5-3521-9c1a-93090a505d39 | -10.358 | -49.9742 | 2026-08-30 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 8494f0d3-e756-3a3b-a063-1f7a4ea9b447 | -5.871 | -57.7715 | 2026-08-30 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 294dbd48-cda2-36b3-824c-b303d5058d9b | -7.2933 | -60.5905 | 2026-08-30 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 190.7 |
| a643530f-2b3e-377f-8b80-e7dd9d3a7ec0 | -7.211 | -44.0252 | 2026-08-30 15:00:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| af109cc7-50cb-3b83-9f66-a2014300febf | -10.8253 | -45.3152 | 2026-08-30 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 434cca36-33d4-399a-8126-819542e2a853 | -16.2735 | -42.5653 | 2026-08-30 15:00:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 177.7 |
| ebc47412-a335-3693-8b70-2026a7229d68 | -7.0998 | -42.2283 | 2026-08-30 15:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| c89c7886-8b42-378e-999e-a12914f2beeb | -10.7641 | -50.7005 | 2026-08-30 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 242.8 |
| df6a2784-aeea-36ab-b703-33d068462528 | -12.2468 | -50.577 | 2026-08-30 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |


[Clique aqui para ver as próximas entradas](README89.md)
