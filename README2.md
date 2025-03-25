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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a37b6a51-a569-3378-baa4-e8b598f9e8d2 | 2.9275 | -60.4265 | 2025-03-25 01:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 0580708b-e26c-3a2c-a91b-aa15b4c223f8 | 2.9275 | -60.4265 | 2025-03-25 01:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 1b988ed4-e653-3a23-8a7b-af025db764e7 | -17.8455 | -39.8705 | 2025-03-25 01:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 96.6 |
| 9949c957-9877-305e-bbfc-cfb504abbd53 | -17.8463 | -39.8443 | 2025-03-25 01:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 96.0 |
| a08b4dba-9e60-3450-afe4-f0b9e4099f5c | -17.8666 | -39.8386 | 2025-03-25 01:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 115.1 |
| 591e0884-f36b-3504-9eb3-d8dc30999a16 | -17.8658 | -39.8648 | 2025-03-25 01:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 173.8 |
| 09990eb0-76a3-3ea3-aa8a-2172fa4447f1 | -17.8861 | -39.8591 | 2025-03-25 01:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 64.8 |
| b3270bc7-c979-3c74-b9a6-6bce343f58a5 | -17.8455 | -39.8705 | 2025-03-25 01:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 112.0 |
| 40474634-65d3-3484-bb0d-3d078b768dc3 | -17.8666 | -39.8386 | 2025-03-25 01:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 167.7 |
| f134db2f-eb08-3841-b6e9-5f39ba70531a | -17.8463 | -39.8443 | 2025-03-25 01:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 130.2 |
| 068298c2-bb66-324e-91bd-912ac6143025 | -17.8658 | -39.8648 | 2025-03-25 01:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 257.7 |
| 62df85f5-a303-31e9-82c0-4ea71e7558b6 | -17.8658 | -39.8648 | 2025-03-25 01:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 216.8 |
| 631b19f7-4813-3caa-b3c9-e450fb7d1166 | -17.8666 | -39.8386 | 2025-03-25 01:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 171.1 |
| 7b7f5a30-fca2-38a7-a7ef-8fe348059702 | -17.8861 | -39.8591 | 2025-03-25 01:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 84.8 |
| 81c1004e-1738-3550-a125-bd0a92ed650b | -17.8463 | -39.8443 | 2025-03-25 01:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 111.9 |
| 2fb1ab42-3282-37dc-bbea-ca005651271f | -17.5613 | -40.6441 | 2025-03-25 01:50:00 | GOES-16 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.8 |
| e7a74352-73f1-30f2-afd3-25b1d5fc9b9c | -17.8455 | -39.8705 | 2025-03-25 01:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 106.0 |
| 142b6fab-d590-332d-bd82-f5fe3fed07cd | 2.9092 | -60.4458 | 2025-03-25 01:50:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 473c5d6e-5e70-3b0d-aa0c-ee1d3d66d97d | -17.8666 | -39.8386 | 2025-03-25 02:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 93.4 |
| 178e55f4-c795-3f2d-998f-d3d6f7e7767a | -17.8861 | -39.8591 | 2025-03-25 02:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 76.7 |
| e347413f-ef7f-3e75-8202-e228958dbff6 | -17.8455 | -39.8705 | 2025-03-25 02:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 83.3 |
| f9cae9e5-b0b7-3c3f-9342-d3d21800b352 | -17.8658 | -39.8648 | 2025-03-25 02:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 173.8 |
| 4df40b38-43dd-3a8c-aabb-cdcdb41990f4 | -17.8455 | -39.8705 | 2025-03-25 02:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 124.8 |
| 15d18462-af08-3ea2-86a9-653455c923a6 | -17.8861 | -39.8591 | 2025-03-25 02:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 101.9 |
| 7572c7c2-b7b1-3ab7-bfcc-dbfac60ebb09 | -17.8658 | -39.8648 | 2025-03-25 02:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 291.6 |
| c7aeb894-5be7-3acd-a1b9-47b6c276d761 | -17.8463 | -39.8443 | 2025-03-25 02:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 125.3 |
| ac407f45-9169-3279-bf0b-a7792875a8d8 | -17.8666 | -39.8386 | 2025-03-25 02:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 166.1 |
| 89bf31d7-82e6-36e8-bcc9-5b4d9befa3ee | -17.8666 | -39.8386 | 2025-03-25 02:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 186.7 |
| d0447712-c073-3952-8e5a-7804aeb3b94b | -17.8861 | -39.8591 | 2025-03-25 02:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 118.6 |
| cf89ed3b-5a8b-3126-9b24-5a4be276e62a | -17.8455 | -39.8705 | 2025-03-25 02:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 116.0 |
| 46d94744-48de-3e0f-9048-43d10da5c72b | -17.8463 | -39.8443 | 2025-03-25 02:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 95.6 |
| f09770b1-14de-3fe8-ace3-3ef2f91dc228 | 4.6634 | -60.9225 | 2025-03-25 02:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 7ba42341-d5c1-30e8-8816-9c508667b72a | -17.8658 | -39.8648 | 2025-03-25 02:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 300.9 |
| ce073297-da6c-3ed0-9435-b0857c1a596e | -17.8861 | -39.8591 | 2025-03-25 02:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 136.0 |
| 63b1b254-2267-3df2-aff4-000234f23d3e | -17.8658 | -39.8648 | 2025-03-25 02:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 419.1 |
| 91be6920-8f84-3485-8657-83b5b8ea8cdb | -17.8666 | -39.8386 | 2025-03-25 02:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 176.2 |
| 0bec0acb-7809-3d69-9d8d-053a310c00d3 | -17.865 | -39.891 | 2025-03-25 02:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 108.8 |
| be2c83a6-48a3-31d6-bbf7-5d10124f917b | -17.8463 | -39.8443 | 2025-03-25 02:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 93.3 |
| 3b2fb2d2-4345-33ed-830b-66c9ec3a5530 | -17.8455 | -39.8705 | 2025-03-25 02:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 134.0 |
| 65884736-628d-3945-91de-27305cffd653 | -17.8455 | -39.8705 | 2025-03-25 02:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 118.0 |
| e6732d02-d78e-3849-9521-05b067a48260 | -17.865 | -39.891 | 2025-03-25 02:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 107.0 |
| 1cee2671-6ce4-3f25-915e-0773d4a5024d | -17.8463 | -39.8443 | 2025-03-25 02:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 95.9 |
| 9a0e7929-7c59-394e-8a0b-843c54aa02dd | -17.8658 | -39.8648 | 2025-03-25 02:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 389.4 |
| 9706e080-399c-360e-aa1a-3083f46e8e8f | -17.8666 | -39.8386 | 2025-03-25 02:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 161.3 |
| 9137dfdb-a22a-33ab-936e-f6fe7a235b07 | -17.8861 | -39.8591 | 2025-03-25 02:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 201.6 |
| 721a6d6b-5433-3a84-afaa-690701d18446 | -7.06594 | -35.05412 | 2025-03-25 02:49:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 52c1abe2-88e8-3683-8883-805644345d0b | -7.07042 | -35.05791 | 2025-03-25 02:49:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 03173254-5894-3482-a6e9-b4fc56bb70d3 | -7.07243 | -35.05579 | 2025-03-25 02:49:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9b74a337-da3b-3c6c-9dba-780fd6c138c2 | -7.07148 | -35.05234 | 2025-03-25 02:49:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 53d332a6-e4ba-398e-850e-6550aae30ca9 | -7.0714 | -35.06137 | 2025-03-25 02:49:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 16903e04-2dd8-3a9d-a084-e8fc475a8801 | -17.8861 | -39.8591 | 2025-03-25 02:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 99.0 |
| 64747c2f-db46-3eb6-b5f0-c7c43faa27ef | -17.8658 | -39.8648 | 2025-03-25 02:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 403.8 |
| 8468271d-e4a8-3acf-b2b6-95099c7ba110 | -17.8666 | -39.8386 | 2025-03-25 02:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 179.7 |
| f143ef93-9f61-3c35-bf6f-2eaaa6ce7d04 | -17.8455 | -39.8705 | 2025-03-25 02:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 111.3 |
| 18703c5a-5582-3af1-aa2a-eaf688a80f3d | -17.8463 | -39.8443 | 2025-03-25 02:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 98.5 |
| bc48a56d-9a32-32ca-89a4-e14f601acd9a | -17.865 | -39.891 | 2025-03-25 02:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 121.5 |
| eb857c69-cb5a-371a-8002-412fcc8b46a1 | -17.86457 | -39.87315 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.4 |
| cb11e08d-6209-3298-b0e9-91c36ab8839a | -17.84834 | -39.86757 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| cc9a7ef3-859f-33ea-be61-b15ac89a9882 | -17.86428 | -39.86393 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 57.6 |
| 7581063c-4d5d-39f5-8630-0f16b6eefdfb | -17.8501 | -39.86013 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| e32660f5-506c-3202-aeda-8aaa21f12ce7 | -17.85545 | -39.86937 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 57.6 |
| 10ee4bcf-da8f-3370-aa08-ae46cbde7dd4 | -17.854 | -39.8545 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 27.8 |
| 262f2260-d9c4-3ee1-8bdc-12018ca5d7fe | -17.8572 | -39.862 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 57.6 |
| 4c22e02d-783d-3814-aff8-e56e55d76bf4 | -17.86602 | -39.85657 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 40.7 |
| d2543ce8-be67-33ed-9abb-a1d013aece6e | -17.86274 | -39.88067 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.4 |
| 11036f69-ee58-3421-90bb-a745c373cc3b | -17.85892 | -39.88659 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 75a12610-0d7a-3caa-8493-1daa05649fcd | -17.86111 | -39.85629 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 56.9 |
| 74245786-b9bc-34aa-8c06-543df8bb9f21 | -17.84686 | -39.85283 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 27.8 |
| d9a60577-7faf-3485-a1c6-edcd9e1e28b6 | -17.86636 | -39.86576 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 56.9 |
| b8142f3e-632d-3ac5-8c3d-2754f8a9b460 | -17.86254 | -39.87131 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 57.6 |
| 825092a7-012c-3590-9779-b4f192efd6fb | -17.86814 | -39.85845 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 56.9 |
| e4914ca6-46ef-3b3f-a88f-2a683bf52475 | -17.85751 | -39.87112 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.4 |
| cfdd0566-7a63-3445-bac3-a137edb1e6a2 | -17.85929 | -39.86377 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 56.9 |
| 18d5f7df-5b3e-3382-8570-6cf9c260f25e | -17.85219 | -39.86194 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 27.8 |
| f283da5f-9577-346c-b6ae-6733e54e0659 | -17.86075 | -39.87886 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0c99380c-b762-370d-a53b-6b4959b9f4fb | -17.85186 | -39.85273 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 45.3 |
| fe2bb56c-daa7-3022-a917-4f35ec4eed9f | -17.85897 | -39.85452 | 2025-03-25 02:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 40.7 |
| ed98c605-df56-3317-8653-78162c886705 | -17.865 | -39.891 | 2025-03-25 03:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 94.3 |
| dd669cdf-b350-3896-ba4a-a79a7e1216d1 | -17.8463 | -39.8443 | 2025-03-25 03:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 104.7 |
| 87d93ab3-5f4a-34d8-8c89-25cd4a594cbd | -17.8455 | -39.8705 | 2025-03-25 03:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 101.8 |
| 8d46597d-0ed8-30ea-8fed-56aed6fea624 | -17.8666 | -39.8386 | 2025-03-25 03:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 145.7 |
| 2f972cbf-d4ea-3584-8bc8-3f03f6d006f8 | -17.8658 | -39.8648 | 2025-03-25 03:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 392.9 |
| dd7cd36c-dbc7-35bb-9f83-9d0b4c939d16 | -17.8861 | -39.8591 | 2025-03-25 03:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 134.3 |
| 5b300228-abe8-3458-b03f-8d43a40dc67e | -17.8658 | -39.8648 | 2025-03-25 03:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 354.3 |
| 7f882567-c4cf-3c98-b83c-98a5f31bf5cc | -17.8666 | -39.8386 | 2025-03-25 03:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 149.0 |
| a7c85dd5-d90a-34d2-b9a9-48ceec50d66c | -17.8455 | -39.8705 | 2025-03-25 03:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 102.1 |
| 32339ad8-6969-3865-aa52-d97363815fda | -17.8463 | -39.8443 | 2025-03-25 03:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 92.1 |
| 3dd2cfe0-c574-3639-8e03-aae5cb0e08f9 | -17.8455 | -39.8705 | 2025-03-25 03:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 95.7 |
| 006dcd7a-bac6-3fbe-a751-f7357e0db4ba | -17.8658 | -39.8648 | 2025-03-25 03:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 307.2 |
| a464829c-944e-31ed-9e46-4893135fce4a | -17.8463 | -39.8443 | 2025-03-25 03:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| deebf896-776f-32d3-be97-4f82cc96367f | -17.8666 | -39.8386 | 2025-03-25 03:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 153.6 |
| 528854df-7144-3553-9a2d-8099c78dba99 | -17.8658 | -39.8648 | 2025-03-25 03:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 292.6 |
| 69dec7d1-c17d-355d-b578-8d7ebfe2598a | -17.8666 | -39.8386 | 2025-03-25 03:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 118.6 |
| 5bc40daf-d157-3e55-978f-ef3143d3a43e | -17.8455 | -39.8705 | 2025-03-25 03:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 86.4 |
| 8235b938-c159-3896-b4c1-46fb6ab0c0aa | -17.8463 | -39.8443 | 2025-03-25 03:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 89.9 |
| 8fada86c-2a98-3085-976e-45c297e9981b | -17.8455 | -39.8705 | 2025-03-25 03:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 87.3 |
| 99002aa0-c3be-3f5e-a4dc-6665cfcf4245 | -17.8463 | -39.8443 | 2025-03-25 03:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 85.4 |
| bc68e0b2-838b-30a1-b7a6-04b62d978f20 | -17.8666 | -39.8386 | 2025-03-25 03:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 116.9 |
| e6f43ba5-87b2-3870-a9a4-ab6526d0dea2 | -17.8658 | -39.8648 | 2025-03-25 03:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 231.8 |
| 276edd76-aacd-3de4-873c-5855bacf356c | -7.23134 | -44.77145 | 2025-03-25 03:42:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
