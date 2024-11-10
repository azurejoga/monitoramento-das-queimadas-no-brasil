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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4de0f6cc-a0a0-3156-8190-fae096138e06 | -1.5531 | -52.2101 | 2024-11-10 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| d298e213-26c0-3351-b92d-73ea9f5104f8 | -2.7772 | -49.3492 | 2024-11-10 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| dd4cfe16-d61b-38ac-9b13-38834a86cd13 | -2.6388 | -46.7597 | 2024-11-10 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 5f9c5429-994a-3e1c-b5e7-143af9aaf1b3 | -3.2984 | -52.9486 | 2024-11-10 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| eaea3923-4be4-3d17-80b4-7f883926afc9 | -2.7586 | -49.371 | 2024-11-10 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| de4979d3-6bfe-3ca8-a154-1f5a65a91551 | -17.293 | -57.5062 | 2024-11-10 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.9 |
| 00353670-8b4f-3961-80fc-c9e9c62b718a | -3.5818 | -47.3621 | 2024-11-10 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 0250e497-1017-3c96-8cd8-80e634536820 | -3.2353 | -50.2645 | 2024-11-10 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 2415df76-1cb6-39ac-a0b1-6e5c1522c165 | -3.5819 | -47.3403 | 2024-11-10 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 6cafc710-78aa-3ec5-91b1-fab7d6778002 | -1.5346 | -52.2308 | 2024-11-10 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| a24c6330-8be1-3649-83cc-ec3f45001018 | -3.2352 | -50.3065 | 2024-11-10 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 184.0 |
| 5109269a-5641-344b-b923-5a5a3a2720f5 | -2.7587 | -49.3497 | 2024-11-10 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 89abfc4e-7355-332c-aa1b-a1b19e76b44a | -3.2244 | -53.0524 | 2024-11-10 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 226.5 |
| 6a4cb853-74f5-396e-9830-6613060debba | -2.2672 | -47.0556 | 2024-11-10 01:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 62acc8e7-f260-3bd5-944f-f5e3ecefd0c7 | -3.6004 | -47.3395 | 2024-11-10 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 201.1 |
| 2dcddcd9-4307-39e2-b68c-b268bed4ab78 | -2.9355 | -51.482 | 2024-11-10 01:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| aedcc936-fc95-3477-a053-d5024bfcd548 | -17.2933 | -57.4857 | 2024-11-10 01:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 217.9 |
| 5a063929-74dc-30d7-b3b8-52f467ac8584 | -2.931 | -52.7753 | 2024-11-10 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 154.7 |
| 8cd9e438-99ee-392c-b1da-4f3cb4ef7aab | -5.0535 | -44.2654 | 2024-11-10 01:00:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 6b5d7862-7c6a-31c6-90fb-591d8e135eb3 | -3.3117 | -45.6706 | 2024-11-10 01:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| c4fa3fa6-1ffa-3d8e-a3ee-e3f669110069 | -2.7586 | -49.371 | 2024-11-10 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 9dc0bb7c-5754-3e8a-9405-85383eb69b94 | -3.1239 | -50.4358 | 2024-11-10 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ed7165c7-728d-31ce-9676-5b31858c6d95 | -3.5818 | -47.3621 | 2024-11-10 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 153d9d1e-dcd1-31ba-89eb-dc206bf59795 | -17.293 | -57.5062 | 2024-11-10 01:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.4 |
| d1c348ae-dcf0-3d14-8db9-99d87d8856a4 | -2.2095 | -47.733 | 2024-11-10 01:00:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| ddd65e32-9acc-301c-9467-2787cfe30946 | -2.9171 | -51.4825 | 2024-11-10 01:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ebca716f-8488-3f47-a224-a621b9d9f147 | -3.035 | -49.5537 | 2024-11-10 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 3486c5e8-e54e-3aa4-91c4-30f35ccf98c9 | -3.9485 | -48.1508 | 2024-11-10 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 17a4dc78-e736-305d-a251-958fc785e93d | -2.7771 | -49.3704 | 2024-11-10 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 2d8afbd4-64b3-39fd-bd12-5645ea08a6c5 | -3.5819 | -47.3403 | 2024-11-10 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| bdf45cd4-071b-3383-8d37-72883785b940 | -3.2427 | -53.0722 | 2024-11-10 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 8b50d250-e5ef-3b86-aafb-ce1f8d2b5d6b | -2.2076 | -48.3596 | 2024-11-10 01:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ac6a675c-cfd6-3ab1-abf2-6c76f55284f2 | -1.5163 | -52.2106 | 2024-11-10 01:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| ca32bada-912e-3e2f-8a83-fcfb5cf4ecdc | -2.7772 | -49.3492 | 2024-11-10 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 4e174341-30f0-3c4f-9fb9-83dcd0ca6bc1 | -4.1112 | -45.7018 | 2024-11-10 01:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.8 |
| b64898af-d825-3832-a17a-fccd859e24d4 | -3.865 | -49.9477 | 2024-11-10 01:00:00 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| cd0591d5-a6bc-3343-8fbb-5cf88c8cb5f6 | -3.619 | -47.3388 | 2024-11-10 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 9c7ac12d-af8b-381a-a058-ecf062611871 | -3.2244 | -53.0524 | 2024-11-10 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 175.4 |
| 80bb4024-d82e-3c25-81dd-369fb1b6243c | -3.9669 | -48.1716 | 2024-11-10 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 9415f6f0-1531-3288-8af5-a79784b0ff0b | -2.0953 | -48.8338 | 2024-11-10 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| c3371746-1735-360d-9c67-718717a49ca8 | -3.8413 | -44.1283 | 2024-11-10 01:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 1a947740-0bf6-33ba-bfb0-35f6051d5c71 | -3.1095 | -49.4241 | 2024-11-10 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 450d2ca7-7a4a-3ed4-9eb0-464552b13fcd | -4.6736 | -45.1541 | 2024-11-10 01:00:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 163.5 |
| d0e285de-08b8-3c32-964d-77cb2ea2d0b3 | -3.9483 | -48.1724 | 2024-11-10 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| 4d726fa3-4191-37c6-86e1-8792110008c9 | -3.1238 | -50.4568 | 2024-11-10 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| df0b9b57-0816-3d75-890a-a1daba23ac4c | -3.4383 | -50.2999 | 2024-11-10 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 99778d8a-6681-3a79-9328-9d6555243884 | -3.2428 | -53.0519 | 2024-11-10 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| f0535bc2-7885-3ca6-98db-bc0e803558f7 | -2.8802 | -51.4835 | 2024-11-10 01:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 478324de-9386-399f-8362-e708d897d97a | -2.318 | -48.5288 | 2024-11-10 01:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| bef1153d-f54f-351f-8c04-4364838dbfe5 | -10.0428 | -36.4554 | 2024-11-10 01:00:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 103.8 |
| b3d29833-9f12-3e81-9935-f3fe9e676341 | -3.3097 | -50.136 | 2024-11-10 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| b2960072-6631-3c7f-b5a9-dd9d1a40a39b | -2.2487 | -47.0561 | 2024-11-10 01:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 91e2fb2c-eb2e-35ad-a0d4-b3ba23b3332d | -3.1096 | -49.4029 | 2024-11-10 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 040a0c63-4d4a-3c3b-b238-0c18bd807660 | -3.2984 | -52.9486 | 2024-11-10 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| cbf9570c-9a6d-3a03-bac5-704abcc9ae6c | -4.6924 | -45.1304 | 2024-11-10 01:00:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 39f64723-9db1-33ca-acdb-594c9f6394e1 | -3.2932 | -45.6713 | 2024-11-10 01:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| bca0f825-ae56-357f-b724-c8479f47af65 | -1.5347 | -52.2104 | 2024-11-10 01:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 365.0 |
| 899b9159-3160-380d-8b90-f5f5601676e2 | -2.9249 | -49.3661 | 2024-11-10 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| da731900-182e-3383-9af7-8b9589601ec4 | -2.803 | -52.5337 | 2024-11-10 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| c3717466-96b7-3bbb-9ad6-d3438253a766 | -2.6203 | -46.7602 | 2024-11-10 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 8643ad8f-18d5-3bdc-9226-7a2b76438855 | -4.6737 | -45.1314 | 2024-11-10 01:00:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ea387e31-fcbb-3107-8e1d-d020ed82f6cc | -3.1423 | -50.4352 | 2024-11-10 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ae884f24-10da-3ad9-b2f7-1ca9b2be0dd7 | -3.967 | -48.15 | 2024-11-10 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| c287edf5-dcd0-3f8c-b7d5-cf73100f84f5 | -1.5346 | -52.2308 | 2024-11-10 01:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 4a9d4778-dd37-3dc8-bfe7-8afe8be6cb47 | -2.8803 | -51.4628 | 2024-11-10 01:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| f62ff94b-48b8-3af7-aaa5-593768c76b2f | -3.1091 | -45.2968 | 2024-11-10 01:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 4a8c4c55-99bd-32bf-84e1-31c8ebec2e7c | -4.6922 | -45.153 | 2024-11-10 01:00:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| c035f1fb-53b5-317f-a370-9ec5a94dbf5a | -4.8657 | -46.9718 | 2024-11-10 01:00:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e115c368-06c5-3add-9a2e-d98a8d89532a | -3.2243 | -53.0727 | 2024-11-10 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 4ca497e3-c3d4-315e-9621-512583eacf8f | -3.1422 | -50.4562 | 2024-11-10 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| d977dfe1-26f2-399d-8145-cc5997735051 | -1.5163 | -52.1901 | 2024-11-10 01:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 87c4e211-891a-3d80-acd3-7ddd9538f3a5 | -2.0954 | -48.8125 | 2024-11-10 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 00004e41-bb0a-3adc-a3aa-68c5f30198c5 | -1.5347 | -52.1899 | 2024-11-10 01:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 541d89b4-f57d-3e91-84e8-0b20a3152092 | -2.9494 | -52.7748 | 2024-11-10 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 6b78baad-db91-3ddd-a7f9-890cac8940e4 | 2.8552 | -60.0853 | 2024-11-10 01:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 1d7eeef3-a677-3c26-a1e4-7d0d183d9bac | -4.2083 | -48.1176 | 2024-11-10 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| ae3af6c7-ad87-39d6-8520-25d6a3e69976 | -8.3778 | -44.1386 | 2024-11-10 01:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 26bfb0c7-5130-399c-954f-4243d69f5ade | -3.9486 | -48.1291 | 2024-11-10 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a9c7f9b9-4b7b-38a3-a6be-3114ab5a53ba | -3.5249 | -44.0516 | 2024-11-10 01:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 7bb76910-e57c-3cca-892d-ac680c74ead9 | -2.8337 | -49.0496 | 2024-11-10 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| f8b44c1c-90f1-3086-8715-c104477968e3 | -2.2671 | -47.0775 | 2024-11-10 01:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 0ea605b7-1be2-3c81-976a-305d1edc89d1 | -3.5064 | -44.0294 | 2024-11-10 01:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 0b596cbb-c698-3893-bbb4-f65d497e1a03 | -8.3967 | -44.1365 | 2024-11-10 01:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| f860fa82-141f-3f76-81c8-69a59bd74258 | -3.9668 | -48.1932 | 2024-11-10 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| e67723bf-1506-3dca-bd43-af96ef56a17d | -3.525 | -44.0286 | 2024-11-10 01:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| a5e8abbe-a03b-3b98-9705-1b883e12f028 | -2.931 | -52.7549 | 2024-11-10 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 24964b66-621b-3fcc-b441-5532b62a39c4 | -3.6003 | -47.3614 | 2024-11-10 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| f6a445d1-fe32-38a6-b806-a5a3b2797c3e | -2.7587 | -49.3497 | 2024-11-10 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 1add1523-e6bb-3225-94ec-597067e0cc8f | -3.11 | -50.42 | 2024-11-10 01:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa620511-ef01-3fe2-b89d-2c2bc0b6ea96 | -17.63 | -57.54 | 2024-11-10 01:00:00 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9b415528-f2cd-34d9-9c53-5be40e7f64e4 | -3.23 | -50.32 | 2024-11-10 01:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3023c31-ada2-3e0d-8c97-51c262e8f75b | -3.23 | -50.26 | 2024-11-10 01:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c37e7ba6-b0c5-3333-a3d5-4d9f80666fbb | -17.59 | -57.51 | 2024-11-10 01:00:00 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6405e85a-c3da-330d-b925-facdd840c886 | -3.58 | -47.35 | 2024-11-10 01:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb20035a-07e5-3bf4-bb62-e426cbd92709 | -3.967 | -48.15 | 2024-11-10 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 79d9ff96-e787-33dd-b1a9-33ba09004e16 | -4.8471 | -46.9728 | 2024-11-10 01:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 4b33fca7-2c79-340a-a95a-61ec5501cfc8 | -3.9668 | -48.1932 | 2024-11-10 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 3c6dc6db-04ac-3e80-90b5-9bf732dd95ed | -3.9669 | -48.1716 | 2024-11-10 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 194.0 |
| 78791a6e-979a-34ef-bb78-4d5dcf9caed2 | -3.9483 | -48.1724 | 2024-11-10 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| c423d657-6855-327f-9749-76a7a0d59a42 | 2.8552 | -60.0853 | 2024-11-10 01:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 32.8 |


[Clique aqui para ver as próximas entradas](README7.md)
