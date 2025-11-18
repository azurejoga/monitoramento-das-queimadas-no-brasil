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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a2e3f92-a9b5-3795-84b8-c1ee76018716 | -3.3554 | -44.4026 | 2025-11-18 01:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| d8d77bf0-8f44-3c38-81a5-50c0be115d0d | -2.4669 | -48.2238 | 2025-11-18 01:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| a71095e8-11e0-3889-b6f7-900309fd1fd4 | -9.3969 | -48.4523 | 2025-11-18 01:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 8e3bdffb-b193-3263-ad2a-6865aee4b459 | -2.8297 | -45.4419 | 2025-11-18 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 783cb930-a5b9-3fd3-90f8-026ff6962e3d | -3.2506 | -43.0449 | 2025-11-18 01:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 71a5d2f2-0551-35a1-b794-e23652029d71 | -9.4956 | -40.3586 | 2025-11-18 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 78eb6bbe-ca2a-3a64-9c58-216a638268c1 | -3.3367 | -44.4034 | 2025-11-18 01:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| a7664244-664f-3047-b367-7a16cd78d2b4 | -4.195 | -44.2247 | 2025-11-18 01:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 2296b33e-5309-300a-b83a-3155cebeba7a | -4.1949 | -44.2476 | 2025-11-18 01:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| a8d1f099-7004-3c5b-bf05-3d1760cfebc0 | -5.4377 | -43.0568 | 2025-11-18 01:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 2e6a6871-89d5-3f25-8dab-e68f9fd1e436 | -2.4669 | -48.2238 | 2025-11-18 01:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 513f5e6a-7748-3743-b117-f91d968ebed5 | -2.5238 | -47.8115 | 2025-11-18 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| e3544730-5fbe-30c4-9320-8f699c373f6e | -4.195 | -44.2247 | 2025-11-18 01:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 361c4725-27a9-361c-8c89-e5e45e7ce881 | -4.1762 | -44.2486 | 2025-11-18 01:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| ec047041-df2f-38c2-95bc-c5be212b7e93 | -4.1313 | -52.1239 | 2025-11-18 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| d3e368ec-11ba-30c5-a290-68bc76f81735 | -5.4379 | -43.0333 | 2025-11-18 01:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| ce06cac8-0ba4-3139-8e23-4de40bf64f89 | -6.1138 | -42.9569 | 2025-11-18 01:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| ccc19e71-6b49-3177-b047-c322c2f036cc | -5.419 | -43.0582 | 2025-11-18 01:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| baf5f3c5-76db-3c4b-b596-dd849203bf1e | -9.3969 | -48.4523 | 2025-11-18 01:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| bba42556-067b-35c7-9290-d771641993fc | -2.4854 | -48.2233 | 2025-11-18 01:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| fa9072e8-08a0-3fe2-b0e6-0500fcc592ec | -6.7202 | -40.7943 | 2025-11-18 01:50:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 8e5cdc23-c54f-3419-b435-01d1d0319a8e | -5.4192 | -43.0347 | 2025-11-18 01:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 903a6677-154d-3d08-992c-2ef5897e1f9b | -4.1764 | -44.2257 | 2025-11-18 01:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 9f5dbfe8-27ce-3420-b530-0c2a5eed6298 | -3.477 | -46.0656 | 2025-11-18 01:50:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| fd4236c4-7667-34ba-85d8-53f65f11d66d | -3.3555 | -44.3798 | 2025-11-18 01:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| e72f3542-d782-328a-ab68-308c2a150c45 | -2.8297 | -45.4419 | 2025-11-18 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 2985ed55-142d-3b42-b72d-ba7498bdb9a3 | -3.2506 | -43.0449 | 2025-11-18 01:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 0b37492e-c239-35d3-8681-ff6616ddfb78 | -4.1949 | -44.2476 | 2025-11-18 01:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 9605d2d1-2ab0-3388-9700-2118234e15fe | -3.3554 | -44.4026 | 2025-11-18 01:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| df0f8c63-2226-3d1f-a42a-057541c27e2f | -10.3535 | -48.9174 | 2025-11-18 01:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 512ae30f-8c67-3125-b2ed-fe03215055c4 | -2.8298 | -45.4195 | 2025-11-18 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 233.5 |
| adba9935-0ba6-3d52-9ea0-b3b4e5dcd9fe | -3.3367 | -44.4034 | 2025-11-18 01:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 31f5ba16-25f8-30da-b80e-3d4e5d89ae40 | -5.4379 | -43.0333 | 2025-11-18 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| cfbef312-1b0f-3142-ad84-a491a9d7eaca | -10.3535 | -48.9174 | 2025-11-18 02:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| daa80d40-d8a3-3416-ae01-0a0aa24f19ea | -3.3367 | -44.4034 | 2025-11-18 02:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| bed91d83-e9c3-346f-9da2-771549fe215c | -5.338 | -43.7623 | 2025-11-18 02:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 308c4d93-508f-3a90-b086-1649a98ca570 | -3.2506 | -43.0449 | 2025-11-18 02:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 2d8785e7-c42d-346d-ab49-08ac53e596be | -2.5238 | -47.8115 | 2025-11-18 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| d27e2d03-d759-3fa0-a914-7dece7a2469f | -2.8298 | -45.4195 | 2025-11-18 02:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 223.6 |
| 39cf3746-ff98-3ecb-84d3-ca5e067ae445 | -12.7378 | -45.4274 | 2025-11-18 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 03668c62-d4df-3c60-a28e-428c37af3b47 | -4.1764 | -44.2257 | 2025-11-18 02:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| f347c929-3d3a-3303-a1c3-fa460c7302a3 | -5.3382 | -43.7391 | 2025-11-18 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 82ba08ec-c9ec-398d-8242-e745789c5163 | -4.195 | -44.2247 | 2025-11-18 02:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 4ab19e02-588d-3857-b0b2-d8aee850bd0e | -5.4377 | -43.0568 | 2025-11-18 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 68493dac-9a35-3ccb-8655-32e390159492 | -5.419 | -43.0582 | 2025-11-18 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 5bfb4393-374f-3d8d-a583-8988aea7788c | -4.1949 | -44.2476 | 2025-11-18 02:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 4bc639c3-16c1-3616-b541-7b8f826d181b | -5.4192 | -43.0347 | 2025-11-18 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b0fd5e7b-6324-32d1-a9aa-9ca1ba3ea9c0 | -4.1313 | -52.1239 | 2025-11-18 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 235.8 |
| a9bd80b2-dd66-392a-b754-5054ba955a31 | -4.1498 | -52.1026 | 2025-11-18 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 7d2d46c5-9c03-3a42-861c-b584c5a2e331 | -6.1138 | -42.9569 | 2025-11-18 02:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 487e9411-1ef2-3ea2-83c1-f013abfde4d3 | -2.4669 | -48.2238 | 2025-11-18 02:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 1eaac753-8e89-38c5-97bd-96e30a086bc9 | -3.477 | -46.0656 | 2025-11-18 02:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 13786bb1-d1af-3709-8cb0-d6583e8b3308 | -4.1497 | -52.1232 | 2025-11-18 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 7b2bee2c-8254-351d-b14e-728ce5c5fd75 | -4.1762 | -44.2486 | 2025-11-18 02:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 7d4f9a6c-343b-362b-bd29-aef2b9287896 | -3.3554 | -44.4026 | 2025-11-18 02:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| d8ef2f9b-7b3c-3ea6-9ff5-c632abf6132e | -9.3969 | -48.4523 | 2025-11-18 02:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| bef639a1-4c0e-30ef-8d23-2770d5aae7af | -2.8299 | -45.397 | 2025-11-18 02:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 3b95a9db-2f3b-3cb9-8a9f-11c1de7aad3e | -4.1314 | -52.1033 | 2025-11-18 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 135.8 |
| b930994e-1707-392e-9f65-5a72f8848517 | -3.3555 | -44.3798 | 2025-11-18 02:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 4e9c1f23-26bb-3a60-bf9b-5dc9c61e1aed | -4.195 | -44.2247 | 2025-11-18 02:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 534b5735-d76a-3902-bac1-ae69b2d0a214 | -2.8298 | -45.4195 | 2025-11-18 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 485fbbf5-7745-3ee0-af70-12ded7f11941 | -2.2851 | -47.2302 | 2025-11-18 02:10:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 8b65779d-28d0-3e50-89e6-3a4553a32d50 | -12.7378 | -45.4274 | 2025-11-18 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 334d505e-dd0d-3625-9c0e-0b80ee062f06 | -4.1949 | -44.2476 | 2025-11-18 02:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| fa5aceed-9737-39ee-bea6-131faea6faf8 | -2.5238 | -47.8115 | 2025-11-18 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 373fea1e-8ccd-3a42-976b-de11c6f93fbf | -4.1314 | -52.1033 | 2025-11-18 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e0945bd5-035d-38b3-a1d9-f72f8cf51a42 | -12.6933 | -46.7803 | 2025-11-18 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| b1c363ec-1070-33db-90dd-3694996a11ea | -2.4854 | -48.2233 | 2025-11-18 02:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 316672ef-e258-3874-b7e2-afe8aa5a0c56 | -9.3969 | -48.4523 | 2025-11-18 02:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| e87b6dcb-3cf1-3979-b0e3-9f96dc810176 | -3.3554 | -44.4026 | 2025-11-18 02:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| c85d6580-e8e3-357e-8d77-8df55a5742fd | -3.3367 | -44.4034 | 2025-11-18 02:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 0e57f18f-39a9-35b9-891c-be2b577c647f | -5.3382 | -43.7391 | 2025-11-18 02:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 562c2702-8ce7-346b-8678-5bbbb39fb8dd | -4.1762 | -44.2486 | 2025-11-18 02:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e14401b5-f070-368d-8bf2-e36de061b895 | -3.3555 | -44.3798 | 2025-11-18 02:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 17163b7d-3dbc-3c17-b420-61a414a03a86 | -2.4669 | -48.2238 | 2025-11-18 02:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 1cbbc1dd-41ab-39c9-89ab-2001058d5a8a | -4.1497 | -52.1232 | 2025-11-18 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| c980c9ee-fce1-3073-82ef-fbe11a53f76f | -4.1313 | -52.1239 | 2025-11-18 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 682b122d-2690-3ca6-ae29-63b26bcbfd83 | -4.1764 | -44.2257 | 2025-11-18 02:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| d49528d4-07a7-31a4-9608-50efe9d05527 | -5.338 | -43.7623 | 2025-11-18 02:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 278a942f-99f9-31e4-bb9e-b24596b766f3 | -12.7378 | -45.4274 | 2025-11-18 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 23595f0f-80fc-36b5-b400-8da07f98207e | -2.8298 | -45.4195 | 2025-11-18 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 477b77b2-b8e2-352d-b402-7e672ac12039 | -2.4669 | -48.2238 | 2025-11-18 02:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| f6a48205-68a6-3713-824e-37f1655d9e18 | -2.8112 | -45.4201 | 2025-11-18 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 44f18d3c-d226-3086-8212-caaa1205f12a | -2.4854 | -48.2233 | 2025-11-18 02:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b862a919-094f-395d-878d-9cfd57c697dd | -4.1764 | -44.2257 | 2025-11-18 02:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 9356b585-aa59-3583-8ef5-a43add2e167c | -2.2851 | -47.2302 | 2025-11-18 02:20:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 59595a0f-30ef-3e1f-884b-6a96f9cef52a | -2.3037 | -47.2297 | 2025-11-18 02:20:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 9de58dcc-53e9-3bf0-95a6-79c639a57a23 | -6.7202 | -40.7943 | 2025-11-18 02:20:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 6bd20ff7-9c65-374c-9281-232278eb2847 | -9.3969 | -48.4523 | 2025-11-18 02:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 1282ae35-5519-3ebc-aaec-5e6f6ee5ceb2 | -9.0596 | -45.4175 | 2025-11-18 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 0204f003-0f21-374a-aeb6-19dfab519ddb | -3.3555 | -44.3798 | 2025-11-18 02:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| fffb1dec-e10e-35a8-9796-a997994d6351 | -3.3554 | -44.4026 | 2025-11-18 02:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 7d72f221-5024-322f-9c89-d4dacb70d091 | -12.6933 | -46.7803 | 2025-11-18 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| e4e2e962-b65b-35b7-a7d2-2c4528586619 | -4.195 | -44.2247 | 2025-11-18 02:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 86473d42-6f99-34ee-9ea5-2fe1d0522463 | -4.1762 | -44.2486 | 2025-11-18 02:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| b028f5d8-d87b-3d02-9770-c3c347c21ce4 | -2.5238 | -47.8115 | 2025-11-18 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 47edb568-41d4-3af0-ad9c-a17b21e176a9 | -4.1949 | -44.2476 | 2025-11-18 02:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 67fc533f-97eb-3b1f-a669-99f98425a16b | -9.0934 | -44.3356 | 2025-11-18 02:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 0a122536-8cdb-333f-821c-2e094bbdc3f6 | -12.6933 | -46.7803 | 2025-11-18 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 240e7b9d-e9eb-330f-aa19-b60114e47a77 | -4.1764 | -44.2257 | 2025-11-18 02:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |


[Clique aqui para ver as próximas entradas](README16.md)
