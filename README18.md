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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1642c3b1-58e5-3378-8c88-bb0a32c7eb09 | 1.35959 | -50.63016 | 2024-11-27 01:11:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.0 |
| fe3ef077-9d83-3fc2-9164-002fa22de260 | 1.36123 | -50.61857 | 2024-11-27 01:11:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e3ca2ec5-7d63-3341-b98b-96db6f26fa1c | 1.47489 | -56.05553 | 2024-11-27 01:11:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4be121b5-414f-3ca3-8682-fd590a96b7e0 | 0.94476 | -50.74543 | 2024-11-27 01:11:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8ea3c759-9ea2-3cf2-acc5-09a8a52ccb56 | -3.5226 | -52.1448 | 2024-11-27 01:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 8269f26a-bded-3d4e-8053-562a8b1ff404 | -2.6988 | -45.6481 | 2024-11-27 01:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| cca81179-633d-316f-b12f-5dec059f1270 | -2.8424 | -46.8413 | 2024-11-27 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| a3db67b6-27df-32c2-8719-2178111bfb3b | -1.6813 | -52.4333 | 2024-11-27 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 9e35b29e-43d7-3dd1-8e37-7d16173ebd82 | -3.1876 | -48.4387 | 2024-11-27 01:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 198.5 |
| ab086554-28bc-35af-87d9-4daa03b25b67 | -3.3199 | -44.0607 | 2024-11-27 01:20:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a4dcb4ef-aa7b-3ca1-8128-732eefbd41cd | -3.0392 | -48.5297 | 2024-11-27 01:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 34e0f016-8218-3508-8236-81d2cf1464b8 | -1.9562 | -45.7137 | 2024-11-27 01:20:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 6324e90f-bbc3-3b4f-b1c9-f52265266497 | -2.824 | -46.8199 | 2024-11-27 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 30a47889-ded0-3bc8-9d33-1b45fdf6e74b | -4.7381 | -46.5816 | 2024-11-27 01:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 36.6 |
| a0ab07b3-7206-3e7f-9008-4d75cd024c78 | -3.0577 | -48.5291 | 2024-11-27 01:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| c6d228d5-395f-3f80-ae02-4aa30ad9fa0b | -5.9975 | -45.3607 | 2024-11-27 01:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 408f5d5c-2e75-3c0c-b88f-47e2735f0f7e | -3.986 | -48.0626 | 2024-11-27 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 5dd7d1cd-e114-3abc-8058-c2663c46f9c4 | -3.0393 | -48.5082 | 2024-11-27 01:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 178.5 |
| c953df9d-afe7-3478-82f7-a22a5d878b4a | -3.1506 | -48.44 | 2024-11-27 01:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| a8b73f58-774c-3890-a16d-429dfeb6290a | -4.7383 | -46.5595 | 2024-11-27 01:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 43.1 |
| f7516f99-99dc-38db-af02-ff771fb5eec8 | -1.6629 | -52.454 | 2024-11-27 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| e9c886e2-d0fa-306d-8fe3-a57b3ba41abd | -2.9967 | -45.4809 | 2024-11-27 01:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 7f4415e8-dab9-344d-a755-7266fea54dae | -4.7195 | -46.5827 | 2024-11-27 01:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 6ce9cca3-750b-3e07-b416-1393cf993cee | -1.9561 | -45.7361 | 2024-11-27 01:20:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 8e4ec61e-f4ea-3b7f-bbdf-100c96a67851 | -4.1417 | -43.8135 | 2024-11-27 01:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| d009961d-36bb-33b1-a106-d7ca91a3efaa | -3.1691 | -48.4394 | 2024-11-27 01:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 327.1 |
| fb023c24-fe0a-3c53-837a-73e9c31987c7 | -3.9859 | -48.0843 | 2024-11-27 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 6ac01455-4651-33e2-8b5f-42193aca30cc | -1.6629 | -52.4336 | 2024-11-27 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e4344385-be88-3778-92d3-758e9841d854 | -3.1692 | -48.4179 | 2024-11-27 01:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 6bcf1b9c-4990-33c8-b488-c73aa875fd25 | -3.0578 | -48.5076 | 2024-11-27 01:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 258.1 |
| 54889d1e-910c-3815-a7f0-629de48e1f4b | -3.1877 | -48.4172 | 2024-11-27 01:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| a388ca25-43cd-3d88-8e8d-f6fae2282286 | -3.169 | -48.4609 | 2024-11-27 01:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 442ab3e8-ce4d-303c-b223-d26e428cefc7 | -4.1419 | -43.7905 | 2024-11-27 01:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| fe8b2fd0-5d94-39be-b7fc-23e5aaa0cd52 | -2.8425 | -46.8193 | 2024-11-27 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 7eeeb40a-b1e7-3f80-adc2-56dcf6b56107 | -2.8347 | -54.1125 | 2024-11-27 01:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| a018e7f6-3f65-356c-8426-92607d8af007 | -3.5226 | -52.1653 | 2024-11-27 01:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 72191cfe-9ea0-3615-b70e-055531a641ad | -3.9674 | -48.0851 | 2024-11-27 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 8b22c949-91d4-3c43-a687-9809d0582811 | -4.7197 | -46.5605 | 2024-11-27 01:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 863a1356-3c90-36ee-a3ec-057220787ac0 | -3.9675 | -48.0634 | 2024-11-27 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 815f75ba-c678-35f1-aee7-39719a345711 | -2.6987 | -45.6705 | 2024-11-27 01:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 9a1ea63b-3bd3-3030-9af6-697e0b6fdc66 | -4.2115 | -50.8782 | 2024-11-27 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1ad43a14-aba3-368b-b780-c7e520e77f84 | -1.6813 | -52.4537 | 2024-11-27 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 186c8f23-1b6c-39fd-8e69-e5da5d3f03c6 | -2.9968 | -45.4584 | 2024-11-27 01:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 105.5 |
| eb34b84a-5c3b-3774-bbe1-c35e80bd1223 | -3.0154 | -45.4577 | 2024-11-27 01:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 7fadab5c-e1d3-3bde-8263-fe19b5d255a1 | -5.9788 | -45.3621 | 2024-11-27 01:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 48bd4adb-6976-3a1a-a4d9-c35752c86eb7 | -2.8346 | -54.1326 | 2024-11-27 01:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 89e80a6d-1953-3231-aadc-4f2331d0acc7 | -4.1604 | -43.8125 | 2024-11-27 01:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| a2368fca-3bb4-3fe7-b79e-8da4406c6650 | -4.2114 | -50.899 | 2024-11-27 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 69a17e6f-7591-39f0-a388-f42a62fcccff | -4.2115 | -50.8782 | 2024-11-27 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 3fc50679-359f-3d45-87de-cbbeb396ec9c | -3.1876 | -48.4387 | 2024-11-27 01:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 145.5 |
| c137934a-d99f-3855-aa3f-a39621cab9b9 | -2.8424 | -46.8413 | 2024-11-27 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 2eb65479-a32e-3499-970f-c184751b01ba | -3.1692 | -48.4179 | 2024-11-27 01:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| d76f1bb8-8d1c-3858-9126-189a4fe1504f | -2.8347 | -54.1125 | 2024-11-27 01:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| f023b236-993f-31dd-9252-3632b74e805e | -2.1928 | -53.7839 | 2024-11-27 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 0200c52e-0033-3252-ac6e-6587c7934fed | -3.0393 | -48.5082 | 2024-11-27 01:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 244.4 |
| 41fa42f9-b066-3998-b3af-4f1e6e9febca | -4.2237 | -48.6557 | 2024-11-27 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| a56bf6ac-484e-32b2-bdde-ca79c211acba | -2.824 | -46.8199 | 2024-11-27 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 9ee57447-9d1a-3afe-9ca0-d01c584e6b93 | -3.0578 | -48.5076 | 2024-11-27 01:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| c5849a70-5fb1-3cf3-a971-9c7f1514e09d | -3.1691 | -48.4394 | 2024-11-27 01:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 369.4 |
| 301c6704-59a0-3edf-a263-e7fd608f39e6 | -3.5226 | -52.1448 | 2024-11-27 01:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 89675293-732d-3842-98f4-4e8e7bec9978 | -4.2299 | -50.8983 | 2024-11-27 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| a8a5cd61-f306-3138-9865-b53ecb0bf207 | -3.9675 | -48.0634 | 2024-11-27 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| df5afdc0-48b0-3677-bed7-9e4c3cd58f01 | -4.1417 | -43.8135 | 2024-11-27 01:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| c6dedf08-9a14-3dd1-a0e6-719ac798772d | -3.541 | -52.1647 | 2024-11-27 01:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| ddf8dfcf-2854-3c9b-947c-fee4c6800dcd | -1.6629 | -52.454 | 2024-11-27 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f9538908-1372-3168-bd8f-d03c0a38188d | -3.5226 | -52.1653 | 2024-11-27 01:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| d8cb04bd-d9c4-3f2f-bc1c-1397ac835e69 | -4.7381 | -46.5816 | 2024-11-27 01:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 46.1 |
| d669a074-5c21-3eda-9236-691a16851875 | -3.9674 | -48.0851 | 2024-11-27 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| ce43abb9-6054-3117-8197-6e412b4adc52 | -1.6629 | -52.4336 | 2024-11-27 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 20a71680-62fb-34c2-b10c-9d50eafe7ca8 | -3.0392 | -48.5297 | 2024-11-27 01:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 148.2 |
| f5afe471-d362-30fa-807a-29581ea31306 | -5.9788 | -45.3621 | 2024-11-27 01:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 8ce211b2-6542-3b97-8b06-d6684f4e4ec6 | -3.6529 | -44.4807 | 2024-11-27 01:30:00 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 1711ee25-9ea5-3706-a3eb-fd72d34fea5d | -3.058 | -53.28 | 2024-11-27 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| c26f2e2c-cecb-34d4-80b0-bdbe15701493 | -1.6813 | -52.4333 | 2024-11-27 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b023dabc-9143-3ae3-bf57-152073d801c4 | -2.9968 | -45.4584 | 2024-11-27 01:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| a5ffbc65-caa3-3ee2-919f-1b2c532d6e5f | -4.7383 | -46.5595 | 2024-11-27 01:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1016d94a-a0eb-3506-9e0b-622d65b7d587 | -4.1604 | -43.8125 | 2024-11-27 01:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 923a2095-2bb5-31f7-9933-25b45ef747d4 | -4.7195 | -46.5827 | 2024-11-27 01:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 46.3 |
| d37a461a-6ad6-3a59-bb85-ad743f5b413a | -3.0577 | -48.5291 | 2024-11-27 01:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 44d63440-6a47-311d-a093-8f53e8a75d2b | -2.8346 | -54.1326 | 2024-11-27 01:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| ed2b2801-3521-3e03-8b7f-fa8e15e9ee83 | -4.2114 | -50.899 | 2024-11-27 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| c729a5e2-f292-3b25-a0eb-4aabacead0e9 | -1.6813 | -52.4537 | 2024-11-27 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| afcbedfe-692a-35c7-ae1d-fc1eef14d8cb | -3.5411 | -52.1442 | 2024-11-27 01:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| be9ef437-7377-3b70-a17b-59016e3b975e | -1.9376 | -45.7365 | 2024-11-27 01:30:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 4a94b2d6-448e-3153-af5b-c5949fa7b17f | -3.1877 | -48.4172 | 2024-11-27 01:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| bf77f5cd-741c-36f5-a05b-713c348fe158 | -4.1419 | -43.7905 | 2024-11-27 01:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 5dc3e359-1e60-34b4-8a40-c27b1d515e1c | -4.7197 | -46.5605 | 2024-11-27 01:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 7eed5ecd-ad8a-34b6-85f4-3d155b31b56e | -2.8163 | -54.133 | 2024-11-27 01:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| a359c009-8731-3c85-8acc-d66edb8d3c60 | -1.9376 | -45.7141 | 2024-11-27 01:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e42a933a-23fc-3260-8600-6db96e3bee24 | -3.5226 | -52.1448 | 2024-11-27 01:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| e3cf48c9-f35d-3ca0-b6d0-a785712574aa | -3.0948 | -53.2791 | 2024-11-27 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 68222a9f-e90e-3824-81c1-73364da46b6e | -3.1133 | -53.2381 | 2024-11-27 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 0bfd89bd-6a3d-3198-b135-9087438fe61d | -5.9788 | -45.3621 | 2024-11-27 01:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 855cf50c-fa0d-320c-b0af-6fc27182d980 | -5.9975 | -45.3607 | 2024-11-27 01:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 70a2f9ec-03ee-36cb-a22b-4b2a135e982d | -4.7381 | -46.5816 | 2024-11-27 01:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 1d757215-bea8-32c4-b79e-0a6f5c1bec3d | -3.9859 | -48.0843 | 2024-11-27 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 388fc896-e36d-356f-9817-c6b7fd5d0c05 | -4.7197 | -46.5605 | 2024-11-27 01:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 1b566495-0574-3734-a5ba-6b24444b455d | -1.6813 | -52.4537 | 2024-11-27 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 817f1792-e12a-3410-acff-62528405c0de | -4.2115 | -50.8782 | 2024-11-27 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| ef1ec93c-6150-3735-87ce-6bd21d7e55e0 | -3.1133 | -53.2583 | 2024-11-27 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 357.4 |


[Clique aqui para ver as próximas entradas](README19.md)
