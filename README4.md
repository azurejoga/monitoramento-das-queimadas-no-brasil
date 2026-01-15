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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a902007-be6d-3c3f-a4ef-b257b0c231ce | -8.1518 | -43.186 | 2026-01-15 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6b89c3af-c231-3c56-9f3b-f6e8811d3683 | -9.21496 | -36.64771 | 2026-01-15 03:44:00 | NOAA-20 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 557141d9-d6f3-3973-bf84-34218148ff61 | -11.66333 | -43.77099 | 2026-01-15 03:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac28499b-7ff2-3483-a09a-5c66871cd1a2 | -5.26215 | -44.73679 | 2026-01-15 03:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7129929-5a15-3cc5-bcaf-cb8b03f99d07 | -10.34629 | -44.8276 | 2026-01-15 03:44:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5cdfd57-4e47-30fb-9cb9-b26fd20ad290 | -8.4277 | -44.0234 | 2026-01-15 03:44:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3ffb25c1-bf37-37f7-afba-72faf405581b | -10.58915 | -44.96856 | 2026-01-15 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf4f9685-2a91-32f9-8772-bef04c052cc8 | -7.23942 | -43.05567 | 2026-01-15 03:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 523d4ffd-6a90-3536-9728-e71ba319e177 | -10.34063 | -44.82971 | 2026-01-15 03:44:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e43d06ed-728b-3882-bcbf-c244b3798221 | -8.42775 | -44.02246 | 2026-01-15 03:44:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d88aeb8-91aa-3825-b37b-6547bba8662f | -6.85989 | -41.47025 | 2026-01-15 03:44:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 36b73161-7b61-32b3-bdf4-810a3a453af9 | -10.34805 | -44.82947 | 2026-01-15 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e765761d-08c5-3684-a955-9aa44b0b2044 | -8.42677 | -44.02801 | 2026-01-15 03:44:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 959ac666-0cab-3b8e-a87f-87a5c2464eb7 | -5.25661 | -44.73597 | 2026-01-15 03:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 965e5931-97f1-3526-8f2b-0a158178ca1d | -10.48776 | -44.93122 | 2026-01-15 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61c6694b-2471-3531-bd49-47a52ef16a7d | -11.86456 | -37.60262 | 2026-01-15 03:44:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| da4d6d9c-f649-3c86-b7b2-3ca636425d21 | -7.50274 | -38.81778 | 2026-01-15 03:44:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7598bf21-d414-3c9b-a1c0-7198fbcc9968 | -7.86124 | -39.09616 | 2026-01-15 03:44:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4754c897-b2d4-39d6-98e8-9192883b0e53 | -7.87095 | -41.59988 | 2026-01-15 03:44:00 | NOAA-20 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b25b3d0a-fac2-3d10-be80-4029a752b3dd | -10.48264 | -44.93035 | 2026-01-15 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 882b6e25-7d6a-3d99-9887-d7d3a00797f3 | -7.988 | -43.38773 | 2026-01-15 03:44:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6082e61-24a0-38f7-a650-a4fe2670f881 | -7.04609 | -43.95298 | 2026-01-15 03:44:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44a967e1-1cf2-3eaa-9a98-22be67fe355a | -10.67123 | -39.19233 | 2026-01-15 03:44:00 | NOAA-20 | QUIJINGUE | BAHIA | Brasil | 2925907 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 837b043f-6702-3eef-9027-73f9e7a016e9 | -10.34121 | -44.82667 | 2026-01-15 03:44:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 715620ac-8703-3fbb-bbf0-308368b0aef7 | -9.38013 | -36.91039 | 2026-01-15 03:44:00 | NOAA-20 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8aadb5f0-8fe0-3749-8edb-f243b7b1ee84 | -8.15122 | -43.18422 | 2026-01-15 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 75350b61-acb0-3877-bacd-2aca7b45fc43 | -7.2299 | -43.05399 | 2026-01-15 03:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 963cb366-f712-355a-9cca-a801bb38a141 | -9.0077 | -39.86246 | 2026-01-15 03:44:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d3a6d7c1-d877-3005-b8cd-27bb673f04ba | -8.42279 | -44.02143 | 2026-01-15 03:44:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57912190-f1cf-3af2-a1aa-7ea93fbf50d3 | -12.31438 | -44.54164 | 2026-01-15 03:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 626684c7-a83c-335a-860b-d631bf6fc532 | -14.40224 | -44.58673 | 2026-01-15 03:46:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8699fcbf-f085-353b-a566-a961afae09e6 | -12.09071 | -45.29915 | 2026-01-15 03:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d87e801-6c81-3a1d-bba2-a0bf8b567eeb | -20.36181 | -41.72914 | 2026-01-15 03:46:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b6d580a8-6e9d-3e85-98f0-80d2ac300624 | -13.54032 | -43.63311 | 2026-01-15 03:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46651025-00dd-31a3-a20b-5106a9c90226 | -14.16728 | -43.72075 | 2026-01-15 03:46:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 192e2bd6-44db-3842-8fbc-03727c5fa430 | -12.51012 | -43.68273 | 2026-01-15 03:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c757fffb-a54d-3acd-b1a5-82ba88fee074 | -12.5138 | -43.68832 | 2026-01-15 03:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0095f00c-237e-3287-9f16-024b7d5174b0 | -14.40526 | -44.58394 | 2026-01-15 03:46:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11a1c187-6fa7-3a8b-9954-a40b3e2b618a | -16.24711 | -42.23506 | 2026-01-15 03:46:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b78b5efb-c184-348d-9cef-c9d5cdec2158 | -14.14471 | -42.75874 | 2026-01-15 03:46:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e4854a2e-a65b-3d92-9c62-9e1b90b6bfb4 | -12.09015 | -45.30214 | 2026-01-15 03:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5387c0ee-736c-34ca-91bf-0c1e92860bb8 | -12.08832 | -45.29937 | 2026-01-15 03:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79181a50-bdb6-34b2-b94f-e12e07ad15ab | -12.09008 | -45.29028 | 2026-01-15 03:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99de0364-f7d0-3550-b2c3-a780016d9801 | -13.74294 | -43.66362 | 2026-01-15 03:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3e9c251-29dc-32dc-b07b-b215b83e776b | -12.08677 | -45.29209 | 2026-01-15 03:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7dae155-105b-304e-8010-1fbbfb4f5f15 | -16.24825 | -42.23243 | 2026-01-15 03:46:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3c356a98-85b3-3755-8341-7279a6ae6cd2 | -12.51152 | -43.67977 | 2026-01-15 03:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee019d93-063f-3c70-9fff-3f807097b886 | -12.12591 | -45.5746 | 2026-01-15 03:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5519f72f-b8cc-3a07-9c10-48bab320cd82 | -13.60362 | -43.56258 | 2026-01-15 03:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 75bfd19a-8edc-32dd-bb4e-9478e60ca081 | -12.51096 | -43.67805 | 2026-01-15 03:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c1e50d4-254f-3ebb-9f12-e5539896497b | -14.76332 | -45.92633 | 2026-01-15 03:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 370844b7-8bc4-3a1b-932b-941e5210cad8 | -12.08795 | -45.57673 | 2026-01-15 03:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57e0b888-c5ee-3680-9f5b-27eef89533a9 | -12.66095 | -46.76344 | 2026-01-15 03:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e82b22fa-440b-38e3-968b-d5f01b41c949 | -12.33467 | -43.68944 | 2026-01-15 03:46:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2e9deff-3040-3a1f-9aec-2a99bf84ae14 | -12.50247 | -43.67801 | 2026-01-15 03:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 457d5020-0472-3a63-aba4-240e26d181e0 | -12.09068 | -45.28724 | 2026-01-15 03:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3243dc85-e9a5-3f86-983a-df00ec71c9a6 | -12.66022 | -46.76719 | 2026-01-15 03:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69534525-acc0-3a06-a1a8-c1a15d94c8d3 | -12.0889 | -45.29638 | 2026-01-15 03:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 346f392a-66a6-377f-bc33-fc32ba6f9ca6 | -12.08773 | -45.30236 | 2026-01-15 03:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7340d57-3ee6-3175-ae9a-daa2648ac432 | -12.08734 | -45.57991 | 2026-01-15 03:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 051d03cf-ac4e-3544-83e1-096b34956fc1 | -14.40429 | -44.58896 | 2026-01-15 03:46:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce080a33-f250-319b-abca-a575b423a613 | -14.17168 | -43.72162 | 2026-01-15 03:46:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc70076e-2ff6-32ed-8c67-16b84871e3f4 | -12.65468 | -46.76609 | 2026-01-15 03:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dec12963-da9a-37e8-8ea2-18e685ab956c | -12.12471 | -45.58093 | 2026-01-15 03:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7caf99c-c707-352c-832f-704022021f2e | -14.4069 | -44.5876 | 2026-01-15 03:46:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 395f3474-3a97-38a4-9908-da1a748b4cd0 | -12.51429 | -43.69001 | 2026-01-15 03:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc2815f8-867c-3269-8309-bbbd47c12a4d | -12.08734 | -45.28901 | 2026-01-15 03:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8efd360-e3ac-37ef-a044-5250aa551fc1 | -12.51064 | -43.68444 | 2026-01-15 03:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d3e7990-99b2-3dcc-bb2d-d9d0111394de | -17.28992 | -39.22794 | 2026-01-15 03:46:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 53bc1586-20f1-3786-8bad-c1df0b8c2e8d | -12.50107 | -43.68095 | 2026-01-15 03:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a866fafd-c615-316d-b3d6-140eca1e6451 | -14.75887 | -45.92225 | 2026-01-15 03:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6e459c1-bf9f-3716-8de8-d50123797569 | -12.12531 | -45.57775 | 2026-01-15 03:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1540d40e-e10b-3106-9ede-24a1fc7aa0ab | -12.50191 | -43.67627 | 2026-01-15 03:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5d767e6-fd04-333d-bcc4-f61f69500d72 | -12.1265 | -45.57147 | 2026-01-15 03:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8aa26de-c250-3163-be3e-4da8bdf4e54f | -22.72865 | -42.82149 | 2026-01-15 03:49:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f2c835de-915e-34ba-8460-eac1910087cc | -20.83815 | -51.74202 | 2026-01-15 03:49:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cfeb15ac-55b6-30ed-a8b4-5330f2d0d866 | -22.86797 | -43.08674 | 2026-01-15 03:49:00 | NOAA-20 | NITERÓI | RIO DE JANEIRO | Brasil | 3303302 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8ccd2b66-8f91-3566-8977-96704bcf9ab1 | -20.84447 | -51.74378 | 2026-01-15 03:49:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 38a83013-9cff-3248-b376-58fd64762bbd | -4.372 | -37.8918 | 2026-01-15 03:50:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 67162925-f437-3e16-8be5-f7f518dfe07b | -4.372 | -37.8918 | 2026-01-15 04:00:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 81.5 |
| d9d33683-47e8-351d-8bd7-f3b292d21cf8 | -5.44547 | -35.6115 | 2026-01-15 04:31:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6ab3bda1-9634-33d1-bb8a-5f2024c0d4d5 | -3.47648 | -43.33616 | 2026-01-15 04:31:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da52fb01-b6f1-3f47-894c-270c4e313b23 | -4.3709 | -37.90564 | 2026-01-15 04:31:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 9afb0570-4c27-3f6d-9334-153d74d5a6c2 | -0.09065 | -51.27904 | 2026-01-15 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8303c58a-3002-396f-8860-d5f0e64fcae0 | -3.11781 | -40.16101 | 2026-01-15 04:31:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74506459-f414-39eb-98fb-cfb374256981 | -2.93268 | -48.23042 | 2026-01-15 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45f92a0b-ee22-3fcb-8665-ed38fe507608 | -5.45187 | -35.61239 | 2026-01-15 04:31:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fd2e430c-cee6-3f44-b4fc-e8964bd736d1 | -3.23308 | -41.80263 | 2026-01-15 04:31:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a5d4e81d-6826-3972-a945-96346d79ec9e | -2.45628 | -46.90797 | 2026-01-15 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43c30be8-ecc1-3448-9c06-f9f1945c8e33 | -2.26479 | -47.8683 | 2026-01-15 04:31:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a483b47e-6be9-3e3b-949f-4023a5422744 | -5.46661 | -35.55197 | 2026-01-15 04:31:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 7.4 |
| ef0f0c29-dc79-3667-aaf0-e0e98c164762 | -2.86736 | -45.53708 | 2026-01-15 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00ac2aa8-7146-38ff-a970-164bdbc63a4f | -5.46618 | -35.5575 | 2026-01-15 04:31:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8e29c7a5-d89e-3714-ac92-28af7221227b | -4.37196 | -37.89838 | 2026-01-15 04:31:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 5884c63e-0ddc-3cb9-bb0c-5406b04dd2c7 | -3.31463 | -41.86739 | 2026-01-15 04:31:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 3c1c6894-5caf-359a-bcce-cf52008f15e3 | -4.37143 | -37.90201 | 2026-01-15 04:31:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 881f983f-2cc8-345a-a148-0811d8db628d | -5.45197 | -35.61233 | 2026-01-15 04:31:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9933459b-7cd1-3d5f-8bf5-2af5c167473b | -0.90558 | -47.55185 | 2026-01-15 04:31:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83656b25-6437-39af-b214-a627b82a018d | -1.05364 | -47.26007 | 2026-01-15 04:31:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6ffa678-0771-313e-9fad-c953f49dd384 | -1.89511 | -48.29192 | 2026-01-15 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README5.md)
