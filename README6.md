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
| 8bfe0ab4-0527-3ed4-9e92-2d0a860d4c01 | -4.25665 | -45.13105 | 2025-11-26 03:27:00 | NOAA-21 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3d0df609-0529-3ad4-8890-70890e320a76 | -4.15949 | -43.7347 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 673d45a5-afc3-39c1-843b-7593aecbd26c | -4.17901 | -43.73784 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b8215f8e-bcb4-3607-8992-4dbb948112ff | -3.47798 | -43.42878 | 2025-11-26 03:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3bfc3e2-1538-3d6b-b9f4-e5053ffd85a5 | -4.27194 | -45.12656 | 2025-11-26 03:27:00 | NOAA-21 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| afa92765-c213-33cc-9faa-59eaf08d7625 | -4.83854 | -38.6115 | 2025-11-26 03:27:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 349c93b2-76da-31f8-b48e-afc79af3fbbb | -4.2637 | -45.13223 | 2025-11-26 03:27:00 | NOAA-21 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 990d3af7-5c36-357d-923e-eb89bfd148fc | -4.23671 | -40.38913 | 2025-11-26 03:27:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 36b41c00-7b17-3416-8a3a-5f2c9fd25e74 | -4.17348 | -43.73116 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b4ac8053-3f0f-3689-a94c-ff1dd5107400 | -4.65729 | -43.97759 | 2025-11-26 03:27:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aa814fef-b8c4-3455-91aa-9c75d7d82613 | -4.17072 | -43.7085 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bdb732d-6a00-3f21-af3d-3bb5a72ac52a | -4.166 | -43.73572 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bb06828c-75fd-3ae2-8213-65b26bffc94a | -4.55666 | -43.29689 | 2025-11-26 03:27:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df9349da-ae73-3182-93b5-ff221b25406e | -4.16696 | -43.73018 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 8300c709-4f2b-37ea-aef3-a3d3c6fb033d | -5.60376 | -35.63321 | 2025-11-26 03:27:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 09435298-9535-3d09-8910-f37b38963222 | -4.16138 | -43.7238 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 42175526-4369-375e-bdae-a07784f18ba9 | -4.17922 | -43.73654 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d86acd2d-f871-3df5-8a9c-bc377f7a7783 | -4.17252 | -43.73671 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 93892567-a08b-30b8-af9a-f0c6463bd1b0 | -7.50688 | -38.33188 | 2025-11-26 03:29:00 | NOAA-21 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 638f946d-18e5-3e60-bb86-dac451d601b2 | -6.31068 | -43.79098 | 2025-11-26 03:29:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 32578995-d483-3c65-bcb4-c39bde7b55b7 | -6.30442 | -43.78963 | 2025-11-26 03:29:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| db178cd5-3b73-30e0-a8a9-8c3a2a100222 | -6.68933 | -42.47334 | 2025-11-26 03:29:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4dc8999d-bdb6-36b0-8ad7-144872df7fdb | -7.46211 | -45.18436 | 2025-11-26 03:29:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1818b86d-aa98-3671-afbc-f9a8804bef61 | -6.60544 | -35.22623 | 2025-11-26 03:29:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8079a9c2-112b-3c8c-891a-14bc6027e0c8 | -8.08123 | -41.08354 | 2025-11-26 03:29:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 92a74005-bf82-3df8-8ae6-da0aa005cb11 | -6.52294 | -38.98899 | 2025-11-26 03:29:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9ea325df-d0b5-3247-ab9f-59d502f8da25 | -5.04049 | -43.26343 | 2025-11-26 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 79de8ccc-f4e5-32e6-a021-ee4296c94091 | -5.29197 | -43.64042 | 2025-11-26 03:29:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 336c9e4f-988c-3a77-946c-e47294a4216b | -6.29985 | -43.79694 | 2025-11-26 03:29:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0faf35af-478c-3f7e-af6a-497357d1d490 | -4.91138 | -43.79618 | 2025-11-26 03:29:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58604b62-65e6-34e3-9a44-2d31484aa607 | -6.68859 | -42.47741 | 2025-11-26 03:29:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f6cc2e70-a3d0-36f3-a897-f145ac4ac1f6 | -6.51691 | -38.82972 | 2025-11-26 03:29:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| af6683f5-9d0a-3866-b387-319eeaa0eaed | -7.74884 | -44.19543 | 2025-11-26 03:29:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 95895be5-35e4-32cb-802f-3dc36c078c33 | -5.03512 | -43.25761 | 2025-11-26 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 19a29753-0975-3db0-a6cd-125fe09eacb8 | -6.74328 | -39.05145 | 2025-11-26 03:29:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| fd56236f-e138-3a3e-933a-a45f0ee41191 | -5.29412 | -43.64272 | 2025-11-26 03:29:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f3b5b02-efb5-3b60-91a7-3507ae1e333e | -5.63871 | -43.9238 | 2025-11-26 03:29:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6da6b969-25a8-31bc-b8de-e3d0bfe85a8e | -7.16912 | -44.99575 | 2025-11-26 03:29:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 91806f52-de4a-32b4-a436-995dd301a370 | -4.90495 | -43.79497 | 2025-11-26 03:29:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c33f7c70-2268-3529-8c27-c92319b1d728 | -5.28051 | -43.64551 | 2025-11-26 03:29:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9694230e-618b-3c4c-b286-f1a5c3b32b61 | -6.81313 | -38.57706 | 2025-11-26 03:29:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a98e67c6-c811-3ce9-84ce-ce8f46493137 | -9.97846 | -36.30192 | 2025-11-26 03:29:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a68698ea-fc4e-3cd6-811d-c0947054a490 | -5.03575 | -43.26543 | 2025-11-26 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0c8fa8b4-e53c-369f-a17a-b31b2448c283 | -6.72779 | -39.03184 | 2025-11-26 03:29:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e573e6d9-013e-323a-9c9c-171827b9663f | -4.81189 | -43.82799 | 2025-11-26 03:29:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f33b4e85-7b97-36f1-afc8-87c0195e1192 | -7.30172 | -45.43799 | 2025-11-26 03:29:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a29f68cd-20ff-3556-8744-0aa0d3ae841b | -5.03032 | -43.25968 | 2025-11-26 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d3bd766-65d3-3073-bc1f-ea1ca72ad527 | -9.98139 | -36.30692 | 2025-11-26 03:29:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 16441349-8e69-3b6d-bbb6-7d866c262881 | -8.54426 | -40.21667 | 2025-11-26 03:29:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 50523782-8c7d-3245-8d14-0f7898fc05eb | -5.28779 | -43.64147 | 2025-11-26 03:29:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cf2e9a07-b39c-35d5-a0f5-62f8fe4d0a34 | -7.05901 | -38.85818 | 2025-11-26 03:29:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 41dc6b98-d552-37f6-8906-d73caaadf0dc | -7.68066 | -37.0996 | 2025-11-26 03:29:00 | NOAA-21 | PRATA | PARAÍBA | Brasil | 2512200 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 23c07b51-b3aa-3c8d-95ce-7f389e397f9c | -5.28564 | -43.63915 | 2025-11-26 03:29:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e2280697-e826-3965-ac2f-48bf265e501c | -8.7147 | -36.65238 | 2025-11-26 03:29:00 | NOAA-21 | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6287fc6c-4abd-3ace-a75b-f1fb54a8a860 | -5.04286 | -43.26139 | 2025-11-26 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 430ae267-8af2-3f9c-884a-febda781552b | -7.7524 | -44.19429 | 2025-11-26 03:29:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3a989b1-b57f-36fe-bcc3-c8cce2626f07 | -6.81248 | -38.57521 | 2025-11-26 03:29:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6c51270e-b921-3520-b0cb-a2d9d11ae383 | -7.74978 | -44.19052 | 2025-11-26 03:29:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d7c3cb9b-abf5-3fc7-808e-76ea0a5df35b | -7.51122 | -45.72038 | 2025-11-26 03:29:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 17a0d20b-2726-3d8d-8df0-75f1b7965205 | -6.56016 | -39.01944 | 2025-11-26 03:29:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 904595f7-6683-3144-aa47-eb0022dd7cbf | -4.82602 | -43.82033 | 2025-11-26 03:29:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a69b5c47-455d-3479-9391-a44f4d57675a | -6.91869 | -38.85417 | 2025-11-26 03:29:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3f6cf59f-0d41-3d83-b03e-961ba41e9e48 | -6.30823 | -43.78696 | 2025-11-26 03:29:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 674b8098-dc1e-3232-99c1-01a367188ac6 | -7.15442 | -35.26709 | 2025-11-26 03:29:00 | NOAA-21 | RIACHÃO DO POÇO | PARAÍBA | Brasil | 2512762 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3f5b002e-ed9c-3137-9a07-014d4bf92bee | -6.30724 | -43.79222 | 2025-11-26 03:29:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fbdbe422-c043-3ec9-b6ba-a21737660a0d | -5.29106 | -43.64561 | 2025-11-26 03:29:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ea0f1ce-df07-39a4-823a-a24aff67d129 | -5.71827 | -39.50254 | 2025-11-26 03:29:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2914a5c8-80f1-3e47-9229-5b9f3b51d6c3 | -6.30535 | -43.78448 | 2025-11-26 03:29:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 525e89e3-d772-35de-b01a-86bf75e1c330 | -4.81118 | -43.82907 | 2025-11-26 03:29:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89f09d88-7fb9-32a4-a279-a2124932efe2 | -5.04138 | -43.2585 | 2025-11-26 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d1505c35-1a8c-3bb6-89a5-a4ca3b130e57 | -6.30343 | -43.79517 | 2025-11-26 03:29:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e144f8cc-33e9-3d3c-8f90-d5f92ccfece9 | -6.3023 | -43.80142 | 2025-11-26 03:29:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b22ff903-f96b-3457-b5b1-74bb2b0b1d8b | -7.16633 | -44.99298 | 2025-11-26 03:29:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3ec36eab-ea3d-3127-b8d9-641d5c1448e0 | -10.20751 | -36.36985 | 2025-11-26 03:29:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 1e85b6b0-0f66-3761-9e1c-eacb4c5ec4d0 | -4.81213 | -43.82363 | 2025-11-26 03:29:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0b404e2-f514-3858-ab9a-b65f2668ae14 | -7.26941 | -39.67173 | 2025-11-26 03:29:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 909e9e06-935e-3e6e-8785-54286fd3b784 | -5.03422 | -43.26258 | 2025-11-26 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 7afa48d0-475c-34d2-a31b-6a7326bd2a5b | -7.50995 | -45.72699 | 2025-11-26 03:29:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b552197-e321-3738-9041-02d5fdc8c91d | -5.41903 | -43.05601 | 2025-11-26 03:29:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 84017f14-c708-3f17-a671-0d6276e23ecb | -5.03747 | -43.25545 | 2025-11-26 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cb97c218-ab63-3436-93c6-b1f358a41e1b | -7.74616 | -44.19271 | 2025-11-26 03:29:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1c139e6d-b2b1-3966-b25f-e3de85f0a171 | -5.27839 | -43.64319 | 2025-11-26 03:29:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 921a6c60-834a-3c55-bf0b-87073ac7bbbd | -6.30618 | -43.79792 | 2025-11-26 03:29:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7173ceaf-2b23-30a6-9c9e-2c81fc7b87bd | -6.48483 | -38.82624 | 2025-11-26 03:29:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cb681709-1a2f-331e-b113-a9c36f69cc33 | -7.16243 | -44.99461 | 2025-11-26 03:29:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ca38f3e-bb44-389a-b949-aa249f90afb1 | -5.28473 | -43.64437 | 2025-11-26 03:29:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ddf89e0f-3973-3865-8866-f7c75639cdd3 | -5.03332 | -43.2676 | 2025-11-26 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c042eb07-01ee-3054-b342-1aad5b9aeb54 | -6.51835 | -38.98822 | 2025-11-26 03:29:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f2614d64-9510-30ce-a21a-d177c1eb1229 | -6.95475 | -39.13724 | 2025-11-26 03:29:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ef630af3-3b80-3ca6-8968-8375177871a9 | -6.49015 | -38.82243 | 2025-11-26 03:29:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bb974b0e-d412-3b81-8ed0-acf8c79f41db | -6.51308 | -38.8248 | 2025-11-26 03:29:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b432c6ea-23a4-38f5-944b-7a4e1bcd72d9 | -6.95938 | -39.13786 | 2025-11-26 03:29:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 571ae4c4-986c-38f1-a1af-6293c5be826f | -6.60419 | -35.22653 | 2025-11-26 03:29:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6ac01901-ca1a-3868-be84-1cf798577bd6 | -9.29229 | -35.60039 | 2025-11-26 03:29:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| fc8b81c1-c53c-3fa8-9598-9924180f0468 | -5.28146 | -43.64031 | 2025-11-26 03:29:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 117fce14-3cad-361c-abe0-3f2291b0b73f | -5.03662 | -43.26039 | 2025-11-26 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 340d1532-17c9-3261-b06c-5f0abcf10cdf | -20.57844 | -45.87053 | 2025-11-26 03:34:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edf6e846-8a41-3df6-8f20-cfda3eaffb0a | -22.47447 | -49.1301 | 2025-11-26 03:34:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f73c32b3-5cd9-3b6d-87cc-16a58c477c6d | -20.57014 | -45.88177 | 2025-11-26 03:34:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9e976bad-25e7-3f2c-9991-baacedb43200 | -20.57582 | -45.88241 | 2025-11-26 03:34:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README7.md)
