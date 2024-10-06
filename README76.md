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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 605fb491-8b9d-3708-9a3f-954f53119f46 | -8.77836 | -49.95369 | 2024-10-06 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 841fb96d-d2d2-3b92-9b0f-4bca8ffc0abf | -8.76698 | -49.97287 | 2024-10-06 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b03f1ab7-821f-3e37-9e76-0432a0e492e2 | -8.76389 | -49.96706 | 2024-10-06 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b13eb20-dca7-3316-8271-5c716d678cd7 | -8.6651 | -49.49924 | 2024-10-06 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c6360602-7db7-38e3-abf7-5d0b9639b8cd | -8.64584 | -49.49592 | 2024-10-06 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 627b7ae5-9a2f-3c7a-a8e4-ff34080de442 | -8.63391 | -50.04415 | 2024-10-06 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29f981f2-1503-3178-851e-ee156a6ffec6 | -8.63111 | -50.03648 | 2024-10-06 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d2bc7bc2-6c4e-3598-b84c-56dc808fe8ab | -8.63052 | -50.03996 | 2024-10-06 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 20fdbe01-c16e-3f6d-9e6a-a4709b024f4a | -10.54238 | -49.13505 | 2024-10-06 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8609cbd-7d69-339f-9d42-d284b4aa4c11 | -10.52333 | -49.11346 | 2024-10-06 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b75d81ec-b7b2-3072-b8e1-edfe2e719790 | -10.51892 | -49.11718 | 2024-10-06 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 910c24d1-dd2b-3346-ad17-93bb671d9e10 | -9.87629 | -50.14924 | 2024-10-06 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18051eb7-40b7-30c7-a720-0dff9cbf22de | -9.78931 | -50.06601 | 2024-10-06 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48c8dd12-bf92-35c2-b17d-537823634f09 | -9.5881 | -50.08905 | 2024-10-06 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f78e69bf-dee3-3216-a1ea-06e397b75cae | -9.58722 | -50.09415 | 2024-10-06 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7668ddb7-d954-3f92-b12d-6deb7196dc84 | -9.58187 | -50.22028 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 090a6519-2eac-3a2f-8b7f-03b64ce5e429 | -9.57215 | -50.22924 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1af114e1-40c9-39f7-a822-d7758f6e81c6 | -9.57126 | -50.23446 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf8bf09d-cc86-3d41-bfa8-c626c2aad419 | -9.56728 | -50.23377 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ac3ef45-4a79-3818-9d2f-9ba9d6b314f3 | -9.5633 | -50.23309 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a5d8a83-6f78-3ee7-8a89-f200718802b7 | -9.56112 | -50.222 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f0d274c-311d-3e9f-b37d-4ddb2ba23ca5 | -9.56023 | -50.22719 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b30a1165-86b1-3bbe-b5ed-07312c86b42e | -9.35877 | -49.99612 | 2024-10-06 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d56a9392-59b0-3c39-8970-f0419cb64c40 | -9.35791 | -49.99831 | 2024-10-06 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9430ba2-dfc5-3c38-89e4-33a6f14210b8 | -11.92784 | -50.10674 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e3cc733-206e-3c01-a94b-7c3cddca9983 | -11.89492 | -50.11562 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b23e3d91-42fc-3014-a063-3fd2ed136a03 | -11.89193 | -50.11017 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27d2ec1e-2a8a-37af-9572-d961af5f08c7 | -11.89111 | -50.11494 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77ee84ae-af27-3cae-8572-e2b17cfbf650 | -11.88513 | -50.10402 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 188287c8-9428-38c7-b3fa-91cb620f4d58 | -11.88132 | -50.10334 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 16110cc4-9fd6-305a-b2d7-faaad4b34346 | -11.8805 | -50.10812 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b69db30-15c1-3144-8a8b-72faf034cd65 | -11.87669 | -50.10744 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08dafaab-cf71-3a4d-9606-7e1b823ece93 | -11.87586 | -50.11221 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f99a41c-f14e-3e83-99c7-6c31159ece7b | -11.86576 | -50.1252 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d69fbae-ce26-38d0-a7c4-fd18834f0e87 | -11.86493 | -50.12999 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21bda78e-740f-3645-a423-2f5dbb021320 | -10.96675 | -50.15269 | 2024-10-06 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 603b02ed-ed01-3d3f-bf3b-ead89e884e8d | -10.96589 | -50.15762 | 2024-10-06 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c12b2656-4ef5-397a-93a4-8f775fd88a94 | -10.86079 | -50.13689 | 2024-10-06 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d0fa9004-ca09-390a-8e93-4e2a392bff5f | -13.26456 | -50.62751 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f831a577-e879-3ffa-8539-4bea812d0ba4 | -13.2627 | -50.62409 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7257eff-b234-3b70-bc13-94207d801d43 | -13.26183 | -50.629 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2351d4c0-7141-3cb1-a6fb-f7bac3596f2f | -13.26071 | -50.62679 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 44b988c2-8ffb-3cec-9f2f-e1cb567b121d | -13.25885 | -50.62338 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 578d572f-7723-3cd6-bc1d-7846f9d2868c | -13.14568 | -51.17502 | 2024-10-06 04:19:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9585c86c-7815-3f9b-a513-94e7e65e0821 | -12.7787 | -50.53023 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63823f3c-6970-3259-b0e7-1d80c3745ccd | -12.77484 | -50.52953 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 70e3c64a-c128-390b-9000-61877721c93b | -12.77398 | -50.53445 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 34179e8d-0af3-3e4a-84de-bf2df635d75c | -12.77312 | -50.53937 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 826ed2c1-7d68-3e42-b2a1-4439a7a6bcf5 | -12.77185 | -50.52391 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 102922d1-f7a9-3620-95f9-002613d0490a | -12.77099 | -50.52883 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a6f275a8-4b14-37a8-b1d9-0bd90a45e328 | -12.77013 | -50.53374 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5f092886-e6e5-3330-99d9-826aef2845f1 | -12.76927 | -50.53867 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b879cf6c-f7f0-3980-af16-eacd0758491e | -12.768 | -50.52321 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 6a2549d8-7a95-348b-aecb-0f76ef3c787e | -12.76714 | -50.52813 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| ac587c71-7edb-3aca-907a-994985b53e1f | -12.76627 | -50.53305 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 43644f11-094f-34d8-91ec-9bc6fa5ab484 | -12.76541 | -50.53796 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| e930adb7-2e62-32b3-854a-5a125a800420 | -12.76415 | -50.52251 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 3ffeef81-eeb2-3fbd-85ec-9172aa2ae68c | -12.76328 | -50.52743 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 30fa5022-5090-32a7-a4cc-1e4a9bd63a28 | -12.76242 | -50.53234 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| b76f126c-94fb-32c3-81c3-033e99400937 | -12.76155 | -50.53726 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| ee78205a-e699-3d98-9d8e-3869e59b3ce0 | -12.75943 | -50.52673 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 57e67f57-c232-3db6-8e9d-7d983fd000f5 | -12.75856 | -50.53164 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4da61279-e18d-39ec-ae1c-17159b394db1 | -12.7577 | -50.53656 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 14e95c26-c154-3360-ab26-bca4025cba84 | -12.75683 | -50.54148 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53de270e-a2a7-3ede-9016-2453eb9ea861 | -12.71961 | -50.61642 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a9976e6f-eb33-3053-881f-d7269a11f068 | -12.71873 | -50.6214 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d2153f3f-7908-3249-a7a2-1627358a78a2 | -12.71833 | -50.61881 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ac93c83a-a0bb-310f-a4b1-ee146ee6684a | -12.61181 | -49.62916 | 2024-10-06 04:19:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 537fb55b-5286-3204-87fb-20a1bf91e4e1 | -13.91977 | -50.85008 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1640c61-14f1-36c2-84f7-b4e00281521f | -13.91678 | -50.84443 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eb749d79-4fb6-30ed-80d3-e460579bf81a | -13.91539 | -50.8749 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e02e867-0a5c-3321-9d52-4425b3228aff | -13.91152 | -50.87418 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c073cb1a-4b9d-3aae-8c93-52765540c725 | -13.73555 | -51.04784 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce10342b-91c1-3f5a-b946-92932581dd47 | -13.73537 | -51.05074 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3cd8284-bf5b-3f72-8a12-a3e06604c1a4 | -13.70481 | -50.85703 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb963c89-6101-3aed-9b38-e9e57b5d801b | -13.68351 | -51.18527 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 84b5e3e9-bf70-3376-bfc5-58125ab18c28 | -13.68259 | -51.19049 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b7cb0762-4370-316c-8277-6b9fc1308cd5 | -13.67955 | -51.18453 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 3be3b76a-c134-3e60-bdfe-9ec8006f5d03 | -13.67864 | -51.18975 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 3db76319-9394-3825-a186-def3178164fe | -13.67772 | -51.19499 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8685f02c-40d3-3d73-8807-eed827a5e052 | -13.67468 | -51.18902 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 24.8 |
| ff063401-32a3-3c1b-aec6-49eff411f78a | -13.67073 | -51.18827 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 963e1af7-10a6-3267-9229-b4387d218ad4 | -13.66981 | -51.1935 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e857acbc-77bf-3987-a0c9-34d209c040bd | -13.66677 | -51.18753 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7de028d7-81be-3fe1-babc-67d172224132 | -13.66282 | -51.18678 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 439b09cb-028a-3422-8960-7a596e495394 | -13.6619 | -51.19202 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ba8bfcc-fbf2-3725-8097-9f6f9da8a9ca | -13.65886 | -51.18604 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4a734e7-e008-3957-a900-78939b60c493 | -13.65794 | -51.19127 | 2024-10-06 04:19:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f558e7e-db4a-3fa1-b79d-df643cb2d5b0 | -16.12042 | -50.46403 | 2024-10-06 04:19:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 23846f27-38d4-301e-8332-cd729da12ba0 | -16.11721 | -50.46551 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 221d6ab6-8ccd-3b40-a526-fe6c3bf12411 | -16.06668 | -50.45159 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dd61afe6-de4c-3ac7-a74f-54bd0b7de93e | -16.12203 | -50.45497 | 2024-10-06 04:19:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89d22f54-fe10-3b8c-a05c-9fd19035cfb8 | -16.08214 | -50.44965 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 85448045-a13c-372c-b54a-22401e5e7e0a | -16.0748 | -50.4484 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2e2feeb6-7232-39a0-960f-2980db82c8bb | -16.12164 | -50.46172 | 2024-10-06 04:19:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44411455-dcf8-3d87-9ab7-f9a7ea0bef6f | -16.12123 | -50.4595 | 2024-10-06 04:19:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4f92e763-8c12-3f0c-9f29-ad02ab3ae287 | -16.12087 | -50.46624 | 2024-10-06 04:19:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44857429-e4ff-3e0b-8880-c3721b664ade | -16.11799 | -50.46093 | 2024-10-06 04:19:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6bb675c-c8d3-32ec-9379-6f09fc67b6ca | -16.08135 | -50.45422 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 89c7178c-b3ee-337b-848b-b75925c63cec | -16.07768 | -50.45356 | 2024-10-06 04:19:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |


[Clique aqui para ver as próximas entradas](README77.md)
