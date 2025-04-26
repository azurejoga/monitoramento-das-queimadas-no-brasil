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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f515c6aa-eb8a-3355-9882-1181b6b83f95 | -11.3963 | -52.9477 | 2025-04-26 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 328fe52e-64ba-38fa-b986-ec510a58a2ce | -11.3965 | -52.9269 | 2025-04-26 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 751cc54d-c179-3274-ba45-6bb9db574347 | -11.4152 | -52.9458 | 2025-04-26 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| f8b98bdd-d989-319b-9f7c-5ca921abb6e0 | -11.3963 | -52.9477 | 2025-04-26 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 754d0538-a17b-3a1e-96e7-8127f96e9f79 | -11.3965 | -52.9269 | 2025-04-26 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 5117ee84-af60-3e77-b7a9-6f29718b7963 | -11.4152 | -52.9458 | 2025-04-26 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 3953a693-d6b5-3812-bba9-24f86717d24c | -11.3963 | -52.9477 | 2025-04-26 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 64f843a6-5977-3ccb-81d3-3ff27a05d438 | -11.3963 | -52.9477 | 2025-04-26 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 74aa9720-26cc-36d4-83a3-6649e5979a6b | -11.3965 | -52.9269 | 2025-04-26 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 8b5928b2-83cc-3aec-bcbf-415dfbec54f1 | -11.3965 | -52.9269 | 2025-04-26 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.6 |
| a72ec8f8-8563-39d9-ba34-285ab33bd087 | -11.3963 | -52.9477 | 2025-04-26 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| af84a3f4-e037-35c9-9eac-5ffe7dd2ca3a | -11.4152 | -52.9458 | 2025-04-26 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| be0e6f23-2247-3ccd-8c7e-1187d1722da1 | -11.4152 | -52.9458 | 2025-04-26 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 14861222-8d99-3662-8bdd-2c0480d006a0 | -11.3963 | -52.9477 | 2025-04-26 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| c9a6a698-226a-38ed-b67b-acf206749fc0 | -11.3965 | -52.9269 | 2025-04-26 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 5b587724-0052-3ae2-ad9c-65598dfd1aa2 | -11.3963 | -52.9477 | 2025-04-26 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| f6ca8c8b-6c10-3598-ac89-49777b26f0a7 | -11.4152 | -52.9458 | 2025-04-26 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| fd74d856-c96f-3089-9e55-514bcf6b2f4a | -11.3965 | -52.9269 | 2025-04-26 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6d9e2d5d-0280-3037-8b0c-3cbf533ece35 | -11.3963 | -52.9477 | 2025-04-26 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 35c43c8a-ffc5-33a0-95c4-91d01e432202 | -11.3965 | -52.9269 | 2025-04-26 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 8903976e-b97f-3d93-b6e0-1d7fded0c12c | -11.4152 | -52.9458 | 2025-04-26 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 187751c5-b1b0-37ae-982a-f9fb75cf4106 | -11.3965 | -52.9269 | 2025-04-26 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| d9b993c9-a5b0-372e-88b8-1e75070cadd3 | -11.3963 | -52.9477 | 2025-04-26 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 6884dc0e-8bb4-3496-93dc-6e853cd37aec | -5.50307 | -35.60231 | 2025-04-26 03:40:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 35c2af0a-de44-3204-a0bb-19151a884bdf | -9.56666 | -37.79588 | 2025-04-26 03:42:00 | NOAA-21 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 69c60bd7-8a00-3f30-acc0-592168bf2863 | -8.94346 | -44.23425 | 2025-04-26 03:42:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d3592ac-c973-3979-9d55-71139180de1b | -11.47582 | -37.91912 | 2025-04-26 03:42:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b35dde2c-15a6-3f4b-80b8-b0848e46d8b1 | -10.28463 | -38.60403 | 2025-04-26 03:42:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9e8a91a3-6f95-3151-9103-9fef9856a00c | -8.94289 | -44.23732 | 2025-04-26 03:42:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a705ff2e-27aa-31cb-8fb3-83cf99e0e567 | -7.44731 | -37.30185 | 2025-04-26 03:42:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0847aad7-a5cf-381c-be70-a09b5b861e72 | -9.56323 | -37.79529 | 2025-04-26 03:42:00 | NOAA-21 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2474d582-c947-33f5-9f27-db651cd61ecb | -9.7483 | -37.00202 | 2025-04-26 03:42:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5160263c-5d6c-348a-ba1a-b0f6145705b3 | -8.07385 | -34.97672 | 2025-04-26 03:42:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 84ca0e2d-aae3-3e74-918e-adaf4a4d44d7 | -10.57361 | -37.97801 | 2025-04-26 03:42:00 | NOAA-21 | ADUSTINA | BAHIA | Brasil | 2900355 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5499db51-9adf-3a6e-9aa7-375d5ea78a2b | -8.94743 | -44.24123 | 2025-04-26 03:42:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb530f9f-4796-30a3-a0d6-513f9808ea66 | -8.93985 | -44.23595 | 2025-04-26 03:42:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28672ee7-0ec5-3e13-9c7b-b30e745eda2c | -10.33497 | -37.01702 | 2025-04-26 03:42:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5592e05d-60e2-3b98-af9c-11581016ed61 | -8.9444 | -44.23992 | 2025-04-26 03:42:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9cb57317-6d49-3dab-bb7e-9bf7db174447 | -11.30415 | -40.4533 | 2025-04-26 03:42:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9d150b65-c758-320b-9f3c-eb4f841fbc50 | -8.93836 | -44.23339 | 2025-04-26 03:42:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0d72cd3-34f1-38c9-b129-342eaeec13b3 | -7.17363 | -44.87133 | 2025-04-26 03:42:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d06bc353-8f43-3a9b-8a34-4659ed9a8ab4 | -11.57775 | -37.96242 | 2025-04-26 03:42:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 66b44a2d-2558-3f3c-a086-aad7598f025a | -10.69744 | -37.05058 | 2025-04-26 03:42:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| da9b9e28-8227-3732-bf1d-b73ebfe62f2b | -9.75614 | -36.99595 | 2025-04-26 03:42:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 704fd292-8cbc-36cf-b281-cf4a9191bd01 | -9.86736 | -37.10953 | 2025-04-26 03:42:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 22d8e460-6be3-3642-b904-5f986d14bf4a | -8.94039 | -44.23289 | 2025-04-26 03:42:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f681540-064f-3427-8618-cbb8a2d8dd18 | -10.72549 | -37.6221 | 2025-04-26 03:42:00 | NOAA-21 | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2cc5d08c-6e32-3dd8-8ca2-3c4583ef6188 | -8.93779 | -44.23645 | 2025-04-26 03:42:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb27333c-0b06-3589-b332-440af03ef019 | -10.10047 | -37.62539 | 2025-04-26 03:42:00 | NOAA-21 | MONTE ALEGRE DE SERGIPE | SERGIPE | Brasil | 2804201 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| db29d013-40ae-38e7-af81-9d6a3d1283dd | -9.80311 | -37.48654 | 2025-04-26 03:42:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 86fc968f-69e3-3bef-b682-e41776db00db | -5.42263 | -43.19334 | 2025-04-26 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce662818-cfa6-331c-96da-727c1f3c32b5 | -8.94494 | -44.23684 | 2025-04-26 03:42:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98ba27e0-8086-33a6-95b7-c24c5172a77e | -8.94799 | -44.23817 | 2025-04-26 03:42:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f212828e-1ad7-3b9a-95de-a5dc25b30a55 | -7.44389 | -37.30129 | 2025-04-26 03:42:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 116637d5-2aa4-3707-acc8-a1a12f773edf | -7.23237 | -35.61657 | 2025-04-26 03:42:00 | NOAA-21 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cb4727a9-60cd-329a-9083-6ce9537029ad | -15.59656 | -41.79163 | 2025-04-26 03:45:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 12fad043-55a5-38b2-8016-d44af508fd23 | -16.28793 | -39.87799 | 2025-04-26 03:45:00 | NOAA-21 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b69d2c39-ed74-3d68-b815-cf14b386636e | -15.60041 | -41.79245 | 2025-04-26 03:45:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 2193f013-7d12-36d8-997f-75372758244c | -12.56612 | -45.35778 | 2025-04-26 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d1d6153-efa6-39cc-9d0c-115f01fe132c | -13.65714 | -43.79121 | 2025-04-26 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ce0181c-5df3-3333-8aa4-46df2c3f47d0 | -16.6806 | -43.88491 | 2025-04-26 03:45:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27af8b34-7931-34e1-a4c9-5c8fe11c3646 | -17.27236 | -41.8611 | 2025-04-26 03:45:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e5eed606-9660-3dc4-8bad-1599588e01f3 | -13.667 | -43.78877 | 2025-04-26 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fc89d689-42c2-34cc-adc8-d37c83417f39 | -16.81607 | -41.22389 | 2025-04-26 03:45:00 | NOAA-21 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 312278d2-cf50-3f01-a713-dbf0eeb0f640 | -14.19539 | -44.35535 | 2025-04-26 03:45:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80a6be7c-8a92-3c33-acef-989913514155 | -11.9669 | -44.00675 | 2025-04-26 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a8ef57f-c528-3eb0-a461-da1da4408231 | -12.55522 | -45.35899 | 2025-04-26 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03048027-5dde-3dde-9343-d88468057d27 | -15.79374 | -41.2782 | 2025-04-26 03:45:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c911e88d-eb53-38aa-8347-3d303d878a87 | -17.75328 | -42.89619 | 2025-04-26 03:45:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad4c844b-14a8-3a9d-a252-9a92c830c807 | -17.74927 | -42.89548 | 2025-04-26 03:45:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef3e6293-c31a-3c39-b6f6-9bdd749f2f21 | -15.59566 | -41.7966 | 2025-04-26 03:45:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 881f5a0c-5965-3c1a-b86c-f1a9bb115c31 | -13.66164 | -43.79231 | 2025-04-26 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 739a2b48-974b-36e5-a307-05d22a31fd54 | -17.53533 | -40.0498 | 2025-04-26 03:45:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3f1d359f-41d9-3928-8126-a42a9dc0ad72 | -12.56037 | -45.35995 | 2025-04-26 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f81232a-87a0-3b1d-83d2-eb4313bcfeb6 | -29.80985 | -51.34793 | 2025-04-26 03:47:00 | NOAA-21 | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 833fb99c-9565-3fa9-b8af-8d1a35208990 | -29.80868 | -51.34728 | 2025-04-26 03:47:00 | NOAA-21 | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| d78f689f-cc2c-3d23-85e5-fe14f45fd531 | -28.20422 | -48.70451 | 2025-04-26 03:49:00 | NOAA-21 | IMBITUBA | SANTA CATARINA | Brasil | 4207304 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 28e5808e-6aef-3418-b605-2733550cc550 | -28.06162 | -48.67325 | 2025-04-26 03:49:00 | NOAA-21 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 788abbeb-9c43-3a30-9738-39e766e2df5c | -11.3963 | -52.9477 | 2025-04-26 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| e65eed2b-4536-30ee-859a-8f114b062ce5 | -11.3965 | -52.9269 | 2025-04-26 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 9e91c0d8-7491-3848-acd8-53a334076a67 | -11.3965 | -52.9269 | 2025-04-26 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 675a69cb-86d3-3c22-bf42-02821a34e485 | -11.3963 | -52.9477 | 2025-04-26 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 78ee773f-75e9-3e98-b987-a945b573bc70 | -8.93874 | -44.234 | 2025-04-26 04:08:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66c89e8a-1f25-396b-baf7-545f7c800e31 | -7.17526 | -44.87304 | 2025-04-26 04:08:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5ceaf34-af7b-3d08-9498-135af5a996a4 | -10.34966 | -37.97962 | 2025-04-26 04:08:00 | NPP-375D | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9701d18b-471f-3c56-ad1f-99bcb55e0550 | -8.94158 | -44.23839 | 2025-04-26 04:08:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 618c1b82-ff70-31b7-8db3-d1cf91760d5d | -8.07315 | -34.97614 | 2025-04-26 04:08:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0401d6e9-6e14-36a6-b8ab-1615a03f1e21 | -8.94504 | -44.23895 | 2025-04-26 04:08:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 488a4fad-c4be-33a6-8417-37d8020b1f81 | -8.93811 | -44.23782 | 2025-04-26 04:08:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f55aa6ca-98ba-3f4d-9b09-ca94be1c5ac0 | -5.4223 | -43.19212 | 2025-04-26 04:08:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e96dfd5f-7670-3e18-830e-c9d9cf638e62 | -5.41827 | -43.19529 | 2025-04-26 04:08:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af09223c-aacd-3b68-af12-3f8262287b51 | -8.94566 | -44.23513 | 2025-04-26 04:08:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0169a1e-b76e-3351-866d-095daae79f88 | -8.9422 | -44.23456 | 2025-04-26 04:08:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0999c546-d139-3451-815f-9806b63a768f | -10.1021 | -37.62404 | 2025-04-26 04:08:00 | NPP-375D | MONTE ALEGRE DE SERGIPE | SERGIPE | Brasil | 2804201 | 28 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 386899d1-2b73-333e-b1b2-d73da61f94cc | -8.9485 | -44.23952 | 2025-04-26 04:08:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f86e0da-f106-3ae0-9ada-9a3f7594f922 | -5.50272 | -35.60031 | 2025-04-26 04:08:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b47e2cd6-54cd-3e44-b4fd-25d67a8ee8d6 | -11.3965 | -52.9269 | 2025-04-26 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 1d06259a-b3d0-36c4-a448-f28f77edf4c6 | -11.3963 | -52.9477 | 2025-04-26 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| db840e25-b70b-3766-a836-844ae323321b | -11.4152 | -52.9458 | 2025-04-26 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 3c95172e-bcac-3b89-89c5-d194442f982e | -10.96941 | -42.18112 | 2025-04-26 04:10:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README3.md)
