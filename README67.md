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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a9936b7-4a03-3aa2-b80d-0a1a9482f3d5 | -8.52251 | -51.3802 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8e5d38a-c610-3484-ab52-26dbd30b39f2 | -6.42579 | -44.44152 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8de5da5d-68bd-337a-b66a-528db32fc133 | -12.14211 | -44.84563 | 2025-09-10 04:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f61204dd-cc2d-3f5a-a30f-79b32d5cea39 | -9.31767 | -46.72655 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 4f7f1953-f2fd-324e-b613-ae444670d6b4 | -11.11636 | -48.41782 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e594f82-f239-3271-b6e2-fc1643daf048 | -5.86212 | -48.16291 | 2025-09-10 04:42:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d46edded-ed84-341f-be3a-3b5982a4e1fb | -10.01593 | -51.69241 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d1d08ead-bf26-39a5-91f1-b1df12ba4849 | -9.67656 | -46.89365 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a957087-4e9a-3bea-b2ff-f4bdcec7a82f | -11.56978 | -44.66182 | 2025-09-10 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31cebfc1-be00-3ae7-b5dc-d6f8b1037188 | -9.76545 | -51.12292 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cc7c510-5e68-3019-af22-84216e68c4d5 | -10.028 | -51.66087 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ffae2da-5d76-3323-8e98-95dfd6f509a5 | -9.80872 | -47.7644 | 2025-09-10 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 068379fe-27c3-3ff3-806e-eff4aaab4c9f | -11.33556 | -46.52071 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 405f2183-92ce-35da-9e3a-0f7019f153c8 | -12.02028 | -46.76042 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fa4e62b-0d7a-3e07-a64e-d2c5944008b2 | -7.88789 | -46.26147 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d05da63c-3e66-37fd-9caa-1fde3b52a392 | -7.54847 | -48.2196 | 2025-09-10 04:42:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bfa5d91-fafc-3036-be43-4d6c6db3726e | -9.31288 | -46.71477 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17f2f409-40c9-367f-ac19-539717ade820 | -12.08255 | -45.47239 | 2025-09-10 04:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8d0acad2-f172-33b5-bc4e-7d94fbf9db21 | -9.05264 | -50.48547 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 418e0228-6f68-375a-889b-ba5c8ef6ae9a | -8.08568 | -52.34996 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c843d5c-9179-333b-9070-49606d882067 | -9.00883 | -49.53838 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ec8718a-0a13-36c6-ac9f-15417013a3ee | -6.85338 | -47.90904 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8052f7c-696a-3c7c-b764-d64d7348996d | -8.20228 | -47.15026 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 199dd35c-b4bb-360d-b222-88fddb7a1dbe | -9.05653 | -50.48251 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6e79e9d-7498-3a4c-b5c1-e41280e2f5ea | -8.42726 | -49.10473 | 2025-09-10 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95b6f025-fa1b-3cd6-b0e4-9437669171f1 | -9.08345 | -50.45812 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30221573-a9f4-3895-a019-82a2e0b6da86 | -6.85963 | -47.93608 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d52c8e5-6fec-3e1a-92e9-91753dcd6b54 | -8.41643 | -47.28189 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3b2cf73-4e51-3167-bb91-0542172c278a | -10.03023 | -47.84752 | 2025-09-10 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a993044-8f5b-3b78-ae1c-830dedb7b5c4 | -11.45993 | -49.27194 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d89cc423-2fb1-31c5-b56d-4aca534cd7ef | -10.89517 | -47.7614 | 2025-09-10 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a355f03d-232c-3628-bed2-7735fbd7a969 | -7.54794 | -48.24543 | 2025-09-10 04:42:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb1fa5d3-f733-30af-8c7b-cde7399b5180 | -9.51824 | -54.63924 | 2025-09-10 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 857e117b-7ddf-302e-a35f-ad3f6de01ef8 | -6.46707 | -44.11327 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2558bcb8-3b48-3242-a7db-a9cb8346b2c4 | -10.02785 | -51.6833 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c64822b4-e463-3539-880d-dedf1b0e7edb | -9.06139 | -49.81229 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9aa0913c-2cce-39ea-9a45-fb9aa927bded | -10.33738 | -48.26701 | 2025-09-10 04:42:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 929aeade-6ff8-3a8e-85f6-8392222c183e | -8.66453 | -45.74265 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8347e1ff-c874-32ea-a10e-bb0b333f6824 | -11.80428 | -46.7662 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1b3a3dd-dea6-37ce-9a25-e6090242b256 | -8.98667 | -45.72466 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4c3e2dc-5fa0-3c50-a7e8-a19c337674ec | -11.11016 | -48.36572 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5d8de46-e75f-34f2-ad59-4a73eb917ba5 | -7.09273 | -44.13404 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a730094-4018-37ef-a287-e01d258af63c | -9.75732 | -51.06663 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63d6db58-6d7d-3772-8be7-78486ce7d623 | -7.788 | -46.09426 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31f5dc44-88b0-32aa-888c-49739ba1630b | -10.04337 | -49.16391 | 2025-09-10 04:42:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef01e981-9cc1-3eec-9a7f-a3ab085c022a | -8.38537 | -47.99172 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ebed15ed-556f-36a0-95b8-09127a4b5bf1 | -11.84149 | -46.74815 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29db1208-2b47-31eb-a200-7bc2675cfcfc | -10.01223 | -48.08672 | 2025-09-10 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fd4435a6-47b2-373b-961e-adfe8d2d1d00 | -9.6649 | -46.64109 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 904f2fff-ee9b-37d5-a0a8-91bc60133982 | -6.35085 | -44.85505 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 73d8d7d2-1576-39e3-8212-cdd87d03fb3b | -11.57032 | -44.65776 | 2025-09-10 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aabe649b-8704-3b00-aacc-65855e1e54f3 | -10.5758 | -52.02962 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 269ab8e8-1d6a-3558-8b5f-c0ceb8c2c9e4 | -7.70412 | -44.84062 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0a90048e-7644-3ebb-a1d1-4a5da5011940 | -9.56317 | -48.01188 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14740b07-39b2-3ebf-97ac-64a378e7e5c3 | -5.48121 | -51.22503 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a75c86b-57e1-3347-a56d-2dfe82ecac80 | -11.46387 | -49.26884 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50f62167-e6c0-3c79-a49b-b6c4e0f21e60 | -7.46639 | -44.9384 | 2025-09-10 04:42:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ddd02cc-fdd4-3f56-89e1-0270741cb033 | -8.0475 | -48.68642 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 6caae617-19b6-3936-acab-30c524471017 | -9.5157 | -54.65412 | 2025-09-10 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06816f01-f11a-37ea-afe1-98b4da97f332 | -6.81291 | -51.8785 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4140d0bd-312f-327a-8475-c5daf586e251 | -7.69815 | -47.2954 | 2025-09-10 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d7d0891-49af-335b-9b67-e5dd2ecea954 | -9.21657 | -50.53693 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37a69653-335e-36b3-9dbf-8db75e37098f | -8.46815 | -47.29797 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2b4909d-3165-3e81-9a32-cca9af781416 | -8.04675 | -52.38867 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e77ca5d-1580-32f8-941d-91b7343cb25a | -5.90982 | -52.4664 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70dd463a-d36d-34d9-97df-512fe6336862 | -11.41721 | -43.57381 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f9f6b8a-8e9b-3402-9112-e6f2b440868f | -7.72134 | -50.34367 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13bddec8-1da8-3c92-a472-5f97a299dbae | -7.61335 | -42.54308 | 2025-09-10 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4dd546d9-b14f-3593-9f32-cbcd3993f88c | -8.06007 | -52.32961 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce16ee00-b486-3a9e-a0c5-fc3efcc871e7 | -8.70257 | -48.87902 | 2025-09-10 04:42:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9395df56-850a-3e84-ab18-2290c59c461f | -8.026 | -45.50278 | 2025-09-10 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7be47466-4fe9-3dc1-b805-64e6874ee82b | -9.66068 | -46.61806 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bcfe5d8-ee0d-394e-96a8-32f05c007835 | -7.08153 | -45.20028 | 2025-09-10 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cbfe71d7-327e-36f3-ad63-cd141be710f9 | -9.07326 | -45.70488 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e4666335-0083-38de-98d3-b551b1199f11 | -6.85507 | -47.89816 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69fbe931-56de-3444-af07-603e75338111 | -10.46899 | -47.94377 | 2025-09-10 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f0a2aa7-caa1-3206-81e5-b40b0e1cbb36 | -9.09264 | -46.96769 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 394b1c24-6e9f-3a77-b446-bc6f601eaba5 | -9.98453 | -50.30118 | 2025-09-10 04:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57b22741-a8f6-35ee-9bf6-a396fc836207 | -8.2086 | -49.51265 | 2025-09-10 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e943c384-d5a1-3439-8e50-e90f5926eb8a | -11.72802 | -46.70603 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcf712d5-a342-330e-927a-7be950c5eb73 | -11.68071 | -46.90325 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bb616977-7804-3043-85bb-a405e9c37323 | -7.86348 | -46.25992 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e4dc5e1-245c-3b2b-9734-601dc0bc39cd | -12.07977 | -45.47202 | 2025-09-10 04:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 63c186d2-8567-3268-b116-17c706e39520 | -9.06029 | -49.81928 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2a12922-ae6d-3240-a49c-5ad7cef919d8 | -11.37757 | -45.58536 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abe7b840-eb62-3335-bbbc-5b434dac1600 | -9.34684 | -46.75717 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7dc34567-7e24-3c58-89c4-76e2f927662d | -11.47827 | -50.41503 | 2025-09-10 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a9f198c-3529-3537-8a84-73a3287f3e82 | -9.31829 | -46.72227 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 97772ec1-a54b-3838-9ade-8a058e543365 | -5.72415 | -51.69383 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dc7839c-22b4-3e89-ad4a-22ff185afa67 | -11.18875 | -48.37391 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ceba1201-789b-3c4e-8a96-4525457cb297 | -10.01711 | -51.68513 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b8be9a00-daa3-3550-9cc2-7a57577cfe80 | -9.0614 | -45.73232 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 422c6e33-c5d5-3f8b-8dd7-512d89ec7abd | -11.4462 | -43.6022 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f67e607e-6fdd-30ea-9cbc-2522185fe6ae | -9.10465 | -46.98615 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43209807-c1a8-30b9-9efa-80c70fe66076 | -8.06929 | -48.66743 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6da2336a-a8a0-3e86-b991-be06ff260fcc | -9.4501 | -46.71357 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9262ec65-9e56-30e1-aade-c8855f2cd564 | -11.67385 | -46.8979 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08d4818f-acd5-336c-81bf-5c6e26559221 | -10.57519 | -52.03331 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 892a7f6e-c28f-3eae-8145-cd112c5f1463 | -8.42203 | -47.38769 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29612c69-04c8-398b-897b-98f1c049bd04 | -10.31104 | -48.80479 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README68.md)
