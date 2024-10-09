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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b41c84ae-5a0f-3d81-bf06-a947943c11ea | -9.8107 | -56.41835 | 2024-10-09 01:13:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7a899094-7951-35e1-8ba2-0661e8a45259 | -9.81001 | -60.4432 | 2024-10-09 01:13:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 642f6cbd-77f3-3218-83ec-f908cbfd17e2 | -9.80999 | -60.43649 | 2024-10-09 01:13:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| a54abb95-311c-3244-816e-35bbe118169d | -9.75225 | -53.15273 | 2024-10-09 01:13:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3b1a0efe-c9e5-3960-b066-5b337ba8f7f7 | -9.73613 | -56.99278 | 2024-10-09 01:13:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 547cc77a-f844-3795-aa16-52755a00cc7b | -9.73444 | -56.98453 | 2024-10-09 01:13:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 1358661d-6e5f-312f-9e55-137e98daae97 | -9.73431 | -56.97808 | 2024-10-09 01:13:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 725f1e12-7e3c-3268-8418-192d26cc3883 | -9.67338 | -52.24199 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3da5799e-00e4-39e4-a698-dd05fe1d8721 | -9.59065 | -56.47321 | 2024-10-09 01:13:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 9aefa1c7-5d74-3bbd-8df9-01e1b7fecaf4 | -9.49159 | -56.08137 | 2024-10-09 01:13:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 52ca5bd9-9e4a-361a-821b-8cbaaf364663 | -9.46954 | -52.10204 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9a225aec-0c51-3ca8-9b1f-3e83b5b37b64 | -9.3196 | -54.52449 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 86a1f9fb-de92-31bf-ba8a-b4cc4ccd20f5 | -9.31467 | -54.53093 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 72f12213-24e6-32fe-ad41-ec9faffdefe7 | -9.30528 | -54.53226 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 15ac20f6-ad44-38d7-940e-52abddf01c63 | -9.26669 | -46.72464 | 2024-10-09 01:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 6cc29eb3-7388-34a2-9841-ef83c84e96da | -9.26403 | -46.70752 | 2024-10-09 01:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 0821b578-163d-36cc-9d15-9760b0c1c7fa | -9.24998 | -50.36952 | 2024-10-09 01:13:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fe604036-7670-3679-b06e-50d866c6baa1 | -9.21229 | -47.95565 | 2024-10-09 01:13:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 166ffc96-c976-3a88-9fa5-c8a80e9cf087 | -9.16732 | -61.57636 | 2024-10-09 01:13:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 46077d98-1821-3ec9-a8d2-9c41e0aafc47 | -9.15871 | -61.58397 | 2024-10-09 01:13:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b657ff25-8d89-3835-b6e1-638cb2ead0c3 | -9.11975 | -50.30459 | 2024-10-09 01:13:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e034ce10-13af-3181-83a5-c54f1cd27f6c | -9.1183 | -50.29465 | 2024-10-09 01:13:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c1fc0511-718c-3074-ba27-01b6af7c6b04 | -9.09018 | -61.1385 | 2024-10-09 01:13:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| e698dbd4-1f06-3531-bdcb-eadd5ab04c7f | -8.98425 | -52.79635 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d599eeea-f45f-36b8-b2da-f58feca04d7b | -8.93999 | -52.80271 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e20b5f77-e25c-3a69-82a5-43116cded1cb | -8.86756 | -53.01056 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d7d262ec-5c0e-3183-9330-9245c4e7200e | -8.86632 | -53.00156 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 495d6922-946f-306f-b8c9-364d9fd5024b | -8.86509 | -52.99261 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 826402a4-9867-3ec2-ba6a-60f570e92543 | -8.86486 | -53.05679 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e671aef6-6389-3041-bbb7-0ec7659af0ab | -8.86362 | -53.04779 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d0ce08aa-062a-3ef4-a217-155348544085 | -8.7446 | -49.5706 | 2024-10-09 01:13:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 60d76cec-f899-3949-aba2-870ea3802f0f | -8.62404 | -54.93663 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3f25676f-977e-3d6c-91ef-e3813ae89f4e | -8.62263 | -54.92626 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9d023d01-6cb4-3a33-94ba-f0b7040db33c | -8.56427 | -50.53177 | 2024-10-09 01:13:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8463972f-a317-3036-bde7-b2e0159b27e9 | -8.54581 | -51.37278 | 2024-10-09 01:13:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5ff20acf-eef0-3c6d-a1fd-fcda6da5849d | -8.52543 | -50.02609 | 2024-10-09 01:13:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 18786b98-9cf8-39ea-a9a0-aeb7eff554b3 | -8.52345 | -48.78039 | 2024-10-09 01:13:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 5911f3ad-bdd1-37f2-8da8-d9215013bfe2 | -8.50269 | -48.64385 | 2024-10-09 01:13:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 6f8fe7a7-7d20-34c0-9f7b-a274be6d626c | -8.49425 | -48.65829 | 2024-10-09 01:13:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 7b98ae6e-8f57-314e-989c-6a6e796de8d0 | -8.49229 | -48.64554 | 2024-10-09 01:13:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 397.7 |
| 8e7edaae-c07a-37ab-bfc6-5022e6398cfb | -8.49033 | -48.63269 | 2024-10-09 01:13:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 06bec1a7-570c-3e8c-954a-73402ff9eac5 | -8.48446 | -55.16636 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3c624b1a-0ede-3bc1-ac3b-1317e0b4ed7a | -8.33714 | -49.66381 | 2024-10-09 01:13:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 04b3604b-9566-3c44-9f60-30c1027fe215 | -8.30394 | -55.1167 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 8ddfeb5c-1958-3983-8694-d2b0879468d5 | -8.30256 | -55.10615 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 5127346d-aac4-3d4a-b8d2-9b72a3d2a4cc | -8.23975 | -46.28519 | 2024-10-09 01:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 1cf82fe8-31aa-3432-b890-6f691ca74e97 | -8.22213 | -54.90029 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2157353a-b492-3cc0-a292-c9f2460a8b6c | -8.22076 | -54.89005 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 153d92bf-b0a0-3204-a378-a7a61b8ca47b | -8.07118 | -49.66665 | 2024-10-09 01:13:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 954d7659-231e-34ea-9eec-3512a6ba57e4 | -7.9747 | -54.8283 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cfe2bc4e-a25e-3c69-8353-e5287fbb5c4f | -7.9653 | -54.82962 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8c63c0ca-47ea-3456-a476-b117f8fabb2a | -7.95705 | -54.76915 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 02c69f97-b684-373c-808a-a61193dd2d38 | -7.95569 | -54.75913 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1f11e862-b054-3c27-8029-b4661de1127c | -7.85445 | -54.90249 | 2024-10-09 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 90b8ae94-80da-341f-bdcc-9f110fd31788 | -7.67858 | -47.3261 | 2024-10-09 01:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 10c8b408-fbf2-326e-be69-c4e80dabfb3e | -7.67609 | -47.30988 | 2024-10-09 01:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 438befae-7c1f-3401-ba39-29e2c355a7b5 | -7.48549 | -46.67385 | 2024-10-09 01:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| d1a0c568-90ad-3e68-a0d4-d6ba744f424d | -7.44056 | -49.68542 | 2024-10-09 01:13:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f0a3b5ad-b38e-3529-85d2-0e68c29d2a25 | -7.43817 | -49.68062 | 2024-10-09 01:13:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 840e943a-1c87-36c9-a0d7-37ffdac1e0cb | -7.31027 | -44.97963 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| dd01b109-3a1c-33c5-82dc-02981470d002 | -7.20643 | -47.69709 | 2024-10-09 01:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 16fd3e30-3c23-398b-a0f8-cd2def130b3c | -7.11785 | -49.86058 | 2024-10-09 01:13:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 233853d8-b21f-385c-b5e1-bfbb8787325c | -7.04236 | -48.05919 | 2024-10-09 01:13:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8c71103e-1ca2-3fea-9caf-876c825bb838 | -6.66902 | -47.10332 | 2024-10-09 01:13:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2407f0e8-fe00-301b-a700-abbf5d3ef029 | -3.99711 | -46.08611 | 2024-10-09 01:15:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0f1d92e1-2272-35c5-b639-e3f19bcfd7db | -3.99351 | -46.06234 | 2024-10-09 01:15:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 455abd6f-d1c4-38fb-a1d2-13cb7405cccb | -3.93861 | -46.45797 | 2024-10-09 01:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 157.4 |
| ecc7152c-f4d3-3d7f-b79b-4ca405a9344d | -3.93687 | -47.97424 | 2024-10-09 01:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| d0f55193-f4f2-37c5-9b10-900b947530ed | -3.93634 | -46.47435 | 2024-10-09 01:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b848e485-ca3d-3a0a-9b1e-65e004f97ebe | -3.93548 | -46.43636 | 2024-10-09 01:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 55e5efc8-3da6-3ffc-b796-aea3a60954a1 | -3.9344 | -47.95737 | 2024-10-09 01:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 7583b2fe-2f5e-3bfb-970b-e48b7f29ee7c | -3.93316 | -46.45354 | 2024-10-09 01:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 298.5 |
| 9cfbe021-e82c-3a10-b500-d40d615edc5c | -3.92978 | -46.43151 | 2024-10-09 01:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 8772c3cb-cca3-356f-9ad0-079b09631911 | -3.9252 | -46.46027 | 2024-10-09 01:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 4f4e33e2-066d-32e4-9151-73335d9b3c2e | -3.92278 | -51.21253 | 2024-10-09 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1400e3a6-56e3-3588-bc91-a67f4151d080 | -3.922 | -46.43836 | 2024-10-09 01:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 412b4a60-6923-3def-b154-2751739a6e51 | -3.91534 | -45.3428 | 2024-10-09 01:15:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 5432df4f-e8b0-3f43-8a5b-966dfdb03eda | -3.91177 | -46.46247 | 2024-10-09 01:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 3b9e6e71-c075-311f-a652-68228d8c3490 | -3.91115 | -48.34782 | 2024-10-09 01:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 4cf159d3-f72e-3952-a88b-54859773e0de | -3.9096 | -46.47919 | 2024-10-09 01:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| ee6481bb-6c4f-3561-8c24-f96852ac9191 | -3.90629 | -46.45786 | 2024-10-09 01:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 155.0 |
| 700fb532-4f69-31df-9fbd-dd9cb510c1eb | -3.89913 | -52.41082 | 2024-10-09 01:15:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9175ec5a-a1c0-3401-a08f-174b727486ae | -3.89834 | -46.46468 | 2024-10-09 01:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 8cbe5325-370b-31f9-94cc-4e3a908d0ed2 | -3.89501 | -46.44218 | 2024-10-09 01:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.7 |
| aaa841d9-da8f-33b7-8a67-f6dbd6f1ee6b | -3.88094 | -49.98944 | 2024-10-09 01:15:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 703af639-b92c-3ade-92c1-a131a3756335 | -3.84329 | -49.45698 | 2024-10-09 01:15:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 61d60d05-0411-322e-bf39-66797a7250a5 | -3.82498 | -52.40878 | 2024-10-09 01:15:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 31b32820-e976-3d8e-b6d0-696f53f8ba12 | -3.81072 | -49.49408 | 2024-10-09 01:15:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 19570594-d574-3496-9b71-eb33fdf453b9 | -3.80889 | -49.4812 | 2024-10-09 01:15:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 296d00d8-ce96-3dbd-9d60-beea76479588 | -3.79799 | -52.21693 | 2024-10-09 01:15:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0c0750d1-3c60-3da2-9c8c-b855b60a9b9f | -3.79042 | -52.42294 | 2024-10-09 01:15:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 43ad1c1a-b961-326f-9d7c-189106ae9ea6 | -3.78516 | -52.25623 | 2024-10-09 01:15:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 88a1cf05-4c16-3f9b-8bb4-4eca1e9341da | -3.75603 | -52.31352 | 2024-10-09 01:15:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 36bb78e6-2e28-36e4-9b24-4bdd8a03293e | -3.74703 | -52.31475 | 2024-10-09 01:15:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 998e7b01-c1a1-3aa0-b62d-1d545c7bc216 | -3.70374 | -50.18353 | 2024-10-09 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ac65a748-1c04-39a0-82d9-79b2c55fc781 | -3.70208 | -50.1719 | 2024-10-09 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d43ef5d1-63c1-3389-9765-01e51a1cd560 | -3.69811 | -47.59754 | 2024-10-09 01:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 6410a36a-2b1b-333f-a5ac-a3ff7ac57f35 | -3.69544 | -50.12534 | 2024-10-09 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 8294bc64-8bf9-325f-966f-87c71141338a | -3.68533 | -50.12675 | 2024-10-09 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b4c939ee-9371-36e1-b951-c687532373ac | -3.65498 | -54.29874 | 2024-10-09 01:15:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README31.md)
