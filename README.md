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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f184645b-d4ba-3784-93f3-31241aa9cd9a | 1.9044 | -61.1026 | 2026-04-04 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 120b7301-eca9-371c-9225-2089170a2ead | 1.9044 | -61.1026 | 2026-04-04 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d440d89e-ee88-317f-9688-ccc8b034a842 | 1.9044 | -61.1026 | 2026-04-04 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.6 |
| b31ed5a9-9a4c-3855-9d3d-dbe5485311ef | 1.9044 | -61.1026 | 2026-04-04 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 9faf8cbe-32ea-3e8f-882b-ddfd5f0cf0f8 | 1.9044 | -61.1026 | 2026-04-04 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 7d20b699-19e1-3c97-adec-aed0b01121a0 | 1.90456 | -61.09462 | 2026-04-04 01:02:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 6f2395a7-409d-3420-8aca-6f351d34737c | 1.90333 | -61.10352 | 2026-04-04 01:02:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 24b396a5-d267-3133-b8a9-2422fba50385 | 1.9044 | -61.1026 | 2026-04-04 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 590bb473-3091-3ea8-a5ad-5ecceadb98f7 | 1.9044 | -61.1026 | 2026-04-04 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 28af4711-56fe-3a9a-a3ea-58f11126c975 | 1.9153 | -61.079601 | 2026-04-04 01:26:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f4a9c748-41ac-3fbd-975d-0017b773e8d2 | 1.9109 | -61.099098 | 2026-04-04 01:26:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1deb8811-087e-3aa1-9cf4-50958a086ead | -10.2466 | -70.501099 | 2026-04-04 01:59:00 | METOP-C | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3c37b286-8339-3258-a054-476c122e6704 | -9.94748 | -35.97093 | 2026-04-04 03:45:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e61c6196-a789-36cc-a592-8a8c8fe3b298 | -19.1214 | -40.63528 | 2026-04-04 03:47:00 | NPP-375D | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 59d58e5f-5283-3ed9-8f16-5d8ad8523231 | -19.12204 | -40.6333 | 2026-04-04 03:47:00 | NPP-375D | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a53d7976-2816-3aa6-9888-f21084168471 | -21.67882 | -54.14276 | 2026-04-04 04:08:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f2af25a8-b15f-3883-92a0-5c0c7754b8da | -21.67858 | -54.14792 | 2026-04-04 04:08:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6002787c-a8ef-32f4-aa5b-59969a5a59f5 | -18.79736 | -48.54915 | 2026-04-04 04:08:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97ae4bfb-195f-37e1-9225-e8d82ceddf81 | -21.67795 | -54.14659 | 2026-04-04 04:08:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 82f43810-2df0-3144-8aba-23de7a0028bf | -21.67942 | -54.14408 | 2026-04-04 04:08:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07f152b1-8d45-3bfc-b6a7-2ebc16102169 | -27.94925 | -50.93949 | 2026-04-04 04:10:00 | NOAA-20 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 46bad36f-63f5-37fe-81aa-ac1b0e987790 | -5.03156 | -56.19229 | 2026-04-04 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0ffe8d5-bff9-3528-88d9-876884ff81e6 | -5.03066 | -56.19414 | 2026-04-04 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03557c77-9cf8-3790-89ea-68ec4af27473 | -12.64052 | -52.14371 | 2026-04-04 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da0b9785-f845-3eea-96a8-b9e0986b28d8 | -12.64008 | -52.1443 | 2026-04-04 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2678976f-5aad-3099-b194-3851a58fde48 | -13.55941 | -55.27539 | 2026-04-04 04:53:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5661d7cd-118b-3a01-bd66-49e3bbd3736a | -13.55607 | -55.27483 | 2026-04-04 04:53:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 575200e2-425e-3b23-ab9d-ba1b32a520ed | -21.67863 | -54.14548 | 2026-04-04 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f1fa08c2-25d6-345e-b368-cc04009aabf3 | -21.68184 | -54.14495 | 2026-04-04 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 780110df-8485-3012-b653-d00cec3082e8 | -16.30541 | -58.47495 | 2026-04-04 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 049424e3-113e-3840-9ab7-39e476d24763 | -16.30516 | -58.47297 | 2026-04-04 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5911afd2-f242-3d09-a359-e4fc6d0c318e | -21.67898 | -54.14042 | 2026-04-04 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b90b100-4150-36dc-9b70-5595e847cae4 | -18.79602 | -48.54763 | 2026-04-04 04:55:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb9dadff-6418-327a-b12b-b64ec17c97dc | -21.67921 | -54.14151 | 2026-04-04 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fd661136-6c02-3703-ab16-00e52280adde | -21.68241 | -54.14098 | 2026-04-04 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 50bfc4f2-70d1-35ac-b849-a850018acec0 | -21.67841 | -54.14439 | 2026-04-04 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0b7a2ed2-aac5-3e75-b61d-640dbadc7ec6 | -19.89932 | -54.36164 | 2026-04-04 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8eca0005-b615-3904-9292-0a04a447a544 | -17.90563 | -54.13772 | 2026-04-04 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c2a483d-e6a5-3845-9a63-9d23d764206a | -18.21983 | -57.44511 | 2026-04-04 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 92740881-f73c-3b68-a119-7dac79ce8305 | -19.38951 | -53.35878 | 2026-04-04 04:55:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c5eb693-b64d-32fc-a0df-af8c7e13be20 | -23.77556 | -55.33284 | 2026-04-04 04:57:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 985f4fa9-453c-3103-adfc-ae3bcd3bf654 | -27.94954 | -50.94076 | 2026-04-04 04:57:00 | NOAA-21 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3796c8c9-e97c-373d-9cf9-a1306fde6681 | -23.7722 | -55.33225 | 2026-04-04 04:57:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 543bd466-8a12-38f0-9e40-528a39116e01 | 1.90394 | -61.10207 | 2026-04-04 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfc6f5fb-4eb2-3c3e-80e0-1efb7fe67268 | 0.98109 | -59.38475 | 2026-04-04 05:23:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8851e5e-2784-37eb-a985-32f6a7dad485 | -5.03257 | -56.19126 | 2026-04-04 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e40ac5b6-73df-3d91-a976-aa8b73a86ba1 | -13.55574 | -55.27644 | 2026-04-04 05:25:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 866898d5-d2ea-3119-884d-ac8042592850 | -16.30586 | -58.47512 | 2026-04-04 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| a1ad6d47-e4a1-3c20-8ac2-4bd519fd7f9a | -23.77516 | -55.33205 | 2026-04-04 05:27:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 94339c7f-20ae-3721-a738-281a4f8f3311 | -19.89948 | -54.36005 | 2026-04-04 05:27:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53a66144-8381-3f6a-8205-414067156987 | -18.21585 | -57.44631 | 2026-04-04 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 69719c92-b6dd-3dbd-ae5e-93ce1bfa75c3 | -18.21968 | -57.44688 | 2026-04-04 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a3157c6b-21b5-3d4f-912a-040919544757 | -21.67681 | -54.14314 | 2026-04-04 05:27:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39bebcd1-3ebc-33d4-8159-c39120afb5fc | -19.89964 | -54.3631 | 2026-04-04 05:27:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c53f8c4-7d7a-3b07-b819-24d3765f1c32 | 2.04913 | -60.86776 | 2026-04-04 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 990f1dd3-63ce-38c4-994a-f9ffb58b28eb | -14.08077 | -43.69202 | 2026-04-04 11:47:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b22d17c5-1b10-3893-9626-3a13b3687ba6 | -14.07948 | -43.70131 | 2026-04-04 11:47:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b84c012a-ede9-3f40-ac4c-c7a34d8a276c | -27.69155 | -50.27912 | 2026-04-04 11:51:00 | TERRA_M-M | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 83.8 |
| a984bdf5-b4c6-3eec-9fde-d3c564ef6355 | -27.69338 | -50.26777 | 2026-04-04 11:51:00 | TERRA_M-M | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 43.7 |


