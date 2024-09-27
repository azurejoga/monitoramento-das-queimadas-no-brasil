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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 637ce2ed-5d13-3700-9d52-4e1cf5e5eba5 | -9.3901 | -50.010799 | 2024-09-27 00:34:53 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bdfc840e-a299-3ef0-a8dc-3c32160f708f | -9.3918 | -50.018398 | 2024-09-27 00:34:53 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f1c8f62-eb8c-390f-b21c-6119b3672c6f | -9.3934 | -50.026001 | 2024-09-27 00:34:53 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6fb76124-ad98-32c0-8591-c4cee14c7061 | -7.5768 | -42.278301 | 2024-09-27 00:34:54 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7a6e21ec-7e63-3d96-abda-411f2d67d569 | -7.5797 | -42.290298 | 2024-09-27 00:34:54 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c72a367d-1b1e-3f6f-971c-bebb24234794 | -10.2228 | -54.099098 | 2024-09-27 00:34:54 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 686f711f-06e4-395c-81cd-bd572b039715 | -10.0428 | -53.422501 | 2024-09-27 00:34:54 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37b2ecc6-56c5-3a5c-aa11-b87ec26c5be8 | -10.0453 | -53.434299 | 2024-09-27 00:34:54 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50d9c8d4-5e7f-3651-91cd-c24a7813d9b0 | -10.0526 | -53.469799 | 2024-09-27 00:34:54 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e98517d-8fcb-3cd5-a1c8-0122d3dd99f2 | -8.8457 | -47.9193 | 2024-09-27 00:34:54 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e901016-6ea4-344e-88ab-dbc835ab989e | -10.0306 | -53.412701 | 2024-09-27 00:34:54 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3f6261d-5acb-378c-a976-3f39f7b1aa8d | -10.0331 | -53.4245 | 2024-09-27 00:34:54 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69eea801-61e6-3de2-b075-22f90d8dc36a | -10.0355 | -53.436298 | 2024-09-27 00:34:54 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c05262c3-ad07-3dd2-860c-2d7621956f98 | -10.038 | -53.448101 | 2024-09-27 00:34:54 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07034554-9e49-3647-8f2e-1903f4f1fbcd | -10.0404 | -53.459999 | 2024-09-27 00:34:54 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b3882ca-c1c0-32ea-b2cb-b7f3e44f7f24 | -10.0429 | -53.471901 | 2024-09-27 00:34:54 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8aa0cd1c-c3ba-36fc-9f9a-d4062a024d4b | -10.0208 | -53.414799 | 2024-09-27 00:34:55 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a51031f0-33fe-30c1-9589-08968f139644 | -10.0257 | -53.4384 | 2024-09-27 00:34:55 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd9b0f8f-2396-3c15-b7ff-b7e40a094e89 | -10.0306 | -53.462101 | 2024-09-27 00:34:55 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 439eb55a-702f-35ea-abb6-ab25e4b23e8f | -10.0331 | -53.4739 | 2024-09-27 00:34:55 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 446aebe3-739d-3542-abae-e75c3cccc82c | -10.0135 | -53.4286 | 2024-09-27 00:34:55 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ea66e69-b86e-3fe2-9d3d-92f1dad36f2c | -10.0159 | -53.440399 | 2024-09-27 00:34:55 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59ff1627-d177-323f-8c8a-83ee64887b73 | -9.3304 | -50.729698 | 2024-09-27 00:34:57 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90e0e457-f208-3dc8-835e-67668cb4498e | -9.3321 | -50.737801 | 2024-09-27 00:34:57 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a14b9f4-8872-314e-a863-b48d9eea9a90 | -9.3241 | -50.7481 | 2024-09-27 00:34:57 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 948ad8f5-3bbe-33d5-80a9-8cc5dc3f7ac5 | -9.4552 | -51.4543 | 2024-09-27 00:34:57 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d28bae5-2a33-3a99-9da4-f2b28f950cef | -9.4571 | -51.4631 | 2024-09-27 00:34:57 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eec93349-482f-362f-812f-824bebee4323 | -9.4454 | -51.456402 | 2024-09-27 00:34:57 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb86c590-aef2-3d2a-ada3-6e9efbdd789c | -9.4473 | -51.465199 | 2024-09-27 00:34:57 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d64e3050-a1c5-3ccb-be4b-425f1a03ccb4 | -9.4338 | -51.4496 | 2024-09-27 00:34:57 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef3eb4d5-c9b8-3828-959d-7c7aac08bc53 | -9.4357 | -51.4585 | 2024-09-27 00:34:57 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e010de5-2982-3072-a252-9d4d97132c26 | -9.4221 | -51.442902 | 2024-09-27 00:34:58 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7582964-94b8-3444-b07f-5981bdef0de3 | -9.424 | -51.451698 | 2024-09-27 00:34:58 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cbd530c-1317-321c-ae22-d8c7f81829d5 | -9.4259 | -51.460602 | 2024-09-27 00:34:58 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03dbba51-07ca-3893-bf8e-d59d8d5cf559 | -9.4067 | -51.418598 | 2024-09-27 00:34:58 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3af6fd73-8a96-33ee-97e0-13969c7bd99b | -9.4085 | -51.427399 | 2024-09-27 00:34:58 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75a41b15-7e7a-3ee8-a96e-2f9ac51e1b68 | -9.4104 | -51.436199 | 2024-09-27 00:34:58 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e1596e6-01e5-358b-8fd4-a18b929fc038 | -9.4123 | -51.445 | 2024-09-27 00:34:58 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 077bbb06-b956-33c3-8f66-ef3db578b642 | -9.4161 | -51.4627 | 2024-09-27 00:34:58 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13c78aae-683b-3aac-979d-e347ed780bf0 | -6.599 | -39.5686 | 2024-09-27 00:34:59 | METOP-B | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cc8113bb-e8a5-35bd-a34b-81b4d093eb72 | -8.9473 | -49.724098 | 2024-09-27 00:34:59 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f7482d3-e520-3686-a456-e585a9ab01bf | -9.6617 | -53.501801 | 2024-09-27 00:35:01 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 630226f1-1d57-3c05-80f3-e2ec99251588 | -9.6641 | -53.5135 | 2024-09-27 00:35:01 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dccc3dc1-8954-3bd4-b8b5-691b67063185 | -8.3572 | -47.5798 | 2024-09-27 00:35:01 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1614925-4497-3f65-b77e-9717395990fa | -8.7827 | -49.629601 | 2024-09-27 00:35:02 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 107e56a8-e9bf-3d8d-bd0c-3f63c5a8dbbf | -8.7843 | -49.636902 | 2024-09-27 00:35:02 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c1a3124-090b-3fda-98d8-c99b2d7f2695 | -7.804 | -45.5187 | 2024-09-27 00:35:02 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53b5c959-cb86-3760-9dab-a642d8311bb9 | -7.8058 | -45.5266 | 2024-09-27 00:35:02 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 785e2809-54cb-3181-896e-444deba45a8b | -8.7512 | -49.7672 | 2024-09-27 00:35:03 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fedf9493-94a8-3a99-ba33-251ad8f094d0 | -8.7528 | -49.774502 | 2024-09-27 00:35:03 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de0e4e72-5dfe-38d4-ad68-c0c1435eb61e | -8.6631 | -49.413101 | 2024-09-27 00:35:03 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87f90cf0-8444-3998-8837-03682bdadc62 | -9.0462 | -51.172001 | 2024-09-27 00:35:03 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66fc3bae-8843-343c-9cf3-c98d84e39bcc | -9.0481 | -51.1805 | 2024-09-27 00:35:03 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf6bee44-9601-37c6-ab39-e17dd51e212a | -8.5576 | -49.5877 | 2024-09-27 00:35:05 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d66672d-6e2c-3438-8e5d-2f92f94e49d9 | -8.5592 | -49.595001 | 2024-09-27 00:35:05 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d642545-7bb7-378c-9d09-8de49b331597 | -8.5608 | -49.6022 | 2024-09-27 00:35:05 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6965a9db-8561-3cf1-9666-47d68a8a6fda | -8.5624 | -49.609501 | 2024-09-27 00:35:05 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6410aae9-4ae0-3b8a-8da8-207f449920b0 | -8.5478 | -49.589901 | 2024-09-27 00:35:05 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 480f299b-ad61-3e20-8179-9dccb979cf29 | -8.5494 | -49.597099 | 2024-09-27 00:35:05 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e698ee6-287c-3866-b810-782949b7e938 | -8.551 | -49.604401 | 2024-09-27 00:35:05 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 506141d2-0a84-370b-afe3-e5844f1ff039 | -7.7635 | -46.148602 | 2024-09-27 00:35:05 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 234d7c6f-05b2-304f-a65d-73896e08f638 | -8.7571 | -50.736 | 2024-09-27 00:35:06 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa5f298d-0b9d-34ce-9ac8-d9516a3d072e | -8.7589 | -50.743999 | 2024-09-27 00:35:06 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a99923da-951d-388d-9a68-e9bb191c0c3e | -8.7606 | -50.751999 | 2024-09-27 00:35:06 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09bb6b69-3168-3db1-9aa4-b6bbc71b9b43 | -9.0099 | -52.1031 | 2024-09-27 00:35:07 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a2e9443-846a-378b-a819-7ce192cc5ed1 | -8.9923 | -52.116699 | 2024-09-27 00:35:07 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc0d22ce-09c8-39eb-8bf7-f39ef4110a5e | -8.9825 | -52.118698 | 2024-09-27 00:35:07 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15bdb9b0-26a7-3da8-818b-96ab5784d136 | -8.9845 | -52.128201 | 2024-09-27 00:35:07 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b79ff73d-a644-300f-8978-8df701f57e2d | -7.4213 | -45.158298 | 2024-09-27 00:35:07 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ef1f770-c240-325b-bbd0-206acf112978 | -7.0526 | -43.933701 | 2024-09-27 00:35:09 | METOP-B | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6c0712e3-862c-34c2-a889-e33f5a2aaf0a | -7.0549 | -43.943401 | 2024-09-27 00:35:09 | METOP-B | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ca63ff08-d8e4-3480-9289-fa31ce4cae3d | -7.7656 | -47.1059 | 2024-09-27 00:35:09 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9c1c9f2-4f56-3ba4-976a-44551f4b43cc | -7.2196 | -44.7789 | 2024-09-27 00:35:09 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71a83d96-d3c8-3a30-97c7-395b591aeac9 | -7.2216 | -44.787498 | 2024-09-27 00:35:09 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46d7c535-53bb-3f95-99ba-519357b0d6c8 | -7.2098 | -44.7812 | 2024-09-27 00:35:09 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad561f52-b1bb-350d-b42c-754e8a738311 | -7.2477 | -44.9436 | 2024-09-27 00:35:09 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c971788-2b05-3eff-9cb8-4e8e59679054 | -7.2496 | -44.952 | 2024-09-27 00:35:09 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee106fa6-654b-3b53-8245-877a4ae41f16 | -7.2516 | -44.960499 | 2024-09-27 00:35:09 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b3e912d-3955-39c8-aac8-396f9fe3cb8e | -7.2398 | -44.9543 | 2024-09-27 00:35:09 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffedc518-d3f1-3160-a0b6-3a6c3c8a7e13 | -6.6586 | -42.574402 | 2024-09-27 00:35:10 | METOP-B | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c1224e41-b4de-373d-8136-ec7bc8392614 | -8.7881 | -52.022999 | 2024-09-27 00:35:10 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d960da35-81ea-3bfc-b6ea-d0d6dc0aa4e3 | -8.7901 | -52.032299 | 2024-09-27 00:35:10 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3397a627-de3e-31ab-9353-a6dbf5581118 | -8.9123 | -52.751999 | 2024-09-27 00:35:10 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abc35366-44c9-3abe-a04d-e2aba6c66e28 | -8.9145 | -52.762299 | 2024-09-27 00:35:10 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e0d825d-c564-33ba-b164-736d185d6683 | -8.6047 | -51.454601 | 2024-09-27 00:35:11 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf185b92-1ef4-36fc-91f6-1a12a5e92570 | -8.7037 | -51.9636 | 2024-09-27 00:35:11 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 987755d9-7d90-315b-8224-695c4344d3be | -8.7057 | -51.972801 | 2024-09-27 00:35:11 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83026081-0eff-37ec-9adf-1c07ef4a70cd | -8.7195 | -52.037601 | 2024-09-27 00:35:11 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f77997d8-c9a5-3560-8720-fc259557b569 | -8.7215 | -52.046902 | 2024-09-27 00:35:11 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d12cb9f-7b8c-33fd-bdd2-265a5dfd7a49 | -7.3268 | -46.0434 | 2024-09-27 00:35:12 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 753880d3-0532-36dd-a3ac-4e4067b3d991 | -7.3285 | -46.0509 | 2024-09-27 00:35:12 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80ab9fac-6d1c-375f-b22f-ddc9d56beb02 | -8.1762 | -49.816799 | 2024-09-27 00:35:12 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7805d8dc-c6a2-3476-ad58-b129e2d3095b | -8.088 | -49.509998 | 2024-09-27 00:35:12 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12cfde6a-4a20-3d40-a584-b6023377e895 | -8.0895 | -49.5172 | 2024-09-27 00:35:12 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a17cf8a-82d4-33e2-bf19-43307c766a6f | -6.6834 | -43.504002 | 2024-09-27 00:35:13 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76a31fc2-8b24-35b9-9b44-76076a1aec68 | -8.1388 | -49.786701 | 2024-09-27 00:35:13 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de93699b-4f9c-31f9-9207-78c240e1b07e | -6.8674 | -44.2864 | 2024-09-27 00:35:13 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 291df620-660f-3da4-b3dd-d7455c068c14 | -6.8696 | -44.2957 | 2024-09-27 00:35:13 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19666a4e-2a33-34b5-b617-20ae217569c0 | -6.8576 | -44.2887 | 2024-09-27 00:35:13 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 120c51ca-2628-3c2b-8a34-17f573c4f471 | -6.8598 | -44.298 | 2024-09-27 00:35:13 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README13.md)
