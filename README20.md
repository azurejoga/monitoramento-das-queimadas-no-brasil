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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c7b2c3c-d2e7-3ad8-9399-90fdf53ee20c | -12.06754 | -48.20957 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee5bb920-3f87-3e87-a197-aa4f9d23c890 | -4.46106 | -43.91497 | 2025-11-14 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00c2487d-9efd-3324-a1c3-144a8977b72a | -3.25158 | -42.05685 | 2025-11-14 03:55:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4d3700d-9053-3132-a3f3-b822c6d7e688 | -4.45304 | -43.21236 | 2025-11-14 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62c7522d-f1f7-3ad0-a80a-8825f11738ac | -15.47554 | -43.54911 | 2025-11-14 03:55:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64ea227b-c5a9-3dd8-92b4-0badb6d52e4c | -4.61452 | -43.38155 | 2025-11-14 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 70228c01-5648-38e1-8f57-98cc5d99e049 | -11.73911 | -48.53421 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0353f816-495c-33e3-ab58-8c6c6262ea90 | -5.02837 | -41.10026 | 2025-11-14 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 18af6d47-e811-3993-8022-5543658b096b | -4.60259 | -43.2979 | 2025-11-14 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce01885c-6cc3-35a5-9dbf-248934cbe50d | -3.01762 | -49.4357 | 2025-11-14 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 148e53bd-dadf-3f4e-afd9-1bb579349a64 | -12.71634 | -45.41781 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a11d2607-9ad6-3711-8b4a-642fe1646ef8 | -8.63304 | -46.69714 | 2025-11-14 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f1a607a-fe56-3c27-8403-79475284235a | -4.50319 | -43.95614 | 2025-11-14 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e7605cf-83c7-3175-b430-ef6404d283d8 | -3.35968 | -48.40031 | 2025-11-14 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fbb44dad-2378-3fbc-ac8d-ea70e7985ac7 | -3.35843 | -45.34703 | 2025-11-14 03:55:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fa7b4ae2-b39a-36e8-995a-6eebfb62170a | -12.02238 | -46.7664 | 2025-11-14 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9fc6ef2-753e-3244-8372-7477ab52272e | -9.94545 | -36.21539 | 2025-11-14 03:55:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c3f9129e-03dd-3f75-953a-b6eee04233c8 | -9.18958 | -41.03175 | 2025-11-14 03:55:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b752085d-06ad-362e-a2e2-ed63566a5acc | -11.73572 | -48.52345 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cead627-3dea-333d-9af3-f9c23789bb70 | -3.76797 | -46.00741 | 2025-11-14 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1374ac02-030b-3ec8-92ab-e1a78bf5049d | -4.02414 | -43.9857 | 2025-11-14 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 734a695b-7be4-3716-8466-ad0aa10fc47c | -9.01365 | -44.06538 | 2025-11-14 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7222521-c3b8-33bb-a6fb-7aaaa5f31845 | -12.68776 | -45.4328 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 72bbd3bb-c9af-3d54-b882-8b2232123517 | -2.24198 | -46.07618 | 2025-11-14 03:55:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ace4c4a0-a318-3fe2-bc68-1306a4c169e9 | -12.99786 | -43.86018 | 2025-11-14 03:55:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b6ce381-dacf-38d9-8b64-3a04913965e4 | -2.65478 | -46.99768 | 2025-11-14 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b4ad006-ff23-38b8-8c71-8e90348ad40b | -8.94499 | -49.81751 | 2025-11-14 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c8556bb-923d-35f9-b95f-8d80a14b5426 | -3.26836 | -43.12423 | 2025-11-14 03:55:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 979fac5a-ca99-3621-8d3b-fd5f81a00024 | -4.89996 | -42.91033 | 2025-11-14 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1f3fb6e-8f81-3a90-ad0c-673874e5bff7 | -9.00694 | -44.17748 | 2025-11-14 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d5039055-c919-3adb-8fcc-a3b8c512528e | -15.13923 | -42.93554 | 2025-11-14 03:55:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1cf13b4-9768-3f90-887f-5fda7e174510 | -3.01672 | -49.44093 | 2025-11-14 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 13de46fe-5805-38d8-afc6-7619d53bf609 | -11.85368 | -49.22924 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 10cfb7c5-bc74-388f-8d27-4a581ea1bafb | -3.46192 | -43.18259 | 2025-11-14 03:55:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6094e2c7-3815-30a4-b815-091f4d686df3 | -4.23887 | -46.1111 | 2025-11-14 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da84197b-12ab-36ce-a46f-02c67cbeaa1c | -13.73709 | -43.14408 | 2025-11-14 03:55:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7a68f97d-bd3a-3ed8-ba1e-b779a2eb1517 | -3.01176 | -39.94282 | 2025-11-14 03:55:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b6291a7a-472b-3a67-9c3e-8dc501195204 | -12.07263 | -48.2105 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 128ede7b-b3da-377e-9bdf-c8301e65a71c | -2.65418 | -47.00126 | 2025-11-14 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcb881e1-3f77-3065-b640-18d1189d4d69 | -12.03965 | -49.44394 | 2025-11-14 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48f47aaf-cd81-31a2-8cff-6893baf39478 | -3.82291 | -44.25054 | 2025-11-14 03:55:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d746dea-50ff-3fcf-9ccd-ea8a4e37de99 | -11.99171 | -44.21851 | 2025-11-14 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fcdae02-2004-30c4-8217-7d7ea72d5268 | -9.91261 | -47.86532 | 2025-11-14 03:55:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dddc44f2-16f4-3fe5-9289-b2f6005c1b01 | -4.07616 | -44.13394 | 2025-11-14 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbeab5e3-401d-3c4c-b138-e38a0b0765df | -4.23791 | -46.11683 | 2025-11-14 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aaf4ab0b-7c8b-3b70-8b8a-85739d946310 | -4.89535 | -42.83761 | 2025-11-14 03:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0aa1b31c-b308-3e13-b423-96eb9c9d77d8 | -8.53975 | -49.58268 | 2025-11-14 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfecfff2-ce1f-38ab-8426-a96c6fdb0ded | -12.27743 | -43.83671 | 2025-11-14 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3e9baba-4d8d-3525-89b4-7137b43fdcb3 | -5.398 | -39.51092 | 2025-11-14 03:55:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 214ea85c-928e-3de9-8c13-57710e9b0a08 | -10.75026 | -44.91347 | 2025-11-14 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de2cbdfd-4942-38fe-be83-c4fa4c567dfc | -13.50244 | -43.63811 | 2025-11-14 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b142225-893f-34a2-8927-34bdfe16935b | -2.47153 | -45.18983 | 2025-11-14 03:55:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de1338d9-7ff6-3fbc-a79c-2d70d3137e58 | -11.85509 | -49.21642 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 8fb1b5cc-88b3-3ab8-8975-dcb9c9075bf7 | -11.05356 | -37.1293 | 2025-11-14 03:55:00 | NOAA-21 | ARACAJU | SERGIPE | Brasil | 2800308 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 637524d7-699d-3dd4-9d86-ed3a19b34a88 | -4.90052 | -42.90685 | 2025-11-14 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b356a51-dbbe-359e-952c-c75fc125a8b0 | -14.94579 | -49.7931 | 2025-11-14 03:55:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| f0dad242-93e1-3c03-917d-e84f4bceb5f9 | -10.28954 | -44.35996 | 2025-11-14 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6bac3000-90bc-3303-8200-ad9ba9ab72db | -8.63558 | -46.69582 | 2025-11-14 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b22a1da-79e3-3008-9774-4f326492b9ee | -12.00765 | -46.76852 | 2025-11-14 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 960a0e6e-9c8c-3f00-a6ed-ff90649cbd00 | -9.68068 | -47.8909 | 2025-11-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea3de4ef-7e9c-3239-b104-d0a4cbde70da | -4.26882 | -42.11123 | 2025-11-14 03:55:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dc0b6b60-4d66-31ab-b86b-9ad6ce6bf1b5 | -3.36296 | -48.39812 | 2025-11-14 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2a4aa2e-dd9c-3faa-b1ae-2ee605eeff86 | -9.94899 | -36.21593 | 2025-11-14 03:55:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 946cd481-221e-3f0c-8aff-47686bae9c16 | -11.85033 | -49.21175 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d3ad11c6-7e09-34f3-9099-807a6f45eb0e | -9.93908 | -45.09744 | 2025-11-14 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c42417c-bca9-362a-acf7-1f3acc1b590f | -12.6824 | -44.14858 | 2025-11-14 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85fd177a-e06a-3c7d-9feb-b135ccfb0641 | -10.636 | -44.82151 | 2025-11-14 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 467fdadb-00d5-39d7-b368-580cb234b52c | -16.59181 | -42.21659 | 2025-11-14 03:55:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9f95b3ef-bdb5-344d-aa5b-fd21af4ac407 | -12.69123 | -45.43749 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bbdbfc57-0d76-3179-ae46-b0167d065be6 | -13.66425 | -44.21355 | 2025-11-14 03:55:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5310dfa0-557a-3c54-859c-9230f163c840 | -14.14055 | -44.20774 | 2025-11-14 03:55:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28d03896-f781-3d06-85fd-c9907585c094 | -10.10802 | -40.89444 | 2025-11-14 03:55:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| b3416e67-cfd9-35c0-9c01-f1f30fd5ac30 | -3.77303 | -46.00822 | 2025-11-14 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a19ea835-d3d2-38d6-84e9-e824e5fc49c6 | -11.57341 | -44.86987 | 2025-11-14 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93cc11de-4232-345c-aebc-30d46671adf0 | -3.81916 | -44.24533 | 2025-11-14 03:55:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e70c698b-77ca-319b-b356-ae76bbc9aad4 | -2.17067 | -48.3674 | 2025-11-14 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76f09bbc-7208-35d4-ab7a-21175cc9b714 | -4.68553 | -42.81675 | 2025-11-14 03:55:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 798af274-86b9-30a0-8a07-c15f0264cfa2 | -2.63254 | -47.30151 | 2025-11-14 03:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d9d1af70-3860-3e5c-a955-f5bd2d354a03 | -11.84758 | -49.22628 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 7ad97a45-1565-3355-bed7-c76eecbef8e2 | -15.78812 | -41.4727 | 2025-11-14 03:55:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 17a94f51-02dd-340f-88cc-4ccd77bdd09e | -11.93219 | -44.71416 | 2025-11-14 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f039535-49b9-39d9-b91f-9d6803c4bc10 | -13.37664 | -43.20784 | 2025-11-14 03:55:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3eff1eab-82ac-3cb0-9905-90cdc050924c | -11.8544 | -49.22558 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7f331a77-e0ef-3952-a3fb-c66c5d95bbac | -9.85496 | -47.61556 | 2025-11-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f43ece6a-f9b6-3f77-9484-5298042e54bb | -15.30644 | -47.37783 | 2025-11-14 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5f6f21e-9b20-381f-8c3f-9b04775dc45c | -10.174 | -44.77721 | 2025-11-14 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31c1a7f9-5168-33fd-9489-a13d94cc1356 | -4.86922 | -37.44967 | 2025-11-14 03:55:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2d55b0e7-2a58-3a24-9aa1-08d7629b1c81 | -2.46664 | -45.18909 | 2025-11-14 03:55:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1e22cf4-29e9-3056-b0a7-9251e0c1e40b | -2.88213 | -45.29178 | 2025-11-14 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 59f140e5-02e6-3675-a7c8-4b6b917d40d2 | -10.72919 | -45.08395 | 2025-11-14 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd701ea9-ca41-3ba3-a1ef-19a12c80002a | -11.85652 | -49.21478 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| c55dc729-fb51-3253-8de7-acf6fbb8657d | -2.45561 | -48.8201 | 2025-11-14 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed66481c-5442-38b2-9d8a-05a8b6d7a7de | -14.78703 | -43.57546 | 2025-11-14 03:55:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be463153-00bf-3773-84c6-f537938a8c2d | -9.91317 | -47.86226 | 2025-11-14 03:55:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f46eb774-e89f-30d0-a75c-b6d8c688f25e | -13.1531 | -48.21495 | 2025-11-14 03:55:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ddb0d5d-85c1-349f-815c-15d5de1cc55a | -2.23677 | -46.07539 | 2025-11-14 03:55:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd1e162a-e119-3f1e-bf54-182a9251b137 | -12.99734 | -43.84065 | 2025-11-14 03:55:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd7b6cf2-e21e-3b4d-a814-c3cd5d50d9f1 | -4.52831 | -41.10251 | 2025-11-14 03:55:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eac1f15e-e1cd-3a12-9ce1-30d570ddd8ca | -5.31322 | -37.61169 | 2025-11-14 03:55:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c665aada-b125-3b4f-a11f-b827ca62b53e | -8.90872 | -44.44079 | 2025-11-14 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README21.md)
