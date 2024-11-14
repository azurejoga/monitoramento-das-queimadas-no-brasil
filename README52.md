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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa3ba513-0a07-3d7f-9da7-15d4f573cdd7 | 1.05869 | -60.60759 | 2024-11-14 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9bf58d0-813a-3794-a65e-1ec17f1e8531 | -0.41083 | -51.58128 | 2024-11-14 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cd5625d-9092-3f1c-8f97-37a9b8e642e6 | -1.39575 | -51.13131 | 2024-11-14 05:27:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be2f5272-e8c8-3854-b1e2-23727d98421f | 1.05708 | -60.59732 | 2024-11-14 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 099d1667-2078-3436-868d-28732864bd44 | -2.88025 | -51.7911 | 2024-11-14 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5f87620-2b1c-361f-97f8-c60e084fbd25 | -1.57069 | -52.02523 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0133370f-662a-3b8c-b1c3-d56c80dfa7e6 | 1.05324 | -60.5944 | 2024-11-14 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dac034fe-e478-3b97-835d-2353716b8329 | -3.74112 | -50.44346 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6725d19-2187-3832-aeba-cd75c59c8d0a | -3.08884 | -50.48964 | 2024-11-14 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b75df011-72c8-33d6-a92f-45851e50474e | -1.22692 | -51.7869 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3127505-c602-3f7c-970a-143d4b8ffeab | -0.19646 | -51.50871 | 2024-11-14 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 707a60c6-4d78-3164-889c-1e836c97ad5a | -1.40135 | -51.13221 | 2024-11-14 05:27:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 881ffa54-44d6-335b-bd6e-9472dfca673f | -1.35785 | -53.08259 | 2024-11-14 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1ef65534-e0a8-3afc-9015-c8086e13bb3e | -1.22144 | -51.75154 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53b2bba9-6fe4-34cb-89e0-73860cd27ab7 | -3.74046 | -50.44805 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 179f69e6-177a-38d8-b480-82de63a4643c | -2.90011 | -54.60653 | 2024-11-14 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e63887d-2881-3c4b-be5e-b66814a6c3c2 | -2.80064 | -51.50177 | 2024-11-14 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f22e1daa-9d4e-3e72-b8c6-814f74394d88 | 0.3279 | -50.96912 | 2024-11-14 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b865294-1835-30eb-933a-6dfb6ef35e07 | -3.0947 | -54.30867 | 2024-11-14 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 31e242f1-13b2-3037-b0d5-a22c440f47ff | -1.21189 | -51.77776 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2865ad4b-8433-3625-9d53-6cc23f9f8c77 | -2.8742 | -51.7939 | 2024-11-14 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cfe1f78-9152-3556-95eb-8fe9f2d54a14 | 1.06145 | -60.60366 | 2024-11-14 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6507e5c-ef12-36d6-aaff-1c9b0e2daa9e | -2.35514 | -51.984 | 2024-11-14 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9fceb8f-a438-304a-83fb-4015607685d6 | -3.43414 | -50.31229 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29143d3d-33c2-3be5-88db-ff42a12f71c5 | 0.90761 | -50.14256 | 2024-11-14 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc20c79d-8fb0-36b7-ac49-c4cc14df80c9 | -1.79434 | -52.17957 | 2024-11-14 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a60739ab-680e-3c99-bb6b-e2f15e5300a5 | -1.41821 | -53.48112 | 2024-11-14 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f888a6a7-136b-3acb-b442-d50b338b3bc3 | -1.55904 | -51.86275 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d922aebd-e33c-3b05-a9d1-10cceb1f2de3 | 1.05654 | -60.59389 | 2024-11-14 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03cca56a-4134-3cee-86b3-977dcd30ed7b | -3.43481 | -50.30765 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d45b087-47d6-3fc4-a582-9cf1d4c97056 | -1.80159 | -52.16745 | 2024-11-14 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5753dc32-7a0c-335b-ac86-92797b2d0484 | 1.05378 | -60.59783 | 2024-11-14 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f61ec55b-668d-3e6a-869a-2bd2d2a65406 | -2.77692 | -50.30802 | 2024-11-14 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 020db733-8214-341a-a5c7-181b9061ec8d | -2.12168 | -50.69402 | 2024-11-14 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ec6acbf-4539-348d-a372-9a439c0c150c | -2.11462 | -50.70124 | 2024-11-14 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ccd98ae-c36f-3a02-90fc-d34187c51830 | -2.88022 | -51.79546 | 2024-11-14 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc350698-5bbe-358b-9c92-c016d20bd786 | -2.83972 | -56.79316 | 2024-11-14 05:27:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a6b0d96d-cdc9-3928-9139-5653a95542dd | -3.47961 | -50.25724 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 217feb5e-eb94-338f-b052-981dfc0a1f8e | -0.19216 | -51.50109 | 2024-11-14 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c82e4266-4d93-3e27-9b40-78cda9f4beee | -1.22733 | -51.74898 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc20cee5-4348-3fa0-b0c6-76d7c8769561 | -1.13494 | -51.6871 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50aa154b-8cdc-3095-8795-005386a6ae47 | -1.84674 | -53.69097 | 2024-11-14 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccc0999c-2d17-32dc-a3e8-c765c1b2dd34 | -3.49997 | -50.8442 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e38a3b1-0749-3b6c-9820-b1bca7b47745 | -1.13441 | -51.69052 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 144f919d-fc0c-3f21-8bcb-d7bf211737ba | -1.63634 | -53.2746 | 2024-11-14 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 3800a7b3-f6b0-3663-9f3d-be78dc440c0c | -0.19162 | -51.50449 | 2024-11-14 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdcd93b8-7ef7-3d07-9d7e-bfd26ef6d197 | -3.42803 | -50.31145 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b26c520-0ce6-30a3-ac60-d7a323f0f9a7 | -0.20775 | -51.50695 | 2024-11-14 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5599c4b6-c941-349b-a83a-a99438ff6042 | -1.21607 | -51.75071 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0eb0c99-45f7-330c-bf02-59a9b62154d2 | -2.74761 | -51.62606 | 2024-11-14 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f19dce7e-afe5-33e3-9dcf-3cd77d70d6b5 | -1.7996 | -52.18037 | 2024-11-14 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5717844e-623c-3f44-9fe1-a27956407f2e | -1.41887 | -53.47631 | 2024-11-14 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 881398ca-808e-3f87-973b-a8a01c5e589a | -2.87969 | -51.79909 | 2024-11-14 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be8cd446-1f8a-30a8-83be-ac80456ec9b2 | -3.49474 | -50.8388 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2988f5b7-0d0c-32d7-a8ab-52eea3fdd5cf | -1.80586 | -52.17472 | 2024-11-14 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4439ec22-8dd6-35fc-897c-42752aa0b635 | -2.11523 | -50.69722 | 2024-11-14 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ac2a570-7262-3883-a345-de62210ed962 | 0.65931 | -51.78503 | 2024-11-14 05:27:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20b77de1-8d28-36d7-b1b8-4476c10cbc7f | -2.15416 | -50.71583 | 2024-11-14 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c04d8c0-473b-3d60-87cb-9b3108133900 | 0.65881 | -51.78185 | 2024-11-14 05:27:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56563ad5-d7f3-3caa-a588-d984e71f7292 | -1.22156 | -51.7861 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e901efe-0942-3554-8adb-ab80b7f17d27 | -1.2162 | -51.78532 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8275344-7222-36ad-a7f4-1cb9a64fa32a | 1.06091 | -60.60023 | 2024-11-14 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 580b52cb-b7c7-3563-ab1d-ccdb6f1cc8a7 | -1.55368 | -51.86197 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 64eade3b-2627-3fc8-8a72-c37cff1f4311 | -0.18572 | -51.50704 | 2024-11-14 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ad4aec77-d6c4-30e6-ad8f-3abfe2465cd4 | -3.08819 | -50.49405 | 2024-11-14 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d0474c9-1168-3351-8d43-7c7365b07072 | -3.49409 | -50.84317 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce1150a6-ddd9-30dd-a2ea-580acacf09bb | -2.08735 | -47.73459 | 2024-11-14 05:27:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84b8f9c3-d63a-3364-9a18-44a267310fed | -2.77824 | -50.299 | 2024-11-14 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c5ebcf7-7ec4-3efb-8474-1dd3f74c47e7 | -3.73501 | -50.44284 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a824d74-e127-3742-9459-b0000d5cfa1c | -0.20829 | -51.50356 | 2024-11-14 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 077cfbaf-f8ab-3c45-a40f-84a85110ba6d | -2.74816 | -51.6224 | 2024-11-14 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b178bf8-baf3-3851-ade7-f38e1bb2fb02 | -2.87474 | -51.79458 | 2024-11-14 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fbb3609-5639-30f5-a4bf-ab549c69a30b | 0.44751 | -50.93863 | 2024-11-14 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f81f35ec-5ca6-34f3-b1c5-368a1accac48 | -0.10149 | -51.49848 | 2024-11-14 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee96eea0-2cbf-3200-8111-976c776f65ef | 1.05485 | -60.60468 | 2024-11-14 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fac197aa-5db1-3435-b27b-53747193e980 | 0.85245 | -50.20802 | 2024-11-14 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e0e0b9f-cc67-30ea-93e4-71bc36b39e07 | 2.62261 | -60.41518 | 2024-11-14 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a6dad37-6e93-33e3-ad61-f04d4c74a5f6 | 2.2647 | -55.92449 | 2024-11-14 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cec2d34-9217-388d-9304-a8e34f20ff1a | -3.49346 | -50.84749 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 987a9236-f2fa-3748-8feb-91ca3eb6e65d | -3.48572 | -50.25822 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6102a7dd-4b17-3d88-8266-a6b6693d7a6c | 0.318 | -50.97574 | 2024-11-14 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4bea306f-e68a-33fa-b4ba-22525fef22f5 | -2.83581 | -56.79257 | 2024-11-14 05:27:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b104f8b2-5b9e-3fa1-88fa-cb328d91030b | -1.39129 | -51.1229 | 2024-11-14 05:27:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 066c5ba2-6112-3e57-998a-1b146e387154 | -2.08634 | -47.74115 | 2024-11-14 05:27:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 932f6ef0-4b0d-32f8-9c2b-091bd2335962 | -3.74524 | -50.45782 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bb09745-506d-35ca-ab51-6a60397a769d | -1.55956 | -51.85941 | 2024-11-14 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6836a6e3-4dec-3c4c-9970-32ab438598be | -3.46597 | -50.30764 | 2024-11-14 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7842fefc-9874-3b5e-956d-f5a90073e6dd | 1.06038 | -60.5968 | 2024-11-14 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 053ea10c-9478-3f14-954b-28e660ebe8cf | -2.89015 | -51.69011 | 2024-11-14 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d5f58b9-9499-3c48-9f77-8e97799e755a | 0.31745 | -50.97444 | 2024-11-14 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88a3ac62-b96b-366f-b18d-ca0e6da0a1f0 | -1.39071 | -51.1267 | 2024-11-14 05:27:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07a37ea1-6447-3b60-be73-467ca3f0fe2e | -1.8001 | -52.17714 | 2024-11-14 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65018dc3-ca82-34a9-8bd8-06be2e8a71e9 | 1.05761 | -60.60074 | 2024-11-14 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d7246f0-6598-3546-ac32-2c9176e61cd5 | -2.34926 | -51.9865 | 2024-11-14 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3465fe2-6301-324f-8674-e6869943f4a5 | -2.88077 | -51.79176 | 2024-11-14 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7540aaee-2809-3eac-89a6-6e7734ca0be9 | -2.77758 | -50.3035 | 2024-11-14 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adaf7de0-0b84-37ca-814f-bbb69541cb2a | -0.1729 | -51.55344 | 2024-11-14 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 928c81dc-5109-3548-8504-bd68f057e1d1 | -2.87968 | -51.7948 | 2024-11-14 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20be8592-f53d-3021-a628-d22a6acad67b | -1.39633 | -51.12753 | 2024-11-14 05:27:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e21c44a5-4840-383c-8f4b-59275b914d6f | 2.61931 | -60.4157 | 2024-11-14 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README53.md)
