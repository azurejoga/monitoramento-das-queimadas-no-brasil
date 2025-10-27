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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8af958b5-d3de-3ed4-bfc7-a1442ca91610 | -4.4433 | -43.4027 | 2025-10-27 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 440a72ab-db5c-3f9c-8c78-2ee991964548 | -16.1901 | -45.0841 | 2025-10-27 00:50:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 9e6fd29a-f2cf-3d0b-b483-6537e60a856d | -4.462 | -43.4016 | 2025-10-27 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 54a992bd-b195-34a5-b730-a8cb91214d73 | -3.7101 | -47.6403 | 2025-10-27 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| d5f8c1bc-57b5-3f20-b903-9a380ffd5517 | -12.2888 | -43.7495 | 2025-10-27 00:50:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| f1f5102d-f60e-3ecc-8930-56962ffea018 | -4.3879 | -43.3129 | 2025-10-27 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 98c9abe5-ee6f-3c93-a4a0-6f1e4f610599 | -6.8777 | -43.5686 | 2025-10-27 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| aeee8e45-1d12-3cf0-990f-a75d1cb79c43 | -4.448 | -45.4374 | 2025-10-27 00:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 201.1 |
| ba5ae69f-48d7-3bba-9fa1-d6c3203174a7 | -7.8596 | -46.4853 | 2025-10-27 00:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 839305b8-a3d9-3bec-890a-2c3bcb702e71 | -4.4617 | -43.4481 | 2025-10-27 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| b8ea3399-3ca1-37a6-8b46-f1f939804bbc | -3.5595 | -44.5305 | 2025-10-27 01:00:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| f7d2be3f-3248-35a0-b05e-98e44cd857ed | -4.4663 | -45.4814 | 2025-10-27 01:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 586ad3bb-ad6a-39c4-b750-cb3634ae075b | -3.5782 | -44.5297 | 2025-10-27 01:00:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 20c0368c-5dba-3ecc-95e3-4eb8d4e4d9bb | -4.4665 | -45.4589 | 2025-10-27 01:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 234.0 |
| d4fdd4c3-59af-31dd-ade1-bdeeae9698c9 | -4.448 | -45.4374 | 2025-10-27 01:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 234.0 |
| fb8be606-1451-3004-bb1b-4a21086c7586 | -4.4477 | -45.4824 | 2025-10-27 01:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 159.9 |
| e22c50cd-ab2a-30db-96e6-7976e70812ee | -4.4479 | -45.4599 | 2025-10-27 01:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 666.5 |
| 398accb9-47e0-3e52-a6c8-8335a08b360e | -7.8411 | -46.4646 | 2025-10-27 01:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 19f084da-305a-38a0-9a53-33fbbf896c1d | -4.4433 | -43.4027 | 2025-10-27 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 675aa8b6-0ee4-3f51-a345-d4f012fb73e8 | 1.1502 | -51.0603 | 2025-10-27 01:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 88861829-8fe2-3bb0-bc03-1cc2a887fdd4 | -4.4805 | -43.4237 | 2025-10-27 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| dac0bf96-ddc7-3244-ad86-b89598656e1b | -13.2969 | -54.3861 | 2025-10-27 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 95266e5d-64e2-37d6-99c9-cbafcbe000f7 | -10.7484 | -44.1932 | 2025-10-27 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 5c6a7fb0-799b-34d1-8040-ea4fc79bc8ee | -7.8596 | -46.4853 | 2025-10-27 01:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 50199047-e622-3315-8657-a18a74410291 | -16.2099 | -45.08 | 2025-10-27 01:00:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 5154a336-3ad2-38da-af48-d7e7034b95b7 | -13.2966 | -54.4068 | 2025-10-27 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| e756c43e-fe05-3095-b89e-189c3e47ff90 | -4.3879 | -43.3129 | 2025-10-27 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| cdcbc6f8-94d6-35d7-b350-bb684846040b | -7.8408 | -46.487 | 2025-10-27 01:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 0a135a58-a28c-3f60-ba64-abf6a459a9b9 | -10.8401 | -56.959 | 2025-10-27 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 73cf0520-7515-3a45-98c4-1833f2766f75 | -16.1901 | -45.0841 | 2025-10-27 01:00:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 80.5 |
| b57125be-fa9c-3708-b3ab-8cc839297d82 | -4.4431 | -43.4259 | 2025-10-27 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 57a129a8-4d52-3758-88a9-c0e1e8cb6036 | -19.0724 | -48.3148 | 2025-10-27 01:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 3e880715-61c6-323a-873c-93e5c777e1cf | -12.2888 | -43.7495 | 2025-10-27 01:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 2e282cb8-bd18-366d-8903-b4db0d6b86f3 | -13.316 | -54.3841 | 2025-10-27 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 08cdc3e6-5dce-3d32-9739-72f141675397 | -6.8965 | -43.5669 | 2025-10-27 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 9035945b-8130-389d-a7b9-dfb0834dbb72 | -4.4618 | -43.4248 | 2025-10-27 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 54133de1-eb1f-3a71-ae76-4366e076f266 | -3.4768 | -49.9619 | 2025-10-27 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 0942d7a7-8d03-3ccd-9680-527ed66d168e | -4.4666 | -45.4363 | 2025-10-27 01:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 85.9 |
| f5d3814c-09d1-38f8-9391-db2bc583f559 | -4.3877 | -43.3362 | 2025-10-27 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| fe654473-a32f-3bb8-93bb-1dde51ba9f09 | -13.3163 | -54.3634 | 2025-10-27 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 62551dda-aa0e-3b1f-90ff-72aca85850ab | -3.7101 | -47.6403 | 2025-10-27 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 115b03c5-21cb-3eb9-9420-d208c067004c | -3.1612 | -50.3298 | 2025-10-27 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3ed381c7-d649-3f8c-8898-ae0f5e20c2f0 | -4.462 | -43.4016 | 2025-10-27 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| ec3a6fd2-c929-3c8f-a66b-4b2e32caa39e | -12.5258 | -47.5678 | 2025-10-27 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| f3c76ef4-14b8-3979-91a4-fc286d4a4223 | -7.0692 | -46.7541 | 2025-10-27 01:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 4941f3dc-edbd-31d9-bc06-a34b75a4f89d | -13.2777 | -54.3882 | 2025-10-27 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 9a26e68c-6919-3486-8433-92a4860105c9 | -4.4807 | -43.4005 | 2025-10-27 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| b8686834-55e1-38fb-990b-9c65edd05e0a | -12.5258 | -47.5678 | 2025-10-27 01:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 5e9e3826-60f4-311a-8420-d0a6c89f2659 | 1.6203 | -55.726 | 2025-10-27 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 5d92d476-4cbb-3f32-9a60-a75b309f85ed | -7.8411 | -46.4646 | 2025-10-27 01:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| a61cd243-22ff-34b9-a66e-73c913f8fffc | -10.7676 | -44.1905 | 2025-10-27 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 521cec16-9898-310e-af08-65c97662af03 | -4.4617 | -43.4481 | 2025-10-27 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 4a90f654-f5e6-3f4f-9534-0f9ff00471c8 | -4.4663 | -45.4814 | 2025-10-27 01:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 653600c6-2dde-3244-b887-206384f58e7c | -4.3879 | -43.3129 | 2025-10-27 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| e412cd89-92eb-3460-8bd2-a41eac061820 | -4.4992 | -43.4226 | 2025-10-27 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 03d107c9-8908-3b37-8a94-5efbf8d24a1c | -6.8777 | -43.5686 | 2025-10-27 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 0b6ca320-f33d-3370-89a1-98aac21e82aa | -13.2969 | -54.3861 | 2025-10-27 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 852d4099-cdbe-33e9-b8d9-dc22010c56f3 | -3.5782 | -44.5297 | 2025-10-27 01:10:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 5e963b21-f140-376e-b224-c1d404d2394b | -4.3877 | -43.3362 | 2025-10-27 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| a254ba45-d50e-39c2-9e5d-2b27d0661cb7 | -4.4618 | -43.4248 | 2025-10-27 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 217.6 |
| e83407e7-564e-328a-a39a-b2a76cf1b8cb | -4.4477 | -45.4824 | 2025-10-27 01:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 6b7814af-3159-3dd3-9516-b269216260ab | -4.448 | -45.4374 | 2025-10-27 01:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 70727960-ee01-3e8f-af66-f6712eedf008 | -4.4804 | -43.447 | 2025-10-27 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| ab123122-cf81-3ed8-9bd0-53315e449edd | -10.8401 | -56.959 | 2025-10-27 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 9fcc77af-60fb-3bc6-ba52-57391a17a97f | -12.2888 | -43.7495 | 2025-10-27 01:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 6c4e9ccf-6f17-3e85-a252-cdbc43e354c0 | -4.4665 | -45.4589 | 2025-10-27 01:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 242.0 |
| a1037571-b1f1-3e7b-9698-83dc1219dff6 | -4.4805 | -43.4237 | 2025-10-27 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 241.7 |
| a7f74432-1921-3df1-9230-7cab50affb12 | -4.4807 | -43.4005 | 2025-10-27 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 89c1c774-b8c9-3ec1-a4e5-bc1e1667b8cf | -4.4431 | -43.4259 | 2025-10-27 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| fbaf3273-4a79-3fd2-b372-e33f2a7baf5e | -19.0724 | -48.3148 | 2025-10-27 01:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 6d7d7047-3c5c-333e-9309-d97fa97b9f44 | -7.0692 | -46.7541 | 2025-10-27 01:10:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 86917e32-35e8-3a81-85af-9cd6f8265c90 | -4.4479 | -45.4599 | 2025-10-27 01:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 652.0 |
| 4854e6ca-01d0-36d6-9881-baf07ec8bc93 | -4.462 | -43.4016 | 2025-10-27 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| b6143abb-91cc-3fc7-9166-e5002ec54ed5 | -4.4479 | -45.4599 | 2025-10-27 01:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 563.1 |
| cabb4c6d-c6e6-305b-b5eb-85182f08bc43 | -4.3879 | -43.3129 | 2025-10-27 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 91ec7136-62f7-319e-88cf-3c53a866a1a8 | -7.8411 | -46.4646 | 2025-10-27 01:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| b7cc5abb-e371-3e71-a157-b95ea11fbc8e | -7.8408 | -46.487 | 2025-10-27 01:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 8bfe883f-9404-3b0d-88c0-53f93265d3a9 | -7.8596 | -46.4853 | 2025-10-27 01:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 429f17ab-d2c6-376f-8cd2-5897d820c7d3 | -4.4431 | -43.4259 | 2025-10-27 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 169333c0-c860-3ead-9d1a-0b8e0649a3a7 | -4.4804 | -43.447 | 2025-10-27 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| d906c42b-c254-3140-9bcb-708b9dac309b | -10.8213 | -56.9604 | 2025-10-27 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| bef70e12-9c66-3f33-8e24-9df423624c2c | -4.4665 | -45.4589 | 2025-10-27 01:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 225.4 |
| 1b4cbbc5-f7e1-31c9-b71a-fed06040f7cf | -10.8401 | -56.959 | 2025-10-27 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| bf2d1e4c-2666-3350-8cd0-df5234e0d90d | -4.4805 | -43.4237 | 2025-10-27 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 362.4 |
| fab81459-c4e6-38cd-8624-522fae9f7955 | -4.4477 | -45.4824 | 2025-10-27 01:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 1c01de2b-8681-38d9-9420-f48e7c27799a | -12.5258 | -47.5678 | 2025-10-27 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 26e3439a-68a2-3103-8109-7bb71c689c7e | -9.4761 | -40.3862 | 2025-10-27 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.7 |
| e90d2557-17eb-389c-b578-2362e4d28296 | -4.448 | -45.4374 | 2025-10-27 01:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 152.3 |
| 6dae06f4-844c-3d57-a97a-3c7ae5f4cdd5 | -4.462 | -43.4016 | 2025-10-27 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| f33c927c-9772-35a3-bf04-c03ea93b305d | -4.4663 | -45.4814 | 2025-10-27 01:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 49.8 |
| ccade1c8-8d56-3172-860c-cc7ee47431d9 | -7.0692 | -46.7541 | 2025-10-27 01:20:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| baa092c5-b054-330f-b01c-de62feb68e85 | -10.7676 | -44.1905 | 2025-10-27 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 1b3e8ab4-d0ff-3a7a-b266-704f7e9897ad | -4.3877 | -43.3362 | 2025-10-27 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| dde2f861-ddf5-3920-ad4d-ff59bdddfebf | -3.5782 | -44.5297 | 2025-10-27 01:20:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 8c46ffbe-257e-315e-8959-772d5ab079e1 | -4.4807 | -43.4005 | 2025-10-27 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 0159579b-04e2-39ba-b01e-3059983b4a09 | -4.4992 | -43.4226 | 2025-10-27 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 80cf29b2-a2ef-304a-8164-845363d7dd13 | -4.4666 | -45.4363 | 2025-10-27 01:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 43e8e35c-91e6-34ee-9513-2b465dad100c | -4.4617 | -43.4481 | 2025-10-27 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| cc635a4a-0380-351b-9e87-336f56db7c67 | -4.4618 | -43.4248 | 2025-10-27 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 4ed9bbfc-5fb6-304e-b910-e654a9a5af40 | -4.4431 | -43.4259 | 2025-10-27 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |


[Clique aqui para ver as próximas entradas](README10.md)
