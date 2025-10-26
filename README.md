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
| db87cf5d-4e6f-3890-a89f-2a30fca1672d | -5.1183 | -43.1731 | 2025-10-26 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 0e2d5b01-e38e-366b-9251-2eccb21c92e5 | -4.0345 | -46.0852 | 2025-10-26 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 95.6 |
| f47e1c82-d012-3f45-8de3-5f661aaf0112 | -14.4079 | -48.9123 | 2025-10-26 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 431820c0-d0cc-3ba5-9f5f-4ebcb2f9beb9 | -7.7864 | -43.152 | 2025-10-26 00:00:00 | GOES-19 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 64.9 |
| b0ac057c-6c06-3008-9184-62e1546dbc60 | -3.1093 | -49.4665 | 2025-10-26 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 82fac526-1142-3508-9ed2-00f6be32ff8c | -4.0346 | -46.063 | 2025-10-26 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 202.5 |
| 8ac260a3-1222-3aff-bc4a-d2b387a0330d | -6.725 | -42.0499 | 2025-10-26 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 178.6 |
| 1628eb36-d9e3-39ae-a169-60e9cfc36934 | -3.0909 | -49.4459 | 2025-10-26 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 96398d3d-deab-33e1-858f-d119ef97ac25 | -3.1094 | -49.4453 | 2025-10-26 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| d8b3d2ce-8818-33b2-ba4f-4700ad587014 | -12.5406 | -45.688 | 2025-10-26 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 30b7a853-687e-30f7-a80f-3cae2e09793d | -4.7018 | -46.4508 | 2025-10-26 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 43.5 |
| df5ff74b-4f36-3951-a8a0-fa0e0b98f230 | -14.4074 | -48.9344 | 2025-10-26 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 92.0 |
| f9c68404-e59d-3a50-888d-3d99294c62d3 | -14.4465 | -49.9388 | 2025-10-26 00:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 388ca1b6-40fe-313b-8f3b-9fbe83a3f33a | -2.7754 | -45.1061 | 2025-10-26 00:00:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 80.2 |
| c070fa2e-4b9c-37c2-ba08-9359be76bb75 | -9.4568 | -56.6396 | 2025-10-26 00:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| ac1eea50-667d-3bdf-8dc1-09b418c6faf9 | -6.7252 | -42.026 | 2025-10-26 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 118.9 |
| 88aed6f0-cd58-3449-9376-24bdb478b9e3 | -5.0994 | -43.1977 | 2025-10-26 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 248.6 |
| 46a171c7-fbfc-3c4b-b5e5-42fd1373cf79 | -2.7569 | -45.0842 | 2025-10-26 00:00:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 121.1 |
| bc555a77-f0a8-3ebf-ba2e-f9daef93eb58 | -4.016 | -46.0639 | 2025-10-26 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 6fd4eb83-9a65-3b42-b3da-afd33e33a542 | -6.1707 | -49.064 | 2025-10-26 00:00:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| d3615d92-81f4-3c06-9202-800924b59431 | -5.1181 | -43.1964 | 2025-10-26 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 241.1 |
| 5e267a64-174f-3f3b-ab8a-68fee43279fc | -5.0996 | -43.1744 | 2025-10-26 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| db579f2a-da68-3494-bb65-81a353240551 | -14.9037 | -52.4779 | 2025-10-26 00:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 76b339ce-da55-345b-9dba-936f8fafaebd | -2.7755 | -45.0835 | 2025-10-26 00:00:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 148.6 |
| 222fb04b-e9d5-3825-b216-7aef113f7f93 | -5.0992 | -43.2211 | 2025-10-26 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| c91d1fb8-968c-39a1-9b70-1284352e648e | -6.6873 | -42.0535 | 2025-10-26 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| c8633367-5c02-386f-b0c6-655bdcb12389 | -4.7204 | -46.4497 | 2025-10-26 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e6adfe98-0b47-3b58-8420-e4c8db79167a | -11.738 | -50.2295 | 2025-10-26 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 9c5ac03c-7af9-33de-848e-09dba4749656 | -4.702 | -46.4286 | 2025-10-26 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 82be7e09-a8bd-341c-8582-9232ed77258a | -6.1706 | -49.0855 | 2025-10-26 00:00:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 7e73d0bf-8f26-37f4-9234-c69202907bc8 | -4.8397 | -42.911 | 2025-10-26 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 9c065bd4-6e63-3a3e-b18d-36ac407e3368 | -14.4267 | -49.9635 | 2025-10-26 00:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 57451561-99c0-35fa-9709-f045b06883c5 | -4.7206 | -46.4276 | 2025-10-26 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 7643b92c-dfcd-37c7-926b-e1468380700e | -9.4382 | -56.6409 | 2025-10-26 00:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 6d379158-bef4-3ec2-9a03-de5e9484e363 | -14.4461 | -49.9606 | 2025-10-26 00:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 7c8fb0d1-e54d-3fd0-8f2c-a55d933b1477 | -5.118 | -43.2198 | 2025-10-26 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| a03f4be3-71ac-3741-9f64-3a2460bd9573 | -11.7377 | -50.2511 | 2025-10-26 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| c409191b-618e-3952-ae89-e0aa311e8996 | -6.7064 | -42.0278 | 2025-10-26 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 194.9 |
| 447f4e60-e94b-3227-9a30-b6d38ac2501f | -2.7568 | -45.1067 | 2025-10-26 00:00:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 19c9a9ac-19c0-3449-bffd-55bd6413273e | -3.0908 | -49.4671 | 2025-10-26 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 1dcfab8d-c644-3e9a-9146-b7606267c9c7 | -12.5213 | -45.6909 | 2025-10-26 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 85950c02-ff04-3f6a-b1e2-2c37d3f6af2f | -6.7061 | -42.0517 | 2025-10-26 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 290.5 |
| c364a251-8202-3dc3-9bca-ad7f9a8aaa3b | -5.2266 | -48.5192 | 2025-10-26 00:00:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 2e573bdc-5632-3158-9ba7-6b9a4e204f5f | -3.0908 | -49.4671 | 2025-10-26 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 9dc1abb2-d516-399d-9f63-4179bc1d9d48 | -4.7206 | -46.4276 | 2025-10-26 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 9bde76b3-2ef1-34e9-b89f-ff3af4039ca6 | -6.6873 | -42.0535 | 2025-10-26 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 65ac5e48-2ada-324c-b8d7-9ca199e838ea | -4.702 | -46.4286 | 2025-10-26 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 122.0 |
| e8b8b002-9342-3cc1-9470-907c6c9e508a | -5.1181 | -43.1964 | 2025-10-26 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 175.2 |
| bd1c5722-6b1f-34a9-b91e-f81c9ee87d2b | -3.1093 | -49.4665 | 2025-10-26 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e4dfd69b-9d25-3508-8086-6fcb614af9cd | -4.0346 | -46.063 | 2025-10-26 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 156.7 |
| ad44f445-7283-393d-a288-00ee037ceb2f | -9.4568 | -56.6396 | 2025-10-26 00:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 57620025-632b-3fb4-aa9f-9f1c85a16b51 | -20.8973 | -49.0191 | 2025-10-26 00:10:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.4 |
| bc79b08d-f072-3b9f-aea1-0bc28c48be2b | -5.1183 | -43.1731 | 2025-10-26 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| b45ce002-a90e-3a7e-aca0-e555041ac69f | -2.3178 | -48.5717 | 2025-10-26 00:10:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 03b13331-adfe-3107-9f47-685db18b7d7c | -5.0994 | -43.1977 | 2025-10-26 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 254.7 |
| 13f34c8d-d238-36ad-a819-e1d044fdfc65 | -11.7377 | -50.2511 | 2025-10-26 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| ce0a9654-7a36-338b-9775-ada5d13fa24c | -4.7204 | -46.4497 | 2025-10-26 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 6adc456d-36b5-3d30-9186-3d8bfa2b6c00 | -3.1094 | -49.4453 | 2025-10-26 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 39333e18-bbac-3769-add1-028f2dc98370 | -2.7569 | -45.0842 | 2025-10-26 00:10:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 90.7 |
| a11f5360-8bd9-322c-be07-9fa51cbf0b71 | -20.8774 | -49.0006 | 2025-10-26 00:10:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.8 |
| c9605355-f6c5-3d90-bf08-89669ef9c371 | -2.7754 | -45.1061 | 2025-10-26 00:10:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| baddaeab-4579-363c-813c-76c941d9d6b5 | -20.9185 | -48.9913 | 2025-10-26 00:10:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.2 |
| a8790ce0-08d7-3754-8cc8-e175ceb75d4e | -20.878 | -48.9774 | 2025-10-26 00:10:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 43.8 |
| 24620c8c-46e2-396d-b62c-c4080a4eb878 | -2.7568 | -45.1067 | 2025-10-26 00:10:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 2ee8add7-341b-38a6-98d9-7b52fab0f3cd | -4.016 | -46.0639 | 2025-10-26 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 49.8 |
| b32b73a0-1782-346d-b8e3-0b06fb798470 | -14.9037 | -52.4779 | 2025-10-26 00:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 59bf8d7c-e8d1-3c41-a6c7-f1cd52cc1a61 | -5.6916 | -48.4921 | 2025-10-26 00:10:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 97fefebb-b3c6-3f49-9d02-845f5b1a0b19 | -14.4465 | -49.9388 | 2025-10-26 00:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 9d643a4f-630d-341c-a980-fc6f477190af | -4.7018 | -46.4508 | 2025-10-26 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| c9b3231e-20c9-3945-8ead-9a27fce5f594 | -5.0992 | -43.2211 | 2025-10-26 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| afeaeda5-af18-3e89-b268-790e602f67f2 | -14.4461 | -49.9606 | 2025-10-26 00:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 68635233-79eb-384f-859e-aea17c75e385 | -6.7064 | -42.0278 | 2025-10-26 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 206.8 |
| 7ab90091-887b-380f-afbf-dc839dff0e8c | -20.898 | -48.9959 | 2025-10-26 00:10:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 496.0 |
| 9801185f-58ec-3cc7-870a-12a870b76e1b | -5.118 | -43.2198 | 2025-10-26 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 9f3bb4b6-8047-3f5f-b277-3b9fb4c65cb8 | -6.1707 | -49.064 | 2025-10-26 00:10:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 582852ff-17ab-397c-8f5c-2a83dac9444f | -20.8986 | -48.9728 | 2025-10-26 00:10:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 162.4 |
| 27381f0e-b419-302e-a945-c11c25726b7e | -6.7061 | -42.0517 | 2025-10-26 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 266.0 |
| 2fbbebbd-859f-3e99-83ef-82b55b3195fc | -2.7755 | -45.0835 | 2025-10-26 00:10:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 96.1 |
| ec37f132-1ea6-3714-835d-ca6932c4a512 | -9.4382 | -56.6409 | 2025-10-26 00:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| e9e6dd14-fc53-36d8-b800-c674257a9993 | -3.0909 | -49.4459 | 2025-10-26 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| c1fddf8b-607a-3834-9e6c-222153002529 | -5.0996 | -43.1744 | 2025-10-26 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 30293984-e098-3b39-8acf-6897d13651f8 | -6.7252 | -42.026 | 2025-10-26 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 5e93f3a4-5d45-3fcd-b8dd-deb3a4eb2297 | -4.0345 | -46.0852 | 2025-10-26 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| b6f6c05d-c03b-36c7-8cdd-74f8d23a4647 | -6.725 | -42.0499 | 2025-10-26 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 134.7 |
| c964182f-8b5a-3b87-b7d5-c40bc71100d7 | -3.8727 | -52.1948 | 2025-10-26 00:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 13b3e470-208e-365f-8e8e-4a3be1799735 | -4.7204 | -46.4497 | 2025-10-26 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| d2d56744-48da-34c3-ae8c-5e9504db7b1b | -4.0346 | -46.063 | 2025-10-26 00:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 163.2 |
| 783c1a93-ef02-30ec-ae5b-8b75c1832547 | -14.9037 | -52.4779 | 2025-10-26 00:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 9ef45675-19df-3290-8245-69aacb2f255e | -5.0992 | -43.2211 | 2025-10-26 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| b6225a6d-41b7-38a3-9746-d20f44a973a6 | -2.7754 | -45.1061 | 2025-10-26 00:20:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 019cb95c-f9ff-358b-a538-6e8ec984e853 | -6.7061 | -42.0517 | 2025-10-26 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 241.7 |
| 558de28e-5b43-35e8-bdb0-6cbf0be2cc8f | -2.3178 | -48.5717 | 2025-10-26 00:20:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 9f3df5c8-07c3-3e40-8955-1c6d808002c4 | -6.725 | -42.0499 | 2025-10-26 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 666cf461-2b46-37eb-8b22-8e5d6af16511 | -5.6916 | -48.4921 | 2025-10-26 00:20:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 191.5 |
| dea5b910-0096-3b83-89a0-18c31041bc6a | -2.7569 | -45.0842 | 2025-10-26 00:20:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 86.9 |
| a2d44773-f21e-3788-b748-2aa2884e1687 | -9.4382 | -56.6409 | 2025-10-26 00:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 82dfd843-2822-3e95-a3cc-3b8f97aa1a8a | -6.7252 | -42.026 | 2025-10-26 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| ef7d5753-5783-3bc8-96ce-f4699e7cb01b | -5.118 | -43.2198 | 2025-10-26 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ce247a44-1e60-3450-b8da-80150cfb7063 | -5.0994 | -43.1977 | 2025-10-26 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 299.2 |
| 741fa249-9b9b-34f1-9456-f5a1a6e966bf | -5.6917 | -48.4705 | 2025-10-26 00:20:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |


[Clique aqui para ver as próximas entradas](README2.md)
