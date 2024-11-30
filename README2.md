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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f342cc0f-08c8-339e-a6fe-6df359e39b2b | -2.6985 | -56.829 | 2024-11-30 00:10:00 | GOES-16 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 7503111f-4949-3995-9adb-48cb5e6096d1 | -1.6595 | -54.2341 | 2024-11-30 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 378aa72b-5860-3a65-8ebd-95a5df71a132 | -3.1481 | -53.8233 | 2024-11-30 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d3016f5f-f605-3f0f-9511-071d00c5750c | -2.9428 | -45.0776 | 2024-11-30 00:10:00 | GOES-16 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| d0ac1c0f-f5ca-3f11-85d6-626e3913a55c | -1.4379 | -55.2136 | 2024-11-30 00:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| e0167240-9e10-319d-959e-941ac2b9bdb5 | -3.9697 | -41.5416 | 2024-11-30 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 4057edc8-1520-3a02-99fe-198e4fe2bdbc | -3.9884 | -41.5405 | 2024-11-30 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 57.5 |
| 7fc7ad62-c4d7-3e64-aea5-65c5b635b0b8 | -4.8715 | -41.2674 | 2024-11-30 00:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 46ba6ec7-6948-3489-8c00-133bee89386e | -2.0163 | -50.7768 | 2024-11-30 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 8b61960a-7013-3274-a8e9-2c48d3d58d1e | -6.086 | -48.0557 | 2024-11-30 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| fbac531b-dc6c-3dd8-a433-2fb9f3261eef | -2.5216 | -48.4591 | 2024-11-30 00:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| b27fad99-3c6e-3d45-afae-9119c762ee3e | -3.4975 | -53.8137 | 2024-11-30 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 216a393b-8fb4-39b9-aa63-0c52fb467ba4 | -1.2556 | -54.5589 | 2024-11-30 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 652a6d8f-1a9b-3ab0-8336-ae829a83caa4 | -1.6419 | -53.8731 | 2024-11-30 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f3fca514-7ddd-3336-b731-f7f5ec6ea555 | -1.0022 | -51.7235 | 2024-11-30 00:10:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 245440a5-ddab-36d5-92b4-4e7d4fea5290 | -4.6238 | -46.9849 | 2024-11-30 00:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b767fff3-f4e2-329e-906d-9e16903a57a3 | -1.4379 | -55.2335 | 2024-11-30 00:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 426610a0-d63a-33fc-9377-883ef860a8b4 | -4.6837 | -46.3852 | 2024-11-30 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| af60bacb-5a20-3e4f-8b4b-006e96836afb | 1.1805 | -55.9671 | 2024-11-30 00:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ab5c4f0c-bc06-34db-ae40-528a6b4b3bf6 | -3.3668 | -49.7545 | 2024-11-30 00:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 4988873c-14f6-3f88-b2f2-fd0b8467423a | -3.6757 | -47.1395 | 2024-11-30 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a7a58df9-b5b1-3c7d-be37-309dfa77ef6b | -6.0862 | -48.0339 | 2024-11-30 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 49fd1578-8d4d-33b1-bd1a-6c0da97e9859 | -4.6052 | -46.9859 | 2024-11-30 00:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d35f3a53-3a12-356c-93d7-0fc3aaab8fe5 | -17.6457 | -57.5668 | 2024-11-30 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| d19009b9-ed17-3c79-8183-26e2e41c6de3 | -17.6651 | -57.585 | 2024-11-30 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| 7705d0ee-9701-3355-a537-3d0acc38c881 | -3.4792 | -53.7941 | 2024-11-30 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 5a8bdbfc-b4b1-3ad8-b953-aaf4b522964f | -1.3271 | -55.8475 | 2024-11-30 00:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 98405d3e-fd4b-3ace-9363-760388364196 | -4.8713 | -41.2915 | 2024-11-30 00:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 270.0 |
| 4dc31cd6-e949-3067-aab1-806de8c39d98 | -4.665 | -46.3862 | 2024-11-30 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 18b520ae-40e6-38f4-a339-3bc642550f69 | -2.1928 | -47.1451 | 2024-11-30 00:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 334e4d69-36ac-37f1-9e4c-d21753b16119 | -2.8304 | -45.2845 | 2024-11-30 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 113.5 |
| f19f2436-3ee5-3d08-b0a7-996d58d5d9fd | -3.7021 | -45.6764 | 2024-11-30 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 2c2a9871-c665-35f7-8e2f-34224e9536dc | -3.259 | -53.6388 | 2024-11-30 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 5ae2b2e6-8e9d-3d49-bd19-a57734376f24 | -17.6457 | -57.5668 | 2024-11-30 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 799b6835-6089-3b9a-b68c-e11f4a30accd | -2.0163 | -50.7768 | 2024-11-30 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 2bf95256-213d-3549-88b0-91e51d10d779 | -2.9614 | -45.0769 | 2024-11-30 00:20:00 | GOES-16 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 253cb9da-e52a-30ef-85a7-ac6cdfc2ef94 | -3.4975 | -53.8137 | 2024-11-30 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 0e355ce2-ae68-387c-9490-a2af134fb3b6 | -3.9888 | -41.4925 | 2024-11-30 00:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| 7fae9646-d478-3da3-8f77-d9c7777cccab | -4.6837 | -46.3852 | 2024-11-30 00:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 1086939c-6112-3077-bb27-eb7ba146ec22 | -3.7021 | -45.6764 | 2024-11-30 00:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 2a4ba81e-d943-381d-a972-ad68250dfded | -3.3668 | -49.7545 | 2024-11-30 00:20:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ba70e49b-7711-36de-b932-27a97ba66155 | -2.9965 | -45.5258 | 2024-11-30 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| afdeaa40-fe91-3683-b929-a9cd68a6a7ca | -3.9886 | -41.5165 | 2024-11-30 00:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 225.4 |
| 6cf5be85-f8b8-3c6a-9375-66e08fb142ed | -1.2739 | -54.5387 | 2024-11-30 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 0d7c458a-c53a-3295-b32d-16dc9df22244 | -4.8901 | -41.2902 | 2024-11-30 00:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| a879fcf2-c41e-3592-b9b1-f432122c3aa3 | -4.694 | -42.3787 | 2024-11-30 00:20:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 5ea4ed74-7a5d-35db-bdaa-d0645981d548 | -1.2739 | -54.5587 | 2024-11-30 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 179c904c-16ef-3df4-a959-63ae51853235 | -2.6985 | -56.829 | 2024-11-30 00:20:00 | GOES-16 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 7d129940-cf07-32a2-894f-62ed29e2c851 | -4.6051 | -47.0079 | 2024-11-30 00:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 258.1 |
| 5f889505-dc3b-399e-8c5c-595b427b5cab | -2.5963 | -53.9771 | 2024-11-30 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 9676c7f0-cf73-382d-a768-4ef7719736a4 | -1.5116 | -54.9546 | 2024-11-30 00:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 3c86a197-9c6b-32f4-bca5-1182ef453bef | -17.6651 | -57.585 | 2024-11-30 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 99ab5c79-ae82-32eb-a013-6b31103a3bd4 | -1.4379 | -55.2136 | 2024-11-30 00:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d5c5e23e-a719-338a-8c6b-33a43e2b84ac | -4.6052 | -46.9859 | 2024-11-30 00:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 84723945-6d11-3585-a0d3-929432d461de | -2.8304 | -45.2845 | 2024-11-30 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 129.9 |
| a426fd3d-4cac-3175-85f7-f9061d49b583 | -4.8711 | -41.3157 | 2024-11-30 00:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 0266f691-00f5-381f-bd89-7bdeb318c2ad | -6.086 | -48.0557 | 2024-11-30 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| dfd54c50-8761-31d3-a59f-2930eaf8ca3e | -1.4379 | -55.2335 | 2024-11-30 00:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| c1ef989d-a9cc-3382-9889-2f96f5f46767 | -1.0022 | -51.7235 | 2024-11-30 00:20:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 233d6586-00b3-381c-b870-6ec8d62ad333 | -4.8525 | -41.2928 | 2024-11-30 00:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 116.5 |
| 6045dd94-adbc-302b-b4dd-db8b70c20ab6 | -3.1481 | -53.8233 | 2024-11-30 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c8cb71c0-793b-397e-b4c4-d005f7f3ba57 | -1.6938 | -46.7833 | 2024-11-30 00:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 16e2ddc0-2ff2-39c4-8037-7e2fd96f7cfb | -3.2591 | -53.6186 | 2024-11-30 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| ec44002e-de3c-383e-a077-e76f3f1d5121 | -2.1928 | -47.1451 | 2024-11-30 00:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| b1cfcd7b-4c74-30b1-9070-cc4f07bf7dc6 | -3.9697 | -41.5416 | 2024-11-30 00:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| c2a262e3-86a5-37bd-90cc-d99457cdef62 | -4.6652 | -46.364 | 2024-11-30 00:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| d340e2e2-e597-3381-bc98-0748890fdfb4 | -4.6838 | -46.363 | 2024-11-30 00:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 9ba9f3a9-bfc9-3c3c-9add-f3205ed79680 | -1.6419 | -53.8731 | 2024-11-30 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1e49f750-2ece-3cd8-b290-0d739c430299 | -3.97 | -41.4935 | 2024-11-30 00:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 82a0412f-fa36-37c4-8c1f-f73920e15ef3 | -4.8715 | -41.2674 | 2024-11-30 00:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 100.4 |
| eb4dfc5e-c41f-3e2a-833c-c1793b3c30ae | -4.6049 | -47.0299 | 2024-11-30 00:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 63c50981-44d2-3ffb-8dfc-9e2e3b16ac6b | -3.4791 | -53.8142 | 2024-11-30 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 7b5cf6e5-697b-36ec-a27c-3b435e85c684 | -3.9699 | -41.5176 | 2024-11-30 00:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 232.2 |
| 8ab7355c-5247-3a88-abda-5c25d247519a | -3.4976 | -53.7935 | 2024-11-30 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| ac8c6688-3b61-33a5-ab84-6ff64f7e7cf1 | -1.2556 | -54.5589 | 2024-11-30 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 577f8161-b599-3f42-a664-cea78a69c5c2 | -3.2406 | -53.6393 | 2024-11-30 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 4d30159e-4e5c-3ac5-b556-3f4141954392 | -4.6237 | -47.0069 | 2024-11-30 00:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 100.1 |
| a2e58602-cb16-3236-84cd-85ff9f604107 | -2.5216 | -48.4591 | 2024-11-30 00:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 1b9b107b-8c8c-3bf2-8bab-79f33acb5818 | -6.0862 | -48.0339 | 2024-11-30 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 9eccc062-6b0e-3b48-9acc-5de982a5c14b | -4.8713 | -41.2915 | 2024-11-30 00:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 251.0 |
| 0f04506d-187d-3991-aa33-8207706cc8eb | -17.6851 | -57.5621 | 2024-11-30 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 7888d8cb-0b3c-37a2-bbc6-9e0264b66ba1 | -1.2556 | -54.5389 | 2024-11-30 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 9a30935d-6ba7-36c7-b2f8-f9277b42aad1 | -3.4792 | -53.7941 | 2024-11-30 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| b252d74f-ccc7-3df2-9aed-9750d711cd75 | -1.3271 | -55.8475 | 2024-11-30 00:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e66f1c37-1e2c-3dc5-a306-38f4002af366 | -2.8303 | -45.307 | 2024-11-30 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 4530ce12-812d-327e-ac74-e1e7e3c67bce | -2.614 | -54.2177 | 2024-11-30 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 648ca7d6-78da-35ec-a463-2d0ca6601bfc | -3.148 | -53.8434 | 2024-11-30 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 2fe56e99-2e5f-3f3a-bf09-20b5124756d6 | -1.6753 | -46.7836 | 2024-11-30 00:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 0e77f4a0-24fe-3c33-82e6-08674467ebcb | -17.6654 | -57.5645 | 2024-11-30 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.1 |
| ae7c1957-29fb-3785-a63c-619d88df8f84 | -1.4379 | -55.2533 | 2024-11-30 00:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| bf7e4d6c-bb5b-3506-8a40-7cfecf6c28a0 | -1.6777 | -45.7868 | 2024-11-30 00:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ce432415-aa8b-3f8e-8f1a-463885e0a4bc | -3.3998 | -50.6573 | 2024-11-30 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| fe0694b5-d838-38f1-9173-cee567e2d679 | -4.6837 | -46.3852 | 2024-11-30 00:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| d38163c8-d157-3967-b53f-594fa4f5e492 | -3.148 | -53.8434 | 2024-11-30 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ac1cc545-2c06-3b68-88df-21a5c785298f | -4.8899 | -41.3143 | 2024-11-30 00:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| c82ecbb6-8fcb-3086-be6f-9e1bd04f3aae | -4.6049 | -47.0299 | 2024-11-30 00:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 955abbf4-bd72-3f85-a9bd-6657f393f099 | -3.2591 | -53.6186 | 2024-11-30 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| d8286c84-d3f7-334c-b1b7-4b5c03675b43 | -4.8525 | -41.2928 | 2024-11-30 00:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 200.6 |
| 99a8c22c-8c8c-3214-852b-7b69762faafc | -1.2739 | -54.5587 | 2024-11-30 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 0f023705-c4ce-3a80-9820-242b16b5691f | -3.9888 | -41.4925 | 2024-11-30 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |


[Clique aqui para ver as próximas entradas](README3.md)
