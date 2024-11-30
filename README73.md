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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0ba2f6b-d2a7-38bd-848e-f90ed7444d8d | -3.36038 | -50.40717 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11388b85-f613-3d90-b42d-641dff239eee | -2.82996 | -48.47507 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7be02c19-1985-3c18-af0c-a433028e04cc | -3.47049 | -50.53051 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac7ade80-b585-3cc4-90fd-8a8d87f66a67 | -6.08599 | -48.04508 | 2024-11-30 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aba59ae1-c15e-302c-8558-e8afd4446f80 | -2.45169 | -53.99687 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbe8a65b-9d65-3a97-84d2-7ba01824b7a4 | -3.98094 | -46.72606 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd4c08a0-3120-3368-8503-a6c7e5977c34 | -3.26976 | -50.55453 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abbe93c9-662a-3098-b583-bcc8b2f71aa3 | -2.58676 | -53.9876 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c1b0cd42-0899-38b2-bc49-cf68f789778b | -2.46489 | -46.5494 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4f27249-3505-3721-8f8e-590f3ca89943 | -6.38137 | -44.75652 | 2024-11-30 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62dfc1c3-448d-3626-928e-763cb26733d6 | -3.07197 | -49.10422 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4eb3eb5d-8849-3673-8174-9c73e9948bb0 | -2.03615 | -46.50936 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f605827-3546-3d4d-881b-3a09d8182a28 | -3.83138 | -50.13961 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| decd6399-13f7-30c5-b4cd-dc7898fc127a | -1.18888 | -51.76534 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 566dd20d-c832-3ffb-8ad8-0860228cf561 | -3.95888 | -46.73044 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7eb5a7d8-1040-32ae-a7a9-65bf80b69802 | -6.9145 | -43.55244 | 2024-11-30 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 39.5 |
| a7968d6e-adbe-3039-a7a1-8374d69bb7fd | -2.70917 | -46.18605 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb0bc3b3-1ce8-3d7b-a87e-500709c8b585 | -3.78518 | -46.70119 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a6901352-f4f6-3764-809c-5d7f5f04502c | -4.17023 | -48.62761 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d82a8dc9-8c96-3943-91f8-0d12dee66188 | -3.25866 | -48.89112 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d82da7a-d9bd-3f35-adea-11123006c17f | -3.74175 | -50.79157 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54e7976c-2bba-3a90-9e8b-27d4a0cde45a | -1.61587 | -52.29212 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e2ab835-2d95-389c-9b66-83c44c687196 | -2.01406 | -51.20002 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 29cc3ec3-14f7-3660-b513-40bd13d444ae | -5.58659 | -45.20729 | 2024-11-30 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7a295a06-9331-35d6-a3f7-bdfcfa093fdf | -2.5525 | -46.23608 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31e46745-07af-377c-ac0a-68ecab645aef | -6.86583 | -47.23476 | 2024-11-30 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9530817e-4cb4-3493-9c42-3fd592a80127 | -2.90142 | -49.45514 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e74f2a0-50d0-30ba-a177-a10af8a16f74 | -4.50871 | -50.13832 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b877a861-afc5-32a8-aba3-4b6a0bb3eed6 | -4.81942 | -41.28145 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 30a74347-e4ff-3634-b3e7-111819d58b0d | -11.3179 | -49.00948 | 2024-11-30 04:42:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45b1b58f-ad0e-3ed7-b305-c4a3e073abfa | -11.19853 | -49.17362 | 2024-11-30 04:42:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f7cf0bd-49fc-352d-aefd-234faa401329 | -14.10847 | -44.08488 | 2024-11-30 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4db19d5d-03a3-313e-a17a-9c97f43aeed5 | -10.22231 | -59.08485 | 2024-11-30 04:42:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96ef93a3-0d15-3a18-9521-d8f349ba6c09 | -9.20378 | -63.61269 | 2024-11-30 04:42:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b48d281c-7954-3c64-a4a7-9be3a951870a | -10.88081 | -54.31839 | 2024-11-30 04:42:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 211874b9-69de-3829-a978-4418d5337764 | -9.41334 | -63.23553 | 2024-11-30 04:42:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0fe3e816-c514-3d34-a434-36db6c8d12f6 | -11.76866 | -44.63485 | 2024-11-30 04:42:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c3e3927-03b5-3646-b592-c7a1c8f49abd | -10.46486 | -45.08762 | 2024-11-30 04:42:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fde4812-86e2-318f-867f-350464f4ff51 | -11.77301 | -44.63548 | 2024-11-30 04:42:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f50b7a8-1381-3a3f-8d28-ea3909b00e3e | -10.77393 | -48.16294 | 2024-11-30 04:42:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be6b4ab0-5eed-340a-a8d7-ed62a35a2b5c | -10.45389 | -44.94081 | 2024-11-30 04:42:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1bd03ea7-4d25-30a1-8f0c-ae6310661306 | -11.41259 | -45.09882 | 2024-11-30 04:42:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5509accc-6396-372c-a820-e4caa533ee6f | -11.40858 | -45.091 | 2024-11-30 04:42:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2a36237-9959-314b-988c-2718fb28785f | -7.98483 | -55.30261 | 2024-11-30 04:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e84e40f-1f28-3616-ab27-ae343f1f1215 | -9.08872 | -49.57812 | 2024-11-30 04:42:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99baa50c-ae32-32a5-9227-903f58de5b19 | -10.54085 | -44.68666 | 2024-11-30 04:42:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4419be9-6286-30b3-837e-92c2ca2d5daf | -10.46434 | -45.09139 | 2024-11-30 04:42:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdb92c44-da29-3c58-afb5-7ccfd700180c | -10.66217 | -44.48977 | 2024-11-30 04:42:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3ee70d1-76dd-3c2d-9cf9-9cb557dfb76d | -7.89271 | -63.26696 | 2024-11-30 04:42:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 599b6e6e-c8ce-383b-a552-9418b3f41d2f | -9.73231 | -48.13289 | 2024-11-30 04:42:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9aa3efe-4f7c-3d7f-9ae6-65a3fa964459 | -11.41311 | -45.0949 | 2024-11-30 04:42:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0616591f-12b6-3bba-ac73-2ab1515704ec | -9.04538 | -50.01141 | 2024-11-30 04:42:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4febdb6-1229-3365-a194-07f13695be51 | -7.98039 | -55.30563 | 2024-11-30 04:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5844e487-c69d-31aa-b28a-44ad6cc2491d | -10.4549 | -44.94063 | 2024-11-30 04:42:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2bd437cb-be91-3efd-b7e0-12cb51fd8dfb | -11.40804 | -45.09491 | 2024-11-30 04:42:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bba3a49-d853-3c3f-bd84-eb707b5a0b6e | -10.65671 | -44.49757 | 2024-11-30 04:42:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f00a0f93-bd3a-3341-b6d4-cfa14bfc9edd | -9.0854 | -49.5776 | 2024-11-30 04:42:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4426bcf-dec6-3e92-bd4e-8655eb66c527 | -8.91831 | -49.84474 | 2024-11-30 04:42:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5292132a-f5f6-3f18-ac17-8b83e8fa309e | -7.89392 | -63.26068 | 2024-11-30 04:42:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d2726c16-3d1a-3db0-9b49-697c0fd28950 | -8.8227 | -49.69402 | 2024-11-30 04:42:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e054268-22ad-368a-b480-79d925a2d014 | -11.83834 | -43.72391 | 2024-11-30 04:42:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba161499-2e87-3fde-a82c-590080f6d3d7 | -8.14212 | -54.86156 | 2024-11-30 04:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecaf5bc5-9c11-3c6b-8724-35f1cbad5822 | -9.08154 | -49.58059 | 2024-11-30 04:42:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebd4d8f1-deeb-3a0a-a1f2-208ffff20a25 | -10.09347 | -47.57089 | 2024-11-30 04:42:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07ef67d8-d222-3684-8556-17f4db9bba7e | -9.04208 | -50.01089 | 2024-11-30 04:42:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49840792-c6c0-3211-8fce-fd941a94c512 | -10.42472 | -44.90468 | 2024-11-30 04:42:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5522558-4c2a-3acf-ba22-3cfe78525dec | -10.5414 | -44.68265 | 2024-11-30 04:42:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e5bfaa2-15ec-382b-a25b-0a1b2c89cd68 | -10.65784 | -44.48914 | 2024-11-30 04:42:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a829cacd-445b-3c80-9c50-459df460d335 | -9.08486 | -49.58111 | 2024-11-30 04:42:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31af92ef-86eb-3cd2-baa6-ace37aa8db42 | -8.14297 | -54.85642 | 2024-11-30 04:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcb5a051-4365-36f5-944c-1003817548c3 | -7.98507 | -55.30268 | 2024-11-30 04:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4a8f78a-e225-3186-8b67-4fcc6330ef6d | -10.45335 | -44.94468 | 2024-11-30 04:42:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5047c10d-ee72-3f45-b693-8985e7991c2c | -10.42893 | -44.90524 | 2024-11-30 04:42:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2631802e-ce3e-3904-bf3e-1c6bc54f81b9 | -10.45438 | -44.94451 | 2024-11-30 04:42:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 99baab66-7933-3752-9927-b3561d7faec5 | -9.03877 | -50.01037 | 2024-11-30 04:42:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82044644-b0d8-3e18-b5c9-ead4257a0b96 | -8.15256 | -54.84755 | 2024-11-30 04:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c97664d-e417-37c3-be72-64e1c5421dfa | -9.04593 | -50.00793 | 2024-11-30 04:42:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16dc2c85-01be-33bc-813b-d55ec64ec0b7 | -11.41679 | -45.09943 | 2024-11-30 04:42:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00652b4d-5fb3-33d5-87b8-d19d187ec3b1 | -10.45807 | -44.94147 | 2024-11-30 04:42:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a848f8a-b122-300f-a1be-b4734c82ac59 | -11.40891 | -45.09428 | 2024-11-30 04:42:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88762904-0e71-36a1-b6df-50416e7be9b0 | -7.91618 | -61.54752 | 2024-11-30 04:42:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3e0215e-5565-31c2-8309-0bd9ba0b386e | -10.66593 | -44.4946 | 2024-11-30 04:42:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2adb2b25-810f-3966-9005-a60537556dd2 | -8.13902 | -54.85577 | 2024-11-30 04:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cf20777e-6b80-3a4e-83ac-beb0e6faf643 | -7.97632 | -55.30495 | 2024-11-30 04:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e3103c7-719b-384a-b857-50d0fdb4768a | -11.41224 | -45.09552 | 2024-11-30 04:42:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ffe59bed-f1a8-3801-a18e-a400b1a7bb30 | -3.97729 | -41.50577 | 2024-11-30 04:44:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| b78b4e19-a81f-3b22-be2c-3422e6d19ac0 | -7.21649 | -39.76835 | 2024-11-30 04:44:00 | AQUA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ac4cbfbf-d8bd-34e3-be5c-a57d1061b5e4 | -7.21703 | -39.77386 | 2024-11-30 04:44:00 | AQUA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| f1e812b0-6972-3d93-a70d-0511de23c595 | -6.92415 | -43.54934 | 2024-11-30 04:44:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 65e3b8c6-d507-36a4-a5ea-ad1502b18727 | -3.94498 | -40.97022 | 2024-11-30 04:44:00 | AQUA_M-M | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 5f02f3fc-256d-32b7-94a7-6c68fc79c434 | -6.13821 | -43.94152 | 2024-11-30 04:44:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| a6585c6b-2138-383a-b138-1abf5ed3a659 | -3.97463 | -41.52306 | 2024-11-30 04:44:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| ee3d39b2-02b9-3637-956f-d2b9b276886a | -5.89874 | -35.42019 | 2024-11-30 04:44:00 | AQUA_M-M | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 116.0 |
| 37504d42-2d5f-343a-875d-55dc1b459dce | -4.87263 | -41.28419 | 2024-11-30 04:44:00 | AQUA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 28.9 |
| 34d4003d-0af0-3896-b1ef-98f3cf4f9fd7 | -5.90007 | -35.4112 | 2024-11-30 04:44:00 | AQUA_M-M | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 19.0 |
| f081eb82-45de-3d0e-bed2-b71f9ad1759e | -4.87015 | -41.29973 | 2024-11-30 04:44:00 | AQUA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 30.6 |
| e3cc77d7-cde6-349b-8425-9060df385a34 | -4.87511 | -41.26874 | 2024-11-30 04:44:00 | AQUA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| b8c09821-5c14-3bf5-8e63-8ed46af1d775 | -3.98931 | -41.50759 | 2024-11-30 04:44:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 866da359-4de5-3d23-b146-e40a611a1d67 | -6.39891 | -35.02887 | 2024-11-30 04:44:00 | AQUA_M-M | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 291a46c0-5ac0-3f19-9535-f31a6d664d65 | -6.18398 | -42.6081 | 2024-11-30 04:44:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 45.6 |


[Clique aqui para ver as próximas entradas](README74.md)
