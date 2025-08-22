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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03bdb841-2c95-33bc-bd27-e11ea2ea7bd4 | -14.8348 | -47.9311 | 2025-08-22 13:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 137.9 |
| cd50cda4-c19f-3409-bc32-b044d5c0fa77 | -7.8538 | -46.9969 | 2025-08-22 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 541c6ed8-01e7-311c-b12c-c0a319b48423 | -13.3966 | -46.2406 | 2025-08-22 13:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| a689408b-3c32-3a43-8d3c-fc62f11285e1 | -7.6366 | -46.2823 | 2025-08-22 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 157.3 |
| ad231592-81ce-3f0a-a292-a1627e48a611 | -7.6559 | -46.2358 | 2025-08-22 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| b87a5f0d-21e7-3f01-a47f-23db589b6af5 | -7.6369 | -46.2599 | 2025-08-22 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 44b63a57-524b-3988-9651-b2a47e4a9ab1 | -12.9921 | -45.2252 | 2025-08-22 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 200.1 |
| 274886b0-052e-3bda-ab46-7e55334cc696 | -7.0352 | -44.6396 | 2025-08-22 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 221ec970-3a63-3cb2-8b8d-555b9c7b65d0 | -20.2287 | -46.7066 | 2025-08-22 13:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 117.9 |
| be30ad37-d61f-3252-a976-d24b9a428ae1 | -7.8726 | -46.9952 | 2025-08-22 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 9fadd81a-2627-3aa2-87cd-ca7e1da4425b | -14.7717 | -45.4055 | 2025-08-22 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| f87610cf-7ff8-397b-a959-ba248284f67e | -20.2492 | -46.7017 | 2025-08-22 13:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 237.6 |
| dd7d960e-6334-368c-af27-6e6d97b019dc | -5.7784 | -44.7642 | 2025-08-22 13:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| ded0f699-3a28-3142-a786-9b77efda799b | -7.6296 | -45.2464 | 2025-08-22 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 75d20f6a-8520-3c43-aaab-32bc77b5e59f | -11.3275 | -44.9468 | 2025-08-22 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 97dc0b1f-6806-3ba8-99e9-ba971a941377 | -7.6181 | -46.2616 | 2025-08-22 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 36e0d5d2-bd7d-3fc0-8077-77cf5c1623c8 | -8.3009 | -47.3094 | 2025-08-22 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a45e3ac1-9805-3031-9e75-0704330320f2 | -12.3133 | -49.9881 | 2025-08-22 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 46205832-5fc2-368c-8f6e-bcbfca5a9db9 | -8.3011 | -47.2873 | 2025-08-22 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| b7d63698-076f-3ce7-94a8-6f3fe3402ab6 | -12.3133 | -49.9881 | 2025-08-22 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 215.9 |
| b6126506-b91a-36f4-9c59-092b9fef49c6 | -7.6559 | -46.2358 | 2025-08-22 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 3ee8e3b2-7d60-3cd2-9f5c-ac98f369a004 | -6.5196 | -45.5464 | 2025-08-22 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 348.5 |
| 46b711ea-d292-3d2f-897b-777a6f8d0e01 | -8.7759 | -45.4486 | 2025-08-22 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 5ffe9c7c-c955-3632-87c3-32b537f5f196 | -10.8757 | -50.8376 | 2025-08-22 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| bd7eec32-e365-3a9d-8187-1a86a55201c9 | -6.5386 | -45.5224 | 2025-08-22 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| c70cf0ad-4ba2-31c7-91e1-981d201dce8f | -7.0352 | -44.6396 | 2025-08-22 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 5183b86a-cd01-3cf2-831f-65aee206486d | -7.6369 | -46.2599 | 2025-08-22 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 206.6 |
| 06e65bc6-c0d3-32f7-b27b-c9874c11b00a | -14.7694 | -56.0335 | 2025-08-22 13:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| aacb7e15-b117-3716-80d6-6d1ee910817c | -11.3084 | -44.9495 | 2025-08-22 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 103c30e8-18d8-3db3-8fb0-1c69046e8ff6 | -7.8726 | -46.9952 | 2025-08-22 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 4ec20b85-dfa7-3212-af98-143d3855533f | -11.3275 | -44.9468 | 2025-08-22 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 204.7 |
| d7ad90fd-cc1f-3ca3-abcb-d97d4b122a29 | -7.6366 | -46.2823 | 2025-08-22 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 488.3 |
| 4da18121-a71f-3e94-ac55-bdeca70cd2e8 | -7.6296 | -45.2464 | 2025-08-22 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 56daf7c4-e52c-3e19-af2c-507f4ea352bb | -14.6519 | -54.875 | 2025-08-22 13:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a1f29ca4-0cea-3762-9af4-f2510b53785c | -7.6484 | -45.2446 | 2025-08-22 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 567df03f-7365-318a-be6d-80a969112253 | -7.1662 | -44.6736 | 2025-08-22 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 8407f0e1-1bb1-32ce-a649-8050c1241217 | -20.2492 | -46.7017 | 2025-08-22 13:40:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 163.7 |
| c5d3040d-5e7d-3dc4-b7cc-71ef93bb23ef | -12.3129 | -50.0097 | 2025-08-22 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 070f3801-cb3d-3e66-918d-cd3ac8c8cc0f | -8.4588 | -48.2595 | 2025-08-22 13:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 262acad3-4a7c-32c7-acde-9c07e5cecfe2 | -6.4449 | -45.5298 | 2025-08-22 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 5500258c-6de2-3bba-ac1c-117304003c40 | -14.8348 | -47.9311 | 2025-08-22 13:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 237.7 |
| 316a0488-17f2-3ee2-bb47-35b6e22b1169 | -6.7319 | -43.1379 | 2025-08-22 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 3f54b8b6-3dac-3b89-9783-fb662ed9ac5d | -14.7501 | -56.0356 | 2025-08-22 13:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 9102c772-1114-365d-85b8-22608341d965 | -6.5199 | -45.5238 | 2025-08-22 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 11d159c0-3439-331f-ba8e-9064eaf7862a | -12.9925 | -45.202 | 2025-08-22 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 53d3b1ec-c206-32e4-988f-0aad47023dcb | -7.6181 | -46.2616 | 2025-08-22 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 281.4 |
| bffefd9a-345c-36e5-bf1c-8fd55588a51f | -12.9921 | -45.2252 | 2025-08-22 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 202.1 |
| bf76fd26-44df-3d0b-a1df-2e52ecce224f | -7.8538 | -46.9969 | 2025-08-22 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| bfee3b05-61d9-3ebd-b5ee-d5909a464bfb | -6.436 | -44.5306 | 2025-08-22 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 9e5b0e49-8e6b-3af7-b776-a917925f77cd | -14.6713 | -54.8728 | 2025-08-22 13:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| df4bc44f-5822-369b-bd50-9ea8e7a53bc8 | -14.5257 | -47.8469 | 2025-08-22 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 80ce786a-fc7b-3c16-b0cc-5926f6e77a11 | -14.596 | -54.7575 | 2025-08-22 13:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 9b12ad76-1137-3656-9d0e-697162773a7d | -8.7567 | -45.4733 | 2025-08-22 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 363a36af-2233-3b72-9b8c-9a1d5886d04f | -5.7979 | -42.6295 | 2025-08-22 13:40:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 115.7 |
| 94d7236b-ea35-3c84-a3ce-9fe419316ec0 | -14.7717 | -45.4055 | 2025-08-22 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 132.2 |
| a2720033-1e6d-3a41-a9a6-fe02b3f05c95 | -14.7712 | -45.4289 | 2025-08-22 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| f53a064d-3e50-31b7-9b20-f8d8142fdf2b | -12.3133 | -49.9881 | 2025-08-22 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 170.9 |
| bd9685bd-6db5-3fb4-aa69-b6219223672e | -20.2287 | -46.7066 | 2025-08-22 13:50:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 5b57d8d4-b979-327f-8812-fe6bf2308f42 | -8.4776 | -48.2578 | 2025-08-22 13:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 5b5201fc-2900-3cdf-9cf2-947dc3ee109d | -11.3275 | -44.9468 | 2025-08-22 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 53aefb82-3864-3c5c-8406-5ed0259850fe | -5.7784 | -44.7642 | 2025-08-22 13:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 42b4d245-2c8b-3339-aae5-eb4d308aedf0 | -11.3084 | -44.9495 | 2025-08-22 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 8a4a9bfa-d5d2-3332-8594-52a3c91b19d3 | -14.8348 | -47.9311 | 2025-08-22 13:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 40239911-0dc2-35fb-a5d8-473bb1d83e84 | -6.9649 | -44.1864 | 2025-08-22 13:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 38568174-e115-3cae-b4b2-3ea0fb8c6084 | -7.6366 | -46.2823 | 2025-08-22 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 0ce74a1f-9ae6-32e4-8855-1fdebe4a1e69 | -12.9921 | -45.2252 | 2025-08-22 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 182.3 |
| e38faa23-01f1-33a8-b575-b8e2e7b777fe | -12.2938 | -50.0121 | 2025-08-22 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| a54ca993-ff0e-3298-a25c-a88d5cfbaa6f | -8.3011 | -47.2873 | 2025-08-22 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| f1719243-f364-3dd8-a1fb-fa14f07c5623 | -6.5199 | -45.5238 | 2025-08-22 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| e38346af-fc09-3535-beee-c5dd2bc64900 | -6.539 | -45.4772 | 2025-08-22 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 42dd433c-61de-33aa-80e9-d45fa42de87f | -20.2492 | -46.7017 | 2025-08-22 13:50:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 320.2 |
| 423f68c0-ff83-36c8-abf3-76fa6a2299b8 | -8.4588 | -48.2595 | 2025-08-22 13:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 0a9c4c3b-ad59-3c1b-b6d5-38aa3a13dfe1 | -7.1662 | -44.6736 | 2025-08-22 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 10d96eb5-1b23-39ba-81c2-58dbb5d2afe2 | -7.6296 | -45.2464 | 2025-08-22 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| e358aa9d-0cc5-3385-bf19-08ccb9ef0be2 | -10.8757 | -50.8376 | 2025-08-22 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 34472a6d-0ea5-3e48-b543-18129f6b0e35 | -6.4362 | -44.5076 | 2025-08-22 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 2f1f2dcb-70bf-34b4-b7dd-69b57c979a4f | -7.6484 | -45.2446 | 2025-08-22 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| cdefe27f-fb0e-3463-98c9-5be02e989ed7 | -13.3966 | -46.2406 | 2025-08-22 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 66efe1dc-c8c8-3de5-ad82-633df7bc813d | -7.0352 | -44.6396 | 2025-08-22 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 559e5897-9518-3fd2-80e1-3a165ccc4430 | -12.3129 | -50.0097 | 2025-08-22 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 30459e81-a842-372f-a01e-7e96b9eb429d | -10.876 | -50.8163 | 2025-08-22 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 94c5b06c-95c2-38cd-88bd-2d3ac1ac5bd5 | -14.7501 | -56.0356 | 2025-08-22 13:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 155.0 |
| cd7822f5-98b6-38dd-a450-f7e31b2bb98c | -5.7782 | -44.787 | 2025-08-22 13:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 152.1 |
| a575ef35-3a5f-35f6-98f9-828c772b8d1c | -6.4449 | -45.5298 | 2025-08-22 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| d0d0b58a-c0c9-376c-a731-151258f5d51b | -14.596 | -54.7575 | 2025-08-22 13:50:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 121f5606-5756-3091-8685-c04f871ee17d | -6.5386 | -45.5224 | 2025-08-22 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 177.9 |
| fb437207-3925-35a8-aa19-69e78565b87e | -7.6181 | -46.2616 | 2025-08-22 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 611007ec-c686-3051-9bf6-fe8ba175d112 | -6.0058 | -44.4501 | 2025-08-22 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| b5e7cec0-4583-35af-9713-da82f0295171 | -7.0354 | -44.6167 | 2025-08-22 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 9028e9d2-4659-3fab-b102-f2b7a09c9dc8 | -7.6486 | -45.2218 | 2025-08-22 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 9cee4360-6df7-3982-b829-360c0b4e3639 | -6.5196 | -45.5464 | 2025-08-22 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 267.5 |
| 4424013a-7983-3bcf-b35e-f95766e2c386 | -12.9925 | -45.202 | 2025-08-22 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 9fc59f1d-b261-3567-8e38-f53bbc41dad2 | -14.7717 | -45.4055 | 2025-08-22 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 2e2b1a70-d062-3056-934f-a28d3728020b | -14.7694 | -56.0335 | 2025-08-22 13:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| f20f5554-0d78-3248-b38a-f77d5ffcebff | -6.5573 | -45.5209 | 2025-08-22 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 175.5 |
| cd13b693-e235-3d2d-942b-17ca8d26409a | -7.8538 | -46.9969 | 2025-08-22 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 3ac665a3-a025-3db1-9437-f753a14a0c96 | -7.8726 | -46.9952 | 2025-08-22 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 7523ef9d-67ea-3525-81fa-411b90b4b07d | -6.1187 | -44.3955 | 2025-08-22 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 91a9507b-1e66-35c8-8745-db7f2b2db2c8 | -20.2492 | -46.7017 | 2025-08-22 14:00:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 118.0 |
| e0c414c1-ff73-36c1-a554-7d8ce73279b2 | -6.4449 | -45.5298 | 2025-08-22 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 152.1 |


[Clique aqui para ver as próximas entradas](README69.md)
