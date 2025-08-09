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
| d55ed21f-5023-3e57-9990-def283ad7d91 | -12.4115 | -47.781601 | 2025-08-09 00:44:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4783180-dd32-3125-b0a3-8e75f018475b | -17.5149 | -50.278198 | 2025-08-09 00:44:00 | METOP-C | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| abec90c5-11b6-3881-b5b0-7936576210ab | -19.8113 | -47.058201 | 2025-08-09 00:44:00 | METOP-C | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 68f3813e-47d1-3f4f-952f-0e2807c7cbdd | -4.471 | -48.1175 | 2025-08-09 00:44:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21bc5165-452c-3bdf-96d7-4d93c646fbe6 | -14.3505 | -47.1003 | 2025-08-09 00:44:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 40a336ba-6a6c-3910-915a-7a22127edae1 | -11.7265 | -47.492199 | 2025-08-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84f33e21-66a7-3205-8389-220aa94ead0d | -11.1094 | -50.4841 | 2025-08-09 00:44:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8541e2a1-cc10-3371-ac31-3934bdd62be0 | -13.0486 | -43.844002 | 2025-08-09 00:44:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 697c3d05-fac9-325a-bfe2-4b3be8012731 | -11.738 | -47.497002 | 2025-08-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27039cd0-f714-3e06-b4dd-a88ae328cff2 | -12.0511 | -47.512501 | 2025-08-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6aaac89d-c2ad-3708-93e7-b907908f8870 | -8.9363 | -60.719002 | 2025-08-09 00:44:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90041cb8-757d-3ec2-bc80-1ac0b9f749ac | -4.2958 | -48.0737 | 2025-08-09 00:44:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f49a442-7cb0-3bfb-b98d-b8dc43041dd2 | -6.5803 | -44.578201 | 2025-08-09 00:44:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d5de707-ed68-3d8c-9259-492f6fb0894e | -6.0494 | -43.741299 | 2025-08-09 00:44:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89037482-3dc0-3958-bcf9-81b1224c9f76 | -7.2597 | -44.6567 | 2025-08-09 00:44:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45b4583d-a18d-3764-a73e-d9642d8c4665 | -9.0558 | -45.084202 | 2025-08-09 00:44:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b2e50ea3-69e4-3cd5-a3a2-a90c3aadd252 | -7.0931 | -59.181 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff89e8d-cda1-37be-8803-345d5ec195b9 | -14.3587 | -47.0909 | 2025-08-09 00:44:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3e4d79cc-1751-3772-89b5-b422cd6df44b | -7.8983 | -45.559601 | 2025-08-09 00:44:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a21d17e-7ae1-3127-ba02-85bced061999 | -16.2586 | -48.457401 | 2025-08-09 00:44:00 | METOP-C | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b9b21991-d091-36d8-9d8e-a0550856fbc9 | -7.9081 | -45.557301 | 2025-08-09 00:44:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52842a43-2839-35f0-9784-8a1de1c48cf3 | -7.0544 | -59.1408 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5d82d2a-79f3-359b-899f-ac8aab7e5230 | -7.1084 | -46.1059 | 2025-08-09 00:44:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8196d4b2-166d-3663-876a-93489d28e3c3 | -13.0704 | -43.848301 | 2025-08-09 00:44:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bfe828e7-7ce1-36ea-8791-34de3a9701e6 | -4.2941 | -48.066502 | 2025-08-09 00:44:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c07da947-cb18-34fc-9f6e-0b52b2c21a33 | -9.0656 | -45.081799 | 2025-08-09 00:44:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| db08d9b3-f281-3ef4-8fac-3f0d26e31c4b | -9.081 | -45.059601 | 2025-08-09 00:44:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 89ac8141-bdb5-316e-9654-ab7807000b69 | -19.814501 | -47.072899 | 2025-08-09 00:44:00 | METOP-C | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d39e96d4-3af7-3b84-804d-b5856120e491 | -8.9203 | -60.6894 | 2025-08-09 00:44:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ec9f906-1983-3ed2-ba16-8eb1e2a8cc9b | -7.9061 | -45.548801 | 2025-08-09 00:44:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a80ca05-82ab-3cf2-a319-ecd40603636c | -17.5247 | -50.276001 | 2025-08-09 00:44:00 | METOP-C | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 804fcf30-a3df-3fac-b0b6-291f2e2e295a | -7.0883 | -59.157902 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc69c489-98d6-3726-8dcc-aad79f789270 | -7.0544 | -59.188801 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 369ca07b-dbea-3d7f-a0b3-9b2cb6b8987b | -11.3223 | -55.2117 | 2025-08-09 00:44:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 371ab725-9673-393c-8720-9e71508f2157 | -5.4639 | -43.964802 | 2025-08-09 00:44:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0543d7b-4d51-34cd-9510-958724f2e220 | -12.4946 | -47.512402 | 2025-08-09 00:44:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01ee671a-9984-3a25-97e7-cebf3798d138 | -17.51189 | -50.27947 | 2025-08-09 00:45:00 | TERRA_M-M | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 047569d2-12d8-3679-9e87-20524fa1e3c8 | -17.52081 | -50.27813 | 2025-08-09 00:45:00 | TERRA_M-M | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 39.3 |
| e01a4187-3295-3f3c-80e1-345426a37086 | -18.45149 | -50.70879 | 2025-08-09 00:45:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| ed8a04e5-5a49-39ff-9257-5c154cb4be81 | -17.51315 | -50.28885 | 2025-08-09 00:45:00 | TERRA_M-M | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 2cf50bfa-b635-3e50-adbd-9f32e0d40eb3 | -19.80746 | -47.06304 | 2025-08-09 00:45:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 894b9a5f-5ec8-3a04-94d0-c41bec0adfc7 | -18.96788 | -45.18637 | 2025-08-09 00:45:00 | TERRA_M-M | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f40578ab-90a2-3f96-833a-457b94e7a4c0 | -17.531 | -50.28616 | 2025-08-09 00:45:00 | TERRA_M-M | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f607c61d-6196-3a35-b3e9-1ea1724fccd8 | -19.59506 | -42.68836 | 2025-08-09 00:45:00 | TERRA_M-M | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| d61490d2-70f9-32ed-993c-8a8dfa447d9e | -17.52334 | -50.29688 | 2025-08-09 00:45:00 | TERRA_M-M | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 04a1d31e-e6c6-3dc0-8e02-12d5e724481b | -17.79395 | -50.12341 | 2025-08-09 00:45:00 | TERRA_M-M | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6054896f-b3b1-3e87-bb99-f0c4f0cfdb49 | -19.80902 | -47.07338 | 2025-08-09 00:45:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 56.5 |
| b968f9ad-2dfc-3721-b78d-949655d21f14 | -18.44243 | -50.71018 | 2025-08-09 00:45:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bf795223-7ce3-3197-9141-3098467ba5ef | -19.81667 | -47.06139 | 2025-08-09 00:45:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 7621e61f-d5f3-345d-a10a-1a0ce23d3d8e | -17.51567 | -50.30761 | 2025-08-09 00:45:00 | TERRA_M-M | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6c2e6c53-5071-3981-a53c-5664ec688b65 | -19.81824 | -47.07176 | 2025-08-09 00:45:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 97b40baa-8a48-31cd-84c1-5c00b77f59bf | -18.45278 | -50.71852 | 2025-08-09 00:45:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 96f81fd9-7a39-377e-8991-4566801873f6 | -17.52208 | -50.2875 | 2025-08-09 00:45:00 | TERRA_M-M | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 5a474652-862a-3905-869e-2af4474de3a5 | -17.51441 | -50.29823 | 2025-08-09 00:45:00 | TERRA_M-M | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 9f486d26-5d1e-38cf-af3e-226cd7450570 | -17.79268 | -50.11404 | 2025-08-09 00:45:00 | TERRA_M-M | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7ad6e476-982e-3a37-b88e-f26cf1a62533 | -16.96198 | -51.05342 | 2025-08-09 00:45:00 | TERRA_M-M | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e7720a03-db4e-3d4a-8d2c-e610656f7ed9 | -11.37762 | -54.36039 | 2025-08-09 00:48:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5244b80e-1aec-3a5b-934e-5b7dec933ae7 | -12.04554 | -47.51908 | 2025-08-09 00:48:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| f5ba01c4-0231-39f5-aa10-0972975c5cb6 | -11.37607 | -54.34834 | 2025-08-09 00:48:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0dff0c31-bef7-3e5f-bffe-954803ee0a51 | -11.32572 | -55.21724 | 2025-08-09 00:48:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 51a87804-2d7f-3a94-b818-ed43776c29a0 | -11.71977 | -48.35187 | 2025-08-09 00:48:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cb7fb40a-75ad-3335-b86e-cb2e2c2ca5cf | -14.35788 | -47.09132 | 2025-08-09 00:48:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 63e2a485-fbbc-3b1a-956d-ca4257ea85a2 | -13.63479 | -49.02701 | 2025-08-09 00:48:00 | TERRA_M-M | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6695c4ba-eb9d-3235-b882-27c50daf0fe0 | -9.05458 | -45.07742 | 2025-08-09 00:48:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 67aa7fce-fc7d-3402-a386-941be4db24b7 | -11.73321 | -47.48675 | 2025-08-09 00:48:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 8e5a3a9f-135b-3b01-b282-8be6bab49150 | -13.62553 | -49.02493 | 2025-08-09 00:48:00 | TERRA_M-M | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 19b0ef0f-6f41-37ab-9b91-aee826f4a08a | -10.00597 | -48.12156 | 2025-08-09 00:48:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3ff87049-f54d-326b-8b18-274b82eb598d | -9.51819 | -45.42551 | 2025-08-09 00:48:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c4dbbc03-e40b-339c-9014-54ffb26e5bac | -11.9413 | -44.54502 | 2025-08-09 00:48:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 8e8073e4-2bbf-3486-8202-144793da4386 | -12.69304 | -48.20711 | 2025-08-09 00:48:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 03baf5ec-144f-338e-85d2-64a14a5984df | -11.73496 | -47.49852 | 2025-08-09 00:48:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| b3e374c4-b6db-36cf-936e-a3c846ee2f14 | -12.55694 | -47.11057 | 2025-08-09 00:48:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 49d9b6c5-cb4d-35cf-adf0-20f8a0db7c40 | -10.00766 | -48.13276 | 2025-08-09 00:48:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| eb312fba-01e8-37fc-87d4-0f44c3573347 | -13.63148 | -49.84549 | 2025-08-09 00:48:00 | TERRA_M-M | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f9b30b24-7ac3-399a-a0a0-e54c9ab1fd43 | -16.25288 | -48.45901 | 2025-08-09 00:48:00 | TERRA_M-M | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| bf4199a0-9797-3bde-b23a-63f4cda3a5de | -11.10596 | -50.48526 | 2025-08-09 00:48:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 49f60ed8-e12d-345b-873a-994e264b8e6b | -11.80276 | -44.9285 | 2025-08-09 00:48:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 823ddc69-19c9-3d10-b64a-9c56af502fa6 | -9.05797 | -45.09032 | 2025-08-09 00:48:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6cbb9f27-1e40-3f22-9d9f-1dc800ec9c12 | -11.71822 | -48.34141 | 2025-08-09 00:48:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0aadff14-f5c0-3f51-9398-97407ce3e36e | -14.18534 | -49.72509 | 2025-08-09 00:48:00 | TERRA_M-M | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6a1d1948-66d1-3686-8719-b9f868c9a35f | -14.35775 | -47.09733 | 2025-08-09 00:48:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 9c6aa120-f6eb-33ae-8290-1ff597133cb8 | -12.7228 | -47.79247 | 2025-08-09 00:48:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c138ec77-7192-3953-9a55-768b184ebd12 | -13.05812 | -56.85356 | 2025-08-09 00:48:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ad7a4606-d545-3750-ae66-644a14f3ee85 | -12.04377 | -47.5075 | 2025-08-09 00:48:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 22272c76-eb0d-3235-bfdf-633e800c3c81 | -14.36821 | -51.1148 | 2025-08-09 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a9636437-d32f-39e1-b317-1f1690263356 | -10.17513 | -49.5102 | 2025-08-09 00:48:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 61e5b396-8f49-3ee0-aa07-1d8954215af2 | -13.78 | -48.88179 | 2025-08-09 00:48:00 | TERRA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8fbab252-9a05-3bc7-899e-7a1ab9455e70 | -12.49523 | -47.51004 | 2025-08-09 00:48:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 267dab9e-7b6b-3ea0-b2de-9bb818ab6253 | -11.94441 | -44.56384 | 2025-08-09 00:48:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| cc57abf5-9bbc-3998-8f13-d8f80326ac19 | -10.82866 | -49.38227 | 2025-08-09 00:48:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 208e8d54-57fc-3d45-94db-887565ef7245 | -11.93981 | -44.55088 | 2025-08-09 00:48:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a563d844-43b1-3b07-b49b-105a901939c2 | -13.63346 | -49.0178 | 2025-08-09 00:48:00 | TERRA_M-M | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 31a5e4d3-5668-3819-b659-e1b5502b8ca9 | -13.62418 | -49.01554 | 2025-08-09 00:48:00 | TERRA_M-M | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ed623c77-70b7-34a1-aa1c-5f50e6b68792 | -13.06161 | -43.84422 | 2025-08-09 00:48:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 69557e1b-fd7f-3a65-b6f8-65709575c992 | -11.92885 | -44.54713 | 2025-08-09 00:48:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 1dd6eb87-8325-33bc-90be-4eac0354288e | -12.05372 | -47.50592 | 2025-08-09 00:48:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| ac4d5358-bbce-3c59-a27c-1e08c76258ab | -9.87128 | -49.96514 | 2025-08-09 00:48:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b5c405e7-c221-3249-9bf9-9729f0a8af64 | -11.77165 | -47.40174 | 2025-08-09 00:48:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 13296d6f-c414-369c-8406-e9b92b66eec2 | -13.04545 | -56.85527 | 2025-08-09 00:48:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 6fb36d9e-246d-327d-86cc-9c0575f92e97 | -11.33014 | -55.22437 | 2025-08-09 00:48:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |


[Clique aqui para ver as próximas entradas](README5.md)
