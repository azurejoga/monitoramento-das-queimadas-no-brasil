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
| d43a569e-6650-362e-a9b0-dfe6e472e7ca | -7.81068 | -72.94849 | 2025-01-15 06:05:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cea815b-aa3d-37ca-a9d5-bc16b9169d82 | 2.1038 | -61.8354 | 2025-01-15 06:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 1c959e3d-b7ad-326f-90c6-6543d0f43cab | 2.5247 | -61.0009 | 2025-01-15 06:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 1564087a-6ac9-3ea4-b36b-dd24904c29ef | 2.5247 | -60.982 | 2025-01-15 06:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f675b0ea-3c41-3259-868f-117dcc88d57c | 2.1039 | -61.8166 | 2025-01-15 06:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 90bd11ee-5d03-38ae-8ebd-1194798a7c05 | 2.1038 | -61.8354 | 2025-01-15 06:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 062e1531-5aca-369c-ae32-476bdeae39c7 | 2.1039 | -61.8166 | 2025-01-15 06:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 82cc5c0a-4e77-301a-869b-ca8e99b18124 | 2.1038 | -61.8354 | 2025-01-15 06:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 47.3 |
| b2f7a37b-e9c9-342a-836a-5c50dacd1153 | 2.1038 | -61.8354 | 2025-01-15 06:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 46.8 |
| a8d4e0e8-84e6-3b3a-bc1c-bad531790f62 | 2.1039 | -61.8166 | 2025-01-15 06:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 63.3 |
| dbf2f7af-ddc7-3453-b53c-b5411cd9bf62 | 2.2889 | -60.2076 | 2025-01-15 07:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 97257f42-42ee-382b-8b90-b7749e24ab98 | 2.1039 | -61.8166 | 2025-01-15 07:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| fc071924-9750-3632-aab6-a74e16742b8c | 2.1039 | -61.8166 | 2025-01-15 07:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 1e418738-0199-3068-9117-e317b96945e0 | 2.10703 | -61.79309 | 2025-01-15 07:13:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 45.2 |
| d54ac5b7-99eb-3825-9517-bfdee7673b8e | 2.11245 | -61.82919 | 2025-01-15 07:13:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 4993bee6-60bf-3875-ad2c-b0ab8e7dd415 | 2.11869 | -61.82419 | 2025-01-15 07:13:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 31.3 |
| fdf4ddbe-44b7-379a-ac27-8d2697d3851d | 2.10201 | -61.8261 | 2025-01-15 07:13:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 8e51d880-37d3-3d36-a7fa-46c4fd46bfad | 2.1039 | -61.8166 | 2025-01-15 07:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 5732eb35-8506-3805-a41d-2da8b01c17ad | 2.1039 | -61.8166 | 2025-01-15 07:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| a4063d9e-418c-3775-85cd-3df489f49d0f | 2.1039 | -61.8166 | 2025-01-15 07:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 4447339f-7ab1-3629-aed3-3a319ccb68f2 | 2.1039 | -61.8166 | 2025-01-15 07:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b8ea7e7a-294c-3c81-b84a-991c76ab63ac | 2.1039 | -61.8166 | 2025-01-15 08:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 18039f4c-18da-3420-a75a-44d8ed603354 | 1.3217 | -60.4452 | 2025-01-15 08:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d08acd9c-36ec-3963-b890-f03f7754fa4b | 1.3217 | -60.4262 | 2025-01-15 08:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.0 |
| a9839032-8d56-381a-8307-198e3f865eb9 | 2.1039 | -61.8166 | 2025-01-15 08:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 2a58e566-248c-3975-98ea-6bbb79f2f264 | 1.3217 | -60.4262 | 2025-01-15 08:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 6d169684-cb4c-3bf0-b7de-cdad46530d30 | 2.1039 | -61.8166 | 2025-01-15 08:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 3c3a266c-b28a-3d98-a61f-78b5320006f6 | 1.3217 | -60.4452 | 2025-01-15 08:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 1260973d-7942-3b4b-8041-067de2ac5835 | 2.1039 | -61.8166 | 2025-01-15 08:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 4cdc6423-02fc-3ecf-a538-67c1d8af0747 | 2.1039 | -61.8166 | 2025-01-15 09:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 07b12976-458e-315c-a705-74e75d94e6ee | -6.55809 | -35.26444 | 2025-01-15 11:42:00 | TERRA_M-M | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 11.8 |
| f2b73003-96d5-3225-9947-71734cbe7833 | -6.55654 | -35.27485 | 2025-01-15 11:42:00 | TERRA_M-M | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 2dc4217c-a285-3b87-ba86-5f41f8133e64 | 2.1039 | -61.8166 | 2025-01-15 14:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 1eb75cbf-9d44-31c6-9723-546364dd794f | 3.0375 | -60.2536 | 2025-01-15 14:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 73.0 |
| e8d3a2f7-4243-3466-823f-d1abf5803f8f | 3.0376 | -60.2346 | 2025-01-15 14:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 0dfef6ef-eb61-3d8a-a2c0-1779d89c37ac | 1.3217 | -60.4262 | 2025-01-15 14:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 9083119b-1581-304e-9b53-f14a46e6b337 | 3.0375 | -60.2536 | 2025-01-15 14:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 76be7f6f-40f9-3ef2-b98f-3feca5bd6f8f | 2.2889 | -60.2076 | 2025-01-15 14:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 88.9 |
| f371a854-00ef-34ba-ab70-a3e8c4b57154 | 2.1039 | -61.8166 | 2025-01-15 14:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 2bec58b2-c504-3d69-8319-3da2f20885bc | 2.2889 | -60.2076 | 2025-01-15 14:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 79.7 |
| fec66737-02d1-3c78-baa2-1c43c6158c1c | 2.1039 | -61.8166 | 2025-01-15 14:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 86.7 |
| e6418b63-004e-36fd-bb4e-18c62acfafaa | 3.0375 | -60.2536 | 2025-01-15 14:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 25e2ac65-0655-343d-be4c-53af02894335 | 2.1038 | -61.8354 | 2025-01-15 14:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 954a675f-f28a-3a64-957b-aed828ad483e | 2.1038 | -61.8354 | 2025-01-15 14:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 1b3d0ffb-580d-3527-9932-60277faad2d0 | 1.3217 | -60.4262 | 2025-01-15 14:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 44508c2c-cc6e-3260-becc-c05d09725650 | 3.0376 | -60.2346 | 2025-01-15 14:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 75.9 |
| d17be3d1-4113-3842-a4c2-e6b52694ec9f | 2.2889 | -60.2267 | 2025-01-15 14:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 65f1558b-0d04-3bfa-9d51-b46b32c16326 | 2.2889 | -60.2076 | 2025-01-15 14:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 84.2 |
| f8bff887-b9c5-3750-aa51-0b3e6f5ff5d2 | 2.1039 | -61.8166 | 2025-01-15 14:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 83.4 |
| d9eae224-8b7d-334e-9d81-984b80ad1c4c | 3.0375 | -60.2536 | 2025-01-15 14:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 120.9 |


