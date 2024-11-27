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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00d1a787-7938-3044-9fa5-6aadd47a8e2c | -3.0949 | -53.2588 | 2024-11-27 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 358.4 |
| 43d89566-fa68-3d1d-b595-dba5aa6b3f30 | -3.1691 | -48.4394 | 2024-11-27 02:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 239.9 |
| e65f47b6-3748-3b86-87af-01dc07a6a174 | -1.6813 | -52.4537 | 2024-11-27 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| e85c2c2d-4d9a-33dc-97e3-c22835e43249 | -4.7383 | -46.5595 | 2024-11-27 02:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 2a1a6748-0437-323f-8339-fdc3aa0ae26a | -3.5226 | -52.1448 | 2024-11-27 02:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 8c54df46-f5bb-3a28-bd61-eb7e54a90caa | -4.1606 | -43.7894 | 2024-11-27 02:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 418d926a-83af-3941-90e0-6f7a458da5e7 | -1.6629 | -52.454 | 2024-11-27 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 2d0b3f5c-4138-3782-a865-f40ff8451a9e | -2.1928 | -53.7839 | 2024-11-27 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 2bc208b7-c4d5-3914-8b2b-5c6f540421c0 | -1.6629 | -52.4336 | 2024-11-27 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| ecbfca52-27e4-3638-bf9d-d9afc3d278bf | -3.0948 | -53.2791 | 2024-11-27 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| d58359de-8903-3a77-926e-f5a76f224ac1 | -2.8346 | -54.1326 | 2024-11-27 02:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| a08c4387-9557-365f-b0ae-d583238146d1 | -3.0949 | -53.2385 | 2024-11-27 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 5742c67f-7dc6-3b06-92c7-1cf1a74377dc | -3.1133 | -53.2381 | 2024-11-27 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 9080f0c0-e512-39a9-8720-665604e491a3 | -3.1692 | -48.4179 | 2024-11-27 02:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| dc567b96-ba18-35a9-80b9-9ef9adedb961 | -3.0577 | -48.5291 | 2024-11-27 02:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4fce6d1f-8dfb-3744-82b0-67f3cba15448 | -3.11 | -53.27 | 2024-11-27 02:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13f41f33-4da8-3cc4-a94f-e2e604ba2eb0 | -3.08 | -53.26 | 2024-11-27 02:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82f2e048-f45f-3d30-9c86-f044c4863414 | -3.16 | -48.42 | 2024-11-27 02:00:00 | MSG-03 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45bd505a-7ebb-308a-81a3-7352bccffc71 | -1.6813 | -52.4537 | 2024-11-27 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 59fb399d-c07e-35ac-88c5-bd074592b53a | -3.9674 | -48.0851 | 2024-11-27 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7e331867-4a16-3015-9ce8-ebb987d789a6 | -1.6629 | -52.4336 | 2024-11-27 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| e75571f3-44cb-3110-9f7f-33683a912d11 | -4.7197 | -46.5605 | 2024-11-27 02:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 44.9 |
| ace0718e-6102-3ab0-8e65-6ba846fa5e81 | -4.1604 | -43.8125 | 2024-11-27 02:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| efe93765-7b57-3bd0-ae67-25bd622b8216 | -5.9975 | -45.3607 | 2024-11-27 02:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 6b9957c0-5995-3cb0-9bf1-436cda4e91b1 | -3.1692 | -48.4179 | 2024-11-27 02:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ab07ba44-3672-393a-a9c2-9a750213a7cc | -6.4086 | -35.0981 | 2024-11-27 02:10:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 125.1 |
| 603efae3-b207-3e18-8169-cc5ec83fef47 | -3.0578 | -48.5076 | 2024-11-27 02:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| ef9bc4e3-c447-3a3d-bcd2-abf68daf3edb | -3.1132 | -53.2786 | 2024-11-27 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 8aeb79b3-17e5-3dfb-a52d-cfbb05026fa6 | -3.1691 | -48.4394 | 2024-11-27 02:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 212.5 |
| 491db878-644c-3f82-a50e-a1109f76bbea | -2.1928 | -53.7839 | 2024-11-27 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| fdc15c1c-2249-3ecf-96fc-dbed3defa92c | -2.8424 | -46.8413 | 2024-11-27 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 796b88ff-0377-37de-a47c-b723ce1c32a9 | -3.0948 | -53.2791 | 2024-11-27 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b3a1a141-6537-3182-a4b2-0157be11e684 | -4.1419 | -43.7905 | 2024-11-27 02:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 00c652e8-3a06-3eb6-9ff5-37f4006376b7 | -6.4089 | -35.0706 | 2024-11-27 02:10:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| 7d168d97-147d-3225-bb2b-502b45470a6f | -3.9859 | -48.0843 | 2024-11-27 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| b53c26e9-fe13-30a4-823a-44a0445ed079 | -3.0393 | -48.5082 | 2024-11-27 02:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 3325aad1-2b14-3224-887c-28c7362bced3 | -2.8346 | -54.1326 | 2024-11-27 02:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3a6f27c3-5fed-33b7-9ef2-4dee1901f8df | -3.0949 | -53.2588 | 2024-11-27 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 257.2 |
| d373ea71-83bb-3fb1-ba0b-5c89325d6575 | -3.5226 | -52.1653 | 2024-11-27 02:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b0429039-1ea9-3f72-94a2-f269798fe754 | -3.0392 | -48.5297 | 2024-11-27 02:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 9745eabb-7740-39cf-86a5-fa33e9a93919 | -3.1133 | -53.2583 | 2024-11-27 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 241.9 |
| a02f9324-11bb-333d-b92c-6891f58bb2c9 | -3.0949 | -53.2385 | 2024-11-27 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| bcee5491-d1e0-3f58-b446-7fab032ade1b | -4.1417 | -43.8135 | 2024-11-27 02:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| f5446ff8-47ce-30dc-9d0f-192e0844ddc0 | -1.6813 | -52.4333 | 2024-11-27 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| a77a4908-5d04-3c2c-8b94-e8cb94e9097f | -3.5226 | -52.1448 | 2024-11-27 02:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| c581ba3d-98b1-3757-9876-f721f30ade7e | -2.8347 | -54.1125 | 2024-11-27 02:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 024c92cf-decc-3f8b-a11e-7bdd9f9770a1 | -3.1133 | -53.2381 | 2024-11-27 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| de1b10b7-d03a-38b1-8f73-f766893697eb | -3.1876 | -48.4387 | 2024-11-27 02:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 5ba08557-a5a5-3d09-a49b-97ef5c95d5cc | -3.9675 | -48.0634 | 2024-11-27 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 3539df7f-b287-37a7-a951-96ba103dba9e | -5.9788 | -45.3621 | 2024-11-27 02:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 9358f493-89f6-3d1e-b539-fe1f7528835e | -3.1876 | -48.4387 | 2024-11-27 02:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| e2590a2d-24ed-368c-aaae-5abfdd29d8a6 | -1.6629 | -52.454 | 2024-11-27 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| e22f4e47-dd5d-3274-84c7-ac5471f21a91 | -3.5226 | -52.1653 | 2024-11-27 02:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| eac8ca57-202a-3a98-9b43-b01e3248a285 | -4.1417 | -43.8135 | 2024-11-27 02:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 69d2dee5-caf8-3481-a393-d79387e422de | -3.0578 | -48.5076 | 2024-11-27 02:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| db697137-22a6-3974-9954-5a39303c7d2a | -9.874 | -36.2161 | 2024-11-27 02:20:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| 2623c548-2e06-36e5-a4db-37bc0bd60fd5 | -3.0393 | -48.5082 | 2024-11-27 02:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 6c0c3bf1-4f02-32b8-94ec-c43b1360185c | -3.9859 | -48.0843 | 2024-11-27 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 212eb0df-4368-34c6-b1ff-79f3f0b414f4 | -3.9675 | -48.0634 | 2024-11-27 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| bcdc68d0-9575-397a-9cdc-ef16ead38522 | -3.0949 | -53.2588 | 2024-11-27 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 280.0 |
| 027e818a-1968-3d5c-8575-4d094ef5d771 | -9.8547 | -36.2195 | 2024-11-27 02:20:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.5 |
| f4d07c80-bdab-3fd3-9bf7-8e2882efea3d | -4.2115 | -50.8782 | 2024-11-27 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 48848398-e1f6-3906-baa7-0c275894d743 | -5.9788 | -45.3621 | 2024-11-27 02:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 7b5a2a9c-0513-37b9-a16f-2622e79d32a3 | -1.6813 | -52.4333 | 2024-11-27 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| b7f8f3b6-9fd7-3771-98ea-39715abd3ddf | -1.6813 | -52.4537 | 2024-11-27 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 6248fb4c-ca48-3cb6-832a-2d2337dbe574 | -3.9674 | -48.0851 | 2024-11-27 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 270fd30f-f4e7-3604-b49e-21386966f9f8 | -1.6629 | -52.4336 | 2024-11-27 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| b73d055e-6eb1-3d65-aab7-e0238f8a27db | -3.1692 | -48.4179 | 2024-11-27 02:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 0d59c96c-e1c3-3f59-b2d1-9dd1309f1410 | -3.1691 | -48.4394 | 2024-11-27 02:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 168.0 |
| 0b42fe52-db4d-3a02-9270-a0df6fd050ce | -2.1744 | -53.7842 | 2024-11-27 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| fb79dddb-ce89-3fd1-bfb0-26d9cbb789a2 | -3.1133 | -53.2583 | 2024-11-27 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 260.8 |
| ead9e0a1-bd5e-3906-bbe2-c71784bd6b4c | -4.2114 | -50.899 | 2024-11-27 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 5a87bea4-0e71-332a-9674-fb3741272889 | -9.8735 | -36.2432 | 2024-11-27 02:20:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 95.3 |
| 22ccb978-a3b8-3d02-a353-5134f644b55d | -9.8542 | -36.2465 | 2024-11-27 02:20:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 101.0 |
| fb4ade9c-b97b-38d9-b63c-e94ceee9de63 | -3.0949 | -53.2385 | 2024-11-27 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 33271f80-8717-387b-a737-62507a7f6c34 | -3.1877 | -48.4172 | 2024-11-27 02:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c7da065c-70e5-3a2e-8f2d-a6d25de73b71 | -2.8346 | -54.1326 | 2024-11-27 02:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 50fbddf1-59a5-3772-95a6-7675a84451e9 | -3.0577 | -48.5291 | 2024-11-27 02:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| bd7e633b-683a-34d2-ae05-3d990e7e78b5 | -3.1133 | -53.2381 | 2024-11-27 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| ef01cb77-7e23-3694-a1fd-14deaae39ff2 | -2.8347 | -54.1125 | 2024-11-27 02:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| d82567ff-9be4-3ef2-891b-bb2a441576d4 | -3.0948 | -53.2791 | 2024-11-27 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 13c2b423-b54b-3301-860a-fb9872425c2b | -4.1419 | -43.7905 | 2024-11-27 02:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| f439578e-416b-3602-98d2-06fc1c1ea088 | -3.5226 | -52.1448 | 2024-11-27 02:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 93d93ce2-4d19-381b-bffa-028b793e0e6b | -5.9975 | -45.3607 | 2024-11-27 02:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 11c9b70a-47a2-3ca1-ade4-669e84976912 | -3.9674 | -48.0851 | 2024-11-27 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| e2ad9aab-e876-3d4d-a9a4-14d5659129fa | -3.0948 | -53.2791 | 2024-11-27 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c7fde983-3e6c-3078-b258-52f0992b9696 | -3.0949 | -53.2588 | 2024-11-27 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 284.7 |
| 4202ab4e-7741-3fd1-ad75-60c1a2d85f5e | -3.1691 | -48.4394 | 2024-11-27 02:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 168.6 |
| 9e8ca304-b35d-356e-9ceb-60a71b2a6258 | -5.9788 | -45.3621 | 2024-11-27 02:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| d081e81d-71b7-39b3-a5c9-03f6a0b89a3f | -3.1133 | -53.2381 | 2024-11-27 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 3f79742d-8f38-37b5-9bbe-4dcf7f07cf65 | -2.1745 | -53.764 | 2024-11-27 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 38d3618c-4312-32bc-b2f9-db812c22dbb9 | -4.1417 | -43.8135 | 2024-11-27 02:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| a4b251ca-e2e4-32f1-9108-681b3a5d0dfa | -3.1133 | -53.2583 | 2024-11-27 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 224.3 |
| 0041becd-f38d-3c7f-864b-d1f0034b4068 | -3.0578 | -48.5076 | 2024-11-27 02:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 7f3c8fda-a6eb-3a28-a7b6-2023fceb3ecf | -3.1692 | -48.4179 | 2024-11-27 02:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| fb5e2c98-a3a4-3a7f-98fa-d1690895d317 | -3.9675 | -48.0634 | 2024-11-27 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| a9d917cc-5417-38ab-b240-6c9918d061f0 | -4.1419 | -43.7905 | 2024-11-27 02:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 76a2167e-c4d7-38a8-a2b3-46bc16a9fc07 | -3.9859 | -48.0843 | 2024-11-27 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| d8cf2788-3ef9-323b-bded-082ec6805068 | -1.6813 | -52.4537 | 2024-11-27 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 3a754a4d-de8a-36fb-8d86-e8ab609d2557 | -2.9428 | -54.7904 | 2024-11-27 02:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |


[Clique aqui para ver as próximas entradas](README21.md)
