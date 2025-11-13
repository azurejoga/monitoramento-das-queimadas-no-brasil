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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8ea51d9-ab92-3f55-a155-b294141b0eb1 | -3.9261 | -41.886799 | 2025-11-13 00:14:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 37ff9939-949e-338d-a1ca-4735940c0065 | -4.8948 | -45.236401 | 2025-11-13 00:14:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23843430-8e3b-3e5a-832d-215f77ffd31b | -7.1128 | -42.700699 | 2025-11-13 00:14:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7fb998c0-15bd-3d1b-abc9-9379ff9699e9 | -20.212099 | -41.7994 | 2025-11-13 00:14:00 | METOP-B | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2f1873b2-5b6d-3988-9040-3b8dd91efb27 | -2.8949 | -48.0802 | 2025-11-13 00:14:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8c57fa-b17a-3aa9-85ca-5737f0ae456b | -3.4018 | -50.440601 | 2025-11-13 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e7f0bbf-d093-3af8-bb20-878c92e694ab | -3.2093 | -50.182301 | 2025-11-13 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0807d97a-ffe0-318b-a8ed-01df512ace19 | -14.0987 | -43.446602 | 2025-11-13 00:14:00 | METOP-B | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb0ffc9c-a789-32b8-aaac-9a9e946ccc3f | -3.8596 | -49.778599 | 2025-11-13 00:14:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4be30aa-6251-3370-af0b-ace0b2e01a5f | -4.2457 | -49.6633 | 2025-11-13 00:14:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c9253b9-15ae-301c-a5bd-db3d3417eeb9 | -8.7307 | -49.588402 | 2025-11-13 00:14:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 948649cb-32b3-39e9-87ac-b1cdf7544560 | -4.5651 | -48.4869 | 2025-11-13 00:14:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfdb1564-6291-3215-903b-d365b03c3af2 | -11.0222 | -44.625 | 2025-11-13 00:14:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b6f2eb8-b169-374e-aa75-8827f1482c74 | -3.648 | -50.1632 | 2025-11-13 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6bc9717-66fa-3e5f-abb5-d1148c3a28ce | -3.0368 | -50.285301 | 2025-11-13 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1896721d-a921-351c-9e26-213b003d73b5 | -4.2535 | -43.780602 | 2025-11-13 00:14:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f51aa78-b9a6-3a30-be86-f45c239245e4 | -3.4827 | -45.8494 | 2025-11-13 00:14:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6a699561-f7a9-3cf3-ad0c-44acf8044bba | -5.8859 | -46.435101 | 2025-11-13 00:14:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc899989-e6d2-3632-9cde-b2fba28a275e | -2.6331 | -49.189499 | 2025-11-13 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d734fcf4-aa71-368e-a4ab-92120ce946e6 | -3.1501 | -45.481201 | 2025-11-13 00:14:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 433c69a0-9849-3172-b25d-49dde5c96fec | -5.869 | -48.644299 | 2025-11-13 00:14:00 | METOP-B | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1188da88-3cd5-397b-842a-9761b8f63a02 | -3.4391 | -45.573002 | 2025-11-13 00:14:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 298d69e5-5964-3b47-9751-3728d17af41d | -2.4531 | -49.259201 | 2025-11-13 00:14:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8314c7e-4f64-3981-8e77-5ca7e9a00b49 | -12.599 | -48.329899 | 2025-11-13 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e265e45-e884-3d88-add2-a5ac8e40f4e2 | -14.1011 | -43.4562 | 2025-11-13 00:14:00 | METOP-B | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40bd547b-1241-3c69-b909-b213268f0e47 | -3.0945 | -49.269501 | 2025-11-13 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 290a9ed3-6fef-38c4-a54d-9da7b61eeff0 | -5.8706 | -48.651299 | 2025-11-13 00:14:00 | METOP-B | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 750a1066-c474-3d89-aa48-38341f9bb93a | -3.8627 | -49.792301 | 2025-11-13 00:14:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54021dd4-cdfd-324f-92ce-e5697f1c2674 | -9.6368 | -44.5313 | 2025-11-13 00:14:00 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b539ff28-c838-3bda-83d1-96a981c10cef | -4.1055 | -48.010601 | 2025-11-13 00:14:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd6e486b-d67e-3b25-9be8-1d433571e9ff | -3.0861 | -45.737 | 2025-11-13 00:14:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 73f65676-fd54-3910-9577-cea2e5fac582 | -3.4637 | -50.577702 | 2025-11-13 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faaa85d6-1572-3b17-8e6d-b1b865c6bd6e | -3.3133 | -49.460701 | 2025-11-13 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ddeb366-3e24-3fdd-8abf-302ac0bd309b | -8.4117 | -44.0257 | 2025-11-13 00:14:00 | METOP-B | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d0cc1b34-0f40-393b-ac00-3949c6c6e14e | -7.1419 | -49.120201 | 2025-11-13 00:14:00 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| df571078-18bc-3675-b09d-fa6251bc680c | -7.7872 | -43.7873 | 2025-11-13 00:14:00 | METOP-B | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 955261a1-5ef3-3bb3-b1bb-41e2877d7416 | -3.3538 | -49.819901 | 2025-11-13 00:14:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eb5ba4c-a824-3221-a5c3-cb00c7d62fe6 | -3.1485 | -49.461399 | 2025-11-13 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbd3c998-d5b9-3900-a205-a13c9c0309a9 | -7.7935 | -42.619202 | 2025-11-13 00:14:00 | METOP-B | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 09187cdb-667f-3bd1-9c1f-b5910269b4f6 | -6.1542 | -48.0434 | 2025-11-13 00:14:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f2aa4e2-388c-3f4a-b4c7-a9b4e14111d2 | -2.6346 | -49.196499 | 2025-11-13 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71cff88d-bc4d-3703-88ae-5859c53993e3 | -2.1521 | -45.5695 | 2025-11-13 00:14:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a02e0b21-e2e6-3613-8aac-72ee7f50bb5e | -2.7184 | -47.400501 | 2025-11-13 00:14:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e5f9c1e-8d2c-3073-9978-19d9489a0923 | -7.5587 | -47.244499 | 2025-11-13 00:14:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2678402-4609-3238-b135-557b7508dd62 | -3.0913 | -49.2556 | 2025-11-13 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a51dbdcb-32ff-39bf-99f4-b2f7e55ba19c | -10.5532 | -44.8241 | 2025-11-13 00:14:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2d7b04a8-bb4c-3317-9d2e-059c1ea12819 | -4.5198 | -46.411499 | 2025-11-13 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8de0ea3a-7a14-3ff4-8a14-47c39b1ec262 | -6.4904 | -46.995701 | 2025-11-13 00:14:00 | METOP-B | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe216ca3-c71a-37ed-90b3-c8ac11da8ecc | -6.1444 | -48.0457 | 2025-11-13 00:14:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a46df29-06f6-3f6b-8124-88e77e890729 | -7.7774 | -43.7897 | 2025-11-13 00:14:00 | METOP-B | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 03319c47-4571-351e-9553-25ad573f20d7 | -2.0615 | -56.598202 | 2025-11-13 00:14:00 | METOP-B | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77779422-20cf-3868-984e-c1fcbeb45025 | -3.489 | -49.962101 | 2025-11-13 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cf68f4d-1136-3bdf-9812-e7eaa3fff924 | -3.3117 | -49.4538 | 2025-11-13 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b40198dd-efac-3e74-a212-b0ab73b19b11 | -7.4692 | -42.556702 | 2025-11-13 00:14:00 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b1f690a1-aea0-3a26-89d3-07a3e0426459 | -9.9462 | -44.4865 | 2025-11-13 00:14:00 | METOP-B | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f319c423-4d80-30f8-913c-b05f2fdd716f | 1.4605 | -55.824799 | 2025-11-13 00:14:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71a4d21e-947f-318b-b74e-e859622abab8 | -17.622499 | -46.698799 | 2025-11-13 00:14:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 788270f9-b928-32d2-a8db-ed43b3104952 | -4.3113 | -48.2341 | 2025-11-13 00:14:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fad3b24b-6e37-3c74-8b98-2a7e895b5cd9 | -5.0927 | -47.461899 | 2025-11-13 00:14:00 | METOP-B | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 63d5bad6-2560-3cd1-a84f-f7d038613441 | -3.1463 | -50.268101 | 2025-11-13 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bf2f35c-f200-3c57-ad31-163482e3e51c | -22.220301 | -46.743999 | 2025-11-13 00:14:00 | METOP-B | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4a374c9f-dfeb-3fdc-a80f-8f94e3392231 | -8.4696 | -47.978001 | 2025-11-13 00:14:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01287b8b-7491-356b-864f-b23390dc4437 | -13.0 | -49.7808 | 2025-11-13 00:14:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e15b676e-d93f-3c82-8f96-34822dc43299 | -10.928 | -44.619301 | 2025-11-13 00:14:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d62b940a-844d-3fba-83f8-e45f85a47a8c | -8.869 | -49.931702 | 2025-11-13 00:14:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e501f1b2-fd08-36a2-b7ab-9bfba23efff8 | -3.4034 | -50.1749 | 2025-11-13 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22331148-c67d-3f65-aaae-baea481b28f3 | -12.0659 | -48.202702 | 2025-11-13 00:14:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b78fd324-43da-3beb-960f-d2567fb0a4c1 | -4.5316 | -46.4179 | 2025-11-13 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0cd4988d-95e6-30ee-9172-b2edc06ed254 | -7.5232 | -40.066898 | 2025-11-13 00:14:00 | METOP-B | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 961cec3e-3c90-3ab7-a94d-cb21bc729eb5 | -6.0267 | -43.4925 | 2025-11-13 00:14:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0dd1b493-5e23-3c7c-8c40-303526e648f7 | -3.0961 | -49.276402 | 2025-11-13 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65a912b6-6f3c-335d-b8c9-c5cc1c1acf57 | -7.1161 | -42.7141 | 2025-11-13 00:14:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b810b452-3df0-32dd-9108-78d15dba01a2 | -2.0099 | -54.448399 | 2025-11-13 00:14:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbd48797-3394-35ed-b900-e302b1ba48b0 | -9.9365 | -44.488899 | 2025-11-13 00:14:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aae6c08a-56b0-3c40-a49f-07bcabf1384b | -13.0254 | -46.5229 | 2025-11-13 00:14:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0d506668-44a3-32bb-ab7b-a11acfac3e81 | -4.6943 | -49.641899 | 2025-11-13 00:14:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac6ee571-ce64-33c4-b050-60d0ed826baf | -4.9374 | -48.537201 | 2025-11-13 00:14:00 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b0bc75b-1842-303f-b995-ba1ce71ae53c | -3.7794 | -46.018299 | 2025-11-13 00:14:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 43f212bf-e431-3eec-b85d-9d53d79da3e7 | -4.1072 | -48.018002 | 2025-11-13 00:14:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef5ede49-607c-3c78-994d-b6a08d961aa1 | -6.9576 | -46.342701 | 2025-11-13 00:14:00 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d14528f-cda4-37b1-84fc-dabc92cece91 | -8.7291 | -49.581501 | 2025-11-13 00:14:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0468de22-b484-3215-8015-f681304d7250 | -3.7695 | -47.714901 | 2025-11-13 00:14:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d70f971-c339-398b-883f-27bdb5173084 | -2.9496 | -45.548401 | 2025-11-13 00:14:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c17dd51c-ff9a-3d77-b5fd-0f83aad45781 | -8.7124 | -44.2477 | 2025-11-13 00:14:00 | METOP-B | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fe374aba-c908-3d88-8e1a-337c54a12e88 | -6.3074 | -43.805401 | 2025-11-13 00:14:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d97f196d-fbaf-3811-b5ad-b13c7fb691a6 | -3.153 | -50.252201 | 2025-11-13 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4917784f-f70b-30db-af84-33310f9b55be | -11.7353 | -48.5205 | 2025-11-13 00:14:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5e62a3f-60d5-39f1-8968-e115b5cde1d7 | -5.3236 | -44.7822 | 2025-11-13 00:14:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3edadcfe-7d8d-3641-9169-b93b8d56ce24 | -7.4184 | -46.549599 | 2025-11-13 00:14:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7355b3b-6d16-3a37-9464-fa88403e6269 | -10.8489 | -44.938999 | 2025-11-13 00:14:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 84f2af04-864c-3b9d-9bf7-4510a4e2f73f | -3.3686 | -48.393501 | 2025-11-13 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bbf6d18-96e6-306a-8da3-b6aa615bd269 | -2.6384 | -52.076801 | 2025-11-13 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc481eba-6af6-3582-96e9-1858edb90be8 | -10.9236 | -44.6012 | 2025-11-13 00:14:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5dc88d85-d4df-3638-b133-c2a0c6fb9f3e | -2.6316 | -47.292198 | 2025-11-13 00:14:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba4ce8cf-35b1-36e0-adaa-1a898363af39 | -4.7253 | -46.719898 | 2025-11-13 00:14:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3dc4b96d-7446-3aeb-b364-17f85f91d7b4 | -6.8793 | -42.8419 | 2025-11-13 00:14:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fce775ca-7dde-3d9d-9bea-7ccdfbdeaea0 | -3.6655 | -45.9268 | 2025-11-13 00:14:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff91b7d-b746-3d22-a907-d898f97fda4d | -17.6241 | -46.705898 | 2025-11-13 00:14:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6e62fa48-b742-38d9-b924-717ba86954e9 | -5.4425 | -47.683102 | 2025-11-13 00:14:00 | METOP-B | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89a1d4e5-2fc1-3f63-adff-04a873579975 | -18.027399 | -51.0168 | 2025-11-13 00:14:00 | METOP-B | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
