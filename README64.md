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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94a4c2b8-2cba-329a-ae9f-dbb23564e04f | -9.25359 | -60.33464 | 2026-08-28 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d206b900-c2eb-3f4c-9e97-36f430894df6 | -8.51515 | -70.26733 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3b21bda-35c1-3ea2-b1cb-639078eb5a3a | -10.50008 | -64.49915 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 4986b636-f0ee-3432-af18-64e631bdf161 | -9.85162 | -65.01901 | 2026-08-28 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0b88882-8e3b-34c6-b0ea-1e8b14cf3001 | -7.53695 | -70.02635 | 2026-08-28 05:55:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d1bcf65-2764-3194-ac6d-b3758a75f35c | -8.83249 | -62.3231 | 2026-08-28 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad1bd15c-9512-3b2b-9e65-f0201c772b90 | -7.58932 | -61.32453 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 77f2d26b-c4c2-350c-a066-1713dc9d918b | -8.24224 | -70.49268 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5bb246b-431d-3791-aa43-7d2b1855d053 | -8.98762 | -65.43938 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 04f9d2f5-a4ca-36fd-a108-90c6168b2bb9 | -10.35459 | -64.46393 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa2c5c11-38bd-3d52-853b-b89b1856f3f6 | -9.13474 | -70.80013 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7dd9ed45-b46a-3421-8c56-646610c730d7 | -7.60224 | -61.33696 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0872b69-0d82-3160-9a3a-b244bd410ce7 | -9.53954 | -66.77322 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bc88bbd1-e453-300d-b661-26cd7dfc085d | -8.8518 | -70.78826 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9c17162-9afc-3117-a887-de46c18e9625 | -9.52943 | -70.50407 | 2026-08-28 05:55:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66815e39-7019-3f7a-86e2-6436268bf6b1 | -9.86162 | -60.26182 | 2026-08-28 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa8ca815-c305-395c-9cc1-3f9fa4df3bf8 | -6.16241 | -57.79009 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ebaa1dcc-74fc-3940-88a5-03b0d892aaaa | -8.23886 | -70.49213 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1227157b-c8ba-39ef-832b-a3d9a5b246d0 | -9.66791 | -65.53004 | 2026-08-28 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da02bd28-fe39-3be5-9647-2404ed922fb9 | -8.60292 | -70.21188 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 634b318a-82cf-3fa7-8a42-1f693cf021c0 | -8.99134 | -65.43996 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ecb914fa-dbb7-3245-8d3a-0d6395f9649a | -7.58525 | -61.31864 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cc02d2f8-5f30-37fe-8196-97d726c30aa0 | -8.99906 | -70.75156 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddd0a5d4-a577-3494-b82b-22be1b644fba | -8.85235 | -70.92017 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b346ee6-6edc-385a-962b-5820913b094c | -6.16181 | -57.79458 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b7633075-ff6b-3ad2-9553-256205fdfef7 | -7.60701 | -61.33767 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ef49d09-fbcb-3a3e-adcd-12ec95c79caa | -7.58862 | -61.32968 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cad451f5-1a63-3fbf-a09a-f036ccdc367d | -1.36367 | -54.63742 | 2026-08-28 05:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6327b98-a82e-3815-8aba-01c82608eab9 | -10.51065 | -64.51163 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 929919e5-d074-37c6-a093-fc98502f65f4 | -8.61174 | -70.66721 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c59aa88a-fb1a-3336-9bdf-4bc20ec58285 | -6.16121 | -57.79896 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6ca82e8-4458-3ac0-9da9-a2b58c2f5668 | -7.79415 | -71.95564 | 2026-08-28 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28199997-33d6-3798-89bf-7a4188097adb | -6.52688 | -55.25139 | 2026-08-28 05:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 563c25af-1822-3a0f-b401-ac6f2c7f5b5e | -8.59736 | -70.2037 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3afb1dea-2a46-3bae-9e55-c76a8d914c61 | -8.59902 | -70.2149 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 26fed59d-0d5b-397b-91ec-d3accb27bfc8 | -6.00239 | -57.82827 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a320ca6-24b9-3c8a-9565-3a2abf56ae16 | -6.24292 | -55.47715 | 2026-08-28 05:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71116277-ddf6-3875-bc7f-2beb99c63644 | -8.15543 | -64.00317 | 2026-08-28 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eedc3190-0f76-3bf4-b2c3-289b44ac85ce | -9.27595 | -68.78165 | 2026-08-28 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7a41ef8-bae8-32d4-a802-4ea00c025ba1 | -8.81635 | -62.31293 | 2026-08-28 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a0b44e9-bb54-3400-b312-5d4d09b09b13 | -9.85697 | -65.02311 | 2026-08-28 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c7130d6-bc1a-3073-8a61-0af4a97f5e9a | -10.38985 | -61.24414 | 2026-08-28 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| c4ac7587-da1d-36b7-9a82-25e38210a12a | -8.60627 | -70.21242 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38fa37d8-4fa5-3454-89ab-2f274ff24cbf | -9.20594 | -67.77869 | 2026-08-28 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5321eb74-c845-3a60-8a45-9928b88c370b | -8.5968 | -70.20726 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 975e8c0a-95ae-3844-9d5d-eb0b8514201e | -6.23691 | -55.47009 | 2026-08-28 05:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1f12db9-3630-35e0-abbd-ebbf1114ca6e | -7.57689 | -61.30615 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e80c0b83-9cdd-3249-8c48-8e421075665f | -8.44436 | -70.9006 | 2026-08-28 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43dd3795-3267-3a9a-b312-67c67b2c7670 | -11.09548 | -68.57131 | 2026-08-28 05:55:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e8b0a67-4235-393e-a522-36bc634d6f4c | -8.44495 | -70.89689 | 2026-08-28 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 780ea867-a5d6-3114-8b20-3cb81363bf61 | -6.83763 | -55.61486 | 2026-08-28 05:55:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 075eb556-8a06-3b4f-91ad-36ff106ebb77 | -6.16063 | -57.80329 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d450014-23f0-3476-a65d-55b62bcdc967 | -9.83523 | -65.06426 | 2026-08-28 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6a43af4-452a-39f2-ba8e-d138f53e49fb | -8.6381 | -66.53194 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 464a0881-0c7f-3edd-abdb-cf5a6c5bfaf3 | -7.53751 | -70.02279 | 2026-08-28 05:55:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bf6d85e-44f6-347f-b934-b496e280c6d1 | -10.3906 | -61.23826 | 2026-08-28 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2e4fdd41-5dd8-3d7a-90ba-e60a5d00fb5d | -7.77329 | -69.99511 | 2026-08-28 05:55:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68259b79-b0d3-3a91-9567-90ad096b764f | -8.32945 | -70.7158 | 2026-08-28 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7df708f6-8444-354e-880e-d6f28c5807f1 | -8.8793 | -66.90406 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 627e6676-3eaf-39b0-bdb1-c9f5d13e99e7 | -10.4991 | -64.50623 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 76a8edee-11d5-3fc0-8f25-ecc3ba50a6ec | -9.19974 | -67.77403 | 2026-08-28 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35b48141-9626-3de9-937f-3a6c1deb3f08 | -1.36706 | -54.63081 | 2026-08-28 05:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af4a117e-3d96-36d3-a7c8-aade6952ef53 | -10.50664 | -64.51103 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b8238573-9428-3376-a8d0-5b608be2205b | -6.53386 | -55.24441 | 2026-08-28 05:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 622dd09b-4b5e-3968-a617-edd946461b19 | -6.79756 | -58.74492 | 2026-08-28 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e0fff5c-d96d-3fb2-935a-38ebca6d9427 | -9.20839 | -65.7947 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54020dc5-983d-3cf3-ab8e-5c0b07184a8f | -7.58315 | -61.33413 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 365b50f9-0ef5-3437-b558-a73ccada7974 | -9.52608 | -70.50352 | 2026-08-28 05:55:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ae76827-d971-3233-a0e2-c38ea53c336c | -6.16894 | -57.78655 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f16eeff3-774b-31f4-9435-5cd6af819f49 | -10.51016 | -64.51518 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.9 |
| f4f290ce-bca5-3390-81e0-2a1d2201b8d5 | -10.10251 | -68.13408 | 2026-08-28 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 102b813f-053e-37ef-910d-b262fa15bcb3 | -9.42763 | -68.1257 | 2026-08-28 05:55:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e58b93db-1a0e-38fb-8b01-62bfac7c9a69 | -6.17428 | -57.79179 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6e914f6-29ac-3ddb-b01c-3acda8678747 | -8.82623 | -71.03773 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 769ce9b9-fb28-3f95-a8e6-883182b7dcc1 | -7.58048 | -61.31787 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4f656e85-fbf8-316e-b341-d9763bf9b29d | -6.53469 | -55.24594 | 2026-08-28 05:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5b26abe7-72d7-3f9c-b712-bace519a9677 | -8.59958 | -70.21135 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e0d0cc5c-9dfb-3a8c-bbd7-d3e2bc9b58fc | -8.59624 | -70.21082 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5211e84-a664-3f75-b6bf-bb0842b88ee1 | -8.98696 | -65.44387 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc5312b5-0ab0-30eb-b6d3-f0cf77154f81 | -7.61108 | -61.34353 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27620e65-299c-3f52-9a3a-92714a8cc298 | -8.68966 | -69.68393 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ad01651-807f-34a1-ba76-2f74e2fea77c | -9.27927 | -68.78217 | 2026-08-28 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d91444e-4e3e-34dc-9935-6e265d954f1e | -6.16302 | -57.78559 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 495d2af5-6c42-31cc-af6f-954a09e8db42 | -8.88219 | -66.90842 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87c95659-1124-3b82-be74-0008182a6153 | -7.57978 | -61.32306 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f5bf3437-f973-3104-b037-0f9ce74f131f | -8.826 | -71.03796 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 699ce7e5-c57c-3b05-b172-fb2564466416 | -6.76416 | -55.69813 | 2026-08-28 05:55:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d06259f0-57ac-3827-a02c-21fcf26d5f38 | -8.6334 | -66.53928 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24b5e2ba-76c0-33a9-9bc6-044db2c70f0e | -6.53305 | -55.25087 | 2026-08-28 05:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6b1d62fc-f866-3daa-880a-85c8a1950587 | -8.39323 | -70.73701 | 2026-08-28 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96d7e0f2-8e95-38d0-805b-aadbac6f7410 | -8.95066 | -62.3904 | 2026-08-28 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 912eff7d-3674-3ca5-bc64-caa4fd5b4c4e | -9.24834 | -60.33393 | 2026-08-28 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2cfa61b4-77e1-3c00-9e5e-469cf3be958f | -7.71623 | -70.0954 | 2026-08-28 05:55:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72e32362-f5f0-367b-96e0-df62a2ad1199 | -10.26741 | -64.50137 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90d6e902-c31c-38a5-9a1d-9aa6e2741583 | -7.57782 | -61.30149 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 87398c64-76ba-3310-9d0b-2d3e6b06f576 | -6.24374 | -55.47116 | 2026-08-28 05:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72910b59-1b64-3b4a-8cef-c4ba85100775 | -8.95457 | -62.39562 | 2026-08-28 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2a723a33-f648-306f-92d9-fd317385fc82 | -9.17941 | -70.89715 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e656543-0b23-3dc4-8095-ea15977172b8 | -8.60071 | -70.20425 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43700907-234e-3da4-a7fc-3023d7d4bcb0 | -7.49252 | -55.28567 | 2026-08-28 05:55:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README65.md)
