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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d8fcf41-8f5d-3268-8f38-6a579dc00620 | -1.6419 | -53.8731 | 2024-11-30 07:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 47f046c3-e884-3cbb-8407-91f98c76d639 | -2.5699 | -45.3831 | 2024-11-30 07:50:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| bda34d8b-03cb-3b77-8dab-34a03036082d | -1.5868 | -53.8537 | 2024-11-30 07:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 93377d08-caf6-3c9a-a916-1161711559a0 | -1.5868 | -53.8738 | 2024-11-30 07:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 9d0249b8-937f-35a2-823f-e45a01c3b386 | -3.2591 | -53.6186 | 2024-11-30 07:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 1c9f2119-56a9-3139-b757-a13489f1ff1f | -2.9983 | -45.1433 | 2024-11-30 08:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 120.7 |
| b76ec7e4-bfae-318d-9999-1faab444defd | -3.0169 | -45.1426 | 2024-11-30 08:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| d276a290-d376-3999-9615-8895f1e5203d | -1.5868 | -53.8537 | 2024-11-30 08:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 8009431c-e84f-3cbc-9269-0e67f8205738 | -2.9984 | -45.1207 | 2024-11-30 08:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 5383ecfc-d8db-3190-97e0-d72d08d30978 | -3.2591 | -53.6186 | 2024-11-30 08:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 7aa0191a-90fd-33e0-b894-7d045dd8425b | -3.259 | -53.6388 | 2024-11-30 08:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 8a258e01-a148-382e-8fa9-70fbbf8d7e0b | -2.57 | -45.3606 | 2024-11-30 08:00:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 142.2 |
| b7a67e79-744e-34cf-baad-28aad9dabe2f | -3.259 | -53.6388 | 2024-11-30 08:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 88683650-4e24-3075-9e2f-38b0009d75dc | -3.2591 | -53.6186 | 2024-11-30 08:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 990efc15-1f21-3a14-b63a-60d3c3176bc2 | -3.259 | -53.6388 | 2024-11-30 08:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| edb56133-6497-3866-872e-e387411e0b02 | -3.2591 | -53.6186 | 2024-11-30 08:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| a63182e1-0136-3d86-93f9-3067869a90c6 | -3.259 | -53.6388 | 2024-11-30 08:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| e10a2c0c-13b1-3c13-a3b5-a35c689cf134 | -1.6419 | -53.8731 | 2024-11-30 08:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| efbb91a2-c772-366a-94ba-6122ef8a25bd | -3.2406 | -53.6393 | 2024-11-30 08:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 3a39598b-43a3-3a55-8f55-e19e553d0897 | -3.2591 | -53.6186 | 2024-11-30 08:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 601d8ae7-3fa2-325e-aa16-02ee957676e1 | 1.1805 | -55.9671 | 2024-11-30 08:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| efffbcf0-84f5-3500-93e5-e3ca88f92367 | 1.1805 | -55.9671 | 2024-11-30 08:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 62d2182e-e3e4-3c5a-b055-b0c56fc9ed0f | -3.3502 | -45.4223 | 2024-11-30 08:50:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 33f4598d-36de-38e2-8477-fa93a02a62e0 | -3.3316 | -45.423 | 2024-11-30 08:50:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 109.2 |
| e2d3e349-3303-3b3f-b736-ba58aa8c6cbb | -3.3316 | -45.423 | 2024-11-30 09:00:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 99.8 |
| fb90cc4b-a19a-3627-ab69-3afed003903e | -3.3317 | -45.4005 | 2024-11-30 09:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 7072dfc0-1042-3718-9d87-0284177a68a7 | -2.9606 | -45.2574 | 2024-11-30 09:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 8134e64b-e9ec-3547-ab42-f576a03c4e79 | -3.3502 | -45.4223 | 2024-11-30 09:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 460d98de-84e9-322c-a998-eff7cc1e9e60 | -3.3503 | -45.3998 | 2024-11-30 09:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 09bc7b92-bfcc-320b-82e4-93bc769dd6d9 | -3.3316 | -45.423 | 2024-11-30 09:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 692dd3da-e4a3-398d-9d56-b83fc5051142 | -3.3317 | -45.4005 | 2024-11-30 09:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 95942e2c-f80f-3e4a-b2f2-9db40a1316a9 | -3.3316 | -45.423 | 2024-11-30 09:20:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 620d62f5-3d7f-316b-ad56-efb48238643b | -3.3502 | -45.4223 | 2024-11-30 09:20:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 18308a61-da88-3e5c-86ef-c91cf478d279 | -3.3503 | -45.3998 | 2024-11-30 09:20:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 6ac47a5e-ed9f-3765-994c-627b9f9d153a | -2.756 | -45.2871 | 2024-11-30 09:30:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 01dc2a4b-0a8d-37a6-8f1a-e584be994cc0 | -3.3502 | -45.4223 | 2024-11-30 09:40:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 95.1 |
| d2a7d8ed-a84b-3fcf-83ec-05ca08b4a056 | -3.3503 | -45.3998 | 2024-11-30 09:40:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| c51b1f27-8daa-3374-912a-f49f913dbd93 | -4.0924 | -45.7252 | 2024-11-30 09:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 154.2 |
| 98e70b66-5583-3191-bdd7-308ee6922eca | -4.1112 | -45.7018 | 2024-11-30 09:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 165e344d-3561-338f-bdc3-61a0e180314c | -3.3502 | -45.4223 | 2024-11-30 09:50:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 400ba0a1-195b-3a46-a45b-1139adefc335 | -3.3503 | -45.3998 | 2024-11-30 09:50:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 0085054f-5ed5-3c02-9eb8-f84502a52898 | -4.0926 | -45.7028 | 2024-11-30 09:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 189.9 |
| 73f39f2f-5cf8-33ec-a003-9d7ece1a400e | -4.1111 | -45.7242 | 2024-11-30 09:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 86.8 |
| ce118585-618f-39fc-a9bd-e9e50215c26d | -3.3502 | -45.4223 | 2024-11-30 10:00:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 114.2 |
| e414e2f0-fe0c-34ef-8d49-c49aec4413c4 | -3.3503 | -45.3998 | 2024-11-30 10:00:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 115.8 |
| b33c4107-b164-3f93-9666-ac5243862932 | -3.053 | -45.3665 | 2024-11-30 10:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| ea95f2d7-28a1-3eb7-b245-910c90588d65 | -3.0529 | -45.389 | 2024-11-30 10:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 41e11c5d-3fc7-3555-a7b5-5fac4ef1c64c | -3.3503 | -45.3998 | 2024-11-30 10:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 112.1 |
| c833e174-bea3-3f69-984c-115140627603 | -3.3502 | -45.4223 | 2024-11-30 10:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 2a19daba-4ceb-3189-a041-80cf1ca6abe0 | -2.8683 | -45.1028 | 2024-11-30 10:20:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 82b9a12f-d613-3f01-86b4-ca5be28a4976 | -3.92 | -42.39 | 2024-11-30 11:00:00 | MSG-03 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d3dfc2ed-574e-3361-94fe-b49158c17390 | -3.92 | -42.44 | 2024-11-30 11:00:00 | MSG-03 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2bee1ab2-9336-32fa-a2d0-744d5fc1be6c | -3.92 | -42.39 | 2024-11-30 12:00:00 | MSG-03 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b70b101d-d3d0-3573-b890-d4985eaf7997 | -3.92 | -42.44 | 2024-11-30 12:00:00 | MSG-03 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7b949815-cdcf-397a-a2c0-a122e99c79fa | -3.34 | -42.05 | 2024-11-30 12:00:00 | MSG-03 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 35c9a10d-a562-3cce-a8b7-9b253c3183da | -3.37 | -42.05 | 2024-11-30 12:00:00 | MSG-03 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cbc54fca-69df-3bdb-94d2-d479e7149a72 | -3.37 | -42.09 | 2024-11-30 12:00:00 | MSG-03 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 781e4bba-849b-3b35-8351-fda12133f373 | -3.99993 | -43.2564 | 2024-11-30 12:14:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b8762d71-b3da-36b8-ac00-312bd09b37f7 | -5.45147 | -42.15286 | 2024-11-30 12:14:00 | TERRA_M-T | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| bbf292b1-4eeb-3c4c-adee-e0d6adf79755 | -6.80379 | -37.96901 | 2024-11-30 12:14:00 | TERRA_M-T | SÃO DOMINGOS | PARAÍBA | Brasil | 2513968 | 25 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 09cbc0d9-9f13-35d6-be82-a5d5ec98507b | -6.94595 | -42.77518 | 2024-11-30 12:14:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 56.3 |
| 1e11b9be-2c30-3ea1-b22c-646513fadcce | -6.19334 | -39.83937 | 2024-11-30 12:14:00 | TERRA_M-T | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 41c698f1-67d8-3c42-a8e8-aae3daf88668 | -3.11561 | -41.14944 | 2024-11-30 12:14:00 | TERRA_M-T | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 1277fc67-4dcd-3da0-b7f8-808dc917682c | -6.94741 | -42.76547 | 2024-11-30 12:14:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 28.0 |
| d62b17c5-bcc7-333b-8985-cf0d3eb8d4d1 | -3.4374 | -42.09587 | 2024-11-30 12:14:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| 0fae10ef-934f-3461-bc42-2c578ce63523 | -3.36918 | -42.06017 | 2024-11-30 12:14:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| 8f50b15a-0c01-3181-bfa5-11c608f70b13 | -3.23879 | -41.37764 | 2024-11-30 12:14:00 | TERRA_M-T | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 4ba910a0-cb01-393d-b55c-23f759da3eb1 | -3.57664 | -42.16204 | 2024-11-30 12:14:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 52.5 |
| 8a66e241-b279-3df7-9731-2a0915be9b4c | -3.37974 | -42.18172 | 2024-11-30 12:14:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 7d69bfc6-996a-3d42-af1b-c9fd539d198f | -6.11332 | -42.61147 | 2024-11-30 12:14:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 7d7f4513-9d51-3c0a-b499-8b0ed71b0756 | -6.41232 | -38.28165 | 2024-11-30 12:14:00 | TERRA_M-T | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 30f9a225-ba6b-3732-8917-41101e41f1e2 | -3.6811 | -42.57742 | 2024-11-30 12:14:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 31.8 |
| 4c97bb25-1a3f-3daf-8abb-2f97795125ab | -3.52385 | -42.13459 | 2024-11-30 12:14:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 59.4 |
| d66cdfd8-5ff0-31b7-a75a-570fe4460cf6 | -7.03638 | -38.77269 | 2024-11-30 12:14:00 | TERRA_M-T | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| b8570219-f124-3d35-bcd4-76f7868f890a | -6.95837 | -40.35787 | 2024-11-30 12:14:00 | TERRA_M-T | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 247c5d87-29e8-3aa5-ac97-e37c69530b18 | -6.41376 | -38.27126 | 2024-11-30 12:14:00 | TERRA_M-T | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 61.2 |
| 8e2fed44-8824-393d-8348-14ad18d20dd5 | -4.55801 | -43.57647 | 2024-11-30 12:14:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3857d239-53dc-337a-92f8-eb53c962f38c | -3.35849 | -42.06857 | 2024-11-30 12:14:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 322.5 |
| 05d598d2-23c7-3826-9e75-1542e217b10b | -3.69163 | -42.31174 | 2024-11-30 12:14:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 96ea0af4-1d48-38a2-a3c7-f5741096de7b | -3.57022 | -42.14119 | 2024-11-30 12:14:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 39.7 |
| cc69e214-6c6c-3435-a8fa-ea3ce049658e | -4.69654 | -42.38307 | 2024-11-30 12:14:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 3f16dde3-23bb-32a9-863a-54c841435892 | -4.86536 | -41.30304 | 2024-11-30 12:14:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 4013b508-4a6c-3642-8ec2-8cc84cb39c74 | -5.65089 | -39.69877 | 2024-11-30 12:14:00 | TERRA_M-T | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| cdd89657-674e-3661-aee2-d3b0a75a690f | -5.97289 | -36.35453 | 2024-11-30 12:14:00 | TERRA_M-T | CERRO CORÁ | RIO GRANDE DO NORTE | Brasil | 2402709 | 24 | 33 | nan | nan | nan | Caatinga | 18.8 |
| a6cbc890-33b8-3a87-9abe-911d4c91de92 | -3.91001 | -42.40602 | 2024-11-30 12:14:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 214.0 |
| 797e1ce8-fd1c-346e-bb09-f3534b5bff87 | -3.80601 | -42.48705 | 2024-11-30 12:14:00 | TERRA_M-T | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 46aa63a5-d5fe-3b24-b101-3569d15b6094 | -7.25637 | -37.94956 | 2024-11-30 12:14:00 | TERRA_M-T | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 9.9 |
| caf65868-8e8a-3df8-b088-5c52c760728c | -2.94958 | -45.71961 | 2024-11-30 12:14:00 | TERRA_M-T | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b4b02fdc-7914-3c50-987b-d598d62059c0 | -3.80749 | -42.47693 | 2024-11-30 12:14:00 | TERRA_M-T | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5c316164-28f0-363b-bae7-1a201eb538d7 | -4.88444 | -41.29682 | 2024-11-30 12:14:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 09e01729-c32e-3792-bdcc-821e34e08d11 | -4.86667 | -41.29412 | 2024-11-30 12:14:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 35.9 |
| 5b2a4108-41b3-32dc-bca7-8c6a264e5da0 | -4.87816 | -41.27762 | 2024-11-30 12:14:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 13c6b233-3ef2-3247-b65d-a522df82392f | -4.5614 | -43.55363 | 2024-11-30 12:14:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 695a205d-d057-3bd9-9fab-1d9df31a56e9 | -3.59073 | -40.48675 | 2024-11-30 12:14:00 | TERRA_M-T | ALCÂNTARAS | CEARÁ | Brasil | 2300507 | 23 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 69ccad16-3477-3f93-b87f-38f74cf43a5e | -4.13209 | -42.14953 | 2024-11-30 12:14:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| b0f46427-16ed-3589-ba6b-ff88edebb414 | -3.90855 | -42.41599 | 2024-11-30 12:14:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1219.3 |
| 71e2930f-2716-3144-a66e-84e379494116 | -3.41186 | -42.02669 | 2024-11-30 12:14:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| f5b6cdc6-c1af-3d15-81cc-25fe80bc2e3f | -3.36775 | -42.06987 | 2024-11-30 12:14:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 183.8 |
| 4d1d94ad-279d-3ca0-b380-b5a27a475710 | -3.3214 | -41.69568 | 2024-11-30 12:14:00 | TERRA_M-T | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 1ec4e8e7-1dbb-3751-b396-4aa0cfb08a62 | -3.3941 | -42.08359 | 2024-11-30 12:14:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |


[Clique aqui para ver as próximas entradas](README135.md)
