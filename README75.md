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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36ff5808-93ed-3533-8cdb-5ed5c0e7019f | -4.70215 | -44.48559 | 2024-10-26 04:44:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84cd44d9-8b03-36a5-9035-0a60673afd33 | -6.45304 | -44.68012 | 2024-10-26 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2dfdb127-5660-324f-865b-5c179bf234ef | -6.40799 | -44.5204 | 2024-10-26 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9a2c4f9-3539-3ce3-be66-778f2ffd82ea | -6.3485 | -44.56336 | 2024-10-26 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42a93085-6221-3587-ae47-b690e4d918bf | -6.28352 | -44.76524 | 2024-10-26 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e026cbe-7cd2-3d24-bcf3-36556f9501d5 | -6.22701 | -44.62774 | 2024-10-26 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26c08b4f-df5f-3435-aada-67a89e1984a6 | -6.22322 | -44.62282 | 2024-10-26 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0bd26aa-0dfa-32b1-82b2-f01391437021 | -6.22261 | -44.627 | 2024-10-26 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4fb0530-bc46-3201-b4ff-c8eeca05aa90 | -6.21881 | -44.62214 | 2024-10-26 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25bb22d8-365c-3d1b-bc7f-40373c9a1981 | -6.21821 | -44.62627 | 2024-10-26 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82d7e006-f669-3b17-bf08-4c90b86385b3 | -6.11665 | -44.88777 | 2024-10-26 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 082b3210-fc4b-35c8-b86a-7379a365e256 | -5.93149 | -44.65028 | 2024-10-26 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 555e705d-9e73-3abc-b670-34d0bb51f66a | -5.93085 | -44.65462 | 2024-10-26 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f008826f-c7e7-3472-9110-b09da80ea539 | -5.82948 | -43.65017 | 2024-10-26 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6ec18d1d-0807-326f-9816-f582f49d7c7f | -5.82877 | -43.65513 | 2024-10-26 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ed12205b-cf74-3927-b731-910a722dde90 | -7.7619 | -45.16764 | 2024-10-26 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 798f47cf-7302-3e12-9ffb-7ff6965867b4 | -7.02504 | -45.19686 | 2024-10-26 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5cb20535-9783-3129-bd8b-41f92a9a438b | -7.30519 | -44.96787 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d240bbe2-f6ce-3608-ae3b-253b620cc653 | -7.30517 | -44.97062 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 687630e3-01ce-3797-86f2-2a6049b31182 | -7.30455 | -44.97223 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b5d009a-5f98-361e-a01e-039c87ab57e1 | -7.30397 | -44.97928 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 148688f9-b47c-3897-b65d-12527ef858ea | -7.30329 | -44.98083 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b0216c87-c34f-3d2d-876d-e0fde2982834 | -7.29891 | -44.98022 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 455c9c15-6c61-3c1f-a73c-5a186a3b0178 | -7.29079 | -44.97465 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bc00669-6c45-3fc7-b68d-69dd3a05ef90 | -7.28642 | -44.97393 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bee313e-2610-302a-a571-46bd2bcb2d67 | -7.03238 | -44.67497 | 2024-10-26 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f4810e0-4081-34d1-8973-b474eca0974c | -6.81608 | -44.46887 | 2024-10-26 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 099aa7f2-c9fd-374d-86fd-af74daa9b2f7 | -6.81092 | -44.47273 | 2024-10-26 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee2785c4-5f05-349c-80bb-4d34a7c9dfcc | -6.71054 | -44.70264 | 2024-10-26 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d3ad1c8-ce65-3de7-a445-daa226b12e18 | -6.71014 | -44.70071 | 2024-10-26 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0122f20c-1fd7-35f1-b5e8-e57a8b10619d | -9.00689 | -44.31424 | 2024-10-26 04:44:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50dbfd0f-8db8-37b6-a9c9-bc8cdea8d1b7 | -9.00511 | -44.31153 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a1857a1a-dcb6-33dd-a62e-1648ea32195c | -8.78897 | -44.72061 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7df0de0-cb1d-3305-a60c-43f1357df336 | -8.78833 | -44.72523 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90503059-2c11-36c4-b054-ca6ad16b3ff4 | -8.78769 | -44.72986 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67cf6b59-be0a-3ca1-a1d8-ebf9c7f15fdf | -8.78706 | -44.73449 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 214e4bfe-57a0-3d29-9680-e9f0a4dcfbe5 | -8.78642 | -44.73911 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d172bc04-210b-3879-b20f-5a6ebc9b873e | -8.78049 | -44.71474 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57b99eb1-7af3-38a5-bbf5-d1080522414f | -8.77985 | -44.71937 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f3b0491-2bf4-3664-a088-19b4ca1c859b | -8.77922 | -44.724 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a0f7551-59f4-35af-8e46-421b02c36d46 | -8.77466 | -44.72338 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1623213-b69c-3a3e-9a7d-f89bb4d479ad | -8.77403 | -44.728 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 442395e6-64ea-3ba4-a66e-68b36d843836 | -8.76745 | -44.70822 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ebdb4f4-de83-38c1-8875-3f0e7562d50c | -8.76681 | -44.71286 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7eab6cf0-2c0f-3fe0-b969-362e4e88e4dd | -8.76618 | -44.71748 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30e420c5-1f80-3092-9a2e-e636de1fe0c4 | -8.76351 | -44.70296 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a77523db-1566-315b-b44a-e966f8dcd2b1 | -8.76163 | -44.71684 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddba7f81-1229-3e06-9fcc-dfc5967a94f9 | -8.761 | -44.72147 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4b7f981-fb9a-345f-9cf4-38331ee82863 | -8.76037 | -44.72612 | 2024-10-26 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 390f59fa-57dc-31c3-a49a-eaff56b05229 | -8.65386 | -45.04918 | 2024-10-26 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2dacf2ac-db18-3457-ab86-ff7582a4e19f | -8.64878 | -45.05306 | 2024-10-26 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a7b69bd-9883-324f-b84d-0f26aab97167 | -8.47897 | -45.4011 | 2024-10-26 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a95b624-0b70-35cd-81e5-8ad2de5f3374 | -11.04129 | -45.27911 | 2024-10-26 04:44:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de1d20fa-9a45-3ed7-9638-b3e0454c7f5d | -5.08207 | -45.24928 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3f877d2-2684-37fb-97c4-bef965c3bb49 | -5.04315 | -45.45253 | 2024-10-26 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd5103fd-e48a-390e-ac0c-ad086d80f100 | -5.0426 | -45.45616 | 2024-10-26 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d818c8a1-9807-3e56-b75b-d4b955c8c892 | -5.03851 | -45.45557 | 2024-10-26 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9010c72a-c0cc-3699-ba66-4d80ffbb66fc | -5.02855 | -45.12062 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70d15aa8-5242-3775-a0ff-18ad73282a11 | -5.02741 | -45.12076 | 2024-10-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d49f1e64-3e02-37d6-87f7-a531524dd862 | -4.94833 | -45.61546 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cb0eec7-32f2-3309-8d36-5f204c3f7b40 | -4.9478 | -45.61913 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50cea17b-d845-3cd2-8d92-3feec0bd796e | -4.94774 | -45.61508 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48d223c2-7973-33e4-ac17-e5afbb6efae6 | -4.94718 | -45.61877 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 891eb04c-95a7-3abf-b6d5-2e7aa7b25635 | -4.92149 | -45.85564 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2f58981-fff4-3bb8-9505-c0efb991d267 | -4.921 | -45.859 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d992c980-3b0a-308d-a4c9-ebc8643dd34b | -4.92051 | -45.86237 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04c7e5be-5995-3976-8fcb-8dd6cd2152f3 | -4.91751 | -45.85503 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5f713b3-d612-385b-9c5d-7fceb308c538 | -4.91702 | -45.85841 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d435fe4-0482-3d83-a093-87c71f0bd675 | -4.91652 | -45.86177 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d860771-d81f-35bf-863d-824b9f229a41 | -4.91603 | -45.86516 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 943148ab-8747-300f-819c-b8711503cb64 | -4.91471 | -45.85756 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2aeb203f-24a4-3da0-99fd-24ad89b8123e | -4.9142 | -45.86092 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb063e67-6e22-3d33-b99d-78b194acf776 | -4.91368 | -45.86429 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2a2be63a-be21-3ad4-a199-082d2cff4555 | -4.91303 | -45.8578 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f71c246b-1019-3f85-95bd-79f435a87ba4 | -4.91254 | -45.86118 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4352ac7c-2a0d-3959-8f69-57f94df2491c | -4.86129 | -45.77901 | 2024-10-26 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5af3c6dd-5921-3b06-a7ea-975ea3434fab | -4.82254 | -45.67292 | 2024-10-26 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bb50d15-d210-3a35-b001-97c1d910e377 | -4.76003 | -45.76086 | 2024-10-26 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fca34158-7f65-3660-ab45-59e401f5c976 | -4.74395 | -45.67588 | 2024-10-26 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b32356f2-779b-39fd-a5e3-aec64ead77c3 | -4.74342 | -45.67944 | 2024-10-26 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f25974e-76aa-3317-bef8-9bd9ecab6661 | -4.7394 | -45.67891 | 2024-10-26 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48418f6c-bd30-3b8d-b658-55cf8ac6e00e | -4.69138 | -45.71484 | 2024-10-26 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 546811b6-75bc-3ee3-b7bc-7209cc1d9d96 | -4.68746 | -45.57708 | 2024-10-26 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00982bdb-3c71-3526-838d-0f2643f2cb8c | -4.68061 | -45.81262 | 2024-10-26 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46b3e161-bd05-304e-a1ed-ee56de9ceb3a | -4.57977 | -45.84473 | 2024-10-26 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 760c60d1-8755-30e2-a52e-ba08142d8a68 | -4.57726 | -45.67343 | 2024-10-26 04:44:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f290962-0f65-345c-b451-812f0bb7a6c8 | -4.54267 | -46.03448 | 2024-10-26 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd1d48e3-ff1f-3e6e-970c-fbf59296d007 | -6.406 | -45.82107 | 2024-10-26 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de44a864-1486-3810-9dd9-381aa929342b | -5.99509 | -45.96143 | 2024-10-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 319704c8-1563-3282-a99c-08aabb040145 | -5.97713 | -45.36722 | 2024-10-26 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 3ffd3fb8-3c16-3b1a-bf5c-bdf31c6163ee | -5.97658 | -45.37104 | 2024-10-26 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| e61c511b-935d-3873-8c2b-89b3b5c16f6f | -5.90882 | -45.58764 | 2024-10-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e03a149e-9c25-3376-aeeb-b374b3f00d82 | -5.84247 | -46.23893 | 2024-10-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0412e762-31f2-35c1-b0f7-4b9cbb534817 | -5.75402 | -45.56188 | 2024-10-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e35f4a0-6ef8-3072-9af1-2962c21ca165 | -5.75348 | -45.56555 | 2024-10-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49a7ac39-0cb0-380d-944a-422f3d7268d3 | -5.70426 | -46.30674 | 2024-10-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 468e373e-edcd-30a9-90ce-5e66e80d0bb4 | -5.64874 | -46.38389 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56683f61-af8b-301c-a6c6-c04de448d90d | -5.6373 | -46.40727 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dca41eb-6218-308d-974f-80156719f78d | -5.61202 | -46.22602 | 2024-10-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7a3b7a2-d6d0-3733-90b3-5c6079d1db7a | -5.58428 | -46.38962 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README76.md)
