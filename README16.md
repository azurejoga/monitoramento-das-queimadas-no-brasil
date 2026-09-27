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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd3839dc-7bca-30da-9548-1fe380691331 | -3.50033 | -50.4841 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 855fbfad-8a5e-3527-b23a-e494c6eedb18 | -8.3518 | -44.14502 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d15b289e-4bc8-3771-a0a0-5f519212b2fc | -6.34995 | -46.44644 | 2026-09-27 04:08:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9143829-f751-3eec-94a5-34d609714e7e | -7.3739 | -44.76237 | 2026-09-27 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27634034-07ce-3056-adc0-56fb47830107 | -5.47843 | -48.58215 | 2026-09-27 04:08:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44fd4e99-26e1-34e6-8baf-10241cce436a | -7.37975 | -47.02451 | 2026-09-27 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2059179-4318-3aa2-997c-ed5ee700927a | -4.25846 | -51.056 | 2026-09-27 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33ca5176-fcd2-355e-bcbf-e57f684071a0 | -3.9698 | -50.7165 | 2026-09-27 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 13105afb-7f15-3426-bc1c-c6531e032436 | -7.37079 | -42.10852 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fdab54ea-4c77-30dc-9c64-b3ca03154a49 | -4.78305 | -43.65302 | 2026-09-27 04:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56b7bfd3-176e-3a5f-9a35-2a2d073bd19f | -6.92927 | -41.61205 | 2026-09-27 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d3f1f8e-3bf3-3262-9a16-90a70f860359 | -7.4039 | -42.62256 | 2026-09-27 04:08:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b66f8924-7793-3942-9ecc-a02b117af8e7 | -8.34727 | -44.18791 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| a8964bdc-609b-3567-b6a7-ffb55fe41687 | -7.19197 | -46.51175 | 2026-09-27 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbecb024-e5ca-342d-b288-15ed4e9e16d3 | -6.83883 | -43.56972 | 2026-09-27 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4482afd6-1be3-37fc-b6d6-d5935733309c | -6.38368 | -44.84559 | 2026-09-27 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 476aa004-1c3d-3800-90a2-38e4a3e15ff8 | -3.95576 | -48.11703 | 2026-09-27 04:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfd0e449-f362-3894-9da8-13a8fa588359 | -8.33851 | -44.13376 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52daac02-5c92-3e5b-a6e8-15a179022775 | -5.50291 | -45.51085 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33af2424-df40-3c99-9ddb-70460bd4ac0f | -3.698 | -51.37899 | 2026-09-27 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 028e861d-eccb-3a9a-964e-d9b13da05f0f | -3.67026 | -50.84764 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 114e7073-516c-352a-8e33-dc6a05cee4d1 | -10.01647 | -50.16008 | 2026-09-27 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa56d892-f7d6-38e7-b6ee-3ee69d4b3d0d | -6.1305 | -53.05614 | 2026-09-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 143ab519-9658-3d67-98f9-03047a688c88 | -7.12262 | -43.66644 | 2026-09-27 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c55fcb6e-7112-3abc-aa97-d4d4bb0ea69c | -8.37018 | -44.1422 | 2026-09-27 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93471471-be87-348d-9555-338ec84ab085 | -10.46339 | -48.32171 | 2026-09-27 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a48de91-7e43-31a6-90eb-c1d8c91bc0cb | -7.27412 | -43.31232 | 2026-09-27 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94880ade-07bd-380d-88ff-bcd879cf7e33 | -4.74142 | -43.47719 | 2026-09-27 04:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5bf1d27-4b64-3dee-8a16-d1dea728b71a | -3.84663 | -49.13731 | 2026-09-27 04:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0218aac5-92af-3f9d-9f84-191fe4c88a64 | -4.25705 | -51.05746 | 2026-09-27 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 253aafdb-b5b7-3d70-b6a8-c5071c4390db | -4.8464 | -42.89542 | 2026-09-27 04:08:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4dd94298-3392-35c6-8b6b-60e18a0b5eaf | -3.26823 | -50.14319 | 2026-09-27 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d933800e-5eec-31b2-b7bb-0ccfa6f485b7 | -9.08104 | -49.87664 | 2026-09-27 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f469cdc5-3521-3a33-b69b-bc7dd3dc84d8 | -4.56057 | -44.07955 | 2026-09-27 04:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a027b47-a3c2-30de-9f51-1303e64b65ba | -8.34876 | -44.1791 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 859ce271-4276-3375-8cf1-8da30e873657 | -2.96072 | -49.56519 | 2026-09-27 04:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d24a2544-6d03-3644-aa23-43441d513236 | -6.1532 | -47.28731 | 2026-09-27 04:08:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| abd94f31-4868-3f79-adb4-b2a7eb340b15 | -3.20209 | -51.04273 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fccf6513-98aa-3eb3-bf61-a15726e51272 | -5.73967 | -45.06082 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8feb3e6f-8e23-31eb-b1e5-77f91037b39c | -3.42256 | -50.42222 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1ba53120-1be1-3f95-869e-f0a270fc1489 | -5.7437 | -45.06156 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 056c3ae5-f8cd-3c74-ba24-0172f0f66359 | -11.34362 | -41.84741 | 2026-09-27 04:08:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fd295a7d-24bf-3816-9a97-a896e5db65a4 | -3.96091 | -48.11775 | 2026-09-27 04:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fb46dc5d-482f-33e7-b9f2-5115ff31e0b1 | -8.33918 | -44.16855 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c4807f79-c749-3a76-926a-53ddc34bfa03 | -6.93599 | -41.61315 | 2026-09-27 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 09672fb2-27a5-345a-843e-eabb5f98bb50 | -6.83449 | -43.57333 | 2026-09-27 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67e61080-0f48-3c5d-9c50-d2871548411c | -7.37138 | -42.10484 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a50be9da-cb55-31cb-abea-d981d5c46c03 | -7.32492 | -42.08978 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9610a3c6-f64c-3dd1-8420-783876db8a71 | -5.73906 | -45.06441 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2fd1c756-5632-3008-ae0a-6f7e3a5397fa | -8.3364 | -44.1696 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5cd9f43f-defc-3be9-8fa1-4f3761b5719c | -5.73352 | -45.02333 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 74f22f73-b8b8-3710-be57-bd7261f61eeb | -9.44805 | -37.60803 | 2026-09-27 04:08:00 | NOAA-20 | SÃO JOSÉ DA TAPERA | ALAGOAS | Brasil | 2708402 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a7c17514-af0f-368e-aaae-9aa3fa34b57f | -4.30514 | -43.91837 | 2026-09-27 04:08:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81ddf998-e1e9-3194-8883-360ac7fce2a4 | -6.83572 | -43.52124 | 2026-09-27 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f51c74d9-fd65-331c-bfb9-e0d8e2523737 | -8.3606 | -44.15406 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b0890075-b0b5-3f97-9f02-6b9dd9134722 | -3.09892 | -50.32625 | 2026-09-27 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d45475fa-5d79-3335-a617-53fb46d3c260 | -4.143 | -48.22279 | 2026-09-27 04:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fcbfb04b-7d41-3546-af54-95634bc7c2a6 | -7.36901 | -42.11958 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| df97916e-e220-30f8-822f-0706742f479d | -3.96605 | -48.1185 | 2026-09-27 04:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 36bf7383-29c3-346b-b0e7-380d8f5f68c9 | -6.3728 | -39.84321 | 2026-09-27 04:08:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 01e204bf-c6e6-3ce6-8743-16f959604670 | -8.34524 | -44.16193 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f3b886d-eaff-3ff4-83f2-c5bf182fdc05 | -8.34732 | -44.16531 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0cc45dbb-a997-373a-9851-88aa77dbefac | -6.38235 | -44.84713 | 2026-09-27 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 558abc70-6ea0-35c0-b347-fa11235da326 | -8.34442 | -44.13782 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86a518ef-8e08-3ab1-9f73-efd20bfb9500 | -8.41013 | -47.01938 | 2026-09-27 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aba460a4-7bf5-337e-884d-da53ee5ba991 | -8.07705 | -40.83636 | 2026-09-27 04:08:00 | NOAA-20 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 16a3c6f5-be7e-34a5-92dc-91e6da37fd33 | -6.12602 | -53.05415 | 2026-09-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7423b3e-7987-3ac7-afa3-66c1431aba2e | -4.29072 | -48.62298 | 2026-09-27 04:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcbc1f82-2f11-39a8-bbaa-a00e0a80d2d9 | -8.34137 | -44.17793 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb7444aa-d3ad-36d6-951d-e2ecc240a2d8 | -3.96292 | -50.72021 | 2026-09-27 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b2433551-c567-38d0-b293-25e29e7af8cd | -6.83519 | -43.5691 | 2026-09-27 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e2e623e-fe85-3e5d-95a5-371b81bb8caa | -4.67507 | -45.99157 | 2026-09-27 04:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a0f59ca-4db4-3472-bcae-8bab29147047 | -6.15656 | -47.12817 | 2026-09-27 04:08:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a72990b1-7090-35ae-9d5f-e872e4d6f89a | -8.32083 | -49.97773 | 2026-09-27 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11a7163e-2cc3-3a36-9416-66df07066298 | -8.24616 | -43.78633 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7d192c19-cf8b-3dc8-a402-7b9d40647cbd | -4.5589 | -44.08218 | 2026-09-27 04:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fef2085-d93e-3c0d-aea9-444218464f6c | -4.25928 | -51.05115 | 2026-09-27 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83e78971-e810-32ab-b92a-4510cbba1b4b | -3.43037 | -50.34106 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f20c14de-c4b9-3f45-ae0d-da11e96c19bf | -7.19315 | -46.51033 | 2026-09-27 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48669ce4-8687-3c8c-928f-4a1b45589d5c | -6.13257 | -44.58876 | 2026-09-27 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 826c5ac3-7e52-3527-a16f-cf369d17d8d8 | -11.37022 | -43.3988 | 2026-09-27 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1da636a8-9e98-3733-9e2d-8784aa3f7eca | -7.37538 | -42.10171 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 688672c7-c44d-3917-a8db-c154dc8f73ae | -5.18322 | -41.14687 | 2026-09-27 04:08:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 25b6db85-0b9c-32e3-ac67-457063601f37 | -7.34032 | -42.08091 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e582e268-7b59-35a5-9f09-bfffd6da25c8 | -6.93935 | -41.61371 | 2026-09-27 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9c5dd2e0-05ae-3bd1-9b4b-22f2b71b3927 | -8.35764 | -44.17155 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 1ccd9c84-fccd-373c-bbb7-b8054b327e63 | -11.05008 | -43.23211 | 2026-09-27 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98354ea2-a3f9-3b1a-b1e9-fb2917b57c86 | -10.93449 | -43.75407 | 2026-09-27 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba9cb573-4521-36c6-b783-1f12490ae2f3 | -8.3503 | -44.1478 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c75722fe-6a29-3ad9-acda-3c6ec2e62b51 | -5.21484 | -46.02661 | 2026-09-27 04:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 294a1090-a391-3a29-beed-33def1e60bc6 | -7.36058 | -42.10686 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9e33f2ec-0582-37d3-baf7-85b6055358e3 | -8.34062 | -44.18232 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a9864d1-e7c3-396c-9705-46f486678b22 | -10.01773 | -50.15345 | 2026-09-27 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b7b2aff-dcd7-3115-b4a2-90212ee72a7d | -6.04938 | -53.61217 | 2026-09-27 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 106a1803-376f-3bf7-8a58-59bfbaf96a9e | -11.34305 | -41.85094 | 2026-09-27 04:08:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 82745c84-4617-38b1-aa9d-9ab56241d6d9 | -8.34965 | -44.15816 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f02b690-5820-3511-8782-85df606e24e0 | -11.34694 | -41.84796 | 2026-09-27 04:08:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 803b602d-d2c1-3db4-b662-9ce8266fd6b5 | -10.107 | -50.19605 | 2026-09-27 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea7439db-7084-3bae-97ae-f309ddea1e6d | -6.40307 | -42.78782 | 2026-09-27 04:08:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 09b210f6-b501-38ed-98c2-a51a927672e5 | -8.34227 | -44.15692 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README17.md)
