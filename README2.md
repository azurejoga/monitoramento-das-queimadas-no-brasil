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
| 678adb78-c297-3628-b490-97c324ba1d24 | -5.6363 | -43.9027 | 2025-09-24 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| ceb33f85-ef91-37d7-87fc-e39cc2b48e70 | -5.6393 | -45.7239 | 2025-09-24 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 200.9 |
| a8550185-3c52-37c0-a674-dc3e458ceb00 | -5.6207 | -45.7252 | 2025-09-24 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 962e1e25-52a4-3dfb-8def-4bd0a740cfc4 | -14.2877 | -41.8157 | 2025-09-24 00:40:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 149.4 |
| 1e388b6a-8e3c-3927-b83e-aac825161b5f | -11.0253 | -45.9046 | 2025-09-24 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| e449dce8-4458-32b2-954a-7b438c57e142 | -6.4319 | -43.0707 | 2025-09-24 00:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0f551295-c399-3e54-bc7f-18f60a475c97 | -14.3061 | -41.8612 | 2025-09-24 00:40:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 116.1 |
| 51d9cf6b-bd3e-33ef-81b3-65e601a2f895 | -14.2871 | -41.8405 | 2025-09-24 00:40:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 802.0 |
| 4128872b-6056-3dba-9812-03c35533d3d2 | -5.8352 | -42.6501 | 2025-09-24 00:40:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| fb1523f5-ccc5-31e7-a053-2ff43ca782df | -5.6361 | -43.9258 | 2025-09-24 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 1cd7f2ad-801f-3747-b861-aebb2b826b92 | -7.3847 | -47.0378 | 2025-09-24 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 6fe5109f-2737-3fba-8f67-fbe12b1f23cd | -14.3073 | -41.8117 | 2025-09-24 00:40:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 133.9 |
| c40a2e8d-32c9-378b-876c-a6beac963bc0 | -14.3067 | -41.8364 | 2025-09-24 00:40:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 512.8 |
| f361c634-9c55-3c5c-a1b8-e673389d1377 | -14.2865 | -41.8652 | 2025-09-24 00:40:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 179.0 |
| f6a1ca45-316c-3d97-934f-99542a722589 | -10.9944 | -44.3217 | 2025-09-24 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| c49c2286-0113-392b-85f5-108a7f07c752 | -10.9728 | -45.6156 | 2025-09-24 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| ee4ede08-1fdc-3d21-ba45-2ab6268893c4 | -11.0066 | -45.8844 | 2025-09-24 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 28885eec-fafd-3f48-ad8b-3e21904b8080 | -11.0062 | -45.9072 | 2025-09-24 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 72f628e7-6881-3e94-9e5d-b241ae7240c6 | -14.3061 | -41.8612 | 2025-09-24 00:50:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 113.3 |
| 8fd47acb-966a-3266-a489-340d6442e4ee | -6.4129 | -43.0958 | 2025-09-24 00:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 120.4 |
| f9db5878-67b4-3f58-8c42-ff376b8b22d0 | -10.9944 | -44.3217 | 2025-09-24 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e3a403fc-e2ff-324a-b62b-7208aaf7fdc7 | -5.854 | -42.6486 | 2025-09-24 00:50:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 141.7 |
| 5e33b325-67af-3d53-8994-35850d61ae0f | -10.9732 | -45.5927 | 2025-09-24 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| b0ad8dc5-0c36-30e8-9431-cfe64c2641b1 | -6.4131 | -43.0724 | 2025-09-24 00:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 5e056866-0f6f-3740-8eea-6b001c9ef138 | -14.2865 | -41.8652 | 2025-09-24 00:50:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 136.8 |
| ceafffb9-fe25-319b-b23f-671967d90f0a | -6.4319 | -43.0707 | 2025-09-24 00:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 99b75a3e-a2d4-3175-87c7-0fe177fcabed | -5.8352 | -42.6501 | 2025-09-24 00:50:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| a9674acc-9a89-347c-b032-5e9e431ebc9a | -5.6207 | -45.7252 | 2025-09-24 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 3ccc56ba-012b-3117-a812-6f1cd40bcb15 | -14.2871 | -41.8405 | 2025-09-24 00:50:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 374.7 |
| ee3c01c9-7b85-3fa7-99d5-f35765246a02 | -6.4317 | -43.0942 | 2025-09-24 00:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 141.7 |
| b9568360-749b-3b94-89c9-cfc0081856e3 | -5.6392 | -45.7463 | 2025-09-24 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 82186198-2772-3e08-949f-5d185b70e362 | -5.6363 | -43.9027 | 2025-09-24 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| ef904df7-8d7f-3a54-b599-6dc1dc7be7a9 | -14.3073 | -41.8117 | 2025-09-24 00:50:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 117.9 |
| 31aaa216-8206-307f-81ba-74f8eea78e39 | -14.3067 | -41.8364 | 2025-09-24 00:50:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 331.5 |
| 97b92762-6423-3e0d-8eef-0124fd5f8797 | -11.6508 | -50.9875 | 2025-09-24 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 51a63d1a-17f6-3629-a13c-5322b2253ab2 | -11.0257 | -45.8819 | 2025-09-24 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 6044d166-1837-3f1c-82a8-659aa112bd0a | -5.6361 | -43.9258 | 2025-09-24 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 1cb82b7b-9eec-3823-8ced-60cf184b27fe | -14.2877 | -41.8157 | 2025-09-24 00:50:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 46efc5ed-14db-3b50-ae21-2ea2db29e637 | -5.6393 | -45.7239 | 2025-09-24 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 162.6 |
| f240b053-f33a-3ec6-a5cd-c441c4e91da5 | -6.4317 | -43.0942 | 2025-09-24 01:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 537c133d-4c82-3ce2-8cee-c55a06f34fdc | -5.6363 | -43.9027 | 2025-09-24 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 39dee7e4-79d4-346a-8314-c9df0e2c7b91 | -5.6392 | -45.7463 | 2025-09-24 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 44322449-7e51-37d8-95df-bc91166e1f63 | -6.4131 | -43.0724 | 2025-09-24 01:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 132394bc-2c8f-39af-8de2-8434ef66528d | -11.0062 | -45.9072 | 2025-09-24 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 70e8b28f-b5d7-35aa-b2ce-6bc15a818c1f | -14.3067 | -41.8364 | 2025-09-24 01:00:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 256.6 |
| cf27c2fe-f3d1-3017-885a-f41037060762 | -5.8352 | -42.6501 | 2025-09-24 01:00:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 2c3bd0bf-e16c-3ca6-8a53-dc2dbdc27f04 | -7.3659 | -47.0394 | 2025-09-24 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 7839a2e1-4aa1-3486-ac95-ae93dec34018 | -6.4129 | -43.0958 | 2025-09-24 01:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 9d3bde65-cca2-3063-8c30-f1a03c472948 | -5.854 | -42.6486 | 2025-09-24 01:00:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 8b81579c-0b13-3ca4-929f-a4fbc038dbd3 | -6.4319 | -43.0707 | 2025-09-24 01:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 4998ae23-5de0-32f6-aa37-cdc8bf199b72 | -11.0257 | -45.8819 | 2025-09-24 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 06552fb6-c505-381f-8a86-f3bba298a26b | -14.2871 | -41.8405 | 2025-09-24 01:00:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 266.2 |
| 4f3ad241-f269-3054-a3b6-c1440acb5b1d | -5.6361 | -43.9258 | 2025-09-24 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 83d4dca4-e586-3af4-be27-caa04a0d24d4 | -5.6393 | -45.7239 | 2025-09-24 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 749031ed-2d58-32df-89bd-313854a64f20 | -11.0066 | -45.8844 | 2025-09-24 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 190.8 |
| 163b847a-e762-3943-8bd5-660cd4bd7f43 | -11.0253 | -45.9046 | 2025-09-24 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| caa4a5aa-447f-3147-adbb-707f48781487 | -5.6207 | -45.7252 | 2025-09-24 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| b4ae26c7-dd2c-3e6d-a995-dc68218c6fe0 | -14.3073 | -41.8117 | 2025-09-24 01:00:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 88.5 |
| ee8200c0-e0d0-3e54-b0f4-4ad6d1e3d6ef | -5.854 | -42.6486 | 2025-09-24 01:10:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 1a15a93d-10fc-3819-8ba3-cbd32d1240f9 | -14.3067 | -41.8364 | 2025-09-24 01:10:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 187.0 |
| 631cc0a0-5b5a-3351-863f-5c9734bfbecb | -6.4317 | -43.0942 | 2025-09-24 01:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 421b5d6e-7005-3dfa-8134-6eebb606ef94 | -5.6392 | -45.7463 | 2025-09-24 01:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 1887f51d-8091-38b9-965e-bb7879d21f54 | -5.6393 | -45.7239 | 2025-09-24 01:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| f43a375e-6db1-3f58-aabf-cb1e0b2a6d00 | -6.4131 | -43.0724 | 2025-09-24 01:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| a590dd3b-13fd-3ce2-9564-c46fbe5f15d4 | -5.8352 | -42.6501 | 2025-09-24 01:10:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 62c11cf9-02e7-3967-a84a-1f0a0ee1abd4 | -6.4319 | -43.0707 | 2025-09-24 01:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| bb031b66-0147-3da7-9c2b-898a0d7b30d8 | -5.6207 | -45.7252 | 2025-09-24 01:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 71f49a1d-9eee-36c7-b323-9bb50ca6883b | -11.0062 | -45.9072 | 2025-09-24 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 65ddd1f1-4255-3034-9523-0656ec3b722b | -11.0066 | -45.8844 | 2025-09-24 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 8db53426-3d65-3998-8485-59ab026f48c0 | -14.2871 | -41.8405 | 2025-09-24 01:10:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 191.6 |
| a444d21d-4c7e-3a6d-87fc-eb91f0a6b722 | -6.4129 | -43.0958 | 2025-09-24 01:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| f090494b-fe34-3023-8343-2f98ed6f9be6 | -14.3073 | -41.8117 | 2025-09-24 01:10:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 5143410c-ed29-397b-be13-ffd9f3219175 | -10.5788 | -44.0767 | 2025-09-24 01:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| fee1035c-f3f4-340f-8b64-c9e2e719b1bd | -5.6361 | -43.9258 | 2025-09-24 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 41418beb-111a-3e12-9581-f63f1f64a973 | -5.854 | -42.6486 | 2025-09-24 01:20:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 73ffe754-044a-322c-8cfc-00d67374823c | -6.4129 | -43.0958 | 2025-09-24 01:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| ae7a6a03-8082-3eb2-84e6-8d3e94d7c022 | -14.3067 | -41.8364 | 2025-09-24 01:20:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 167.2 |
| 8444b291-3b9e-396f-9d38-506fafcdf505 | -14.2871 | -41.8405 | 2025-09-24 01:20:00 | GOES-19 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 144.5 |
| 76837d9e-82fa-36bd-ad29-144ccad08f76 | -5.6393 | -45.7239 | 2025-09-24 01:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 19674093-316b-3dae-bc76-6b1cb8abaff1 | -5.6361 | -43.9258 | 2025-09-24 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| d239fb0e-d8f9-3718-aff8-6f6fc63bb3a9 | -6.4131 | -43.0724 | 2025-09-24 01:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 0ba1b890-0d59-353c-9223-8c6ad5a769d1 | -6.4317 | -43.0942 | 2025-09-24 01:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| f32c0764-d9a3-3898-a269-72d49614a076 | -5.6392 | -45.7463 | 2025-09-24 01:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 7cf7ecd6-e2c7-3574-a4cd-43dfb772b7cf | -6.4319 | -43.0707 | 2025-09-24 01:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 63d4018f-9d13-38d0-8fb3-98e5fb185427 | -5.6207 | -45.7252 | 2025-09-24 01:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f1bc3d8d-4367-3096-b0f6-3ad529d3890b | -17.95691 | -55.86077 | 2025-09-24 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 7adc75ff-6c18-3fb5-8412-58d3cf05311c | -15.82791 | -59.59583 | 2025-09-24 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e1554c22-3378-3cf3-a9ee-6e7d3312c3a9 | -15.83721 | -59.59433 | 2025-09-24 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 6363b825-0afc-3e46-a8eb-bd520c46859f | -15.27739 | -59.42574 | 2025-09-24 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dd52350a-fb82-3af5-a7a1-5870256353a5 | -15.26795 | -59.42719 | 2025-09-24 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a1a1a339-c97f-3c12-b6ca-35c1fd1835bd | -15.35521 | -59.19935 | 2025-09-24 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 42f77b83-c886-362f-8e23-41bc6a438eec | -15.89402 | -59.35867 | 2025-09-24 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fe493a1f-637a-3c52-8e81-f6628054cf4c | -15.96229 | -59.49489 | 2025-09-24 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 72b3a884-78af-339c-81dc-044ab4f45051 | -15.3536 | -59.1886 | 2025-09-24 01:28:00 | TERRA_M-M | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 499b4082-7dcb-369f-bc71-66e802f97382 | -15.9638 | -59.50517 | 2025-09-24 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 51a5ce5b-2a0d-38f2-bfac-54598ca3295d | -15.78424 | -59.47345 | 2025-09-24 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8cf48a6d-b121-31af-892c-ce51a85a2382 | -15.36155 | -59.17627 | 2025-09-24 01:28:00 | TERRA_M-M | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 95ba2026-66e7-3a56-9c3c-1bf0b2bbf807 | -17.94541 | -55.86295 | 2025-09-24 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 1fc9ddb5-19f1-3af5-9b35-5878b4c5a9d9 | -15.78571 | -59.48336 | 2025-09-24 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a998cd6c-bbb5-31aa-80d4-72d1f067dd48 | -5.6393 | -45.7239 | 2025-09-24 01:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |


[Clique aqui para ver as próximas entradas](README3.md)
