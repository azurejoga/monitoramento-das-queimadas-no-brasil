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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a60ad19-2951-3ea9-920c-ef818885d80f | -6.94543 | -44.17567 | 2025-08-26 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d1ac7821-3018-3441-a049-9ff0701f1610 | -5.52898 | -60.20793 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 03e22029-8ce7-35de-ac53-770091f71530 | -7.73266 | -51.13715 | 2025-08-26 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64cf8063-bf7b-33dc-ab60-08dd1b3d38b5 | -7.21493 | -44.41497 | 2025-08-26 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 268286c0-2bf7-3b4d-aaa8-8edf4216fbe5 | -7.89974 | -45.87799 | 2025-08-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4e87a52c-9983-3967-9ece-95bfd6bad693 | -2.64675 | -48.05382 | 2025-08-26 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cbf5556-27b5-3524-a03c-9fd7d212ff35 | -7.53034 | -50.54145 | 2025-08-26 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 37009428-1afb-3b65-97d5-d5bb178126f0 | -6.74878 | -43.03453 | 2025-08-26 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b963492-7265-3443-a57f-89875c48e566 | -6.5239 | -44.43783 | 2025-08-26 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b869c512-c287-30b7-ad42-cfa87e976521 | -6.25904 | -60.00861 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4ba6b16-1b86-3b50-afbb-f39a0fbd6cad | -3.84111 | -49.11626 | 2025-08-26 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d14ba82-e041-3c73-8ead-c8a4725c6457 | -6.25415 | -60.00736 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6f43ee2-f197-32eb-a625-9955618fb38f | -9.16541 | -40.60072 | 2025-08-26 04:44:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0b1cec59-17f9-36c0-9bb4-1e5fcc5fa26f | -5.29708 | -60.2064 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c661175-c949-3e78-94a2-1d2fdaf9b2cd | -4.82644 | -47.31888 | 2025-08-26 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b460da3-f857-3374-8b1a-4a4cbf4b6111 | -6.57232 | -59.88314 | 2025-08-26 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f52ca549-d5f7-33fb-9fec-8a3fbc1c60ac | -6.19444 | -44.15711 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6b21aa6-463f-384a-b028-9f1eab83c683 | -5.705 | -45.53012 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8928080f-6625-3cb6-8190-5bee7733be4d | -6.18492 | -44.15768 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6539b2a0-1cd8-31e4-b16d-21c4cba19d9a | -5.8668 | -46.41392 | 2025-08-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee5bf8a4-d187-308a-9a7b-214c9502705b | -4.96289 | -55.81551 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9c258076-bb64-33ba-85f7-cac915ba0b4a | -7.0814 | -46.0595 | 2025-08-26 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a82c765b-119f-3b87-996c-5783bdac97ff | -6.18991 | -44.15612 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 477f4d2f-6304-3546-b9a6-82191b8eca5e | -7.65096 | -42.68051 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c68e6c83-6f77-32f6-a0b1-adc508ee8462 | -8.07691 | -47.31316 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80603870-779a-344b-84f3-2a3d04bd0af3 | -4.96003 | -55.80778 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bbd81b0f-b440-3266-96bf-255f35362b12 | -3.43016 | -49.05351 | 2025-08-26 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6585078a-2f1f-3c86-86bc-07b5480e7c41 | -7.73979 | -50.2877 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a8ffed7-30b4-3497-9897-cf6d86ab3bf7 | -7.61352 | -45.22647 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c3ad89b-e758-3d9f-a90a-75ddf175c6e2 | -8.22333 | -45.13691 | 2025-08-26 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83e0de0e-7865-3610-a9a9-a4c3f2468543 | -6.80266 | -44.99285 | 2025-08-26 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e4a97a8-9c23-333e-b133-a73c30717a54 | -4.96573 | -55.82336 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6ad2db2a-a90b-3d3c-8cd6-4f2890c36b50 | -5.79219 | -59.22237 | 2025-08-26 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cb93c25-313b-326c-b254-8002aaa5b104 | -6.25245 | -60.01719 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b6a0d9d-d779-3639-b76d-41735a3695f8 | -8.24706 | -45.09584 | 2025-08-26 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9643a39-e26d-3fc2-836e-8ec138629418 | -7.75153 | -50.30037 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c69e5a5-1c7e-37c3-81a7-329e92d67aad | -2.25345 | -47.85918 | 2025-08-26 04:44:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 311a23f9-629f-3409-a0db-00a6e0fc5fed | -5.29829 | -60.19949 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d95ee862-355f-33f9-b758-b7e6b69f2860 | -7.18801 | -47.56721 | 2025-08-26 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b3079e1-6439-3137-9b40-fa98ca6a66eb | -2.44489 | -47.3319 | 2025-08-26 04:44:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bd209f5-626d-317b-ba89-7766a0e98c5e | -6.31326 | -47.41978 | 2025-08-26 04:44:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c9ad938-485b-3e74-9d6b-6b7c0815d663 | -5.46714 | -42.91706 | 2025-08-26 04:44:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4badb085-7445-36d7-be48-93e8481d4961 | -7.30138 | -44.52858 | 2025-08-26 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b5117b5-b7f1-3732-a402-49e531349800 | -6.06758 | -43.99856 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 375f8002-0c49-3033-ad20-6e6e34d5ff05 | -6.81136 | -44.99418 | 2025-08-26 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90bfc212-6eb8-3319-8040-60c0387c3cc6 | -6.06374 | -43.99252 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b996ff2-a852-3a69-9c40-dd60c3ab5acf | -7.59125 | -45.22728 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2cfeae1f-9ba8-39f1-a3b3-62ab908c1e60 | -7.20966 | -44.41919 | 2025-08-26 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5b459b7-8e2e-3fae-88d8-7328b166d864 | -8.28795 | -46.33075 | 2025-08-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83c82b35-ff85-341b-bf45-2ad7ea2e508c | -4.79204 | -47.27411 | 2025-08-26 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c8df57a-de3c-35e7-9b31-4155195db4d1 | -6.80701 | -44.99351 | 2025-08-26 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79a63667-eedd-3860-a024-a3330cd086b5 | -8.15899 | -45.05377 | 2025-08-26 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16688442-b998-3186-be84-54a3382b46ed | -3.97841 | -51.05653 | 2025-08-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c68b79f-5efc-310b-b7c9-1bbbfc0a993d | -6.23676 | -60.01417 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 66801238-f631-3326-84a5-fa7d6eebf112 | -7.58315 | -47.48927 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f192d5c0-172e-3187-bc60-3e43571aaf92 | -6.25845 | -60.01186 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 035105ac-fbba-3a8d-9200-98ec8a0772e1 | -5.46981 | -42.61435 | 2025-08-26 04:44:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 779c412f-313e-38da-82ed-dcee8d511ba3 | -5.75879 | -53.77501 | 2025-08-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ab941cc-7544-3607-9d26-6cf3d31fc624 | -7.21425 | -44.41967 | 2025-08-26 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9699c424-52f2-3324-a53e-59e4239427d6 | -4.70017 | -56.06555 | 2025-08-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f06df732-04c3-3139-b180-289ef4174d89 | -5.52701 | -52.00313 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 224bf8c2-f20f-314c-9538-b1ca3cd778fb | -3.42463 | -52.63484 | 2025-08-26 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e5fd3f7-061b-3fd6-8d6e-f92e690dcccb | -7.53088 | -50.53794 | 2025-08-26 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce0e0f2a-1529-3304-b6ca-2483ad04823b | -7.21225 | -45.31065 | 2025-08-26 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3e0dcf0-720e-3560-9370-a365117a122a | -4.55482 | -55.96429 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c286e54a-84fa-3179-ac03-8ca037f1761f | -6.25189 | -60.02043 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e1dbf83-282c-3afb-8926-09d65ba42527 | -4.93572 | -47.5537 | 2025-08-26 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a893679-a11c-3ffe-b6e8-4135e58effa3 | -7.79045 | -51.05013 | 2025-08-26 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7508d6e-5d1f-381b-a5a9-d1f78a6f329a | -2.58252 | -51.913 | 2025-08-26 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91a7e5e7-4450-325e-9f79-5f69f0cfce9c | -7.5794 | -47.48871 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7d14bc8-8448-3ba2-ab69-37bcb3b9b8e5 | -6.23845 | -60.00439 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa82b9a8-24b7-350e-8a16-f7f44cd66c76 | -8.22774 | -45.1375 | 2025-08-26 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a38a2ea-109c-367b-8ae2-c53fb1f398ab | -4.69953 | -56.06938 | 2025-08-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a32eab3-9424-356d-afe9-e68267558398 | -2.29364 | -47.88847 | 2025-08-26 04:44:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a691bfdb-decd-35d4-be05-22bfa90548a8 | -6.02541 | -43.99688 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ded1598-041b-30d9-9dba-6bdef626b1db | -5.07178 | -43.0771 | 2025-08-26 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d7a0bd0-3322-31e7-a930-b95eee916f91 | -3.54506 | -49.49472 | 2025-08-26 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2368fae9-458f-3ffc-a8d4-0970c5489476 | -2.46981 | -47.77361 | 2025-08-26 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1fc53b7-1a1c-3176-b743-1acd15093ef6 | -7.74202 | -50.29537 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d95111ea-c88e-336c-b289-4d5a4b113030 | -6.65329 | -53.18736 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5920207d-9c4e-36fa-8293-68c999c97fae | -7.58732 | -47.51294 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e929b56b-7b44-3a22-a9c2-4632b0a9b3ef | -7.12575 | -43.67852 | 2025-08-26 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61bfe141-779b-3cef-a648-735429e779fc | -6.24769 | -43.82944 | 2025-08-26 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8367b29d-4a49-3f54-8438-bed3086e11c2 | -5.52237 | -45.89641 | 2025-08-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85aa0f82-a1e7-310a-a9a4-9c0f271be1ef | -5.43142 | -60.1806 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e702d64a-0f8f-3bdd-85ed-f3a6b8cef951 | -7.63519 | -45.22986 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bc90d37-90f2-38b0-aca3-4ed9193134de | -7.67644 | -46.9354 | 2025-08-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fc315c7-4b0d-36cc-a86e-d61f7b965a90 | -8.28846 | -46.32713 | 2025-08-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fafe76ee-dda6-3f59-a122-521bb6c480c5 | -6.25787 | -60.01508 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d03bd3c1-c46b-32ac-85fc-d2c9283a8c07 | -3.06709 | -40.04933 | 2025-08-26 04:44:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 09c2f333-990e-335c-9916-05be1340b040 | -7.46446 | -45.01382 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e7222b5-bbc0-37bf-8835-41b7bdc8e02a | -6.24198 | -60.01521 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ce2a9368-eff3-370e-8451-7862c71a91c0 | -8.23905 | -45.12091 | 2025-08-26 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ccaa5d3-f8d4-32d4-a7cb-676e70fcf283 | -6.25827 | -60.01482 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6650267-368c-367c-a093-6301dab7afad | -6.24041 | -47.57899 | 2025-08-26 04:44:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e98ec2d-6e2c-353a-8e40-2ddfa64a39e2 | -3.17366 | -49.47982 | 2025-08-26 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70497e0c-2003-3bef-ae81-8a30fc0139fd | -2.98726 | -49.30428 | 2025-08-26 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3da6f685-433e-31b4-8332-7b44c5de5d61 | -7.22022 | -44.4106 | 2025-08-26 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97a40155-016c-3913-87fe-d8ec47f2c6da | -5.89526 | -43.39949 | 2025-08-26 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60e67411-be9c-33a7-b4e7-faeb5dfecea8 | -7.74763 | -50.30341 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README56.md)
