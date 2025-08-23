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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec9d7d86-f15e-363f-ad1e-c7fcbdd979cb | -5.7429 | -57.6009 | 2025-08-23 11:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| bb91f6f0-b3b0-3e6c-a7bc-1db2ba6b4622 | -7.0352 | -44.6396 | 2025-08-23 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 75db7ce0-f0e9-3ef9-aa22-789bfac1e4e3 | -14.0842 | -43.9103 | 2025-08-23 11:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 53a94c71-3987-3fae-a9bc-78d1ba7db06b | -7.6296 | -45.2464 | 2025-08-23 11:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 81286f00-eb9c-3d65-9131-2111434bb0a0 | -5.7431 | -57.5814 | 2025-08-23 11:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| c5917803-79c7-3a1f-8418-42f2aefe8637 | -7.0352 | -44.6396 | 2025-08-23 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 48a28378-f6a4-38aa-9616-a905f7d4cbb6 | -7.0164 | -44.6413 | 2025-08-23 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 5ae6e4bf-5cd8-3beb-b46c-4bdc94277f01 | -5.7431 | -57.5814 | 2025-08-23 11:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| e880d972-c007-36af-b55d-774ef4bc071d | -7.0164 | -44.6413 | 2025-08-23 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| d96bfb0d-7593-3184-ae4d-ecf6efc6cea3 | -5.7429 | -57.6009 | 2025-08-23 11:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e9d3e7a2-af74-3a77-9c24-fe6e2024f6e4 | -14.0842 | -43.9103 | 2025-08-23 11:50:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 5f46b63b-4a28-325e-b60c-b09742295323 | -5.7615 | -57.5807 | 2025-08-23 11:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 78d81da1-869e-3773-a3fb-7b1b35ba114d | -6.1416 | -43.9563 | 2025-08-23 12:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 4e7c47d5-7a8b-34b1-aad7-af45696a47af | -14.0842 | -43.9103 | 2025-08-23 12:00:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 29b90f3f-234a-32f5-a093-99bd641247a2 | -5.7429 | -57.6009 | 2025-08-23 12:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 7a19f6b0-70b1-3861-8fee-afc93145002c | -6.5578 | -45.4757 | 2025-08-23 12:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 143.5 |
| ec6b9cfb-7bf7-3382-996c-28a03734b86f | -7.0164 | -44.6413 | 2025-08-23 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 3be9214a-9478-39db-aa2d-50a226e1c639 | -7.0352 | -44.6396 | 2025-08-23 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| b6e292f7-2a2d-352f-84f4-244b577b8e46 | -5.7431 | -57.5814 | 2025-08-23 12:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 51c0560b-db4a-3389-9505-cab4e29596ba | -6.558 | -45.4531 | 2025-08-23 12:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| e3e16577-961e-3dfa-9bae-7192f6e3a5ee | -6.5578 | -45.4757 | 2025-08-23 12:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| a7fbfbd1-1be9-3556-a2ad-3d2f541a90be | -14.0842 | -43.9103 | 2025-08-23 12:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| a4a32de5-227e-3315-b935-8895f09746f7 | -6.1416 | -43.9563 | 2025-08-23 12:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 9df4f6cb-840c-3e80-be05-703365aaffdd | -5.7431 | -57.5814 | 2025-08-23 12:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 03773c3e-41ed-3d97-aa1a-c74b38500898 | -5.7615 | -57.5807 | 2025-08-23 12:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| fdde4b81-2994-34c5-974d-bd4fa6d33beb | -6.5856 | -44.564 | 2025-08-23 12:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 8105454c-9aac-385e-b734-b44978c770b2 | -5.7429 | -57.6009 | 2025-08-23 12:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 6b0cb1bc-d8c9-3a75-955b-033a8637f2c3 | -14.2936 | -58.5249 | 2025-08-23 12:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 416b53c4-6bb4-3740-886e-fabfc3c22cb7 | -7.0352 | -44.6396 | 2025-08-23 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| fa444e6e-b0d0-3c0a-935e-eb92433a74fd | -7.0164 | -44.6413 | 2025-08-23 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| bf5b3d5e-82b0-3f49-bd38-8ecdfb9598a3 | -5.7429 | -57.6009 | 2025-08-23 12:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 381f254c-dc7a-3ee3-9535-090620fe2dfd | -7.0164 | -44.6413 | 2025-08-23 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 3f0302e3-dec4-3f57-8bae-26f56b272e6d | -14.3128 | -58.5232 | 2025-08-23 12:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 771ed6fd-a5b5-31ec-aeb8-c95777ab1244 | -14.2936 | -58.5249 | 2025-08-23 12:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| abcc967d-d489-3e92-866e-ee074a959f3d | -5.7615 | -57.5807 | 2025-08-23 12:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 460a32e2-77a3-3184-8a91-456ab483e40c | -11.6613 | -51.5798 | 2025-08-23 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 111a36a6-6b22-3a17-be91-4ff9e68032f8 | -5.7431 | -57.5814 | 2025-08-23 12:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 850da70e-93b9-33c7-979e-fe04f930d1f8 | -7.6296 | -45.2464 | 2025-08-23 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 8aa018fa-0a2c-34ab-a672-4fe56b2800be | -6.5856 | -44.564 | 2025-08-23 12:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| b9e477e5-aa3c-314f-8eec-51f4cc72c052 | -7.0352 | -44.6396 | 2025-08-23 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| e1db4608-8eb5-3fe9-9c00-3b63c5e8d9bb | -6.1229 | -43.9578 | 2025-08-23 12:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a50c4819-124a-3d4f-bfe4-5985c372632a | -14.6706 | -54.9142 | 2025-08-23 12:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| c47033ff-3bb1-38ef-b0ed-dbad38dcd92d | -14.8098 | -45.4451 | 2025-08-23 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 878e1a6b-efd7-36c4-9aaf-9f4d929ad744 | -7.0352 | -44.6396 | 2025-08-23 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 930b6f9f-d5d0-3493-81e5-7cfd00978bce | -5.7615 | -57.5807 | 2025-08-23 12:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 02c6b61f-318c-3fb4-99af-80b3a672d099 | -14.6706 | -54.9142 | 2025-08-23 12:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 72442d66-bb7c-3dd0-a417-21484ae7c14e | -7.6296 | -45.2464 | 2025-08-23 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 761be14f-7f45-306a-b267-dd3b6da995d4 | -6.5856 | -44.564 | 2025-08-23 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 133803ce-2bd6-380e-95d0-d89039f40f07 | -5.7429 | -57.6009 | 2025-08-23 12:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 844716f9-ad2c-3334-b6b2-ccc54839bff0 | -5.7431 | -57.5814 | 2025-08-23 12:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 424cc7e5-c949-3734-b871-aceb9c1403c2 | -7.0164 | -44.6413 | 2025-08-23 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 7d31ae61-4a2e-3387-9a28-1eb0413ca2a0 | -6.1416 | -43.9563 | 2025-08-23 12:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| fc1de86b-ad5f-30e3-8fe8-18aaca9ad95f | -10.6201 | -50.1609 | 2025-08-23 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| dbae9e36-c68c-3ef0-b2f8-18ff7dceb7b8 | -6.1229 | -43.9578 | 2025-08-23 12:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 1ae3f0b9-ef21-375c-a9ed-a1e4e8b3cb7c | -6.3887 | -45.5342 | 2025-08-23 12:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 05288516-07d7-3d5b-bc1a-00d67841c6f1 | -2.03731 | -47.69543 | 2025-08-23 12:32:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 53c40793-454d-34f6-9a90-a67149ea97b5 | -3.10824 | -47.49519 | 2025-08-23 12:32:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 66e62c93-5f30-3d04-87d6-fb562db73443 | -2.47873 | -47.76766 | 2025-08-23 12:32:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f235143d-faaf-32dc-b197-ec3b9e06ea26 | -2.46957 | -47.76637 | 2025-08-23 12:32:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 32afa3ef-ca3d-3cac-88e9-fd56382127b4 | -2.55257 | -47.70963 | 2025-08-23 12:32:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 644318ee-f387-39f6-9ca0-9af3b7af5f61 | -2.25638 | -47.84408 | 2025-08-23 12:32:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 17acd595-5678-39fd-9714-a7879901cc56 | -10.68882 | -50.13792 | 2025-08-23 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2456ecb3-d305-36af-891e-36817da9fc86 | -6.55135 | -45.48148 | 2025-08-23 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| b9643918-ac74-3d9e-a750-1f28f1301914 | -7.84581 | -46.96621 | 2025-08-23 12:34:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 7c27f2cc-7b3c-3746-b33e-cd85e1a566c3 | -6.37538 | -45.08158 | 2025-08-23 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5a684e3d-048a-3938-8162-cd54bd1380f8 | -13.42201 | -46.25788 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 5acb5502-cf55-3ff1-b545-433ef36f68e9 | -7.87661 | -46.29117 | 2025-08-23 12:34:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b44fff44-30a7-31d4-9636-79766754b746 | -10.74652 | -48.2568 | 2025-08-23 12:34:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bdd0b70e-c76b-3ee0-89eb-0e7c7a867977 | -5.83697 | -45.16605 | 2025-08-23 12:34:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 974c3a4c-b56f-3eaa-bd60-862cda3a6aae | -11.3231 | -47.83852 | 2025-08-23 12:34:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 08d24bee-80b0-3ebf-aa72-a9456571a0b9 | -6.19086 | -45.42988 | 2025-08-23 12:34:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 5127fcde-d245-3ccb-85ae-159aa9a4f687 | -10.63499 | -50.13039 | 2025-08-23 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a01bf855-7ee3-323d-a963-ac9508a3487e | -11.19971 | -55.02307 | 2025-08-23 12:34:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6a633fcb-8d0c-368c-9cbe-f36769eb78f3 | -12.32254 | -44.85126 | 2025-08-23 12:34:00 | TERRA_M-T | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 165d9867-55d7-3652-beab-add1408541a0 | -5.82342 | -45.17987 | 2025-08-23 12:34:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| e6ce58cb-37d7-3a31-9b8e-0e3e61ff9ff1 | -12.71761 | -48.10238 | 2025-08-23 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 877dab12-67d2-31ce-969a-b35a10da6d5f | -6.80161 | -44.99591 | 2025-08-23 12:34:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 724f85df-eb08-3cf9-97fd-bc83be79da15 | -6.58476 | -44.56839 | 2025-08-23 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 3ad5b0c6-345b-34a4-ad9a-b80d7d995c08 | -8.79897 | -47.32061 | 2025-08-23 12:34:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 5f7eaa44-22eb-3dc8-b7c3-7d0692abeebf | -10.82256 | -50.82393 | 2025-08-23 12:34:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 155ce4ba-a766-34ac-932e-5d6a07cb8a49 | -6.95663 | -43.00265 | 2025-08-23 12:34:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 34a21253-c283-37e2-81b6-d7f338cc1606 | -8.30838 | -47.32801 | 2025-08-23 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 70d555c7-4778-3f26-be67-46fade8f05e0 | -10.29256 | -46.75979 | 2025-08-23 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d2626b33-21bf-369c-b565-d9ff09000c15 | -5.34347 | -45.16385 | 2025-08-23 12:34:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 1b4c647b-e0fa-30aa-9840-38dcd476fbac | -10.62216 | -50.15677 | 2025-08-23 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 78055abb-b518-3c1d-be7d-3a53e6bd5cd7 | -14.097 | -43.89151 | 2025-08-23 12:34:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 7cbb4222-1a5e-3d98-b444-6f9a4660f384 | -7.62707 | -45.23109 | 2025-08-23 12:34:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 863c45ae-8b90-3896-8be8-eb9eb90f3808 | -6.55345 | -45.46627 | 2025-08-23 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 7343ac89-daf4-38ed-ae3f-511396aa6d2c | -9.55412 | -47.93744 | 2025-08-23 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 48dfc7e6-3bf4-3b99-b9ea-da5cfac79b47 | -5.68244 | -41.3998 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| dc058a78-cfe3-3d42-9b27-c59cc3d7037e | -2.58382 | -51.91481 | 2025-08-23 12:34:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d3375903-c883-3be5-a6e1-c1757fe54958 | -9.85215 | -44.69382 | 2025-08-23 12:34:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| ae37cc37-4d2e-3d9e-a4c4-c99eee5b6057 | -8.30642 | -47.2671 | 2025-08-23 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 4baedf24-b497-3aa6-a83f-2ddc5dfb445f | -12.65714 | -45.32743 | 2025-08-23 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 18486056-c3a4-3eb6-a599-789ec5f4ea67 | -7.0215 | -44.63664 | 2025-08-23 12:34:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| d302838c-6f0e-30fa-a531-7897e61e27a2 | -6.79627 | -45.00173 | 2025-08-23 12:34:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| e95ee59a-7f8c-3d0b-939f-3c62343fdbd2 | -7.03131 | -44.65593 | 2025-08-23 12:34:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| c08b3401-b2f5-3b81-9f8c-a34e7680bcdc | -8.25542 | -47.41574 | 2025-08-23 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b25dbc30-007d-3031-9abe-48aa6bf1d336 | -6.37108 | -45.5418 | 2025-08-23 12:34:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 24831b42-8321-360b-bf6b-3676297eafe2 | -6.36911 | -45.55673 | 2025-08-23 12:34:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |


[Clique aqui para ver as próximas entradas](README86.md)
