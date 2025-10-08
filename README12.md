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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba7e728d-861d-332c-9485-9baa4894382e | -5.2601 | -44.1368 | 2025-10-08 02:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 4dc89d12-e639-3574-8b1f-7ef62e27c9a7 | -8.2263 | -44.178 | 2025-10-08 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 6ccb2a4f-4054-3566-bb42-39ed2841ab08 | -10.9489 | -51.021 | 2025-10-08 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| ef5f100d-df26-3e60-a273-a44d81f83ba8 | -7.0167 | -42.8998 | 2025-10-08 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 3257d51e-f153-3629-ac7e-a10fffeab19b | -7.0359 | -42.8744 | 2025-10-08 02:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| c3e77cd8-81ec-3713-926e-a3f55907b5c1 | -10.93 | -51.0229 | 2025-10-08 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 5e49933a-76c0-3e63-bde7-583587dc5651 | -5.1414 | -44.967 | 2025-10-08 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 161.7 |
| a541bbb7-b431-3551-8ccc-94e6ecded77b | -17.284 | -42.6479 | 2025-10-08 02:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 157.3 |
| f6fce569-5363-3ea9-8617-be98c6ed2b6a | -12.3971 | -63.8811 | 2025-10-08 02:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 72d7ebc6-a1c4-3275-adb0-819804bd4b23 | -17.9418 | -57.531 | 2025-10-08 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.6 |
| e24926b9-6f57-3215-82f2-50011a17e470 | -4.4978 | -46.3509 | 2025-10-08 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| cdd84409-bc63-3c19-a25f-8699e8384c32 | -11.6891 | -50.9619 | 2025-10-08 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 5040594d-cdfb-35bd-bccd-51586b1904c2 | -10.911 | -51.0249 | 2025-10-08 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 7eae0faa-a392-3717-b3ad-7ea0ca996ea7 | -7.5874 | -64.5097 | 2025-10-08 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 43d1f705-a351-3336-beff-afc745dea617 | -7.7922 | -44.2229 | 2025-10-08 02:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| ca2cc522-7837-3f7d-9f3d-b06d6d9d3348 | -11.7272 | -50.9577 | 2025-10-08 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 31cdc00d-a141-3240-b022-05fd34c01ca3 | -11.7082 | -50.9598 | 2025-10-08 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 509d1482-6ccd-3790-a0bc-d97ecdc4ad59 | -11.7079 | -50.9811 | 2025-10-08 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 685a0c36-054e-39c4-b2cd-4e47d7f82f1f | -5.1416 | -44.9443 | 2025-10-08 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 0b035e96-0253-3978-8f57-4cc7124c77be | -6.9982 | -42.878 | 2025-10-08 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 00bc50f5-1f8e-356e-8da6-89372a6a4dbb | -4.6873 | -45.8504 | 2025-10-08 02:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 7a250b90-04bf-3adb-81f1-e53ec104b073 | -7.017 | -42.8762 | 2025-10-08 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.5 |
| 0a81a829-d35b-399e-a829-3d5a97fd3cb5 | -11.7269 | -50.979 | 2025-10-08 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 22bbf442-74a6-31af-9710-96a33e69ea0a | -17.7137 | -40.2435 | 2025-10-08 02:40:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 70.3 |
| 42af1f80-24d9-372a-b7cb-8e768f49d38b | -8.2263 | -44.178 | 2025-10-08 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 4acf46d4-0ba0-3d78-98ef-9d1dc09b11a4 | -5.2601 | -44.1368 | 2025-10-08 02:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 392041d5-54cc-355c-8c1e-536e18347f04 | -12.3971 | -63.8811 | 2025-10-08 02:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| d95e53d2-3e41-3594-8330-24addbe6849d | -7.0167 | -42.8998 | 2025-10-08 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| f10cba06-33c6-3482-8c1e-47d4d1c75155 | -11.6891 | -50.9619 | 2025-10-08 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 9100fe6c-c7f4-33ff-8471-2e632d7e2cdb | -11.7269 | -50.979 | 2025-10-08 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 7738b52e-b5fe-3e62-ba3d-8ab181f709e3 | -7.5874 | -64.5097 | 2025-10-08 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| fd7a25aa-2ef0-3850-b2f5-acd3c597b6a7 | -17.284 | -42.6479 | 2025-10-08 02:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 783da5d0-5182-316c-be7d-0b619f82fc24 | -7.017 | -42.8762 | 2025-10-08 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 167.8 |
| 4c10b886-c89f-3302-9ecb-f43334e745b7 | -6.9982 | -42.878 | 2025-10-08 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 088a95d9-07ca-3498-bf52-c88f2ef2a7f9 | -11.7082 | -50.9598 | 2025-10-08 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| b021a04e-07eb-3c76-8b0b-f5a8c4e7338c | -4.4978 | -46.3509 | 2025-10-08 02:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 96eae815-2360-34a2-bcc1-754e87c9c275 | -5.1414 | -44.967 | 2025-10-08 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 135.7 |
| b8532701-201c-3b46-bd89-3e805cf14c52 | -7.0359 | -42.8744 | 2025-10-08 02:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| ae6dff23-5f0b-3504-96c3-e275b275877d | -15.6393 | -52.5688 | 2025-10-08 02:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| ed3aaf65-bc79-3a30-8c8f-35a1490068cb | -11.7079 | -50.9811 | 2025-10-08 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 39a7093b-8e23-3f37-9aac-92384baf6249 | -17.3041 | -42.643 | 2025-10-08 02:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 73.2 |
| dfde7c88-82c1-3442-b8f8-a6c8eacfbd48 | -11.7272 | -50.9577 | 2025-10-08 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 8f05cb0d-0206-3cba-b8a2-f7b524fb128e | -6.74344 | -34.96331 | 2025-10-08 02:56:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e31a1136-f33a-315a-841f-e225f57fa32f | -5.82225 | -35.48419 | 2025-10-08 02:56:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 563f70e9-e769-3c99-baff-e8a4915bf465 | -6.74264 | -34.9676 | 2025-10-08 02:56:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 80520bee-673e-35e3-93d1-782dd5cd840f | -6.74026 | -34.96595 | 2025-10-08 02:56:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 04d6f82a-a5a9-33f6-9dd3-68034f6389ab | -5.82312 | -35.47927 | 2025-10-08 02:56:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8fba25b6-d207-3a35-a2b9-f5f356151592 | -5.8201 | -35.48166 | 2025-10-08 02:56:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 31a373df-cc99-3032-94f4-849bdf12c6bb | -9.67371 | -35.85953 | 2025-10-08 02:58:00 | NOAA-20 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0e4f9d50-b72b-3e6a-b54f-07796a565764 | -9.67284 | -35.86411 | 2025-10-08 02:58:00 | NOAA-20 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cb758cfe-11e8-3606-903d-3941e6897517 | -7.0167 | -42.8998 | 2025-10-08 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.9 |
| 45a162a0-d7bb-3c99-b03d-6bcc7d9f4c1f | -17.284 | -42.6479 | 2025-10-08 03:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 67b11cef-241b-3113-b748-0ae18ae98cdb | -5.1416 | -44.9443 | 2025-10-08 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| bb3277c8-a44a-30af-a197-fb6cca269fba | -12.3971 | -63.8811 | 2025-10-08 03:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e8f10ced-e29b-3218-9e17-4ac4a2b90158 | -5.8574 | -44.3008 | 2025-10-08 03:00:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 062c1f45-2995-3dd6-bfba-3231b1b415de | -5.1414 | -44.967 | 2025-10-08 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 968221fd-7fd8-37b8-b511-fa6062c27aaa | -11.6891 | -50.9619 | 2025-10-08 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| c1781dbd-f2fd-3e80-9c76-e3424152a08b | -7.0359 | -42.8744 | 2025-10-08 03:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| 7d648141-ae86-3e3f-b25f-411541f288d6 | -4.6504 | -43.2038 | 2025-10-08 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 512fc9ee-154f-3f36-9f59-e64d04edf6e5 | -11.7272 | -50.9577 | 2025-10-08 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 603249f8-fab4-3799-b267-b455bcf2f215 | -11.7082 | -50.9598 | 2025-10-08 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 155.7 |
| b1dba7ad-21fe-33b7-8147-effb50316e51 | -6.9982 | -42.878 | 2025-10-08 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 77d592d9-f650-3c82-ac24-7371b6dccd34 | -7.017 | -42.8762 | 2025-10-08 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 197.6 |
| 77e22fd1-3b8a-3bca-add2-48be288d075a | -4.4978 | -46.3509 | 2025-10-08 03:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| e6913598-45ac-31c1-968e-ebe44c4f8992 | -11.7079 | -50.9811 | 2025-10-08 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| f1d0ea4f-a71b-3cc7-be2e-c2d560f59800 | -12.3971 | -63.8811 | 2025-10-08 03:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 387dd5ff-e382-3b4b-ba48-84b40b2c5c3d | -5.2601 | -44.1368 | 2025-10-08 03:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 7e87b0d5-d7f3-30de-8e2f-e6d590b0ad0f | -11.6891 | -50.9619 | 2025-10-08 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 2a21a57b-22d6-30ac-9c8e-c77cb1d2eb5d | -5.1414 | -44.967 | 2025-10-08 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 77060407-f4bd-33d2-8f22-d97e3526b288 | -7.017 | -42.8762 | 2025-10-08 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 211.2 |
| c70bc86a-98b1-346f-bb13-1d9a9f76c4bc | -4.6504 | -43.2038 | 2025-10-08 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 9001ad34-7293-34bc-9505-45298e50e955 | -11.7079 | -50.9811 | 2025-10-08 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 162.0 |
| e4265936-1ce6-319f-91b9-bebb78eb325f | -7.0167 | -42.8998 | 2025-10-08 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.9 |
| 682dc6bd-e2ae-3f53-b445-b8b7a954fbd0 | -5.1416 | -44.9443 | 2025-10-08 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| b8714cde-e3e3-3b85-bad3-67ed9caed0c0 | -4.4978 | -46.3509 | 2025-10-08 03:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 49bf4183-24c1-3fbc-bcdb-a74178880592 | -11.7269 | -50.979 | 2025-10-08 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c13d9649-bc92-3fc7-ac9d-3a881edcef89 | -11.7082 | -50.9598 | 2025-10-08 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 272.0 |
| 4299b577-7dd6-34cf-ac5c-923300b30815 | -5.8574 | -44.3008 | 2025-10-08 03:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| d294cdb3-b550-3339-980a-d54d6150b26e | -17.8219 | -57.6277 | 2025-10-08 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.4 |
| d530d6a6-b6c7-3f9a-b7b2-0fe7a526607d | -7.7922 | -44.2229 | 2025-10-08 03:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| d4e17361-c484-3e87-ac0d-a09cf9f8a4f4 | -17.8417 | -57.6254 | 2025-10-08 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 1f2a7ae2-f53d-3de1-bc31-8fca49bb4503 | -12.2525 | -47.8728 | 2025-10-08 03:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| ca019650-3864-3fcf-80b1-b139a5ad7e42 | -17.284 | -42.6479 | 2025-10-08 03:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 2540f880-fd0b-3c8d-a217-a3387980c3b3 | -17.8216 | -57.6483 | 2025-10-08 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.1 |
| e3d56f18-5248-3e76-badd-c103c32f15f2 | -6.9982 | -42.878 | 2025-10-08 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| fc063736-d7b6-3d44-8176-759eac95bfbe | -7.7924 | -44.1998 | 2025-10-08 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| d94d43d8-7b27-3103-a186-3c7dcffde4a9 | -7.0359 | -42.8744 | 2025-10-08 03:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 105.4 |
| 0e981e34-9693-3aee-b1fb-20fad39dc9da | -11.7085 | -50.9385 | 2025-10-08 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| f46222f2-e681-3ff2-a951-8f014a138a4e | -17.8413 | -57.6459 | 2025-10-08 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 8b21d981-4c09-3c65-b27b-bca91dc0bcf4 | -11.7272 | -50.9577 | 2025-10-08 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 6b0df12e-f56b-3b30-a962-99afe889e3e5 | -17.284 | -42.6479 | 2025-10-08 03:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 7635b0f5-19cc-399a-b75d-6c2b9d3d1868 | -16.0012 | -50.9674 | 2025-10-08 03:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 71e53b76-3d15-3798-bf8e-6a0318baa07a | -5.8574 | -44.3008 | 2025-10-08 03:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| e31aaaf4-0860-333c-a928-e3169f2062a4 | -7.7924 | -44.1998 | 2025-10-08 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 61833c7f-df7b-3654-ae44-2b3294bcb568 | -7.7922 | -44.2229 | 2025-10-08 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 1d26503a-eeac-35ac-82ef-5d18ab8f4712 | -11.7079 | -50.9811 | 2025-10-08 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 44ed975c-1623-31bd-b00b-a5c312116869 | -5.8761 | -44.2994 | 2025-10-08 03:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a2565d03-67cd-3a20-9db3-8961aabe5a7f | -4.6504 | -43.2038 | 2025-10-08 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| aa7f4179-3826-3a3d-a08f-1e2be36f5bfe | -11.7082 | -50.9598 | 2025-10-08 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 329.7 |
| 2ab83442-0e8e-36be-ab63-716e4d7af848 | -11.7272 | -50.9577 | 2025-10-08 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 301.8 |


[Clique aqui para ver as próximas entradas](README13.md)
