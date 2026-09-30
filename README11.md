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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab3ce81d-e953-3411-8803-275be9aa43e1 | -11.81207 | -43.32122 | 2026-09-30 03:55:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5f0716e-2cfc-3f2d-9189-83dc88030f3f | -9.86574 | -44.94323 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bb70ab0-da67-31b2-85d7-3a4557209b1b | -6.07884 | -47.28836 | 2026-09-30 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d78ff9a-5dea-3fe1-afa1-a8b5bf0dce7b | -11.17566 | -44.82816 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5089d783-f061-382e-bab1-0a78d6ce2f7a | -7.82726 | -45.8282 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 155ce70f-f22f-3526-89b1-6f6a1aa17f89 | -7.38006 | -44.7802 | 2026-09-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3bcdf434-827a-3277-ace4-e08b098e6ba7 | -5.74327 | -45.16009 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a3999b4-9cd1-316a-9e76-44b54b8aceba | -5.74621 | -45.17022 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12fd5ca5-820a-3e65-b9e0-588b57a2773d | -11.38625 | -43.46425 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f085a952-2392-3982-96a1-a600895a1c52 | -7.4757 | -45.78881 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 75cd1146-daa0-3d9e-b0a3-b656611e9019 | -10.88879 | -43.62527 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3b1fd0a1-8c78-3180-84bb-fd45c8773c90 | -4.45503 | -47.91936 | 2026-09-30 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a8b48394-447b-3680-bc1f-3290bd56cdf7 | -8.2507 | -45.43903 | 2026-09-30 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28d40845-9127-321b-9f89-64a6c4a77d85 | -8.27906 | -50.27168 | 2026-09-30 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2adb30d4-0b13-3fc2-a323-2c06155ffd2f | -7.936 | -47.37205 | 2026-09-30 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 532dd921-ea38-3484-ace3-d7e170d8fb90 | -11.46129 | -43.46156 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69820c47-ed40-343e-8bf5-a5ef30bb4949 | -7.45179 | -44.60954 | 2026-09-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d0930ef-ba17-3e51-96a2-8c972c9f0b90 | -11.63249 | -43.53434 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9eca168-441b-37b8-a9ed-6d46117e0c6e | -7.83806 | -45.8199 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f0c0d10a-4e02-3764-8ab7-8c39cb95c01e | -11.41667 | -43.46486 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1a1769c6-9431-3a29-bad6-155a9c503b66 | -10.73661 | -44.442 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aaf6643b-15f4-3317-8444-18c3ad257f75 | -10.15515 | -36.2414 | 2026-09-30 03:55:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e6ca4d3d-9b5d-3889-aaaf-0c9f98d3c790 | -4.28885 | -48.55836 | 2026-09-30 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b610eebe-7000-3102-885b-9fa5ad60d1be | -8.97274 | -44.17585 | 2026-09-30 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 82133396-d9cf-3ff9-af85-464943ba3fff | -7.85095 | -45.82694 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 59adf291-45ee-3215-8f64-1a830469187a | -5.03042 | -43.57237 | 2026-09-30 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b3e287a0-c8da-31ae-83cb-ee93e8646edb | -11.43332 | -43.42448 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 602ceecf-de16-3e53-bdae-ac04c4efe327 | -4.11771 | -48.82217 | 2026-09-30 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 497d90ff-217c-3ae3-a757-debbd2126801 | -4.94807 | -49.4174 | 2026-09-30 03:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8170f7a-11f7-3d3e-8ef5-39f4a3167ffd | -9.80564 | -44.83536 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91de936a-4eb4-35e4-8bd7-797126bdbbe7 | -11.6757 | -43.50474 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0aba1208-4920-3fbf-ae2c-99f394729f8c | -11.18309 | -44.83702 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f11a1bfe-0e58-3a14-9f9a-508dd7252797 | -7.82352 | -45.82261 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 822df9b4-6d99-3c50-99ca-4105b05507fc | -10.28731 | -44.64099 | 2026-09-30 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7612ec62-091e-3e60-b8eb-1cdd8c5aaf4f | -7.49246 | -45.80101 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a25e646-deb5-32aa-835e-f8617bf9f5bb | -6.07666 | -47.29374 | 2026-09-30 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cf87cae-9ff6-326e-bb26-6164bf2022d7 | -7.85169 | -45.82606 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 31eecded-9d82-3c8a-9063-41d5ce09ef1c | -9.12728 | -44.74952 | 2026-09-30 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5e781cf2-005b-3c0e-81a3-b43ba56afb42 | -6.28657 | -43.63622 | 2026-09-30 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3aa433b3-d222-35ce-8c95-72384cf0d612 | -5.72564 | -43.51168 | 2026-09-30 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2fbdb98-5eee-309e-8a7c-06c7f0e68753 | -6.29286 | -43.64815 | 2026-09-30 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23f13cf2-523a-372a-9a93-f6e5f86cf85c | -11.36582 | -43.35962 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb44cc46-c566-3c78-abe1-5168924cad3e | -8.36825 | -45.38961 | 2026-09-30 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c14da5d-b365-374b-8de3-4ee78672ac30 | -7.07193 | -44.36256 | 2026-09-30 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5fba916f-778d-3294-9362-498042e06e74 | -9.78827 | -44.81303 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a44ae31-feab-3723-8c3c-4af003d96a16 | -9.82019 | -48.20548 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d692055a-987d-3ec2-94cb-0f3355533474 | -7.81518 | -45.81647 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bc5bdf9-8aa3-342d-b613-c2a495e2e9df | -5.81621 | -46.21476 | 2026-09-30 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 95328bed-48c8-30a0-b2ef-421ad9a0743f | -10.90755 | -43.85452 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb733f69-cb82-393b-b578-1e3d7cc35678 | -7.85082 | -45.83095 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 874bd4dd-480f-3aca-8deb-11f77c22de6c | -11.20008 | -45.14783 | 2026-09-30 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b47b6569-bec7-363e-afa4-61f113acab4d | -11.18714 | -44.8377 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59890779-8cb3-308b-bcd9-9b24628e2500 | -11.19633 | -45.12054 | 2026-09-30 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5ae1ae4-4a47-3a73-b484-840ddf61dac1 | -10.83408 | -48.70219 | 2026-09-30 03:55:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a506e928-ca9f-32fe-bf18-961a868ff40f | -5.7264 | -43.28088 | 2026-09-30 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 697d7a10-89b2-37f6-8f0c-5b7d453109fa | -11.16473 | -44.77064 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f972f0e5-30eb-3b78-8a81-6841e8433e76 | -5.75445 | -45.17646 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f8384a0-aeba-38f6-ac35-f0c7689d8826 | -7.50532 | -45.80855 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3725ff19-1ce0-34aa-bee9-863ad0614af0 | -7.51474 | -47.33444 | 2026-09-30 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82c84393-e76c-3298-bd54-d6f98abbf03f | -10.9038 | -43.86032 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85000743-6491-3953-83ab-f4ef0de6e2d2 | -7.92519 | -45.44162 | 2026-09-30 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6b11c07d-33ac-34d6-bbb6-458a3f3e0214 | -7.06994 | -46.56985 | 2026-09-30 03:55:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15dd0e57-7e0c-3dd7-9eeb-145b0a0133cb | -5.75601 | -45.16716 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0ee041ca-6785-3a9e-8f44-80c908390065 | -8.36845 | -45.38668 | 2026-09-30 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fd8806f-4b8f-3eef-8dca-378f26533da5 | -3.38262 | -50.95213 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b3cb0c59-0b13-38e2-9679-d2945ef811a8 | -5.8153 | -46.22014 | 2026-09-30 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1d78aa12-5e0f-3236-8021-ce428429df9d | -7.4803 | -45.7895 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d615943-fa40-3d35-85df-853f5009a55b | -11.43548 | -43.43405 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 31442974-3354-3773-b9f8-1aa3302da7b0 | -7.1675 | -35.3621 | 2026-09-30 03:55:00 | NOAA-21 | GURINHÉM | PARAÍBA | Brasil | 2506400 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 111408b0-d200-336b-89c5-85eb129dc678 | -11.39738 | -43.46614 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 4cdb504f-e6f9-3be8-b5a7-f317d69ef905 | -11.18032 | -44.82521 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87dc1283-ad89-3509-ba69-9b95e5c623f0 | -3.97092 | -48.00407 | 2026-09-30 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e3d641c-5861-3cbc-a301-bac309355030 | -11.42336 | -43.42454 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| edc37df3-0838-3e04-8501-dd96acee12e1 | -6.33262 | -43.914 | 2026-09-30 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd1a22a0-9b8e-3086-87c8-0a1cc0c3fdb2 | -6.30444 | -46.06529 | 2026-09-30 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b79ead4-bac2-39d2-ad1a-af5fcfd94200 | -11.26266 | -43.55148 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98151900-245f-3b1c-a2be-ff9e74f88aea | -8.39003 | -45.44621 | 2026-09-30 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2533340-894d-387a-ba56-a8af5de66b5c | -7.84342 | -45.81974 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e07c072d-aa9f-3cbc-ac3a-e4d4fe385110 | -11.19289 | -45.11599 | 2026-09-30 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7185416a-5e2f-3964-8b00-e3545be855c8 | -11.39529 | -43.38757 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b06966b-097c-386b-8be7-cbe4cb5f65db | -3.37581 | -50.95093 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cf70668a-9fed-35b9-a580-93012d9ce671 | -7.68158 | -45.96275 | 2026-09-30 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca12f3ff-0846-366f-9a43-12f31978f0f5 | -6.33459 | -51.15143 | 2026-09-30 03:55:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9e63f900-bcc5-3cd2-8f88-3c744dba7c7e | -5.09553 | -46.04671 | 2026-09-30 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9569132f-a49c-313b-b86a-3ddce3b476c0 | -9.82073 | -48.21061 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba9a380f-015a-35f3-806e-8e2dbca0947a | -5.747 | -45.16553 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1908eb70-017c-3d5e-ac8d-8848f1a8a55c | -10.72857 | -50.50172 | 2026-09-30 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a75cb9d-c9dc-37b2-8a63-396504496a09 | -9.20336 | -45.74037 | 2026-09-30 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff11529a-3284-35ed-a4e8-76829a1d07e3 | -11.81429 | -43.3081 | 2026-09-30 03:55:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7258e0da-250c-3e71-b4ee-e9a434cf7043 | -6.36512 | -46.25764 | 2026-09-30 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3253ed1-7d79-3b9c-a7e2-bfef3cbba6a9 | -7.19286 | -46.50689 | 2026-09-30 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 774a6751-4fec-3fe8-a73d-42fa0f85ec09 | -3.573 | -50.25794 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ce91a79-d68f-3a24-bd30-2b08ac01c2ba | -4.11844 | -48.81792 | 2026-09-30 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 48580767-8ed9-3ebe-ac7e-fb26ca5279ea | -7.93088 | -47.37151 | 2026-09-30 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61e12cdf-490b-3a49-ae29-e81e27d206de | -11.94137 | -44.80506 | 2026-09-30 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71d3be4c-f8d4-3177-b4c5-e98d6a04afb5 | -11.3916 | -43.38694 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 606d284d-52b6-344a-a39f-23ef88a5e847 | -11.34961 | -41.27526 | 2026-09-30 03:55:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 92754115-f142-3c08-bf0e-3627a69fe0d2 | -9.81283 | -48.21669 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de3dd495-704c-333d-85d6-43e3dedc91af | -11.25519 | -43.55021 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b22afd40-97ff-3fcd-ba0b-31ff634958ff | -11.16753 | -44.77847 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README12.md)
