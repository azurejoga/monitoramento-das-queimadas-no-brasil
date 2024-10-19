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
| 7a7e96ac-19ee-3c27-9536-c717c918860f | -4.5528 | -48.013 | 2024-10-19 00:35:36 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f898ae85-7156-33b4-96b5-d0b8f05280c9 | -4.5545 | -48.020802 | 2024-10-19 00:35:36 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 636b4bcd-00db-3c2b-97b3-1a5b24532696 | -4.5563 | -48.028599 | 2024-10-19 00:35:36 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9bdfb6f-2fc2-3870-b48a-0d20c116a699 | -4.4269 | -47.774502 | 2024-10-19 00:35:38 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 041e95f7-38ca-37cd-842e-40884667d6eb | -5.0153 | -50.4487 | 2024-10-19 00:35:38 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 266a6224-8937-3a25-b00a-2fb882311dd3 | -5.0177 | -50.4594 | 2024-10-19 00:35:38 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb8b82b3-36ab-3e19-bb57-b7f540c5db74 | -4.3083 | -47.705399 | 2024-10-19 00:35:39 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca516408-66ae-3622-aa6e-497435fcdc50 | -4.0217 | -46.941399 | 2024-10-19 00:35:41 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 52e4d7f2-34c3-317c-a45c-426560285a00 | -4.0233 | -46.948502 | 2024-10-19 00:35:41 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 91048763-ea0b-3a60-84ba-59f5342328c0 | -4.2527 | -48.005901 | 2024-10-19 00:35:41 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74bce6c5-1acf-3f8d-8518-a9b09edade54 | -4.2544 | -48.013599 | 2024-10-19 00:35:41 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa17db2e-b97b-3d6e-b5be-1961153372e5 | -3.6914 | -45.9006 | 2024-10-19 00:35:43 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9d19895c-64f4-3913-b0c3-27ad62951ec8 | -3.693 | -45.907398 | 2024-10-19 00:35:43 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64b1965c-b97a-3508-bcca-071e4c842743 | -4.5397 | -49.6488 | 2024-10-19 00:35:43 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56d56eed-1989-3d76-8f15-59eb7c34ba47 | -4.5418 | -49.658199 | 2024-10-19 00:35:43 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfb5c7e2-e19e-3b7a-9de8-6d8be0ceb2a6 | -3.2242 | -44.4067 | 2024-10-19 00:35:45 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffeea83c-c7dd-3482-88cc-936eb6756e80 | -3.2259 | -44.413799 | 2024-10-19 00:35:45 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a75301d8-4c79-33d0-a4ce-e693226e5c15 | -4.3881 | -49.751301 | 2024-10-19 00:35:45 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f56917c-03c3-3e48-91f8-797bafdaf8eb | -3.4116 | -45.9846 | 2024-10-19 00:35:47 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3473e1a1-f8f0-31e1-9e73-2b1f231b3a68 | -3.9091 | -48.352699 | 2024-10-19 00:35:48 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19f1e25b-bcee-3dee-9169-f6522eb7ff48 | -3.9109 | -48.3606 | 2024-10-19 00:35:48 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38b8baad-c594-3d87-8cad-c2d13f5ca816 | -4.397 | -50.526699 | 2024-10-19 00:35:48 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee82e570-c429-3c60-9d08-82242b578747 | -4.3994 | -50.5373 | 2024-10-19 00:35:48 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81a5d4a6-fe4d-3681-b823-434a1af52618 | -3.8957 | -48.338902 | 2024-10-19 00:35:48 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac9b8a2-24c9-39d2-bb00-b28a9a71eb11 | -3.9011 | -48.362701 | 2024-10-19 00:35:48 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d64c7f27-70f3-3757-8e10-d22a2b6a1a1c | -4.3873 | -50.5289 | 2024-10-19 00:35:48 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 837c7953-c438-3587-b6d1-4d74868b01a7 | -4.3897 | -50.539501 | 2024-10-19 00:35:48 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52ce81fc-2906-34c4-90b8-c7beec8c1d2b | -3.8842 | -48.333199 | 2024-10-19 00:35:48 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1d2d5c5-11bf-362d-b0c5-1fd74cd0c140 | -7.6815 | -47.3213 | 2024-10-19 00:35:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 474f9c36-1c7c-3a95-8686-c21ce82f6ed1 | -7.6391 | -73.1162 | 2024-10-19 00:35:50 | GOES-16 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 9b9d9497-3c17-3d1f-8f47-b4bfe682528a | -4.3057 | -50.8069 | 2024-10-19 00:35:51 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a0bd5f7-d7a4-3a4e-88f1-4952f29b7777 | -3.2624 | -46.233398 | 2024-10-19 00:35:51 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c991eb59-6cbf-3b5e-885e-ee69ff2a4e2a | -3.2639 | -46.240299 | 2024-10-19 00:35:51 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0784c99f-8fad-340c-91f7-8e082c829eb2 | -3.0727 | -45.945599 | 2024-10-19 00:35:53 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3b13d19b-552b-3e58-a143-7ceb4a9ca835 | -3.0743 | -45.9524 | 2024-10-19 00:35:53 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ae2e4cd-b1c1-3497-9183-ea117a0e96d7 | -2.9848 | -45.6073 | 2024-10-19 00:35:53 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ca86b6e5-93a3-3b28-97f0-7f30e80b1d89 | -2.9864 | -45.614101 | 2024-10-19 00:35:53 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c866f0d4-f009-3e3e-9451-594c8fcfa03b | -3.2897 | -46.9851 | 2024-10-19 00:35:53 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5e87a0b-6cc7-30ee-915e-4edbf05ea03f | -3.2913 | -46.992199 | 2024-10-19 00:35:53 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5adaf2fb-1dbe-33a5-ae1d-50db7ea6ab13 | -3.2929 | -46.999199 | 2024-10-19 00:35:53 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d588270-e59d-3922-887b-5422b30fe716 | -3.2993 | -47.027401 | 2024-10-19 00:35:53 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caaa769e-b149-3625-8dbd-bc6aef43a052 | -3.301 | -47.0345 | 2024-10-19 00:35:53 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa12501-5d1d-32cd-bca2-73eb29a4bfd6 | -3.4454 | -47.669102 | 2024-10-19 00:35:53 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b523d9ee-8eda-3719-9c61-53061727ed4a | -3.447 | -47.676498 | 2024-10-19 00:35:53 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56173e1e-7d88-34a4-b27c-7c61bb44ccf8 | -3.2895 | -47.029598 | 2024-10-19 00:35:53 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deeb8cbe-e03f-317f-8f16-5ca61eeb4364 | -3.2912 | -47.036598 | 2024-10-19 00:35:53 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e0424a2-412c-33aa-8922-8e3aec63eb0f | -3.2957 | -47.1922 | 2024-10-19 00:35:54 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d3b3b7e-7f46-32e1-8200-6577f876fd81 | -3.2973 | -47.199299 | 2024-10-19 00:35:54 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8724ffa9-8e62-3e15-9114-b22a5663a8fc | -3.299 | -47.206402 | 2024-10-19 00:35:54 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c36fc72b-3b90-3d04-8ca3-7016851759d1 | -4.1517 | -51.2197 | 2024-10-19 00:35:55 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39ed671a-404b-3e19-ab3b-646a7ac19721 | -4.1543 | -51.2314 | 2024-10-19 00:35:55 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61f74f8b-3cbc-347f-83a8-ff4677b63785 | -2.8279 | -45.4632 | 2024-10-19 00:35:55 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d5deca3-b1b7-375e-b52e-3c6b98ea8f1e | -2.8295 | -45.4701 | 2024-10-19 00:35:55 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e80e3aa-3dd4-3664-a00b-809e822a450f | -2.8181 | -45.465401 | 2024-10-19 00:35:55 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 577a6abe-f64d-34a2-a398-e53b03ecf234 | -2.8197 | -45.472301 | 2024-10-19 00:35:55 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2c7d3776-90e3-3df0-ba2b-04ec0ed6cf61 | -2.8213 | -45.479099 | 2024-10-19 00:35:55 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6fd3884a-53c3-3851-9afd-26e3e0476bab | -4.0566 | -50.9771 | 2024-10-19 00:35:55 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec701868-37da-3265-92f9-3b432fe0104a | -4.0591 | -50.9883 | 2024-10-19 00:35:55 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84061b61-3a26-3e11-885a-fe804ca5605f | -3.5688 | -48.940601 | 2024-10-19 00:35:56 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b4aa64a-afe9-3efd-b93e-b4c641b404f4 | -3.5706 | -48.949001 | 2024-10-19 00:35:56 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9e1f9ae-806e-3b47-ae60-0a6e683c26be | -2.7707 | -45.4832 | 2024-10-19 00:35:56 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 88d345fb-53fd-3f5b-8869-a9b52c788e39 | -2.7777 | -45.6035 | 2024-10-19 00:35:56 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8912262b-9494-3ff3-a0dc-2aac4458dc28 | -3.8342 | -50.074001 | 2024-10-19 00:35:56 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 945cd9d8-a8a1-3c1b-8b67-f1be0493dd6d | -3.8364 | -50.083801 | 2024-10-19 00:35:56 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d43f04e9-a801-324b-9e85-d0f9ce2b0929 | -4.0602 | -51.130699 | 2024-10-19 00:35:56 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4750053f-ffdc-3499-9e36-cf2b9c8aa8ca | -4.0627 | -51.142101 | 2024-10-19 00:35:56 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48038c10-fd05-3d9f-80ee-0f7f29828e89 | -2.7722 | -45.490002 | 2024-10-19 00:35:56 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a6b6dafb-32f6-3d48-ad57-dc868b1553b9 | -2.7738 | -45.496799 | 2024-10-19 00:35:56 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aeb103aa-2dd6-3297-be37-368db89a1244 | -3.8545 | -50.2561 | 2024-10-19 00:35:56 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71965919-1f1f-3856-a1a1-6edd22264149 | -3.8567 | -50.266102 | 2024-10-19 00:35:56 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bb10a90-f650-3ab7-b290-5e430434e189 | -3.6858 | -49.825298 | 2024-10-19 00:35:57 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a67dd184-7873-35cb-ad2e-5498fa326067 | -3.6879 | -49.834702 | 2024-10-19 00:35:57 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f0eff68-c780-3845-9c81-af48f5f2aa27 | -9.0344 | -67.4641 | 2024-10-19 00:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| fc0cd18b-c6ab-3786-98f7-7819589e5a50 | -9.0345 | -67.4455 | 2024-10-19 00:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 2bd22bef-aa23-3b2d-a5db-e9b1e933a85a | -9.053 | -67.4636 | 2024-10-19 00:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 2652e280-a215-352b-a091-70214eb10266 | -9.053 | -67.4451 | 2024-10-19 00:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 21b3b9fc-d587-37f9-b44a-4cd2698cd983 | -2.7463 | -45.961201 | 2024-10-19 00:35:58 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 720cc528-63b1-3113-85ad-2540b4a41b4f | -2.7479 | -45.967999 | 2024-10-19 00:35:58 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b9a43235-7403-34c3-8603-315a2537b641 | -3.4421 | -49.245399 | 2024-10-19 00:35:59 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39e38329-a18f-3e91-9667-1911fe47c485 | -2.6457 | -46.062401 | 2024-10-19 00:36:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26caf18d-a8f2-3334-b3d3-012cbadaa81e | -2.6473 | -46.069302 | 2024-10-19 00:36:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 79a43d21-78e9-39fc-845d-d5090c9c7129 | -3.7962 | -51.187901 | 2024-10-19 00:36:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d81b579b-d148-3551-b05a-3915b93757fd | -3.2054 | -48.608002 | 2024-10-19 00:36:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b43836bf-a4f5-37f3-9742-b3b61294190c | -3.1956 | -48.610199 | 2024-10-19 00:36:01 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb1bcb8b-4ff6-3e6f-b229-6526e1ccebb5 | -3.1974 | -48.618198 | 2024-10-19 00:36:01 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e94cec0-9314-3255-a3da-0aab0691b8c4 | -3.7687 | -51.339401 | 2024-10-19 00:36:01 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8a6e54e-5b18-3a0d-8af6-671821ef2133 | -3.2508 | -49.0811 | 2024-10-19 00:36:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb5018e3-a3d4-3e34-a1f1-79701862a47f | -3.2527 | -49.0895 | 2024-10-19 00:36:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13b9b6f4-caba-38ec-8c20-6ff33b23c928 | -3.5887 | -50.581402 | 2024-10-19 00:36:01 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 326a6ad0-6ed8-325e-8bd8-739e9c894f9f | -3.591 | -50.591801 | 2024-10-19 00:36:01 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f499e4c-676c-3f16-b37e-a5db91518643 | -3.705 | -51.100498 | 2024-10-19 00:36:01 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8144f56f-5c07-3ab9-be0f-5b9d05847beb | -3.7076 | -51.111801 | 2024-10-19 00:36:01 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a648780-28b1-3a83-9e36-d74500084a34 | -3.5789 | -50.583599 | 2024-10-19 00:36:02 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4ca8a89-71c6-3144-99fe-1ec2deb1c4cd | -3.6927 | -51.0914 | 2024-10-19 00:36:02 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f1450d5-4347-3e65-b292-94b5cae21a42 | -3.6952 | -51.102699 | 2024-10-19 00:36:02 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35c40b92-8e54-3dea-aeb4-eb68c71260ae | -3.6978 | -51.113899 | 2024-10-19 00:36:02 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14ace370-e878-3cc6-ab5c-1be4dfefbd0d | -3.7003 | -51.125198 | 2024-10-19 00:36:02 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10431541-1571-3505-a696-d900a77d6c1e | -2.4963 | -45.995602 | 2024-10-19 00:36:02 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fc2e0ae7-5282-3a8d-98b0-7d18dadd0247 | -2.4979 | -46.002399 | 2024-10-19 00:36:02 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d206f941-b5b5-3b4b-9687-4ec1e13cd803 | -2.95 | -47.9818 | 2024-10-19 00:36:02 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
