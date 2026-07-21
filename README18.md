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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a512b3b-1465-3489-9b7e-12e4857ca6ee | -7.6188 | -49.7522 | 2026-07-21 14:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 3f0c29ba-c5a6-3c31-ba9c-4e9da6fe5666 | -11.2259 | -50.1807 | 2026-07-21 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 5f9b944b-57f3-3007-9941-5994fe7befa9 | -7.6375 | -49.7507 | 2026-07-21 14:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| b8ee9af4-39a6-3368-980b-d7bf4ded621a | -10.3807 | -48.3254 | 2026-07-21 14:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 54f9d05b-0596-351d-a7ee-e9305c85cdbe | -12.533 | -48.2555 | 2026-07-21 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 871ed0c1-2f00-3384-a38b-3f8398e41b8d | -12.5138 | -48.2581 | 2026-07-21 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 505f900d-309f-3c81-b252-d93cc43438f3 | -12.0925 | -53.334 | 2026-07-21 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 776ec831-c2d2-3bfa-b261-ca7d49a1f85b | -13.3202 | -51.5986 | 2026-07-21 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 1741a015-7fb5-3cc3-9ac5-a50edbd2c25b | -12.533 | -48.2555 | 2026-07-21 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 180470e6-257f-36f2-b99f-4eed61ff3d1f | -12.5138 | -48.2581 | 2026-07-21 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 01910264-4d10-34a8-98f0-10d20862b32e | -10.6373 | -50.2874 | 2026-07-21 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 6f0bba84-426b-3c03-890b-52d81af8f084 | -13.3394 | -51.5963 | 2026-07-21 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 7ab23c44-7e95-3f59-b517-fe20fd90b885 | -10.8623 | -50.4344 | 2026-07-21 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| dbc6d828-978b-3f82-893e-7bd654e4327f | -12.5138 | -48.2581 | 2026-07-21 14:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 1f62dc13-d3b5-3e17-9246-75da0765e0fc | -10.8816 | -50.411 | 2026-07-21 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 220126e2-3a35-34c4-a8d6-5bc107ec6c72 | -13.3394 | -51.5963 | 2026-07-21 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 4631c257-0410-3bd3-8a37-02e054d53da7 | -12.533 | -48.2555 | 2026-07-21 14:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 839d612f-984e-3e0f-b65c-454f91b17361 | -13.3202 | -51.5986 | 2026-07-21 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| e644f794-982d-3180-9610-9ecd28455713 | -7.6375 | -49.7507 | 2026-07-21 15:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 1c17e356-a26b-3e20-bb11-615371100494 | -12.533 | -48.2555 | 2026-07-21 15:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 6f5c3b69-f3ec-31c5-b83d-da2b68bbf7c2 | -10.637 | -50.3088 | 2026-07-21 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 686b9b35-d5b0-31ad-acc3-2609d9c1ef0b | -10.6373 | -50.2874 | 2026-07-21 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 155.7 |
| ee3874c9-fa9b-3898-95df-27204a8cd961 | -9.6214 | -47.1751 | 2026-07-21 15:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 2c42381f-ef1e-301d-8e21-3da644edaa75 | -12.0925 | -53.334 | 2026-07-21 15:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 5b5f4b93-23df-3c5b-b884-7e326a987424 | -12.5138 | -48.2581 | 2026-07-21 15:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| a7347540-99c5-325c-bed4-fb8d793e83f3 | -10.8816 | -50.411 | 2026-07-21 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 5fad50b7-97fd-3f56-963c-8cea6fc9a7bb | -10.8623 | -50.4344 | 2026-07-21 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 4b390ae4-6877-3f57-9e55-73ed1abdefcc | -10.637 | -50.3088 | 2026-07-21 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 5914335d-497d-3e1b-9bfe-5e479abb51a8 | -12.5138 | -48.2581 | 2026-07-21 15:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| d858c403-f276-390b-9012-ab8af63c39d0 | -10.6373 | -50.2874 | 2026-07-21 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 95753624-8644-3a8e-9449-15bea59e3671 | -9.6214 | -47.1751 | 2026-07-21 15:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| af209260-55e6-32af-b7be-d4f0bdec781a | -12.533 | -48.2555 | 2026-07-21 15:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| fb25c150-adec-3fce-83e5-6a04bef82990 | -13.3202 | -51.5986 | 2026-07-21 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| b09663f4-4745-3efa-8184-3a4b5a237b46 | -13.3394 | -51.5963 | 2026-07-21 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 39b4b247-16fd-3101-9464-2a079df4eeb8 | -10.6373 | -50.2874 | 2026-07-21 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 9df2b5c6-0ffa-3349-8163-d29cab338ac5 | -12.0925 | -53.334 | 2026-07-21 15:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 80c8fa45-6b8a-39ba-b83d-927bc1ebc562 | -12.533 | -48.2555 | 2026-07-21 15:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| b1474a5f-c8ce-3067-890b-5d3a215fa9ab | -10.5429 | -50.2759 | 2026-07-21 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| db2dbe8f-43ce-3b3b-a9b7-ecc9f7a815d7 | -13.3394 | -51.5963 | 2026-07-21 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 6ba6a930-0f39-3d6a-8803-558bc7e2bfd8 | -10.6373 | -50.2874 | 2026-07-21 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 2836667a-6ac6-3083-baad-c5a02a6fcfc3 | -11.3997 | -47.4966 | 2026-07-21 15:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 1a25787a-a5ba-3722-8609-1d7517b9dc7f | -10.8623 | -50.4344 | 2026-07-21 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f24790ab-c549-3b7c-b5bf-299e7ae39d94 | -12.533 | -48.2555 | 2026-07-21 15:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| fe095fc5-9a4e-3a3a-bda6-df741a89ec0d | -10.6562 | -50.2854 | 2026-07-21 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 2c37c7d8-07b7-32d7-959b-7d22145edba3 | -10.6559 | -50.3068 | 2026-07-21 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| a6376a45-e8e9-3a0f-a68b-dbd640cee54d | -11.3997 | -47.4966 | 2026-07-21 15:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| c30d6e0a-89a5-37ae-a73c-2e7cf1905ce3 | -10.6373 | -50.2874 | 2026-07-21 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| d653303a-bad5-3fec-bbc7-d5bcaff4b27a | -12.533 | -48.2555 | 2026-07-21 15:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 3e0f695d-f788-3205-ab5e-622e455d80d3 | -10.637 | -50.3088 | 2026-07-21 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |


