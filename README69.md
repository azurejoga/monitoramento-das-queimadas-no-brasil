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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fa7a7a3-c668-3eaa-964d-d36fb016c1ae | -3.17757 | -48.01534 | 2026-09-24 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 088663cd-1345-3675-b59c-45297fdf5e4b | -3.17697 | -48.01923 | 2026-09-24 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8bdf7582-d9f2-369c-b1c3-d10e12d8c601 | -2.92523 | -48.74132 | 2026-09-24 05:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16887170-4064-364d-be0e-28b225722354 | -3.45264 | -50.61398 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff03759d-a761-3b68-a02f-4a576236ee85 | -5.99892 | -57.72577 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fd11b6a-4936-3222-841e-866a1f1faa21 | -6.44646 | -59.95481 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 97fe4a93-c3b3-3769-ac42-7c2ab321978a | -7.4912 | -54.96586 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bab5e071-8f94-3235-9bff-ab6204a37f4b | -2.88225 | -54.07993 | 2026-09-24 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28033fe3-8ea3-3553-b893-be89d181a70b | -4.46998 | -54.96985 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c899088f-302c-311b-b727-1453d3125189 | -6.51551 | -52.82723 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31805553-b1f2-3041-bad7-2f440cbd4525 | -6.62614 | -59.93874 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 279f4e02-317b-3215-886d-6db7d2daf9f6 | -6.44165 | -59.95791 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b23d4ffd-0b6d-38f2-a357-cf33ecb6da3a | -5.19696 | -44.68762 | 2026-09-24 05:04:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e82ff4f8-afca-313e-af32-5a703ac5b10f | -6.52783 | -62.94258 | 2026-09-24 05:04:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ee61edc-29d0-31e3-aca9-d1bcad3778a1 | -3.23426 | -54.32345 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0a5db6e8-b78d-3d20-8809-a2e2b2e91f58 | -6.75258 | -59.05756 | 2026-09-24 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f02b886-d40c-333d-a5e2-9f97604aa01c | -7.46911 | -54.9979 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 69e6f5ad-dbd3-3894-a37f-3d56241d484b | -9.17403 | -49.99577 | 2026-09-24 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d14fbfbd-b9b2-30ef-b757-d4a92ec25dfd | -2.94253 | -54.08624 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1a197e1-5099-3ac3-861c-85f1ff0c14cf | -7.19436 | -47.45287 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e8f2ee2f-7171-358d-969f-f27527f42f61 | -6.63029 | -59.93941 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3bb4e12a-5254-3ab6-8d0c-0c7a2daebc69 | -3.68428 | -60.59124 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1155d5d5-0f34-3804-b370-7438dda7940e | -6.65347 | -55.06341 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fb08c719-744b-328d-8864-a8d28634d7b3 | -2.79527 | -51.36566 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b7e1508-e184-3e3e-afeb-267f1f108eee | -3.78935 | -52.42184 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e12f321a-f5ad-3d22-8faa-a9b3176153f1 | -4.99653 | -45.55598 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8488688e-2718-38a1-b1c9-ac024ab5fad8 | -2.1275 | -49.52738 | 2026-09-24 05:04:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbea809a-0d66-3eb3-ad14-8ecfc088780c | -3.71477 | -54.20785 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25cab478-e61e-3efc-ae2c-6f4e076fc317 | -6.61848 | -59.93354 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6604e126-08a6-3f2b-89fd-71510a7ac698 | -6.78449 | -48.68221 | 2026-09-24 05:04:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| efcee159-a198-337d-8857-5875c96a54b5 | -6.10592 | -59.88396 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d92fae1-7ede-34eb-b99c-37a3bdce7290 | -6.46559 | -59.99342 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10dc3501-2c7a-3901-87fa-d81b697e5bfd | -3.91871 | -59.66352 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 537a10db-be38-3bfb-86c5-0620e7ff5fa3 | -6.10718 | -59.87632 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a2cb227-7a3d-38c9-b605-9327c9a386a0 | -6.61689 | -59.91764 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94830e0d-23b8-3420-bd4b-74de4e504cbc | -3.15267 | -54.60342 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2ad98c67-0893-3de1-8648-aa16c5f8fc5b | -5.77368 | -56.52559 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62b67e54-81cd-3229-92a0-d216ef587619 | -6.41836 | -43.48046 | 2026-09-24 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd9371ab-d01e-38f0-93dd-79386abf9094 | -7.09225 | -52.76532 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68534b0e-4c11-3bc6-85a7-9eac1b4897eb | -6.63921 | -59.93705 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7fe4b5a8-884f-3bb5-804f-7f0fe8f04ff0 | -5.71804 | -49.8318 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc987e72-36d6-36ac-a699-88e41a3be19f | -4.53725 | -54.97295 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcbd059b-bfc4-3b1a-8c0c-ed9819d4124d | -2.56396 | -57.50405 | 2026-09-24 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acb3c60a-ad98-33ce-a553-0e14c5ba7c00 | -8.20159 | -54.72755 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3de98be2-170b-38b9-9967-2728306bdf3a | -7.39727 | -55.21468 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d6e9374-ecd3-3904-9dc3-34b206c6edc7 | -4.49314 | -55.56953 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d21ffae9-f6f5-31fc-989f-832c07f8fd73 | -2.71075 | -57.50715 | 2026-09-24 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b2c12f95-db74-3880-99f0-14fc72f3a3ed | -3.00672 | -51.53136 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae3a405c-6c84-355f-ac06-8bb5127fcafb | -4.6611 | -54.47499 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4004488f-d9ce-36bf-8dc7-17bf5211b2a1 | -6.75529 | -59.73885 | 2026-09-24 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d34626c-7241-3140-b2c3-40e6751eceec | -6.46417 | -54.99363 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7fc00c8-8ded-3aac-8419-fc5d4559cf68 | -3.81382 | -58.88596 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b5cdcdc-714f-3602-a373-997cd6bed3b2 | -3.02156 | -51.3758 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee043a0c-1394-3fc1-a1ba-63363a1a5316 | -7.47721 | -44.57175 | 2026-09-24 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84fe9576-f875-3c50-844e-60bdaa4c3f97 | -7.27277 | -46.79074 | 2026-09-24 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34204bbb-e262-3303-b1cb-66ab3045897b | -6.29717 | -57.73544 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e68d7e63-167c-3615-88ab-f554aa8d6f60 | -3.21557 | -53.41275 | 2026-09-24 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c4a82c7-f63d-30e1-8b3e-a7f7345cf12e | -2.97958 | -54.15227 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20f1e22e-bc43-3ca5-bc00-2c620ba3102b | -6.46208 | -59.98883 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31d4876e-3436-3130-83af-4e0a7ede3d36 | -6.62677 | -59.93495 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 800eccf7-b82b-3165-bd50-60043e67e927 | -6.68003 | -55.04621 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7400a470-3e63-391c-92ba-6f88e2864e20 | -6.53216 | -51.5087 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 619f5ab8-d34f-3841-939d-cfc6e969fb82 | -5.5994 | -60.19332 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 597bece4-f705-3719-9df4-af78ac19f74b | -3.78422 | -55.8788 | 2026-09-24 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a8741a8-a343-32fe-b9ed-08a98c393ac6 | -4.55956 | -54.9405 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 519759d6-0668-3483-b065-c257a96c0a8e | -6.60254 | -59.92691 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b063da68-4b8e-32b5-8f5e-ae16f547d0cf | -6.23712 | -60.03573 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3b1cfa8-2782-3970-aa41-8d17b9663902 | -3.00745 | -51.53202 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c20e60b7-b96c-3fb6-8ca4-4f4321a3d4d0 | -6.12655 | -43.7454 | 2026-09-24 05:04:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb2bee58-d270-3d9c-9df7-e792afaf8a80 | -7.6718 | -45.47897 | 2026-09-24 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 696ba00c-81dc-359a-9a66-106bfe08f070 | -4.56289 | -54.94103 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28d7e849-d1bf-33d5-9dd2-022bc0bdfcae | -5.86009 | -60.15984 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 969af0b0-54b7-3252-9798-4d32be28bec3 | -2.16576 | -56.71637 | 2026-09-24 05:04:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b18011a5-3e2c-3f49-bf47-199a4d63e666 | -9.15045 | -49.95966 | 2026-09-24 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2936aaa0-9a06-3f47-a2e7-68d530e75a70 | -3.44328 | -50.07798 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7106f171-73b9-3a2b-beea-131559bd0d5e | -6.04313 | -53.2716 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f926090-e4b1-36ed-8a8d-04aa2edab714 | -1.92173 | -58.25815 | 2026-09-24 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9be2bda8-3f9b-36a9-9767-a3f120d2644a | -6.307 | -59.95286 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 73e8103a-bdfe-3025-994e-3f092b050c34 | -8.14233 | -46.82271 | 2026-09-24 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8f1842af-e6ad-324c-9298-14fc692f4a8f | -5.81657 | -47.75512 | 2026-09-24 05:04:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0e0ffc6-4db8-31b7-97b8-610398c1528c | -7.41991 | -47.35956 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcb0f97a-a227-3c46-807e-9531dba71204 | -8.29 | -54.74909 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b4d660f-263a-3561-9261-cee2020b44ed | -1.11492 | -57.06471 | 2026-09-24 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ed29315-12ce-3792-8e51-b7cc35a9b930 | -7.42486 | -49.82866 | 2026-09-24 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4414210-d1dc-3a69-9f31-1c86eb2fb3b1 | -7.03092 | -44.6523 | 2026-09-24 05:04:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 45429469-875b-347d-b3db-6830d690f8bb | -6.62558 | -59.99336 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82ddb91d-c76a-33ee-82de-c636286f0e78 | -2.77067 | -48.65804 | 2026-09-24 05:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b834c740-4084-3fdb-a508-6c4eebc682d7 | -7.78748 | -50.22331 | 2026-09-24 05:04:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87fefcde-8f46-3223-b78f-31b77f70460c | -4.52116 | -54.97079 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f62cf513-e22a-3afd-b5ee-052ac2b70b99 | -4.12157 | -51.07921 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ffc6fae0-7e73-359d-9bfa-fb8888a17c65 | -5.76736 | -56.52067 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4baefcbe-e829-34fb-94de-0cc1364f4214 | -9.26346 | -46.24736 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4d3b5ae9-e161-355a-b9ce-01f58a2b7f38 | -3.22126 | -53.95683 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ad37103-49ed-30ef-87ba-f47ea9939a53 | -6.21607 | -47.49372 | 2026-09-24 05:04:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 157b91d5-092a-3e2c-9a91-1ce3f0f37e29 | -4.66165 | -54.47154 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 235ae2e3-330e-3dc5-a61a-be9414215557 | -1.19126 | -54.137 | 2026-09-24 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c9308c7-83f5-36e6-9fbb-504505827dce | -6.78025 | -48.68156 | 2026-09-24 05:04:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 40932e57-f9b5-3d19-901b-3c853bc2e1f0 | -4.22066 | -48.61677 | 2026-09-24 05:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 817eed18-e275-341e-81fd-911e069de504 | -3.88985 | -51.95804 | 2026-09-24 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14819a73-58ac-3fd2-af22-ffda9182410d | -3.70538 | -54.20285 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README70.md)
