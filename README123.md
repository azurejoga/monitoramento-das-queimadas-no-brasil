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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd661082-c5e8-3b78-b292-6c01849fb8dd | -3.2244 | -53.0524 | 2024-11-10 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| b4e62788-e489-3986-847a-7912deab3e86 | -3.2168 | -50.2861 | 2024-11-10 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 06030f0a-5094-3bac-85b4-82cb922f048c | -3.9669 | -48.1716 | 2024-11-10 06:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| fde75768-61ba-3be6-a614-7d0692372a1e | -3.9485 | -48.1508 | 2024-11-10 06:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 13561f77-4bf3-3bc9-a223-dcfb0471e61c | -3.2352 | -50.2855 | 2024-11-10 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 8f3518a3-5e90-34ee-bb0f-15d8b90d4c6e | -3.9483 | -48.1724 | 2024-11-10 06:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 775c92bd-14c9-3e81-a9d2-846ee50cd0bb | -2.7587 | -49.3497 | 2024-11-10 06:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 47f83317-4d2a-381d-bbff-a0b91e07085e | -3.2353 | -50.2645 | 2024-11-10 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 7f095875-a5b0-3603-99e1-d057f3241519 | -1.5347 | -52.2104 | 2024-11-10 06:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| dc633982-ba94-3d0f-a97c-bd32f174d532 | -3.1423 | -50.4352 | 2024-11-10 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 145.1 |
| af0b64a5-63ca-3f05-8d21-e8075e147d2c | -3.2243 | -53.0727 | 2024-11-10 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| ed7b94ad-185a-3634-a619-bc331cf3411c | -3.9668 | -48.1932 | 2024-11-10 06:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b581eb7c-aeba-3d51-bf51-94a403c5ff8e | -3.2352 | -50.3065 | 2024-11-10 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 5353a8b5-553d-3e45-b2db-c0c49c885070 | -2.7772 | -49.3492 | 2024-11-10 06:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 01da4d77-2f68-3ae9-a229-18a6b7a665af | -12.41906 | -64.1417 | 2024-11-10 06:20:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e4b396a7-345d-31e5-afb1-d107d67379d5 | -12.41966 | -64.13649 | 2024-11-10 06:20:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ccf3dd76-3343-3a7a-bea5-630bd85b37cb | -12.42666 | -64.13188 | 2024-11-10 06:20:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2329436b-a9ce-3cb8-835b-39f3364d60c6 | -12.42027 | -64.13116 | 2024-11-10 06:20:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0559cb1a-01a1-308b-9c56-b7e82fa82eca | -12.42605 | -64.13713 | 2024-11-10 06:20:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 55737610-23dc-3881-802e-db2a59d5d464 | -3.2352 | -50.2855 | 2024-11-10 06:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 857915de-9b54-3212-bd2e-df635070ccf6 | -3.2244 | -53.0524 | 2024-11-10 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 514188ab-74de-3703-afca-8c72be1fcd8f | -3.5568 | -45.0302 | 2024-11-10 06:30:00 | GOES-16 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 8e390154-4f3b-365b-9587-eb9449b1f9e9 | -3.9483 | -48.1724 | 2024-11-10 06:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 8a1c520b-177a-39d0-a074-5e1c1727b2df | -2.7587 | -49.3497 | 2024-11-10 06:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| fe383ff3-a969-3d48-bd31-946373e79a58 | -1.5347 | -52.2104 | 2024-11-10 06:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 64f0e6bb-239a-399f-9e05-b4e93c405fa6 | -3.1239 | -50.4358 | 2024-11-10 06:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 10fac540-8462-369a-8655-62d343d8c29b | -3.5064 | -44.0294 | 2024-11-10 06:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| b8c65997-e97c-3261-a2c3-7dc627d22017 | -3.1423 | -50.4352 | 2024-11-10 06:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 81f19cdd-fb08-343b-849a-d50dd4144fb9 | -2.931 | -52.7753 | 2024-11-10 06:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| ef253ca8-f831-3d5f-9295-b1a558fff953 | -3.9485 | -48.1508 | 2024-11-10 06:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 64f9993a-1f37-38c9-a72b-b5949058e20f | -2.0953 | -48.8338 | 2024-11-10 06:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| ba5b6158-713b-3013-9d56-9ec0cfaa4237 | -3.1238 | -50.4568 | 2024-11-10 06:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b3d8a2ea-fd89-3ac6-9a81-8384ff577069 | -2.7772 | -49.3492 | 2024-11-10 06:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 6a42e99e-3254-3ef6-84f6-0e1de1d62fe1 | -2.9355 | -51.482 | 2024-11-10 06:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 177523b1-1ec9-3fca-b98f-ab88cef4b6cd | -3.2243 | -53.0727 | 2024-11-10 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 186ef1ee-1512-39f3-9540-ce0449ef39b5 | -2.0954 | -48.8125 | 2024-11-10 06:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| cd927626-2f31-3bde-89d7-494bd130a062 | -3.2353 | -50.2645 | 2024-11-10 06:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| ab8e101b-07dd-316a-983e-298b5ebba71f | -3.2168 | -50.2861 | 2024-11-10 06:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 0ba7ee3b-369e-37c3-9d2a-010628d44304 | -3.1422 | -50.4562 | 2024-11-10 06:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e1dc81e1-5357-3205-9395-13fb42119ea5 | -3.2352 | -50.3065 | 2024-11-10 06:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 95ed18a3-6a6c-3618-ad76-abca8ce4374c | -3.9669 | -48.1716 | 2024-11-10 06:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| c951d67a-8b76-378c-a1c7-5d865e167a88 | -3.2536 | -50.3059 | 2024-11-10 06:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| bda37e42-2b5e-3230-84af-1256b2d9de2e | -2.931 | -52.7753 | 2024-11-10 06:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 3459775b-b7e7-3690-92eb-1b4d3bb9231f | -2.7587 | -49.3497 | 2024-11-10 06:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 9ac056bd-aae2-3eaf-a549-c1941d4ea382 | -2.7772 | -49.3492 | 2024-11-10 06:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 560aae20-11c7-3347-b1e8-eaaed3df0690 | -3.9483 | -48.1724 | 2024-11-10 06:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| e2aee0e9-60dd-3617-90bb-8d00fd8ab086 | -1.5347 | -52.2104 | 2024-11-10 06:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 7d77ebfe-ac0d-3266-8731-c7a9a3c0f0af | -3.1238 | -50.4568 | 2024-11-10 06:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 00c35185-c08b-3ba4-89f9-923262acc0bb | -3.3544 | -44.5851 | 2024-11-10 06:40:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 5580b5f9-1766-3d06-a339-404acde95acb | -2.0953 | -48.8338 | 2024-11-10 06:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 9e6cc6fd-59ba-346a-9bbd-6a6aebcab9f1 | -3.1423 | -50.4352 | 2024-11-10 06:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 89bbe2c4-7796-36bf-a9c4-c6a57965560f | -3.2352 | -50.2855 | 2024-11-10 06:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| cfb64818-062c-386e-b69e-4b9dee1262df | -3.1422 | -50.4562 | 2024-11-10 06:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| fa226732-a1dd-30f6-b891-ef23e3eae25d | -3.2244 | -53.0524 | 2024-11-10 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f03d862d-46ef-3e4f-9438-cc754670a8eb | -3.5064 | -44.0294 | 2024-11-10 06:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| ae0b9a0b-23d5-3f78-8d9d-da459d8ef48a | -3.2352 | -50.3065 | 2024-11-10 06:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| e4e0ef3a-7e46-3679-b0f3-af753b976675 | -3.1239 | -50.4358 | 2024-11-10 06:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 145.8 |
| 38cbcb08-4c22-378b-80a1-9c03c63d0162 | -3.2168 | -50.2861 | 2024-11-10 06:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 9d0fe7fd-1f43-33fb-87b7-21cfda704261 | -3.9668 | -48.1932 | 2024-11-10 06:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 73eb982a-0c5c-3e38-a1a3-a8302d4caaa4 | -3.9485 | -48.1508 | 2024-11-10 06:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 10b19cc1-fd51-30c7-b746-8bb89bc4a2dc | -3.2243 | -53.0727 | 2024-11-10 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 9781a902-8022-350d-a88f-3f47ffc8efe8 | -3.9669 | -48.1716 | 2024-11-10 06:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 45abf52a-044d-3b11-8109-43784c4a5584 | -2.0954 | -48.8125 | 2024-11-10 06:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| fb4ff28d-6108-37df-bfc6-bf8f31996de7 | -3.9483 | -48.1724 | 2024-11-10 06:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 3ea59969-d9e0-39e7-9aa4-8514ae17388e | -1.5347 | -52.2104 | 2024-11-10 06:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| b485b98b-e640-343a-9642-08914d8270b7 | -1.4576 | -54.3168 | 2024-11-10 06:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| ee561df6-44cc-3279-b577-64b77484751b | -1.476 | -54.3166 | 2024-11-10 06:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| e9cb920d-519d-3f8e-a5f9-56c90b0d730e | -3.2352 | -50.3065 | 2024-11-10 06:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 2750d308-2da5-34db-87e4-946df073e4f3 | -3.2244 | -53.0524 | 2024-11-10 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7f4fe6f2-4ddb-3363-b330-77e65052520c | -2.931 | -52.7753 | 2024-11-10 06:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e5fdc8f0-444a-3d19-b041-018c7cc7110b | -2.0953 | -48.8338 | 2024-11-10 06:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ed52192d-6abe-39b7-af48-3ca1b5c568bd | -3.1239 | -50.4358 | 2024-11-10 06:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 7a1a01ab-e9d7-34b3-b7c7-f2517549accf | -3.2352 | -50.2855 | 2024-11-10 06:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 8ab2eb59-fa2d-3aac-8ac4-d0eff36215c8 | -3.2536 | -50.3059 | 2024-11-10 06:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| eee101f3-0307-3499-a590-6ebd3651f9d6 | -3.1422 | -50.4562 | 2024-11-10 06:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 262f274f-1618-3f99-b86d-53b0ab90b310 | -3.9485 | -48.1508 | 2024-11-10 06:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| c5fd4ba9-5356-3d29-8201-9deb08acf319 | -3.1423 | -50.4352 | 2024-11-10 06:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| ec417d82-50c9-3c55-85e2-228ccbdecac3 | -3.1238 | -50.4568 | 2024-11-10 06:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| bce633d9-c254-391b-bbbe-9e8db8119845 | -2.7772 | -49.3492 | 2024-11-10 06:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| b71a392c-4aa7-3af2-8b0c-199ef3a2a0d3 | -3.2168 | -50.2861 | 2024-11-10 06:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 48252a99-013c-327e-9706-20cfd7f4b808 | -2.7587 | -49.3497 | 2024-11-10 06:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 1f2955ee-fecb-32c4-b56f-eebc4cd291e3 | -3.2243 | -53.0727 | 2024-11-10 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| a8559201-bb9f-3c34-8b29-eb2a79251a6a | -3.2353 | -50.2645 | 2024-11-10 06:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 7b4412a4-69ca-3f30-bb8e-4614ec9813b4 | -3.9669 | -48.1716 | 2024-11-10 06:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| e04c97ef-b425-355d-94ba-c3a51a0bf501 | -3.2168 | -50.2861 | 2024-11-10 07:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 03e09489-e4c6-36ef-a752-123e0e23e889 | -2.7586 | -49.371 | 2024-11-10 07:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b642f263-bfc6-3469-b7b3-7d092486c80d | -2.7587 | -49.3497 | 2024-11-10 07:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 1eb90171-a3a0-3b22-8422-60c74c1fc241 | -3.2352 | -50.2855 | 2024-11-10 07:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| e1f1466f-6358-3a36-9a3f-b5a1600bf9ca | -3.2243 | -53.0727 | 2024-11-10 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| e94a754f-0426-3852-93ca-e64ead91ada0 | -2.931 | -52.7753 | 2024-11-10 07:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| f053255d-6bcb-3c72-bc8d-3ff68a24f650 | -1.5347 | -52.2104 | 2024-11-10 07:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 492eb978-26cb-3afa-85db-6adac3c362c8 | -3.2536 | -50.3059 | 2024-11-10 07:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| f389f9d1-46e6-3d74-9263-2ab308f28210 | -1.476 | -54.3166 | 2024-11-10 07:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 4290fea6-ea45-3fa0-ad45-701d981442e8 | -2.7772 | -49.3492 | 2024-11-10 07:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ac28ba0a-4595-3dcc-a15c-a40452147a38 | -3.2353 | -50.2645 | 2024-11-10 07:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 6cceb185-da7b-3c86-88b4-9942a5e17dc5 | -3.2352 | -50.3065 | 2024-11-10 07:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 9a888447-6298-32e5-baa7-c8eda6139e0b | -3.2398 | -45.1791 | 2024-11-10 07:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 8ea141b2-4606-3c72-a7aa-5bffe5bea03a | -3.1239 | -50.4358 | 2024-11-10 07:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 6060f611-de4e-3bc6-a8e0-44da4687a623 | -3.1423 | -50.4352 | 2024-11-10 07:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 184.4 |
| 5c75cb01-8824-325a-aa2e-eba0de572e28 | -2.0953 | -48.8338 | 2024-11-10 07:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |


[Clique aqui para ver as próximas entradas](README124.md)
