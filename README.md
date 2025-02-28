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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5261d9af-0ac9-34a3-bec0-7c1c13f2747f | -10.3123 | -36.4607 | 2025-02-28 00:10:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 111.5 |
| 0397f6aa-28d4-313b-82d3-376ce8811f28 | -10.3118 | -36.4876 | 2025-02-28 00:10:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 95.0 |
| b848f944-f9e3-3b40-ba51-02402369d050 | -22.95904 | -42.87945 | 2025-02-28 00:30:00 | TERRA_M-M | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 1a3a1f4e-2fe1-3e38-a3a0-910d05fb2d7b | -20.7753 | -44.03777 | 2025-02-28 00:32:00 | TERRA_M-M | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f7c8cc92-578d-31e3-9826-9082bb23d52d | -13.49636 | -43.61311 | 2025-02-28 00:32:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5f47dca9-54e8-3cf1-98c4-d476905026c2 | -18.58473 | -48.28621 | 2025-02-28 00:32:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 3c8df10b-99e7-36ae-9914-23a3a7381ec9 | -21.61061 | -48.47895 | 2025-02-28 00:32:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 976a1b69-aa46-3099-a9af-efa25274c7c9 | -7.06179 | -44.38617 | 2025-02-28 00:34:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6baa79f8-6a83-3b32-80cb-aedc0e375c7a | -9.80819 | -38.09611 | 2025-02-28 00:34:00 | TERRA_M-M | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| cc079e30-2045-310d-b438-63cf1ad7849c | -7.0529 | -44.38748 | 2025-02-28 00:34:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7d8ae7b0-29db-3fef-aadf-69ba2b6083a2 | -7.81763 | -44.18528 | 2025-02-28 00:34:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b08a6c7d-d28e-3677-927a-1e96f83f793e | 2.1192 | -61.8004 | 2025-02-28 00:42:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 09a6f3cf-bdfc-301f-9fda-eb539edf1371 | -21.6199 | -48.460602 | 2025-02-28 00:42:00 | METOP-B | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0a1f751f-85bc-3bca-a469-34eb03fbafc7 | -21.167601 | -48.561199 | 2025-02-28 00:42:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49091255-dc0d-30b0-855d-23eea1e488ef | 2.1066 | -61.810398 | 2025-02-28 00:42:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cea40637-0d0b-3889-914c-a426a5460574 | -23.2117 | -50.798698 | 2025-02-28 00:42:00 | METOP-B | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c381687-0911-31b9-b65f-32be5392c80c | -21.6101 | -48.4631 | 2025-02-28 00:42:00 | METOP-B | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 69f3e80c-8634-3f2d-b34d-157be1ad54e3 | -21.1658 | -48.553398 | 2025-02-28 00:42:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1450326e-4cea-31a2-ac03-411a1749b95b | 0.8289 | -59.936798 | 2025-02-28 00:42:00 | METOP-B | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 36a88d49-e920-3c84-9e18-f0b74255c50f | -23.2019 | -50.801102 | 2025-02-28 00:42:00 | METOP-B | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| caf7dad3-1caf-3914-8d25-00febabdd157 | -23.203501 | -50.808601 | 2025-02-28 00:42:00 | METOP-B | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 45b24a72-c660-3479-b1e6-7d811c75da86 | 2.1164 | -61.812599 | 2025-02-28 00:42:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1591a24b-f7c8-35a7-9a2a-cd659dd6c460 | 2.1094 | -61.798199 | 2025-02-28 00:42:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7da1b223-3d69-360c-b47a-59c2d6d20642 | -22.950199 | -42.868698 | 2025-02-28 00:42:00 | METOP-B | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 21d8997b-e44e-3726-9926-ad614563a7ea | 2.8054 | -60.812599 | 2025-02-28 01:35:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4fb3ee7f-83d4-3ccf-a138-03d425c01b8e | 2.1032 | -61.819801 | 2025-02-28 01:35:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7db5aa34-3780-31f7-94bc-7abdb8d9ac32 | 2.113 | -61.821999 | 2025-02-28 01:35:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6fad4669-1424-3a3b-be95-dc56e97f79b4 | 2.105 | -61.812 | 2025-02-28 01:35:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2148a239-5b42-31a2-b6bc-47940a6c8ac4 | 2.8074 | -60.803799 | 2025-02-28 01:35:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee41276-a409-39c7-8510-72b13611e6cf | 2.1014 | -61.827499 | 2025-02-28 01:35:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7894a5d6-55ac-3b39-9130-2f138275af19 | -22.67339 | -42.85836 | 2025-02-28 03:17:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0f50d002-2160-386d-8dd5-4eceb899724b | -22.67447 | -42.85377 | 2025-02-28 03:17:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 64bf97e1-c94b-37e7-a5a6-c3476930f7d7 | -22.95722 | -42.86381 | 2025-02-28 03:17:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| a6b0f61a-80eb-36ba-8775-30b28451a82e | -22.95834 | -42.86594 | 2025-02-28 03:17:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 3945926f-a6da-3360-9f5e-6cdf7c42b712 | -7.05975 | -44.38237 | 2025-02-28 03:36:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 537e03a2-23b8-3772-907b-be227a40a3da | -7.05463 | -44.37724 | 2025-02-28 03:36:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93982087-ffe3-360e-9aa5-17f5453dedf9 | -7.47677 | -34.84296 | 2025-02-28 03:36:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 82e2f5a8-00b5-352b-b17d-6d3ebf4144c0 | -6.54858 | -44.48704 | 2025-02-28 03:36:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e8f7962-e48c-3e58-a80a-297a4c04abd8 | -6.54933 | -44.48276 | 2025-02-28 03:36:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b74c2d8c-218c-3ca4-a482-d10d413a9387 | -6.97067 | -43.01308 | 2025-02-28 03:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| ab9ca3ea-41c0-3f46-9170-5aa67f67fb3d | -7.81581 | -44.18547 | 2025-02-28 03:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20b8d1c5-d7d7-30a5-a215-50bcb1537f01 | -6.96531 | -43.0121 | 2025-02-28 03:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3b10bd1c-b1d1-338d-8a11-e815238988f0 | -7.81011 | -44.18438 | 2025-02-28 03:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7844092-a0ae-35cf-95b4-844a803ec4cb | -7.05903 | -44.38638 | 2025-02-28 03:36:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a059fd9-31a4-333a-8cab-adfc0a9c9646 | -7.0532 | -44.38517 | 2025-02-28 03:36:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b89c4a8-66ae-3d66-b7b9-aabe417d1529 | -11.87794 | -44.38194 | 2025-02-28 03:38:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6962ad8c-281e-3e8a-ae23-fb1af1605330 | -14.15453 | -41.95856 | 2025-02-28 03:38:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| afd6db95-355e-3a85-8154-9c6d3e1e3936 | -15.37636 | -43.71917 | 2025-02-28 03:38:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2a0ce85a-e544-3c28-a0bf-1177fee3c47d | -10.71546 | -42.33457 | 2025-02-28 03:38:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 11e2c52e-4d95-3d9d-973d-815aec387b46 | -22.6774 | -42.85784 | 2025-02-28 03:40:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| b6d1fa10-6f5d-3357-9dda-cb92c0d61bb3 | -22.6734 | -42.85692 | 2025-02-28 03:40:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2349ffb2-cd3b-3c72-89bb-d20ddcca400b | -19.71789 | -40.35652 | 2025-02-28 03:40:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| da0ce98b-161b-3782-8501-3b84e78353c7 | -22.96111 | -42.8616 | 2025-02-28 03:40:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9869a961-7c3b-39f7-a612-137da89e27a8 | -22.78612 | -43.75662 | 2025-02-28 03:40:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 25bcfa75-eb96-384b-a058-9c9abc90a587 | -20.85499 | -41.07796 | 2025-02-28 03:40:00 | NPP-375D | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 63c01cd1-cdf0-3736-8373-dc6b0919a9cc | -21.05177 | -47.78239 | 2025-02-28 03:40:00 | NPP-375D | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffbdf22b-ce50-353e-8c1b-b449b4ef45ea | -22.67812 | -42.85408 | 2025-02-28 03:40:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 008ca921-bba4-3ad0-9dcf-a781f7f0f89d | -22.7464 | -42.36811 | 2025-02-28 03:40:00 | NPP-375D | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6360be39-6e37-3b0b-9039-081f92838226 | -22.96006 | -42.8672 | 2025-02-28 03:40:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e830041a-a592-308b-9d0b-b612ecea2e69 | -22.95649 | -42.8673 | 2025-02-28 03:40:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 126a5a38-da3f-3e5d-8728-8f9dc042aa36 | -19.37835 | -46.04914 | 2025-02-28 03:40:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a6971b8-02ca-312d-bfee-d53bde4aa8d8 | -19.37956 | -46.04614 | 2025-02-28 03:40:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c20dc8fa-c38a-3553-a051-47a5b53a93c3 | -19.717 | -40.35371 | 2025-02-28 03:40:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0445d496-760d-3f3c-877e-94d51474b8a1 | -22.95758 | -42.86171 | 2025-02-28 03:40:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a4dab347-ecdb-3121-94eb-393ae20f464c | -21.61616 | -48.46679 | 2025-02-28 03:40:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97183b4b-097b-3009-b681-2be11c502fde | -21.61514 | -48.47126 | 2025-02-28 03:40:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b9cafa2f-1b56-31ab-b3c4-a74eecb1ebd0 | -19.37909 | -46.0457 | 2025-02-28 03:40:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6609bd7e-3c4f-3312-a40f-ca2f25f4a363 | -19.37445 | -46.04454 | 2025-02-28 03:40:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d0aab0c-0f26-37ea-a9e3-09d46c2c367c | -22.22705 | -42.82677 | 2025-02-28 03:40:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cfe08dbf-90ef-3abc-806a-e6442335676b | -22.8552 | -42.97911 | 2025-02-28 03:40:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 13ed017f-8aca-3c14-80e3-c30284b3d046 | -22.96157 | -42.86259 | 2025-02-28 03:40:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f76df04a-4b1f-3dd9-ac21-bf480fa5e58b | -22.78438 | -43.75848 | 2025-02-28 03:40:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b5ba436d-ecfc-3e36-833a-9b544342b1d2 | -19.71868 | -40.35203 | 2025-02-28 03:40:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9c3bf4d7-e353-3dbd-a59b-4cae80bc1b03 | -22.22307 | -42.82564 | 2025-02-28 03:40:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 04fda989-3855-3d88-8081-71aaac2b641a | -23.986 | -48.91936 | 2025-02-28 03:42:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 464f1329-eb41-3978-a0c1-0aefdea9b798 | -5.00379 | -42.93821 | 2025-02-28 03:57:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71bc8108-8144-37a1-bc2b-918c4d3c9518 | -5.0031 | -42.94244 | 2025-02-28 03:57:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d621ad18-634f-3797-817e-cd59e9f999f1 | -4.6706 | -43.26254 | 2025-02-28 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2f1229f-2eb4-3f8f-9dd2-975583b51515 | -10.50089 | -42.40716 | 2025-02-28 03:59:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b51608d9-11b3-34b2-a0ac-dcfda8c55c61 | -11.96532 | -44.66626 | 2025-02-28 03:59:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac7345d9-928d-3aec-bc82-78563c3b1df9 | -11.87812 | -44.38066 | 2025-02-28 03:59:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbd4ba57-8107-3d44-8ba8-80e95c23f25f | -11.04609 | -43.1476 | 2025-02-28 03:59:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 200e9fcf-f7ef-3cea-818c-41e94f5fedfe | -6.63716 | -44.57693 | 2025-02-28 03:59:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76786cfb-1f19-3113-8ca3-2bdf98f991b5 | -6.96724 | -43.01014 | 2025-02-28 03:59:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a7e4886-d5d5-3f47-99c5-a56308fef114 | -6.99452 | -45.62277 | 2025-02-28 03:59:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 798fa934-6240-34dd-9f6d-a26ad3ec49bf | -6.60072 | -44.18195 | 2025-02-28 03:59:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7071f277-b492-3220-b75b-7273f1614a2f | -10.69573 | -37.04925 | 2025-02-28 03:59:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9c546f78-a0b2-3d20-ab48-a1ace601423e | -6.54745 | -44.48503 | 2025-02-28 03:59:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db1df3ea-abe0-3ead-a309-8b8d9d451312 | -6.54067 | -44.42892 | 2025-02-28 03:59:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cdc3ff1-678e-37a9-83c9-f0f0790ea66e | -10.485 | -42.41954 | 2025-02-28 03:59:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9f6beb93-0b35-3c6b-bd8c-119438481f18 | -6.54462 | -44.48154 | 2025-02-28 03:59:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c6dc9d9-b96f-3457-81bb-029ccdeb4060 | -6.54851 | -44.48218 | 2025-02-28 03:59:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a95b3ffc-f2bc-35f5-8808-b41235f80c04 | -6.54768 | -44.48707 | 2025-02-28 03:59:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93a0d215-d36e-3e44-97c9-32b0ba3b82a1 | -6.53681 | -44.42813 | 2025-02-28 03:59:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40448a31-89d4-3c4c-98d7-0720b29f8fde | -6.16047 | -44.41904 | 2025-02-28 03:59:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d104cbae-e4c2-37b8-8cec-f1c4e64e689a | -6.96367 | -43.00956 | 2025-02-28 03:59:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d3cb24bb-48b7-3980-80bf-2370a72608a0 | -6.59915 | -44.18381 | 2025-02-28 03:59:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61d17fc2-0ab2-3d7c-8fc3-1fc50c763024 | -7.05639 | -44.37776 | 2025-02-28 03:59:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 641b0739-f771-33c6-ab8b-d38dd1f54dae | -7.05561 | -44.38246 | 2025-02-28 03:59:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe44f16e-49a8-37bb-bd5d-1145979c161b | -6.15965 | -44.42394 | 2025-02-28 03:59:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README2.md)
