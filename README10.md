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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c9abfab-812b-376a-b87f-2ae5d40e0768 | -5.8641 | -42.000599 | 2024-10-10 00:20:30 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 51d40de2-3093-3312-8bd5-f3cb372a2e81 | -6.2764 | -43.8232 | 2024-10-10 00:20:30 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f82f7f8-2770-31ec-8741-999df2d61dd7 | -6.2781 | -43.830898 | 2024-10-10 00:20:30 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eda1ad4d-c85b-339c-9070-64130bae295f | -7.5497 | -49.433998 | 2024-10-10 00:20:30 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f2cdd8b-e151-3472-9afe-29397ecd3a21 | -7.5533 | -49.451302 | 2024-10-10 00:20:30 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 708ae300-f16c-325b-842f-d46cf6f7828c | -6.4327 | -44.3382 | 2024-10-10 00:20:30 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78890b9d-2924-33f9-baff-618fe7b07393 | -6.4344 | -44.346199 | 2024-10-10 00:20:30 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 258e1dfa-d83b-328c-8e34-2bb4f4719e73 | -6.4362 | -44.354301 | 2024-10-10 00:20:30 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3fd4099b-63ec-3683-bead-bf59804c5e81 | -7.54 | -49.436001 | 2024-10-10 00:20:30 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3f213bf-9e73-3ded-b155-7f31ee420898 | -7.5436 | -49.4533 | 2024-10-10 00:20:30 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9602225f-2b55-313a-aaf0-d797b5ca1279 | -6.382 | -44.157398 | 2024-10-10 00:20:30 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb7d6f0c-20f9-3eda-91cb-92d96e2d77e2 | -6.7113 | -45.641399 | 2024-10-10 00:20:30 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e375e67e-fbdd-31a0-b43a-ab9610c9f328 | -6.7134 | -45.650902 | 2024-10-10 00:20:30 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e34883a-5088-31a3-be64-32e4e2191e56 | -7.5193 | -49.386299 | 2024-10-10 00:20:30 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18a2ce23-237c-3ec9-bf9f-8251e3ee3401 | -7.523 | -49.4035 | 2024-10-10 00:20:30 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b96ea91-bf55-317a-9bc8-073dc6d61c6c | -6.7015 | -45.643501 | 2024-10-10 00:20:30 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9132d21d-4d36-33ba-a45e-c13dfa760059 | -6.7036 | -45.653 | 2024-10-10 00:20:30 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84d27e92-e0bc-33d6-97c8-5dce0a9fccaa | -6.454 | -44.5723 | 2024-10-10 00:20:30 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5bef1ecf-eddf-3e5f-ac41-c5a3ba5a7575 | -6.4558 | -44.580502 | 2024-10-10 00:20:30 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e1307c9-858d-3c81-a7ef-3a8bf6222c03 | -6.1167 | -43.341999 | 2024-10-10 00:20:31 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 447614b7-572d-3f4c-9c2f-6d1bbfe25527 | -6.1184 | -43.3493 | 2024-10-10 00:20:31 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d34e9bf-da7b-3983-a94f-95d142afa7b3 | -5.804 | -41.9636 | 2024-10-10 00:20:31 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 87b4a366-ceef-3450-a3f4-9ac4812b2e1d | -5.8056 | -41.970402 | 2024-10-10 00:20:31 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3081eec9-46db-3b29-8da4-ea3ece4b9b7d | -5.7942 | -41.965698 | 2024-10-10 00:20:31 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ed861806-7bf9-3169-bfa5-cac11e341ef1 | -5.7958 | -41.972599 | 2024-10-10 00:20:31 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e1c29541-1af9-3215-aed7-e607f24223a9 | -6.2546 | -43.772202 | 2024-10-10 00:20:31 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4555deb-7b10-3926-8021-e6e885147c5c | -6.3658 | -44.268902 | 2024-10-10 00:20:31 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74d51bd5-c138-34cb-bdc6-f312447c1ab0 | -6.3676 | -44.276901 | 2024-10-10 00:20:31 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96bf170a-7713-3ca0-8deb-8903a2183066 | -6.7423 | -45.968899 | 2024-10-10 00:20:31 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9684bf38-82be-3f9e-b7d1-44403e336a85 | -6.7445 | -45.978802 | 2024-10-10 00:20:31 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24abcfab-9db9-3cf6-b843-9302c24c4856 | -6.766 | -46.216801 | 2024-10-10 00:20:31 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b321ba6-78fa-3dfc-aacd-3bad1b9a8f5c | -6.7682 | -46.2271 | 2024-10-10 00:20:31 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d0fe213-a48d-36c6-ba0c-135097a122d9 | -6.7705 | -46.237301 | 2024-10-10 00:20:31 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 938d15bc-d333-3805-8ca1-3f22b29f891c | -6.3526 | -44.4403 | 2024-10-10 00:20:31 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8755005-5a91-317c-9f95-727d5489aa37 | -6.0645 | -43.384201 | 2024-10-10 00:20:32 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b58248df-1692-3200-a8f1-5a09a0b84756 | -6.9337 | -47.221401 | 2024-10-10 00:20:32 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee1c92f0-e2d7-3086-9a22-44082f15cb45 | -6.9363 | -47.233398 | 2024-10-10 00:20:32 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfd91f73-5d68-3beb-9af5-abac45a19b1e | -6.9389 | -47.245399 | 2024-10-10 00:20:32 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd2de687-4372-3eb4-9b81-40f7fc487000 | -6.0987 | -43.719398 | 2024-10-10 00:20:33 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbd9df01-3d43-3a8a-a88c-cadec4034b69 | -5.9261 | -42.908199 | 2024-10-10 00:20:33 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4384a5e7-1351-3c83-a73f-d746b0a9b1d1 | -5.9277 | -42.915298 | 2024-10-10 00:20:33 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ec815b38-607e-3e0d-be55-7dae0373c452 | -6.097 | -43.7118 | 2024-10-10 00:20:33 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed0560a1-17d6-355f-8105-f7cfa601e5a7 | -6.2881 | -44.565498 | 2024-10-10 00:20:33 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fadc2bb4-6fdb-3c0c-8f31-e0f17b14e366 | -6.6719 | -46.301701 | 2024-10-10 00:20:33 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d2f033b-9da6-3a0b-864f-36f9ce949cfc | -6.9065 | -47.378799 | 2024-10-10 00:20:33 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96905e28-5198-3a72-b651-16f6055e5ffd | -6.9091 | -47.391102 | 2024-10-10 00:20:33 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5802909e-e078-3fed-b6d6-c414a1075937 | -6.1923 | -44.182598 | 2024-10-10 00:20:33 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d44901c6-6d5e-3a87-8f0a-23b595412360 | -6.1941 | -44.190399 | 2024-10-10 00:20:33 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87467e9c-6032-3378-9d8c-87e5c798c6a8 | -6.8993 | -47.3932 | 2024-10-10 00:20:33 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 557e23ee-dde3-3654-9025-4462aa95870c | -6.7774 | -46.925499 | 2024-10-10 00:20:33 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ce729ea-9da1-3c9c-ab9f-e207a7c79389 | -5.7552 | -42.518398 | 2024-10-10 00:20:34 | METOP-C | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 49940a5e-e73d-3c95-ae08-9d9157ffb641 | -5.9009 | -43.206699 | 2024-10-10 00:20:34 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 9a276dd3-3943-34e0-bdea-ca55cfd4ea4e | -5.8911 | -43.2089 | 2024-10-10 00:20:34 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 77ab9894-60d3-377e-b5ab-d930c828e857 | -6.7676 | -46.927601 | 2024-10-10 00:20:34 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1501549b-70f3-34a8-a6f6-aa4066881d85 | -6.7701 | -46.9389 | 2024-10-10 00:20:34 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5bc07310-071e-3bdf-811d-a6a0975a118b | -6.1356 | -44.1129 | 2024-10-10 00:20:34 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ba09c9a-aa10-3926-b2d4-b8f990c89c29 | -6.1188 | -44.083801 | 2024-10-10 00:20:34 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2459f8ef-c6f0-39b6-985d-fd895f0bc1e7 | -6.2177 | -44.5723 | 2024-10-10 00:20:34 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0ea8332-dd8e-3cdc-9f6b-820d9369727e | -5.9225 | -43.485001 | 2024-10-10 00:20:35 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11343193-3ebc-3908-b07f-dc72e43fafcb | -5.9241 | -43.492401 | 2024-10-10 00:20:35 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b12cbed-b6cd-3780-9c60-dc581815847b | -5.9258 | -43.499699 | 2024-10-10 00:20:35 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a6b8e47-f17e-3928-ad91-e34d664f31db | -5.9127 | -43.487202 | 2024-10-10 00:20:35 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3bb8527-b332-3c88-a93e-fc630c1f5b2d | -5.9143 | -43.494499 | 2024-10-10 00:20:35 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cacd11e7-cd79-3d0a-b762-de634336bd2c | -5.6491 | -42.3237 | 2024-10-10 00:20:35 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fb54ba5d-a689-3302-b77f-c6fcbcac10d5 | -5.6507 | -42.330601 | 2024-10-10 00:20:35 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7b8b8363-fc4c-3d9d-9ffd-6f5b535f9a7b | -5.6523 | -42.337502 | 2024-10-10 00:20:35 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4b067c10-df17-3897-ba1a-ef1a9e4cb555 | -6.5831 | -46.364201 | 2024-10-10 00:20:35 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28bef35d-d48d-3cf4-a00c-6aa73709a42f | -6.5854 | -46.374599 | 2024-10-10 00:20:35 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac1a9679-9d97-3c74-b7c1-b8c93ad28ff5 | -6.8572 | -47.717098 | 2024-10-10 00:20:35 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 800ca921-970a-3e6f-8cae-69ca3f0c7efe | -6.86 | -47.73 | 2024-10-10 00:20:35 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de14b4cb-235e-3705-94f3-d181a12ccfe8 | -6.1137 | -44.382801 | 2024-10-10 00:20:35 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9c439cc-b299-3beb-aa18-41b983dbd78e | -6.1155 | -44.3908 | 2024-10-10 00:20:35 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88f2b9b2-40ce-30ae-9f85-8b8ca1edd9cf | -6.1173 | -44.3988 | 2024-10-10 00:20:35 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4db93501-9b58-3dc1-b8a2-c7819bf471f7 | -5.1549 | -40.484699 | 2024-10-10 00:20:36 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 10a3b28a-364a-3e7c-8b14-3c394c2b2208 | -5.1566 | -40.491798 | 2024-10-10 00:20:36 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d13839cb-b988-3432-a1e8-45e888cb652d | -5.3213 | -41.251202 | 2024-10-10 00:20:36 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4d6c622a-5501-3e10-9a82-8d27abe361c7 | -5.3229 | -41.258099 | 2024-10-10 00:20:36 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 70a85d58-aa8f-364c-8b75-9f522f08f5a4 | -5.5848 | -42.4034 | 2024-10-10 00:20:36 | METOP-C | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 65f54d8f-c90e-3a1d-9d09-9c6954653461 | -5.5864 | -42.410301 | 2024-10-10 00:20:36 | METOP-C | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 381b0f92-88c8-3812-87ef-7c378c1b8aba | -5.744 | -43.241501 | 2024-10-10 00:20:37 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a118be4b-bbb3-37fd-8fb6-cb01b51c3fc6 | -5.9687 | -44.239799 | 2024-10-10 00:20:37 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d57cf06-bf6e-3f81-b9cd-a3245738b4ad | -6.5924 | -47.1092 | 2024-10-10 00:20:37 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b762bbd4-a56c-3bc8-9257-6296d207ca5b | -6.5949 | -47.1208 | 2024-10-10 00:20:37 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55b23c3e-17e6-3bb5-a39f-8497d69b98e6 | -7.0742 | -49.442799 | 2024-10-10 00:20:37 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 188d8da7-98aa-336e-8fc8-e97bb3a2ca50 | -5.7847 | -43.741402 | 2024-10-10 00:20:38 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d01aa5e0-606c-30f6-bfee-7aef83a16437 | -5.7864 | -43.748901 | 2024-10-10 00:20:38 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1e8c891-5464-3855-9719-99cd81f088db | -5.7749 | -43.7435 | 2024-10-10 00:20:38 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29c96276-c3f4-3e2d-9ba8-9ba2eab5b948 | -5.7766 | -43.750999 | 2024-10-10 00:20:38 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f5e23eb-dcfe-3262-afc8-6309b558b89f | -5.7783 | -43.758499 | 2024-10-10 00:20:38 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c175e2b5-b040-3902-97dd-60b32164069b | -5.6642 | -43.0709 | 2024-10-10 00:20:38 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8b1f41a8-7bcb-3c81-97af-c33cdf99aaac | -5.6918 | -43.1926 | 2024-10-10 00:20:38 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6c146db-2dec-30da-adeb-a05199f5bf89 | -5.6674 | -43.130299 | 2024-10-10 00:20:38 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 049c99e6-6232-3685-83f7-e175cad569f4 | -5.669 | -43.137402 | 2024-10-10 00:20:38 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 6956a97e-4cdc-34e8-b106-26be49f17977 | -5.682 | -43.194801 | 2024-10-10 00:20:38 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 9e824dd5-dfa6-397f-9565-782565e52ef0 | -5.6836 | -43.202 | 2024-10-10 00:20:38 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 228365e4-1f18-3871-92d0-54ffa8a5bb8a | -5.6576 | -43.132401 | 2024-10-10 00:20:38 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| e216c920-2cb6-3bb9-b732-7cedc31d13ac | -5.6592 | -43.1395 | 2024-10-10 00:20:38 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 409b2359-80b6-3578-822e-678587dfbc6c | -5.6461 | -43.127399 | 2024-10-10 00:20:38 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 24458b1a-46ee-31b7-a645-892c7b2f93ac | -5.6478 | -43.134602 | 2024-10-10 00:20:38 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 895b242e-287b-336e-b84b-7367d8f40947 | -5.9978 | -44.646099 | 2024-10-10 00:20:38 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README11.md)
