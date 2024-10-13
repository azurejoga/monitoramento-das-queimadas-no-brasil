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
| f7d78db2-fcda-340e-8329-60441b0d10ec | -4.8967 | -47.6548 | 2024-10-13 00:59:24 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bea418d9-ef4a-38d8-8661-c41e3b141fc4 | -4.8988 | -47.6637 | 2024-10-13 00:59:24 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 04b0c093-dbad-3812-a33e-becae1954221 | -4.9009 | -47.6726 | 2024-10-13 00:59:24 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b5453ee1-c032-34f1-b100-d32ffdc1d75a | -4.8547 | -47.739201 | 2024-10-13 00:59:25 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 57e1860a-5db2-34ef-b73b-44df867068d2 | -4.8449 | -47.741501 | 2024-10-13 00:59:25 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6dbeedb-9da5-387b-b1a0-1beb5f0cf2c4 | -4.1603 | -45.764801 | 2024-10-13 00:59:28 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e505955b-28a6-3002-9b5b-6f4c72f1642a | -4.1631 | -45.7766 | 2024-10-13 00:59:28 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ea304f52-3b75-3380-981d-34308a9a8986 | -4.1659 | -45.788399 | 2024-10-13 00:59:28 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f3e2fdc-ac76-383f-b1a9-2c32968cdaca | -4.1506 | -45.767101 | 2024-10-13 00:59:29 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 55252cd0-2137-337f-92ac-b0c8475779bd | -4.1534 | -45.7789 | 2024-10-13 00:59:29 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c30fb883-03dd-303c-98b0-73e85d560e4d | -4.4874 | -48.1068 | 2024-10-13 00:59:32 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e156f820-a360-3873-b3b2-86bfa07f65bb | -4.2835 | -47.284 | 2024-10-13 00:59:32 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6cd7b308-7f73-35b3-a0eb-d49e51ba78c9 | -4.2858 | -47.293499 | 2024-10-13 00:59:32 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b48cab0-41da-3a3e-8098-e07b14682c6b | -4.288 | -47.303001 | 2024-10-13 00:59:32 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c1597b7-8937-366a-ac62-af0f393d4768 | -4.4697 | -48.119801 | 2024-10-13 00:59:32 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3be740ae-063d-3868-b001-4a92683cb987 | -3.9339 | -46.4151 | 2024-10-13 00:59:35 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e71feb8-a470-371c-a0de-a01854594e06 | -3.9365 | -46.4259 | 2024-10-13 00:59:35 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2df8f9d-996d-3b05-a11f-5ebcdb08d4fa | -3.939 | -46.436699 | 2024-10-13 00:59:35 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f56b60a3-4d0d-3c7a-a835-f8a666c4b38e | -3.9267 | -46.428101 | 2024-10-13 00:59:35 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5e47b428-160b-306b-8901-5d709971b62c | -4.2762 | -48.217899 | 2024-10-13 00:59:36 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d98d7a4e-c630-330b-9248-74a08f6e225b | -4.2781 | -48.226299 | 2024-10-13 00:59:36 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3afdd42-a9c1-3cad-afe3-eaed3ba5aa0e | -4.2801 | -48.234699 | 2024-10-13 00:59:36 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 901d2b6a-5c6c-30e6-9e98-463fd0dce63a | -4.2886 | -48.6236 | 2024-10-13 00:59:37 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d328f061-ce8c-3d96-a2f1-9853af427767 | -4.2788 | -48.625801 | 2024-10-13 00:59:37 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbdc0cf9-15ee-31b2-8f0e-13fefdd9b2ad | -4.0604 | -47.9132 | 2024-10-13 00:59:38 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 923a3d7a-cbf8-3913-a5f9-be25684dbcd0 | -4.1137 | -48.2285 | 2024-10-13 00:59:39 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a05c65d4-e333-32db-a0e2-41a1a5b0f0e7 | -4.1157 | -48.2369 | 2024-10-13 00:59:39 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb87541a-ecab-34e1-9d60-dec97ea7f130 | -4.1176 | -48.245399 | 2024-10-13 00:59:39 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e25ee218-1281-3e1b-abeb-dce404a5a80f | -4.1216 | -48.262299 | 2024-10-13 00:59:39 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e6233c8-8870-3c30-bbe9-b55736d323e8 | -4.1236 | -48.270699 | 2024-10-13 00:59:39 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae787e08-b694-3920-a7e5-d231d2fa1958 | -4.1059 | -48.239201 | 2024-10-13 00:59:39 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce5a5b43-ac25-3e3a-8c2a-5ab029536a5b | -4.1079 | -48.247601 | 2024-10-13 00:59:39 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56163d92-ba15-3492-90d3-9cf4cd5dfc69 | -4.1098 | -48.2561 | 2024-10-13 00:59:39 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4856cab-4d0f-33d6-a620-866a424854eb | -4.1118 | -48.2645 | 2024-10-13 00:59:39 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 287565c2-8e1c-3c24-a487-273bd40550d1 | -4.1138 | -48.2729 | 2024-10-13 00:59:39 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8111349-56a8-3a0d-a7b2-eef3682db816 | -4.1158 | -48.281399 | 2024-10-13 00:59:39 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e3cac3b-7daf-3ea8-abd7-d28dcdb9062b | -4.4057 | -49.747299 | 2024-10-13 00:59:40 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f89b02b-e4b8-395f-b635-ab10c21036dd | -4.4074 | -49.754601 | 2024-10-13 00:59:40 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41b7124c-58f2-31e2-b464-978c7683e3da | -4.4091 | -49.761902 | 2024-10-13 00:59:40 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2272fc9-01db-3bf4-b17e-0706ee63d8f3 | -4.3959 | -49.7495 | 2024-10-13 00:59:40 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5503090-b653-3706-b185-23addd1a4577 | -4.3976 | -49.756802 | 2024-10-13 00:59:40 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6660e11-07f7-351d-aab3-ab25a343735f | -4.3993 | -49.764099 | 2024-10-13 00:59:40 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17039096-32bd-3f9b-8d47-5a26e7f43514 | -3.957 | -47.955601 | 2024-10-13 00:59:40 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc05c0b5-96ef-37e2-b539-14f03a0488dd | -3.959 | -47.964401 | 2024-10-13 00:59:40 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23959b6e-ef75-3a28-91e0-94284fbcab6e | -3.1076 | -44.497898 | 2024-10-13 00:59:41 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4a8f430e-b04f-3549-92c2-767890d99b13 | -4.6117 | -50.952499 | 2024-10-13 00:59:41 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18ff98a6-3ed3-3b86-9c0c-cbedcbf01688 | -3.924 | -48.342999 | 2024-10-13 00:59:42 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0247689-7d5c-3aeb-994f-0d9c2dd64a96 | -3.9259 | -48.351398 | 2024-10-13 00:59:42 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d35cd77e-e7f6-37fb-9e68-5ec32a5b83ce | -3.9122 | -48.336899 | 2024-10-13 00:59:42 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53204f58-d594-302f-aee3-b48bc075c367 | -3.9142 | -48.345299 | 2024-10-13 00:59:42 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b6cf4ae-2832-32de-a6d6-bab3202aa466 | -3.9161 | -48.353699 | 2024-10-13 00:59:42 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33b60c1d-dda1-3acb-8257-e82178ef0ee4 | -3.9181 | -48.362099 | 2024-10-13 00:59:42 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 562123bc-a0a7-3d79-9e2b-99748e4f9937 | -3.9044 | -48.3475 | 2024-10-13 00:59:42 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c236c299-8260-3996-8bba-8c249049476a | -3.9063 | -48.3559 | 2024-10-13 00:59:42 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68cb4b84-ac9e-3b42-b27f-2efcabead7bb | -4.41 | -50.569 | 2024-10-13 00:59:43 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19bb27af-69b4-3e84-be85-5d9fe845017e | -3.6051 | -47.5103 | 2024-10-13 00:59:44 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fcf570f-89f3-3d72-993f-aac1ac08bbe7 | -4.3583 | -50.792198 | 2024-10-13 00:59:44 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7605c132-5ddf-321b-b62f-12fee846e854 | -4.3599 | -50.799099 | 2024-10-13 00:59:44 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6884c269-b1e1-3807-b78e-7ac639021ccf | -4.3615 | -50.806 | 2024-10-13 00:59:44 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03f5af06-1bfa-3190-8526-fc90eb33da93 | -4.2581 | -50.581299 | 2024-10-13 00:59:45 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0db64b0-6e92-3201-8206-9f3288a53957 | -4.2597 | -50.588299 | 2024-10-13 00:59:45 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a88a108-99ad-3539-a2ed-35cba81f3f14 | -4.2708 | -50.949799 | 2024-10-13 00:59:46 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2f9914c-504c-35eb-b27b-d4dd21ea0e83 | -4.2724 | -50.9566 | 2024-10-13 00:59:46 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 681f9217-3956-338d-b8bf-8865cdde3955 | -3.3512 | -47.306801 | 2024-10-13 00:59:47 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4ddc8d5-0b9e-3c5f-99d7-8c35c26b43fd | -3.3535 | -47.316601 | 2024-10-13 00:59:47 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3654cbf9-988c-3604-9353-f98a79cff6af | -3.3414 | -47.309101 | 2024-10-13 00:59:48 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42f239d0-4d1a-3ee1-8cd8-f7b560496078 | -3.3437 | -47.318901 | 2024-10-13 00:59:48 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30809c07-d10a-3acf-afe5-8cc682f86a0f | -4.1218 | -50.7509 | 2024-10-13 00:59:48 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8718635f-2a96-3372-962d-4fb0c51b0994 | -4.1211 | -51.106201 | 2024-10-13 00:59:49 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12927b4f-750f-3416-97c7-beec2ca8b0bc | -4.1227 | -51.113098 | 2024-10-13 00:59:49 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84fa33a5-2ef5-36ee-b02c-900a9c0be5cd | -2.7953 | -45.603901 | 2024-10-13 00:59:50 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 57e51460-f9b4-3852-bb8b-da12327de280 | -4.0364 | -51.096401 | 2024-10-13 00:59:51 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77d0e3dc-9e86-3e58-b312-150e0142d519 | -3.7765 | -50.1483 | 2024-10-13 00:59:51 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bef0802-1b29-3b08-82e0-c623e08059c6 | -3.7781 | -50.155399 | 2024-10-13 00:59:51 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70a8aba8-1965-3e0b-8e27-9766369c5155 | -3.9766 | -51.0159 | 2024-10-13 00:59:51 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e3589a8-1d4d-30b6-9bbf-4b8064c0288b | -3.6946 | -50.1064 | 2024-10-13 00:59:52 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b2d8ed4-6401-3f97-ad31-3d5ce192e412 | -3.6963 | -50.113602 | 2024-10-13 00:59:52 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed34e4e5-c5f5-3812-9226-e31237381f8e | -3.6979 | -50.1208 | 2024-10-13 00:59:52 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1afcafe-197e-3474-b4ba-0712a1e81835 | -3.0902 | -47.775501 | 2024-10-13 00:59:53 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81b2a05b-7d1b-3e68-ab1f-3ba485015ef7 | -3.9212 | -51.223202 | 2024-10-13 00:59:53 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ce15b99-2391-3554-858e-48ecfbdb5ce8 | -3.9227 | -51.230099 | 2024-10-13 00:59:53 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88250ef3-8723-34f7-a62b-8c5b0c8bea2b | -3.0804 | -47.777802 | 2024-10-13 00:59:54 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49366d9d-9b8f-3133-bd95-f1c30b482d2c | -2.961 | -47.355499 | 2024-10-13 00:59:54 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b72833d2-8078-369a-aee2-d06e490dcf1a | -2.9632 | -47.365299 | 2024-10-13 00:59:54 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdfd7514-b016-3233-a686-a999410382e7 | -3.3386 | -49.1497 | 2024-10-13 00:59:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14146679-6ff5-3704-8d7b-3796a0a4b6f8 | -3.3404 | -49.157501 | 2024-10-13 00:59:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 330fadff-2ba9-31de-a72a-74904cdd90aa | -3.3288 | -49.151901 | 2024-10-13 00:59:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e95c6528-28c9-3d72-97b5-4c144ae82ea6 | -3.3306 | -49.159698 | 2024-10-13 00:59:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 529a1f46-487e-3f65-ba20-7817cbdd03e3 | -3.2965 | -49.101501 | 2024-10-13 00:59:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78f3bb23-36ce-3fe7-bd8b-1aca32f3d6f1 | -3.2983 | -49.109402 | 2024-10-13 00:59:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 684c0fc0-9cbe-35d5-8ea9-904c9603af89 | -3.8282 | -51.402302 | 2024-10-13 00:59:55 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7da20c06-b783-3388-a3ce-e95fda944c34 | -3.8298 | -51.4091 | 2024-10-13 00:59:55 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad064274-3ba7-34a2-9b78-ba83d0dec13e | -3.221 | -48.909698 | 2024-10-13 00:59:56 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca143caf-2e3d-336a-b634-841ab86e722a | -3.2228 | -48.917801 | 2024-10-13 00:59:56 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06fa181c-83a9-30f2-8044-4c88fb26b094 | -3.2247 | -48.9258 | 2024-10-13 00:59:56 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40304ec6-08ff-3707-b25a-3bf7e851fb30 | -3.213 | -48.919998 | 2024-10-13 00:59:56 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d808a73d-a8a0-3f36-a7cd-6870c212fe45 | -3.2149 | -48.928001 | 2024-10-13 00:59:56 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 505518e5-7b4d-3120-8cce-d41053e14915 | -3.9627 | -52.169201 | 2024-10-13 00:59:56 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8179c11-d838-39fc-b626-01d5f2ea4fab | -3.3087 | -49.464401 | 2024-10-13 00:59:56 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8c8c6d8-b49e-3bc7-9082-e37347aaf733 | -3.3104 | -49.472 | 2024-10-13 00:59:56 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README18.md)
