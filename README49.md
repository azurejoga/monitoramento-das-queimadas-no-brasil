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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 628c2cf8-36ca-3d61-ad96-912ea4f64052 | -4.7334 | -48.30671 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f757642-dae8-3e98-b228-d493a7221f29 | -7.85526 | -47.09973 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82d7f20d-b34e-3b9e-ac6c-1761865de626 | -2.75962 | -47.75602 | 2025-10-28 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a32b8958-3285-3917-bcac-30d83db70dc5 | -7.47527 | -47.15865 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4af37d9b-1661-33f4-9cbc-389cd072083c | -1.55503 | -55.41602 | 2025-10-28 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a39d8905-2c46-3f53-aeac-3ed19dcea590 | -8.19713 | -46.93737 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b16ced91-c7a8-3874-a6af-0ae3e40f2b4c | -5.30402 | -48.69935 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 375e0617-a116-367d-bb91-5a61ae9348db | -2.19936 | -56.97625 | 2025-10-28 04:42:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea1aed1d-cc24-3786-8e67-d69e9a2efbd6 | -5.64981 | -48.02781 | 2025-10-28 04:42:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7632e14a-6268-3cea-93c1-5ee3a71a6960 | -5.65006 | -46.3283 | 2025-10-28 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e46bbc5-3303-38f0-9084-7e7c6162407f | -5.63415 | -47.6137 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbeac8aa-6e36-3244-aacf-8c41b81535e8 | -7.07242 | -47.36442 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dc3348f-9d7b-3c73-9fe2-8c909bfaede0 | -8.04206 | -45.14106 | 2025-10-28 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4923a46-0cf9-33dd-84b8-139e656755f3 | -7.27611 | -46.90305 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61cd3f85-cfc4-3bb3-83da-556295def522 | -7.82521 | -46.41908 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b44d395-28fb-31af-a557-2856c4221be9 | -6.483 | -42.23127 | 2025-10-28 04:42:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0f037270-20c1-354f-bdbc-4f997bf8a2a4 | -3.15173 | -50.33425 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b57d5719-94a1-33fe-b754-495f2c67821e | -4.22929 | -48.36767 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43241ea6-e634-3f4a-a039-8d1aaec7d341 | -5.11113 | -48.48368 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a384304-23ac-307b-9cf4-4cf3620da405 | -7.86715 | -46.39026 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f710862d-fffb-3a2f-ad63-01de7fcf5251 | -6.5895 | -42.68911 | 2025-10-28 04:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7fd59018-7177-32de-855f-9ac6b977d564 | -5.2013 | -46.14777 | 2025-10-28 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c10a0c89-aa10-304b-8503-6fb08b28f0af | -4.36737 | -44.29509 | 2025-10-28 04:42:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ace35dc5-d625-37bf-9573-2fc98f8e45ac | -5.61691 | -47.11092 | 2025-10-28 04:42:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f107650-47ee-3099-a9fb-5520fd8825fd | -7.96916 | -46.74853 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c8fd9a4f-23bc-358b-93a6-3518d272e3af | -4.87337 | -47.54762 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48e23dbb-5c88-3061-ace9-04f1b683a2af | -7.3119 | -44.10315 | 2025-10-28 04:42:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ae2b37b-6849-374d-b49b-124b02c0f5d7 | -4.33108 | -48.08968 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4694297-b0c7-3231-b151-148d66c4ca7e | -5.532 | -48.98792 | 2025-10-28 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be392857-809e-34a2-98b0-1836e8b13d2d | -6.48738 | -44.44236 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f07ac38a-007d-3595-bc3d-be3ecac25d5c | -4.44049 | -45.97923 | 2025-10-28 04:42:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a3a2a6a-d6d7-345a-b0fa-c351dc8a2fd9 | -3.44783 | -41.85087 | 2025-10-28 04:42:00 | NPP-375D | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 13b3c47e-5cb3-3085-bb19-49f2b2b76501 | -7.86284 | -46.39388 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bb4bb10-869b-365a-9b8b-aeb17cdce77f | -6.11596 | -41.73472 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 11378203-826b-3233-879b-df73124cd85e | -3.05047 | -53.02243 | 2025-10-28 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 596aeecf-3740-3de7-9819-d764b9c7680b | -6.97668 | -47.3377 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76955c46-bcf5-3c96-9267-c306523c0295 | -4.26855 | -48.69721 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4fc4304-40d5-3826-9d9a-400b0571a667 | -7.274 | -44.97535 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5be681c2-cab7-3454-978b-7487a193b73d | -4.99332 | -48.34707 | 2025-10-28 04:42:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4714c9ea-c9af-35db-aa9a-535893f42cc1 | -7.07879 | -44.94868 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 98b93657-583c-39e6-9d62-53cda8fd20b0 | -7.86113 | -46.39599 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4d42e69-ef78-373b-9090-39cb87d8f239 | -3.3985 | -50.27618 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3755df04-1c0c-32eb-b1d8-6c73e0f7a811 | -3.47118 | -49.97257 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e99ca7c1-5795-3ce5-b907-a70d678e2a5e | -7.877 | -45.18538 | 2025-10-28 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ca42442-4988-394a-b093-72c70e5f7fd9 | -7.07955 | -44.94363 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4389a5f7-2706-3a6b-83be-943292bdd837 | -3.67059 | -51.94632 | 2025-10-28 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93e78e40-b5c2-351e-831b-54354d698756 | -3.58864 | -43.63965 | 2025-10-28 04:42:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7f2e2fbe-5c53-354b-8a03-79415321fa2d | -4.20392 | -48.36018 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34149af4-4524-3dc9-afaa-a655b4744825 | -2.41782 | -48.44211 | 2025-10-28 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c485e5ab-eca6-3d5d-baf4-94569fc3b54d | -8.11389 | -45.95833 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38f080d0-f521-3652-af11-6a60f919e001 | -5.11168 | -48.48019 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65464305-77a1-34cf-9ea0-591878a6d748 | -6.63663 | -47.20164 | 2025-10-28 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 248dfaf4-6c18-37aa-ac1e-d74a22a80634 | -7.90311 | -45.69 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fef00f3-8f63-37f6-b1bc-7e447e60f49e | -3.72279 | -47.65177 | 2025-10-28 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 953053f1-25c8-397b-86e3-be4f3b3a96d1 | -3.39296 | -50.39779 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c22093df-5034-336e-905c-bffe4f406dcf | -3.67126 | -51.94221 | 2025-10-28 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01ac713d-1d89-3ad0-a97b-50cfb1b31cc8 | -2.82844 | -49.39975 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb34084f-9cc4-388d-8151-123548d32330 | -7.27106 | -44.99525 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aedbc835-fa25-3d38-b2d5-a2d1882bc296 | -3.57466 | -49.02018 | 2025-10-28 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c84d3e6c-813b-3234-beb0-563bbbd05989 | -5.48141 | -47.74349 | 2025-10-28 04:42:00 | NPP-375D | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37d89acd-e55b-3225-a764-8dd40a9097bc | -3.5731 | -49.43866 | 2025-10-28 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 107f85a6-e8e9-32d8-8c6b-8ae7b0de8584 | -7.45705 | -47.15984 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c558618-701c-3230-b084-9c49c6cfd7d2 | -4.68822 | -48.2673 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dba73896-926c-3140-97de-c21b21a98c5c | -7.80888 | -46.47771 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 54c817e4-01ad-3195-82fa-263d7ff2d8f4 | -7.45557 | -49.57975 | 2025-10-28 04:42:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73909a71-bbf1-3f2c-90e0-da412b6b5f1a | -5.70215 | -43.5316 | 2025-10-28 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09a61554-23c2-3101-a845-6ccdaf21b8f1 | -3.76936 | -48.92693 | 2025-10-28 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ee74784c-e69f-3bce-96ba-290fa2f8d697 | -7.45412 | -47.15534 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fbb9d0a-bb43-371d-9030-7a2b431fa75d | -1.67132 | -51.99628 | 2025-10-28 04:42:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9496a7a5-72ec-30b0-a87e-7465f7ad8ceb | -7.07485 | -44.94797 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9196d353-e3c0-3192-8926-5b5885a7533a | -6.11899 | -41.71347 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 10770aa1-dc50-34ae-9da9-eb70a9eeb093 | -3.12257 | -51.20855 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b05e84c9-1fd8-3379-bbd1-d97a835dd3c6 | -2.74434 | -45.40839 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a494575d-2f14-3e2d-ade1-a8ff0df94b11 | -7.97968 | -46.28403 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c9e38d4-2976-3f15-92d4-871f3971e9a1 | -4.43182 | -43.44493 | 2025-10-28 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b673597b-3117-3767-a13b-1896f425bef4 | -4.9013 | -48.57221 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22b81efc-6a38-39b7-adb2-38411c0745da | -8.18212 | -45.71119 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c12da2ae-c2ae-30b6-bf8a-4a8a84083807 | -7.00039 | -46.99016 | 2025-10-28 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f1a2c26-6b30-3ec6-88a4-463ffe189d5a | -6.68933 | -42.0464 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| f22c532d-6d4d-3e1a-86de-86c6d5d0dc82 | -7.47175 | -47.1581 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d012967-bc46-3d41-8331-64e0fd32568b | -8.05001 | -45.15604 | 2025-10-28 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4dc5865-e71f-3c0f-97a2-9366e216a6b0 | -3.06002 | -54.61831 | 2025-10-28 04:42:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d62f9604-354f-3a75-bcbb-48fd14c2d915 | -7.13211 | -46.99685 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 539b4d20-0b18-3c51-864b-85ee2c713819 | -6.77677 | -46.45808 | 2025-10-28 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 318433b8-27af-3d76-874e-ba56b63a159b | -8.32647 | -46.15868 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 391f3706-98eb-39d5-9995-7da8df543fba | -7.30078 | -45.0669 | 2025-10-28 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5327310a-98c8-3938-90a2-870572f8de56 | -6.13785 | -41.72053 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 93ee7fb5-bf26-3d15-87f0-cd05019e72c9 | -7.82843 | -46.39766 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00c1161d-46ff-3919-a7e4-d737789773b0 | -8.19195 | -44.4387 | 2025-10-28 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da62ac08-a31d-3e8d-a9a6-4231c3340f29 | -7.98127 | -46.74173 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8222b363-caea-338e-b031-2c22d9d963ff | -7.92302 | -45.6877 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 800735ae-68cc-35aa-8e03-c9693b5b27c1 | -6.42607 | -42.32792 | 2025-10-28 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 268da9bc-45d5-38aa-a11d-c40e692f8d93 | -5.65532 | -41.14293 | 2025-10-28 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8725eaf6-48fb-37ac-bb5c-75ead7f99caa | -6.60317 | -48.76289 | 2025-10-28 04:42:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b80d89b-a655-3b22-afa3-0b76c3eecf05 | -6.26805 | -42.71886 | 2025-10-28 04:42:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fa45e27a-46b7-3355-a307-61863347505b | -6.55802 | -41.59952 | 2025-10-28 04:42:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ce345cae-f44f-384a-9bba-e4a4d0fde416 | -3.44906 | -49.23806 | 2025-10-28 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03045f2d-d5d3-38ae-951d-c58202dc37ae | -3.02979 | -45.37068 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 9151a494-98a2-3093-b8f5-dc6279c48af1 | -2.43661 | -49.75626 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2d95b5d5-08a1-36b4-805a-31daf506d372 | -7.98489 | -46.74225 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README50.md)
