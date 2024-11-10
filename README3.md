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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1ed7514-edba-379f-9d77-f7cc40eac391 | -3.1096 | -49.4029 | 2024-11-10 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| fd40c9d9-7663-37bb-9298-4c8a0de51583 | -4.0682 | -50.0029 | 2024-11-10 00:10:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ca5a7003-3fbe-3561-a6f9-5449bd0a67c7 | -3.6003 | -47.3614 | 2024-11-10 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 165.1 |
| 370958c4-c2c6-369f-96ea-758fe956bbc9 | -3.9485 | -48.1508 | 2024-11-10 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| f90c11fe-c14c-31ac-9051-ab072c62dc39 | -2.9171 | -51.4825 | 2024-11-10 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 5b04f777-2eed-3dc8-acb4-c961d062b527 | -2.0954 | -48.8125 | 2024-11-10 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 40a6b8d3-6012-3f37-9b71-07458daf4799 | -8.4156 | -44.1344 | 2024-11-10 00:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| e736f1c4-ca5b-3ba5-a935-b9c3316f8633 | -3.2353 | -50.2645 | 2024-11-10 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 8043ecca-16b3-34ca-9eec-35479265e74d | -2.4661 | -48.4606 | 2024-11-10 00:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| a933d8cd-7311-3b83-8e66-53437ed45fd0 | -3.6189 | -47.3606 | 2024-11-10 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| f1728e66-9ed9-34f0-976b-f673e27e6d8d | -8.4156 | -44.1344 | 2024-11-10 00:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| fc5902e4-6aea-387c-b973-638e39d0aee7 | -3.2428 | -53.0519 | 2024-11-10 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| a1f30af6-fa4b-3802-ad12-685c1338e743 | -17.2933 | -57.4857 | 2024-11-10 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 215.7 |
| badcbce6-af12-3345-9feb-25bfea114ed4 | -3.2537 | -50.2849 | 2024-11-10 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| df8a5249-4a78-3a01-8d44-a82f32404cc2 | -2.2094 | -47.7547 | 2024-11-10 00:20:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 254c0cb0-6849-386a-b537-c0c79d05c4d1 | -3.2243 | -53.0727 | 2024-11-10 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 235.4 |
| 387d6309-85a4-3fef-8308-58cd96a22f0c | -3.525 | -44.0286 | 2024-11-10 00:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 0efef622-49d6-3f85-947c-7734d136b07a | -3.035 | -49.5537 | 2024-11-10 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 151ddade-45da-3b7c-8f3f-d6d8a2af8bb8 | -1.4926 | -55.431 | 2024-11-10 00:20:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 6054db5f-d64a-3906-a517-307e0d0e597c | -2.4662 | -48.4391 | 2024-11-10 00:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 59ef3f04-bfd7-3a72-95ac-5a408080e12e | -8.3964 | -44.1597 | 2024-11-10 00:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 610ec8b1-d0f8-3239-9e6a-7fddc3b47dd6 | -3.76 | -52.6695 | 2024-11-10 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 414609bf-5804-3fa4-8f91-eda8fbf8a12d | -2.2672 | -47.0556 | 2024-11-10 00:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 3d88884c-d606-300a-9b23-6b0056740b06 | -3.2168 | -50.2861 | 2024-11-10 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 4b290ded-87ce-3179-bb3f-bd64e6fd3e27 | -2.9355 | -51.482 | 2024-11-10 00:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 26b5df8e-17de-3fdd-bd0e-c47498c5f05a | -2.6203 | -46.7602 | 2024-11-10 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 4a15dded-8d5b-3753-9287-6c6e2a3f3a4c | 2.8552 | -60.0853 | 2024-11-10 00:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 41.0 |
| b39ffed2-d15d-3824-b76e-b6ece531029d | -1.4742 | -55.4312 | 2024-11-10 00:20:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 71b99f7c-0402-3cb3-ae59-9ee936ae19b8 | -2.0768 | -48.8342 | 2024-11-10 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 3958dd6b-a7b4-3857-bc41-048d703870c5 | -23.8884 | -54.0649 | 2024-11-10 00:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 72.6 |
| db5a0bf9-8d16-300b-bc03-529f14c25b5f | -2.9442 | -49.1529 | 2024-11-10 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| d43c18be-f3bb-352d-8fa5-11d32667df58 | -2.9443 | -49.1315 | 2024-11-10 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| f44d0108-74e9-3fd1-b446-84de1b61ab96 | -2.9356 | -51.4613 | 2024-11-10 00:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| a806a209-1310-3784-b212-b34e8938848d | -4.1112 | -45.7018 | 2024-11-10 00:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 112.1 |
| aeb53933-1716-34c2-9078-a08505e84559 | -3.0351 | -49.5325 | 2024-11-10 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 2a33b88d-25ce-3a63-a6d7-878c510b07e2 | -3.6004 | -47.3395 | 2024-11-10 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 285.1 |
| 98ee83ab-283b-35c2-858a-1702647e9d37 | -1.5347 | -52.1899 | 2024-11-10 00:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 4b044149-f60a-3462-befb-daae43875c70 | -2.2076 | -48.3596 | 2024-11-10 00:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0cbccb30-5c81-3111-96cb-7c4cac7b53fb | -4.2083 | -48.1176 | 2024-11-10 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| eda19278-890d-362a-bfc9-083243946451 | -2.2487 | -47.0561 | 2024-11-10 00:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 2d7624db-b7a2-3ce5-a829-14718070d5dd | -8.3967 | -44.1365 | 2024-11-10 00:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 156fcdc8-8a6e-3c0f-bd09-fa80b415e82f | -8.3778 | -44.1386 | 2024-11-10 00:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| be86f66e-4e8d-30b3-ba92-becaa9c63615 | -2.2075 | -48.3811 | 2024-11-10 00:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| a65abd82-d383-3e2b-b96f-b590136e65fd | -2.0954 | -48.8125 | 2024-11-10 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| eeaefc5b-6fc2-38bf-9a29-c598041d0736 | -2.7586 | -49.371 | 2024-11-10 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4e923a95-5cea-3b4d-8777-85df74153052 | -3.2352 | -50.3065 | 2024-11-10 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| a38f3891-4fea-3b70-a578-5d6465ab7ccb | -3.6003 | -47.3614 | 2024-11-10 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| 13fa99e1-f5dc-3f48-a29e-4da5aaa56e01 | -2.803 | -52.5337 | 2024-11-10 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 38b23654-260e-3b1f-af28-9aded427a616 | -3.1095 | -49.4241 | 2024-11-10 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 620dcda0-73b3-355d-a4d1-1446da757256 | -3.0029 | -53.2612 | 2024-11-10 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 05c9a649-9957-360f-94a0-0c34755773c5 | -4.054 | -49.1978 | 2024-11-10 00:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 987c79b8-53e1-37b9-b94e-f1ae9dd8916e | -1.5163 | -52.1901 | 2024-11-10 00:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 4d5fc391-3be6-34f1-ac01-e49114586aee | -4.0682 | -50.0029 | 2024-11-10 00:20:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| a4daa164-2651-3689-adcd-a0abcf1b2e7c | -17.313 | -57.4834 | 2024-11-10 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| a9f3b989-e9dd-3ae1-ae1c-8cc26fc208b3 | -3.5818 | -47.3621 | 2024-11-10 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 833375ce-5a06-367e-9e7e-06641bc09122 | -3.2427 | -53.0722 | 2024-11-10 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| c4ba3f0c-c4f8-37aa-8298-0e6b5fd8384b | -3.2352 | -50.2855 | 2024-11-10 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| c66d0338-86d7-3ad8-9dd9-959852ad6e3b | -2.2486 | -47.078 | 2024-11-10 00:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 152dd705-3b82-321a-972f-a352acf8fbc9 | -4.1246 | -43.5833 | 2024-11-10 00:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 92e789a2-3e2e-3714-89cc-03da3822b71e | -3.1422 | -50.4562 | 2024-11-10 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 66f99711-6dae-3a59-b170-e9df6220fe73 | -2.0953 | -48.8338 | 2024-11-10 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 05dcb76f-2ee6-3c4a-ab78-122a9f6624dc | -3.619 | -47.3388 | 2024-11-10 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 96a32f75-0010-333d-8c3a-59c2b0dd8057 | -3.5064 | -44.0294 | 2024-11-10 00:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 9756345f-de1a-3775-8922-47e9abc4390d | -3.2536 | -50.3059 | 2024-11-10 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 2f83d70e-b03d-3aab-a089-6cd7041305e1 | -3.0213 | -53.2607 | 2024-11-10 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 4aa16fc2-51c7-362d-88a1-25b816ab17ca | -1.5163 | -52.2106 | 2024-11-10 00:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 93c242b9-fbfa-36e2-8f53-ff4824d91d97 | -2.2095 | -47.733 | 2024-11-10 00:20:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| a1ae827b-6874-3746-9ec9-3c6cd6e6ac3c | -3.2353 | -50.2645 | 2024-11-10 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 9f6905e3-b571-3eb0-ae9f-2dce587b9c6b | -3.9624 | -49.0096 | 2024-11-10 00:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d3bd8c24-dcb8-3943-9668-38441a06324c | -3.5712 | -45.8163 | 2024-11-10 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c8738674-5aad-361d-9f1b-d0d0db4b30f2 | -2.7772 | -49.3492 | 2024-11-10 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 9461fc3f-58cd-314e-bf03-4355645fdfc0 | -3.1239 | -50.4358 | 2024-11-10 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 258.2 |
| 6dee868e-aa37-34e3-983c-cc0e5ef3e2a4 | -4.8916 | -48.6234 | 2024-11-10 00:20:00 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 649cc62a-6a20-3cdc-afa5-adc9c4896bf5 | -2.7771 | -49.3704 | 2024-11-10 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 6a19b344-c1bd-331c-a403-b1c9560c558f | -4.6736 | -45.1541 | 2024-11-10 00:20:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 46351088-6eb6-3f25-9816-7e15a94cac47 | -4.6922 | -45.153 | 2024-11-10 00:20:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| cb7153ae-f084-3a99-9fbe-82bc33629ee7 | -3.1238 | -50.4568 | 2024-11-10 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 195.1 |
| 0e0ad7ae-9bcd-34bf-8e7d-a1080ca32206 | -17.293 | -57.5062 | 2024-11-10 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.9 |
| 252d78cd-5da7-3eb4-bf1c-adb03bd0bcb6 | -1.4925 | -55.4508 | 2024-11-10 00:20:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| c15be81d-a392-34cd-a392-c5238cef00bc | -1.5347 | -52.2104 | 2024-11-10 00:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 296.5 |
| a9e47d35-e352-3abb-96a4-a8931e220e83 | -2.109 | -50.5663 | 2024-11-10 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| ecf4b883-fa6b-3ffd-9fdd-f83f24ac3b5b | -3.1423 | -50.4352 | 2024-11-10 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 213.8 |
| 28b1a0fb-9fa0-3c15-b567-f5b7860fced0 | -4.1111 | -45.7242 | 2024-11-10 00:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 179cd1a4-f1e6-31b3-a8e0-a493d7c811fe | -3.8413 | -44.1283 | 2024-11-10 00:20:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| bc88e7a5-d1f4-35fc-9306-513eb90a862c | -2.9171 | -51.4825 | 2024-11-10 00:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 6c998c07-1d17-32bd-8dff-b001584f53c4 | -2.2671 | -47.0775 | 2024-11-10 00:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| fb8755c1-a87f-3ebc-9b0e-7dc5a8e7b9dd | -3.5819 | -47.3403 | 2024-11-10 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 4d662beb-7946-376d-838f-baa9775eaa4b | -3.2244 | -53.0524 | 2024-11-10 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 250.5 |
| 7596ac42-0350-30d0-8967-9d5ef1574632 | -1.4742 | -55.451 | 2024-11-10 00:20:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 8839e01b-8c9a-399f-ae9c-289df7ada4f9 | -2.683 | -49.8598 | 2024-11-10 00:20:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 38363816-6312-3054-8638-45db7c3b62ed | -2.7587 | -49.3497 | 2024-11-10 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| be2d1a2d-a134-3a29-bc06-2d5ab9b26a56 | -3.1095 | -49.4241 | 2024-11-10 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 7d36254d-7202-390d-b573-bcf8589dbb7e | -3.9669 | -48.1716 | 2024-11-10 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 179.1 |
| dd7941db-f5ed-3fe5-b996-25840beb0612 | -1.5163 | -52.2106 | 2024-11-10 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 13e48a47-b106-35a2-9346-e5581ce8c408 | -2.0768 | -48.8342 | 2024-11-10 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 4b0513b1-7b46-31a7-bc13-cd0ee3a32f79 | -2.9249 | -49.3661 | 2024-11-10 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 9ff38349-5438-382c-a8cb-9c4121a6475a | -2.109 | -50.5663 | 2024-11-10 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 134f54ef-af3a-386a-88f5-f7d4fff86db8 | -17.293 | -57.5062 | 2024-11-10 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 143.3 |
| aa002864-e6f7-3a04-a8b0-0911e0ae7738 | -2.7586 | -49.371 | 2024-11-10 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 57d9c20f-6861-3515-be2c-a5ff023b47b4 | -3.2428 | -53.0519 | 2024-11-10 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 151.5 |


[Clique aqui para ver as próximas entradas](README4.md)
