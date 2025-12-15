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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a909318-c81d-3621-a1e7-2ea38bf29fba | -3.20591 | -46.83671 | 2025-12-15 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9acc9a0-ba35-3cf5-9b79-ae2e1a7a3176 | -2.3935 | -45.77189 | 2025-12-15 04:42:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eba4da11-969f-3a9f-b390-5d5d5467a459 | -3.30575 | -42.53498 | 2025-12-15 04:42:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd079dec-4ecd-34e5-9828-fb3b4a384daf | -2.45682 | -52.22272 | 2025-12-15 04:42:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4a5a99a-1d15-363a-8722-3d2eae150889 | -2.63752 | -47.30005 | 2025-12-15 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fa387df-b5ab-3ca3-a92b-85673150f569 | -2.23211 | -45.6544 | 2025-12-15 04:42:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86913210-e9dc-3221-ba02-e4a77269bb9f | -2.22916 | -45.6498 | 2025-12-15 04:42:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9a376aca-809e-3017-8abc-bcd39d1f5345 | -3.12954 | -41.77372 | 2025-12-15 04:42:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 40ff001d-2810-362d-844f-81cfa8e84a8a | -3.71196 | -39.62429 | 2025-12-15 04:42:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 671faddb-257b-3349-b47c-f581c0ba2add | -3.80226 | -47.06338 | 2025-12-15 04:42:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee474f01-b945-32e6-b210-77f3b6ccdb01 | -11.14771 | -43.32792 | 2025-12-15 04:44:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1902c362-58a2-3e4e-b43f-98193a9007de | -3.93018 | -47.56071 | 2025-12-15 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f8e1455-d8da-3762-be30-098a57216324 | -5.26785 | -45.85629 | 2025-12-15 04:44:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f859ac6e-0ddb-3bfa-a0a9-8d239e630e26 | -5.48376 | -45.38058 | 2025-12-15 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de1617e1-b4a2-3f07-a9f5-27f3e8677b50 | -4.9021 | -44.05742 | 2025-12-15 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf47723c-6302-3111-bdc0-4bd1c38317c8 | -6.48205 | -38.82457 | 2025-12-15 04:44:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2011a3cc-3e9b-3898-b814-f926eea32f7c | -8.14209 | -43.55337 | 2025-12-15 04:44:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae918039-84fb-3c5d-8df2-fa566763462c | -4.90176 | -44.05712 | 2025-12-15 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6cbb7d9-0433-3467-a9af-1eb1bcbff9b2 | -4.23526 | -46.31209 | 2025-12-15 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9a33171-53be-3a0f-b2be-21941ffa2c3a | -5.49135 | -45.38163 | 2025-12-15 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8adebc5e-b835-32d9-ad8a-e4257bae64c4 | -3.53296 | -52.14619 | 2025-12-15 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d771efee-8126-35cc-898d-9b0f1941a03d | -2.83389 | -54.83454 | 2025-12-15 04:44:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 45ccf085-2552-341e-a7f5-b847bffcea5f | -11.14837 | -43.3229 | 2025-12-15 04:44:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 14975b96-2ff9-3111-af4b-dc00b5166fda | -4.10494 | -47.22582 | 2025-12-15 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 06ea06a0-bd82-3691-b90f-c0ebfc24e58f | -3.31999 | -52.83048 | 2025-12-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa3abb1e-6510-3c99-a3c4-4e919f8ebb3b | -6.47608 | -38.82382 | 2025-12-15 04:44:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7594f0a2-a945-3ee6-8604-241fc52911a3 | -2.83758 | -54.83933 | 2025-12-15 04:44:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a75018fa-3544-33d9-8711-568d3b51eee8 | -2.83323 | -54.83864 | 2025-12-15 04:44:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 006710a1-7224-36b2-9d3c-d3abb2dc54e2 | -11.14301 | -43.32725 | 2025-12-15 04:44:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 48e58e15-10ad-3c33-866b-ccc6d288ea73 | -5.49577 | -42.16346 | 2025-12-15 04:44:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2f9772da-9fd8-316d-aea9-951662c5093e | -5.03044 | -41.3038 | 2025-12-15 04:44:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 83b0f4e1-871e-3330-b645-1bf16693de0d | -4.69799 | -43.25547 | 2025-12-15 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1deceec-0ff4-37ea-92b8-81989033c7e6 | -4.69585 | -43.25364 | 2025-12-15 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9566c13-14ab-3385-912c-0f4b1e4998d9 | -4.6894 | -43.25423 | 2025-12-15 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f36fefd7-6541-316f-964d-3229004333a2 | -10.587 | -45.22295 | 2025-12-15 04:44:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5756a1c9-4483-325c-8b0c-fb4b9956d8ce | -4.23434 | -46.31069 | 2025-12-15 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b80cfac-fd7b-3050-b17d-061f5878fc42 | -11.14367 | -43.32224 | 2025-12-15 04:44:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ab94e581-5dd0-3c1b-bc52-3894c4cfad1b | -4.69861 | -43.25145 | 2025-12-15 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 907a26ed-dbd6-372e-986f-b29ee722f082 | -4.70014 | -43.25428 | 2025-12-15 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8043065b-9507-3626-9a8c-b1ca26d0dfd2 | -12.63853 | -55.78589 | 2025-12-15 04:46:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6c8ad1f2-9224-33d8-a648-456588937911 | -14.53536 | -59.54832 | 2025-12-15 04:46:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b1c6218-8d94-3f00-ae3a-d1ceffd9bfaf | -16.03539 | -58.44889 | 2025-12-15 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ae6f43db-6fdd-3aba-ad5f-6f1d67189a52 | -16.07297 | -56.59143 | 2025-12-15 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75b254e8-ec31-3687-9b66-c4c71a12e042 | -16.0769 | -56.59222 | 2025-12-15 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b108fbda-9359-3bec-865b-19710ba1c472 | -12.63153 | -55.7792 | 2025-12-15 04:46:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dea45d80-28d6-3889-b201-2ded7941a1d2 | -12.63458 | -55.78516 | 2025-12-15 04:46:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 40fc66d1-767f-322e-8141-2fb67fe5f848 | -12.63548 | -55.77995 | 2025-12-15 04:46:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 278dc01a-3776-3a6f-8f8f-18eeeef2698b | -12.63062 | -55.78442 | 2025-12-15 04:46:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5b433cf-c0ad-30a9-9560-a0cc8f9e40a0 | -12.63944 | -55.7807 | 2025-12-15 04:46:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 5d1b26ab-36d4-3585-95db-5b12213574b1 | -12.63366 | -55.79039 | 2025-12-15 04:46:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5e55fd01-fbda-3645-9d32-2d05f17b635f | -12.45937 | -54.91734 | 2025-12-15 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 612c8b71-a4a3-3576-8ab5-731433054702 | -12.31669 | -46.03341 | 2025-12-15 04:46:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a25d587-a81a-334d-9f6d-34220de90be3 | -14.54024 | -59.54935 | 2025-12-15 04:46:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8044bb9-3361-38e1-a5de-a92240f64940 | -12.6301 | -55.7827 | 2025-12-15 04:50:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 90b1b13d-6f79-34c5-82d0-464c919828f7 | -12.6301 | -55.7827 | 2025-12-15 05:00:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| deb350af-0ddc-325f-8ab3-3c15d4935f3f | 0.05443 | -51.11221 | 2025-12-15 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1f5d623-acf4-348f-97ac-add0a1c23bba | 2.71417 | -60.91275 | 2025-12-15 05:01:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9dc9501-9fdd-3c56-8d2f-a1002c4b345a | 2.71262 | -60.91108 | 2025-12-15 05:01:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49123671-4841-3003-ad93-0940b07f3879 | 1.12723 | -51.0533 | 2025-12-15 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea7be096-b9a6-3a0d-b8f7-884b2ba5dd04 | -3.20636 | -46.83024 | 2025-12-15 05:03:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7960cc5a-e9d7-31bf-9c08-d691532fa915 | -3.0533 | -52.82898 | 2025-12-15 05:03:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8806eed-b53c-3cb5-94d7-54981568a511 | -2.18822 | -53.73617 | 2025-12-15 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7376cd79-8b0a-3594-b328-84a8e80cd591 | -2.83642 | -46.73347 | 2025-12-15 05:03:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7b75df2-d871-324a-a41c-d84b02bd174d | -2.63551 | -47.30031 | 2025-12-15 05:03:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3ebeb2a-d3bf-32b3-9e36-6383c583ac7a | -1.29505 | -49.31042 | 2025-12-15 05:03:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7154c8ab-0a68-3cf8-9cae-e2d1bc75543a | -1.31339 | -49.30173 | 2025-12-15 05:03:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9df78ca5-d5dd-3065-8c50-4980016f84ea | -2.83685 | -46.73056 | 2025-12-15 05:03:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1963372-5863-32a5-ab94-287f9e57a022 | -2.23145 | -45.65294 | 2025-12-15 05:03:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9f9bda5b-aeb7-30ea-a183-0a860f0ca5bf | -2.63766 | -47.29919 | 2025-12-15 05:03:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 504701c2-1fac-39a4-ad9f-9d6ba8ab3db8 | -2.63279 | -47.29845 | 2025-12-15 05:03:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 906f12f6-dbd8-316d-ab6e-d5b2041a45bc | -3.66593 | -53.81798 | 2025-12-15 05:03:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37c51e5c-7393-38a6-a539-0a35a47af7b1 | -1.30924 | -49.30109 | 2025-12-15 05:03:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 72d770ee-d769-3b3f-8b29-2c225cac9677 | -2.45596 | -52.22629 | 2025-12-15 05:03:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02250dc4-c9cc-3452-bb06-4eed78621f1f | -2.22603 | -45.65218 | 2025-12-15 05:03:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5e913303-41a6-398e-a2f0-d619647af140 | -3.20591 | -46.8332 | 2025-12-15 05:03:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8506a1b6-cd57-3b6f-a3d4-44646d8e7347 | -3.05905 | -52.83767 | 2025-12-15 05:03:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc2592f4-848c-3514-a6ca-3e468f2a1e1a | -3.02205 | -52.82407 | 2025-12-15 05:03:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 405d30b3-3485-33b5-b299-4f24e3590d24 | -2.45658 | -52.22229 | 2025-12-15 05:03:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eecb691f-d838-3418-84c6-3cb7a3ae5e61 | -2.6363 | -47.29495 | 2025-12-15 05:03:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 793b3eaf-dfb3-3db4-85c4-cc7f8f956b5f | -1.13325 | -52.58207 | 2025-12-15 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9434cab9-b52a-3cac-a3fd-3198abc2740f | -1.12174 | -58.06283 | 2025-12-15 05:03:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 977622fb-d8ef-37c1-97c5-9628195a1584 | -1.29621 | -49.30291 | 2025-12-15 05:03:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69738053-f457-372e-a112-2946b55daf6f | -2.19101 | -53.74023 | 2025-12-15 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9145df90-4ca9-3e6a-85fd-e8ca316e0431 | -2.83349 | -54.83486 | 2025-12-15 05:03:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 549e53b9-09c7-3c95-9dc8-7bccd45947ae | -2.93858 | -49.13738 | 2025-12-15 05:03:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b7e5993-3f01-3ceb-9189-17225b958c3f | -2.83295 | -54.8383 | 2025-12-15 05:03:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 92a8f06d-c3f7-3efa-b1ac-1522f1099f03 | -1.29563 | -49.30666 | 2025-12-15 05:03:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99c68ca9-6425-32a5-8590-4378ab06dadc | -3.066 | -52.83873 | 2025-12-15 05:03:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2526dd5b-d02f-3bf7-a451-be76b4b89be9 | -2.19157 | -53.73671 | 2025-12-15 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bede2c5a-79c4-3a08-bcfe-3ddf01809ceb | -2.8325 | -46.73429 | 2025-12-15 05:03:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eadbd019-f97d-3534-8e83-772c6b57af9b | -2.41047 | -48.28419 | 2025-12-15 05:03:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 569d122f-22e4-3d91-b294-7e1ec2401914 | -2.58469 | -45.14602 | 2025-12-15 05:03:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 907861b8-5a0f-3273-b0c1-5bf488652429 | -3.05389 | -52.82518 | 2025-12-15 05:03:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26ab1a83-a24c-34b7-8bf0-98bdfe98c5f6 | -2.1666 | -45.93213 | 2025-12-15 05:03:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7e0ce77-5d0b-38cf-815b-82ebd280b350 | -1.30036 | -49.30355 | 2025-12-15 05:03:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d21b717-ee0f-3440-8df9-e299b349538e | -3.20129 | -46.82946 | 2025-12-15 05:03:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c19b348-a27c-3a6a-b07b-687c01d44926 | -2.77696 | -54.5258 | 2025-12-15 05:03:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b21f4fa7-ffab-3ead-95aa-aa89d93af66d | -3.05965 | -52.83386 | 2025-12-15 05:03:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52924515-3760-33f5-82d6-8b98a805562f | -3.32195 | -52.82867 | 2025-12-15 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bdfe2fb-0afc-3623-8497-2967963801c8 | -2.8334 | -46.72847 | 2025-12-15 05:03:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README7.md)
