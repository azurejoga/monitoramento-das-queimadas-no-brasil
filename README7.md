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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a27f875-da08-3f9e-96a1-d5fded187e69 | -2.88259 | -45.28862 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8526b6d-d1ed-3082-b7bc-5b9ddbf92872 | -4.83717 | -44.06458 | 2025-11-23 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6fe50301-fa84-301e-a3d3-c1d2572ea1dd | -2.64217 | -47.38626 | 2025-11-23 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcbf2e3d-4207-3fb7-ab58-b9f9f7140a57 | -3.90918 | -46.13771 | 2025-11-23 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8547b49b-74b6-3fbd-b0af-306cec1fee7f | -1.32496 | -53.14355 | 2025-11-23 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e4274d2-ae33-331f-bb56-a287ac63fdc6 | -1.19276 | -53.71956 | 2025-11-23 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3414fee8-094c-3ed0-a7de-48da6d930ffc | -6.55066 | -44.46209 | 2025-11-23 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64c2c47c-ff68-392f-9f7f-ea62c43cc6ae | -1.88837 | -50.97015 | 2025-11-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5f340e0-7e1e-315d-9990-b0887f188230 | -6.54726 | -44.46156 | 2025-11-23 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f33a8a5-0d6f-3720-abbe-bc2bd361517e | -2.02664 | -47.14778 | 2025-11-23 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89c23ef9-9b74-3081-893a-2119f9008494 | -4.83661 | -44.06825 | 2025-11-23 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79fa1307-e402-3c94-b0b0-dc4fc257a284 | -4.04075 | -42.52431 | 2025-11-23 04:25:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 51b2e9ef-b217-3075-84cf-ffe50b620209 | -1.85871 | -54.07186 | 2025-11-23 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de6fcbf3-0ebf-3d13-b113-c2f8186f9ae7 | -4.05036 | -42.52056 | 2025-11-23 04:25:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e90a7ecd-9d8b-3166-9f79-bc730131b063 | -3.70163 | -47.67941 | 2025-11-23 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41d52167-a787-3384-8949-68822fd060ec | -3.29012 | -45.726 | 2025-11-23 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee2e8f04-bf0d-319a-ab85-1322cb93686c | -2.99222 | -44.43407 | 2025-11-23 04:25:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b27b73e5-bdbb-300a-960e-967c4f941ade | -4.02083 | -42.46166 | 2025-11-23 04:25:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f414d44f-c392-30d4-a5de-de7d9b691bee | -3.35902 | -46.86798 | 2025-11-23 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e51b6e1-3403-3b81-b1c7-4fbcb8f3c84d | -2.64221 | -47.38603 | 2025-11-23 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74342d68-3e17-34ab-9c3e-ec0ffdd3cda4 | -2.27483 | -46.44777 | 2025-11-23 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14bbf791-94cf-3633-b6af-95c80c128578 | -2.88473 | -45.27489 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3644a1bf-710e-319a-9252-333d72076fae | -3.86751 | -40.64349 | 2025-11-23 04:25:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 63b62370-594b-321f-9291-0b7c30d903eb | -5.17938 | -46.99526 | 2025-11-23 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f13bbf82-bb75-35d7-bee3-25b737cbf492 | -2.73037 | -45.21569 | 2025-11-23 04:25:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40aa6af6-11b3-3e31-954a-d5ed3e562c2b | -4.40404 | -46.43178 | 2025-11-23 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44d15b27-98b0-35e3-84ea-6656d2e2995a | -9.55067 | -47.77211 | 2025-11-23 04:25:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62e1d380-7ac5-3f8a-a0f7-a087a0f59eaf | -2.9646 | -45.439 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adac7071-ee7a-3f86-bc43-24e0ec307d4d | -4.04436 | -42.52487 | 2025-11-23 04:25:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f6809ed7-f611-31e7-b976-4b0f89b0af8c | -2.63163 | -47.29689 | 2025-11-23 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51566a7d-265c-3b7e-9d42-011a6b4beef9 | -3.96731 | -43.23969 | 2025-11-23 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64dc541f-f556-37bc-bf60-c5ac739de8ef | -2.50838 | -49.21688 | 2025-11-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f51fd008-7e00-359d-82ad-2e7a9a54eaa1 | -2.98889 | -44.43355 | 2025-11-23 04:25:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e63df9d-db88-3c5a-ba3f-7a95a447f254 | -4.59165 | -45.5192 | 2025-11-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebe61a55-0385-3c24-8007-d4cd74df5ba0 | -7.40469 | -40.06248 | 2025-11-23 04:25:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d36a752a-5dfb-33bf-a64d-b7d40ab18319 | -3.93854 | -47.56023 | 2025-11-23 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9507f516-7722-301d-994d-821e6ba349f3 | -4.37688 | -46.38854 | 2025-11-23 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e19048b6-3825-312b-b81a-24ef6267c215 | -2.49817 | -47.09945 | 2025-11-23 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 614fbc9b-3781-3ad9-ae41-b9296d1379e1 | -4.17105 | -44.22006 | 2025-11-23 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2255ab8-c787-35c1-9a80-12799a6dc0c4 | -2.88312 | -45.28519 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 27917979-2845-3374-a429-7213601bd8a9 | -3.75512 | -50.94035 | 2025-11-23 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99b6bac8-85dc-3dbe-998a-99fa83386f5e | -4.01884 | -46.15475 | 2025-11-23 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8235de1c-4d0a-3fe4-a4d4-b4cbdce953ea | -3.97884 | -42.51909 | 2025-11-23 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e51cd5b3-6794-3875-b987-90c69911ffdb | -2.87384 | -45.45243 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a8f64d8-b2a0-3d1f-9d24-31319b2f29a3 | -5.62982 | -46.49159 | 2025-11-23 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 748c1150-7d1e-30aa-abdf-afd82a961d33 | -5.98024 | -40.38357 | 2025-11-23 04:25:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 2a4ab727-fe24-307c-a317-76d2d025d9e9 | -2.95814 | -53.28047 | 2025-11-23 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df277d2f-9238-3859-a0ed-0388361241c9 | -6.94167 | -39.22811 | 2025-11-23 04:25:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c2ab9153-af98-38d8-ba7b-1ec2407ec9fa | -4.04139 | -42.52018 | 2025-11-23 04:25:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b8a2f439-d547-33a2-b063-cec8919efa3c | -5.54532 | -41.03936 | 2025-11-23 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 935aa8c8-0faf-3b06-a503-b8fc9b1e3950 | -4.25077 | -46.45424 | 2025-11-23 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d37af2af-103b-3641-9c4d-2a178035ef7e | -4.64722 | -44.79091 | 2025-11-23 04:25:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b91c909e-a476-31c9-a80d-807cbbb7bb11 | -2.87759 | -45.2773 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 472f6c1c-999d-3d1d-b029-33057484cea1 | -2.89357 | -45.28329 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 101754b8-6ac8-31c6-b6b9-230238b7d30c | -5.21918 | -41.07541 | 2025-11-23 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4768ba29-9d3e-379c-993b-02b8a2dddd87 | -2.64277 | -47.38255 | 2025-11-23 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36eae979-94e4-3af6-93af-7fdcfd11aed5 | -4.55541 | -45.48818 | 2025-11-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a0287be-a78a-3290-bd6e-6e41cd36ad8c | -1.32993 | -53.14431 | 2025-11-23 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00e5f0b0-9ff8-3580-8799-9e6c9232540e | -4.01553 | -46.15424 | 2025-11-23 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b543ede-f887-3bf7-b5ba-774e18996a1e | -2.8782 | -45.14009 | 2025-11-23 04:25:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36f8aeda-3dae-3e95-844f-bd7b9c49cab9 | -3.97418 | -43.28807 | 2025-11-23 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e562961d-0b94-3dbc-9b32-7b1d1adcf32a | -4.71593 | -46.45998 | 2025-11-23 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 27c8e921-7fdc-3488-97f8-ebaf4d79195c | -4.61843 | -46.12959 | 2025-11-23 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0713b8a5-2a3a-3ef0-abb7-89cebe68174c | -1.74004 | -52.03072 | 2025-11-23 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72480836-681a-3e2b-9cf3-d443d9acc5d2 | -5.867 | -45.27843 | 2025-11-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 576dae3d-4528-3a06-b5a5-a006df9cf6ba | -4.39383 | -45.73795 | 2025-11-23 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48c28496-9cf0-3b81-8aee-ed226c24bc22 | -2.86723 | -45.45141 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 4ed5eeb0-3bae-36a6-86de-bb180d5838a8 | -2.0265 | -47.15113 | 2025-11-23 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bb9ad9de-bd0b-3e0d-9277-e7e2ebf6bac5 | -1.73623 | -52.02536 | 2025-11-23 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f37d35f5-055b-355b-b39d-5955eb38a1e1 | -2.9872 | -44.42253 | 2025-11-23 04:25:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fda0d03c-252d-351a-9fec-aae28b5d59e6 | -10.53254 | -42.4375 | 2025-11-23 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b4e4cbb5-c8b8-3289-be84-5cdf73c40b0c | -16.14041 | -41.09475 | 2025-11-23 04:27:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d4e2e67e-3f08-3b7d-877d-642200424469 | -16.14322 | -41.09743 | 2025-11-23 04:27:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ac5edcc2-cb3a-37ac-9bf5-b3ab7041e79a | -9.5851 | -49.11724 | 2025-11-23 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 342b8903-5222-329e-b425-6af4539a3ed6 | -10.53648 | -42.43809 | 2025-11-23 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4adb715a-830a-322d-af94-18028cc35939 | -10.54509 | -42.43415 | 2025-11-23 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d9229c1f-4a73-3bc5-b115-8dfdb4eff3af | -10.5569 | -42.4359 | 2025-11-23 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af8f3165-45e1-3de1-8534-ca214ac5b546 | -10.54902 | -42.43473 | 2025-11-23 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a61f1e57-279f-3047-af24-119eb9f3ff93 | -22.34565 | -42.87442 | 2025-11-23 04:29:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a9f9c2b6-99df-368e-bd43-0120a7a9231f | -18.98007 | -42.34372 | 2025-11-23 04:29:00 | NOAA-21 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 54708b8e-5cc8-3f1a-87aa-e8b73da478d9 | -22.34813 | -42.87058 | 2025-11-23 04:29:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8498429a-cbe9-358e-858a-d0721d00ca5b | -18.98102 | -42.34719 | 2025-11-23 04:29:00 | NOAA-21 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a9b51ddd-c62e-3070-bf69-0ecde1277952 | -21.17335 | -53.26502 | 2025-11-23 04:29:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12f0692c-cc13-33bc-ba7f-5fa9cacc47d9 | -18.73242 | -42.81504 | 2025-11-23 04:29:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a35a5899-5017-3a67-8de2-b82f74220510 | -23.46063 | -47.25043 | 2025-11-23 04:29:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8d970ecd-b2fa-3612-8ad5-2c1157b5a3a0 | -18.50491 | -55.52687 | 2025-11-23 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c6d71f86-c664-34d0-a808-41e936f3ade6 | -22.34756 | -42.87587 | 2025-11-23 04:29:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 36478c89-9eea-3d6f-8cbc-83165f4bf436 | -18.98159 | -42.34252 | 2025-11-23 04:29:00 | NOAA-21 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b7921d88-928d-3fc9-ba7d-e266bcc02794 | -22.19622 | -56.745 | 2025-11-23 04:29:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 345c3136-85f7-3655-9a42-4ae9e6e1d383 | -18.50059 | -55.52597 | 2025-11-23 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 065111da-71b3-3fb5-ae41-0aab9356c2e3 | -21.93389 | -56.7791 | 2025-11-23 04:29:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5ada817-96bb-3c85-9411-c4dbd6fef7eb | -24.67364 | -51.44403 | 2025-11-23 04:31:00 | NOAA-21 | BOA VENTURA DE SÃO ROQUE | PARANÁ | Brasil | 4103040 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5c786b12-2ca0-374d-bfe0-31a0dec700b0 | -24.66968 | -51.44723 | 2025-11-23 04:31:00 | NOAA-21 | BOA VENTURA DE SÃO ROQUE | PARANÁ | Brasil | 4103040 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bb4f7314-5361-3042-914e-78f88813fa6b | -25.10976 | -52.72847 | 2025-11-23 04:31:00 | NOAA-21 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2162fcc4-50e0-3eb7-8193-ba6eb640efa2 | -27.20425 | -52.56337 | 2025-11-23 04:31:00 | NOAA-21 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d3750f16-a88e-307d-824d-f76122430f6d | -26.09242 | -52.16028 | 2025-11-23 04:31:00 | NOAA-21 | MANGUEIRINHA | PARANÁ | Brasil | 4114401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a67dd132-8dda-37c5-a6b6-c000d02d2fd6 | -31.82445 | -53.04637 | 2025-11-23 04:33:00 | NOAA-21 | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 31c6b975-fbf1-3c90-9ca8-6c8146d7ecb8 | -3.86136 | -51.1391 | 2025-11-23 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99c6c107-b29d-3032-b1a0-49806d84970f | -3.39206 | -47.19038 | 2025-11-23 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0be99cd-b507-3401-b7c1-a098638f855a | -1.67267 | -52.04688 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README8.md)
