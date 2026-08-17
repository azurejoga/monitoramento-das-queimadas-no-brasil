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
| d06bd176-7c76-324c-9e00-7d46828613a3 | -11.7157 | -54.6063 | 2026-08-17 00:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 84f7a681-af41-313b-8ce9-5c129ac2c295 | -14.1031 | -58.4423 | 2026-08-17 00:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 9a40d651-6d5d-3b0c-bab6-0224ec1010cc | -8.9787 | -60.5156 | 2026-08-17 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| a3009735-7c2c-3d3e-bdca-a7a48a4e1582 | -6.7123 | -58.9412 | 2026-08-17 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 2154d40e-0a21-3c3d-8086-3239d08101c5 | -10.4655 | -50.412 | 2026-08-17 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 507dbffc-9b18-3b23-8aa9-88b40115b2f4 | -6.763 | -59.7679 | 2026-08-17 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 4d67936e-20e5-3b58-8065-c1a9b5ccd08a | -15.9189 | -55.531 | 2026-08-17 00:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| c107787d-cf13-397f-ac0a-21a758bb29bb | -8.9601 | -60.5165 | 2026-08-17 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 027426c0-00a9-3a30-b980-0d852fa854e1 | -6.7124 | -58.9219 | 2026-08-17 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 9168e92c-7abf-3637-846e-aca70a03ec0e | -10.4658 | -50.3907 | 2026-08-17 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 6b1a0c01-84a1-37cd-b787-85c5b50bb7c0 | -8.9788 | -60.4964 | 2026-08-17 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 94816e39-f3e3-3c69-b1ca-6ac460f98ede | -7.3639 | -55.4935 | 2026-08-17 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7a124bab-eefd-3dd4-a625-6f4a7e73ddce | -6.1291 | -57.7418 | 2026-08-17 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 1d8f8078-5f1c-3f4d-83bb-a0de0c2161f3 | -12.3756 | -50.8825 | 2026-08-17 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 389bd6ec-83bb-3386-ae34-cda619ae0a17 | -14.4934 | -45.6647 | 2026-08-17 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 9e00bb60-c884-3a96-bf4a-5e60e6bb51f0 | -16.236 | -57.6465 | 2026-08-17 00:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 2c009895-3fbc-3147-a3c5-847a862ac05f | -6.6568 | -58.9628 | 2026-08-17 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 88d3c84d-991d-3148-b9a8-97a8c569dab0 | -6.1292 | -57.7223 | 2026-08-17 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 9340f8c6-25de-3c59-a06e-e4aed5febb6a | -16.2165 | -57.6486 | 2026-08-17 00:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.6 |
| 5212aabb-1c9d-3ab4-94fb-83753e7fe768 | -14.4734 | -45.6914 | 2026-08-17 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| dd910dfc-39e2-39a7-a4bf-3c6ed4bef17b | -7.3824 | -55.4924 | 2026-08-17 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| a01d80a4-e295-383d-9dd6-fca5f9a6d6f2 | -6.6938 | -58.942 | 2026-08-17 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 78bae626-c170-3718-8929-efeb3d3dab9c | -7.38109 | -60.00418 | 2026-08-17 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 9cd92991-d783-3f26-8fee-3e95babe3ff4 | -8.51333 | -54.90619 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 745cc5fd-6a79-38fe-866e-4f07f2b248b5 | -10.05021 | -62.45913 | 2026-08-17 00:30:00 | TERRA_M-M | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 53755901-6d73-3874-b1ca-d62eb30682cf | -6.39704 | -54.93531 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| ad302254-d9ad-3b10-9fc7-d92fd70e7530 | -8.90509 | -60.54415 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| fc02cce1-8a35-37e1-aeea-76cab5fdcd29 | -8.52552 | -54.91676 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 5e35a8b3-4ce1-374c-85ef-699e3189faab | -8.523 | -54.89884 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 41713c4f-70ee-3033-8bc0-72060b0dd6b0 | -8.72173 | -62.89685 | 2026-08-17 00:30:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 36.2 |
| e8a0b80d-c772-38a7-b1f0-18369644fa0e | -7.35953 | -55.48835 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 738d430a-e949-3db4-8493-4abc0216374c | -8.95491 | -60.57845 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a1f18d83-f20a-3f33-8187-16c196f38495 | -8.96044 | -60.5312 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.6 |
| e47e0807-a5c7-3d8e-94d6-d55ec525efe0 | -7.45518 | -59.99409 | 2026-08-17 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 1f3cb167-c59c-35f9-b5e5-ec32c19f718f | -7.36199 | -55.5061 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 8aa32f08-63f5-34cc-bd83-3ced99a8e031 | -10.0637 | -62.4575 | 2026-08-17 00:30:00 | TERRA_M-M | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 5495b828-b4a7-35e3-bb5f-adfb2d861eb3 | -9.99331 | -53.95134 | 2026-08-17 00:30:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3940a5a4-58f5-3f83-87c3-814a9ce78005 | -8.72461 | -62.92002 | 2026-08-17 00:30:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 0c56e98c-e76d-38d1-9b9f-76993484c818 | -7.36076 | -55.49722 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 8adc9cbe-dc84-3094-8857-febfb41ec1e9 | -7.40393 | -60.01428 | 2026-08-17 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 7fe4004f-8bd9-37d4-ae71-522a4c310dee | -6.86827 | -56.40999 | 2026-08-17 00:30:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 1256f6c5-1b71-31b0-962e-68e4b689f823 | -8.94913 | -60.53272 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 3c4f5ffc-cfae-3668-ba1a-cad67a56ffbc | -7.61588 | -60.951 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 21a92c65-2ab8-3429-ab6a-79ad03779667 | -9.4747 | -51.66516 | 2026-08-17 00:30:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c443f6ea-82a8-3da5-a0e2-bd9d6a8c1e40 | -8.72889 | -62.88939 | 2026-08-17 00:30:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| d719d4b9-a50c-39cc-8383-dfecc18528de | -9.47253 | -60.50727 | 2026-08-17 00:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 124c0c03-5f30-3987-9097-9e69cf842116 | -8.54455 | -54.59949 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4b36159f-51b3-30a1-bac3-1cb10f0bf44f | -10.07746 | -60.49844 | 2026-08-17 00:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| a887d0bc-ee06-3186-b744-efbdd6f5d2c7 | -8.09466 | -61.36041 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| dc7284d7-80cc-3532-9150-ba51363f0578 | -8.9819 | -60.522 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 61a7b726-5fcb-3bcf-af49-fe2c429ef0d1 | -8.89995 | -60.60107 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 168.3 |
| d068a16a-ab6c-371e-8c89-00a723f3ebb3 | -9.98293 | -53.94327 | 2026-08-17 00:30:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| dfb13f0a-96f5-3fc1-8c2c-62a3f2060a83 | -8.0324 | -55.15254 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| e1c7ffae-49d9-3ffe-8349-c420f04d5835 | -6.96098 | -59.03858 | 2026-08-17 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 315eb757-de7e-3c81-b1d1-5a5c478ecb44 | -7.38085 | -55.51244 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 969b0082-6f2e-36df-8d2d-9f03123cdc62 | -8.51459 | -54.91523 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f799d2ac-54c6-3094-a534-d6101d3a27fe | -6.86948 | -56.41882 | 2026-08-17 00:30:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| d7999a1d-292e-3340-b106-9c2a74574bd0 | -8.66844 | -54.76088 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 114958c8-531e-3f18-b989-1fd56fa66bf2 | -6.40725 | -54.93691 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| edfd8c37-c3ca-3fe6-b92b-6d7d3b244ed9 | -7.50374 | -60.07544 | 2026-08-17 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 506cbb0e-1e61-380d-8ab0-f22f54dc16af | -7.56015 | -60.87094 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 93a0a6b7-c5d3-393c-bc61-7d7fc9aed099 | -7.38721 | -55.49346 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 002aaa6d-e302-3778-8328-f2406b80eab0 | -8.59596 | -54.69733 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| aeaabb3d-d2c6-3b61-b74d-ed2f07a4d144 | -6.41621 | -54.93562 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 540fb12a-c203-3126-8423-e7d5877555c4 | -8.52426 | -54.90782 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| a5656608-dda5-3ae5-a8b3-15d7c05fa2fd | -8.94721 | -60.51757 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| c03d9283-dffb-3dd5-8d5f-9051076c4b55 | -6.99337 | -59.05692 | 2026-08-17 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 864aaa3a-7104-3112-bb1c-2c1a8e6b2223 | -7.37717 | -55.48584 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 10f6df9d-579f-3085-8736-7bec93ce4326 | -7.37839 | -55.49471 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 82dc7b90-5462-3b6f-abad-ed1d2f061cf6 | -8.52677 | -54.92569 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1932ef1f-ac1b-36d3-8e7e-9a77065578bd | -8.50696 | -54.92543 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 032c58f3-f6c8-3d01-a172-ccba7171eca6 | -8.98112 | -60.51308 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 427520ef-4074-3d74-a92e-dab5cbf6f99a | -6.41492 | -54.92646 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| cb4fa734-ab11-3bf0-af43-0e95b912b223 | -8.58577 | -54.68954 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| bd621a21-b889-3246-b871-71e5b16c6b54 | -7.57004 | -60.86323 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 9eb42b6f-3e5e-35a3-bdb5-1b791649700e | -9.30354 | -49.10282 | 2026-08-17 00:30:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c6a21c61-a258-3b3f-a17e-c25846355a28 | -8.89377 | -60.5456 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 26ffdcd8-78cc-38db-b6e3-1af69e4a7700 | -8.90182 | -60.61646 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 488fc1e7-78da-3c5b-93e1-81ccc5ba0af6 | -7.45107 | -60.00155 | 2026-08-17 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 11e062e9-dcfd-3f0d-bdfc-9b222f9ead3d | -8.97176 | -60.52975 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 44755738-f3c6-3d06-b8b4-3f924241b89b | -8.96982 | -60.51461 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 883efb5b-8b2a-32ab-bfa2-68f8e2168ecb | -8.73161 | -62.91257 | 2026-08-17 00:30:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 3f2b95b7-fef9-3622-8104-5526b5d9216e | -7.55462 | -61.19114 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 943c451f-3316-3b86-8d6f-a2d87198bb49 | -6.82025 | -56.45275 | 2026-08-17 00:30:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f54d5060-a074-3390-a87f-69d8c8d1e784 | -7.3708 | -55.50482 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| eb56693b-8013-347c-a6d5-f973807dc243 | -7.45693 | -60.00719 | 2026-08-17 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| c057f5d6-7684-3509-973e-bd16fa67ec24 | -9.17454 | -59.6749 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 5246a43f-e460-38a4-9df8-6eea8b960ea2 | -8.9076 | -60.56915 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 81227e38-931f-3d5d-b5e7-332e126998c6 | -9.30041 | -56.81165 | 2026-08-17 00:30:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 04de6f54-2bb2-38fe-bb28-1cfee97eb529 | -8.8944 | -60.5554 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 717892e9-c99e-3d2a-9d0f-609b4967c2da | -8.97917 | -60.49802 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| dcc86e27-9ac3-3eea-b409-211aeb71f5bb | -8.56242 | -54.5969 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| db8238c0-cf85-3dab-b857-d5823bf34aa9 | -8.67097 | -54.779 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 240c2cfe-92fa-34a4-be3b-79f24f5bba5a | -8.66971 | -54.76995 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 57c3f260-9dae-351f-bf95-1b15ab723c39 | -8.02232 | -55.14489 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0bea8a4e-4c5d-3cf5-b44b-650fb716717b | -9.20016 | -60.78956 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 83c4c4e3-e0af-3bb2-84f4-5f0ee7d2cb6e | -8.98307 | -60.52823 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f9c6b5c1-c89f-3f2c-a219-0580904e743b | -8.03116 | -55.14365 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| e83af313-4ead-3c8f-8c0f-2d753c5b2dc3 | -8.95684 | -60.59373 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 801fc426-232c-3996-b81a-5a01f6171f8d | -7.07752 | -56.65759 | 2026-08-17 00:30:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |


[Clique aqui para ver as próximas entradas](README5.md)
