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
| b007fd6a-3200-3596-af4d-4d2bbd03aad2 | 4.4435 | -60.9846 | 2024-12-17 01:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 779be907-3c86-348a-b92f-43fcd0ee7b5c | -3.1503 | -53.1762 | 2024-12-17 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 94974eed-cf01-31dd-9730-3771df25a723 | -3.2506 | -46.8049 | 2024-12-17 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 005da70e-6f3b-3f09-a869-6ace2e654c4c | -3.2968 | -53.3749 | 2024-12-17 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 6e510379-f8e6-3cd7-b738-64e5ab522f82 | -19.1038 | -52.8711 | 2024-12-17 01:40:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 707563cb-2b2b-390e-a5a2-e0429a0dc61e | -15.0865 | -59.6487 | 2024-12-17 01:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| db795df8-af6e-3003-8516-18bc74eabee3 | -6.214 | -46.2202 | 2024-12-17 01:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 19653361-411d-3d53-9608-c62e327b4ff8 | -9.9297 | -59.940102 | 2024-12-17 01:44:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5afde1d3-0a0d-3530-a3f9-c6369af24eba | -9.9273 | -59.9305 | 2024-12-17 01:44:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1d6447a-c335-3c27-92f5-23909d4da5d2 | -15.0828 | -59.648701 | 2024-12-17 01:44:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0bbd2413-f75c-3b22-aa47-13e96cb1cc07 | -18.895599 | -56.049599 | 2024-12-17 01:44:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 01d364cf-f0d4-327f-b673-c6b396a7a9e5 | -15.073 | -59.6511 | 2024-12-17 01:44:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d5a0e21-ce68-3caf-82f8-fcbead3681cc | -18.9021 | -56.0345 | 2024-12-17 01:44:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e45488e3-3f49-36b8-b046-487831457123 | -19.0909 | -52.850101 | 2024-12-17 01:44:00 | METOP-C | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5cc79857-6384-3fa8-a343-b7f743906208 | -21.3349 | -56.113998 | 2024-12-17 01:44:00 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 01676f3f-0c3c-3593-bb89-20bc076d2f91 | -18.9053 | -56.046902 | 2024-12-17 01:44:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| eba36cdb-383d-3d99-87a0-0bb4da9fb685 | -19.0963 | -52.869598 | 2024-12-17 01:44:00 | METOP-C | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 19f62544-bfd9-372d-93f7-6a873dedf49e | -18.908501 | -56.0592 | 2024-12-17 01:44:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 846305ca-ff48-33ae-a2f7-deafdbbbc897 | -15.0807 | -59.639999 | 2024-12-17 01:44:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3293c46c-bc58-3e91-93be-9a9293daba2c | -19.071699 | -52.855999 | 2024-12-17 01:44:00 | METOP-C | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b3138cd7-066c-36f7-ad31-dd51c37e7651 | -19.0662 | -52.8363 | 2024-12-17 01:44:00 | METOP-C | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 58fb37cb-4053-3c18-b254-633cbb77ddbd | -19.1005 | -52.847099 | 2024-12-17 01:44:00 | METOP-C | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 76c72606-7ff5-3db2-8aef-37d120058534 | 4.4385 | -60.964298 | 2024-12-17 01:46:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ca9ebad6-3c58-3ce0-ac45-ff42d01a130c | 4.4415 | -60.950901 | 2024-12-17 01:46:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bff72cce-a4b8-3ec8-8af9-094cde924d05 | 4.4453 | -60.979801 | 2024-12-17 01:46:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5d4dcc05-477e-300b-8462-cc7067e0fddd | 4.4326 | -60.990898 | 2024-12-17 01:46:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ec1a9235-643c-377c-ab76-9f8c784a9239 | 4.4483 | -60.9664 | 2024-12-17 01:46:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 52b18bdc-3e90-3f4a-ab94-fa622215b0da | 4.4356 | -60.9776 | 2024-12-17 01:46:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 23db09f1-06c5-3821-8b4a-f7b0de63565b | -19.1043 | -52.8493 | 2024-12-17 01:50:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 99ea0af3-049d-3c35-96e5-cc86b40f6496 | -3.2968 | -53.3749 | 2024-12-17 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| addae58a-9c2f-349c-94eb-e65d2391b3a8 | -15.0672 | -59.6504 | 2024-12-17 01:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a0d20299-73c2-3456-a1c7-b358b6a779ae | -3.2506 | -46.8049 | 2024-12-17 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 81e0732e-2ed3-33c3-b4e3-78a6c9b617ef | 4.4435 | -60.9846 | 2024-12-17 01:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 62.7 |
| b6475d51-6721-3595-8319-92dca50c127c | -3.232 | -46.8056 | 2024-12-17 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 1079b3b6-debb-3a94-96f1-870ae4eff946 | 4.4435 | -60.9657 | 2024-12-17 01:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e2e00f4a-67fe-3702-b858-7566b65291f3 | -15.0865 | -59.6487 | 2024-12-17 01:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 4d4e45d3-2b48-36e4-842b-cb8646ed9ce2 | -6.214 | -46.2202 | 2024-12-17 01:50:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 7bbf6b05-0359-3c89-97d4-a9920673d1ca | -3.3152 | -53.3744 | 2024-12-17 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 0af53102-cc0b-31ab-9955-4e1ce6537c73 | -6.1953 | -46.2215 | 2024-12-17 01:50:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 0fddb159-e0d3-3021-bef1-569ea54fadce | -19.1038 | -52.8711 | 2024-12-17 01:50:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 77.8 |
| e30af251-9afe-307f-9130-f2133955de0a | -19.1043 | -52.8493 | 2024-12-17 02:00:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 4cc589de-018a-3f68-ba20-f7820e50de34 | -3.2506 | -46.8049 | 2024-12-17 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 2fdfc7a1-a199-3f2d-880e-489f174d4901 | -3.232 | -46.8056 | 2024-12-17 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| a5e7ad6a-7856-30cd-815f-06be78f99e67 | 4.4435 | -60.9657 | 2024-12-17 02:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 6ce6ed95-c5c5-39e5-9612-51300064f46d | -3.2968 | -53.3749 | 2024-12-17 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| f527254f-573e-33fe-8075-11e43dd5f531 | -3.2507 | -46.7829 | 2024-12-17 02:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e6ac6136-d2db-31c4-968f-21d10fc01f41 | -15.0865 | -59.6487 | 2024-12-17 02:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 6a05e62e-8295-3b48-b3d8-cf514758b8d7 | -15.0672 | -59.6504 | 2024-12-17 02:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| cc8e8e51-9773-3647-a66f-61d2fa05b515 | -3.3152 | -53.3744 | 2024-12-17 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 3763d5d4-649d-3dab-aac1-0e6f86fec2de | -19.1038 | -52.8711 | 2024-12-17 02:00:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 4ff1423c-0687-3104-af2b-d497aa6d6cc9 | -6.214 | -46.2202 | 2024-12-17 02:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 60e95654-41d4-3b63-a145-889ac4f5c502 | 4.4435 | -60.9846 | 2024-12-17 02:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b52ed6d0-7170-3463-8cc2-a8f03fc994a2 | -5.11 | -43.96 | 2024-12-17 02:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b47c9f99-3466-3b67-805e-47b256a0d65b | -5.08 | -43.87 | 2024-12-17 02:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f35124b9-f3bc-39d6-9a0e-1beb85f3e5e6 | -5.08 | -43.96 | 2024-12-17 02:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1be2b8f9-08f0-36e6-a5ad-9156450d89f9 | -5.05 | -43.91 | 2024-12-17 02:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe6b1455-9162-31d8-994b-874924333891 | -5.08 | -43.91 | 2024-12-17 02:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 989d7e1e-c1fe-3cc9-a564-1b6366dde3a2 | -5.11 | -43.92 | 2024-12-17 02:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ff0121c-9ce8-393c-8720-b3175fd5a8ac | -5.11 | -43.87 | 2024-12-17 02:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05365269-2a1e-36e0-9a46-040417acdb87 | -4.7952 | -46.4012 | 2024-12-17 02:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 9e84c9ab-adf2-35d1-abab-1f68ed261b6c | -15.0865 | -59.6487 | 2024-12-17 02:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| c00309f4-98f2-3211-be74-d017cd8615e5 | -19.1043 | -52.8493 | 2024-12-17 02:10:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 8f66f187-3227-325f-ba6b-d4edddbaf4ec | -3.2506 | -46.8049 | 2024-12-17 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 154.2 |
| 38967c2c-4c8e-32a9-8f42-b85c84905b9c | -19.1038 | -52.8711 | 2024-12-17 02:10:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 04d52216-41cb-3598-bf93-547d1f2b10d9 | -15.0672 | -59.6504 | 2024-12-17 02:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 7e109b76-abd8-3509-8833-9dad88bfe7a6 | -3.2968 | -53.3749 | 2024-12-17 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 819ed133-f3aa-3b4a-bdc8-093f7daa05a2 | -3.2969 | -53.3547 | 2024-12-17 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 556d3526-5c1a-3f5b-9583-d547b3a0eb9d | 4.4435 | -60.9657 | 2024-12-17 02:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 01bb3638-78e4-3242-be23-dd47ffa8c2f5 | -10.1811 | -36.2691 | 2024-12-17 02:10:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 166.7 |
| 07331da7-fdb4-3eed-a662-b08a54135d21 | 4.4435 | -60.9846 | 2024-12-17 02:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 1f25c2c0-69c0-3fa5-b0da-be9f7febc126 | -3.232 | -46.8056 | 2024-12-17 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 3aacf200-bac6-350e-8896-4df111ed193f | -10.1618 | -36.2726 | 2024-12-17 02:10:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 202.7 |
| c010becd-a274-3550-ab08-3719018a3a37 | -6.214 | -46.2202 | 2024-12-17 02:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 91e072df-6a16-363f-b6a5-ecebb6e25606 | -6.214 | -46.2202 | 2024-12-17 02:20:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| be8f819a-a9ea-32a8-9e10-4961147ff0b4 | -3.2968 | -53.3749 | 2024-12-17 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 9bd180f4-317d-35b9-bbd0-758210309834 | 4.4435 | -60.9846 | 2024-12-17 02:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| dba7e607-9c9b-3a69-8f6b-edaa26db3f41 | -6.505 | -35.0042 | 2024-12-17 02:20:00 | GOES-16 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| ac6619e1-7206-3bd4-be19-d0c28862ec6a | -2.5676 | -45.9648 | 2024-12-17 02:20:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 38.9 |
| cdfdf926-16d9-3de7-bc69-c151df1294bf | -3.2969 | -53.3547 | 2024-12-17 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 9145382e-ac5a-3023-a168-eea59d3f2b10 | -3.232 | -46.8056 | 2024-12-17 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 187.2 |
| 41ad2fc2-a620-3def-a344-1f7fb17c5f2f | 4.4435 | -60.9657 | 2024-12-17 02:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 68.4 |
| bd75f8b1-cf8a-3405-9260-22b189c253aa | -6.4859 | -35.0065 | 2024-12-17 02:20:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 183.2 |
| 90c3c6d2-666a-3bf7-af7f-42834c4723f7 | -6.4862 | -34.9789 | 2024-12-17 02:20:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 55.1 |
| f96878ad-6cdb-32fb-aca0-4b8d2d854497 | -15.0865 | -59.6487 | 2024-12-17 02:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 3ba2af46-0f66-3abe-a1a5-f3464e5c6a51 | -3.2321 | -46.7836 | 2024-12-17 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 94bc4f81-9347-36dd-90f2-7699497aba40 | -6.4855 | -35.034 | 2024-12-17 02:20:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 63.8 |
| 37892e7f-8aef-3b7d-8a4f-ac11f68fed83 | -15.0672 | -59.6504 | 2024-12-17 02:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 4d13c89d-9003-3917-83b8-1213d819cb84 | -3.2506 | -46.8049 | 2024-12-17 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 275a4061-8c3a-3844-9b97-bf38eb9d6986 | -3.2321 | -46.7836 | 2024-12-17 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 93d3b992-f9ae-3e24-9cb2-cf07c8ee161c | -4.7952 | -46.4012 | 2024-12-17 02:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| ec86a585-1151-3b9b-b8ff-6f89b7712c01 | -6.214 | -46.2202 | 2024-12-17 02:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 40ea7f31-b1af-393d-a0c4-afeb97dd3095 | -3.2969 | -53.3547 | 2024-12-17 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 1e31f8f8-36e1-3ea1-b020-760b4ab2aa43 | 4.4435 | -60.9846 | 2024-12-17 02:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 54458298-f47b-34c3-8237-76cab86bb736 | -3.232 | -46.8056 | 2024-12-17 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 183.7 |
| 8435c484-e455-3c95-9fdc-98e29203568f | -3.2968 | -53.3749 | 2024-12-17 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 41c5331d-091a-3086-a63a-3b2ee1644660 | -3.2506 | -46.8049 | 2024-12-17 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 150.8 |
| 98aa5306-ec70-3b9b-b378-ce58befe4030 | 4.4435 | -60.9657 | 2024-12-17 02:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 3a31b9d9-116d-31fe-aa7a-e664bf82fd4d | -3.2507 | -46.7829 | 2024-12-17 02:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 521541af-058f-3726-bf00-98191c95fb4f | -3.2968 | -53.3749 | 2024-12-17 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 99820e30-6114-383f-94c1-d37a8421840f | -6.214 | -46.2202 | 2024-12-17 02:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |


[Clique aqui para ver as próximas entradas](README7.md)
