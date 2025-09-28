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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc377189-4ace-357e-8e1f-2a542cdb9367 | -8.2668 | -45.4564 | 2025-09-28 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| e4e67c03-a3b7-337c-ba97-832c16c8ce28 | -13.7704 | -47.8763 | 2025-09-28 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 1bb06aa7-cd02-3dbb-b0d3-10120f922cf0 | -4.6757 | -37.6624 | 2025-09-28 14:10:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 849.8 |
| f915f579-fed8-3c9a-a628-a9dd1209769c | -6.2759 | -43.6442 | 2025-09-28 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 8e71f516-c971-3f4c-a427-a5667c6c6b33 | -12.7637 | -50.4921 | 2025-09-28 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| e6fc1d9f-018d-36d2-9c6d-179d83b59c20 | -13.77 | -47.8987 | 2025-09-28 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 28950d79-1c5a-3c9e-acc3-03bacd4c47df | -4.676 | -37.6366 | 2025-09-28 14:10:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 134.1 |
| 4ebab8b0-53fb-30fc-9600-817e8d76a8ee | -7.2605 | -42.9939 | 2025-09-28 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |
| 91ea855b-12a2-36d6-a66a-7d58456d8e43 | -12.9156 | -45.1912 | 2025-09-28 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 285.3 |
| 0b80a9a8-243c-326b-9448-6dc39056c69b | -6.5803 | -45.0889 | 2025-09-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c3894327-8cf2-3ab1-8d9d-de672608ba83 | -4.6946 | -37.661 | 2025-09-28 14:10:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 361.0 |
| 692a8c6b-2ea6-3504-b258-e0be2998685d | -9.1102 | -45.8653 | 2025-09-28 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 7b3879e3-7d99-30bc-93d7-23e9606b95e9 | -12.791 | -47.7533 | 2025-09-28 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 2731405b-4fa1-3d93-bdc1-84925f4c0417 | -8.8226 | -46.2115 | 2025-09-28 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6c08ed43-6bb1-3777-90f4-d972f92d283d | -12.6917 | -46.8708 | 2025-09-28 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 185.2 |
| ac78c8b8-9e94-37ce-b8ff-e88e753414bd | -6.5611 | -45.1359 | 2025-09-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 381b5178-8c58-307d-87ce-595d324cb0f5 | -5.17 | -43.7276 | 2025-09-28 14:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 3b5f6d80-8761-3501-9676-ef17bb402a50 | -9.9581 | -43.5987 | 2025-09-28 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 318.9 |
| 4a7b858a-c714-3bfc-957e-6b421e082dc5 | -9.9585 | -43.5752 | 2025-09-28 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 91374017-90a8-3528-8a15-e8f9b22bd217 | -7.7555 | -45.7324 | 2025-09-28 14:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 72e50c0c-5127-38be-b645-72913ae6e38a | -12.0218 | -47.9481 | 2025-09-28 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 1dabda25-a17e-3c55-a621-ea0102f44974 | -11.964 | -47.9779 | 2025-09-28 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| f46920e1-2716-3606-8014-56def30d689f | -12.0214 | -47.9703 | 2025-09-28 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 056029cd-1584-3ada-988f-e2a59774c723 | -15.9076 | -46.2139 | 2025-09-28 14:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 7ea92074-e575-39be-a8b3-97386bf93464 | -6.6002 | -44.9736 | 2025-09-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| caa61557-be42-30f2-86aa-46d5f4555190 | -9.4009 | -54.6781 | 2025-09-28 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 34cc66fb-9513-38f0-bacf-fbf7b1153e4e | -4.6944 | -37.6868 | 2025-09-28 14:10:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 420.5 |
| eb0cb8d4-9145-3dd7-856e-1a832a539055 | -12.0222 | -47.9259 | 2025-09-28 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 9d551f28-aaca-30dd-8d3d-3d1f8615dda5 | -9.7643 | -47.7786 | 2025-09-28 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 6973a420-86fb-33fa-aa8a-d8c1dec76c18 | -12.9363 | -45.1184 | 2025-09-28 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 46fa08e4-c049-32c2-a7e6-5300bf4611da | -10.9137 | -45.7375 | 2025-09-28 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 15ab26af-74e9-3390-a9a4-e39dd2dac232 | -18.1977 | -53.3208 | 2025-09-28 14:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 67bfffd3-2945-320e-871a-eead942e3151 | -11.9982 | -47.0821 | 2025-09-28 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 13827eef-3a5f-3119-b982-ef0d17be855f | -18.1778 | -53.3239 | 2025-09-28 14:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 62c93ef1-70a5-31e6-82d3-c83ebfa0ce39 | -13.7893 | -47.8957 | 2025-09-28 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 0ab6e043-477c-318f-9947-09f940013f1e | -8.2854 | -45.4772 | 2025-09-28 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 2531c542-edc0-361b-803c-44022a0d47ee | -13.5884 | -47.2987 | 2025-09-28 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 119ca02e-11a4-3754-a785-0faede92a62b | -6.5614 | -45.1132 | 2025-09-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 2f832f54-edc9-3db6-b51a-d1958290a2fc | -5.9006 | -43.6744 | 2025-09-28 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 71a80c94-ea9a-3c3f-8450-2fe598d20ae5 | -5.8272 | -45.5985 | 2025-09-28 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 899f48c0-9d92-3a19-a6a6-c04f53b44659 | -14.9046 | -45.5672 | 2025-09-28 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 1a669fa3-596f-3326-9d50-e9e6eed03c57 | -11.4213 | -45.0488 | 2025-09-28 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 1f7a9ff2-72ac-34d6-95ca-e1bbde961d93 | -9.4196 | -54.6767 | 2025-09-28 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| ecda1111-8501-373c-9f78-05efe88630a1 | -14.3813 | -54.9472 | 2025-09-28 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| d4ed4611-af9d-35f4-b068-d94cd6ec7d84 | -6.2762 | -43.621 | 2025-09-28 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 6138fe6e-d467-3029-bd4c-d79b8b7e5b1d | -13.6267 | -47.3152 | 2025-09-28 14:10:00 | GOES-19 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 69f04ae1-1638-381d-9de7-6fd3b359d49b | -11.3654 | -44.9645 | 2025-09-28 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 222.6 |
| dddd1988-021c-3454-bf9a-c64c0a84e8d5 | -8.8393 | -44.9399 | 2025-09-28 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 972883f5-2365-3c0b-b055-ff754caa2c9f | -8.1611 | -46.4122 | 2025-09-28 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 0fd1248e-8bfe-3cd6-b8df-c073c150b675 | -8.2856 | -45.4545 | 2025-09-28 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 1b0a1b51-bbce-3d5c-8bf4-18557c5c94ad | -17.4579 | -50.8397 | 2025-09-28 14:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 50d2f480-2e94-31bd-9e3c-226491052885 | -11.3889 | -46.9847 | 2025-09-28 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 37652816-6cb4-390e-9701-d475628f6dbd | -9.1099 | -45.8879 | 2025-09-28 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 6cc1fb36-cf6e-3616-93da-0411a2fd5af9 | -11.9824 | -48.0197 | 2025-09-28 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 6a7eed4e-3ba8-3f0e-81a2-369a351b4160 | -11.4409 | -45.0229 | 2025-09-28 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 168.1 |
| eb137fb5-f4b9-3252-80c2-04216e8ac821 | -5.9076 | -42.9268 | 2025-09-28 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 73ffa10e-2a08-3bb6-b9b4-4a22b4772591 | -8.6442 | -43.9931 | 2025-09-28 14:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| a37f5094-8c1f-3204-80a2-372500b7cd46 | -14.7851 | -45.6818 | 2025-09-28 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 7a6f97f1-3321-3f47-9e4f-2feb4f3ff440 | -7.3659 | -47.0394 | 2025-09-28 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| a99bff18-2825-305a-940d-eb3115f81b6d | -5.6275 | -44.9115 | 2025-09-28 14:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 3f7fe7cd-9447-3c6a-b545-32e17e3bf861 | -6.0625 | -42.4422 | 2025-09-28 14:10:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| 24b32df2-232a-3468-9baa-e9e21250ece0 | -9.3013 | -45.7082 | 2025-09-28 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 4b52ab60-0b6f-3a74-ae43-eb0156529684 | -11.9986 | -47.0596 | 2025-09-28 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| d73f3e24-0563-333c-8d89-1b4d5053bef8 | -7.3661 | -47.0173 | 2025-09-28 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 83fa5ed9-5238-30b4-b5aa-452f258108fe | -7.1574 | -45.4932 | 2025-09-28 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 582cb76c-9660-3b28-a057-0b02801fc4ad | -11.946 | -47.9138 | 2025-09-28 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| a938fdf8-b007-319f-85dc-a706343cbb63 | -13.7889 | -47.9181 | 2025-09-28 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 215c8e21-8a33-39e0-83dd-d5c1222c0acb | -8.2665 | -45.4791 | 2025-09-28 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 7593a258-eaea-3e18-9b71-808b7aaa4b75 | -9.4192 | -54.7172 | 2025-09-28 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 92451806-4a89-37c9-9302-05287fd899ee | -8.5206 | -44.7685 | 2025-09-28 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| b03eb65e-5857-3c1f-9eff-1cc3fb82d4ef | -11.9644 | -47.9557 | 2025-09-28 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 36072325-8d48-3a48-a0db-5fa2b0d4f760 | -5.9004 | -43.6976 | 2025-09-28 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| b77ed613-89be-3ce3-9465-8208877a2b87 | -11.9637 | -48.0001 | 2025-09-28 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 0f99752c-ef20-3f40-9518-137f775907bf | -7.1571 | -45.5158 | 2025-09-28 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 0a12842c-9f35-33bc-9e1f-e172564cd660 | -4.4013 | -44.0755 | 2025-09-28 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 248.7 |
| e7958acc-0e19-3b7e-be3c-7d2b7994852e | -9.3331 | -47.56 | 2025-09-28 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 8640c22b-6385-3ac9-be35-ba64ebad57f4 | -15.8879 | -46.2177 | 2025-09-28 14:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 140.5 |
| a65a1631-04c7-34e9-a0d8-741887f52ade | -12.9547 | -45.1618 | 2025-09-28 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 363f6287-5a78-3ee4-8c4d-53e2b945fbd1 | -9.0913 | -45.8673 | 2025-09-28 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 724c75cb-104a-3978-8913-fd15f65b391c | -5.3059 | -43.1365 | 2025-09-28 14:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| abb7e630-8250-3938-84b2-dcd5a39ee6f8 | -6.5163 | -54.8784 | 2025-09-28 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 9a41099d-3453-378c-a8c8-da67a2d71322 | -8.1614 | -46.3899 | 2025-09-28 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| bf77317c-f92a-3324-bc9c-6671f9f5cfaf | -6.5616 | -45.0905 | 2025-09-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 494ebfcf-b1fc-32b2-bf07-a126ff91fe31 | -10.0184 | -48.5401 | 2025-09-28 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 3ac1dbee-3a8e-3f05-b518-294428de8661 | -12.6725 | -46.8737 | 2025-09-28 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 68244e16-1e07-3913-ae9a-aa05375a9698 | -15.8873 | -46.2409 | 2025-09-28 14:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 71b21851-a356-3f74-9ac7-16d2fbabe054 | -6.6181 | -45.0631 | 2025-09-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| b91be6d3-2745-3a56-bfd9-838694815c8b | -9.4007 | -54.6984 | 2025-09-28 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 83877143-ebaa-3249-ab74-ac1dd69707ac | -14.576 | -48.2417 | 2025-09-28 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| cbbf06a8-83a6-3608-b915-aea8d66f6fb0 | -9.2824 | -45.7104 | 2025-09-28 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d87a3c94-ac38-33f4-8133-64c8815bf339 | -11.3892 | -46.9622 | 2025-09-28 14:10:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 6f8eaacd-5f38-3f76-8668-bc4e5508777d | -10.0065 | -45.3976 | 2025-09-28 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 94be8d4c-f3a8-3d87-9917-9f24309cee7b | -5.7583 | -42.8447 | 2025-09-28 14:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 7426bb8a-d9da-3e1c-935b-e118a76c95a7 | -10.8242 | -45.3841 | 2025-09-28 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| e29a9bbc-fadf-3660-b309-2c0d5a3f3f12 | -9.3016 | -45.6855 | 2025-09-28 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 02c0b0fb-153b-3b2b-b4cb-51635b5122af | -11.9633 | -48.0223 | 2025-09-28 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| d7e12fa9-7273-3770-a948-9a91dd49c763 | -11.3642 | -45.0339 | 2025-09-28 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 1af2883e-fa82-3912-b5e4-6fea8c74ea93 | -5.6461 | -44.933 | 2025-09-28 14:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| e790a756-723f-3b08-b3df-184f451d1383 | -7.5449 | -46.089 | 2025-09-28 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 3c2017e0-5979-3ac0-a1d8-d15a6c74e0ad | -14.8845 | -45.5941 | 2025-09-28 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |


[Clique aqui para ver as próximas entradas](README105.md)
