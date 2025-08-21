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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66cfa677-de8d-3506-a22a-99c9d33ac21e | -13.0321 | -45.1492 | 2025-08-21 07:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 0848dbc7-e5d7-3aff-90aa-b8624fbc047f | -13.051 | -45.1693 | 2025-08-21 07:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| ab8f4492-143e-3208-8b01-4989f861c202 | -13.0123 | -45.1756 | 2025-08-21 07:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 0b1240be-c3cd-3d8c-863e-3e54d2653b43 | -13.0317 | -45.1724 | 2025-08-21 07:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 228.5 |
| 0c70e40d-7d9b-3a85-ae39-1fde1b8f2f6d | -13.0128 | -45.1523 | 2025-08-21 07:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4b20e8f0-a418-3233-87a5-ef55b424968b | -8.8736 | -62.4115 | 2025-08-21 07:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a50f5d1d-b51a-3a1d-a265-c87aa628ae59 | -8.8737 | -62.3925 | 2025-08-21 07:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 030fc824-e446-3d63-aa65-680b78c18b8b | -13.0312 | -45.1957 | 2025-08-21 07:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| b1a8a626-ab94-3625-ad69-05ce526fbc05 | -7.0354 | -44.6167 | 2025-08-21 07:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| bec8d1b8-50ff-37c8-ba8b-a89db8c31812 | -7.0352 | -44.6396 | 2025-08-21 07:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a4db7c29-fa7f-30e0-8464-6455f216a8a6 | -13.0123 | -45.1756 | 2025-08-21 07:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 5fa27019-1a8e-3274-a1c8-2f6c056b49ba | -13.0321 | -45.1492 | 2025-08-21 07:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 9648a174-d8de-3025-a3d9-42d20c3fb8bf | -7.0166 | -44.6184 | 2025-08-21 07:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| b18831d9-ac04-352e-b0f3-bcc257e73dd9 | -8.8552 | -62.3933 | 2025-08-21 07:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5c98b928-be83-3e46-8c98-ddbb2d1eb769 | -14.8543 | -47.9279 | 2025-08-21 07:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 56.6 |
| ab285881-6dfa-33e1-b66b-951845749dcb | -13.051 | -45.1693 | 2025-08-21 07:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 268fc9eb-d4b8-31b2-8005-ea798f804b4f | -8.8552 | -62.3933 | 2025-08-21 07:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| ee678a8c-3d65-3696-a076-f5981e228da0 | -8.8737 | -62.3925 | 2025-08-21 07:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 12a1609d-d1be-3698-86bd-1cb19b7141d8 | -13.0128 | -45.1523 | 2025-08-21 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| a52dd466-5669-3e46-9a3d-99d375f3cce0 | -13.0312 | -45.1957 | 2025-08-21 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 99808418-5a5b-34bd-b9c5-0b4d158e9032 | -13.0317 | -45.1724 | 2025-08-21 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 205.7 |
| 099fa85f-578a-3360-a521-7b8cb08bc758 | -8.8736 | -62.4115 | 2025-08-21 07:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 562e9a2e-411e-30c2-87f6-b87daef105c2 | -7.0354 | -44.6167 | 2025-08-21 07:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 3994597d-2893-330c-b954-6cf5176bf664 | -13.051 | -45.1693 | 2025-08-21 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 4f0bf669-47d2-3546-8e16-f2f978ba596e | -13.0123 | -45.1756 | 2025-08-21 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.1 |
| e07bdd81-23bd-388d-8cf8-e5f626ac5f40 | -7.0164 | -44.6413 | 2025-08-21 07:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 9f6b081a-9402-38cc-9a8c-265d8959479f | -7.0166 | -44.6184 | 2025-08-21 07:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 139ebb33-bba4-3859-a9fe-61bd48ecb016 | -7.0352 | -44.6396 | 2025-08-21 07:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 9b3db0a8-30b4-3ec0-acfd-a8a1a715ceac | -13.0321 | -45.1492 | 2025-08-21 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 1ffe48e9-afd0-31c4-895d-8c9e06599cdb | -14.8733 | -47.9472 | 2025-08-21 07:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 33ebf647-71c6-362a-be61-f8786ea28fc0 | -7.0166 | -44.6184 | 2025-08-21 07:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 1d82f09b-e7a0-3920-8b5b-c650bc7a514a | -7.0354 | -44.6167 | 2025-08-21 07:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| a98f0e7a-312e-32ec-8c6a-86235397ac6f | -13.051 | -45.1693 | 2025-08-21 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 8e7913f3-2e23-3664-bdbb-b0e9c068c671 | -13.0317 | -45.1724 | 2025-08-21 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 207.4 |
| a819cda8-dc27-3e9d-aea4-cb5d9ac27e01 | -14.8538 | -47.9504 | 2025-08-21 07:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 66655656-60ed-3d20-bc27-b08b4528ded0 | -14.8738 | -47.9246 | 2025-08-21 07:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| dff57aa0-9a71-36ee-8bad-22d96aa65b7e | -8.8552 | -62.3933 | 2025-08-21 07:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 17917f8f-2a67-365c-bb92-1ea6bdf9318b | -14.8543 | -47.9279 | 2025-08-21 07:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| d6c304b9-c392-34ee-a60c-ac931ab9686e | -13.0321 | -45.1492 | 2025-08-21 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 40a3118a-0033-3408-8b3e-9bf7d6dd4b4e | -13.0312 | -45.1957 | 2025-08-21 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| c9f3feed-ce58-3c3d-a5f8-2308f4f18a28 | -13.0123 | -45.1756 | 2025-08-21 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 19a827ab-ced4-3d77-8e2a-eba65be91062 | -8.8736 | -62.4115 | 2025-08-21 07:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| cc6f44f5-3ab1-3ff8-b4d6-0e9590153977 | -13.0128 | -45.1523 | 2025-08-21 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 0cce6071-89ad-3e12-bcb8-6656905321b0 | -8.8737 | -62.3925 | 2025-08-21 07:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e412e973-4d21-306d-89d5-f15fa9b50374 | -7.0352 | -44.6396 | 2025-08-21 07:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f1b38e1e-1a6a-302d-8af3-0a78e2b8a900 | -13.0321 | -45.1492 | 2025-08-21 08:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| cf21dbe3-6e43-34f1-8a88-470ea0998443 | -7.0354 | -44.6167 | 2025-08-21 08:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e2bda643-f215-37f2-9834-ddf8a2b09e7e | -13.0317 | -45.1724 | 2025-08-21 08:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 210.4 |
| 6e639b12-469b-32c7-8aa8-052078a52202 | -7.0164 | -44.6413 | 2025-08-21 08:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| e2ca4161-b336-330c-8dce-de3a12c128d7 | -13.0312 | -45.1957 | 2025-08-21 08:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| c4dc74b6-0e87-3d8f-8e6c-1b5239334d18 | -8.8736 | -62.4115 | 2025-08-21 08:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 9f568f3c-2c17-3f57-b821-c2984084f8ee | -13.0123 | -45.1756 | 2025-08-21 08:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| d26942f3-4737-38e2-a739-68289799a987 | -14.8738 | -47.9246 | 2025-08-21 08:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 97017ae9-4f13-34f6-8640-87e88229cc21 | -13.0128 | -45.1523 | 2025-08-21 08:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 59443fc7-a360-3432-beb4-6d6b0d29c4cd | -14.8538 | -47.9504 | 2025-08-21 08:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 39.2 |
| d1d1f13a-c348-3643-97fb-6363e5902098 | -14.8543 | -47.9279 | 2025-08-21 08:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| c1cf0619-1d31-35a9-aae8-abfab5163252 | -13.051 | -45.1693 | 2025-08-21 08:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 667339ca-6308-3ed6-bf90-c92c98557366 | -7.0166 | -44.6184 | 2025-08-21 08:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 84d08a5b-487f-3308-8493-d6152051236a | -8.8737 | -62.3925 | 2025-08-21 08:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 840b195f-93a0-3be8-b9c5-708164f9039d | -13.0321 | -45.1492 | 2025-08-21 08:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 44b01b77-c197-3a29-95ba-7096e2e2c8df | -13.0317 | -45.1724 | 2025-08-21 08:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 240.1 |
| 7a9af82d-82a9-3622-8bf1-52dab027998f | -8.8736 | -62.4115 | 2025-08-21 08:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 74032367-414e-351a-b889-bcdc7f6ce332 | -13.0128 | -45.1523 | 2025-08-21 08:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 6c909987-d156-3040-937d-9c69a8557dd4 | -8.8737 | -62.3925 | 2025-08-21 08:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3310446f-6d8d-3609-aa36-f81c5be680e8 | -13.0312 | -45.1957 | 2025-08-21 08:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 2fa70412-2a4c-384a-ad22-d34a1454677d | -14.8543 | -47.9279 | 2025-08-21 08:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 47.5 |
| dfcb883f-38e4-3da5-978b-d55aade8dab8 | -7.0164 | -44.6413 | 2025-08-21 08:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| a1c4cc48-2ee1-3eaa-8f2b-ae91febb2fde | -14.8738 | -47.9246 | 2025-08-21 08:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 57c25e75-fcee-3a3b-8c80-d70f61c67181 | -13.051 | -45.1693 | 2025-08-21 08:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 4ef43d54-5b9d-396a-9960-eb6fdec6bb85 | -7.0354 | -44.6167 | 2025-08-21 08:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 36053b9a-2cf8-32ba-9785-c322d78d057d | -13.0123 | -45.1756 | 2025-08-21 08:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 54ab2f96-3f8c-3107-ab06-4b3db45de936 | -7.0166 | -44.6184 | 2025-08-21 08:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| e9549434-03c1-353b-9442-9a24f719bbaf | -13.0123 | -45.1756 | 2025-08-21 08:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 21b4c410-d1a4-3180-8042-8cbefa94900d | -13.0128 | -45.1523 | 2025-08-21 08:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 72dde600-4ca2-3b46-8d38-0c3e8b5d2034 | -13.051 | -45.1693 | 2025-08-21 08:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 865d8825-66fe-3cea-bbdb-8d433430a4b2 | -7.0352 | -44.6396 | 2025-08-21 08:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 5fbb7dc2-3754-3439-87f4-3fddbae7be59 | -14.8538 | -47.9504 | 2025-08-21 08:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 0d3db1c5-a863-31fc-8950-40421c90123c | -13.0317 | -45.1724 | 2025-08-21 08:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 240.2 |
| 40e0a663-708f-3cb1-b8ed-51b9d0549559 | -13.0321 | -45.1492 | 2025-08-21 08:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 5e8e793f-b6aa-3eb1-beb5-515878ec3787 | -14.8543 | -47.9279 | 2025-08-21 08:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 18580f9d-d33f-3933-b016-99d53d3c04ee | -7.0354 | -44.6167 | 2025-08-21 08:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 99cbcd85-75be-348b-905f-e273d3283e3e | -8.8737 | -62.3925 | 2025-08-21 08:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 42.9 |
| f34c7cfd-1493-391e-85dc-812bfca2e4c8 | -13.0312 | -45.1957 | 2025-08-21 08:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 235af5e2-ce99-3049-80a7-cedbf684cc13 | -7.0166 | -44.6184 | 2025-08-21 08:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| fc585ebc-b232-3066-b3e4-30368a60e8c1 | -8.8736 | -62.4115 | 2025-08-21 08:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 5d3a8e06-6cae-3cc5-a176-4aec6abd9131 | -8.8552 | -62.3933 | 2025-08-21 08:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 86ff1e75-6413-36a3-b908-c178f44a9070 | -8.8737 | -62.3925 | 2025-08-21 08:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| f252b2a1-5ce5-3f62-bbba-6e17c1a6d1ab | -13.051 | -45.1693 | 2025-08-21 08:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 77d77815-43f8-34c2-9df1-70d366db013c | -14.8543 | -47.9279 | 2025-08-21 08:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 76d4ca11-eb67-32e4-afee-d1218c1baa8c | -13.0321 | -45.1492 | 2025-08-21 08:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| e8b902a4-0678-352e-8d6a-edc12f637214 | -8.8736 | -62.4115 | 2025-08-21 08:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| a3a7d997-bc44-3deb-9c4a-ceb2c8f7d09d | -13.0317 | -45.1724 | 2025-08-21 08:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 229.2 |
| b27edf23-3b28-3e13-aba2-5e87ad8c6a94 | -13.0128 | -45.1523 | 2025-08-21 08:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 0eb3ddbb-eecd-396e-b545-c85685f7824d | -13.0123 | -45.1756 | 2025-08-21 08:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 1d6231de-16cc-32cf-925e-69834e111d03 | -13.0312 | -45.1957 | 2025-08-21 08:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 6f47e697-2124-3cc7-81d1-b5d047bbe19f | -8.8552 | -62.3933 | 2025-08-21 08:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 37.4 |
| c8f1d664-92e0-3ad2-87dc-1e7829d04a92 | -8.8737 | -62.3925 | 2025-08-21 08:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 165f81cd-4883-37dc-be1d-ee3d11508bd8 | -14.8543 | -47.9279 | 2025-08-21 08:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 19077e3a-950d-3f2c-abef-d980b016f324 | -8.8736 | -62.4115 | 2025-08-21 08:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 5cabd668-2203-306a-8d56-29372628d00e | -8.8736 | -62.4115 | 2025-08-21 08:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |


[Clique aqui para ver as próximas entradas](README60.md)
