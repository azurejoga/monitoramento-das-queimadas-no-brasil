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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3fd4205-a81d-342a-9e58-a10ae6af92a9 | -11.2663 | -54.022499 | 2026-08-29 00:52:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f65e1c41-1a94-38ed-a007-917e61e1f8a2 | -6.9514 | -59.466 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84b166c8-86d0-335e-92b0-ad30912cae5f | -10.4037 | -61.186199 | 2026-08-29 00:52:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 649f8ec1-35ff-33ae-b3f2-01a0277e85ab | -7.3408 | -55.156399 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9db78467-43b0-3d39-82a6-bad6c0ced93a | -11.0273 | -57.233101 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5303045a-0533-34be-bcca-5a9cfacfedd4 | -6.5725 | -56.529301 | 2026-08-29 00:52:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a42ba58a-c06f-351f-977b-e4a91476a0cb | -6.8144 | -59.452801 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ecb09178-f8ea-38eb-927f-e5dd659264b0 | -14.9523 | -56.312698 | 2026-08-29 00:52:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c130d175-8c41-3c4a-9498-2f133b9e5339 | -8.9479 | -63.271702 | 2026-08-29 00:52:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 19347ba4-b2b0-3dba-8282-b55f2e8405c9 | -9.182 | -59.625198 | 2026-08-29 00:52:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d73932c0-1a6b-3784-be90-aca45f14b1b0 | -9.8686 | -60.3004 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2919002e-4f27-3dae-8b6d-89dd31db68aa | -11.0336 | -57.2155 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d57e1c9e-5250-3da4-9b66-333fefff4ead | -23.135799 | -48.659599 | 2026-08-29 00:52:00 | METOP-B | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d80e5171-e921-36cb-ae1f-9584899dc3b2 | -7.2811 | -49.5242 | 2026-08-29 00:52:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbb37c68-7999-3809-a751-f6ef7029fc15 | -9.8758 | -60.2402 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92c9489e-eb62-3589-8261-dce922ee6d50 | -14.931 | -56.3097 | 2026-08-29 00:52:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 12c3de01-8d56-3c21-8f94-4e89ca56004c | -4.1588 | -60.690498 | 2026-08-29 00:52:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5cf0abc-2dc6-3481-b23f-50c837e2975e | -8.678 | -62.830799 | 2026-08-29 00:52:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 865125f4-07a1-3de1-9f28-b95311537ecd | -11.0211 | -57.250801 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3589336-15a8-3793-a4da-edde136aed8f | -11.6182 | -54.5798 | 2026-08-29 00:52:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d25af8a-0eb0-3a42-807c-6cd5abf1b477 | -9.5956 | -55.098499 | 2026-08-29 00:52:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8282475e-5dc8-3b2d-85d9-f609891140ac | -8.5301 | -55.345299 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72323f35-301d-397b-930d-d64a0c81fbb3 | -8.5899 | -54.775398 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1af403c-5556-3e2a-8801-ccb19f3e5b55 | 0.1533 | -60.390598 | 2026-08-29 00:52:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 11a8ab81-f66c-3bd5-8407-263222ba1035 | -6.1196 | -57.683201 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| effb8c37-01d5-34cd-8417-97cbb2ce7816 | -15.5752 | -56.282902 | 2026-08-29 00:52:00 | METOP-B | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0667c92f-4ecc-361a-b75e-caf8bd52ce13 | -6.9379 | -58.9548 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4299f4f3-7c34-3862-8688-48a8d15f7024 | -6.1741 | -57.696098 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f67e965b-4510-3d7b-9e84-5640b72df5ab | -7.4934 | -55.277599 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e144692-7c9b-38d1-a5b8-a7f54f485d26 | -8.5325 | -55.3554 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a080eb9d-5257-389d-928b-6f317eaca637 | -9.1909 | -51.555 | 2026-08-29 00:52:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 243ef3eb-b435-38b9-abfe-cdebe53e2827 | -14.9151 | -56.330101 | 2026-08-29 00:52:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 35c1ef79-be68-381d-b3cd-abcf2c1fa7da | -5.9751 | -57.6824 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0400f85b-5b34-34ba-bafc-2c68156b5ef6 | -7.5105 | -55.306801 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05b47d8c-7f6f-3717-ad9e-4d5996905452 | -14.9328 | -56.317501 | 2026-08-29 00:52:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f5ec3bd-d9c8-327c-bfdb-74de4b06373a | -20.9314 | -57.559799 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3ecf1517-cc73-3ceb-9111-ff5feb17fc32 | -7.4762 | -61.3857 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1011c183-e41c-3de3-8dc5-db9ce4fcb1e7 | -9.8784 | -60.2981 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0fa2d28e-28e0-3d3b-8450-9f0919b8d95c | -6.7718 | -55.668098 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51bf80bc-23c9-39b1-99ac-37cab8bebf46 | -5.8885 | -57.753502 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 782c9207-7bee-342e-9e1e-f2b6cb756143 | -15.6232 | -56.401299 | 2026-08-29 00:52:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b0624fb6-4e65-35a7-8a02-3b50351e71cf | -5.8769 | -57.747601 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7f6e441-491e-3c9f-8690-3a98286b5380 | -6.176 | -57.704201 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e724ac3c-1903-3d07-a22f-d9f149d6abda | -11.0416 | -57.205399 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 008ee036-b468-3702-bd0c-c32fcda0df32 | -7.3506 | -55.154099 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63ed4ca7-ab31-318c-9206-c9521650f673 | -10.8996 | -46.6216 | 2026-08-29 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| ee0c0926-5576-3b31-8648-6410045a34a2 | -7.5137 | -55.3051 | 2026-08-29 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| f66ed2d5-541d-399a-a50f-f91583750391 | -7.5139 | -55.2851 | 2026-08-29 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 34cbc2a8-b812-37c9-b1f8-f3901be37ca3 | -10.4794 | -64.5012 | 2026-08-29 01:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 8a0ec8df-ef1d-38ad-aa03-ab8ea3404327 | -11.0445 | -57.2023 | 2026-08-29 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 768a6653-1643-328f-bfec-8b150f725137 | -6.7884 | -55.6635 | 2026-08-29 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 2e6c8005-581d-38bc-be63-9be054a57939 | -6.77 | -55.6445 | 2026-08-29 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 288a420e-e587-3ab7-99e2-5599da3e855b | -11.0252 | -57.2436 | 2026-08-29 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| fe6923eb-073f-3289-8830-ee6eee3ec507 | -7.2849 | -45.8427 | 2026-08-29 01:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d9e3381d-8988-3558-9f37-aa3bd8581f0c | -8.9613 | -63.279 | 2026-08-29 01:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 93748e7a-3080-3420-90b5-b06b1af5a602 | -5.9079 | -57.7506 | 2026-08-29 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 13314a3c-dec2-3f18-9ea8-2a64f7ea5b19 | -11.0441 | -57.2421 | 2026-08-29 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 8e5f9e51-457d-3ca1-86d4-e7a240a0ce81 | -6.7698 | -55.6844 | 2026-08-29 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 4a5ab32f-8009-3db3-974a-9d9af755df5b | -10.9 | -46.5991 | 2026-08-29 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| d76a4147-f020-32c6-a594-ee58de3b1e49 | -4.3774 | -47.7627 | 2026-08-29 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 8e41fc8d-95dc-3f61-bd25-3aab4320f45c | -5.9078 | -57.77 | 2026-08-29 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| cb2a8453-ba35-3a57-b4bc-f72bf30df78b | -10.4981 | -64.5005 | 2026-08-29 01:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| f0e067a6-03e7-32aa-bfff-9908caa45bce | -4.3588 | -47.7636 | 2026-08-29 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 18a40c0b-6bc0-3461-b640-4f9dee8ab77d | -5.8895 | -57.7513 | 2026-08-29 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 186.1 |
| a1a2b5b9-0a3b-3de4-a1ce-1d4b90c20699 | -6.7699 | -55.6644 | 2026-08-29 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 179.0 |
| bdc9766e-d5ed-3aee-8985-a7ebacbe3ba9 | -5.8894 | -57.7708 | 2026-08-29 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 06b4b3ea-eec9-33c4-beb8-a977103a15dd | -6.7343 | -55.4671 | 2026-08-29 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| f8e89baf-1686-37de-bb4b-7b7a193f0ae9 | -6.7528 | -55.4661 | 2026-08-29 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| fc4946a8-094f-35a1-96b7-8b7b59722ea0 | -11.0443 | -57.2222 | 2026-08-29 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 1f7e25e8-8a22-35bf-b025-dd38558991b0 | -5.4179 | -43.1752 | 2026-08-29 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| a5660392-4492-39b2-895c-4092a50d079d | -8.9428 | -63.2797 | 2026-08-29 01:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 78c2908b-64a2-3eda-a934-79ae761efdb4 | -8.5358 | -55.3629 | 2026-08-29 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| b1100b14-3292-30d5-955e-c7462ed77568 | -7.2847 | -45.8652 | 2026-08-29 01:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| f9aa456c-dc45-3111-a79b-dd12d64d8cbc | -11.0254 | -57.2237 | 2026-08-29 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 94c76582-7fad-3308-a4a3-8632f4d5672e | -10.4795 | -64.4824 | 2026-08-29 01:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 1f28b9ce-f154-304b-9e20-fda6ebbb7c7d | -4.3587 | -47.7853 | 2026-08-29 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| db18f06f-c0d3-3908-bc69-f65321afd72c | -8.5359 | -55.3428 | 2026-08-29 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| e91b6bff-1724-3652-862f-4f83e5e1da4c | -5.8894 | -57.7708 | 2026-08-29 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 2950a3be-8ddd-3b03-b092-898a1dd95323 | -6.7528 | -55.4661 | 2026-08-29 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 964101bd-19da-3a48-9024-203f3aa2e0de | -5.9078 | -57.77 | 2026-08-29 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| de74cbc7-aa33-30b8-a572-3205b361b27b | -7.2849 | -45.8427 | 2026-08-29 01:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6b58f613-174c-38ab-8fb1-4c43cb8febc5 | -6.7699 | -55.6644 | 2026-08-29 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 174.8 |
| cffee20c-e05e-33d5-8594-32b821f7c8c2 | -8.5358 | -55.3629 | 2026-08-29 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7eac9df4-69c2-3dd7-97c1-e33d5f43690b | -5.8895 | -57.7513 | 2026-08-29 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 175.4 |
| f3d26512-a7bf-3296-8f21-e96f5abdb16c | -11.0252 | -57.2436 | 2026-08-29 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| dfa3a2b3-9066-37c8-8aa7-910f29c634c9 | -6.7343 | -55.4671 | 2026-08-29 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 24cafbaa-0c51-3a1f-a81c-c4313f730338 | -6.77 | -55.6445 | 2026-08-29 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 2949d800-9969-361a-82b4-05c313252918 | -10.4981 | -64.5005 | 2026-08-29 01:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2e33ba0b-f3a8-361a-92bc-1897d933be1b | -8.5359 | -55.3428 | 2026-08-29 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| a45f255a-7508-3a4d-9a90-5b23525cbf6e | -11.0254 | -57.2237 | 2026-08-29 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| a7ddfb6d-1292-3c86-826e-11b6829e3906 | -6.7698 | -55.6844 | 2026-08-29 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 09d1c6ac-395c-3e27-9937-7571496e4104 | -11.0443 | -57.2222 | 2026-08-29 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 8861c711-4263-358d-9927-a853b91c4d15 | -6.7884 | -55.6635 | 2026-08-29 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 407b4cab-e078-3d5a-b4fa-96880d0745c0 | -10.4795 | -64.4824 | 2026-08-29 01:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 4e321a5b-cee8-3ba0-a526-b7645a3138d9 | -10.4794 | -64.5012 | 2026-08-29 01:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 52c06567-bea3-357b-8b4b-0fab53306a5b | -7.5137 | -55.3051 | 2026-08-29 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 030f5982-4b81-3542-8694-d784521e820b | -8.9613 | -63.279 | 2026-08-29 01:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 3790f6a1-ac22-3569-b30d-1988b5dd7d67 | -14.2027 | -52.8432 | 2026-08-29 01:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 8950fc6d-cb8e-3d82-be8e-300404daa987 | -7.2847 | -45.8652 | 2026-08-29 01:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| a113674e-1d03-3d7a-b7a4-ec9b2ea1516c | -5.9079 | -57.7506 | 2026-08-29 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |


[Clique aqui para ver as próximas entradas](README13.md)
