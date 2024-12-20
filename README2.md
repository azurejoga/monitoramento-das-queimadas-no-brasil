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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9da5cc0-db07-38ac-b4da-c2478edd1a26 | -9.2215 | -60.3495 | 2024-12-20 00:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 76d8f756-12c9-370d-859d-98b8fd1f8ae7 | -3.2321 | -46.7836 | 2024-12-20 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 56cc8238-a263-3aac-bf2b-4e1ba9ec2f06 | -3.2136 | -46.7843 | 2024-12-20 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f0fb9a73-87f0-37d2-97aa-2ddcc7eef056 | -5.9369 | -48.0654 | 2024-12-20 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 5e6b9d3b-88e8-3ef2-a901-aeca4c883d5c | -2.7661 | -47.3912 | 2024-12-20 00:30:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 7ce0fb46-4645-368e-9282-e11e56acfdbd | -3.2507 | -46.7829 | 2024-12-20 00:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 5c1c2d30-3564-3f73-9dad-b72209e5df76 | -3.232 | -46.8056 | 2024-12-20 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 157.9 |
| 8f6219cf-7945-3cb0-90d7-a48eec498334 | -4.9272 | -41.3358 | 2024-12-20 00:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| e4718b96-ace8-3525-a601-1df6386f8df1 | -9.2216 | -60.3302 | 2024-12-20 00:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.5 |
| d2dd7fff-1fb9-3c77-9a6c-1ffe73735af3 | -9.2403 | -60.3292 | 2024-12-20 00:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 59b03d66-5049-3d92-b4a6-118f21450ef7 | -2.7661 | -47.3912 | 2024-12-20 00:40:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| ee706ccc-30db-3404-b148-574fe25d2422 | -9.2216 | -60.3302 | 2024-12-20 00:40:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 8efa7a66-c1a9-3fa5-83ce-0b0932415788 | -9.2403 | -60.3292 | 2024-12-20 00:40:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 21220f30-3cbd-3023-b383-26b574b3e4cb | -4.9272 | -41.3358 | 2024-12-20 00:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 6273261a-4710-3cee-bcfa-0704b55845dc | -9.2215 | -60.3495 | 2024-12-20 00:40:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| e27be9fc-9f64-353d-8758-d70f3ea84b91 | -3.2349 | -46.809601 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b23c9286-e00d-37ab-8d69-0fbc9897ff1d | -1.2 | -47.235298 | 2024-12-20 00:45:00 | METOP-C | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 492d7438-10e9-3e65-a07a-ada25956d9a0 | -4.1119 | -46.723099 | 2024-12-20 00:45:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 350b8e33-97a4-3202-8dcd-3224b1ecf29d | -4.1179 | -46.7043 | 2024-12-20 00:45:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d76834e9-7b9d-3343-892c-4b8be2c5fccb | -3.6141 | -46.005699 | 2024-12-20 00:45:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2c86941-50bc-3358-9a2f-04926425190a | -3.2427 | -46.799 | 2024-12-20 00:45:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f7a7b4e-007d-374d-b05b-688670a2d93b | -3.2232 | -46.803501 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56c11786-b939-3925-82ce-5a4c04931082 | -3.0853 | -46.5662 | 2024-12-20 00:45:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 24630b32-e7ab-335d-9ae0-2f2c5a5aada7 | -2.7728 | -47.394501 | 2024-12-20 00:45:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ee5edf8-7d6b-3e54-a708-be7fe6d077fa | -1.3826 | -53.736599 | 2024-12-20 00:45:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bea55933-80d0-31f1-ae8c-7a2a59deda1f | -3.2525 | -46.796799 | 2024-12-20 00:45:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 259488ba-5d03-3764-ac16-9ebf8bd5279d | -12.3742 | -52.479599 | 2024-12-20 00:45:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75a43f31-6cab-33fb-824d-4b56a080c84d | -1.1981 | -47.226898 | 2024-12-20 00:45:00 | METOP-C | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af55af12-4f0d-324e-a59d-955e8ef72a94 | -3.2112 | -45.518501 | 2024-12-20 00:45:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f87afaa-6bef-3923-be07-e6499727e6b1 | -15.1993 | -43.729401 | 2024-12-20 00:45:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 648bdab7-2d0c-3537-8627-0686612e3a70 | -12.4118 | -43.7999 | 2024-12-20 00:45:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ac2a577-bb96-3e43-9299-8fdaed8a3a64 | -2.7649 | -45.547901 | 2024-12-20 00:45:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 239c27f3-c5ce-38f2-b0ad-362d91e304ff | -1.9438 | -52.0877 | 2024-12-20 00:45:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbcaa401-94dc-33e3-90d8-2d29e5272950 | -4.9395 | -41.3493 | 2024-12-20 00:45:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e8f15663-b907-3117-8147-15127555985a | -2.451 | -49.305302 | 2024-12-20 00:45:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6db1b4f2-9d8b-356c-b4de-d68d6e17a125 | -3.2446 | -46.8074 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92ded948-c439-3433-abce-513969dfb8ef | -3.2291 | -46.784401 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57194bf8-eba5-37aa-9a9c-757db4fd57df | -2.5612 | -46.927502 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0562f4a-d1de-3919-a099-49d3244334b4 | -2.5632 | -46.935902 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca8c84f-cbdb-387c-aa8a-39ad0448255d | -2.7067 | -46.136101 | 2024-12-20 00:45:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f6259cd6-62ff-36da-999f-9ca0d4673198 | -4.1168 | -49.416599 | 2024-12-20 00:45:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| babcfebf-f60f-3298-a6da-fcb0d49449bf | -4.0784 | -50.0135 | 2024-12-20 00:45:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21bb09b0-d386-3224-958c-27f2f661ba90 | -2.7574 | -45.560001 | 2024-12-20 00:45:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2f80fa25-2c99-3fdd-90f2-ff66164c2d55 | -2.6501 | -47.176998 | 2024-12-20 00:45:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb079e7c-47b8-3e6f-a4f9-096a7556ec5a | -3.2486 | -46.779999 | 2024-12-20 00:45:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fcc716e8-0b56-323a-8fb6-94f3dc8c80cd | -3.2173 | -46.778301 | 2024-12-20 00:45:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 76682547-e392-3582-8a99-248a0ee536e9 | -3.2271 | -46.7761 | 2024-12-20 00:45:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dfa15533-2dce-33f7-bbf7-a380219f9bb6 | -2.7672 | -45.5578 | 2024-12-20 00:45:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c4112490-8643-397f-8f71-5efaae71135d | -7.2596 | -44.717701 | 2024-12-20 00:45:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0769200e-7fef-3290-b061-2e8398667889 | -2.7695 | -45.567799 | 2024-12-20 00:45:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1a4fe156-ce13-36cd-93a6-b389c80d8399 | -4.5759 | -46.634102 | 2024-12-20 00:45:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 055f83a3-d04b-3170-b9c4-d4bda8c99d6f | -1.3126 | -53.52 | 2024-12-20 00:45:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e83b01a9-dcff-369a-8c00-6e529f96f8af | -2.4637 | -51.836498 | 2024-12-20 00:45:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45a473a2-1278-3616-aeac-67d9e0be5543 | -4.9255 | -41.334 | 2024-12-20 00:45:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 72d33dab-6c2f-3792-80fe-cafe22084f02 | -3.0536 | -47.093899 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa779b95-3354-33b3-af60-319e7be7644f | -3.7264 | -48.974899 | 2024-12-20 00:45:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5943122d-1aef-369a-a933-271a78cf23d9 | -2.6539 | -47.193298 | 2024-12-20 00:45:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3b89550-fc4c-3e0e-8df0-0662fac09291 | -2.6942 | -51.898399 | 2024-12-20 00:45:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f04a6283-ea60-3b3b-9656-b095f3f2e44f | -6.0475 | -44.051102 | 2024-12-20 00:45:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9062ed69-a145-3251-957f-5f0c4d7f2a52 | -3.6162 | -46.0149 | 2024-12-20 00:45:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ae7c1813-cecc-33f2-a308-05edd97d4658 | -4.1277 | -43.561798 | 2024-12-20 00:45:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5aa7a793-01f4-3423-af1e-eb7c1c2b57f0 | -3.9689 | -47.038601 | 2024-12-20 00:45:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b07e0ec6-c93c-3a9e-b828-623ce97dd251 | -2.7088 | -46.145302 | 2024-12-20 00:45:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2bc3ec66-5207-38e0-ab63-cdb2755ee1f0 | -3.2089 | -45.508701 | 2024-12-20 00:45:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| daf989d0-e611-34c0-87e5-347e74a9733e | -3.2212 | -46.795101 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0e77f4d-9c63-37e0-aa80-4177c9cfca3a | -3.2251 | -46.811798 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0086ff6b-7dd1-33e9-9f16-e4b09629a458 | -2.5954 | -45.308399 | 2024-12-20 00:45:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 48fc81a7-25d7-3ad0-a102-dd7432cc1247 | -4.1541 | -48.995499 | 2024-12-20 00:45:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d65fc76-a5ea-3918-a10f-de754ed62450 | -3.2114 | -46.797298 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97b525b0-b677-3820-83a9-0595ec06866f | -4.0209 | -46.907799 | 2024-12-20 00:45:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb44eb9e-75f7-3412-a401-ae94194bc1e6 | -2.771 | -47.3866 | 2024-12-20 00:45:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 649acd9f-5414-3e4a-b64a-3360e7419743 | -4.1152 | -49.409698 | 2024-12-20 00:45:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3bc21ef-46b3-3e90-97df-d145cc631f85 | -4.157 | -43.728001 | 2024-12-20 00:45:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0bc7bdb-e22c-3514-849e-11b3fcd30208 | -3.9671 | -47.030499 | 2024-12-20 00:45:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 359138e0-b0b9-3712-bf75-a70cc6507d51 | -3.2382 | -45.501999 | 2024-12-20 00:45:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1a2f5b9-6c22-323d-b9a5-716c67bd8049 | -3.2095 | -46.788898 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3855afd3-3543-346f-af33-8370d3350380 | -1.3322 | -46.649101 | 2024-12-20 00:45:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0edf992d-11cd-3059-a5e8-53f2d394b5f2 | -2.7747 | -47.4025 | 2024-12-20 00:45:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39533617-0db0-30f8-97c2-abe928b9bb5f | -3.2368 | -46.773899 | 2024-12-20 00:45:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b300e802-d385-308d-898f-a2c097c8e27c | -3.7903 | -47.112999 | 2024-12-20 00:45:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 031ba68b-9d44-35ce-b286-9d18aa0831f2 | -3.0057 | -46.7108 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c97318b-15b6-3e62-9970-73f6ad17323a | -6.0449 | -44.040001 | 2024-12-20 00:45:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c46922e7-c1e4-3d93-8230-cfd3b1c7b014 | -3.2193 | -46.786701 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f287b7cd-4c2f-3bc1-8152-04aa50d96353 | -1.3845 | -53.7449 | 2024-12-20 00:45:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 768ffd15-52aa-3fd4-8079-4f6c2b9d1599 | -3.2388 | -46.7822 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e464939e-ca2d-3f5a-80e5-c3cfc45989fe | -2.9784 | -45.009701 | 2024-12-20 00:45:00 | METOP-C | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ef6cb47-a2e5-30e4-b87e-64f910ac22c5 | -4.9352 | -41.331699 | 2024-12-20 00:45:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 082d3fb7-d493-3316-9e29-3a639b164045 | -3.2505 | -46.788399 | 2024-12-20 00:45:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8028ac6f-ed13-35bb-b4cb-190fcd3e0a08 | -2.763 | -47.396702 | 2024-12-20 00:45:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dab6e73c-3a73-3159-a5f9-de1030b1c8ac | -3.2407 | -46.7906 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f9f7717-666a-3648-894d-eef0ce9a0156 | -12.384 | -52.477501 | 2024-12-20 00:45:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 478e67a6-b016-3741-8208-fc097be29446 | -12.6753 | -43.437401 | 2024-12-20 00:45:00 | METOP-C | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d6261d0d-9177-309e-9154-3e3dc0d775ae | -3.233 | -46.801201 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d299038-ec07-32a5-9b56-d3269fed6ed3 | -3.231 | -46.792801 | 2024-12-20 00:45:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d00f939f-446c-389a-a523-5302af0b7ee5 | -4.0228 | -46.915901 | 2024-12-20 00:45:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ed43af8f-485c-3a9a-8e87-64df51fb24ea | -4.2767 | -48.096699 | 2024-12-20 00:45:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b08a077b-4035-37be-b163-73a71fff57eb | -4.0799 | -50.020302 | 2024-12-20 00:45:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35e239e1-b06f-3755-a24d-bf5c5108c176 | -2.5863 | -51.922401 | 2024-12-20 00:45:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d126124a-f03d-39ab-9916-f8982aa24842 | -2.5979 | -45.318699 | 2024-12-20 00:45:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 49a22721-24b4-3a5b-85a7-dd2370fae975 | -4.1159 | -46.696098 | 2024-12-20 00:45:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
