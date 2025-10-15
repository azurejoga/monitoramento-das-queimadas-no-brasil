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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83dc41f4-a5da-36e3-85a2-269095925c90 | -7.17277 | -42.20534 | 2025-10-15 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2e78b062-7788-3260-8c14-3196f9b45215 | -5.91509 | -46.37906 | 2025-10-15 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ea593f2-145b-33f2-b67d-f9f60c8f6017 | -6.27746 | -39.68419 | 2025-10-15 04:06:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9804164d-4689-3280-a8f3-6950d9ee586a | -4.91531 | -46.71349 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8eed7444-2231-3065-abed-649f70f729f1 | -8.2485 | -43.38431 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c9ffef02-118d-3859-b62b-75d3d62318a4 | -6.45496 | -41.89015 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4754e36e-e32f-38ba-9977-fca16c2f0d78 | -4.28759 | -41.73977 | 2025-10-15 04:06:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7d573732-b775-348f-a85f-cb992a55b578 | -6.4605 | -41.83402 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f9ea5be3-136c-349c-b44f-d4470db02c8b | -5.00528 | -45.87193 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a9002c0-c1e2-3950-b071-1df224e18b69 | -5.11786 | -46.05478 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 859cf0b6-234a-3c16-83f8-46b40d8b92ba | -6.22998 | -44.17158 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cf9b63d5-f47a-3a99-8158-caa6c5422713 | -6.91607 | -42.23919 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 23fd12c3-be1c-3523-bdae-e271bd89cd03 | -6.48905 | -44.11708 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 641d9452-3a34-3bb6-985c-8a586c19f5f0 | -5.14686 | -45.76917 | 2025-10-15 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0fae0278-a5a3-371a-877a-f6685c03aed3 | -4.87187 | -45.67743 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a83f811-1f71-3a56-849a-34f8d949dc80 | -8.46306 | -44.1869 | 2025-10-15 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10bc1d2c-b3df-3704-af3d-ebcda9595a75 | -7.67553 | -42.37547 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7b514687-97a4-368d-8ce6-6d605132eb23 | -5.72716 | -43.83217 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bf5314e-6f41-39e4-956a-b004db7573e6 | -4.36226 | -46.77781 | 2025-10-15 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c80bbbc-ae7b-3b3a-9e53-5379347503cc | -6.43733 | -41.80898 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 339d8c24-8afe-3b71-8d2e-3ce143a97f84 | -8.45547 | -44.18963 | 2025-10-15 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 613e7021-277d-32c6-8d4c-289d2605e986 | -4.41982 | -42.8983 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c47a2bb7-d5dc-37f7-894c-c026645b97d9 | -4.58413 | -45.64407 | 2025-10-15 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13fc63af-1bbc-32af-9fdc-0855432ad8ba | -4.28302 | -48.5837 | 2025-10-15 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 930377df-ec09-30b8-bda9-ef47c7bd8a06 | -5.23559 | -43.66837 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8935ccf6-fcb6-32a0-b669-c8212aa2c497 | -5.06683 | -41.19452 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5e5dfde0-7427-3109-b82c-c198dd8448f0 | -5.6122 | -42.72224 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3e8726ab-f1b8-3e27-9d46-ac9263351d07 | -7.45437 | -43.9319 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f38ab0f-8eeb-30a3-b469-409432f187a5 | -5.51489 | -46.19925 | 2025-10-15 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4aa7222-2313-3cca-8319-d344abae5960 | -6.83707 | -42.77909 | 2025-10-15 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 31bb8c04-273c-3fd1-b770-a689742c23bc | -5.26759 | -43.20659 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cbfce5a-03c2-3143-9d92-1c724d5281a7 | -5.32343 | -42.90559 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fc5eb5b-0402-340b-bc68-5351392ee426 | -5.89616 | -42.83352 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9dcfb192-3fc4-33c5-8580-1035ccb0f106 | -6.22783 | -43.3638 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d773786-0f06-3cb8-875a-de3ad1060a4d | -5.86533 | -43.8741 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 302fb10d-3c4d-36a1-bb71-ca3572443e1a | -5.36202 | -42.73131 | 2025-10-15 04:06:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2776b179-6cd6-3239-8c3c-40aac7b6f091 | -6.89873 | -43.9613 | 2025-10-15 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3571ab48-5e79-3994-9284-ee682020ee71 | -5.82518 | -47.81881 | 2025-10-15 04:06:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80e22d9f-85c1-38e3-b584-8fcf28e9e47a | -3.57068 | -49.44273 | 2025-10-15 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 207d7167-04fe-3e8b-b8d5-ac2063deff43 | -5.4939 | -43.79587 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1397a25e-3d55-3b89-a1ac-bbbfe990efd6 | -5.73004 | -43.83674 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95ec72fe-3eb9-315d-8307-e16470c293e5 | -4.77953 | -46.61665 | 2025-10-15 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 427dd574-00e7-357a-9a00-1d2dd2c7b4d6 | -6.4539 | -44.59034 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 58ee52ea-6fbe-3ad9-85d4-2014431c596f | -7.93694 | -44.13111 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99834893-bd12-3189-b194-8f735e2b8042 | -8.28009 | -43.38882 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df8d7bf7-953b-3764-98f7-343e2af51dd5 | -5.54463 | -41.33016 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 142fcab0-6349-39de-8e48-a2d1a260a21b | -5.40699 | -40.89175 | 2025-10-15 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 24ef891a-667d-3c3d-8217-f4c6dfc6d85b | -4.1201 | -50.7219 | 2025-10-15 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c087ef19-d369-3a20-a656-bab5d12b6ddf | -5.72108 | -44.27592 | 2025-10-15 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b02773d-cef4-3515-a3db-bb4e9d835ca0 | -6.79307 | -44.53539 | 2025-10-15 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb30ea63-2cde-3f97-9283-74920fe3a9af | -4.78371 | -46.61751 | 2025-10-15 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b61e2b6-1021-326f-b630-368ef1624572 | -5.49324 | -43.79986 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9079e850-981c-3b3e-a722-5cf78d4e4215 | -7.17113 | -42.19433 | 2025-10-15 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 64966902-a0a8-3e8d-9afd-a05ac98b65f4 | -5.57479 | -43.02136 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a31d617b-3802-361e-baad-90db7d1b3a3f | -6.05559 | -41.90149 | 2025-10-15 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 36ff2572-42da-3628-a6cf-732166a204db | -5.06574 | -41.20142 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e7fd0e43-809f-375c-b6a4-7f2c83f71265 | -4.881 | -45.9442 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a490136e-d25d-38d1-8f31-1eb06468cb77 | -5.97422 | -42.80902 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dcd09e60-a73f-39f0-93eb-eb1c66d296e9 | -5.16624 | -45.16625 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1033da02-efc9-316d-9447-7773e90a2131 | -7.25863 | -44.91523 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6149f0de-18aa-3e08-a723-3e02c460019e | -7.55505 | -43.82983 | 2025-10-15 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61353a17-6a1f-3877-bf74-3a13ae65f77c | -5.43103 | -44.22276 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 5a80e4ff-4e2a-362d-a7cf-600829245064 | -5.39256 | -44.0414 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b399bbf0-f388-379d-9309-313c3cfa4f3f | -4.88542 | -42.77274 | 2025-10-15 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfe514dd-29ee-38e0-b3fe-509305bf4bdc | -7.28038 | -42.95323 | 2025-10-15 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ca796b1a-c70a-3a8e-b7c0-1f6f308f904c | -5.57765 | -44.74323 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db42da1a-8795-3f3a-bf10-939d9857abbb | -4.75534 | -44.11038 | 2025-10-15 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a60ae8b0-311e-3d0d-a33b-612d55d2c397 | -6.74587 | -42.09068 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fe3a051e-9b44-3ebf-bb6b-6966334be2af | -5.97083 | -42.80847 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aa8894b4-1012-3091-a983-9af9f33f9d4f | -5.58762 | -46.36622 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| caca5dd5-48de-302a-b164-3309464ee699 | -5.39159 | -41.16112 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f2c2ef1d-515c-3682-9387-48ccfa9fb96e | -6.14679 | -41.77722 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ed5d5730-ef21-3e22-8268-ba8737b77ff0 | -7.15779 | -42.49118 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 916b006f-79f6-3a91-a9bf-0b3627a0286a | -6.3984 | -42.52216 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9d3fa64a-1c7e-3a84-b8c3-7bf44da0f56a | -5.60295 | -46.24715 | 2025-10-15 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c1ad63d1-8995-3488-a0f9-7b486caf0395 | -6.14392 | -42.7099 | 2025-10-15 04:06:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 96a3ac22-8899-3bd0-88c5-80905bfd89b8 | -5.41205 | -44.21757 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1e517ea-0490-309f-ad6e-f95b1d2128c8 | -5.4217 | -41.37783 | 2025-10-15 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cb01b1b0-8868-3ced-8cc7-aba5d250ec3f | -4.28392 | -48.57843 | 2025-10-15 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8994deeb-52c5-3994-8904-555ca073ac99 | -5.46545 | -44.65038 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a994a814-407a-3fab-9729-4b9f429e8c5c | -4.3529 | -48.20062 | 2025-10-15 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8f66817e-f9df-3af1-b3ee-7b3f0b7de215 | -5.32283 | -42.90931 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69847654-49cf-33a0-99f7-7e161257eb29 | -6.55096 | -43.93805 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 707dd456-1d72-311d-a35f-29dd37e20c73 | -8.20207 | -43.99438 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 641cb8ad-5bfc-3d49-9972-c4be9271dbf0 | -2.7981 | -48.9441 | 2025-10-15 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9baf3ee5-da1f-3fbd-9b7e-c283e57b5b35 | -6.55162 | -43.93406 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 032076c6-7615-3948-a34c-fdf4c9d2abc0 | -3.06785 | -49.51601 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b065820-1979-3b07-b035-fd27f489d782 | -5.39435 | -41.16508 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ebf7ef96-81dc-3ad3-981d-b6e0a6c2ea21 | -6.1445 | -42.7063 | 2025-10-15 04:06:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 871386b0-f437-3e39-9e79-4ac9c0cdc70f | -7.17333 | -42.20184 | 2025-10-15 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0ceb1815-4ed9-35fa-abb5-55d9bc369292 | -7.57206 | -42.68446 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d3e12bc9-e315-3879-b2f9-b40264c56d72 | -4.14762 | -41.65649 | 2025-10-15 04:06:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2acece80-8fb7-33d4-ad6b-83b44447f6f0 | -7.07582 | -41.96078 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0c3d0db9-5161-3130-9920-56c2219ce5fe | -5.32968 | -43.47045 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9edb4deb-a544-3b72-a91b-56bd697af299 | -7.49539 | -42.14202 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| db953a5a-6735-36da-b5f8-29d85285b3ed | -5.43035 | -44.22691 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| ec2d5035-1cc9-3ccf-98ac-6cfd3c700ada | -5.91088 | -42.82842 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 90c80475-df30-3e7a-a79a-6a3eabcd5419 | -8.1964 | -43.98558 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73f80dfe-722e-3363-b2e3-83cf64213577 | -7.74803 | -42.45547 | 2025-10-15 04:06:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 160f3c4c-7942-39c4-8290-19b7ca0699b0 | -5.42247 | -44.22985 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README33.md)
