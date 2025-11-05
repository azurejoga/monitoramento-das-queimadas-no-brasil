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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43ae2eb7-e176-33af-8025-665b1b8c3b54 | -7.23956 | -45.70106 | 2025-11-05 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4759f758-e017-3973-970c-6e52de03616d | -8.10127 | -45.71009 | 2025-11-05 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8e732dd-8a40-3d32-866a-695df5f624b3 | -7.66897 | -47.41852 | 2025-11-05 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aa47f4af-87df-3176-b1ab-3c9db2d3ac51 | -12.32827 | -43.43873 | 2025-11-05 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbe55299-88a2-3962-a20c-b24b2c6c7ca8 | -7.46032 | -46.94921 | 2025-11-05 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cd7690e-edb7-3bd2-b754-f25d9b9f719f | -7.29729 | -46.23314 | 2025-11-05 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58f4bc61-4731-3cad-b8d9-c532ea329c15 | -8.58331 | -47.22692 | 2025-11-05 04:14:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2e1727c-21f4-349b-8e6d-27aa2b4de530 | -10.38492 | -47.75665 | 2025-11-05 04:14:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9f6ccaee-39bd-3760-a32c-0edc4820e788 | -7.32986 | -38.84953 | 2025-11-05 04:14:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bd7583b7-7b6d-39c1-8ab1-002f8f71a9be | -8.59179 | -43.74488 | 2025-11-05 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e552b3ae-847b-3ea2-a40e-e7c5bdb076b6 | -10.41289 | -44.38935 | 2025-11-05 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 225a80bf-e2e9-34c8-a3c9-a60a87022485 | -12.81529 | -43.77922 | 2025-11-05 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9739da9-9482-3cc1-a05d-f28d5bde2722 | -11.53334 | -50.17405 | 2025-11-05 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d934ea0-46e1-37f9-b747-f2af39a326fa | -7.1472 | -41.82407 | 2025-11-05 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4d4b7c84-017f-3f0b-bbed-bca7004a83cf | -8.67383 | -36.6935 | 2025-11-05 04:14:00 | NOAA-20 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bb205a63-6e2c-35bd-a5d3-cc97c831b639 | -6.70484 | -40.83207 | 2025-11-05 04:14:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4c40cdbf-f8d4-3313-94cc-762af9a063f9 | -7.43828 | -46.60854 | 2025-11-05 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f01c5fdb-53b3-319a-8fb9-079a6e8db5fe | -6.36975 | -42.40872 | 2025-11-05 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2547abfe-2bed-363b-93c0-f3c1c20e64de | -9.06671 | -48.83097 | 2025-11-05 04:14:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 421ad928-bebe-3b72-b161-98e3b7a2d509 | -9.71929 | -48.01632 | 2025-11-05 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 682b14e0-451c-3b8e-ab5a-f167d8508f73 | -7.11422 | -46.52847 | 2025-11-05 04:14:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 377aa3cb-0c1f-35bc-bb45-cff37d945f01 | -6.27074 | -42.56382 | 2025-11-05 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3177144a-b129-37ef-b00c-9466593cb2bf | -10.40519 | -44.37373 | 2025-11-05 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d10555fb-9f05-3e9d-a041-7c267a897585 | -7.93762 | -49.7362 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0af08df-6cb7-35ca-8711-45bb64e27d70 | -7.23258 | -45.69994 | 2025-11-05 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0301f6aa-8f75-3d2e-8a19-6d196b5808e3 | -12.39985 | -49.90161 | 2025-11-05 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05d68c18-d55c-30c7-b0d5-6d523447c40a | -6.21055 | -43.26915 | 2025-11-05 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c97a143b-6c1c-39ad-8a7f-030834e14364 | -10.18184 | -40.95472 | 2025-11-05 04:14:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c594967c-66eb-31f0-b507-9e3954bc0204 | -7.68291 | -40.86793 | 2025-11-05 04:14:00 | NOAA-20 | CARIDADE DO PIAUÍ | PIAUÍ | Brasil | 2202554 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 035b4582-2c77-3e35-8580-d2d8fecd0271 | -5.91527 | -44.01475 | 2025-11-05 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9084cb46-4c65-35a9-9313-206e14fc7ee5 | -8.8617 | -49.88012 | 2025-11-05 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0fadc9ff-2ab0-30b1-a610-3e5bef79798c | -11.28111 | -44.63494 | 2025-11-05 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6807d74b-b4fd-3089-a243-9878bcea96ed | -8.67362 | -36.69113 | 2025-11-05 04:14:00 | NOAA-20 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 215e22e3-44e6-30f7-b7c1-824ee0f0a005 | -7.93771 | -49.73474 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 258e5ec6-129b-3e4f-b053-915df4d09119 | -8.58461 | -47.22923 | 2025-11-05 04:14:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cc7cc73-1d0c-3bc5-bafe-182565e19ef7 | -9.21114 | -48.5943 | 2025-11-05 04:14:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14d96f89-8386-3b90-9c18-564743560464 | -7.14115 | -44.99213 | 2025-11-05 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 999d55a9-0161-3ef5-8bcc-2a81d8d57e97 | -6.04414 | -51.3886 | 2025-11-05 04:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2a9a972-0643-310d-941a-da4cdd044db8 | -7.72717 | -45.81769 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c3b7e06-87e2-389d-9139-184c88a7f4e1 | -12.24638 | -50.29462 | 2025-11-05 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09c0babc-6f3d-3a40-90be-c0ec8fd327ec | -8.3816 | -47.04959 | 2025-11-05 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ce3aad2-60d0-3258-b2ed-bc2bb9102a08 | -12.94323 | -40.65529 | 2025-11-05 04:14:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ff589a98-24e8-3e8a-88e6-d71f5e0f5b0d | -5.85907 | -44.0022 | 2025-11-05 04:14:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cfb708f-490b-33ee-a34d-12dcd7578a89 | -6.73315 | -44.14853 | 2025-11-05 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e84e3b6d-0c52-39c3-9c1d-2d3165b7057b | -6.12066 | -44.06913 | 2025-11-05 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b54afea5-8551-3314-bb0c-7cd7da7f553e | -13.01166 | -43.6497 | 2025-11-05 04:14:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f52b5cab-81ce-3964-b32c-c811121414db | -6.05369 | -47.28633 | 2025-11-05 04:14:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b267beca-81cc-314b-9c54-060607b0ab36 | -5.54036 | -50.07333 | 2025-11-05 04:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2053cce7-325e-3b85-9aa8-2d9c02511372 | -7.7278 | -45.8138 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9369806-5426-3ab4-9139-d23781c7277b | -7.15884 | -40.10167 | 2025-11-05 04:14:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b7740910-72d1-3fce-8be0-252e589565ff | -7.96847 | -50.00233 | 2025-11-05 04:14:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| abd7f41d-4749-32fd-9070-7c7420b6b1d1 | -10.48114 | -44.30323 | 2025-11-05 04:14:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bfe27efe-60de-3436-852b-b757cbbd6a20 | -6.05102 | -43.03132 | 2025-11-05 04:14:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f02cd4b8-3d30-374e-9467-6928a285ddce | -8.2559 | -39.43913 | 2025-11-05 04:14:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f98c327b-b985-35e5-837b-567e34925752 | -6.94881 | -41.13906 | 2025-11-05 04:14:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8d6ad292-b245-38fe-9648-901989d6a770 | -8.05625 | -49.64779 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a644401f-2a37-30f9-b252-9714046ef24c | -9.04799 | -47.00881 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5005dfa-90a8-3120-b553-33cdcae23d41 | -9.9186 | -47.84851 | 2025-11-05 04:14:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 957f0804-c6cb-32ef-8822-4c6dc9d3bf43 | -5.91193 | -44.01423 | 2025-11-05 04:14:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fc85c77-061f-315d-a66e-df82f494db01 | -10.50194 | -42.4039 | 2025-11-05 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 6ac65b2e-b60d-35ad-846e-70b4f133c808 | -11.63024 | -41.46614 | 2025-11-05 04:14:00 | NOAA-20 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 05d43c6b-4f26-3283-a183-3594e453b1cc | -7.71491 | -47.18575 | 2025-11-05 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 996f89d9-bf7a-3433-8e3f-8557d2bf6230 | -8.22925 | -49.98575 | 2025-11-05 04:14:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36571dbd-055f-38e9-830e-16ad26b6b5a7 | -6.70542 | -40.8283 | 2025-11-05 04:14:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 6b67aa90-81ac-39ea-b8fe-036dca6ff8df | -10.37824 | -47.75095 | 2025-11-05 04:14:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9a3f2450-6724-3825-82aa-37ba5543e088 | -8.05836 | -49.64285 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3e9c4245-714f-3366-bc8e-61a8d3001d55 | -8.19587 | -44.43777 | 2025-11-05 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41924ae4-bfa4-3288-9108-c6f7e3d05905 | -8.37957 | -47.85038 | 2025-11-05 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69e47343-cc81-31a8-a7c1-093612ec6db3 | -8.27134 | -48.00989 | 2025-11-05 04:14:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58dd24ee-41ec-345c-9a04-a37d4771d72e | -9.77732 | -43.61809 | 2025-11-05 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 03f3fa87-c4c6-392a-bb0f-2ae5c47afea0 | -5.30935 | -50.5668 | 2025-11-05 04:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| effd1081-d797-301c-bed5-a089d41da2cf | -7.93086 | -43.21997 | 2025-11-05 04:14:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ed97ded1-5a7a-33f1-a7c0-a9b24cab3fdb | -6.04985 | -47.28571 | 2025-11-05 04:14:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3d7b086-49a8-31e2-a1cb-71431be3a261 | -5.23299 | -48.5099 | 2025-11-05 04:14:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 15.9 |
| c0754543-7ec0-3d00-95ab-3b17822b85cb | -5.55932 | -46.38873 | 2025-11-05 04:14:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d57108b1-16a1-3204-b505-76e911933fdc | -11.29669 | -44.62334 | 2025-11-05 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fcebda46-5776-37c5-ab16-cbbaaba0650c | -6.21518 | -46.13477 | 2025-11-05 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0749e0e3-7f42-3975-b585-379f5a9252c4 | -8.13907 | -42.21131 | 2025-11-05 04:14:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 349eefb0-9ff1-3724-9f4a-9dcf36466751 | -5.93011 | -43.68634 | 2025-11-05 04:14:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cef9072-50c0-34e7-92e8-69cf1d0ec5de | -7.1048 | -44.86647 | 2025-11-05 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e039f12-1228-32ae-bdcf-6c9874e05b4a | -6.20724 | -43.26862 | 2025-11-05 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| badbfe5f-12f9-302e-9a5d-d0365a055b89 | -7.32915 | -38.85439 | 2025-11-05 04:14:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 37e75890-f159-3bc2-b815-2241172e1b54 | -10.49406 | -42.41017 | 2025-11-05 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 66245d2d-6497-3802-b5aa-a9a8ed2516d5 | -6.07337 | -43.25408 | 2025-11-05 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9efa441b-445a-3318-b548-64e2c1534676 | -7.89974 | -45.5691 | 2025-11-05 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39abeece-7805-3ca0-ac06-60ad847a8979 | -11.84233 | -43.72549 | 2025-11-05 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24a90de2-a64e-31df-a68e-3ec7ae5acb27 | -8.46071 | -49.63725 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 381e3507-8abc-341b-83cf-4b499cb6730d | -13.04505 | -43.22932 | 2025-11-05 04:14:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 10780a7b-5be8-3361-adc7-a8885f52c3e4 | -7.03967 | -41.45931 | 2025-11-05 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7998386a-cb15-3af2-a782-9d2f273a54b5 | -5.51722 | -46.23195 | 2025-11-05 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 212fdb37-6e03-39dc-8a42-cacc0a2beef0 | -6.58957 | -44.62396 | 2025-11-05 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c70208b0-49d0-35b9-abd6-5fe8975bf084 | -10.43688 | -42.51335 | 2025-11-05 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a9e0ec6e-b24b-356c-a83f-ac0a7b5ce5a0 | -7.17089 | -42.73729 | 2025-11-05 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fe7656df-8331-31e2-87e7-2ea507352018 | -11.53829 | -50.17081 | 2025-11-05 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d424238c-bb19-30d6-be2c-c06690f16d4c | -6.32517 | -46.33251 | 2025-11-05 04:14:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ea35d5c-941c-3824-b373-26820824196d | -9.74387 | -44.00174 | 2025-11-05 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13c59578-20e0-3e24-9339-31cdf5102d27 | -7.9016 | -48.72844 | 2025-11-05 04:14:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecc42c88-59a1-3c3f-ae62-e8a0a91823cc | -6.05725 | -46.0975 | 2025-11-05 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 456a1916-7e01-31f6-aca3-553f577a08b1 | -9.08683 | -50.61999 | 2025-11-05 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7290d56d-3f82-3b11-8d86-2f1608775884 | -6.06288 | -47.30272 | 2025-11-05 04:14:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README25.md)
