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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8295837-3296-3400-a50a-85fd6ce51653 | -19.76723 | -42.08107 | 2026-08-03 04:42:00 | NOAA-20 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9e497a19-d4fa-3939-a2af-d9738a6a6b7d | -19.31466 | -48.92013 | 2026-08-03 04:42:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce739523-2a71-3805-8ecb-eb859016bd5f | -20.87993 | -45.54971 | 2026-08-03 04:42:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 11a053b1-2ab0-3359-9bbc-00dafc3fdf30 | -1.6591 | -54.4543 | 2026-08-03 04:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 4d9b00ac-2c0f-3dfd-b923-3f9e5153a9e1 | -1.6408 | -54.4545 | 2026-08-03 04:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| e0ee9bbd-a694-3570-8767-2294666598f2 | -1.6591 | -54.4543 | 2026-08-03 05:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6943bf20-a8e7-3b0d-a00e-92bb7bddb71b | -1.6408 | -54.4545 | 2026-08-03 05:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| b812817f-049c-30f2-b928-8dd41d2ab965 | -1.6591 | -54.4543 | 2026-08-03 05:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 8c3cabb8-5e49-3ec7-9706-af7cf3f3fef7 | -1.6408 | -54.4545 | 2026-08-03 05:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 5b7a1d6a-f050-3aac-90dd-19a72472f1f6 | -1.6591 | -54.4543 | 2026-08-03 05:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 5c41e977-1d94-39c2-9c99-e6654b545af4 | -1.6408 | -54.4545 | 2026-08-03 05:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| f4ba517c-7915-33a0-9e82-ec49895b55d5 | 4.35533 | -60.80136 | 2026-08-03 05:21:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c37f332e-01ce-3587-9476-975a5eff5954 | 4.35303 | -60.8098 | 2026-08-03 05:21:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 803cf1c5-21bd-3875-8ea9-1c3b821c7cd1 | 4.35243 | -60.80588 | 2026-08-03 05:21:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56a91133-b85a-392b-9cae-1c182a3708a1 | 4.35183 | -60.80196 | 2026-08-03 05:21:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f036b234-5f63-3e58-916e-752cd9f2253c | -3.11265 | -47.9082 | 2026-08-03 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 467f5996-71da-3963-a730-503a1e49d4f4 | -1.65308 | -54.4492 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 639dfe1a-1c5f-396a-8a08-14dc8d14c7d6 | -6.74442 | -60.02226 | 2026-08-03 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68ac781d-4e59-3ed5-b741-4f88d009c2bf | -1.65254 | -54.45272 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5b5f866c-0db6-34e0-ad18-c97490d3b6e7 | -1.65712 | -54.44982 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4579251a-d36a-3a83-89d6-563e9a5e9eda | -2.75575 | -49.46767 | 2026-08-03 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58e9ea3b-3f99-3349-bc24-0d5252338a62 | -1.64094 | -54.44751 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f396e00c-8900-337e-94a4-0671cc10d3dc | -7.24826 | -59.44648 | 2026-08-03 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f8e36ffa-fedb-3d47-b54d-116ea5b51144 | -4.27373 | -48.19452 | 2026-08-03 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f74e5f8-164c-300c-9c86-b078a9e92097 | -3.11309 | -47.91656 | 2026-08-03 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7509bb68-70e4-3de2-bf99-d673d1e0be10 | 2.53566 | -60.35699 | 2026-08-03 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c3dae02-e984-3352-9899-c2770e4b9aa8 | -8.17602 | -49.19718 | 2026-08-03 05:23:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57f1eb59-ba43-3531-a336-fe1d184c4831 | -7.25107 | -59.45057 | 2026-08-03 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e5b73b33-c949-3d4f-bd04-f630bbd207b7 | -8.55062 | -47.7494 | 2026-08-03 05:23:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c6438d2-3eb8-3a71-a135-31a1a1a280da | -7.25218 | -59.4434 | 2026-08-03 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40234b6c-6984-322f-aaa5-dba61ec93cd9 | -1.64688 | -54.4628 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7133bd39-1018-3bce-8fa6-594c25269914 | -1.63531 | -54.45737 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bafbb2d2-042d-3f48-bd98-0ecd91bd359d | -3.52313 | -54.481 | 2026-08-03 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59e71659-99df-3986-9d2c-b4074541c98b | -1.64446 | -54.45155 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4a1806f0-2f0c-34d2-af7b-6eb431e1d055 | -2.81831 | -52.28673 | 2026-08-03 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3122bbc2-fcc0-3c3b-85dc-a6b7da576e16 | -2.06407 | -59.78364 | 2026-08-03 05:23:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11dc5441-49c3-3cb2-aa63-140ebe1cb5fb | -3.09611 | -61.20797 | 2026-08-03 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bba9f10-c157-387c-a570-db8f2499f280 | -4.27593 | -48.19408 | 2026-08-03 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 984a3e74-5b59-3f63-a8b8-f0a1951700ca | -7.32035 | -64.70685 | 2026-08-03 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4d0fcfd9-07cb-3921-b694-17c0049e23d1 | -7.17781 | -59.32174 | 2026-08-03 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7e37b34-ebaf-3243-a9f8-db9b9a1a06dd | -9.41098 | -48.57641 | 2026-08-03 05:23:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 618b8455-fcaa-35d0-9460-dbfbd43cd1a3 | -2.81757 | -52.29179 | 2026-08-03 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7506b47e-8b92-3cef-bc5d-c762d9c9f3dc | -7.48842 | -61.379 | 2026-08-03 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 903729f5-8a1f-32dd-9958-44fc3b50ef81 | -3.11747 | -47.91977 | 2026-08-03 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 41c3ab92-09e3-3cfa-a775-80f06408be39 | 2.53283 | -60.36116 | 2026-08-03 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| cbef98a7-b56b-301f-a162-efaa9cceb817 | -9.08135 | -65.38101 | 2026-08-03 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e7c947e-b347-33cf-b72c-74f3e9042a8e | -5.62385 | -47.10416 | 2026-08-03 05:23:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a8769cee-4da7-336c-bb6c-c57d529e68ed | -2.75396 | -49.4797 | 2026-08-03 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9333c787-a820-3e9a-8783-112b30b7a6cb | -4.26658 | -48.19883 | 2026-08-03 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 428086a6-c2df-3c4a-904c-1b4ebe20d919 | -7.49173 | -61.37952 | 2026-08-03 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 458f2360-2f2f-3393-91c4-0ee64827afba | -3.98138 | -48.43074 | 2026-08-03 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad2a148e-157f-397a-b052-4094d24c5efc | -1.63935 | -54.45798 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4f116976-d185-3e4c-ba18-2b8d3eea495b | -1.66062 | -54.45397 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7fb64b39-39d8-359b-8e4d-3a89927ae84c | -1.64285 | -54.46215 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ef804f58-55d4-3deb-9ae5-218bb856d084 | -10.67702 | -51.37009 | 2026-08-03 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 113134b6-3405-38e1-8ceb-6c6e3769a646 | -3.92712 | -59.39826 | 2026-08-03 05:23:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8290241b-fa56-340f-b330-20f4126f178b | -2.81279 | -52.29118 | 2026-08-03 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20666f7a-ad09-30fb-b73e-78f663773a1c | -7.49119 | -61.38301 | 2026-08-03 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a6f3b32-b010-33cd-8dbe-ef2f3e4212b4 | -3.57954 | -50.26387 | 2026-08-03 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d19e0d63-94a1-32db-bfc9-4e6588518803 | -1.64797 | -54.45566 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d017afc5-3370-3f65-ad7e-a8dc278c8143 | -1.65604 | -54.45689 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7e9267b3-05f6-3876-9146-a941006be5f5 | -6.74389 | -60.02575 | 2026-08-03 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b416cd0b-bbec-3ee5-863d-fbfddbc94f61 | -1.63882 | -54.4615 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cfd97241-a27f-3dec-b8e1-54f36c5340ec | -1.67566 | -54.4637 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0905120-15c2-35a0-8e3c-a5f359a8e750 | -4.26881 | -48.1984 | 2026-08-03 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ce273d6-7d83-3fce-9bf1-00c284a2149e | -1.6485 | -54.45213 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a310c49b-3dd6-3bd0-ab0c-ef66157f4254 | -6.74774 | -60.02277 | 2026-08-03 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8ef2f15d-9722-3e7d-a26a-25d09185094f | -4.26734 | -48.1936 | 2026-08-03 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cfcfb45f-07aa-39af-83a9-eb7c88ada1b2 | -1.67511 | -54.46726 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 468198ac-f01c-3f08-8be1-ae860ce530ea | -3.11237 | -47.92171 | 2026-08-03 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 080ed003-22ed-3ef7-bb3d-95715dad02fe | -1.63988 | -54.45447 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f0318efc-71e9-3f81-aefd-77f0ab47cfcc | -7.24882 | -59.4429 | 2026-08-03 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f30f10a-a222-37a3-a340-4cd089ec0931 | -1.65658 | -54.45334 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1002b5ef-c2ed-3665-98a5-d3c42cd57951 | -7.24771 | -59.45008 | 2026-08-03 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4c72ca0f-4617-3c2a-afb5-b43ea83f27ff | -1.64041 | -54.45099 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c1db2455-051a-3fc6-a8c9-382360543a35 | 2.53623 | -60.36064 | 2026-08-03 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f4e72442-7f40-338e-a06a-0bf8886688ad | -9.18573 | -58.06429 | 2026-08-03 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67356d6b-a177-3b0f-9dd6-a4ab64731abc | -3.11109 | -47.91879 | 2026-08-03 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 356a3181-5961-3787-8836-be5018e590b9 | -2.75515 | -49.47168 | 2026-08-03 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb41225f-6813-385b-a221-866b32262f7b | -7.25162 | -59.44699 | 2026-08-03 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5002cc70-e294-3726-ac12-8678b9b90bd5 | -1.63584 | -54.45387 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95eebc7d-efc2-3c4a-9026-e36f57bb8a76 | -4.26954 | -48.19315 | 2026-08-03 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 068d11d4-89f5-3990-9188-4460b9cbc257 | -1.64499 | -54.44802 | 2026-08-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c4ebe64f-24d0-350f-af91-6bbaee7dd727 | 2.52943 | -60.36168 | 2026-08-03 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50e3f8bd-04ed-3634-8567-fea376714b82 | -3.11383 | -47.9113 | 2026-08-03 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fb66b2ad-8631-34c1-9912-2969274e8578 | -8.18233 | -49.19814 | 2026-08-03 05:23:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea00bf75-7db0-31dc-b503-5bdb30fbe43a | -3.58507 | -50.26478 | 2026-08-03 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4298acfe-a62b-3d8c-84b3-723f8b3daafb | -4.36784 | -47.77222 | 2026-08-03 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19d0e999-c5b7-3c9b-9bc3-796b912222cb | -11.23622 | -54.86377 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf5f03b8-4d13-34ef-94e5-0a0f6fe5a67b | -6.23427 | -55.62883 | 2026-08-03 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| cd8a06e4-11f5-3f1e-a886-49a58b6de39e | -11.91559 | -55.89573 | 2026-08-03 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1dedc82b-ab28-39d6-b755-83facdc32de5 | -5.15059 | -62.53106 | 2026-08-03 05:25:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ea30b7e-e550-3102-b055-410195c0df8c | -11.26367 | -54.84159 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8069c40-e973-3ed4-8563-c624d34cc5a1 | -11.27112 | -54.84461 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09d53651-a806-366b-a55a-e26bf2ab958c | -6.55514 | -55.16645 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73042e8f-bb3a-38b3-bd8b-af22abe42396 | -11.26762 | -54.84678 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8241817f-fe17-360c-a8a8-cd262b2c3512 | -6.55154 | -55.16211 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4146768-ea25-3893-b4ef-12f16e0029d4 | -11.23561 | -54.86834 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2ee02b4-73d3-311d-a9cf-9a8c54df16e8 | -6.54794 | -55.15775 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6e406ce1-0aa2-3f12-9563-f2aae154dea1 | -11.24637 | -54.82249 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README9.md)
