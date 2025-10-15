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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71fe27ce-b0bd-3a66-b143-9b24a4319ff5 | -3.56268 | -43.50854 | 2025-10-15 04:04:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ab2dee2-a44d-3c62-9517-cc1ba7ed0293 | 1.07474 | -51.04506 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8e7b0f1-a48c-366c-8a25-7e3fe2569dfe | -2.53095 | -47.81022 | 2025-10-15 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52c41f9e-c768-3aee-85d5-91b648686429 | -3.05712 | -44.47371 | 2025-10-15 04:04:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd9d2e9d-1621-378f-a5ca-d5ff17133cb7 | 1.08552 | -51.22525 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64b01e37-9a8c-32ad-b52f-5bc2b0f50700 | -2.29997 | -48.57709 | 2025-10-15 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07c19367-b1cd-3b34-a0c5-b7cbe9b8f5cf | -2.77702 | -45.59879 | 2025-10-15 04:04:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8aa317ae-a4c8-3b81-96fb-dfdf52f60c1d | -2.43981 | -49.3759 | 2025-10-15 04:04:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0331feb-3b87-380b-aac8-79db91b19552 | -2.29951 | -48.57999 | 2025-10-15 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7cde44d-0926-3d96-ab30-9d056d8fbe78 | -3.72528 | -40.37286 | 2025-10-15 04:04:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dd34794e-e907-388c-a59c-a4109d827032 | 1.33303 | -50.72242 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fd12fd7-65ec-3330-a61a-688028d8eab9 | -2.6281 | -48.05744 | 2025-10-15 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 541de660-a5de-3e23-a550-bd07e7793471 | 1.01279 | -51.08648 | 2025-10-15 04:04:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab53cc12-131b-31e9-a0aa-b7d98961b984 | -2.44508 | -49.37678 | 2025-10-15 04:04:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c48072c0-797e-35a7-aac9-178f858d74aa | 1.08094 | -51.04404 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cf5f44c-0691-3dc4-bbb8-324aebfe6c00 | -2.62819 | -48.06136 | 2025-10-15 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3182f4f-068e-3d89-b1ff-8fd4e0284e0e | 1.08475 | -51.22034 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8af73878-f6e9-3301-a0c9-cce2a78194b6 | -2.24609 | -47.87415 | 2025-10-15 04:04:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0ba4a409-b8ff-37fc-9f28-d49d1d064ce9 | -2.24132 | -47.87336 | 2025-10-15 04:04:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9f31619a-1b62-3bec-b352-8134a1cedafd | -2.54995 | -48.40399 | 2025-10-15 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41301c46-83e0-3bd0-a23d-4c7215f45f14 | 1.33521 | -50.73633 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ca07c11-9cbd-3e31-adb7-0a51092a85ca | 1.07654 | -51.04637 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a25a4f89-a336-3a80-888c-d4bb63935f3e | -3.05262 | -44.47765 | 2025-10-15 04:04:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e5dc267-2980-3863-a4f2-714a0ddb1c3d | 1.31473 | -50.72533 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 260ee05e-83b9-309d-91d2-caed1e73c1e5 | -3.04728 | -44.46278 | 2025-10-15 04:04:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2adeb52c-84cd-34be-a7ef-5a24a1d5e4fa | -2.04875 | -48.80043 | 2025-10-15 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f7aae06-6618-3f80-8ae6-9ebb59755ebd | -3.05105 | -44.46339 | 2025-10-15 04:04:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 897b0f1c-e8fb-3830-a9ac-7a41243e4b1d | -3.36542 | -40.63024 | 2025-10-15 04:04:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6a9b8468-555f-3a62-aed3-4a8e2604255b | -3.36872 | -40.63075 | 2025-10-15 04:04:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 667a8916-4d07-3e24-81fd-5cc0e8bc077c | -2.53183 | -48.48118 | 2025-10-15 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10beb833-d23c-34fe-8e79-c35c4619a5c2 | -5.23753 | -43.17879 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff7cda5d-6195-3ab8-9801-fefdae55a845 | -5.185 | -46.17588 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 038380a6-8b85-31ce-b496-d18b93563740 | -5.42525 | -44.30299 | 2025-10-15 04:06:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bae24fe9-27f3-3f56-9f4a-e68950428be8 | -5.62533 | -42.68352 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 627e3939-a41d-3487-b7fb-579723bf3e45 | -5.99367 | -42.86065 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 12a4d693-0fe7-3262-99ae-005d25045786 | -5.61759 | -48.26843 | 2025-10-15 04:06:00 | NOAA-20 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb863e87-eda5-32e9-86a7-4feb2c631454 | -5.8663 | -43.8457 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbb42578-4249-3ec2-a234-84379eb65adf | -5.1943 | -46.14434 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 477ffbc2-470e-311a-af3f-777c5ec3f99e | -5.58506 | -44.74438 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1713b8c3-403d-354c-951f-046f5d84b50a | -7.65524 | -42.82197 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e011f91b-29b5-34d0-9482-a42dbb937543 | -5.68599 | -44.35574 | 2025-10-15 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e0411e4-13a9-3ac6-9b78-b1cdc0335aee | -5.97506 | -42.93275 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 55c6fb2b-0792-35d3-bbdb-cd36cbf5f280 | -5.41526 | -44.22868 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 961c3fdf-9527-31f8-a243-80b9aa0f89f7 | -2.95089 | -49.34431 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cd2734a-c8e0-3ced-aad6-0aae9b1bc3fd | -5.50355 | -43.78115 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 336749ca-55ae-37e0-9a66-65badb503ad8 | -5.42675 | -44.2263 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0e7b7e4c-b3c6-3f82-a1ec-b971154291ec | -6.14072 | -41.77268 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 34ca6d96-cf88-3848-bb34-4d4d2fc4a44d | -7.29335 | -41.96018 | 2025-10-15 04:06:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2ed32cfb-23bd-31d4-bc15-d9e79b3f5d26 | -6.53142 | -42.1996 | 2025-10-15 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 50f68712-f91f-351e-afcb-003384a74f66 | -6.77407 | -42.12741 | 2025-10-15 04:06:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b1b613e0-5ecc-3533-9121-3340c25c76dc | -5.97143 | -42.80479 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 94e4dd93-8550-38fa-85b7-820d91fe9024 | -5.19893 | -46.1414 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c90dd9f7-6781-304f-9a32-8574c11dbd47 | -8.24202 | -43.33818 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e7ac2d25-b97d-32bb-ad87-b79e0ac12c82 | -4.14429 | -41.65595 | 2025-10-15 04:06:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e50cbf5f-3e79-3197-8e55-9c798c6ba2f5 | -6.26477 | -44.34206 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f16fbc4-2b39-3227-a996-31fccee18f3b | -8.45895 | -44.19026 | 2025-10-15 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e95d833b-bd07-328c-ac04-3a279416dd24 | -6.23128 | -44.16359 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65da5778-47a4-3c1f-9367-7739484ab709 | -6.45884 | -41.84444 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 948260fe-d93a-3f65-b2a1-aae0d2f89b6a | -7.13663 | -42.49503 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f0e4161e-8914-3a76-bf9b-aa4d8607eac5 | -5.31721 | -42.90078 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8fabd09b-6d0b-337e-9e5d-5656b3f406f6 | -4.63756 | -42.52386 | 2025-10-15 04:06:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fb4da14f-4694-3c23-aa43-9fc5308ba5b2 | -5.97601 | -42.798 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7e084d98-11d2-31a6-abbf-a5028d85d925 | -4.91664 | -41.54257 | 2025-10-15 04:06:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a286a7fa-ac65-38d6-932f-b3e2129001ab | -5.41565 | -44.21817 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5d05b9e-3d5f-343d-948e-41474bd65d9e | -3.06838 | -49.51279 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9db35399-52fb-3ef7-a9fe-e78045431585 | -7.83425 | -44.51144 | 2025-10-15 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed7ee741-2c28-3fac-b4b2-b59f7b410826 | -5.99027 | -42.86013 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e41043ff-e957-38e5-a26a-a4c442cbce89 | -6.77683 | -42.13142 | 2025-10-15 04:06:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b7ebcce7-eeaa-351f-b1c3-5629037d07e0 | -4.85765 | -43.20532 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2d02de16-adb6-3ebf-9761-c056e3520109 | -6.05946 | -41.89853 | 2025-10-15 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7a6235ab-a5d7-3067-a524-0c91c68c2fa5 | -8.27111 | -43.37984 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cc804b65-814c-3086-99ac-cfdb5b2547b3 | -4.83524 | -45.65856 | 2025-10-15 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e498d156-7694-3db8-8299-c543c8df4910 | -6.4605 | -41.85538 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d6f7ae4-92ff-35e9-bd52-93cb9fff327b | -3.73174 | -44.14062 | 2025-10-15 04:06:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dafe1123-fae4-3492-8aec-2855c471de1e | -4.23086 | -44.43552 | 2025-10-15 04:06:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a34fe70d-5f82-36c0-9319-b4a1e82739b0 | -6.54795 | -43.931 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d312ebe3-778d-3396-8574-0214c6e44756 | -4.14873 | -41.64951 | 2025-10-15 04:06:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc180606-dcea-3ec3-8984-32c4e9c63d65 | -8.73189 | -43.86475 | 2025-10-15 04:06:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2f5cfc8-f922-3f5c-ab1f-9867d6225958 | -6.44648 | -43.81826 | 2025-10-15 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0b74f6ed-bdd4-36f3-9f33-90a663bb9784 | -2.94749 | -49.33556 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 767f20ae-466b-3623-94d2-d3f817c5ce51 | -4.59424 | -47.03198 | 2025-10-15 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08550b82-4fa4-3acd-a129-e9a598d7646f | -5.88067 | -42.77879 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fbd1eb5f-5937-3bb8-9438-fe28cf3ad939 | -6.23484 | -44.16417 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 02d586ca-8cd1-3e8c-be19-f557b9ed21cd | -7.79546 | -42.39138 | 2025-10-15 04:06:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8c1e6420-f879-37f5-9a8a-316d003207be | -8.2169 | -44.05603 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 213a9913-a9df-36b0-a384-a0b2de4dcb7b | -3.52815 | -50.31378 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82d5eee4-2c84-3067-a0e7-f4ff7ec19e5d | -5.99372 | -44.08574 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1eac456b-8a82-3ac5-a3d5-1f59c88e52b6 | -4.42364 | -47.75387 | 2025-10-15 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c7b9223-33e2-3c2a-bfe9-2fd8277efdf7 | -3.07421 | -49.51035 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76e037dc-bf60-3d29-a96c-96449376ad97 | -4.83207 | -42.77552 | 2025-10-15 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 0fe8c65c-2ebb-3b8a-a7dd-1f00c8a3badc | -6.43801 | -42.53244 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a023dcaa-b5db-3e20-93b3-27d95f300167 | -4.29255 | -41.6867 | 2025-10-15 04:06:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 09a0107a-4d30-37e9-8202-7f9dd20b2117 | -6.35473 | -42.6656 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 88548ec9-f283-32d8-bcc2-451725415516 | -6.52478 | -42.19847 | 2025-10-15 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cc0a7538-e233-3b4e-8c9a-9348724c8141 | -3.60802 | -48.92586 | 2025-10-15 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb73a33b-2862-379e-acd6-47d1b466fe13 | -2.81178 | -49.21027 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| aeaf9cb7-f5f3-34d8-805d-e2be59fcedac | -4.14774 | -43.13108 | 2025-10-15 04:06:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8831755e-b30d-3ca2-80a2-72e1e1a966e2 | -5.04728 | -42.85503 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9bf3e04-f4b6-397b-b424-ad82f2ce68fc | -5.98231 | -42.86636 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6da9b5f9-e2b0-3f8c-8bd0-eafb09330708 | -6.53691 | -41.48066 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README22.md)
