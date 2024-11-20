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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b25e8bf-ce14-3dbc-8cc7-52d1c5977b63 | -0.9256 | -51.6436 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eab093c-7252-3271-b2d1-3e41f303cdb1 | -0.9233 | -51.722301 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 77c88380-f4ea-308d-87ba-02dd81f8d581 | -1.1253 | -53.668701 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50a8de82-9101-34c9-a2e3-73a7ef76d00b | -2.5245 | -54.5476 | 2024-11-20 01:04:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 903c4e6a-1c8b-3cf6-b66b-73dfc8407758 | -2.4419 | -53.6968 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8eeecfb9-e0e4-37e1-80b9-5a10a31ec27c | -1.2395 | -53.358501 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e973fdad-487f-3d58-8fdb-e17a0a26dc95 | -2.5833 | -54.041698 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c27331ea-f597-37eb-86f0-7587788a0dcc | -1.4391 | -52.6605 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94948033-0c9d-39f6-aaeb-469f82d5261e | -2.1964 | -53.7062 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a429561a-f915-3f12-9d0f-0c9168f3aba1 | -2.6189 | -54.285099 | 2024-11-20 01:04:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 341363dc-3ce1-3c85-a8e3-5c6d8b0cf79e | -1.3056 | -52.3951 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7824981-ae04-3d25-8d84-5e0671b4345b | -0.4688 | -52.0732 | 2024-11-20 01:04:00 | METOP-C | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ba2cbb48-9970-3160-b1cc-0a5accc3af5a | 1.5774 | -55.868198 | 2024-11-20 01:04:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0719c5bb-f9e1-3ce2-ad30-f49ee8593b5c | -1.3173 | -52.401199 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 540c1cc5-0805-3e5c-8bad-2c85dfe43c07 | -2.3318 | -54.7864 | 2024-11-20 01:04:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aef918ec-bbf1-3726-9b1a-b2a4c5d254fc | -1.1881 | -51.976601 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42af99e7-25b9-3b67-84f1-7f630ae8987b | -0.2979 | -51.555801 | 2024-11-20 01:04:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 789f070e-68ce-3d93-8999-316ffee74aa4 | -1.6174 | -52.628799 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d4d5fce-7781-3456-962b-6b0f0de48a13 | 1.5759 | -55.875 | 2024-11-20 01:04:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60257c93-a942-30cb-bbbd-dffec0075579 | -1.6403 | -52.6833 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7d260bb-20df-3ffc-bca6-fa9200a5c798 | -4.1594 | -43.9739 | 2024-11-20 01:10:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 1cd8f22c-5e75-34b8-8091-3e737485acfd | -2.7218 | -49.3295 | 2024-11-20 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 034eabc0-9a29-35d9-8c99-c8f1dc89dfcb | -3.802 | -47.8104 | 2024-11-20 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 027a6ac3-e942-3634-aa98-04c8a0f32a18 | -4.3774 | -47.7627 | 2024-11-20 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 9858ebd9-3054-31fd-a469-9ff8ea6e3b7d | -1.3138 | -52.3973 | 2024-11-20 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 7a53911c-5c43-3de4-b8f3-14bb027cccc9 | -4.4592 | -46.5745 | 2024-11-20 01:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 90.3 |
| d9b08c0e-91a7-36c4-a307-df7bf1d0eaa5 | -2.93 | -53.0601 | 2024-11-20 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 357b2c30-30f5-3752-a1fd-f74610ffa31e | -2.6397 | -51.7992 | 2024-11-20 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| fbe538b3-4111-3973-8a61-5955c1a20b32 | 1.5284 | -55.9045 | 2024-11-20 01:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 500de98e-4033-316e-8775-8a88a49d3984 | -1.2017 | -53.6769 | 2024-11-20 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| af3418a4-b5b7-3ecd-a45b-7a8e1f153f23 | -2.9968 | -45.4584 | 2024-11-20 01:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 441fdcdb-1b3c-3c9c-97e8-f5d76099f1be | -2.9969 | -45.436 | 2024-11-20 01:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 139.7 |
| 66c0f046-82e8-36bb-a1e8-b203a0bd3a07 | -3.2014 | -54.3243 | 2024-11-20 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 56348b0b-8b12-3648-bd92-e217a7aad678 | -2.8124 | -45.1274 | 2024-11-20 01:10:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 8bb60a0c-d03b-32db-b43e-b08b886d380b | -2.831 | -45.1267 | 2024-11-20 01:10:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 133.9 |
| 3dc823e0-2bd7-38a3-bed0-3d0c4f1c295b | -3.011 | -51.0028 | 2024-11-20 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 6c083a01-e29d-3df8-8a66-4b00e3bf9903 | -2.3181 | -48.4858 | 2024-11-20 01:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 7b9ed395-d81c-3a59-b1b2-6890fb2805c2 | -3.0155 | -45.4353 | 2024-11-20 01:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 8b297991-a83a-3cb0-9922-88067e519cdc | -2.6212 | -51.8203 | 2024-11-20 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 32c9237d-5984-36c0-abe3-32b8e8f4a28b | -17.1362 | -57.5041 | 2024-11-20 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 7f5e667d-6f15-3130-8b8d-571184d689a2 | -1.2018 | -53.6568 | 2024-11-20 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f45ed494-e5f3-3acf-afe6-cccd44496568 | -4.4405 | -46.5754 | 2024-11-20 01:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c4a8dbfa-67b3-357d-a67d-8f4e0f27fde9 | -4.4404 | -46.5975 | 2024-11-20 01:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 51.8 |
| bfd1bfbc-e4b2-3b9e-9771-82908d38d604 | -2.9116 | -53.0606 | 2024-11-20 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 32648c71-1940-392f-9d4f-b344cfabcbfc | -4.459 | -46.5966 | 2024-11-20 01:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d2739fb0-c15c-3b6d-990b-763fa765bae7 | -2.6212 | -51.7997 | 2024-11-20 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 76a73ab8-b955-3aa6-a33f-f5b4e498ace2 | -2.7217 | -49.3508 | 2024-11-20 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| a59a247c-21b6-3e42-8a1a-ad5318fdbca4 | -1.3321 | -52.3971 | 2024-11-20 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 5d3a1983-3bd4-3a42-bbd3-d8a7d55342da | -2.2996 | -48.4863 | 2024-11-20 01:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 25c56326-f8c4-38f4-83f8-947d30ee7ae7 | -3.0109 | -51.0236 | 2024-11-20 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e5828708-ce5e-3705-8d20-db0a7add66df | -2.8309 | -45.1493 | 2024-11-20 01:10:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| b74ba642-4f5d-372c-b247-cf87903e73a1 | -4.3959 | -47.7618 | 2024-11-20 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 1abb7776-5033-319d-a2da-125db8d61611 | -4.5614 | -48.0141 | 2024-11-20 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| f07bb2b6-6203-3328-8b21-376371113b21 | -24.01138 | -54.22329 | 2024-11-20 01:19:00 | TERRA_M-M | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| fb9a3ee6-bf66-397b-96cf-430f6defe74f | -23.28088 | -51.40532 | 2024-11-20 01:19:00 | TERRA_M-M | ROLÂNDIA | PARANÁ | Brasil | 4122404 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 363f245c-799b-3cb4-9582-aafe587b54c2 | -21.22549 | -56.34898 | 2024-11-20 01:19:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f590db25-a595-33eb-b3ef-2136b00d0ff0 | -22.30388 | -49.77184 | 2024-11-20 01:19:00 | TERRA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 75757cab-07eb-31d0-bec5-8b632a119482 | -23.28229 | -51.41502 | 2024-11-20 01:19:00 | TERRA_M-M | ROLÂNDIA | PARANÁ | Brasil | 4122404 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| 9ff61036-0c4b-3667-893a-361f8eee8a74 | -3.1477 | -49.1251 | 2024-11-20 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| f0cfd8ae-9e2d-3a60-94a8-466cd09d7269 | -4.5614 | -48.0141 | 2024-11-20 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 3d36e9ab-5093-351f-b480-cf5fae809ff6 | -2.6212 | -51.7997 | 2024-11-20 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| c2e2687d-c53a-369a-abc3-78cb30488900 | -2.6397 | -51.7992 | 2024-11-20 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 709f6225-126c-33e8-9cee-f2af9b41044c | -2.9116 | -53.0606 | 2024-11-20 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| be91bacf-4e5e-3e27-8ce7-427c703132f7 | -2.2996 | -48.4863 | 2024-11-20 01:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c65d92bd-829d-3723-a447-df7305a28cc3 | -2.2725 | -45.4593 | 2024-11-20 01:20:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f6a722ee-ec23-3577-87c8-3c6ae45e40d4 | -2.7218 | -49.3295 | 2024-11-20 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 70db4298-e6dd-3446-bc04-d407b3170358 | -3.0109 | -51.0236 | 2024-11-20 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 66209073-a541-36e4-aa8f-851e7bb4ad6a | -3.011 | -51.0028 | 2024-11-20 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| cf884944-b053-3679-b9e7-62590dec763d | -3.802 | -47.8104 | 2024-11-20 01:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 2b66acb7-ec46-3598-aed4-d21c8f5fdcdf | -4.3774 | -47.7627 | 2024-11-20 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| fae2cc55-4655-3c97-8d83-3b5d8614ec32 | -2.7217 | -49.3508 | 2024-11-20 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 262d853a-9ccc-3ada-855d-a3c346a69551 | -2.9968 | -45.4584 | 2024-11-20 01:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| aa9d365b-4810-3c37-83c2-8d82c8be1bfc | -3.1292 | -49.1257 | 2024-11-20 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 50bb6d10-0d7f-3b68-a5e4-786b84cc0c59 | -3.8205 | -47.8096 | 2024-11-20 01:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| c6c27f3a-f256-3b91-8c07-84a092db7955 | -2.9969 | -45.436 | 2024-11-20 01:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 1342aa64-0d6c-3eb9-bd3c-e54650842653 | -4.3959 | -47.7618 | 2024-11-20 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| bb0f8242-8c63-3cf6-b9c2-ac6317fe1c01 | -3.2014 | -54.3243 | 2024-11-20 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 5fd80c0f-66d9-33f0-b297-aaa0e6866cc4 | -1.2017 | -53.6769 | 2024-11-20 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| ba629278-7fee-3c31-9ed9-7ca1c33da5e8 | -2.831 | -45.1267 | 2024-11-20 01:20:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 64f52a84-f067-35a5-9a49-fc8b583acc7e | -3.8206 | -47.7879 | 2024-11-20 01:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 6546d16a-106a-3484-add9-18ef7b3d6790 | -3.8021 | -47.7887 | 2024-11-20 01:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| a34aa6ad-5b41-374d-b465-f6b9d773d63d | -3.0155 | -45.4353 | 2024-11-20 01:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 6d3721bb-8725-39b7-b962-4d138ad14222 | -20.21122 | -56.63142 | 2024-11-20 01:21:00 | TERRA_M-M | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 3f7ba23e-c1f7-398e-9c8f-45aa5baae6ac | -17.13338 | -57.50114 | 2024-11-20 01:21:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 047b1f06-0620-3aa5-b61b-83ddbb8d67e9 | -17.12305 | -57.50251 | 2024-11-20 01:21:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| ab613161-4ecf-3582-bd54-c238328f0ae7 | -3.04367 | -49.46024 | 2024-11-20 01:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| f509f860-2ac3-3cb3-80d2-34d8a8a449fc | -2.63259 | -54.27497 | 2024-11-20 01:24:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e0ff6b42-f9be-39b4-82b8-787297920461 | -3.28736 | -53.83767 | 2024-11-20 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3a07b0d3-be2b-3dec-a50d-9b4b97d2ff23 | -3.00662 | -51.00743 | 2024-11-20 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| fd972680-df3b-3fe9-bd00-38fbfa253b3e | -1.93722 | -52.9895 | 2024-11-20 01:24:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 66254dfa-4464-3511-81c9-7a3120d49076 | -3.06628 | -53.29023 | 2024-11-20 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e58db905-6b5e-3cdb-8d13-3050f7b8d71b | -2.22588 | -46.50427 | 2024-11-20 01:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| cdf53211-9c73-3790-b9c2-ca7493a1b577 | -3.31142 | -54.07486 | 2024-11-20 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a021c423-7017-38ff-b324-447dfbce313f | -3.2858 | -53.82674 | 2024-11-20 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 7982d34f-316b-360e-affb-3bf0c9e84b88 | -11.09345 | -54.63663 | 2024-11-20 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 70d864df-9de1-3bab-8f0d-fd21508f9132 | -3.01033 | -51.00115 | 2024-11-20 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 8ffede16-329c-3d36-8287-5968e83cbf10 | -3.20182 | -54.32554 | 2024-11-20 01:24:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 4d95a750-38b7-3015-978f-46d22f33682a | -3.04912 | -54.4118 | 2024-11-20 01:24:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 47f70260-4ab8-3486-afc8-4fc366a5a690 | -3.11102 | -53.75198 | 2024-11-20 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b465d5d3-3be3-3434-814a-f328e5f73c9b | -1.88767 | -50.96949 | 2024-11-20 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |


[Clique aqui para ver as próximas entradas](README14.md)
