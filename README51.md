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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bd3c357-fde5-3159-980d-d32e681a21a0 | -6.8245 | -52.82539 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 034e0050-5a0a-3bc4-a56a-8e85496a8d85 | -9.22927 | -47.10733 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd599ac0-dbda-37b0-9939-75fa32d47faa | -6.43441 | -55.61582 | 2025-09-01 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ad8b80b9-18ff-3c73-9971-afa07d092e5e | -6.84294 | -52.81261 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0fc79fb0-2a06-39d3-862a-693c671ef549 | -4.15015 | -46.79161 | 2025-09-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2b0b05b-4ec1-39a3-ba42-fa1ec99e056b | -7.44719 | -44.83292 | 2025-09-01 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e745d111-6cd9-3e75-9bb0-807431fa8f95 | -7.97572 | -46.41898 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec7edefd-66d4-37ab-a07c-cb1db7490235 | -7.15009 | -45.14727 | 2025-09-01 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e86f4ed8-a6ea-3c8f-879d-4cda21b757cf | -4.07455 | -47.96032 | 2025-09-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbd20d5e-870d-372f-87b7-dcd673dd1029 | -6.41335 | -43.62626 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf225ec7-b803-3ee7-8507-05d554aab82a | -8.82032 | -47.49894 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 717763a9-1b92-3c40-b2c9-bfb98ead67c9 | -9.63225 | -47.82103 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e007c52c-846f-35d8-8dbd-744a2312d106 | -6.3275 | -53.43209 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e0d78d3-476a-3f9c-9a17-16fb40682f6a | -3.44953 | -52.72237 | 2025-09-01 04:32:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68d20d1b-3f29-3d91-bec0-44c09fdeaa3d | -9.22141 | -47.11353 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dea06c1-865a-30e9-ae16-a188e68c2949 | -6.33935 | -53.43805 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d09c98d-bf9f-366d-905d-cfcd514e78f6 | -7.84501 | -46.95375 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74dd54e9-7400-37ed-abd1-3804bdbcc7f2 | -6.5758 | -43.69905 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 74a2696a-ab4f-3ca0-9781-fff71c64a7fa | -7.45825 | -44.80893 | 2025-09-01 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfb0a59c-a91d-3247-95d0-1c1d1f61392b | -6.56797 | -43.7103 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bcc2a632-59a2-306b-a725-c62bbd5b40de | -7.10217 | -45.34597 | 2025-09-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd501f1c-a2b5-32c9-bdca-42be3d7d3ef2 | -7.69949 | -44.99599 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecdf9214-a360-3008-b846-54522db96f78 | -5.82462 | -43.86924 | 2025-09-01 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a0d38f8-898e-3099-8a36-9cc1335486ee | -6.64388 | -44.26051 | 2025-09-01 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed9f0c14-00ed-3b7b-b1bc-1510bc45373c | -6.30214 | -43.64742 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63fcb017-449e-3fad-8848-bda2f2e570e8 | -5.85185 | -42.5312 | 2025-09-01 04:32:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d8ea7d9b-7f8a-3f1b-8db4-10f842e916b8 | -6.33994 | -58.17903 | 2025-09-01 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a938b7b7-7ea7-36b3-9b44-6dea1d7d5b7f | -7.67268 | -61.10019 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 12fed585-b732-3ca4-9f0e-ffc11c7d9a34 | -6.76426 | -44.62792 | 2025-09-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 550bbf08-8bd5-30fc-87d1-5b3812173d1c | -6.62986 | -44.37966 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94aa1985-1aa5-368a-8bb7-831bab3bdae7 | -7.58667 | -42.6872 | 2025-09-01 04:32:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dbee3091-f4db-35a8-8647-d7550ac99be5 | -6.59111 | -43.63574 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79dc6836-4cda-3a4d-aeb6-8141637f2a9c | -6.83018 | -52.81576 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 277227d7-f6ef-3ba9-8b9b-c2d7f4246b5d | -6.33442 | -53.42468 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20cc3b99-f1c8-315f-b8bd-2c21ad62414e | -6.83157 | -52.83194 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0aa65ecc-8131-37a2-b4bd-47ad244b6539 | -7.11179 | -44.77745 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c5e17ed-4118-3453-977c-7e026fca5b7b | -9.92929 | -51.6258 | 2025-09-01 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6092c0b-7d2d-3fe8-8dac-6d9d15bf26d3 | -11.08347 | -44.62893 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41fa2fa6-0068-3607-972f-fd7032b77609 | -7.61829 | -42.65632 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 07de3ae9-5573-3b73-a753-74118340cc68 | -8.83402 | -47.49312 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5cb3abc-4338-3302-9309-100e9cd716d2 | -10.7514 | -46.3589 | 2025-09-01 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed41bfbd-dbe4-3e92-877a-e7e95bc69bb2 | -6.19527 | -43.33943 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cbcf5a34-40d8-3e89-917c-7f7b0acc5bd5 | -6.33707 | -53.42591 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b50c2357-dc6c-3874-b755-095f6b10643d | -6.8452 | -52.82359 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f76308d-f81a-373e-976c-a94b06414129 | -10.03961 | -48.10185 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68d8a6d5-39d7-3157-a254-b207405b8004 | -7.62349 | -44.03786 | 2025-09-01 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39e6544a-12f3-33c7-a021-2e560aed86c4 | -6.26866 | -43.55433 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90a5d90f-f15b-3400-b8db-1d30b8d2d73d | -6.12702 | -42.94112 | 2025-09-01 04:32:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b77be9d7-9876-3c8d-9615-45275184068c | -6.46716 | -41.74984 | 2025-09-01 04:32:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 93bf4f80-4a48-32dd-9c24-43113c4adc89 | -7.0795 | -44.34559 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e928dd8b-baea-3955-891e-78b2e2324e3d | -7.11066 | -44.55872 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20f66a5f-b8e2-31c7-9af4-904547e0bc04 | -8.06168 | -48.41631 | 2025-09-01 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4381ef24-2bee-392c-88b7-16f312c49267 | -9.92575 | -51.6251 | 2025-09-01 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 293cfe2f-f31c-3b97-99a0-1b2e226d6ba0 | -6.56988 | -43.7129 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d816b9d-abf7-3798-b4e1-837ca1e53270 | -8.08383 | -49.94039 | 2025-09-01 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a949ce59-b2d1-30ce-a6e4-e257c3600408 | -8.44413 | -47.36002 | 2025-09-01 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81fc1ec8-020c-319c-a102-2db4768169cf | -4.161 | -46.78624 | 2025-09-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bba87909-f915-3dac-aec9-80e6a22e2528 | -8.33283 | -47.44416 | 2025-09-01 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4f4e304-33f8-3237-9a64-771a6100021b | -5.82358 | -51.37759 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 965dece0-e17d-37e0-9424-dbb51e49669b | -4.12603 | -47.65724 | 2025-09-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d07afdc5-6d32-3215-bfbb-7c1673bb3657 | -7.94388 | -46.44445 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a5e6c3a-9025-376b-845d-e7e85f1451e9 | -6.83104 | -43.32245 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 5c193851-eff8-30df-8302-456d749adab7 | -7.70034 | -50.27517 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7592c71-a921-3941-b7e2-b89ab99f01ab | -6.18378 | -44.21255 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 237c1e45-a8e7-3f22-907f-3e2c69bca56d | -8.19861 | -46.77218 | 2025-09-01 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a750b4aa-227d-35c9-8440-b91f6c2c8abd | -8.83742 | -47.51538 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32feb039-4de6-3e18-8a22-bafce427b539 | -5.73485 | -45.53396 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47c85923-42c3-369b-bb35-c77b1128acab | -6.44703 | -43.97326 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| eec7786a-cc48-327f-ae1e-aaf6d4933a7c | -6.84133 | -43.33437 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d35860d6-26e3-3f24-b36e-e2b34cba4ff2 | -7.5885 | -42.68678 | 2025-09-01 04:32:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b6b5b09e-186d-3cf5-bfc6-53fcea886537 | -8.95196 | -47.85095 | 2025-09-01 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bab06c5e-e907-365d-9af6-4eacf35c77cf | -9.25262 | -48.18542 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37252a78-ca07-3a94-98b1-6fb4aa072f18 | -6.1516 | -43.33805 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3079179d-6eac-3137-ba41-887282f3591e | -5.62194 | -42.62285 | 2025-09-01 04:32:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9e5e05f4-2345-3782-9336-676b0e5b467f | -8.82035 | -47.80128 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f7534e9-7935-3fbf-8282-cc3c12896b95 | -7.08563 | -44.3554 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 46f32d66-a0e2-3a3d-81af-22d4869dbad0 | -6.30026 | -43.79081 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be8b0373-f91f-3bf6-a486-3ff068e560be | -7.50491 | -45.83593 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef7d438d-c510-35c8-b8b1-01a6e5dd7aec | -7.84837 | -46.95427 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5b7d809-3330-3361-8853-20b7dec60ece | -9.4499 | -48.29148 | 2025-09-01 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 022c4e28-c5dd-3c5e-a82a-4dafa7bba08c | -8.82843 | -47.48499 | 2025-09-01 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dba5ba35-68a6-3cd3-86b4-53c88190c602 | -10.60192 | -44.33438 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 3b49a926-85a2-3111-aac8-d2417db340b3 | -8.83862 | -45.74078 | 2025-09-01 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f833ea8-ae48-3bba-9d06-6e6114c37232 | -6.57253 | -43.70613 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e04c070-057c-3867-add6-c811a584a4d7 | -9.26864 | -47.12085 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7d59b89-545e-37ff-bb74-0b0b73bd86fd | -6.53057 | -44.59201 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac8babee-e0f7-34de-ad60-01d5caad5192 | -6.7647 | -44.62679 | 2025-09-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 090c9f8d-8b82-3bbb-86b5-8bfcbbc55b9a | -4.16154 | -46.78279 | 2025-09-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b51f28d8-594d-3a10-aa8e-533b7a4b6a00 | -8.84403 | -47.49468 | 2025-09-01 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 540e9b01-c7ae-3f8f-be20-cacc5d36ec46 | -6.16014 | -43.33427 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0890e2c5-fce6-3a89-9f65-135b47a6425f | -6.9393 | -42.01513 | 2025-09-01 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5b452141-ccba-3951-ae09-bcc29e3e5783 | -6.28714 | -43.82661 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa786358-16d3-368f-bdae-229206557223 | -6.45131 | -45.60785 | 2025-09-01 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76be8d4a-978b-3afd-b41a-d87637e01dae | -6.96079 | -44.33839 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd4a9fad-64a9-37e2-ba3e-f76df511acaf | -7.11606 | -44.77378 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70688771-760a-3774-a9cc-b3d3345802e1 | -6.46838 | -42.42966 | 2025-09-01 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| bd07d417-2ace-393a-953c-285e05ff27ac | -6.26397 | -42.60999 | 2025-09-01 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d84743e4-37b8-3809-ab7f-046693e833c7 | -6.9491 | -44.05315 | 2025-09-01 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92b54f6d-6265-3392-8c21-7228611485fb | -8.8941 | -47.96019 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 390989aa-27a9-3feb-8e74-f6970eebfb6f | -9.26752 | -47.12811 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README52.md)
