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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a7610ea-5f5f-32c0-b725-3ae262c48485 | -5.9479 | -45.8574 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1faa08a3-7b29-3747-a2d1-641c2504c900 | -3.09085 | -47.01035 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd11df91-e7d6-348a-9459-50e721d57fc9 | -8.55717 | -44.71637 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41db593a-3ee4-3c94-b7c7-cc2b2450e555 | -7.76527 | -45.77285 | 2025-10-01 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fda090a-c2b7-34fb-befc-2c18dbca3ea0 | -6.03155 | -43.78135 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07078698-08b4-3de0-8f1e-9231ef4e37c0 | -5.79712 | -43.07326 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 76e6c29c-cc9d-3c90-a594-f95d313be375 | -8.86646 | -47.64557 | 2025-10-01 04:19:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c251b4a-429b-31c3-85af-8085250bf4dc | -5.95291 | -45.86908 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4768707b-58ce-340b-9508-6d9c7ee1ec6e | -7.82499 | -46.98022 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| acb2ab14-a6d2-3dc4-a9c6-1a45d57d074e | -5.82731 | -43.93476 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d1b3476-cfc4-3ed1-8309-2d68f91ca1b5 | -3.10092 | -47.01602 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 78ffe83d-1821-36c7-a943-f49905da7436 | -5.88717 | -42.50708 | 2025-10-01 04:19:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d81157b2-3c3d-33c5-a821-02fa4c5479b7 | -7.02708 | -44.77576 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b87402e-1143-3138-b57d-ac6db1f80cec | -6.64722 | -42.03286 | 2025-10-01 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ff4f082f-191c-394a-8d2d-16c4ba7bd22b | -9.98165 | -40.50616 | 2025-10-01 04:19:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 39a9a4f3-8004-33d0-bd74-91fb3aa77f76 | -6.06383 | -42.68298 | 2025-10-01 04:19:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 36358d94-19fe-38aa-b7ee-b37718c0ef69 | -6.61314 | -44.26428 | 2025-10-01 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e727e1a8-4652-3ff5-a65c-a5fab50fe7fc | -5.41819 | -41.32277 | 2025-10-01 04:19:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3176fdd1-0cd2-3292-b7d3-5224d66ac8c6 | -7.45671 | -47.26143 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a506a23-29e7-3617-8f2b-2c92450c2f4a | -5.95625 | -45.86961 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c6d39eee-6fb4-325b-bf31-08fc82909c52 | -6.11002 | -42.65566 | 2025-10-01 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a8d0421d-f6d3-3aa8-ba4e-44a96438f7bc | -8.64897 | -46.61809 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c1ac0cc4-2844-3036-9816-a6df3548cd1d | -1.87699 | -48.39395 | 2025-10-01 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 928eaaa7-2af3-3064-89a2-21106825390f | -3.9157 | -54.56585 | 2025-10-01 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dfba4e5-35f3-3165-845a-c3a010c0e7cd | -5.81408 | -42.84924 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0f270ff7-4c17-3df7-bb6f-40b2c10b1ba8 | -9.93327 | -43.67212 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67983b43-168e-396f-aa95-cd68761f716a | -5.63925 | -43.89852 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e1fbd85b-1abd-3538-b2a9-b4c7e9517b9d | -4.43244 | -40.7586 | 2025-10-01 04:19:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 258f226b-5564-39ea-9655-80d646a85f7b | -8.64647 | -43.98365 | 2025-10-01 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7850d433-51b3-33b2-9b8c-1206aa8046d0 | -6.88255 | -44.52298 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bef2447a-48b9-31ad-9d79-1951d894bf0a | -6.66205 | -41.39368 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f716afe6-63da-3dc1-931a-4617300cc58d | -8.92201 | -47.58775 | 2025-10-01 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bdda48ec-88fb-34f1-b8ec-e71478f8a128 | -9.26665 | -45.6865 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b472c93-2688-31f4-ab38-9678d2b087cd | -5.81352 | -42.8529 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f5023f2b-7d86-30a5-baa2-75a8d3154f20 | -6.70596 | -42.95688 | 2025-10-01 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 55747dd0-bbd1-3825-9e53-1362974c5951 | -7.73824 | -46.20111 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d6f4d5e-e0ba-399e-8de8-1d47b0e2f7a2 | -5.94173 | -45.89649 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ea43d708-e978-3b63-a5ad-53834a3240f8 | -6.23718 | -45.33937 | 2025-10-01 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0a7ee95f-bd95-3cf5-9601-8c67f2ace4e5 | -6.69495 | -42.79977 | 2025-10-01 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3f4e9a89-234a-3857-a288-baeb7a617f63 | -7.47749 | -46.47128 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31758c93-5531-33d2-ab5f-48ef9c263987 | -5.91666 | -43.71004 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 946e0136-47ba-391a-a33b-c471a0cccf72 | -7.33927 | -45.23547 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90106581-d361-309e-9c8f-47554dcc18ea | -9.9406 | -43.64647 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a41ee037-e1d9-3d7a-a3d6-9d3809d13364 | -6.01781 | -43.80428 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 083035e1-8056-36cf-8504-a6cd65cadd83 | -6.11161 | -43.12862 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| daef77d1-8193-3829-9b74-71d05ea86ccf | -8.52631 | -44.67219 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22576f37-a2b5-3f95-96f5-efa1d4c06bc5 | -6.07678 | -44.34241 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c58d8d89-98f0-37f6-a345-51f75a44f8bc | -9.35505 | -46.33114 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c6844b35-7ed6-388f-a5e0-6ece3e99ff7a | -7.56337 | -46.77556 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40b84bf6-849c-3bd1-ae93-44b51368aa39 | -3.89565 | -47.17675 | 2025-10-01 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 698e94ae-735c-35f8-83ca-073ca487c4e9 | -6.08883 | -42.47172 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 84380be5-0d1e-3807-b16c-dcddbad474da | -5.86178 | -43.40531 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ceb7a1a-1922-39a3-96c7-2e4dc3b9a8cd | -5.15803 | -46.41091 | 2025-10-01 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4c1c6b1-8f11-3012-a464-48c5b2d55e67 | -5.64157 | -43.92735 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cc3f76d9-ca3b-371b-8f7b-e5b282be867d | -5.82893 | -43.92436 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a5e2c50-e3fd-3871-af7f-8eed96356442 | -6.08777 | -42.66372 | 2025-10-01 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 117ef17e-51c4-309f-bb9a-94f9fcface9e | -7.77134 | -45.71306 | 2025-10-01 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3530f7df-a2b7-392f-b766-3467ec9049e2 | -3.0967 | -47.01954 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| ca341a10-2b66-378d-840e-0ff80c214718 | -7.20927 | -45.47701 | 2025-10-01 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4afa395-aca4-32c3-9100-7c16b2bfb0f9 | -5.82183 | -43.94811 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 294267ce-9977-38ea-b712-e2f14d099cce | -3.81167 | -47.5904 | 2025-10-01 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a650d1cf-ada8-3fff-9916-336a5bf36b93 | -5.82784 | -43.93129 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9a5c6cd-1c21-3552-a906-a9f03ed86f16 | -5.98443 | -42.65166 | 2025-10-01 04:19:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c365dfed-42e3-3b90-9ad2-b36c5dbcd6a9 | -9.94172 | -43.63899 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67025c17-ee6a-38cd-8c69-6ff611763fba | -5.71009 | -42.84121 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5238f5ec-a00a-3fde-b641-48a77fa03111 | -8.65232 | -46.61864 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e96b6199-4ea1-38cb-8173-c030d571e937 | -9.39613 | -45.81397 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1026d00-b8a6-3013-8a82-eb352f288f34 | -6.05498 | -43.65213 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85f38581-2608-3cb1-b860-74abd06adc79 | -6.15356 | -43.8931 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dee03569-dc51-32c7-87b5-c842c081ee6b | -3.51575 | -49.44515 | 2025-10-01 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 238912af-6ac1-31fc-8d33-cb2a6d18f1e6 | -5.70806 | -42.69437 | 2025-10-01 04:19:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| be5cc41d-5fd5-39a1-b8de-73715fe04a36 | -6.98788 | -44.39398 | 2025-10-01 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79bcb727-89bf-3d20-ae98-8671d745ad5b | -6.4536 | -44.45894 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 924d7cb5-c6d7-370d-a980-632b7d6c705d | -7.25932 | -45.48543 | 2025-10-01 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d16ba01-ef30-34ad-be6a-c1a236658a5d | -5.77798 | -43.2871 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd3c2b76-cb14-309f-9941-a8701cf9d571 | -6.12425 | -45.90314 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 661469e9-f4a9-3e4c-8073-0198d51cbcf5 | -9.77678 | -46.22631 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b6f545f-1755-32ec-b13a-975cad9aa22c | -5.90188 | -43.91506 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b71b4ad9-5268-31f8-a3c4-5a74f5eab9e0 | -4.809 | -42.76075 | 2025-10-01 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0a421ee7-99d6-3b2d-9344-72bc809368f8 | -3.84608 | -48.9616 | 2025-10-01 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1423fc0e-4a55-37b3-ab21-0428152bf124 | -5.82737 | -43.95607 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1df2ea51-714f-3b74-825a-5f625044cd11 | -5.25754 | -42.90974 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 240fa641-71f7-3747-970a-0eb63f48e18f | -5.98385 | -42.65539 | 2025-10-01 04:19:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b82b1aa3-45b9-3e33-b4af-ff6a8fb8a8c3 | -7.46682 | -46.47328 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8b8cdab-5f55-374c-8aa0-867367c4d083 | -4.05429 | -49.31771 | 2025-10-01 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66b6b183-8f3c-367a-ad0b-ef194d8b447d | -5.70237 | -42.68587 | 2025-10-01 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fedf2e02-955f-3f5c-a469-97cb454a0b78 | -3.9904 | -43.1022 | 2025-10-01 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86eb32bf-a584-3a73-82e3-1a3b2380c8ed | -6.83114 | -42.98684 | 2025-10-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 47da6aee-68fe-3034-bcc9-1233435d246c | -9.3299 | -45.71436 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afc0253b-117c-3172-a5ed-a9dd25ee0d0e | -6.28488 | -42.49612 | 2025-10-01 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 44466ed9-32ed-36f8-a04e-06318abe01cf | -3.28213 | -50.034 | 2025-10-01 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8edd7a3-b568-3659-bc05-b4c9cb99282f | -8.75225 | -45.92447 | 2025-10-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| caecec53-7239-3bfb-8279-afa9237b848f | -3.35679 | -43.19421 | 2025-10-01 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f34492de-589d-36e6-a39c-8cd870a0d6e0 | -7.09878 | -45.55198 | 2025-10-01 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39285437-c94f-3b8e-9f7f-969abc01adfc | -9.80065 | -45.92554 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cd5d679-1060-3759-b7a4-1b33e5801fa5 | -7.02066 | -44.48766 | 2025-10-01 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c208b29-cacb-3eb2-89fb-c8e67afe9063 | -5.05844 | -45.60407 | 2025-10-01 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4ce4b90-2015-3646-b642-5341548cf119 | -4.5738 | -46.50365 | 2025-10-01 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 660da2a9-3ccc-3532-a014-47089352c5b0 | -6.05182 | -44.43735 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ea033cd7-f190-371b-95a4-21d220c13cce | -7.72152 | -47.22899 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README38.md)
