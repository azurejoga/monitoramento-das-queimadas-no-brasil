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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acf16dfc-35b0-32e5-816e-c7c491c2f396 | -11.4036 | -47.2511 | 2026-08-07 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 1380dbd0-64dd-3088-a77f-ed4f56c3c4a8 | -11.3103 | -44.8337 | 2026-08-07 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 202.6 |
| ffbd884a-b539-3be7-bce2-f98ee3cfc4bb | -9.2918 | -60.9228 | 2026-08-07 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 48bc52a0-4eb7-3caa-a7ed-e32a05ef4297 | -11.3099 | -44.8569 | 2026-08-07 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 75bc4763-9389-3e0c-b47c-56fbdb795296 | -13.7839 | -47.1779 | 2026-08-07 14:10:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| f76cb638-a4d4-3f8b-a095-534465042fe9 | -12.441 | -50.3602 | 2026-08-07 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 88359cd0-6b2c-3476-8cdf-96249486d3e7 | -11.2912 | -44.8365 | 2026-08-07 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 3ac5b695-2959-31a4-8d94-a54735f2e98e | -13.8236 | -53.7264 | 2026-08-07 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 58f5eac0-d8be-391c-b251-29dd549ef758 | -11.3107 | -44.8105 | 2026-08-07 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 399a3184-509c-3c72-b2a0-22ea8ade5c52 | -6.909 | -42.4372 | 2026-08-07 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| aff75114-c466-3278-9c61-3af6f735dce3 | -6.9092 | -42.4134 | 2026-08-07 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 07177fc8-9f00-371f-b92f-6b485b58a228 | -14.3434 | -54.9103 | 2026-08-07 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ea33c2d0-3612-33fa-accd-a92da165188f | -13.6978 | -51.9763 | 2026-08-07 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 0927ea02-6dfd-3d23-9645-891e4185c453 | -6.9791 | -42.9034 | 2026-08-07 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.0 |
| c50e581a-ae07-35c6-9d33-d66596882620 | -14.3232 | -54.9744 | 2026-08-07 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 84a8a850-d8f7-30ed-9ec3-3ef0c5cda1bf | -14.3627 | -54.9081 | 2026-08-07 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 491feb6d-f60e-325e-b599-9dba5bc7b6fd | -12.4601 | -50.3578 | 2026-08-07 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 7a80c3c8-9040-3799-b150-9cb16fd18b02 | -14.3232 | -54.9744 | 2026-08-07 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| ade351f0-c946-3687-865b-dfbf916180ef | -12.4789 | -50.377 | 2026-08-07 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 4c626cc2-706f-3f42-977a-8b37bec12674 | -8.5504 | -45.3817 | 2026-08-07 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| a7e41883-a06e-3165-9a3f-cb70a4a5f872 | -6.9702 | -43.6997 | 2026-08-07 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 84a8d035-de7e-37a9-986c-abbf2a3f826a | -6.8901 | -42.439 | 2026-08-07 14:30:00 | GOES-19 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| f8ff07c1-d4ed-3de1-b787-5b470d36e67d | -12.441 | -50.3602 | 2026-08-07 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| baa24ca2-5d8a-3d7e-9884-e9e3b8414b12 | -14.3434 | -54.9103 | 2026-08-07 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 80ddba09-6e74-3087-acef-0cb6578559a9 | -11.1453 | -54.9024 | 2026-08-07 14:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| f1a6bd55-802b-359b-9211-902c6466f6c8 | -11.2916 | -44.8133 | 2026-08-07 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 0bc10f10-c81d-30fb-975e-1b2e0823b7da | -9.2918 | -60.9228 | 2026-08-07 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e13011d8-5031-3845-98bd-371196f91ea0 | -11.3099 | -44.8569 | 2026-08-07 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 314.1 |
| 2ff6ad8f-a1d2-3742-97ee-ded5c11201b1 | -11.3845 | -47.2535 | 2026-08-07 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 6d81fde7-42f6-384f-9fdb-a3ffb5bbc6e7 | -11.2908 | -44.8596 | 2026-08-07 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 4307d7b9-a261-3386-95ab-84256e0b1356 | -12.4601 | -50.3578 | 2026-08-07 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| bd8d5e13-ad3d-3ab9-acf4-31e29d6ef459 | -11.2912 | -44.8365 | 2026-08-07 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 180.8 |
| a75cb495-8e56-339c-84c6-8d225c444f8f | -9.2918 | -60.9228 | 2026-08-07 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| b7067f61-a927-3dbc-aa46-8b98653362b5 | -11.2908 | -44.8596 | 2026-08-07 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| f0cae91b-64c7-3f03-b8ea-9bc220cdece1 | -11.2916 | -44.8133 | 2026-08-07 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 23781bba-baca-39b5-ae94-582054a7d8c0 | -14.3232 | -54.9744 | 2026-08-07 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 257.6 |
| eb77cba6-1c07-392d-b1de-1c6883067b97 | -13.8432 | -53.7033 | 2026-08-07 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| a25b8736-d635-3771-af8d-c60145c576b1 | -12.4601 | -50.3578 | 2026-08-07 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ffb7e51b-ceff-3dd0-8f3f-f409e13481c2 | -11.3845 | -47.2535 | 2026-08-07 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| d8fbbcaf-c803-3b21-b42a-926fd1f88172 | -11.2912 | -44.8365 | 2026-08-07 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| fd26916d-81e2-3f30-bc15-d91dc30faf94 | -14.3431 | -54.9309 | 2026-08-07 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| b52ce1bb-ac09-3384-a46c-d34ff8062333 | -12.441 | -50.3602 | 2026-08-07 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 2c9f2a85-ffb8-3bcd-8897-e3b0d526ee93 | -6.9092 | -42.4134 | 2026-08-07 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 0f161013-7b14-3584-bcad-c25429b864f6 | -11.3099 | -44.8569 | 2026-08-07 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 261.6 |
| ae26c701-8da4-32cf-ac21-95966b2f6e65 | -13.8428 | -53.7241 | 2026-08-07 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| b11c0170-8d12-3dee-86de-0712a5023199 | -11.4036 | -47.2511 | 2026-08-07 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| bb95ba79-9998-3397-9df5-566fd03d15b4 | -8.5504 | -45.3817 | 2026-08-07 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |


