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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56e45249-5303-3c31-934f-7e94c1da7931 | -3.9396 | -46.4229 | 2024-10-12 04:15:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| d94a906b-8626-310b-9846-8b406e025d8b | -3.9394 | -46.445 | 2024-10-12 04:15:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 45597027-98eb-3e38-846c-3863814d4de8 | -4.4538 | -44.5763 | 2024-10-12 04:15:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| a2441974-895a-364d-b603-f8f714041f88 | -4.5859 | -47.0968 | 2024-10-12 04:15:32 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 79.4 |
| ebf959cc-4e5a-35ed-b516-80998af3d50c | -4.5673 | -47.0977 | 2024-10-12 04:15:32 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 54f089a4-7996-3191-b1bb-118462ed1880 | -5.2486 | -48.0424 | 2024-10-12 04:15:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 1e5bde84-259e-374e-876f-b9d283f86e92 | -5.3997 | -45.3574 | 2024-10-12 04:15:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| c53c29dc-49f6-38a4-bf3e-3e95479ed766 | -5.381 | -45.3586 | 2024-10-12 04:15:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 0cf0ce33-a7a6-3e5e-9b7f-d030661fd293 | -6.747 | -59.3259 | 2024-10-12 04:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 5ddfb48e-39b6-36ef-8894-73a130a5c117 | -7.292 | -64.6676 | 2024-10-12 04:15:48 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| c5c3bfcf-023a-3202-af0c-ef4b2a96612d | -7.8715 | -54.7016 | 2024-10-12 04:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| f5225a83-8868-36fd-90c9-3ccc01390bc7 | -7.8713 | -54.7217 | 2024-10-12 04:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| d2b343f6-f4bf-3634-9f52-b89a03382c45 | -8.4231 | -55.4704 | 2024-10-12 04:15:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 88c5f939-ffe5-3312-893e-d0246800893c | -10.9506 | -44.653 | 2024-10-12 04:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| ea1f6595-ff37-336d-b82c-ddf612be6321 | -11.8377 | -58.8445 | 2024-10-12 04:16:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| a7355acd-4fdb-3be4-955c-b7d7a546bd01 | -12.456 | -54.5554 | 2024-10-12 04:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 129.0 |
| bb2e38d5-7b14-3e8c-81e6-dadd9b1ff324 | -12.4558 | -54.576 | 2024-10-12 04:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| cf395f1d-d2d3-39ec-a773-a87dbebf5224 | -12.437 | -54.5573 | 2024-10-12 04:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 8c4d85df-e57e-37e4-a513-c7c2249fbfe3 | -12.4367 | -54.5778 | 2024-10-12 04:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 9b0580b2-fed1-3ed2-9763-a1244ac018af | -12.7871 | -44.8639 | 2024-10-12 04:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 68bca433-385c-34ec-8ca9-977bd545487f | -12.8893 | -53.5194 | 2024-10-12 04:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 48a89e2a-3984-322f-9850-98e3d9a1d642 | -12.9464 | -53.5339 | 2024-10-12 04:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 237.4 |
| d8d902fa-721f-3520-854e-fd0b113c5899 | -12.9658 | -53.511 | 2024-10-12 04:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 130.1 |
| db6cf4be-645a-35b0-8dc1-b6718924c5e0 | -12.9655 | -53.5319 | 2024-10-12 04:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 184.2 |
| e6942a76-80fa-3221-8b0e-7655b416d0e3 | -12.9652 | -53.5527 | 2024-10-12 04:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 096f8e29-54c6-3ee0-9e9f-e28d8aa3a222 | -12.9467 | -53.5131 | 2024-10-12 04:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 165.6 |
| ce7c5b88-6d1c-34d2-8ee8-22af11d191ed | -12.9461 | -53.5548 | 2024-10-12 04:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 35044a22-6ee4-32a8-9647-25b4aa224992 | -13.7346 | -60.6079 | 2024-10-12 04:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 36907ce8-619d-3a3a-af95-42a74115f45e | -13.7153 | -60.6289 | 2024-10-12 04:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 8b1bb71a-5e47-3ab1-993a-c68c38cf96c9 | -16.9805 | -57.4404 | 2024-10-12 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| cf9611ce-ece0-36bf-afac-a52650195d63 | -17.1761 | -57.4585 | 2024-10-12 04:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| f10c3e0c-d42e-392a-9118-ff738f091728 | -17.6471 | -56.3084 | 2024-10-12 04:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.1 |
| e989f7b0-c471-3bc2-87ae-a263a3f38118 | -17.6467 | -56.3292 | 2024-10-12 04:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.1 |
| 30e24934-41c9-3ced-957c-e52072c85afa | -17.6679 | -56.2435 | 2024-10-12 04:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.4 |
| d44eaf37-9b91-3f21-b433-9888b3bcb462 | -2.8254 | -51.3401 | 2024-10-12 04:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| ac2fe73c-d0f2-3df9-97b2-fce125d79cc1 | -2.807 | -51.3406 | 2024-10-12 04:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ab984ace-0952-3357-90f2-559cdbf8ba42 | -2.7885 | -51.3618 | 2024-10-12 04:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| e3546f31-aace-30cf-a7c3-cc5d06c7b7ac | -2.7701 | -51.3622 | 2024-10-12 04:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| a2330273-a507-32e9-a26a-9d1dbcf9b1ee | -3.1611 | -50.3508 | 2024-10-12 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 7858c2a9-5b8a-316c-a783-bad88a35adac | -3.6979 | -50.1015 | 2024-10-12 04:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 3a2f779f-e511-3257-8ece-60092dcbafbf | -3.6978 | -50.1225 | 2024-10-12 04:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 5573030f-59af-3d27-a5c9-3553cce20ed4 | -3.9267 | -42.401 | 2024-10-12 04:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 39.8 |
| 0a022794-f80e-347c-9073-15bda8346c53 | -3.9396 | -46.4229 | 2024-10-12 04:25:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 159fb2b2-24a0-3684-b938-55fb206afd7c | -3.9394 | -46.445 | 2024-10-12 04:25:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1c77de38-d8d0-3197-b84c-2ec4bd9bed98 | -4.4352 | -44.5773 | 2024-10-12 04:25:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 097708eb-30b2-3da0-8d7d-1345793465ea | -4.4538 | -44.5763 | 2024-10-12 04:25:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 348b56e4-aacc-34e1-b41b-970f9a574d09 | -4.454 | -44.5534 | 2024-10-12 04:25:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| d2b461ec-bf46-31e4-ae29-03bf4e12a0b7 | -4.4725 | -44.5752 | 2024-10-12 04:25:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| cd8d2769-7aab-31ff-bbe5-5d3c575f3ca7 | -4.5859 | -47.0968 | 2024-10-12 04:25:32 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 624882e9-9618-3478-a53f-a99b8edf7d9b | -5.2486 | -48.0424 | 2024-10-12 04:25:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 5807bfb6-c4f7-3ff5-b8ab-4d1ab844c715 | -5.3997 | -45.3574 | 2024-10-12 04:25:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| c8b53030-0248-3a37-8575-1ef8b3426f56 | -6.747 | -59.3259 | 2024-10-12 04:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 5cc92982-17ee-3f0a-ae3c-3882667e4585 | -7.292 | -64.6676 | 2024-10-12 04:25:48 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.1 |
| b70fd16c-f4b1-3e6e-961d-4f93420f5ac0 | -7.8529 | -54.7027 | 2024-10-12 04:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f8eee636-a2c3-3cf9-a803-ba3d8e414751 | -7.8713 | -54.7217 | 2024-10-12 04:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 556d769f-b176-315f-b6df-8b7ba720ec1e | -7.8715 | -54.7016 | 2024-10-12 04:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 33bca66b-c63f-3c7e-9e69-db0717f835cd | -7.8717 | -54.6814 | 2024-10-12 04:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| d24488b5-76f3-3615-8e6c-072eac9571da | -7.89 | -54.7206 | 2024-10-12 04:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 65c8ee8d-dc54-31f6-94cf-21e4bf4e4b64 | -7.8901 | -54.7004 | 2024-10-12 04:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 512c7d33-476e-3df2-805c-1e5920f814b4 | -10.9506 | -44.653 | 2024-10-12 04:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 891eca0d-905f-3c61-876c-c4fb8a85c772 | -11.8377 | -58.8445 | 2024-10-12 04:26:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 0963c7c1-97b4-3944-b058-f3109ceac89d | -12.4367 | -54.5778 | 2024-10-12 04:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 32c407ff-5e65-36cc-bfbb-7188767f06c2 | -12.437 | -54.5573 | 2024-10-12 04:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 14f6e2ee-280e-3616-ad22-9f76bd450e6d | -12.4558 | -54.576 | 2024-10-12 04:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 787c24a0-a858-368d-a6e1-49a66183642c | -12.456 | -54.5554 | 2024-10-12 04:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 9a72d455-3678-3fd2-96b5-9cfb83f5d5db | -12.7941 | -53.509 | 2024-10-12 04:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 561e6e9c-e717-34ca-bc25-9f8db5fa32fc | -12.8132 | -53.5069 | 2024-10-12 04:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 2cce0f75-a70d-335c-9361-41511f521f05 | -12.8135 | -53.4861 | 2024-10-12 04:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 05ce7eb7-030b-36a0-8118-2dd87f53d0a7 | -12.832 | -53.5256 | 2024-10-12 04:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 3f682f81-d297-307c-9550-63771aeb900b | -12.8323 | -53.5048 | 2024-10-12 04:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| a27595aa-7f90-31b0-8cbf-f19268a21606 | -12.8511 | -53.5236 | 2024-10-12 04:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| be9de0b8-f722-3e98-8a86-5cde8fcd7350 | -12.9464 | -53.5339 | 2024-10-12 04:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 181.5 |
| f0ffa945-e285-37b2-b41f-e7647d7632e7 | -12.9467 | -53.5131 | 2024-10-12 04:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 155.1 |
| e23a76f0-ed4e-3460-b6a7-d46492bb9488 | -12.9652 | -53.5527 | 2024-10-12 04:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 301e439a-4167-3804-9d1f-2a08599627d6 | -12.9655 | -53.5319 | 2024-10-12 04:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 160.5 |
| f939d6f2-9ec6-3c6e-b083-1a84120970b6 | -12.9658 | -53.511 | 2024-10-12 04:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 084769f7-1f85-3f70-a6ba-8ea0754f5451 | -13.7153 | -60.6289 | 2024-10-12 04:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 1c6bdaa0-78df-3b5b-9968-d97ad1da9591 | -13.7346 | -60.6079 | 2024-10-12 04:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| d79ef723-9174-3f98-8b4c-e3142e64e397 | -13.7348 | -60.5883 | 2024-10-12 04:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1ca3174e-f2a3-3435-88c0-8a35db2a098e | -16.9805 | -57.4404 | 2024-10-12 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 7cf7b910-3517-32ce-b1a2-6680a872bde1 | -17.1761 | -57.4585 | 2024-10-12 04:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 8576c34a-0b41-3a24-9ef8-5b3f5ba79d44 | -17.627 | -56.3318 | 2024-10-12 04:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 856139ea-46ba-369b-9832-d5536e9e31fa | -17.6467 | -56.3292 | 2024-10-12 04:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 48e10ae3-c934-38f6-b0af-282ab6e53378 | -17.6679 | -56.2435 | 2024-10-12 04:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 13702685-ee86-31d8-a347-785b8bddcfb9 | -18.1956 | -56.5483 | 2024-10-12 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 70618631-aaf3-3ae2-96be-07ccec621550 | -18.196 | -56.5275 | 2024-10-12 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 05c466fc-957d-3c5e-9393-5022b2e0732a | -18.2158 | -56.5249 | 2024-10-12 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.0 |
| e0b9adac-5280-3039-b8f7-048e05473677 | -2.8255 | -51.3194 | 2024-10-12 04:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 8e9522dd-ab80-34c2-b878-da6a1808bd9a | -2.8254 | -51.3401 | 2024-10-12 04:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 2cf81b77-302f-317f-b7b7-66f51299db8c | -2.7885 | -51.3618 | 2024-10-12 04:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| cd9d7cdf-cd3d-3d12-8fbf-1dbb16369311 | -2.7701 | -51.3622 | 2024-10-12 04:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f331e52d-f725-3a10-aea3-1a2b587c7e54 | -3.1611 | -50.3508 | 2024-10-12 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 4aa0ae36-91d2-31a6-b450-cde031ad3d2c | -3.6979 | -50.1015 | 2024-10-12 04:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 895b6237-c5b9-3538-a477-1e7229ab5ce1 | -3.6978 | -50.1225 | 2024-10-12 04:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 6ace70d4-bee2-3c45-be71-32402f79ab01 | -3.7845 | -51.3104 | 2024-10-12 04:35:28 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 41d089ad-a654-33a0-b36f-e8d1f1b976a4 | -3.9267 | -42.401 | 2024-10-12 04:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 4bc159c3-d0dd-3c97-afcb-01ac830e5a7a | -3.9396 | -46.4229 | 2024-10-12 04:35:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| f721270a-a63a-3d6c-80bb-548842bc2f7b | -3.9394 | -46.445 | 2024-10-12 04:35:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 2304fe5b-be89-31a9-9522-b701b6b23c75 | -4.454 | -44.5534 | 2024-10-12 04:35:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 6bb22c70-a077-3d20-8f88-e5825976ed22 | -4.4538 | -44.5763 | 2024-10-12 04:35:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |


[Clique aqui para ver as próximas entradas](README56.md)
