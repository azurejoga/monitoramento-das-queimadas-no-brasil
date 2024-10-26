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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70446945-f44c-3c75-88fe-62a2f8ea00c6 | -17.7868 | -57.3649 | 2024-10-26 04:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.5 |
| 501e2c62-b7d4-3fb0-8c89-9809ad497310 | -17.7872 | -57.3443 | 2024-10-26 04:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.3 |
| 426f453e-7e7f-3660-8658-3d97b3bbb97e | -17.843 | -57.5431 | 2024-10-26 04:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.1 |
| e6eeefc5-41f2-39ca-b1dd-4da569690e53 | -17.8628 | -57.5407 | 2024-10-26 04:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| b41f8590-5905-354d-8b62-73c1dd852d43 | -17.8631 | -57.5201 | 2024-10-26 04:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 164.0 |
| b1158448-b7e9-3ae5-ac22-f9c7b3f24ced | -17.8634 | -57.4995 | 2024-10-26 04:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| cd5cd298-cbda-3429-8a5f-0ed2ab56a781 | -17.8828 | -57.5177 | 2024-10-26 04:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.0 |
| 2c6b7097-d9cc-3158-bea8-b71ae8060579 | -17.9415 | -57.5516 | 2024-10-26 04:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.5 |
| 3dc27d00-d86e-3e2f-ab61-ddb330027ea8 | -17.9418 | -57.531 | 2024-10-26 04:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.0 |
| 3f6629b1-a3dd-3f85-9fc2-80348783e440 | -18.0431 | -57.3745 | 2024-10-26 04:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.2 |
| 24d0860e-6138-37fb-80e8-23063e693eb0 | -18.0629 | -57.3721 | 2024-10-26 04:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.2 |
| fbaca91f-1c28-3d97-8355-f345923a3396 | -18.0827 | -57.3696 | 2024-10-26 04:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.6 |
| cac676fe-a6fb-3d70-a0f4-5b9bbb293cd8 | -18.083 | -57.3489 | 2024-10-26 04:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 3efcd193-5798-3641-84a5-684b0a640d44 | -18.2649 | -55.9975 | 2024-10-26 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 3605f3d7-8319-3faf-bfa9-eb696b84e2d0 | -5.14979 | -37.73906 | 2024-10-26 04:17:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c26dc579-1526-3fc6-aefe-01396b0ff490 | -5.1453 | -37.73839 | 2024-10-26 04:17:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fdedaec7-16d6-3ae9-8052-2c354845ef82 | -5.05508 | -40.8878 | 2024-10-26 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 67871b04-fe93-3436-9422-6734ad8793bb | -5.05471 | -40.88596 | 2024-10-26 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5a4b7704-5ef5-389d-afac-35f327c34a77 | -5.05407 | -40.89026 | 2024-10-26 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e82d7101-5a4d-38be-b838-a5b458471780 | -4.9236 | -41.9731 | 2024-10-26 04:17:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4990cb08-28f3-34f2-834a-c039702b5b26 | -4.92302 | -41.97693 | 2024-10-26 04:17:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9ed91a22-bcf8-3534-ba09-28852c141cb2 | -4.91954 | -41.97638 | 2024-10-26 04:17:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3817b0b3-5a24-321d-89ec-81f1c3d47c23 | -5.81137 | -43.21066 | 2024-10-26 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0162049-16a4-362c-933c-0e64497aad6a | -5.81082 | -43.21424 | 2024-10-26 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2aeda724-9aac-3c0f-bbda-479bcd57aeb6 | -5.69311 | -43.18531 | 2024-10-26 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15459b56-2ca0-34b9-81a4-81da18f319a6 | -5.40454 | -43.62922 | 2024-10-26 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a708264f-9c7d-3664-a393-933b211713ec | -5.29399 | -42.9448 | 2024-10-26 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c3130df-0f9a-3a3e-a06a-c91bc113e948 | -5.34506 | -43.36071 | 2024-10-26 04:17:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66c0cd47-5c32-3707-8eb0-a9b0622030a6 | -5.9137 | -43.92318 | 2024-10-26 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd6ab47a-5edd-3e87-b5bc-f212371e32ad | -3.61655 | -42.99727 | 2024-10-26 04:17:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 220569f5-bf5a-3776-ad32-73c7a0638c2c | -3.53928 | -43.6199 | 2024-10-26 04:17:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b0ab392-d0b7-3e84-9343-642cddc80bfc | -3.51881 | -43.62025 | 2024-10-26 04:17:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34907648-9d61-3664-9090-5394fd748804 | -3.48801 | -43.32398 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 85060c78-ee99-3c8e-a304-3f20486726fc | -3.48746 | -43.32745 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c83d653c-5ee9-3907-9bbd-a0446f9775a8 | -3.48468 | -43.32346 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cbe165ca-7f0e-3520-99cd-044149f26f12 | -3.9805 | -43.1542 | 2024-10-26 04:17:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eaef5f7e-a326-38a9-aa53-a115d83570d6 | -4.8535 | -42.95082 | 2024-10-26 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68bb596c-035b-3956-ad26-87493a5bf6d4 | -5.068 | -43.66269 | 2024-10-26 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1732fb5-37d0-3e3f-bc19-8d2dbb2571f5 | -5.06745 | -43.66618 | 2024-10-26 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8499666f-48a6-325a-9a77-6f1604e2a195 | -5.06691 | -43.66967 | 2024-10-26 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 227311cb-6267-39c2-9c70-c0618100333a | -5.06637 | -43.67315 | 2024-10-26 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a3b9af2-1695-3401-8d2b-6861068c3748 | -4.74327 | -43.25373 | 2024-10-26 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f4d6a204-021b-37bc-b254-0ac0aa4b06a7 | -4.74272 | -43.25726 | 2024-10-26 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d90574a9-9d7b-39ba-85f9-8b90264e718f | -4.73992 | -43.25321 | 2024-10-26 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31dee536-e7a8-3e2d-a7a6-5b0e9cc9b28d | -4.73657 | -43.25269 | 2024-10-26 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdb27c23-5de5-3e8e-b87d-65595c9f1fbe | -3.48354 | -42.87172 | 2024-10-26 04:17:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c76950e5-2d8b-3d8e-86bd-afeef5b0469e | -3.48019 | -42.8712 | 2024-10-26 04:17:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a742f3b-8796-3133-96aa-71fe7928704f | -3.2303 | -42.6992 | 2024-10-26 04:17:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e26f2b6-8b4f-344a-b36a-655077c5b7c8 | -3.21238 | -42.7037 | 2024-10-26 04:17:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aee093a8-2530-32c9-98f7-e33e7cdb946f | -6.71467 | -37.49896 | 2024-10-26 04:17:00 | NPP-375D | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2ed5a69b-b1c5-3754-a856-b31f0a48b586 | -5.6804 | -39.29996 | 2024-10-26 04:17:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f69490a9-325e-31b7-ac0e-89f0638ad0a5 | -5.39246 | -39.48419 | 2024-10-26 04:17:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f6498549-7922-37bc-91f0-c2f6a07dc170 | -3.12439 | -40.99509 | 2024-10-26 04:17:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ecd42b9e-0f0d-361f-aeba-1ac4f7167cf4 | -3.12082 | -40.99454 | 2024-10-26 04:17:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fce1a8e6-4c5d-3b75-b08f-52d843d00000 | -3.89664 | -41.03297 | 2024-10-26 04:17:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3055546d-a55a-3f4b-94ee-3c8591c9e1a4 | -3.89602 | -41.03705 | 2024-10-26 04:17:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9da3d2d8-5fd0-356c-85b7-88b27d5f2013 | -3.89305 | -41.0324 | 2024-10-26 04:17:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 20.2 |
| f1341c8e-bde4-3877-aa11-31358674d72a | -3.89243 | -41.03648 | 2024-10-26 04:17:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| dd723e37-3d03-37d0-bca7-c8ff4892745d | -3.88947 | -41.03182 | 2024-10-26 04:17:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 2b6634e7-fef8-3514-a7df-6692b248be61 | -3.88884 | -41.03591 | 2024-10-26 04:17:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fa345cd1-e760-3496-8cfc-157653b6bba0 | -5.98002 | -41.51428 | 2024-10-26 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d390ee1f-0fc4-3b31-848e-5c4eeed3261d | -5.65586 | -41.82545 | 2024-10-26 04:17:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 940eca3a-2516-38f7-b9bd-971e3b7e0947 | -5.65525 | -41.82941 | 2024-10-26 04:17:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| eedf592f-e7d3-3ed5-9eeb-5e66d4e2b90f | -5.65172 | -41.82886 | 2024-10-26 04:17:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 83e5cc54-eb0b-3122-9cd5-a79fe6677514 | -5.60786 | -41.73732 | 2024-10-26 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f40cff31-afa3-3a86-9d4e-e8b44c57faf9 | -5.2421 | -41.17658 | 2024-10-26 04:17:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bc20ee8b-bdf1-3961-b045-afc3e5e23730 | -2.79777 | -42.4761 | 2024-10-26 04:17:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 580d3867-f78c-3618-9f7a-03fe102a04ca | -2.7944 | -42.47557 | 2024-10-26 04:17:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 415a46ed-3f77-3d6c-bb72-a43baf5c1378 | -2.79384 | -42.47914 | 2024-10-26 04:17:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf2fb674-b6ee-3299-8a6b-aa12b45fa5af | -4.48472 | -42.89445 | 2024-10-26 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26301ec6-67f8-3a6f-b338-b655b51e4246 | -4.48416 | -42.89803 | 2024-10-26 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f955a7d-4ec7-3685-92a3-dbec0368887b | -4.48361 | -42.9016 | 2024-10-26 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bab16231-3e4e-382e-97ce-0f55be75dfc3 | -4.48305 | -42.90517 | 2024-10-26 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c5666e6-4784-3dad-8cc3-9602ef41ee8b | -5.98449 | -42.67247 | 2024-10-26 04:17:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7345787e-7b36-3df1-b626-713082ad3ac0 | -5.98393 | -42.67616 | 2024-10-26 04:17:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 562d67f5-f61f-3c05-b84e-0face51f5eca | -5.98106 | -42.67194 | 2024-10-26 04:17:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b9ad65a1-78d6-3589-a5dd-94975abebb26 | -5.94993 | -43.27999 | 2024-10-26 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b6102259-bab6-3bbc-aad1-90476b2384aa | -5.83643 | -42.77475 | 2024-10-26 04:17:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4fe6e479-1f54-3293-9282-062297d660fd | -5.7766 | -42.64126 | 2024-10-26 04:17:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c9cb07d0-0cdd-33c0-9a16-d1815cea3aea | -5.77544 | -42.62587 | 2024-10-26 04:17:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 717cc1b1-303c-322a-a9f0-9841e5f83647 | -5.77202 | -42.62537 | 2024-10-26 04:17:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e30c7474-1307-3304-8bf7-0a5a18d63af4 | -5.76516 | -42.62437 | 2024-10-26 04:17:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 396efb47-6982-3a2f-8167-69d3006db9d8 | -5.68974 | -43.18479 | 2024-10-26 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 55548a18-8103-3bb8-b908-90972e5cbf74 | -5.65696 | -42.6951 | 2024-10-26 04:17:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3fd890db-cd78-3162-aeb0-d500c0d74293 | -5.64801 | -42.75359 | 2024-10-26 04:17:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f1a7d28b-de21-3dca-b7ec-016c3e5642dc | -5.63445 | -42.77391 | 2024-10-26 04:17:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 300d363c-c834-35a4-84cc-b20e2f8f3aba | -5.63407 | -42.7743 | 2024-10-26 04:17:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8cedbed0-a633-36a1-b4d2-73faa6a40254 | -5.63166 | -42.79212 | 2024-10-26 04:17:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab44ec7a-454e-3fda-9418-46af15fa4ab4 | -5.63123 | -42.79248 | 2024-10-26 04:17:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b323c470-3c6d-3e5c-97a3-521b12e84f78 | -5.62102 | -42.76857 | 2024-10-26 04:17:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 90345132-9763-3135-a74b-8444790cdaa8 | -5.61818 | -42.7644 | 2024-10-26 04:17:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| add75ddb-6ded-340d-8610-4aa6cebbb5f0 | -5.5485 | -42.80959 | 2024-10-26 04:17:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 815ef1c3-d203-3e5d-ac44-8802fbade71c | -5.54794 | -42.81322 | 2024-10-26 04:17:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f46aef71-7546-3b8c-8aa8-6924c3c3369e | -5.5451 | -42.80906 | 2024-10-26 04:17:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1bff59c-c53a-32e6-9104-8257ecf69468 | -5.53854 | -42.91933 | 2024-10-26 04:17:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05913653-691a-3804-ac59-fa38f41241a9 | -5.53651 | -41.89647 | 2024-10-26 04:17:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c5958ea5-bbd6-36c0-a1b7-da630a8d1ba7 | -5.48277 | -42.08224 | 2024-10-26 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 571dea1c-f5be-3c86-a6e2-6dc483db9aaa | -5.48218 | -42.08607 | 2024-10-26 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| da976570-a50d-367b-817d-431c8ddaf428 | -5.47929 | -42.08172 | 2024-10-26 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d925c302-42d8-38fe-999d-d756ae599112 | -5.4787 | -42.08555 | 2024-10-26 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README38.md)
