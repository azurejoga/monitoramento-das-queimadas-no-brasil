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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03ed0376-f586-33db-a97e-a297edec6e96 | -17.293 | -57.5062 | 2024-11-10 02:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.2 |
| f70ae4ca-0531-3d21-a175-1027f63fb002 | -2.9355 | -51.482 | 2024-11-10 02:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 1c141868-7fdb-3265-a2d9-c374665a11f5 | -2.7587 | -49.3497 | 2024-11-10 02:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 5dab6395-3b79-335a-9942-e11b025b20ab | -3.967 | -48.15 | 2024-11-10 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| f7241a53-4340-3e75-aa9b-35468b813432 | -2.0954 | -48.8125 | 2024-11-10 02:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| fe8d7be2-783b-37be-b9a8-05bdd5faaf4d | -3.9486 | -48.1291 | 2024-11-10 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 99d97990-9370-3bc6-9a24-88fba3f7f4b7 | -3.9668 | -48.1932 | 2024-11-10 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 357432f3-8df6-3334-b379-78a13d6a0c77 | -3.5064 | -44.0294 | 2024-11-10 02:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 54aa70b4-534c-35be-89e2-30d3f80aa5f1 | -2.8803 | -51.4628 | 2024-11-10 02:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| bd2bf0e2-ffdd-3251-b6d7-044a3f03b697 | -8.3967 | -44.1365 | 2024-11-10 02:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 161.6 |
| ca079652-916a-3dd8-a937-6a12d9e90b42 | -3.6003 | -47.3614 | 2024-11-10 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| cfddbb8f-c1fe-3192-bc23-eaa72e3dbda3 | -2.9494 | -52.7748 | 2024-11-10 03:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 2ae6549c-c1f4-344f-b672-a400eb7899ac | -17.313 | -57.4834 | 2024-11-10 03:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| a83b1993-c3f9-3def-82a3-bcfa0c140f02 | -2.4365 | -46.3019 | 2024-11-10 03:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| dfc92f85-80b2-3321-b324-3c8b445fa81c | -3.9483 | -48.1724 | 2024-11-10 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 3667f92c-7ab4-3b26-ad4f-f01b8512bba7 | -3.1239 | -50.4358 | 2024-11-10 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 213.7 |
| 152404ac-ad64-38a3-858a-459794e1c2ac | -3.9668 | -48.1932 | 2024-11-10 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 95e1f5e5-6dfc-36f1-8a58-c2510cf3fc0c | -3.9669 | -48.1716 | 2024-11-10 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| d2a0a38f-481f-3528-89a2-a3722b59cc16 | -3.1422 | -50.4562 | 2024-11-10 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 333.9 |
| 0b9a2aac-b295-3bc0-9191-4c4b9677e5ff | -2.8802 | -51.4835 | 2024-11-10 03:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 4b67016d-1b30-34f6-acb8-c59f07c50075 | -17.2933 | -57.4857 | 2024-11-10 03:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.7 |
| e6876c65-ab67-3440-b308-3cf80962a301 | -2.8803 | -51.4628 | 2024-11-10 03:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 839d84cd-8cb4-39f6-9b13-5a920b0bfbc3 | -2.9355 | -51.482 | 2024-11-10 03:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 1f15a8a9-3a5c-3122-8f97-cb850f4bc059 | -3.1238 | -50.4568 | 2024-11-10 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 9d62ce33-08fa-3e84-8c5a-ad6df8fed723 | -3.525 | -44.0286 | 2024-11-10 03:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 768a7a28-5071-36cc-8143-71c8e791bd6a | -5.5608 | -43.9775 | 2024-11-10 03:00:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 1e4bb6ea-8cee-323b-8b0d-d125b08b3c75 | -2.931 | -52.7753 | 2024-11-10 03:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 993fccdf-db57-331d-b69c-c4ebb7dcbadb | -3.6004 | -47.3395 | 2024-11-10 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| bb7c6c91-c04a-3233-b02c-d2801403620f | -3.1423 | -50.4352 | 2024-11-10 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 480.6 |
| e22d49e9-5747-3d20-95cf-a7bde125bcd1 | -8.3967 | -44.1365 | 2024-11-10 03:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 2a9ab5fb-2a97-328b-874b-57c4ffd7dec3 | -1.5347 | -52.2104 | 2024-11-10 03:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 0daf19d9-7c4f-3417-aea3-3d4e7289626b | -17.293 | -57.5062 | 2024-11-10 03:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 9992da11-caf5-3e97-a701-8c0d676ecb40 | -2.8857 | -45.3726 | 2024-11-10 03:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 44cbae8b-1c32-30fb-88ff-261d31241721 | -2.7587 | -49.3497 | 2024-11-10 03:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| ab4d505c-4ab3-30fb-8fc2-079d5f6fd3f3 | -3.5064 | -44.0294 | 2024-11-10 03:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| b6c55097-e0bc-3149-b6df-41d48b60dd1e | -3.6003 | -47.3614 | 2024-11-10 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 2aee5d9e-e22d-38d4-b7a1-f094a713cfcd | -2.0953 | -48.8338 | 2024-11-10 03:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 2d36fbd5-77d6-3770-b6da-b6e21c6ace4c | -8.3778 | -44.1386 | 2024-11-10 03:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| b0b0e5be-a63a-39e5-a5fc-56552f52294b | -2.9171 | -51.4825 | 2024-11-10 03:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b1f4b91e-b146-394c-bfc7-91edee26f3dc | -8.4156 | -44.1344 | 2024-11-10 03:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| f970e69a-ff1f-3f7d-b3aa-79d75d5670ab | -2.8618 | -51.484 | 2024-11-10 03:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 3040494f-dcc2-39cf-bd96-bed6622eb1d0 | -3.4383 | -50.2999 | 2024-11-10 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 3b8c4795-bb5c-33b5-855b-e7f4528aaf06 | -3.9671 | -48.1283 | 2024-11-10 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| bd35c3b9-497d-3111-b49f-36529970d342 | -2.7772 | -49.3492 | 2024-11-10 03:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| e53a481e-c893-3b21-b1be-1a91d13a17f3 | -8.3964 | -44.1597 | 2024-11-10 03:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 6b36d97e-4db2-3a2b-a5bb-c71a6510991c | -2.9356 | -51.4613 | 2024-11-10 03:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| f10c282f-7b16-3274-a9a6-3d3609b2b7d9 | -3.9485 | -48.1508 | 2024-11-10 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| f89244ea-9854-3f5c-8302-a3794e6ba348 | -3.11 | -50.42 | 2024-11-10 03:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f181c25-f6ae-32b5-bbe1-4ba71283284f | -17.59 | -57.51 | 2024-11-10 03:00:00 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 74b33a66-2110-3c68-b972-a6aad85a84d3 | -3.14 | -50.47 | 2024-11-10 03:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8a42039-b281-351e-b557-79320bdc1adc | -3.14 | -50.42 | 2024-11-10 03:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25f1f93c-d4e9-3aef-99d2-e3ffc8775d46 | -5.5608 | -43.9775 | 2024-11-10 03:10:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 5b6f86a7-0261-3071-86fa-286d4b6486d2 | -2.7587 | -49.3497 | 2024-11-10 03:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 4b545371-8a88-35d9-9100-892f1ccf3e59 | -3.9485 | -48.1508 | 2024-11-10 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 6bf85fbd-9eff-3bbe-a042-2330ef00f69a | -2.8803 | -51.4628 | 2024-11-10 03:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 4ef28d73-d839-3fdd-b4fa-c652641c5ff2 | -17.6073 | -57.5099 | 2024-11-10 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 391.3 |
| 77359170-2750-3116-b054-a2ecc6d2fae1 | -2.8857 | -45.3726 | 2024-11-10 03:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 79b25e99-f80a-31cf-8095-c2862874d770 | -3.6003 | -47.3614 | 2024-11-10 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| d00a1cbe-60a9-363e-a098-6ce6b407ce6f | -8.3964 | -44.1597 | 2024-11-10 03:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 32b2ab57-ef57-31bb-8856-5dbd5357b073 | -8.4153 | -44.1576 | 2024-11-10 03:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 21314a47-5cb7-3bb0-9f15-c63f7718a8d1 | -2.418 | -46.3024 | 2024-11-10 03:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 1f4234bd-03cb-3fa8-860e-17e4dff44d5c | -3.5064 | -44.0294 | 2024-11-10 03:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 3e17bb9b-381f-350c-8488-bd9f4ba4da1e | -17.627 | -57.5075 | 2024-11-10 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 278.5 |
| 08b04669-74db-369f-b1f6-f3865e8af744 | -2.9356 | -51.4613 | 2024-11-10 03:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 3437f2a1-5fe2-3c60-8826-2d3eb1c2a71b | -2.7772 | -49.3492 | 2024-11-10 03:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 5cc6da9d-6d3f-313f-93b2-95280122c54d | -1.2751 | -53.7164 | 2024-11-10 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 132fcc94-dd02-3d65-b32d-aec86121b708 | -3.1608 | -50.4347 | 2024-11-10 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| c5bb54ff-e6cf-3441-82b9-5297ec08d3ca | -3.4383 | -50.2999 | 2024-11-10 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 30772008-e8d5-3c5e-8406-2bb9eb998dfd | -3.1238 | -50.4568 | 2024-11-10 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 187.2 |
| 950fe1ad-acff-388b-9fa9-6253c7c79d83 | -3.9669 | -48.1716 | 2024-11-10 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 0919624b-5ecb-3ca0-b36a-35b3eb2ad5c5 | -3.9486 | -48.1291 | 2024-11-10 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 030d2c00-04b6-39fc-88cf-0111fac58961 | -17.6266 | -57.5281 | 2024-11-10 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 308.2 |
| 61b5652e-b366-3d16-ad0d-b457e2700d70 | -3.1239 | -50.4358 | 2024-11-10 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 320.6 |
| 3a59dec6-909c-3159-b0bc-ad6dff4da770 | -2.0953 | -48.8338 | 2024-11-10 03:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 1d8dee98-5e8a-3651-a524-e55c96aaf46e | -2.9355 | -51.482 | 2024-11-10 03:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 92cdd762-f3ae-3301-9f94-af6ad8784f43 | -2.9171 | -51.4825 | 2024-11-10 03:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 0f8147ac-d4db-342d-88e6-572638327172 | -8.3778 | -44.1386 | 2024-11-10 03:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 97984ba1-f97e-3364-8fd6-6aa18ef411eb | -2.8802 | -51.4835 | 2024-11-10 03:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 06c7ca20-647d-33d7-b481-0f83df8275f3 | -3.525 | -44.0286 | 2024-11-10 03:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| c7199366-71d4-3d73-961d-d6902ddd50e0 | -3.9483 | -48.1724 | 2024-11-10 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 6da86336-e98f-3f26-aff7-e3bb42c641ae | -8.3967 | -44.1365 | 2024-11-10 03:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 158.5 |
| e4563a66-2527-398c-bf08-da576629d202 | -17.293 | -57.5062 | 2024-11-10 03:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.9 |
| ff7028ed-5d96-311e-aa8c-6176f7cbb586 | -17.2933 | -57.4857 | 2024-11-10 03:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 152.2 |
| 9ea871e6-5a67-3183-b4b3-e81ceeb0b0d6 | -8.4156 | -44.1344 | 2024-11-10 03:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 8399a0e0-f18d-3771-97ae-cd093b7c9afe | -3.6004 | -47.3395 | 2024-11-10 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| cc9bedab-1f73-34d2-878c-15b915e7dc9b | -17.6069 | -57.5304 | 2024-11-10 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 420.5 |
| 4241cd7f-a224-3967-8b92-f2fa25823759 | -3.9668 | -48.1932 | 2024-11-10 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ee2216f7-f66f-3a59-88cb-1fc2807eb3d5 | -3.1423 | -50.4352 | 2024-11-10 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 385.5 |
| fe86f995-fcfe-307a-ae5b-20fedc4525fb | -17.6066 | -57.551 | 2024-11-10 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 0383e602-334b-3160-b919-37e21058e85b | -1.5347 | -52.2104 | 2024-11-10 03:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| c0e8e332-36b4-3d95-9ab1-dcbecb72dc53 | -3.1422 | -50.4562 | 2024-11-10 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 222.5 |
| d31f5653-40af-3cbe-99c6-2c47dc7a0b39 | -2.99955 | -40.28957 | 2024-11-10 03:19:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fe718818-6082-31a3-bdd2-e3ddf5c954b8 | -3.00025 | -40.28531 | 2024-11-10 03:19:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 55391d30-8cd0-3fb8-a3aa-17ebea0714f8 | -3.53818 | -43.56394 | 2024-11-10 03:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5996eab0-f821-3a41-8617-3e62a17e5c40 | -2.99817 | -40.28739 | 2024-11-10 03:19:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b0963870-9f0c-3cbf-9b6d-8f662011cd25 | -3.5453 | -43.56509 | 2024-11-10 03:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d8496c0-39ef-3ad2-9ada-0536bce104c2 | -3.75791 | -41.03283 | 2024-11-10 03:19:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a3aacfff-0fe3-37cb-90a4-190fe4fd7641 | -3.54178 | -43.56368 | 2024-11-10 03:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| efbe5c62-abd7-32c1-80bf-db18779af4d5 | -3.75747 | -41.03325 | 2024-11-10 03:19:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 759150d9-9f0f-3b2a-a2a8-a75d963d22b9 | -3.75668 | -41.03801 | 2024-11-10 03:19:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README21.md)
