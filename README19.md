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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cee9208e-94b7-34ac-8781-eeecd250f64c | -12.4669 | -45.5155 | 2025-10-05 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 6ea2ba93-400e-38a1-bbb5-34bf8eeb1bca | -16.3884 | -52.1612 | 2025-10-05 03:00:00 | GOES-19 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 18748082-6ecb-34e0-9e26-db9bf12300e0 | -10.6378 | -46.3396 | 2025-10-05 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 5c4d18f5-6067-30e0-a928-d3290e3eda3e | -10.6568 | -46.3372 | 2025-10-05 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 0037aeaa-57ed-39fd-99c3-ef6fa24e8eab | -3.6196 | -51.0461 | 2025-10-05 03:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 9888a3b7-125b-333a-ac1b-7e151fc9d781 | -11.823 | -45.0596 | 2025-10-05 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 0268e022-b423-3c01-a0e9-56547f285aab | -8.595 | -46.3246 | 2025-10-05 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 3da71abe-cdd2-302f-9297-76f1ee46e80e | -8.5953 | -46.3022 | 2025-10-05 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 200.6 |
| cbb6dc1b-c9e8-3a05-921a-97a740ad2025 | -4.4445 | -43.2397 | 2025-10-05 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 4030e274-81b6-3874-8483-fca935f1a2bb | -11.8777 | -56.8769 | 2025-10-05 03:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| f1f4e662-fb12-37bb-af28-1b4ba2bfee21 | -4.6505 | -43.1805 | 2025-10-05 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| fb9e08a9-7b71-3291-803c-d652bbca021b | -4.6318 | -43.1816 | 2025-10-05 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 2b1d1c34-431d-3809-a8ba-5c0cec03e065 | -8.5956 | -46.2798 | 2025-10-05 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c5569c62-4452-3f9c-9a2e-2b136e212352 | -13.2741 | -47.6158 | 2025-10-05 03:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| c467a02e-963a-3344-b950-cbc13143f04d | -11.8418 | -45.0799 | 2025-10-05 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 186.9 |
| d3ed284c-973d-39bc-8c0c-bd7b38d9fcb3 | -8.5761 | -46.3266 | 2025-10-05 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 208.5 |
| 026610c1-1f5a-3a09-970c-a099eec29453 | -11.8225 | -45.0827 | 2025-10-05 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| f73d6964-2f27-3644-a2b3-fca7a1bdf4ae | -14.3353 | -47.6755 | 2025-10-05 03:00:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 5e3fad61-de48-3712-9fc2-9fc548af99a6 | -8.5581 | -46.2611 | 2025-10-05 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 8a46eeb2-1b01-3bc8-9661-7e97119597e3 | -7.29269 | -39.26713 | 2025-10-05 03:04:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 9a5b4ac6-9417-3f57-8b09-ec33598c0f8e | -5.09328 | -37.60417 | 2025-10-05 03:04:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1f75fe18-bbe1-39ab-b1ed-d7db2018d62f | -6.9215 | -37.44207 | 2025-10-05 03:04:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2d9ebb11-154e-38d3-82a8-d398ea25659c | -7.52318 | -37.98977 | 2025-10-05 03:04:00 | NOAA-21 | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 16a9e076-4c93-3c3e-b832-ab0e14586d44 | -5.09231 | -37.60958 | 2025-10-05 03:04:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a6aa040c-a92a-328e-938c-23e069e4aa96 | -7.29205 | -39.26933 | 2025-10-05 03:04:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d282a42c-fc47-3d68-be5d-e5d43b34394a | -7.52217 | -37.99522 | 2025-10-05 03:04:00 | NOAA-21 | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 128b46f1-3669-3723-8a36-cd86145507e1 | -13.5308 | -47.2851 | 2025-10-05 03:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| b411ba4e-6a90-352e-be21-40fca4aa2369 | -8.5953 | -46.3022 | 2025-10-05 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 214.0 |
| e1a6057b-f3fd-3d1d-9988-4ef17d065ee9 | -11.8777 | -56.8769 | 2025-10-05 03:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| d9c1d11c-254d-366f-bfc8-f098b975c70c | -14.3353 | -47.6755 | 2025-10-05 03:10:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 4e720650-7a3e-35b2-9274-359f4b8a5ee6 | -5.8891 | -42.9048 | 2025-10-05 03:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| b178f6f2-8aab-3f04-b27f-9dbe401bb8b8 | -8.5956 | -46.2798 | 2025-10-05 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| eef41e55-645f-360b-a4e2-d384d7d01db5 | -11.8422 | -45.0567 | 2025-10-05 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 78bb0874-85d5-3b51-8b7e-c1e93e43c808 | -12.4669 | -45.5155 | 2025-10-05 03:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 55719098-ddfd-30f8-b58a-d6b410a7563a | -11.8418 | -45.0799 | 2025-10-05 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 150.4 |
| e4e5539a-aa2a-3f85-9ead-5242b8137a9f | -16.3884 | -52.1612 | 2025-10-05 03:10:00 | GOES-19 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 65bff668-4fab-34f5-a5c3-7fa7ca47a5f3 | -6.4134 | -43.0489 | 2025-10-05 03:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 49697d61-0a81-35f2-a119-9bc4464f810c | -11.8225 | -45.0827 | 2025-10-05 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 002a9dea-17a0-3870-a1bf-78cfb51cf066 | -4.6318 | -43.1816 | 2025-10-05 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 27af3e3d-c63e-36f5-996d-50c7f2c58096 | -4.3197 | -48.0908 | 2025-10-05 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 0bccfc61-9c69-3ad6-af7a-31e8fc3b4a4b | -14.6906 | -48.335 | 2025-10-05 03:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 2c23ea40-044d-389e-b482-49f0ad44c04e | -13.1585 | -50.9359 | 2025-10-05 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 899c1ef1-305b-3000-a1ea-384b9cc9b6df | -14.3348 | -47.6981 | 2025-10-05 03:10:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| cd6e8dbd-b321-3427-8bde-387ac3f7acd0 | -4.4445 | -43.2397 | 2025-10-05 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 28be6bda-4221-3671-9dc3-a8e9331b92b3 | -14.6707 | -48.3605 | 2025-10-05 03:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 248347bc-be1a-36ca-997b-6bb23a1143fa | -8.5761 | -46.3266 | 2025-10-05 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 333.6 |
| 40c3bf84-4754-3c19-aea8-f8778c288abb | -8.5573 | -46.3285 | 2025-10-05 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 6b017558-84cc-3a21-bd82-b6bba8bac1e3 | -13.1589 | -50.9144 | 2025-10-05 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| cea5d292-dc67-372e-a6df-f7cff22b7c9d | -18.3345 | -45.8734 | 2025-10-05 03:10:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 81.8 |
| be08335a-96c6-3395-bced-35353c185e00 | -4.6505 | -43.1805 | 2025-10-05 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 3fe25aba-a8f1-3e15-8b85-b609660612e8 | -8.5764 | -46.3041 | 2025-10-05 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 280.3 |
| 84b3c178-fab0-3177-b9c8-2be46720ab57 | -8.595 | -46.3246 | 2025-10-05 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 135.7 |
| e45745b4-6cd9-35b9-8d45-e551a942aa4d | -9.2973 | -46.0026 | 2025-10-05 03:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 642c4d81-7cd7-3820-a99f-36efab294164 | -11.823 | -45.0596 | 2025-10-05 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 3118ebf8-08e4-3974-8b2b-20b86588b598 | -10.6378 | -46.3396 | 2025-10-05 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 82bd6739-ad3a-3cd8-ac89-1063eee066ee | -6.4134 | -43.0489 | 2025-10-05 03:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| cbac95f9-e15f-3038-afbf-d1439379f786 | -16.3884 | -52.1612 | 2025-10-05 03:20:00 | GOES-19 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 7ce056b7-da30-3cd3-a181-e013509d1b12 | -5.8891 | -42.9048 | 2025-10-05 03:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 0bc3d714-852a-3c0d-a68a-6327303b771e | -14.6906 | -48.335 | 2025-10-05 03:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 4dd31703-eb0e-3309-8ae0-d19336be0950 | -4.4445 | -43.2397 | 2025-10-05 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| dc283616-7d42-3043-8a14-d44c224ce12c | -5.795 | -42.9358 | 2025-10-05 03:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| 07f0d984-a094-370d-be7d-aa303beba345 | -6.4131 | -43.0724 | 2025-10-05 03:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 8a0e4156-c321-321a-a654-7b12e2ad5c0e | -13.1589 | -50.9144 | 2025-10-05 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 9094d17b-37df-3381-8996-35aa05fafa8d | -11.8777 | -56.8769 | 2025-10-05 03:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c6b9f5a9-231c-3bc4-a07a-fe09869fc3a6 | -10.6568 | -46.3372 | 2025-10-05 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 25c81649-b0f9-3ed8-bdb2-d4cef63931ae | -5.7764 | -42.9137 | 2025-10-05 03:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 115.7 |
| 57f382fa-add5-3a29-8951-93b4e61ab3aa | -4.6505 | -43.1805 | 2025-10-05 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e0e39ce0-7514-3fc7-b522-618b54239364 | -12.1271 | -50.9332 | 2025-10-05 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 7a993705-f5a2-3351-bfbd-09580fe02e74 | -12.1274 | -50.9118 | 2025-10-05 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 7b94e037-cf1d-3b2f-88d9-6124ec2e0ec3 | -8.595 | -46.3246 | 2025-10-05 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 57dabec9-c66f-350c-99dc-a92db2355324 | -5.8374 | -44.4399 | 2025-10-05 03:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 58d6e8f8-455c-3a8b-b268-3cbffb0f69e6 | -14.3348 | -47.6981 | 2025-10-05 03:20:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 0e8f7b36-e910-3eec-a761-e8b056487963 | -10.6378 | -46.3396 | 2025-10-05 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| d673617e-d0d0-3319-a8c0-2fe5991d74c1 | -11.8418 | -45.0799 | 2025-10-05 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| f3ef6be3-4002-3a14-b09d-129f3106d134 | -5.7952 | -42.9123 | 2025-10-05 03:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| e770412d-72c2-306a-82ef-04ad248b9064 | -14.6707 | -48.3605 | 2025-10-05 03:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 4c9a2cd6-a948-33d8-adda-a187d4f0f631 | -14.3353 | -47.6755 | 2025-10-05 03:20:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 4abd9be8-1e8f-3e72-b109-02a79dcdc090 | -18.3345 | -45.8734 | 2025-10-05 03:20:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 86.4 |
| f76f0f1d-66a0-33dc-81eb-06e99a5bd55b | -13.1585 | -50.9359 | 2025-10-05 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 8bb0bf3a-e51a-33f8-ae65-883a86331116 | -4.6318 | -43.1816 | 2025-10-05 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 1a9986ae-b505-338f-8abf-dd291e14edfa | -8.5764 | -46.3041 | 2025-10-05 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.5 |
| bebb6466-fd99-341f-8706-eca7bf898f2a | -12.4669 | -45.5155 | 2025-10-05 03:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 6e193d30-783f-3c1e-bdd6-d0b6bc6e1c01 | -4.6504 | -43.2038 | 2025-10-05 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 06cb2c18-f93c-3598-9c2d-9fd3249c77f4 | -8.5761 | -46.3266 | 2025-10-05 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 152.2 |
| feb81b2e-5e1e-3034-9354-dbcb81ef6fdc | -8.5953 | -46.3022 | 2025-10-05 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 68961a72-47de-3d99-8bba-69f38b08b75c | -5.7762 | -42.9372 | 2025-10-05 03:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 165.5 |
| 2e909a6c-898f-33dc-81fa-b271236fe9a0 | -4.3197 | -48.0908 | 2025-10-05 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 9454392b-e48f-3e76-8279-ead3586354c5 | -18.3338 | -45.8971 | 2025-10-05 03:20:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 88cddbd7-7e5f-3536-a796-6d205bc5b9a1 | -8.5956 | -46.2798 | 2025-10-05 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ec5de164-2e1b-3cbb-801b-8e2771f6c03b | -11.8422 | -45.0567 | 2025-10-05 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b3d04944-3e83-3e58-9cc4-7625e442d250 | -11.8225 | -45.0827 | 2025-10-05 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| cf990722-4601-3c10-a73d-a59ed2332054 | -15.6015 | -52.5102 | 2025-10-05 03:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 995d3745-86ef-39a0-87d2-37a507e1b1ba | -8.5761 | -46.3266 | 2025-10-05 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 9bab1dc2-c815-3b3b-9a25-77224f50ec2a | -4.6318 | -43.1816 | 2025-10-05 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 55b41a55-cc62-3c04-80df-1d30d5c010a4 | -18.3345 | -45.8734 | 2025-10-05 03:30:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 19fa439b-280d-3970-9932-e3657d5a72aa | -11.0126 | -46.6971 | 2025-10-05 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 4e896ba4-51d6-33c4-8491-822493661a0b | -5.795 | -42.9358 | 2025-10-05 03:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 256.5 |
| 3b358148-ba27-355e-bc17-25d1e6025bf4 | -6.1351 | -44.6461 | 2025-10-05 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| fab74803-c77a-3aab-a95a-7ff7ec5f1c9e | -5.8372 | -44.4629 | 2025-10-05 03:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| f277a2fc-957a-3d5c-a5ff-7f9d97c7b0a1 | -14.6707 | -48.3605 | 2025-10-05 03:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |


[Clique aqui para ver as próximas entradas](README20.md)
