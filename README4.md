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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea6fb252-a5ab-377c-97cb-138e33c88a7a | -12.1952 | -52.7821 | 2026-06-17 01:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| af57be6c-870f-3034-9e15-1753fa30e748 | -9.3234 | -45.4787 | 2026-06-17 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| c21e0b2b-99be-3de5-8f88-777bd9f9eb6a | -9.4387 | -40.3419 | 2026-06-17 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 7f5560c9-4993-3403-afed-6e78c9ce86c1 | -5.7943 | -45.0813 | 2026-06-17 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| b0ef1187-53f5-3aa5-9571-6d793d23e48b | -12.0756 | -54.6131 | 2026-06-17 01:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 4bfcdb71-ace9-39b5-a58e-38ecff354139 | -9.3048 | -45.4581 | 2026-06-17 01:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 131.6 |
| fbb1baf8-cb19-38ed-ab91-046e1242d6d5 | -12.0945 | -54.6113 | 2026-06-17 01:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| eab57746-947f-3ec9-a2b1-8289967c4ed4 | -9.4391 | -40.3171 | 2026-06-17 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 127.2 |
| 43b25d84-0b83-3998-8282-0034f2364e6b | -12.8548 | -44.3625 | 2026-06-17 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| b2ce8b43-9faa-3dfd-8767-e6e9052f95bb | -9.4387 | -40.3419 | 2026-06-17 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 94651048-72c1-39de-8a68-1972f54166d3 | -12.8354 | -44.3657 | 2026-06-17 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| bdfcccb7-2290-3d6c-aee0-d07640a05636 | -12.8548 | -44.3625 | 2026-06-17 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 4d116385-bbdc-3d6f-b912-d285d28b66c9 | -12.2143 | -52.7801 | 2026-06-17 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| c111843c-7a2c-3ac6-a2e6-3fb37ac7479b | -9.3048 | -45.4581 | 2026-06-17 01:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 36ad9d25-edbf-3bb0-bebe-3cf8b6d6c4b5 | -5.7943 | -45.0813 | 2026-06-17 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| a2194cee-d886-3672-a9e3-c0f8519c6a3c | -12.233 | -52.799 | 2026-06-17 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 0060cacd-f12f-3d03-b6df-8f658efd2e84 | -12.2333 | -52.778 | 2026-06-17 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 019f7f65-d771-3008-b4e6-c804621380bb | -12.0756 | -54.6131 | 2026-06-17 01:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 0c2716e5-4343-3379-9df4-30db6ee9512e | -9.3234 | -45.4787 | 2026-06-17 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 22199960-e12d-3142-aacd-ff37704e0fea | -9.3045 | -45.4809 | 2026-06-17 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 56eaa6dc-bd1d-3219-967e-3786ff0eb1db | -9.4391 | -40.3171 | 2026-06-17 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 12124850-9656-3772-a09c-40f9dda399b6 | -11.5176 | -56.118999 | 2026-06-17 01:25:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 184b69b6-6585-30db-bff9-d9c4a2d5c8f7 | -14.1054 | -59.462601 | 2026-06-17 01:25:00 | METOP-C | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7717f123-086c-3db5-b132-1eeb6336a0ca | -10.1569 | -56.608799 | 2026-06-17 01:25:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f1314ee-e959-3433-9758-383d3e1d03b8 | -12.1993 | -52.784698 | 2026-06-17 01:25:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12a86b3b-d1e3-3db0-b034-4321049f31e2 | -12.0793 | -54.592499 | 2026-06-17 01:25:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a71dca15-a54b-3712-90e8-2f58cdfa9a11 | -12.1863 | -52.773998 | 2026-06-17 01:25:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18b38598-32f4-39b8-bbd5-a6b9e3047f25 | -11.5866 | -55.3302 | 2026-06-17 01:25:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41eda9e6-c01e-3ee9-a864-6c9fdbdcff62 | -18.987101 | -52.459801 | 2026-06-17 01:25:00 | METOP-C | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b6a512a9-6a30-3d16-a246-7ca4d1b9620c | -11.5964 | -55.327801 | 2026-06-17 01:25:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b254f020-aa19-3e1c-b95d-baa5bad80d31 | -14.1039 | -59.455502 | 2026-06-17 01:25:00 | METOP-C | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c2ff7ec8-ecbb-33de-804d-45f910276508 | -11.5197 | -56.127602 | 2026-06-17 01:25:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6ad8088-76fd-3f41-a5da-b389cfd992ac | -10.1265 | -52.1847 | 2026-06-17 01:25:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3474174-33e6-3f00-a83a-5bf132559775 | -10.1323 | -52.1665 | 2026-06-17 01:25:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5878de83-5406-3905-8c7f-e3af75399b56 | -11.5889 | -55.339699 | 2026-06-17 01:25:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10091a73-c131-31cd-8413-e30535fa8977 | -12.183 | -52.7607 | 2026-06-17 01:25:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 819f36d6-f2c3-3189-becc-924702e17775 | -12.196 | -52.7715 | 2026-06-17 01:25:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c87f4850-140b-3c51-ad76-82afede76ffa | -12.4312 | -58.391602 | 2026-06-17 01:25:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d1b8739a-e6eb-3fd5-a2d3-09455b3e75da | -12.1927 | -52.758202 | 2026-06-17 01:25:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0473b3d-20ff-36f8-9bb8-075c574bfb31 | -12.1896 | -52.787201 | 2026-06-17 01:25:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24062ce1-8034-3180-b878-07fd4670b632 | -12.0868 | -54.623199 | 2026-06-17 01:25:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7758966-8e36-3178-a0a8-4949155e3aff | -12.4328 | -58.398701 | 2026-06-17 01:25:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 20df18b3-c82f-32be-b5ce-d6dbd6779474 | -10.1226 | -52.168999 | 2026-06-17 01:25:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d52d0fd-c413-34b9-802f-01a1e4f4d336 | -14.0941 | -59.457699 | 2026-06-17 01:25:00 | METOP-C | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a281bda5-ccb5-3045-9025-3235b65cb6a3 | -10.1362 | -52.182201 | 2026-06-17 01:25:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0685ce6-f8fa-3007-a66f-7562892b5105 | -11.5987 | -55.337299 | 2026-06-17 01:25:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a02b936-8894-3720-be9a-ee7489a6d73f | -12.0818 | -54.602699 | 2026-06-17 01:25:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5f6338b-074a-334e-8efe-9f2a210f3ec9 | -12.0843 | -54.612999 | 2026-06-17 01:25:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e64f2da2-a255-3ec5-a535-69f9cf26df45 | -12.7664 | -59.003399 | 2026-06-17 01:25:00 | METOP-C | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 86df8366-9f94-3082-a96a-f30c04bc35eb | -12.1799 | -52.7897 | 2026-06-17 01:25:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d64683ab-3b12-3d45-b620-d4a11419fa45 | -9.2087 | -58.065701 | 2026-06-17 01:25:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9771fe2f-d5ac-3a44-a467-565fea95071b | -12.1766 | -52.776501 | 2026-06-17 01:25:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cbb29f64-4120-3921-b684-bd481e454bb6 | -12.4344 | -58.405899 | 2026-06-17 01:25:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a9af73dd-0009-3f14-a286-c39c7ffd0404 | -10.1549 | -56.600399 | 2026-06-17 01:25:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f0d3296-823f-3a8b-8c95-31b676f2e635 | -9.3045 | -45.4809 | 2026-06-17 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| fdc635f1-6d42-3085-9129-f95a58df2927 | -9.4391 | -40.3171 | 2026-06-17 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 157.0 |
| e62f842c-21d8-326f-aa37-f616e9ec93d4 | -12.8548 | -44.3625 | 2026-06-17 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 6ee8b785-cfd3-3e69-b216-591e57bf5bd1 | -12.8354 | -44.3657 | 2026-06-17 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| f31ea8cf-ba05-3ad1-8c98-f911dd51830f | -12.0756 | -54.6131 | 2026-06-17 01:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| ffdc517a-5922-3776-ad2c-451e7b7ab503 | -9.42 | -40.3198 | 2026-06-17 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 113.5 |
| a74384d9-4baa-349d-b2b8-d3fa1cde2cbc | -5.7943 | -45.0813 | 2026-06-17 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 3928303d-271b-35fb-8467-f5168c020602 | -9.3048 | -45.4581 | 2026-06-17 01:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 7a14ac77-1373-38ef-b2fd-34724ad012f0 | -9.4387 | -40.3419 | 2026-06-17 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 117.6 |
| 96701bb0-604f-3f81-957d-fe8faa11c582 | -9.4196 | -40.3447 | 2026-06-17 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 40182cee-8ce5-3ab8-8f94-d9e7b7b9a0d7 | -9.3234 | -45.4787 | 2026-06-17 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| bf564771-c062-31c9-af3f-9f0af6fc2ac0 | -12.8548 | -44.3625 | 2026-06-17 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 4e4be155-6912-3129-bbfd-8d24823d7aa0 | -9.42 | -40.3198 | 2026-06-17 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 413.8 |
| 19c31512-7295-366d-a694-3c74c04a14a2 | -5.7943 | -45.0813 | 2026-06-17 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 0eca91be-e913-3f9f-a6ad-19ea28fc85f1 | -9.3048 | -45.4581 | 2026-06-17 01:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e9bc7a56-2523-366c-a44e-eac9254f23c3 | -9.4387 | -40.3419 | 2026-06-17 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 180.7 |
| 7879da14-1f15-3bfc-99d3-a86391d810ba | -12.0756 | -54.6131 | 2026-06-17 01:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 58985596-e8d5-3245-b44c-a03f341e885a | -12.0945 | -54.6113 | 2026-06-17 01:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| d9f557de-de2b-385d-8090-861cd0d96417 | -9.4196 | -40.3447 | 2026-06-17 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 217.7 |
| b116e857-0d4c-3de9-a444-7d5fe3d71e8c | -9.4391 | -40.3171 | 2026-06-17 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 337.3 |
| 4a06bc74-b0c9-34ec-a189-3968a839765c | -12.8354 | -44.3657 | 2026-06-17 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| da93ac19-b660-3ca8-bda0-2dc0cd89e51e | -9.4391 | -40.3171 | 2026-06-17 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 158.0 |
| 4d39651f-0af5-34f3-845c-641bed0e48c4 | -12.8354 | -44.3657 | 2026-06-17 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 9c05b772-4e12-3e52-8170-e8ac74248ac8 | -9.4387 | -40.3419 | 2026-06-17 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 57.3 |
| b3e8e1c2-db84-36a0-a058-4de92ea1b8b7 | -9.3048 | -45.4581 | 2026-06-17 01:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 7ddb2d31-1ffe-324a-b88a-bf8c4dbbcc32 | -11.5502 | -52.7659 | 2026-06-17 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 0abd81da-baa4-3dea-a406-6ba4f4abe0a8 | -12.8548 | -44.3625 | 2026-06-17 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 5b39dd0e-8359-3387-b365-a51c93598369 | -12.0756 | -54.6131 | 2026-06-17 01:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| a3c73ee8-6412-3bb5-b59b-848bb349785c | -9.42 | -40.3198 | 2026-06-17 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 143.4 |
| 6b6a6a71-4fee-341e-a5fd-ea188d22fb45 | -5.7943 | -45.0813 | 2026-06-17 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a4f3fcaa-334b-3154-845d-9f60ce110d83 | -11.5502 | -52.7659 | 2026-06-17 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 0bc815a9-50ac-3f11-b9d0-9d4af988d724 | -9.3048 | -45.4581 | 2026-06-17 02:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 29e53837-1a3f-3042-8195-d226ce13e9d2 | -12.8548 | -44.3625 | 2026-06-17 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 99eb4e27-082f-3dc3-867f-92abf89fd0f1 | -11.5499 | -52.7867 | 2026-06-17 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 115af34b-b8ad-3bf7-9f13-b391be58d13d | -11.5309 | -52.7887 | 2026-06-17 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 5a4bda1a-b61e-332b-92b3-be40823aeed4 | -12.0756 | -54.6131 | 2026-06-17 02:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 8005d463-a9c2-3255-bf1f-34b3055d777d | -9.42 | -40.3198 | 2026-06-17 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 9a1dbc83-6a1b-3981-befc-0fdd47fc806b | -9.4391 | -40.3171 | 2026-06-17 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 128.6 |
| 43cdad1b-00f4-307c-8dc6-441d6080aaef | -12.8354 | -44.3657 | 2026-06-17 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 19532824-4dfd-39ab-bba8-5aa41050bd44 | -11.5312 | -52.7678 | 2026-06-17 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| e121e5a9-548f-34ea-b68e-51b62adc5bf2 | -12.8354 | -44.3657 | 2026-06-17 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 3bdfa6d5-7c61-3c8a-bb63-4cc5d7663f54 | -12.8548 | -44.3625 | 2026-06-17 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| c63d2543-a1a9-3309-a40e-7e7b285b3df7 | -9.42 | -40.3198 | 2026-06-17 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 155.9 |
| 345edf63-89af-39c2-8dfb-c01837e8dfa6 | -12.0945 | -54.6113 | 2026-06-17 02:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| dfa06f3c-449c-396e-bb42-ba13b4499687 | -5.7943 | -45.0813 | 2026-06-17 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 865d5528-e10c-383d-95c6-ae8377d0c809 | -9.4391 | -40.3171 | 2026-06-17 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 228.2 |


[Clique aqui para ver as próximas entradas](README5.md)
