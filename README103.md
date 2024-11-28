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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c76f6d9d-3b29-3f26-8c29-373cacc88afd | -17.626 | -57.5692 | 2024-11-28 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 5621f65e-f980-3a4d-92b4-e8c71a9d5f92 | -17.6457 | -57.5668 | 2024-11-28 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 62c1d02f-2471-3943-befd-8d03d5f0ffde | -1.6552 | -47.4405 | 2024-11-28 13:50:00 | GOES-16 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 9a1b589c-9319-3c6d-9807-ce786d498fd0 | -0.5976 | -51.7059 | 2024-11-28 13:50:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 3ab4d2bd-2619-3404-9c61-ac6d2b49dd91 | -4.6564 | -42.4048 | 2024-11-28 13:50:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 220.4 |
| f3c9f892-3c54-37b0-8fc3-293b6260caa3 | -6.0683 | -45.8058 | 2024-11-28 13:50:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 9fb46ecd-e83d-3d77-9b8b-a973f22d717f | -5.4548 | -43.2426 | 2024-11-28 14:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| b839daa1-a17b-3385-a09b-f451a99beafc | -3.9675 | -48.0634 | 2024-11-28 14:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 5f271ba6-89a6-3f6f-82b6-0e11e496505e | -3.0696 | -41.9213 | 2024-11-28 14:00:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 113.3 |
| 6ab12a1d-b983-334a-8c22-e9d5c604b75e | -17.6457 | -57.5668 | 2024-11-28 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| c752048f-149e-3bd4-95e4-1d1f7046b44b | -2.861 | -46.8406 | 2024-11-28 14:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 9e938083-ea7e-38f7-9a94-66fa6779369f | -6.1794 | -42.028 | 2024-11-28 14:00:00 | GOES-16 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 68bd75aa-1c7b-3276-ad9b-4e4fb5e8aa7f | -3.6716 | -44.4798 | 2024-11-28 14:00:00 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 6fef45e5-fc1e-38b1-900d-9da75e0567c0 | -4.8209 | -45.4162 | 2024-11-28 14:00:00 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 01a30ce2-a74c-36e1-8f03-7f48b2fff916 | -1.6552 | -47.4405 | 2024-11-28 14:00:00 | GOES-16 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 621ada0e-4eaf-3d02-b412-c2e81469974f | -3.0882 | -41.9443 | 2024-11-28 14:00:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 3abe66c4-831e-3c22-ade7-e31521de1b97 | 1.2354 | -55.9666 | 2024-11-28 14:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| f342a1e1-50e7-31cb-b2d1-b502d7a672d6 | -6.0683 | -45.8058 | 2024-11-28 14:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 56aaba7a-6cde-3986-98da-bf127450763c | -3.0695 | -41.9451 | 2024-11-28 14:00:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 15aba31f-08d0-3f9c-908b-ff8bd0d2b32d | -17.4054 | -57.8408 | 2024-11-28 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 1741bc07-453e-3656-a66f-859c33078c1e | -2.3017 | -47.8391 | 2024-11-28 14:00:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 9b303ba8-a8a5-3392-bd75-da9be8035bb6 | -17.6453 | -57.5874 | 2024-11-28 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| a880f308-ad0f-3dcd-a61b-14d6dbb931ae | -2.824 | -46.8199 | 2024-11-28 14:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 39ceaa40-abe6-3e9c-a009-67de7bfa09e1 | -3.4717 | -43.5466 | 2024-11-28 14:00:00 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| fca80367-11cb-34bc-8b9f-756999233d1e | -4.1662 | -49.001 | 2024-11-28 14:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7d822adf-6e58-3996-b2ab-98d1ede1da58 | -4.6753 | -42.3799 | 2024-11-28 14:00:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 197.0 |
| 84aec3b9-38d7-3eea-8b86-420153c8c188 | -17.6256 | -57.5897 | 2024-11-28 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 222528d0-6564-3a86-9737-184c7e4a632b | -17.626 | -57.5692 | 2024-11-28 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 0f86f031-7824-3dd0-9668-a0f6d5713484 | -6.1792 | -42.0518 | 2024-11-28 14:00:00 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| d087d5c8-8ce5-3f38-bc10-0fe881c2d76f | -5.4546 | -43.2659 | 2024-11-28 14:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| b47b74e4-94d1-3be3-91d8-d9bc84662230 | -4.6565 | -42.3811 | 2024-11-28 14:00:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 223.0 |
| 591d8c7d-b3ca-3a82-95a8-728ded64a974 | -4.6564 | -42.4048 | 2024-11-28 14:00:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 156.4 |
| 46a4afde-600c-38eb-86e1-eb70a37e892d | -6.09 | -43.94 | 2024-11-28 14:00:00 | MSG-03 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfc1e3d9-6424-3f64-ba4e-5a4144c25ce6 | -4.1603 | -43.8356 | 2024-11-28 14:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 13aec718-251a-3ea1-a83b-9298dd34c5a6 | -17.5862 | -57.5944 | 2024-11-28 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 2811441c-bd61-3cd0-aa87-ff99845c66dd | -9.1827 | -44.7173 | 2024-11-28 14:10:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 122.3 |
| a79ca3ae-395a-3156-9843-2e93c95d1b76 | -9.1824 | -44.7404 | 2024-11-28 14:10:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 8d5170eb-8038-3296-9deb-b8670b7024e6 | -6.1794 | -42.028 | 2024-11-28 14:10:00 | GOES-16 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 5ccb0feb-0570-322f-8f17-0e51267a787c | -3.0696 | -41.9213 | 2024-11-28 14:10:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 100.7 |
| d8835db2-d152-329b-ace6-1e70fdc762c3 | -17.6457 | -57.5668 | 2024-11-28 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.4 |
| c7b62cb8-5578-3a39-9b46-0a8dfcbe3547 | -17.626 | -57.5692 | 2024-11-28 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| a39198cf-9279-310a-bafb-49bfe163aae3 | -18.2383 | -56.3763 | 2024-11-28 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 8d491ff1-3d2b-3aac-9aa6-147271770699 | -6.1792 | -42.0518 | 2024-11-28 14:10:00 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 4f78a92f-ab54-30ac-85ff-09a883ff13c0 | -2.0305 | -45.6896 | 2024-11-28 14:10:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 9522c691-118d-3df6-b6f9-7477b81b6682 | -2.9968 | -45.4584 | 2024-11-28 14:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 9c886135-dbe5-3878-a3ac-fdfa74be4ab0 | -1.3649 | -54.996 | 2024-11-28 14:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 074999f6-a323-3a98-9ebb-bdc465d73397 | -3.0695 | -41.9451 | 2024-11-28 14:10:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 736fac05-c3b5-313b-abdf-caadd2aa0d94 | -6.0683 | -45.8058 | 2024-11-28 14:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 2c66f2b0-7389-3982-a1c1-cb1dbf099236 | -3.6716 | -44.4798 | 2024-11-28 14:10:00 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 193.8 |
| e99f50cd-6f0c-3393-a70f-dd49d4769a37 | -4.6564 | -42.4048 | 2024-11-28 14:10:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 173.6 |
| 4e855420-4b1b-3a63-85cb-d4bdea770d37 | -5.4546 | -43.2659 | 2024-11-28 14:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 86aefb9c-02c6-3c1a-a540-25858681d987 | -17.5688 | -57.4529 | 2024-11-28 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 2a47bb5a-85c8-3a0f-865c-27a7cffb28b2 | -4.8209 | -45.4162 | 2024-11-28 14:10:00 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| bc7c4d16-15e2-3966-b7cf-33fd0fc9d8b1 | -4.1604 | -43.8125 | 2024-11-28 14:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 00f5f2a9-c3f1-3820-b84f-15fb23c17865 | -4.6753 | -42.3799 | 2024-11-28 14:10:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 205.7 |
| 7704920e-0e8f-3cff-a8cf-104b0bb168f2 | -2.9755 | -42.0679 | 2024-11-28 14:10:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 8950a299-57b9-3577-9f75-e4c0b0e1484c | -4.6565 | -42.3811 | 2024-11-28 14:10:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 279.2 |
| ebad546c-3d5d-3009-bedd-37d86d006dc0 | -17.6453 | -57.5874 | 2024-11-28 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 74ea83d4-9eff-3f0e-b57d-cc7fa1141ecc | -3.9675 | -48.0634 | 2024-11-28 14:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| c460e880-5bd4-3187-aab8-cc70f0c1e3eb | -17.6457 | -57.5668 | 2024-11-28 14:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 45de8d6f-54a1-38cc-ae35-0319154b1210 | -4.8209 | -45.4162 | 2024-11-28 14:20:00 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5a665597-28b3-3690-bba0-0be280a32467 | -9.1824 | -44.7404 | 2024-11-28 14:20:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 4a129292-867f-3572-82f3-649ab54a1418 | -6.1794 | -42.028 | 2024-11-28 14:20:00 | GOES-16 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| f015bc78-8ba8-3c20-b144-64488f0e8a82 | -6.0683 | -45.8058 | 2024-11-28 14:20:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 8ecda740-cfa8-3af3-99fc-4b86359b03ea | -3.9675 | -48.0634 | 2024-11-28 14:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 34e0b05a-c6e0-36ad-9d41-80a96595e329 | -0.5792 | -51.706 | 2024-11-28 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 7570441c-5ee0-3eb8-85fd-e4331bea0a28 | -3.8538 | -45.1747 | 2024-11-28 14:20:00 | GOES-16 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 3819e69e-05a1-357c-8359-ab52364e266e | -1.165 | -53.6773 | 2024-11-28 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| ba1985dd-6190-3c06-af86-f8e0805c0229 | -17.6453 | -57.5874 | 2024-11-28 14:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 2b29355c-e002-35c1-bf7a-45272d600697 | -2.3016 | -47.8608 | 2024-11-28 14:20:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| a5215860-dffb-3e6f-a223-2bab3cbf9068 | -2.2331 | -46.13 | 2024-11-28 14:20:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 73bdffd1-cf96-3d62-adba-4faaa3b3af96 | -4.6565 | -42.3811 | 2024-11-28 14:20:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 194.6 |
| ef35dde6-f6c3-36a6-9ab8-59d13daafc92 | -4.6564 | -42.4048 | 2024-11-28 14:20:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 149.5 |
| 1526b534-67db-3554-bb1f-b98e250cca8a | -2.3017 | -47.8391 | 2024-11-28 14:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 4d94104b-1c93-3d84-b5ca-d52842aef361 | -4.6753 | -42.3799 | 2024-11-28 14:20:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 252.7 |
| 6592994f-91e1-3330-94d6-dac2ab29568f | -9.1827 | -44.7173 | 2024-11-28 14:20:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 8284c068-800c-3a10-9c85-3826a28cc75b | -17.4054 | -57.8408 | 2024-11-28 14:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.9 |
| aebf93d4-d855-35e2-a198-b7433e3b4379 | -5.5461 | -41.4335 | 2024-11-28 14:20:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| c9b42882-9e7b-3ac7-a70a-d726115f4ce2 | -6.1792 | -42.0518 | 2024-11-28 14:20:00 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 89fbd149-b76e-3a2e-a265-03f3c6fb8828 | -6.0496 | -45.8072 | 2024-11-28 14:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| dc4de70e-e7e1-3918-84d6-fe08b0755c0f | -17.4054 | -57.8408 | 2024-11-28 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 38c198bb-db9a-37be-bb0b-cad0310c403f | -4.6753 | -42.3799 | 2024-11-28 14:30:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 180.8 |
| d66da73b-5cb5-3003-ae7b-c7502aa13038 | -3.1787 | -46.2995 | 2024-11-28 14:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 90.3 |
| a5c8193f-d80b-3f01-b355-40ec4a5d4ae1 | -1.3649 | -54.996 | 2024-11-28 14:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 8354b4d5-ba23-3546-bb40-2384f7e4035a | -6.1794 | -42.028 | 2024-11-28 14:30:00 | GOES-16 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| f911bbde-5fcf-3c42-9c79-12b59c7523b4 | -0.5792 | -51.706 | 2024-11-28 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 23b5bd91-8441-333d-8aa5-a05ff9ad49b4 | -3.6716 | -44.4798 | 2024-11-28 14:30:00 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 365.5 |
| abc5c2e1-b7bf-3388-9857-bebcf9d522a0 | -0.1196 | -51.3359 | 2024-11-28 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 74.9 |
| c8f1499f-3b34-3c5a-9d42-484e76f75352 | -4.1603 | -43.8356 | 2024-11-28 14:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 31d4498f-0524-3513-885c-1814cda8bb3c | -4.8209 | -45.4162 | 2024-11-28 14:30:00 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 41809dc7-7d37-3104-94f0-5f6fc845fa4c | -3.1151 | -44.0462 | 2024-11-28 14:30:00 | GOES-16 | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 107.0 |
| a5b38911-1cf5-346c-a1fe-5f9691eae8a8 | -4.1761 | -44.2716 | 2024-11-28 14:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 83343007-b625-3f2b-8493-d3667f3ef760 | 1.2721 | -55.9466 | 2024-11-28 14:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| c50f0925-d39f-353d-82ff-1d345bbee436 | -1.3321 | -52.438 | 2024-11-28 14:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 28ba9a74-f5cc-304e-bcf5-0a963381f8de | -0.138 | -51.3359 | 2024-11-28 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 99b9de65-5cda-3095-b8b3-bd4a2bc945ed | -4.1604 | -43.8125 | 2024-11-28 14:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| e716d32d-2b0c-3788-b638-7ae7d10ce71b | -17.6457 | -57.5668 | 2024-11-28 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.2 |
| e6645f78-7e84-3afa-bbc5-079899c0aa29 | -4.1947 | -44.2706 | 2024-11-28 14:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 8d639d22-51d3-35af-9f1a-bcf049b529a9 | -17.6256 | -57.5897 | 2024-11-28 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| ecb7a10c-5ec6-3b2a-bb71-826a6b92cbd0 | -4.6565 | -42.3811 | 2024-11-28 14:30:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 208.0 |


[Clique aqui para ver as próximas entradas](README104.md)
