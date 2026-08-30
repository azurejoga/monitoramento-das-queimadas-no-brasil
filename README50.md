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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acaa7df7-8c8a-342a-95c9-8015e346ca1b | -7.56731 | -61.32032 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b99348f6-6619-3809-af29-3648d03de870 | -9.0512 | -65.40819 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 11ab3e10-a804-38ec-9d4a-f658fee521f9 | -6.97504 | -59.59422 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cc76380-22ab-32d2-98e3-316fa8f96171 | -6.61729 | -55.44864 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5aac869d-e4a9-316c-96b7-294832bd655a | -6.8822 | -59.40532 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a2047b5-c59d-3673-9c5d-c211e7ca14d6 | -8.62169 | -54.6949 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc4838d0-d65e-34a3-9947-66ec1d26f194 | -9.17616 | -59.6099 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 82c7ea8c-9c19-3790-ab57-295b63b7711d | -9.84408 | -60.27385 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1601bc71-0e9d-33c7-a51a-4d67a87a3038 | -7.58545 | -61.33854 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 732f3d66-e983-34c9-93be-7c93bf84e028 | -6.87215 | -56.56902 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9553e63f-a1c4-3932-8a5d-61c2f2fe374c | -8.97461 | -50.80516 | 2026-08-30 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bea688ef-3a4a-3302-a3df-9f455cf010a7 | -8.92886 | -67.37112 | 2026-08-30 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c1bd963-dddd-37a1-a3ef-4c71165a48db | -7.39771 | -60.57893 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35799c3c-115a-3024-bc65-8050684b400e | -8.65801 | -62.83978 | 2026-08-30 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e9051891-167e-3f48-9a89-080cf4314dd5 | -9.78722 | -59.43926 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0e4fcec-79f2-33f9-9304-7cf70f9a4648 | -7.01045 | -59.64951 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27f1ba9d-0ae6-3b1d-99c1-854dfcfe9a4e | -8.61612 | -54.79016 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bbc407c-d3b4-3a50-a626-54e209ac12dc | -7.55824 | -61.31123 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab88054d-e77b-3562-9884-7e291bbbd4e1 | -6.25964 | -55.42115 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cbdf086-18a6-39e7-a334-4b28db17b794 | -11.16166 | -51.31763 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9573d9e3-b80d-3117-b60a-ef87f2cd3ae9 | -11.16687 | -51.31839 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c79d7cd-6b88-3ae8-a862-00cd2506773a | -8.50523 | -55.28501 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 001bdbd6-cf43-3441-8ed0-2600aea4c863 | -5.4831 | -57.14406 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| db700421-ffd9-3277-b045-3f263b10890b | -6.19983 | -55.4164 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4d6b4e5-9712-3fcf-9c38-dd3d87ecc275 | -9.25917 | -57.52456 | 2026-08-30 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5018be6d-477d-35c4-925f-153867a1190c | -9.15215 | -59.50279 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ce0015c-1a06-3e1d-8083-726f58616a47 | -9.58809 | -61.02971 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8dbedc6c-f62f-3621-b577-720309f7307d | -9.01766 | -65.40234 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa6f1d62-6763-3402-bbf7-7bd1cb4b0bd5 | -11.18733 | -55.09974 | 2026-08-30 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 548b26a2-5788-3905-853e-8f93906a7c5b | -11.1635 | -51.29446 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 49ac54da-3b2c-388f-a784-e5086c8599e6 | -9.24377 | -60.41453 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3de25569-3deb-3774-89db-7b050ffb5d71 | -6.79631 | -58.99521 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d695f6e0-5248-332d-a8e8-fcd4effb9866 | -8.95174 | -62.37746 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bbe99ab-8dbd-31d2-9551-1f68f06f897a | -6.93494 | -58.95649 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f522faa-549a-3892-9ceb-fa6d4b4e6e2d | -6.76801 | -55.64846 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a2e3c78-0e6f-3325-9476-025e20bef4c8 | -7.55945 | -61.30378 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0b708c9-47b7-3a67-9a7e-1492df3a1a7a | -6.26333 | -55.42177 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ad749df-e944-3764-8e20-9138f473ec36 | -6.18795 | -55.44588 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d90c6256-c8d6-3eb8-b67e-2e8d3469a1f6 | -9.71081 | -60.74993 | 2026-08-30 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ed04b8b-5a55-379e-a745-f710f663bb81 | -9.04713 | -65.41174 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18926705-e7de-35da-b921-7af1d97110ad | -5.96542 | -57.68337 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25e60801-1f98-3c92-a750-d779d2147882 | -6.77054 | -60.00771 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b1ae7a4-7461-3e0b-8739-e34b6c4640e0 | -10.75191 | -54.03894 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e819516-e297-35ed-b26e-6e7964ed056b | -9.06966 | -60.48355 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbfb5fbc-3ec5-36fa-8850-724401b172d8 | -5.96597 | -57.6798 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35e31db1-e1df-3614-b2b2-547c5f965e45 | -7.315 | -60.61 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 15695800-92cb-3397-b670-58f8906b45e0 | -10.76423 | -54.045 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 015a18a6-aa4e-32c9-92a6-9d4c6beefa90 | -11.04058 | -57.2138 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 458d7048-5dde-34fa-bb3f-c4a437c39116 | -10.77339 | -54.04203 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f93d69b3-9609-3869-bcdf-998af3a6967f | -5.97441 | -57.69208 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| def97ab6-de51-371f-894c-e4ae87e6abd5 | -9.15768 | -59.51075 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af9aeed8-684f-39d7-8d30-825e8d47c5af | -6.93137 | -55.70527 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a3651c8-f3b3-3004-9457-5a67c2396a4e | -6.76736 | -55.65281 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e34e7f09-a063-3106-abfe-9b830749577a | -5.96261 | -57.67929 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6f74a25b-0d5c-3273-8388-f2abedba63d2 | -11.0382 | -57.23026 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 099d7be2-7251-3ad8-adb6-d05e41037a8a | -7.48428 | -61.3997 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8fb8582-4113-302b-8b8e-10f5eb0ca8a9 | -5.88857 | -57.76628 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6ae411b6-4138-3fa5-8654-ea7b4541c5a1 | -11.80482 | -51.04052 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| db18f0ae-5b82-3145-a230-e8891fafd804 | -6.94111 | -55.71553 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c490680a-887b-3fcb-b9c2-e31af2139117 | -6.15481 | -57.79961 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91c1b3da-dfcb-357e-91e9-a1e02fd8ec9c | -10.49097 | -59.61532 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d52a0bb2-d358-370c-93b4-fae83849937a | -6.79006 | -59.47229 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa5b4008-a507-392a-af9e-ed60ca58bef4 | -6.78913 | -55.68286 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b819f776-0c4b-3065-a291-4a8cffee657b | -5.88023 | -57.77588 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 809a9916-6e38-3d3c-988e-3c16748ca866 | -7.24101 | -60.6203 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 832a2e85-0d61-3e9f-be04-ba6a5b21e7fb | -7.62896 | -61.3301 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8fa5a4a9-28a5-3ae2-888f-b9478a6f02ff | -5.98503 | -57.69007 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8b7b09f-babb-3c00-92d6-5c737871ef15 | -5.88241 | -57.76168 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2a4c43d0-d0c1-359f-998c-881f52c9e110 | -7.34045 | -55.15701 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 960a3237-b1ef-3b6d-bce3-638b28ea4b24 | -5.48824 | -57.15607 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6589e925-19b8-3ec4-a6c9-832f53768f6c | -6.18425 | -55.44534 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99a9c003-ab02-3d72-90e9-71ae62f36286 | -8.97515 | -50.80473 | 2026-08-30 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5059bbb-b90d-3807-99d5-1cbf99c172c8 | -8.46879 | -62.71151 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d9631ee-25ba-3954-8b63-68fbcbe6733f | -9.16484 | -59.50831 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a00ef70-197f-34b9-8fc8-8f1afda1fb14 | -6.78714 | -55.66738 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f61bd063-f0dd-305c-8c48-36d4c1e2c63e | -5.87633 | -57.77892 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ef755652-1c76-3dfd-9123-bc08e7a2fce2 | -7.55079 | -61.31386 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 971060aa-52d1-35de-a3ef-02e4fd126d45 | -6.90569 | -59.79629 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 696cd8d3-7e23-374b-998d-dcd245beb670 | -11.15318 | -50.58594 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 74480576-1147-38e6-afad-7dbcb4380317 | -6.75701 | -59.4424 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c77c01b-8f81-377d-9382-135033957c1b | -9.63858 | -62.0853 | 2026-08-30 05:18:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81f7c0fa-6069-3f78-ac0c-930db90d0ddd | -11.03464 | -57.22971 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 068dfab7-b00c-3bda-92fc-8eaeb851f5e0 | -7.57837 | -61.29533 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0ee8443-9511-31be-8d52-01448cafb33e | -6.88231 | -59.44787 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58e16d8c-1471-3506-aa95-98dd06837519 | -9.89342 | -60.28579 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1c995400-9e5e-3022-bd5c-15744c76ff66 | -11.81017 | -51.04124 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 34.9 |
| cb5811ac-5559-3b50-a2d8-1d90dac4eac8 | -6.79481 | -59.39863 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0302291-828e-3049-b08a-f3d0c18a0fb8 | -5.96769 | -57.69103 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3fd4027-f528-39f7-97bf-fff48c66793e | -5.482 | -57.15139 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 37a2934a-7a6e-313d-a936-967178615689 | -11.24422 | -53.99014 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb66fcf6-e368-3f93-aaba-bbf31b31a76f | -8.95645 | -62.41516 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f78f6b9a-5f0e-3428-8614-ca7d5cd9e4cd | -6.12199 | -57.68522 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 864b0f9f-0d3d-3645-af0e-97a9e0d4efd0 | -5.89075 | -57.75208 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6411141-6a95-35db-870f-154c799327e0 | -11.22697 | -54.00733 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7211e57f-788b-313c-a697-06327feb228b | -5.76594 | -51.68507 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2b24366-08fe-35fe-9b42-334b3cbed9be | -6.8474 | -58.97476 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24b181d1-4f8e-31bc-b112-410351feca24 | -6.79072 | -55.6475 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c8a46ca-368d-317c-a5dc-ec49aee377ba | -6.88678 | -59.0482 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9be1b401-8070-3bfb-aeb4-e9be2515e870 | -6.63344 | -53.18305 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 208819ae-fd36-383c-a06a-202b7ce15279 | -11.18682 | -55.10333 | 2026-08-30 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README51.md)
