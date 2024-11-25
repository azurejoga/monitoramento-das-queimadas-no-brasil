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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88b7fd22-b914-31b8-a100-cf05f8eb8d3b | -4.29715 | -48.24058 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a97b49bb-183b-38c5-971c-2c3eb54db656 | -2.33225 | -53.87181 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 52e51b24-a76d-3a47-96cb-04aa369d1b1e | -4.24471 | -47.98827 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 079c2ecf-4da1-3790-8c5b-05e145b3d922 | -2.70956 | -46.29195 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6caacdfb-0fc7-392b-894b-b952c0a05d5e | -1.72401 | -52.4878 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9d739d66-715e-3868-a87a-22024a3de881 | -9.46371 | -47.34966 | 2024-11-25 04:33:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dba899fd-a9e1-3d5e-9ae1-8a88ed29c321 | -3.24571 | -46.43168 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8e38795-1018-3d4c-beb2-3e559d9316cc | -4.95365 | -45.32897 | 2024-11-25 04:33:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51d8d966-cd06-31ad-bf62-019e9b332a87 | -3.498 | -50.46628 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52a898f5-a229-3344-9ce4-04cc1165059c | -2.64888 | -46.57427 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a012244-3392-33ac-9d59-08d40a30142a | -4.09074 | -46.83777 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af4801ac-8354-3c2b-adb4-ccb5df0ea64a | -4.10603 | -45.71631 | 2024-11-25 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71315cdb-bd3a-3a51-964a-d128e98b5228 | -2.71334 | -46.26743 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e3f49ab-7ead-3fa6-8ffc-08bc68d84322 | -2.6209 | -46.20611 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9382a300-3c63-3d56-8a4d-113c60dfe142 | -4.35453 | -45.78724 | 2024-11-25 04:33:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57469835-dfe9-363c-83b4-df5ebd323389 | -3.16703 | -51.10088 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca144b4f-8e60-3978-886a-a6d0eec565bb | -4.32404 | -45.89542 | 2024-11-25 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 1fab4f07-329d-3131-a31a-c14f03ec2f04 | -1.62686 | -52.44257 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 43b07367-2347-3f7e-bfb1-bd4e4f99c47e | -4.29537 | -48.18708 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44b94f72-5c2d-388e-aafa-e2c1766bd670 | -4.31441 | -45.89023 | 2024-11-25 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37ab4497-3a01-34d2-9084-c04a3dd9c9da | -3.32261 | -51.62833 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7d145e6-1b99-34eb-baca-507ce81005f9 | -2.91057 | -51.70977 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e562e5e6-1842-3080-9cbf-20d09a82b162 | -2.73879 | -46.10215 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39b4d7f9-5a09-30e0-830f-f42e440869cc | -1.73665 | -52.79604 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 237bb7f4-2a93-3b84-a0b2-d1f3b5c18024 | -3.89338 | -52.30623 | 2024-11-25 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ab778f0-6d65-3154-a857-b90749c7aabe | -3.29486 | -50.53728 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| debec3c8-e19f-316a-9a02-ee3347dba6e1 | -4.2978 | -46.90574 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8ca548a3-bb73-3312-96a0-2a0773b9ae11 | -3.33688 | -53.30683 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54175f14-e591-329d-871e-543dd8615705 | -1.7534 | -52.66373 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a61826b1-6e54-3ed4-994d-fbf65f2c0764 | -2.60865 | -53.97043 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04d3cf75-5a60-3986-9f0a-4fa7dcf0e6c6 | -2.73933 | -46.09862 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 446df6f5-c61e-3549-bfa3-6ab0fb482b3a | -3.19143 | -46.56277 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30dba715-1924-3132-9f58-5270b914f009 | -3.61509 | -51.47458 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 121073e7-efce-3407-a2ba-4e3273b8e8f5 | -3.55248 | -51.52637 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f190dde-34de-37dd-9a9c-64fe065c74fe | -5.13398 | -46.19657 | 2024-11-25 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b6f2a0e-d6cc-380b-9bf0-27b2939b6b3e | -3.49445 | -54.02164 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd52a03e-3658-36cf-9af5-b1f4825bbabd | -2.75185 | -54.07055 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b467ae90-c286-3b7b-a080-b347af60aa6e | -4.07292 | -54.48704 | 2024-11-25 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e8cdd45-7d56-333c-b30c-acc01d99c81a | -1.78024 | -52.739 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4c0d09b-6253-3184-8381-99f0feca70a4 | -1.607 | -52.2735 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a06c186-46f2-3c35-b431-531e1ac71ed5 | -2.64303 | -46.85326 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e7b10e2-84f2-3e99-8e6a-d0e1ff244895 | -2.32139 | -51.3144 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91251b2b-c05d-33fb-a8d8-734287abbb53 | -4.69559 | -45.84995 | 2024-11-25 04:33:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ef40f9d-a68b-3fa3-a63b-315ee402db3e | -4.24078 | -48.70761 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42bb90d5-cb88-34ce-bd99-68c1912d8b67 | -3.64024 | -51.1469 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07a36607-bbfd-3547-8221-74d8d1a6956e | -4.24694 | -47.99567 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f14597f2-6388-3f20-8f32-10e5a6582c8e | -2.54408 | -46.37337 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf18268d-073a-32a1-9397-70647b3b4d20 | -3.02453 | -54.04815 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d15ddeb5-96ef-3893-b2cb-eb9408eaa90c | -3.28518 | -53.83657 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8ac52bea-bd36-3cf7-af7b-e46270575505 | -1.39248 | -52.55648 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b46c989-18d7-379d-8db2-7177f28c31e1 | -3.72037 | -47.12003 | 2024-11-25 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24ad0d41-01c1-3e3f-8e5b-9f57be58a288 | -2.81663 | -45.20449 | 2024-11-25 04:33:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56f18279-fb41-33c1-b72d-7cb8e6453083 | -2.80397 | -53.0103 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7453885e-12fd-3d03-8040-d1cfcc270af7 | -3.45798 | -50.83204 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| aefa6d9d-4ef4-3f95-bce1-a911c8ba6ff1 | -3.7847 | -46.94619 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c648b32-f560-3610-b6d1-8a25d8bea501 | -7.18321 | -44.96127 | 2024-11-25 04:33:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b208de57-5539-3d7d-93d9-3967e142daec | -4.70168 | -49.63667 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7aa70926-98b9-3934-9891-c6f06f8d8408 | -3.20743 | -52.57441 | 2024-11-25 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b107948d-e5fa-3560-97c8-5bb54c196d64 | -2.59432 | -54.05811 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8d061c1-2635-3c5a-bda6-b1c2a3cc2800 | -3.1742 | -46.54229 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e4622b4-7583-392b-9282-38a863e7d5e6 | -3.78477 | -46.68349 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 596a2715-5795-32ff-8661-7f336df1dc4c | -4.10121 | -46.11047 | 2024-11-25 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 015c49d3-2882-3816-8ff7-5c3d2935b07a | -3.22305 | -53.93611 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74763f78-3d20-377d-8efa-c11f7c55269b | -3.63163 | -52.25484 | 2024-11-25 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a5d5b97-8df4-32bd-945c-e461a6638d97 | -3.78207 | -49.45649 | 2024-11-25 04:33:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66913afb-84c9-36f5-bbc5-bd2cc49b8d59 | -3.70653 | -51.79666 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8da4f72-72ee-33ff-9934-e77f642355ae | -3.95761 | -52.23022 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 445a5e89-a5be-3748-ab65-d10c8e5a7852 | -2.50858 | -46.22854 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f36e0543-2776-397c-bfe5-e929763d9c80 | -3.3677 | -50.76278 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c35eceb-f64c-35f7-aece-e73041b20b76 | -2.71668 | -46.26795 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db3746d4-e214-3a5c-a2af-1125c9afd00b | -4.20709 | -48.12025 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50fc43ce-3eb5-3db6-b901-3f50a852e4b4 | -2.70677 | -46.28794 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 126dd0d4-2ffe-3423-b3b1-6ae5f7f4c45a | -3.84281 | -49.96189 | 2024-11-25 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d7173d55-7fdd-3f13-9601-1f6f23258101 | -2.81894 | -54.12297 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a2e4ccb-77c1-3d46-9247-989d05c8f15f | -2.58491 | -53.96389 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a4ea428b-ebb2-34fe-9f1f-e6df9f55c16e | -2.54745 | -46.54813 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2fc17d7-08ad-3215-a643-1f2465cf9964 | -4.16581 | -46.8137 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 133a9e54-bd05-33d7-a7c9-2e6c1d5903a1 | -3.19412 | -46.37015 | 2024-11-25 04:33:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96c9ac6e-12dd-35f2-ad28-cbfeb24ab4a4 | -1.60106 | -52.58136 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d520716a-7f48-33eb-8d29-45e7d97f4f85 | -1.62447 | -55.17677 | 2024-11-25 04:33:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1b151ea2-3816-3053-8911-06284e8a4ecf | -2.89758 | -45.22454 | 2024-11-25 04:33:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e18e3b1b-31d8-32a3-9bc4-d88df3638bb1 | -3.25146 | -54.24131 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 050a8d8e-8e04-3528-bbe9-bf5dba346f97 | -3.67568 | -54.58763 | 2024-11-25 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1fb870c-9a5a-3f3a-ae24-38c511006b4f | -4.37773 | -48.50677 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| da4914a0-dd3f-3b48-9935-fa2ceb6054be | -3.09522 | -51.32685 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b404f125-d4cb-3076-b0ab-975ff5d89ae6 | -2.90568 | -51.56676 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aede9a6a-2275-389b-8244-6c6cd1784151 | -2.80817 | -53.01112 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90146a66-9d86-3679-b6c8-c84e7014b84c | -5.79787 | -47.07735 | 2024-11-25 04:33:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25809849-3063-3293-a28c-4b7a1c4814e6 | -2.99107 | -52.90182 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33eaa932-3e49-385b-8fb1-904593d73a04 | -3.8946 | -50.07277 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1d1abfe-49da-3b96-a41a-496eb2d56976 | -2.62595 | -46.21766 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a6712d1-65f1-36e8-903b-31e880bda4c4 | -3.76978 | -46.6704 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bbbbf93-c698-3920-a1d2-2809c997ab1c | -3.95675 | -50.85695 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f6805cdb-b017-370c-8192-b38f562145e7 | -3.39364 | -50.34693 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 631f2ef2-af3e-3ef6-9ef6-5ef1668f7d74 | -4.05647 | -46.83965 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cf4b142-1234-37e1-bbd1-ab5a2ac3ef45 | -4.36181 | -48.08764 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6adca3f7-6e0e-31b2-8364-663cf43454aa | -4.35201 | -50.86845 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4120cc74-ce38-3ae2-a6a0-eefea83b678d | -2.90132 | -51.76822 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 462cc943-e801-310d-b161-aca1b00f66a3 | -5.97264 | -46.30832 | 2024-11-25 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d5cb4b8-0b4e-3275-926f-9a9eedd7951d | -3.23016 | -54.2286 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README18.md)
