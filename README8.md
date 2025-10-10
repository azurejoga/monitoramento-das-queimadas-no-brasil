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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1dddb270-b117-35ee-b247-c0466e49fc46 | -14.8898 | -47.1543 | 2025-10-10 01:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 7ce04fc8-f5b5-3df5-9494-db67152f9e09 | -13.0773 | -43.8537 | 2025-10-10 01:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 1832b6e5-e4d3-36d6-a4a4-a5bf1cd60541 | -17.9382 | -44.9909 | 2025-10-10 01:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 6db5a545-462a-39d7-a2c7-ca56d1efeb30 | -13.058 | -43.8571 | 2025-10-10 01:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| d1a212a6-b1d8-3862-b07f-875bd7ef2dbe | -7.4154 | -45.9211 | 2025-10-10 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 35107778-353d-3811-9c10-4bcf30261622 | -3.7937 | -49.4211 | 2025-10-10 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 8eceb9ea-a80f-3e37-88ab-d4640742cf9f | -10.1714 | -44.5496 | 2025-10-10 01:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 9727ed9e-8df9-3241-962a-04cac77b0dfe | -13.0778 | -43.83 | 2025-10-10 01:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 62a96828-9623-3f4c-8dc2-594340be4d55 | -6.5851 | -44.6098 | 2025-10-10 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 6281c515-23ba-3777-aceb-ff01be142b9d | -3.7752 | -49.4219 | 2025-10-10 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 3b313fcc-a6c1-3460-b536-02510bc92f91 | -8.5409 | -46.1282 | 2025-10-10 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| bc66a57f-e799-3cd1-b63b-95f4d1a9fd55 | -8.5407 | -46.1507 | 2025-10-10 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 4dede84b-0be5-3886-aede-504ca393cfaa | -17.9577 | -45.0103 | 2025-10-10 01:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 338b649d-e6a1-3fc8-b875-f255fcfd135c | -6.5849 | -44.6327 | 2025-10-10 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| ec1c1eb9-0993-3c18-9b88-4e15653c1cc3 | -14.8703 | -47.1576 | 2025-10-10 01:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 260fa238-e7ae-3666-bdb0-8081e791fb62 | -10.1711 | -44.5727 | 2025-10-10 01:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 0c09aa00-ea3d-30f7-b3b6-63cb6171e1c6 | -17.9175 | -45.0194 | 2025-10-10 01:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 3ce2ba00-9579-3384-a274-098bd2a8cb62 | -3.7936 | -49.4424 | 2025-10-10 01:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 3696e498-e6bf-37b4-a292-12280c9b739d | -13.058 | -43.8571 | 2025-10-10 01:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 0edb3c1a-c232-3ed4-87a2-42449a4a3156 | -8.1996 | -43.3189 | 2025-10-10 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.1 |
| 18f8d1ae-1a23-3341-8a23-dfcd6dd36588 | -13.0778 | -43.83 | 2025-10-10 01:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 6597aa22-577a-3b0e-a724-f05b3ad6a160 | -3.7751 | -49.4431 | 2025-10-10 01:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 61f73873-e6a2-3cd4-a3b4-9fc8b2d7b352 | -15.9195 | -43.2779 | 2025-10-10 01:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 91.6 |
| ce65277b-da4f-3ed0-95aa-4ef0e7e4a77b | -13.0584 | -43.8333 | 2025-10-10 01:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 86a01bae-0f94-37db-b6e8-5998660beff0 | -6.5851 | -44.6098 | 2025-10-10 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 9b9d1c36-f20d-30e5-b289-23e57369aa8e | -6.5849 | -44.6327 | 2025-10-10 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 4863466b-b320-37b3-b9ee-9889f34f1e5c | -7.4154 | -45.9211 | 2025-10-10 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| d9530e74-652d-3a2a-b08b-92b4b531341d | -8.1993 | -43.3424 | 2025-10-10 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.1 |
| 44b44a2d-1067-3773-bb27-735f2d0b43b3 | -17.9369 | -45.0388 | 2025-10-10 01:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 4a383d92-d246-3404-97b7-0361eae0077a | -18.6497 | -43.9301 | 2025-10-10 01:30:00 | GOES-19 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 107.6 |
| fd719536-7be7-3c6d-8949-0ff8ef3c54b6 | -3.7937 | -49.4211 | 2025-10-10 01:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 4eb2580a-1245-3456-81ce-893de9088b89 | -17.9382 | -44.9909 | 2025-10-10 01:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 1bd25c0b-37a5-3ce0-a2e4-8aa7f5b47e5b | -12.629 | -45.0749 | 2025-10-10 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| b65e842f-9843-359a-ba90-d88dc869d3ba | -3.7752 | -49.4219 | 2025-10-10 01:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| c606a449-5052-3ed9-99cd-0e94df6989c8 | -12.6294 | -45.0517 | 2025-10-10 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| ebf57732-7b7a-36dc-aae2-d49b3079f895 | -17.9376 | -45.0148 | 2025-10-10 01:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 346.6 |
| 4858afce-03c3-3d4d-8db6-ac65871fd108 | -10.1714 | -44.5496 | 2025-10-10 01:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| dcf895c9-fa65-3ca8-854e-48843c8e4678 | -6.5849 | -44.6327 | 2025-10-10 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 244720ff-3fd4-3057-b6e1-8a7e561249e2 | -3.7937 | -49.4211 | 2025-10-10 01:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 7de5b49f-37dc-3409-870e-12794ff4a342 | -17.9577 | -45.0103 | 2025-10-10 01:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 913b1b32-8dbd-3c70-b2cb-5598be661396 | -6.5851 | -44.6098 | 2025-10-10 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 2c616258-6dc6-3413-8daf-90804a8bf8ce | -17.9175 | -45.0194 | 2025-10-10 01:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 51b5c8bb-8008-3ccb-bdee-c687b56a2e4b | -17.9382 | -44.9909 | 2025-10-10 01:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 7f1c83cb-db7b-337d-8c64-7f7f2a19ab0f | -17.9369 | -45.0388 | 2025-10-10 01:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 0044e2d2-7ab7-3b30-9bfd-3101241f323f | -7.4154 | -45.9211 | 2025-10-10 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 75136d89-fbee-329a-802f-99c713f7e4c6 | -8.1993 | -43.3424 | 2025-10-10 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| 536178e9-eb72-3f10-995a-8eed4bc2f243 | -12.6294 | -45.0517 | 2025-10-10 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 101e2076-bcdb-360f-947d-30b14d63643b | -8.1996 | -43.3189 | 2025-10-10 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.4 |
| 424a19f9-aa66-3859-9fc7-bb571f25b35a | -17.9376 | -45.0148 | 2025-10-10 01:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 321.5 |
| 119ebfdb-407e-3226-b02f-98d22057cda1 | -8.1993 | -43.3424 | 2025-10-10 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.2 |
| a75d956c-dab9-3f4d-9b8e-73526a5eb54a | -17.9577 | -45.0103 | 2025-10-10 01:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 91.1 |
| a59de03c-02b9-3e41-a101-f8ce99613675 | -10.1711 | -44.5727 | 2025-10-10 01:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 29e19d1d-4b9e-3758-9ce0-ef37b191fd2d | -8.5221 | -46.1301 | 2025-10-10 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 74cd7655-1c97-3420-a981-2759144d2b5a | -13.0584 | -43.8333 | 2025-10-10 01:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 7186dfb2-798d-3d84-ab72-b805602729e5 | -17.9369 | -45.0388 | 2025-10-10 01:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 123.2 |
| a7a25709-dc98-3be7-8019-31330ad3a658 | -13.0778 | -43.83 | 2025-10-10 01:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 7af93a1b-1639-3506-90e9-cba8f043dc67 | -10.1517 | -44.5984 | 2025-10-10 01:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 8c3e4476-516d-3ada-badd-46179f79e2e5 | -8.5032 | -46.1321 | 2025-10-10 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 4d2e3532-21d7-3511-9883-57394d2b1763 | -17.9376 | -45.0148 | 2025-10-10 01:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 246.7 |
| 5f5b9264-c815-3a67-b25a-41ae53a6f9b9 | -6.5849 | -44.6327 | 2025-10-10 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 57e051f1-7e45-3a07-8961-fe3ad931c8de | -17.9175 | -45.0194 | 2025-10-10 01:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 45f7e028-773e-355c-b831-252c398ffc59 | -8.1996 | -43.3189 | 2025-10-10 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.8 |
| 1b45dfa1-5f75-3fd1-89a4-4c2e9f6571ef | -7.4154 | -45.9211 | 2025-10-10 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 71f0cb66-638a-3175-8c73-3e157cfff925 | -17.9382 | -44.9909 | 2025-10-10 01:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 27d83590-0960-3a99-a40c-dd466cae6b57 | -10.1707 | -44.5959 | 2025-10-10 01:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 218d0904-26ab-35ff-84fa-283bac07253a | -17.9369 | -45.0388 | 2025-10-10 02:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 088345d2-4f20-3f9b-ac3f-bf1c4a152b6d | -10.1707 | -44.5959 | 2025-10-10 02:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 1d23621b-0779-322d-bf70-500765d55ae1 | -12.6294 | -45.0517 | 2025-10-10 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 1ed6fe84-22d3-364a-bc50-c0dd98fcdac2 | -17.9376 | -45.0148 | 2025-10-10 02:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 270.3 |
| 24558a97-a1f5-33da-babe-e283cdf11f37 | -17.9175 | -45.0194 | 2025-10-10 02:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 7a2d501e-612d-3e48-bb29-23069c4f13b2 | -13.0584 | -43.8333 | 2025-10-10 02:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| b260c43b-853e-3837-a2fb-cb39754ecd0b | -6.5849 | -44.6327 | 2025-10-10 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 486f3f72-765a-3c07-a630-e812470e69f2 | -8.1996 | -43.3189 | 2025-10-10 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 41.1 |
| 803e5ba3-efd4-3559-9ec7-00d487cad4c7 | -8.5032 | -46.1321 | 2025-10-10 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| e1bf6159-0146-358c-95d2-2bf91d725beb | -10.1707 | -44.5959 | 2025-10-10 02:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| e669004c-dfc4-3fd1-b122-54ea6df8b91f | -8.5221 | -46.1301 | 2025-10-10 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 3ed1e0e9-c8e5-319b-9ae3-9bb4469660df | -17.9369 | -45.0388 | 2025-10-10 02:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 120.6 |
| e33867c2-9626-3f77-b565-89637c80c7bc | -8.1993 | -43.3424 | 2025-10-10 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.0 |
| 50ca6e00-adb9-3200-8607-6e1d54db2924 | -13.0584 | -43.8333 | 2025-10-10 02:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 934504ea-cf7e-315f-8ad2-f22e09ebfcdb | -12.6294 | -45.0517 | 2025-10-10 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 3634cee6-ecf8-3b65-bcd1-c22c98702f1e | -17.9376 | -45.0148 | 2025-10-10 02:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 257.3 |
| 0387a600-e263-3df9-94af-38002e4e7919 | -17.9175 | -45.0194 | 2025-10-10 02:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 529a1df9-1ef3-3a48-989f-19da8408c975 | -6.5849 | -44.6327 | 2025-10-10 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 63352a3c-a7d9-3c52-bbdd-d90238c61923 | -10.79532 | -69.31082 | 2025-10-10 02:11:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a81e561c-dc79-3c92-8aae-603907aae443 | -9.66571 | -66.82119 | 2025-10-10 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 46af4fc0-2ced-3c16-ac18-f8efadface26 | -9.66736 | -66.83639 | 2025-10-10 02:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 288c2200-bbef-3f25-81b8-013ecb8cac36 | -17.9577 | -45.0103 | 2025-10-10 02:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 742d8678-75dd-3ffe-bd52-6e2fa5370bd9 | -17.9369 | -45.0388 | 2025-10-10 02:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 105.5 |
| f7ef44fa-1bbe-3843-b9c2-f8ae2c75fd23 | -8.1993 | -43.3424 | 2025-10-10 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.4 |
| 76fd473e-59b1-380e-a000-29dca63f7968 | -12.6294 | -45.0517 | 2025-10-10 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 0af810d1-3e77-3a95-af96-853d6a2fdd3d | -10.1707 | -44.5959 | 2025-10-10 02:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 0122fb0c-3abf-3a5a-9de8-81eda1df1306 | -18.6497 | -43.9301 | 2025-10-10 02:20:00 | GOES-19 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 402ce081-4145-3390-92d9-e3179230fee3 | -17.9026 | -57.5153 | 2025-10-10 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.9 |
| bdf9e158-a6db-374b-8f45-6301303f65b1 | -10.1517 | -44.5984 | 2025-10-10 02:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 5cf8c813-03bd-352a-b493-b51b873acf54 | -14.9372 | -46.7591 | 2025-10-10 02:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| a6fcc581-b45f-3256-ab6f-3e94d92b92a1 | -17.9376 | -45.0148 | 2025-10-10 02:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 254.6 |
| a4e08949-3c61-3736-b46f-5c4466e43cf9 | -8.1996 | -43.3189 | 2025-10-10 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 3decb8ce-e755-3fe0-8063-4be2fec772a4 | -17.9175 | -45.0194 | 2025-10-10 02:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 98.1 |
| aa0190ae-231e-328d-aeaa-e6657bc9eb09 | -10.1711 | -44.5727 | 2025-10-10 02:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 18c7908e-1578-3376-b20b-e445953bd0d9 | -14.9372 | -46.7591 | 2025-10-10 02:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 122.1 |


[Clique aqui para ver as próximas entradas](README9.md)
