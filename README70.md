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
| 2fc4ea91-8ad5-3091-b222-65fed5d2fd6a | -6.16794 | -57.78669 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de2e3deb-47b3-3bb8-8084-882aedb364de | -10.50183 | -64.5238 | 2026-08-30 05:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7a2af41-b3bc-3966-9723-c0439be0d880 | -9.93192 | -68.55582 | 2026-08-30 05:55:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7fc0fb02-c972-30da-a009-c664b1b3f2c9 | -6.61412 | -55.4522 | 2026-08-30 05:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca9f47f0-4595-3b56-87f8-bb5ca5c08598 | -9.3869 | -66.51149 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67bd146a-9b40-3ad4-a69a-120cd5bac10e | -3.62978 | -60.55101 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 508560f9-14b0-38e4-b120-564cfe100b74 | -8.7408 | -69.56869 | 2026-08-30 05:55:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69cb1f2e-916f-3a0a-9c0b-f8b5211c9285 | -9.03511 | -67.61708 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50fe75ff-5599-37b2-bf8f-0c11ed860195 | -9.93639 | -60.51225 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3d9a382-6def-3a20-8bd1-1c69bf002466 | -6.15622 | -57.80379 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fdeb28b-3fa1-34c2-b7a0-d7c570c6b721 | -8.92802 | -67.37101 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ac3eb55-dbca-34bd-a1a2-4803759a8a5c | -3.62439 | -60.54813 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22930d5e-74fc-394d-81eb-50028f26220c | -10.57044 | -59.61516 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dee46790-6861-399b-b8ee-0da5b7090f39 | -10.01457 | -67.69724 | 2026-08-30 05:55:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fe64a5a-fd0e-335b-aa34-aaf1b52cfd2f | -4.95847 | -55.84243 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 0e6bdd69-f6c6-3ad6-98c7-aea51e7f1b01 | -4.95955 | -55.85081 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 069e2794-58ca-3062-b6da-c42fc97dc050 | -9.75004 | -66.7579 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff52d3e5-e99e-3202-9556-5ba5f3708fff | -3.63604 | -60.56165 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a07e3357-1627-3015-b9e7-3cf7ec7d35fe | -10.49244 | -59.60719 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4f8c6d78-f3ca-3e58-beed-62a91a4f9a18 | -5.48185 | -57.15532 | 2026-08-30 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5bc8902f-0dd9-395c-8a67-08c672253e49 | -6.1801 | -57.77509 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2707c44d-661a-3e48-bec6-6c09bc234657 | -8.88174 | -71.26379 | 2026-08-30 05:55:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1d5fd7a-366c-3271-931c-ce1957890018 | -10.48698 | -64.50616 | 2026-08-30 05:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9dfaffa8-6f21-30a6-b290-396790ff7bb6 | -4.15487 | -60.69524 | 2026-08-30 05:55:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ac858ab6-0c2a-3423-ac35-e6158ccae42e | -9.93583 | -60.51619 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 452666e9-54d0-3189-bd11-169ab999ed26 | -5.48432 | -57.1384 | 2026-08-30 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f1e53c98-ae27-3079-b9e8-fee42cae024d | -9.03232 | -68.50832 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2f0d34c-c17f-37f8-b5f6-53becd74d059 | -9.97633 | -60.26171 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2be6d733-3e08-3b41-b256-391ea054953d | -4.96003 | -55.84738 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e3263de7-e51e-35d9-a500-81bb9bec0bd4 | -5.48351 | -57.14396 | 2026-08-30 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 55a87b1e-5594-3228-83c8-f0a1e3c5d749 | -4.96097 | -55.84069 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 29060e69-6ecd-3ee5-a99f-ff8cadf61819 | -15.12435 | -53.57704 | 2026-08-30 05:55:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1be7e6e9-b986-34e9-9fa1-77832d222ce1 | -5.8781 | -57.771 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9a79ba9c-7ecf-3fdd-a847-d3d2d6f41190 | -8.87693 | -71.49053 | 2026-08-30 05:55:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1a20d61-84f5-3ee1-9a22-7c422f4d5316 | -9.88993 | -64.98896 | 2026-08-30 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a1642d8-a084-3fa5-8136-9abfa43a4d22 | -5.87884 | -57.76583 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 41b2541f-8b3f-37d5-afc2-8be78f70f8b0 | -11.19179 | -55.10754 | 2026-08-30 05:55:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fd0462d-e0cd-38d5-bd00-de11eb458b80 | -5.96825 | -57.68389 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fe6beda-94f1-3127-8b8e-1e2af7b45b9c | -5.97839 | -57.68968 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b357e80c-2bfb-3182-84c3-1ce5724509e1 | -9.18056 | -71.63616 | 2026-08-30 05:55:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e357ea5e-f3af-30be-bf71-0ed32863ef45 | -11.44238 | -61.48838 | 2026-08-30 05:55:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24000fed-c55a-3bbf-b028-0f59c53cfd7f | -8.91612 | -66.95266 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f6fd6d4-8c7c-31ab-b0ef-e5eb063e59a6 | -3.61511 | -60.5439 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 156dbbc8-fecd-358f-9e2e-ce5fe8a674f4 | -6.16869 | -57.78132 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61e91cf5-b5ac-3254-832b-5814159f6918 | -8.60042 | -70.21422 | 2026-08-30 05:55:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d5b65c1-48c4-3938-af62-b5e098fb9e85 | -14.15942 | -52.82049 | 2026-08-30 05:55:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e91c9a6-e38d-3019-916e-acc7aec2e5b2 | -4.96389 | -55.84306 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 57a512e8-2471-3551-a46e-93f9ce3616ff | -4.9605 | -55.84401 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 82ca45ed-385f-3400-9ba1-49372fea56b7 | -6.15775 | -57.79335 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49ecd0b1-32e3-3197-9c63-2f9683bcdafb | -11.04261 | -57.2154 | 2026-08-30 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccba7ef9-c8fb-3223-8513-d2b2048a5970 | -11.23727 | -54.01168 | 2026-08-30 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8355a002-1dd1-3717-896f-8b0821f9ae2a | -9.50719 | -65.58002 | 2026-08-30 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e487ce4-42e6-3e6d-b256-d6160d9695eb | -4.96593 | -55.84464 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 937d1e7b-95e6-3fb3-95e3-a3ea32d51563 | -5.96953 | -57.68287 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 443f0be9-714e-34df-bfa5-731e1d9ac49d | -3.6322 | -60.56108 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7554ecb9-fca3-35d4-8248-8d1aa4fb003c | -3.72894 | -60.6068 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fad02897-e449-33c4-8794-fb8f306a2013 | -3.62906 | -60.55577 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d2a336e0-3056-386f-ad36-640be01ecb51 | -11.23989 | -54.01216 | 2026-08-30 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d6527a9c-a494-39ff-bf5d-99d0f62ddcdf | -6.07907 | -57.898 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e5f7e614-b191-3772-a26c-be0b57b1d2ee | -14.16015 | -52.81327 | 2026-08-30 05:55:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 978362b6-c331-329a-97d5-87ef121966b0 | -3.75946 | -59.33542 | 2026-08-30 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4cc8d156-6049-3b87-b48b-76f68a0a9e16 | -11.70877 | -54.53379 | 2026-08-30 05:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 660a8c2f-b224-3260-9029-da9bf50dda6f | -3.76363 | -59.33605 | 2026-08-30 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4334018f-7846-3d3c-aeac-c37c6d012d55 | -6.15853 | -57.78807 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c510c1b-55cb-3242-9cef-d98ecf137338 | -8.92919 | -67.36376 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4ae997e6-9405-3c6d-8239-4b4e6ffc3c95 | -4.96438 | -55.83973 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 60193a1c-9d7a-300f-8bff-f7f395671b0c | -8.91984 | -66.99348 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d9fbdab-635d-3e8f-9170-83cb532fd9d1 | -6.11553 | -53.56157 | 2026-08-30 05:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f65684f-525d-31c1-95a3-c01887434152 | -6.15371 | -57.78739 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9de2bcf4-05bb-33f9-8169-5a24fcb19670 | -5.96549 | -57.67683 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2948c00d-7f51-3bb8-a7c1-e2ef435e666b | -8.60345 | -70.2197 | 2026-08-30 05:55:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8bf22f4-392c-3e9a-a673-015768c8568d | -3.61359 | -60.54161 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 372a0f30-010c-3a79-bec4-937439fbee3d | -6.16893 | -57.78418 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ee1739a-4786-3c28-9efb-4bac49d7c056 | -9.44565 | -66.73734 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1eb9cdd2-ed39-3c52-a1fd-9b76063c46bd | -11.6306 | -54.5885 | 2026-08-30 05:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2611c57b-f6a2-3c32-9744-c4f6e9533294 | -5.4885 | -57.14463 | 2026-08-30 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c874d29b-d568-35b2-aaa1-587b3a713ddf | -6.15698 | -57.7986 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24a23c1b-3899-3db4-a1a6-b69a53395476 | -14.15287 | -52.81219 | 2026-08-30 05:55:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d68c841a-842e-33b0-87b2-a06a5cbcb10e | -5.87659 | -57.7816 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 933363ba-315d-316b-ac47-eef14fa7ecff | -5.47852 | -57.14328 | 2026-08-30 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 18ed277c-9eb1-389d-b23f-b92622247d5c | -3.45254 | -61.71624 | 2026-08-30 05:55:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18346b60-5d59-3677-8d97-d56e1a8a379d | -5.96876 | -57.68814 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6909f5c-5d6e-3d7f-a3c8-feeca3351cbd | -11.03725 | -57.21462 | 2026-08-30 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9b56fc9-3228-3c24-a79a-476cea42e6df | -19.08569 | -57.39939 | 2026-08-30 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 97f00b2c-c0e8-3ce3-ad83-111d3674b6f8 | -19.07981 | -57.39874 | 2026-08-30 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f44a275a-fb50-3e63-8b92-7401f7579c9c | -19.48036 | -57.56472 | 2026-08-30 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f97d3807-9498-3882-8a74-5ce1da6599d8 | -19.4728 | -57.56526 | 2026-08-30 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ec623fed-f7c6-363a-b93a-9ccac34ac216 | -19.09346 | -57.40303 | 2026-08-30 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 71ea9ae0-3644-33fc-912c-1f51587116b1 | -19.08215 | -57.39735 | 2026-08-30 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| bee2bb2b-5973-32e0-860b-9f2a5e75290c | -19.47864 | -57.56594 | 2026-08-30 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7e918e80-8d07-3790-9419-ff3f67c6cc0f | -19.47451 | -57.56406 | 2026-08-30 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| abac1e26-85af-3f41-8f86-71171cae1fa9 | -19.09157 | -57.40008 | 2026-08-30 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 26a80096-7db9-381d-b017-265983eb583d | -19.08803 | -57.39801 | 2026-08-30 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ce9346e6-7ac7-3c41-a463-aa34186b793e | -19.47408 | -57.56836 | 2026-08-30 05:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 336020d5-a6f9-31b9-bfab-dfc84f06e178 | -9.8927 | -60.2752 | 2026-08-30 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 3fda08e8-551a-36d0-966d-8693609e7a94 | -11.8018 | -51.0556 | 2026-08-30 06:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| c5f0bdbe-2776-3fc9-9b41-456476e6766e | -5.4876 | -57.1416 | 2026-08-30 06:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| cb31c72c-8c48-395e-b1aa-b27532883e80 | -4.9604 | -55.8424 | 2026-08-30 06:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 92926196-c3d5-3f09-8d91-95917d5c382e | -11.8021 | -51.0343 | 2026-08-30 06:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.2 |
| e018c560-27a0-3a6a-9681-3d4ae1cdd5d7 | -10.8062 | -45.3178 | 2026-08-30 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |


[Clique aqui para ver as próximas entradas](README71.md)
