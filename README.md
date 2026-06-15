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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dce7d92b-d233-3a0d-8fdd-4bdab2e15968 | -5.61057 | -37.53342 | 2026-06-15 03:15:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ff34339d-a169-36f1-b5c1-7a36f914609d | -5.6109 | -37.53178 | 2026-06-15 03:15:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 899a05ba-a802-3f32-95c0-d7eb313a030c | -22.83334 | -43.33086 | 2026-06-15 03:19:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4756ea4d-0ee3-3b5e-ae37-c2fb2087d50c | -22.83216 | -43.33575 | 2026-06-15 03:19:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2f235441-0e5d-3de3-af33-9c512adce3db | -3.49855 | -48.04013 | 2026-06-15 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8841de8f-31f0-3369-bb30-2c8a8b805674 | -3.50961 | -48.03822 | 2026-06-15 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f835a33a-bc77-349f-af2d-3050281b7239 | -3.5159 | -48.0326 | 2026-06-15 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 439f2a2c-1e3d-3b28-bd26-d7afad764c3e | -5.13507 | -37.66683 | 2026-06-15 04:00:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3241f8d6-8fa6-348a-9c33-361ec800ffef | -3.51538 | -48.03579 | 2026-06-15 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5add0d87-8e28-31e8-8b6c-a0bd78c2e32b | -3.5038 | -48.04088 | 2026-06-15 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69bd3ba3-9bf2-37e4-ab57-52d6e850cdc4 | -3.51065 | -48.03186 | 2026-06-15 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc550b25-7e4c-3ea3-bd66-43ba7a41e9c0 | -3.50436 | -48.03745 | 2026-06-15 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f362766f-eacb-3805-b337-abe3f297f4d6 | -3.51014 | -48.03499 | 2026-06-15 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d661270c-4198-36e8-919f-d40548b78026 | -7.11496 | -41.16904 | 2026-06-15 04:02:00 | NOAA-21 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 882268ee-03c4-395b-9b13-a33899b6f992 | -7.31427 | -48.87993 | 2026-06-15 04:02:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a486383e-d245-371c-93f7-8d692eec15d6 | -6.16408 | -48.4937 | 2026-06-15 04:02:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d11859c-2de4-3fea-9131-8e8bf5fcbd29 | -6.12014 | -48.50193 | 2026-06-15 04:02:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2b2e373-4dd8-3d0c-a493-31a39539cbbb | -5.61155 | -37.5327 | 2026-06-15 04:02:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 88b5c0db-49eb-32ac-bc1e-47711c7a63bb | -7.1183 | -41.16957 | 2026-06-15 04:02:00 | NOAA-21 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0bc39521-6dec-390f-9e2b-3c4796b815f9 | -6.86684 | -41.91187 | 2026-06-15 04:02:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6b31d3f9-0ac1-395b-b552-8661459878f7 | -7.32634 | -48.87228 | 2026-06-15 04:02:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ceacf4ed-da7d-3a6c-89b8-d8c27f52427e | -11.02666 | -44.69568 | 2026-06-15 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| e2985dec-d70b-3e88-bbbf-954fa26bd499 | -5.29136 | -43.95786 | 2026-06-15 04:02:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 786ef877-a3b4-3f1d-94f9-19b5d9f58560 | -8.19431 | -46.75751 | 2026-06-15 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 120b050d-d1db-3607-9c78-f58c67e5add0 | -7.32059 | -48.87454 | 2026-06-15 04:02:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 62918f64-6c19-3a8d-8ffe-a82032f35139 | -6.7252 | -44.38096 | 2026-06-15 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 746edf93-50ce-3197-9550-05c285d933b6 | -8.18622 | -46.75164 | 2026-06-15 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8e5d971-83b7-398d-bebd-9f3c5cb725fc | -6.16506 | -48.46936 | 2026-06-15 04:02:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3909692f-bab3-3752-a0a4-94580b9ce26e | -6.15925 | -48.47219 | 2026-06-15 04:02:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96a2c318-e24a-3b41-baf3-6ad9affff64c | -8.38472 | -46.49709 | 2026-06-15 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f60cb60-146d-3506-8697-e7ff6aa8535e | -8.43826 | -51.55003 | 2026-06-15 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4644a0c-1551-3a64-b07f-c529881e9c62 | -8.18666 | -46.7533 | 2026-06-15 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff46eb93-9b6c-3f5a-b4b7-71414a24d3bc | -8.88778 | -48.50826 | 2026-06-15 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c92f7aa9-f86f-3641-82ac-1ca9ed0f8cd0 | -11.02741 | -44.69115 | 2026-06-15 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| f34e3d34-1c16-3606-a2fe-c5c070cddc71 | -8.19109 | -46.75404 | 2026-06-15 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fed1548d-3331-3144-8edd-faf288687b1e | -8.19478 | -46.7592 | 2026-06-15 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1f6244b1-50f9-3d39-a46d-b7506ffd67c5 | -10.28869 | -47.60015 | 2026-06-15 04:02:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64544cdd-e1bd-36b6-af6a-02007d35f461 | -6.72603 | -44.37587 | 2026-06-15 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5040be59-4d4f-3258-a938-a2bfa1b4e02e | -8.19874 | -46.75823 | 2026-06-15 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a22b98c3-31cd-36c9-a25c-8b87ae67cb88 | -9.26549 | -50.66153 | 2026-06-15 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78c421d2-017a-3e76-8fa1-bc5d6e88cec5 | -8.95163 | -46.93407 | 2026-06-15 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b96849a-33cc-314f-afac-490aa4cb005a | -6.12071 | -48.49862 | 2026-06-15 04:02:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6beea00-efd0-3cca-b358-208cff166c2e | -5.28957 | -43.955 | 2026-06-15 04:02:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31e19b5a-5812-3f88-8e63-776f37d32040 | -11.03189 | -44.68726 | 2026-06-15 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5527f489-a284-3f99-a72e-57c6ea96a115 | -8.88285 | -48.5074 | 2026-06-15 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96b40448-13e7-3da6-aa16-e61811721cf8 | -6.86743 | -41.90815 | 2026-06-15 04:02:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7c64c887-1fdd-35fe-9f0c-520fadf9ac0b | -6.15995 | -48.4867 | 2026-06-15 04:02:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8beb6b32-cf06-3268-bed4-156af10c32f7 | -6.16187 | -48.4874 | 2026-06-15 04:02:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 213c1168-c8a4-3669-8b52-393b6c2ed20f | -6.17065 | -48.49789 | 2026-06-15 04:02:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c41c994e-a9c0-3cbf-b17b-e59fcd5bfd6d | -6.15941 | -48.48993 | 2026-06-15 04:02:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5699bb98-ca02-350d-902d-b92163204080 | -8.38972 | -47.47316 | 2026-06-15 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 715f54da-99d8-3d25-a553-b1ed02e207ea | -11.03038 | -44.69629 | 2026-06-15 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| d28a0ed9-5c5b-3889-8004-f731b44e912b | -7.31484 | -48.87676 | 2026-06-15 04:02:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bae32c72-8da6-31a1-8948-22495ecc6498 | -6.12538 | -48.50243 | 2026-06-15 04:02:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 011f5a3c-fe54-3dcd-b7b3-a125a796767a | -6.16238 | -48.48452 | 2026-06-15 04:02:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 591990ca-91d2-3a4e-8a7c-a0b8fc7fd511 | -8.19922 | -46.75992 | 2026-06-15 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 900b116a-7044-3869-8126-756fc77a14d6 | -5.28877 | -43.95981 | 2026-06-15 04:02:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adaef71a-3989-3691-b796-bd82a2750fb5 | -9.26622 | -50.65759 | 2026-06-15 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee878cd4-6aba-3209-9168-bd812f835ba0 | -8.18987 | -46.75678 | 2026-06-15 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64032ac6-6bcc-3ff5-ab1f-13cc6046cfc0 | -11.19821 | -49.68365 | 2026-06-15 04:02:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1157d1ca-e9cb-3f4c-b577-74b69a35e256 | -11.68128 | -42.06057 | 2026-06-15 04:02:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b69f68f4-ff4f-3aa5-86b2-013b1d0cdefe | -7.32003 | -48.87767 | 2026-06-15 04:02:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f054dd0b-81b8-307b-9ea2-4c212d8dc528 | -10.29321 | -47.60102 | 2026-06-15 04:02:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b8e53cf-2a28-3e85-82ba-b9e82436cc7d | -11.03113 | -44.69178 | 2026-06-15 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| eb4b97c8-b909-30de-80d0-bd0ec619c605 | -5.29343 | -43.95563 | 2026-06-15 04:02:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ad7b7ac-9a47-3e38-ac91-120ed69a68fd | -11.02817 | -44.68663 | 2026-06-15 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 803dfbb1-76b6-3300-802c-0344837d2c15 | -7.92021 | -48.25257 | 2026-06-15 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 00566e3a-816d-316c-8903-13ec6f06cf26 | -5.93895 | -43.64986 | 2026-06-15 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2dfa92d5-2218-3051-9b58-53cc797e70d6 | -6.16127 | -48.49076 | 2026-06-15 04:02:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ebef51c-1b4d-3375-ad72-168fa9a96e16 | -5.93821 | -43.65441 | 2026-06-15 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 13422db3-c940-395c-97db-3e1fa87616bc | -8.96949 | -46.91025 | 2026-06-15 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9783bb8f-ddc3-3d7b-a553-a6ac035dbfd2 | -8.13929 | -47.55595 | 2026-06-15 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f89d889a-a155-3ddf-af91-0d120b463d90 | -6.15981 | -48.46906 | 2026-06-15 04:02:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b3971a6-c22e-3634-af38-d746e4a09bd6 | -7.32578 | -48.87543 | 2026-06-15 04:02:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6429fe14-dc90-37b1-bce3-57e725b81d7c | -8.19796 | -46.76265 | 2026-06-15 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75226a97-5a3b-34dd-8e88-c45d45aa609b | -10.41841 | -44.95927 | 2026-06-15 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fff45eb-e574-3ea0-969a-29bc3d31fec8 | -11.02445 | -44.68603 | 2026-06-15 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 123ca7e1-cca7-305b-80ab-36fb60f65f4b | -8.9873 | -48.09352 | 2026-06-15 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa022977-5ff2-3a37-be0e-0a8d464cc27a | -5.94045 | -43.66426 | 2026-06-15 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fbb8fbc-0d00-36be-aea8-f5af8ab6159d | -5.93745 | -43.65901 | 2026-06-15 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c83082d-a93d-3021-8dbc-d2963638dae5 | -9.04908 | -38.26715 | 2026-06-15 04:02:00 | NOAA-21 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 271e74cb-4ff1-3840-8587-eb8ee917cd3b | -6.16593 | -48.49447 | 2026-06-15 04:02:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45a32d8b-882d-31c7-b1e4-c5bb883193da | -7.92165 | -48.25452 | 2026-06-15 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd76a6ff-7cb3-360a-9a9d-935601e89592 | -7.91671 | -48.25373 | 2026-06-15 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33a6692b-4931-369a-80e1-82266f6c58b4 | -9.27115 | -50.66247 | 2026-06-15 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f4da960c-0a3f-3a84-89e0-d28e50cca1be | -7.31947 | -48.88081 | 2026-06-15 04:02:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| badef102-b39f-3b1d-af5a-b7db6d00308c | -12.73188 | -46.29427 | 2026-06-15 04:04:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd7b2418-7e67-3a67-b952-0437ade447fc | -10.83632 | -53.7347 | 2026-06-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5406a93c-c086-3abd-8c44-47c543f485d3 | -14.37396 | -45.54455 | 2026-06-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57523cc1-b847-34be-a835-bd4545aba45c | -13.50691 | -47.85334 | 2026-06-15 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4b60799-04d7-33be-adbd-c6f79d3e3961 | -13.50841 | -47.8451 | 2026-06-15 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7be38b23-f4be-35b3-9b41-fc7011b0c13d | -14.86717 | -42.19079 | 2026-06-15 04:04:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a877b884-5f85-3dcf-a5cb-32dabc7b6531 | -14.0453 | -47.04788 | 2026-06-15 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ffa5dd4-dd89-3162-b4c2-5f4125eeb7c6 | -15.14022 | -42.84798 | 2026-06-15 04:04:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 921da63a-4f8b-3742-b3f6-57006fb5133a | -13.81131 | -43.65144 | 2026-06-15 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| aa80f18e-9dd2-3d29-83c3-a3e8ad1106e2 | -11.82621 | -51.62397 | 2026-06-15 04:04:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6891ca6d-668e-3fc6-b38b-d6438671fdc1 | -12.73432 | -46.29189 | 2026-06-15 04:04:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4c79a9e6-a1b3-3638-82bb-10e0aaf3618a | -14.70036 | -41.73729 | 2026-06-15 04:04:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 751c2dd3-0818-3922-93bb-01c728f6cb90 | -13.81068 | -43.65529 | 2026-06-15 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 30a399f5-e600-357f-a3b2-45af3db77a24 | -11.71995 | -54.49152 | 2026-06-15 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README2.md)
