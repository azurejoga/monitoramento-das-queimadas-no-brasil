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
| 7eb62802-b289-37ce-b7c7-df18ab9a318d | -12.6341 | -56.9926 | 2025-09-03 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 31d19350-4bbe-376f-8170-16a24831b001 | -15.5652 | -48.4143 | 2025-09-03 02:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 55.7 |
| f3a86e4a-66d1-3e59-8ec5-e59281f225d2 | -11.1228 | -44.6288 | 2025-09-03 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 223.7 |
| 0ba1524b-8c36-3811-a6a3-2c3911ff3db5 | -7.5476 | -61.3437 | 2025-09-03 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 62802a86-d12f-3397-b19d-a6cd922df04a | -4.8935 | -43.2115 | 2025-09-03 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 3e2848d7-4514-3dd0-af70-83a2c0c8455b | -4.1604 | -46.7881 | 2025-09-03 02:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a074e7f9-73d2-3647-a73e-950e22675c4d | -11.1033 | -44.6548 | 2025-09-03 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 5e2e4521-5ae9-3afb-bde7-bf80b60645a3 | -4.8933 | -43.2349 | 2025-09-03 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 6791d555-2c8f-39c1-9b9b-2c343a83d0e8 | -11.1224 | -44.6521 | 2025-09-03 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 224.9 |
| ba9dc9da-bcdf-3968-aff8-d601f2ae7946 | -11.6647 | -57.3533 | 2025-09-03 02:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 0f2ce121-3c48-3031-8b3d-edfb9f3c5ecc | -23.7196 | -51.764 | 2025-09-03 02:10:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 79.6 |
| f96fa099-a538-3d6a-9870-b56c1046d834 | -7.5477 | -61.3247 | 2025-09-03 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 1d122d05-395d-3c36-bd45-47bbc5f6511d | -8.3644 | -48.3116 | 2025-09-03 02:10:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 7e71c5d1-e228-3147-a63b-4bd5100c34fb | -3.212 | -47.1357 | 2025-09-03 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| d78cc373-baac-3afa-95aa-17901e106de4 | -11.1037 | -44.6315 | 2025-09-03 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 88741910-5165-388a-a0a6-83ff666bad19 | -11.6836 | -57.3518 | 2025-09-03 02:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 8eddb6e4-f652-3851-999b-010b90ae44d1 | -9.3394 | -55.2277 | 2025-09-03 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| c92a047b-dfbb-3b1f-95b3-c0bac98b44e3 | -3.2306 | -47.1131 | 2025-09-03 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| e012a49f-0684-3fa1-8b36-99564cba784b | -11.1033 | -44.6548 | 2025-09-03 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 3c966701-4c62-3e0f-890f-214250a45011 | -15.7175 | -53.6376 | 2025-09-03 02:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f75a30b8-2b8b-305d-becd-91284f416ed4 | -4.1604 | -46.7881 | 2025-09-03 02:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| df19e5b3-ba5a-3b67-9e8c-a6fbb4310bd3 | -4.8935 | -43.2115 | 2025-09-03 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 1b114f69-ee40-3d74-a304-3fc99f8ab59c | -18.688 | -52.7027 | 2025-09-03 02:20:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 6f990d3e-1164-31e6-8ec2-bef55ac3fdab | -11.6647 | -57.3533 | 2025-09-03 02:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 3fd9a7c6-b34b-3928-ac75-1229b8e52308 | -7.7226 | -48.7355 | 2025-09-03 02:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 84.2 |
| b1d6393d-1052-302d-99af-4939a667bff5 | -11.1037 | -44.6315 | 2025-09-03 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| be96af81-f61f-338b-b359-06b4426449b6 | -3.2306 | -47.1131 | 2025-09-03 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 35e525a3-32e5-3c90-99bc-ca6646fd9bcf | -22.1777 | -48.8368 | 2025-09-03 02:20:00 | GOES-19 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.6 |
| 55bf063c-82df-3972-88d0-8326d7c95413 | -11.1228 | -44.6288 | 2025-09-03 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 334.5 |
| 7e45a293-1af7-3e4c-bf44-8bf446eae9f4 | -11.1224 | -44.6521 | 2025-09-03 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 434.7 |
| 1293b750-ee12-3054-979f-abb4b5fa7dd7 | -19.8519 | -45.6824 | 2025-09-03 02:20:00 | GOES-19 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 89.1 |
| f75a8d53-ea43-3575-9f44-e0dc36d8d28c | -19.8242 | -49.6376 | 2025-09-03 02:20:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| 548de528-a077-30a0-8f69-68a1c37ff4dc | -12.9189 | -57.0074 | 2025-09-03 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| ac8cdb1c-ee53-3b06-ad59-fb7cb02fa1ec | -12.9573 | -56.9839 | 2025-09-03 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| e4bcc01a-6082-311c-957e-9bcf3a51ca6d | -3.2305 | -47.135 | 2025-09-03 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 9f76e786-6297-3d15-a199-7ccb42fec32a | -12.9387 | -56.9454 | 2025-09-03 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 632a0e5f-0010-3b53-b740-dd781e53fb01 | -22.1784 | -48.8134 | 2025-09-03 02:20:00 | GOES-19 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.3 |
| 42895963-4c3e-3c0a-bce0-60ddeadb794f | -4.912 | -43.2337 | 2025-09-03 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 5cceffab-9277-3855-8501-6556af2c7f5c | -11.122 | -44.6753 | 2025-09-03 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 14083088-761a-3b28-afdf-f87a58af7ad9 | -7.7039 | -48.7371 | 2025-09-03 02:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 73.5 |
| f7dc32dd-9064-3e2a-95c0-60a04a518227 | -7.5476 | -61.3437 | 2025-09-03 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 6adfa58d-6a49-37ad-b67a-c8f69fc1caa3 | -12.9385 | -56.9655 | 2025-09-03 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 099cff0d-480b-3ce8-b1cd-26fa86aead23 | -7.7224 | -48.7572 | 2025-09-03 02:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 31.0 |
| ade31326-118f-3537-b868-d198b6a2f3d2 | -12.9382 | -56.9856 | 2025-09-03 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 46963379-69bd-3c4a-a202-732075a4dc04 | -7.7036 | -48.7587 | 2025-09-03 02:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 02d9dbd4-7dcd-34a9-9b91-94682be6a7de | -12.6341 | -56.9926 | 2025-09-03 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| a8579ce2-7cab-34bd-915c-37aa597c775f | -3.212 | -47.1357 | 2025-09-03 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| dc03cc14-d89f-34b6-83f2-274c8ef9e7f6 | -4.9122 | -43.2103 | 2025-09-03 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| f7f59376-b83f-305c-b7a2-f113b2570c10 | -19.8445 | -49.6334 | 2025-09-03 02:20:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.0 |
| 54c5e155-acbc-38f8-8f8f-17260a9ed171 | -9.3394 | -55.2277 | 2025-09-03 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| fa706b30-4228-32f1-b23c-71aeb02a3944 | -3.2121 | -47.1138 | 2025-09-03 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a7e962b6-37aa-3725-9a9e-aaf842519e65 | -11.6836 | -57.3518 | 2025-09-03 02:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 54080380-8260-3c60-850c-e4fdaf3fb2fb | -4.8933 | -43.2349 | 2025-09-03 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 94a9f9f9-879d-30d1-ad39-641ebda36d55 | -4.8935 | -43.2115 | 2025-09-03 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 2dcbb86f-9264-3681-ab9f-0c787f4d4d9e | -12.9573 | -56.9839 | 2025-09-03 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 20edf780-c74c-3172-91da-b1640caccf8f | -11.142 | -44.6261 | 2025-09-03 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 1a470bc7-a3cb-3368-9648-c528c434ae10 | -7.7039 | -48.7371 | 2025-09-03 02:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 101.5 |
| babd863f-0ef2-3e9e-8e81-5f2b661dc25c | -12.9002 | -48.0936 | 2025-09-03 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| cfbd31a7-068a-3f85-bd88-a1d3db1a3a27 | -7.7226 | -48.7355 | 2025-09-03 02:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 82.7 |
| e69528cf-01b1-31c5-b219-bec9cbf9aad1 | -3.212 | -47.1357 | 2025-09-03 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| afc814e1-1249-37ed-b856-535685cb833b | -11.1033 | -44.6548 | 2025-09-03 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 407c160f-afe6-32e5-b5dd-d7f671e34e00 | -3.2305 | -47.135 | 2025-09-03 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 8a37ef8e-2293-3bb3-ae8f-eb5bf2e4f8e7 | -11.1416 | -44.6494 | 2025-09-03 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 8806450b-f0af-39d5-8f26-ccfb32db1b20 | -15.4616 | -49.6524 | 2025-09-03 02:30:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| ae84acd7-6930-3fdb-b738-24530c65b9a4 | -4.9122 | -43.2103 | 2025-09-03 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 65d9c895-fe37-3c75-a05b-e3687bcacebe | -15.462 | -49.6303 | 2025-09-03 02:30:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| fca4da24-9935-31d1-87b3-e16b7df575c9 | -22.1777 | -48.8368 | 2025-09-03 02:30:00 | GOES-19 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.7 |
| a756ca40-07b7-3ca7-8b5e-d995b7822551 | -12.9385 | -56.9655 | 2025-09-03 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 51192acb-a5de-3578-b6f2-976eddba8bcd | -9.3394 | -55.2277 | 2025-09-03 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 14966f74-9280-3a0c-9479-a1711fd3b5a8 | -11.1037 | -44.6315 | 2025-09-03 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| d36f2003-03f3-391f-93fc-8004dda500fd | -11.1228 | -44.6288 | 2025-09-03 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 264.0 |
| b7ad1f47-5152-396e-ad30-ea1116ccb2b2 | -4.8933 | -43.2349 | 2025-09-03 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| dba65767-7ae7-3afd-88a8-0fa602773df6 | -12.9387 | -56.9454 | 2025-09-03 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 15755f12-db4b-3184-988d-69bf8c73d7a5 | -11.6647 | -57.3533 | 2025-09-03 02:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 5331245a-bd9d-395f-8b25-66c905420f26 | -12.9189 | -57.0074 | 2025-09-03 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 376e5ca9-e8be-33ad-b265-30c5d3d2afef | -11.6165 | -52.0689 | 2025-09-03 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 547d7ae7-e666-3af1-ae03-a46dc20c3a24 | -4.1604 | -46.7881 | 2025-09-03 02:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 29a9e1b5-9089-32f8-a785-dde66898034f | -3.2306 | -47.1131 | 2025-09-03 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 16266038-fe59-3c6f-9bec-02797d583f8c | -12.9575 | -56.9638 | 2025-09-03 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| d948b391-4594-3aa7-a27f-b04da5b589f2 | -12.9382 | -56.9856 | 2025-09-03 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| affe4152-ff7b-3dab-bd95-628d90617a6d | -7.5476 | -61.3437 | 2025-09-03 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 7215e4ca-3789-3bf8-b373-7c8890d3987b | -6.1667 | -43.3039 | 2025-09-03 02:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 39.9 |
| 798ad11a-59fd-3678-82ce-e0cbb73cbc9c | -6.1665 | -43.3273 | 2025-09-03 02:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 36d2c8fd-653d-3a11-b4d2-efdc106be25e | -3.2121 | -47.1138 | 2025-09-03 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| adfca154-0df6-3a2b-9482-1c7d27ab9bfe | -11.6836 | -57.3518 | 2025-09-03 02:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| cdf86732-09ca-33c6-94d3-6bb6e86d925b | -7.7036 | -48.7587 | 2025-09-03 02:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 00fd6620-4941-3449-ac00-b9a9393575e1 | -11.1224 | -44.6521 | 2025-09-03 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 374.7 |
| 294f4f1a-92d9-3200-b82d-dd1b029530a4 | -3.2121 | -47.1138 | 2025-09-03 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 4255a5a2-ecb9-384d-a8b9-a10c3b574477 | -7.7039 | -48.7371 | 2025-09-03 02:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 05394fa6-a3a1-31c8-b9ff-30a4298b84ec | -10.5409 | -50.4256 | 2025-09-03 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 5427aa42-261f-376c-bca3-3f934e2d901e | -7.7226 | -48.7355 | 2025-09-03 02:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 5c187a00-5e2c-3351-bfaa-1a1759fc671d | -11.1228 | -44.6288 | 2025-09-03 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 244.5 |
| 438ca345-8e29-368e-a7aa-0efb28eb5809 | -22.1777 | -48.8368 | 2025-09-03 02:40:00 | GOES-19 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.3 |
| 69f66b72-2a29-380a-8f76-574f84407806 | -3.2305 | -47.135 | 2025-09-03 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 75b66fb4-c699-3f11-ba1b-9ff9d5c92208 | -11.1033 | -44.6548 | 2025-09-03 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| eb526b8c-31d6-311a-826d-58b1bde680c0 | -12.9382 | -56.9856 | 2025-09-03 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 7a6ca1e4-8b0e-3e35-851e-c3fe6d41b945 | -22.1784 | -48.8134 | 2025-09-03 02:40:00 | GOES-19 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 97.5 |
| f73b7f58-9b21-30d7-baf0-e6665b74967c | -4.9122 | -43.2103 | 2025-09-03 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| ac8a0fce-421f-3285-a3e5-c05f9332e0fa | -11.1037 | -44.6315 | 2025-09-03 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| dc79736a-5ef7-3329-b6cb-e3cefbb5163a | -3.212 | -47.1357 | 2025-09-03 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |


[Clique aqui para ver as próximas entradas](README20.md)
