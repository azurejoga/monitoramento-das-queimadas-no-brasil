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
| b52297d4-8987-326b-8326-847ffcef3b60 | 3.14675 | -61.00861 | 2025-10-20 05:29:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39c993ae-336f-33e1-9dc3-d784347d990e | 1.77638 | -55.70802 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54f1c105-7b24-3188-9bf7-647dbe2d3538 | 1.75745 | -55.7161 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ca12096-429c-39a6-a3e8-ab48560b71f9 | 1.82146 | -55.6678 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96baaf40-8e72-3b80-b96c-ab036aa1723a | 1.74138 | -55.91304 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| daee46f9-7ddf-3b9e-88c8-12e487a2231b | 1.71638 | -55.95677 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a24d7d72-fa4e-307d-8579-f73e71f97dda | 1.76849 | -55.70928 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 037807fe-8288-38a8-99f8-913c66430ffd | 0.96693 | -51.15935 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 094a9da4-fc9c-3ce9-8bf1-2d04d3231222 | 1.78033 | -55.70739 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 793b985e-728c-3e9b-b1a0-1c86c5921421 | 2.04224 | -55.76809 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5740f63f-4ba5-358a-af2e-219b3a9c66ed | 1.79217 | -55.70554 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87c7eb21-b3b2-37e7-be4b-8ebc3f703ebf | 1.74489 | -55.91072 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cd9d5453-3966-3ea4-9d25-cde978794431 | 0.98639 | -51.13873 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fa02864f-7724-3b23-949d-06a7e90fc7ad | 1.71022 | -55.76622 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f38748c0-5209-3b83-9cfb-7131c4fd6f3a | 0.99615 | -51.13001 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a169f39-cebf-3991-a746-b46582ad64c6 | 1.82215 | -55.66455 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a42d5399-0ee0-35eb-93c0-fba0f4d04f9b | 1.71667 | -55.76346 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11a21736-ff4a-313b-a3d0-3feaa6c6b3cd | 1.74921 | -55.912 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cdaa24e7-bea4-3c0f-8328-98fc45f977b7 | 0.9718 | -51.15195 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89e51553-f52e-371e-a539-ac7803f044ad | 0.87485 | -51.25574 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d213041b-3e48-3f54-bb2c-e0da752640ad | 2.04147 | -55.76318 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ea519e4-39a0-3449-a18c-ed8dae7a93b1 | 1.70708 | -55.77182 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 508be3c8-da47-393d-9b1a-85ab688e109e | 1.77244 | -55.70867 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8c5cddb-edd5-3fbc-9b45-e8c75c9b84f1 | 1.74528 | -55.91245 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1b657e17-cacf-39cc-bec3-26a2f9584fa1 | 1.72496 | -55.9355 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| d1def676-e0fa-3e86-87f8-6477f12b32db | 1.71337 | -55.7606 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a38e700-cae6-383a-8f51-d5cc0f272ced | 1.8261 | -55.66393 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d82811d-8309-3999-aa6f-cfac1ad3941d | 0.97126 | -51.15142 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ef6a328-f198-3b2d-84a0-60b109ad2f3b | 1.72885 | -55.93488 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 799f73ce-b1d6-383f-ac0d-ade9003ea831 | 2.04412 | -55.75592 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50056ae4-fd59-3657-91db-444bb1984d62 | 2.07066 | -55.72134 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cacc44c-68ac-3b0c-b96c-5ad17c331e61 | 1.74214 | -55.91787 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bc8f1d3c-cf31-38d0-83dc-b2c28e16c22d | 1.74881 | -55.91024 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 441de9ae-a75f-311b-b018-0cf13ae3f2be | 1.81127 | -55.67976 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dbfa3138-dfb4-357b-87b6-09931e93c7a7 | 1.08056 | -51.30756 | 2025-10-20 05:29:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 046fb54b-eb92-3261-89a1-4835f60bced5 | 1.78822 | -55.70618 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ad2d60c-facc-3b68-84f0-f2b6e293943f | 1.73785 | -55.74485 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 70210333-60e7-3b6d-912a-e28e8f0950da | 1.71585 | -55.75848 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 865de829-9294-3200-bf5e-4dcd0d686e67 | 1.73587 | -55.92877 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c96f0e9-7814-39bd-9b64-b3e1c270b72d | 1.82064 | -55.66278 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 101aa418-ecac-3afb-ba8a-18e1b026c4ba | 0.86071 | -51.12582 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92685870-c55c-3f0e-acff-09ee95fabff2 | 0.97671 | -51.15057 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a8758df-8e70-33e2-a9e0-614797a45651 | 1.70314 | -55.77244 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| af6daafe-8570-3e73-a462-72f95385afe4 | 1.72756 | -55.74812 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45c21a9a-0db2-374b-b5b7-3f755e548cba | 1.74567 | -55.9155 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ebeb3cc3-cb0e-3fc5-86ba-6e4ae5656c76 | 0.98153 | -51.14317 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e72f5c27-f477-3f49-b2c2-d73b95e83386 | 1.75037 | -55.72237 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e943622d-cd99-36aa-b550-d98053a39d4d | 2.04231 | -55.71743 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1baab0a5-8a41-3ae5-8c3d-891785df59c7 | 3.1434 | -61.00914 | 2025-10-20 05:29:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3891a39-49eb-34e1-83f4-19685809aec2 | 2.04155 | -55.71581 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48c2ea6d-eb6c-37aa-944a-eaeb2a2149f2 | 1.70629 | -55.76684 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d5d7d63b-5c94-3107-bba4-411c457916b0 | 1.73664 | -55.93363 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8df0777a-dfdc-3b85-9bbd-a91f4fdae7f4 | 1.73824 | -55.91848 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 887d772b-889a-34be-b2b0-8e704fe6f1aa | 1.7315 | -55.74749 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eca61ce6-22a0-3df7-8dcc-76db16271cbd | 1.74412 | -55.73367 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e204424-5ea3-38dc-ac84-ff4423f5a170 | 1.84438 | -55.65911 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96a98173-00a3-3f12-b0ff-5d9a510d28e0 | 1.08002 | -51.30416 | 2025-10-20 05:29:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b66aa5d2-5d48-33bd-b3e3-f75abfa47022 | 1.72026 | -55.95615 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69e4079f-05cc-3114-b1cf-f2dd4e932337 | 1.81582 | -55.67588 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78982b49-d0e9-3911-a55f-81b3ee9eed5b | 1.73511 | -55.92393 | 2025-10-20 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21bb769a-66cd-3908-b7a9-0c102817bab1 | 0.97725 | -51.15111 | 2025-10-20 05:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0da0aac0-ea7a-3ad4-9fd1-643c7486a2f2 | 2.04309 | -55.7224 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a910ddb-b750-36ae-a8c3-606c2a55c37d | 1.73391 | -55.74544 | 2025-10-20 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb432f22-344f-35ff-90a8-c59b5d161126 | -2.2527 | -51.9108 | 2025-10-20 05:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| b2967211-aaab-3637-af46-fd8c2fae5dc2 | 1.7118 | -55.7643 | 2025-10-20 05:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| cba3ee9e-55d2-3c7f-b0fa-49233661ef2e | -2.2507 | -51.91808 | 2025-10-20 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e0497129-e726-337d-b21e-a0601f7cadb3 | -2.0604 | -56.83477 | 2025-10-20 05:31:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3a27527-2862-314d-a259-da94aa569aa8 | -3.33514 | -50.22661 | 2025-10-20 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9455b55-ef1e-3840-a63b-18b5f2ceb6cf | -1.44488 | -49.30236 | 2025-10-20 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa677263-2fcd-3adb-bf49-97621ba44c56 | -2.25123 | -51.91462 | 2025-10-20 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f110d87d-956e-39b8-a2f0-954189bda779 | -3.50878 | -55.48372 | 2025-10-20 05:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32e8b4e5-082a-342c-83f2-db16749e5429 | -3.098 | -59.36897 | 2025-10-20 05:31:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f321451a-924f-3e31-8535-ee6d6b65f163 | -2.27193 | -51.92493 | 2025-10-20 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b113788-9fc9-3196-ba22-adf80e75e923 | -3.11712 | -59.11143 | 2025-10-20 05:31:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa52be81-ac0f-3a1e-8a48-307fcb27ecb2 | -3.50817 | -55.48786 | 2025-10-20 05:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6db2d140-39cd-3f33-a132-5b4a6dc5354e | -2.08336 | -56.9241 | 2025-10-20 05:31:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0cc3131-2f03-3b2a-825e-bbd72ef56b02 | -2.25228 | -51.90764 | 2025-10-20 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 530aede2-da31-30f6-b4be-62f19fc950ec | -3.32985 | -50.22491 | 2025-10-20 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ee743b0-3737-3d24-97de-fab244f61d02 | -2.0565 | -56.83421 | 2025-10-20 05:31:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77d377a5-1f89-3909-8bac-fd85c5420771 | -3.49547 | -55.47944 | 2025-10-20 05:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70e40e56-7223-395e-9681-a2e525d2b537 | -3.49982 | -55.48001 | 2025-10-20 05:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5661bf7e-26f9-3f78-8557-08bbed8cedc1 | -3.14459 | -50.25135 | 2025-10-20 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e20fb37a-fb1f-3ce5-b7d1-10c13a4737ba | -2.24632 | -51.91025 | 2025-10-20 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 053526a1-07b8-31c7-ab57-fb6604c8239f | -2.24579 | -51.91375 | 2025-10-20 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8ec57901-a8ba-3f41-81ab-c6e084c23482 | -2.91018 | -52.71626 | 2025-10-20 05:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| ab557c80-a570-34c4-bab1-196327bb518f | -3.50445 | -55.48303 | 2025-10-20 05:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fe5e860-bab2-3fe3-bc19-0835f559396e | -2.03028 | -56.61393 | 2025-10-20 05:31:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7f76be0-336a-3b37-9cfe-b3c9fca65c07 | -2.08167 | -56.92672 | 2025-10-20 05:31:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31996e31-8ff4-3909-9524-5f2288f15ecd | -3.50071 | -55.47824 | 2025-10-20 05:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ff92c3e-aca3-37ee-ac51-fb55b3e991cd | -2.91538 | -52.71711 | 2025-10-20 05:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 113c8cff-7772-3af6-9baf-1a132b9d32a6 | -1.63672 | -54.05316 | 2025-10-20 05:31:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7f5d72b-0abd-35f9-9fda-375c80bc97b9 | -2.91588 | -52.71384 | 2025-10-20 05:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a151f87-f0f4-3b38-b51b-6b08586225b0 | -3.32914 | -50.22952 | 2025-10-20 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cadbccc9-5ba9-3b11-8917-fe19d95f080f | -2.25615 | -51.9189 | 2025-10-20 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1795a6d7-0bde-342d-ad3a-c2735855467a | -2.8137 | -54.38079 | 2025-10-20 05:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25f03f14-c44c-3bb5-9272-ba897f974e4c | -3.32897 | -50.22563 | 2025-10-20 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19bea2f9-f225-3e80-ab95-5fe376da9143 | -2.25018 | -51.92153 | 2025-10-20 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 592ca772-f667-32db-b7ac-548b538dbd3c | -2.27246 | -51.92148 | 2025-10-20 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 059abd26-37f2-392f-848a-2d55fa688967 | -1.09147 | -54.13513 | 2025-10-20 05:31:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e37b64dc-3565-3a7f-88bd-af9b3f0aa509 | -2.25667 | -51.91546 | 2025-10-20 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README20.md)
