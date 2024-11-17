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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d20e7fe-7767-3cce-9f86-1f38ff94369b | -19.49301 | -56.61674 | 2024-11-17 04:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 16b21cff-6579-345a-b909-97cd24660e3d | -17.59432 | -57.58874 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 894b7924-4d27-3b76-8b90-58e2f28f2298 | -17.59621 | -57.57918 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 3fdcefdb-13a5-35c3-aea1-15c4cc4bdae2 | -17.57878 | -57.4706 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fd7a4346-39b6-3322-86fc-c8e52c9da5b4 | -20.76397 | -46.76824 | 2024-11-17 04:33:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ec21a2a1-a26a-36ba-813f-c32795764de8 | -17.59392 | -57.58786 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d300bc4b-f3a1-3812-b308-421164c37d4b | -15.92138 | -59.81156 | 2024-11-17 04:33:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00fe0e7d-21c3-39f9-a225-c9e053a99f43 | -17.61163 | -57.57253 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| d929ed1e-5b76-39f7-a73e-30c0813d8ebb | -17.60787 | -57.59166 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 0fccfa8b-78c3-388a-9709-ff6d6d317db1 | -17.58791 | -57.59735 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 824151b1-61ff-3d05-8299-ab4005c61a5a | -17.60712 | -57.57155 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a39f46ca-104f-3640-8d89-61f7bd19fb73 | -15.66904 | -59.73647 | 2024-11-17 04:33:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4f99d4e-4ff7-325f-9970-aaf8de534eac | -17.59213 | -57.57251 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e8afde05-1eda-3eb1-b911-5487dbbfe3d6 | -17.59169 | -57.57821 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 90ece50c-ead6-3939-8a2f-af40cf5d6eef | -17.59715 | -57.5744 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 43655dc7-597d-39ee-b79c-f516f16ec8eb | -17.61708 | -57.56871 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ec770650-98f7-3456-836e-eee08db8eba4 | -16.0768 | -60.11499 | 2024-11-17 04:33:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb0bf47d-5ae7-3c79-a189-29175d6e1794 | -17.82923 | -54.54692 | 2024-11-17 04:33:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b72351c0-d8a8-3212-981e-85fb56dbdd84 | -17.56624 | -57.46297 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 07bf10d1-1a96-38b6-b2b2-265194bc1bc7 | -17.60167 | -57.57536 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 6c3503ec-46e9-348e-897d-bfd30c825f99 | -17.59755 | -57.56869 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7a49a4a0-760b-3304-9aa6-881d44032841 | -15.92066 | -59.81514 | 2024-11-17 04:33:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5310102-dfbb-3370-adfc-15696141b61e | -19.48406 | -56.61891 | 2024-11-17 04:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| edcbfaff-c969-3753-b6df-5a6830bf7f06 | -19.4889 | -56.61586 | 2024-11-17 04:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0592cf4d-36c9-35fa-a445-046bcd43a83c | -17.62159 | -57.56968 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9a85ce3b-a788-36dd-8786-5cf56a07b805 | -17.59301 | -57.59266 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6aabe01f-0147-3835-9a3e-31d5d216179d | -15.67515 | -59.73408 | 2024-11-17 04:33:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79d72777-5d12-3dcd-b326-a7e2b6f2d076 | -17.59264 | -57.57343 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4c79e080-f1bb-3b66-9192-4e169115e364 | -16.07209 | -60.11009 | 2024-11-17 04:33:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e76920b0-d0d3-3d2c-92c4-5947eb048b61 | -17.60261 | -57.57058 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 68eb5281-3f9e-3de7-8250-5b9b404a845f | -17.56533 | -57.4677 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d31d6390-cde1-37d3-8793-f64fa04dff7e | -17.58886 | -57.59256 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0f016af3-7b04-3c56-94f0-659abb5d09d8 | -17.60073 | -57.58014 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| aa3df80e-6b82-3b95-bbae-1c10dc3532fc | -15.9192 | -59.82234 | 2024-11-17 04:33:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a11e2508-8b67-3827-a9f8-6f97086f5b8a | -20.99811 | -51.79658 | 2024-11-17 04:33:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 30a1aff6-81a7-3957-bdec-1d0adb0f9e0f | -17.59243 | -57.59832 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 1df429a6-f88a-3616-8f48-e9e3470646d1 | -15.92603 | -59.81636 | 2024-11-17 04:33:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2409eae4-fe6e-39a4-a010-c8b174c862f5 | -16.09693 | -60.10017 | 2024-11-17 04:33:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2d01149-1f1d-35e9-b2fe-fb074c7c2db8 | -27.05932 | -52.62471 | 2024-11-17 04:36:00 | NOAA-20 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| cbf40020-9628-3805-90ff-9305aed93bb7 | -25.19162 | -49.33003 | 2024-11-17 04:36:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e6d6f2ce-4d8c-3049-a149-bf7e20902a52 | -27.05601 | -52.62407 | 2024-11-17 04:36:00 | NOAA-20 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 1d57e084-5c54-39b6-949b-434a39b0c049 | -22.96242 | -54.43312 | 2024-11-17 04:36:00 | NOAA-20 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 29c25a7d-8436-3042-8d9d-ca421cae9078 | -23.04404 | -49.89565 | 2024-11-17 04:36:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 49719911-c00e-3d2d-8883-15a0d55e1b3a | -25.19223 | -49.32553 | 2024-11-17 04:36:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a6c1b3a1-db31-3a39-bf9c-6c4b4d797914 | -23.93847 | -54.08734 | 2024-11-17 04:36:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 9ec233e1-6d21-3e18-b8d3-998d46eaaac2 | -23.93011 | -55.41675 | 2024-11-17 04:36:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9abcfeba-f1d5-3ee4-8a91-9ec46b4071b5 | -23.93092 | -55.41224 | 2024-11-17 04:36:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 56487326-7bdc-3be5-8e86-21b45ba69465 | -24.24194 | -50.73984 | 2024-11-17 04:36:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 38750382-f7bb-3c3f-9927-5b7cc709eaa9 | -22.41458 | -54.17756 | 2024-11-17 04:36:00 | NOAA-20 | GLÓRIA DE DOURADOS | MATO GROSSO DO SUL | Brasil | 5004007 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9b557ac8-5649-3ecc-92b3-8fb54d4379bd | -26.54853 | -48.85359 | 2024-11-17 04:36:00 | NOAA-20 | SÃO JOÃO DO ITAPERIÚ | SANTA CATARINA | Brasil | 4216354 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5daacab5-b07e-3503-85d4-f79bc88efaac | -23.98444 | -48.91665 | 2024-11-17 04:36:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ec3f8c1-29cf-3e63-83f1-b909d1247625 | -28.95809 | -49.41657 | 2024-11-17 04:38:00 | NOAA-20 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0aee05af-94eb-3517-9dd1-cccf60e53f48 | -28.96177 | -49.41718 | 2024-11-17 04:38:00 | NOAA-20 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4c43b377-8ed0-38a1-a27f-94993c69fb5e | -29.13519 | -51.52522 | 2024-11-17 04:38:00 | NOAA-20 | BENTO GONÇALVES | RIO GRANDE DO SUL | Brasil | 4302105 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 18d15c2e-d2ef-39c9-9c2e-054dd19962ac | -28.57649 | -50.14762 | 2024-11-17 04:38:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 61ed3f5c-5220-3e46-b98b-65ed5764ea56 | -29.89901 | -54.93378 | 2024-11-17 04:38:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 9977e4b3-156b-3efa-81a4-ad7e985b90f2 | -29.90434 | -54.94343 | 2024-11-17 04:38:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| bf2914a7-a349-3ff9-95eb-6f22a7f2cbc6 | -29.74319 | -51.93596 | 2024-11-17 04:38:00 | NOAA-20 | TAQUARI | RIO GRANDE DO SUL | Brasil | 4321303 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| 3bfa0d92-6902-36ac-bf22-3c3acc683da3 | -28.95933 | -49.40676 | 2024-11-17 04:38:00 | NOAA-20 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e6c21913-f7db-3b9c-87e1-0cfbf32d5d6a | -28.95871 | -49.41167 | 2024-11-17 04:38:00 | NOAA-20 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 295d48e4-8af1-359d-be63-4156d0d2ddc8 | -28.95564 | -49.40615 | 2024-11-17 04:38:00 | NOAA-20 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3564f786-ab72-3750-ac9b-46ad4fde055a | -28.96239 | -49.41228 | 2024-11-17 04:38:00 | NOAA-20 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9dd58472-fac9-3615-b66e-62f8febdcd8f | -28.71158 | -52.54143 | 2024-11-17 04:38:00 | NOAA-20 | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 59be84c1-9a2f-3748-9b91-97bbbe449b27 | 0.6159 | -51.7881 | 2024-11-17 04:40:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 51.6 |
| eb74687a-3c84-3ea5-81ba-16556a33867e | -3.531 | -50.2337 | 2024-11-17 04:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 21e3d69f-935f-3d16-94d8-9ef065e58605 | -3.5309 | -50.2547 | 2024-11-17 04:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 1b8fc010-f68d-33d7-ad91-013602c457be | -4.5614 | -48.0141 | 2024-11-17 04:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| b9b4d80e-ecb6-33e1-98e6-5f7a9a28d870 | -17.6063 | -57.5715 | 2024-11-17 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 899b6946-6cf5-301b-b6d3-d02083a39601 | -4.5616 | -47.9925 | 2024-11-17 04:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 52cab3c1-5489-3eb7-85dd-82fa97b6eec7 | -2.6321 | -48.5849 | 2024-11-17 04:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 74296ab8-1927-3cd7-b3b4-ba2f284e9e69 | -2.8615 | -46.7086 | 2024-11-17 04:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 56590165-2bea-3177-93ca-42ed3b87bd28 | -2.6322 | -48.5634 | 2024-11-17 04:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 50020a76-4a2a-3efb-94a1-f2ae7c7d8632 | 0.6159 | -51.7676 | 2024-11-17 04:40:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 73.7 |
| eb28ea9d-539c-3683-ba46-2c6c46b2bcc9 | -17.6059 | -57.5921 | 2024-11-17 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 3d2479b6-5f54-35a4-8018-e397887b5c3c | -4.5614 | -48.0141 | 2024-11-17 04:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 0613b4fe-d5f4-34d4-ba3f-a3dafa6276f7 | -2.6322 | -48.5634 | 2024-11-17 04:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 71a48ed6-46b6-342e-9dd2-bfe6ab8f5b63 | -3.9422 | -42.8942 | 2024-11-17 04:50:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 0b3c0216-ed08-3127-bc0e-853f55dd27ff | -2.6137 | -48.5639 | 2024-11-17 04:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| e4718897-0bbb-354a-b332-f99eab12c8f6 | -3.9236 | -42.8952 | 2024-11-17 04:50:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 8f1e5497-49cf-3e2c-bcf1-dc1e4eb936c0 | 0.6159 | -51.7676 | 2024-11-17 04:50:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c225f249-4a87-3b6f-869f-5d9df29856bc | -3.9234 | -42.9187 | 2024-11-17 04:50:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 6d8483e9-6879-3654-b257-3a96f33e895a | -4.5616 | -47.9925 | 2024-11-17 04:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| bc0173d8-5072-3109-9eec-21abf1d3bb7f | 0.6159 | -51.7676 | 2024-11-17 05:00:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 0e3de2f5-759e-362d-a0eb-0ed5a4d37df0 | -2.6322 | -48.5634 | 2024-11-17 05:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 17fad060-124b-3e64-90ae-4d7258433d1e | -2.8615 | -46.7086 | 2024-11-17 05:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 98d527a3-4874-37c2-961b-59c1e370ceb7 | -3.9236 | -42.8952 | 2024-11-17 05:00:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| e6260110-f30f-37c0-b58a-61f874a6b109 | -4.5614 | -48.0141 | 2024-11-17 05:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 4ee42c05-b703-3865-b5b6-8133abe0d207 | 0.6159 | -51.7881 | 2024-11-17 05:00:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d2386ea4-be0c-31e9-8de0-b9e225685ecc | -4.5616 | -47.9925 | 2024-11-17 05:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 5bea4a94-f90f-380e-a478-7a525b819878 | -2.8614 | -46.7306 | 2024-11-17 05:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 9f5dcaca-167e-3584-857f-a30533148708 | -3.0537 | -45.2088 | 2024-11-17 05:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| c652290d-3702-3ed7-b524-88a8d36c43b2 | -3.5309 | -50.2547 | 2024-11-17 05:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 28222402-a7b0-357e-80ff-f075481e33dc | -3.9422 | -42.8942 | 2024-11-17 05:10:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 5ec7fc99-5fb3-31f8-96a6-b3cb888ef9ac | 0.6159 | -51.7676 | 2024-11-17 05:10:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 65.4 |
| ffbe2c5b-c5ba-3b31-9eb4-b893ccb16827 | -4.5424 | -45.2519 | 2024-11-17 05:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 7093f281-2014-3f11-a97f-ddd23f6fe369 | -2.6322 | -48.5634 | 2024-11-17 05:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 3290b31b-db4b-3e64-a3df-38ba50940a1f | -3.9236 | -42.8952 | 2024-11-17 05:10:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 4a52c597-8104-3b2b-81c0-8cdfa1105a23 | -4.5614 | -48.0141 | 2024-11-17 05:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 7fbce00a-4480-35f3-90e7-2aad46a2a1cf | -2.6137 | -48.5639 | 2024-11-17 05:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 7ba1873e-1512-3d69-824e-134bd8e3890b | 0.6159 | -51.7676 | 2024-11-17 05:20:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 72.8 |


[Clique aqui para ver as próximas entradas](README60.md)
