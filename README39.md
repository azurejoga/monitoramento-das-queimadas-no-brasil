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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d192496f-e75b-3966-b2c8-16518f1bbdee | -11.0738 | -51.5787 | 2025-10-23 12:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d2ed3d5b-7c60-31eb-9a31-cca0696c3358 | -13.3697 | -46.632 | 2025-10-23 12:30:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 207195ea-a2cd-3528-a838-a13b3e782275 | -13.3697 | -46.632 | 2025-10-23 12:40:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| cb65657a-b883-34bf-a53f-000470cb232d | -11.0738 | -51.5787 | 2025-10-23 12:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e61db78c-f975-36f1-a891-298315731f83 | -17.5973 | -46.5948 | 2025-10-23 12:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 180.1 |
| f8e3ae14-c7d3-3411-8b8f-dfc20b441a49 | -17.6167 | -46.614 | 2025-10-23 12:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 420.3 |
| 0fd8375b-dfcc-35bf-aede-dcecbb89c913 | -17.6555 | -46.6523 | 2025-10-23 12:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 89.1 |
| d66f65a6-c68d-3ce7-8b3f-44a565f979de | -17.5967 | -46.6182 | 2025-10-23 12:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 342.0 |
| 8dbebef2-0a4b-3689-b350-39632dcf39f8 | -17.6173 | -46.5906 | 2025-10-23 12:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 8e0a0775-c65f-3104-ab7b-ee39febe7723 | -12.2671 | -47.0221 | 2025-10-23 12:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 80dc2ff1-11b4-3ed7-8e29-f76c29cbea7c | -17.6173 | -46.5906 | 2025-10-23 12:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 143.8 |
| def6d3cd-eaee-3d69-a072-c6fee82c1fea | -17.6555 | -46.6523 | 2025-10-23 12:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 93.3 |
| b20e74ea-11ba-3ac4-9c8a-7d15991b1241 | -17.5973 | -46.5948 | 2025-10-23 12:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 257.6 |
| d864222f-a5c3-30c4-82f0-9d724024331c | -13.3697 | -46.632 | 2025-10-23 12:50:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 83882bf1-c937-3bc0-a071-78006804eeb0 | 0.3957 | -50.9412 | 2025-10-23 12:50:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 4fe9f9af-8ef2-3154-947e-90848fd63adc | -17.5967 | -46.6182 | 2025-10-23 12:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 400.2 |
| 7f1bafdc-5cff-3938-a810-0bd736977555 | -11.0738 | -51.5787 | 2025-10-23 12:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d35d6fa1-a15d-3a2a-894f-a89a53ac69f2 | -17.5973 | -46.5948 | 2025-10-23 13:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 273.6 |
| ec05d41c-295e-3262-8d49-34247962051f | 0.3957 | -50.9412 | 2025-10-23 13:00:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 1f27b3dd-a49c-38b1-a7a0-5b1b4d0432df | -17.5967 | -46.6182 | 2025-10-23 13:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 468.9 |
| 98b20376-0cb9-352c-8110-13454445bafa | -17.6173 | -46.5906 | 2025-10-23 13:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 3b8e90d5-8b7d-3435-b5ff-0d0bccfbb485 | -15.1405 | -43.8014 | 2025-10-23 13:00:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 6f6759b3-4599-3829-adcf-068221175c0d | -17.6167 | -46.614 | 2025-10-23 13:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 252.4 |
| 0e7895e6-b867-3e91-8ff8-533ffd46654f | 0.3773 | -50.9413 | 2025-10-23 13:00:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 0146877c-93e2-3128-976d-944923f0d579 | 1.6569 | -55.765 | 2025-10-23 13:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 677ff5aa-3146-3d72-a49f-ef587f5bf309 | -17.6555 | -46.6523 | 2025-10-23 13:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 87.1 |
| e6782fb6-a463-3cca-ba15-5d3f28afe264 | -13.3697 | -46.632 | 2025-10-23 13:00:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| b85b0b81-48b5-364c-a2a5-4e8c39880a0b | 0.3957 | -50.9412 | 2025-10-23 13:10:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 85.8 |
| c51e66e5-669d-38e6-8fed-d4e459696c99 | -17.5973 | -46.5948 | 2025-10-23 13:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 318.8 |
| 58bf9a9a-7798-39ed-ba15-5e64ddb631b8 | -17.6173 | -46.5906 | 2025-10-23 13:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 20816f56-eae8-3a92-981e-7beb0324bd94 | -13.3697 | -46.632 | 2025-10-23 13:10:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f18c6367-bcad-3682-877b-07d868261971 | -17.6555 | -46.6523 | 2025-10-23 13:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 85.0 |
| f2847bc6-36cb-37f5-89f2-143979d4adb5 | -17.5967 | -46.6182 | 2025-10-23 13:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 433.3 |
| 65b0aa14-e920-3643-8d51-83abeab7d755 | -11.0738 | -51.5787 | 2025-10-23 13:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| a1e4421a-8744-36c6-be68-1958ea3009fc | -17.6167 | -46.614 | 2025-10-23 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 44e7cae1-399d-3e21-ac81-3308a0b8f3b8 | -17.5973 | -46.5948 | 2025-10-23 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 251.5 |
| eb1cf66b-6cc5-3f4e-b765-de66dc9661a2 | -17.6555 | -46.6523 | 2025-10-23 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 7984f00f-7c23-37f3-be7a-850603f57b6d | -17.6173 | -46.5906 | 2025-10-23 13:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 847f1fb6-fe62-3991-92e8-6304a7385c1a | -13.3697 | -46.632 | 2025-10-23 13:20:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 1216372b-784d-3b93-bff7-f2411a0626b1 | -11.0738 | -51.5787 | 2025-10-23 13:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 12e2eaa2-b336-36bb-84fe-2dd69346efcc | -21.9536 | -42.9148 | 2025-10-23 13:20:00 | GOES-19 | ALÉM PARAÍBA | MINAS GERAIS | Brasil | 3101508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 136.2 |
| 967502c4-24f9-3d74-9940-4945644c3216 | -13.0504 | -47.223 | 2025-10-23 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 5cdc8e48-5967-355b-afe0-96b9fe83a72a | 0.3773 | -50.9413 | 2025-10-23 13:20:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 7fb226a4-9fb5-35e5-a53f-390e6985f75a | -13.3697 | -46.632 | 2025-10-23 13:30:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 0186248c-42ce-30b3-b72b-a712e81d888c | -17.6555 | -46.6523 | 2025-10-23 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 85.7 |
| eab700a0-1c9a-37f0-9023-aaef74536511 | -17.5973 | -46.5948 | 2025-10-23 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 232.7 |
| 54abc19f-bc3a-3acf-ba33-c47770dbefd5 | -13.8962 | -48.3696 | 2025-10-23 13:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 30795b00-3f8b-3e3a-8a88-9dabae50be67 | -13.3693 | -46.6547 | 2025-10-23 13:30:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| e50869b2-90a6-3925-a5d8-5ec97e56143c | -11.0738 | -51.5787 | 2025-10-23 13:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| e99ebaa7-96c4-3b43-866b-81e50723ac42 | -14.5672 | -56.707 | 2025-10-23 13:30:00 | GOES-19 | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 6755d678-2b55-38f1-8c95-7c47d890979a | -17.335 | -55.0366 | 2025-10-23 13:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| 6895a35d-ab93-3012-b05d-0d28195b1f3b | -17.6173 | -46.5906 | 2025-10-23 13:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 204.4 |
| f74304b7-f208-3be8-a436-59ffd0fd2385 | -15.601 | -45.9016 | 2025-10-23 13:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 61e9234a-7037-348c-a520-d32cfa06512c | -13.3697 | -46.632 | 2025-10-23 13:40:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b9e59f6a-74f2-3fe9-9710-46c1a7b05ade | -17.335 | -55.0366 | 2025-10-23 13:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 8f43d014-b632-3cdb-a704-8647bb8c1080 | -17.538 | -46.584 | 2025-10-23 13:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 446da32f-9447-31f2-995c-29944a5cbc4e | -17.6173 | -46.5906 | 2025-10-23 13:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 118.2 |
| c9366b81-f77c-331d-a33b-820768023e31 | -17.5973 | -46.5948 | 2025-10-23 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 312.8 |
| 7e71df19-5f25-3c72-938b-b643d4926d48 | -17.3037 | -58.077 | 2025-10-23 13:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 6b90d672-ad0b-3693-9081-77773d450bbf | -15.6004 | -45.9249 | 2025-10-23 13:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 881daf2d-6773-3dcb-b3cf-fa5eda51ae48 | -11.0738 | -51.5787 | 2025-10-23 13:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| c6a99409-de02-340a-a255-c82b206e4f83 | -10.942 | -50.1478 | 2025-10-23 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| d98ce398-96b3-31c7-bfa1-24597c380516 | -1.2085 | -49.0838 | 2025-10-23 13:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| a8813fff-f939-3967-8cc7-e613eaf1e4ea | -4.6988 | -39.4141 | 2025-10-23 13:40:00 | GOES-19 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 105.2 |
| 7ce867bf-a8b7-3d65-8b9f-007d2fef75a7 | -10.9041 | -50.1519 | 2025-10-23 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 239.8 |
| c8f37dc4-6891-3117-9339-0f1131263f1f | -10.9231 | -50.1498 | 2025-10-23 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 1b56174c-17af-37cc-a8a9-390079895820 | -14.5672 | -56.707 | 2025-10-23 13:40:00 | GOES-19 | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 842b4f9c-e365-34f4-b783-393ca03f861c | -13.0504 | -47.223 | 2025-10-23 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 5a8a586a-b448-322d-98b4-a9e4297a0505 | -17.5961 | -46.6415 | 2025-10-23 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 56368310-089f-392a-b6c0-40ab4e53bfa7 | -13.0311 | -47.2259 | 2025-10-23 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 02dff1a6-bbf9-3770-a4f8-06e4a949f554 | -11.2492 | -49.8773 | 2025-10-23 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 97ac3c7f-4de6-31bc-8f81-ce345c08308e | -10.9782 | -50.2723 | 2025-10-23 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| affd4e52-aadf-3dad-8ce9-ddbf86ff1628 | -13.0504 | -47.223 | 2025-10-23 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 1e030e1f-b36c-3f6a-94ee-ae92ec01e41d | 1.6753 | -55.7253 | 2025-10-23 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 6fb95a05-16ad-3d78-b46b-29d3b45194fa | -10.9592 | -50.2744 | 2025-10-23 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| a57cbc8a-1c28-3148-8a40-c7d0c0a21bc3 | -17.335 | -55.0366 | 2025-10-23 13:50:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 74d6cf39-eee1-3680-8f2f-8c401f8a99ae | -17.538 | -46.584 | 2025-10-23 13:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 8edee02d-a28f-3e11-a0d5-f1965a08e036 | -13.3697 | -46.632 | 2025-10-23 13:50:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 7fcac03e-2ab1-3a41-bc93-a0672cb027c5 | -15.6004 | -45.9249 | 2025-10-23 13:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a7528ab6-f8a1-3dbb-9a5e-0cd771061fdc | -17.6173 | -46.5906 | 2025-10-23 13:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 94f65f0f-908c-349e-838b-e8dbeb69703d | -1.2085 | -49.0838 | 2025-10-23 13:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4348fbae-6b19-3d14-9ed2-6a1bb7a57a1d | -11.9388 | -47.2022 | 2025-10-23 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 427b1179-cc20-3dee-8380-3b8b251a5451 | -17.5973 | -46.5948 | 2025-10-23 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 331.2 |
| ad77fc15-f917-34f2-b501-6e5c1165d679 | -19.0319 | -57.5382 | 2025-10-23 13:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 5beb3155-d097-36d6-8abd-052127fe6e8d | 1.6569 | -55.7453 | 2025-10-23 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 57ddee97-aac6-3a58-bd70-7f7a477ef7a5 | -17.5973 | -46.5948 | 2025-10-23 14:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 384.5 |
| 3113ece0-c8e7-3253-a1e6-b71e1e81b828 | -17.335 | -55.0366 | 2025-10-23 14:00:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 133.9 |
| 9d8c985e-035e-3378-bc8f-86b9588aab87 | -10.9592 | -50.2744 | 2025-10-23 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 77912788-e284-3871-a808-db2cdb375b5d | -17.6561 | -46.629 | 2025-10-23 14:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 71.1 |
| d9b53bcd-7774-31a6-8250-d26e29ebcad1 | -11.7057 | -51.1302 | 2025-10-23 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| bc522dab-df85-3abc-938e-4c7a5137215b | -1.2085 | -49.0838 | 2025-10-23 14:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 2b9f1bc7-c107-325d-a04e-b12751ce01b6 | -17.6173 | -46.5906 | 2025-10-23 14:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 2f85e319-2b9d-3288-8924-fe2e0f8dac94 | -13.0311 | -47.2259 | 2025-10-23 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 8b776f40-5391-315c-8616-a61dbaca9d90 | -15.6004 | -45.9249 | 2025-10-23 14:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 65.6 |
| f0306dc9-d12a-32b5-87d1-bcc94745524e | -11.2492 | -49.8773 | 2025-10-23 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 480100dd-1af0-3f8a-a93e-b89e4f0207c5 | -13.0504 | -47.223 | 2025-10-23 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| b79e4ad0-0fc5-3df2-8b82-ae5e7c59c925 | -11.0738 | -51.5787 | 2025-10-23 14:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 92536025-1ccc-316b-bb0c-b82a7ae7b354 | -13.3697 | -46.632 | 2025-10-23 14:00:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 78d306fe-e1bf-34d1-aa0c-b544de05505d | -11.0738 | -51.5787 | 2025-10-23 14:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e8dd7973-605f-3ac0-b8b5-0f0e11320f82 | -17.3547 | -55.0339 | 2025-10-23 14:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |


[Clique aqui para ver as próximas entradas](README40.md)
