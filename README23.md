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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38021156-f7e0-3cc9-a334-bc37a2fc733c | -10.83505 | -53.76105 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 943b924a-f577-3973-9d29-f2ce60ecc0c7 | -11.19431 | -55.92513 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc7ae673-e2ca-3c95-84ba-0afe82382d25 | -11.01343 | -45.24487 | 2025-06-28 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c731f75-26eb-30d0-990d-4fa5797fe02e | -11.57664 | -52.11377 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e7002c54-a0ee-3704-a742-1d670d286ee7 | -11.18241 | -55.91634 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60a689fe-d0e5-3104-972e-167bff2f8889 | -10.04026 | -59.36046 | 2025-06-28 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f51ff560-1540-3d4b-b729-25e0a53209b8 | -11.86672 | -52.25612 | 2025-06-28 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebd021e4-43d5-30c9-bd4b-60069a8e2070 | -16.45465 | -49.51859 | 2025-06-28 04:51:00 | NOAA-20 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b0a6cc4-ddae-3c04-b5c5-e908f5a09f90 | -11.04907 | -55.07777 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d26d932b-a68e-3391-b74c-850baf2cca34 | -12.11425 | -54.58552 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dc0c531-95fc-3f3c-91a6-2af4523fff86 | -8.85635 | -50.16429 | 2025-06-28 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b95b58e-4e64-3967-84e8-173e83d81269 | -12.52301 | -57.21038 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1667e0ef-7063-303f-ba8e-49c95593c53c | -14.01576 | -54.4854 | 2025-06-28 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41aff8c3-32b2-389f-a9f2-47190d533362 | -11.60755 | -47.61166 | 2025-06-28 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2dc47c9-0124-3bb3-97f3-81d24a5d3d0b | -11.18179 | -55.92014 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df42f4c2-6ef5-3dc0-a8c4-5437d8f57e68 | -10.52762 | -53.62172 | 2025-06-28 04:51:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ddcd1b7-47de-3dec-a78f-aa214589c287 | -11.78084 | -59.32189 | 2025-06-28 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00256d05-2568-3b80-886c-8db9839c8d86 | -10.82789 | -53.74198 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2af356f7-b0d5-38b2-9833-4417e4965555 | -10.84222 | -53.75862 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90c72e07-9369-3266-8b15-6a985bc4abb1 | -12.10317 | -54.59095 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d9d803f-ab4c-3641-b321-c2dd52851394 | -10.84553 | -53.75916 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c23abac5-1f50-30d3-8378-0c42ea1007ab | -8.568 | -51.5713 | 2025-06-28 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb5d02e3-f72d-3305-828d-47a34b386c8a | -8.56123 | -51.57026 | 2025-06-28 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70e5b798-d133-3e99-ac66-44ff8e8b6141 | -13.29415 | -57.09371 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc765a23-9f07-3a7a-864c-8fe11c8e0a8a | -7.89227 | -61.4634 | 2025-06-28 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 769f2ede-2f62-3b33-a5a6-7098d67ef8f2 | -11.61344 | -58.29053 | 2025-06-28 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64f3ce4a-ebb6-372d-8c81-6e2b485f3749 | -11.84017 | -43.79419 | 2025-06-28 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbd251a2-38b0-3593-8883-35320a4c07c4 | -11.88031 | -58.72724 | 2025-06-28 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 74f025b3-484a-3491-b08e-c86ccf166b44 | -10.29554 | -57.13277 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bbfe7e8c-a926-3a69-8ebb-3f6d4bffb267 | -9.08814 | -59.48423 | 2025-06-28 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34505297-e76c-3584-8dda-bcec09685706 | -10.27504 | -44.64322 | 2025-06-28 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9a8d8d0-b190-3a1f-9641-a6b2d30b7d0b | -9.71732 | -56.18626 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 90573a11-8207-3af9-aaa7-89a9ba606e02 | -9.36508 | -47.63013 | 2025-06-28 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd86168f-7760-3b3b-ac52-db2fc0999dc2 | -9.69742 | -48.33069 | 2025-06-28 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f96be9a4-db6a-3f78-a2b1-a73f559c41fc | -9.70673 | -56.18448 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 5531c854-c451-3f58-9a86-824ee51bd919 | -10.03819 | -54.32951 | 2025-06-28 04:51:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 135d12b2-6421-33e1-9ac2-06b6573cb295 | -15.26224 | -51.4735 | 2025-06-28 04:51:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37957008-afc4-3ccf-a462-a52233574ac7 | -12.52373 | -57.20617 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1827ef45-07cb-378b-98e0-2cf44622828a | -10.82384 | -54.04619 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 641b7ab4-8b72-3604-a0b6-8a92473cf475 | -10.95583 | -48.15355 | 2025-06-28 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4a92ee08-2075-3d3d-ac6a-cf0ac4e9820d | -11.05164 | -55.38239 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 96c558ae-c377-349b-8ce3-0ee9cded008e | -10.83836 | -53.76159 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a190c99-7ce8-3888-b86e-4947d98b6b3f | -10.84497 | -53.76265 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce3501db-2349-3b25-827f-29b2cd4ee915 | -10.30289 | -57.13406 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 287892b3-49bf-3cf0-a21a-00c7f7d38e01 | -11.57436 | -54.51843 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc5994c1-427b-3073-b3d8-f5e459307ea0 | -9.36874 | -47.63468 | 2025-06-28 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c954d28-7452-3bc4-bcd4-d3be9298e016 | -9.72151 | -56.18286 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8485d3db-3a9d-3768-bf15-1a516d5feeb6 | -10.95245 | -54.36959 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98b69f28-0f10-34fa-96f1-5831d522878a | -15.25863 | -51.47294 | 2025-06-28 04:51:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 277d2431-db8b-3b6a-bd43-7c105fcea6fb | -9.42621 | -63.4589 | 2025-06-28 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2db24ce1-1dfa-343c-ab22-062518cf70bf | -10.82844 | -53.75998 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96a83061-c1ee-33b7-8892-f83373cb8a4c | -10.8334 | -53.75003 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88514f1b-071f-367b-ae9c-8e97a215d96e | -9.37294 | -47.63531 | 2025-06-28 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7231798-1a2f-3ba9-8809-c12682ec1e93 | -10.84167 | -53.76212 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14c1026d-c5ca-37c8-b664-0d03fc7746c3 | -9.4374 | -63.46122 | 2025-06-28 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b3f1801-be3e-363f-917d-03377e4ec7b9 | -11.05223 | -55.37871 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9cac36c7-e74d-3ca0-bc81-562e8df1d79f | -8.84146 | -49.85752 | 2025-06-28 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4045b923-d5b6-3cd4-87b0-10c3345f2656 | -11.5806 | -52.1106 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97556242-4a5e-3d3d-8c9a-71a5f77fbb45 | -9.69337 | -48.33023 | 2025-06-28 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5933d912-ed37-3ecc-b29e-70495577c1b3 | -8.56744 | -51.57496 | 2025-06-28 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9943c41-0d2d-306f-a27a-ad773a06dee3 | -9.16952 | -61.40461 | 2025-06-28 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4151f414-5738-3c78-8060-278f1bd31322 | -10.8266 | -54.05023 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e491010c-c58e-3012-ad1a-08431ae86806 | -12.03301 | -48.75051 | 2025-06-28 04:51:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0c2baa4-ed97-3a0e-91b3-95a6bfdd54e0 | -9.70739 | -56.18047 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ecdcca87-1e0b-3803-a39b-edb561064e48 | -8.56067 | -51.57391 | 2025-06-28 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 547b29b5-c1c7-3fb2-8dfa-e76fd67cf136 | -12.10487 | -54.58033 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 211b8bbf-0780-3158-860c-8694f83aa6bf | -12.2591 | -46.77629 | 2025-06-28 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8ed68e51-f1bc-33f6-a92a-962526f7bc2f | -10.50282 | -53.58551 | 2025-06-28 04:51:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d967393-747a-313c-b372-aa242c30ba94 | -9.17092 | -61.40543 | 2025-06-28 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cefdfbaf-d25b-3008-b4b3-cc1ef706f62c | -10.83395 | -53.76804 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c346c2e9-0190-3937-a055-ba905badb081 | -11.44143 | -54.47856 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c8e8ceb-04dd-3667-92fb-b6e322f0b633 | -10.00792 | -48.12914 | 2025-06-28 04:51:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d48b3bb-49af-3d77-8641-3a631e2e2f0d | -11.8776 | -58.74282 | 2025-06-28 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf4b7ff8-c3a0-351c-802b-fb5b8b061bb6 | -9.43438 | -63.46457 | 2025-06-28 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2144706b-44ca-3a1a-b734-3362351692ec | -11.77524 | -54.36704 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 100c7395-9ad3-3c52-b980-09d23830dd33 | -10.03933 | -54.3404 | 2025-06-28 04:51:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65f8b1bc-93c0-361a-a9db-bf8bfd8c2e99 | -10.82569 | -53.75595 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c28336c-ca9c-3a32-93ab-33634e72d5a4 | -11.32429 | -51.44744 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc063c08-a7d8-36e4-a79e-fa53d6473a34 | -9.13191 | -63.91877 | 2025-06-28 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d528e55-b270-31f3-9d66-84d9e9a48ae7 | -12.5223 | -57.23618 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dd99e58-c860-3c59-aa95-11a44a8040ee | -11.04885 | -55.37813 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 27fd29c6-9ca5-3da7-a1dd-8e86cb7f853f | -12.10431 | -54.58387 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fbf701f-67bc-39b1-81a8-3ffe23604dd2 | -11.27735 | -52.75264 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70073fc7-7d73-3506-a802-6946318008e4 | -12.02549 | -57.08688 | 2025-06-28 04:51:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dca663d-e81b-3dfc-85c6-5f5a7a2be78f | -11.56772 | -54.51734 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ba97858-7b81-3652-9010-7d9e82e9eec7 | -11.26788 | -52.74749 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| b51361da-78f7-3064-9e07-af64f1c684e7 | -11.88155 | -58.74351 | 2025-06-28 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a83cdc44-8c61-3a20-b086-48b00d1b6a72 | -11.57044 | -47.62403 | 2025-06-28 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4f0d1d3-df5e-33ea-8fb7-6b67799d2638 | -9.36929 | -47.63076 | 2025-06-28 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 26298d30-efa4-301f-8cc7-ccb9c8eab12f | -12.66014 | -54.10015 | 2025-06-28 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e72fa080-7702-3546-b0d6-f4bf015dc8b6 | -10.8132 | -57.74698 | 2025-06-28 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0184700e-b87e-3b00-9ea1-d6ab0447440e | -11.05004 | -55.37078 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2ecec8a2-b420-3f78-9567-401fb7055881 | -13.13953 | -56.80734 | 2025-06-28 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5f3113b-f702-347a-9ade-75b8363bfc85 | -11.57041 | -52.10899 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c15ca646-2ab7-3056-a0f0-25d89ef0ced8 | -14.69452 | -53.39317 | 2025-06-28 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8d85a8ad-de85-3c67-ada5-b665b4e98b4e | -14.69507 | -53.38951 | 2025-06-28 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 585617ce-f3db-3083-8b4e-aa59147d0697 | -12.10932 | -54.57382 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa250c76-77d1-3b89-9ef3-d5ef274f49f5 | -9.70253 | -56.18793 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39f175d8-4f81-3293-aad3-9383d0012e12 | -11.04825 | -55.38181 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f86ae4c7-273b-3d7d-a32d-484e32d54210 | -9.43479 | -47.96029 | 2025-06-28 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README24.md)
