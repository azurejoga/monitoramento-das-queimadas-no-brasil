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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca5ee8e4-fa30-37f1-ab5e-fe9da98ecb33 | -7.27432 | -60.17744 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 317bca6a-fc5f-3159-b2b4-08de027bc7c5 | -12.49659 | -57.77752 | 2025-07-22 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 553eae62-a968-31f7-aabe-87cf0cd16e57 | -11.73272 | -48.18858 | 2025-07-22 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| d03206c9-e644-348c-8e24-2b44fbe06597 | -8.8856 | -50.15648 | 2025-07-22 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1313a0f3-1367-3bd0-8c38-d216e568f1ae | -7.97484 | -55.30076 | 2025-07-22 05:21:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3261ac3-34ee-363b-9973-1b14eaf9f4a3 | -7.27375 | -60.18098 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fff38d12-25ae-3022-a5fc-c259970c379b | -11.72634 | -48.18775 | 2025-07-22 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 441a45e5-e6f6-378a-9a5e-ff2bcbc07e81 | -10.09831 | -60.49431 | 2025-07-22 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f8db22e-2b77-33e9-ab56-e540766fc215 | -10.2338 | -48.06584 | 2025-07-22 05:21:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43fcb890-82bf-3a43-833a-018805d9b4fa | -9.86987 | -57.19329 | 2025-07-22 05:21:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f20e16f-92f3-3859-ae5b-9b195008ada6 | -7.97415 | -55.30539 | 2025-07-22 05:21:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17cce1aa-b59e-3f53-930f-1642c673d527 | -9.02173 | -61.23732 | 2025-07-22 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f38617e-666f-3ae9-8a7e-996f80f610ab | -10.05433 | -59.09864 | 2025-07-22 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ea1aca0-a5d3-3572-877d-6b4bba5de6d1 | -7.23253 | -60.19292 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cb97790-d3f4-3734-821d-386b6204b56e | -7.26705 | -60.1799 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f08cb57-6935-306c-9527-aa48f20d6ead | -9.62166 | -67.28191 | 2025-07-22 05:21:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b4e1d2e-ae7a-3006-b052-1e01668c35d5 | -8.74784 | -63.93436 | 2025-07-22 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebde3d79-bfbb-3672-bd02-00effb9ec246 | -8.89103 | -50.15717 | 2025-07-22 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adf31f8a-944d-37a8-9f44-9f1f90c4707f | -14.38274 | -47.75611 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6e2e8aa3-0dd2-3f7d-98a3-84e0c40e7118 | -12.49308 | -57.77697 | 2025-07-22 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 860c5bb3-fc0f-3e99-a0cb-0a4c9e1bbba3 | -7.24407 | -60.19444 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d79934f-7ff8-3d82-b3e4-6cebc6cc688e | -10.23305 | -56.76601 | 2025-07-22 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4aa33962-d7a7-3fb5-8aae-517aa35c5d79 | -7.25642 | -60.18183 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c64892ce-55c7-318c-9245-bd60654b3833 | -9.53701 | -58.33582 | 2025-07-22 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79030462-c04a-38ef-97c1-65b7a8c9139f | -12.49836 | -57.76547 | 2025-07-22 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3f3e06f7-2a33-3a17-8882-188ad52af0d2 | -9.38248 | -66.58302 | 2025-07-22 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce4abad8-2294-3626-beab-526fb10c032b | -8.96053 | -62.24021 | 2025-07-22 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce0760b5-2ff8-3d6d-9813-b03b219e2bbb | -7.25585 | -60.18539 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9cfcdef3-b048-32cc-90db-ebd33dfde8e5 | -8.94427 | -64.12553 | 2025-07-22 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4647e97-4267-30fa-945f-b1cc17a43919 | -14.78103 | -48.28907 | 2025-07-22 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6565cdb-0b28-3b95-b1d1-8fc6fe3872c5 | -7.23794 | -60.1898 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acc703c1-2a95-3fce-a88d-a993796f5982 | -8.89149 | -50.15373 | 2025-07-22 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b109c980-e776-3074-a035-0037899b5b64 | -10.30143 | -57.12665 | 2025-07-22 05:21:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 850356c4-96e7-3da8-922d-d80d20acb92b | -7.24522 | -60.18732 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bcff950-399a-3c07-9979-79f097d13fb3 | -10.22975 | -48.06583 | 2025-07-22 05:21:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00c7cdfc-feae-36af-abe2-46651579a8d3 | -12.50011 | -57.77805 | 2025-07-22 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9fdd0b32-acb2-3bc3-871e-300b63c21be5 | -11.9455 | -63.18105 | 2025-07-22 05:21:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7b258e4-fbbf-36f7-a76d-8cd503368535 | -7.29279 | -60.16947 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59567eda-2fea-3103-9f31-6532b0bdcaf2 | -9.46054 | -63.15112 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b60cf8e8-cb6e-3883-8e24-6ce4507accb6 | -7.29671 | -60.16647 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 03dd2733-8140-3a76-9645-081c22076a34 | -10.041 | -59.09651 | 2025-07-22 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3a4dc12a-3142-3b15-a33c-c3f7ebe51a68 | -7.28552 | -60.17195 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89dadd96-e9e5-39d1-b361-fad95b6fce39 | -9.46166 | -63.15298 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 731704f3-6b8d-3c72-be82-c34e61474fdd | -14.64204 | -46.83369 | 2025-07-22 05:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d4ad1f8-a1d4-3846-9114-b57935bfcaea | -14.38998 | -47.75208 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 12b06d77-021c-3be0-9072-efc078c598d4 | -7.29336 | -60.16593 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f8cae8b-d3ad-3ebc-ac64-96ee80d6f8d9 | -7.27881 | -60.17088 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29eb753e-e70b-3dc3-ae16-f938961379b7 | -7.28887 | -60.17249 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f0d69c6-b29f-3911-91dd-2fd979f53548 | -7.28665 | -60.16485 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf4170f4-dc1a-33b0-9025-4046cee27371 | -10.04712 | -59.10109 | 2025-07-22 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5b340bf-ced5-3e6a-a276-cc3e28be86d2 | -11.30879 | -55.11558 | 2025-07-22 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 550cac40-1b0a-348e-b094-c48e88536ef6 | -7.28217 | -60.17142 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1db2e4ab-2d1b-3f45-8269-2f20062c7829 | -7.27767 | -60.17799 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e9cc830-d1aa-343d-ad9c-25dd36976195 | -8.89196 | -50.15025 | 2025-07-22 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fc4588c-baa1-3dc7-b59c-1e183180ff35 | -14.77506 | -48.28246 | 2025-07-22 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a34edc93-d444-3647-9015-7f19ec4f08df | -7.26256 | -60.18645 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b55947f-2740-352b-a350-438f86394c6d | -9.13181 | -63.91864 | 2025-07-22 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c3116da-3944-33ce-87f8-6dd9306d6214 | -14.39628 | -47.75742 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 123df267-f315-36fd-9246-2d03912d80b5 | -9.97681 | -62.25501 | 2025-07-22 05:21:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d793bad9-3907-33a8-815e-bab2b226d87a | -14.38015 | -47.75566 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44a5877d-fef8-3604-ade4-e8a386201f74 | -12.50128 | -57.77004 | 2025-07-22 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d1082838-8140-337f-a71c-23c280e3fd0b | -11.73338 | -48.18316 | 2025-07-22 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7ca3788d-8ba4-3304-a9a1-3d956c0d82c1 | -11.9482 | -63.17903 | 2025-07-22 05:21:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1f8e639-1b8b-3355-af33-b3a93965fc68 | -11.24075 | -50.36596 | 2025-07-22 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cedcc84-1bb7-3921-b64c-27bd4a21b61a | -7.23679 | -60.19693 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea72dd0d-824b-3cc0-ace4-47dffcfa986d | -8.88018 | -50.15581 | 2025-07-22 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b5ae4ef-cc43-3556-bfe9-21b375f33084 | -7.24015 | -60.19746 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0458039-b472-3e31-8c5c-97396070015c | -10.10138 | -67.74635 | 2025-07-22 05:21:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8ea72ee-a9dc-38e5-b350-d0450236dad7 | -11.46051 | -48.16369 | 2025-07-22 05:21:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca42ef5b-dde6-3b28-b7df-27f9933f5092 | -10.05488 | -59.0951 | 2025-07-22 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c7fb86a-517c-395d-987b-a971c1aa4191 | -7.2704 | -60.18044 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8103366-0d56-3ca8-829b-49b8f199fcc7 | -7.25193 | -60.1884 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9c56020-f872-3d01-bd5c-507aef36defa | -11.94908 | -63.18167 | 2025-07-22 05:21:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f29c25e-4964-317b-8572-0af98db954a2 | -7.24465 | -60.19088 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ee85f98-1903-353b-9a00-6c41eb736406 | -10.10213 | -58.22482 | 2025-07-22 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2a9aab0b-ca9f-33b4-81a6-b6a82a61c5f3 | -13.6252 | -47.73433 | 2025-07-22 05:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7259d55a-877f-3005-984c-b8523852636e | -12.49718 | -57.77353 | 2025-07-22 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 31f8613c-c7f2-3a5f-ba27-950d194376a5 | -9.9733 | -62.25442 | 2025-07-22 05:21:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 035de73c-bf4c-3bc1-a91a-4a552b1c7abc | -10.04767 | -59.09757 | 2025-07-22 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f16f1146-6930-38a7-bcba-94c32657960c | -11.94106 | -63.84842 | 2025-07-22 05:21:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b23631cd-4dc6-3bfd-bba1-54913f0e2642 | -9.98032 | -62.2556 | 2025-07-22 05:21:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8623eba0-08de-3cf3-899e-031ec5b7eb7e | -14.38676 | -47.75776 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d87d65a3-b666-38ad-b96d-9f320c7c75ef | -12.5007 | -57.77405 | 2025-07-22 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 04dde93d-9e7d-3407-8633-5860d9e1fa28 | -7.23343 | -60.1964 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29a9aa27-362a-3d76-b221-38dd8951019e | -7.27489 | -60.17389 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3aa4185-f6ab-3b27-b7a8-4074eeebb475 | -7.97106 | -55.30019 | 2025-07-22 05:21:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84def1b2-ebdb-3bd2-990d-a0d2970e77cb | -9.55801 | -65.98854 | 2025-07-22 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| edd0b2e8-31b0-3d14-a071-e847762e195e | -9.24769 | -58.76219 | 2025-07-22 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cc8de28-0722-3e22-bb39-b5c8d67a4611 | -14.39359 | -47.75784 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d806e734-b8ce-3933-8680-7af60f301c35 | -14.3889 | -47.76279 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f953e1a6-ef0d-35c2-be4e-55585c7bc15d | -10.29789 | -57.12612 | 2025-07-22 05:21:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fab7ab26-e7f1-345b-a06a-badc01807c2e | -14.38942 | -47.75761 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8b2cd099-96db-38ed-9fc2-ecb4d6247bd9 | -14.64918 | -46.83447 | 2025-07-22 05:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 511df486-60d4-34f7-97a7-36b7fba342f0 | -10.29661 | -60.54502 | 2025-07-22 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74d3d308-840d-3837-944b-73f214f99431 | -9.46238 | -63.14861 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe854172-b385-3767-983e-b6127e73a305 | -7.28103 | -60.17852 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 396d65f0-a585-3f3a-bdd4-db0d0dee3097 | -10.05155 | -59.09458 | 2025-07-22 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18a92d04-edc3-3f37-af5c-1499d30b14a0 | -10.5574 | -50.38155 | 2025-07-22 05:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c277a89f-4a1b-3ff8-a225-1f1d2877a6dd | -14.38378 | -47.74577 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e30d0aa2-107b-31a1-bbd1-93fd55cc4ff8 | -12.2595 | -63.82178 | 2025-07-22 05:21:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README19.md)
