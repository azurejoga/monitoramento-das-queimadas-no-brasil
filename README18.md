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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b653727a-f53f-3e2e-bfe8-f25f9e7027e2 | -3.47145 | -47.66994 | 2024-10-03 00:33:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 89c4b8c7-ea37-388e-bd28-24db474db146 | -3.41201 | -47.06485 | 2024-10-03 00:33:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9b5aba98-791a-3508-ac48-ebe7bd5dc90c | -3.41197 | -47.07119 | 2024-10-03 00:33:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| bd7c0bca-9093-302f-944c-b9762ece41a6 | -3.24575 | -50.1422 | 2024-10-03 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| defc0544-f936-3b7b-bf2a-5c71aeb2b6c5 | -3.22587 | -48.93928 | 2024-10-03 00:33:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 7ff1eea1-f356-3b1a-a89b-f36bddeee190 | -3.22467 | -48.92437 | 2024-10-03 00:33:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 90a63d8a-662f-3a07-85da-628992cdc24c | -3.22319 | -48.91908 | 2024-10-03 00:33:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| cb953769-ac25-3fe6-9a5b-1e69604ae638 | -3.13336 | -49.41438 | 2024-10-03 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 306a0f88-b6bc-328b-bb54-824346e3c96f | -2.95684 | -49.36142 | 2024-10-03 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 2acff436-08f6-364b-9692-62c0229bc237 | -2.57632 | -49.06936 | 2024-10-03 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| e8aa54e0-e0e5-382e-a317-89d4be3af0f1 | -2.53899 | -47.22979 | 2024-10-03 00:33:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 4532b828-fe56-3705-b844-937fcc2ebb46 | -2.35832 | -45.67423 | 2024-10-03 00:33:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| b418dde0-1521-3d04-bcd6-4b5f0f31ef65 | -2.35433 | -45.573 | 2024-10-03 00:33:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e8772e7b-9e38-3b86-aab0-c4df6ea43e35 | -5.71753 | -43.78903 | 2024-10-03 00:33:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 65ea1383-8fae-3670-9023-6a073b35cf8d | -6.30514 | -43.04162 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e799a659-ad79-3ab8-a5fc-9959810216c6 | -6.3046 | -43.43895 | 2024-10-03 00:33:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d099c909-2dfd-37a3-9c95-f508f49d2b42 | -6.29612 | -43.04289 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fbd7042f-2999-3a15-af1b-80368f645bb7 | -6.29544 | -43.44022 | 2024-10-03 00:33:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 4f238747-4a0b-3d5d-a2db-6918390ce597 | -6.29485 | -43.03359 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 04b1b4e0-3680-31c1-b2a7-4bb17fda3853 | -6.26631 | -42.75819 | 2024-10-03 00:33:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 7c7fc6c9-6373-3304-9aa3-2206e35af4b5 | -6.2543 | -42.53902 | 2024-10-03 00:33:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 84c3ce3e-a9b0-3ca8-97e1-90d96e73d001 | -6.25306 | -42.53006 | 2024-10-03 00:33:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 86d5ffac-720b-310d-97f3-c911961168a2 | -6.16255 | -42.47584 | 2024-10-03 00:33:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 97c97ae7-beda-31ef-b34a-7c8239f51d98 | -5.92725 | -42.83929 | 2024-10-03 00:33:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 25b41f8d-5e15-3cb0-962b-82e7b10e1a97 | -5.87871 | -43.42613 | 2024-10-03 00:33:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8d78d239-05c6-3d3c-91c7-b0288d14b458 | -5.83279 | -43.95654 | 2024-10-03 00:33:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a59d713f-bb26-3ee5-ad60-57ee4c4f9387 | -5.82092 | -42.53933 | 2024-10-03 00:33:00 | TERRA_M-M | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 472bf829-539f-32f1-ad68-56c65cf5b1e0 | -5.3934 | -43.10858 | 2024-10-03 00:33:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3b00abc8-ba10-34a8-bd7c-f435eab77a0e | -5.31839 | -42.9674 | 2024-10-03 00:33:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 52152d8d-639e-377d-9d70-6d6899e02a4f | -5.25133 | -43.81506 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ec8f7cf7-9fba-3a2b-98b4-681cc3aab398 | -5.25001 | -43.80543 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 82265521-a96e-32f8-ab00-6fdff0aa5276 | -5.24868 | -43.7958 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 07eae0c7-16db-3914-b376-acb9ec311746 | -5.24478 | -43.83568 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| db96e5b3-1499-32ec-9814-014bc67ffff9 | -5.24212 | -43.81635 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| fd6ec07e-e1bc-3bbb-88a4-cb092e522f4f | -5.2408 | -43.80671 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 965.9 |
| f7e07e6b-48dd-313a-87a8-d0e1c1b06e61 | -5.23947 | -43.79708 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 277.9 |
| 080b22d0-059c-3ab4-8767-d3e29f51c52c | -5.23159 | -43.80802 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0548d22f-9d0a-3a50-9d48-abed79fdf687 | -5.11082 | -43.33176 | 2024-10-03 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 56062309-a703-39bc-af5c-ac47e82b0bff | -5.10953 | -43.32251 | 2024-10-03 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 14945beb-e225-33d4-bf7d-3a65b90e4dfc | -4.93277 | -43.78001 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 156.3 |
| bc89263a-67e7-328d-904e-7806bfd059cf | -4.93146 | -43.77042 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 72b107a0-1eda-386c-a6db-e9057e92ea3a | -4.9249 | -43.79089 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2d6ad4a4-2921-3412-bae1-9c1e589de485 | -4.92359 | -43.78129 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 8024a6da-24eb-3f4d-bc94-120e6b999765 | -4.92229 | -43.77172 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 86782a18-f619-3eb8-89b7-03f6fc24e914 | -4.70277 | -40.02163 | 2024-10-03 00:33:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 3c62dd72-9c4e-3a77-b353-cc9c9bb0a174 | -4.66422 | -43.76764 | 2024-10-03 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 20c5c2bd-fd7f-3a1d-968e-bfbc48f32d24 | -4.66292 | -43.75816 | 2024-10-03 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 27c80340-441e-3c9f-b1b2-25d0082ff407 | -4.56432 | -38.84118 | 2024-10-03 00:33:00 | TERRA_M-M | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 4be9a3de-7b67-3e0c-aeef-96d6bfbfa665 | -4.54665 | -43.31619 | 2024-10-03 00:33:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 488d382a-bf65-30d1-81ab-c621be2b70bc | -4.54538 | -43.30704 | 2024-10-03 00:33:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 6679a632-0d59-3dce-ac90-afc7e66bc468 | -4.53766 | -43.31744 | 2024-10-03 00:33:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 5ed2c888-4139-3551-a342-e59a05073382 | -4.53639 | -43.3083 | 2024-10-03 00:33:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| a4722d85-18a9-3821-a180-09a911697349 | -4.53513 | -43.29916 | 2024-10-03 00:33:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 31511c69-d629-3d72-a7bb-e3f67cfba0fc | -4.47754 | -42.88429 | 2024-10-03 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f579d3ec-3562-3679-8b93-80804c138806 | -4.46988 | -42.89446 | 2024-10-03 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 59187699-2694-3fe4-8fe6-338ea87a18c5 | -4.46865 | -42.88554 | 2024-10-03 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 7bb1a9eb-4ca4-3ae4-891c-929721e65479 | -4.43678 | -42.91734 | 2024-10-03 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a04bf5b0-7087-3ae8-b77a-15b7a0e62893 | -4.43555 | -42.90841 | 2024-10-03 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 99bc8cbb-e25a-3cbe-8cd0-30cb3e61ea76 | -4.42815 | -42.85485 | 2024-10-03 00:33:00 | TERRA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0a4e7ef1-f287-301d-9db2-46d16670e39f | -4.42692 | -42.84594 | 2024-10-03 00:33:00 | TERRA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 1f56a2e3-5c77-3be0-ac25-2d1c1aa77753 | -4.42665 | -42.90967 | 2024-10-03 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 72137baf-4285-38db-aa3e-3f0277e7726e | -4.02125 | -43.24414 | 2024-10-03 00:33:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 209f0f1b-c41f-33ff-ad37-447d3f6d6477 | -4.02001 | -43.23512 | 2024-10-03 00:33:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7535a674-7230-30de-9663-d3fbf289356b | -3.94815 | -41.52534 | 2024-10-03 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| da16a981-736e-38cb-9d28-bd63caa8aac6 | -3.94689 | -41.51641 | 2024-10-03 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 31.1 |
| be62fc53-3dc6-38d8-ba59-b73d0263899a | -5.70851 | -43.92989 | 2024-10-03 00:33:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| bd6389cf-f201-3558-a548-99798e4fe944 | -3.94562 | -41.50747 | 2024-10-03 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 40e3b93d-8ac1-33ac-9199-7f1e090641e4 | -3.86128 | -40.78335 | 2024-10-03 00:33:00 | TERRA_M-M | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1a0a4ae3-b438-3285-8621-ae0623c66104 | -3.60144 | -43.80706 | 2024-10-03 00:33:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c40e3654-3e81-37c5-a33d-04714e150cdf | -3.42506 | -43.33379 | 2024-10-03 00:33:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 14295918-2053-3f97-a785-2448f1d01c3c | -3.40952 | -42.28549 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d623b674-f98c-3c3a-886d-ad0b913132eb | -3.40069 | -42.30164 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 91168126-4680-34c3-a058-f4a76b157978 | -3.39947 | -42.29284 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7cd146b1-6840-3662-9f04-d50372ab1971 | -3.39824 | -42.28405 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 387.2 |
| 3e4a7646-1b25-3ca2-9904-74bbfaaca2d2 | -3.39702 | -42.27526 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 349.6 |
| a0c05a7e-e87a-3746-a4b4-7bfbb7eb57bb | -3.38941 | -42.28531 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9ad1d1cc-f0db-3fce-9895-c5f80a6b7e48 | -3.38819 | -42.27651 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 55c845af-6130-33cc-8eee-2156d1470698 | -5.56976 | -43.11849 | 2024-10-03 00:33:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 643a4c6f-9068-3025-b151-8e8fd3ce9ce4 | -5.5685 | -43.10933 | 2024-10-03 00:33:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 6b23b700-9e86-37f6-bf9f-455c14380b5d | -5.40419 | -42.92198 | 2024-10-03 00:33:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 0ff41686-4b55-3886-b952-cfc4c35cd5ed | -5.41439 | -42.92977 | 2024-10-03 00:33:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a709cecc-2c87-33e0-b9da-ea539b4bd104 | -5.52367 | -42.78253 | 2024-10-03 00:33:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 831efd7e-1e0d-31c8-b82e-7122a66cde5b | -5.53258 | -42.78125 | 2024-10-03 00:33:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| db4c552a-d686-3c58-8654-4161ef0592c3 | -5.5595 | -43.11056 | 2024-10-03 00:33:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c33f45f2-3751-3466-99a1-395cc3ec498a | -0.9906 | -46.8108 | 2024-10-03 00:33:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fe184293-d500-318d-b431-15ff1e20461e | -1.90593 | -47.88951 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 11b8c30c-b613-3927-b348-7e32402428a9 | -1.91754 | -47.88783 | 2024-10-03 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a31db314-ebcc-327f-a2c5-4bb43f5a8b57 | -1.7509 | -54.4531 | 2024-10-03 00:35:16 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| a86116a2-cdd8-38dc-bce2-262634a252e2 | -1.7692 | -54.4528 | 2024-10-03 00:35:16 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 1c41c144-7cad-3d7c-89d8-36f7db2d38c4 | -3.3854 | -42.2866 | 2024-10-03 00:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 231.3 |
| d0765348-857f-35d6-a575-0037cc7f6a8c | -3.3855 | -42.263 | 2024-10-03 00:35:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 800fb137-1a8d-32a1-a6b0-af287a1ffc6d | -3.404 | -42.2858 | 2024-10-03 00:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 356.4 |
| 842e3775-56eb-3d23-9e06-71d8a271e76c | -3.4042 | -42.2621 | 2024-10-03 00:35:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 163.8 |
| ba646949-6b90-335f-884c-93d548103b30 | -3.4227 | -42.2849 | 2024-10-03 00:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 9c539f90-dcdd-30d1-9f9c-3ca46541f9aa | -3.3322 | -53.7579 | 2024-10-03 00:35:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a86b8514-2923-3e89-9d09-ed63006cdd2b | -3.802 | -47.8104 | 2024-10-03 00:35:27 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 93eaca4b-39a1-3eba-869d-91600f80604b | -4.0949 | -48.4894 | 2024-10-03 00:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 1675594c-4be4-34bd-8e75-cfcf67b0f1b1 | -4.095 | -48.4679 | 2024-10-03 00:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| df82f485-4215-3cf2-a0de-ff8856369ccd | -4.1134 | -48.4886 | 2024-10-03 00:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 81d5fb19-86db-3bf3-8058-9d22f4b6f931 | -4.4286 | -42.8431 | 2024-10-03 00:35:31 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |


[Clique aqui para ver as próximas entradas](README19.md)
