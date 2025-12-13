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
| 56ad4eab-6cec-3ce6-935a-ada22fae1e32 | -2.79275 | -45.21449 | 2025-12-13 03:59:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 373ae212-2f42-3062-9fc8-8b94413b13a6 | -2.63497 | -46.94931 | 2025-12-13 03:59:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f7816f1-9d80-302d-b917-63b9febed46d | -2.81633 | -45.26019 | 2025-12-13 03:59:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6604be36-0290-358f-9b5c-85ddba1dfa9c | -1.72423 | -47.15521 | 2025-12-13 03:59:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 883442e0-af2a-31ef-8721-433e7776a75b | -3.20507 | -41.85707 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 9761108c-849b-36a5-b8e2-4dc928c1c612 | -2.66777 | -46.89983 | 2025-12-13 03:59:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0ad36d9e-fa72-3da2-84c6-069381e87d95 | -4.33242 | -39.14763 | 2025-12-13 03:59:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a5677eb3-53cb-3ae5-9bbe-fef344dec7db | -2.51117 | -47.81369 | 2025-12-13 03:59:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 549d4105-0968-3eef-b5d7-2d0c577d8e19 | -2.41445 | -45.05746 | 2025-12-13 03:59:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4cfe79aa-b5d9-399f-a2f3-91bb7cb9d21a | -2.41872 | -45.05817 | 2025-12-13 03:59:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ca2f66f-cd64-3bc0-9a95-0f5e511bb22e | -3.2022 | -41.8526 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 53060f08-28d5-3e6b-a857-a88e88911655 | -3.47633 | -44.21025 | 2025-12-13 03:59:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 954f6ec1-b550-36aa-aaa2-c4274164864e | -3.19519 | -41.85149 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1eec356f-f4b4-3659-afc8-fb73d3436a8a | -1.8974 | -45.42855 | 2025-12-13 03:59:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec05340d-33cb-3f00-b628-ce090933cc6b | -3.20632 | -41.84929 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| ec5cd1d2-2447-3318-8b58-712b15194380 | -3.20094 | -41.86041 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 503a8a51-6f47-31f7-854e-b46818092270 | -3.80423 | -42.78956 | 2025-12-13 03:59:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9aa3cde7-dd66-3333-9f05-2c5beddd3411 | -2.41994 | -45.05895 | 2025-12-13 03:59:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9cb6ccf-b971-35ea-bb2c-cd66ad2a004c | -3.47716 | -44.20511 | 2025-12-13 03:59:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 351d95e3-308c-3f09-b004-57b5f2690e0e | -3.01832 | -47.09187 | 2025-12-13 03:59:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4d1d7d3-5b8c-3c0f-a10c-0ce88283f245 | -2.8681 | -45.44629 | 2025-12-13 03:59:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 870f74fb-356f-344d-9098-7281b471de6e | -3.19456 | -41.85538 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 55.6 |
| d0fbea97-b20a-36e0-9d24-9539c9f9e286 | -3.43817 | -41.64814 | 2025-12-13 03:59:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6a4b2462-576c-3a09-96e8-fa62b26dba0f | -2.79786 | -45.12844 | 2025-12-13 03:59:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64b9e5ca-424d-34ae-a415-97b06d735cf2 | -3.95304 | -41.52316 | 2025-12-13 03:59:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ede789e2-3637-3794-a1f9-affe031f54f2 | -2.86742 | -45.45048 | 2025-12-13 03:59:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8476c15a-567a-346b-af3e-20ab7c38281b | -3.20569 | -41.85317 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| f75a8597-975b-3f38-a7c6-06ac01b8a27a | -3.47319 | -44.20446 | 2025-12-13 03:59:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0caff01f-e077-3e33-8430-df0d1494d4d5 | -1.90446 | -45.46984 | 2025-12-13 03:59:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 57b2ed0f-2b97-3ce3-b08c-ca37ad166792 | -2.41566 | -45.05824 | 2025-12-13 03:59:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e9e649d-00f1-373a-a8f1-2380abf32a1e | -3.43062 | -41.65086 | 2025-12-13 03:59:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 624f8e5a-951c-30f5-884b-e0d00ca14b1e | -1.70938 | -47.02617 | 2025-12-13 03:59:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac82d223-a417-3015-b66a-603f98c657da | -2.48617 | -47.77198 | 2025-12-13 03:59:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89451f5b-3c19-3a38-83ce-636ea61e2624 | -3.19932 | -41.84817 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c1e093d5-680a-3df6-8476-ea0c76393165 | -3.31886 | -39.34792 | 2025-12-13 03:59:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7aaebc3e-c322-346f-8289-7ba9f8a79a88 | -2.41806 | -45.06215 | 2025-12-13 03:59:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9bf1ff99-9bc6-3a11-b599-f87a652f3cee | -1.11985 | -47.73671 | 2025-12-13 03:59:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 118b19da-f469-3ee9-a1d5-c55b7a7eb77f | -3.4485 | -44.73382 | 2025-12-13 03:59:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 18708f50-37df-3d50-8550-ed7ebbecfc0c | -2.41537 | -44.03968 | 2025-12-13 03:59:00 | NOAA-20 | RAPOSA | MARANHÃO | Brasil | 2109452 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1129b917-42c0-31ca-ac58-888704024b1a | -3.19393 | -41.85931 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 15e4c40d-95bf-3bb5-88a8-11eb4cadf4cd | -3.19744 | -41.85986 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 1d417ec2-e805-3fac-8fea-7e479f5f1e9c | -1.90377 | -45.47419 | 2025-12-13 03:59:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d4ea69ce-9263-3d20-9f91-fcb98e3c4e84 | -1.72378 | -47.15808 | 2025-12-13 03:59:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dfefefcf-2469-3216-9f24-998f1fa5433b | -3.20919 | -41.85377 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c29532e2-69b3-3900-a12c-9d42334fcfb2 | -2.01062 | -46.38421 | 2025-12-13 03:59:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa1bce84-993d-3c0c-b2e2-115d1e500e33 | -2.48567 | -47.77506 | 2025-12-13 03:59:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a430370a-6892-38ee-b9a9-4f5fecc1b215 | -3.19106 | -41.85483 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0088fe17-6a2b-3523-b576-b332a3b7b003 | -3.20444 | -41.86097 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 5967720c-4fd3-38ff-ad85-b6e5441ba7f0 | -3.44585 | -44.73392 | 2025-12-13 03:59:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 06dde18e-4091-3496-aadf-50823669bea4 | -1.11959 | -47.73863 | 2025-12-13 03:59:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| baee158c-2751-3ea1-abd6-e520cea6a95f | -3.19869 | -41.85205 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ed1d6711-342d-31e7-a22c-94f9be6fe076 | -2.78564 | -45.78662 | 2025-12-13 03:59:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| deabf7c0-21f7-3d5b-873c-a642f5b9d00f | -3.19807 | -41.85594 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 55.6 |
| eb662c56-05f3-328d-a271-b3bab06ee469 | -2.66707 | -46.89569 | 2025-12-13 03:59:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f025976d-9c33-3c76-b3d9-8599659bbd7a | -3.18755 | -41.85428 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b8c159d-f4a3-3684-a942-10b781b85252 | -8.0513 | -43.1001 | 2025-12-13 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 809ede54-8462-38dc-ad40-7b67a0330143 | -3.2007 | -41.8678 | 2025-12-13 04:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 167.0 |
| d59d1ac5-4206-3d37-b276-47f4eb607d55 | -3.2009 | -41.844 | 2025-12-13 04:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 0f03241e-7663-3a3d-ae1d-144552635dce | -3.2196 | -41.8431 | 2025-12-13 04:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| db92b6d7-f3b7-30cd-ae96-358c190f5e48 | -8.0324 | -43.1022 | 2025-12-13 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 44c6f901-47f6-3f30-9f65-b9347c15d4c3 | -3.2194 | -41.867 | 2025-12-13 04:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 5fc7b967-e992-3dea-88d8-16f306e1d00a | -3.1822 | -41.8448 | 2025-12-13 04:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| c8f371b4-d9c3-362a-94f4-52b2db4f76eb | -3.182 | -41.8687 | 2025-12-13 04:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| ccfbff6e-7b4f-3f90-9ed6-862489c128ce | -3.51832 | -47.21035 | 2025-12-13 04:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78cfc642-6c80-39a0-b999-9fe59ff2d4c5 | -6.96246 | -39.98397 | 2025-12-13 04:01:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8c5db87d-f591-3773-8e55-521ba401afb0 | -7.47703 | -35.24882 | 2025-12-13 04:01:00 | NOAA-20 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 9e2f810a-ee8c-3ffb-89b8-cb13177405c6 | -8.04609 | -43.10743 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c8735658-c302-326c-8864-f0b5d020aba9 | -6.06667 | -43.25269 | 2025-12-13 04:01:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0d83c170-deac-329c-8e51-f8ccd280c7d0 | -8.04544 | -43.1114 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d7b41005-0155-3722-b6de-f5706ab88e0a | -5.07278 | -43.67009 | 2025-12-13 04:01:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7bc9e5ea-80e3-3051-a02d-afc183138b25 | -8.02847 | -43.10449 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0511f065-22cd-3e96-9615-235b0134e256 | -8.0371 | -43.11819 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d594a791-f746-3511-a25e-8e1adc88e896 | -8.38478 | -44.05948 | 2025-12-13 04:01:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9286642-d81c-3a24-a352-4f2d0032bb68 | -10.29076 | -37.80844 | 2025-12-13 04:01:00 | NOAA-20 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fec451ec-3094-3459-aeb5-b5b04152110e | -3.97329 | -42.50841 | 2025-12-13 04:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 891f59cd-38ba-357d-8a2c-d714d5a2c370 | -8.03422 | -43.11363 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 98a3df5c-81ab-3539-a7da-525532a94c28 | -6.71247 | -39.99729 | 2025-12-13 04:01:00 | NOAA-20 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 15deb5a6-c295-3691-9243-20165bc2fdfd | -3.23853 | -47.24898 | 2025-12-13 04:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| aedb30df-a1ff-3839-8e06-6b63f188f123 | -5.32556 | -40.55797 | 2025-12-13 04:01:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8f16e617-b25c-3ea7-b606-79622b09e85f | -4.11311 | -45.32414 | 2025-12-13 04:01:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b6e3a8f-221a-39aa-a13d-3c051f423751 | -7.23048 | -43.10745 | 2025-12-13 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 276208df-a387-35aa-9c9b-b014399e8cb9 | -8.0243 | -43.1079 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 168d441e-17e1-3cde-b251-b87c48104b3e | -8.41046 | -44.0414 | 2025-12-13 04:01:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b72a627-8938-3d3b-9ba7-60f253d775d2 | -8.02782 | -43.10848 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5f93d5a3-9708-325d-a8f5-12a674641848 | -8.40679 | -44.04076 | 2025-12-13 04:01:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df5e65e9-4140-3099-8f3c-98d0e1ba32fb | -7.21848 | -43.11382 | 2025-12-13 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 167a63d2-35f0-3816-85d9-d1c37bc66858 | -5.84728 | -37.48243 | 2025-12-13 04:01:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 06e2f61b-323a-39ff-8f2e-7f62d3d90af5 | -8.03552 | -43.10566 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cba991dc-6a30-325b-a393-fec889de8241 | -5.19614 | -38.49348 | 2025-12-13 04:01:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 22cfd274-200a-3747-8ed5-939417745378 | -8.40974 | -44.04576 | 2025-12-13 04:01:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a14d96a-16ba-353d-b9f5-27e6f7df022c | -5.54507 | -41.65363 | 2025-12-13 04:01:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bc35a125-348b-3707-b77c-6e40c139ff2a | -7.21492 | -43.11324 | 2025-12-13 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ac31f901-484f-3be1-87da-4087910509e7 | -3.8097 | -47.05266 | 2025-12-13 04:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c70eed3a-7ea0-3887-b648-333029c50f61 | -8.3811 | -44.05886 | 2025-12-13 04:01:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de2b50b8-04e0-3353-90e1-b0ebddbab8bf | -5.19558 | -38.49705 | 2025-12-13 04:01:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 241f8674-156a-34c8-a2bf-cfd7343fd744 | -8.75422 | -39.68725 | 2025-12-13 04:01:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3cfd03f2-62c0-39c3-a35b-1983e08c40a2 | -2.49724 | -51.80616 | 2025-12-13 04:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cab4ed0b-3ad0-35f9-94b5-38bba5aa43ab | -5.71678 | -40.53404 | 2025-12-13 04:01:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 47f7a227-4e1d-3ee8-a1af-9868d2d51d1d | -3.56244 | -47.18543 | 2025-12-13 04:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5212f987-3ae7-3544-8c28-ac617ab90379 | -4.73399 | -39.85334 | 2025-12-13 04:01:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README7.md)
