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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a796f391-d4e0-3f71-b727-6e26bde4f7e4 | -2.10148 | -46.13987 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e8d04703-b168-3e58-bdfd-2e7a7a363625 | -1.664 | -52.75267 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31e7b512-8fdd-35e6-a4d5-1d07f62f79b2 | -3.84667 | -46.56599 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a02f8c3c-aefc-3d7b-a9b9-27c5b27582d7 | -3.33656 | -51.21236 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9152f21-2dac-3250-ad8b-b274d69aeaf5 | -5.05507 | -41.86041 | 2024-12-04 04:10:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7dc3eed9-c92f-391c-ab4c-f92e38e56701 | -3.9745 | -46.66549 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5fa8adc-b7d1-3fa4-873e-83c7334bd8c6 | -3.85414 | -46.51939 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef760ca1-df24-3abf-9535-63fb6b780600 | -4.32648 | -45.81292 | 2024-12-04 04:10:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d19d5f2e-4667-3149-a01a-564bc15c43db | -4.07211 | -46.81858 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72362b89-2565-3cf6-bfd4-1b9bb7aa443d | -3.70631 | -50.45358 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d7cb823e-4bcc-3464-a41d-3649416b77fa | -3.70093 | -51.82804 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91804e30-749a-39bc-aa22-8bf56ef2e890 | -3.19202 | -51.17349 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09016d7f-5338-3865-a934-57d22370ef1d | -2.84654 | -46.79089 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1822f993-0543-3894-b8cb-c94a70830b9a | -3.54643 | -50.17894 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d086e1e-b149-3c42-afb1-6a5000c2adbf | -3.904 | -46.66378 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d57013a1-3e1c-3d9a-9cb6-77a49af463d2 | -2.0963 | -46.58514 | 2024-12-04 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50e91ef5-ad7a-3aa9-a2ae-377f7cf78d58 | -3.11169 | -54.69745 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d12fc2b-c428-3ffe-a4f5-f3d48fe491f7 | -3.97345 | -46.66313 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbe04c4e-ca93-3434-937f-c2b1a48c4cdf | -5.37701 | -42.88199 | 2024-12-04 04:10:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 65594655-75c3-38b9-8f45-bba6eee81951 | -3.08466 | -53.38087 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8412178-e025-3477-8703-15a3cf97ee23 | -3.80889 | -46.95216 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4bd88c9e-2578-309e-a264-d4537a94db4f | -2.60308 | -46.00629 | 2024-12-04 04:10:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b22c61a-7d25-3536-964d-beda67015650 | -2.27364 | -45.49244 | 2024-12-04 04:10:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 271bf78a-9c27-36f8-847c-86ffd44238f1 | -4.05284 | -46.81525 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84f546ef-43c9-376a-ad2f-5ef71ca4524b | -3.54552 | -50.18441 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d2cca272-69dd-3473-a150-8769c0f0b643 | -1.34219 | -46.01784 | 2024-12-04 04:10:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c2d48f2-e209-3047-8fef-ade8947b721d | -2.72606 | -46.20644 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9fb98c8-10c6-320a-89ad-aa03197cd607 | -4.18678 | -50.68357 | 2024-12-04 04:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5b8cd09-c34c-36b2-8986-74498acd8537 | -3.66373 | -47.13099 | 2024-12-04 04:10:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ada51863-c317-30d2-b056-db6b2c86b389 | -4.0425 | -46.82136 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28790e42-e6ca-3f31-b96f-e67f1190bf93 | -3.20497 | -50.6525 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fcad55d8-37db-308b-8a04-46ecb36a3a34 | -3.3767 | -52.78984 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 123c9674-2605-30fc-a428-3926d64ce632 | -2.55614 | -46.57141 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edecaba4-c9a8-35e4-92e7-8f3315554a25 | -3.85124 | -46.56183 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4c489c7-badf-3d26-91c1-6d6aa0a268ab | -4.51881 | -46.38787 | 2024-12-04 04:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeee9abd-14fd-32ce-aa88-1236f7cce81c | -3.57704 | -50.30999 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 82d8c571-e00d-3734-a79e-fe7b96354995 | -3.12302 | -54.67073 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f9d405d-8506-35ec-b2bb-d7bc34a24a4b | -3.51846 | -51.31188 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57ba01b8-9fdf-3878-bebd-8296d96889f6 | -2.47166 | -46.54534 | 2024-12-04 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a37796c7-8e64-3579-8a9e-c83ab6442667 | -3.10699 | -54.68535 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 771234de-43cd-3f44-947f-7e23f011939b | -3.04142 | -51.26967 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a94fc7a0-0b7c-33ea-8d9e-e60133a01fbf | -3.81916 | -51.668 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1b3cad3-e5db-3eed-b2e4-5ed6448b3d59 | -3.47579 | -50.24006 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ad3c3a7c-ce3e-3775-9750-ccd2894a312d | -1.75319 | -52.63763 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 87257322-4049-3599-be5f-f257c3f82855 | -3.1999 | -50.6517 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9cfc0c3-c8c2-3f15-90af-fd33bf1aab67 | -3.19095 | -51.17996 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54db74c1-e630-3063-80dc-facc9f95bed7 | -2.81925 | -54.14854 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66de3dd8-2b28-3785-ab7d-efdc4ad0d443 | -5.17017 | -43.7398 | 2024-12-04 04:10:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0269430-21e4-385a-a93c-38231e82fff1 | -3.54016 | -51.50513 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9edd20df-64dd-3c59-9f02-d06222cdc755 | -3.64653 | -51.12649 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b398b582-569c-3444-8929-2bcb8bbc98e6 | -2.8116 | -53.04638 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51534aaf-1a4c-3bd8-9141-49511b8a47fe | -3.83541 | -52.33701 | 2024-12-04 04:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c24c92ba-a140-3680-9b66-df51a5d0c48c | -3.5539 | -51.52146 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9c7aab4-deef-3993-9ba8-06014355044f | -2.63843 | -45.73866 | 2024-12-04 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bc0a8c4-7817-3dbc-a20f-4858cd42ef2e | -4.05948 | -46.81425 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 128253d0-329c-3291-803c-aefc0618e0a8 | -2.85538 | -54.82972 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ec871d40-1f23-3ec1-bc2a-7eb1493cec31 | -2.10022 | -46.58575 | 2024-12-04 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea4c7a5e-19f9-396c-8d6a-687f5acd5ca1 | -3.81671 | -46.95342 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6eb0979a-ce88-38db-bd0a-1928b21a604a | -3.49242 | -51.55944 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 030d9458-c7ae-3964-9675-be4a782334ff | -1.66105 | -52.75143 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da0d90eb-af7c-3073-a117-fc1358c149e8 | -5.57237 | -45.15338 | 2024-12-04 04:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 41d903a0-9a46-36c6-853d-b2f01cc6c6ff | -3.92666 | -52.39891 | 2024-12-04 04:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed762ff6-8dde-3d7d-8195-abe849333899 | -3.28586 | -50.79522 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69ea576d-0822-36ba-8100-13335dcd9011 | -2.67271 | -46.62497 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 526e0718-504e-375b-92b2-1121717e403d | -1.65662 | -52.76041 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f6b9e9f-39b7-35eb-9e8d-b121d64b303c | -1.64629 | -52.38405 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 19f398e7-3f70-3848-b15b-21a1e9a6bf99 | -4.04934 | -47.00541 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14100632-54b1-3154-a809-2acd5c31e8ba | -4.0596 | -46.99173 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05b45c75-661a-3048-b7f3-db5fd72e61fb | -4.45819 | -45.92669 | 2024-12-04 04:10:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59dcfc09-20b2-35c0-ab86-540f767dd2a8 | -1.7546 | -52.62907 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 55fc688a-d568-3252-b63d-177986dece60 | -3.4798 | -49.99038 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b22f435-fe4e-39eb-906a-be350d3f61c7 | -5.33779 | -40.35757 | 2024-12-04 04:10:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4202b8cd-b114-3e43-87ec-bacb1a765ce1 | -4.89786 | -40.09118 | 2024-12-04 04:10:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5011cb34-c275-300c-a169-637dad73dd99 | -1.7605 | -52.63008 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| aba5a8ee-f655-3193-a244-909630e1e6be | -1.74869 | -52.62807 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f068f250-8c92-3fae-8abf-cc2ca655bd39 | -2.8171 | -53.06536 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6f3fab93-292b-3d27-b5b8-8eb989d3f2b1 | -4.01586 | -48.81675 | 2024-12-04 04:10:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b0107064-ee41-363f-b036-d6a0d36b197e | -2.79901 | -54.1433 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d11fb480-7884-326c-9e58-6d2966c17637 | -3.2934 | -53.67035 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 471d26c9-568a-35ca-8c2c-d356769a7a17 | -1.65168 | -52.38309 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b4552048-3f0a-399d-9ebb-cb30359bd57f | -4.05752 | -46.60452 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6910e27-1d86-3ef2-87c6-d64460f1c1b0 | -3.37694 | -51.09842 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29af9c75-6eb2-36d9-b943-efc092087114 | -1.7093 | -46.21619 | 2024-12-04 04:10:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dacad39a-8831-335e-a551-04083de7b1dd | -2.92465 | -48.016 | 2024-12-04 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8482fd48-b527-3769-a594-c910bfde98e9 | -2.63403 | -45.74246 | 2024-12-04 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f4befba-1c2e-34c0-877e-471f4c5479a5 | -3.8994 | -46.66782 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a0f552f-89c1-3cf1-80b8-82e17a4c8413 | -2.15434 | -46.14627 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c93a3d87-e97e-321a-a4c2-f12c9d804ffc | -2.63104 | -45.73748 | 2024-12-04 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b5f68944-c4b9-32f6-a442-69863e96e8db | -3.25191 | -50.62081 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b429d59-f587-309e-a087-58c965973a73 | -3.20039 | -50.64878 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 19df22a6-0b3c-3fb7-9ebb-39ab0a74adc1 | -4.01516 | -48.82106 | 2024-12-04 04:10:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47dfcf95-11a0-3e69-9dfd-28e51ceaae58 | -2.31431 | -45.4246 | 2024-12-04 04:10:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 93e27148-60c6-33f9-b0d5-0b7100a93474 | -1.95906 | -46.4399 | 2024-12-04 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 646dccbc-b2f6-383e-8381-0e3ea251d428 | -3.92626 | -46.721 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 959c7d23-b470-3a2d-8a21-d78fc102f4bf | -3.00912 | -52.45711 | 2024-12-04 04:10:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6f1d1a9-1bad-31a5-82a0-96823d260f90 | -3.58523 | -50.53262 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c03dc7d-d0fe-3b54-8ab0-afd86a98795c | -3.92932 | -46.72655 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd44c307-272e-3d15-b615-b76950784e79 | -3.82381 | -46.6106 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c6588a2-9047-3374-a51e-5996482a4002 | -1.73308 | -52.61226 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0e5a7ae0-745a-396b-bdae-8462819c92ec | -2.77725 | -45.85799 | 2024-12-04 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README23.md)
