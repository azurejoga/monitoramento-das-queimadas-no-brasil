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
| 85a4bcbf-f0b3-3199-8aea-6d3b5813f514 | -23.99891 | -54.12531 | 2024-10-29 05:31:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 0e1fb4d5-a9e3-3459-94e8-d1fc9d8d9c2c | -23.99385 | -54.1171 | 2024-10-29 05:31:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 50202d8f-1f3f-38c0-b575-8e16be1d0d1b | -23.99344 | -54.12223 | 2024-10-29 05:31:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3bfde299-8079-3871-938e-805a702899fc | -23.99274 | -54.12473 | 2024-10-29 05:31:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| be206359-0e55-3f09-b189-34d1a4d8cfeb | -19.50878 | -56.59206 | 2024-10-29 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 72fcd8b4-6d87-34d8-9f6c-6427b800e5fa | -19.50844 | -56.5951 | 2024-10-29 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 2ba96e84-469b-3c0b-adca-3d70f2441cb8 | -2.833 | -49.2413 | 2024-10-29 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 71a12e9e-be38-3857-9687-6f4eae6f4a9d | -2.8331 | -49.22 | 2024-10-29 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| b284c9c8-b381-3bdd-9193-43d5edfbcd29 | -3.1097 | -54.2865 | 2024-10-29 05:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| cc3da89e-b600-3a58-b7f3-4045597acd7a | -3.2503 | -46.8709 | 2024-10-29 05:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| a7b93277-8a38-3167-b3d8-1d2d7509bb92 | -3.9289 | -48.3458 | 2024-10-29 05:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e40a54b7-7c38-38e7-845c-8063b254152b | -6.137 | -42.507 | 2024-10-29 05:35:40 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| 7bd08359-8769-3a6c-931b-a48f788f3260 | -2.833 | -49.2413 | 2024-10-29 05:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 4b67e31d-d109-3fce-967b-1d8d393561c9 | -2.8331 | -49.22 | 2024-10-29 05:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 634f899f-6b97-36da-b58d-8ab2276b686e | -3.1097 | -54.2865 | 2024-10-29 05:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 518a1035-65c9-32e4-b82e-50d5e417cbbd | -3.1794 | -50.3922 | 2024-10-29 05:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 1cdf1e6d-1fdb-3ebd-838b-467caf1e73a1 | -3.4065 | -45.3074 | 2024-10-29 05:45:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 4fc747c7-4c9a-3a4b-90f9-1105c8e23ca4 | -3.4066 | -45.2849 | 2024-10-29 05:45:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| e18b3591-aefa-3a1b-8461-a852b0326d2f | -3.9289 | -48.3458 | 2024-10-29 05:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 1bf2f444-8213-389e-8739-f5f34b2c5cfe | -2.833 | -49.2413 | 2024-10-29 05:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 8e71845b-b190-31a8-971b-4fbcf91d3943 | -3.1097 | -54.2865 | 2024-10-29 05:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| e9c9641e-9f38-38bd-9466-fe7cf0993305 | -3.1794 | -50.3922 | 2024-10-29 05:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 788ff47a-26f4-33cd-920b-e2ebe2eb3d69 | -3.4066 | -45.2849 | 2024-10-29 05:55:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 50.0 |
| aac503a4-1c0c-3aa5-b006-8e213cb0a16f | -1.4211 | -54.2171 | 2024-10-29 06:05:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 7468ffb7-8940-377d-ad4b-c7e8e6a46579 | -1.4394 | -54.2169 | 2024-10-29 06:05:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 7900b84c-79ba-3c00-9b1f-1cb557ab6b30 | -2.833 | -49.2413 | 2024-10-29 06:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 672c9829-b249-38d9-80ac-c4c94bfe0a8e | -3.1794 | -50.3922 | 2024-10-29 06:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 7f02c20c-cf96-3246-9eed-8dca7074d90e | -1.4211 | -54.2171 | 2024-10-29 06:15:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| c1ad24d1-e86e-3e6d-8c36-4117c8b492d0 | -1.4394 | -54.2169 | 2024-10-29 06:15:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ecd44c9c-e0f9-3fd6-b81f-49ffa2543b3a | -2.833 | -49.2413 | 2024-10-29 06:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 86811abd-bf78-374b-927b-6401174bb41a | -3.1097 | -54.2865 | 2024-10-29 06:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| fec550d2-d936-3522-91b9-3a23eb388d97 | -3.1794 | -50.3922 | 2024-10-29 06:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f551631b-ed9e-3dac-be2d-be79203fdf43 | 4.05593 | -61.24677 | 2024-10-29 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 575f0971-a9fe-3a81-89a5-8b5068b503c5 | 4.05647 | -61.257 | 2024-10-29 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7fa4b52-892e-3026-a884-ad55d5aadc42 | 4.05685 | -61.25203 | 2024-10-29 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| faf9c0df-6a85-38b1-8023-09d69dc2dcac | 4.05713 | -61.26093 | 2024-10-29 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53966372-0663-3fd9-85ef-3a9761b7a84b | 4.05762 | -61.25643 | 2024-10-29 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37c7429c-b977-3300-be75-b10b5f48e631 | 4.05486 | -61.24745 | 2024-10-29 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15d7dba5-e7ae-3371-b285-acd81205864d | 4.06445 | -61.2598 | 2024-10-29 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f874bc37-94b1-32ff-8346-4c84e365a7cd | 4.06389 | -61.25665 | 2024-10-29 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4eca824-a557-308f-9167-e6b7c727f4ce | 4.06332 | -61.26075 | 2024-10-29 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a39f8b2c-1b30-354c-995d-f65e0fb40459 | 4.06278 | -61.25753 | 2024-10-29 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e3cf205-808a-397e-8f25-6f3495f6ea0d | 4.05571 | -61.25251 | 2024-10-29 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc6966b4-3043-399c-8dc4-1cafba151e9a | 4.05829 | -61.26021 | 2024-10-29 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6cc74604-9f39-3197-838c-b4a806c275fc | 4.09805 | -61.12876 | 2024-10-29 06:18:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 02269f88-e6db-3f98-80b4-58b77b7a288a | 4.09274 | -61.1344 | 2024-10-29 06:18:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a20f2b8-9b09-30da-9087-1d115012c6f8 | 4.09197 | -61.12987 | 2024-10-29 06:18:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3d22cdc9-56d8-3adc-ad9f-86423d2be6fb | -1.42769 | -60.29014 | 2024-10-29 06:20:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 48eb88bd-19f0-360a-a215-24999c7f9ee2 | -9.60434 | -67.19527 | 2024-10-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18387aea-4e75-3920-8e76-584571881d0c | -9.60396 | -67.19818 | 2024-10-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab79f76c-1486-39a4-9e1f-5eaa14763703 | -10.43077 | -69.75673 | 2024-10-29 06:22:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf79dc9c-38b8-312a-9dcc-453db4e98ce0 | -10.43133 | -69.75268 | 2024-10-29 06:22:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98ebfd89-2884-3074-868a-9ca7b982c038 | -10.4356 | -69.75327 | 2024-10-29 06:22:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa7e211c-76de-3acb-bef7-4ecaa285b93b | -9.60357 | -67.20108 | 2024-10-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3fef7c6-5d48-3d28-a579-ee8fdbbe1f02 | 4.09115 | -61.12685 | 2024-10-29 06:25:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 20e97414-f790-3a9c-a073-8f5c6d51d341 | 4.05488 | -61.25232 | 2024-10-29 06:25:00 | AQUA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 607cb4c7-adb0-3abc-8a5e-9554cda263ea | -3.12932 | -54.27109 | 2024-10-29 06:25:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 8106a111-06b9-3ad0-bead-975bc4d1e8d2 | -3.11531 | -54.26933 | 2024-10-29 06:25:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 2e4e2a87-9cd5-3f63-8004-003c51a1acd3 | -3.08333 | -54.15871 | 2024-10-29 06:25:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| a05090dd-1aed-33d0-8e43-b97f9a2077d6 | -3.07272 | -54.16455 | 2024-10-29 06:25:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 8679a1db-5d97-361a-b421-ac42d16e4ace | -2.86736 | -53.33644 | 2024-10-29 06:25:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| a7367d34-8e33-3256-bcbb-f7eb529c23b9 | -1.43875 | -54.22532 | 2024-10-29 06:25:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 462d497b-2cd6-3e94-aca1-ddae1f72db06 | -1.44221 | -54.20245 | 2024-10-29 06:25:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 32bdf760-299a-3101-bb70-bd3f96d1fed9 | -1.43485 | -54.20858 | 2024-10-29 06:25:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 44bf719b-747c-31f6-9400-932063194144 | -1.43155 | -54.2317 | 2024-10-29 06:25:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 7a8c5cee-d05d-3770-a2c0-26a52f8a2dd2 | -1.42852 | -54.20076 | 2024-10-29 06:25:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 679433c1-af07-3458-bc06-6498bbdcb73f | -1.42502 | -54.22409 | 2024-10-29 06:25:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 175da54f-45fa-32ef-aa17-783075aaae34 | -1.21617 | -55.90104 | 2024-10-29 06:25:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9c9d4f13-6fe9-3d98-8442-855cd7c3175c | -0.76885 | -62.89077 | 2024-10-29 06:25:00 | AQUA_M-M | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| baa19df1-2936-362b-be6b-915183e2fe2a | -1.4211 | -54.2171 | 2024-10-29 06:25:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 17a08076-919a-3132-a7df-d86bbd6e4732 | -1.4394 | -54.2169 | 2024-10-29 06:25:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 58a8b728-b5f8-3cb0-81a2-77221b1e94ba | -1.4394 | -54.2169 | 2024-10-29 06:35:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 050c864b-8edc-315d-9083-3b1ef1216077 | -1.4211 | -54.2171 | 2024-10-29 06:35:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 5f1008d5-eb87-312d-80ac-d676aeb6c78e | -11.1378 | -55.5515 | 2024-10-29 10:46:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 79c4c01c-904d-32c0-974c-bbdb7a8d0423 | -11.138 | -55.5313 | 2024-10-29 10:46:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 858d4619-b212-3c4a-8ab1-3d842911c23b | -11.138 | -55.5313 | 2024-10-29 10:56:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| a2b6cdbb-8ebd-3d00-805b-283e2f54c317 | -11.1378 | -55.5515 | 2024-10-29 10:56:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| eb73dfde-bd7e-37bf-a5ab-c0a1046e1a0f | -11.138 | -55.5313 | 2024-10-29 11:06:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| ffb92f36-07a8-35af-b277-118a85140163 | -11.1378 | -55.5515 | 2024-10-29 11:06:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 8d5948e1-fb87-33eb-a7e2-4af627d9cc3e | -24.0128 | -54.1286 | 2024-10-29 11:07:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 97.2 |
| d6b6c96a-6dcc-3246-ae75-f345559bf42d | -11.1378 | -55.5515 | 2024-10-29 11:16:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 40c8244c-a918-3ceb-b99b-68fcafa6a747 | -11.138 | -55.5313 | 2024-10-29 11:16:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 84d9ab8b-6ca4-3e91-8c3f-a26915d20959 | -11.1378 | -55.5515 | 2024-10-29 11:26:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 192.1 |
| 0e84e2c1-87eb-3ba3-89a3-7991d24e684d | -11.138 | -55.5313 | 2024-10-29 11:26:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 1181e070-2be2-3efb-a6b8-f2468e8d47b6 | -11.1378 | -55.5515 | 2024-10-29 11:36:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 6ae2271a-a1e4-3d90-a615-a6336b9d1f02 | -11.138 | -55.5313 | 2024-10-29 11:36:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 52d2234b-be5d-3db0-aab3-23fa62a79acc | -11.1378 | -55.5515 | 2024-10-29 11:46:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 208.7 |
| 98dd24aa-88db-3284-855d-e5c4833f71ed | -11.138 | -55.5313 | 2024-10-29 11:46:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 192.4 |
| f63574af-4c67-38b1-b233-207ecd57901e | -13.6222 | -45.5838 | 2024-10-29 11:46:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 74b7ce95-a51b-3f30-bf06-995dbfade875 | -11.138 | -55.5313 | 2024-10-29 11:56:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 206.8 |
| f0629653-b384-3202-bf8b-0ca99dda307d | -11.1378 | -55.5515 | 2024-10-29 11:56:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 193.6 |
| ffa35b7f-bd39-3542-b361-70196881f718 | -13.6222 | -45.5838 | 2024-10-29 11:56:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 261.6 |
| eac73c45-de94-3ab1-bda8-b154ef375f60 | -11.138 | -55.5313 | 2024-10-29 12:06:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 250.1 |
| d9b6bcad-051f-3bbe-95aa-751f35e9ab3a | -11.1378 | -55.5515 | 2024-10-29 12:06:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 212.7 |
| e3d63cff-914b-3cb0-9002-2a3d181ec76e | -13.6222 | -45.5838 | 2024-10-29 12:06:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 247.3 |
| d6168cbe-9bb4-38a5-bd42-317c9d373663 | -6.12512 | -47.28227 | 2024-10-29 12:14:00 | TERRA_M-T | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 95cc1495-f4d4-31fa-a1ac-69d822c84023 | -6.12889 | -47.25907 | 2024-10-29 12:14:00 | TERRA_M-T | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 8937e9ea-8c8e-3559-a0ed-06ed0764ca88 | -6.13281 | -47.27732 | 2024-10-29 12:14:00 | TERRA_M-T | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 13f1bcd1-b988-35ab-8bf0-4e83d75bd6fd | -8.48382 | -46.5143 | 2024-10-29 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 95e702a3-3bf9-3f0c-b38e-d0a7b4b8305f | -7.87682 | -45.57348 | 2024-10-29 12:14:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |


[Clique aqui para ver as próximas entradas](README106.md)
