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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e437c377-e581-305c-a067-0700f44faec7 | -14.7393 | -45.1082 | 2025-06-06 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 1954965d-ca1b-3ddd-8912-ee8b0baf45fc | -12.5425 | -58.3561 | 2025-06-06 13:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 25c8daeb-efb5-3fc9-85eb-9b7e0bdade75 | -14.7398 | -45.0848 | 2025-06-06 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 39ea5981-c75c-34f8-837d-cf54c428937c | -8.6097 | -51.5731 | 2025-06-06 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 017bffaa-53ea-33a7-b375-e8241a638b97 | -11.3716 | -56.558 | 2025-06-06 13:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 6c72dd8a-6dc0-3b45-ba64-b403c31fcb54 | -12.3518 | -52.4722 | 2025-06-06 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| e8dc87eb-9c33-33ca-a117-7d0a33ace17d | -14.7393 | -45.1082 | 2025-06-06 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| c75a84f3-02ee-3f89-a9fa-c20e0660384f | -14.0328 | -55.13 | 2025-06-06 13:50:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| d692252e-38bf-315e-b3c2-3455b372ed89 | -9.5539 | -47.9769 | 2025-06-06 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| f23e5664-5da1-3eab-a979-ee2989f8ee4a | -8.0014 | -50.7186 | 2025-06-06 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 76d9f187-e13a-3f02-948b-696d58b8a6d2 | -12.3376 | -46.2891 | 2025-06-06 13:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| b45d245b-bfd1-326f-9109-bb2bf24b0c67 | -12.5236 | -58.3576 | 2025-06-06 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| d94d4f18-5296-3905-889f-76d45afca8fd | -6.2228 | -43.3226 | 2025-06-06 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 2c424c45-abd2-3363-9768-0872eecd6b49 | -12.3325 | -52.4953 | 2025-06-06 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 9e120789-98e5-34f1-a37e-275fa898a64c | -8.6097 | -51.5731 | 2025-06-06 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 4a625735-d7ab-3f50-8e74-2e6eb5708ad9 | -11.3716 | -56.558 | 2025-06-06 14:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| c42d3934-2a39-3927-b6c6-17a343518d78 | -6.9424 | -42.8126 | 2025-06-06 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 75030f17-d325-3fd2-9a2d-13eecee6cf3b | -14.7398 | -45.0848 | 2025-06-06 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 3a520252-28da-34ff-ab44-43267503c391 | -12.5236 | -58.3576 | 2025-06-06 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 496055d7-c0bb-33aa-9811-36af1a00f524 | -6.2228 | -43.3226 | 2025-06-06 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| afb2aff1-e280-33b5-9b5b-99438e2c5843 | -12.3518 | -52.4722 | 2025-06-06 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 44aa5181-6aa7-3282-bcff-e0904824d80b | -14.0328 | -55.13 | 2025-06-06 14:00:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 3272592a-89f9-3bd2-8e3e-1458237e3687 | -14.7393 | -45.1082 | 2025-06-06 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| c841b559-6ef8-3f12-9988-0761a4eadf97 | -12.3376 | -46.2891 | 2025-06-06 14:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| df62aaad-8304-3aa9-baf6-903a647739e6 | -8.0014 | -50.7186 | 2025-06-06 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| ccaf41aa-9c34-3cb2-965a-3f117c75246d | -12.5425 | -58.3561 | 2025-06-06 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 2c5bad48-c482-3abb-af22-efe61858f78d | -12.3518 | -52.4722 | 2025-06-06 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 852c429e-ffc8-3ad8-a999-63fcf84182b4 | -14.7398 | -45.0848 | 2025-06-06 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| cfdf3629-d452-3a95-bba5-9f14f5d7e29a | -13.072 | -49.2374 | 2025-06-06 14:10:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 8527a56b-1931-37a4-881a-8542ea599970 | -6.9424 | -42.8126 | 2025-06-06 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 68560ec6-4d86-391e-928b-7db9e73c6b6d | -14.7393 | -45.1082 | 2025-06-06 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 5e460de7-0883-3fcc-8c77-3e5179246017 | -14.0328 | -55.13 | 2025-06-06 14:10:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 6ee06d2d-0cc1-3450-8b21-830d7b092288 | -12.3325 | -52.4953 | 2025-06-06 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| c156a3af-799a-3ce5-80cc-d607de154fe1 | -12.3376 | -46.2891 | 2025-06-06 14:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c2e3a285-a200-30d1-a9ff-915ef26c3025 | -6.2228 | -43.3226 | 2025-06-06 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 4b5e5da3-52dc-321f-a694-b49844f1f667 | -11.3716 | -56.558 | 2025-06-06 14:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 002a8f65-e87d-39d1-8038-c6e476ff953c | -8.0014 | -50.7186 | 2025-06-06 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 8e9960a3-c96a-35da-8d1e-9dc622e2337f | -12.5236 | -58.3576 | 2025-06-06 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 53c23a3e-bf47-38e7-b694-bab9cac78898 | -8.0014 | -50.7186 | 2025-06-06 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 5522efb4-b4cc-3731-b5de-1a9a50de1811 | -6.9424 | -42.8126 | 2025-06-06 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 152e76af-1f9e-3e62-9089-634e93c22124 | -14.0328 | -55.13 | 2025-06-06 14:20:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 9b88c510-0535-3b38-bd60-4b29d78fbc23 | -12.5236 | -58.3576 | 2025-06-06 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 78e7f5a5-644e-3bbc-90eb-04bf743827c9 | -12.3325 | -52.4953 | 2025-06-06 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| dfcf30ab-a10f-3256-b5e3-0773d496c72e | -14.7398 | -45.0848 | 2025-06-06 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 432e5d6b-9777-3ed9-a3c0-1ae6d9765c9a | -11.3716 | -56.558 | 2025-06-06 14:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 99bea92d-576d-36a5-8d28-6eb31f803caa | -14.7393 | -45.1082 | 2025-06-06 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 5c06dd5b-a33e-3e90-b335-6314d7f2bdd2 | -12.3376 | -46.2891 | 2025-06-06 14:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 0e650901-8797-31a6-84ba-8f12b5cf904f | -12.3518 | -52.4722 | 2025-06-06 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 447b096c-6174-3a3a-a141-ed567c5e893e | -7.1646 | -43.1442 | 2025-06-06 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 53c6ae33-e893-3001-8cac-e1e23fd0f901 | -12.5425 | -58.3561 | 2025-06-06 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4b9a5c2e-6057-3c0d-86ea-d9e7cb6d3fb6 | -7.1834 | -43.1424 | 2025-06-06 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 1209da02-3bcd-388b-aad9-da9d49104dec | -7.1646 | -43.1442 | 2025-06-06 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| d74ee913-9e1c-3ac3-814a-8a5f86720f16 | -6.9424 | -42.8126 | 2025-06-06 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 9bad8512-5052-3ac0-b103-2ded83940e38 | -12.9628 | -46.7626 | 2025-06-06 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 780b78e6-2c06-31bc-baf7-f574ddabd1cf | -12.3518 | -52.4722 | 2025-06-06 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 8403858b-ceec-36eb-acea-13062d71034f | -6.2228 | -43.3226 | 2025-06-06 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 8aa7acfb-ed66-3243-841a-7541afcc2d52 | -13.072 | -49.2374 | 2025-06-06 14:30:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 4a06bcdf-ca9b-3c4b-a3c5-4428fbcb5567 | -12.3325 | -52.4953 | 2025-06-06 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| b1dd60c1-dce2-3ffe-a378-8a8cc5ecae65 | -12.3376 | -46.2891 | 2025-06-06 14:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 61fa5862-8173-3f21-8436-020aa2293d33 | -12.5425 | -58.3561 | 2025-06-06 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| ade8a451-98bd-3e4a-b5d1-762fa267e7dd | -8.0014 | -50.7186 | 2025-06-06 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 9fb5bf9b-4b9a-3629-ac0c-74a603dba2d2 | -14.7393 | -45.1082 | 2025-06-06 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 7f62bdfd-beeb-3185-b344-d7ee21525657 | -11.3716 | -56.558 | 2025-06-06 14:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| f6312d33-c120-3910-831b-bc71e5095da4 | -12.5236 | -58.3576 | 2025-06-06 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 772359c7-eecc-3e14-9aa8-5f362355348c | -14.0328 | -55.13 | 2025-06-06 14:30:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 2589c918-2c0e-3623-9ef7-f5e017f439e5 | -11.3716 | -56.558 | 2025-06-06 14:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| ddbbc309-c8ce-3879-a2ba-84a296200b4d | -12.3325 | -52.4953 | 2025-06-06 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 67096c3a-af27-3051-823e-874abe0d1e20 | -13.072 | -49.2374 | 2025-06-06 14:40:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 50abe67b-a513-3bea-af60-01117bea473f | -12.9623 | -46.7853 | 2025-06-06 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 95df1ee9-b62b-323b-a686-c3fcafae917e | -6.9424 | -42.8126 | 2025-06-06 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 9663ebc9-53b6-3511-8284-05b46b7c05ee | -14.0328 | -55.13 | 2025-06-06 14:40:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 79e8e3d4-9fe0-3027-8981-9f0e6200e1d8 | -12.5236 | -58.3576 | 2025-06-06 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 51825c39-33b5-3993-a1c2-c818439bc295 | -6.204 | -43.3241 | 2025-06-06 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 7791a2e0-f5b8-3585-bead-5f674581304f | -12.9628 | -46.7626 | 2025-06-06 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |


