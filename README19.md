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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0e78998-f4ad-30cd-9c4c-bc15a5d75fcb | -2.4854 | -47.57523 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 41acdd90-ecb8-38cf-99df-e97cb492164d | -4.43368 | -40.92308 | 2025-08-15 04:00:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fd23f35e-0b9b-3060-9988-dd499f8df687 | -2.5406 | -47.71491 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 538ae7f1-130a-3a94-84b2-611e130de113 | -4.1879 | -42.42864 | 2025-08-15 04:00:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 699cbeba-e6cd-3ae9-8f95-65949bfe184f | -3.82164 | -41.56569 | 2025-08-15 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2d2dff0b-12a7-3f69-895d-f8aaab06b114 | -2.90849 | -48.30387 | 2025-08-15 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31f9a979-9520-32e4-9c64-8975976e70ae | -3.81999 | -41.55397 | 2025-08-15 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 14404ccf-4f3e-3ea1-aaf9-9dee47d1c390 | -3.38008 | -47.60834 | 2025-08-15 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0825b81-50b1-337f-8339-c3eb08f4cddb | -3.10958 | -47.50084 | 2025-08-15 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7685907-655f-3741-b7a8-421d557743ef | -3.82104 | -41.56943 | 2025-08-15 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cdc999eb-f58b-36ff-ba35-14a6904e1801 | -4.18825 | -40.75691 | 2025-08-15 04:00:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8be452a6-c8dc-34e4-a046-efd85334a4a5 | -2.49094 | -47.57314 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 051aeda2-152a-3f64-a812-f395867e7aca | -2.4919 | -47.56734 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3316bac5-ee1a-3ed2-ad77-69a763123639 | -2.54108 | -47.71194 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7f734bd-cda2-3248-82c6-b82ccd6813f4 | -4.18435 | -42.42808 | 2025-08-15 04:00:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b3acd351-6197-3f9c-a4c3-107b87b40530 | -3.88508 | -42.55342 | 2025-08-15 04:00:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6128c16b-7b94-3c79-9dfd-7d2779808d8a | -3.42558 | -40.4149 | 2025-08-15 04:00:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aada0ccb-28c8-372a-86f8-774899b412e2 | -2.49045 | -47.57602 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9fb0843d-345f-39b7-8b40-ba5d7ea2870c | -2.90831 | -48.30126 | 2025-08-15 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74bae451-4053-39a8-b47c-eb340c1dd991 | -3.95465 | -41.48021 | 2025-08-15 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2f623c62-0cec-3faa-b60f-a35a86946762 | -4.39164 | -41.90834 | 2025-08-15 04:00:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 79709236-c874-31cb-9fb0-88a9a5121c8c | -3.3796 | -47.61119 | 2025-08-15 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d942cf7-5d73-341e-9bfb-5bb12a14c2f6 | -4.18453 | -42.42846 | 2025-08-15 04:00:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 71b6b3a0-4a63-330e-9a98-179ade123e66 | -2.48588 | -47.57233 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f3e18ebd-55c6-31a0-8418-c21d8175aa9d | -3.32331 | -48.72438 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 774f9f44-5551-3a14-a3f8-a42642e31a54 | -3.95866 | -41.47703 | 2025-08-15 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 232f1c4e-7908-364f-9b62-5bac2ec661b4 | -4.1839 | -42.43248 | 2025-08-15 04:00:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e7f189f8-b4b8-38db-aad8-57abff4db6ec | -3.49457 | -43.31297 | 2025-08-15 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 049940b5-0263-30ae-8c18-a9ad8f9334b5 | -3.94481 | -41.83278 | 2025-08-15 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c43e6e4c-ebba-3263-968d-f5a389c87c9b | -4.39103 | -41.91214 | 2025-08-15 04:00:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 39958302-2728-3900-b42f-cae59101b6a4 | -3.49586 | -43.31127 | 2025-08-15 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 490970c3-7aad-3622-8c59-90f7fac716e2 | -2.48741 | -47.56865 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29aedfa2-9856-3db5-b9a8-907a62a84196 | -4.43313 | -40.92657 | 2025-08-15 04:00:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ff3c0e36-173c-3b1e-99ca-d854d75b3eba | -3.49831 | -43.31358 | 2025-08-15 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45bb18ce-40c1-34f7-9959-ed7f79343855 | -3.42114 | -44.31136 | 2025-08-15 04:00:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17cad534-73fa-36ef-af49-68f634de0f4f | -2.48637 | -47.56943 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 998be615-c9c9-3be4-81e3-dac34e39fabc | -2.91359 | -48.30207 | 2025-08-15 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9998df10-9832-3101-a88e-9b8ee55f7718 | -2.48695 | -47.57155 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9cd4df31-f986-387a-9255-b9e5c94ce156 | -2.53551 | -47.71403 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| caf5814d-5304-39cd-bfaa-b1d9fea53752 | -4.22716 | -47.21535 | 2025-08-15 04:02:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ae9c3ee-b15c-3532-842b-c39e40c4143b | -7.09608 | -41.46926 | 2025-08-15 04:02:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f06e2e90-5494-3ab8-89b8-978aa23dfb37 | -9.84446 | -43.17693 | 2025-08-15 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 02bb99d6-ad57-3541-9c68-91e04dcfcdeb | -3.43344 | -49.04909 | 2025-08-15 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1710a663-547d-3b34-a5ec-ad9321e43140 | -8.52476 | -43.29574 | 2025-08-15 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d99c7a45-c06e-3925-86c1-445ab1804505 | -11.92059 | -43.43999 | 2025-08-15 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33665402-0b95-38f5-a57f-c85609a7ec6e | -5.59797 | -45.38154 | 2025-08-15 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a671351-d55b-3dcf-bf80-0be68e2d70d5 | -7.42775 | -44.57903 | 2025-08-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f279358-1e5a-3393-8b65-b923f5cd91c8 | -8.29 | -45.00442 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af236ae8-9f18-3484-a936-f347de8c4641 | -8.74328 | -44.0372 | 2025-08-15 04:02:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cde0fa9-d2d9-3c09-888b-6d6116426bb8 | -4.58962 | -43.32289 | 2025-08-15 04:02:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3f847641-15e8-36e7-a502-352b91d95213 | -10.35556 | -50.80978 | 2025-08-15 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df0d0199-31c9-32da-8723-a3b7426b6ef5 | -7.56946 | -47.06575 | 2025-08-15 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01555866-4e69-3b09-90d9-016a2f631062 | -3.43403 | -49.04548 | 2025-08-15 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 10daed27-a1bc-385c-a0b7-155f4703d158 | -7.31527 | -44.69456 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bc2a338-051b-3f5f-96a7-791f1b02ac4c | -9.2137 | -45.3351 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9cd44859-ed4e-32c2-97fc-f3a1ed566fe1 | -7.39491 | -44.86699 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65f2b357-a368-302a-9edf-775f31c9293b | -9.18336 | -45.32481 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 06fbec78-7f2c-3adc-8dc2-f747ac0365d2 | -9.8552 | -44.68598 | 2025-08-15 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42573312-0647-3a18-9148-ddb91154910b | -8.30162 | -45.00641 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eca32e53-4cfa-32fc-955d-54cc1df3d3f9 | -8.30082 | -45.01126 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80de8bef-d467-34d7-ab5a-168dbdf0f982 | -3.4523 | -48.97318 | 2025-08-15 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b25183d6-dfc2-35e2-a71d-d666915060bb | -6.24489 | -43.23208 | 2025-08-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8b7c81d-817e-3962-84a7-f000941e4a73 | -7.37825 | -44.89441 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48555085-4ec1-3642-82e6-c1c52cdaa8b9 | -3.43402 | -49.04725 | 2025-08-15 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 64f48461-4a0c-3325-9bf9-28e09b6d246e | -8.29388 | -45.00509 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb9a42b7-7d98-3044-a728-f739a6d91006 | -5.49658 | -44.41066 | 2025-08-15 04:02:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88c5ac82-d8ce-3308-a893-e7a59ebb2d86 | -5.78559 | -43.89064 | 2025-08-15 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83bfcd1e-b783-3e88-8fab-71722e2e939c | -7.38467 | -44.88022 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e11b3f27-7b49-3507-9a48-9bb12712d069 | -6.96078 | -42.87292 | 2025-08-15 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| d0e2a46d-6e94-37ab-afd1-6068a44ebb1e | -3.42735 | -49.05181 | 2025-08-15 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| caa4a4b5-4d78-33f0-8604-f12b2a1cc979 | -5.76711 | -46.67352 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b83246a5-0a38-309a-82a3-ca5e2d9d5899 | -11.80944 | -44.26875 | 2025-08-15 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a459041d-8daa-3405-8a21-b264fcff9416 | -10.96279 | -49.56817 | 2025-08-15 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66f5030c-f6cc-309e-ad64-2ca8ee30ae9f | -5.37062 | -41.23547 | 2025-08-15 04:02:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4af5bbff-473f-31ab-9a17-591e05cd4cd4 | -6.91033 | -45.20799 | 2025-08-15 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e6eab64e-3560-3fca-b953-fc2bd56c30a5 | -4.59332 | -43.32344 | 2025-08-15 04:02:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 198044bc-ecf1-3513-a27d-1281391d1218 | -8.19659 | -42.24974 | 2025-08-15 04:02:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d3b3f591-7ca7-3f59-9c02-154d220cb59f | -6.95958 | -43.86177 | 2025-08-15 04:02:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0d398b3-97e6-3dbf-a585-909524694273 | -8.29775 | -45.00575 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a014b15e-992c-31b0-9236-bcb2dc4e8f0d | -10.86417 | -48.49645 | 2025-08-15 04:02:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 609c60a7-4be7-3881-bbe2-a8f829a21c63 | -3.4334 | -49.05087 | 2025-08-15 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 07b65094-9ef7-3ec3-ad04-d59007c6f023 | -6.96429 | -42.87349 | 2025-08-15 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 3eb76d14-3d54-35f8-bfd9-b72b111573e6 | -8.31551 | -45.01879 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| edf0dd01-33f6-3590-8ce7-8e5a2b06d61b | -9.03353 | -40.52842 | 2025-08-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 940cc28e-556e-30db-8b7b-cb651c249d80 | -7.00828 | -43.85889 | 2025-08-15 04:02:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| acdbf0d8-4086-3cb0-80ac-32e2d5276c30 | -7.15806 | -46.43484 | 2025-08-15 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de22d709-dcd2-3eba-9e1a-b57c050305f3 | -5.61682 | -43.46962 | 2025-08-15 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be656d24-b4f3-3137-a00d-83f4769f8405 | -6.55594 | -49.49835 | 2025-08-15 04:02:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a07e6ca4-e4a6-3599-9951-59c8eef04b42 | -6.33379 | -42.80048 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d52f28e3-9167-34d7-9b82-ba9741ffbbbd | -3.82602 | -47.74124 | 2025-08-15 04:02:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4258b6c0-46fa-3e8d-8cc2-68dc5bfafdf2 | -4.66813 | -48.86545 | 2025-08-15 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28646b0f-8a01-33b6-86a5-bcd307bad1a5 | -5.54608 | -45.37327 | 2025-08-15 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8ab6efd1-6916-3bf9-acba-d72846c3365a | -8.32403 | -45.01543 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53b2e579-784a-3e3f-aaa3-788a1408d8c5 | -5.3507 | -37.61725 | 2025-08-15 04:02:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6332dc3d-a5b9-3478-aafa-3b5af5b9eaa7 | -7.38686 | -44.89092 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98df7722-a497-3058-9e7d-157ed7850a0a | -11.19093 | -40.95564 | 2025-08-15 04:02:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7df14aeb-6e2e-327f-83d5-9025274d221d | -6.2135 | -44.19584 | 2025-08-15 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 616ba0fb-d536-3f33-9572-0b5337ce4330 | -6.38042 | -43.38643 | 2025-08-15 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 23ae08ea-86a0-3b32-a762-1a51fd05defa | -6.97132 | -42.87462 | 2025-08-15 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 25e69642-50e5-3e54-ba7b-01f5a80817de | -10.1838 | -49.50724 | 2025-08-15 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README20.md)
