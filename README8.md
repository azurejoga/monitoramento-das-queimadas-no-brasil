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
| c52b0cff-27a7-3f5a-8190-4528b54c0dff | -4.2913 | -43.7822 | 2026-01-08 06:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 0e654d33-ed54-338f-9246-b619b8a22ab6 | -4.2914 | -43.7591 | 2026-01-08 06:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 65d64361-826e-3c73-a3a5-6928c04161aa | -4.2728 | -43.7601 | 2026-01-08 06:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 58f466c5-d905-361a-a1e9-354fd06e447c | -4.2914 | -43.7591 | 2026-01-08 06:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| cdd9354a-605f-3671-87d9-961fbe7e5f8c | -4.2913 | -43.7822 | 2026-01-08 06:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| add28fe2-bf67-3ddc-b491-f917509b1d9f | -4.2726 | -43.7832 | 2026-01-08 06:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 8bed52d3-6457-3086-81af-5c304822a6ac | -4.2829 | -43.78 | 2026-01-08 06:29:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 2be507da-8ece-327d-b722-7f44709cf791 | -1.58834 | -46.68316 | 2026-01-08 06:29:00 | AQUA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| dd6ad730-fc63-38e2-a7dc-f0e968c05263 | -4.27217 | -43.7531 | 2026-01-08 06:29:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 0c7c3e4b-e4e3-3d3c-9a26-53326a0fbb47 | -4.26865 | -43.7781 | 2026-01-08 06:29:00 | AQUA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 6df002da-105b-3240-ab91-9b8cd45f92fe | -4.28643 | -43.75511 | 2026-01-08 06:29:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| e197cf42-20eb-32f0-a869-91a89c91d296 | -4.2726 | -43.7832 | 2026-01-08 06:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| f99b032d-557c-3087-9e7e-83b446c1510c | -4.2913 | -43.7822 | 2026-01-08 06:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 428f7bea-d99c-34b4-b725-b0ec3be12d1b | -4.2728 | -43.7601 | 2026-01-08 06:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| dfc46651-db43-33f9-9522-f855942a9ce2 | -8.95008 | -50.13341 | 2026-01-08 06:31:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 485e3e31-7b9e-3bb1-bc02-8802f6c94709 | -16.86868 | -57.79885 | 2026-01-08 06:33:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 58de7e36-28e5-38de-b6e3-3b53f617664f | -20.88976 | -52.34077 | 2026-01-08 06:33:00 | AQUA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 5fbec125-2d02-3c45-8623-06414872aec9 | -17.7909 | -57.52065 | 2026-01-08 06:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 39403d75-c313-3744-b06f-bf146f00c434 | -4.2913 | -43.7822 | 2026-01-08 06:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 94634967-8f30-3b6b-82f3-6476fd60657f | -4.2726 | -43.7832 | 2026-01-08 06:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 7757f9ec-b09b-35af-84ea-8ff28ab759a0 | -4.2914 | -43.7591 | 2026-01-08 06:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 29d19da5-8077-3bfb-a4db-5e9f45c7d5e7 | -4.2728 | -43.7601 | 2026-01-08 06:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 71651bac-fb0e-3120-a325-6b5b4d6d27cb | -4.2728 | -43.7601 | 2026-01-08 06:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| aecf9f07-76c7-366a-bf7c-7accaff655cf | -4.2726 | -43.7832 | 2026-01-08 06:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 6a556327-3c65-30c8-aa0e-123821583be9 | -4.2726 | -43.7832 | 2026-01-08 07:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| a35a6365-9f85-3655-a7d3-432f9f29be40 | -4.2728 | -43.7601 | 2026-01-08 07:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 86bbf8fe-e8f6-3bf7-99de-e5b12caf02bf | -4.2728 | -43.7601 | 2026-01-08 07:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 4e2c5aee-63a9-3eb4-8e86-e13e193dfe65 | -4.2726 | -43.7832 | 2026-01-08 07:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 4b39ba73-1aa1-3138-ad55-e53b5820c953 | -4.2726 | -43.7832 | 2026-01-08 07:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 18cc8704-2f64-3e1d-92fc-7babc903e86b | -4.2728 | -43.7601 | 2026-01-08 07:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 7ddc933d-f54e-3f5f-b3e8-2dd19673f7be | -4.2913 | -43.7822 | 2026-01-08 07:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 913e8665-cf53-32f0-9ee2-540f566f8261 | -4.2913 | -43.7822 | 2026-01-08 07:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 8944afa3-d5de-321f-80de-ce55def8f7a3 | -4.2728 | -43.7601 | 2026-01-08 07:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 73817ad0-d21a-3976-950c-22c74e3b4a2a | -4.2726 | -43.7832 | 2026-01-08 07:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 2d9128bc-06d8-386d-950f-77ba88d9a0a5 | -4.2728 | -43.7601 | 2026-01-08 07:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| b68c77e5-bb78-31b4-8864-bb935244c5e9 | -4.2726 | -43.7832 | 2026-01-08 07:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 988bde35-de28-3c6a-a76d-b05c95abd153 | -4.2726 | -43.7832 | 2026-01-08 08:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| e10cd580-7f9c-301f-9fb6-e68cb0bb56a4 | -4.2728 | -43.7601 | 2026-01-08 08:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| fd73aefc-aad6-37ab-a836-73bde5d233ee | -4.2913 | -43.7822 | 2026-01-08 08:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| cb289ba4-4e5c-34d9-be16-1533079dd033 | -4.2728 | -43.7601 | 2026-01-08 08:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| a297bbb2-c77b-3694-9351-c22587d9446c | -4.2726 | -43.7832 | 2026-01-08 08:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 59259b2c-2f7c-33cf-a2f2-7f621fc37e62 | -4.2913 | -43.7822 | 2026-01-08 08:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 7e8d5fe0-59a5-3ea8-93be-43352893a099 | -4.2726 | -43.7832 | 2026-01-08 09:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| bbb05671-7bee-3334-88e9-4d8f38ca31f3 | -4.2913 | -43.7822 | 2026-01-08 09:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 01db51e8-b707-3258-b560-b3077f11cd19 | -4.2726 | -43.7832 | 2026-01-08 09:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 6f276095-b1de-342d-8710-7996c469b090 | -4.2913 | -43.7822 | 2026-01-08 09:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| a299a15d-3932-39ea-bef5-05d50c2978f8 | -4.2726 | -43.7832 | 2026-01-08 09:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 38b79fb5-074f-38f0-81f8-55b411acf569 | -4.2726 | -43.7832 | 2026-01-08 09:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 4ad32cda-8178-3750-a839-0523f6728a0a | -4.2726 | -43.7832 | 2026-01-08 09:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 571eac25-0078-39b3-872a-b50bb5ba26b4 | -4.2726 | -43.7832 | 2026-01-08 10:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 1d73c84a-26eb-364b-bb41-d3ed41f1d036 | -4.2913 | -43.7822 | 2026-01-08 10:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 985d5828-f518-383d-9898-f2a5e7e34163 | -4.2728 | -43.7601 | 2026-01-08 10:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 1295962f-0cc4-3dfe-a10e-e0d32abb26ee | -4.2726 | -43.7832 | 2026-01-08 10:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 47d4a134-b02f-3b2d-8f8c-4b11dd158d26 | -4.2914 | -43.7591 | 2026-01-08 10:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 6c6270a8-61b4-34a0-a899-223e516979e1 | -4.2913 | -43.7822 | 2026-01-08 10:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 21155ba0-a8cb-3950-aefa-0296c6d279ef | -4.2728 | -43.7601 | 2026-01-08 10:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| cc0550dd-19c8-389e-9619-e759f36d1972 | -4.2914 | -43.7591 | 2026-01-08 11:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 610ac9ec-4f78-38ee-bd81-ffe50e8c1885 | -4.65757 | -37.70121 | 2026-01-08 11:14:00 | TERRA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 35.7 |
| e40805be-ab09-3e01-bec0-a9e8e88020a3 | -8.86458 | -44.15791 | 2026-01-08 11:17:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 4c63aad5-575d-34d7-9c97-2b9cebc116db | -4.2914 | -43.7591 | 2026-01-08 12:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 248.0 |
| f782777f-d548-3d73-96c2-114e309e5103 | -4.2728 | -43.7601 | 2026-01-08 12:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 397.7 |
| f2cb5e3b-bc8a-3aaf-bdb3-d823e2491d33 | -4.2539 | -43.7843 | 2026-01-08 12:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| a90821fa-e89f-3f03-abec-39bbbf3a0cd3 | -4.2914 | -43.7591 | 2026-01-08 12:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 358.8 |
| b001131d-85e3-3915-80bd-21555ab33cd5 | -4.2541 | -43.7612 | 2026-01-08 12:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| f509746d-d81c-3093-b362-a74eca50242d | -4.2914 | -43.7591 | 2026-01-08 12:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 259.8 |
| 8c3ef046-4f7d-39be-84c5-16044fc4a621 | -4.2728 | -43.7601 | 2026-01-08 12:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 361.0 |
| 5af10f4e-1450-3bec-b52c-b46e27070aeb | -4.2539 | -43.7843 | 2026-01-08 12:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 172.7 |
| a96b61e5-8cbc-39b6-9dcd-904f0f08d9f2 | -4.2914 | -43.7591 | 2026-01-08 12:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 544.7 |
| 4339c57b-6ee3-3b7e-8faa-37ee398ab06c | -4.2728 | -43.7601 | 2026-01-08 12:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 505.7 |
| 3c1c9d2d-022e-3312-85ff-fd8c85bcb8a5 | -4.2539 | -43.7843 | 2026-01-08 12:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 4532ec81-b0ff-343a-811e-99da24021883 | -4.2541 | -43.7612 | 2026-01-08 12:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 090249d8-89d2-3cf5-a423-c10a6c69556f | -1.29238 | -53.68847 | 2026-01-08 12:53:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e71b2441-9856-3fb3-9fa7-565bfa36c192 | 3.44012 | -60.45308 | 2026-01-08 12:53:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 05267a46-f25d-34bf-ab1b-2efa24a99881 | 3.29246 | -60.78753 | 2026-01-08 12:53:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| cfd7a5ee-80ee-3d34-9c3a-1494322e615e | -4.2728 | -43.7601 | 2026-01-08 13:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 290.7 |
| 0d18169e-e54e-3ec5-bfaf-8f403be399d1 | -4.2539 | -43.7843 | 2026-01-08 13:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 30f51099-810d-3283-8f2a-a18024cca490 | -4.2914 | -43.7591 | 2026-01-08 13:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 280.7 |
| b9ffbe1b-b00c-3ce0-ab50-fbde1ee0ff98 | -4.2728 | -43.7601 | 2026-01-08 13:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 270.5 |
| 5867ed22-3526-3805-8d04-d47ee8774482 | -4.2914 | -43.7591 | 2026-01-08 13:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 322.5 |
| 95846b0e-5312-3ac1-a09b-bc8eef870d48 | -4.2539 | -43.7843 | 2026-01-08 13:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| f816bc5a-17c2-31e5-8d7f-db049d20e049 | -4.2728 | -43.7601 | 2026-01-08 13:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 388f22f6-808a-3309-b1c1-4009257b1897 | -4.2539 | -43.7843 | 2026-01-08 13:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 72c39f72-8189-3e6b-93d2-9ec7c4185805 | -4.2914 | -43.7591 | 2026-01-08 13:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 4d67e05d-1c45-3a22-8943-70a5e6db35ad | -3.4217 | -42.4739 | 2026-01-08 13:20:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 7325106a-76a4-3680-8a54-765d0d859dea | -4.2728 | -43.7601 | 2026-01-08 13:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 181.5 |
| b01dea34-64bc-3e5e-9bfd-5f6db775d0c1 | -4.2914 | -43.7591 | 2026-01-08 13:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 2c71eca4-27fc-3599-a52d-88a96d86fe2b | -20.5692 | -57.9565 | 2026-01-08 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 33c78164-3360-321b-8020-b62f76dd4163 | -4.2728 | -43.7601 | 2026-01-08 13:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 41195816-8cff-3323-9ca7-d7f2f03eb1e4 | -4.2914 | -43.7591 | 2026-01-08 13:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 16bd46bc-c803-34c2-b339-ade197a0477c | -20.5486 | -57.9802 | 2026-01-08 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 7a8387a1-1a9e-3f5c-bd2b-d6c04d478bff | -20.5692 | -57.9565 | 2026-01-08 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 569405f7-686a-3be7-9416-bcde7b1e957f | -4.2914 | -43.7591 | 2026-01-08 13:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 7df22b7f-8197-3e61-901a-c63481a4d12c | -4.2728 | -43.7601 | 2026-01-08 13:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 859baf7e-cdf6-3bd2-8994-ea382a7966e7 | -4.2914 | -43.7591 | 2026-01-08 14:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| ae5589c4-da4e-312f-bbd1-449014267b06 | -4.2728 | -43.7601 | 2026-01-08 14:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| ccec9b26-0c73-30a5-9970-c027acb73661 | -20.5486 | -57.9802 | 2026-01-08 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 5c1cc671-6557-3751-b865-4b885735b0cd | -20.5283 | -57.983 | 2026-01-08 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 02a159b9-9f9d-3bcc-ae3d-e9b17dc0b6bb | -4.2539 | -43.7843 | 2026-01-08 14:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| ea672d16-eaee-3681-bad4-7621d1729cb3 | -4.2728 | -43.7601 | 2026-01-08 14:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 6065ce77-32a6-3314-b5de-5f4721e963a3 | -20.5486 | -57.9802 | 2026-01-08 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.3 |


[Clique aqui para ver as próximas entradas](README9.md)
