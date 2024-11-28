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
| e3cb4cdc-6d4a-3b22-8f52-44f948aebc4c | -3.97716 | -46.65127 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed03ed78-a299-3dd5-aeb9-6e5a521bf028 | -3.28213 | -46.1923 | 2024-11-28 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e47e140-7cd5-349f-840b-8da5d6ce17f3 | -4.18535 | -44.26884 | 2024-11-28 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 484891f0-4e8a-3e82-8dd2-ce5234de524e | -2.57957 | -48.07331 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e35bba46-3c4c-3bd6-ad28-e4003aa0d539 | -3.18669 | -48.12778 | 2024-11-28 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bbc671e-f896-34ea-897d-d861a5f2ee5f | -3.24891 | -50.6143 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f88eb2c2-d37c-3b67-8026-3c396f69d8d1 | -3.47 | -50.53758 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8af5bdf-9ee8-378b-99da-6b95df181af0 | -3.0499 | -53.6786 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a9c89b5-003f-367e-8bc3-0b5c0a6377fc | -4.19922 | -48.56512 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88557636-c4e8-361a-9734-7acf2866f759 | -4.50706 | -42.07256 | 2024-11-28 04:25:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7c45d502-41fa-380a-b3ec-8b65350eea00 | -3.81252 | -52.2379 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6e6c34c-fe5a-37da-b749-f3197344e6d6 | -1.62216 | -53.87224 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c22a02c1-1628-3f86-b069-15789e747d6a | -3.1935 | -50.82517 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c82e458a-7dbc-341b-941b-9bf806055f9c | -3.70586 | -43.4314 | 2024-11-28 04:25:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9b02c41a-f231-38aa-9949-5fdf4659054b | -3.74841 | -51.78155 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5b6a3e8-8907-3950-8dd0-3a4664ee65db | -3.29419 | -45.51222 | 2024-11-28 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 99e57899-364c-3f02-ae2e-884346419fe5 | -3.20108 | -46.59513 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b9f73e48-68fe-32e1-8a1f-56e4cee6e0aa | -3.29329 | -50.54509 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97232ea6-ddaa-3289-b227-226606c47a20 | -2.94999 | -48.33805 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8656b433-1d06-35b6-b9c2-6b4c39e82b80 | -2.87231 | -46.80512 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e71e02a-eb9b-3216-9775-6e7ee545adcc | -3.80729 | -46.60996 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fb31cfb-4464-371f-a25e-f1904ec90a1b | -3.91503 | -46.53031 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0387656c-f70e-33bc-ad43-414d16b4db8a | -3.85112 | -47.06429 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d6d521a-53f6-3df8-89e6-54392fc1fa6e | -3.24069 | -46.43212 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c24371c9-7ec1-3dbe-ae1a-e9230fc26762 | -4.61832 | -49.58138 | 2024-11-28 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 741b925e-1ede-38a4-a3d2-8aae1343caba | -3.65036 | -51.39408 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f13526a3-a2a5-3c74-a38c-93295094127e | -2.98223 | -53.89534 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f1a3ef8-6b2b-345d-9551-b5da0f10ff71 | -2.87039 | -53.98163 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa282da0-fdb0-3cf9-9bdd-17aa3691b63a | -2.8368 | -51.84258 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9ce188cc-9854-3ea6-bdb6-9acff91c3209 | -1.49592 | -54.46242 | 2024-11-28 04:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9c63f9b7-b736-360d-824b-269e953f9ff1 | -3.7193 | -52.01762 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 408420f7-d095-35d5-b8bc-f8f65657720d | -3.50079 | -53.80963 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7c01135c-af59-3124-955c-650a22cde53a | -14.91158 | -52.87023 | 2024-11-28 04:25:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7367ea4e-aa95-3eee-a014-19d791993b38 | -2.75308 | -54.13247 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 425346b9-bc68-3fe4-8b1a-53d17cf775f3 | -3.99874 | -46.32232 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de7f3d42-a5ea-3fe5-84af-6eb1f827aef7 | -3.19784 | -48.58423 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2628180-25cd-3365-acae-0ec98216617f | -2.8615 | -46.87316 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 524788d5-368b-3471-934c-0804910acab1 | -3.38317 | -50.10924 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3da38a85-a511-37ab-9c69-8d37e037e41b | -3.70737 | -51.81371 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccf053df-dec6-3c18-b4d1-264de9b4932a | -2.73583 | -51.65921 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b6a8623-7035-37b2-b83f-690f66ba65eb | -4.04273 | -48.25642 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8f016d1-275d-3f79-a9dc-b8564104789b | -2.85647 | -46.86133 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4522faf4-458f-3be8-bd28-e40cb34ada90 | -3.17268 | -48.44149 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0297cf1d-d82e-3791-bc07-90c986241dbf | -3.33673 | -50.51196 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 653eb54c-8936-32c7-83a4-2ffc26e3f66e | -3.46377 | -43.52547 | 2024-11-28 04:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 37a192be-92da-30e0-9a74-6e9fd0ab0474 | -4.5128 | -45.79846 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32b1ae73-3fe0-3aca-bfbd-f18cef77a268 | -3.34881 | -50.51384 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0313771-0ea0-3902-b058-d60dff36fa6e | -4.20707 | -46.55148 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 76c9d4a7-fe54-3a63-9a7e-cca1b14f12df | -3.97856 | -46.98877 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 311aeb85-23e5-368e-a551-837cf8ecd558 | -4.6743 | -44.61723 | 2024-11-28 04:25:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 26ce5452-6ae6-3e45-80ef-580eff8a1e19 | -3.68967 | -50.22662 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2977a494-5ab4-38db-9a6c-acae1ca8e847 | -3.94654 | -46.69323 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e86d11b9-4e17-3674-a7a2-56726133b191 | -2.88109 | -52.68857 | 2024-11-28 04:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 247bcce6-77dc-320b-9b7c-1442a04ed556 | -5.20804 | -41.28453 | 2024-11-28 04:25:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ca0d1c69-6a36-3c43-9b13-a468826afa64 | -3.09346 | -50.36222 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7713650-429b-3be3-ab46-d4421aeeb7ca | -3.9451 | -46.91765 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6abc963e-1326-373f-8357-3614f56b2e82 | -4.03545 | -46.542 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5226e6f8-eabc-39f0-8a87-2550b08ee8f5 | -3.83667 | -46.53205 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e28f438-894e-36b3-a305-66fd14e7748d | -2.9346 | -48.02587 | 2024-11-28 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8da02fa0-21ca-3901-8d44-9580a7b15017 | -4.13807 | -46.36588 | 2024-11-28 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75b10c23-c64d-305b-bb84-38de0cd40090 | -2.72521 | -48.89489 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 600a577c-6485-3938-a900-d47350bd2cc9 | -2.85896 | -51.84626 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d0b0fe9-7919-3fe4-890d-441c171d2f77 | -2.8299 | -54.11948 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f16ee3d1-9453-3a38-a96a-2da0d4d25763 | -3.4779 | -50.31472 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9384d18-15ca-31c5-b031-f0a317805df0 | -3.43456 | -51.20483 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2b76b69-11ce-3478-bad2-a6803960cd24 | -3.04854 | -48.51487 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe4bc8c5-ae02-341b-a2d9-dd8415bfe060 | -4.23186 | -46.02982 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed669881-b743-30e3-9e7c-a1547da87172 | -3.90016 | -46.12914 | 2024-11-28 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e78fdc1-a50b-363d-84c5-b9e3aa0716fe | -3.91351 | -47.20303 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b071c555-5062-3dcc-b89d-c71b49a0910b | -2.01801 | -52.07887 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66658b6f-27f4-3a80-8aea-400adab7853e | -3.10582 | -53.26736 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2551cc1f-d8e2-33b7-94dc-51a18da8be47 | -3.39748 | -50.70084 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a1ab5aa-8326-3565-b1fb-1494eb995e70 | -3.37925 | -50.10861 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2d356dad-86f1-3b5f-bd86-f041985a3722 | -3.62478 | -44.04816 | 2024-11-28 04:25:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 0ba40102-637a-39b2-9cd7-d0527ede1c00 | -2.94013 | -51.59205 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7032f775-a2ed-3d98-bda5-7e5335339c37 | -2.00042 | -51.04489 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e41cda5-8bc5-39b1-9785-f2cae1b1b161 | -16.34817 | -43.6982 | 2024-11-28 04:25:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 931c2a9f-1c13-3eeb-9ef1-5ec2edda00ee | -2.85538 | -46.84645 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e236dbe6-e4c9-37db-8ff0-d68caee129d1 | -2.95999 | -53.88512 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 004a388d-768a-34c7-a5c3-1bbacf2866ed | -3.90845 | -47.71854 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15b6808c-042b-3084-b970-7008ae0a7659 | -4.7375 | -46.50676 | 2024-11-28 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c8693db-7a18-3b35-bbe8-584d48bca8b8 | -3.92998 | -48.14765 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3e737aa-5acb-36a8-914e-4ea2ec08d949 | -3.76277 | -46.67508 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f5cd499-bbae-3055-8712-35c3f16db264 | -2.69576 | -51.68339 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9814fd56-ebda-36d0-8951-534f5bd1fbc1 | -2.62436 | -53.99389 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d9eea2c-57f6-3fc2-9863-72d9b62878ba | -3.64589 | -50.17334 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17448194-fc1f-382f-8aba-29b0ac27d1be | -2.71944 | -48.9136 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7826ebb7-d141-32b7-84ce-b95dc865459a | -2.25391 | -53.75131 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6769d330-cb3b-359f-9d7a-8d798cce36cc | -3.37766 | -50.11859 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 2bbe143f-ea52-3f62-86c1-f6f06fcdef27 | -5.22777 | -44.91957 | 2024-11-28 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d55d3778-a432-38db-bc88-9d76d1d94c70 | -3.27031 | -48.76545 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 850c2335-5492-36c4-a0b3-b08d74596540 | -2.86894 | -46.80459 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 187929fc-bcb0-3151-b6f8-d5d18dab90d7 | -3.34845 | -53.73695 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb1d0b36-9c0a-3751-b1d5-d416c3b2548c | -4.83237 | -46.91565 | 2024-11-28 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f4f99aa2-d004-3b72-939c-303802562825 | -2.95421 | -48.33457 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ca8689c-0ef7-3d7f-a330-5d7e6a02e6b5 | -2.87783 | -46.85734 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ceccecae-c9a3-3ebd-923b-2781ea1534aa | -2.83712 | -54.11566 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2ba6ada6-59d1-3907-8c4f-8cc398b8865f | -2.80566 | -51.58833 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a2cdc013-101f-3283-a3ef-5fcd2f64635d | -4.17443 | -48.62751 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 599b7987-6b6c-3fcd-b7e8-fe0f32393798 | -2.85652 | -46.83928 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README62.md)
