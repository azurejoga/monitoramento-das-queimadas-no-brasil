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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c47b84b3-58e7-30c0-a405-847927bf18fa | -7.18626 | -48.2109 | 2024-10-16 04:32:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1ce6998-3ab9-3497-aaa2-5a376f5671c5 | -7.10072 | -48.32208 | 2024-10-16 04:32:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 240b328f-9534-3bf0-b45e-d8a96c7362d0 | -7.09741 | -48.32156 | 2024-10-16 04:32:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f845f78b-f8ea-353f-8aa7-79d4a3d8dca6 | -6.74287 | -48.06977 | 2024-10-16 04:32:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36aac7db-99dc-3d8b-8105-92015c793e09 | -6.51262 | -47.82849 | 2024-10-16 04:32:00 | NOAA-20 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d958e561-6e02-39af-9edf-dc8763519357 | -8.00065 | -47.21257 | 2024-10-16 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95238aaa-fcb7-3c2b-a47c-1be6f95df585 | -7.801 | -47.29731 | 2024-10-16 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7c11c38-6770-30b3-85bf-7e6ad8456f32 | -7.64185 | -47.16425 | 2024-10-16 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d1d0564-264a-37dc-91f8-54f97b2944c9 | -7.6413 | -47.16779 | 2024-10-16 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ac77306a-7da1-3a28-a1ac-34656b515a3f | -7.63866 | -47.22865 | 2024-10-16 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ec6f05d-2cd8-308f-aec1-3e3b6994f526 | -7.63851 | -47.16374 | 2024-10-16 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fecc6b3b-3cbd-3d36-834f-0ad3c1682ce3 | -7.63796 | -47.16727 | 2024-10-16 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47305852-c68e-3786-a094-bc49dcd763c4 | -7.6313 | -47.16623 | 2024-10-16 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c0de7af-2a49-3ce2-baac-d82be39b0407 | -7.62797 | -47.16571 | 2024-10-16 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75ce7b55-a353-39b0-bb51-b7ebb82a6ddd | -7.492 | -47.58168 | 2024-10-16 04:32:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ee0c93c-bc0b-3234-bea6-333b35efe2db | -7.45543 | -46.96515 | 2024-10-16 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7d24fdc-42ee-33e9-ab6f-631bfeb298e7 | -7.33145 | -47.28128 | 2024-10-16 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6a50cc9-bcce-3a26-a5d6-ceb2eddc7863 | -7.21454 | -47.33525 | 2024-10-16 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cb43159-8026-3534-a0bf-2fd39a5a4454 | -6.91186 | -47.3161 | 2024-10-16 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 29fa67c6-fca5-3bba-b312-ed5bf90a3600 | -6.91131 | -47.31959 | 2024-10-16 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dd7a09bc-2162-3794-a9a5-0f016e94299f | -6.90908 | -47.3121 | 2024-10-16 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f21b55ed-8336-327a-8223-aea0054bdbe4 | -6.90854 | -47.31559 | 2024-10-16 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 722169fe-f75f-37ef-bfd9-25245036096d | -6.90136 | -47.31804 | 2024-10-16 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 71c7df32-0a4f-33de-bbd4-939cbfcf9891 | -6.72597 | -47.22316 | 2024-10-16 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18e11255-2247-362d-8d1e-886ab31bce87 | -9.32412 | -47.37035 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ebc8a86-ff03-3a52-8de0-09ecc255f24a | -9.28801 | -47.60451 | 2024-10-16 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fcf7542f-c4d6-32d3-a9bb-141867a38ac7 | -9.28746 | -47.60804 | 2024-10-16 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9371fc7d-2716-3f3b-ae85-4c1dd85025e3 | -9.28468 | -47.60399 | 2024-10-16 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e60448d1-9121-3caf-91ed-567081247961 | -9.28413 | -47.60752 | 2024-10-16 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c80a7de-906a-31e4-b8e2-fc9f6f1b2d97 | -9.19528 | -47.56841 | 2024-10-16 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44bec23d-76fc-3317-8ca9-55d396fb84aa | -9.12028 | -47.70102 | 2024-10-16 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf157587-465a-3141-b021-5eb37356c27e | -9.01194 | -47.67653 | 2024-10-16 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c61196b-2b45-356b-9d97-65377989ce71 | -8.8615 | -47.55259 | 2024-10-16 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15cfba09-3e97-3515-8c7e-351386a95d83 | -8.52436 | -47.44938 | 2024-10-16 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a80e75d-152a-3b6b-abea-1ffa8de36a92 | -8.51662 | -47.45538 | 2024-10-16 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c1444e6-9841-371a-9c03-be39d26852c7 | -8.51275 | -47.45837 | 2024-10-16 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60feab17-23d0-3a1d-84fc-1622b628ce25 | -8.50997 | -47.45432 | 2024-10-16 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00d0b61c-56ee-316a-97de-6edc84531554 | -8.50943 | -47.45784 | 2024-10-16 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f2f5818-ec9f-3e31-a122-1c9f657c2d35 | -8.24771 | -47.67933 | 2024-10-16 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7463b4f3-a92c-38e6-81dc-da2cf89adacf | -9.21034 | -47.95208 | 2024-10-16 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e72e2c62-df7c-3780-bff4-deb7418028eb | -9.20979 | -47.95557 | 2024-10-16 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ff017be-aa67-334d-8186-4a793fd6aeb7 | -9.20588 | -47.93705 | 2024-10-16 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f10d1a53-bb17-3093-af62-24eb0f6be67c | -9.20425 | -47.94754 | 2024-10-16 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b562ed99-728b-300c-9fd7-3aa8eb8f682b | -9.20371 | -47.95103 | 2024-10-16 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 937df107-d157-3f22-8e8b-d015370da96f | -9.20094 | -47.94702 | 2024-10-16 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac565462-a985-3d98-b17d-c26188ae25ee | -8.91053 | -47.91528 | 2024-10-16 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54c51d80-f2a2-3b1d-ac60-2c600c61eb6e | -8.90721 | -47.91476 | 2024-10-16 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 468af6fc-a63d-3629-a3dc-513f5387eaf5 | -8.87181 | -47.88058 | 2024-10-16 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77a3a339-b523-308c-bfee-38aaf6e8d088 | -8.87126 | -47.88408 | 2024-10-16 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11a77cfc-c9df-326f-8967-11b88c063a83 | -8.86795 | -47.88356 | 2024-10-16 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bb14350-56f0-3ccd-b2c4-26b4b8174f87 | -8.8441 | -47.92661 | 2024-10-16 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d87ff66-d21a-3dbd-a9b6-941ce3857abb | -8.80312 | -47.86299 | 2024-10-16 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4700986c-7e47-33ac-86e6-6caec5035128 | -8.80258 | -47.86649 | 2024-10-16 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42e6de1d-33da-32e6-b353-1464d7fce54f | -9.99889 | -48.20919 | 2024-10-16 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a27215cd-bd07-36af-b5e0-ad56eb944516 | -9.99583 | -48.64119 | 2024-10-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 97672164-f99d-3317-b5b7-317fd576a785 | -9.99252 | -48.64066 | 2024-10-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 43bb85d2-ede0-3bdd-a8d4-b68e8beadc14 | -9.94798 | -48.1222 | 2024-10-16 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9167cdcb-4446-3874-b4b3-aff47ff5a1d1 | -9.94521 | -48.11816 | 2024-10-16 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e88ef08f-c9c4-38f9-aa0a-ab55d9040497 | -9.88121 | -48.24457 | 2024-10-16 04:32:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8368a2b5-d57a-321e-961d-286405e17ad8 | -9.74732 | -48.58036 | 2024-10-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a9ad5df2-05ad-339c-8982-e92d7b14ce68 | -9.65182 | -48.56158 | 2024-10-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 298ad2df-2c98-3193-8dda-c89337d8c739 | -9.63001 | -48.5471 | 2024-10-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22e4f662-aeaa-3fee-8810-293ca11f3272 | -9.62946 | -48.55058 | 2024-10-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f8afc22-9545-3c9f-949d-547fa2ead2f4 | -9.62616 | -48.55005 | 2024-10-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 054d2560-39e5-3aa5-8a7f-8e39201929b9 | -9.61465 | -48.60173 | 2024-10-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b556ca2c-6c34-3000-ad50-4f97dc69c7be | -9.61134 | -48.6012 | 2024-10-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c0f0dbea-167d-3afe-b105-b59724fda2f9 | -9.51993 | -47.79566 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07dfe560-ab36-34cd-8916-53db7db9aeb5 | -9.51938 | -47.79917 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5090793e-8aa4-3ec3-9168-f16b5ce9bc15 | -9.51606 | -47.79865 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7c8eb7f-f3ec-3d92-a7cb-f335bfbb77e6 | -9.51274 | -47.79812 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58adefc5-ff7d-3f7b-a3d9-12db7fd5db47 | -9.49176 | -47.82366 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55c4a5d6-1a5f-329a-9314-957a5def015a | -9.48844 | -47.82314 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6a9b331-7464-352e-85e7-d065ce55622d | -9.48621 | -47.8156 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e2193119-2dd0-3ce3-bd90-79828c771328 | -9.98578 | -47.50556 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1732a4f1-3e80-31fe-a689-abfaa6d99f99 | -9.98243 | -47.50504 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90c2213b-ee9e-3b81-9c38-f142aa0f142e | -9.62147 | -47.73243 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45b76f96-6389-3dbc-a89c-e28534c81c7e | -9.61108 | -47.55677 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8454ecb-359a-3ea1-a995-4724278d507f | -10.03045 | -47.65464 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2026ca6a-5682-3715-8230-8f161d0c7b92 | -10.02663 | -47.67951 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e9c96f8-a5be-39a0-89ee-b603fcb808a4 | -10.02329 | -47.67898 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da9aeb00-51d9-321e-9425-863d5ca8a28d | -10.02274 | -47.68255 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55dd4219-0e7b-3b9c-a46b-d13c68aee378 | -10.83572 | -47.78375 | 2024-10-16 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36151545-5cf7-3c01-8f0e-b30de382004f | -10.83516 | -47.78735 | 2024-10-16 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 522d5f74-50c6-3ed2-af84-020dddcce51d | -10.7576 | -48.52728 | 2024-10-16 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7a1f35a8-41e5-3eab-a917-f90a94be92a3 | -10.75706 | -48.53078 | 2024-10-16 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22a2507f-d365-3f4c-9021-88c02cb89357 | -10.7543 | -48.52674 | 2024-10-16 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7425a5a7-81a2-3802-b14a-fff0237bc892 | -10.75375 | -48.53024 | 2024-10-16 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cb52bd7-85c3-3459-ad68-ebc4a0ea497b | -10.68685 | -48.54438 | 2024-10-16 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a0c90ca-3e00-354d-9783-ea48f1da5b22 | -10.68354 | -48.54386 | 2024-10-16 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58890ba3-df1c-3616-9e88-3cdb6f4488c8 | -10.50299 | -48.91589 | 2024-10-16 04:32:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 199be7a8-afab-39fb-9706-4d85e6736fdb | -10.49969 | -48.91535 | 2024-10-16 04:32:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8eae4815-2a7f-39e0-b318-ccd75996b7aa | -12.18227 | -47.98566 | 2024-10-16 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0842999-6d23-30fc-8893-f88f74ba0d71 | -12.06968 | -48.38532 | 2024-10-16 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7804af8b-9d0b-3c2a-bc06-4170b3a9ca43 | -11.73214 | -48.65739 | 2024-10-16 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0bb6cb5a-b7a0-3019-89e7-b0e52e0aafe3 | -11.72828 | -48.66037 | 2024-10-16 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3b3a7e2-6a9d-3491-bd44-e02ddad864d3 | -11.72552 | -48.65633 | 2024-10-16 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bb94bf87-8bfe-37ba-ab7e-52df536acfe4 | -11.72497 | -48.65984 | 2024-10-16 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 72e16e5f-4ba2-34d2-a43e-02c27070bb60 | -11.58337 | -48.43502 | 2024-10-16 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 013f0cf0-687e-30b2-99f3-9d91e2050f5e | -11.52781 | -49.07411 | 2024-10-16 04:32:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cff86683-6878-30ed-949f-86d61c5afda8 | -11.31799 | -47.75586 | 2024-10-16 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README52.md)
