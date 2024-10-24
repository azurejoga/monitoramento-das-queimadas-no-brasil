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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e942fd58-6ba0-3200-b028-424a166e33aa | -19.6438 | -56.8521 | 2024-10-24 04:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.6 |
| fa7ace9a-606d-3973-9f58-6baab6c8fb04 | -19.7262 | -56.7358 | 2024-10-24 04:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 56f25d73-c174-3f4c-9a37-330e4a0d5a52 | -1.5878 | -53.3089 | 2024-10-24 04:15:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 9b338bf4-c788-3fe8-a864-e278342666bd | -2.9578 | -50.4198 | 2024-10-24 04:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 57ffb5f9-2811-343b-a651-b72d9fd46b9a | -2.9763 | -50.4193 | 2024-10-24 04:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 019037bc-a1eb-32e5-8500-1aeb479992e2 | -3.1607 | -50.4556 | 2024-10-24 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| e5b031d5-d376-308d-b2d4-fb13a8546160 | -3.9394 | -46.445 | 2024-10-24 04:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| aa167aa6-2ef3-396e-b34d-10ee35416223 | -3.9396 | -46.4229 | 2024-10-24 04:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 3ac2348e-dc95-3094-9492-d541bd5ef896 | -16.94 | -57.5268 | 2024-10-24 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 209c7386-a632-3530-8fd4-6e656e8b494e | -16.9596 | -57.5245 | 2024-10-24 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.0 |
| 6ecf081d-53b5-3820-84e1-f0178d23f533 | -16.9599 | -57.5041 | 2024-10-24 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 2755d831-9ae1-3778-b624-a1061f9ac948 | -16.9792 | -57.5223 | 2024-10-24 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 0f2e8b10-2a79-3148-b7f9-b50831627169 | -17.2383 | -57.2462 | 2024-10-24 04:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.6 |
| 7e5638c9-77cd-300f-8a9f-5188951fb798 | -17.2579 | -57.2439 | 2024-10-24 04:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| e82b3b2f-8cfa-32ba-babe-635cc0b62413 | -19.5681 | -56.6114 | 2024-10-24 04:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 91a1a9d6-d7a8-3dd7-8ee7-d38335518001 | -19.6438 | -56.8521 | 2024-10-24 04:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| eaa52c7e-31d6-3c5f-b45a-e47ae5ff2792 | -1.5878 | -53.3089 | 2024-10-24 04:25:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| b19d09a9-9798-3e82-a09c-3678e02866df | -2.9578 | -50.4198 | 2024-10-24 04:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| b09d010d-4ddf-3bf5-b0f6-1699a34e9766 | -2.9763 | -50.4193 | 2024-10-24 04:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 1f31647e-2270-38b5-895c-86c5ae400ee1 | -3.1607 | -50.4556 | 2024-10-24 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 81fae265-1500-3cf9-a649-8cb5c124490d | -3.9396 | -46.4229 | 2024-10-24 04:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 85b52b30-2362-32a3-aa92-d2d8e8badcc3 | -16.94 | -57.5268 | 2024-10-24 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| eea77213-57b5-350a-ab32-f4ec95bdb6dd | -16.9596 | -57.5245 | 2024-10-24 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.7 |
| 7b0eb396-8780-3dcf-9b9f-72960f74c642 | -16.9599 | -57.5041 | 2024-10-24 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 5e998bc6-7e7c-3575-b916-eb20726e9a13 | -16.9792 | -57.5223 | 2024-10-24 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| f50f84b4-c050-3575-9b2f-c89d33311219 | -17.2383 | -57.2462 | 2024-10-24 04:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| 9760832e-466a-39c3-98cd-1876e49f6c95 | -17.2579 | -57.2439 | 2024-10-24 04:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| c14cc5f4-9c60-3522-a89f-d3985210677e | -19.5071 | -56.6619 | 2024-10-24 04:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 7c9bbb6b-f7f9-3fbe-b52b-862213843195 | -19.5075 | -56.6409 | 2024-10-24 04:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 068ffb0c-55f5-3832-8978-c59548a3eab9 | -19.5465 | -56.6983 | 2024-10-24 04:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.7 |
| fb60ec06-65ac-3d43-a343-3ddbc82343c9 | -19.5469 | -56.6773 | 2024-10-24 04:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 131.7 |
| 7262e879-9d4e-3f8a-a27f-b74ea582cf07 | -19.5473 | -56.6563 | 2024-10-24 04:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 415457e2-d6bb-3224-8d1b-148604c64937 | -19.5666 | -56.6954 | 2024-10-24 04:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 4a5f7b7c-d9ad-3c4c-a791-99386b634448 | -19.5669 | -56.6744 | 2024-10-24 04:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.8 |
| 97c57d4a-7012-3ebc-8211-91a32ce5293d | -19.5681 | -56.6114 | 2024-10-24 04:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 36b537c7-b2a8-320a-b5e1-d339bc237f29 | -19.6438 | -56.8521 | 2024-10-24 04:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 37cc9c5f-6925-3a59-8391-e0fa5f3bd2d6 | -19.6442 | -56.8311 | 2024-10-24 04:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 60.1 |
| 483e5d92-94a1-36ff-8322-1d9b89ca6d62 | -23.8155 | -55.2933 | 2024-10-24 04:27:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 63.7 |
| 0516b0a4-3e7b-3284-97ac-6b528fa841e8 | -23.8366 | -55.2894 | 2024-10-24 04:27:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 73.6 |
| 8ec639a3-72db-3598-aeef-01dc0141c4c9 | 3.52089 | -51.45605 | 2024-10-24 04:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4df1772f-9a01-3bb5-9657-132871643db9 | 3.51712 | -51.45581 | 2024-10-24 04:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3be3494-078b-3ae4-b628-6772186a2d13 | 3.51663 | -51.45668 | 2024-10-24 04:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ede9fc68-9e5e-3f1e-93bb-7296ab980d99 | 3.48715 | -51.25652 | 2024-10-24 04:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb0dc64a-6584-3592-b561-6fc342103ebb | 3.48616 | -51.25613 | 2024-10-24 04:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63b7fabc-123b-3e3d-86ab-2e06ec60785d | 3.48295 | -51.25715 | 2024-10-24 04:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a74fcab-1ae5-3ee6-b2af-2247a3017a7a | 3.48196 | -51.25675 | 2024-10-24 04:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3f5675d-f3b0-341d-b430-3b3b2d20d642 | 3.47955 | -51.26893 | 2024-10-24 04:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db1d9392-edaa-3e65-96b5-f5a3d89ff525 | 3.47932 | -51.26163 | 2024-10-24 04:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 693b1330-7775-324c-bff5-58e2cfe7f8fa | 3.47896 | -51.26508 | 2024-10-24 04:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efdae5e8-ae2c-3d3c-bae4-b9bafc156eaf | 3.47836 | -51.26122 | 2024-10-24 04:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d26bd926-4930-3fec-8f40-4655f34d56df | -6.51141 | -35.25595 | 2024-10-24 04:32:00 | NOAA-21 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 12.5 |
| a4a9a7b6-ede9-3753-8e1c-c1f42437bab7 | -6.5072 | -35.25599 | 2024-10-24 04:32:00 | NOAA-21 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 13.0 |
| fa580511-f1db-3913-9b86-0067f82c00ef | -6.5048 | -35.2547 | 2024-10-24 04:32:00 | NOAA-21 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a21ec080-f57d-37ca-910e-cd50fde0d43f | -5.16758 | -37.71085 | 2024-10-24 04:32:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 28667d99-9e42-38df-ba31-cdb6b48846e1 | -5.16704 | -37.71462 | 2024-10-24 04:32:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6c576c47-4515-3e61-afbe-5548e51aec78 | -5.20778 | -38.99891 | 2024-10-24 04:32:00 | NOAA-21 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7b1fcf7c-6e23-3b89-ad8a-cfc984ec83d7 | -3.45549 | -41.26519 | 2024-10-24 04:32:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b55079e0-6ecf-3bce-908b-ddb23824bb07 | -3.45181 | -41.26067 | 2024-10-24 04:32:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0144dc2c-e6de-36ee-ba0c-ba820ddb9ecc | -3.45124 | -41.26441 | 2024-10-24 04:32:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 47e8c6a8-dd2e-36d1-a724-1f841e617f8b | -3.16393 | -40.2066 | 2024-10-24 04:32:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4dce2e31-f27c-38d7-b6b3-dfecf95cfe8a | -4.0923 | -40.89594 | 2024-10-24 04:32:00 | NOAA-21 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5be4ec7f-73f6-3bb7-848f-3cd526f92d2f | -4.09179 | -40.89761 | 2024-10-24 04:32:00 | NOAA-21 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 46ce8e19-9c43-313a-92d6-aa3c22fe8e19 | -3.85546 | -40.7007 | 2024-10-24 04:32:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cbaecf4b-c30a-3e74-9a83-8943951cb98e | -3.85479 | -40.70519 | 2024-10-24 04:32:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3f1eea69-e122-33eb-9037-91c14943564d | -5.27043 | -41.20869 | 2024-10-24 04:32:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e91c2837-23a6-361b-9de4-c8bd00a59283 | -5.25782 | -41.20249 | 2024-10-24 04:32:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 96357c1e-3bb5-38cf-aa37-27ee26de23d0 | -5.24078 | -41.19581 | 2024-10-24 04:32:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| af71ad94-5aa7-3e36-af06-d1567d1bbbdb | -5.24057 | -41.19798 | 2024-10-24 04:32:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d61b426c-7d85-3b4a-b8d1-9e5ce7fcde73 | -5.13007 | -41.06247 | 2024-10-24 04:32:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2a95f048-59bc-3748-981b-347f3a03dccf | -3.46528 | -41.99804 | 2024-10-24 04:32:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6d0811bf-0ed7-3936-addc-4e58df04d42b | -3.4341 | -42.54478 | 2024-10-24 04:32:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 847e57f5-e1b6-3a23-bfdf-d61eacc00915 | -4.85338 | -42.46982 | 2024-10-24 04:32:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 226451c2-e093-3931-881f-42925d7ec53d | -3.71696 | -41.68381 | 2024-10-24 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bff4f1b6-7ff6-3cb8-b88e-8716e27759d5 | -3.71639 | -41.6876 | 2024-10-24 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5537ecd1-1bd1-3bf0-9b2d-7ee9dfd2b0d8 | -3.7128 | -41.68318 | 2024-10-24 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 531bc304-506c-3ab6-a6e4-e00ae66302e4 | -3.71223 | -41.68697 | 2024-10-24 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| db18d89d-9165-3962-a57c-054b0faa615a | -3.70864 | -41.68255 | 2024-10-24 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 5391b856-0cc5-3522-b402-12f8be53c0dd | -3.70807 | -41.68633 | 2024-10-24 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 77b0e50a-008e-37c1-a544-350def264679 | -3.80659 | -42.55115 | 2024-10-24 04:32:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb16738e-297d-3c5e-9307-7337d0b4a0cf | -6.03235 | -43.10175 | 2024-10-24 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 397c5fb6-fdf3-3555-b80a-e1c4ef61aaa9 | -6.03202 | -43.10342 | 2024-10-24 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 46110397-258c-323e-946a-5fc533095a59 | -6.03157 | -43.1069 | 2024-10-24 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 509b5414-9d9d-33df-a4a3-45ef075f8065 | -6.01 | -42.21807 | 2024-10-24 04:32:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a9bae9df-29f2-3a09-922f-89dad39a7a69 | -6.00585 | -42.21744 | 2024-10-24 04:32:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 711fe46d-eb52-3436-b231-37c8424217d1 | -6.00169 | -42.21681 | 2024-10-24 04:32:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5d2e313f-226b-3add-8e9a-ab8bd93c57b2 | -5.91027 | -42.75742 | 2024-10-24 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0374b8fd-116a-368a-9c6b-b8210b60f0df | -5.90798 | -42.88401 | 2024-10-24 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ec375af7-15a7-3f5c-a8fb-64c71e3b2aa1 | -5.90748 | -42.88741 | 2024-10-24 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c24c40c8-37b7-35ca-ac75-2bd54b35967d | -5.90626 | -42.75683 | 2024-10-24 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0a9dc947-c3be-3e44-8334-eb9500213976 | -5.90401 | -42.88345 | 2024-10-24 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 53312ff9-4031-3664-988d-eb144d9532c2 | -5.90351 | -42.88679 | 2024-10-24 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 4862cead-c841-326a-8aaa-4e2ccc216041 | -5.8956 | -42.85767 | 2024-10-24 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3fd75e1b-459b-3fd6-8a02-947f9f7ec894 | -5.76964 | -42.63268 | 2024-10-24 04:32:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7944504f-7e83-3c73-b548-af78afa457f9 | -5.76507 | -42.63568 | 2024-10-24 04:32:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f72f9d56-d041-3c66-aa3a-03800b0917e1 | -5.76337 | -42.33818 | 2024-10-24 04:32:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 38932868-4ee7-3ca9-936e-78d215d56e53 | -5.76282 | -42.34193 | 2024-10-24 04:32:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 52c98ba4-ca6c-3f3e-8d7b-029d8e1623f3 | -5.75871 | -42.3413 | 2024-10-24 04:32:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 512dcd51-d592-3700-b4c8-d4d58137472a | -5.6657 | -42.94825 | 2024-10-24 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 41002878-5071-30a3-b490-ea70bc203145 | -5.62571 | -42.7887 | 2024-10-24 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0177a8c7-6b22-30ec-9fb3-2091238dc82d | -5.6203 | -42.77038 | 2024-10-24 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |


[Clique aqui para ver as próximas entradas](README26.md)
