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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24ab08e5-0e76-3e68-9dc5-566de1c09b01 | -10.70107 | -53.03419 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea3fc42a-07fb-364e-adab-0cd87f6f8cc0 | -10.70082 | -53.03315 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 53880494-a60e-32e2-8c4b-0d3f9d4c9df9 | -10.70055 | -53.03785 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 065a7012-090d-3d49-8628-cb242eb24da8 | -10.70033 | -53.0368 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f01f3810-d962-3d6e-92f8-3602bc25c3d0 | -10.70003 | -53.04151 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2043210b-1619-3b49-9caa-15d81f4dcce6 | -10.69983 | -53.04047 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 632abf56-2fe8-3800-bd2c-99f6745cbc4d | -10.69698 | -53.03366 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0cb6c9dd-ef51-34d9-991b-395df3f89e58 | -10.69646 | -53.03732 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 48aa03f3-1cb5-3065-86f9-a1564f9af36e | -10.69623 | -53.03627 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 70745e7b-70df-3689-b3dd-131889a75c29 | -10.69593 | -53.04097 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a238fdfc-c26b-3e9a-8a0f-13b61793fa22 | -10.69574 | -53.03992 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e76386a8-355c-3e8d-b533-2b00925d49fb | -10.69524 | -53.04358 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec3da810-3108-3acf-97da-3ca66f105f3f | -10.69237 | -53.03674 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8e70b75-df03-3bac-9b1c-a3db7976cb2a | -11.52954 | -53.44318 | 2024-10-06 05:12:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8af346a-8654-3cf3-92af-3cd9d630523f | -11.52551 | -53.44262 | 2024-10-06 05:12:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e8889ae-6277-3b45-bde3-b7b6abc7a52f | -11.26154 | -53.30611 | 2024-10-06 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87f30074-f8f8-3455-862d-da491e0afae2 | -11.25749 | -53.30557 | 2024-10-06 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b2317f3-fc81-3dc3-83cf-d14a69c9265e | -10.94067 | -52.40737 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ba276c2-9c48-30dc-b607-b2e3129847f1 | -10.94012 | -52.41141 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4f6b5ec-01f0-39a0-85ca-5e4d646e6b7a | -10.93694 | -52.40268 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 549450f5-d46b-3138-a691-213215596840 | -10.93267 | -52.40205 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2042123b-4cb7-3c85-b3f6-ba737a3298c0 | -11.24089 | -53.74032 | 2024-10-06 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7341bf00-521a-3ee8-b769-485755356e22 | -11.24031 | -53.74168 | 2024-10-06 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b9cad65-f118-32f5-954b-2c59b3733ec9 | -11.23695 | -53.73974 | 2024-10-06 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c0f3b4a-d60c-3b6f-b441-035fa4c2c18c | -11.23681 | -53.85489 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 22dfc515-0e78-3092-afc7-fc2a79f3311c | -11.23623 | -53.74475 | 2024-10-06 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d262bbde-26f5-361d-be1d-9e55bbb45bb2 | -11.23612 | -53.85995 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3500087-de3a-396f-b941-13943f3a9d4d | -11.2359 | -53.8583 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7b3d8acc-d64c-3364-9e41-653c7966a183 | -11.23543 | -53.86497 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b82470a2-11be-34cd-be32-00a80a3f75a6 | -11.23518 | -53.86334 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 066c1c3f-a18b-35bf-b98b-d456a7498994 | -11.2329 | -53.85432 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a15af338-3455-307f-822f-9b4f2f173a96 | -11.23273 | -53.85268 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f388dd40-0b23-3d97-9348-dbc3457f0449 | -11.23221 | -53.85939 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 195b822c-0d29-395e-b651-54bd4ba2dfae | -11.232 | -53.85774 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 74759d79-19af-3f85-ad05-5646db4bba1f | -11.229 | -53.85375 | 2024-10-06 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d49066b-465a-32fa-bf15-d6c913f02368 | -12.67658 | -53.19278 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7440ec6d-3460-35eb-a609-36a4bde249d0 | -12.67242 | -53.19218 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a879301-f5d5-3a66-ae7c-b3102789176b | -12.63587 | -53.11566 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22657d34-9340-3bbb-a843-0f47918981b5 | -12.63536 | -53.11957 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14391f66-c159-3e99-af5e-537c2f333e37 | -12.63492 | -53.11295 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 087745a8-efaf-365e-ab79-e6ed6d77bc21 | -12.63438 | -53.11685 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6552d9da-086c-3cf7-a24f-cc00ce796aa6 | -12.63384 | -53.12074 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0ae4bd69-5c59-3082-91b1-6ba060c6052d | -12.6333 | -53.12466 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 576b3770-b1d8-33bf-9007-a3bcc1fcef06 | -12.63221 | -53.11114 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ff8c9f3-0b40-3e6f-ba41-6a72f0e6e92a | -12.6317 | -53.11504 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c708212c-3ed7-30cf-9f71-a95b883c1481 | -12.63128 | -53.10848 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba324618-6f7c-32ee-9c29-f06ef4473168 | -12.63119 | -53.11894 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6ae4622f-d343-3632-91df-5b663218be0a | -12.63075 | -53.11234 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 79710510-0e6e-3db9-a635-c552794475ef | -12.63067 | -53.12286 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4bb4a111-3656-3dea-a402-5286b5046a50 | -12.63021 | -53.11623 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4bf2c0fc-581f-39d4-b670-5f0d83eee8c6 | -12.63016 | -53.12678 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 294156b9-5f8d-3ad6-9b2a-e75bfca37e66 | -12.62967 | -53.12012 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f93a0c67-2442-3939-a866-cb62594a7438 | -12.62913 | -53.12403 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7dc7c94e-e894-3fd7-9de8-c93d46f2e53d | -12.62858 | -53.12794 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73c2d850-3e2e-3fcd-9838-2529a30046c5 | -12.62803 | -53.11054 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3be5354-04dd-305f-9210-d4500223b0b2 | -12.62752 | -53.11442 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed8bd5f1-eb6c-332b-abbd-5e20b672718c | -12.62701 | -53.11832 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5a8af9fb-6dd6-31b3-9f87-e019d7d52a68 | -12.62657 | -53.11175 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9642e8ab-864d-3409-b5ad-952e5f337c3f | -12.6265 | -53.12223 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fb5a4543-3d3c-33f9-b0eb-f9dd2d58124d | -12.62603 | -53.11562 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9ca9171-dd68-3e6c-bc0c-60888b137515 | -12.62599 | -53.12616 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0d54cef-6fb1-375f-ac1f-2eee877b81ce | -12.62549 | -53.11951 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82b1f391-a3ba-38c0-b7d5-fb0a9679dadb | -12.62495 | -53.12342 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d7911ed-d3a5-38b5-8393-9dbe8e7f72ed | -12.62441 | -53.12734 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd42672c-004b-3d93-ad1a-171ff5a86485 | -12.62185 | -53.11502 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f6db580-4e68-3d92-a74a-e0faed2d9ea5 | -12.62132 | -53.11891 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95147227-8ced-311d-8b96-2dc16e90b0b8 | -12.62078 | -53.12281 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a3a7bc0-3eb6-3d6f-aee7-55da3bad4d1b | -12.62024 | -53.12672 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2aa797d-9a44-38f3-80a6-ddca5d472871 | -12.61768 | -53.11443 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32edff52-9fd4-30be-bcbe-6197ee142468 | -12.61754 | -53.14629 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffd1b66b-7973-3937-b0ab-1c201dfb2e8e | -12.61714 | -53.11832 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58eee5d7-449c-39d7-9150-15ade837f69d | -12.61661 | -53.1222 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bb0edfb-3184-3332-ae8d-f839d0bb938f | -12.61607 | -53.12609 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e95040e9-d84d-3bab-80bd-e449542816de | -12.6135 | -53.11383 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73a9e076-2ad4-36be-82a0-f52da05dcc6f | -12.61337 | -53.14568 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21b6d100-ea63-3a6d-a7d3-11d328a7da3a | -12.61297 | -53.11772 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdaba91b-70f5-39d3-adbb-fe47586df6a6 | -12.61243 | -53.1216 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e989d2e3-67aa-349b-bf44-ad95d2f95bb4 | -12.6119 | -53.12548 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5c8f363-1a8d-3100-aaa4-a8fd5b43cfbf | -12.61137 | -53.12936 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d6d514d-f03f-3331-9674-0adb1d22e14e | -12.61082 | -53.1333 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73eb687d-51df-3232-af3a-1983a5ec2ad6 | -12.61029 | -53.13723 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f91d8bde-d6f9-3198-840c-e9f6f2f90ea4 | -12.60985 | -53.10939 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44b63b6a-b12e-3072-8b3f-6bc045a01363 | -12.60921 | -53.14503 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a70c2d1a-8861-3932-84cb-eb6685a00cd9 | -12.60879 | -53.11712 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d241d9a6-a754-3d17-ab92-82195afff40a | -12.60826 | -53.12099 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eba5f419-f950-3dc0-ba72-f0c484db7bdd | -12.60773 | -53.12488 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c3b0ced-e2fc-34e5-b2bc-9331e4469e4d | -12.60719 | -53.12877 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31b16a16-33a5-3f74-bde5-cd72b6c01916 | -12.60666 | -53.13268 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4fe0232-ca1b-33ae-b8a9-49a6fd56f47a | -12.60612 | -53.13659 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edc3add5-a7c9-3747-a072-ed590db0c438 | -12.60409 | -53.12038 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dafef793-0970-3dd4-b61f-62a2b9a723f2 | -12.60356 | -53.12427 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4547cb54-5d18-3001-a291-d85a23d7d695 | -12.60302 | -53.12816 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f87c895-9596-3cf8-90a4-6bd8603626e2 | -12.60249 | -53.13206 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cf52ed0-5040-3338-bb1c-587bde85d05c | -12.60196 | -53.13595 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e56805d-86fa-3f77-8817-b80073bee4b1 | -12.59992 | -53.11977 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad5e49a8-c443-3aae-867b-65419d9c7554 | -12.59939 | -53.12365 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d5e4129-d0cd-397e-9a2d-6df57634c79b | -12.59886 | -53.12753 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 169e15b6-897d-318c-80b5-fedebfb26fe7 | -12.59832 | -53.13143 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 363d33dd-2500-3623-80c1-e052042bc249 | -12.59779 | -53.13533 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| febb6b2e-d1cc-3479-a3e9-c8b461a757b3 | -12.59584 | -53.48123 | 2024-10-06 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README106.md)
