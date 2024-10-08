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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d6960f7-9efd-37eb-9073-8099e650f3f2 | -21.6336 | -47.71616 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9a80f10-3cce-3005-be56-a89c02ab8398 | -21.60303 | -47.71812 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9cd44ad-e78e-3dfb-b32b-5252a46f8881 | -21.6016 | -47.71802 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b035ea95-eab6-3bc1-a74c-7080f729d883 | -21.60095 | -47.72103 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb7b52f4-7822-319e-b7f0-35ae2e223741 | -21.59818 | -47.71616 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc186dec-2231-3456-ab8b-e6cdf879b0ba | -21.59755 | -47.71914 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e455cc34-e6ad-3f32-ac1e-8f8ff1df4d2e | -21.59691 | -47.7222 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b6c2239-febc-3a92-ba1c-90a7ec5a9e1e | -21.59553 | -47.72877 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6eb6bc85-63ae-3f45-9f40-d45205d06e53 | -21.59427 | -47.97247 | 2024-10-08 03:45:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25bf7660-4f48-3c50-8a5c-90957ff2c642 | -21.59329 | -47.71435 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 678b0049-cf2e-3694-9eef-b5254ce49a32 | -21.59267 | -47.71733 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c70e7d1-c8e7-39da-b45f-1ad41d0c9ae1 | -21.59203 | -47.72034 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24f950bd-a70c-3803-8f76-af38fc416de3 | -21.59133 | -47.7237 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2974870-cbdc-3c4b-bb53-65a2be5137c2 | -21.59059 | -47.72721 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c47933e2-2997-381d-89a8-d7cd7fc816a4 | -21.59058 | -47.96478 | 2024-10-08 03:45:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6335fb03-cca8-38a7-bdf0-d8c2eb140bd1 | -21.58917 | -47.73395 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52506c70-ba26-3977-87ce-dca16f05f6df | -21.58776 | -47.71564 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f662540-32e9-3e2e-ad00-e8447972e76d | -21.58351 | -47.73581 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1f8ef68-32b2-38d3-bbb7-b954a2827d22 | -21.58167 | -47.9319 | 2024-10-08 03:45:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ea5f39e-d6ce-37d4-abd5-0286a30ce26d | -21.5787 | -47.92096 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 143ef7c0-b915-39d4-82d2-df3bcc2403d7 | -21.578 | -47.92418 | 2024-10-08 03:45:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1b9abb0c-c5ab-3ba2-989f-af2884a5b8a2 | -21.5773 | -47.9274 | 2024-10-08 03:45:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 37ba19de-a7a5-3173-b805-ccddcbf09f25 | -21.5766 | -47.93063 | 2024-10-08 03:45:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ac00976-1d79-3044-98c8-5e8edb9b6565 | -21.57294 | -47.92289 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46ee6af4-23d5-339f-b897-6df40323ada1 | -21.56782 | -47.73521 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 855bdcc4-4c30-3452-8c75-ca28548f0702 | -21.56649 | -47.92798 | 2024-10-08 03:45:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 879aa75b-c6b5-3cba-81cc-0f850876f75a | -21.56354 | -47.73056 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5bff4874-ead8-345e-8f0b-f2a2801e9cd7 | -17.50736 | -49.07513 | 2024-10-08 03:45:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 182b9332-7f2f-3846-875d-c3fb213c1fdd | -17.51317 | -49.07688 | 2024-10-08 03:45:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86842dbb-dd2c-379c-a417-dab392799d56 | -17.51085 | -49.07504 | 2024-10-08 03:45:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 363e1436-7cc8-3a34-a16b-dc17b11fafc7 | -17.50985 | -49.07957 | 2024-10-08 03:45:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a7f82e5-9ae0-37c4-bd82-013a21225613 | -18.16667 | -48.52593 | 2024-10-08 03:45:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 51ffc95c-6bfd-3f6e-842c-2a69a9ded8bf | -18.18922 | -48.14478 | 2024-10-08 03:45:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc4434bf-708b-3283-a6e9-d31d50e0925b | -18.1682 | -48.52904 | 2024-10-08 03:45:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e4679c8-1319-3669-847e-9c9998d6e084 | -18.16574 | -48.53035 | 2024-10-08 03:45:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 35a2e107-b530-346a-80aa-98bbdb0a3ceb | -19.14701 | -48.29863 | 2024-10-08 03:45:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb7acc76-9849-3898-8765-248330b09693 | -18.18379 | -48.1432 | 2024-10-08 03:45:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31e5e722-a91f-39f0-85e0-10e3c552c1d1 | -18.16249 | -48.5281 | 2024-10-08 03:45:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d051af9-febc-3908-9943-479d289d0d8f | -18.16344 | -48.52375 | 2024-10-08 03:45:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ccf94129-3a30-30ca-91a1-3d2687437d86 | -18.53792 | -48.41198 | 2024-10-08 03:45:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 75fbbaad-605a-3633-8993-8f370246b5d9 | -18.54346 | -48.41328 | 2024-10-08 03:45:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f8d59f88-137a-3079-bc3a-f5428496b297 | -19.55137 | -49.49353 | 2024-10-08 03:45:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f04788b1-59e4-3984-97cc-98f8f0371315 | -20.3721 | -48.91111 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25be2eb3-7ba1-3f21-b064-0b17b0a41b76 | -20.37094 | -48.89033 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 034b0182-cd5b-3a40-9b3d-89fb5abae16c | -20.36872 | -48.90614 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 516ece74-49b6-3489-877a-362e66216047 | -20.3666 | -48.88913 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dc1bf9b5-a376-3e37-b369-0398681fdc0a | -20.36577 | -48.89294 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7f5a903d-aa1e-3cce-ab12-b239b162282c | -20.36272 | -48.88026 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c56e6cf6-ad76-3e65-8b10-c60b0bb7561f | -20.35908 | -48.89137 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 89354e3f-ef6e-3b51-81cb-45f077bd8292 | -20.35646 | -48.90303 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0de8901a-ffff-3bde-a013-b231f4378ff2 | -20.35604 | -48.91104 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0be901a0-f8af-3e9b-ba64-16219acafe7d | -20.35559 | -48.90692 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89013121-7e65-3b1f-b44d-f609e2160ea8 | -20.35476 | -48.89017 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f530459f-f4eb-3f6d-b8d1-dbcd92a3b3ff | -20.35088 | -48.88135 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e83f2e75-1f62-31a8-9a5b-cefe8a667a0d | -20.01758 | -48.9121 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8c8d0edc-525a-3d79-aff3-d3730e528fa2 | -20.37292 | -48.88669 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 55a64740-533f-3fe4-beb6-9b019863d243 | -20.3721 | -48.89052 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ba95163-3b69-3887-b6a5-40245efdfc05 | -20.37042 | -48.89829 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc0049c0-09e0-3435-9c8a-36a312fe1a02 | -20.37008 | -48.89417 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a222d7e-83f0-3b51-8676-821c7e82a5f5 | -20.36788 | -48.91 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ecbb1fc-a015-3816-8835-152fb0c12089 | -20.36659 | -48.90975 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2de3f9ea-8117-3ca0-90af-ca3a115256dd | -20.36485 | -48.91751 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56d7b8ee-a36e-3223-9bd3-03f9a940a380 | -20.36408 | -48.90075 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f860504d-2c6d-37b6-9de3-15cf427f4ad9 | -20.36372 | -48.8966 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c6c6c036-5338-3c41-a6be-9c7443d3aa79 | -20.36284 | -48.90051 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 976b8899-6b1f-3941-9c07-697e471df102 | -20.36152 | -48.91253 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f89dd931-01aa-3e9f-8e4a-6ac61a1ebfba | -20.36109 | -48.90835 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c27e6c66-08cc-35cd-a44f-48b1fd04120f | -20.36077 | -48.88385 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 786416b6-5c7d-35d7-a43b-3a4ac4613acb | -20.36021 | -48.91225 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d1c03a1-8467-33f4-8408-9a04d9e0f370 | -20.35993 | -48.88758 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f8d2e824-deb6-3c40-8db6-097177f628e6 | -20.35822 | -48.8952 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f98fbdd-e70c-3815-901c-80c44e09ebd0 | -20.35472 | -48.91078 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f581ae1d-3675-34e7-ab34-396d8678de2d | -20.35007 | -48.88508 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e0e684e-8ccc-3605-8bc3-3ef38bbb1e18 | -20.37247 | -48.80864 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 393140a8-fb57-31a0-a6b6-87c6665c4af2 | -20.37211 | -48.83329 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 2c242e01-8b4c-3e55-9dd9-405339891eff | -20.37207 | -48.83712 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 743cdaa2-8e55-3121-b113-dfd77f5e88da | -20.36998 | -48.82011 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6aa4d2de-5d00-3e75-8b99-ddf25c26f90a | -20.36913 | -48.82405 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| da6bca0e-c5ab-31cd-aab7-75a306746b7a | -20.36199 | -48.83028 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 552204c5-f439-3463-bef2-1563fcbcd7da | -20.3553 | -48.80794 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2261cc2-f6ac-3471-af6e-887ead6b46ba | -20.35487 | -48.83644 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 174.5 |
| f1485e75-5f91-311c-8a86-0dd8d16cf073 | -20.35193 | -48.82338 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de1115b0-83aa-3f5a-b627-b272fb04ca7a | -20.34938 | -48.83508 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f776437-6fbc-3f7d-8afe-4f0aaab63c26 | -20.3905 | -48.80533 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c81d4737-858a-378e-8902-740c2d4f2f9d | -20.39024 | -48.82986 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 24.7 |
| aba6d18d-f4e2-3363-af19-b7d60cace6c3 | -20.39014 | -48.83379 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 1cd8179c-d12e-3e76-b272-a73d918279c3 | -20.38991 | -48.8054 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00514521-c17a-38e2-89cd-0ce4093cb56e | -20.38965 | -48.80928 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2fdac0e-5aca-302a-a230-33d21c0742de | -20.38937 | -48.83376 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 1e285834-9a39-3c72-aa1c-48d50234b126 | -20.38929 | -48.83772 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 1cdb7bc9-349c-3fe1-9f80-93de530a60b8 | -20.38904 | -48.80933 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97c543fe-829a-3b7b-97d9-8c97b7c7e04e | -20.38881 | -48.81319 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 558328f2-86b3-3271-a7d9-13570aed7b84 | -20.3885 | -48.83766 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 9bef4d3d-fbc2-3a56-9da6-42ec680dbaed | -20.38844 | -48.84167 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 158.2 |
| ae832fae-7dd7-33c2-9e0a-fc6bbdef9f42 | -20.38817 | -48.81321 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d10d13aa-6839-345f-a2a8-0aa6d1b5c2eb | -20.38797 | -48.81705 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 532ae16e-7c79-3961-b14e-36161ef9c82c | -20.38762 | -48.84159 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 98976f38-cd3b-30f1-b709-603003121587 | -20.38731 | -48.81706 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b402330c-109a-3465-938f-71e5d0196df0 | -20.38714 | -48.82091 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2644d643-aad4-32cf-9f60-05d6cd609dfd | -20.38646 | -48.82088 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 21.9 |


[Clique aqui para ver as próximas entradas](README44.md)
