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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a5a1701-13b0-379f-9d5a-601caebf9ad0 | -10.22007 | -49.9798 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39aeb22b-8ea1-3e4f-841e-7d6b34c100fe | -7.3785 | -42.13182 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 77cf599e-dbc2-3b0e-ad5c-51ad7014aba3 | -8.10811 | -46.35007 | 2026-09-28 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 433d9a47-0ff4-36be-9dd5-c0baf98f8b1e | -12.6339 | -47.32061 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f889cab4-45a1-342c-bd50-6abc72758640 | -6.59759 | -47.16953 | 2026-09-28 04:34:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad87af3b-f6f8-31f2-bec9-aec9322c14d4 | -8.00077 | -39.70538 | 2026-09-28 04:34:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 80f4b34f-6757-346c-a82b-20ec608296d2 | -9.9916 | -50.13329 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 01aed508-961d-3103-bb0d-83bfe9bbc8d7 | -7.88475 | -45.44396 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66425295-7c37-3bc5-a579-94dad399fd47 | -6.71802 | -45.59558 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eeca0b37-3daf-349f-bc4b-fb57dfffeafb | -7.86972 | -61.19388 | 2026-09-28 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c0d1d46f-20f0-3bdc-973e-6a2295f805b4 | -6.59427 | -47.16902 | 2026-09-28 04:34:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 631b5c8d-2f38-391c-8935-a76d54972a4a | -10.2022 | -50.00615 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1af11ebc-34c4-3f43-bccd-7db7ad09b9e2 | -10.21561 | -49.98639 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20ffd5fc-05f2-326c-93d0-70f1088ee84f | -12.31059 | -46.40591 | 2026-09-28 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7b527eb-dd51-3f33-a809-6c214beaf636 | -10.22228 | -49.98746 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 243eef44-922d-33a8-b513-ef0a545a7092 | -11.86175 | -47.09711 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b16b010b-b434-324e-8aac-7f882ac57129 | -8.24872 | -49.96309 | 2026-09-28 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcab67aa-76bb-3f9a-a593-d9e9eb790d7d | -7.6952 | -54.7599 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7f231fb-20ce-3744-8395-b8a01ae5d2d4 | -8.03345 | -54.89745 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9c07c6c-ab64-3403-ba59-c0764dd3b0e3 | -11.3762 | -43.39884 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f321117f-ad4b-3221-954e-3b61ac3eba4a | -8.42502 | -45.01103 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60e11b14-2632-346e-b985-50d6cc0c1ae2 | -10.82502 | -57.22742 | 2026-09-28 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0d546081-e951-3e40-a956-954ad7475298 | -11.12922 | -47.49479 | 2026-09-28 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d737b54-ba40-3760-9680-e48fba1d71ca | -10.2095 | -49.98174 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02a3ba9e-a832-3cc3-8e69-fff9a5faf6f4 | -11.83984 | -50.51318 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d854bce3-f603-35ac-8457-e8d153c9eb09 | -7.38028 | -42.11942 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7037bebd-c214-3749-b72f-8780c89e75fd | -7.71656 | -54.76663 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de5de7ee-2ed8-31d1-a75b-05bd3093837c | -10.8184 | -60.7453 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 72fde38f-a203-398a-94a2-d0788e13cea7 | -10.41602 | -53.82861 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6c003388-d2de-3fb1-b2c4-7cb1dbba35b3 | -11.3856 | -43.42443 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dafa31c2-4385-3005-8224-6cba0de65cea | -10.20333 | -49.99902 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 253519e0-8fbd-3e55-855b-5c0283c99ec6 | -7.28199 | -55.57878 | 2026-09-28 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 040a23d4-ba0f-349d-9980-0a74013b7200 | -10.82116 | -57.22071 | 2026-09-28 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3165ce9c-145a-3a6c-a270-b4722f93b25b | -11.1853 | -44.80847 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 9f670d37-549c-38e6-8635-f2d84242f908 | -11.59544 | -44.13403 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 388e149e-737b-3a97-a446-032d28e764af | -12.14433 | -50.35353 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cc256912-882d-3570-beb8-76a5f0c99185 | -11.19543 | -44.81991 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 474711e5-1431-3d9d-a14e-50e830e1b247 | -10.57699 | -51.28186 | 2026-09-28 04:34:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e28b77f8-d9d6-3355-aaf8-ef661a47eb89 | -7.78776 | -50.23116 | 2026-09-28 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 378eefc4-1db8-3867-b51c-42d2c7783bb9 | -12.83934 | -43.39479 | 2026-09-28 04:34:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7d07262-0bbb-3726-9540-6428b71ad1ab | -11.04131 | -54.0387 | 2026-09-28 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4d87e95-6cc3-36c1-bb7d-def6ad0935a1 | -6.99115 | -42.699 | 2026-09-28 04:34:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8c304f14-119e-3cbf-bc61-a8d8de6d5f93 | -12.68556 | -45.02261 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 357c131a-c92a-3b73-880c-6a529dbb7970 | -6.6773 | -45.6291 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebe400f6-5275-35a0-9e0a-3ee335097adc | -6.09006 | -57.63251 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7352c050-c58e-3a67-88a5-85ee09117acf | -9.77275 | -48.2112 | 2026-09-28 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91b0c5fa-d54a-3dce-84f1-22341da164e7 | -10.21725 | -49.99762 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24166d9f-5e79-362d-87b1-d7da5c2f5ce5 | -7.72095 | -54.76739 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67a4bbf2-806f-31b4-9927-50d08008da1a | -8.89547 | -46.19168 | 2026-09-28 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb8dbee3-da29-3f95-8d7e-eb1d5d758f31 | -11.11987 | -47.57961 | 2026-09-28 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36381129-5654-3766-952f-2226b505e099 | -12.6299 | -47.32391 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2bfbc3ab-16a9-3e9a-81a2-ad6acf9b784e | -8.59552 | -54.64974 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baa1d6cf-40e9-3bd5-81c8-b327c5574e8e | -10.89812 | -50.69066 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a289fba2-4f82-3870-88b0-5d8bdc199731 | -6.06761 | -57.82694 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f981b099-c44f-3440-8c64-bb2c98235fc7 | -7.06207 | -55.48518 | 2026-09-28 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49e4ce07-d032-33da-8751-1e0e9446c380 | -11.04071 | -54.04218 | 2026-09-28 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b9906b2-6dbb-3907-9661-71e0dccbbff5 | -6.94792 | -41.61713 | 2026-09-28 04:34:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8310e07e-30cf-3f0b-b824-8d6211296558 | -10.79684 | -48.73553 | 2026-09-28 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 98796ce9-a219-39b1-aee7-67e01f944aa5 | -11.43864 | -44.92566 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79e2785b-9f27-3611-a5c0-ae8fb701a4e8 | -8.95962 | -44.16894 | 2026-09-28 04:34:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8b58908e-b4ff-3a8d-946b-e0da42195428 | -9.77884 | -44.82701 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89d60788-10e3-3600-b4bd-d90ef5038bb2 | -11.52003 | -50.68394 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b538fdc-463a-3926-9d05-3a5ab5b90f79 | -12.73954 | -47.78783 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c98d1e07-232c-3889-993c-4f7cc39071f6 | -9.08235 | -49.87621 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 657d494e-b0d0-359e-9074-5d3a22aed1e1 | -9.98261 | -50.14659 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5319b6bb-a22d-3494-a0e2-ac14f1398d68 | -12.63334 | -47.32444 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5f8c5ac9-e165-3067-b942-c7e89dd8b91c | -8.03421 | -54.89311 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f0a56b2-7810-3ec1-98be-e19e27789212 | -11.03794 | -54.03453 | 2026-09-28 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86cf55ec-a242-3325-9965-df50f75be337 | -11.70626 | -44.52192 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04a4b90f-683b-3071-b177-641defb0be0b | -10.80355 | -57.2058 | 2026-09-28 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 035ac7b4-cb90-370e-88d2-abcd700f32c0 | -7.3318 | -42.08654 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 60a8c27e-e34c-3d1b-9d94-903861a24214 | -6.99061 | -42.70285 | 2026-09-28 04:34:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8d16ceae-866a-3950-a560-8193ed617cb6 | -7.70907 | -44.92057 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fb43c711-7839-37c7-978c-1c0f261789e6 | -9.66463 | -48.90781 | 2026-09-28 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7791dcd-4be6-38c9-beed-b946f27415d6 | -11.70944 | -50.60337 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 894ec5cd-3279-3bf7-9236-6b66683ce030 | -9.82091 | -45.25945 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5d582fb-2185-32cd-aef3-50216bbf3aeb | -9.14843 | -45.63278 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 735f1ceb-994d-31b2-8cf9-84ca6921c50f | -8.36725 | -45.45604 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bbbc0471-b370-3c9d-902f-8dc0263dbb43 | -7.26641 | -45.33957 | 2026-09-28 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 029eb2bc-46b3-3f98-9d1a-06888ed69008 | -11.18283 | -44.79817 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d792d1f8-6916-399c-ac31-58dcbafef4d3 | -12.62126 | -47.31078 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 485d8e09-540f-3236-8f67-def4ab913421 | -6.72151 | -45.59611 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de206bcd-8216-3340-bae3-689d6e14700a | -11.85807 | -48.88707 | 2026-09-28 04:34:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00c5e066-80fe-3586-8441-d277dc38b925 | -10.41778 | -53.81836 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6bf72dc6-a0c4-312d-9323-2e39f47d45ed | -11.20274 | -44.79602 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99ffd3d2-398a-35d2-843c-b59c1bec65fb | -9.97338 | -45.34242 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03a9f70f-8709-390c-bba1-25d0b4136cee | -10.90949 | -44.65726 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54757a2f-d9eb-3845-a1b2-9f0fcf7d69b1 | -11.70725 | -50.59556 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 15a8619c-1a20-30d9-b458-c7042b4cb4c2 | -13.451 | -46.31669 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1a5be76-5e61-3063-a98c-bf2959c19fb0 | -11.70224 | -44.54875 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04e0e02b-4627-36bc-af10-160084005651 | -6.30614 | -56.03009 | 2026-09-28 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74de57b3-4753-3c04-8774-f891a5f11b6f | -10.45309 | -45.09333 | 2026-09-28 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c16f0023-3a3c-379f-af14-e095e2bc6a88 | -11.38614 | -43.42043 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42bcc69d-8b9d-3233-a0c7-28725555258a | -9.92846 | -60.72313 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f7f93ba-27e0-3d39-823a-2ffd6e3bce61 | -10.24996 | -44.61703 | 2026-09-28 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05c5672e-de24-3299-8b57-f92e835bdbc4 | -9.97657 | -45.34518 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4c0a47c-751f-37ad-87f3-dfedcf40c5ee | -9.63967 | -47.65844 | 2026-09-28 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 622c4442-77fd-34cf-8f00-5ff26ec0c5fa | -12.74245 | -47.2971 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c7d20446-2adc-3a35-9138-c765dc607a59 | -10.11832 | -50.18728 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0e1870d-ab5f-36ac-b760-49a32b8e7b6d | -13.0713 | -48.51296 | 2026-09-28 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README35.md)
