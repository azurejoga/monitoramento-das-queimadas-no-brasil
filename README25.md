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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdb0783d-1edd-3bce-b4e8-d5adb341c576 | -8.4617 | -44.51199 | 2026-09-18 03:36:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 387555fe-4127-38a7-8f19-32c71f3f2a40 | -6.34458 | -43.37398 | 2026-09-18 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c96329d2-5f27-36cd-9146-7964545c1e57 | -7.7871 | -44.87907 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83b85b96-dfe8-3b53-8589-4303c6ff1f15 | -7.05831 | -46.22593 | 2026-09-18 03:36:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2cde2b97-38d0-37cd-b11b-8511f7f1e904 | -7.00418 | -43.6348 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8539e711-dc17-3125-873b-02e1dd1d8d6d | -4.55573 | -42.96927 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f68d66dd-08ed-3f90-b279-57f1b0e1224a | -8.4944 | -45.6561 | 2026-09-18 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e21d4d6-2b22-3e8d-bbab-33e678c6511d | -6.66296 | -43.63489 | 2026-09-18 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de1f6b66-6864-346b-be9b-d2eaaa38781e | -7.93486 | -44.84075 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 796313a4-d7a3-3813-9823-0e4bbb2b1e92 | -4.41021 | -42.31522 | 2026-09-18 03:36:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 88cae2f7-a6a3-37e8-99ee-cedd7866d369 | -8.45072 | -45.84398 | 2026-09-18 03:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81da961c-36b9-3048-a5e4-6445106dd1e5 | -6.66211 | -43.63944 | 2026-09-18 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7fa560bc-7e59-3c30-96e0-ff7fc510e927 | -7.34562 | -44.63038 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 39381364-27f3-3afc-bec0-44bdb8bfe6f1 | -7.00329 | -43.63951 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5ecc7a08-7dd0-366b-9829-117c5c7d4ed2 | -5.74868 | -45.1023 | 2026-09-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d7a826da-a12e-362e-be00-59828e2e5d1f | -7.00939 | -43.64056 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8846024a-bbdd-30e3-b417-7413012cd35b | -4.55133 | -42.95883 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13e79f30-5b29-3636-943f-115715bde4df | -8.67741 | -45.44145 | 2026-09-18 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef5bb3a0-1865-3664-ae51-303c55f95939 | -6.96164 | -42.57238 | 2026-09-18 03:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 279b7005-5ced-3144-b1d9-487229bf7972 | -6.27207 | -41.66542 | 2026-09-18 03:36:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4eea3e97-8d9f-3ee0-8b9d-5536d6658a6c | -8.55851 | -44.90821 | 2026-09-18 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa23ceb6-1a54-3e9b-9ab8-bf921ca9d0e8 | -5.63382 | -44.80574 | 2026-09-18 03:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3802972f-5dde-30fb-a3ae-e8cb3769a187 | -4.56426 | -42.95655 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0b2ab163-b7f0-3735-871d-cfd73891766c | -8.88183 | -45.9 | 2026-09-18 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 192ebb9e-2b48-373a-98f0-09fc82f84665 | -5.6309 | -44.80302 | 2026-09-18 03:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8efc6b3b-f840-3cab-bd2c-d1747fb25f65 | -5.32859 | -45.14925 | 2026-09-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfae3ae6-4a08-3747-8a02-e6d146fe5a7b | -7.0026 | -43.64231 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6998719e-6b6a-3284-9575-4cdbc8c1a123 | -7.78922 | -44.90328 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c434439f-a5b5-3b7a-88b4-5688fe0aae71 | -8.49542 | -45.65087 | 2026-09-18 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bee7605-444c-3f07-a4b5-8987305ca38a | -7.01731 | -43.63052 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3801f88-e0eb-36a4-b4fd-8b935795b9b5 | -4.56064 | -42.94173 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c87ef0d0-4a85-30a6-940b-d1ebeb8af360 | -7.19373 | -41.81109 | 2026-09-18 03:36:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c828a3ea-60da-39ef-b45d-378fa0d2a0f5 | -8.43898 | -45.71337 | 2026-09-18 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5047969f-2190-3c12-bfbc-c48f005951a5 | -4.56551 | -42.94548 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a523e359-106c-3f3a-a8cf-7879fd77c640 | -5.63435 | -40.86546 | 2026-09-18 03:36:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f3459062-79ea-3198-bb09-6af47ca18de1 | -4.55982 | -42.94635 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ca4edb1-2cce-3a91-96b7-220922d29acd | -4.51171 | -38.50986 | 2026-09-18 03:36:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e0925ea0-c67a-3bf2-853d-810ff317fa8d | -7.2014 | -44.10543 | 2026-09-18 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d66984fe-b070-3206-8713-37361501b46f | -7.29174 | -38.9621 | 2026-09-18 03:36:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 09f268b8-cfa0-3108-b136-0076e2a5acb7 | -8.54052 | -44.55826 | 2026-09-18 03:36:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bc1fa20-f0a4-3ba9-a097-fc156f06b0f6 | -4.58327 | -42.95524 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8acca9eb-09f2-3fb0-8d66-741bf0ca345d | -8.46501 | -44.5285 | 2026-09-18 03:36:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 008766e8-427b-34fe-a006-02ecdcb7da40 | -8.4882 | -46.88728 | 2026-09-18 03:36:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f94b1ac6-9117-3522-82cf-a559c163804f | -5.76782 | -45.11275 | 2026-09-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa27ce3c-db35-3f4b-97cf-1f51f4efd0b4 | -7.01039 | -43.63404 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5ac0f928-50bf-3796-8867-3f93d183fd80 | -7.67573 | -46.0923 | 2026-09-18 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f4ae46e3-5478-31e8-865a-784757986eea | -8.87657 | -45.89106 | 2026-09-18 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 925667f5-ef0e-34ed-bcbd-2a01f0561dd8 | -7.34235 | -44.64411 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9747369b-5964-3c00-9c6f-7ee48580d470 | -8.7016 | -44.89473 | 2026-09-18 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa2d81a8-23c7-31a5-b88f-78bc0ad9355c | -4.3885 | -38.21738 | 2026-09-18 03:36:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2180e53e-6755-319e-8edf-4a37051b38ae | -5.75089 | -45.09017 | 2026-09-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| a07b43e2-0814-3d61-a9d7-330a32972005 | -6.91192 | -41.71388 | 2026-09-18 03:36:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f49260d9-cc0e-3650-9b69-703bfb9da9b9 | -5.75777 | -45.10035 | 2026-09-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25347d20-2053-3a49-a5ac-ca19fbead04b | -7.14699 | -41.40678 | 2026-09-18 03:36:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6c2de25c-0762-3423-81fc-0a6bd1ea7396 | -7.00069 | -42.161 | 2026-09-18 03:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 60e2fcc7-199d-3121-8753-3562dbd61974 | -4.93518 | -42.8908 | 2026-09-18 03:36:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df21f06a-106f-30a3-86d3-c8428d9cc5b4 | -8.4702 | -44.53532 | 2026-09-18 03:36:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c69697dc-9313-3785-9649-8c178826db0e | -8.90759 | -45.01297 | 2026-09-18 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 833ea08f-4da5-3805-b600-4d5fc03c3bbe | -6.34373 | -43.37862 | 2026-09-18 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 28c9c137-8cc6-3baf-9058-49ab38c72ead | -5.54826 | -35.75737 | 2026-09-18 03:36:00 | NOAA-20 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3f1dffa3-c81f-39b4-8050-c8c003f97333 | -7.34445 | -44.63274 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4ce7fa8-6c0d-3ef6-8ef9-6ac397a5ccc7 | -8.07796 | -37.6893 | 2026-09-18 03:36:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e4f7afe9-076e-3e08-80ad-a2d10e1e7a6f | -4.56924 | -42.96027 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6bcea979-aa7e-3696-a3b9-fd95966a0003 | -8.67534 | -45.31084 | 2026-09-18 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7eda96d8-d474-3bf3-b597-0e74ae291f47 | -7.93383 | -44.84624 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f1d9e32-63a0-36bd-b964-c77c5a870c5c | -7.81527 | -44.90773 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9197222-cbf7-38cd-a4b2-2c44d7c3fff1 | -7.01647 | -43.63517 | 2026-09-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d372b73b-3b5a-3a0f-87aa-fab0c21c4ae0 | -5.33538 | -45.15077 | 2026-09-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da0ccb23-8f3f-3ecc-92be-b35b71dd92c2 | -8.46074 | -44.51695 | 2026-09-18 03:36:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aedc0968-52cc-3dbd-84cf-7104f29066f4 | -8.68125 | -45.44484 | 2026-09-18 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 391cdacc-07c7-31a4-93ec-b1d3e1ba68c3 | -5.76899 | -45.10625 | 2026-09-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8c01130-2958-36da-8a95-aff407006835 | -7.29415 | -38.96584 | 2026-09-18 03:36:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f9793223-cf7a-3118-8729-62a2914f3ec5 | -6.91349 | -41.72538 | 2026-09-18 03:36:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6ee126bc-7ec4-32ad-9e27-769ba0fb74af | -6.29097 | -41.78532 | 2026-09-18 03:36:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0255fca8-82b2-3e45-a557-61391319a98e | -4.58931 | -42.95647 | 2026-09-18 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d902e57f-feed-3bad-a915-94961a2d06b2 | -7.80875 | -44.90666 | 2026-09-18 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4126b238-cce3-37aa-a506-d45676390c01 | -6.40858 | -43.47156 | 2026-09-18 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c936c355-fcf2-3f9d-b3bb-8f08606b87ee | -10.4847 | -46.31725 | 2026-09-18 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4664066-20fe-3509-8613-c1d55e03041e | -9.39167 | -46.85911 | 2026-09-18 03:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 721d1f9f-285e-3762-bbf2-1b39182c0368 | -13.2511 | -46.91452 | 2026-09-18 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6a103d42-4998-35f3-9791-a8c41345161c | -14.96089 | -46.24976 | 2026-09-18 03:38:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d37c3e98-93fa-3f18-8b08-7f1bb5f2f452 | -10.60585 | -46.56431 | 2026-09-18 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 10964870-28d1-3645-ab76-648c0cfe82d7 | -11.15941 | -42.7983 | 2026-09-18 03:38:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 06478c7e-4630-34b3-bae8-5dce2e430f24 | -13.24609 | -46.92013 | 2026-09-18 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f57a46f1-3b01-3944-ba96-d65e6fdf23ba | -10.61097 | -46.57033 | 2026-09-18 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d07e3807-ebbf-3fe7-9677-23140a160ed9 | -9.09356 | -45.71885 | 2026-09-18 03:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a16cc6d-759a-31ac-a2cb-af61cdbc4225 | -10.11636 | -46.30293 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 602f58e8-5134-3ae0-8797-3d30f355c0a2 | -13.24595 | -46.90588 | 2026-09-18 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 62b4db9c-b3be-3350-9ad8-7004a16ac632 | -10.61255 | -46.56625 | 2026-09-18 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fb1dd11d-b3fd-30f2-a8fc-04350a0f1721 | -11.31309 | -46.77425 | 2026-09-18 03:38:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 26b846c2-6a49-3eb3-9ab3-323934f4199f | -9.74631 | -46.5767 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 132b44ea-d956-3c1c-8a24-6237e823be1c | -12.16302 | -46.98656 | 2026-09-18 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7c587941-bd6d-3248-b84c-53f3957502fb | -9.93745 | -46.61494 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 88809a38-141a-3054-8b92-9dd4b6b7f4e1 | -13.6155 | -46.9636 | 2026-09-18 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1307e2d-7eb6-36a3-9e80-92d4bdc7a6e1 | -14.11028 | -46.94316 | 2026-09-18 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e800e5d-ae73-32f7-b24e-8b51948a9c9c | -11.51985 | -46.87861 | 2026-09-18 03:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a6d68ecf-4f9e-3e13-8549-4cdf442dd78a | -16.55857 | -43.99546 | 2026-09-18 03:38:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b44c0dbd-b8c9-31e2-a9f8-3d4bd4670886 | -12.67906 | -43.91283 | 2026-09-18 03:38:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0106200f-9920-3b8e-9f4e-a79a31bf2a2f | -9.90976 | -46.50723 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b6907f2-72e3-3c8a-a135-bc2a4545997e | -10.02527 | -45.57267 | 2026-09-18 03:38:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README26.md)
