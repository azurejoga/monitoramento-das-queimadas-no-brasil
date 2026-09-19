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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5cb7093-27be-33df-b442-2059bfe4588f | -13.6476 | -46.94019 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8dfdd2d-ee71-36eb-9c78-5e0a06b16a65 | -9.95458 | -46.54804 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 873e308b-fdc7-3cdf-8628-4302eb56489c | -10.20855 | -46.59227 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93de0e9b-fd3d-381f-af83-7654d74c2440 | -10.69113 | -60.74509 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f5e4db4-070e-39d4-9357-12cc3746e470 | -9.55795 | -46.57862 | 2026-09-19 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69617987-abae-3d52-86c2-d46abd92bcff | -9.61172 | -45.38377 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e652399-b9f6-3b27-986c-d9539128bbd0 | -8.36262 | -50.83617 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b079830c-a2f2-305b-be00-7c562ef45fec | -14.66596 | -46.66302 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db82d3de-724b-384f-a823-4c53e2321089 | -14.15357 | -45.16345 | 2026-09-19 04:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a016feed-95e3-34ee-9ebc-c8992ad418b7 | -12.85815 | -46.33434 | 2026-09-19 04:40:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e934098-bcc2-31c9-83aa-b1062a289882 | -9.04385 | -48.71578 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cc5ebde2-aa93-3180-b288-346ee014308e | -11.07689 | -48.31362 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7f36184-23da-36b6-aebc-e8285683e34b | -11.30609 | -46.78833 | 2026-09-19 04:40:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 83415d88-2681-326b-98ae-39acf96b0d4f | -13.01734 | -46.97705 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4dadbe60-a4a2-3775-bb74-7115c4394f1b | -14.92981 | -49.92194 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5212f6c4-4261-388c-a7c7-4df39b05ff1e | -12.55712 | -50.69123 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dcf026f-c845-3e1a-af2f-4f77e39e376b | -12.12697 | -46.98471 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a4d24c87-9e34-355a-b1ae-174ea4f6d30c | -10.93374 | -53.95499 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 91c04e7d-8a78-3e05-837e-0b01bf7a205d | -12.3399 | -50.71621 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 600da28b-635d-32b5-aa47-72cc12ab4e42 | -12.1399 | -45.14472 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40404d58-75f8-3cd6-abe7-1a022c6df545 | -10.53635 | -46.73843 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 629c2b63-c358-3b5a-b472-c3fb32f4072c | -12.3363 | -50.71558 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8555c544-00e2-36f6-997e-746091f63e97 | -9.95403 | -46.55156 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 573eadd4-dad0-310a-a064-31f131b4832d | -10.85817 | -56.19206 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00b49c2c-3567-34c8-9e23-c3eb967c4f2d | -11.49685 | -47.72364 | 2026-09-19 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c3cb837-962f-3af3-baca-a66caa257b03 | -13.87797 | -48.5938 | 2026-09-19 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d9242da-8186-326d-8c9d-4383e73bc213 | -10.50568 | -46.72219 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecd4a48a-f04f-39a0-927b-ab1f121d6ebf | -9.95513 | -46.54452 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7a8a542-9e39-328a-842c-96bf67231886 | -8.49294 | -57.6257 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7d778376-fe78-3613-b2bf-db788617d26c | -12.17142 | -48.9519 | 2026-09-19 04:40:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa5500cb-20d0-3ffd-8759-3bdd76631924 | -10.85956 | -54.11003 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 55c4a1e2-de38-36ca-994c-7c0fb7897f92 | -10.83294 | -50.16558 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 420fd4eb-fb9b-303a-adce-ac4acf4e31ce | -9.56299 | -45.47405 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87f3aad2-cd8e-397c-9e26-3be2bf63ec58 | -9.89198 | -45.82664 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bca6ce8-98e7-3111-8a36-f39dcbde2fef | -8.87829 | -50.78651 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8f6f0e9-6fec-3742-8701-376bb8fd125d | -11.05337 | -48.30998 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1eec4b04-f21d-3973-9a74-611f0f1488a7 | -12.70516 | -45.94612 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c060bb5f-d484-377c-b84a-65c473c99d55 | -9.55351 | -46.58511 | 2026-09-19 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff344d53-b087-373b-a0f7-c06c6f644dbc | -13.73453 | -48.79126 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 781cfbdc-29ca-3c81-bcf9-9f30ff52f2e5 | -13.02112 | -48.64264 | 2026-09-19 04:40:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65a44cd9-4f3e-3c1c-b4ac-830e0edf0c02 | -11.51603 | -46.87302 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 62279949-5e44-35e4-bc0c-95efa3ae9616 | -9.76913 | -45.06371 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5ad8665-ec7e-3a4a-ba40-bbf2890d6c86 | -9.80247 | -46.09203 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 204d66f6-b072-3d4f-9411-8cd7488ed9e0 | -9.25069 | -46.20552 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f0dc19ac-d0c9-38ce-80b3-9cd8f19902a7 | -11.90953 | -50.11605 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd8dbe11-ccd2-31c0-8a36-42d62bc10c78 | -11.84142 | -47.44699 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61ec9c37-8ac3-3c4c-ba6f-15c49f80936a | -10.23906 | -48.84544 | 2026-09-19 04:40:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de1ba1a3-d41a-358c-8759-feab779a481a | -13.60612 | -46.9336 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ec737ef-919e-3f1d-8fc0-088a8fca3226 | -8.33948 | -50.74791 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca9af47e-3068-354b-bfe3-162afadad76c | -10.79513 | -50.8838 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48d3265a-c5ba-3169-87e4-a5d4f8460928 | -9.60831 | -45.38324 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0080930e-06de-3db3-8447-ded0bdecc17a | -11.32968 | -47.34924 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31fb1c7e-036c-3e45-8be2-695e4a86dac9 | -14.92854 | -49.92957 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bc6cdc25-a768-3086-b2a2-354d1f17f9dd | -10.91002 | -50.84349 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54141353-1a24-3ed3-a4cf-2aa1a71f413c | -9.82 | -46.3967 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2416fb9c-7aab-338f-8f33-ef35a5e69c1a | -8.61109 | -54.60474 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b828e198-fea8-3eb3-9a65-14cb95a80089 | -9.71633 | -47.13206 | 2026-09-19 04:40:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e05c3c9-bf10-3190-b35e-828b75c32158 | -9.04824 | -48.7319 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5db16c81-500e-3411-b2ff-9d97c4b92ceb | -10.00116 | -50.27568 | 2026-09-19 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20e95a2c-e561-35cb-bb89-e28f50900004 | -9.82676 | -49.22277 | 2026-09-19 04:40:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c6e2150-72f6-36f5-a16a-847b7ad1afb0 | -12.70175 | -45.94555 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bd6444e-2c6f-36f6-8c63-74ac364c1e69 | -9.04605 | -48.72385 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95826150-7ad8-3f15-b7a6-968fd1056d7a | -12.55187 | -47.07829 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2905c443-f94b-35d9-87d3-ac18af9fd5d1 | -11.30272 | -46.76607 | 2026-09-19 04:40:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e52a912-7e30-3f25-a9df-23e7658019ce | -14.7932 | -48.58145 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33c4a0a6-9f5a-33db-8d5e-0c33f67e4c54 | -10.63665 | -48.69832 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5377b60-fb97-32ec-aeac-43d9d408affd | -11.08658 | -48.27508 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44adbf54-9eed-326b-b4ba-ef64a74409e2 | -9.89377 | -46.54922 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 009e4bb8-eea8-3642-802c-653c91a1d6c4 | -10.86855 | -56.19625 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 156d9a49-5046-3a0b-86ea-88fe5fe669d7 | -10.53803 | -46.74953 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 280b5e9a-ca99-3813-a7f0-6570269989cc | -11.83564 | -46.83971 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6bb95bd-857c-322d-af0e-79426bffc655 | -9.24514 | -46.21914 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57c1235d-0f34-38a2-b0a6-2e99e68a0f57 | -11.94116 | -50.12117 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e8762ff-99f4-3ca0-9488-f5b08f28703d | -9.91961 | -46.57485 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88c3c5f5-4c63-30a2-adab-91129c4c7a8b | -11.06565 | -49.76292 | 2026-09-19 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 977a6031-d827-3a93-b2a5-9eeda1c2b35f | -13.60959 | -48.32918 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7114e1b0-3290-337e-860c-cca65179152c | -14.68467 | -46.67749 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92620b8f-0e1e-3682-956a-90ead0622d2e | -11.76946 | -47.43499 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c967728-f07b-3eb3-bed2-f40edd74ff8a | -12.69548 | -45.94067 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3981ba8d-43e8-3b20-b4e7-6b2b45f75ac0 | -11.11971 | -49.43776 | 2026-09-19 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd6f406b-8393-39ca-987a-ef173dd979c2 | -10.53652 | -44.84671 | 2026-09-19 04:40:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c3d9073-d5b5-3b25-bd52-e82b0e4ec3c0 | -11.08257 | -48.29984 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 31ae64be-79b9-3aaf-b69f-6308b9f8e9f9 | -11.00158 | -48.32375 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8941d110-9ecf-343d-b821-73630c7225f6 | -11.81062 | -46.83236 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf9dcd2d-b4c8-3a00-81b4-081a242e23e4 | -13.02125 | -46.974 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c93b3e00-2f0e-34a1-83ae-ad0a85f7a5c2 | -9.93776 | -45.28152 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5615dcc6-f103-3607-a557-7906309b77e4 | -10.20243 | -46.58768 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5632c715-e9ac-3ff0-8a67-8a64a796c859 | -10.92003 | -53.98018 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9448568c-5d79-3309-848c-0be0017cb4ae | -14.78653 | -48.58033 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 978e1be7-d175-3879-b48a-42d7c64541cf | -11.33189 | -47.35683 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c9dd3c56-c768-388d-8159-bbb266ebaf1f | -11.06311 | -48.27123 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 983e7e71-0d6e-34ef-b443-2b235b365bf7 | -13.01789 | -46.97349 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07a790c0-036a-344d-b0b4-2e0cf66c3f1c | -10.89969 | -53.99045 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15fe65ef-3556-3bbc-ad41-60c953a97acc | -12.69202 | -45.96328 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 395303da-c617-3065-8748-0897fb5ff6e4 | -12.26688 | -57.17704 | 2026-09-19 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0ec08ad-208d-335d-a094-f3ea69b0477f | -12.99838 | -46.98871 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 97d6eab0-b8f8-36df-a7fa-7f08c25a9442 | -8.1494 | -54.80472 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f4c6dd8-c1a4-3f35-9682-7f082f3bea4a | -13.73729 | -48.79544 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70f01ea2-0c5e-3642-acb5-2ec2ff5f9da4 | -11.12771 | -45.29342 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a6755fe-35bf-34e0-a03a-e3fd9fdea2b9 | -12.41558 | -45.03471 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README62.md)
