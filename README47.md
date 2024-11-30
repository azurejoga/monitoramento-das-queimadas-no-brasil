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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b2998c1-77c7-3bfa-9d35-9d8fdb7e2824 | -5.04243 | -43.62511 | 2024-11-30 04:40:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b0ca669-2e32-313b-8b1b-799fb350b2ad | -2.69518 | -48.59863 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0d79ff8-30ed-3ad5-8989-a6101531cdb2 | -4.19762 | -46.35043 | 2024-11-30 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77ae6435-3d94-3416-ab24-30e1e112a060 | -3.10794 | -53.80499 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b8ba4b21-965f-3ba1-838c-f111158d6fa7 | -2.60869 | -46.5751 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9a79a41-a1cd-3586-a9ef-b207f0a909b1 | -3.93924 | -49.90923 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b8c9471-daf5-3912-9817-33d4b81dc40c | -6.79094 | -39.45054 | 2024-11-30 04:40:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5922baf2-a3be-3564-a8dd-51002e6ca44d | -3.82378 | -46.59917 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13fbee67-7b83-334d-a780-a887f3829fb4 | -4.05491 | -48.33977 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7188930a-0389-35a2-b5d2-54e8e1d384c2 | -4.04191 | -41.90725 | 2024-11-30 04:40:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7b5ebf0e-2191-3ce7-b270-e6f00b95c5d4 | -3.345 | -50.74523 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2ddee2b4-afdb-3b41-a8c7-21cce52daa45 | -2.68207 | -46.10206 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76d728dc-6d0c-33f4-b49d-98787b8b28ca | -1.83211 | -54.521 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f7b649f9-db22-36de-b8fd-4f5b7c0bd800 | -2.95204 | -48.5861 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cec85654-9998-3528-abfd-26a105d3c542 | -3.05691 | -51.057 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 005549e5-8a6e-33ca-ba17-b28cedf90913 | -2.7654 | -55.33208 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df717bd6-278c-3ba0-9137-680c535c9ef3 | -1.36845 | -51.38947 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28483b31-ac8b-3043-a118-d71d617bdaa9 | -5.1282 | -45.11068 | 2024-11-30 04:40:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b1e47a8-6c7b-3410-a800-ff4e7c144f6b | -2.11206 | -46.56261 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c716161c-90f3-3eec-ab51-5b8a279b9243 | -1.34168 | -54.98311 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 842ec104-37b7-3ba7-9e1b-1f232a8b60f3 | -2.17 | -48.41085 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a710f62-9021-38c5-bd5d-e025a16c9e2d | -2.27548 | -48.49804 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 722532d2-afa2-388a-ba8a-76e7d71ebe53 | -2.98634 | -53.28756 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2f9595c-df40-38e3-a3dd-0c411413bde9 | -3.39024 | -50.15361 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4dfb142-4a38-3040-b8bd-781d54934081 | -2.86533 | -48.09444 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37dda925-840d-3cc8-bcd4-49834c18454f | -6.7087 | -47.27103 | 2024-11-30 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 193fff87-78b7-35d5-981e-f2318a4dad6d | -2.22947 | -53.68868 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa92c711-901f-3293-9782-17b27d991905 | -2.32036 | -51.95513 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbe9a8d0-7082-3939-9e8f-a3a0dde714ec | -3.17711 | -48.58212 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f26b274e-8514-305a-ba67-8533bc1058e0 | -6.68554 | -39.26189 | 2024-11-30 04:40:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e52035ad-9d59-3ac5-931c-f7a5b7053f3d | -2.58965 | -53.96972 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6cefc839-614a-3c37-94b7-86bcb4853253 | -4.02712 | -48.89164 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3567728-c0e4-3285-a6b7-f64e15badf17 | -2.88721 | -48.87157 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 704ca2b1-4351-3872-91b1-c4aa38b6f627 | -3.24737 | -54.21502 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e19c6611-9dd2-364c-a25f-3106381b5654 | -3.34961 | -49.91651 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 390dbef4-792b-37ab-b680-72b1eb36c14e | -3.39062 | -54.28278 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef1f26ef-47d5-3f32-8cb4-2b39eec33192 | -2.60928 | -46.5713 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c483aa8-c21a-3a57-9ce0-7eb21af2914c | -3.99266 | -41.50863 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e4df6bb7-0940-316e-af10-14ee5cec60a5 | -3.30451 | -51.06841 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41671053-cb6b-3d0d-8024-a1dc9ce7b00e | -4.67219 | -46.37319 | 2024-11-30 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 042a97a6-c0f7-3391-a2e2-6a38f4bd2ff8 | -2.51417 | -47.41728 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 569798e3-76c6-323b-b262-82850c4669ba | -2.19885 | -48.33428 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74a6e966-1903-3690-b8eb-7534b486a962 | -3.07104 | -50.99017 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc90760c-e452-39c3-a83c-6521759b4484 | -0.87812 | -53.68391 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 081a68ce-8cbd-31a8-86da-1d39e3321b26 | -2.47444 | -50.36137 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee473a52-74bb-38f9-be87-74edd8990b90 | -2.63297 | -51.76155 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec24445b-e032-3ffb-9dd7-09b31fa05abe | -1.55778 | -51.26802 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc411448-d5c1-353f-841a-51c689376a56 | -1.7562 | -53.64973 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bdc216c-0936-352c-b7ea-b4670f4528e5 | -3.59152 | -49.97964 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 718c1ae4-1ee7-3e67-8ec0-61a83986470b | -1.71249 | -52.49308 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ec5d2d5-82a3-3902-8910-4178f6c9249a | -3.93897 | -47.98772 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c8420f03-16ab-3a50-80e7-53c2b55441a1 | -1.20346 | -53.86923 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ae91adf7-c59c-3d46-b86c-ccfa07513a5e | -4.29597 | -50.75172 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e801279f-fdf0-3015-859c-f1c62d03913b | -3.68142 | -44.70243 | 2024-11-30 04:40:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3773a5f7-e738-364e-a28a-8923fb105f3f | -3.43982 | -50.12155 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f2b046f-6fa7-349c-805b-f9b57254a69d | -3.54398 | -50.19537 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bae53149-516a-3b8e-a926-8c381900f627 | -3.0267 | -49.52411 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46f13e97-aaa7-3159-aa2f-81d0c2852cef | -3.18768 | -46.56606 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd80e40c-d4df-3510-adeb-2378b8f29fc2 | -3.2877 | -53.28114 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53ac3244-e7b3-3c4f-8012-33a343fe967c | -3.00235 | -49.50618 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25d4546c-7c46-30c3-ab17-faafd17625f5 | -2.02025 | -51.19236 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7045734-c603-359b-9a6b-c414f67acc83 | -4.04431 | -46.83676 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0c5d472-eb42-353c-ba30-208d48df4361 | -3.77697 | -53.4209 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8f48f8da-64b7-3bea-8310-143b63ecc785 | -4.00271 | -48.30319 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 071eb50b-9dbf-3902-a509-bc9de6334cab | -1.97505 | -52.89397 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff36a613-6e89-3112-9892-a00f0f935eb7 | -2.72903 | -48.66364 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dae25d44-2163-319b-b5bd-7a935946d7c1 | -1.62613 | -53.86119 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77f4a8fb-0dae-3d92-9195-d0ab89612cd5 | -3.75726 | -49.94156 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 32f4a77c-34d1-3d34-a218-fa3fe3035dd7 | -1.42646 | -55.27322 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e57248b-9c31-3fdb-aa55-ec68e1030358 | -1.70552 | -52.63913 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 684c44f4-6212-3316-9dc8-1a6ef655ba04 | -1.58323 | -53.84356 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d26f0d43-bd40-36cd-8e83-5340e8a20217 | -3.1034 | -53.80788 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba4614c7-85c6-3514-a10d-73d59f40b52e | -2.80862 | -53.04474 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 675e75fd-58a3-3dce-abee-a6e0d33273c9 | -4.86627 | -44.01075 | 2024-11-30 04:40:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 463cd612-c33c-30c6-af06-7276055d98c7 | -2.55738 | -47.03977 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d354245e-2664-3ea0-b4eb-418308ba8246 | -1.70529 | -52.76232 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 670884d2-78d1-3d4d-bdf7-e63959bfdeca | -3.07877 | -50.25361 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6cb77ae-ddc9-3457-af5d-dd3ab7812605 | -1.71784 | -52.68345 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a1c4ba2-4af8-31be-a025-f4bbe07addee | -1.25144 | -51.745 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b086955-2b16-34f9-8927-f7a20928b052 | -1.62561 | -53.8906 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1877e09b-c8f8-3b0a-b381-ff183891a10c | -4.17685 | -48.62864 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52c58627-c96c-3971-9432-15421185cdfe | -3.97266 | -41.51081 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| d0253c0c-9ac3-3093-bb73-d0a22efa330b | -2.63531 | -46.87794 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1570741-02ad-39cd-91ae-015eff6373bd | -3.16718 | -51.09293 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d94a1320-e7cb-3163-bd6b-76f80c44c08a | -0.9578 | -51.65579 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b15427a0-7ece-3713-b009-576bcc5b4255 | -4.38244 | -50.93584 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f91024dd-ae54-3a49-b2f6-bec575015e7e | -1.1383 | -53.7017 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e6dee76-f05c-36ad-8919-c371c677da65 | -3.12517 | -53.27223 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 819e94f2-064d-3f0b-acbc-958fbfd089c7 | -3.77226 | -51.61969 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e43b4b50-9f52-3154-bba8-a7910642b16b | -1.32464 | -51.66576 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 06d57bcb-dbef-3b11-a562-fa7356f95a0f | -1.19812 | -51.75391 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ae465c5-e390-30c3-a7da-ee35fa22333e | -2.71816 | -46.12676 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40782b6f-8af5-3cf8-b2ab-affd90edc38f | -2.63105 | -51.77368 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 481969c5-bf91-33bc-9c23-681e9c3bd678 | -1.66804 | -52.79969 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e62c7f8a-0d65-3fe1-94c0-4a2004b23388 | -3.09231 | -54.29549 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 840b15b0-f259-3614-8b16-911fa20ca13c | -6.6425 | -47.91572 | 2024-11-30 04:40:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee26c00e-d9db-3eed-95c4-738bb31a236a | -2.68437 | -46.11055 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee3eb310-40a7-3814-b28b-4c8742f18ba4 | -3.69802 | -50.16874 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9eb8caf4-e84f-3c17-8343-3afb5fddbe90 | -3.69788 | -50.23059 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8b514eb-ef68-37cd-a10a-1dec317d6183 | -3.34755 | -46.29812 | 2024-11-30 04:40:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README48.md)
