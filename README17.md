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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d31cd12-220d-36aa-a235-ceb650825bff | -8.4858 | -54.7023 | 2026-09-02 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 3fee7841-fd8f-33bc-b2fd-71fc3e6a0d3d | -8.4485 | -54.7048 | 2026-09-02 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 847fc77d-f1a7-3665-ab2d-a51a72d03871 | -8.4298 | -54.706 | 2026-09-02 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 2eac18c2-5d3b-34c6-a27e-fb2587f89ba3 | -8.4671 | -54.7035 | 2026-09-02 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 81a1dd44-6704-3a82-ae79-e961e2fb3609 | -11.6783 | -54.5689 | 2026-09-02 03:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 797639dd-4317-3ee8-8b2d-3d38ec967879 | -8.4669 | -54.7237 | 2026-09-02 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 7fa5d2c7-c364-39e1-9f46-6a30ca18e46b | -11.6624 | -50.1954 | 2026-09-02 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| df4005c0-bed7-3f0c-8855-bc3952fb8b3c | -4.3587 | -47.7853 | 2026-09-02 03:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 4105c883-205e-35bf-bf3c-170f0f79bc52 | -6.6764 | -58.7686 | 2026-09-02 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| fa8c65d7-32fa-39da-bdbb-2f5e55f3d1c2 | -19.55253 | -40.62256 | 2026-09-02 03:40:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d3a2b845-97a7-311f-bd4a-5490f344e06e | -19.54853 | -40.62165 | 2026-09-02 03:40:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3a861fbe-170c-3c53-a6e7-7b93e6f296a5 | -19.20626 | -43.18437 | 2026-09-02 03:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ca321cc6-b3b9-349b-b5ee-125b8ff9a2d9 | -19.20659 | -43.18315 | 2026-09-02 03:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a0d5f94b-bb57-321d-b0c7-08d1cefcc7f7 | -4.3587 | -47.7853 | 2026-09-02 03:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 93b00bcc-6c9c-348e-b335-ba791e814fec | -10.4804 | -64.3313 | 2026-09-02 04:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 849730de-f1dc-3761-9ced-17ec6cc24886 | -3.23 | -47.2445 | 2026-09-02 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| c944190a-04d6-318a-b5b2-c3a2be140108 | -4.3587 | -47.7853 | 2026-09-02 04:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 15d5b73a-7122-3ac1-8dbb-ecdd9ef00ce3 | -10.9 | -45.35 | 2026-09-02 04:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e80d7675-6253-3483-ae9c-588b11d9651c | -5.45418 | -42.66125 | 2026-09-02 04:19:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c5f8e1d4-580f-36fc-8ddf-4e77befd7cb4 | -4.46756 | -38.50819 | 2026-09-02 04:19:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8561414f-44db-3116-bf3e-4dd95210c837 | -4.37281 | -39.55498 | 2026-09-02 04:19:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4c9a86d5-8130-3814-a43c-a518c3711c78 | -2.50159 | -48.1357 | 2026-09-02 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38c38d89-ea97-3151-8b2b-a5633241a871 | -6.14339 | -55.6675 | 2026-09-02 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edd01f13-d2b9-385c-8566-4cc898c33e6d | -6.83583 | -41.68981 | 2026-09-02 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aff3f13b-3dde-361f-98b9-8a3f462b32f2 | -6.78313 | -42.74998 | 2026-09-02 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 95dd2e89-3ba1-3173-92a1-89381cb90f15 | -6.05282 | -53.83663 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f2b146a-0c72-34a3-b583-6dd7be14a0b9 | -4.36652 | -47.76797 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 200b8137-aad9-39c0-b592-9525309ae03d | -6.64187 | -51.87236 | 2026-09-02 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 104bd849-3f4a-390b-a694-863a29ca8419 | -1.5104 | -54.96186 | 2026-09-02 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 071c0b23-9e56-3909-8324-84b912afa061 | -4.3681 | -47.78133 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d7fd3e6-8f32-32d2-971e-1af628c9ae79 | -5.97363 | -53.58162 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b8ff7ed-f929-3036-a02a-9a17b20ab33b | -3.37589 | -49.51328 | 2026-09-02 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a23ecd5d-a068-3b0c-ae1a-5c520a36a044 | -6.83344 | -41.68096 | 2026-09-02 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 252932d6-9850-3e63-8551-cd77c24fbf22 | -4.37018 | -47.76853 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b814bfb-4646-3288-bfd0-7e5f1b2a1d11 | -6.07158 | -53.66967 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05e5af4c-ae26-3c8c-84c3-553e2674270c | -4.9153 | -48.99457 | 2026-09-02 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67a9571d-3b07-32b0-9919-1e98f906a5be | -6.32077 | -54.75491 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ec35870-c2aa-3ec4-a6d7-8ecd8cd8f2a6 | -6.57706 | -44.78476 | 2026-09-02 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc9ca778-aede-31a0-846c-ce21ff9325c4 | -7.14353 | -45.81332 | 2026-09-02 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87420769-4161-3de6-b327-a3a7c124906a | -7.65838 | -45.87059 | 2026-09-02 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 186fc01f-4c93-3ad5-ab71-25b34a921b17 | -1.59032 | -50.43459 | 2026-09-02 04:19:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a4c87b6-e8b9-39fe-a0df-20b7fbb62e32 | -5.25173 | -55.90926 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad729e99-d64b-3d05-a499-56f910cc6f83 | -4.3608 | -47.78018 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdbc93ed-ab77-385b-bd8c-8a7b65cbf9e9 | -4.94738 | -47.65522 | 2026-09-02 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e9525ba-b2bb-3b74-89f4-95813f432399 | -2.00046 | -47.25143 | 2026-09-02 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f6bc9b7-dbec-3788-a628-450b013d2086 | -4.18184 | -49.40469 | 2026-09-02 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e822c58f-37cd-3e1b-a036-2c1a09dcf9f0 | -4.36011 | -47.7844 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf476ad3-64cf-30d8-a9ad-4a0ad5bf2c79 | -6.20568 | -53.48234 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57ceab2e-35e7-3655-b3cc-c1a42abc4775 | -5.97885 | -53.58247 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 018b1ccc-82cd-37f1-8d7b-c36cd0974682 | -4.116 | -51.02731 | 2026-09-02 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 23b30964-3617-3f21-9541-d1c505f722d7 | -6.7728 | -41.17391 | 2026-09-02 04:19:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2ac87d29-a96f-3c8d-b140-9adebfa07070 | -6.14847 | -55.67329 | 2026-09-02 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30bb45e9-75e7-3548-ad8d-8c3fd46309c8 | -3.24165 | -47.25443 | 2026-09-02 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| c2b27f8b-f2bc-35ad-998b-7e76d1e601e4 | -5.97251 | -53.58795 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bde7e5de-96a7-3ae6-b91b-773ecf627eb8 | -4.99562 | -37.10138 | 2026-09-02 04:19:00 | NOAA-21 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 90f0117e-fcb2-302e-8b09-0649eda84469 | -6.31672 | -54.75477 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9ee02d0-3366-3a93-8723-58efeab0c7c4 | -5.25076 | -55.91412 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e312bc12-2e21-3eb5-a277-8a4f4fca89c9 | -4.5829 | -48.29539 | 2026-09-02 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e20ee7e6-1bea-338d-a4ad-2e7f2877b1f7 | -7.65341 | -45.88057 | 2026-09-02 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f9ef388d-32df-3c05-94c3-dae0de95b530 | -5.25157 | -55.90943 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3227b957-bc75-3411-9138-d3af26ebd786 | -6.67828 | -46.1706 | 2026-09-02 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24a5a721-b034-3899-81dc-fe652f28ee3d | -5.7989 | -52.05337 | 2026-09-02 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| abe12c5b-fbee-30d4-94af-d1251b23f74e | -6.04525 | -53.84861 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 115d7a01-baf1-329f-8727-a6e63ff4b7f5 | -7.65673 | -45.8811 | 2026-09-02 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 92d664f9-514c-3bab-95a2-cff9988aed79 | -6.83946 | -41.69033 | 2026-09-02 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aaaaa60a-a577-3be3-b5f8-72594f23074e | -6.25919 | -55.42967 | 2026-09-02 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3db35a63-880d-369d-b7de-028bd98f16a3 | -7.65948 | -45.86361 | 2026-09-02 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92a0cd6f-9e74-3d1a-8d5a-4b9a7f06e871 | -5.85876 | -51.709 | 2026-09-02 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01de6516-a08c-338c-9c5c-c6ad67060af2 | -7.45073 | -43.81843 | 2026-09-02 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63102691-5f37-35af-96d8-291e9dc088f1 | -4.35738 | -55.03064 | 2026-09-02 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0dc2870-d8d0-3064-ac41-e97c130ccb8b | -4.37176 | -47.7819 | 2026-09-02 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 151948bb-3205-3339-88ce-d505c244ce56 | -6.67549 | -43.43943 | 2026-09-02 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a7fbf27-27b6-3911-bea3-dd334e5ea45c | -6.58698 | -44.7863 | 2026-09-02 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f88c6f29-e657-3c67-a52f-e563d2f73798 | -5.68992 | -42.72583 | 2026-09-02 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7943f859-e15c-3264-8263-a4969cbbc371 | -3.064 | -48.74717 | 2026-09-02 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6a157e51-cd67-3e4b-8797-da390c888c34 | -6.09145 | -53.8026 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfe07265-96db-3550-b3f8-e3035961bd5c | -7.9316 | -44.22704 | 2026-09-02 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5eef88e2-328c-3214-b1ee-bac65fd24391 | -6.32296 | -54.75201 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 946cfe45-86b0-3155-b284-01d408263456 | -5.86336 | -51.70971 | 2026-09-02 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14fd5589-ca7d-36de-8f0f-5c405bb51bf8 | -1.50969 | -54.96624 | 2026-09-02 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ed90109c-96a5-3420-8de0-ffcdf4a5d039 | -7.36791 | -45.05464 | 2026-09-02 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9408a26-bf46-3380-8e17-1a59ccad70e4 | -3.85382 | -44.06026 | 2026-09-02 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6a4b1d3-d015-3147-9d1d-f0d1740ce72b | -4.1205 | -51.02812 | 2026-09-02 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 10a62188-d5ad-31e5-b038-cd98242bc578 | -5.24544 | -55.90841 | 2026-09-02 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc0b9f8f-536e-331d-b72d-0ddf6363d971 | -1.99979 | -47.2557 | 2026-09-02 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13be1975-8137-3244-8479-d245653be9ed | -1.01974 | -53.72422 | 2026-09-02 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09933f2b-85c8-317a-89c0-f161f2a288a7 | -7.52773 | -47.33245 | 2026-09-02 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7927e815-ba2c-37f2-b6d7-c3ea0b9883f5 | -5.45817 | -42.65806 | 2026-09-02 04:19:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0e47446b-d0ff-34a9-923a-41df863829de | -6.08315 | -53.66518 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a14a9a70-a111-3094-a6aa-7e580df02c28 | -6.77968 | -42.74944 | 2026-09-02 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fd3a1d24-c4fd-305c-a270-803d85838226 | -3.08295 | -43.17809 | 2026-09-02 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cd6dd0f-8c51-3b45-a12b-c5fa355b48e7 | -6.80682 | -46.198 | 2026-09-02 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bc6aee7c-a3b0-3899-a684-f9ce3155cd83 | -4.4955 | -45.91118 | 2026-09-02 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| d0d1e412-826d-3be1-b231-8a2a19ddda33 | -6.2062 | -53.47926 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bf92476d-6182-354b-9870-6fe004ca4bc5 | -3.97098 | -41.51824 | 2026-09-02 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 13084006-cb18-379c-9c0d-1ec7fdc9f147 | -6.11386 | -53.44906 | 2026-09-02 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9baa537-b228-389f-a4e1-02ec0caff606 | -7.66448 | -45.87515 | 2026-09-02 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b737170f-f91f-3638-8c3d-8dc3a6bca79b | -4.7163 | -42.76483 | 2026-09-02 04:19:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c501ea15-8d40-32f1-aacf-2649ac056fb6 | -4.54631 | -46.65332 | 2026-09-02 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d607cb3a-df23-3bc1-98d3-29ddd3058a4a | -5.62195 | -42.93855 | 2026-09-02 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README18.md)
