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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbd8eefa-bd47-3882-b226-6d5a7d479e51 | -6.64305 | -48.80802 | 2025-10-18 04:49:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db27d4fd-5af9-3843-91f9-b0e9440bba02 | -5.21448 | -45.5198 | 2025-10-18 04:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e16f3810-5027-371d-a991-513957191405 | -2.95392 | -49.33499 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7ab8a1f8-10cf-315f-9aeb-d0240ad67864 | -5.53416 | -51.39038 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb89358b-0869-3eda-80d9-907b797129ba | -8.54 | -50.07841 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad5ade35-7b4c-3349-af02-26b5d208b94d | -7.48125 | -47.02777 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5bcf7cf-709f-3cb1-91fe-ae5159f1bd86 | -3.8512 | -41.58438 | 2025-10-18 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c88f27cf-08d5-3a96-848e-662cc9b35a4f | -3.14808 | -50.25102 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7c8fb89b-417b-31b0-b580-000a95ebc799 | -8.33631 | -49.96746 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b33962f-e166-3244-9c3b-9d7517c13869 | -5.98724 | -42.80116 | 2025-10-18 04:49:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ecf05636-ef67-3d42-9499-a3cc7be6750e | -6.83862 | -42.42521 | 2025-10-18 04:49:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7c4cddcd-f4c7-3dca-9e18-21c47b6014fc | -4.07564 | -43.39542 | 2025-10-18 04:49:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68693076-96a0-3c44-9139-78e875d0e2ca | -7.83182 | -44.12475 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9aced332-daa8-366a-ad5a-59661c760064 | -9.1946 | -46.87211 | 2025-10-18 04:49:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bde8db40-b5ce-367b-81fd-3e28375ef0a3 | -8.54355 | -50.07894 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e966d8d-e2e2-32dc-8060-dd7bfeb9cb02 | -4.45845 | -43.23327 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 68ab797f-dfb7-3a58-b468-a80df9b54303 | -6.5348 | -55.04661 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64027f4d-5bae-32c2-8a0a-26b8e7634252 | -6.59266 | -44.15912 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a16ac38-3ae5-3511-9023-5b459dacbb48 | -3.59037 | -43.04659 | 2025-10-18 04:49:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fc282e8-9a40-3389-a5d2-a776a8c88eb5 | -6.58675 | -44.16441 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fd32c87-3643-3fab-959e-dc25c44e040a | -3.23702 | -42.07552 | 2025-10-18 04:49:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7c49ad6e-74d8-313c-947e-f4d7b0e58113 | -2.11522 | -56.88767 | 2025-10-18 04:49:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f920c93c-b19f-39e0-a865-5dd356f42f6d | -8.82201 | -50.05185 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a76efe1-089e-3aeb-959d-75596fdf09f5 | -2.11936 | -56.8883 | 2025-10-18 04:49:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83a0aca1-ed5c-3de2-9e65-3cef6c1222f6 | -6.5839 | -48.77204 | 2025-10-18 04:49:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67ae23f5-5eaa-3808-88a6-60848ce951ae | -3.53963 | -49.44942 | 2025-10-18 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba713c35-3c1b-38dd-be54-9f262294f0bb | -8.7173 | -49.59926 | 2025-10-18 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd17aacc-5c07-38f8-a73d-1918d3e88db2 | -6.37636 | -44.70893 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 053ff56e-d183-3a71-a385-c0190d03e6b8 | -6.7675 | -50.36106 | 2025-10-18 04:49:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aaf3a9e4-6e30-3fc2-a807-32cec271d8cc | -7.76167 | -42.48233 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 752f3f4e-6a81-34b2-93a3-11d062adf5f4 | -9.77913 | -43.86827 | 2025-10-18 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 983238f9-a6d9-3c57-9973-5b015993cfc5 | -5.56009 | -46.37836 | 2025-10-18 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbdef0a5-f46c-3d51-b7e0-c82fa154296c | -9.12684 | -46.62104 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72980374-f215-32ee-b174-49c030156c54 | -7.36283 | -44.23207 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 028ed48e-12e1-3a3d-b35a-f58920d7bf3e | -7.82158 | -44.12292 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bbfbe0b-685c-3bb6-8f14-cba2d50c0c2c | -3.79705 | -52.175 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 710464f6-17dd-3ae8-9428-9ab7d7ad5c5e | -6.20857 | -44.68097 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2de49af-7e5b-33a9-9b78-f07ac7523531 | -1.18031 | -54.21289 | 2025-10-18 04:49:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f13b2dfc-0678-3f2a-9b4b-7099eafa9b59 | -6.60969 | -44.21752 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6faf99fd-3353-33fb-8206-6a5748966678 | -5.37567 | -46.00328 | 2025-10-18 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa15c763-7475-36c0-b974-bbe7047de0ca | -8.2372 | -44.01358 | 2025-10-18 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb08a963-475d-3c99-91d6-ea92dd5415a2 | -6.23517 | -44.15761 | 2025-10-18 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8ef863e-cc1e-3d18-9b97-9c9071e39bcc | -9.7228 | -44.54581 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 376e1410-846b-3a0a-a1ea-0f4c6abbacbb | -5.92501 | -45.43824 | 2025-10-18 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 64ad2c13-1f62-3ffe-a547-356459be40ed | -2.22694 | -48.37207 | 2025-10-18 04:49:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 758f6f19-e29d-322c-81b0-568a0b186ddc | -8.82534 | -49.67476 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab278910-d8f5-3771-8ab8-292f27673536 | -3.86602 | -51.41419 | 2025-10-18 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff4ce303-4b7a-3a48-b300-b762dec88515 | -7.1675 | -42.36325 | 2025-10-18 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3b089e56-53c4-37b4-b8e0-2f024066f9dd | -8.35933 | -46.24733 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97b2b428-4f81-3386-a017-50eb01b78a20 | -2.94023 | -54.17435 | 2025-10-18 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e827ab5-18c2-3d5c-a590-72576a7a030c | -3.80215 | -51.64769 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d5ab93dd-3492-3b55-aefd-57e89e632f12 | -8.35589 | -46.22294 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9759ff18-edbd-3889-a016-c9bfd4a7bac5 | -7.79701 | -54.93853 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1579346e-e727-302c-a76e-7175b5fbca41 | -8.16201 | -43.30196 | 2025-10-18 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b319543-dd37-3420-a2e2-1dcf3dba1323 | -5.20818 | -46.19254 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5b251a1-a7a8-31b9-9c1a-9fb8c677ea0b | -4.93572 | -49.76761 | 2025-10-18 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24e4bddd-7157-3b44-8efa-45674c6c3411 | -8.9512 | -49.01942 | 2025-10-18 04:49:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fbee942-39a6-3ec7-99c6-e0a25bdd0d72 | -8.779 | -47.9273 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e0ccb35-45f6-3b84-8912-77200b24995a | -6.30787 | -45.5437 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5347eb17-d698-3d36-a1c0-12a700d946c7 | -2.86737 | -50.74315 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 190848e6-6d1d-3723-8940-f06f4b7bec21 | -5.9321 | -51.55975 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c48101a-598e-3a2c-86f9-6a814880991f | -6.95379 | -44.86962 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ab39c3a-4939-3f02-9fa9-477d443e5f9b | -4.45371 | -43.22934 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d09c1708-c470-38f0-8e27-0e65e599b711 | -6.13477 | -44.21533 | 2025-10-18 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c06cf891-5c0f-3db2-9520-c16c3724a439 | -3.06462 | -43.21809 | 2025-10-18 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df2bc50d-5c3e-3825-b1e8-4cd521998cc1 | -4.56755 | -48.40181 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7f20a82-7699-3b84-af1d-94dd36ee855a | -8.16627 | -47.03861 | 2025-10-18 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99280afe-98b7-375a-9989-16f8294d0a6e | -4.30646 | -48.06652 | 2025-10-18 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26663f2b-5fde-3fe1-a3e0-d91c063626a5 | -6.61229 | -43.61118 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7aa7c310-21f7-3b05-bb38-148d44d22bbe | -8.22307 | -43.3116 | 2025-10-18 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0ad1b816-bcdf-32b3-88fa-d73c169d9a36 | -2.56815 | -49.1137 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f696703c-0819-35ee-951a-ae5cece134c2 | -5.24777 | -50.96389 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cfb9051-bdb1-3f8c-a66a-e86c9483f3e3 | -8.61116 | -40.19842 | 2025-10-18 04:49:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 61cf8a4c-591e-3a50-9211-21a7be5ef5f1 | -8.88087 | -47.97101 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b985201-820b-3568-9a76-a5d72baa5dd3 | -8.81316 | -49.68161 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51aa1a11-9351-3385-8fea-7c853fe58bb4 | -5.89141 | -43.92138 | 2025-10-18 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 489f0f03-cb1d-319c-a797-b302851880bb | -8.1705 | -47.0393 | 2025-10-18 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6cfb449-9963-3923-a0a1-61733fba80a1 | -9.71877 | -44.57619 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0f4dc64-65f4-3c7d-8927-f73e54aff0f3 | -2.57164 | -49.11423 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17135c3d-fe57-3d70-9cc9-974cab9c1561 | -5.55656 | -44.14417 | 2025-10-18 04:49:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e28b48a-6359-3cc9-b8e9-ff81a90d2690 | -6.35152 | -45.75536 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9cf278fe-f22e-3129-930b-345872a4364b | -3.07038 | -49.21508 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad89b84a-a757-3f97-8240-6c788a44c537 | -6.94929 | -44.87204 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da950580-a2f8-31fc-bcd5-e7bd36b0ee4b | -8.20024 | -43.30761 | 2025-10-18 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fa387237-770f-3901-9af8-ab1b9571a23c | -2.87732 | -50.72324 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffd894d6-92e2-3c3f-8253-eac76f840b8a | -8.88888 | -50.58959 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1603405b-43af-397e-9db0-d6bf579bd19f | -3.407 | -46.90221 | 2025-10-18 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d12040a-1b42-3f01-b912-4e3e74de0e00 | -7.89386 | -55.42432 | 2025-10-18 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8e3fe01-6c44-3bfd-a043-f236a626b60a | -9.55496 | -47.77935 | 2025-10-18 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8100cc80-6779-3ee4-8c8e-fe24e9795c4b | -7.92761 | -44.13153 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cea38f69-f7be-3ddb-8cef-33bf8b00eb21 | -6.30778 | -45.54152 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f86d77cb-aa10-39e6-ba02-41e9050e52ca | -4.40769 | -44.36629 | 2025-10-18 04:49:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| faffae09-676c-3d3e-83be-62ae9db5866b | -9.66947 | -44.55363 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69052023-4cb1-3fb9-941c-65cdf936a384 | -7.58189 | -44.98519 | 2025-10-18 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f54a980e-ec66-3131-8d1d-7dc952834efa | -4.21852 | -48.35896 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5fce71a-a143-3411-9c06-9895a5660333 | -2.86181 | -50.73514 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 276e3e5b-6e5f-306a-bcb7-9a3999df0d88 | -6.89126 | -45.45468 | 2025-10-18 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1e0ec98f-361d-3c58-a001-0eac2b28e2bb | -8.3873 | -46.22759 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a4d69e4-6bf2-3958-9d11-4d78ae86274a | -3.84719 | -41.57173 | 2025-10-18 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f39cb1cc-2a64-3da1-b7e0-08b0f866c2c7 | -4.69 | -48.62537 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README71.md)
