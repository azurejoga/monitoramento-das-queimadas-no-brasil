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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e418cba3-516e-3452-9cda-c56f127693fd | -4.18632 | -40.68805 | 2024-10-27 04:00:00 | NPP-375D | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 45f698ee-b58c-3313-992f-7e7fc1229f8a | -4.18295 | -40.68747 | 2024-10-27 04:00:00 | NPP-375D | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2a0dc906-dd8e-3b0c-bb7b-5175bf23b5ff | -4.06449 | -40.48338 | 2024-10-27 04:00:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| af028294-3065-3529-acd8-b7e19036972f | -3.94531 | -40.97236 | 2024-10-27 04:00:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f3d1e939-95a8-38cb-9ecd-c7d58da3fbb0 | -6.5536 | -40.51099 | 2024-10-27 04:00:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 15bc69b5-9311-3581-8b87-25e059cfc858 | -6.55027 | -40.51047 | 2024-10-27 04:00:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 92f5ff16-1fb3-3d75-b912-4cd9ae1f0669 | -6.29232 | -41.91028 | 2024-10-27 04:00:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c889a402-602b-307a-8a26-efaec9e5c020 | -6.28947 | -41.90598 | 2024-10-27 04:00:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 151a8dbf-bdfc-3f55-9fbe-a3cd1e0807b1 | -6.28886 | -41.90975 | 2024-10-27 04:00:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6d9ac63a-97ab-34b9-a2bd-8a5e8d396981 | -6.19368 | -41.8294 | 2024-10-27 04:00:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 95a0e4e3-0c4c-3500-8991-b7a7dc67aff8 | -5.73056 | -41.72989 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4a0c210c-49fe-37c6-baac-688e35d8c9bc | -5.69601 | -41.64407 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c29e5803-0eb0-3a5b-86a3-916e7785d0c7 | -5.69541 | -41.64781 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7a4cd917-63cc-387a-8a5b-7957d62ca03c | -5.69316 | -41.63977 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b4dcdf3-3cc4-3c19-900b-e439501b8385 | -5.69257 | -41.64351 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5821ef14-d2fc-30b4-92d7-11f4f4494cde | -5.69197 | -41.64726 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2cdb89aa-e2d7-3378-8c3f-b43819ce856f | -5.69136 | -41.65101 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 106ec3d1-db9c-38fb-ab01-55fa874a5426 | -5.68913 | -41.64296 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 14f570a3-c4f0-32de-b108-fdcfd3609bc0 | -5.68852 | -41.64671 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d419eea6-fd6a-37fb-8b98-52256501bbda | -5.65886 | -41.83148 | 2024-10-27 04:00:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3fd84b4f-a766-31ce-a8c0-8a980338a02c | -5.65826 | -41.83526 | 2024-10-27 04:00:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9d9f5937-d665-3cdb-9b56-20d80e2dd844 | -5.65479 | -41.83472 | 2024-10-27 04:00:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f1d14a4c-5aa6-38bf-aab1-6b95f5ae0e85 | -5.65132 | -41.83418 | 2024-10-27 04:00:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9bd9d9cc-ed55-3a33-88ee-04fe36cdd315 | -5.61069 | -41.73443 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8c834206-f667-3f9c-83c4-a4215b4394e8 | -5.60893 | -41.73438 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a8e43e9c-b36d-397d-8ac1-a0c2010d8413 | -5.60022 | -41.74463 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 160695c4-f881-3770-bb8e-e34501d2ee25 | -5.59961 | -41.74843 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3441a8f6-c883-3352-a712-884b3c5e39da | -5.59796 | -41.73651 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0a1db060-500f-309f-adb9-cb84f4e74c36 | -5.59736 | -41.7403 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dfd62095-49bd-386f-99cb-7edf7de71fa1 | -5.59676 | -41.74408 | 2024-10-27 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d49e6bd-e48f-322b-8671-23ccdf9995a2 | -5.48695 | -40.79023 | 2024-10-27 04:00:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a52c74ae-d96b-3aa3-bfc2-431a0d6c2135 | -5.44736 | -41.62425 | 2024-10-27 04:00:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e0dcd047-93dd-38c5-9a88-8c3581120f29 | -5.44676 | -41.62799 | 2024-10-27 04:00:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67cf3e11-f1b1-386f-8ebe-65b845f4edcd | -5.27061 | -41.2247 | 2024-10-27 04:00:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5960ed16-28e4-353e-9025-0404cd647750 | -7.25848 | -41.22431 | 2024-10-27 04:00:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d8b865bb-3ec6-377c-be91-dbd815deba9c | -7.25455 | -41.22734 | 2024-10-27 04:00:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ce94757c-c4dc-339d-abf1-e432c2f77a73 | -7.25118 | -41.22683 | 2024-10-27 04:00:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 664cb9a4-e8cb-3472-a49a-e62f1151dd97 | -7.25061 | -41.23039 | 2024-10-27 04:00:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 127a0416-022d-3ff5-ac8a-c161d5f9aef3 | -7.24838 | -41.22275 | 2024-10-27 04:00:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6c944213-6bdd-36cd-9b53-a965839279db | -7.24781 | -41.22631 | 2024-10-27 04:00:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b3de5706-4fe4-3f80-a93a-1271390b0ffb | -7.23526 | -40.8644 | 2024-10-27 04:00:00 | NPP-375D | ALEGRETE DO PIAUÍ | PIAUÍ | Brasil | 2200277 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 26aadbeb-a413-3807-8820-3eb41ab5d011 | -7.00251 | -41.29724 | 2024-10-27 04:00:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7979552f-a2c7-3c44-ad67-816e704ad4b9 | -7.00019 | -41.31166 | 2024-10-27 04:00:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0bc2bdc4-fc3c-366d-95b5-d3739caf2c1d | -6.99961 | -41.31527 | 2024-10-27 04:00:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 112ac8ec-b766-370d-884f-7872e6dbb4bd | -6.96058 | -41.31693 | 2024-10-27 04:00:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6bdc4c0a-5fd6-303c-a9e6-384d51bcf054 | -6.9572 | -41.31638 | 2024-10-27 04:00:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 52377982-9747-371e-94c6-cb37540d735f | -6.95433 | -41.33434 | 2024-10-27 04:00:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7883c400-ce74-3309-88ed-04052fb383b6 | -6.95376 | -41.33792 | 2024-10-27 04:00:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 10045a9e-6c71-37a6-a746-c283af8e45b7 | -6.95325 | -41.31944 | 2024-10-27 04:00:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b43fd367-490d-38ae-b55b-3baf5d917ac8 | -6.95096 | -41.33379 | 2024-10-27 04:00:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 85184142-a2a1-3807-a51f-06a51348d1de | -6.94929 | -41.3225 | 2024-10-27 04:00:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e378d699-1ece-3f1a-968b-0da39746e37c | -6.71444 | -41.11209 | 2024-10-27 04:00:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 22779677-ebfb-39fd-a1a1-de2f409d1ba8 | -6.71387 | -41.11567 | 2024-10-27 04:00:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a6aecc5f-2b91-333e-baad-909a2f81e38e | -6.70772 | -41.11098 | 2024-10-27 04:00:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3a03221e-7326-38cb-9a0a-2b0a05e962d9 | -6.69248 | -40.89354 | 2024-10-27 04:00:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c5a4072-4f06-3edb-a9f2-4527772c5452 | -6.69136 | -40.9006 | 2024-10-27 04:00:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 54261677-fc35-3b27-b8c5-b5955e273d1a | -6.68913 | -40.893 | 2024-10-27 04:00:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 113a1490-c587-3aa9-bb9d-feb2a1a4c6fc | -6.68635 | -40.88893 | 2024-10-27 04:00:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 456bfa45-d6ed-355b-b9c5-3d22962d5d78 | -6.68418 | -41.23589 | 2024-10-27 04:00:00 | NPP-375D | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ebb700e3-9664-33fc-8d97-be1366a0d04f | -6.68244 | -40.89192 | 2024-10-27 04:00:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f2b92857-0fe7-3bc1-84a9-2ba6fc83e1d7 | -6.68187 | -40.89545 | 2024-10-27 04:00:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9a2a894c-1ca7-39d3-a421-c41445bc16c6 | -6.68131 | -40.89898 | 2024-10-27 04:00:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| febacb1c-c382-3f47-a6fc-706a7d461895 | -6.68019 | -40.90605 | 2024-10-27 04:00:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 85fb4811-9ccd-3fe1-b287-76c4c1539491 | -6.67963 | -40.90958 | 2024-10-27 04:00:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2836e68d-5844-3005-92df-d96dd6b4b010 | -6.67796 | -40.89844 | 2024-10-27 04:00:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2854a8f4-a8a0-39f0-aae6-77e616dc6b99 | -6.6774 | -40.90197 | 2024-10-27 04:00:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f2686f62-a53c-3e95-b8cb-bd533593a7af | -6.67684 | -40.90551 | 2024-10-27 04:00:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 05321529-a8d1-3066-8275-7f36e843720a | -8.90344 | -41.44316 | 2024-10-27 04:00:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8c84c98c-ee27-37fc-a34a-bc2d8d6d9d2b | -8.67219 | -41.03967 | 2024-10-27 04:00:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9e8ee56c-70b6-3b8a-980c-348e610a0d42 | -8.35208 | -42.26202 | 2024-10-27 04:00:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| ce69dba1-a718-334d-b8d4-c99cba915060 | -8.34864 | -42.26146 | 2024-10-27 04:00:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 8202d17e-7b8f-3137-b7e5-4306b19a1828 | -8.29593 | -40.96143 | 2024-10-27 04:00:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 75dc2cb8-571f-303c-a477-1cb65473068c | -8.2926 | -40.9609 | 2024-10-27 04:00:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0188ecff-7007-35fe-a8e6-a1bf0b4d9f7f | -4.84757 | -42.95255 | 2024-10-27 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dadfe3a-67fa-39d7-bdae-bd8770dcc7f9 | -4.33986 | -43.03906 | 2024-10-27 04:00:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 410cacf8-654a-3e31-9e47-1aa24d0aaf4e | -4.33614 | -43.03848 | 2024-10-27 04:00:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7e8a7d33-08fd-3bf6-b06d-e4147421fecb | -4.92176 | -41.97323 | 2024-10-27 04:00:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ef605479-3666-3044-bdca-7d82410109d6 | -4.92151 | -41.97429 | 2024-10-27 04:00:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b5cc9e40-0fa0-3711-8989-2cc66d88c3f2 | -4.8514 | -42.46953 | 2024-10-27 04:00:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 37841696-b9a2-3f47-a0e8-17d469a68c0a | -4.42473 | -42.5202 | 2024-10-27 04:00:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8a03f0be-50c0-3c45-be83-d76d93fa22d1 | -4.42255 | -41.758 | 2024-10-27 04:00:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7c814af0-4179-3290-b83c-29a9da772ec8 | -4.42111 | -42.51963 | 2024-10-27 04:00:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 340727b6-ca07-3cec-a3d2-4e7d0546d952 | -4.42043 | -42.52378 | 2024-10-27 04:00:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 78f1cde1-fd85-36d7-9aba-4ab2abc8dbf4 | -4.41975 | -42.52795 | 2024-10-27 04:00:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1a8b0850-a096-3854-b082-eaca91453e58 | -4.41681 | -42.52321 | 2024-10-27 04:00:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 83244884-4235-342b-9399-e64bf8f59ff2 | -4.41613 | -42.52737 | 2024-10-27 04:00:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9d454746-2f0c-37af-a49b-9d399fef8861 | -5.5975 | -42.97559 | 2024-10-27 04:00:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e00fb6bd-d806-3a8e-a105-1cf180bf3046 | -5.67719 | -43.31542 | 2024-10-27 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a343f19-c290-3e6a-9119-8a28e19a73b0 | -5.67532 | -43.31308 | 2024-10-27 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 651fcff2-93a6-3e7a-8685-a62822685adc | -5.481 | -43.34066 | 2024-10-27 04:00:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 96fed029-0959-324d-b9a2-6c44e99b101f | -5.30106 | -42.94017 | 2024-10-27 04:00:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92bfa88f-2b57-34f1-b115-dc7c2f9ea8ca | -5.29741 | -42.93954 | 2024-10-27 04:00:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dfd2aab-bd28-3007-942f-a73dafbc1256 | -5.29375 | -42.93891 | 2024-10-27 04:00:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9bbaf41-5230-3efd-8e88-1788d9633a0c | -6.29018 | -42.3718 | 2024-10-27 04:00:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cd9af893-8248-347f-94a0-6ff7650e28ae | -6.19382 | -42.43018 | 2024-10-27 04:00:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4efe4cf3-54dc-3bbc-be48-10f0001b75ef | -6.11663 | -42.50872 | 2024-10-27 04:00:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c334017b-a70f-3c88-b527-0f004782651a | -6.06284 | -42.84306 | 2024-10-27 04:00:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8d7f7a0e-4565-3886-961a-edfb2f139a28 | -6.06218 | -42.84719 | 2024-10-27 04:00:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b384d035-3f31-33a6-b093-c0c536004768 | -6.05211 | -42.72676 | 2024-10-27 04:00:00 | NPP-375D | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6ec1d686-2920-3a5c-8729-e9e807d09772 | -5.97269 | -42.1237 | 2024-10-27 04:00:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |


[Clique aqui para ver as próximas entradas](README32.md)
