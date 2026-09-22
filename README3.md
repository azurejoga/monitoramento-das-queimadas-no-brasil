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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75f492f8-0059-306a-bfde-e358a1f59107 | -5.7567 | -45.1067 | 2026-09-22 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| a3412e28-4ac2-375a-8ac8-68952de542c5 | -11.3257 | -54.0282 | 2026-09-22 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 164.8 |
| 1e7684ca-6c75-3abf-9114-9238912bd4a3 | -11.6793 | -43.4684 | 2026-09-22 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.0 |
| f8712473-e444-39ba-915a-b3d3c48e13b2 | -9.2573 | -46.1647 | 2026-09-22 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 533.9 |
| 20cf862a-94eb-344e-b1b1-ad13b532f46f | -2.4206 | -58.2712 | 2026-09-22 00:20:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 2876ce7a-6cc7-3f76-a9cb-e20fc328958f | -6.5898 | -44.15 | 2026-09-22 00:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 13079606-f36c-36b4-aee0-a54299d4ceea | -7.5888 | -57.6953 | 2026-09-22 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 11ac1e5e-0793-36a4-9831-75fbdada8d42 | -5.7866 | -43.8453 | 2026-09-22 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 183.4 |
| eac4b498-c132-3018-bbe6-e6514548bdae | -6.0925 | -57.6847 | 2026-09-22 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 31d144d7-63e4-3ad8-998c-42e9582f8b52 | -6.1109 | -57.684 | 2026-09-22 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 507cd32e-a37e-3808-89cc-f1fb22e6b991 | -11.7675 | -50.804 | 2026-09-22 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| a3b957b4-024d-3e68-87ad-e7d7f78be0a6 | -6.0549 | -57.8227 | 2026-09-22 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 8478eddc-104b-3249-85f3-a02488d80025 | -6.0925 | -57.6847 | 2026-09-22 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 3f2c3d86-648c-39fd-a827-27f76a01eaa1 | -3.405 | -59.522 | 2026-09-22 00:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 4c6f478e-ada7-39ab-a261-bdef6c307e5c | -6.467 | -59.9902 | 2026-09-22 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 96ea1b36-5529-3095-a7bd-7dfb259aa328 | -11.6793 | -43.4684 | 2026-09-22 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 8ef720b6-aa3b-347d-8996-fc1c1808aca1 | -8.2576 | -55.2403 | 2026-09-22 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| bd076cd1-bf5d-3257-95a7-994f554a1c57 | -12.8059 | -54.0255 | 2026-09-22 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 98f7e63b-818d-30f2-8589-751a7f1c5a66 | -3.3867 | -59.5223 | 2026-09-22 00:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 7ac81415-8f74-302f-b29c-bf0cf7425a54 | -8.2388 | -55.2616 | 2026-09-22 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a3517b16-cc12-3c83-83e4-52976bebe642 | -8.2572 | -55.2805 | 2026-09-22 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 8a389714-5e04-3eb6-8bba-839c3e0097e9 | -12.5551 | -45.9376 | 2026-09-22 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ce653eec-7ee6-316e-8bab-59b926c87288 | -18.7466 | -46.9534 | 2026-09-22 00:30:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0965ca57-815a-3b77-a4c2-fdaa811f363d | -4.2951 | -49.1234 | 2026-09-22 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| a17f5293-e971-3579-a600-f3992744c3f9 | -7.3467 | -45.3405 | 2026-09-22 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c88160df-0977-31e3-a9d4-bbff8a6e8aaf | -8.8275 | -50.482 | 2026-09-22 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 5e352029-3b16-3666-b594-f168ba7c0ac0 | -4.3137 | -49.1226 | 2026-09-22 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 72658c5a-0463-39f4-8183-fce5b20eca52 | -7.326 | -55.5953 | 2026-09-22 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 76acfe0b-b8e8-333c-8796-cf650607ef50 | -8.2389 | -55.2415 | 2026-09-22 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 1016d278-d6d5-3724-b068-23056560cfcf | -12.5547 | -45.9605 | 2026-09-22 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 6984cb12-048c-3047-8cb5-1bed4257c999 | -7.5704 | -57.6766 | 2026-09-22 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 6582d1a6-fc6f-34d2-a0f0-cec463edb2d4 | -11.3068 | -54.0299 | 2026-09-22 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 72ddcc27-aa55-3dd8-b29e-7ab446e33b3e | -12.574 | -45.9576 | 2026-09-22 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| cfa5df5a-cec9-359f-91bd-89ea6ad28489 | -8.8273 | -50.5032 | 2026-09-22 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 9a1c3085-5146-33a3-b43e-add2b66908f4 | -2.8608 | -57.7994 | 2026-09-22 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 6b1305cc-3d79-3872-9eaf-9c002d04ac5d | -5.7569 | -45.084 | 2026-09-22 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 539.9 |
| f12e4cab-91e9-39b0-98fc-d51cf081d39a | -11.6798 | -43.4446 | 2026-09-22 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| c1ec59bf-1383-3b18-83b8-b801b981c5ae | -8.257 | -55.3005 | 2026-09-22 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| e791fc60-1190-3191-b2e0-833909190009 | -6.4485 | -59.9909 | 2026-09-22 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| b6fc2200-fc89-3da3-97c5-9e9f4ba402c7 | -6.5898 | -44.15 | 2026-09-22 00:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 2d5d58fe-b047-3b44-97b6-2a1657e5c52c | -11.7672 | -50.8253 | 2026-09-22 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 8fde2c9b-8aec-3491-99e9-de478238eb57 | -5.7382 | -45.0853 | 2026-09-22 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 184.5 |
| a08d9b37-22f1-3470-a504-f6bb9c58a7a4 | -7.5703 | -57.6962 | 2026-09-22 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2da999bc-7f4d-3c63-bee4-992511b3d7db | -6.0928 | -57.6262 | 2026-09-22 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 4eb3ede2-d206-3cf5-ba4c-e02eca7290fe | -11.3255 | -54.0487 | 2026-09-22 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 02ff2306-1dbc-38b0-9758-7d9d18873c3d | -9.1438 | -67.9428 | 2026-09-22 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 7ca28b8a-382d-3259-b866-fe1068bce4d7 | -6.1109 | -57.684 | 2026-09-22 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 87b8773d-a74b-33d5-8763-693208905c6a | -3.0542 | -54.4081 | 2026-09-22 00:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| fd264462-d7df-3038-9675-a8ae38ff7c8e | -8.6169 | -54.6328 | 2026-09-22 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| a5d9864b-bbc2-3a8a-8c82-4aa0acfba22a | -7.5888 | -57.6953 | 2026-09-22 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6ff68ac8-bec5-3542-988e-a5f91772fa54 | -6.0365 | -57.8235 | 2026-09-22 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 2eb5e01b-64dc-32da-b82f-bdc240716eda | -12.8056 | -54.0462 | 2026-09-22 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 794480ed-f805-3e7d-83f7-0240bd1bd6ac | -11.3257 | -54.0282 | 2026-09-22 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 136.4 |
| c3ea00f3-f32f-3f40-86ee-77a158f9d9e4 | -5.7864 | -43.8684 | 2026-09-22 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 46de73b9-7d2a-3631-8ca3-46ea588bdddb | -18.7472 | -46.93 | 2026-09-22 00:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 56dbb33f-b009-3cf8-bf50-f42ae8ca5881 | -7.6621 | -69.9215 | 2026-09-22 00:30:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 08d35761-a665-38dd-b63b-7f8d26c44188 | -11.3066 | -54.0505 | 2026-09-22 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f31c2216-d70a-31a9-a5f8-816f5d885fb9 | -6.571 | -44.1516 | 2026-09-22 00:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 00922580-1661-32ea-8ae7-19b25e5663c3 | -3.0726 | -54.4076 | 2026-09-22 00:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 7af3638d-acce-361f-9aa4-3a5e6fa266dc | -6.789 | -48.6779 | 2026-09-22 00:30:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 54.8 |
| d7478a28-8386-30e6-9927-ed91410908a3 | -5.7571 | -45.0613 | 2026-09-22 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 82829a65-e4fc-378d-986f-604d51be95d5 | -5.7756 | -45.0826 | 2026-09-22 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| a01adeb4-8a6e-334a-86d8-237112734cb7 | -8.2574 | -55.2604 | 2026-09-22 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| efb732f3-0cad-3ed9-b754-4a6eef51ca67 | -12.7868 | -54.0275 | 2026-09-22 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 08d15a81-d98d-3db5-841e-c32808b627eb | -7.5889 | -57.6757 | 2026-09-22 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 163.7 |
| 10c9e53a-62cc-3c35-b16c-3e6fb3582499 | -5.7567 | -45.1067 | 2026-09-22 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 471cb830-eaff-3454-9e4b-b32e7679039e | -2.4206 | -58.2712 | 2026-09-22 00:30:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 2dfcd02c-e11e-35fd-ae9c-41270806407e | -11.7675 | -50.804 | 2026-09-22 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 640686a5-22b7-37dd-9bee-79b24bc07fce | -18.7466 | -46.9534 | 2026-09-22 00:40:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 3c08eb97-750b-3765-a3e5-715dbe7c4b9b | -3.3867 | -59.5223 | 2026-09-22 00:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| a3286cd2-bc62-38ea-abb2-0e94a8f45c20 | -5.7864 | -43.8684 | 2026-09-22 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 67581f43-bdb8-3bb1-9bb8-b83864cb5b64 | -6.0928 | -57.6262 | 2026-09-22 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 99cd8886-244c-3613-8294-444f28753897 | -8.257 | -55.3005 | 2026-09-22 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| fd8abc90-f9d4-3273-82d3-9af7f49c9df5 | -11.3257 | -54.0282 | 2026-09-22 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| e0c017e5-1882-385c-b5cf-e3e001614961 | -6.4485 | -59.9909 | 2026-09-22 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| cc349a22-2dd6-31f8-907b-9e1e07982384 | -6.5898 | -44.15 | 2026-09-22 00:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 3ec1fcb2-eb97-39af-8220-d36c178d25d1 | -2.4206 | -58.2712 | 2026-09-22 00:40:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e3df46f9-7df4-36c0-9ade-ecd6ef5a629d | -6.571 | -44.1516 | 2026-09-22 00:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 61af24dc-f44c-3d3c-b21c-182d5daf749b | -6.1109 | -57.684 | 2026-09-22 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 582456b5-d24f-3c49-939c-299b69f72cc8 | -3.405 | -59.522 | 2026-09-22 00:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 0793e9cf-d5a8-385e-bd6e-e3bdddccb62d | -12.4196 | -47.0679 | 2026-09-22 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 40c6f718-7bbd-3005-9896-5da52a1494fb | -12.1458 | -47.3974 | 2026-09-22 00:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 6d94ecd0-102c-3920-a3d4-b7b0798d3b17 | -4.3137 | -49.1226 | 2026-09-22 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 49b5f301-8f16-3089-b4a0-a67a5a3d4daf | -11.3066 | -54.0505 | 2026-09-22 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 0acc370c-582b-3ab2-96f6-207b05f45700 | -3.0542 | -54.4081 | 2026-09-22 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d56df7e8-1c15-3fb5-bd9d-64d9e1d43b7f | -3.0726 | -54.4076 | 2026-09-22 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 271fae16-59d1-3e07-9aae-919c10772771 | -5.738 | -45.108 | 2026-09-22 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 3c6a2343-dece-3bd4-b642-73100e642468 | -5.8052 | -43.867 | 2026-09-22 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 16073b88-2e39-3b4a-8322-982bb173524b | -8.8273 | -50.5032 | 2026-09-22 00:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b072b60d-7b4d-34d7-ba55-660e051297ce | -18.7472 | -46.93 | 2026-09-22 00:40:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 128.7 |
| dfaf1319-24e3-3ad0-bd97-670f93cfd0a5 | -11.7672 | -50.8253 | 2026-09-22 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 43877d3f-7deb-3b71-8d6c-91d29c4b5ed6 | -5.7571 | -45.0613 | 2026-09-22 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| af1bb871-2862-3e5b-bd75-8ec033267ce3 | -5.7569 | -45.084 | 2026-09-22 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 448.2 |
| 70a51ef3-aef8-3782-bc74-933d0c645036 | -11.7675 | -50.804 | 2026-09-22 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 8b658c3b-a73d-33c0-b340-c1af6142e172 | -6.0365 | -57.8235 | 2026-09-22 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 18e31b2a-6b50-34ec-89cb-5ddfa0cb1a4f | -7.6621 | -69.9215 | 2026-09-22 00:40:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 1563dfa4-f063-3f64-82cb-4701806b2153 | -7.5703 | -57.6962 | 2026-09-22 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| c2c237b3-d5a7-392b-800d-bd98f4de2e6e | -8.6169 | -54.6328 | 2026-09-22 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| d1563dd0-f896-33bf-bf2e-a6a72bc8a66d | -12.4004 | -47.0706 | 2026-09-22 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| ef1a3f87-2258-3986-8224-b5c8d5c9ce77 | -8.2574 | -55.2604 | 2026-09-22 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |


[Clique aqui para ver as próximas entradas](README4.md)
