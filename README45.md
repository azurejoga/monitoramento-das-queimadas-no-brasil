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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6945b44f-e9bb-3049-b60a-606378b88771 | -4.73394 | -48.9963 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87e9445e-97cc-3b08-9e3a-429df8a5e065 | -3.33353 | -50.08424 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fd54200-a9df-3a2d-8e98-eb411b49390a | -3.03917 | -50.36398 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab02015c-9a24-3837-b7b2-b3cc666fb718 | -3.33664 | -50.08781 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9d18c8f0-399a-3531-b7d9-0f65e7172d97 | -5.63731 | -44.82952 | 2024-11-09 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df486df3-5ebd-3f0d-9015-419476267be2 | -3.55642 | -47.37718 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23f5f4bf-c95f-30aa-8d01-f69899829def | -6.23712 | -47.28459 | 2024-11-09 04:33:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a78acc3-055c-3f79-b673-abdf66aae465 | -3.08232 | -50.5671 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 70b38017-4317-38dc-93cf-6164d5704605 | -3.79891 | -49.94417 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8c546838-3178-35f9-b8b3-cdead2a6a15a | -2.72188 | -51.70747 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eaae52fd-e586-3105-8cab-56e6f760eb5a | -3.02705 | -50.37056 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5b5c8422-504c-3ec2-bd68-3626e4beb9f7 | -3.0246 | -51.52921 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5f4be0a8-468f-3d5e-bad8-6303b3d3571f | -3.88666 | -46.65176 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19518bad-c8ef-300a-9dd1-8a7d6145e5a9 | -3.87594 | -48.33307 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e27a31d-128b-30f1-a4e2-49a25ca50a6c | -4.21322 | -48.61256 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89a0ef5f-da5a-3678-ba94-f00c8e17c0f2 | -3.58758 | -51.43408 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6cbf4ecd-bcb1-3af2-b0c7-17f4efbfc957 | -3.83387 | -46.48686 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47744caa-cba6-36bf-9ab8-b6a44aa539d5 | -3.96405 | -49.00103 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fde2276a-d9c4-348c-b22d-7c826cc304ad | -3.17129 | -50.21648 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 35f5c746-1255-3cde-bfdd-68e0a6b66351 | -5.26762 | -46.31562 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9de25dd4-9806-3db8-9619-42ee1183663f | -3.6889 | -50.19821 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98bfe470-656c-39e0-ac99-1c96a528435c | -3.56283 | -44.8253 | 2024-11-09 04:33:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f9154f3-85e7-3850-8bf4-a583337e8454 | -4.71299 | -44.2332 | 2024-11-09 04:33:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc68c599-56d0-331a-a268-355b68d332bc | -11.09418 | -43.34313 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 9b9baa5e-abbe-3dfe-afde-c3d30248dbf3 | -3.70993 | -53.75317 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| fe8750ca-612f-3a6a-bd33-1c64506e359b | -3.10259 | -49.40704 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7653f282-9b70-3fdf-88b8-2ca864482953 | -4.66756 | -44.33878 | 2024-11-09 04:33:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74562539-3d33-3eb4-b8fd-d3195b332bc1 | -3.24843 | -46.44604 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd0ecfaf-23b0-35fb-8e5e-2eaa4911bd91 | -2.82154 | -50.43518 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff2fea07-e484-35d3-9f05-ea745d7d88d4 | -3.84422 | -46.44192 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99ea28f6-e67a-38fe-ab1d-8026eb767449 | -5.1159 | -37.56767 | 2024-11-09 04:33:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f0ab0179-0106-3805-8be1-98d419dc46f0 | -3.05079 | -47.69176 | 2024-11-09 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c677c115-83d3-35a4-9218-60a54a14f0e2 | -5.51106 | -43.78868 | 2024-11-09 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7efdaeb1-98b6-34f1-a97f-c0e9c5e20176 | -2.84199 | -49.82401 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98b81514-fba1-3910-8760-d30e01128aeb | -3.91552 | -47.95154 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea0c5348-b157-3f54-980e-a7f624e240fa | -2.82519 | -49.42638 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3ed9879-c255-34d8-a7cd-f94644bf46df | -2.36103 | -52.69564 | 2024-11-09 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fed693b-d85d-3c05-8f15-428852cdc040 | -3.0874 | -53.88511 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2ba6107-98e2-3c24-9b83-1fce51af9b89 | -4.40088 | -45.48954 | 2024-11-09 04:33:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 362e03c6-c3f5-32c0-83ea-eb259d0ea1a8 | -3.38863 | -54.68528 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36eed7e3-eb1d-3158-88a1-824dcef6c9c2 | -3.97796 | -48.13854 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2d6c2a2-5535-3dc7-90c2-6d7b91ba0a44 | -3.91828 | -47.95553 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a0fe7cc-5af8-3b41-8f4a-92d926bd0205 | -5.04073 | -45.86955 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f91e6f2c-3a75-3c8c-9136-ef1081847d0e | -4.05621 | -46.94096 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6748742a-a2c0-31fc-acb6-a19ca722cd20 | -3.13844 | -53.68465 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 192c2465-99f2-3a5e-9ead-22112d30c87c | -4.18384 | -48.80023 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9915e9d8-9713-3d0f-af1b-cff0b758d3b3 | -3.09502 | -51.11747 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55f30164-6fa6-38e3-99cc-141304943946 | -2.83376 | -49.43935 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3127047b-dd4f-3ec4-a761-bf63ba52fa0a | -2.23904 | -53.77348 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| a78234e5-a72d-36e1-9b66-9a4984001df0 | -3.17596 | -53.84893 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 00ad8957-09e7-33ad-8719-3436d4e705d9 | -4.19629 | -48.39414 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da7e39b6-25c0-38cd-a348-d15eb6288995 | -3.50229 | -51.1468 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab540fae-2bce-3458-ab02-f0f4e4d79cb0 | -3.60139 | -47.34896 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5b345883-280c-37ec-8da8-a9b532d0ce30 | -4.4278 | -45.70267 | 2024-11-09 04:33:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b691a88f-0c50-3176-8149-baf11460f59e | -4.1773 | -46.57557 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36696b4e-707e-301a-af97-9263f3604faf | -4.6772 | -48.77594 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 77418f6b-780f-3f79-94ef-c470626a9509 | -2.88136 | -50.4172 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4bc8007-0e5a-3861-b77f-93a1e8ed7705 | -2.97433 | -47.92059 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d7556f0a-e55b-3d20-99f0-85d53ceaa737 | -3.23601 | -50.26301 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cbd8a509-75d8-37df-ae31-8aaa323e75fb | -4.15015 | -46.57496 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e308f49-4945-3ee9-b4a2-b734bf708fad | -2.89333 | -49.39817 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6cba1d0-b6d7-30f3-9a8e-ac11dbe6f3a2 | -2.88422 | -49.2315 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce75721e-cc63-3e53-855d-b620c2c57237 | -3.59276 | -50.23329 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f20360df-999a-3a6d-879e-f8bea69fa52c | -5.42546 | -47.53999 | 2024-11-09 04:33:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7449a0f0-7d81-34a0-9ab9-1b7a67dbac58 | -4.25314 | -47.57445 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| c817b47b-9910-3e70-ab55-5ed4cf74b8e2 | -5.11018 | -47.14056 | 2024-11-09 04:33:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5bf52109-2b65-371f-b308-e5570f79fcaa | -2.94293 | -49.34819 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc7ffea2-853b-35c8-b236-1b38b25b6273 | -4.72835 | -48.9881 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf47daf7-07c6-372e-84ba-39a8480dcc72 | -4.20147 | -48.5566 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72b13d2b-6bf4-340d-ac02-13ef5be841e9 | -3.35276 | -50.123 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9c9b24eb-2507-3d78-87e0-54def0a1eb19 | -4.19979 | -48.54554 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4fb11445-5b20-3960-a6f4-c941fbb6ddfa | -3.55312 | -47.37667 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d790753b-d358-35ed-b918-de8bdf037895 | -5.73507 | -43.50715 | 2024-11-09 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 241ad85b-a400-3032-8cb8-d0bf05cd2469 | -3.04208 | -50.32221 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 33016d53-a1dc-3d1d-b1cf-5336ae704027 | -5.00438 | -46.90029 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 707e6ccf-1645-3b93-a003-28a30ca5a350 | -8.8493 | -47.69521 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70900b3a-20ee-35c7-85a4-b092327a81da | -3.95564 | -48.98866 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cfa6120-7819-318d-be3a-93d10d066a5b | -2.94444 | -51.49946 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 952ac3bb-2de8-3ac4-a956-2a55200a7a85 | -5.49684 | -46.30653 | 2024-11-09 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 835a98dd-a915-33bf-84a4-5308349b18e1 | -4.65001 | -46.70634 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 848b1e9f-9ddc-3886-ac56-77c09126bb1f | -6.13236 | -42.56308 | 2024-11-09 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 22b94f96-d0dc-3de9-832a-4ac8b72699a5 | -5.6389 | -44.24909 | 2024-11-09 04:33:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d460f0d8-661d-3c27-aa31-0a79246d7bd8 | -6.18533 | -45.44449 | 2024-11-09 04:33:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0895ae32-faf7-3876-b722-4e9380098adb | -2.8077 | -52.99593 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 571e9ce4-88e9-3a3b-8cd7-74ef57cc1960 | -5.85052 | -44.08323 | 2024-11-09 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c794aba-83fb-30cf-8a8b-a01b89a39655 | -2.81404 | -51.81048 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ab87bd3a-db73-3ebb-a336-5fd3971a0a75 | -4.37828 | -47.25252 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b7cc9c4-b644-3c0b-9e21-129697f430d4 | -2.693 | -51.68787 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82c579e1-efdd-3f19-8e22-1bef5f6c5845 | -4.30715 | -43.16982 | 2024-11-09 04:33:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94588346-ea1c-3cb0-b49d-f48567b799c8 | -4.20239 | -48.39868 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b26226ae-1b93-3c12-928d-0d89446fe622 | -6.18591 | -45.44061 | 2024-11-09 04:33:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c47773ee-fb09-3ab0-93a7-792d79a7fc4a | -5.74274 | -41.99229 | 2024-11-09 04:33:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fc830651-de92-36b5-bcbf-05a243620931 | -2.89188 | -48.29379 | 2024-11-09 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b99c0a58-6652-3bab-a695-7e6a8ba46fd3 | -6.31319 | -42.75323 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2ceaa324-dd59-3312-a356-72a32c439375 | -2.92695 | -48.31001 | 2024-11-09 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19a923b8-856b-35b6-a634-9cb9f275e3a7 | -4.51134 | -45.68552 | 2024-11-09 04:33:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3331717-7405-3f16-b7f5-3ed32be87594 | -4.50464 | -46.39237 | 2024-11-09 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7edb0576-5705-37d8-9c54-7b647a7500b0 | -6.36271 | -47.89934 | 2024-11-09 04:33:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 069f02d8-ffa6-3fb6-aa26-3a0aa07cf546 | -4.246 | -47.57686 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 5f5717e9-184e-3b22-98e0-ce2a668829ef | -5.19564 | -47.46555 | 2024-11-09 04:33:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README46.md)
