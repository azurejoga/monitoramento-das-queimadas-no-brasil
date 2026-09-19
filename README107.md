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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81b54c1f-37c7-3115-b3bd-53756becb2a5 | -5.6596 | -43.3906 | 2026-09-19 13:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 1bffd4b1-aa0b-3f9b-a992-26579f58b93e | -9.2567 | -46.2098 | 2026-09-19 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 258.8 |
| d06a9e93-5592-301c-89a5-64839fd2535d | -8.7731 | -48.6868 | 2026-09-19 13:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 127.3 |
| f93a1980-70b6-3c1f-93dd-01e954b72f1f | -9.2414 | -45.9411 | 2026-09-19 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 534165c3-dc45-3d9c-9095-fe5809419e6c | -3.331 | -59.8292 | 2026-09-19 13:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 18eb98e6-e5de-30b1-ab11-38dbea6b9c8d | -7.8598 | -44.8595 | 2026-09-19 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 123.9 |
| db972007-d373-3ccf-8d16-ea691709f91b | -12.1535 | -46.9482 | 2026-09-19 13:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 151.4 |
| cc276e03-4be3-31b1-a0d0-1a5fb8abf280 | -12.1339 | -46.9734 | 2026-09-19 13:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 8f914fd6-f99f-3ced-8c63-e8aceab47349 | -7.7656 | -44.8688 | 2026-09-19 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 59f5420b-8d58-3315-a3a7-ca8f5a3bb490 | -5.9344 | -42.0966 | 2026-09-19 13:00:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 36c2e499-d12b-30d1-8536-11672be2c9fc | -6.4667 | -45.2116 | 2026-09-19 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d5f0dff6-f731-3a2c-bebd-252e5d3db796 | -10.8279 | -50.1815 | 2026-09-19 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 7e8ab9c0-6586-3e92-9b8d-0b4897006d96 | -11.0611 | -49.7693 | 2026-09-19 13:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 45d6dbe6-758a-321d-b054-e36ab456b6da | -10.6703 | -50.6465 | 2026-09-19 13:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 47015ec4-b2dd-3478-abf4-d53be8349773 | -10.8282 | -50.1601 | 2026-09-19 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 4827fc9b-1a65-3e98-9b6a-618847195d6f | -12.6892 | -45.9629 | 2026-09-19 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 419f259f-ef95-3480-90e8-9d535e68aa7f | -12.0076 | -50.0254 | 2026-09-19 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 1eb3be7d-733c-3a62-b5ae-3427719ebbe2 | -11.0062 | -48.3407 | 2026-09-19 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 5331160b-565f-3f73-ab1f-712252c1864d | -10.8466 | -50.2009 | 2026-09-19 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 39d7c31b-1b44-30a9-a2da-af8c636d0711 | -9.0355 | -48.7487 | 2026-09-19 13:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 00dea83b-4fa6-37ed-9e90-d6ef9d374d89 | -12.5032 | -50.0508 | 2026-09-19 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 175.4 |
| d9e8d836-6801-3290-86d9-bfcf952fae60 | -12.5952 | -49.1046 | 2026-09-19 13:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 0bcb6ca4-a3c2-30f0-964d-f17e8d9e5838 | -11.7823 | -49.8152 | 2026-09-19 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 142b818d-a080-378d-86eb-c1725fdc0ee1 | -10.5368 | -46.7343 | 2026-09-19 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| e536483b-ee3f-30f3-a5eb-ab16c4790d56 | -11.0608 | -49.7909 | 2026-09-19 13:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| bd625429-ddf1-305f-8461-2beae3dae7f9 | -8.6628 | -45.4379 | 2026-09-19 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 87d7e45e-30d0-36b4-8dcd-96c287d47438 | -11.3604 | -44.1521 | 2026-09-19 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 81f66bfd-34d3-31a2-babc-7c3b487f1ef2 | -9.0096 | -44.9209 | 2026-09-19 13:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 18ff151e-92bf-3690-b942-12eb8c491e64 | -3.4455 | -58.2134 | 2026-09-19 13:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 6262e75a-902f-334d-b275-4fc49d8bf658 | -10.5364 | -46.7568 | 2026-09-19 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 9aa9ca98-3cc1-33da-8509-31436754dd4e | -5.6408 | -43.392 | 2026-09-19 13:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 1d39f43a-77a5-3603-b4ee-00f14debd859 | -11.9112 | -50.1016 | 2026-09-19 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| e7fe45e7-8ac1-35ea-ad33-b7b95601c41f | -8.7919 | -48.6851 | 2026-09-19 13:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 199.8 |
| 457a1a90-649b-3409-94ed-c7ab8f59b466 | -9.0358 | -48.727 | 2026-09-19 13:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 120.2 |
| db46a4a9-8976-3f30-8037-25e64d4ef7cb | -11.3177 | -51.7429 | 2026-09-19 13:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 393c343f-1c9f-3320-bb68-6088d17128ad | -3.3493 | -59.8288 | 2026-09-19 13:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| d2a23b7e-dbda-3f80-b3fb-38bf86a098a2 | -14.667 | -46.6461 | 2026-09-19 13:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 133bbc6e-d5e3-350d-bb28-8fb42656517f | -10.567 | -51.3137 | 2026-09-19 13:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 2270e2ef-73e4-3c16-beff-5015286e326e | -11.1369 | -54.0251 | 2026-09-19 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 216.9 |
| 834ac29d-0290-3adb-b52a-97ee1d029adf | -11.949 | -50.1186 | 2026-09-19 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 24be33e3-bcff-39d7-9e2e-5d1f35e782e6 | -10.8469 | -50.1795 | 2026-09-19 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 91d2ddd4-819e-3ea6-80c4-6ea97f64ca4a | -11.083 | -48.2875 | 2026-09-19 13:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8fa17791-24da-37db-aee0-908e24f2fb1b | -9.0167 | -48.7505 | 2026-09-19 13:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 53.3 |
| cbe0a416-cc68-329c-8b8f-88bc31f18874 | 1.36509 | -56.07569 | 2026-09-19 13:01:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 7171ae5f-0a06-35d0-ad89-8ca3ed6ff13d | -6.32106 | -62.67562 | 2026-09-19 13:04:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 61b68b8d-c4a1-33b1-b9c3-7c7c3968e85f | -10.72002 | -60.72882 | 2026-09-19 13:04:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 0d5b9a23-722c-3fae-b3ef-a07477ffe28b | -7.92521 | -61.33024 | 2026-09-19 13:04:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 6d569bb5-4bc5-3897-9047-e3db895fdb19 | -3.45371 | -58.21089 | 2026-09-19 13:04:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| c450c31a-7919-31c2-80b0-29c517e32346 | -5.74552 | -57.583 | 2026-09-19 13:04:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 8265cfb6-e146-3f82-9970-854ff2805dca | -3.42665 | -59.19363 | 2026-09-19 13:04:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| f2c4ceac-ee51-363b-9974-b7545276421d | -7.92282 | -61.34942 | 2026-09-19 13:04:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 7068d60f-f19e-36ad-822a-ec65476c89b9 | -6.44222 | -59.98057 | 2026-09-19 13:04:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| e06ecee2-7671-388a-b16a-b9b5f51de102 | -7.37637 | -68.01487 | 2026-09-19 13:04:00 | TERRA_M-T | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ecf2be1d-f5eb-3049-871f-79d54f703452 | -7.92168 | -61.3435 | 2026-09-19 13:04:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 85e482ed-e448-34ad-bd59-3f78c2fcc1ed | -2.89004 | -57.78729 | 2026-09-19 13:04:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| d0a025ed-0087-3366-ae07-1c8901b76260 | -6.1308 | -59.94576 | 2026-09-19 13:04:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| b2d41d25-4d72-34fb-9c78-bcc065d3c1ef | -3.45575 | -58.20461 | 2026-09-19 13:04:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| e9bad1f4-0d54-3295-9e5b-b31decb0a3c7 | -3.56226 | -58.54362 | 2026-09-19 13:04:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| dbfba4a0-f604-3359-9f36-fb47ddea86eb | -2.9055 | -57.78931 | 2026-09-19 13:04:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 164.8 |
| d811c018-8248-3a2b-846c-fbaaa4e8ab8f | -6.15514 | -62.62722 | 2026-09-19 13:04:00 | TERRA_M-T | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5223522d-e0b6-3093-b5b1-9d6377e8c455 | -5.75562 | -57.57716 | 2026-09-19 13:04:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 8d377818-c9ac-35bc-b23a-3dcd1689c7c6 | -2.90156 | -57.7944 | 2026-09-19 13:04:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 196.8 |
| f8245995-8877-35f3-8f65-5e4a73a39258 | -10.70615 | -60.72724 | 2026-09-19 13:04:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 7c2513d9-0720-3907-a5ae-d72656366b44 | -2.89757 | -57.82475 | 2026-09-19 13:04:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| c0186d1f-ab0c-3e6a-b4ec-81637f022a53 | -6.3714 | -58.31041 | 2026-09-19 13:04:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 89b36f2f-94b8-33db-9881-2b5ddc62db71 | -3.45186 | -58.23334 | 2026-09-19 13:04:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 33e0d138-cb0d-3f45-b25b-66701efb91be | -3.43212 | -59.2 | 2026-09-19 13:04:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 62c5553b-5e82-35e8-9e8a-f556976858a5 | -6.44884 | -59.9871 | 2026-09-19 13:04:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| e4b632e9-f38d-3f64-ad81-f21cecff81aa | -7.56104 | -61.31811 | 2026-09-19 13:04:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 5698b5b4-1643-31d4-9718-f8c1f031fac9 | -7.04359 | -59.22348 | 2026-09-19 13:04:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| cc249cef-a056-3418-871f-99e684b00a06 | -6.43513 | -59.98509 | 2026-09-19 13:04:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| b6091e04-d232-3450-8418-19240b8bd025 | -3.14218 | -61.39671 | 2026-09-19 13:04:00 | TERRA_M-T | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0a360a80-b588-3031-8a68-26a5c4cf3e34 | -10.70004 | -60.72115 | 2026-09-19 13:04:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| b6187e78-d207-35d0-be1f-dddf2ec045ba | -7.55707 | -61.33107 | 2026-09-19 13:04:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 6fcea108-c2e8-383f-ba32-14e97cf54b00 | -2.90128 | -57.8196 | 2026-09-19 13:04:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| cfbd125a-43ee-3bf0-acd3-601ac81ae2c0 | -10.71391 | -60.72271 | 2026-09-19 13:04:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 9602d4e8-f99f-3a29-91b2-b11c26fa7dde | -12.1531 | -46.9707 | 2026-09-19 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 787e6c9c-1a95-3839-bec5-2ffd1088182d | -11.8546 | -50.0653 | 2026-09-19 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 6e8b65e3-1ec0-3bc3-8c4f-9d5d043b3937 | -11.2987 | -51.7449 | 2026-09-19 13:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 4b85b5e0-29b4-31ba-aec1-9a63b2092547 | -11.3604 | -44.1521 | 2026-09-19 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 3d075d3f-2666-3d45-b450-b38d3c733141 | -11.083 | -48.2875 | 2026-09-19 13:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| f8d5093d-bfba-352e-a141-b96f5f25cd87 | -11.1228 | -49.4384 | 2026-09-19 13:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 6b2bc065-c59d-3328-ae7b-a3da9b282fea | -3.4455 | -58.2134 | 2026-09-19 13:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 4169c893-bb3e-3765-a893-6ffd599b65b6 | -10.5368 | -46.7343 | 2026-09-19 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| a0474ed3-09bb-3f57-916f-cd9da483d179 | -8.4503 | -45.8448 | 2026-09-19 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| f3e7626a-c78b-3abc-86f4-c8a1934811bd | -6.7776 | -47.8981 | 2026-09-19 13:10:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 4f7651f0-852a-3716-959f-44e374dd574d | -10.5667 | -51.3349 | 2026-09-19 13:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 2c8ed454-ee59-38c5-b74b-6573dba2fae9 | -12.1535 | -46.9482 | 2026-09-19 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 3ed135ce-3f1d-3a8e-a8fd-b0ac3f317484 | -10.5481 | -51.3156 | 2026-09-19 13:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 03851761-8c49-3e39-a4d6-16bba994b3fc | -10.8279 | -50.1815 | 2026-09-19 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 8a9fd191-b593-32ad-8bcd-2ce3414b4f81 | -8.7919 | -48.6851 | 2026-09-19 13:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 162.6 |
| 5cc39f25-9b88-3011-a620-3083d7a37b48 | -9.9706 | -46.5555 | 2026-09-19 13:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 478a14da-2802-3b3e-9608-2e00a439dbb7 | -7.1553 | -47.4971 | 2026-09-19 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 8c6ff66e-1727-3227-af12-bb28fa22040d | -3.3494 | -59.8097 | 2026-09-19 13:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| bd6b1268-6b1c-3b68-acb7-4ab83b94e711 | -11.8549 | -50.0437 | 2026-09-19 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| a7a1a805-346a-3884-a54b-6318d7714abb | -11.1035 | -49.4623 | 2026-09-19 13:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 96fbffe8-d825-3802-a9d8-d5ca5408878a | -12.1336 | -46.9959 | 2026-09-19 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| b9148720-21a8-3b23-b868-46dc56849673 | -6.941 | -55.0366 | 2026-09-19 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| fd2fab9e-d3f9-38b7-82ca-a5fe67181f00 | -10.8466 | -50.2009 | 2026-09-19 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 17835fe7-231b-3480-9abb-fef28bfcf6f2 | -11.318 | -51.7218 | 2026-09-19 13:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |


[Clique aqui para ver as próximas entradas](README108.md)
