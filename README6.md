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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6021b387-38ac-384e-bd18-32df231fbacc | -3.92188 | -47.69993 | 2025-11-04 03:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1738a124-a0c9-3dfa-aa17-ae671e24d6ea | -3.85997 | -38.55857 | 2025-11-04 03:40:00 | NOAA-21 | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e6beedf1-51b9-35b4-a0d3-aa13423dbd3d | -4.81438 | -42.73464 | 2025-11-04 03:40:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 3a863f3a-a921-39ab-8c8b-7366cbc5f80b | -5.61506 | -41.09156 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 07b5b822-b845-32a3-a7bd-e908632a4ab4 | -5.51238 | -41.11089 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c1624107-5ce9-32be-8b1a-68014721d73b | -4.58967 | -44.61123 | 2025-11-04 03:40:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34fbdaff-fbe7-3620-9b83-cfff6834c1ff | -4.47263 | -43.23452 | 2025-11-04 03:40:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3130a7d2-2b9d-3151-aa1c-142bb848b583 | -4.95246 | -44.90365 | 2025-11-04 03:40:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e541b946-4561-3f49-8018-a5db0ce9f992 | -4.81532 | -42.72902 | 2025-11-04 03:40:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 772b99ca-bd2f-3edb-8a4a-9ab45ce25577 | -4.58525 | -38.29501 | 2025-11-04 03:40:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ea8d711f-6848-3265-b8c9-0718462e57eb | -2.37931 | -47.72082 | 2025-11-04 03:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9af683b3-7c05-3d56-8704-7d9dcf1b3f5d | -4.609 | -45.75103 | 2025-11-04 03:40:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9bf1aa1-d805-3184-a0d6-103c5c6605b7 | -5.52774 | -41.12691 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| db3adf4a-af84-3625-afc9-bce24b9548bc | -5.53197 | -41.13094 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3dbf69e4-11ea-399c-a470-62711ebd5625 | -2.37225 | -47.71969 | 2025-11-04 03:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f62fc535-b062-362a-a4d6-94f39d7a6305 | -6.22918 | -37.42284 | 2025-11-04 03:40:00 | NOAA-21 | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b87ae637-7d03-31ab-b2d4-1a5abaf749e9 | -4.59008 | -40.97694 | 2025-11-04 03:40:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6f026346-9dc5-3eaf-acdb-aa21e5c93a89 | -2.87529 | -45.29605 | 2025-11-04 03:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 12a84d05-563a-3cde-8515-4dc4968c61d8 | -3.4362 | -42.54308 | 2025-11-04 03:40:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9db4de34-84bb-3785-a8ab-51c482fdca98 | -4.47367 | -43.22838 | 2025-11-04 03:40:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| bb95482b-79d9-3435-969f-f364910e874d | -5.62819 | -41.09352 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 99d19bd6-2afd-3d39-b7fb-d8fcb11a2676 | -4.96406 | -44.34406 | 2025-11-04 03:40:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d885170-050d-3d3f-ac33-0764c0f4a1b2 | -5.52704 | -41.13123 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9840af54-c8af-32fc-ba3f-6e4dc1709d51 | -4.48528 | -45.88362 | 2025-11-04 03:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c34eac3-af1a-34f9-8c76-e2a6c315c798 | -5.03347 | -43.61893 | 2025-11-04 03:40:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6e83acd9-1350-3034-a9bd-fea6abd217a0 | -4.57873 | -43.33968 | 2025-11-04 03:40:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a70850b5-4c17-3846-bc3f-d7d3428b8a83 | -3.40762 | -39.16946 | 2025-11-04 03:40:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c427f3e8-5539-3b6d-9fa7-de5157f0af74 | -4.90233 | -42.00151 | 2025-11-04 03:40:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2ec9e1e4-6eff-3e75-b09b-9c29ad2ebeb6 | -4.02609 | -45.46733 | 2025-11-04 03:40:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9786726a-3c43-3d44-b1b9-b91775e443a2 | -5.03404 | -43.61566 | 2025-11-04 03:40:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af63d8f0-aae9-3158-b173-d674e82caa9e | -4.47883 | -43.22922 | 2025-11-04 03:40:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77ec2224-2a9d-3837-a4fc-5af241415b9e | -2.8709 | -45.29394 | 2025-11-04 03:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 270d8ef0-38ab-38ca-86b4-7f92ee1f09c8 | -4.58396 | -38.29376 | 2025-11-04 03:40:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 480da909-6a92-306a-9740-ab53b61ee243 | -4.95815 | -44.90475 | 2025-11-04 03:40:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eabe0c0c-1f23-31d3-862f-6f20b4ff6809 | -4.1868 | -45.78438 | 2025-11-04 03:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59d3eb5d-085a-3d20-bfc3-efb28494d464 | -5.53141 | -41.13203 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e8602e3e-ddaf-3c5a-b878-5cb0b37f9db7 | -3.16098 | -46.58767 | 2025-11-04 03:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b907152d-c10c-3053-a0ac-34ac050ba41c | -5.62016 | -41.08785 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cb4ca953-01f2-3027-8562-02d8c448eac5 | -2.37106 | -47.72683 | 2025-11-04 03:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1e73e060-e46a-303a-be54-4d273bd0cd82 | -5.5327 | -41.09676 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 10d8de80-23be-338a-8b4c-decfa53b390a | -4.46748 | -43.23366 | 2025-11-04 03:40:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d4551aa6-40a5-3739-bc7a-fc64013f7659 | -2.87619 | -45.29935 | 2025-11-04 03:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7fe1bbfb-072f-34bb-8a36-ebfd9979a518 | -5.03817 | -43.62296 | 2025-11-04 03:40:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 589d545f-2d96-3f13-ad78-7a3b61eaa41a | -3.10228 | -41.38127 | 2025-11-04 03:40:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dafc908e-117c-3344-95b1-0d7dd74651c5 | -4.33697 | -45.51134 | 2025-11-04 03:40:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 895cb91c-3bc1-3f05-a47d-0272d6c4b1a0 | -4.0232 | -45.46228 | 2025-11-04 03:40:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e1056617-29cf-329c-a429-6fcb93771f61 | -3.95363 | -38.34096 | 2025-11-04 03:40:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7f0d8f19-4d01-307c-bbc9-b64a4ac01617 | -4.0292 | -45.46332 | 2025-11-04 03:40:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 022809b4-aeca-321d-a49d-6a62dd23431b | -4.0276 | -45.45837 | 2025-11-04 03:40:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3f5e97b-78e0-340b-a703-6ca1bdf30c01 | -5.53123 | -41.13528 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3cf75958-35f7-363e-9e77-5d9cf6d2a133 | -2.36945 | -47.72288 | 2025-11-04 03:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 344212b8-11a0-3267-ae91-3483ae97f0d1 | -4.61875 | -46.40718 | 2025-11-04 03:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 208c4033-23ab-3c6c-8519-5a1d36fc6c83 | -3.91501 | -47.69867 | 2025-11-04 03:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| a52c6761-9159-35f4-8479-e56402525cc2 | -4.61419 | -45.75713 | 2025-11-04 03:40:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47c68c05-e479-3353-99cb-bba4383b2d05 | -4.96446 | -44.90222 | 2025-11-04 03:40:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bbddc72a-98bd-38a6-8009-030b597c5a07 | -4.81498 | -42.73793 | 2025-11-04 03:40:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4ddd3752-abf6-3da9-bbb1-8879a65ab9a8 | -2.37652 | -47.72395 | 2025-11-04 03:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 23400e0f-2abe-320f-b1b6-1d138daf943a | -2.37532 | -47.73086 | 2025-11-04 03:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dc4af5c0-0098-348b-956d-9e8f54805be6 | -3.91733 | -47.68551 | 2025-11-04 03:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1646c9d1-1c20-3c2a-9272-6183f8ac1395 | -2.87604 | -45.29152 | 2025-11-04 03:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 73739b85-30be-3829-9509-87dc71edb718 | -4.19368 | -45.78329 | 2025-11-04 03:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67b58e4c-a5c9-3872-ac55-ee5f0c2dea79 | -5.03873 | -43.61972 | 2025-11-04 03:40:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b24cc23c-cc93-35f7-826a-51e7526ef19b | -3.45061 | -39.23265 | 2025-11-04 03:40:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0cb2a733-a0ae-3cc7-9dad-6d465cc3a835 | -4.60058 | -45.58517 | 2025-11-04 03:40:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1949c7a-91aa-310b-ac20-dc89f1f3cff8 | -5.51748 | -41.10727 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 93ac141c-30ae-38e4-91e2-da45a35d6dea | -5.20526 | -35.6205 | 2025-11-04 03:40:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 31d7d269-6e39-3559-907e-e9a4f1d31027 | -5.62454 | -41.08851 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 078e8ad8-27f5-3148-b4dd-0666cd49cd6f | -4.81694 | -42.72669 | 2025-11-04 03:40:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 36.7 |
| a98aae20-a533-3094-8b22-e6c53b73af82 | -3.0711 | -47.77658 | 2025-11-04 03:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 81091457-d341-30bc-9e95-142528fc28fb | -3.92305 | -47.69325 | 2025-11-04 03:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 35c0d211-bf05-3cf0-ba38-e9e6dbf67c6b | -4.33473 | -45.51031 | 2025-11-04 03:40:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7eebacc1-36ce-368a-a7e0-ddf566baca36 | -2.86923 | -45.2951 | 2025-11-04 03:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5a368727-332d-36d1-a919-13746b3f1417 | -5.51167 | -41.11524 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e8a5b5be-37bc-3018-aae0-6bf3d7627715 | -4.62247 | -46.40494 | 2025-11-04 03:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84bdc0ba-6122-3fec-918d-0bcf6eaef2e0 | -4.2343 | -40.69806 | 2025-11-04 03:40:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8aafe161-2b79-3e36-87db-e5ddba49b249 | -5.52536 | -41.08675 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e7b380b6-c4a4-3089-a93a-d73c95c934fe | -2.4969 | -45.97273 | 2025-11-04 03:40:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 728fbda8-0644-325e-8a2e-aad0ce2e3807 | -3.4312 | -42.54225 | 2025-11-04 03:40:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c801a36-cdfc-36e6-bb8a-466f56fed126 | -4.48576 | -45.88103 | 2025-11-04 03:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11f1b02b-c420-3440-987e-d00b11671e8f | -5.52835 | -41.12584 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a1cea979-af73-382c-99cd-46f365c2f30f | -4.03285 | -45.46391 | 2025-11-04 03:40:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6c5303f4-e30b-3f62-bbf4-2830f2b8e41e | -4.81596 | -42.73233 | 2025-11-04 03:40:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 36.7 |
| f77f4f18-2529-3dc3-be1a-0407f00b6a8a | -4.02085 | -45.46178 | 2025-11-04 03:40:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba79b7be-fdde-3a70-a7ae-99f6dacaca45 | -5.33198 | -35.55085 | 2025-11-04 03:40:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4b44f314-221e-38ab-94e7-f5b1830d8688 | -4.02399 | -45.45785 | 2025-11-04 03:40:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 602dc9c2-35c4-30b8-8491-b9fc6fe4a7ad | -4.45392 | -45.70376 | 2025-11-04 03:40:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7ec221d-1b09-35ae-a65e-4b6365e69f84 | -4.54231 | -40.14951 | 2025-11-04 03:40:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7163c7a3-a6e2-3e4a-9418-088ad49d69ad | -5.2282 | -38.60252 | 2025-11-04 03:40:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bb17aefb-8619-3ac9-8289-7cf74bd23eec | -5.52337 | -41.12616 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bce96382-2b6b-3365-8bc2-bb2257414ed9 | -4.02841 | -45.4678 | 2025-11-04 03:40:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 16775e2a-137f-3610-8b50-6f05c0fc6484 | -4.9575 | -44.90848 | 2025-11-04 03:40:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 654b0c76-e4dc-3b16-9cfa-74dd9e8892cf | -5.22105 | -43.75218 | 2025-11-04 03:40:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ec6a531-f9dd-3bc9-8304-06821038d139 | -2.87453 | -45.3006 | 2025-11-04 03:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7a28a6ab-e08d-3025-bfa1-1028079b707f | -4.03209 | -45.46839 | 2025-11-04 03:40:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ea7603f3-5cfe-35ad-bee9-7ead87e2ecda | -4.95311 | -44.89991 | 2025-11-04 03:40:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7140e15-a279-3a49-8c32-4b524e9d3c93 | -4.96381 | -44.90598 | 2025-11-04 03:40:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4be536dc-9dd1-335d-851d-1ddd7e02c2c8 | -2.87012 | -45.29842 | 2025-11-04 03:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 816bb08a-d08f-3007-9a51-07cd2a0c155a | -4.62161 | -46.40992 | 2025-11-04 03:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfe2748e-ca0b-3e0a-a600-bccf3ffcf141 | -4.93304 | -43.42045 | 2025-11-04 03:40:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e722b657-dc61-3a83-9d26-4981f9f02f96 | -2.86847 | -45.29964 | 2025-11-04 03:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README7.md)
