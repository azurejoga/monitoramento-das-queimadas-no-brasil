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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42600dd0-3f42-3d34-97e3-299b35d458a5 | -3.05053 | -50.41124 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b034423-dd9d-3b43-812c-939f26de8c9f | -3.04999 | -50.41469 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f5fd413-4318-355c-b019-b4e4dd97b286 | -3.04721 | -50.41072 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ad4a3c9-f331-3448-9395-3ea93a410084 | -3.04667 | -50.41417 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d29a1be-070b-3168-95a6-4ac237dc0171 | -3.04612 | -50.41762 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 038489a7-20c0-3fd4-82d0-2ebafea17452 | -3.04389 | -50.41021 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16ac7789-ce16-3c6c-9de8-571a1468444c | -3.04335 | -50.41365 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 246ce6ba-8e6f-368e-8c3a-7e6327baf85f | -3.0428 | -50.41711 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c70bd5b5-a591-3d87-9570-d6979b154735 | -3.04226 | -50.42056 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1729465e-cb71-308f-89e7-2df1a85092a0 | -3.03894 | -50.42004 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37efe979-4d7a-348b-9691-f1ab925b716a | -3.03839 | -50.42349 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40c1c604-7633-3978-8e37-5cb65ecde674 | -3.03562 | -50.41952 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59595aa4-3cdf-32a0-8fa9-094a24defff2 | -3.0323 | -50.419 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d14fd866-36bf-328b-ab7e-ecb2c9b28bf1 | -3.03061 | -50.40813 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 279feb4c-3823-351d-99b6-56b6142daabc | -3.03007 | -50.41158 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1710a436-a229-3637-b94c-1a84ab0f1b06 | -3.02843 | -50.42194 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d158ed14-60a7-3af7-9a01-29c46a614b78 | -3.02729 | -50.40762 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4cd76a2d-8fd3-34a6-b273-88b9775ec42d | -3.02675 | -50.41106 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2a0cba5-075b-3f1f-bc3c-0250b266de1d | -3.0262 | -50.41452 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f56e81a2-5fbb-310c-8ead-2f682678743e | -3.02343 | -50.41055 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4e92368-deda-3e40-bd11-c04bc7b06200 | -3.02288 | -50.414 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72af5706-27cd-3c46-98b0-3ee547363fc7 | -3.02076 | -50.44903 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ae2f071-d86a-3d53-b70c-41ba97b537e4 | -3.02021 | -50.45248 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f297e8ad-1d8f-32e2-b9d8-c7592c3763eb | -3.0109 | -50.48995 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcbe8f28-aa0a-36cd-b5fe-5abd361f4484 | -3.01035 | -50.4934 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc839d43-126e-37b8-bc22-7686beb26a27 | -3.00758 | -50.48943 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b549ae1-ce72-309f-8b15-b68884c20e89 | -3.00703 | -50.49289 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78bdfdc9-7500-3c07-a6e4-114b1c7e7c6a | -3.00649 | -50.49634 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86297839-9960-3f28-af8f-a29fd7788656 | -3.00426 | -50.48891 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bd5355e-3337-3750-9df1-2f4e1091c0f2 | -3.00371 | -50.49236 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 300b0646-7eff-39cd-bf25-6db93a7d34b6 | -2.97679 | -50.47416 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 405ad0d5-8fe9-319d-8a5e-4946b41dc207 | -2.97625 | -50.47761 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b318652f-ac55-31cd-b192-96001cbd75ba | -2.97347 | -50.47364 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d530fdc7-56b8-3947-85cb-d33965f3b2fb | -2.97293 | -50.47709 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4375575-0557-3c81-a6a9-9486f8d7ef72 | -2.96574 | -50.47951 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a70dd34f-e0bc-3c0f-a0b1-bf2cb21cf3d4 | -2.9652 | -50.48297 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c6bae7c-ee3c-3bb7-9697-b25b6b2006dc | -2.96242 | -50.479 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bbe57a9-72f1-3f46-8669-d4197152b3c8 | -2.96187 | -50.48245 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae82ef5c-2ade-3c20-a69f-75dd8ca5eafb | -2.74776 | -50.44508 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 090fcac8-9b11-3aea-b128-47eba3bfd3e6 | -2.62592 | -50.07634 | 2024-10-30 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 812fc5b9-ef30-3f31-b175-d151e39f79a0 | -2.62261 | -50.07582 | 2024-10-30 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82b17d1b-1a33-35c6-8edc-73d5582fe700 | -2.60045 | -50.02668 | 2024-10-30 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6003d8a4-f7e2-348a-a315-94e93b20901b | -2.44365 | -50.37661 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec5e349c-f9b1-35a9-a6c0-4b578e19e385 | -2.40892 | -50.42428 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a754e2f3-6824-339d-b607-5f27c21af650 | -2.40837 | -50.42773 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95dc9126-c33d-3114-a367-b1a1ddfc8264 | -2.90652 | -49.45762 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2632e3d-bc7c-38f1-8ac9-4207e862ea06 | -2.89434 | -49.46999 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c5ee915-23d8-320a-8a59-f7316b31453b | -2.88764 | -49.25085 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf5224b6-73a2-3c50-b040-7d97f99fb186 | -2.88709 | -49.25435 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc11812a-4c0c-3a1c-94fd-d997142ebf43 | -2.88654 | -49.25785 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dd28b9d-42c1-3298-870b-da7b22186c24 | -2.88593 | -49.23982 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34f11d91-4bfe-32fc-ade5-6109136dc03c | -2.88259 | -49.2393 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9310cfc9-1c5b-3c1a-a514-8c1f5f308497 | -2.87542 | -49.26331 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbff09b7-5955-35e9-bf8f-ec4f4e588367 | -2.87536 | -49.24177 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3234fd5e-8257-3a8f-969c-514fd0f1d39f | -2.87256 | -49.23774 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe6fe2fc-aefe-3747-b908-29929e5b80d3 | -2.87208 | -49.26279 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bce50c19-7bf5-3fcc-96de-b3f1258a5a98 | -2.87201 | -49.24125 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb380022-4b81-34af-83d1-45aeedfa981c | -2.86867 | -49.24073 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48a9c775-7079-321b-8c76-b6fec2fb812d | -2.86587 | -49.23671 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5435774a-cf1f-3297-b8d6-8c2357310b87 | -2.85768 | -49.46431 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfeabc2a-dce7-3cef-accc-b4fc4c17be11 | -2.85724 | -49.08073 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00a4696e-b5b9-399a-9f37-5a1e0a21590a | -2.85524 | -49.39259 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7b3a2c9-5735-33f7-91fc-5da39702bc79 | -2.85247 | -49.24194 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2880365-ca47-3ae5-a7e3-2b28af4d1943 | -2.84244 | -49.24038 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5500e6d4-20b3-3da4-add2-36cc692772b9 | -2.83964 | -49.23637 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 678d0009-a055-377f-9416-1b9b67350efa | -2.83909 | -49.23987 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 854ae8da-bc64-3662-a452-abd4fd214e6d | -2.83685 | -49.23235 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8e74a172-44dd-3ed7-8485-4a84e0032800 | -2.8363 | -49.23585 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0acecd63-3cb0-31d8-8597-d432ac7209ce | -2.83524 | -49.26438 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaf7b4d5-6a12-3c68-a96c-f3f08075cb02 | -2.8352 | -49.24286 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 398a1859-3445-337d-be70-fc86ba1b7ee4 | -2.83351 | -49.23183 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8c22cc49-5cbc-3e99-8f5f-efbc91f7268d | -2.83296 | -49.23533 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2ded3b70-eae2-3b51-a2a4-ebf4f2a9b738 | -2.83241 | -49.23883 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 88a84396-624d-366b-ad66-c98ac4271798 | -2.82961 | -49.23481 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8e47eb7c-b94f-3963-919c-5d3c4a4c8d1d | -2.82906 | -49.23832 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4678aa1b-5311-3293-b025-5635eaae2988 | -2.82292 | -49.23378 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be09f782-8fa7-3f11-adca-8f8d6d0f4598 | -2.82013 | -49.22976 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 860a69dd-f876-38fc-8f28-e66409446014 | -2.81958 | -49.23326 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e7a1f74-31f3-39e2-b430-b77ef2c8d03e | -2.81903 | -49.23676 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b90a14f-5598-3272-be0e-69bbd84d4d4b | -2.81364 | -49.31475 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d6c8d66-3b38-39a2-bd97-dfadc1b3eaba | -2.81109 | -49.41795 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b902b7c0-b7ee-3394-bcd1-fd0beda3d507 | -2.80785 | -49.22068 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 374b0c01-e1ea-37d3-8200-bff40612966e | -2.79897 | -49.23365 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4499502-8df2-3ba3-a757-7320b5a4e834 | -2.79727 | -49.22263 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c873cd55-b043-3b5a-959b-1de4d9bd0f14 | -2.79563 | -49.23314 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06f180ca-90ea-3867-9239-2f6091076268 | -2.79393 | -49.22211 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4bd2073-4c21-3b25-bfa2-7316161f5921 | -2.7907 | -49.48248 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d0d7585-d50f-34fe-a58f-6db19d607a21 | -2.79016 | -49.48595 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a74d24db-020a-3729-84fd-90b218e5e79d | -2.78404 | -49.48145 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| beb8dafe-d3d9-337f-9dbe-f9d7557921db | -3.46275 | -49.66196 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11460924-9755-3175-a41c-61841b356ca9 | -3.4423 | -49.68371 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41945f9a-460e-31d5-b372-091a15650fca | -3.39383 | -49.75732 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7eec52b5-02de-3d6d-999e-5d6dc7da87f8 | -3.39329 | -49.76079 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1aff8966-f37d-34e9-ba83-1fcfffa41b4d | -3.38996 | -49.76027 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6ba8ea8-62de-39a5-b7f9-33f7326ca8a5 | -3.376 | -49.54456 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e1e17ad-6d03-3211-af26-fe1d7e677af9 | -3.37267 | -49.54405 | 2024-10-30 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16ff5a81-93d6-3502-9c61-edb510ec3372 | -3.3642 | -50.16042 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92351eb8-d96b-35d7-a017-c40e319fea17 | -3.36124 | -50.15931 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fabf1733-e086-3ecf-b3d6-22629826d0e1 | -3.35792 | -50.1588 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4fbd721-ebcd-3753-b5fd-233693df22cf | -3.32575 | -50.12553 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README58.md)
