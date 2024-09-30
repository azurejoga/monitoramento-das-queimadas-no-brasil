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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0535eecd-40e6-3007-a80f-a18234204701 | -7.08626 | -44.15355 | 2024-09-30 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b296ad9-f854-3f97-8595-6efe7605cc74 | -7.08422 | -44.15488 | 2024-09-30 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f2d1d39b-561b-32c5-b2bb-577ca353009f | -7.08255 | -44.15292 | 2024-09-30 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09b1a540-c68d-3416-96d3-a244e9b9abc2 | -6.97218 | -44.21877 | 2024-09-30 04:29:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69b2d294-ecb8-399c-9af1-e38f5c343bdd | -6.97046 | -44.21592 | 2024-09-30 04:29:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| adf0a7f8-3778-3ec0-a948-d558608df5e1 | -6.96846 | -44.21828 | 2024-09-30 04:29:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b55525aa-eae9-310d-9787-3baa0e9d63c7 | -7.34602 | -44.77307 | 2024-09-30 04:29:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 445eb6a3-e91b-3c31-86fe-3bda2b569505 | -7.32986 | -44.73243 | 2024-09-30 04:29:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f01ba639-0ed6-3fb8-b254-8d675908e8ac | -7.32623 | -44.73191 | 2024-09-30 04:29:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 434bcead-54ba-35c2-a667-9a9167846b09 | -7.29611 | -44.98572 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14bfd06e-3374-37dc-8ad5-cbd6b190fca4 | -7.26438 | -44.59396 | 2024-09-30 04:29:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5a25672-44db-333f-8f95-c78f074f8a69 | -7.26138 | -44.5891 | 2024-09-30 04:29:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ed4efa1-a62e-3231-bff7-7f2fd9d29c5e | -7.26009 | -44.59777 | 2024-09-30 04:29:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c83d755-2833-35fc-96c2-9de83a9fe923 | -7.25069 | -45.00471 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f9e4343-58a5-3192-b2e3-dcc1ffc4d614 | -7.24979 | -44.93822 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4938f7cd-75dd-320c-ae99-9ba66717e922 | -7.24774 | -45.00013 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed2b8560-0253-344b-9b0a-84ec31804a0e | -7.24712 | -45.00419 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94bf1293-c526-3b18-8bdc-764207912b27 | -7.24651 | -45.00825 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbff8b76-3235-3bee-9b4f-d89fa1a68445 | -7.2462 | -44.93774 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac26da5e-e7c5-3a02-ae3d-8180a9d5d275 | -7.24589 | -45.01231 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16d00661-5cce-3825-813e-028d4492f2ad | -7.24559 | -44.94178 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dbc014f2-5c3a-3103-8285-6f416b0858b3 | -7.24294 | -45.00776 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8be5f029-2755-37af-a2e2-90f0a5bcb52c | -7.24232 | -45.01181 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8abd20b1-eca8-3625-9a6b-34ff92621aea | -7.24171 | -45.01587 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cab16a1-4f1b-3446-914f-356ab20ee1ce | -7.24038 | -45.04873 | 2024-09-30 04:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08487a26-5cda-3dcc-b349-a04d577a1dd6 | -7.23875 | -45.01132 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84d82d20-a984-3ae9-b43d-2b1e7a2ac615 | -7.23814 | -45.01537 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 086fe5ee-8624-301a-983a-d1bf81d351c2 | -7.2362 | -45.05223 | 2024-09-30 04:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65e9312e-f833-3fab-906c-3c68fd99adc6 | -3.0003 | -44.93692 | 2024-09-30 04:29:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2974c4ac-733d-33be-bf19-ab8bf62886e7 | -2.99686 | -44.93639 | 2024-09-30 04:29:00 | NOAA-20 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cf2e239-1868-383b-bada-da4b5557c867 | -2.61822 | -45.54276 | 2024-09-30 04:29:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc5adc59-d775-3d5a-85ee-91f896954202 | -2.32876 | -45.51998 | 2024-09-30 04:29:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5ccaf00-5722-36f3-91fd-429f68bed4a6 | -2.32821 | -45.52354 | 2024-09-30 04:29:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca6aafc7-414b-3d1a-be8c-50b49d07d448 | -3.59244 | -44.54837 | 2024-09-30 04:29:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4d89625-3055-3939-88b5-aae70430fd40 | -3.59185 | -44.55226 | 2024-09-30 04:29:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b60fafa4-c491-305f-95cd-e052a5d6e2ad | -3.58894 | -44.54784 | 2024-09-30 04:29:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5e41a58-9c83-3874-9150-adec9ac96db4 | -3.58842 | -44.52776 | 2024-09-30 04:29:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5945484c-53f6-33e2-b7d8-6ecf9fa7fc81 | -3.58431 | -44.53113 | 2024-09-30 04:29:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b4e484a-cab9-36d0-a932-b798f5459e81 | -3.58371 | -44.53505 | 2024-09-30 04:29:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 3b562349-3609-37dc-90e8-872aa44f0aab | -3.58311 | -44.53896 | 2024-09-30 04:29:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 63d70f35-f76b-3b90-ae67-842e7d81f9a2 | -3.5814 | -44.52666 | 2024-09-30 04:29:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5dbd5413-0c43-367b-b264-cf0101570fbf | -3.5808 | -44.53059 | 2024-09-30 04:29:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6f184ca6-7bc2-3072-b01e-907ec30308ee | -3.5802 | -44.5345 | 2024-09-30 04:29:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5cc38060-4d36-3510-aff3-ad8d5e020a20 | -3.57961 | -44.53841 | 2024-09-30 04:29:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18e66946-eea3-3ba3-904e-9ead19600aa7 | -3.57901 | -44.54233 | 2024-09-30 04:29:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 445c2e68-7635-3b30-9621-8486b1b24d7b | -3.5761 | -44.53788 | 2024-09-30 04:29:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01e65124-eac7-3f10-ad83-0ad3bcf025d5 | -3.5755 | -44.5418 | 2024-09-30 04:29:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ad2a1d9-ae31-3996-8ae4-e60742e3f1e0 | -4.70751 | -45.8799 | 2024-09-30 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55b86841-8e7f-310f-b887-783d208c3e95 | -4.70413 | -45.87938 | 2024-09-30 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c3711e5-cc16-38e9-bdf8-a18edec139d2 | -4.43879 | -46.14516 | 2024-09-30 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae10a97c-b147-3023-ae19-eba2fc209ed3 | -4.43545 | -46.14463 | 2024-09-30 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8dc7766f-7634-39bb-aeab-b93c24ab412d | -5.90623 | -45.98713 | 2024-09-30 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c483a7c7-61aa-357b-9a73-ca591a5b55ed | -5.90566 | -45.99078 | 2024-09-30 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a92f1800-c9f9-3708-86ef-ff73042d302b | -5.26897 | -46.21832 | 2024-09-30 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88eefc8f-cf08-37da-88f0-66d31b73146f | -5.09366 | -46.16937 | 2024-09-30 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b90f7ba6-eba0-3aa5-bc50-d62bb343732a | -5.09311 | -46.17292 | 2024-09-30 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00bd3317-3caf-3ce9-8c91-11e1f777f520 | -5.71949 | -46.44696 | 2024-09-30 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e44bc15c-f9c3-3c9c-b2c3-0cd11e4e3261 | -5.26561 | -46.21781 | 2024-09-30 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 395e7306-6431-3f2d-9ab3-417a5bdec625 | -7.14413 | -45.72697 | 2024-09-30 04:29:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7da8c43e-6bc0-3af6-894e-87ce7acee181 | -7.03424 | -45.36071 | 2024-09-30 04:29:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5574efa-ec2e-3400-9d5c-567d9e060b29 | -7.03365 | -45.36463 | 2024-09-30 04:29:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57b96e35-27c2-3455-867d-0666f2535f7b | -7.02372 | -45.33523 | 2024-09-30 04:29:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63345ed8-5ccf-3d8d-8eac-aee4249fe9f1 | -7.37764 | -46.78498 | 2024-09-30 04:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86e66e32-0a2a-3b13-96a2-06c448b9439d | -1.73091 | -47.12634 | 2024-09-30 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d7ab7401-293a-3abb-bd06-6bd9420a32eb | -1.7276 | -47.12582 | 2024-09-30 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 75690cfd-401c-352a-ac7f-f89f90e2a90d | -1.65232 | -46.15605 | 2024-09-30 04:29:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6400bd7-2fb6-388a-8c51-6e1cf2b50524 | -1.65178 | -46.1595 | 2024-09-30 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9378ffb-7e5f-3c7a-bf6d-4ae0dbf8eb2d | -1.64955 | -46.15209 | 2024-09-30 04:29:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a89899f-2ff5-3b1c-a04c-6c70a5f43ac9 | -1.64901 | -46.15554 | 2024-09-30 04:29:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42d2e77d-95f0-3e95-b511-e05fd9bcb7d7 | -1.64624 | -46.15157 | 2024-09-30 04:29:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 676c45c7-f60a-3e85-bb95-357f344e76bf | -2.73465 | -46.72705 | 2024-09-30 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d676eca2-893f-3583-aa07-a6b804d40362 | -2.73155 | -46.78991 | 2024-09-30 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b23e3398-0b65-3213-9a25-a95dc3d2ce59 | -2.72197 | -46.72157 | 2024-09-30 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4db32316-6ae2-3e89-93af-ca047ab50ec3 | -2.72143 | -46.725 | 2024-09-30 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12299b84-f0a1-34e3-a40b-9f0b71c68ec6 | -2.71866 | -46.72105 | 2024-09-30 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64ce1dbf-f77f-335e-a59d-309b23b271c0 | -2.71812 | -46.72449 | 2024-09-30 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a7b2970-edb3-36d7-a3a1-2091b31953ab | -2.71482 | -46.72398 | 2024-09-30 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 947a175d-7e36-31b2-a497-17dbcf3bd7e0 | -2.22876 | -46.74648 | 2024-09-30 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ced6fffc-4d65-31d4-ba84-8f8c0130b448 | -2.22822 | -46.74991 | 2024-09-30 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abe3c00e-b37b-3f63-8f05-39ac330b406b | -2.22653 | -46.7391 | 2024-09-30 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca8f05ae-6f43-3f3c-9bb8-8051ffc7bd6a | -2.22599 | -46.74253 | 2024-09-30 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67c92c5f-4a5c-36fc-ba9e-331d3d302aa0 | -2.22492 | -46.74939 | 2024-09-30 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4db0394-e349-3b03-a1e9-308e1221588d | -2.22438 | -46.75283 | 2024-09-30 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26fc840f-e04a-3641-97b4-44e0f8e6b4a7 | -2.22269 | -46.74202 | 2024-09-30 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c2e2f6e-1dc7-3289-b1c1-2ab91ec3844d | -2.20286 | -46.73894 | 2024-09-30 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1911a23c-e12a-3432-933a-6e99de5cf4bf | -4.65362 | -47.44382 | 2024-09-30 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4903f4ad-0704-36c1-ad99-8e4098c47776 | -4.65032 | -47.44331 | 2024-09-30 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 223d1309-f9d1-3d27-bcd9-3b4a88d522cc | -4.60779 | -46.65201 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c1b9724-d39f-33b4-af56-40f53e326646 | -4.60447 | -46.65149 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5523a7d7-7090-3ca4-aee0-9f4743730f0f | -4.37883 | -47.61237 | 2024-09-30 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02cdf18c-a751-34fb-b410-0d7bfc4ccad0 | -4.17775 | -46.86105 | 2024-09-30 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b9a3868-7eda-3637-8f85-94f427ddf244 | -4.17444 | -46.86055 | 2024-09-30 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eab13077-ae16-321f-988d-b0f6908cdfe6 | -4.60888 | -46.64505 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e05ebb77-8cec-3f6f-89c0-584f9f1f3e89 | -4.60833 | -46.64853 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58c7c236-581a-32bb-bf6d-efc0e74604d8 | -4.60502 | -46.648 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a079777-872b-340c-8c73-47fd7a428c7c | -4.60279 | -46.64053 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b9fbc54-0b61-3eab-bf63-b0b4ca45e99c | -4.60224 | -46.64401 | 2024-09-30 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cab30e0-bc55-3934-9d0a-02489e5af0f6 | -4.17828 | -46.85761 | 2024-09-30 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d337c3ae-c6ef-3c14-b798-1cdc7f61bf01 | -4.17498 | -46.85709 | 2024-09-30 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 507f2f07-5d2d-37e1-beb9-7708f9fd034d | -3.91445 | -46.43742 | 2024-09-30 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README28.md)
