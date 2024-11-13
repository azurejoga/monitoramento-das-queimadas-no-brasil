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
| 63d090fc-44bd-3871-9154-83fdda1dafb6 | -1.64951 | -47.47647 | 2024-11-13 04:04:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a99a7c46-ced6-3f18-8e1a-9fc90cc1d662 | -2.46667 | -50.12348 | 2024-11-13 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| eef07eab-8b09-3ea6-a0d0-e16b50a3b39f | -1.28497 | -52.47394 | 2024-11-13 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01ea9e16-2a45-3605-9e63-8802dcf4a7c1 | -4.81938 | -40.14655 | 2024-11-13 04:04:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fb6c4f2b-5818-3a81-9b1a-291a99107af4 | -4.22009 | -46.45446 | 2024-11-13 04:04:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 459a001c-8cc8-315e-aabb-e90e5e74537b | -3.14689 | -53.24424 | 2024-11-13 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b9d547ca-464e-320a-961c-f56d73a0ee1f | -2.64994 | -46.82564 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c25126db-940c-36e1-9236-7fdf71eb21a4 | -2.30355 | -49.08432 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17a4a644-b1e7-3082-b2e4-5991f8b16f64 | -3.06366 | -50.34528 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 82a00742-fb5c-3d03-a391-36f1cef2ff46 | -3.34193 | -48.98377 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 299b571f-3ee6-3e5e-b408-66b77e1839c4 | -3.34634 | -48.95662 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 86325fbd-da67-34b7-b304-a9149df71299 | -1.34653 | -47.34692 | 2024-11-13 04:04:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce671cb5-7f44-3dc2-aad1-cf758db75f31 | -1.99991 | -46.18969 | 2024-11-13 04:04:00 | NOAA-20 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dca7397f-7ecb-35d0-92c6-799b670cc1a7 | -3.23028 | -50.66789 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba0f274f-6500-3db0-8a36-c668e6fe3ebd | -3.02935 | -50.979 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0eb0b444-4f43-3d8c-8709-332473e678e2 | -3.70958 | -43.19755 | 2024-11-13 04:04:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20091db8-308f-3ac6-9b1a-938d05d68802 | -2.36537 | -48.52217 | 2024-11-13 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf6436de-2c44-3922-9060-5fd932a6b26c | -3.76734 | -50.703 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8ddf490-5354-3ae9-8150-bfe4c2d0208d | -4.42479 | -45.95033 | 2024-11-13 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69058471-ff1c-3dcc-829a-6549fd7d2030 | -2.1108 | -50.69623 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 089c4fa5-aa9d-3149-985f-910457aacd92 | -4.04323 | -48.09819 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1b5e5381-50b1-3477-81f8-b410a67c059a | -4.71193 | -42.78555 | 2024-11-13 04:04:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6aa42165-07bf-36fe-af67-4201acb5fc81 | -2.77713 | -50.29815 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4a49cc4-6cb7-33d7-a943-a81a1894180f | -4.04888 | -48.32165 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5853a12f-600f-30a8-b8eb-b619a21a0c9a | -2.20711 | -53.74273 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6ea2eddc-4a7c-3da8-9c23-7e84a08d45cf | -3.07464 | -50.34714 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6550d32a-dea6-36dd-9fe6-d1291424efc9 | -3.35055 | -48.96424 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1fcfed1a-5144-3c95-b715-a8c2ab004a5d | -3.33863 | -48.97409 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 154eb9c7-3906-318d-8fa7-ff8f18c0cba8 | -3.83045 | -46.52439 | 2024-11-13 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06d4efe5-7814-3d01-ace5-2f426ded802c | -3.99953 | -46.52776 | 2024-11-13 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45d0def5-62c6-30f7-ba22-9697f0f904de | -2.59556 | -48.20067 | 2024-11-13 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d37cf852-d016-335a-bdea-fbe8cf1236e3 | -3.05386 | -50.33637 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| aba3166c-87ef-3928-b7b4-1458bc0fa427 | -2.21284 | -53.74841 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5c90faab-288d-3358-b283-2c9f1ddd7947 | -3.06794 | -50.35342 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cfcf194-5039-3633-a3e5-6e40fd55020d | -3.05935 | -50.33727 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8e223177-9b18-36b5-8d3b-cfef1279097a | -1.20608 | -52.13408 | 2024-11-13 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d14db98-f375-36b1-83b1-384baae6b6d7 | -3.4998 | -50.84311 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4c452862-9c9e-3564-acfd-3bc76dd8c3eb | -2.60633 | -48.25632 | 2024-11-13 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28e24b89-3a8c-327b-87dc-2e8ca943d4c4 | -4.58329 | -40.48443 | 2024-11-13 04:04:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 116ad0a3-9d67-31fa-96e0-d7b1d2ea288d | -3.02159 | -50.98309 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 200e86f7-cfef-347f-9ef1-f456bbb58085 | -3.06197 | -50.22147 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| daed261b-2f94-393a-ac1a-15e70bb1db1a | -2.63464 | -46.15369 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e21f291f-770a-3551-94a6-2390f410a631 | -3.25389 | -43.26186 | 2024-11-13 04:04:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 60b0eac8-9c1b-3c0f-8b1e-847e731ae768 | -3.34055 | -48.99226 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52c21f87-c1d1-37ae-9f27-96e1e5ff30f0 | -2.11403 | -50.70091 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b46f1152-3068-302d-bee9-c7256288278d | -3.16648 | -48.37044 | 2024-11-13 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2948f619-5671-389f-9793-f988ae622e39 | -4.42421 | -45.95383 | 2024-11-13 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e2f7e8d-02c1-324b-9f96-4c142b13cfe3 | -3.67078 | -50.74095 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63651d08-6040-3bd6-9a41-e0e6925310ef | -2.63818 | -46.15811 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50b63474-559e-3f5c-aae8-1722d491c4d5 | -2.17982 | -46.99637 | 2024-11-13 04:04:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4f148ec-c786-39cb-a3f4-dcb044950153 | 0.90921 | -50.14545 | 2024-11-13 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4daa1eef-6065-347d-897e-c996f7047375 | -3.3396 | -48.96836 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fca7c4f9-5e84-3a13-96a2-fc1b6b98e19c | -3.34542 | -48.96229 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 072816d7-bd8a-354d-9233-6d5934c5e844 | -3.94083 | -48.14817 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bbe6d74f-169b-3e1c-a04a-5c9d077021ab | -2.73143 | -51.83412 | 2024-11-13 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b723979c-9ef0-3c40-990e-b32fbc1baee5 | -3.14397 | -45.97461 | 2024-11-13 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0c5777c-a7da-3d1f-aa65-3b970d2fd8be | -5.24395 | -37.69354 | 2024-11-13 04:04:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1c2aac9d-40af-30ef-a2aa-10e6d9c03e40 | -3.859 | -49.11794 | 2024-11-13 04:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d75b4ce-3aa9-3392-b9f3-d904a71381d1 | -3.02295 | -50.98194 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39828052-db74-3348-a0ed-1d97f6b4b5bb | -4.22682 | -38.1414 | 2024-11-13 04:04:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1233686c-33a2-3b93-a046-eee419bf4359 | -3.10302 | -54.31023 | 2024-11-13 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7608ce2-d37e-30b4-89f5-39a8e9308f22 | -3.5162 | -49.96187 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ddd5a04-ae3d-38dd-90ea-2e8dd6e1fcf7 | -3.20975 | -46.5311 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d862ca0-95ad-3b72-a84a-75fc1180bdcf | -3.10099 | -54.30922 | 2024-11-13 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d16e818c-5d1c-3d9c-994b-6617cd44057d | -4.04481 | -48.25931 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 985f327f-b132-3bc5-98a8-ac5ad8c66b3f | -2.43612 | -49.22357 | 2024-11-13 04:04:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25fed6a3-e150-3208-8d9a-c35172bc970d | -2.65998 | -46.81877 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2307b528-a847-3778-a08d-3c3671456c3c | -3.35649 | -48.95938 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a7590e1f-8c8f-3b5b-823f-f0dbaa72d299 | -2.7847 | -51.40454 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5985739c-9b99-3519-8ae1-44f85b343b43 | -1.84658 | -46.28266 | 2024-11-13 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 704d14d8-4549-3503-aec1-5459ae07831f | -2.69653 | -49.34753 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c9d9e81f-43fd-3de3-a4a6-9739daa287a2 | -3.33152 | -48.98478 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e57db55d-ec7e-3ee6-824e-8e0fc18af8df | -2.5371 | -46.32326 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c921d25b-60ce-3440-b2e6-742746d87659 | -1.38493 | -52.39602 | 2024-11-13 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ecce997-126c-3543-9a87-0c4fa683d38b | -2.29322 | -47.91534 | 2024-11-13 04:04:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2be5627-16da-3a32-87e6-8ecc4fde8271 | -3.14339 | -45.9782 | 2024-11-13 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48f24713-0b59-37eb-8455-e8acf0fe60f0 | -3.76362 | -50.69117 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| db3451d0-5113-3872-b7e0-81cb20748803 | -2.20599 | -53.74919 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6e57e5b8-0588-39c4-aa0f-7ed8a752f292 | -2.65606 | -46.78831 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4a708a3-043f-311a-a5e5-b3a706dd732e | -3.51674 | -49.95854 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 746803e1-9504-31e4-81c8-d07724f637da | -2.82151 | -46.65517 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d084b0ee-d100-3381-9ad9-18195122bfaa | -2.24036 | -53.755 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 565458e4-20cc-3ca9-b4d2-5665fec1e694 | -3.95289 | -48.19067 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69bdc6aa-5fff-302e-9bac-a1202ccb3823 | -2.12222 | -50.69806 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff9dc903-e463-33e7-8694-d4e38bf0ccdf | -2.1153 | -50.69296 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22d47679-0662-3f0b-9ffe-3c0a1f2a6d7d | -3.25874 | -50.39714 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfe8052c-46a1-3924-8d3a-05781afd612c | -4.58502 | -43.9775 | 2024-11-13 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cae66da-bfe1-3818-88c2-ff9e74ad37e8 | -3.0217 | -51.09338 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b405763-82a4-3867-9618-4f22e095fa69 | -3.29998 | -51.60023 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12af2f4e-4802-3915-a409-b20f1c80981f | -3.04896 | -50.33194 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a473d2fe-9cb4-3a60-94ca-30616875acc4 | -2.18425 | -46.99711 | 2024-11-13 04:04:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0eabf16-9c91-3589-9c9d-0b8f61f8af11 | -4.33111 | -46.54205 | 2024-11-13 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c27bc22-de7c-345f-abb4-e55f1fd817a2 | -3.94781 | -46.70987 | 2024-11-13 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0fccec9d-e217-3c99-b02b-ef356362e372 | -2.37027 | -48.52299 | 2024-11-13 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1966d4a9-b64a-33ab-ae12-2995672956f7 | -2.57202 | -46.53382 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c453d245-e664-35e2-8115-08810df1634b | -3.07212 | -50.32843 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| de589ce0-dd1f-371b-b6e8-4c1f99158f98 | -3.79597 | -47.45906 | 2024-11-13 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 35b65c7e-adca-3b52-8125-feacb80cd21f | -3.3519 | -48.98549 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c51b3d0-de7a-38fc-8abc-530c0773290b | -2.57301 | -48.12814 | 2024-11-13 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a1f2e78-0bb4-3b5c-9c59-7150b8176a7c | -2.73098 | -45.29716 | 2024-11-13 04:04:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README19.md)
