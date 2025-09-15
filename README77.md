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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eba609c8-e7ff-38af-87ac-39895ec2262e | -10.075 | -47.1908 | 2025-09-15 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 6b25c789-e4d1-3064-84f2-30d7f3a2152e | -8.6133 | -46.3676 | 2025-09-15 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 7161b506-60bd-37bd-85f0-41ad126d2401 | -8.917 | -46.2015 | 2025-09-15 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 168.7 |
| ee95f4f9-e765-32ec-a968-f2547d598090 | -6.356 | -43.1476 | 2025-09-15 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 1df24e78-f416-3fa4-85a3-6e9266f79481 | -9.2235 | -44.5052 | 2025-09-15 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 209.1 |
| 9b3cb863-0e99-35be-95c5-9d597d468a53 | -10.948 | -47.1753 | 2025-09-15 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 0cbc9b36-5cc5-36b9-acf0-21faff9ff942 | -14.5163 | -47.3531 | 2025-09-15 14:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 550d7c46-facd-303b-b704-34012226212c | -13.1842 | -47.2704 | 2025-09-15 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 65a227f5-2be5-3810-9c74-7ff74b809222 | -6.1693 | -41.1872 | 2025-09-15 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 304.3 |
| f8680256-5c99-32ee-8183-27f0d940f850 | -5.8399 | -44.1642 | 2025-09-15 14:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 164.0 |
| c17bce43-88c8-3523-b317-617473049b34 | -11.0617 | -49.7261 | 2025-09-15 14:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 726f244e-d468-3281-9374-86e59a52a8b7 | -11.1303 | -45.3196 | 2025-09-15 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.9 |
| b2d9e572-60ba-3dc2-8dbe-7b89cfaf5a60 | -3.4366 | -43.1532 | 2025-09-15 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 824f319f-f886-3660-8b26-4beff1701b69 | -10.0965 | -48.3569 | 2025-09-15 14:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| aae2d638-46d9-3285-b174-24c5228acca0 | -8.9545 | -46.22 | 2025-09-15 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 199.6 |
| dfc23550-e0d4-31a3-bcab-5322c952cf95 | -8.6507 | -46.3862 | 2025-09-15 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| b4455376-af7c-3f9f-b6fe-55f7fa9dcb13 | -11.081 | -49.7024 | 2025-09-15 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 09dfe6f9-2b24-37f4-92e0-ba610c1cf929 | -6.1504 | -41.1889 | 2025-09-15 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 346.5 |
| 54bcb6d6-afef-3142-9dd0-782339de620e | -6.337 | -43.1727 | 2025-09-15 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 37b813d4-ef09-35b9-a054-f87d7984e2ca | -14.4973 | -47.3336 | 2025-09-15 14:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 786602a5-cce1-379d-b59d-5146dae0821f | -5.9459 | -44.8657 | 2025-09-15 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 4e1d333f-6b02-3989-90d3-55b35cf152ae | -14.348 | -46.1054 | 2025-09-15 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 767d2bbc-c965-3618-86e3-785016e4017b | -8.9734 | -46.218 | 2025-09-15 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 7926c0dd-ccbd-3e9b-a7ae-70970fbd6a40 | -5.8397 | -44.1872 | 2025-09-15 14:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 87867021-d4ff-3aaa-ac5a-86f9cfdfc13a | -14.3485 | -46.0823 | 2025-09-15 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 114.3 |
| ad4a04cc-5771-3e8b-813d-1f56ed38ad20 | -8.8984 | -46.181 | 2025-09-15 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 6e8afe80-c9d4-3da7-99df-9ff44d7ef337 | -12.1668 | -44.0988 | 2025-09-15 14:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 3936943d-051c-33c6-b207-d2a69517c278 | -8.5944 | -46.3695 | 2025-09-15 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 193.3 |
| e277b838-b626-3039-9a6b-2a7f801663ba | -11.6626 | -46.5884 | 2025-09-15 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 1d8d0634-55ee-389e-a726-f6bcbecd174f | -8.9076 | -45.4797 | 2025-09-15 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 140.9 |
| d533617c-b460-37a9-b6e8-f344d5447bed | -12.7818 | -47.1952 | 2025-09-15 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 168.8 |
| d708f620-9c40-3b57-be01-239703e2ee81 | -14.31 | -46.066 | 2025-09-15 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 182.1 |
| c93f76d0-d711-3f55-a68b-8b236accbff4 | -7.7285 | -44.8267 | 2025-09-15 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 0c0a9b30-7704-3da1-b4f7-520ffe50c3c5 | -7.6838 | -48.8682 | 2025-09-15 14:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 53cb302a-337c-3f19-9b2e-b8b074ca1510 | -13.8815 | -48.1271 | 2025-09-15 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| f573fd80-b267-34aa-bbcd-110059f14464 | -12.6764 | -47.725 | 2025-09-15 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 62156de7-7b31-36b6-9716-e34d4b15a29b | -8.6136 | -46.3452 | 2025-09-15 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 74c5cbbd-0433-3d24-8cc5-eda7eb29ad48 | -6.4177 | -42.6246 | 2025-09-15 14:30:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 123.7 |
| fd9fa193-e1c6-3c95-b159-3e95e2293ce1 | -15.7977 | -53.5005 | 2025-09-15 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 131.3 |
| ab02ff32-27b7-3016-a2a4-efe8dbe01df3 | -7.6317 | -46.7284 | 2025-09-15 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 2147a1ce-8574-3f93-8bac-8f645f13c7fd | -8.5947 | -46.3471 | 2025-09-15 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 24b165bf-9d2a-3b99-90fc-017b92f9d9e2 | -9.2235 | -44.5052 | 2025-09-15 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 344.9 |
| eb008a32-c622-3fea-b86c-2d8af47bf39f | -7.6871 | -45.15 | 2025-09-15 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 5185e32f-d94d-39e6-ad09-161656f10d6b | -10.9346 | -45.6207 | 2025-09-15 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 603ce035-0551-3c07-9191-8676b2d98d3f | -12.8404 | -47.1417 | 2025-09-15 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 3468b1d7-1669-3992-a56b-9596a963cffb | -10.9155 | -45.6232 | 2025-09-15 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 2e966900-c6bc-3db5-a015-e44ba01e86d9 | -12.8204 | -47.1896 | 2025-09-15 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 304ac428-2bbd-35da-ae36-24d4d8c14b11 | -12.9988 | -47.9462 | 2025-09-15 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 41b09834-01c6-354e-976a-660af4978341 | -11.1303 | -45.3196 | 2025-09-15 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.5 |
| ad2a768c-5ad8-3c27-8e0a-9c62ee082dc8 | -6.3989 | -42.6263 | 2025-09-15 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 122.1 |
| 31777604-6523-394e-b305-853e112752ff | -8.5944 | -46.3695 | 2025-09-15 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 278.0 |
| c0b88e6b-3e67-3c3c-8629-c4ddc1097988 | -7.676 | -44.4879 | 2025-09-15 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 1ebd1db7-145d-3f49-a5c4-ae857ff76fbe | -6.003 | -46.8567 | 2025-09-15 14:30:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 82531dcc-b97a-339b-9e93-8977544532c0 | -14.5631 | -53.1979 | 2025-09-15 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 120.8 |
| ead24dbf-1e8c-34e1-8c50-927174fe12e8 | -12.6345 | -47.9312 | 2025-09-15 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| fb12f546-5745-3bc6-9451-dd7de22a3725 | -11.4569 | -48.7026 | 2025-09-15 14:30:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 2b0c135c-50b1-3d01-a2f7-c4305ab7d9d1 | -12.7818 | -47.1952 | 2025-09-15 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 7d52df3f-1352-3c99-94e4-ae848b7d8a72 | -14.5163 | -47.3531 | 2025-09-15 14:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| a68f5abd-f089-3e94-a527-604547dd3f3c | -6.1695 | -41.1629 | 2025-09-15 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 146.8 |
| b90ee0a4-2c5c-3c0f-a88e-644a3819971c | -8.9545 | -46.22 | 2025-09-15 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 352c4f6e-56ab-30a6-a38c-34a124656098 | -8.8987 | -46.1585 | 2025-09-15 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| b53d3bd6-dd27-3626-80f5-69cf7a59f29a | -13.8781 | -48.3057 | 2025-09-15 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 9e6aefe0-f9fa-38e3-a525-dbd9d9cf5634 | -12.1668 | -44.0988 | 2025-09-15 14:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 174.2 |
| f756a2d9-9417-3280-b357-6311b70c2991 | -13.8974 | -48.3027 | 2025-09-15 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d890de20-61e7-342f-9702-65b69b540e1a | -13.1842 | -47.2704 | 2025-09-15 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 9e3f99ff-07ae-36b8-86f9-acc8699a4e4f | -11.0807 | -49.724 | 2025-09-15 14:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 290.8 |
| 326c9806-704a-388e-89de-2bdcc62683d1 | -8.9542 | -46.2425 | 2025-09-15 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 8f6a408b-3487-362b-83eb-e81eb18cb782 | -8.7677 | -46.0823 | 2025-09-15 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| a7369a68-32ae-3f50-ba40-1a6ca6f31bbe | -12.1861 | -44.0958 | 2025-09-15 14:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| b3a90dec-127f-3426-a81d-6349190beb07 | -10.0965 | -48.3569 | 2025-09-15 14:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 90ac2a42-7314-3591-9d23-e47187468ac4 | -5.9271 | -44.8671 | 2025-09-15 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| d62acfe2-60db-3645-8537-89b73ed20943 | -6.9986 | -44.5512 | 2025-09-15 14:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| c3c8df06-cbb7-3863-a70e-15cac26fd766 | -13.8815 | -48.1271 | 2025-09-15 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 8134509d-d68f-3b39-9d25-ee45c18c25b0 | -8.9731 | -46.2405 | 2025-09-15 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| f4a6f283-ee2a-3630-8966-95dd4054b27e | -8.651 | -46.3637 | 2025-09-15 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 9f4f10e0-a073-3b9c-bcc4-02b778be0426 | -5.2379 | -42.3174 | 2025-09-15 14:30:00 | GOES-19 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 103.8 |
| 03b96c48-fe04-3884-b240-6b3fe3e7ed39 | -14.8218 | -51.6362 | 2025-09-15 14:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| de7f9197-0054-3401-8b1e-ca2a06491991 | -11.6626 | -46.5884 | 2025-09-15 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 906099f8-4c65-36b2-99e1-ddf1f01ca3f3 | -13.0177 | -47.9657 | 2025-09-15 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 4c917c0a-9817-314d-9544-ee19596e46ae | -11.4521 | -50.2839 | 2025-09-15 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 7935d90e-58f9-3e0f-95f0-4cdde684abe4 | -6.3372 | -43.1492 | 2025-09-15 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 89e8f4f0-2a6b-3306-89d8-a47ff6cb0691 | -13.9463 | -44.901 | 2025-09-15 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| d4e9dae9-fea7-39bd-b72a-9ee179e9bb20 | -8.6133 | -46.3676 | 2025-09-15 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 3eb9018d-03d3-3c76-970c-c50d456775f0 | -8.6507 | -46.3862 | 2025-09-15 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 111cce1c-6538-3293-a665-28f20c5fa529 | -6.1693 | -41.1872 | 2025-09-15 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 281.6 |
| 2281a2e8-c4fc-3b68-bb92-f25b2e17ac0a | -11.081 | -49.7024 | 2025-09-15 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 3b36a340-8b30-3531-85b9-2a3b575d0f95 | -12.6533 | -47.9507 | 2025-09-15 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 85c30af6-2f76-31b3-a585-014edaecbe8e | -5.7875 | -45.8707 | 2025-09-15 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 6c933e11-6480-3692-80a7-571922fdadbf | -5.7673 | -43.9161 | 2025-09-15 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 6ada1466-9f9b-38c6-9b2a-585757b61324 | -5.9457 | -44.8885 | 2025-09-15 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 330cf1d3-2ec2-3dd9-a68e-acc055fa9114 | -6.1787 | -45.9993 | 2025-09-15 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| d32d9f35-86e8-3c48-ab8c-31922aa64bb8 | -3.4366 | -43.1532 | 2025-09-15 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| cc60e451-cbe1-37a9-aa18-aa8629098129 | -8.9262 | -45.5004 | 2025-09-15 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 8ae270b8-5091-31c5-b8c0-570c958435e4 | -7.4349 | -45.8519 | 2025-09-15 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 4442d813-8208-39f6-a61f-c6fd3bbe2516 | -6.1881 | -41.1855 | 2025-09-15 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 185.5 |
| c1db75a2-15a2-3d16-a507-1dc537a5346c | -8.8984 | -46.181 | 2025-09-15 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 83dec64a-9c3d-3461-bbf3-417e57386be7 | -8.4329 | -45.7337 | 2025-09-15 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 260.1 |
| 8159529b-9eca-3f00-a817-437676c72342 | -8.9734 | -46.218 | 2025-09-15 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 8c2497a4-a7cf-385d-b08b-0be9a61e30e5 | -14.8111 | -48.1367 | 2025-09-15 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 58.0 |
| cc11f654-aaa7-3e52-9ac9-85293d38b7bb | -15.0286 | -47.9663 | 2025-09-15 14:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |


[Clique aqui para ver as próximas entradas](README78.md)
