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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5ff0d15-942e-3d52-927c-124fa6f13b03 | -1.4739 | -45.761299 | 2025-11-27 00:25:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5c1bb8f3-86df-30c2-b16f-de598c4d928a | -1.4814 | -45.7938 | 2025-11-27 00:25:00 | METOP-B | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 689427ac-6e42-3ca6-9d91-43b2809a5997 | -2.2253 | -53.6395 | 2025-11-27 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e34806b0-a25f-37b7-904c-ebe4432ea67d | -2.7166 | -53.171299 | 2025-11-27 00:25:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba1ac258-b4d4-3189-92d2-303ed66b42d1 | -3.4009 | -54.557301 | 2025-11-27 00:25:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d109b07d-f219-3503-9c75-32a67bb8c750 | -1.3342 | -53.1637 | 2025-11-27 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 199cb1e3-fa38-3c2d-a183-ea6d6894d9c3 | -4.5749 | -43.3017 | 2025-11-27 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| fcdaa226-6e11-32cb-944a-328262f48aa0 | -2.6919 | -47.4153 | 2025-11-27 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| fea52942-9318-3bf2-ba88-9d5e29af9e64 | -1.3678 | -53.0889 | 2025-11-27 00:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e37a04cf-7f35-385f-a27d-79f8403d2848 | -8.0132 | -43.1278 | 2025-11-27 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| 1324317a-8893-34aa-9293-0f7b0a3555a9 | -5.703 | -47.0532 | 2025-11-27 00:30:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 2ca2d64a-e24b-3966-8366-855eef06033a | -4.7204 | -46.4497 | 2025-11-27 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 166.7 |
| ebbb5f8d-36fe-374a-ba48-04f632af4341 | -8.051 | -43.1237 | 2025-11-27 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 364.4 |
| 0cbab6e3-98d8-3603-9a95-b108d43e09fe | -8.0318 | -43.1493 | 2025-11-27 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 399.6 |
| 19b353fb-4c6c-3e54-b2dc-30883231ce02 | -4.7018 | -46.4508 | 2025-11-27 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 85.2 |
| c1186c8f-2680-365a-b391-f28f53d1d981 | -3.5269 | -43.6828 | 2025-11-27 00:30:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 65507c62-4837-3078-92a0-c857aa8ee724 | -2.7105 | -47.3929 | 2025-11-27 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 510c20bc-161c-316c-881a-41c11e6ba347 | -8.0129 | -43.1513 | 2025-11-27 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.0 |
| 64de4b8e-158e-3293-a804-1dcb20889477 | -8.0507 | -43.1472 | 2025-11-27 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 379.8 |
| 054a8845-7c97-340e-8ee4-1f3269b0f1f6 | 3.1094 | -60.765 | 2025-11-27 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 6d471bfa-7a9c-3edd-8e99-e874074893f4 | -4.1297 | -45.7233 | 2025-11-27 00:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 75.2 |
| d06c6289-c4a7-39a1-b9ba-8e504761e2b8 | -1.3494 | -53.1094 | 2025-11-27 00:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| ef893729-62ae-3701-9d15-acf90262505d | -1.3678 | -53.1092 | 2025-11-27 00:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| bc8e6fd3-627e-36d3-b49b-1ab6d723fa02 | -3.8246 | -47.0454 | 2025-11-27 00:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| f75019dd-e23e-374d-b148-5f0b5c47ef00 | -3.2573 | -45.4035 | 2025-11-27 00:30:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 3cff081e-4e97-3de5-ac9f-05e6a43d1885 | -2.692 | -47.3935 | 2025-11-27 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 311b3f4a-27a7-3ca8-b8cb-662cc37555ba | -1.3494 | -53.0891 | 2025-11-27 00:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| c7b4b2bb-bbfa-3743-b6d0-a8594e36430f | -2.7104 | -47.4147 | 2025-11-27 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 15d4739b-b4c9-3daf-9d46-2f7c2acefce7 | -8.0321 | -43.1257 | 2025-11-27 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 362.9 |
| 90f71359-2a90-3cd3-bdc5-731fc9ac87c2 | -3.8061 | -47.0462 | 2025-11-27 00:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 88110e2a-dc29-321c-9892-ddeba564db6c | -4.7203 | -46.4719 | 2025-11-27 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 1514447f-c096-391f-8d91-e1257785aec8 | -3.5269 | -43.6828 | 2025-11-27 00:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 5d832fdb-188b-33c8-822d-ba2f83087b02 | -8.0318 | -43.1493 | 2025-11-27 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 305.5 |
| a174c8fd-ada6-3c27-bf1a-c4e71222da1b | -4.7203 | -46.4719 | 2025-11-27 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 6dad78c2-8e78-34d6-9f4b-7a95f512a376 | -4.7018 | -46.4508 | 2025-11-27 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 70b4b8ee-a51e-3fa2-8a55-056ac315985d | -8.051 | -43.1237 | 2025-11-27 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 249.1 |
| b69ecc62-e4f7-3e69-b0c2-04eab84903d7 | -5.703 | -47.0532 | 2025-11-27 00:40:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 1af264c3-4570-37d4-bd43-b1c15daba44f | -4.7204 | -46.4497 | 2025-11-27 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 155.2 |
| 43e6ce3a-ec90-3916-91f6-caaa09af71ac | -1.3494 | -53.0891 | 2025-11-27 00:40:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e6fcfb40-638a-3d97-a537-60655ac80a30 | -2.692 | -47.3935 | 2025-11-27 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 568b4053-30e2-30a0-809a-0b05e1128449 | -2.7105 | -47.3929 | 2025-11-27 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| f78e48e5-06e8-33b9-a5c1-9798ec0c9d8b | 3.1094 | -60.765 | 2025-11-27 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 2969b716-53f3-3257-b9ea-5e38a2b811e8 | -2.7104 | -47.4147 | 2025-11-27 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7de7d78f-1690-30ed-8668-14bde1681a80 | -4.5749 | -43.3017 | 2025-11-27 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 055ca7a3-0376-35e8-abff-a6533a29539d | -8.0507 | -43.1472 | 2025-11-27 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 312.3 |
| 306d8e94-fb6b-3142-ad89-34218afa1b86 | -2.6919 | -47.4153 | 2025-11-27 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| f88e30d5-f8af-3b87-8be4-aa684bce7ca3 | -8.0321 | -43.1257 | 2025-11-27 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 233.2 |
| 341cac2a-03f1-327a-9890-5b61fc2b18cb | -8.051 | -43.1237 | 2025-11-27 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 168.9 |
| 21d970b5-e754-3050-aeb6-ed8e74747d07 | -4.7018 | -46.4508 | 2025-11-27 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 6da1e3af-bb79-3b98-944a-f4bd568ed807 | -3.5269 | -43.6828 | 2025-11-27 00:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 58bf85f9-6869-3efd-9578-165eede820af | -8.0318 | -43.1493 | 2025-11-27 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 143.6 |
| 881f1c67-2279-3b9e-99e2-a7d9d784d89e | -4.7203 | -46.4719 | 2025-11-27 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 02688900-6629-3369-9955-2fdaaf1b8a13 | -4.7204 | -46.4497 | 2025-11-27 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 160.7 |
| 6994c379-2775-3828-882e-96b78a8470f2 | -10.0306 | -36.0801 | 2025-11-27 00:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.9 |
| 12705fb3-517f-3097-908d-69029627f409 | 3.1094 | -60.765 | 2025-11-27 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 54317664-7bf1-3a5e-abeb-ac2dd53fcc06 | -5.703 | -47.0532 | 2025-11-27 00:50:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 2c3c268e-70f2-3a7f-875c-682681afb7ac | -8.0321 | -43.1257 | 2025-11-27 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 133.3 |
| 189e0fe2-08d3-3e46-b3d6-30fcdd224016 | -8.0507 | -43.1472 | 2025-11-27 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 177.2 |
| 741bbfe0-da2e-35e4-a664-6c15deedbb55 | -4.5749 | -43.3017 | 2025-11-27 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 588d9d6a-5405-3203-92ef-8c2449b805ed | -20.408 | -57.9368 | 2025-11-27 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.5 |
| 6d2ff24d-e20f-3617-a747-01b7e310d49c | -4.5749 | -43.3017 | 2025-11-27 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| e1ac6e30-2bdd-3a2d-993f-2ae4b17629a1 | -20.4076 | -57.9577 | 2025-11-27 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.8 |
| 2b7a2aee-e9c6-3703-ae7a-d105c0d40f49 | -20.4279 | -57.955 | 2025-11-27 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.3 |
| 808550af-4eb2-3bb8-936a-7d8e9264e028 | -4.7204 | -46.4497 | 2025-11-27 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 149.7 |
| c9c468c7-7ed2-3609-b7b2-2445623aae9e | -5.703 | -47.0532 | 2025-11-27 01:00:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 481975c7-3af8-3e26-b067-dfa8190d9021 | -8.051 | -43.1237 | 2025-11-27 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.9 |
| 7508d900-1834-36e1-96b1-32d382c10c0d | -8.0318 | -43.1493 | 2025-11-27 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.5 |
| 60bb05e6-76ff-3d07-9143-74860f4a83a2 | -4.7203 | -46.4719 | 2025-11-27 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 13f1ed37-1856-342e-9963-7e5b3626cd53 | -3.5269 | -43.6828 | 2025-11-27 01:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 0b2d5444-f831-39c3-95d8-cc2d3a9dfdf6 | -8.0321 | -43.1257 | 2025-11-27 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| 994e77bf-5fce-35f9-b7f2-609028181d6d | -4.7018 | -46.4508 | 2025-11-27 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 6e55c5dc-982c-3dda-8855-dfdc0570da49 | -20.3874 | -57.9605 | 2025-11-27 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 2e227be7-3d45-39d4-b79f-81d78e8cd70e | -20.4283 | -57.9341 | 2025-11-27 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 45086b78-697f-3cc0-88fd-6c42a69c465e | -8.0507 | -43.1472 | 2025-11-27 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 1167c8de-5b80-38ad-b0c4-fbe3418bfd1c | -1.3627 | -53.080399 | 2025-11-27 01:08:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25d114f1-2d56-3a05-80fe-72afe14e481b | 2.8759 | -60.2556 | 2025-11-27 01:08:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 627b403e-b67d-3757-9560-b83c5656b203 | -2.9231 | -48.2076 | 2025-11-27 01:08:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c92cc7d1-bcc6-388b-9241-59477194dd00 | -3.2365 | -50.129299 | 2025-11-27 01:08:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b17f9106-76fa-3d53-9021-e64aa73f1f44 | 3.1221 | -60.750702 | 2025-11-27 01:08:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f7920876-e7f0-3f60-8ab8-8f87ffb2f6f8 | -3.7887 | -50.766701 | 2025-11-27 01:08:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdd72366-e77e-32bd-b601-c27598e436c9 | 2.8777 | -60.247799 | 2025-11-27 01:08:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 93fbc392-9894-3e11-b0bd-ebee5c6c6054 | -3.879 | -54.194401 | 2025-11-27 01:08:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5712bda-28b8-3ff7-96ee-f58017ae51e1 | -3.2394 | -50.141499 | 2025-11-27 01:08:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a567ef1-77df-3bd3-8dd5-4b343540ad5b | -2.7154 | -53.1796 | 2025-11-27 01:08:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48bc6a95-3213-304e-aeff-07e00e24b285 | -3.779 | -50.768902 | 2025-11-27 01:08:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eed7e23-a338-3d25-9e91-9d9fbe65a013 | -2.8987 | -50.484798 | 2025-11-27 01:08:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0980b36-0f9f-3938-ad95-d96a0e31fb77 | -3.7815 | -50.7798 | 2025-11-27 01:08:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b99cb48-ec09-3b59-bda1-83ffd092acbd | -2.7135 | -53.171398 | 2025-11-27 01:08:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 602d5101-4eff-3848-8cb1-1a2679570c62 | -1.3666 | -53.0975 | 2025-11-27 01:08:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0ce625b-83d8-38d4-8830-5fb12ef0245d | -1.3549 | -53.091202 | 2025-11-27 01:08:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84d9b15d-8711-3c07-8eed-743c9dc76ac1 | -3.0513 | -54.541401 | 2025-11-27 01:08:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db1e920c-5a4a-3db2-803f-d5c4dd6b0034 | -1.3647 | -53.089001 | 2025-11-27 01:08:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b5cc9fd-8b2c-3b87-a1d3-9766ee02e3a5 | -3.4079 | -54.5667 | 2025-11-27 01:08:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79ed16d6-c593-3a8c-a98f-cf68a2f66adf | -2.7945 | -52.9436 | 2025-11-27 01:08:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4a8b0e4-4ed0-36d8-94d9-0b1bea09c23c | 3.1182 | -60.7672 | 2025-11-27 01:08:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| af142835-592f-34ea-a8dc-8ba223d571fb | -1.3529 | -53.0826 | 2025-11-27 01:08:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfa0d079-0f16-3975-abad-7892869bd956 | -2.9014 | -50.496498 | 2025-11-27 01:08:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fd4b3cf-bdf8-3f6a-ae54-1de4994c755a | -2.7964 | -52.952 | 2025-11-27 01:08:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53e56555-26bb-3a94-b58c-2ae661e6e14f | -3.8226 | -50.170898 | 2025-11-27 01:08:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e009fb4-de67-379e-bcb4-ebb1e050842a | 3.1201 | -60.758999 | 2025-11-27 01:08:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
