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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 951a5b1a-1ae6-36ae-a847-b4921cb7625e | -3.1691 | -48.4394 | 2024-11-26 06:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d15bae67-1b9d-35dc-8728-8d8e80662191 | -3.1876 | -48.4387 | 2024-11-26 06:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 8df77695-1bfa-33ec-8ce0-930e513e1ea4 | -2.8014 | -53.0227 | 2024-11-26 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 30a1f0a7-f4d4-3597-bb41-7b2a61172051 | -3.1876 | -48.4387 | 2024-11-26 07:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 759bafef-f0dd-38dd-a774-5e10756119e6 | -3.9674 | -48.0851 | 2024-11-26 07:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 225.3 |
| 035cb4fc-3cee-3db4-a63b-caa7f2c17902 | -3.9675 | -48.0634 | 2024-11-26 07:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 385.9 |
| bd22344e-1128-36cb-aafa-f79e9e99617e | -3.9676 | -48.0418 | 2024-11-26 07:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 48cbc163-f910-3fea-87df-6a0c2fee5683 | -3.9861 | -48.041 | 2024-11-26 07:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c6a57846-e259-32ab-a56f-c547ce8418dc | -3.9859 | -48.0843 | 2024-11-26 07:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 236.1 |
| 0309925e-aaf1-34a5-bba5-dd9b8968edcb | -3.2209 | -45.2475 | 2024-11-26 07:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| cabdee1f-c6d6-3994-b4b1-7fe6f4b54744 | -1.5438 | -47.6166 | 2024-11-26 07:00:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 870d3b21-fa41-3897-837b-d6eb0a9fb9ac | -3.986 | -48.0626 | 2024-11-26 07:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 304.3 |
| 3f1df94b-f44b-31b5-baef-8e07aaf8d299 | -3.1877 | -48.4172 | 2024-11-26 07:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| a1a92c4e-2347-3a99-9237-c1d1f5adf3e4 | -3.97 | -48.04 | 2024-11-26 07:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a973d0fc-67ce-3900-abf6-ff699bcd3b7a | -4.0 | -48.04 | 2024-11-26 07:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7f60002-18ac-3aa9-908d-0156e9433662 | -3.97 | -48.09 | 2024-11-26 07:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36ed79ca-9bde-3dad-b0c7-45a2bc7a9d50 | -4.0 | -48.09 | 2024-11-26 07:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d4ecebc-1703-3317-af37-8969dcafc208 | -3.1877 | -48.4172 | 2024-11-26 07:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 9f7afab6-e9ec-3be1-a9d5-f65e4075e0ae | -3.9675 | -48.0634 | 2024-11-26 07:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 443.5 |
| d259f464-bdb9-3cf4-83cd-ff4b98e0b92c | -3.3852 | -45.8465 | 2024-11-26 07:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 55af6ec1-0f1b-38c3-9d37-6f9075cd6489 | -3.1876 | -48.4387 | 2024-11-26 07:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 2f0a6bfa-41d9-3438-b933-2628eb793643 | -3.986 | -48.0626 | 2024-11-26 07:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 257.4 |
| 7c80e702-f789-330a-8056-e89cad752c11 | 1.9316 | -55.7614 | 2024-11-26 07:10:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| a1b713e5-9d62-38f8-84b4-51b2792d4418 | -1.5438 | -47.6166 | 2024-11-26 07:10:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| ec06b07e-4413-31fe-896d-90fc9b947421 | -3.3851 | -45.8688 | 2024-11-26 07:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| fe4952bc-85ef-30f6-bdf9-20ef9c7e02fd | -3.2209 | -45.2475 | 2024-11-26 07:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| c3ac240c-d7bb-3dae-a656-cd00dc43f93b | -3.9676 | -48.0418 | 2024-11-26 07:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| d67ca597-72cc-3421-9d3b-5312a5f26944 | -2.8014 | -53.0227 | 2024-11-26 07:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| b424a247-d8f5-3e5f-803a-501de9e03b05 | -3.9674 | -48.0851 | 2024-11-26 07:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 235.4 |
| 5034011c-16d8-3cd9-a1c6-d0c9d4b949ed | -3.9859 | -48.0843 | 2024-11-26 07:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| a863101e-3d39-3a2a-8a54-9d701a92e0a9 | -3.986 | -48.0626 | 2024-11-26 07:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 238.7 |
| 377ace57-6292-3f00-96e0-e54c067080b7 | -3.1877 | -48.4172 | 2024-11-26 07:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 003b208c-f434-3c3b-88b1-0dd915cffe18 | -3.9675 | -48.0634 | 2024-11-26 07:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 406.0 |
| 02049b33-022b-36fd-8e31-1754ea8f9f90 | -3.9674 | -48.0851 | 2024-11-26 07:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 253.3 |
| ec0d01e0-9b56-33bc-8d22-82e41bd9eac4 | -3.9861 | -48.041 | 2024-11-26 07:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 1bea2a9c-59a6-3417-a40f-5983d4b45118 | -3.9859 | -48.0843 | 2024-11-26 07:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 3e7d1819-a862-3115-9b84-a8a25b38c162 | -3.3851 | -45.8688 | 2024-11-26 07:20:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| d0ee9bee-d220-3029-8408-2db03bf15972 | -1.5439 | -47.5948 | 2024-11-26 07:20:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 23d41abe-64f5-31b1-8088-fc576c692aec | -1.5438 | -47.6166 | 2024-11-26 07:20:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 597a0ab4-a837-3c67-ab49-d2fc8be3917d | -3.1691 | -48.4394 | 2024-11-26 07:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| e3f9cd51-320d-32ef-acfc-0316fd68315c | -1.5253 | -47.6169 | 2024-11-26 07:20:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 364758ab-5b89-33fa-ac72-479634c537a7 | -3.9676 | -48.0418 | 2024-11-26 07:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 99efe561-1140-3095-a52b-d1831567838a | -3.1876 | -48.4387 | 2024-11-26 07:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c2d96e97-4eda-36fe-93bc-8ac7de711e89 | 1.9316 | -55.7614 | 2024-11-26 07:20:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 131b32d1-ac7d-3fe3-a96e-0d3dcb794492 | -3.9861 | -48.041 | 2024-11-26 07:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| e945a592-9b91-39b4-b49a-a0c8cfe7dfe9 | -3.9859 | -48.0843 | 2024-11-26 07:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 263.8 |
| 89ecef7f-7163-30a0-bd3d-4de4c7734b50 | -3.986 | -48.0626 | 2024-11-26 07:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 295.9 |
| c330c93a-5867-3ccf-98a2-53b5b9e09b47 | -3.1877 | -48.4172 | 2024-11-26 07:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 8a227a3a-f1a6-3ab8-aded-9891cbebf167 | -3.9674 | -48.0851 | 2024-11-26 07:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 214.6 |
| d28bde9c-3745-384e-8f33-512c79ed4291 | -3.3851 | -45.8688 | 2024-11-26 07:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 324c14c5-0108-39dc-ad96-247b7795dc6f | -3.3852 | -45.8465 | 2024-11-26 07:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 4b157a12-25ac-30de-a6a0-49eb9dd87e63 | -3.9676 | -48.0418 | 2024-11-26 07:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 23d76203-86cd-38d1-a857-0e207b5cecc0 | -3.9675 | -48.0634 | 2024-11-26 07:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 339.2 |
| acba0ca4-c869-3fc6-b857-3247e9605f8b | -1.5438 | -47.6166 | 2024-11-26 07:30:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f6c28205-7d74-33b5-813f-73bae920d3b2 | -3.1876 | -48.4387 | 2024-11-26 07:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 6d987d1c-904d-3dd4-966a-57a07f70db22 | -2.8014 | -53.0227 | 2024-11-26 07:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| dd2efe0e-e994-33e7-aa2b-df8bbb925032 | -3.9674 | -48.0851 | 2024-11-26 07:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 292.3 |
| 2d91a1b3-0a82-3fd2-92b2-615a47905d2f | -2.8014 | -53.0227 | 2024-11-26 07:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| c232f46b-71f4-38ea-b170-b65c0c81ae2b | -3.9676 | -48.0418 | 2024-11-26 07:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 5bebefce-d9fb-3bb1-b51a-d0d2323360a6 | -3.986 | -48.0626 | 2024-11-26 07:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 265.3 |
| ef456c53-a223-3722-93de-dd42645df433 | -3.9859 | -48.0843 | 2024-11-26 07:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 223.1 |
| 5d5acef0-7412-3a2a-b131-704ca06b84e6 | -3.9675 | -48.0634 | 2024-11-26 07:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 439.8 |
| d0801c23-6cdc-3146-b9ed-81afd7e89645 | -3.3852 | -45.8465 | 2024-11-26 07:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 8e294f4d-cdf5-35f2-9356-32c43bf9b09f | -3.1876 | -48.4387 | 2024-11-26 07:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 05536ae2-3c14-33d8-a601-522e76881fb1 | -3.3851 | -45.8688 | 2024-11-26 08:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| e4d0e466-91fb-364e-9555-efd4f50fb04d | -3.76 | -52.6491 | 2024-11-26 08:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 046e492f-686d-3c71-9c77-ef5e9c4da2e1 | -3.1876 | -48.4387 | 2024-11-26 08:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 9cd5f9fe-167b-39af-8fcd-706a0bf7cdf0 | -3.3852 | -45.8465 | 2024-11-26 08:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a1e9f9a6-180b-3dd1-8128-1a62b064891f | -4.0 | -48.09 | 2024-11-26 08:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| febabc60-b62d-3ee6-808f-54519589dbc1 | -3.97 | -48.04 | 2024-11-26 08:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1884118b-79c4-3c51-b7e4-1404b416753d | -4.0 | -48.04 | 2024-11-26 08:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3edb17d-4691-3437-bfe5-9ae75baaf625 | -3.97 | -48.09 | 2024-11-26 08:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78d7f3dd-4556-3b09-9a86-3d905f4824f6 | -3.058 | -53.28 | 2024-11-26 08:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| b62d4a33-b334-33eb-a033-e85ff6e84280 | -2.8014 | -53.0227 | 2024-11-26 08:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d77628cb-4d89-392a-8c30-011015e97b48 | -3.9861 | -48.041 | 2024-11-26 08:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| ca7f7411-a479-3907-b956-1210a5afb0e4 | -3.1876 | -48.4387 | 2024-11-26 08:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| d4544d51-4229-3b78-98e2-2d4238900479 | -3.9676 | -48.0418 | 2024-11-26 08:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| d2d3093c-ffd2-3205-b081-59b6b3a71bd3 | -3.97 | -48.09 | 2024-11-26 09:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c091b4b-7c7d-3278-92d4-c59e10af8afb | -4.0 | -48.04 | 2024-11-26 09:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5df9a6c8-a0a1-312b-89b2-ac9988074ebf | -4.0 | -48.09 | 2024-11-26 09:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd4e2db2-de8d-3d2d-8fd9-f100d5b86de0 | -3.97 | -48.04 | 2024-11-26 09:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5ca5596-f369-3a59-b93f-20b8491897d1 | -3.97 | -48.09 | 2024-11-26 10:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14190f4b-d734-3d56-8b71-7eaca7d4cea4 | -17.4 | -44.88 | 2024-11-26 10:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7cc403e8-5c65-3109-949f-ed2e40ffc3eb | -3.97 | -48.04 | 2024-11-26 10:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0e2b784-9570-3acf-95d1-9c45d7c234a1 | -4.0 | -48.09 | 2024-11-26 10:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1185404b-10ce-3e03-8348-4eceb55a66ae | -3.3938 | -44.1722 | 2024-11-26 10:10:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 874c853d-464f-36a4-b284-06801ec3b9c2 | -3.3938 | -44.1722 | 2024-11-26 10:20:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |
| beadfae7-f047-3250-b3a7-7c656b3a5979 | -3.3938 | -44.1722 | 2024-11-26 10:30:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 6e020469-0edc-38eb-9450-49392dd1a0e0 | -3.3938 | -44.1722 | 2024-11-26 10:40:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 1a58f091-b6ce-3486-83d0-5173075d005c | -3.3938 | -44.1722 | 2024-11-26 10:50:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 77dcd87d-4fc7-3dd4-8272-8da8e8891384 | -3.3938 | -44.1722 | 2024-11-26 11:10:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 154.7 |
| f19fb8ad-ba3d-3750-8a44-8dae5938fa98 | -3.3938 | -44.1722 | 2024-11-26 11:20:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 54afeeff-6f9b-3c87-bc5c-eeb3d84181f2 | -3.3938 | -44.1722 | 2024-11-26 11:30:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 70d00a8d-8f0f-333a-8c27-8c310e2765d6 | -3.3938 | -44.1722 | 2024-11-26 11:40:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 86bde5a0-27a6-3400-886d-dd19a48035c8 | -3.3938 | -44.1722 | 2024-11-26 11:50:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| c528dff2-f6f9-32a6-a788-4ac4e8365c72 | -19.0711 | -53.4599 | 2024-11-26 11:50:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 80.3 |
| e1f2d1cd-8934-3271-bf92-552a05121ba7 | -19.0711 | -53.4599 | 2024-11-26 12:00:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 82.6 |
| bad58a10-e522-3825-9933-6a33b9f9157c | -3.6515 | -41.535 | 2024-11-26 12:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 161.5 |
| 64cf7873-e06e-31ee-b414-b779bc1ee3d2 | -3.3938 | -44.1722 | 2024-11-26 12:00:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 7a00e144-bdd0-3c01-99d0-61529295fa91 | -3.986 | -48.0626 | 2024-11-26 12:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 161.9 |


[Clique aqui para ver as próximas entradas](README46.md)
