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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2083d052-af17-3796-839e-ebddc64221a4 | -15.31687 | -52.99775 | 2025-10-25 05:42:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89afd50e-0dd7-3a75-820f-d1a5dd8d9280 | -15.93853 | -56.11473 | 2025-10-25 05:42:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 021aa83f-f78b-39da-b623-36e38997dcd4 | -15.93339 | -56.11034 | 2025-10-25 05:42:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| dafc3914-2df1-3d88-a585-2f20b73bae1a | -14.84546 | -52.44277 | 2025-10-25 05:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a96c185d-f942-3b66-9e6b-ab6f8124c7aa | -22.14103 | -55.2829 | 2025-10-25 05:44:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55ed4605-8c5e-3e94-a992-6f3356c985c3 | -22.14771 | -55.27832 | 2025-10-25 05:44:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb69bd0f-fb4c-3a22-849c-464c5b81eb12 | -2.7964 | -49.136 | 2025-10-25 05:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 3f12e57e-7871-3d6c-9f5d-5e9e31b3f407 | -2.8149 | -49.1354 | 2025-10-25 05:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| efd3bb0e-2ccd-361c-849e-bccad2a9ea75 | -4.55465 | -46.68224 | 2025-10-25 05:57:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| da220286-467b-3ae4-af03-26cea5261c3d | -2.79302 | -49.14174 | 2025-10-25 05:57:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7aad4591-0bb2-39d1-92ee-f21af6c3a513 | -3.11915 | -49.09316 | 2025-10-25 05:57:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| dd7cfb48-1b59-39fb-a433-12b6d4b509d5 | -4.81496 | -45.57748 | 2025-10-25 05:57:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f2944f2b-cb42-3626-96d3-0bd280056399 | -2.79498 | -49.12897 | 2025-10-25 05:57:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ab7a58ff-c736-395a-8138-6a365dc0a12e | -4.5928 | -49.57994 | 2025-10-25 05:57:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ef7d65f2-3ac5-3f70-988e-773e2b7c7300 | -6.78887 | -46.46165 | 2025-10-25 05:57:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1608ebb3-c96a-3a03-a9b4-f50a02dc88b8 | -6.90979 | -45.1643 | 2025-10-25 05:57:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8c210362-5da0-38f5-a3dc-e6a42d45dae7 | -4.96058 | -47.59409 | 2025-10-25 05:57:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 63100879-ecdc-367f-828a-32d103057b58 | -5.72473 | -49.09282 | 2025-10-25 05:57:00 | AQUA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 84052b42-18f7-333d-844e-659e887bc330 | -2.80352 | -49.14333 | 2025-10-25 05:57:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| de5ac881-4cf4-3fce-9359-f781919adf7c | -4.54572 | -46.68089 | 2025-10-25 05:57:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 660a24d1-7146-3254-a8e5-e3ac2885625f | -4.80618 | -45.57619 | 2025-10-25 05:57:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d18f0605-3f6f-3c68-8ade-0fec1da0dd2e | -6.92 | -45.15664 | 2025-10-25 05:57:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 58a16047-717d-3caf-9820-19840e3a26af | -6.23511 | -46.39621 | 2025-10-25 05:57:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1925541c-a0ad-3c5d-8200-b2c5514a9e6f | -4.24481 | -44.5707 | 2025-10-25 05:57:00 | AQUA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7fcf7006-e490-353d-91e5-532440452341 | -5.45063 | -45.41033 | 2025-10-25 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c27fc7c1-7f1b-3092-9122-dd1e45f94888 | -4.21931 | -48.60555 | 2025-10-25 05:57:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a65aa559-e654-3e42-98b7-05c647e6866e | -3.9103 | -47.69119 | 2025-10-25 05:57:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| af4a4e19-54cd-32a4-817c-d9e86521f5aa | -4.25235 | -44.58093 | 2025-10-25 05:57:00 | AQUA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| df90cd22-5168-30bb-95ee-fee52486b37b | -4.8858 | -43.23521 | 2025-10-25 05:57:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e773c92-13cb-39b6-b277-fe1fe3a3abdf | -4.67112 | -43.2439 | 2025-10-25 05:57:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9126f5f3-d5a0-3110-a353-2008ed91ef43 | -3.92123 | -47.68251 | 2025-10-25 05:57:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d4a92b09-df8c-397d-8c73-5bd5311bc461 | -6.41402 | -46.18536 | 2025-10-25 05:57:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4666eb91-7744-3a77-b3ee-ebd93b8a9e8a | -6.96067 | -43.49442 | 2025-10-25 05:57:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c8ed9e90-a9e1-39df-93a0-cf6ac1a10d09 | -4.25369 | -44.57199 | 2025-10-25 05:57:00 | AQUA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f4e0f9df-5001-302d-9cc1-a1a146e30cb2 | -6.1754 | -42.61633 | 2025-10-25 05:57:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| debecbd6-823f-3a38-9c30-d675025235d3 | -2.80548 | -49.13054 | 2025-10-25 05:57:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| ad15f634-f719-3f02-966b-36a94437cc6b | -4.88729 | -43.22504 | 2025-10-25 05:57:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| be4856e9-d3ec-3f3a-b260-c419139adcb3 | -3.11726 | -49.10572 | 2025-10-25 05:57:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 141083bd-6d69-3712-8a78-308483a00565 | -6.2846 | -42.34987 | 2025-10-25 05:57:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ab8a9a3c-5242-3410-b250-2e81c93e66e8 | -5.25233 | -44.13472 | 2025-10-25 05:57:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3e465984-bb1d-38d4-bed0-163c8867a9fa | -3.91968 | -47.69259 | 2025-10-25 05:57:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6fbd9181-7138-33ee-a7e1-689a402c3770 | -3.11554 | -49.09835 | 2025-10-25 05:57:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 4b6a2840-0c4c-3292-ad6c-bb2cec2fca06 | -5.45194 | -45.40155 | 2025-10-25 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 98d05719-ab7f-32ca-b757-9c266078ad5a | 1.62959 | -55.75138 | 2025-10-25 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bc31a65-ab7e-3f31-8fcd-1f6f4ad5b11c | 1.56342 | -55.99474 | 2025-10-25 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a85bfce9-d720-3f51-9b6c-89c05f7d2db2 | 1.63992 | -55.73262 | 2025-10-25 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 472b19c5-dad8-3214-a34d-4979fa8213e1 | 1.6352 | -55.74466 | 2025-10-25 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1999b8c0-2300-38e8-a286-aa08071a06de | 1.55693 | -55.99564 | 2025-10-25 05:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2a96303-5a33-3c0e-a811-5a9289ac9463 | 3.88585 | -60.11458 | 2025-10-25 05:57:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56a8d3fd-388d-3744-a857-35263f4db1df | 3.88294 | -60.12633 | 2025-10-25 05:57:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2f500c3-6ea4-35e5-89c5-bca4936ced45 | 1.64554 | -55.7259 | 2025-10-25 05:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25dbbcf6-715e-3eab-b895-10cea9af92fc | 2.50952 | -61.03062 | 2025-10-25 05:57:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 762492d1-bff5-3ec7-83b9-e81badde3dfd | -14.99788 | -49.98499 | 2025-10-25 05:59:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 77200b25-0939-35f8-adef-0a09fd59e9fb | -10.86498 | -48.04447 | 2025-10-25 05:59:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| ebba5245-9ded-39c2-8bcf-7981c43e378b | -10.4125 | -44.49354 | 2025-10-25 05:59:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c1889de1-5c45-3220-a716-84cd1e68ba66 | -9.2487 | -45.58551 | 2025-10-25 05:59:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8872f518-fbd1-39a2-911e-db84ee88674a | -12.05663 | -46.39534 | 2025-10-25 05:59:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a4e13261-0ab8-3b03-ae15-f79cbec7a2b0 | -14.92364 | -48.51736 | 2025-10-25 05:59:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3d9fb31c-3f36-397d-958e-6bb19b01c6e6 | -12.2521 | -47.44031 | 2025-10-25 05:59:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3f7f5371-4296-3fda-94f3-0f56dfd56d83 | -13.35288 | -47.41296 | 2025-10-25 05:59:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9acfe41c-8f41-3f0a-b814-4d4d65d2d3c0 | -7.55815 | -47.11554 | 2025-10-25 05:59:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 286d4791-b70f-3bfa-bb99-a5cbc5f3d806 | -13.91505 | -48.40109 | 2025-10-25 05:59:00 | AQUA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f75c7ba2-5567-3c49-8179-50e9e9214c04 | -8.35474 | -46.18217 | 2025-10-25 05:59:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6e1c045a-6608-30a9-94ce-87ed3e0a4bed | -8.5954 | -44.81615 | 2025-10-25 05:59:00 | AQUA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1d4dfbe0-0107-3306-a57f-ea953097e09d | -12.12043 | -46.70655 | 2025-10-25 05:59:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 67b8cb65-36e9-3d46-afdf-b311282ec478 | -12.1191 | -46.71554 | 2025-10-25 05:59:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 41ac8d11-86d4-35cc-8ee4-6e827c6218cf | -9.31457 | -45.20068 | 2025-10-25 05:59:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7677a8ae-ec72-3498-ae12-f5ca508ab929 | -9.25005 | -45.57637 | 2025-10-25 05:59:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7b8f0a8e-03a4-3176-9068-8002342bf018 | -14.41569 | -47.91625 | 2025-10-25 05:59:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f78a3150-4251-3b8a-b140-384ecc3a4546 | -14.18216 | -47.31094 | 2025-10-25 05:59:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3827ffe3-a4ed-3667-8374-0ef19cf0b100 | -16.57868 | -43.50171 | 2025-10-25 05:59:00 | AQUA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e2a549b0-0b93-33f0-a26c-2e49367e4215 | -14.47255 | -47.89739 | 2025-10-25 05:59:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2867a913-61bc-315f-8c24-9c438d4d0434 | -9.30068 | -45.16981 | 2025-10-25 05:59:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 15894856-a115-3baa-b977-ba0a2aaf2dd2 | -16.21308 | -46.48266 | 2025-10-25 05:59:00 | AQUA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0936a693-f336-3410-b9c4-bf9ad7f3fc82 | -10.65494 | -48.07839 | 2025-10-25 05:59:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2ef21452-bd19-3ddc-b505-6068e20d033f | -9.30773 | -46.97784 | 2025-10-25 05:59:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 97a8998f-32f3-3d74-8d14-d32307b80cab | -7.35825 | -46.91687 | 2025-10-25 05:59:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 83c1584f-4f14-3612-a886-fecadd55162f | -11.05245 | -48.32354 | 2025-10-25 05:59:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 157902e5-a30f-386c-b01c-7006c9aeadcf | -14.86091 | -48.08247 | 2025-10-25 05:59:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c96e9d6e-0924-3769-9a5e-692cbcfe3f2f | -16.21447 | -46.47286 | 2025-10-25 05:59:00 | AQUA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 47b02bb4-9ab1-3e0d-b1e9-e391918cd116 | -10.63745 | -45.23639 | 2025-10-25 05:59:00 | AQUA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6adfa998-659f-355f-bafe-a8e4bbf79256 | -14.86695 | -48.10201 | 2025-10-25 05:59:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 614411e9-8861-3b55-86c2-362ba8563d4e | -11.42994 | -44.6752 | 2025-10-25 05:59:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a719607b-7c59-3350-ab6f-2d0ec841bd6f | -10.65639 | -48.06891 | 2025-10-25 05:59:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3d256936-a911-3b8a-b1ea-8a5f7bb01f78 | -14.17202 | -47.31855 | 2025-10-25 05:59:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5a0af8e6-e0a2-36ee-ba65-1be7bde95e32 | -8.71395 | -49.60326 | 2025-10-25 05:59:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3da7ab00-d2e3-3916-89b2-3c3e9fe08e30 | -15.23482 | -47.93472 | 2025-10-25 05:59:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c9251fe8-2113-3b5a-94cc-8e90a4722e48 | -14.4069 | -47.91487 | 2025-10-25 05:59:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 99d9491b-968a-30e8-8573-58e9485d32ed | -16.58115 | -43.49418 | 2025-10-25 05:59:00 | AQUA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d3fe4e6b-8b32-3d67-af02-dc2a49ffc851 | -9.99905 | -47.59109 | 2025-10-25 05:59:00 | AQUA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e11d1c04-d71b-398a-9b1f-ec8080de934f | -9.31733 | -45.1819 | 2025-10-25 05:59:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c89f036a-2b1a-36d6-9fd7-124fdb026e49 | -14.86228 | -48.07344 | 2025-10-25 05:59:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a83b74e4-ef52-3216-9416-57cb625eb6bf | -7.86713 | -46.72484 | 2025-10-25 05:59:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 17371481-267f-302d-8564-baf6096c8a28 | -9.95282 | -48.25929 | 2025-10-25 05:59:00 | AQUA_M-M | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3e3023dd-c666-399f-906b-739817b8a08c | -12.84278 | -48.64421 | 2025-10-25 05:59:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| d6da216f-e110-35c5-9c44-932b70730678 | -12.14344 | -48.01658 | 2025-10-25 05:59:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b59dbe05-ae88-314e-85cd-a35a371463c5 | -13.89451 | -48.41661 | 2025-10-25 05:59:00 | AQUA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 897d6fb9-0b47-3399-95a4-e849127aaf24 | -14.17336 | -47.30956 | 2025-10-25 05:59:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 88d94383-9372-3879-a520-53ce4cd0718f | -12.13992 | -47.01779 | 2025-10-25 05:59:00 | AQUA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8d9614c7-4adf-3bc3-87cd-2501768eb350 | -12.29472 | -47.45598 | 2025-10-25 05:59:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README62.md)
