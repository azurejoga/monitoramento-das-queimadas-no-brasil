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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f83a1f5e-f4e6-3bf8-ab79-1a353a796f06 | -14.6419 | -45.1028 | 2025-05-13 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| a9b05f62-a04f-3b4d-ba7f-d0594c62c884 | -13.9713 | -56.7874 | 2025-05-13 13:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 4ec0e631-7109-34a0-944a-f688bf394fa2 | -13.9902 | -56.8058 | 2025-05-13 13:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 6bd0cfa9-892f-39a0-91e3-a97328789e2c | -13.5683 | -52.8783 | 2025-05-13 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f6d6e181-382d-3ae6-a3a6-0a7f75595e9f | -14.6419 | -45.1028 | 2025-05-13 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| dcc77452-eae4-3fe7-a087-61a8a7a11450 | -13.5683 | -52.8783 | 2025-05-13 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 482dbc35-97a6-3ba9-96f1-38c2ffc4e2ee | -13.9902 | -56.8058 | 2025-05-13 13:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 21b764eb-dddd-3e7d-8237-7d1dda195eba | -13.9713 | -56.7874 | 2025-05-13 13:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| b7305697-c905-3074-8a28-debd0bc45487 | -9.6822 | -49.721 | 2025-05-13 13:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| ea29fa94-b115-32ea-94a5-b0aed8c1e521 | -13.5683 | -52.8783 | 2025-05-13 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| dfa10ef6-335f-3d53-bd44-7ae5a17c15fe | -10.494 | -49.7022 | 2025-05-13 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 4c1af263-2664-371f-ae06-e858afed8903 | -13.9713 | -56.7874 | 2025-05-13 13:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 88914637-6053-3ef9-8af8-f8a3a1132cef | -13.9902 | -56.8058 | 2025-05-13 13:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 8484b7b6-4c71-3102-b491-2db940ab4184 | -9.6822 | -49.721 | 2025-05-13 13:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| eeb22104-1bb6-3d33-9af2-b5aafaaca057 | -14.6419 | -45.1028 | 2025-05-13 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 7dc3a3c7-7c84-3314-ae37-b817e1bc17d4 | -9.6634 | -49.7228 | 2025-05-13 14:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1100eba2-0e1f-3338-b8f6-bd0ab70d76b3 | -7.4061 | -43.4251 | 2025-05-13 14:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 922b9ad4-aba6-36ea-af79-321bf4bf613a | -9.6822 | -49.721 | 2025-05-13 14:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 8606f029-fbf1-3756-a667-c271e0c8c3ea | -14.6419 | -45.1028 | 2025-05-13 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 2bc06994-da90-39f9-a974-47c09a2910b4 | -6.9804 | -42.7854 | 2025-05-13 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 9dd34aff-f4a5-3c59-ba76-bfe0265cbcea | -13.9902 | -56.8058 | 2025-05-13 14:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| bd5a4d2d-9f32-39c1-91b3-c368c8f8f212 | -10.4883 | -46.1778 | 2025-05-13 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| f39e454e-3f38-38df-8d02-b996f0b85e17 | -13.9905 | -56.7855 | 2025-05-13 14:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 64603c30-45b7-3e21-b6ad-9f9518c0e49b | -13.5683 | -52.8783 | 2025-05-13 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 9464e0c5-7a75-34bf-80d9-5aeca90350b6 | -6.9804 | -42.7854 | 2025-05-13 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| aa1d348c-3000-34a1-952b-83bde88e8b15 | -10.4883 | -46.1778 | 2025-05-13 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9d03e513-9484-3f0c-a495-2d275c873e70 | -9.6822 | -49.721 | 2025-05-13 14:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 79b88c1a-198b-305b-8cbf-d26e07b917c6 | -9.6634 | -49.7228 | 2025-05-13 14:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 9c3c22cc-096a-3e88-9cf8-b4cae66ecf37 | -7.4061 | -43.4251 | 2025-05-13 14:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| afc01306-8a8d-346f-ace6-7a1d2fe7bff7 | -13.9902 | -56.8058 | 2025-05-13 14:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 2bd088e9-fa6d-388c-a977-15110513d302 | -13.5683 | -52.8783 | 2025-05-13 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| db2a5d8f-d9a0-315d-a173-697f29d9acff | -9.6822 | -49.721 | 2025-05-13 14:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 2f78d5a3-403a-34b3-9ee8-4c0c77cc20a9 | -10.4883 | -46.1778 | 2025-05-13 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 6511fc9c-3afa-3e8e-af4d-6b9ca5198a3d | -9.6634 | -49.7228 | 2025-05-13 14:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 96eea8d4-d63c-3b46-a07e-9121d075ae04 | -10.4754 | -49.6827 | 2025-05-13 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| de9fa4a5-dea0-3022-b855-97889cdc0e3d | -13.9902 | -56.8058 | 2025-05-13 14:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| fc10f56f-5123-3f5c-8d3f-b2f1066b139d | -6.9804 | -42.7854 | 2025-05-13 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| a46961ed-33ee-356f-a7c4-ab8d1a396757 | -6.9615 | -42.7872 | 2025-05-13 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 6767f805-bcb7-3244-b519-8d7db095c8c5 | -10.8551 | -49.5983 | 2025-05-13 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 9ff9822c-41ec-3e7e-b868-c02ff1b4b8eb | -9.6822 | -49.721 | 2025-05-13 14:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 9f99575e-d4eb-3ea6-8712-269703bdd573 | -9.6634 | -49.7228 | 2025-05-13 14:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 3c84998f-d1ca-37eb-a103-7bc7002f13f0 | -13.5683 | -52.8783 | 2025-05-13 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 233a43f4-ba58-3251-9ac3-0517a2259dae | -13.9902 | -56.8058 | 2025-05-13 14:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| c2b315c2-90f1-3078-9450-a060cc1b3516 | -13.9713 | -56.7874 | 2025-05-13 14:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 8a0a49ea-dca8-3d90-95fe-ba43a574c1fe | -6.9804 | -42.7854 | 2025-05-13 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 5f13e5e8-0b4a-3ea2-b39a-9fa9c2239658 | -10.4883 | -46.1778 | 2025-05-13 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 66524142-04e6-3881-8519-6ae3b8a1f89d | -13.5683 | -52.8783 | 2025-05-13 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 92b15e31-9569-31ea-84b9-8097872e4172 | -10.4883 | -46.1778 | 2025-05-13 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 222b4834-2115-3319-b90b-09dd80d3d764 | -11.6952 | -48.0792 | 2025-05-13 14:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 2ff55c2f-c9bd-35db-b312-fcff5fac0c03 | -9.6634 | -49.7228 | 2025-05-13 14:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 33ec35fe-9dbe-3b3b-8873-1afd51b1c2cc | -11.9748 | -49.6838 | 2025-05-13 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 7475e197-b59c-37b4-9e08-3aae2bb9c988 | -9.6822 | -49.721 | 2025-05-13 14:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |


