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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f7b7cf9-6a7d-38c9-9c28-3aeb2dc6654c | -19.70135 | -54.61485 | 2025-06-23 04:00:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86f2748c-3fb4-32be-9674-0b12ddaaec89 | -22.25355 | -50.03704 | 2025-06-23 04:00:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 14919da4-2898-3bfd-a145-e959ff3c80ea | -23.04582 | -49.89654 | 2025-06-23 04:00:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 09fa83c3-4257-307e-bd55-cae4c6a8c50c | -20.70973 | -50.06734 | 2025-06-23 04:00:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f4b1b6f8-e44d-3b71-8887-0fd5bb0d7f92 | -23.63291 | -46.42558 | 2025-06-23 04:00:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 33485e04-3999-3c84-9759-7b51456872c5 | -19.5181 | -45.3098 | 2025-06-23 04:10:00 | GOES-19 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 54.4 |
| f6fa4b57-9a91-31b4-9bc3-1a4fb52044bc | -4.42288 | -42.1193 | 2025-06-23 04:19:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 64f7b535-88ac-303c-8fe6-5fd3a8ffb217 | -4.66766 | -41.96048 | 2025-06-23 04:19:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7478a956-bb17-3dff-81ca-fefb45cb4a23 | -19.5181 | -45.3098 | 2025-06-23 04:20:00 | GOES-19 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 8605b8e2-8f1f-382e-a7f0-456cfea05a00 | -7.45269 | -45.56713 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb6ddaf9-5daa-3ffb-b102-329f4dffa341 | -8.09256 | -43.14876 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 005ba712-76d7-384e-bd03-94acb181e75a | -9.34805 | -40.48079 | 2025-06-23 04:21:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 57efa50e-d409-3523-b560-3c753ba1b720 | -7.44825 | -45.55205 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f57cce15-1d19-3d94-8ec6-782352a3dcb6 | -9.14863 | -48.9764 | 2025-06-23 04:21:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b0dad33-968a-32a2-b0d6-56f28cdcd79e | -11.58327 | -44.65078 | 2025-06-23 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e097f36-a7db-38a1-a750-95e91fd6a068 | -7.32 | -43.20817 | 2025-06-23 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9854007c-0770-3179-b834-77fe248c7ee1 | -7.44214 | -45.52596 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4c97ebd-ce0d-3781-9b64-051b980a7f2d | -11.57878 | -44.65751 | 2025-06-23 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da8f1588-3afb-3688-8e00-f18fe8874dff | -7.45325 | -45.56363 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f230dc1a-92f5-320f-af14-5162d0c4bf37 | -8.06453 | -43.11074 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| cdde968e-c8fc-3b02-97a7-2cc173b79567 | -8.11091 | -43.14391 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 2111db1d-314d-3db9-93fc-496a8594ea16 | -10.15409 | -48.98793 | 2025-06-23 04:21:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af8693e6-d9df-35a4-8054-8cd201f1347d | -8.65339 | -49.56289 | 2025-06-23 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b173007-b8ba-3504-a710-cac128c41bc7 | -11.5799 | -44.65025 | 2025-06-23 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db24a46d-bc9b-3c77-8baf-e10e5e04ec60 | -5.57227 | -45.21101 | 2025-06-23 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e5aa531-f810-3192-a949-ba7aa16af78b | -7.43936 | -45.54346 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec602dd5-7fe1-38d0-a208-c6af9636e489 | -7.47032 | -45.55538 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c734cd2-bfcd-3ba9-a1ab-d4044aa56693 | -7.87425 | -47.88232 | 2025-06-23 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae9a085b-bf0a-3d04-a707-b05b3620fbb3 | -8.06395 | -43.1145 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 2c6c87c2-035c-354b-b2bd-43b3100c6022 | -7.26925 | -45.35837 | 2025-06-23 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36f69280-c797-3e58-a6ed-39fd0d9f87e5 | -8.48182 | -47.50393 | 2025-06-23 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6fb5ef19-54c8-3ebc-8894-3fe01ffdc3fe | -7.46699 | -45.55484 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 216ff535-1bf0-3d39-b935-01aac9b8b670 | -5.10681 | -43.14642 | 2025-06-23 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 45b40b27-69a3-3f2f-b1ef-f6f11ca4fff4 | -7.30466 | -43.21709 | 2025-06-23 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| c3b525b8-2033-3d17-a3e3-be597a158003 | -7.4538 | -45.56012 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 882d59c8-f33c-35b9-9525-8132377e177e | -8.40541 | -44.60634 | 2025-06-23 04:21:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a592d8c9-4003-373e-a6ee-a9253f375608 | -8.06212 | -43.11715 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 28d70f6b-3b71-3545-ad22-0029dda53493 | -7.3092 | -43.21027 | 2025-06-23 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8bb41544-da00-3155-9406-edb969e1442e | -8.06569 | -43.10322 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f2a5021e-93ae-36ed-a56e-e68b53cac039 | -8.10689 | -43.14713 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a2d59295-dab3-382c-b034-54652c8849d9 | -8.0667 | -43.11015 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 1b6254b0-a542-3241-a193-524707a7ae89 | -10.98654 | -47.40744 | 2025-06-23 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 920c6bcc-7b10-3894-b89c-8380e00db1ed | -8.06727 | -43.10639 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| d256d0b3-f8c2-3507-ac13-2d6c264b1106 | -11.10804 | -46.66022 | 2025-06-23 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8963565-0be0-3f8f-b290-0c1a8db5a548 | -7.44714 | -45.55907 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64b27e88-2419-32fd-826a-b79a4b65acf6 | -8.37724 | -47.43921 | 2025-06-23 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8070da9-addd-30d8-83c1-fa2ab233d4fe | -7.31205 | -43.21448 | 2025-06-23 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cf56cd58-8471-34ef-a046-7247e7740fab | -7.44769 | -45.55556 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b91e011-a0f3-34f5-bf75-1ce653bf9ff0 | -10.06499 | -49.66375 | 2025-06-23 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21f2b037-1975-3aeb-a655-5ce45e39c9bb | -7.44436 | -45.55503 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ea3dcef-b973-3e93-86e8-5e56c3f47e6e | -11.10411 | -46.66327 | 2025-06-23 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bf6a11e1-3e4c-37f0-bf02-61fd9dd2fc93 | -7.31317 | -43.20712 | 2025-06-23 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 579b5284-5712-3e82-a045-54a3feab385c | -11.10077 | -46.66273 | 2025-06-23 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fed08dc0-269c-30aa-b58d-7a29ee46d0f0 | -5.57282 | -45.20751 | 2025-06-23 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22e88482-b024-3262-8cfa-8d984820dd9a | -7.30864 | -43.21394 | 2025-06-23 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 340c0b4e-95ff-33c1-bffb-799516d3c106 | -10.14968 | -48.99165 | 2025-06-23 04:21:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e9b2863-ab37-3d4b-b8d4-ff401553fc75 | -8.06279 | -43.12201 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 41c3bb2e-1ba1-38df-a3dd-2f21ed2ed732 | -5.49341 | -43.98171 | 2025-06-23 04:21:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| ac65c8b1-7e7d-3f81-adf7-ede2f4a0f966 | -11.93224 | -44.81255 | 2025-06-23 04:21:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78787ce5-b192-3a83-bd6a-f25bf0792d2d | -7.44936 | -45.52351 | 2025-06-23 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dbd12b9-0f39-3075-8d7e-17dac17fa522 | -10.45134 | -47.02219 | 2025-06-23 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f99c365-754b-3b45-81d6-6ef7b5d5b729 | -7.46436 | -45.55821 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b0b9476-efea-308c-a99c-709ad53506e4 | -9.41723 | -48.41756 | 2025-06-23 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3f7285ea-366d-3dd9-b7b3-38f135fc69cb | -9.41792 | -48.41344 | 2025-06-23 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9803eaf0-3c93-3814-a31f-59bf88e6114d | -6.89385 | -44.64701 | 2025-06-23 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73f42e5b-3a9b-3057-b369-beb059348934 | -9.41654 | -48.42167 | 2025-06-23 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 574d7309-68cb-36d1-8def-905b5251cdae | -8.48467 | -47.50835 | 2025-06-23 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bec8ec1d-dea3-3432-8469-0c4d8b035f98 | -11.58216 | -44.65804 | 2025-06-23 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cae6e0e-c59b-3167-b305-54c857ee3b23 | -8.11779 | -43.14497 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4e246d94-f51d-3bd8-9279-60861d343457 | -5.49396 | -43.97823 | 2025-06-23 04:21:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 4b2c5ebf-c26b-3560-b8db-64d8d4bfc87c | -8.06613 | -43.11391 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 4d4d9916-1c92-34f8-816c-1494de299365 | -8.06326 | -43.10962 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| b7de7ee2-5eb9-3db7-9ae7-ecdeb0df8cc4 | -7.46643 | -45.55835 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4feb9c3a-69ab-3c47-b89a-5c06e7433db8 | -7.3149 | -43.2187 | 2025-06-23 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a0d22691-01e7-33b1-944f-76b035b2e99b | -7.31944 | -43.21187 | 2025-06-23 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 454f1541-e17c-383a-9c07-9e97c896d9b7 | -10.50578 | -53.58666 | 2025-06-23 04:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2ce80926-b74f-3fd8-942e-0dc3b604b87f | -7.44936 | -45.54504 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04f2870f-076a-3d03-9f7d-d86d2a42b66a | -5.41912 | -45.11463 | 2025-06-23 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebce1cfe-8795-3ea8-a92c-e4fd7d688260 | -8.38071 | -47.4398 | 2025-06-23 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69ca7060-ce1b-326e-9810-9fde8259f653 | -10.06118 | -49.66309 | 2025-06-23 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8cd48895-da44-372f-9fb1-c1feb305526e | -5.41592 | -47.56939 | 2025-06-23 04:21:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57292093-79d2-30b7-a0d3-906d8918a4bc | -7.31887 | -43.21556 | 2025-06-23 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 383c03c6-41d8-3390-9d40-7152e2e8569b | -7.30807 | -43.21762 | 2025-06-23 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 4f09c86e-7aec-3864-8703-b55b854c9c23 | -10.03501 | -48.67665 | 2025-06-23 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe102ffa-b7e3-3dbd-9a62-06f4480fe5f9 | -11.10469 | -46.65968 | 2025-06-23 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76fc5075-c91d-3b50-b218-64c190a4d5f2 | -9.42082 | -48.41817 | 2025-06-23 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 74489431-ecb1-3555-bea3-459282bd526f | -7.35362 | -45.33583 | 2025-06-23 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17460f59-d3fb-33aa-8e14-933021a41aa2 | -7.87358 | -47.88638 | 2025-06-23 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb457d7f-ceae-3099-924c-62a10a8fd01d | -12.23549 | -44.42093 | 2025-06-23 04:21:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac26effc-c988-39f8-9011-c404073e7d12 | -8.48753 | -47.51276 | 2025-06-23 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e94ed41-d2bd-3728-be9a-38460e4f06a3 | -7.45436 | -45.55662 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a5de88c-3e2b-3283-83c7-c239185e3b8f | -10.15211 | -48.98432 | 2025-06-23 04:21:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26105206-0746-3347-87d2-819c539d32b9 | -5.57616 | -45.20804 | 2025-06-23 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 521ccbc0-5006-3912-a1c0-18a78f747048 | -11.10019 | -46.66629 | 2025-06-23 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1775297d-0c97-38fc-a885-7388d36dc88f | -10.0696 | -49.65971 | 2025-06-23 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d97941f-0989-3d0c-8e5f-353d37ba6ab8 | -11.31658 | -47.18229 | 2025-06-23 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fd30d1d-1c09-383a-8d9a-376f881c1ef4 | -8.65479 | -49.5612 | 2025-06-23 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 702e7b39-d9cc-3cae-925e-65745294e203 | -10.2956 | -52.56501 | 2025-06-23 04:21:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72ea955a-06e5-370c-beed-1a3c7133e4b4 | -7.95082 | -46.04398 | 2025-06-23 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c2f510c-ea08-38bd-baf9-08c8aa883dbf | -7.43992 | -45.53996 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README6.md)
