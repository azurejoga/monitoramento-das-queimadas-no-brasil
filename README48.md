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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2782d995-c886-3a6d-a985-64c0afceebcd | -6.54671 | -55.24939 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd2aa21d-a2e2-3508-8d5c-4a656f7cc96c | -7.35596 | -55.17238 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f7d8139-a4dc-3c58-8128-40bc267ac9c3 | -6.15449 | -57.79522 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3cfeba2-d439-363b-8839-51e7e19b7205 | -6.15897 | -57.79596 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a57d13d3-dfaf-3b03-95c5-fcfeed7d53fe | -13.31345 | -48.2041 | 2026-08-29 04:53:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27893a8c-021e-3362-8293-882255b88687 | -8.65902 | -54.75996 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86af5280-23a2-3794-b749-951c498e156e | -8.60145 | -54.71783 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceed94fd-2f13-3151-bd90-fba0267c9173 | -11.27323 | -54.04138 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ef2b0ce-3c45-3ea0-9d4e-7bd4a7248792 | -8.59046 | -54.76231 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8eda969-ed15-3b7d-8ca6-6d40ea99e216 | -16.51192 | -49.25586 | 2026-08-29 04:53:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0144274f-bc27-3b03-aea5-f9a195b01274 | -6.77031 | -55.67561 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b28e2e6d-e21f-378c-8ec6-d2d665c23835 | -6.93268 | -58.95545 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cfeaf88c-8c45-372a-a588-5004259e8193 | -5.98137 | -57.68895 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e9b2a243-cde7-37f1-b4d5-9e2cf8d1418a | -8.95311 | -62.38419 | 2026-08-29 04:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0da395d9-6671-31ad-8165-44218dd6448f | -13.65493 | -47.75717 | 2026-08-29 04:53:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f3475f16-c551-384f-a42c-8c14f3f1fb2a | -9.42263 | -51.68819 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85cfa16a-9101-3146-a2ab-1d67353a58b4 | -8.94767 | -63.28189 | 2026-08-29 04:53:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 30c18e53-8914-3515-8223-c84c2da0ca3e | -6.68177 | -51.96194 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1876e284-7953-34c4-9041-f1ce074e977e | -7.51533 | -55.30373 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 6a4b6572-5f0b-3a1c-a2cd-aae929fd419e | -9.72338 | -47.77069 | 2026-08-29 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de07e8bf-83a5-3456-aaef-2cac92de94b2 | -9.26678 | -45.64199 | 2026-08-29 04:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e5e6e9b6-255f-3be3-b9ae-13b4bce48c55 | -10.8091 | -54.02595 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a560494a-7d9c-32f7-9b0c-1b6b406ab7c2 | -7.48342 | -61.40361 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fcac509-62da-3443-8496-ce216a1becc6 | -8.9481 | -62.37891 | 2026-08-29 04:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e5465f2-57ea-3985-98bd-d5f58d214c5a | -7.48774 | -55.28498 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7bdf696d-62f0-30f6-91b3-74af8a9724b3 | -9.86024 | -65.03611 | 2026-08-29 04:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ac4fb00-aff1-3d42-b453-fadc6fca2797 | -7.17474 | -43.17434 | 2026-08-29 04:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b5a37f98-4cf5-3e30-bc3e-7bc4b59162bd | -11.83777 | -46.77376 | 2026-08-29 04:53:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cb3b6ff-8792-32ee-9f4f-0f0ad398420a | -9.92957 | -60.42418 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcd8013b-7585-3335-8d81-75e6c15cfffa | -9.43086 | -51.59298 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b62b31a7-58c3-3ead-822c-90d5ec346ddc | -10.75689 | -53.97911 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fda1e201-febd-3428-bbd8-754ada0d33d1 | -9.42391 | -50.4329 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 940066e6-cc28-3944-90fe-84ff539d55d2 | -6.27005 | -53.13941 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e46f718a-8752-3b4b-967c-154bd9247e5e | -6.77416 | -55.67625 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36b88dae-4d76-3d43-9ea8-59fc2c67b96f | -11.25931 | -54.02003 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52948224-09fa-3428-b991-e3c07258378a | -5.99101 | -57.68621 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fca96adb-d725-3eac-8f6c-1179d2315c05 | -7.86137 | -56.68186 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b00c059-2985-373c-ab65-1022d82c3c8e | -9.22761 | -51.56808 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5672ff7-eec1-38ee-9bee-9ac9e05c57b9 | -9.01806 | -57.54701 | 2026-08-29 04:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9d53f9d-46de-36fa-be16-561cb6f95d4f | -6.54747 | -55.2448 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fafebb4-b8f4-3990-8497-034dcd7bba83 | -6.17223 | -57.78582 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90dc2051-5d50-3299-90d5-f93d1ce5f36d | -17.59444 | -51.61594 | 2026-08-29 04:53:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19621650-e7c3-3eaa-91aa-1ac28cec5add | -10.88315 | -50.50079 | 2026-08-29 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce5a8aff-cb62-321f-b843-04d3db19c0d2 | -6.15805 | -57.78794 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 685f82ed-beb2-3317-b046-c4bb9131ef74 | -6.28015 | -53.1405 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 605cd697-78c0-38f3-bf30-5bba47473c4b | -11.03512 | -57.22272 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 86704366-7879-32c5-955e-db247c349fca | -8.94109 | -63.28161 | 2026-08-29 04:53:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9db6293-25ec-33a1-b849-bc7750f2e4b7 | -9.61489 | -55.11933 | 2026-08-29 04:53:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e67a35f6-bd69-350b-a646-6ff7a6c6ec0e | -11.23961 | -45.07944 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 866522ce-f870-31e3-835b-fc224411e94f | -8.97535 | -50.79379 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13f219f9-0a32-3135-a4ea-ade37bacaf63 | -11.20306 | -51.26606 | 2026-08-29 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a223fd4-5448-3761-be36-985c1b947499 | -11.76289 | -54.51899 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 833602bb-7370-34cb-8c15-d7fce0a3769b | -11.26427 | -54.03226 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f06d246-d3ca-3930-a909-bb3cb08c0ea5 | -10.50464 | -64.31117 | 2026-08-29 04:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a01e00a5-c944-3db7-96b4-d0a6ade8a8a3 | -11.02472 | -57.24594 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e58eded-d8d1-3afb-a5db-12ee1690c2ed | -10.32133 | -49.96209 | 2026-08-29 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de700db2-d9e9-3ae7-8084-f8c873149e82 | -9.60548 | -55.10909 | 2026-08-29 04:53:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb5d9156-de33-3472-b4cc-b32fda8af2ce | -8.98982 | -50.7888 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6d224d7c-9e93-3be4-8aa9-e23a8dc89f31 | -11.36282 | -45.16027 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 52b4b449-1143-3b5f-9a4c-6c7497d34085 | -11.2621 | -54.02429 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc77d136-2afb-3a91-ae74-93b4cb3e6564 | -6.15495 | -57.80572 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7830a33a-06dd-390b-916b-6237d68ce476 | -6.5437 | -55.24415 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a681b7c5-29bb-312a-8077-58bd4768517f | -11.19522 | -55.09725 | 2026-08-29 04:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88d240a5-9e93-3417-8de7-beca91a18c07 | -9.93347 | -60.43111 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf0581ca-b4d5-3d18-9d85-bba559cd16b0 | -6.88298 | -59.40432 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 627268af-58e0-3d99-8574-79ea3fe5b764 | -8.14893 | -64.00309 | 2026-08-29 04:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 241e1b3f-76f3-373f-a090-f654be7fe7cd | -11.14243 | -50.59301 | 2026-08-29 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06f9c92b-63ce-38ec-b153-c6f65b0fabed | -11.17854 | -51.26951 | 2026-08-29 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fd399dc-d870-33f9-94e7-fb6dd43d8f95 | -6.51499 | -53.60011 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe4299b6-1780-3322-99da-e8195c862371 | -7.2243 | -51.69223 | 2026-08-29 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 975aa844-1d3d-3f20-be75-57319b5f0bdd | -6.95035 | -59.48587 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82ba7814-a16b-3237-b8b9-8207dcb8e5ed | -5.76915 | -57.55643 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92325e58-01b0-353e-a4d0-03e82a6453bd | -9.92573 | -60.44479 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce93de01-e9da-3b6b-b086-7fd9a37dcab8 | -11.35937 | -45.1503 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 817d6fbf-47e4-3a46-985e-eec2e1bb9516 | -7.59198 | -61.34337 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3eed9919-8b14-3f4d-970a-2e3d322f142d | -8.98969 | -52.38372 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bee3546-1b39-36e4-81b1-2e2e3fd95789 | -8.95331 | -63.28409 | 2026-08-29 04:53:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f2da58b5-fee0-35aa-b43c-d6a2c2847388 | -9.4314 | -51.5895 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5d83653-c10d-30b4-90dc-733986f7b412 | -6.25901 | -55.39152 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c4500de-1857-35bb-96a0-540f12b92fed | -11.26922 | -54.04454 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af6645a2-cc28-346b-85b0-2ab2c1a053c4 | -16.72376 | -49.34073 | 2026-08-29 04:53:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9931c3aa-cf12-3eb7-8f5d-4d82072aa072 | -8.6057 | -54.71434 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9a2c24f-6bfb-31ab-b12a-2b94b2c74c75 | -9.24975 | -65.50369 | 2026-08-29 04:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d72fd0b8-3316-3071-9d60-618432d1ca2c | -12.18666 | -50.55864 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 86cdeed0-d293-3144-ab6c-0994e3a11f46 | -5.89876 | -57.75441 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f79737b-a6ed-3c3d-88a4-2042841cea85 | -10.89394 | -50.49867 | 2026-08-29 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd111310-e771-3366-befe-1df404eb3ba2 | -6.95077 | -45.23085 | 2026-08-29 04:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71528b5c-d071-32d4-ba26-abc0014729b3 | -17.27804 | -46.04086 | 2026-08-29 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69530c5a-4a38-3dfc-af03-22c7720e2ac4 | -6.26271 | -55.41631 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad14a1f8-5b9b-39af-8c08-e037abffb708 | -5.88984 | -57.75264 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| cc49ed79-0581-3b80-b572-798edbc0d062 | -8.59558 | -54.77591 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83dcc69a-1ca5-3119-89b0-334f65a6c0f6 | -11.60673 | -46.73187 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dad8836-3dcf-3217-96f2-c822b6f6000f | -5.88751 | -57.76632 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6d5ac47c-580b-3d9f-aadb-9159493f6a52 | -9.96835 | -53.931 | 2026-08-29 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7b3f72ba-a84d-3012-9a74-35df801ac881 | -11.18883 | -55.09202 | 2026-08-29 04:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae713881-432e-3e05-907a-d2d338403e66 | -8.97646 | -50.78666 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 334f2247-d5eb-3655-a50e-838c4f3a65fa | -6.26194 | -55.42096 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 04cbe377-2b8c-344d-a75e-14ea78c76614 | -9.42424 | -51.59192 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 417ad83d-c414-364b-930d-4c7498464d52 | -11.18963 | -55.1088 | 2026-08-29 04:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0dc95ed8-4c3d-3b8a-97cb-a1b046420b36 | -13.32759 | -48.18847 | 2026-08-29 04:53:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README49.md)
