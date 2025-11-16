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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66b70c94-0d4d-36fc-8086-f7d6cf4b8da4 | -6.2045 | -47.2832 | 2025-11-16 00:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 3ea6c2a9-ee1c-346c-9e96-2095a22c30a1 | -12.6672 | -47.167 | 2025-11-16 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 59203e70-b755-321d-9f95-2430bfd5fda9 | -6.2047 | -47.2612 | 2025-11-16 00:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 022aa213-8a0d-33d5-8c7a-29d67715c8fd | -12.2047 | -49.6121 | 2025-11-16 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 4e57dcbb-05c1-3e71-bab3-9c9abb80ba10 | -8.051 | -43.1237 | 2025-11-16 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 73b0679e-9dec-3a0c-a257-db4a4eaa08f7 | -2.5239 | -47.7899 | 2025-11-16 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 5f157f3f-a87b-3d60-b3b2-849d9d48a912 | -4.4246 | -43.4038 | 2025-11-16 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| c178ec79-6fbb-3664-888a-8217bcebb32c | -3.2554 | -45.7846 | 2025-11-16 00:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 4e27a4da-f40f-3c86-aeec-c04876435166 | -16.5637 | -47.6042 | 2025-11-16 00:00:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 150.6 |
| ecd87cdc-65e0-3fe9-ae5f-c138f9f95c7f | -11.9458 | -44.6239 | 2025-11-16 00:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 7a106180-b4a4-30e5-983f-cc8b37a64c77 | -12.6557 | -46.7407 | 2025-11-16 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 271.1 |
| f2ae541a-d69a-3bde-a6f5-510d5d68d106 | -3.8288 | -49.8012 | 2025-11-16 00:00:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b03c580e-2247-349a-b1f9-b9afb6632875 | -8.3239 | -45.4052 | 2025-11-16 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 7f497b2d-01dc-3058-8dd0-9e207d0d06b7 | -4.7029 | -46.2953 | 2025-11-16 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 73fee756-d59b-3014-a800-3d32b18994d7 | -4.8432 | -47.5428 | 2025-11-16 00:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| cee29944-d82a-3889-8881-10faf7f90944 | -8.5798 | -46.0343 | 2025-11-16 00:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 4fff3f4b-554e-334b-907d-5c00ffc763f8 | -11.9262 | -44.6502 | 2025-11-16 00:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 4493cb70-dc13-3152-b1e1-3d5a330bc1be | -2.8925 | -53.2842 | 2025-11-16 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| b44b681e-b6a7-38ad-af2f-4217715dab77 | -6.6873 | -42.0535 | 2025-11-16 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 6860e4ed-8f12-3188-bd55-4d24dc006253 | -6.3119 | -43.8036 | 2025-11-16 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 984d03c1-058c-3856-a464-96d2f7a0631c | -3.5946 | -41.6577 | 2025-11-16 00:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 74a9b16c-a773-3251-905f-6a2c2f75980f | -12.0004 | -49.2683 | 2025-11-16 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 1a99982b-e4b8-3e10-abe3-224e09afda9e | -6.7053 | -42.1234 | 2025-11-16 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| c02133af-5ba0-3907-8449-a04872fc3ad6 | -2.5053 | -47.812 | 2025-11-16 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 39020c71-987c-3844-a171-77bf5a804f64 | -2.9235 | -45.2362 | 2025-11-16 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 44.3 |
| b2f1bddf-7842-3ab2-9cd4-f6c5249ee4f3 | -8.0703 | -43.0981 | 2025-11-16 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 269.3 |
| a8783699-5638-3309-a3ca-7c302659ba1f | -6.6875 | -42.0296 | 2025-11-16 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 415ece56-0ee5-3ce3-ba2f-7d7c4e10bb51 | -12.0191 | -49.2877 | 2025-11-16 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| af7d2e29-2af8-332c-9b7b-d54e42d4f83f | -6.7016 | -40.7717 | 2025-11-16 00:00:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| f3c092a5-9f45-3880-a7d6-37a045c262c0 | -12.0195 | -49.2659 | 2025-11-16 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 83368b0d-584f-32ac-826b-c53c0957034f | -4.7395 | -46.3821 | 2025-11-16 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 13adb719-b276-31bc-83f6-32f4b53d166e | -4.4059 | -43.4049 | 2025-11-16 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 7f6053c7-569a-30c1-b1a1-9b0fb6167903 | -8.0516 | -43.0765 | 2025-11-16 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| b4d8d3fb-1699-3102-90c1-93e4c282cbc2 | -12.0 | -49.2901 | 2025-11-16 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| c718dec1-75d7-369e-b88e-d5f99d8c7a8a | -4.7027 | -46.3176 | 2025-11-16 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 132.1 |
| a831fa6f-5906-3f93-bff6-17904cd8dd4e | -14.649 | -46.5807 | 2025-11-16 00:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 6a0c1dbd-afd0-3928-a9b0-0ccea74c9245 | -2.5238 | -47.8332 | 2025-11-16 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| ebe60d5a-189c-3539-95f7-a2e4586680ab | -3.3294 | -45.8487 | 2025-11-16 00:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 75.9 |
| bb81c296-fc3e-3c62-985b-8030f33b16a8 | -8.0513 | -43.1001 | 2025-11-16 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 229.5 |
| e8e97aca-52c1-391c-b8ff-3ff3e426ec2c | -12.0557 | -48.209 | 2025-11-16 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| ea9ee20e-be13-3c97-b4f6-a717b8cb88af | -6.2232 | -47.2819 | 2025-11-16 00:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 198.8 |
| 39736aad-243f-399b-8368-687088de4ba3 | -4.843 | -47.5646 | 2025-11-16 00:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 4be99145-78da-38d9-920a-3fcfb8fd2854 | -6.3121 | -43.7804 | 2025-11-16 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 7bf60e4e-a561-375b-8b47-414f4164e9f0 | -6.7013 | -40.7962 | 2025-11-16 00:00:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 222.3 |
| 7ec65ba3-35e0-3500-b9f5-ef46ef59c066 | -2.5238 | -47.8115 | 2025-11-16 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 239.3 |
| 39029ac6-786b-39a0-af02-a55743025562 | -12.6553 | -46.7633 | 2025-11-16 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 6b2489e1-fadb-31a7-9687-7659af60d167 | -11.9454 | -44.6473 | 2025-11-16 00:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| fcd9d393-9e7c-30c4-9b2e-a5243733fd14 | -8.0706 | -43.0745 | 2025-11-16 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 86802986-55c4-3706-ab95-2496ecf273db | -6.6824 | -40.7981 | 2025-11-16 00:00:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 106.2 |
| ecbbdf3a-e589-3cf5-9f00-38e60d7007c5 | -8.07 | -43.1216 | 2025-11-16 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| b0612b01-7e78-3443-89a7-166f90ed1c3f | -11.9266 | -44.6269 | 2025-11-16 00:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| aaa1aa6a-6642-3363-91e2-22cef64a3e03 | -1.9885 | -47.3684 | 2025-11-16 00:00:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| a80add28-0154-3c50-875f-51f68e4d1eb9 | -16.5835 | -47.6005 | 2025-11-16 00:00:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 0424973c-a0aa-3cc7-863a-03eb297473a0 | -4.6841 | -46.3186 | 2025-11-16 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 5fc85907-0e86-3be1-87a7-9be2192f4d14 | -6.6687 | -42.0314 | 2025-11-16 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| c08f293a-0e32-3f62-aca3-e73e738d5b3f | -8.5795 | -46.0568 | 2025-11-16 00:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 76d32f47-7759-35ad-bec0-c875796d7d4b | -1.9886 | -47.3465 | 2025-11-16 00:00:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| b02bb036-3af6-3bbe-ae03-a8143ccd8eb9 | -6.2234 | -47.2599 | 2025-11-16 00:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 1a3694a1-9a78-3b5a-91d9-e3118a43b307 | -12.6864 | -47.1642 | 2025-11-16 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| fc1c2793-2922-3ab6-ab19-203e002751c4 | -18.63755 | -41.27965 | 2025-11-16 00:09:00 | TERRA_M-M | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 28d42e00-f102-3ac0-af74-8410143afbe0 | -17.81574 | -41.58499 | 2025-11-16 00:09:00 | TERRA_M-M | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 1061c6c6-43bd-3baa-8144-23e22deb1d7b | -18.6361 | -41.26979 | 2025-11-16 00:09:00 | TERRA_M-M | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| d315e702-3af9-3ac6-93e7-0ba9251560a5 | -19.09319 | -45.93805 | 2025-11-16 00:09:00 | TERRA_M-M | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b23d0e85-0242-3e97-9383-df71d19f7ab1 | -17.81713 | -41.59459 | 2025-11-16 00:09:00 | TERRA_M-M | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| d271534a-c8c4-37e9-9ffa-33eae921a7f4 | -4.6841 | -46.3186 | 2025-11-16 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 90b804ef-99cb-3bc1-9e39-14d72063f2ac | -12.0557 | -48.209 | 2025-11-16 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 1d6a3427-20de-3225-9b39-784466db3bf0 | -6.7053 | -42.1234 | 2025-11-16 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 4cc796c8-5b12-330e-b7f8-a732170c5d77 | -12.6553 | -46.7633 | 2025-11-16 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 541d7545-c84d-309f-ba0a-07edc5f527ed | -16.5835 | -47.6005 | 2025-11-16 00:10:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 91.6 |
| c94801fc-2a7c-3970-9858-9569dee61efd | -12.6864 | -47.1642 | 2025-11-16 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| d732e283-aa51-3d60-9f69-28e64e0c3a75 | -4.7395 | -46.3821 | 2025-11-16 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 438d8755-9971-3577-bd91-24f71ea06005 | -4.8432 | -47.5428 | 2025-11-16 00:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 597901f0-ea06-3b7a-abcb-aaf9c02a908f | -3.2554 | -45.7846 | 2025-11-16 00:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 95245cce-5406-3929-8c54-497d533cadb0 | -4.843 | -47.5646 | 2025-11-16 00:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 1ab4f1a9-714a-3768-a99c-3e85e24411d7 | -6.6875 | -42.0296 | 2025-11-16 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 9005f343-af87-3d8f-b633-90b629617f56 | -6.3121 | -43.7804 | 2025-11-16 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| a8cd0e34-728c-30f9-be84-f1d62f4eb81c | -12.2047 | -49.6121 | 2025-11-16 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| d42467ba-7abe-3231-8349-daa024854d93 | -8.5798 | -46.0343 | 2025-11-16 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| eabc7d94-e611-30a8-9bd2-7dd094b62b73 | -3.8288 | -49.8012 | 2025-11-16 00:10:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| ca1a352a-de7d-3a20-9b71-4ede3628faec | -4.7931 | -41.6816 | 2025-11-16 00:10:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 4892ce12-1e27-379c-98c4-137f7eeb9f0c | -2.5053 | -47.812 | 2025-11-16 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 371d6c6e-85f2-351b-9ac8-31c75e58d05f | -6.3119 | -43.8036 | 2025-11-16 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 0e73f12b-1e7b-352d-b039-41f10d0827af | -8.5795 | -46.0568 | 2025-11-16 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| a0a74132-f454-310a-84ad-2d7855b5f3bf | -2.5238 | -47.8332 | 2025-11-16 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 0d36491c-a17e-3144-9c3b-32c155a3cc52 | -12.0195 | -49.2659 | 2025-11-16 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| c4146255-246d-391a-bde9-795746678253 | -12.0191 | -49.2877 | 2025-11-16 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| da020372-324c-32d8-8ecc-b67ef34177d3 | -16.5637 | -47.6042 | 2025-11-16 00:10:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 1a7b556a-61e4-3b86-8bc7-8a803377754d | -12.6672 | -47.167 | 2025-11-16 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| f754fe1f-dca1-374e-8acd-ffb902f72fae | -8.051 | -43.1237 | 2025-11-16 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 559cf961-344e-37b9-975d-ea1a61d3d1c9 | -11.9458 | -44.6239 | 2025-11-16 00:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 5366db37-1a69-3130-9f56-8c353ac1a5a3 | -8.0703 | -43.0981 | 2025-11-16 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 229.0 |
| d402cc0b-c02d-3370-bcab-c0774720f47d | -3.3294 | -45.8487 | 2025-11-16 00:10:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 7fcd8a83-c979-3e8b-bd43-8718f7a5d1d0 | -12.0 | -49.2901 | 2025-11-16 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 076b20a4-8de7-30d3-80db-255875e83555 | -6.7013 | -40.7962 | 2025-11-16 00:10:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 5303885d-3f8d-3195-98b8-0d7c56cc0851 | -6.6687 | -42.0314 | 2025-11-16 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 39302e67-7038-342e-a926-d0bf4a8f0289 | -8.0513 | -43.1001 | 2025-11-16 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 246.9 |
| 97881a27-1c92-334e-95df-c5d5a359a432 | -3.5946 | -41.6577 | 2025-11-16 00:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 49ba9428-342a-36f3-9ba9-eb025d05253a | -8.07 | -43.1216 | 2025-11-16 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 842c75bd-0295-39c2-be5c-2076dc50904c | -4.7929 | -41.7056 | 2025-11-16 00:10:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 1c89d6fb-e94d-3722-b07d-79a64e5f3037 | -2.8925 | -53.2842 | 2025-11-16 00:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |


[Clique aqui para ver as próximas entradas](README2.md)
