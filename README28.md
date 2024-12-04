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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ff96077-b91f-39ea-9e35-b3d9968a0c93 | -3.25615 | -53.62875 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0b2da4d-264a-35d2-b4f7-209745223e9b | -2.8081 | -45.93864 | 2024-12-04 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ea507e3-edbc-38c8-a480-facbcd34f394 | -4.01146 | -48.81597 | 2024-12-04 04:10:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc20bb5f-eae7-38b2-86d0-49ccb7955352 | -3.2696 | -46.27317 | 2024-12-04 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9afa7ce-0991-3cfa-94f7-f3f6cf6f26e9 | -3.5455 | -51.506 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d45dc34-e454-306a-abdc-11fbd31683d3 | -3.10301 | -53.75801 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59d26d60-57fa-3c66-ab5e-111f449d581b | -2.5678 | -46.5733 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85763ca9-2998-3f37-95c5-33bb7556b5ef | -3.2414 | -51.29649 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87250ffc-dda7-331c-8c6d-77615f3b69e3 | -2.06536 | -45.48432 | 2024-12-04 04:10:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 705b5f32-2127-3c32-b7b8-dc6ad85d32ff | -3.12206 | -54.67638 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76c38137-786c-39f5-bfec-0a3343feee7b | -3.98252 | -50.51935 | 2024-12-04 04:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 56f66356-77ca-3706-94dd-1797b305665a | -3.49126 | -51.56622 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7d7bf34-c52a-3adc-a1f5-672be1e3e0d1 | -1.6633 | -52.75705 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e70c40b3-a120-30c8-9806-3855cc7e9e6d | -2.99776 | -53.82508 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 938e8713-160c-324f-9fc0-0a4778783004 | -2.67886 | -46.13731 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 521edc68-857d-3f20-a504-af585cd36e92 | -3.12109 | -54.68206 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efa2dc06-7966-363c-a6a2-ba6812dba6b1 | -3.05961 | -52.76646 | 2024-12-04 04:10:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98933772-000a-3f2d-bd8f-6e480a72d7c0 | -3.26298 | -53.62884 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2b03bc7-4d70-3d8d-9a0e-6b742f6a23b0 | -3.7287 | -50.05405 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ee5de16-0917-3bd2-916a-772f28ea20a8 | -3.79774 | -46.69878 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5909f6cd-15df-3b49-986d-6838c4b9c345 | -3.85087 | -40.98151 | 2024-12-04 04:10:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1914236b-aa91-35e4-8908-f21df5b1b2ba | -4.05406 | -47.00106 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 649b73f6-ab69-3939-af16-540a2e63b7ed | -2.31969 | -45.06279 | 2024-12-04 04:10:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03cdbc55-c647-357b-8685-b40796ef66ce | -1.66779 | -52.39429 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d2fa6a64-cd66-3f34-9f0d-449d2e61ba61 | -2.82139 | -53.06168 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58db1ec9-e404-3118-bfb0-5ab7435f8288 | -1.62462 | -53.54025 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0bdb25f8-981d-328a-98c2-1b2084c70874 | -5.11923 | -43.20203 | 2024-12-04 04:10:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6d253c2-76cf-3cf6-b378-8e896fe69404 | -2.84665 | -46.68929 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ad463b1-9814-3d0b-aebe-1c969f6c3029 | -5.27228 | -46.17297 | 2024-12-04 04:10:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ea3888f-5292-3b7a-b825-307a9f8d8f9b | -3.71936 | -51.08067 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 678c07fd-41d4-3abe-a4e1-7063fccd6862 | -2.7228 | -45.53992 | 2024-12-04 04:10:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5963354b-7b66-3d2a-ba25-92965d25c987 | -2.66221 | -46.12051 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa28b762-5948-3dff-b1f5-906e2e420a04 | -1.69317 | -46.24298 | 2024-12-04 04:10:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3b77e78-8082-3829-9130-913d6fbd2ee9 | -1.65545 | -52.39648 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b85acf5-8e66-3430-8539-ded3a5c32814 | -3.55128 | -50.17992 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3106a7b5-444d-38c3-8ab7-2fc4c6bc5341 | -2.62805 | -45.73253 | 2024-12-04 04:10:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ce2accd1-4f8a-3121-8af5-ee1ff4b8fac9 | -3.85649 | -46.52907 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ee9faf6-f984-3fcb-8547-3891f11711b3 | -4.05679 | -46.60905 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fe23fc6-285b-34ff-86a9-4d8283a23608 | -2.00428 | -54.11106 | 2024-12-04 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e264ffb1-5f1b-3799-8eff-1134e66a4ce8 | -3.60302 | -50.80048 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14ae1782-aaab-3c29-99b5-51bb4027f7b0 | -1.05034 | -46.59204 | 2024-12-04 04:10:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9c9970f-ee1b-3833-9ab5-d758d8a45512 | -3.70135 | -50.45276 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e874ffd-a7bc-30d4-ae32-a415e2983a9c | -2.62467 | -46.79742 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1f8cd40-0245-356b-898a-e581a95ce7d8 | -1.67005 | -45.56501 | 2024-12-04 04:10:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f95a48b-f0e6-3de0-9c27-5af50dcfb7d0 | -2.67741 | -46.62067 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 292bfb35-baa2-37b5-b665-cb0682fac8be | -3.19148 | -51.17672 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbbb581b-5d72-39fc-abe9-ae0baca43944 | -2.19502 | -47.24744 | 2024-12-04 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b7ec8366-7cc8-3bf5-ba59-55aa53c7e67e | -5.12145 | -43.20946 | 2024-12-04 04:10:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4596db7-ba37-3041-bba5-baa1cc842fe0 | -3.79908 | -50.98325 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4eb25f53-7783-36d6-8086-9f69184316f4 | -3.49401 | -51.56675 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2811dcb6-df8d-3575-83da-220e36e74184 | -3.26313 | -53.62497 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18dcf7e8-4e46-3a53-b326-c756582f85ec | -3.05444 | -51.06256 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d3e221a-5090-3b61-a213-3a45cfc09f96 | -1.62547 | -53.535 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42714073-abea-3875-a18c-f7d0328f7953 | -2.80816 | -53.04575 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34a497f9-55f5-3bd0-ad60-2116501ed4b3 | -1.66032 | -52.75579 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b3880162-6487-3609-b07b-5b8f63152d13 | -2.3212 | -45.42844 | 2024-12-04 04:10:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b85f62a-ca30-3039-a07d-9637338956c2 | -1.74348 | -52.62279 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6809f962-2743-315d-a078-0f8012250c1d | -2.63473 | -45.73806 | 2024-12-04 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 88611e05-c4f4-3f65-8bc1-159e5c82e18c | -4.32655 | -45.81612 | 2024-12-04 04:10:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6203a04f-e110-3ae0-aee2-015393bc5387 | -2.75528 | -45.19407 | 2024-12-04 04:10:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec096fc4-0a0f-3eef-b11f-28b532debb02 | -1.72718 | -52.61126 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 764c1660-c2e1-3a78-9ae2-d8d87185e393 | -2.81614 | -53.05622 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8326519c-581d-3590-b650-5fc880ca3a78 | -4.18726 | -50.68071 | 2024-12-04 04:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4a19c96-8871-35dc-9c9c-911bb14b60b2 | -3.51403 | -51.31085 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0ee9bea-42ff-3926-97db-23f1aab7052b | -2.03699 | -53.94925 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7a7a3234-7228-34d0-a4ed-653344b8be27 | -2.54351 | -53.41697 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2c1ec9e-c03b-355f-b735-b58690d4bb91 | -3.2524 | -50.61786 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0726e2b6-6b98-305d-a79f-4ea986c9f953 | -4.07158 | -47.09081 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be8e8fd0-c031-35fa-bdcc-c2649d40860e | -3.23095 | -46.41897 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b345012-4dac-33a1-8c28-cee2ea1ee8ba | -3.60811 | -50.80132 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48351403-5715-33a1-908d-cd87d6940e1b | -2.97645 | -46.95493 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d926ae51-8276-3eff-9ad6-8d6126b26d2c | -2.87928 | -51.79993 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a80f4b27-c4fd-3381-a14e-eca516e201f4 | -3.81678 | -46.95229 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc1f24d4-a928-33ef-b78d-847123d2920a | -4.19821 | -50.67675 | 2024-12-04 04:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06115497-d416-33a8-995a-e988b1d0db20 | -3.68791 | -42.04454 | 2024-12-04 04:10:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5caff5bf-adc4-37f8-a8dd-74d7fbae56ef | -4.08106 | -46.69246 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| efd3b31a-56ac-30c9-9b40-8607395d077e | -2.02263 | -46.34087 | 2024-12-04 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c104700b-4eda-3f6b-a607-d2cf1a447fba | -4.11675 | -46.91039 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cbda714-d828-3814-981d-6d911cf373aa | -5.57871 | -45.15834 | 2024-12-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e59bb29-7207-390d-b26e-fc4d84bf1935 | -6.25568 | -43.5565 | 2024-12-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a22578bb-0695-3885-bd06-0c43c61666a1 | -10.22137 | -42.18802 | 2024-12-04 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 34fa2836-54ef-358d-af75-a818750d6056 | -9.19444 | -43.16238 | 2024-12-04 04:12:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cc929b76-38f1-35ed-a5b8-40d886e67ab7 | -5.62644 | -44.83919 | 2024-12-04 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9d36b2cd-f414-3297-9306-c9948c771e15 | -6.27384 | -44.73903 | 2024-12-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 438c2e14-e7c5-38e0-a277-5cb90900b8c4 | -5.62928 | -44.84344 | 2024-12-04 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6857784-5978-3cd6-a838-e5f73b5ab55c | -5.57523 | -45.15779 | 2024-12-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e7827667-ab7e-31fe-b798-7cee6d8563e4 | -5.81661 | -44.11429 | 2024-12-04 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 49531b1a-817c-3da0-80c9-036b130882f3 | -6.24544 | -44.1525 | 2024-12-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20c1bd40-8ea4-3633-b949-e21c497d790f | -7.5425 | -45.87437 | 2024-12-04 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f090b094-44f1-30af-bac0-e70e762fe5e8 | -11.24263 | -40.98179 | 2024-12-04 04:12:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 748f65b8-0b5c-3dc9-8a86-969652e5e42a | -7.53962 | -45.86987 | 2024-12-04 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1c01ebd-a850-3597-a627-1e8ed10c03a8 | -5.57461 | -45.16163 | 2024-12-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7849af4f-718c-3d74-b94b-745b47508a5a | -11.18563 | -40.3224 | 2024-12-04 04:12:00 | NOAA-20 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 53652c4f-dc00-3983-8618-2f5bd4403279 | -6.40144 | -44.05048 | 2024-12-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68fadcf0-946e-3631-aba7-b8186dcfa5ad | -5.57747 | -45.16604 | 2024-12-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90132d90-6a5c-3ce3-804b-43ac250cf7be | -11.16454 | -49.43303 | 2024-12-04 04:12:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6436b95-45b7-3672-9ec6-f4aeb3292b90 | -10.03921 | -36.5594 | 2024-12-04 04:12:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| eb8c5934-1a97-30ad-a4cf-563ba1fde541 | -6.08758 | -42.68295 | 2024-12-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6995a58b-4512-3aea-9e6f-c43b7fc8517f | -11.60859 | -44.99533 | 2024-12-04 04:12:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1e9b304-2e7f-3d60-b461-020c8890b1b6 | -11.16046 | -49.43227 | 2024-12-04 04:12:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README29.md)
