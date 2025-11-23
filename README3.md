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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 510718c3-a063-345a-b34e-0feb4c4ed3dc | -2.88664 | -45.28674 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 322eb062-a3e9-3bed-9366-80dcfeb034d5 | -2.88293 | -45.26875 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fec43630-18c7-3847-95d2-3d457f2cd8a8 | -2.95994 | -45.44328 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b392b8fa-aba2-30a4-9e54-d0358201997a | -2.95409 | -40.55182 | 2025-11-23 03:34:00 | NOAA-20 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 56f9cd89-f528-395c-ae92-c9fb47549ad1 | -2.89224 | -45.29361 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 7ba69633-e14f-39cd-8d60-d5e37d3e85af | -2.89881 | -45.29483 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5e6bc50c-dc16-36a8-a573-0583cf159b15 | -2.94667 | -45.44104 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| abff9934-a73e-3b5e-b015-d36a89fd1994 | -2.9007 | -45.28359 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 50c169c7-d1a6-3d8f-b638-c694f9c7d9bd | -2.87637 | -45.26754 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b313768-509a-3b90-bb4d-0d8d69007fd3 | -2.87445 | -45.2788 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 0b8d2fb4-6c61-3707-9d05-b6f3ea08591d | -2.85459 | -45.31571 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5b81af6d-3928-3710-b804-160d89f6fcca | -2.88854 | -45.27552 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 5c167bfd-8b64-3a54-b443-8c913e7347bf | -2.87253 | -45.29005 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| c5d2d449-04c3-3c07-8fc4-61468018781a | -2.92022 | -40.2794 | 2025-11-23 03:34:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e0f06271-2485-3f9b-823d-fa22e5cb415e | -2.89414 | -45.28238 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 95.3 |
| c079d380-2e55-3d74-81a4-b8f201449478 | -2.89782 | -45.29156 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3001c59c-5001-377f-906f-11f370b6ed04 | -2.88568 | -45.29235 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 125.2 |
| f3e9713a-dd3e-35d0-8a17-22b3e0737ba2 | -2.89975 | -45.28923 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 08fc91cf-c960-30b6-9dff-67285544ec27 | -2.95331 | -45.44211 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0f5e380a-bb49-3256-8904-e20f03039e3e | -2.89319 | -45.288 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 6605db89-f363-3fb1-b723-80cd37ef5b87 | -10.26939 | -36.31463 | 2025-11-23 03:36:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aab8ab0b-072a-3d03-a750-b2dd9225d326 | -4.59645 | -43.2907 | 2025-11-23 03:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a337d889-7896-3eaf-97f9-e3330cc06874 | -3.42957 | -45.2699 | 2025-11-23 03:36:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5e73f9f-a6a7-3268-813e-cd4fd3100e65 | -6.90635 | -39.8749 | 2025-11-23 03:36:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ad780394-f47b-3ded-8c8c-c2f569b719a3 | -7.47697 | -38.95623 | 2025-11-23 03:36:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 9d1d72db-64be-328a-9c22-23cbb1f6a5f2 | -3.57306 | -43.37466 | 2025-11-23 03:36:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec92e68d-fab6-3c83-abd9-e2d6e3d767f2 | -4.60146 | -43.29538 | 2025-11-23 03:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a65654d3-2e9c-39ec-8454-6fa3dd06529e | -4.039 | -42.51925 | 2025-11-23 03:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| eefb1714-9b6e-3146-a6fc-d2bd5958ae96 | -7.25494 | -39.43299 | 2025-11-23 03:36:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d63d4e5a-80e1-38a1-8140-6262bfa29f56 | -4.04443 | -42.52016 | 2025-11-23 03:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 71b645ef-1e71-3ab4-9772-ebb209be966c | -3.40933 | -43.14814 | 2025-11-23 03:36:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8368acae-bc4a-38ef-b66c-9027706d3a74 | -3.5736 | -44.73022 | 2025-11-23 03:36:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8b4a423-df8c-3ae1-8fae-73d553ffed4c | -4.74677 | -40.9271 | 2025-11-23 03:36:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9548e6db-5766-3b5b-8b46-9074b1dc99c3 | -7.40728 | -40.06306 | 2025-11-23 03:36:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 3bbc23cf-f530-31bd-b320-90b26932976e | -4.71361 | -46.46427 | 2025-11-23 03:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a7ece0d1-a98e-38f1-96cd-f26db40ebbdb | -4.60343 | -43.28401 | 2025-11-23 03:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e3a5613b-9948-31ca-a8f4-7e6c2faab9e4 | -3.42862 | -45.27546 | 2025-11-23 03:36:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88245996-eec1-3550-9dff-bd602eb8d41b | -8.71555 | -38.3467 | 2025-11-23 03:36:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 93e10cd2-e337-3798-baee-701f3d0818b3 | -7.40222 | -40.06648 | 2025-11-23 03:36:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0f394484-dc5f-3393-bb1c-f15165f78401 | -7.40295 | -40.06229 | 2025-11-23 03:36:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b0ada0a7-e697-3ca5-ade3-ad23d014f117 | -7.40655 | -40.06725 | 2025-11-23 03:36:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9692625d-caba-3a51-99ab-1230e3d1faea | -6.1163 | -39.5226 | 2025-11-23 03:36:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ce47008-071e-37e2-a168-cf23ba1ce787 | -4.71243 | -46.47091 | 2025-11-23 03:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6ebacb0c-a8f7-3d05-96c4-8a34494d920f | -3.28528 | -45.73206 | 2025-11-23 03:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bdd03e4-3cfc-37f3-b966-91c279d4eb58 | -4.0432 | -42.52722 | 2025-11-23 03:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| b6a2de70-c1ea-3bc2-9fd2-9d112842ca33 | -5.61877 | -35.37288 | 2025-11-23 03:36:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 169f8f1b-4403-33e5-b4d4-821906bb48d7 | -4.59711 | -43.28687 | 2025-11-23 03:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b72b01ba-24b0-3eee-833f-b12b99eee4c4 | -4.16844 | -44.22266 | 2025-11-23 03:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdab8307-e0a7-3646-b28f-25f78fe281a8 | -5.54338 | -41.0413 | 2025-11-23 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| c363b285-80d2-3452-ae57-92fd1ecd690c | -5.62219 | -35.37343 | 2025-11-23 03:36:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fd00dcb3-ddb4-345c-98c6-a0ca9cccb7b4 | -4.16919 | -44.21827 | 2025-11-23 03:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 726ed635-0102-324d-8567-c53e223ad3e9 | -4.04715 | -42.52715 | 2025-11-23 03:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 78a81f84-01c2-3f78-a18a-1ffcb8ef5bfb | -4.03777 | -42.52631 | 2025-11-23 03:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 4be417c2-cb00-30fd-99eb-aa3186aa4f31 | -4.60277 | -43.28783 | 2025-11-23 03:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fef585f3-cfe2-3b63-a345-54e6bfa8b105 | -5.97924 | -40.38672 | 2025-11-23 03:36:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 8b9f8fae-9db4-3b7c-a19f-9626a9d7e0da | -7.47637 | -38.95974 | 2025-11-23 03:36:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 1060f119-2390-3aef-ac57-c5ea37e3762c | -6.71804 | -39.68195 | 2025-11-23 03:36:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 16ee932c-a8da-3766-bed5-b80e18d2a5ab | -3.86632 | -40.64328 | 2025-11-23 03:36:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 9f21ca36-63d6-3275-ab8b-73d3d9db02e2 | -4.74781 | -40.92496 | 2025-11-23 03:36:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a45c12e8-776c-3cbd-9972-599a2044b036 | -3.57005 | -44.73102 | 2025-11-23 03:36:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa4cf864-514c-38a5-a9f7-509a5cd457d9 | -6.07508 | -38.47405 | 2025-11-23 03:36:00 | NOAA-20 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| af36d0f3-6d68-37df-a747-49cedcb4c15b | -4.71391 | -46.46437 | 2025-11-23 03:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e6675be2-c861-3051-bdba-f8bbc9bfc275 | -6.84666 | -35.11174 | 2025-11-23 03:36:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6bae30b5-7f29-328e-a4b8-ab33a638e8de | -4.03689 | -42.52175 | 2025-11-23 03:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a01cd8a8-c629-3d7b-92a0-60ef367610a9 | -4.04382 | -42.52368 | 2025-11-23 03:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f093920f-3be9-3155-a99f-eb28971b1577 | -6.72231 | -39.68275 | 2025-11-23 03:36:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 700499ff-081e-36a9-80f2-ae5dc79a3d35 | -4.60211 | -43.2916 | 2025-11-23 03:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0ae55bcf-93a0-3b1a-af8b-39eeb8d3a899 | -4.46039 | -44.10781 | 2025-11-23 03:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19ab40ed-0c42-3a0f-a6c0-3033b0e570eb | -5.70052 | -37.94573 | 2025-11-23 03:36:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 215d043c-528c-3770-9e39-f37f37dd1aa6 | -6.83614 | -39.01485 | 2025-11-23 03:36:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b9d98937-5c75-3c92-95b8-f601bdbf0dbe | -4.58515 | -39.97552 | 2025-11-23 03:36:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a88d12c2-7173-3e5a-87db-e468121572d2 | -6.76504 | -37.84914 | 2025-11-23 03:36:00 | NOAA-20 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 03d6b748-e78d-3ee2-8233-aee9e70f7d25 | -4.0363 | -42.52529 | 2025-11-23 03:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dca2ca94-6201-36c3-8157-edd5ead59e4a | -5.6262 | -35.37027 | 2025-11-23 03:36:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f018b80b-d644-3bb8-a62d-208184040e41 | -6.07905 | -38.4748 | 2025-11-23 03:36:00 | NOAA-20 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0e4c9de1-281d-383c-b733-05ae5e9f0551 | -3.56805 | -43.37019 | 2025-11-23 03:36:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3f44c86-9fa6-30bf-b85a-6ccf8456f650 | -3.41504 | -43.14912 | 2025-11-23 03:36:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 057475c5-88e4-325b-9106-9cb90301506c | -3.56728 | -43.37366 | 2025-11-23 03:36:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a5644fd-470b-37da-912b-3ac4948866c7 | -5.98002 | -40.38208 | 2025-11-23 03:36:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 06e3d8d3-66be-3551-91e3-5169f4af6672 | -5.70441 | -37.94628 | 2025-11-23 03:36:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a023f62-bf8e-3a8d-982b-09d8f92bd66b | -5.97471 | -40.38584 | 2025-11-23 03:36:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5002aa2a-dc15-3a85-9a75-6603ab73ca50 | -10.2734 | -36.31149 | 2025-11-23 03:36:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1465b0a1-9acf-355c-9345-805cda2a259c | -7.41522 | -40.06879 | 2025-11-23 03:36:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cf4f8300-0c11-3f58-b4b8-37095a2b4e12 | -4.0429 | -42.51915 | 2025-11-23 03:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a053a317-30d3-3ea5-a8d5-769ae407e038 | -7.2543 | -39.43679 | 2025-11-23 03:36:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a4d8338d-1108-3f74-b4cc-ded910421639 | -4.04924 | -42.52459 | 2025-11-23 03:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0fc69b67-8db9-36ae-8786-8eca4038ebd3 | -3.29198 | -45.7333 | 2025-11-23 03:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0912974-4a4b-3ab8-a84e-77ea133f76d9 | -7.41088 | -40.06801 | 2025-11-23 03:36:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 2e7141ae-7f0d-37dc-8ec9-332b679a1c25 | -4.45444 | -44.10668 | 2025-11-23 03:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7c793b1-9b50-3ed2-8a4e-39b7486d2d35 | -7.56137 | -43.63872 | 2025-11-23 03:36:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a211e2bc-df32-3c5b-aba7-1ffbc344e6f8 | -5.35373 | -40.60107 | 2025-11-23 03:36:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fa4bb357-d43a-3ecc-8076-83a2a1d0aecf | -4.71268 | -46.47099 | 2025-11-23 03:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dfe7d67b-a8fb-3c2f-a66a-b0bbdd76a7e3 | -4.04774 | -42.5236 | 2025-11-23 03:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9d47c552-3288-3149-83de-02ca595b498d | -4.03839 | -42.52277 | 2025-11-23 03:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| decd6fce-6ec9-3a08-9f1f-5d404fd51943 | -4.04231 | -42.52269 | 2025-11-23 03:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6c8fe07c-2969-335f-ae9f-2ba204707b7c | -4.04172 | -42.52622 | 2025-11-23 03:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e9d8d656-231f-3b2c-ab1a-31b216313983 | -5.21799 | -41.07748 | 2025-11-23 03:36:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a1551ef3-bd5a-37ba-94ad-b0157db85f74 | -6.72164 | -39.68665 | 2025-11-23 03:36:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eb41b43d-d900-30e3-97d9-0bd6323652d1 | -20.34326 | -41.74081 | 2025-11-23 03:40:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ceeb9dc4-f32e-39c1-a509-bc763b70e39e | -22.20512 | -41.5927 | 2025-11-23 03:40:00 | NOAA-20 | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
