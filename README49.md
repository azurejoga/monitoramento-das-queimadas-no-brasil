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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1819e290-617b-3dce-86ed-e16ca0c153ae | -5.92865 | -47.31957 | 2025-10-30 04:25:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5ec3997-c814-3a3b-82bd-12895e9b49c9 | -5.50768 | -45.4541 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fab54be9-6b0f-3010-8ce6-1fbfa563e981 | -9.8062 | -47.57996 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a5024f2-6ea4-349b-8b63-2e7ca41e01d9 | -10.37018 | -44.74577 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea52523e-210f-33c5-a92e-7ae76987f6bd | -6.78898 | -39.1495 | 2025-10-30 04:25:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 89fd39ba-c5e8-31a5-a9b9-24a6a14ac5d9 | -4.96358 | -43.54661 | 2025-10-30 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a798d356-c13f-3128-8c1a-791caed5c960 | -11.12187 | -47.74747 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a9f6a2b-5517-3ae4-92f9-d6a7b36f4c0f | -8.29218 | -49.3181 | 2025-10-30 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d5c2032-a370-3904-903a-22fd22f62aba | -7.32948 | -47.2565 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d46142f-a8d8-3bbd-a863-a7467a21fead | -10.88059 | -45.07673 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2071a652-2a4a-3565-bddd-b20be924487e | -10.47739 | -45.03645 | 2025-10-30 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 595b056a-a187-3816-ab34-6f0b0796c4ba | -4.99402 | -44.16097 | 2025-10-30 04:25:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c0b92c8-a5d4-3897-ade7-86dc4b72919e | -7.32447 | -42.47738 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c54caaaa-f928-303c-bec5-14b8244656f2 | -7.95302 | -46.73104 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e1edee8-7285-3d9c-90af-1bcc229f6405 | -11.9719 | -44.03666 | 2025-10-30 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c1c6196-26e6-3fe4-b44b-90314e94aa90 | -7.40006 | -43.93825 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3faed789-8442-33d2-b92b-22ec8eaa6204 | -8.26284 | -43.92537 | 2025-10-30 04:25:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b85242e-61c8-3085-800b-67a9a55ced48 | -5.58623 | -46.54927 | 2025-10-30 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 91d3d3c4-f1ac-32d8-8fef-94649c39e96b | -5.62203 | -47.1175 | 2025-10-30 04:25:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28510e40-b12c-3fd0-8217-e7e7d33c462c | -10.90861 | -47.99805 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c509c776-d4da-38cf-b627-07bc94a1f7e7 | -5.79775 | -40.82016 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5193c72c-bd4a-344a-9ac2-3fc469928745 | -4.33407 | -47.89337 | 2025-10-30 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bb8329f-ebff-3720-96d3-85f93cc00b93 | -6.17319 | -41.60673 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 87e2d791-9e14-3550-a883-7adc96c09c40 | -4.35273 | -48.1987 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72fb311f-86aa-304d-aa54-edd063ff00e1 | -6.29423 | -42.88067 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b8270c2-ebd9-3b82-8229-faeb25c7e18a | -5.42053 | -45.03384 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57dc8f7e-be0e-3b9d-bae0-fa8058b00943 | -11.72105 | -41.66238 | 2025-10-30 04:25:00 | NOAA-20 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3f6581b0-241c-3524-9a92-81a48c9a6fcf | -7.95687 | -46.72809 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2d3e97b-9f86-3f24-9e70-a3811ad218ce | -7.87274 | -44.23207 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 573707f7-84df-3eac-8859-b8c4aaf793e8 | -8.06836 | -45.14837 | 2025-10-30 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5820424-f562-3905-9aac-c738e84977c6 | -7.07851 | -44.93766 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bcc31e45-8933-33f3-bd8d-a96ca2916fe1 | -11.86322 | -44.73937 | 2025-10-30 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88e10183-3b52-3b12-bef5-b8624795a1e7 | -7.50298 | -46.74093 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 358421fc-51db-398a-be84-7b4e5678f095 | -5.46153 | -40.87253 | 2025-10-30 04:25:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 34c5d235-fa86-3bc3-afce-288862f8a690 | -10.49293 | -43.32643 | 2025-10-30 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93ab2e4c-2c6e-3f36-8303-2104ba5e7620 | -7.06116 | -44.93845 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8e203c7-d97b-38a3-86a6-51e1b4d8b56d | -6.55501 | -42.34285 | 2025-10-30 04:25:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 006e9ec4-7dd3-3095-b4b4-21d62a2ba235 | -5.76617 | -49.11392 | 2025-10-30 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c50e42c7-cd84-394c-8836-04122df00b6e | -3.88272 | -51.19276 | 2025-10-30 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 515478ff-dbcd-34d3-91e6-e71fab31dc03 | -8.05101 | -45.17147 | 2025-10-30 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80c848c7-996a-394c-ac4f-a08817a95a91 | -5.68957 | -46.43408 | 2025-10-30 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6698e9f1-ed4f-3515-b83a-3b7498c7ce9f | -4.25468 | -50.66776 | 2025-10-30 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bac264c6-93b4-3deb-9ffa-05d8a2dbb8ab | -9.93968 | -47.18927 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61bf32ba-0519-318d-8ef2-beb70cd23b25 | -5.26596 | -43.76593 | 2025-10-30 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0decd59-2c9c-3b5d-9bba-cac53756f947 | -6.70805 | -38.21066 | 2025-10-30 04:25:00 | NOAA-20 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3570c9e5-3b8f-35df-acca-1fee7bb8fd77 | -10.85761 | -47.6138 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a34cedd-f539-342a-b7a3-1007e62014e0 | -6.97611 | -47.31905 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de041fd6-5926-3ef6-a508-9d495596b11f | -7.07906 | -44.93407 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 793902d5-30e2-35ba-add0-cb87d4375031 | -6.14468 | -41.69288 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6bbdb584-ac60-3579-93b7-40068aa9f036 | -7.65561 | -46.91451 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67766ec4-0d1c-34d5-86b5-ce390e0d54c3 | -9.08704 | -47.91324 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 909260bc-93d5-3215-9ef0-88d6c0e4714f | -5.6088 | -42.7877 | 2025-10-30 04:25:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f63470e-0eda-3276-8a75-61923432aa83 | -6.14971 | -41.60384 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8cf1d126-fa97-3e98-8a8d-c9ce79591699 | -7.52005 | -46.26828 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66d64aae-a7ee-35b1-baa3-d9a1e0a437d5 | -6.14081 | -41.7094 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 99bd0a95-2be7-3ce9-b286-5bb172f01b6c | -4.25313 | -48.57235 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0969c495-7cd0-3292-b0b8-b6bbaf192101 | -7.32257 | -42.48433 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5effb1b3-7c62-321b-b8b4-b09b69bb1bdb | -7.91638 | -45.71026 | 2025-10-30 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5d83047-5795-38e0-be6a-61d4b7734fc7 | -10.91638 | -47.99211 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5c40071-4090-3963-b1e6-cd3bbf0b3270 | -4.58173 | -45.51051 | 2025-10-30 04:25:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28da4545-901e-3dfa-ac3b-b68596e8412a | -9.23659 | -45.56361 | 2025-10-30 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cb7d79a-db06-3c01-83e2-1db51a2633ab | -11.27636 | -47.75819 | 2025-10-30 04:25:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a1e22a9-b4b6-387e-8a10-b3c0f728ba6f | -6.09884 | -42.44236 | 2025-10-30 04:25:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 25868038-3ff0-3f9f-8342-aeeea0de641d | -9.88821 | -47.44952 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56200f36-d7e5-3e4f-9a45-7061c983addb | -5.53689 | -41.70587 | 2025-10-30 04:25:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| fbffb0ea-e9ae-3ce0-bad8-322b038f80e9 | -4.99459 | -44.15733 | 2025-10-30 04:25:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3a621c5-54f5-3cd5-9f5e-d50779df1839 | -6.63092 | -44.61079 | 2025-10-30 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf0edbe7-9767-34ae-bbb8-6d453c15f22c | -4.54023 | -54.96655 | 2025-10-30 04:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4069230e-56e2-3bbc-8e04-caa6dda873bb | -7.29882 | -45.66421 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fa0d71b4-c5fd-342e-a93c-da4b9c55b45b | -6.0052 | -43.10458 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 72bf0b40-8a19-3315-b52f-279abf947876 | -6.13374 | -41.70381 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 27f8a999-0f7a-3c89-b103-22a3d4892410 | -6.2936 | -42.88491 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7d2cd085-dce5-3038-9be7-d6193e41c048 | -10.42187 | -45.05502 | 2025-10-30 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 689c045b-d442-3e47-a11c-0553719ba2c8 | -11.0632 | -50.3217 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7c241b23-0610-37ac-9972-fac83662882c | -5.34059 | -44.84827 | 2025-10-30 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fe0c01a-a92b-3096-9b70-e9e6482ad2c3 | -4.8432 | -45.42405 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c774b8de-8ce6-341b-8043-b656dd19012e | -9.26797 | -45.2273 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0737788-8d34-31bf-9e22-79d0ece15392 | -10.75762 | -44.7357 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1a85f81-942f-3b69-ab5f-782db31533cf | -11.00525 | -47.96677 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3680a9c0-0261-3fc3-9106-77fcf0ec943d | -4.84982 | -45.42508 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fc9436c-4356-3363-af4b-1e34c5982319 | -11.00192 | -47.96622 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f58ac6e6-bf6c-34ad-96bc-2b5bbd13730d | -7.95744 | -46.74596 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d21090a0-a379-3adf-a65b-e9e3c163a2fe | -11.63885 | -44.04482 | 2025-10-30 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ad976ab-6616-3a80-944a-2f24c50d9675 | -11.24639 | -45.43597 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24fd4ce7-f683-3e0a-b9ca-3ab759d9a1ac | -3.43872 | -54.63945 | 2025-10-30 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78fe4e3b-d2c3-391e-8226-b724f391cf00 | -5.79885 | -40.8128 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7ca3700c-d671-30e2-b2be-3471fc397f8b | -7.29795 | -44.96783 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 586ce6e3-9d15-3d61-b39d-e275140a8ac4 | -4.86497 | -45.54406 | 2025-10-30 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 315e94aa-aadd-3f7e-ab2e-c6b04588331f | -7.14283 | -40.45957 | 2025-10-30 04:25:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| daef8dfd-1800-30fc-818a-86b228e524ad | -7.95194 | -46.7593 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b997694a-bfee-325a-9856-d6275dc019d7 | -11.09834 | -44.70448 | 2025-10-30 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0019f847-6bd8-3e91-98ce-434e2857a44b | -6.13593 | -41.6894 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 963052db-10a2-302e-a392-67e87c132895 | -7.34387 | -47.63239 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 684d097f-5a66-33a3-ba15-6a13942bfd5c | -7.87659 | -48.1398 | 2025-10-30 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5a4a40f-2384-3374-8c54-54eb55489a96 | -9.88601 | -47.44199 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4abb30b3-3bca-3c1d-8049-42b89d981e55 | -5.43124 | -45.33554 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac1a105f-8757-36d9-88ee-866a746ead7a | -10.86367 | -47.61839 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 943146e0-8e0e-371f-9073-e348ec9d084d | -7.07515 | -44.93713 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f6d7e07-c2f0-329a-8132-ad4b51a85d45 | -9.08647 | -47.91682 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb39160c-8ac5-3690-aaa3-10905f07b16d | -10.91086 | -47.79208 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README50.md)
