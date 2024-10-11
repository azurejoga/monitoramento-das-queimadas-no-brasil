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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c655bbf1-6962-3ce7-9977-bdd7e9070166 | -3.9103 | -48.3466 | 2024-10-11 00:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| e343733c-9ed0-32a3-b883-4e3ba64d8075 | -9.7481 | -53.135502 | 2024-10-11 00:45:28 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69d62a63-77cd-3610-a8ea-48840198bf57 | -9.7498 | -53.143501 | 2024-10-11 00:45:28 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45a83a8e-2896-3073-b238-7b5cf6aa69ab | -8.773 | -48.844002 | 2024-10-11 00:45:28 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a68db48c-1bbe-31a1-8f26-ab5e2d7305e0 | -8.7747 | -48.851299 | 2024-10-11 00:45:28 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a17feee9-400c-382a-9361-de96c5d4d09d | -8.7764 | -48.858601 | 2024-10-11 00:45:28 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31b1684c-dfe8-3276-bca2-3757a90ea646 | -4.0962 | -48.2523 | 2024-10-11 00:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 152.9 |
| dfa84690-3e9b-30ae-8edd-5d6beb65e420 | -4.0963 | -48.2307 | 2024-10-11 00:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1352e9e8-abcd-3a3d-bee3-6cfe6c0e22b5 | -9.6674 | -53.094501 | 2024-10-11 00:45:29 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c923af44-6549-3a29-b3f7-03ea01e84f50 | -9.6691 | -53.102501 | 2024-10-11 00:45:29 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb41b527-c28d-37b7-b9f5-0eeeec2ff974 | -9.6593 | -53.104599 | 2024-10-11 00:45:29 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7de3215-94c6-3d9b-9754-cdf53e6fd70b | -8.7132 | -48.988201 | 2024-10-11 00:45:29 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93492ee4-099d-3847-8120-b9e07a32d55f | -9.6385 | -53.150902 | 2024-10-11 00:45:29 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa113a40-765e-354e-801e-dcf0315f055d | -4.1146 | -48.2731 | 2024-10-11 00:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 89afde42-3a37-34df-ad84-670bce0de79c | -4.1148 | -48.2515 | 2024-10-11 00:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 272.5 |
| eaec299a-4dc1-3a13-b193-3518a5704bbb | -4.1149 | -48.2299 | 2024-10-11 00:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 9e87e9c7-9124-3c28-a70e-02f0429ecb0e | -4.1333 | -48.2507 | 2024-10-11 00:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 7ecee336-ddd7-3200-9c49-1300155978c7 | -9.1991 | -51.515499 | 2024-10-11 00:45:31 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1711cf3-4a3f-3393-a0ca-238b41596bc7 | -9.1815 | -51.482399 | 2024-10-11 00:45:31 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6a14ed6-1639-3d0f-a3f8-5e821f235fe2 | -9.183 | -51.489399 | 2024-10-11 00:45:31 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f06247b6-5d53-391c-b5df-6f2110eeda6b | -8.7897 | -49.777802 | 2024-10-11 00:45:31 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b9d7609-3645-30a6-9135-5b26f9dcd389 | -8.7913 | -49.784801 | 2024-10-11 00:45:31 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8a8b6ef-8ea1-3201-a740-1d961c07e643 | -8.7928 | -49.791801 | 2024-10-11 00:45:31 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a88bffd4-0492-34ef-9061-f48f1035ff11 | -8.5855 | -48.925598 | 2024-10-11 00:45:31 | METOP-B | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e00836f-c417-39f6-bad6-706b7b05cb45 | -8.5871 | -48.932899 | 2024-10-11 00:45:31 | METOP-B | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| efd8f18a-5c35-37f8-901f-71c61b96a5fa | -8.7815 | -49.786999 | 2024-10-11 00:45:31 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94f505ca-a541-3cd0-9a86-c068db349668 | -8.833 | -50.060501 | 2024-10-11 00:45:31 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29042594-b60a-3bd0-a7ce-3284428e4c60 | -9.107 | -51.285599 | 2024-10-11 00:45:31 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aedccb4a-6a0f-378f-bdc5-e53feca67363 | -9.1086 | -51.2925 | 2024-10-11 00:45:31 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99d660bc-10b5-3555-98b2-21025b6405e0 | -9.0972 | -51.2878 | 2024-10-11 00:45:32 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0419bc0-150b-39d2-a955-fd5206b12650 | -8.4314 | -48.6586 | 2024-10-11 00:45:33 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 797d00fa-7330-30ee-9b55-9ade24b447d7 | -8.8998 | -50.771 | 2024-10-11 00:45:33 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c659dbc9-88e1-39d7-aec9-a73ea19c2ac7 | -9.4211 | -53.1898 | 2024-10-11 00:45:33 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac525047-67bb-3f6d-974e-d581d4598aac | -9.4229 | -53.1978 | 2024-10-11 00:45:33 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fb8709e-cf80-389f-a0c1-fe8d5befd177 | -8.7001 | -49.9739 | 2024-10-11 00:45:33 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 397d76b3-a9ef-3c5e-87c4-644a92afb3ab | -8.7017 | -49.9809 | 2024-10-11 00:45:33 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c43c622-297f-3769-be30-92516ecfbf7b | -8.7032 | -49.987801 | 2024-10-11 00:45:33 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1e41ccc-19d5-37c5-8f18-daee1e641f90 | -8.7048 | -49.994801 | 2024-10-11 00:45:33 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80e83483-4f80-36fd-a87c-8dfccf9c52ae | -9.4131 | -53.199902 | 2024-10-11 00:45:33 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63fa25bd-7e63-3d73-82ca-5371c0da23cc | -9.4148 | -53.207901 | 2024-10-11 00:45:33 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04cf9095-a545-3d44-8a41-3648d8c844e9 | -8.3854 | -48.637699 | 2024-10-11 00:45:33 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9e30f381-7b31-3c5b-af8f-273895ddf4fc | -8.6934 | -49.990002 | 2024-10-11 00:45:33 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4464cb5f-f42d-3994-82e7-13b3f619d98d | -8.695 | -49.997002 | 2024-10-11 00:45:33 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b526aaf-63cb-3398-94a3-b219a6a0cf97 | -8.631 | -50.033401 | 2024-10-11 00:45:35 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8f26cb0-6565-365f-b757-1706d68eba7a | -8.6326 | -50.040298 | 2024-10-11 00:45:35 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 165b519e-0e53-3059-af87-72ac62fe24c2 | -8.7734 | -50.712399 | 2024-10-11 00:45:35 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bac36977-6372-3ff4-a31a-230535fd1aed | -9.0379 | -52.090698 | 2024-10-11 00:45:35 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50dcfbe8-f796-3205-839e-f2ef1fe56420 | -5.1725 | -48.2848 | 2024-10-11 00:45:36 | GOES-16 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 37dbf5ba-1192-3f1f-aeef-eb3cf5d2844f | -8.7336 | -50.764801 | 2024-10-11 00:45:36 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b11fb70d-effe-3ebd-807b-994ffc083fa1 | -9.0265 | -52.085499 | 2024-10-11 00:45:36 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af06f133-b436-3748-a88a-050de79cdbad | -9.0036 | -52.0755 | 2024-10-11 00:45:36 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ebd8ad6-6cf7-327f-93b9-b34fa1869808 | -5.3265 | -60.1239 | 2024-10-11 00:45:37 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 145b2dc2-9adf-3ddd-a99d-00bfc644fa01 | -8.5815 | -50.408001 | 2024-10-11 00:45:37 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e11f4f9-36ae-3706-80bf-9c9816874de6 | -8.9398 | -52.112301 | 2024-10-11 00:45:37 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e76ccfa1-455b-32ea-84bd-999f2dfaae89 | -8.5655 | -50.520302 | 2024-10-11 00:45:37 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42e76539-44a4-3a66-ab8d-b4e52dccff31 | -8.5671 | -50.527199 | 2024-10-11 00:45:37 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 565ffeb2-a4cb-3b1c-9a8b-ca0598f933c0 | -8.4823 | -50.241699 | 2024-10-11 00:45:38 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9e7271c-63d4-3199-894b-53c6191ee9d4 | -9.0394 | -52.943699 | 2024-10-11 00:45:38 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ebaf63a-0f81-37b5-9e68-6fd68cbd1ccb | -9.0845 | -53.246101 | 2024-10-11 00:45:39 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c0ce3cd-32ac-3914-8a5a-97ba2d7c89e3 | -7.3882 | -45.826401 | 2024-10-11 00:45:39 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5036bcbc-a250-3cca-b0dd-3bb64cba36d2 | -7.2664 | -45.357101 | 2024-10-11 00:45:39 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c35475c3-5ad9-3474-abf9-097ef3219334 | -7.2691 | -45.3685 | 2024-10-11 00:45:39 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05994b23-5c5d-32aa-92d4-6c169f6cbf88 | -8.3299 | -49.977501 | 2024-10-11 00:45:39 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de292899-0612-3ade-8833-560c95d0b9b0 | -6.6873 | -43.168499 | 2024-10-11 00:45:40 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| ceec238c-afb2-3128-9745-3f4cca1b0a91 | -6.6912 | -43.1847 | 2024-10-11 00:45:40 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| e2de6c2a-3a66-35b9-8b94-af8430f8d436 | -7.6798 | -47.240101 | 2024-10-11 00:45:40 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 248238ce-aa54-34d8-a3ec-d11e9807502b | -7.6819 | -47.248798 | 2024-10-11 00:45:40 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eab16b8c-fcc8-3f9d-9392-ec05762eb6a5 | -8.4921 | -50.7901 | 2024-10-11 00:45:40 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be9bd849-ce75-3545-b8c8-6bfc75d0ff49 | -8.4937 | -50.797001 | 2024-10-11 00:45:40 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75e0035f-b87f-3714-b0c1-dd1b82462c23 | -8.9225 | -52.784401 | 2024-10-11 00:45:40 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd835122-882e-30a5-a94c-bcef7070e2c4 | -8.9242 | -52.792 | 2024-10-11 00:45:40 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 084b7977-5708-3bb6-9457-984c3aec8f19 | -8.9325 | -52.8302 | 2024-10-11 00:45:40 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fb881bc-0690-302e-933d-500129a4bcec | -7.2232 | -45.521999 | 2024-10-11 00:45:40 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e0b2d95-7d1a-3d5f-9d7c-a26c0d6f1ce6 | -6.1301 | -47.2664 | 2024-10-11 00:45:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 82d8c5eb-e0fc-3c9e-8b29-f7fde2300f19 | -8.1765 | -49.755402 | 2024-10-11 00:45:41 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f73944fd-b4a1-35f6-a1e4-9abe4f3970aa | -8.8862 | -53.042099 | 2024-10-11 00:45:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1d4a3df-f494-3b6e-9bd7-1277efdec0b7 | -8.8879 | -53.049801 | 2024-10-11 00:45:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08304114-7c5b-3d0f-b25c-3b11a8911644 | -8.8629 | -52.982201 | 2024-10-11 00:45:41 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cccfaaa6-ffd5-31ba-82a2-278b1e4703b6 | -8.8679 | -53.005402 | 2024-10-11 00:45:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a9fd519-1d91-34bf-a17c-c23e1921b06f | -8.8696 | -53.013199 | 2024-10-11 00:45:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6a720dc-b023-38a8-b188-121850798efa | -8.8764 | -53.044201 | 2024-10-11 00:45:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec44b19c-20f6-3c86-b9d6-ae6618f04d6a | -7.0451 | -45.077599 | 2024-10-11 00:45:42 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 441177b9-2a5a-3682-9154-6639578e3eb5 | -8.8548 | -52.992001 | 2024-10-11 00:45:42 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4f33b9f-a99d-3848-92be-34f2354dabc9 | -8.8565 | -52.999802 | 2024-10-11 00:45:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28aff129-efc2-31f4-b166-a5192ede3025 | -8.8581 | -53.0075 | 2024-10-11 00:45:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a92074e-1a0b-31d8-834c-de7d1f6d0ed3 | -8.8598 | -53.015301 | 2024-10-11 00:45:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23055003-7269-38bd-9066-ebbbf5f67b5f | -8.8615 | -53.022999 | 2024-10-11 00:45:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42f8bd1c-d597-3402-ae40-e81189847b6c | -8.8632 | -53.0308 | 2024-10-11 00:45:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42d31931-53d1-315c-a6c4-687af39e59ea | -8.8649 | -53.038601 | 2024-10-11 00:45:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f07da58f-5011-35e8-8d4d-196457d8f564 | -8.8666 | -53.046299 | 2024-10-11 00:45:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19abdb7b-f2f3-3c53-9503-5959fd263e8c | -6.9546 | -44.828701 | 2024-10-11 00:45:42 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef8d7af3-4474-3040-a883-a6b61e4cab36 | -6.9576 | -44.841099 | 2024-10-11 00:45:42 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef1704bf-1a63-36be-9830-9ed6c9f6a6e0 | -6.9449 | -44.831001 | 2024-10-11 00:45:42 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb317278-810b-3ec5-a297-24d9796ff0ff | -6.5589 | -60.0252 | 2024-10-11 00:45:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 1ee022f7-d7d3-31ef-ad48-500918192788 | -6.9439 | -45.2145 | 2024-10-11 00:45:44 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61b22de6-75a9-36b8-91c6-c3933c56030d | -8.0163 | -49.8214 | 2024-10-11 00:45:44 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdf5014a-ff1c-3bc0-8aca-22337fd69334 | -9.402 | -56.2854 | 2024-10-11 00:45:44 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34d895d2-5cb3-3209-926e-283a46cacd19 | -6.747 | -59.3259 | 2024-10-11 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 20b16213-4aea-3be7-983b-65f116cc4d04 | -6.986 | -45.694901 | 2024-10-11 00:45:45 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fcf2fb8f-bc56-3289-84a0-5913a0acdb98 | -7.731 | -49.0219 | 2024-10-11 00:45:45 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
