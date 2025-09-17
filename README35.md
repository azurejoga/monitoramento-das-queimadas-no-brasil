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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e405c8e2-668d-3081-abb9-359a743a591b | -6.16591 | -44.52659 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 831394ad-dcfa-3ff2-83b5-e7cf93b98057 | -5.80363 | -45.70459 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd43a4b4-8118-3e07-bceb-b74fdb158adf | -8.13074 | -43.63932 | 2025-09-17 04:32:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d47e1d44-0b05-3ca3-97e2-1c90a4158ce2 | -9.00873 | -49.7771 | 2025-09-17 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3ba338d-5cc4-3fbf-8230-e54da1992e5a | -11.45984 | -43.55269 | 2025-09-17 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 554c951b-b136-35ad-9760-17b4ac5adb69 | -8.62346 | -46.44527 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a9e22830-f1b8-3c1b-927d-4c7caa33f24d | -6.62702 | -45.5829 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bac35656-96d0-34a2-82cc-57ad74524468 | -6.97803 | -44.44524 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca21fd46-3529-3772-992e-c76effb412c9 | -9.09136 | -44.94422 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6dc76e67-a042-3f60-9fd1-0de269a0e2ec | -9.07971 | -44.94695 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3432585c-477a-3089-bb71-3fccf600753e | -6.1691 | -44.50555 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53835042-4768-3638-9208-45d8efa87067 | -7.58451 | -44.58422 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 232b7462-67d2-38b5-bf74-9e1293065d17 | -6.97735 | -44.44967 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90375a93-691e-3de2-94bf-ca936a4cc897 | -6.67616 | -46.31035 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df2d210f-d3e7-33f9-bf59-3866b886756f | -7.88839 | -48.17585 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a2131a6-b7d5-3919-be29-f2ea91aac8c1 | -6.92367 | -44.80964 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07d90ddc-3376-39cd-a4c8-efba524ef3b3 | -7.58214 | -44.57495 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65f13a3a-d8b3-3238-940a-26c65b61649e | -7.26094 | -46.60709 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0ff94ef-629f-3dbe-8504-546913795ccc | -5.80125 | -45.92376 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30ae6d42-3873-3292-a624-1ed9edf1df51 | -7.26765 | -46.58603 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b2ac6ea-f10e-3086-a6d3-553bd3358699 | -5.80647 | -45.70889 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 343f24f1-e693-3a7e-9cca-70e45bae5391 | -5.78272 | -43.94371 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e0ea2ee-60b1-3165-8a98-7a794dbff941 | -8.89936 | -46.14607 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb020d60-5e94-30e9-98e2-dda1afc83b37 | -10.6782 | -46.51361 | 2025-09-17 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e522067-5aec-3f7c-aa74-9a0daec1c0ab | -11.02523 | -45.06002 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 33a475b4-e2fe-3015-a6dd-f60453fb9297 | -5.78477 | -43.49082 | 2025-09-17 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7671eb5f-831a-3349-974a-cfae18749db1 | -6.29159 | -42.38503 | 2025-09-17 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ee46e50c-ff65-3a32-8c52-38958e32f743 | -5.48918 | -43.98703 | 2025-09-17 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62311cb2-428d-32b3-9f5a-300c116c9528 | -4.64645 | -50.91637 | 2025-09-17 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da5b5269-3f6a-35a8-a486-7617baa43375 | -7.57241 | -44.56458 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7954b19d-d1e6-3076-8a4e-1efe0c3addc5 | -10.40471 | -50.6401 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c368ee1-0517-36f2-aa97-5476de979fc4 | -9.17652 | -46.94711 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 86715695-843c-3d78-bccc-9f5d9bbf3c2c | -10.68133 | -46.50473 | 2025-09-17 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a22af2f6-7d00-33c6-a09a-a2c3ca10f0a6 | -7.59252 | -44.58098 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 813d4a13-1af9-34c0-b538-7088ce47d41e | -5.82009 | -46.36079 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b91cd56-604d-3cc8-a5cf-dcc813103036 | -7.04334 | -44.30531 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05b3271a-166c-33df-b469-d1fa18f583a5 | -8.99034 | -45.75271 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84c8d2f4-b7c6-3549-b6d7-336cbeaed368 | -6.95716 | -44.55714 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f572d744-f7c0-3b7a-a735-fc9992069751 | -8.91495 | -46.27758 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b79b1a5-87b2-3857-81c3-4628ad33132f | -5.78632 | -43.76431 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6566642-830f-3d0f-9b57-7f8aca8f3bdb | -3.50716 | -48.4511 | 2025-09-17 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2883237-9661-320e-b059-b959bccc346a | -8.96325 | -46.28485 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ce048df-096b-3421-b6a0-eecb0643d399 | -7.88563 | -48.17186 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 901ea04a-5a72-3ab0-9c23-d3713179b9d0 | -8.7015 | -45.86773 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b04bde68-f543-32a4-8ab3-e9efdad92d70 | -9.17537 | -46.93208 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09dd0833-4579-322a-9678-dbe8fa0c2490 | -5.6178 | -51.7198 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 640e0f14-393c-3c1f-9bbc-d5bfda0e0730 | -7.81058 | -46.1292 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 487f1bb1-4183-36c3-aec9-0e6e1b6acc5f | -8.63154 | -46.4387 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a67fe8d-2b95-3a68-9849-88c16336f6f9 | -4.63628 | -46.06984 | 2025-09-17 04:32:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e64b7623-6e6d-3a15-8a68-36324a324251 | -7.32669 | -44.06273 | 2025-09-17 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1a98db8-1dfe-3d56-b08d-ab836281ecd9 | -7.60543 | -47.46884 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 585efcfa-fc32-3673-9be7-4577f3140022 | -4.59625 | -45.58457 | 2025-09-17 04:32:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00b8c62e-010a-3bd0-9fb9-b09b94830bf6 | -7.26483 | -46.58194 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 808e818c-076b-33a4-bd49-71e7643bd528 | -10.48428 | -49.37003 | 2025-09-17 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ae5d56b-f5ac-37a5-a0b7-9b058c05089d | -7.7647 | -44.72676 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4082e49a-a3a1-3c05-add1-5b03ab095c90 | -7.61262 | -47.46638 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66c6cc14-f2ed-3cff-9d99-a1e7b206842e | -6.16025 | -45.10871 | 2025-09-17 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0d69a13-89cb-3308-a45e-802abf1ceb0c | -7.88451 | -48.15746 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 016129ad-a285-3a5e-8ca5-97315803f1d9 | -8.08381 | -50.15799 | 2025-09-17 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8cb9f64-f984-31c2-bfc9-7b305d546c20 | -7.48285 | -46.12299 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 713af14d-e2f8-3469-a74f-a2568f0f5bc3 | -8.67766 | -46.36551 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf3a1e37-1e60-313e-ba49-796f031c8738 | -5.77924 | -43.91579 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d6ec016-c57e-3a0d-b58d-c560dacb5c1b | -6.98694 | -44.60828 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c56efebc-f735-3645-a690-949575bce630 | -5.49289 | -43.98756 | 2025-09-17 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 30e2df0b-5926-3098-993c-5905bdf24b5d | -7.56383 | -43.9504 | 2025-09-17 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fd6866f-e10d-3131-930d-30bf2afccfe5 | -7.83167 | -43.85506 | 2025-09-17 04:32:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49676883-ebf5-317d-b81c-7a80652e00e8 | -7.53197 | -44.73441 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c474ed5-de84-3d9f-a6a4-527e52e750ca | -8.43805 | -47.68154 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c90bee4a-b986-3032-b806-d747672f5cbf | -6.48966 | -45.72535 | 2025-09-17 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 845f4a60-53ff-3bff-834e-7ed924010434 | -5.6046 | -44.11477 | 2025-09-17 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3b49b2e-b0fe-3bb8-8ccd-a996ebe4a97c | -6.41368 | -42.65212 | 2025-09-17 04:32:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a87e8d9b-1030-374d-89cd-81e92a39ac64 | -10.89948 | -45.44176 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d48146f-d9f3-3db5-ae8a-3e380a2647f4 | -6.73816 | -46.99967 | 2025-09-17 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d04f0928-f2f2-30f1-a52a-5784b07319e0 | -6.16377 | -43.66861 | 2025-09-17 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 805502a8-d216-3c4c-84b9-507bbcf6420e | -9.16467 | -46.93414 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90ac8364-38b4-3c06-8f38-d119c0e5843a | -7.06461 | -44.34054 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a2d6157-b2c1-3c95-ba73-dedd458d52a8 | -7.70411 | -45.32083 | 2025-09-17 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26cb6105-b12e-35e6-99bf-9f9e96b65250 | -6.1843 | -45.11661 | 2025-09-17 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 451ec722-00eb-3744-b836-26fbd0fc3bb8 | -6.98033 | -44.45474 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 73ed9030-da08-30dc-9e36-001d0d48db9b | -8.15327 | -46.754 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b67cb59c-6e5d-3210-b95a-5f65c31895d8 | -8.41988 | -47.20572 | 2025-09-17 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bb494a8e-49fc-33f8-a9ee-b8cdf8037371 | -10.39566 | -50.63102 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3691a4a0-716d-37a4-aba8-2b3553ba5218 | -8.98643 | -46.2645 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba5832eb-02bf-3612-98c0-3ce0c14b539b | -7.98252 | -43.93995 | 2025-09-17 04:32:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 514552bd-0abb-36f7-a6b8-f18efc800e8b | -9.72639 | -47.40467 | 2025-09-17 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83db3022-566f-3253-b1ff-b4f1b62ccb30 | -6.76829 | -43.401 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9d399c25-2336-3d7c-a472-69a9df1d3f2a | -6.86156 | -46.10981 | 2025-09-17 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afb516c7-13c3-398c-8946-313e2220b7a6 | -6.397 | -43.3399 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e5e692d3-137a-32ff-b189-1202751a52a1 | -7.52832 | -44.73384 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc1b86df-4db0-3fd8-aa94-5268c403f52b | -6.25415 | -43.45871 | 2025-09-17 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f222b1d8-6bfc-3bf2-b111-0707add16597 | -8.87572 | -50.14084 | 2025-09-17 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8b7a74c6-46b1-32ec-a418-c8b0939f36e9 | -7.25023 | -46.58705 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c20d25f-0a92-3912-beaf-c11a957bf50c | -10.41716 | -50.64978 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1ed7b1f-ef8f-309c-8222-2fc7e6fd3b5f | -5.81281 | -46.3633 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9933751-62be-3c0d-b04f-7e99c0579871 | -5.63909 | -43.88982 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0e19c91-c6c7-3a67-9ec7-21cac166cf5d | -5.34785 | -44.81761 | 2025-09-17 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 808a0334-9dd4-3db2-b5c3-c6c345e979fa | -6.28803 | -42.38053 | 2025-09-17 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2859f644-8179-3712-bbd1-78f1584ea56f | -7.67688 | -46.63659 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0602ebe-d1bf-3e96-854c-92964f2711cc | -5.92221 | -45.91161 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9c756b3-6148-30d3-8636-666b0b00f5e3 | -6.26124 | -44.68465 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README36.md)
