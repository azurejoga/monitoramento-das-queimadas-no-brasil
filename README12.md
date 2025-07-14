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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0815b5d5-a6ae-3e2a-bb87-aec7ab5be067 | -6.41174 | -42.4309 | 2025-07-14 04:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1f114dc1-28cc-3bbe-acc5-06b7bba18475 | -4.24756 | -46.62853 | 2025-07-14 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c5625a1-25b4-3d08-b3dd-df73d09d5301 | -4.01482 | -49.47182 | 2025-07-14 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45884462-6337-3e22-ad3d-23ef272eed10 | -6.84454 | -42.76945 | 2025-07-14 04:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8c6d6ba5-e72e-36ce-a101-865a461b2c2f | -7.05308 | -43.96027 | 2025-07-14 04:49:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 604345c8-6ebb-3bc6-9fb9-b660c5e5c57e | -6.12071 | -44.22412 | 2025-07-14 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 553bf99f-2a5c-3d7e-81ee-deff8f6cc3cf | -3.98211 | -48.42004 | 2025-07-14 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e273d58-67ba-3ba1-a8d6-cc485b013415 | -7.27185 | -45.31527 | 2025-07-14 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 15475f36-6d65-3190-bf1d-d4a2d03cb7a3 | -4.86097 | -43.22276 | 2025-07-14 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e476cc5a-72ff-3142-abae-1cd541961121 | -2.91023 | -48.24002 | 2025-07-14 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c020cf93-f5d7-38ab-a6ba-72f08e0a272d | -5.28225 | -44.88247 | 2025-07-14 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 332c4ca7-7d46-3805-9e18-94d0eaf951bc | -7.26747 | -43.49425 | 2025-07-14 04:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a05c6b86-720b-3c4e-a93e-50e8532fb27e | -6.7606 | -47.36574 | 2025-07-14 04:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3ab4b3b-3247-3c95-8561-df9f8aca0509 | -3.78621 | -47.08995 | 2025-07-14 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a6d29de-2e93-3f4e-9036-ce47ece9550d | -5.26638 | -45.12973 | 2025-07-14 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e2cae47-129e-38fd-83d3-e174a124293f | -5.27148 | -49.29987 | 2025-07-14 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 440625e4-0082-381d-8004-90017e47da43 | -7.35509 | -44.63198 | 2025-07-14 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c9ae71b-d0d4-3333-abb2-77c3844e8eff | -7.04383 | -44.37272 | 2025-07-14 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55a26af8-99b4-369e-9c4d-9b2dc0ae45b1 | -7.58172 | -44.72821 | 2025-07-14 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fd4acfb-97dc-3243-8aee-cda23197ea57 | -3.58356 | -47.51451 | 2025-07-14 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e2ead16a-be68-3a71-aacd-3a9d6b8be5d8 | -5.58314 | -52.07427 | 2025-07-14 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 876fc050-c687-3f2f-9e6c-0bb56a98fcfc | -4.12103 | -47.35493 | 2025-07-14 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22e2f661-431f-3aee-af7d-fd1639f3f30e | -3.78729 | -47.08628 | 2025-07-14 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 361b9806-36cf-31e1-89ca-c5dbcd68d321 | -6.84505 | -42.76574 | 2025-07-14 04:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c89b7538-ebbf-3446-ac55-7dc5623fcece | -4.51426 | -38.55171 | 2025-07-14 04:49:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 7c26b301-66d5-39f9-836b-b9f1d095c7ac | -6.27053 | -43.40932 | 2025-07-14 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bc14d5c-cda5-3827-b574-66975d9bb7d8 | -4.01129 | -49.47129 | 2025-07-14 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c27e73cf-fc05-30d6-9299-ac1db0ca7743 | -6.68931 | -43.68897 | 2025-07-14 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d85ab410-c53f-3ea1-be90-3a161e856acf | -7.26243 | -45.31756 | 2025-07-14 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 36850223-495a-3630-9496-c555513c73f8 | -4.11704 | -47.35429 | 2025-07-14 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ac20c2a-494f-3b06-ac66-2709522f3c21 | -3.57964 | -47.51391 | 2025-07-14 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3527b577-5852-3bf7-8f74-0d16e7c30896 | -4.51148 | -38.5455 | 2025-07-14 04:49:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 92e01a9a-f6a8-3d48-9ecf-811e96d84d1f | -8.5211 | -43.3063 | 2025-07-14 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 6ad0e363-eb75-3aa0-86bc-f9b9dd090702 | -8.5022 | -43.3085 | 2025-07-14 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| 48fd092b-a149-3862-b7c0-aa96243ef66c | -11.7186 | -47.04291 | 2025-07-14 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83e171ab-eab6-362c-9c33-8b3f6cfa7324 | -8.51323 | -43.30303 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| b75481d3-be07-3103-bbff-bfdc4f5b4649 | -10.98767 | -47.08772 | 2025-07-14 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 032b3113-87f3-3e1f-b2ed-fd8a1e55847f | -14.31582 | -52.74317 | 2025-07-14 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ba6b070-cf53-3538-a697-6da1ea821611 | -8.44484 | -45.80127 | 2025-07-14 04:51:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 903a4806-df8d-34c3-8e8f-43245eb5c26e | -10.65486 | -49.44241 | 2025-07-14 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95a75066-7c91-399c-9e89-2ea22760918d | -11.93647 | -45.76606 | 2025-07-14 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4eb778be-3d7a-3a3d-a05e-bc76d96bcf1c | -9.28761 | -63.47337 | 2025-07-14 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05be2562-a29f-325f-a081-583ed7f3533e | -8.87774 | -46.90934 | 2025-07-14 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf99e4e1-c74a-34be-b396-08494a7a288e | -9.02145 | -59.53946 | 2025-07-14 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9bf2ee0-77bb-3c05-93ec-d055235cf729 | -9.5073 | -47.56938 | 2025-07-14 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1dd4171-96ce-34af-8727-d91252487134 | -13.18711 | -47.27105 | 2025-07-14 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9af6c584-c456-374a-981c-766ca3cb8822 | -10.0524 | -59.10903 | 2025-07-14 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d14d4d0-45a7-3ddf-99d7-003b9ef10e28 | -10.16297 | -48.47281 | 2025-07-14 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5f75458-e83f-3b2f-a26f-91c05e91058a | -8.03898 | -50.0894 | 2025-07-14 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d23d42a7-e20b-3e7b-a4b7-844a30ed96dc | -11.93658 | -45.76708 | 2025-07-14 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3f81bfc-7d6c-3f67-ace0-216adc6f815e | -12.41358 | -47.50547 | 2025-07-14 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1bf2bf9e-5c6f-3cb0-b35f-05afd3bb709a | -9.94949 | -48.16427 | 2025-07-14 04:51:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 845c119b-2b70-3560-bb9e-bf2c0070bee3 | -8.51375 | -43.2992 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| caf21c8a-edff-3286-875c-ee0e3c025343 | -9.78904 | -62.48663 | 2025-07-14 04:51:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6454c004-1e13-30b5-a595-02b4857180dd | -10.58119 | -49.15043 | 2025-07-14 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce396994-648e-3fa2-8e32-be7da18f63a8 | -13.03458 | -47.82029 | 2025-07-14 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51b0cfe6-c076-3bf5-bcb1-68442e851c30 | -8.51271 | -43.30685 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 6dbd3f02-b9c8-3809-a0bd-22121bdbde61 | -8.5122 | -43.31067 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 5faa7006-174b-3b9c-9b16-e9cf0f514343 | -8.04191 | -50.09426 | 2025-07-14 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9831ecc6-3ffd-31f7-ba3a-eac5570257e4 | -13.10392 | -47.29903 | 2025-07-14 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbde1adf-552a-3b97-8916-3e95edb84189 | -8.04608 | -50.09092 | 2025-07-14 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| f71b3312-6c45-3e69-b35b-e6f8c5f2a82a | -8.04669 | -50.08683 | 2025-07-14 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 158a366d-f8ff-3848-91d0-35c7a255f7a2 | -8.91321 | -47.35165 | 2025-07-14 04:51:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e774b1d-0f18-3464-8d9d-5c8042da036b | -10.48496 | -55.47987 | 2025-07-14 04:51:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 849e1971-adef-3eca-881a-6d6c4cfd6c77 | -8.5071 | -43.30609 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 3e4d848b-7837-3444-bbf9-b07b291db4c4 | -9.01482 | -61.22282 | 2025-07-14 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17c3f6cf-0712-3113-9a44-03d23175676b | -13.0314 | -47.81054 | 2025-07-14 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61416ee1-4dc0-3c52-be4a-8bf31818d480 | -8.9138 | -47.34759 | 2025-07-14 04:51:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff9afd47-d49f-326d-a4f1-358678cded40 | -10.28163 | -47.61404 | 2025-07-14 04:51:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f9eb148d-2231-3e0b-837a-392fdce4d82a | -8.51138 | -43.30284 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| eeab0fc6-8b9e-3a09-b99c-1bcd3cfcd756 | -13.14785 | -47.3229 | 2025-07-14 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a99d0457-66ec-318f-8c30-77c5ed58f718 | -8.90952 | -47.34693 | 2025-07-14 04:51:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae27a943-9bde-3bbd-97cb-9fe79404f3fe | -10.13111 | -57.7776 | 2025-07-14 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2230d6fe-a21c-3725-a734-197d90548563 | -7.62686 | -56.76292 | 2025-07-14 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48d745dc-82a1-39a6-9f0f-28176763e7b8 | -11.03257 | -47.07674 | 2025-07-14 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2840b0e8-1417-3cb3-8577-785964149c27 | -11.22585 | -46.42075 | 2025-07-14 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a669a69-c685-3327-9a76-d98d24063439 | -10.05654 | -59.10976 | 2025-07-14 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 817e57c3-b0bf-326f-a87d-5bfe34fe31da | -8.517 | -43.3036 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 5acc7876-8ed7-3975-a58a-6b4af8cc7ec2 | -9.02 | -59.5478 | 2025-07-14 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 15f8c56f-69e0-3d19-b75b-b54868f79e64 | -12.1295 | -45.89504 | 2025-07-14 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4cdcaed1-6454-31c7-aac5-336bc90d77ed | -11.86659 | -58.70869 | 2025-07-14 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3312bb56-0d15-34ca-bba6-233c09b6b694 | -6.63083 | -56.28162 | 2025-07-14 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5eb8dc1-b0f7-31d3-9519-c8e325981ebe | -10.39548 | -46.6685 | 2025-07-14 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3509e0ad-426a-3653-a588-9286bd083936 | -8.51651 | -43.30743 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 131dba5c-0131-3cbb-a223-9f53f6472cb3 | -9.35558 | -58.8395 | 2025-07-14 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dcfc184-1157-3485-9427-91ef67a9b09c | -9.48929 | -40.38589 | 2025-07-14 04:51:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d0c1b021-38f8-338f-986f-4d59254f8042 | -11.87051 | -58.70937 | 2025-07-14 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 929f9e5f-4669-369f-9f65-edd067df1b0c | -8.86504 | -46.87197 | 2025-07-14 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44511931-7bf0-3809-9007-a15b76dc4571 | -7.63058 | -56.76352 | 2025-07-14 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef2472fe-cf58-3158-889a-0c8fc294f8d1 | -13.18254 | -47.27031 | 2025-07-14 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8272eb0-1f0e-359b-9fbf-180a49042037 | -13.14841 | -47.31849 | 2025-07-14 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afd48022-a9df-39ca-945f-3c37c19da25e | -10.99217 | -47.08834 | 2025-07-14 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89c876bf-519e-3d3d-bb6e-a8160d92b7e2 | -8.5175 | -43.29976 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 7feb9f21-c576-3104-bfa4-cde4adb1b91d | -8.91011 | -47.34284 | 2025-07-14 04:51:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f41e1919-958f-39f0-b381-c5304b69b0fd | -13.09884 | -47.30227 | 2025-07-14 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5849420-a925-3406-b47f-0dc3472873d5 | -11.87516 | -54.67747 | 2025-07-14 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 508f2bfc-d1be-3606-9ee1-54d682944116 | -9.50304 | -47.56875 | 2025-07-14 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6388244-c6b8-37a5-9fdb-da407d84d8a8 | -13.02145 | -47.81781 | 2025-07-14 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ec4ee08-cde3-3d2f-a51f-f53618501ada | -10.6587 | -49.44297 | 2025-07-14 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d1f0f8a-71e4-3c97-aee9-ef9df6aa69c1 | -8.91439 | -47.34349 | 2025-07-14 04:51:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README13.md)
