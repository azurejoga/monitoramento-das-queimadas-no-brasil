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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 394a9441-ad8e-3cfb-8607-9f4efc0f7d4c | -1.63969 | -52.61878 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a77d12c-5f42-3c61-8892-97494de4d8cc | -2.66119 | -46.60776 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc8e92b1-c264-3a5c-9f5d-4cfec570cc13 | -2.72076 | -45.70303 | 2024-11-22 04:12:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 241c1e39-80ee-331d-a624-4a292022d2b7 | -5.43297 | -45.34035 | 2024-11-22 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdb9d9c2-2052-36d0-8921-b7163de1b396 | -2.95134 | -53.72036 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 253d0d02-b161-3609-80f4-1f018341b385 | -3.2888 | -53.86281 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b77d05c-acc3-3497-85d5-bf1625515e71 | -6.19882 | -46.3201 | 2024-11-22 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bad9881a-ee34-3cc1-a386-7d4255ae6180 | -4.40759 | -44.11739 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b3f089c-cfad-3891-89a8-2d5744265da5 | -2.70169 | -51.86773 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2092d6dd-fde6-37bf-b106-cf97932dd344 | -5.81321 | -44.74474 | 2024-11-22 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ad455b7-7796-39f1-a1d7-a4cf2efa2b63 | -5.95655 | -48.05545 | 2024-11-22 04:12:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4dd1b488-a10d-3393-8109-ecdd13e23d34 | -3.41127 | -45.23336 | 2024-11-22 04:12:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2bebe6ec-6ccb-31aa-a731-e008191a56ad | -0.9139 | -51.7389 | 2024-11-22 04:12:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb0f752f-679e-37bf-955a-96ec12d535a1 | -5.50314 | -44.56297 | 2024-11-22 04:12:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a4431dee-a44d-3287-ad3d-1a6e527d3f92 | -3.24409 | -54.24111 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7fdf137e-d076-3c1a-a261-6bba4b7535b3 | -0.264 | -51.54192 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab1af1f0-2607-3c3c-9dd2-6e647d8e54ec | -5.59636 | -43.73965 | 2024-11-22 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d55ea763-fd73-3ccf-b8d4-b1de28b04edb | -2.63516 | -46.21724 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 429e51d7-9383-3dfa-9c73-10a807ef4dc8 | -4.00638 | -49.92321 | 2024-11-22 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c47760e-536e-3dcf-b8a1-01437ce44484 | -2.2809 | -47.91494 | 2024-11-22 04:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0a2c864-ff99-3d81-b0fc-debbd34b5201 | -1.81357 | -52.162 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5aa2f120-e286-396e-a889-15627f674dc6 | -2.70944 | -48.66575 | 2024-11-22 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e15b53d2-d34b-34f1-966b-f938f5bd845e | -4.25459 | -48.69962 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| de96ac10-8738-3659-91ce-9e5765be6482 | -2.05778 | -48.25885 | 2024-11-22 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58b78674-0f3f-380c-b963-21661184956c | -3.1801 | -46.5421 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 125bf9c5-eb9c-3537-b08c-ca54f9754bd9 | -3.28129 | -53.83121 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 583bb4d6-3dfa-3719-b639-7a2f6399ce31 | -5.57667 | -42.60248 | 2024-11-22 04:12:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2854dc31-5aa6-3fde-a5a0-a371f718bc7a | -7.64688 | -35.07021 | 2024-11-22 04:12:00 | NPP-375D | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4b11ff17-d40e-3385-bc6c-c8e233fde65b | -2.55135 | -46.5425 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e337b8a-bb61-3168-a438-8e6f63c4888d | -3.90524 | -46.48282 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75045224-9391-35a9-94d8-5369357617a0 | -3.19625 | -54.32699 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6959a72-87e3-3a45-a13a-6b90783dd70d | -1.77632 | -53.59842 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b601c249-dbf9-3761-b02a-186831479849 | -1.19545 | -51.95036 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cceab5b2-8044-3f04-9be2-d438f61eb362 | -3.23395 | -54.26184 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b93516e8-71f9-3317-9616-47fdfc24c193 | -3.48599 | -42.29959 | 2024-11-22 04:12:00 | NPP-375D | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f2e7779f-a1fb-398f-bbff-fc2b2a94b757 | -2.70191 | -46.08803 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70752dca-1b40-391d-b0ec-cad7d5f75315 | -4.11151 | -51.0608 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35106468-9f37-392c-ab5f-fb5cd98ebdc8 | -3.45965 | -41.49753 | 2024-11-22 04:12:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 67fc9f6a-fdf6-3e71-9d3f-ecbd1e7b118d | -3.65403 | -42.26205 | 2024-11-22 04:12:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 723c5303-9473-367c-810c-637c584ea81d | -2.64773 | -46.13824 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eea7fccc-6c9e-327d-b92b-a6a6d3195d2b | -2.07595 | -50.32271 | 2024-11-22 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 51ab1d0d-2e9e-3e1d-8317-8001e7a9f255 | -0.81139 | -51.79416 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6bcf998a-4444-3d89-becd-27dbd819277c | -3.66519 | -51.575 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2808652a-6a6e-356d-9c33-0816201eb22e | -1.73375 | -52.71056 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8fa8b00f-f93d-3324-868a-eb0e3c23269c | -7.45153 | -39.77522 | 2024-11-22 04:12:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3f30cda5-fdf7-3685-9b45-631af6cffe09 | -1.07593 | -53.36691 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5563a4a9-c698-3974-b386-916b5732c6d9 | -3.25609 | -54.24845 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 54067953-a88d-3607-9150-1ea7625a1ffc | -6.27065 | -44.54789 | 2024-11-22 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fd45fc6c-0814-30ea-99d0-b6fea6676145 | -3.23857 | -54.23463 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b9457363-ee05-3baf-b306-37fd08a02e94 | -4.23782 | -41.92853 | 2024-11-22 04:12:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8a46d886-a62e-32b3-8987-f892fa0a1644 | -3.64246 | -54.32162 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43fde971-02b4-3d90-8480-207407d3aff3 | -2.70066 | -46.23994 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 212549a5-dd61-387f-9a62-85ad699c7af2 | -2.69737 | -46.09201 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c4f74c4-dc94-333a-a289-0bbe7c0af380 | -2.50777 | -54.15821 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 47d5b45e-b21e-37e8-83ba-41c16044f0a2 | -1.7933 | -48.44755 | 2024-11-22 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d7ae8d2-0ece-3703-91d9-81aed5bd4f7a | -5.95593 | -48.0591 | 2024-11-22 04:12:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2935d003-920f-3976-b75c-5a1d4b79e80c | -3.80174 | -46.60418 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6613ea3b-6a25-33ec-a2a4-4f7bbf1c800c | -6.9196 | -46.11173 | 2024-11-22 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f615a19c-fcfb-3916-b066-d5d99895f795 | -2.69763 | -46.25871 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdce7013-05fc-3905-aac9-42160b527f24 | -4.47655 | -45.66082 | 2024-11-22 04:12:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1570ee4e-528b-35ed-9e83-444652f33aec | -4.09626 | -44.85625 | 2024-11-22 04:12:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0c97ad1-194e-349a-a765-dd1d81728edb | -0.7737 | -51.76773 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62dfb6ad-d456-3bd9-aa5d-23f40b1dddf6 | -2.98198 | -45.11945 | 2024-11-22 04:12:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b95d2523-53b0-399a-9a2b-23b457ac1c0d | -3.2257 | -54.23254 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 563f3e93-0f0e-3a33-a175-c7731dd5fe2c | -3.61976 | -41.07534 | 2024-11-22 04:12:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 44d9bffa-ffa7-3ec4-9009-1f215ff81b1b | -2.28087 | -46.55488 | 2024-11-22 04:12:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb33a667-ec69-35e6-8730-0ddfd33a6e51 | -4.39682 | -44.1194 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce6d8802-7170-3632-8e17-619f79e0324d | -2.72768 | -46.09687 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8036fd85-7097-38f8-8b22-7f70d3672818 | -1.60818 | -52.58674 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9aba49a0-a543-3150-8755-068bb15817d1 | -3.0807 | -45.96543 | 2024-11-22 04:12:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c128c7e-f59c-380b-a852-7936321cee9d | -2.22165 | -53.72674 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74d08c22-0063-33f5-a76c-3fe4f96738c9 | -3.23303 | -54.26727 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d21a25c-e6e1-3bfd-956b-7e1d67c57cc8 | -3.24221 | -54.25221 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| c31ed154-d48a-39a8-9dcc-56813e174710 | -1.74105 | -52.38969 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 45dd4df8-e4c7-3e6b-af14-370192857cb9 | -2.67905 | -46.16222 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d518fcfd-430f-3cf5-8266-80412f4f1739 | -0.04917 | -51.23713 | 2024-11-22 04:12:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9fca0311-a91d-3fb1-9f25-693f57df8e47 | -3.24315 | -54.24669 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 2eb09ec2-ff00-3b02-8649-64b5606578b3 | -2.69658 | -46.07529 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 235bf810-79c3-339f-a297-d0a5b566939b | -7.21206 | -45.07899 | 2024-11-22 04:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44c2dc02-21d5-3171-abda-e12f34b819b1 | -3.25097 | -54.24369 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 793bfe44-74fc-3e83-bfdc-24c57025476c | -2.15635 | -53.79529 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3710943-06cc-3601-ba06-3b4b930034c0 | -2.49482 | -49.00103 | 2024-11-22 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcc91d8f-4911-339a-87e9-e4e6b83dc385 | -3.34124 | -53.33462 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5674a9de-53d5-3226-90df-08d689ce85c6 | -3.00935 | -45.13216 | 2024-11-22 04:12:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33ca74a4-ddba-3111-83d4-2583762ac307 | -2.1572 | -53.7901 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbc42245-dc01-340a-9b5e-de7b528881be | -2.72315 | -46.10083 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7d0829c-ceb2-3648-9ee1-382ae488fa5f | -4.24305 | -45.7213 | 2024-11-22 04:12:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 681ffe63-54d5-3a8b-8f40-be739e9203b7 | -4.63883 | -49.54146 | 2024-11-22 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f48d6fec-74b6-3ba5-9113-0e920c37e3af | -5.81605 | -44.74899 | 2024-11-22 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38d08754-1d25-36bf-86f9-a85d1b5297ae | -1.80731 | -52.16312 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 492a14df-a23d-3874-b79c-c34d228d5d28 | -1.24495 | -51.74631 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa898bf3-2d0f-3f26-883d-aebc978b6b68 | -1.07239 | -53.36815 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0df66607-b7e3-3aba-9adb-3b69abd27cf1 | -0.81 | -51.79782 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04d1c2e3-1bf7-359d-b1f1-05ea9cd6138b | -5.67765 | -44.30155 | 2024-11-22 04:12:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd8876c0-e08f-300f-9ef5-d32118fec50a | -2.56331 | -46.15322 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1adba0fd-bd59-3592-bdec-20715c6554ca | -3.24667 | -45.37751 | 2024-11-22 04:12:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e442a23-1229-3c01-a6aa-e8df57acf817 | -4.70295 | -45.80912 | 2024-11-22 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ad53810-6af5-310f-8aaf-24e132db4574 | -2.1557 | -50.45863 | 2024-11-22 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e7126b0-6a45-3277-9aa3-9a74d2151f1a | -4.2394 | -45.72077 | 2024-11-22 04:12:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70b1654a-e1c7-38a4-972a-eb65df1443b2 | -6.8698 | -38.87364 | 2024-11-22 04:12:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README24.md)
