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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80a6e48b-82ec-33e4-8a92-4b38b131b9c0 | -17.00834 | -55.03012 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82700290-c489-360e-b9a1-7f1e92123475 | -17.00504 | -55.02956 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15e55ca2-4793-3b9e-aa48-2007e2813451 | -17.00174 | -55.029 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 414c5be9-896c-35b5-9f01-9fda9e348ac4 | -17.00117 | -55.03259 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0408c5df-3dc0-3e4d-9cfe-fb659f28c364 | -16.90458 | -54.56007 | 2024-10-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b963baa9-f69d-330e-af35-9efa1d4abb38 | -16.90295 | -54.54869 | 2024-10-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16de67d3-2c06-3a69-b689-289ba329537d | -16.90239 | -54.5523 | 2024-10-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88127157-52b2-3b99-868d-c53db212f3e6 | -16.90183 | -54.55591 | 2024-10-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7723d79-ce0b-3b38-80ea-3e9b6e0dfbd8 | -16.90075 | -54.54092 | 2024-10-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e4144ccf-d5f8-3ccd-992a-59fbb6eb84f8 | -16.88643 | -54.52377 | 2024-10-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18a4fd4a-b539-3aec-8113-f5e9e1794bc0 | -16.88587 | -54.52736 | 2024-10-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d7c2fdd-7edd-3a08-a11c-0d4a684cbffe | -16.80421 | -54.10579 | 2024-10-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 607a1937-afe1-3046-bad6-c927c0a44646 | -16.80366 | -54.10943 | 2024-10-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 512c35ca-33d8-3773-af1f-f354533af7be | -16.80033 | -54.10888 | 2024-10-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 69000aa6-2936-357a-908e-d8b14c34bfad | -16.79978 | -54.11252 | 2024-10-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 6c3aa2fa-b345-302c-9655-830eb7a442d3 | -18.10347 | -54.27505 | 2024-10-07 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 972fc1e6-0093-3fca-a0e6-f4c68b31198d | -18.10292 | -54.27876 | 2024-10-07 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f011e02-b3f1-39b0-b01e-48b571a8848c | -18.10014 | -54.27451 | 2024-10-07 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 843225bb-23c3-3c64-85c3-8d4eec4d562f | -18.09958 | -54.27821 | 2024-10-07 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7de3a1be-8bda-32de-86ae-79c48ede0d14 | -18.07734 | -54.31231 | 2024-10-07 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04504e6d-2d99-3804-bf3d-930fb06535d3 | -18.07679 | -54.31596 | 2024-10-07 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 065a48d2-e843-36df-be54-eab97039288c | -18.07345 | -54.31543 | 2024-10-07 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f7eba18-7e86-34a5-8ced-170eca1851c8 | -18.0729 | -54.31907 | 2024-10-07 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff7847c9-bd98-3e47-a5f4-8d0ca8f856b0 | -17.83924 | -53.7947 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a8953622-76ed-3344-9fd5-140733cf3e15 | -17.83869 | -53.79842 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 295e5b39-4195-3d79-9221-1f5ef78da0f7 | -17.83813 | -53.80217 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1b4616d4-0cab-3e34-b916-4108ffe019a1 | -17.83587 | -53.7942 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1e15203b-f706-3224-a681-77f73ac81f8f | -17.83532 | -53.79787 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c7f5c2d7-93fe-341e-9927-1a57a3f45400 | -17.83249 | -53.79369 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cd8ee809-444a-3b53-93c1-55c0ccf47c7c | -17.83195 | -53.79734 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d58e3776-7caa-3a52-b400-e795f5714547 | -17.82912 | -53.79317 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 05262bde-be5c-3d1f-918e-3340b86a41dd | -17.82576 | -53.79264 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ad58d215-aa85-315a-96ae-7f9d89f1a64a | -17.80087 | -53.78558 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5eb2cd24-aacb-30f8-814c-938e0d325223 | -17.79976 | -53.79301 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d740168f-045e-3c0f-b79e-f73086900e2a | -17.79919 | -53.79674 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ec083e0-3f4e-3693-a83c-379702a3699b | -17.79864 | -53.80047 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b756fd8-7d52-3b10-9f91-8facb8240c89 | -17.79807 | -53.8042 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe0bf037-dbe2-3b5a-adc7-95b32e358472 | -17.79751 | -53.80792 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46485061-6818-3210-aefd-0e8bb7c7f986 | -17.7975 | -53.78504 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 66e0abc4-a89f-3176-bcd7-e0acc35135de | -17.77392 | -53.78129 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8d2bef52-db17-3b39-a157-37129cb1b87a | -17.79471 | -53.80365 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e9f1a998-8572-3ab9-8bb3-8cf5ddd5c70a | -17.79415 | -53.80737 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bd9b489b-c021-3f32-a750-812062c5f060 | -17.79413 | -53.78455 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e1ebaa3c-8153-336a-afb6-ca61653687b7 | -17.79359 | -53.8111 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d825c97f-0946-3348-8e15-bafb32f06714 | -17.79357 | -53.78827 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c1379027-5e48-34d6-9afe-5c6e2f176bfc | -17.79303 | -53.81484 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| aa52e152-b175-3fa8-baf3-f65caf47eb1b | -17.79301 | -53.792 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9053a57f-8a36-3aaa-952d-b78f29a7c118 | -17.79245 | -53.79572 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 3b0301fa-104a-3658-a71a-44405115b0d7 | -17.79189 | -53.79942 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 66c6aa49-bdbc-3e89-a3e1-eb8ea2e2c124 | -17.79134 | -53.80311 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f1b29de7-e3eb-33a3-986c-89e8fc97f607 | -17.79078 | -53.80683 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bea9cf3a-e475-3745-a2d5-080604f52bb6 | -17.79074 | -53.78413 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6453d273-0d68-313e-b4d3-7f3f79f6ffb1 | -17.79022 | -53.81055 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6dae1f3d-5f55-3213-97ad-206a16083451 | -17.78966 | -53.81429 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ab1fb091-d072-3303-9c66-36fbe50b694a | -17.78963 | -53.79156 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 35dacbfb-d1e1-30d5-9fb8-64d1f9d321ee | -17.7891 | -53.81802 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37aae978-a22e-3840-82a5-efca2cb21ba0 | -17.78907 | -53.79524 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c5bb804-2b15-36fa-b3ab-2f45ed09969f | -17.78852 | -53.79892 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d469ebc3-4d2f-32bf-ad8e-1ec8b366835a | -17.78797 | -53.80259 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| afc71d17-9961-3e9a-8f6e-f3fe6a28f510 | -17.78741 | -53.80629 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9a466bc7-fb11-32b3-a24b-eeafd1414045 | -17.78686 | -53.81002 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bf1f2dc4-d719-3664-b0d4-fcc657d93fe4 | -17.78629 | -53.81375 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| eedd1d53-ee40-37e3-b74e-92001ed32bbb | -17.78574 | -53.81748 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ba06dd6c-f50d-3bff-b8cf-fabcfa5b245f | -17.7857 | -53.79473 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7b8d169f-8851-38ed-a170-a32b19b97241 | -17.78515 | -53.7984 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eb69e50c-0b9f-3a05-b2cc-13871789732c | -17.7846 | -53.80207 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| beef225e-ea9a-3e03-a56f-69ae9349bd02 | -17.78405 | -53.80577 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b7131cd2-ff95-3eb3-967e-d71f4a260f11 | -17.78349 | -53.80949 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e76c8440-3c31-3c93-9699-f78f203fbf1e | -17.78293 | -53.81321 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0b2397f0-32e3-3ded-b64c-0629026c3709 | -17.78237 | -53.81694 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ed92cca0-e736-3047-bdc7-47c6b1fdb59a | -17.78234 | -53.79418 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f09ff912-5e91-3085-ac73-7215645dd9e9 | -17.78181 | -53.82067 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 505c6dd3-0850-3201-8991-c93b5e79c3d7 | -17.78178 | -53.79786 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eb0115a9-53fa-3b13-bbea-b8b05a3118a1 | -17.78123 | -53.80156 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 40dd4217-c4a4-3d9c-b06d-41a7de126067 | -17.78068 | -53.80526 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 90de673a-76e1-38d4-b91c-dd67a725f3c9 | -17.78012 | -53.80896 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d090c986-963b-3e49-97b5-4d37140568fd | -17.78008 | -53.78623 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4404c67-dae0-356c-b277-5bd6f75b280b | -17.77956 | -53.81266 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f6649048-edd1-3727-a47b-be71e96b608f | -17.779 | -53.81639 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6419440-d705-3cbb-93da-cbfaa8cb4f88 | -17.77897 | -53.79362 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b4efc4f-0aac-3711-b792-64cade0aef9c | -17.77844 | -53.82013 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e7b5b0a-71f9-306b-ba27-cbe93e0df18e | -17.77842 | -53.79732 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b311a044-4fe0-3187-a097-763c379857d0 | -17.77786 | -53.80102 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4fd75aa9-d2df-3b23-ba22-6ea320f564a6 | -17.77731 | -53.80472 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b2cd4c97-9769-326f-8dc9-8503b2c43f35 | -17.77672 | -53.78562 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 56fc4680-757a-3bbf-ba47-1a42d2513b90 | -17.77617 | -53.78934 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bd08a29c-228e-3a20-b947-e2da1ba3b5fb | -17.77505 | -53.79676 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 88266a1b-6530-3b90-914a-7063c0888c75 | -17.77337 | -53.78502 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 08a5b600-679e-3759-8650-621b24af46cc | -17.77281 | -53.78875 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8c466f76-8de8-3d68-b286-37f7218505e1 | -17.18142 | -53.92637 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c0f5ebc4-a6b9-3b00-b478-9fa058c5892f | -17.17807 | -53.92581 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b6093c0-177f-3d8e-b2e6-2703eea26899 | -17.17529 | -53.92156 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a0714b3-7237-3dc6-8fac-fea9ea567a2d | -17.17139 | -53.92468 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7925616-06a7-3770-b4ed-5f17725cfe38 | -17.16973 | -53.93571 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33e034b5-f3fb-3ff1-8928-60def3891af4 | -17.16639 | -53.93515 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36c889d1-65d4-3c4f-88a7-b78ce725074d | -17.16583 | -53.93883 | 2024-10-07 04:55:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 12d970e1-5414-3b55-9171-64cb0d1a5752 | -17.15636 | -53.93348 | 2024-10-07 04:55:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4758e5cd-62a3-36e2-96bd-a80f41c34ca1 | -16.90131 | -54.53731 | 2024-10-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a223c8e7-dc4f-33c2-b50f-62376fe447fa | -16.9002 | -54.54453 | 2024-10-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf187302-e1af-3181-9269-eaa1d56395fc | -16.89964 | -54.54813 | 2024-10-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README95.md)
