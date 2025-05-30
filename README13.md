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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2edf6adf-1374-3a75-8fa9-ba0688cfd8c6 | -9.61556 | -67.29245 | 2025-05-30 05:36:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac657a00-61dd-3ae9-a3fb-68843df110be | -9.65204 | -67.24862 | 2025-05-30 05:36:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fee5562-1939-39c0-bde0-dbbba4cecb24 | -9.65338 | -67.24053 | 2025-05-30 05:36:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce2924e0-ca24-3bc9-91be-f1c90dbd1ec8 | -11.65651 | -55.35846 | 2025-05-30 05:36:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d234fcb8-05e2-327e-9b6f-f77e179bbe1d | -10.68085 | -56.16242 | 2025-05-30 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91d44faa-363b-3de2-b928-d458ca77c3b7 | -11.92339 | -54.81858 | 2025-05-30 05:36:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39005610-5e3e-31b9-85b9-4cd032120496 | -11.65773 | -55.35826 | 2025-05-30 05:36:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73d5f8be-6351-3f04-ba4d-56a15fbb92e4 | -11.66196 | -55.35912 | 2025-05-30 05:36:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bce88328-6872-37cb-8eb7-0f745acdcb05 | -11.92025 | -54.82326 | 2025-05-30 05:36:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc725bce-52d7-3e17-bb74-91901109b509 | -11.92072 | -54.81943 | 2025-05-30 05:36:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f0e0574-5249-32b0-afd9-bb393bcf30fa | -11.90139 | -54.78947 | 2025-05-30 05:36:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfb62dc4-19cb-3b41-98ce-d2e4c2072a47 | -11.92639 | -54.82015 | 2025-05-30 05:36:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1ef358e-9cfe-3404-8c32-41119265f112 | -11.92294 | -54.82242 | 2025-05-30 05:36:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ab35385-bd5a-3404-a910-fef9ebbf62ad | -11.65605 | -55.36198 | 2025-05-30 05:36:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7d754199-b2fd-3427-971e-8c838d01ecd5 | -11.90755 | -54.78624 | 2025-05-30 05:36:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34398caa-ee6b-3ca4-893f-151ceb5a89d7 | -11.91977 | -54.82705 | 2025-05-30 05:36:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af9d70db-015a-3d3f-b504-0bf33ab979e7 | -11.90659 | -54.79404 | 2025-05-30 05:36:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a55cba65-22f1-3360-8fee-811cd6952729 | -11.65731 | -55.36179 | 2025-05-30 05:36:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dceab8aa-de7b-3eb7-ab44-e995d6c6e5b7 | -9.6485 | -67.248 | 2025-05-30 05:36:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d74ea94-4c54-32ed-83e9-c49a33036546 | -10.29838 | -59.09619 | 2025-05-30 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 625abb24-a2ad-3a82-8fe6-00e284d2e126 | -11.91364 | -54.83012 | 2025-05-30 05:36:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbeda467-52f4-3b45-ac44-d69a5d08a583 | -11.90707 | -54.79016 | 2025-05-30 05:36:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad54986f-d86a-31e1-a41e-d95a68292bd5 | -11.66319 | -55.35895 | 2025-05-30 05:36:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e423296-dec0-3e9b-a7ba-eec61565d848 | -22.08001 | -56.85031 | 2025-05-30 05:38:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6a820dd-5e20-3417-bd61-61c9badb6ae0 | -9.61915 | -67.29053 | 2025-05-30 06:27:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81acbac1-1ae3-3ad5-a7a4-1430df3c1765 | -6.9804 | -42.7854 | 2025-05-30 11:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 124.1 |
| 0b5f917b-1ffb-34e4-95aa-bc6fdfb47356 | -6.9804 | -42.7854 | 2025-05-30 11:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |
| 134fc6d3-db02-3136-bc39-0bd63bcb5144 | -6.3536 | -43.3816 | 2025-05-30 11:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 77b991d1-6e23-39ef-a613-3a7f4178254e | -6.9804 | -42.7854 | 2025-05-30 11:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 8e136be8-977c-3927-9370-e176542505e2 | -6.3536 | -43.3816 | 2025-05-30 11:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| cde22cbf-6331-3083-af6c-3475033ae3ee | -6.9804 | -42.7854 | 2025-05-30 11:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |
| ed49eee6-3f33-3852-95af-e8c1fa6804c7 | -6.9804 | -42.7854 | 2025-05-30 11:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| dd5fb3b4-d594-3716-8ace-b18ab118bc3b | -6.3536 | -43.3816 | 2025-05-30 11:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 44a81cbe-f9a9-37a1-bf7c-b59365663677 | -6.3348 | -43.3832 | 2025-05-30 11:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 171.8 |
| e479313b-6621-3aef-a96e-074c36a06bf3 | -13.0874 | -45.2791 | 2025-05-30 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 1edd3de3-b507-33da-b613-f7e21752fc7f | -6.9804 | -42.7854 | 2025-05-30 11:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 517b8eb0-3b3b-3253-ad00-8b23ad78bc7f | -7.983 | -50.699 | 2025-05-30 11:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| a9d83711-42ee-3061-a0be-2c58e34e469c | -13.087 | -45.3023 | 2025-05-30 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| b8cda20f-d40b-3bfa-880b-391225ec0ced | -13.1068 | -45.276 | 2025-05-30 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 4da2366f-53e8-3298-a502-971c8199fc90 | -6.3536 | -43.3816 | 2025-05-30 11:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| f5e1bf29-bc1e-3c6b-b7c2-ff5e2e0d0d4d | -13.0874 | -45.2791 | 2025-05-30 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 207.9 |
| ae47ce87-adb2-3f04-b180-07ed3333f7e2 | -6.3348 | -43.3832 | 2025-05-30 11:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 1ab8dc32-5aa2-3af6-9cdd-112bb3c5b298 | -13.087 | -45.3023 | 2025-05-30 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 33210ab0-20ec-3c87-9bba-5296dca7d5e6 | -6.3536 | -43.3816 | 2025-05-30 12:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 3ab7485b-b376-3cae-9271-49198dc03232 | -13.1068 | -45.276 | 2025-05-30 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 171.5 |
| e4f1d095-8b9c-3994-bdb9-a28edd863a3f | -13.0874 | -45.2791 | 2025-05-30 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 223.7 |
| 49e1bf1a-104f-32be-b545-c341c61de557 | -6.3348 | -43.3832 | 2025-05-30 12:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 6c40fdb6-23e9-3bbb-ba5a-bdc1f7cb2c2d | -6.9804 | -42.7854 | 2025-05-30 12:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 150.0 |
| b87406a6-5c73-39a4-9953-cf0fc6fa3ae3 | -6.3348 | -43.3832 | 2025-05-30 12:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 174.9 |
| b48d26b1-e41c-3902-a2c8-2c97815e39a2 | -7.983 | -50.699 | 2025-05-30 12:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 0f01c5f9-ad42-3758-8192-99f4be4e12e0 | -13.087 | -45.3023 | 2025-05-30 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| e92ff9d7-1288-38c3-a671-cb9e374d7230 | -13.0874 | -45.2791 | 2025-05-30 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| df69e62b-2213-381f-a8ae-e0dae78ef987 | -6.3536 | -43.3816 | 2025-05-30 12:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 4a7aa751-0c7f-3775-9870-18f12c3e10de | -6.9804 | -42.7854 | 2025-05-30 12:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 176.7 |
| 6d580d56-9340-3581-b9dc-045e92fe1785 | -6.9804 | -42.7854 | 2025-05-30 12:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 241.0 |
| d9a07dc5-547e-38ea-b103-791cd09ac528 | -6.3348 | -43.3832 | 2025-05-30 12:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 5c7c46db-4ca5-381b-9575-c7b9aab8f7f8 | -6.3536 | -43.3816 | 2025-05-30 12:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| d5caaab7-ec37-3ae2-a424-b1da1b186dfc | -7.983 | -50.699 | 2025-05-30 12:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 29bf8c7b-a593-314d-bbe2-a36506c61c1d | -8.10642 | -45.31683 | 2025-05-30 12:21:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 42db8968-a185-3182-8d1f-0760593d36f3 | -5.05489 | -43.24682 | 2025-05-30 12:21:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 85092dd8-0c79-39dd-bccd-e367d60960c8 | -8.78495 | -44.94572 | 2025-05-30 12:21:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 78c8129b-aed6-30a4-afd4-2c7fb4cb12e3 | -6.98405 | -42.77694 | 2025-05-30 12:21:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 187.2 |
| 5c70f274-cdad-342e-94de-810b78b0c446 | -8.41091 | -47.10265 | 2025-05-30 12:21:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9ce734f6-89a3-3191-b749-9cd87a8127b1 | -6.32191 | -44.18143 | 2025-05-30 12:21:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5dc6d0d7-4e44-3c84-a376-471443ab99d6 | -6.95128 | -43.01946 | 2025-05-30 12:21:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| ab193ac4-c4e8-3def-949e-4121b8bf05b4 | -7.23193 | -43.2725 | 2025-05-30 12:21:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 935a364a-1462-3f37-9746-8f13126937d7 | -5.04899 | -46.87857 | 2025-05-30 12:21:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 286629e5-f46a-38da-867f-b72d830ecd98 | -6.33906 | -43.39119 | 2025-05-30 12:21:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| cae61cda-480a-3755-be21-f3c651e3ee64 | -6.27272 | -44.20665 | 2025-05-30 12:21:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 438e3c57-7c5d-3bea-85e5-00dfb641d3f6 | -7.95525 | -46.17049 | 2025-05-30 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4e3d7b4c-01f7-38f0-a186-add35fafdfd0 | -8.0764 | -43.88974 | 2025-05-30 12:21:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 41242a8c-4ffd-378a-86ba-ac0c01ebd6a0 | -5.21038 | -43.17802 | 2025-05-30 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8568ee62-e88f-3527-bb99-2fd7e8bb11d4 | -5.1737 | -43.2346 | 2025-05-30 12:21:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2da447b6-b7e6-3c29-b294-c9c0f83220d6 | -6.30773 | -37.71729 | 2025-05-30 12:21:00 | TERRA_M-T | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 7c186c15-1a88-340b-9318-17062310debf | -8.09751 | -45.31564 | 2025-05-30 12:21:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a96b5240-43e6-3c43-94ca-8f83045f0931 | -8.546 | -46.42496 | 2025-05-30 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8e910b01-838d-328d-85e7-ff2cd3cb4f0e | -7.7924 | -46.22247 | 2025-05-30 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 7c65aae8-3ee4-38a9-a469-ddb24df2ff30 | -5.21227 | -43.30114 | 2025-05-30 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7571f9d1-8755-3079-b1cf-bf960153e0b1 | -8.10769 | -45.30786 | 2025-05-30 12:21:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 90d5e722-535e-3714-aee8-cdfc6172f31b | -6.34045 | -43.38101 | 2025-05-30 12:21:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 3e86cd7a-ff41-32c1-a8a6-2e3a01855219 | -7.62048 | -45.74567 | 2025-05-30 12:21:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| dd4ed5d8-c6b4-33f7-b394-0223712726db | -7.57612 | -45.86598 | 2025-05-30 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 95c69f6d-8838-39d2-8fec-61f56f19931b | -5.77043 | -45.91091 | 2025-05-30 12:21:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7864c410-d1e8-3ef1-acc7-de329fad50ab | -7.3444 | -43.72005 | 2025-05-30 12:21:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5d5f9c7e-be0f-3b7e-9626-b850622e0a0a | -7.0892 | -46.04582 | 2025-05-30 12:21:00 | TERRA_M-T | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5a053a2e-7dfe-39a2-86c6-9b3cacc2ecc9 | -7.58497 | -45.86723 | 2025-05-30 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 44bb751c-2ec5-35ae-977c-cafe7f93f03b | -8.51292 | -50.01215 | 2025-05-30 12:21:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b7e01f55-4724-3f84-bd74-9cd9ce87ce6b | -8.1157 | -45.89817 | 2025-05-30 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 164a83e0-867f-3cca-a54b-07219f89aa7e | -8.7836 | -44.95517 | 2025-05-30 12:21:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| bc33ae6a-c407-3b28-adde-5b6faa078a3d | -6.33085 | -46.18732 | 2025-05-30 12:21:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d95ac659-e4f6-364c-a80a-c4d9433efea9 | -7.96409 | -46.17174 | 2025-05-30 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f34aa280-96d9-31ba-bb66-6aba0bebed93 | -5.49594 | -43.31741 | 2025-05-30 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5bb48f05-799c-32e8-9986-9d7cf1413f45 | -8.0778 | -43.87968 | 2025-05-30 12:21:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| ac302be4-1f9d-3a4f-b92e-6343c95f215b | -5.49736 | -43.30738 | 2025-05-30 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b4e029f5-d819-3e97-8125-c6c6dc0b44fa | -6.98253 | -42.78822 | 2025-05-30 12:21:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 245.0 |
| 02351b48-4b8d-3ca9-9cc9-4e880b2085f9 | -7.18202 | -43.35138 | 2025-05-30 12:21:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 7f24e30b-6d46-3166-a86e-aa9bfff52a9e | -6.27405 | -44.19728 | 2025-05-30 12:21:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 1c10445e-123e-38bc-a702-ece1c7d79eeb | -6.14187 | -42.57935 | 2025-05-30 12:21:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 1c1e6032-6754-30ea-9c79-b4ab3cc23865 | -8.09878 | -45.30665 | 2025-05-30 12:21:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 7fdf4d77-98f9-3da9-a78b-dfd59192798c | -5.97715 | -42.44107 | 2025-05-30 12:21:00 | TERRA_M-T | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |


[Clique aqui para ver as próximas entradas](README14.md)
