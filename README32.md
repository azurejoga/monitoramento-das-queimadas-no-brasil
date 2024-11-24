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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a79e1fae-8242-3902-b9d5-683bba8209d1 | -7.34828 | -38.91171 | 2024-11-24 03:57:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9b1fc611-d14d-39e7-a5de-904734b96670 | -1.52179 | -51.62767 | 2024-11-24 03:57:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c98784a5-f94b-3f86-beed-382aa1534350 | -2.71714 | -46.27562 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cf2c333-4075-3882-a105-2b5da35b7f14 | -3.09651 | -49.02061 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d0e8046-bad5-3d92-ac84-4034b2456082 | -1.83839 | -46.64544 | 2024-11-24 03:57:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 89c8c0f1-0b16-3c91-87ad-a6e13d031bed | -2.27646 | -47.14854 | 2024-11-24 03:57:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3ec56de-3301-327e-9eec-b21395bacc48 | -4.1107 | -49.44329 | 2024-11-24 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42405d05-7c79-39a3-bb3d-a863f3238ffa | -3.32346 | -49.89951 | 2024-11-24 03:57:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e77d6e6-9366-36b0-b031-eb42c964b31d | -3.70827 | -51.80102 | 2024-11-24 03:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a474fd8d-0921-3747-af5f-f1b8b5cd5dc1 | -2.68824 | -46.27598 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 30b1f76e-2b9a-37bc-bef3-0e2e2496d102 | -3.15478 | -49.90363 | 2024-11-24 03:57:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c0504f5-2253-3d22-8858-3e18d290fc32 | -3.12335 | -45.27577 | 2024-11-24 03:57:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1c48d00f-a2f6-3970-9e3a-6ab0ce437795 | -2.14582 | -46.74532 | 2024-11-24 03:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc841755-4bc4-3644-92dc-77a96620102a | -5.84946 | -40.79901 | 2024-11-24 03:57:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bd9cc711-47e9-3b9d-8626-f87f3dde1e25 | 0.74219 | -50.82741 | 2024-11-24 03:57:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 831eee03-9951-3828-9347-3297797619ee | -2.53581 | -46.39673 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b530026c-7699-31af-96b5-c6cab1349913 | -5.86805 | -35.31627 | 2024-11-24 03:57:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 68d38535-6086-3877-aa74-cf235e4056ea | -4.86736 | -38.38482 | 2024-11-24 03:57:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 49cdb06d-2859-32de-8c0f-6c8c0860f0de | -4.51997 | -44.44939 | 2024-11-24 03:57:00 | NOAA-20 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b14fcb50-670f-371f-82a7-17c5465d7c53 | -2.679 | -46.15878 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0957d584-f575-37ed-a3eb-e8fa22987743 | -5.19658 | -45.41607 | 2024-11-24 03:57:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbea73c1-6c46-31ef-91a5-df7cd9f52ecd | -1.86371 | -48.16716 | 2024-11-24 03:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80ece382-6846-3ee9-92fa-e4e89782c709 | -4.40251 | -49.65382 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37e746e6-3c07-3ca4-934b-d0e1599f1f6e | -2.70636 | -46.10894 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3ecf5bf-f59f-336f-ab2a-a46486586744 | -2.3269 | -46.34718 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f6f7f13d-923d-3390-9320-b762ecaef933 | -3.34662 | -50.51221 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3921f4b6-911d-3cc6-9ab5-7d1b4de9946a | -3.12053 | -42.4435 | 2024-11-24 03:57:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f69a56d-66e4-3416-b536-ead41680d83c | -5.38143 | -45.76164 | 2024-11-24 03:57:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d78bb74-008e-3aa1-8f93-b4fb96677c60 | -3.15776 | -49.90057 | 2024-11-24 03:57:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d77dfbeb-ddfa-30e6-99be-b90372b934f4 | -1.27688 | -52.2515 | 2024-11-24 03:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8766fa6a-ed00-377b-8a41-9cafa223d5d2 | -3.02887 | -49.45414 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 237197b0-cb20-3f93-a5d1-b4210277fc50 | -5.4965 | -46.25412 | 2024-11-24 03:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3654980e-c681-3535-8d37-460bea1aee6c | -2.70228 | -46.27829 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cce2ab99-10a5-3b14-a3fa-36f29e073559 | -5.93317 | -39.47601 | 2024-11-24 03:57:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8e53a7a8-db8a-3ae1-a8a1-122291839512 | -4.25566 | -48.69572 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f3a642c-7b33-3898-9646-3479887fc612 | -4.35568 | -45.87981 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a960968e-34af-3b57-b9f5-152314ef9b5c | -2.70922 | -46.29465 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1645b99a-d690-3d29-b159-d96dd52b06e2 | -2.56278 | -46.5589 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6fb47e0-3007-364a-9576-44e026870db8 | -3.7743 | -50.99249 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 682b3ee4-639f-3bd4-81b5-348a4d1d3eae | -3.50882 | -41.11106 | 2024-11-24 03:57:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9d315bbe-266f-3442-bf6e-c045857a3d66 | -3.07773 | -40.06775 | 2024-11-24 03:57:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 9b1f847e-289a-328f-acf3-c835a1864174 | -5.06046 | -40.07657 | 2024-11-24 03:57:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bb91b060-1a94-3609-8272-0c625a288006 | -7.32365 | -35.33002 | 2024-11-24 03:57:00 | NOAA-20 | ITABAIANA | PARAÍBA | Brasil | 2506905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8b5646e0-231d-30e3-8f94-c11550e35ccf | -3.04104 | -49.45231 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| e4597462-ab9a-3458-95cb-5f247214e602 | -1.3233 | -49.3946 | 2024-11-24 03:57:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d3ddca76-3c5b-39de-998d-f6747bebe32b | -2.43859 | -46.14213 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffb2d38d-6202-319f-89f7-7f7e00f0f169 | -7.82802 | -34.84809 | 2024-11-24 03:57:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 48712005-136b-3d10-9324-414602793f74 | -2.86834 | -45.84013 | 2024-11-24 03:57:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d32fd071-b81f-33e3-8f95-851f3809009d | -5.02487 | -43.75817 | 2024-11-24 03:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c5582d0-2f0d-3a3f-81fa-b5aefeca3825 | -5.02957 | -40.873 | 2024-11-24 03:57:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5bcf023c-7e7b-381c-9c4a-8a473caaff10 | -1.59218 | -52.5946 | 2024-11-24 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ba073ec5-880d-3690-a780-414eacc1ce81 | -0.57046 | -51.73115 | 2024-11-24 03:57:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 843afc05-80e0-3b53-8686-704f54d44a89 | -1.32399 | -49.3904 | 2024-11-24 03:57:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 822d9c2e-a31e-318d-9001-44fe4e48c562 | -3.95519 | -50.20189 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e2113727-610e-34f2-9b8a-88761263b4fb | -2.45145 | -49.09299 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f4b4078-a1c1-3195-a981-bf65be05d1b9 | -5.1181 | -46.17405 | 2024-11-24 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db914356-d48d-3c4f-8056-f3b536bc2728 | -1.94911 | -49.53368 | 2024-11-24 03:57:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1e5478e-b92d-3808-9dc4-ed61ab4b38fe | -3.70135 | -47.60014 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da018df8-ae5c-352d-82f2-7da4000785af | -2.24393 | -46.86997 | 2024-11-24 03:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9b86f6c-9c43-3b82-8cbb-90571197f1bf | -5.41675 | -45.76311 | 2024-11-24 03:57:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| afcc5408-c11f-3eda-8e94-de7351da1072 | -5.25993 | -43.2035 | 2024-11-24 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97e18828-a3ad-3686-b34a-107d73b3599f | -2.66698 | -46.15409 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e67d4655-ba69-3127-8ef5-e76b32b46869 | -2.79691 | -48.68413 | 2024-11-24 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 748e7a21-4ba6-3284-ba87-97033b505180 | -3.2815 | -50.03993 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 524bd51e-95d2-3dcf-954d-47efb92bcb41 | -3.24319 | -50.67215 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ff7bc831-4927-3947-90b8-4cde38426dee | -2.64611 | -46.13577 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5be22b18-eabc-3b33-8a16-ed8906c9b918 | -2.07028 | -46.51197 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1963751d-0ba6-3699-ab7f-ce18b4dbbe70 | -5.44627 | -45.50623 | 2024-11-24 03:57:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c96aa109-9c14-31d8-b6ea-35e0d9d5d992 | -3.25596 | -52.85458 | 2024-11-24 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5d3986d-6e49-37d6-82fa-320433399e60 | -2.06532 | -50.31226 | 2024-11-24 03:57:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 506be335-62ba-35e6-b618-bab9cac00298 | -4.20801 | -50.40808 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0a52bde1-ed4a-39e9-935e-358772bef17c | -2.45209 | -49.08912 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7ef2902-1815-33f2-850a-5938b3266eef | -6.30071 | -44.88512 | 2024-11-24 03:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93854e87-bff7-3b21-9477-9954446df6f1 | 0.40893 | -50.86631 | 2024-11-24 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eb297a82-ff22-3c4d-b369-7bab188ca748 | -4.53885 | -42.91605 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 959468c2-c70d-3587-b53f-4c8c27ecb7f3 | -2.2733 | -48.42795 | 2024-11-24 03:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5be75baf-f754-3d53-874d-da33706dbe34 | -2.79632 | -48.68774 | 2024-11-24 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cff48fb2-0906-3ed2-a246-57b14872ff1f | -4.08279 | -46.14958 | 2024-11-24 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45e6e866-6e57-3a9b-8dd7-53db031754cc | -4.25624 | -48.69234 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5406ae5-f785-3c50-a9b2-9b5f4c8e92f9 | -2.74479 | -49.1248 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3ac369de-797b-3121-8074-41fed707ef19 | -4.59533 | -44.72575 | 2024-11-24 03:57:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffc4609e-d7ee-3855-852f-4fbd747aff21 | -3.24486 | -50.67173 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 38d4739a-cd3d-351d-8483-922cff4c5946 | -0.57731 | -51.73237 | 2024-11-24 03:57:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce2c7ba3-e884-3df8-ac7c-b9008c3931a5 | -4.40821 | -49.6549 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc6fef4a-da32-347a-9f75-d36ce833231d | -2.71246 | -46.27487 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac3e241e-2bf1-361f-967c-ab6f623d3c48 | -3.28597 | -45.44216 | 2024-11-24 03:57:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d2fb39d-a551-371e-8432-7c2ba1619d3c | -1.04209 | -51.74696 | 2024-11-24 03:57:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a6790a9c-c47e-316e-973c-fd6d49fa61b6 | -2.45485 | -49.03772 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ba9cec6-e7f9-3288-a451-cb4e27c5160f | -4.236 | -48.71347 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 080ad108-0218-3c83-830e-7e7cc9a585ad | -2.278 | -46.20064 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2611eb92-38d8-35fc-82e5-b122ebdd326a | -3.68144 | -47.13014 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 424d0d66-caff-3bcf-ab6d-5567f40e3c29 | -5.10433 | -43.15009 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| fb1c7fb9-966c-3908-9efc-f8bcd38f8d45 | -3.38591 | -50.31999 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2b145126-2743-362e-ac9a-964bd5fb7f00 | -1.79334 | -45.71393 | 2024-11-24 03:57:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb31b1cd-e98c-3505-a4ea-e3eb37355f53 | -3.1577 | -45.53642 | 2024-11-24 03:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d5f26dd-f7ba-3997-a781-b3a253b34445 | 0.40801 | -50.86057 | 2024-11-24 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e637571b-c7f1-3bdd-92d6-05c99be1c197 | -4.37371 | -49.75176 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e437c06a-5386-3384-bb91-369c513cf0b7 | -3.12968 | -45.3757 | 2024-11-24 03:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c11ec97f-8e59-3f82-98fb-bb38977b2efb | -2.59312 | -46.55349 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2602d340-71ac-344e-a13a-9f5afd34b842 | -5.94237 | -39.30697 | 2024-11-24 03:57:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README33.md)
