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
| 319c4d5d-de7d-393b-a75d-9e2defc48a18 | -7.8599 | -46.4629 | 2025-10-27 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 3a9a154f-9631-3a88-93ad-1bdbdf4ffcbb | -4.4433 | -43.4027 | 2025-10-27 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 32704d5d-e431-3e63-98c4-70a096b36170 | -4.4663 | -45.4814 | 2025-10-27 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 44.7 |
| fa4844cb-40b6-3464-a34e-6774ea6d2058 | -3.5782 | -44.5297 | 2025-10-27 00:30:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 829146bd-1384-328c-be97-53052bb9d591 | -7.8596 | -46.4853 | 2025-10-27 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| d4fa75b9-a2d0-3bcb-9235-a4fefa0c5a67 | -5.6425 | -47.6271 | 2025-10-27 00:30:00 | GOES-19 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 4f9ad171-7f2d-39fb-8e8b-4b765b66db67 | -4.462 | -43.4016 | 2025-10-27 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 6e944b64-3914-3e2f-ae57-be899d30de45 | -3.71 | -47.6621 | 2025-10-27 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| fbf94cb5-88e5-3aa6-ac0f-f898ad48a2da | -4.4477 | -45.4824 | 2025-10-27 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 88.8 |
| ab798a8a-de61-338a-9a6f-14c4857550b2 | -12.2695 | -43.7526 | 2025-10-27 00:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 00246cb6-33ed-3ae6-9d77-cf581429468e | -3.7287 | -47.6395 | 2025-10-27 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 07e663fa-8d75-38ae-971c-cb4a77220ece | -3.3573 | -44.0361 | 2025-10-27 00:30:00 | GOES-19 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 3da649b4-b5a4-3338-a1be-c52967d263ea | -8.5236 | -44.5383 | 2025-10-27 00:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| a4492d02-3d33-3d7c-bdc9-48ba04b36563 | -10.8401 | -56.959 | 2025-10-27 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 8f49e4d8-35ff-3ea4-a824-44c9623aff2c | -3.7286 | -47.6613 | 2025-10-27 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| f176ee41-cbd5-3713-82fe-48d4ed5d4e96 | -4.3877 | -43.3362 | 2025-10-27 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| cc6f2b08-55af-3c0d-acc1-531082b78454 | -5.5423 | -43.9558 | 2025-10-27 00:30:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e1dc6d62-b0e5-3399-847e-11905d2b9119 | -10.7676 | -44.1905 | 2025-10-27 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| b94c6a18-3dbd-36d2-b89a-19c90fa9ee15 | 1.1502 | -51.0603 | 2025-10-27 00:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 70.5 |
| e92d6d24-52ca-30bc-90bc-b3686c7c25a9 | -3.3759 | -44.0353 | 2025-10-27 00:30:00 | GOES-19 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| cddc557c-2a37-3302-a83a-44af696cc81a | -11.9221 | -43.8318 | 2025-10-27 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| dfd21bc0-db6c-31c7-b038-528956fc0f5e | -4.4805 | -43.4237 | 2025-10-27 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| fc4d6179-adbf-3858-8b41-00585a1c994a | -7.8408 | -46.487 | 2025-10-27 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| fdeb6ef5-b119-309e-a950-83471d345b39 | -11.9225 | -43.8081 | 2025-10-27 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 2498923f-06b7-3eef-bd9f-3ab911e4618c | -4.4618 | -43.4248 | 2025-10-27 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| c138c411-452f-36a5-8805-efb81fb795e6 | -4.4479 | -45.4599 | 2025-10-27 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 351.2 |
| 60d4e14b-c413-3b5c-9606-dcbd31df1fb1 | -4.448 | -45.4374 | 2025-10-27 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 8c4aba47-b565-3231-b4e3-75653af6bcf2 | -4.4804 | -43.447 | 2025-10-27 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 9e1ecaa0-3a00-386a-afb6-1737eb431fc0 | -12.2888 | -43.7495 | 2025-10-27 00:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 87cba29b-6815-3202-a82d-66ad77f4677a | -7.0692 | -46.7541 | 2025-10-27 00:30:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 9e328c11-83cd-36c4-8d79-d7d6b5818f05 | -4.4807 | -43.4005 | 2025-10-27 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| feba1bb1-6dfe-3229-9ca4-860a039c47ca | -3.7286 | -47.6613 | 2025-10-27 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 2847026e-e430-39ef-80ab-ecf9c48b8b84 | -4.4477 | -45.4824 | 2025-10-27 00:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 3460382a-5e43-35f8-a0bc-3c217a316736 | -9.463 | -47.7227 | 2025-10-27 00:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 245b3d85-ccee-33b6-85d2-57a3856efcb8 | -4.4433 | -43.4027 | 2025-10-27 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| db3dcafc-aa16-32d4-bbaf-e48e48712f2c | -4.4617 | -43.4481 | 2025-10-27 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 987126b3-c15c-38ec-a134-78a5c4af1035 | -3.4583 | -49.9625 | 2025-10-27 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 2e2585ae-eeb7-3062-a731-b4cf0e862dc2 | -4.4994 | -43.3994 | 2025-10-27 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| b9f9cd0d-4e3d-389f-9571-c82b50397add | -10.7676 | -44.1905 | 2025-10-27 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| cef3a9b1-8cdb-3754-849b-07343f696d91 | -4.4479 | -45.4599 | 2025-10-27 00:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 743.6 |
| cbbd047e-f153-31d2-8801-b0d93784a7fe | -11.9221 | -43.8318 | 2025-10-27 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| bc2fd3f4-0f94-3321-b6b2-9c8f8221ba58 | -4.4666 | -45.4363 | 2025-10-27 00:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 22e82a48-1ace-3932-8a01-805a3652cd12 | -4.4431 | -43.4259 | 2025-10-27 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 2f608c93-0cb1-39da-9b72-82ebd1b08eaa | -16.2093 | -45.1037 | 2025-10-27 00:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 87c09945-8a26-3894-9f8d-5d5d4af9b436 | -3.7287 | -47.6395 | 2025-10-27 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 042994c0-d80f-38ea-ad34-789c38033f89 | -5.6425 | -47.6271 | 2025-10-27 00:40:00 | GOES-19 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 9d16445d-2a8f-39de-946f-d5d51034282d | -4.7578 | -46.4255 | 2025-10-27 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 47.5 |
| b97e86b9-defb-33e2-aae6-87e82aba2619 | -5.5423 | -43.9558 | 2025-10-27 00:40:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| a1458fca-2f4b-30c6-8f09-9a281a6941b0 | -10.7484 | -44.1932 | 2025-10-27 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| bb6fcf8a-b684-3fad-9e94-31ad828b2b3e | -3.7101 | -47.6403 | 2025-10-27 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 35317101-78b9-35c9-bf3f-b895dcdd8e07 | -7.8408 | -46.487 | 2025-10-27 00:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 80eee2f6-c385-3006-ba64-10f062b0dc64 | -4.4665 | -45.4589 | 2025-10-27 00:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 203.9 |
| 4614ba8b-1ef4-3733-a41f-34fc7f9248c8 | -4.462 | -43.4016 | 2025-10-27 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| fffe175f-b1df-3449-a32c-2ee0fa67cbad | -7.0692 | -46.7541 | 2025-10-27 00:40:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 551eeda3-ec35-3884-ad32-d22d93187bf9 | -4.4992 | -43.4226 | 2025-10-27 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 5b5ad1ef-699d-31c4-948c-3982f4f6e9d7 | -16.1895 | -45.1078 | 2025-10-27 00:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 8b40a18e-7a92-3a8d-aa11-02a3962ef976 | -7.8596 | -46.4853 | 2025-10-27 00:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 94618a75-d900-32e1-80be-5066e3ebd8c1 | -7.8599 | -46.4629 | 2025-10-27 00:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| b914c59a-3485-3c14-a31e-402d3e6b125f | -7.8411 | -46.4646 | 2025-10-27 00:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c8573112-32bd-30c9-8f01-983116e5f5dc | -3.71 | -47.6621 | 2025-10-27 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 87314968-4211-3cd0-9072-53c0a525c94f | -16.1901 | -45.0841 | 2025-10-27 00:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 134.2 |
| e526cf45-3b2b-34e4-b8d4-170cda03c9f3 | -4.4804 | -43.447 | 2025-10-27 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 44c4f420-03c3-3e56-bbe0-ea3b925790ce | -16.2099 | -45.08 | 2025-10-27 00:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 123.3 |
| b9dfa78c-663b-33d6-b840-c7f0b529f8fb | -4.3877 | -43.3362 | 2025-10-27 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 3dc00aea-1d13-3265-bd41-78e07ba960cb | -4.4663 | -45.4814 | 2025-10-27 00:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 39.1 |
| c2ca185d-84f0-3adc-acfd-077b3035852d | 1.1502 | -51.0603 | 2025-10-27 00:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 61419d7d-97b2-3562-8a91-0ec8356f95ae | -4.3879 | -43.3129 | 2025-10-27 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| ebb03e80-d193-3c02-bb19-4b02e2415c2f | -4.4618 | -43.4248 | 2025-10-27 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 236.7 |
| e0610593-d1db-33e6-ac50-146bc73c40e3 | -12.2888 | -43.7495 | 2025-10-27 00:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 267e811e-4ea8-3164-8523-1e5654211b21 | -12.5258 | -47.5678 | 2025-10-27 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| cae1c444-f501-3bab-8e1f-8a33aae7f3a2 | -12.2695 | -43.7526 | 2025-10-27 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| f4342466-02c4-3e2d-b530-9f913a36c6cb | -4.4805 | -43.4237 | 2025-10-27 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 290.1 |
| 3dff9d9a-80c3-357d-a120-89cd1b9a6a76 | -11.9225 | -43.8081 | 2025-10-27 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 63b7a59c-5318-3fb9-9278-f628436257a5 | -4.448 | -45.4374 | 2025-10-27 00:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 154.4 |
| 25e2c18b-cab3-3912-a140-dfbb8ae8d963 | -10.8401 | -56.959 | 2025-10-27 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| bee942f6-2171-3dd1-aacf-582c35413888 | -4.4807 | -43.4005 | 2025-10-27 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 124e8e9c-afaf-35a8-b7fa-4c41568b75df | -4.4479 | -45.4599 | 2025-10-27 00:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 875.6 |
| c62e6c69-1595-37f6-a6ac-57cdaad976b2 | -3.71 | -47.6621 | 2025-10-27 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 67b3f093-082c-3e89-a45e-4386336000d1 | -7.8408 | -46.487 | 2025-10-27 00:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 786774b7-7307-3cda-8ac7-f41983e092b7 | -4.4618 | -43.4248 | 2025-10-27 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 0e35cd5b-060c-367c-a225-206ab14df199 | -4.4666 | -45.4363 | 2025-10-27 00:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 2a16414c-419f-322b-b41c-9fb8007a4ed5 | -4.4477 | -45.4824 | 2025-10-27 00:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 2ae416cc-64ff-31ec-ab09-8f62ff6d77c3 | -13.2969 | -54.3861 | 2025-10-27 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| f0007555-3149-3363-a9e5-f5a821a200e3 | -4.3877 | -43.3362 | 2025-10-27 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 40fab740-df2f-3840-8858-967c08d85c64 | -13.2966 | -54.4068 | 2025-10-27 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 066f5cc9-b8d1-3b0d-9e33-975a2ba6cd63 | -4.4805 | -43.4237 | 2025-10-27 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 2ea135a2-9c59-3e35-b157-baf50c12eb9b | -7.8411 | -46.4646 | 2025-10-27 00:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| ce59065a-56eb-3d99-92f8-681903964f14 | -7.0692 | -46.7541 | 2025-10-27 00:50:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a84918c4-fd2a-3bbb-a89f-184190e97855 | -7.3324 | -48.4857 | 2025-10-27 00:50:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| e3dcddb0-b19c-3bb1-8e3f-c2471bbe0ef0 | -4.4431 | -43.4259 | 2025-10-27 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| fc8c0b60-07bb-3de8-a529-b7172382ed99 | -3.1612 | -50.3298 | 2025-10-27 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| fccac739-321c-304e-93a9-4b24fd4b5dbd | -10.8401 | -56.959 | 2025-10-27 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| a7bc5aa1-dcd4-3d33-9221-ae219f33142c | -4.4665 | -45.4589 | 2025-10-27 00:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 248.5 |
| 265e7d87-6cb0-3ab0-8041-bbc08eaf8bd8 | -13.316 | -54.3841 | 2025-10-27 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 1e3b3902-315a-3ed5-8f18-3949eb203567 | -4.4807 | -43.4005 | 2025-10-27 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 7616354a-1104-3a87-8930-cf288ac33c1c | -10.7484 | -44.1932 | 2025-10-27 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| be42ae61-a4b0-3217-89b8-4ee8b9411e32 | -10.7676 | -44.1905 | 2025-10-27 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| c76abf76-03a7-3b4a-89a9-acf94356282f | 1.1502 | -51.0603 | 2025-10-27 00:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 0e58f3db-c924-3df0-8dc8-f470050bfd48 | -7.8599 | -46.4629 | 2025-10-27 00:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 118eea4d-4b2e-37a5-b64a-2c3f453dd35d | -12.2695 | -43.7526 | 2025-10-27 00:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |


[Clique aqui para ver as próximas entradas](README9.md)
