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
| 3230270a-1b90-34c3-836e-2db860de1e3c | -6.35924 | -44.50111 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b55a6af-a984-35ed-b9fb-dd7178d63849 | -3.07865 | -48.82374 | 2025-09-11 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 114f0bcc-d999-3191-af3b-c65a9a64aa37 | -7.46498 | -45.28392 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e5e09d3-4b8c-30c2-825f-9e2506f45752 | -5.76847 | -43.14977 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 970feb4e-2a68-3aec-943e-508ae0927275 | -7.49032 | -54.9482 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 856ef272-7d37-3245-ae3e-a813fb7352a2 | -5.59693 | -48.11816 | 2025-09-11 04:21:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4fb5f797-a863-372c-9671-28b51b2a0e0d | -6.19346 | -42.65911 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 45ab19db-35a2-3f5e-acb8-e4292c7e6265 | -5.97575 | -44.72216 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5df80246-492b-3b0f-9d04-5c3e21ac3b65 | -8.53718 | -45.56589 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7dae1f1-7fcd-3d30-a3a2-f3c8f9297e13 | -8.64836 | -45.72088 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5fe20788-1cab-3f9c-8b76-442bca3acfa6 | -7.26761 | -39.38023 | 2025-09-11 04:21:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8da33230-6583-3bbb-8c63-ac17e72ae6b4 | -6.2434 | -44.80293 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1887e151-9073-3bb6-a469-b0f6e64f2ab8 | -5.65055 | -42.62759 | 2025-09-11 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 066bcc0b-5d45-3ff3-888f-b3230e97ad92 | -6.53218 | -44.6036 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20c11929-d8b8-3bf3-9538-a1a0d294b480 | -7.40863 | -45.85141 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fde3cfbb-02b8-3fee-a71b-4245d3549c5e | -6.85242 | -44.86556 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21d073aa-0e43-3ffa-b054-964170fa264d | -6.40475 | -44.38086 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8be607e0-cc7d-3fe3-9235-d7282ad222c2 | -9.15964 | -45.56545 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63f15713-f895-3990-aaae-4a7b6bf7a8d2 | -5.56251 | -42.92571 | 2025-09-11 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ce5e9801-ea3c-3c72-afea-dc98aa9a5333 | -8.03384 | -49.04865 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 01806f52-b60b-33a4-ae99-0b41e8c93d35 | -7.67843 | -50.27776 | 2025-09-11 04:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 141977f0-ee22-3ab1-b363-d8603b0e2c31 | -9.03803 | -45.73663 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7155928c-10cd-341d-b009-080bafbed066 | -6.38347 | -44.43381 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 098b2de6-a07d-3024-a035-b9e60364513b | -6.99496 | -44.79513 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8935d809-ea8d-3e4f-8ead-51d2966ac662 | -7.79115 | -47.93992 | 2025-09-11 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 581ae675-d664-31cc-b6e2-92300e9944aa | -6.48374 | -41.7492 | 2025-09-11 04:21:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9a0c28c0-dc60-39eb-b4b8-01047e62c189 | -5.90957 | -45.75404 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a71cecb3-6e19-3014-b8ab-b6273cb1bf94 | -7.65902 | -50.26721 | 2025-09-11 04:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d637b1d-f6ce-37f9-94ad-5a2afe910c2a | -7.79474 | -47.94051 | 2025-09-11 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b5ea31d-9dcf-3675-aad8-a36be4e799b9 | -5.45662 | -44.00067 | 2025-09-11 04:21:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ce29560-8f55-3b63-a15d-620bcf9d9d1a | -6.81477 | -44.88801 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b643a925-4f76-3f60-b8b1-2f30c6e17780 | -5.86459 | -44.2249 | 2025-09-11 04:21:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 81889f51-299b-322f-8775-99947e48e1ef | -4.13617 | -38.70313 | 2025-09-11 04:21:00 | NPP-375D | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2b62fc2c-e871-3edb-8db2-999731c10f2a | -6.57014 | -44.2106 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 061ee288-5c8f-35ac-a6ee-a246deffe38f | -8.51766 | -45.6885 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1aa47ad9-acc4-36b9-8606-30e773fc6003 | -6.40417 | -42.60527 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 56d1d932-b3f9-3e97-8612-ee0751ea53f0 | -6.30564 | -44.5816 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a26b05d-95c1-3189-9a8d-88cf56808fe0 | -5.54053 | -45.70353 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec48be1a-dc38-34a9-9068-de5dfe3e5427 | -5.89884 | -45.77791 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3395d92e-778d-36f7-81f5-d83bf4ffdc76 | -6.33519 | -43.55065 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88ada644-313c-37fd-9176-d6cdbd0886f7 | -6.37265 | -45.16636 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 727825f3-35cd-3b4d-a531-6ceca837ff44 | -9.03187 | -45.77529 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b51dfda-c9a7-3c15-8d2b-2e094340f085 | -5.44941 | -44.00311 | 2025-09-11 04:21:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b25214fc-5055-3255-9947-2f1474315781 | -7.21796 | -45.31288 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65cb5a72-df61-31f2-b770-2080b19fd262 | -6.80399 | -43.26965 | 2025-09-11 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5dde65b6-38ab-37f2-8822-19ec4c0cca69 | -6.41039 | -53.65376 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2255393-c85e-3794-b771-94d2d7a63bcd | -7.18721 | -44.96871 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a8ae56a-6455-33ce-90ca-3f56d49b8b45 | -5.77337 | -45.52904 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 262a577a-3d11-3ff8-853c-8d9c27cd4000 | -6.54106 | -42.44272 | 2025-09-11 04:21:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3cc3eaf0-5a6f-3319-8544-4cda82697aa3 | -5.75151 | -46.26119 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d730185c-0d43-32c2-b199-fc1c47ae2d58 | -7.70253 | -47.29633 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12d0e3d4-52c1-373c-b1e0-64607b7172d3 | -6.83542 | -45.61111 | 2025-09-11 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f455bb0-e275-34aa-8303-80a4607b71ce | -5.8289 | -44.83437 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cab9ae18-5113-3508-9c45-d35b31b1d6b4 | -6.34947 | -43.41398 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3314540-3d3b-3e4c-82e7-ef78c5acbc43 | -8.04106 | -48.68184 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c346357c-a6f3-33d3-ba08-f5638c595aa2 | -8.9658 | -44.93253 | 2025-09-11 04:21:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e1a2318-dd4d-3718-8dab-f32aad74467c | -7.30837 | -49.61271 | 2025-09-11 04:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b84d04d-1c63-3cca-b30b-2d21d983df5b | -6.90842 | -44.55388 | 2025-09-11 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c68a72ad-23b7-3c63-92b4-082ff57eddee | -6.04827 | -44.81861 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8b224fc-176b-3c89-94f5-5831854aa7e3 | -7.73012 | -50.7339 | 2025-09-11 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fdbcbbca-b573-3ce5-8a36-39a6287dcfd7 | -6.41773 | -44.49327 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91cf9abc-65fb-3146-b9df-3bd8ff067ea5 | -6.53551 | -44.60412 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7051505-869f-3b1d-a5b9-6f97b4432d43 | -6.38031 | -47.2588 | 2025-09-11 04:21:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c46f0a1f-4bb4-346e-b103-2323db246cf2 | -8.74726 | -47.1061 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d78c9853-aee8-342f-85e2-f87d2a877921 | -5.83123 | -44.17691 | 2025-09-11 04:21:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc7586ec-cf76-3b0a-aba3-23e94c75e012 | -8.52489 | -45.68606 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fef176e-257f-3c95-b1e1-3e6a7efa1190 | -6.57069 | -44.20711 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b9da320-c3c0-32dd-b526-4fcf062c6390 | -6.8576 | -44.89101 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ebaba679-0727-3222-b8b8-7abbfbf60260 | -7.19109 | -44.96576 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23152d4d-4bd9-3837-9540-dcc88eb14a9c | -6.24991 | -43.49027 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab053fd4-e315-3731-80de-4a43b9d88b64 | -8.73068 | -47.09954 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 89e98569-31c6-336b-817f-09a07082f096 | -6.99163 | -44.7946 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a5c1c19-a881-3e1f-ad2e-4b5fd743d642 | -5.36419 | -45.97197 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d112ce37-c6e3-30c3-9003-4aed18269a87 | -5.94767 | -45.81873 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42409e7e-508a-3ddb-8812-61aef78edaf5 | -8.51987 | -45.69609 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cc056f17-c1ab-33a9-8b98-ad6e9f4b5268 | -6.41641 | -44.39339 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c9c3b84-8b99-31e5-9a8e-32861238f915 | -5.22006 | -45.43041 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 569606e0-922a-34c8-8958-902abb901515 | -6.19403 | -42.65538 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d415aaf4-e39a-37d2-b6eb-694cdcbe804e | -7.26305 | -44.89873 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b6100cb-816b-35ca-8f5f-233428d1484d | -8.01929 | -49.02382 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f20a7db7-0808-30c8-b14f-a7a9d5e02d8f | -7.36715 | -47.42479 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36b79333-6466-3db4-b613-05f712a99c18 | -5.5514 | -45.08677 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad9b0666-bfac-3392-89b9-1f3f8e712caf | -7.29321 | -45.17459 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6915187-a9b8-33ef-a776-feeeed28d352 | -7.31942 | -49.61985 | 2025-09-11 04:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 470f11b8-4b88-3f2f-80bc-a4a4858070e9 | -5.94617 | -45.7195 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 833ae093-0fc2-3515-bc2f-3d215cbd5ea4 | -5.66258 | -43.89401 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46f7989c-ab5e-35d0-b0b6-0b4d5ac1ee17 | -7.50423 | -48.24736 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c53a6f5-8985-397a-918f-aa92f072b972 | -4.40325 | -50.55997 | 2025-09-11 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91346386-ae6e-3588-919c-4ab9b1c38392 | -6.83598 | -45.60759 | 2025-09-11 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d08174fe-54dc-36bf-a50b-c10e6cd9659a | -8.93676 | -46.15467 | 2025-09-11 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f09f71ec-da5c-3c29-9532-f15b9cd62c1c | -6.75974 | -39.26604 | 2025-09-11 04:21:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f77875b8-7fcc-3391-bbb9-d0882a61dc35 | -6.90419 | -47.90179 | 2025-09-11 04:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b86460d9-fe83-3541-a9c4-71eca614e802 | -6.32053 | -43.41349 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e37697f-f332-3455-bdce-58f1693070df | -6.99715 | -44.78122 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 089d5150-d25e-3837-8945-9d59e09cd54b | -7.92075 | -44.84595 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43bf1292-4cc9-3fe3-b36e-26e331e81cd4 | -7.45428 | -38.18246 | 2025-09-11 04:21:00 | NPP-375D | BOA VENTURA | PARAÍBA | Brasil | 2502102 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 38831dff-5173-33f7-81ca-aaf31f70dbea | -7.10775 | -50.75895 | 2025-09-11 04:21:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46b337ad-c5ee-3be9-a588-03ed95b76ec2 | -6.18949 | -45.65939 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02dc32d6-0b68-3697-957e-9bf2e42b27ef | -7.38641 | -50.88593 | 2025-09-11 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cbe502b9-3218-3d14-86f3-bdd999dc00e4 | -6.25664 | -43.49131 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README49.md)
