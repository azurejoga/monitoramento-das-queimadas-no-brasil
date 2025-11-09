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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e66140f9-f3e0-3855-a8f6-64150bcf1512 | -2.82774 | -40.4058 | 2025-11-09 04:16:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a82c8211-4830-3384-912a-9060262e1be6 | -3.34366 | -50.20601 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 226591ba-5667-3836-a2e0-32fe2e181f7c | -4.24495 | -44.66855 | 2025-11-09 04:16:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 155056bd-58bd-3455-9188-5f2d83b2780c | -3.45513 | -49.9766 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 67d1418d-763f-3fd2-b2df-189ea65a5a33 | -4.25534 | -48.63394 | 2025-11-09 04:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d35e08b-3325-3612-8ec7-a57893f94c81 | -3.73785 | -50.04021 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abb5071f-7699-35ed-9be2-0284be4fc543 | -3.6522 | -49.87955 | 2025-11-09 04:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2da4ad7b-159c-3b33-a721-53b1bff116ee | -5.48168 | -46.09413 | 2025-11-09 04:16:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e7f8ec4-c7e0-3744-bbea-d1c3241b8570 | -3.42289 | -43.16465 | 2025-11-09 04:16:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91f34515-629c-3300-bcc6-043b8dd2a957 | -4.87983 | -48.58975 | 2025-11-09 04:16:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c404d5b0-8077-315d-a6ea-b3ddbdaee16b | -2.91862 | -40.00304 | 2025-11-09 04:16:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b945f1cd-0998-3742-83cf-1956ca0edb05 | -3.65556 | -50.27338 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13c07392-6815-3914-b499-5dc884d2b0eb | -2.94603 | -49.35897 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e7ae02f2-3f75-3654-8f2f-f5728f4059a7 | -3.80986 | -45.99992 | 2025-11-09 04:16:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 051729d2-f08f-3b29-b27a-1cfe7a9c59dc | -4.40128 | -45.96854 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38f29da5-0386-3ed4-b176-af925087dbcc | -5.43279 | -45.03321 | 2025-11-09 04:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3618caa-9a12-3de6-b745-2558687ea616 | -3.09742 | -49.26395 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 601758b4-e1d0-3b2e-896f-02793c9fe013 | -3.33847 | -44.37907 | 2025-11-09 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 85e00abe-54d3-322d-ba25-2bced87d1870 | -4.70872 | -44.41439 | 2025-11-09 04:16:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 316e3fe0-f170-3e2c-bbd4-27157610abbf | -3.81126 | -45.99131 | 2025-11-09 04:16:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ff65b3bd-8401-31ea-859e-fa14c81a20eb | -5.20416 | -44.41765 | 2025-11-09 04:16:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a922840-affe-361f-9608-3583f00a29e6 | -2.96654 | -49.82767 | 2025-11-09 04:16:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b66b2f1d-5e34-31d6-bbf7-3f208cca883a | -3.32112 | -49.1254 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5327ac72-a473-3e8d-a3b3-48675cff1d8a | -4.394 | -45.96724 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30f47d79-0ad5-3af2-8894-fda9c94d2ddb | -3.5925 | -41.65824 | 2025-11-09 04:16:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e90885b5-03ca-3bc8-97e6-f538bb812dc5 | -3.45632 | -48.81932 | 2025-11-09 04:16:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ea82b59-a005-3750-a0fc-c115ca0bc85a | -2.96935 | -44.58829 | 2025-11-09 04:16:00 | NPP-375D | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c3796c9-5399-3b6f-af51-188b3bc48d63 | -5.4853 | -46.09474 | 2025-11-09 04:16:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c40c2437-af15-3ac4-bfb0-8daef515bb4e | -3.81055 | -45.99563 | 2025-11-09 04:16:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4cae7cd-7b2e-35b4-8859-4ea898f6ef8a | -3.44939 | -50.04002 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73347891-088b-3283-b7c0-5a9ce3061d1e | -3.25118 | -45.8784 | 2025-11-09 04:16:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd724dd7-d054-3f5e-82ef-702c2e991704 | -4.20931 | -47.78144 | 2025-11-09 04:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 957a7a75-00c0-3781-ab2b-a970d8bfa17a | -3.10201 | -49.26472 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f11193ba-84fc-312d-96c8-a9f4cf399534 | -3.33588 | -50.07325 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2b46961b-8d80-3188-a63e-6eee6ad8afc3 | -5.24022 | -44.37073 | 2025-11-09 04:16:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f2fef77-8626-3a08-b107-54822a25bc9f | -3.80319 | -45.99444 | 2025-11-09 04:16:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5593af0-37ec-3cd2-a76d-e724f9816249 | -5.30799 | -44.20796 | 2025-11-09 04:16:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59cdf656-97a2-3ce3-8d2e-82775fc986c5 | -3.48307 | -39.52916 | 2025-11-09 04:16:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0ebfd3b3-3e1f-3017-b46f-04567d63dfaf | -3.08024 | -49.474 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e55582a7-0e64-3ea5-88d5-393939ae0cc4 | -3.06049 | -50.21519 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d7e9822f-8ca2-37ad-9cae-f3d0d65e2f53 | -4.2415 | -44.668 | 2025-11-09 04:16:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b5997e2-f3b7-343b-b04b-05dc194410d9 | -4.63378 | -46.39675 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 1e096e31-2c41-3830-b4de-25c36ffbb82e | -3.32904 | -53.25124 | 2025-11-09 04:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| baca1537-bedb-3673-97f0-16f4e7d8bb08 | -4.19036 | -46.22786 | 2025-11-09 04:16:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93503b1f-85c7-3a53-a2ef-b70af35b09ce | -3.59639 | -41.65526 | 2025-11-09 04:16:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3f45bda4-d1c9-3d71-bc92-583fb8f11070 | -3.56632 | -51.12585 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e672775a-3e10-3320-85c3-44d677af7439 | -3.79667 | -48.9092 | 2025-11-09 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c98284e-cb18-3abf-960a-8f7190a1d153 | -4.10079 | -48.94644 | 2025-11-09 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75640206-c5e6-3bc9-8cf0-6d537fb717cb | -5.38519 | -44.72706 | 2025-11-09 04:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9c673a16-45db-37b0-ab37-05301c7a8858 | -3.66343 | -41.46783 | 2025-11-09 04:16:00 | NPP-375D | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 42379a1e-0d37-37f7-a8eb-ce446be1e308 | -4.37586 | -48.69408 | 2025-11-09 04:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67c1ef36-230e-3319-911a-4b43a04f7ab9 | -4.04967 | -46.42701 | 2025-11-09 04:16:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4bfcac09-8a2a-3734-8de4-9a4d60204f67 | -3.28997 | -50.19711 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69dd3836-7721-384e-9a7a-c431592ea3b2 | -3.34275 | -50.21148 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ae6da22-d5d9-3830-859b-c8f89596165c | -3.31663 | -50.30793 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c42a7335-2b9f-3292-b727-9bb5315efba1 | -3.91387 | -50.04518 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b85f099d-1342-3050-948b-dc01b2bfb3a1 | -5.0953 | -37.78947 | 2025-11-09 04:16:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 524b999a-53d0-3e1f-83b5-bd8b3496cf41 | -3.45153 | -45.65588 | 2025-11-09 04:16:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5cb15077-7df8-3698-98fb-c3747845e02c | -3.45111 | -50.02978 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d646315b-b017-3967-8f92-346536de053c | -3.31998 | -50.10856 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e15d5ff3-5b65-3c04-ba2c-806f9adbda51 | -3.31763 | -50.15206 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1327d293-49fa-3b2d-a9c4-0d38344c16a4 | -4.25103 | -48.63325 | 2025-11-09 04:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08ee8211-7176-3d82-8b26-76fc5b232d7b | -3.33863 | -49.73505 | 2025-11-09 04:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f21d24f-50cf-3728-8004-b3eb210e3ac3 | -3.258 | -50.07557 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 12c6080e-a466-36b9-a4cc-c3634159d119 | -4.52106 | -40.35778 | 2025-11-09 04:16:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f8c1270e-4fbe-307a-9692-c8efdaf71327 | -3.41268 | -50.2581 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b679201f-d011-397d-9bcf-0306d311c3f5 | -4.33151 | -49.76275 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 95b80be9-5bac-366b-9299-ce243dfc3c11 | -5.38988 | -44.22057 | 2025-11-09 04:16:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e21df44-575e-36cd-a818-855203c72c89 | -4.90903 | -44.64546 | 2025-11-09 04:16:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c97f4722-4cdd-3a09-a1a0-62a15de477c1 | -4.2809 | -45.97256 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfa0b2c0-b37f-30b8-beb7-1e687fa1bcce | -4.31462 | -43.99643 | 2025-11-09 04:16:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59b3e0d6-978d-3525-9f95-5b7811398d73 | -3.14095 | -50.16278 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18ee825a-304b-3795-91b2-b598b6b63a02 | -3.66709 | -51.16452 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6442e93-e0a2-309a-9a56-cd4936bda2d9 | -4.83741 | -42.84471 | 2025-11-09 04:16:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ade9d181-c251-3c8b-ba27-0a99404854b0 | -4.75764 | -38.67884 | 2025-11-09 04:16:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7a1b9b56-4721-3810-a9cb-6dc0b93be1c6 | -3.76784 | -45.87177 | 2025-11-09 04:16:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc2b66f9-5815-325f-a558-53828bba8c8a | -2.60582 | -49.23176 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 70da3a10-9b06-3d41-92bc-bebba5c52e69 | -3.76469 | -44.28984 | 2025-11-09 04:16:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa25a332-4f37-383e-8def-f36befff83f2 | -3.09504 | -50.31782 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3715aa77-a96d-3aaf-a43b-afb30a7c33de | -3.07357 | -49.38157 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01e0e747-93b0-3527-961b-987ac182d1a3 | -3.32978 | -53.24677 | 2025-11-09 04:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3143ea3f-6ed6-38f9-85cc-4c2a0f3a4190 | -3.09798 | -49.68492 | 2025-11-09 04:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a9296c0-6923-3f9f-87b4-dfb210ac780c | -2.48319 | -48.23351 | 2025-11-09 04:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f575015-7414-30ca-85b1-f8d498096ccd | -2.98973 | -52.82104 | 2025-11-09 04:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b461fe68-a115-3dde-bcb9-3c6d71a4721b | -5.49154 | -39.07452 | 2025-11-09 04:16:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b5f52f49-0115-3663-b4ef-a1e6c8f712cb | -2.26954 | -47.84693 | 2025-11-09 04:16:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea074b3e-1523-3d9b-a8e6-bd7aa618d962 | -4.75829 | -49.39139 | 2025-11-09 04:16:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e798e744-6f9d-3a42-909c-5ec5db847315 | -3.35715 | -51.28486 | 2025-11-09 04:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cde257b9-e76e-3bd0-bf2a-1cff27ef992d | -3.73435 | -50.03705 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef9006d6-dd14-320d-9464-7ad8f7014496 | -3.07434 | -49.37681 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a269503d-cd25-347e-95ad-5bf61290086b | -4.57495 | -48.47727 | 2025-11-09 04:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b099f595-4145-3bde-84c3-e83d514649c4 | -4.52456 | -40.35828 | 2025-11-09 04:16:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c069553-d825-3aca-85d7-fa8df7691426 | -3.4078 | -50.25727 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20d05099-ee29-3def-840e-02a3bf0fe21d | -4.2409 | -44.67175 | 2025-11-09 04:16:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e26f823-d8c3-3c3e-9cb4-1245655328bf | -3.71944 | -43.06549 | 2025-11-09 04:16:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a389588f-0bb5-3a3e-af77-d4f919f720d1 | -2.59118 | -49.23422 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38138e66-8755-3346-abb0-cb922b4d60f4 | -3.80617 | -45.99935 | 2025-11-09 04:16:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df96f474-9a54-33e5-8a7b-4e461be21eaf | -3.3141 | -50.12867 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cee643c0-6384-3a9b-9cc4-ae602de92c9b | -2.54695 | -45.15561 | 2025-11-09 04:16:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2ef6f0d-8043-316e-92e5-0e7094265cfd | -4.291 | -50.66746 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README18.md)
