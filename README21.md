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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3b745a9-0b68-3cad-a178-7a08367f5a04 | -3.29178 | -43.55021 | 2024-11-10 03:19:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6ca9e40-3593-31a3-b36c-9f316ddcc655 | -2.9989 | -40.28316 | 2024-11-10 03:19:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e0a7513f-3011-3f62-ba93-5749abf6b882 | -1.476 | -54.2965 | 2024-11-10 03:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| db879abd-c212-33bb-b148-041af374272a | -2.8802 | -51.4835 | 2024-11-10 03:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3869d728-6129-3aac-9934-1fca52286271 | -1.5347 | -52.2104 | 2024-11-10 03:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 621f7eb2-2ec7-3f0d-8fd4-7726a097b184 | -3.9668 | -48.1932 | 2024-11-10 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| f454c8e9-5b8f-3bfa-8447-20632012533f | -17.627 | -57.5075 | 2024-11-10 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 245.1 |
| 6a415109-e4f6-3410-97fe-e4dc230a87ff | -3.9485 | -48.1508 | 2024-11-10 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| bf729aed-6773-358d-ba2e-0c7bc73a3d34 | -4.11 | -49.1102 | 2024-11-10 03:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| cb2eaaf0-6cc6-3df4-a079-679efd82c02e | -3.6004 | -47.3395 | 2024-11-10 03:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 029d1bbe-5549-3085-805c-f7af875c20d4 | -2.7587 | -49.3497 | 2024-11-10 03:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| e54140cf-2010-3cdf-b2fa-3f771eebd828 | -8.3967 | -44.1365 | 2024-11-10 03:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 235.9 |
| 9a506f4d-ffc0-338c-9a45-02900233ace5 | -8.3964 | -44.1597 | 2024-11-10 03:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 280953a4-6175-3a41-bda7-ed308340ce3e | -2.931 | -52.7753 | 2024-11-10 03:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 81201ce8-3597-3b7a-9bb6-da7b2b4f6f94 | -8.4153 | -44.1576 | 2024-11-10 03:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 7be2b34f-88cd-3104-8eaa-c0a27f112fe6 | -3.5064 | -44.0294 | 2024-11-10 03:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| e7f87e2e-a1f9-38dc-9971-a7fa22fb9b06 | -17.2933 | -57.4857 | 2024-11-10 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.1 |
| 7adf874d-e15a-3fd4-9891-26d9a9e031df | -2.9355 | -51.482 | 2024-11-10 03:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 38b9e5a0-238f-3975-b67c-20324e1c2526 | -17.6266 | -57.5281 | 2024-11-10 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 272.8 |
| 939d20ca-47af-35a2-92b0-8d392f348536 | -2.0953 | -48.8338 | 2024-11-10 03:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| cf79cc27-0eec-37b6-8e63-aaed3170c9fe | -2.418 | -46.3024 | 2024-11-10 03:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 43.0 |
| f80b928c-71a3-3c06-a93e-ebeb0d80889a | -3.9483 | -48.1724 | 2024-11-10 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| a2da1789-2690-3ff1-9834-0fd24efb7c58 | -3.4383 | -50.2999 | 2024-11-10 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| d5602a5d-925a-3e3f-bbb8-38e2fe83f374 | -2.9171 | -51.4825 | 2024-11-10 03:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 6a510cef-759e-300c-8c9a-f99c0ed7ebba | -17.293 | -57.5062 | 2024-11-10 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.4 |
| 43e939af-c860-301c-a3f4-6cb23ac6ae9d | -8.3775 | -44.1617 | 2024-11-10 03:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| d69bfdb1-5094-376d-8102-2ff8984436ec | -8.4156 | -44.1344 | 2024-11-10 03:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 28f05464-f173-3e89-8146-eb71e9d1ed34 | -1.2751 | -53.7164 | 2024-11-10 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 876a9ceb-c364-3dd3-851c-2dba9316c355 | -17.6073 | -57.5099 | 2024-11-10 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 439.1 |
| a9b37439-e97a-3c20-ac58-174fe33d62ef | -17.6069 | -57.5304 | 2024-11-10 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 470.2 |
| 890130e6-c1a0-3ddf-af5a-36e24e5f32ba | -4.1099 | -49.1315 | 2024-11-10 03:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 8721adde-8cd7-33dd-80f6-c66ecc469d43 | -8.3778 | -44.1386 | 2024-11-10 03:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 171.9 |
| ac4acfe3-6591-3ba7-ab49-3662556068bc | -3.9669 | -48.1716 | 2024-11-10 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 8ff688ca-15b7-39ee-ab9a-a4afce9f08b5 | -3.3518 | -53.4139 | 2024-11-10 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 83dd7589-087a-3a2c-ac26-2e0be6699589 | -1.2751 | -53.6963 | 2024-11-10 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c02e4335-3c1d-3004-bad2-c3f49ea75d9f | -1.2934 | -53.7163 | 2024-11-10 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 8eeef777-9074-3021-9d11-2753571aaa14 | -2.7772 | -49.3492 | 2024-11-10 03:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| c1d3f65c-ad5e-3801-9725-a6c01f7440b9 | -2.8803 | -51.4628 | 2024-11-10 03:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| d6893528-884d-3dc8-93d0-c677d5e7c0ce | -6.33602 | -39.62284 | 2024-11-10 03:21:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f34d7c22-3c3d-3dc0-8cb0-b640a716df8d | -7.62784 | -43.56584 | 2024-11-10 03:21:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b2212449-78ce-3788-8c74-0c5992d60d8c | -10.00671 | -36.0144 | 2024-11-10 03:21:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 64a2bf38-f662-37ab-b023-a4d43c6c7cde | -8.38753 | -44.14641 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c87c6225-a4f3-3328-9466-2248a437965d | -8.39436 | -44.14764 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d5f16485-0104-3de0-b587-e0766681a0fa | -10.945 | -40.82094 | 2024-11-10 03:21:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 4b32b026-f2ac-3925-850b-ef6adec4a302 | -7.13961 | -34.99813 | 2024-11-10 03:21:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 536db170-c921-3b11-a12b-f019b477e30c | -7.43077 | -39.77131 | 2024-11-10 03:21:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1ffd72a6-2d50-3f85-bde0-ca3aaff915d9 | -8.40245 | -44.14256 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 94299d21-6797-37a3-b94c-373c1ad557d8 | -8.37157 | -44.15085 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| f87c409e-a591-35ae-8e90-30f6b2a4b31b | -11.1428 | -37.4305 | 2024-11-10 03:21:00 | NOAA-20 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bd56636c-b6e2-38eb-9974-1dd08a7e9240 | -5.56732 | -43.98117 | 2024-11-10 03:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9fca7c91-2679-3871-94d8-d7e9ca9a1419 | -4.11685 | -43.60561 | 2024-11-10 03:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a2b87023-c6d8-33b4-b8b3-5a4e2511ed52 | -11.1855 | -37.33577 | 2024-11-10 03:21:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8a2d809c-e678-36f0-9d9a-bc9068f92755 | -8.38642 | -44.14725 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 32.6 |
| cf9d55dd-db70-358c-b1f3-05f504f3bc1b | -8.37839 | -44.1522 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| b9bb716e-a2ca-3f99-8a5b-b811e9ba468d | -6.73242 | -40.81613 | 2024-11-10 03:21:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2bd34b79-9bab-3981-abe8-ce2333811de3 | -7.4365 | -39.76979 | 2024-11-10 03:21:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d67d3dd7-ab0d-3541-a574-90d456cf15bb | -7.1857 | -35.06295 | 2024-11-10 03:21:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| af84ebd9-53ee-34d1-b2c8-db425733ee52 | -6.46459 | -40.77933 | 2024-11-10 03:21:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 27c36b15-08a8-363a-8e1b-d3c96e13b309 | -8.3796 | -44.14592 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 84b21473-f642-30e2-a9d9-ad84c800e46d | -8.39446 | -44.14222 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| edc72b25-70cb-3c5f-9649-e33aa9db6622 | -8.4057 | -44.15738 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9d4e0e81-d9c9-3ff4-b389-acc72b2b1828 | -8.39311 | -44.15393 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d1fb3f41-f3b6-36a8-a211-21fe8f93b033 | -5.7204 | -42.67897 | 2024-11-10 03:21:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 41453c49-a080-3504-abda-9a579c560150 | -7.47463 | -34.84462 | 2024-11-10 03:21:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 91db1469-7100-3444-a8ef-a16f59c8e7f4 | -6.46349 | -40.7793 | 2024-11-10 03:21:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0226416f-161d-3b3f-9f7f-3ca9e7968846 | -8.4012 | -44.14886 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 6d8eca7a-dea6-3b42-b111-988ba59ab96a | -6.15319 | -41.15021 | 2024-11-10 03:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9af4b008-b30d-3775-935e-5cfccbdfd0f0 | -7.43231 | -39.76279 | 2024-11-10 03:21:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b8da3a42-1d2a-3091-a65d-2a2fee25fb60 | -4.39252 | -41.91322 | 2024-11-10 03:21:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 28cc963b-0fcb-3fcc-91c6-200322f9506f | -7.436 | -39.77256 | 2024-11-10 03:21:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2f26a3ae-6f9a-3c7d-a22c-cb0255772c7e | -11.1897 | -37.33658 | 2024-11-10 03:21:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2f6730cb-6283-3ee8-8e99-b997f5ccc4ca | -5.68745 | -38.0404 | 2024-11-10 03:21:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f7ae6adb-944d-31e3-95f4-1974ef961fe9 | -4.39978 | -41.90923 | 2024-11-10 03:21:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7d193a10-1354-3272-b3d9-5aa99a583b05 | -6.4025 | -42.49388 | 2024-11-10 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 996642f3-e180-359a-93b7-370aa71bd4ed | -7.1158 | -39.72208 | 2024-11-10 03:21:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 594b1177-a3b7-3dfd-9f42-9ab3a0174e72 | -8.40812 | -44.14469 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| c475cf2b-f067-3091-9620-119a981a57c5 | -8.37278 | -44.14458 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| bfe41314-5854-3b4d-a1f0-64c9f3abc181 | -5.09735 | -37.96195 | 2024-11-10 03:21:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5c8088d4-669d-3be1-ba86-d5d05485212b | -4.11399 | -43.60459 | 2024-11-10 03:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ac251314-b388-373f-94ac-7adf264fbc03 | -5.27059 | -37.94952 | 2024-11-10 03:21:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2e14ce2d-6574-3126-8164-c4e702598e60 | -6.24518 | -43.57132 | 2024-11-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3410b881-627a-3032-93e2-077f94ddc281 | -4.39343 | -41.90801 | 2024-11-10 03:21:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 698fd7d7-c786-3ce3-a0b7-71f8b4f31e7e | -7.43702 | -39.76692 | 2024-11-10 03:21:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0b641c3e-cd9f-3f4f-b8d0-7cf286227ea8 | -6.73169 | -40.82022 | 2024-11-10 03:21:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 52f315db-db53-3151-9e43-2006a2fa8939 | -10.94372 | -40.82776 | 2024-11-10 03:21:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| a688c903-57fa-3907-8b1f-46aea71890ea | -5.56573 | -43.973 | 2024-11-10 03:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efed6de1-a8dd-3310-877f-c1cca1cb78e6 | -4.0101 | -43.67191 | 2024-11-10 03:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21925c0f-b62e-3df7-a0f6-0f4e56512f6e | -10.20687 | -36.34854 | 2024-11-10 03:21:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ec7c30d3-e157-38b0-8eb6-0d9561f2fb57 | -8.39995 | -44.15517 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 5e3c3059-0b07-313b-af7c-3e0b80eaaf32 | -6.24652 | -43.56403 | 2024-11-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1483571f-03e3-34df-b376-d2b4228f2c2e | -11.18991 | -37.33618 | 2024-11-10 03:21:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 75c7e886-af17-36ad-b3e2-d0e02dc8a050 | -6.7267 | -40.8151 | 2024-11-10 03:21:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7530978d-5ec2-3952-b346-e8f46f082120 | -10.94436 | -40.82436 | 2024-11-10 03:21:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| d7675013-a941-35e5-9bfc-1007d825ff2c | -4.11519 | -43.59803 | 2024-11-10 03:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a4331379-99d5-322f-8352-2792ce655f1b | -8.40129 | -44.14346 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 5a1325c2-52b5-3647-8f97-c3b17a34d229 | -6.70033 | -40.45742 | 2024-11-10 03:21:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6e0eab58-dad6-3fa2-ae44-95272fb3bada | -4.85668 | -43.97731 | 2024-11-10 03:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1cfe11a-0b47-3604-999f-0e1638390feb | -7.43128 | -39.76851 | 2024-11-10 03:21:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 8.7 |
| fdd059f8-ceb2-3a4a-8675-f7a2b7884d06 | -5.56857 | -43.97421 | 2024-11-10 03:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 39938593-8fe9-3533-8885-25be1540b520 | -8.40803 | -44.15009 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |


[Clique aqui para ver as próximas entradas](README22.md)
