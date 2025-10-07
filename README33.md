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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 871db04f-8058-3a0a-a2b9-2f8215988513 | -10.67617 | -44.14886 | 2025-10-07 04:08:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31e6e5ce-719b-363f-aab6-ca27198d2731 | -5.49855 | -43.0796 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 06296868-5525-34c9-a676-85a1dcf0d90b | -7.02839 | -42.75646 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a2da736c-3fca-3f9e-8ade-44a75fb091aa | -6.4229 | -47.82141 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 466d184d-1979-344d-8275-493b7fe78f48 | -10.92307 | -47.07878 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75e5311a-1369-3db0-a1f8-8b64d17ec179 | -10.14774 | -45.47933 | 2025-10-07 04:08:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d5844df-8cab-3860-9e79-ca6ea61962e3 | -8.55367 | -50.08144 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de63fe6d-0c6e-37f1-a341-b981803d0ae8 | -6.65003 | -41.96401 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d3eae43c-92b7-3be3-bb0a-88654be52625 | -8.64253 | -46.29057 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd6ff44e-8025-3b6c-be51-cc69d67d1d62 | -8.6532 | -46.29707 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 552c6607-d1a9-34ff-9301-cb05d57d9a53 | -12.0218 | -47.78878 | 2025-10-07 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2afba542-5869-3b54-8a3d-13c19bd89be5 | -10.61938 | -49.05833 | 2025-10-07 04:08:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecf0cf12-3234-363b-a279-c70e749f7434 | -11.72044 | -44.30204 | 2025-10-07 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6284bf07-9919-389b-9b6d-b0ac90c813ae | -5.76613 | -45.74878 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2144cd99-c9a2-3143-8ff9-d639084e5221 | -6.45269 | -44.58353 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 44e8a38c-2d8c-3dfb-99bf-74175715ae85 | -6.71032 | -42.18272 | 2025-10-07 04:08:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 22cc2a3e-dd5c-3d6d-8508-2f7b2b77f95e | -5.87452 | -44.30044 | 2025-10-07 04:08:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0cd8f2a-e94e-32a8-a8cd-e9578aab3df0 | -10.25657 | -44.37017 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f7a46fd9-1d37-37c8-a12e-e0bd25d000e6 | -8.10703 | -55.09029 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ce3f504-46cc-31e0-91d0-19e8d0379588 | -5.98426 | -43.51199 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 251d6afa-e688-3a9d-bfa7-101037416893 | -8.18263 | -50.3043 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b9007c30-817b-362e-ae81-e44cdae8b888 | -5.09828 | -46.1581 | 2025-10-07 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a18c6c2-ab70-3974-bb3b-062ac88ea37b | -6.94346 | -42.06395 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9d477ed5-21e4-3186-81d4-e97dcab7b6bd | -5.142 | -43.82673 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30492bbf-39d1-3581-90e3-8840011f7111 | -11.0351 | -50.9221 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5402965c-fe4b-3825-afd8-26aa037d6476 | -6.45848 | -44.59293 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0dd34bbc-6dd2-3122-be1e-63056e0dbc6b | -8.41163 | -50.69925 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fd1b4b2-6488-3824-838d-5e5f45f592d5 | -10.44515 | -50.34598 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f87399f-24ef-3f8a-88be-f2a65e76cf69 | -11.48821 | -44.96845 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b56f1ba-a1f6-34f0-ae02-e19548455121 | -12.23863 | -43.77367 | 2025-10-07 04:08:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79d06fc6-d53d-35c2-97a2-da60fc33db0a | -8.41674 | -50.70024 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 637f2ccb-141d-3197-bca4-f91441810802 | -11.2614 | -47.77363 | 2025-10-07 04:08:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38d6e3b6-2b62-350e-b110-aaf918aa0553 | -9.98046 | -48.01402 | 2025-10-07 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b9184ed-a792-3237-a95b-47ecda170ddc | -6.71766 | -42.84525 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 889fa5f3-3d9e-35ac-9eff-41a72f69b652 | -6.69886 | -42.85994 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3f89204b-0877-3b38-950e-2575d52326a4 | -10.38894 | -50.30455 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 70781b14-3a18-30b3-8988-f0d03346930a | -6.95399 | -43.11695 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78587447-9070-398e-a861-907402a246d5 | -6.72899 | -42.15366 | 2025-10-07 04:08:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 772323c0-4d63-3caf-b4e5-c8a5935371f5 | -10.2656 | -44.37933 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 206fb8c3-3573-3cf2-b77c-939f9156ef54 | -11.80904 | -45.0486 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f09acb82-bbc6-34dd-b4e4-8529aa453bd0 | -7.46049 | -43.0332 | 2025-10-07 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5dc92c2e-2180-337a-9197-a4aeda988b01 | -6.72661 | -42.83215 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3005997c-b05a-30cb-bec9-551299d9fcbb | -10.09081 | -50.52419 | 2025-10-07 04:08:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43eb3051-02b8-30c1-ba68-a9706d1a3f54 | -6.98652 | -42.8695 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 37.3 |
| a2b79382-7735-39d7-ab2e-c17cc111a05d | -7.67731 | -50.2141 | 2025-10-07 04:08:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d3bee8c-adb7-3f94-a271-38a2bc681d09 | -5.50032 | -43.06861 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| a3defaee-68fa-33ba-89a0-8940f516ba8f | -5.34054 | -43.38448 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4adcbcce-af1e-38fb-9450-07a3d2343186 | -10.60014 | -49.63855 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d88787c-7fd1-394c-9b07-c2362f6242a9 | -8.18244 | -50.30435 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd787d24-66c6-3964-a9c5-681b8b914b40 | -7.69025 | -42.40353 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 044b286e-d5aa-3f21-a797-f88373f090ea | -10.88916 | -47.10609 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 59356b32-1a85-33fc-b4f4-5caf55a9d46c | -10.73645 | -50.48702 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 210895ac-291b-3c90-bd86-177417b035a7 | -11.50063 | -44.97379 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd5d846a-1ca2-39f2-8884-23ddc4eb3b8b | -8.44404 | -47.20827 | 2025-10-07 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 71be57a7-0c9d-37ad-ac8e-287a803d4b06 | -10.19542 | -45.5245 | 2025-10-07 04:08:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f313b876-bd3b-3320-ab23-26fbc4e8c689 | -7.75337 | -42.54258 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ae04c576-8ebf-3b4c-b2cd-c22b43a47744 | -7.72441 | -42.40178 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f7edad3b-c4f6-3e64-acd1-9fd5f40b4582 | -10.49603 | -44.41274 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39c7932d-60a8-3175-bc2d-d4f62428ad54 | -10.4545 | -50.41165 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 47291412-a1f7-3b8f-bbfb-5ec782e69cbe | -11.1238 | -47.21858 | 2025-10-07 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8406a0f-2809-3dcc-8465-39af72386cf0 | -10.8492 | -47.1762 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 284376e5-3b90-341b-912e-c23661228ffb | -9.42352 | -49.10883 | 2025-10-07 04:08:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d2b78fa-c428-3fbf-baa6-588d06c54b24 | -10.39338 | -45.379 | 2025-10-07 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 628eca51-6e6b-3227-b91f-673ba595202c | -10.32154 | -51.45795 | 2025-10-07 04:08:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0addf24-8812-3a3e-a584-d41b8e8c037b | -5.316 | -43.38412 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fee243fb-e518-3d38-8fcf-43fe700cd074 | -4.68786 | -45.84069 | 2025-10-07 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 849a2b77-2632-341a-8e79-79459cf6a22b | -6.32319 | -41.61539 | 2025-10-07 04:08:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f0619f81-5708-33b9-9e63-59f5efa7b457 | -8.87284 | -47.68118 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c0ea3916-87f4-3afd-8ad0-dc77cfa733aa | -6.72449 | -42.80268 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 63b37c89-57dc-3e09-8354-59b17baecee8 | -11.81538 | -45.11256 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fb1da79-3eec-322e-adbb-01aea64fc35c | -7.8051 | -44.14333 | 2025-10-07 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 01f2dae6-aa66-3565-8eaa-3a2a148c5058 | -8.18191 | -50.30727 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89486e8b-4997-3fe2-8860-1dd720f48e7a | -10.81034 | -48.59758 | 2025-10-07 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ea1ce4b-b256-3ed8-baf0-74510c47ef8f | -10.91706 | -47.06767 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a91e4d87-907e-3dd8-810c-0286c141a2f9 | -10.81887 | -48.59908 | 2025-10-07 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7682dc8-8206-395c-a9e4-0e53256f5d39 | -7.3888 | -50.33181 | 2025-10-07 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31abfda1-b930-32b2-87ef-5b6ebae27b43 | -11.26586 | -48.84658 | 2025-10-07 04:08:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c3d696c-00f3-38a4-9ea5-4050693300d8 | -11.83928 | -45.0969 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f132174-ca19-3189-bcea-3c15b2ef0632 | -6.28655 | -42.94415 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a799a4a4-f508-3399-b29b-7a43f8008e35 | -12.23805 | -43.77727 | 2025-10-07 04:08:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6d0dd11-469a-321f-a241-6da5afbd6c98 | -6.28046 | -42.91767 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14efea65-62d5-3cef-ad35-6380507be29a | -6.52811 | -42.47528 | 2025-10-07 04:08:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2012c4be-9033-3812-836d-7c227d1076ab | -5.2423 | -46.57217 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e1f34ff-6096-3843-9346-4f6c83172b9e | -6.721 | -42.84578 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4ac36dfa-91c6-3c1f-9cba-1b2888478321 | -6.96544 | -42.01435 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8015fca6-29c6-36bf-97e5-53ed40d2cd0f | -6.29776 | -42.93862 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6d363b2-70ad-3541-9bf0-ac39f7720470 | -8.53335 | -46.24501 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 16a1b942-ceda-3eeb-9f48-9b87ce180cf1 | -14.7389 | -46.0138 | 2025-10-07 04:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 31c2d8e2-c918-3900-9a7f-c2733bc4146a | -8.5584 | -46.2387 | 2025-10-07 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| d2fe6ea7-acce-35a4-9fa2-9860fd21b76a | -3.0826 | -47.0308 | 2025-10-07 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 59b23906-93eb-3d63-9728-4eb2438c6aa2 | -8.5393 | -46.2631 | 2025-10-07 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| a3016494-4623-3f58-9789-7bf70bff6274 | -10.8921 | -51.0269 | 2025-10-07 04:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 4155a204-e1b0-365a-91fb-10aa8be27fd0 | -14.758 | -46.0335 | 2025-10-07 04:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 1c43ef87-1577-361f-b78d-40741481474b | -18.1769 | -53.3669 | 2025-10-07 04:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 7d40da1f-3663-32e6-bb86-fcc532e16892 | -8.5398 | -46.2181 | 2025-10-07 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 619990e3-9cd6-3b19-ac33-cb93ffde4176 | -6.4543 | -44.5749 | 2025-10-07 04:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 9fa9a7fc-9ea5-3019-8df4-a0358070c219 | -14.777 | -46.0532 | 2025-10-07 04:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 380.2 |
| 4d47e2c2-fda2-3e81-b971-92cd6040d691 | -14.7765 | -46.0763 | 2025-10-07 04:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 4e32ec99-68b1-37f7-8477-6b548439b91d | -22.0071 | -49.7321 | 2025-10-07 04:10:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.8 |
| d6963dbb-9755-3dbf-b256-09d1867b922b | -18.1181 | -53.3333 | 2025-10-07 04:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 57.8 |


[Clique aqui para ver as próximas entradas](README34.md)
