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
| 9c4409ae-1db0-3f1f-85f3-efb814e9a31a | -8.9401 | -60.7288 | 2025-08-12 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 080a2b50-f174-3d46-9210-d3e70920de20 | -9.723 | -49.4806 | 2025-08-12 02:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| f772d9f8-bd9a-3567-ab56-1e900f89c081 | -22.9828 | -49.0361 | 2025-08-12 02:20:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 54.9 |
| bdda51b8-cdad-3dd5-b11c-89977da49eac | -7.1298 | -60.1374 | 2025-08-12 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 79ddb7ce-f0dd-35d1-81e2-7bd4a90dacd5 | -13.3619 | -50.2423 | 2025-08-12 02:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 43deb0ed-6960-397c-869d-afc9ae2e7210 | -7.1482 | -60.1366 | 2025-08-12 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 27c805b7-9287-3429-bc56-caf01c24d310 | -12.5746 | -46.9781 | 2025-08-12 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| ddecd49e-ed53-37ba-bbcd-b8e49c1bd8d3 | -7.1299 | -60.1182 | 2025-08-12 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 4f849832-4ff4-33c0-b1b8-2dfc0a8c1962 | -9.7041 | -49.4825 | 2025-08-12 02:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 4c47085f-f65d-3063-a1e2-61e88af36268 | -16.2961 | -52.9016 | 2025-08-12 02:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| acc6d244-a751-39db-b3af-c52ac0fd7a68 | -12.5742 | -47.0006 | 2025-08-12 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 9deedf11-9673-3f82-a791-9049f39abda0 | -6.5856 | -44.564 | 2025-08-12 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| a5fd7c59-77e6-3fd0-a409-33d07e753e77 | -12.555 | -47.0034 | 2025-08-12 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| fe3614cc-f047-3d6d-92bf-464fadff6a0f | -16.2957 | -52.923 | 2025-08-12 02:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e0143790-af2e-3d59-b513-fd107372516c | -12.5554 | -46.9809 | 2025-08-12 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ae069a4f-a619-30e4-9e90-60f3a62e8c5b | -7.1483 | -60.1174 | 2025-08-12 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 6fd1ecc3-9453-3e42-9b4e-f3082b57714b | -8.5211 | -43.3063 | 2025-08-12 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 00d6891f-3c5c-3fb3-9d57-04dbc14f9c9a | -12.7759 | -45.4445 | 2025-08-12 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 02f2c1d7-a65c-3d86-91d5-6460aaaf7b32 | -16.2957 | -52.923 | 2025-08-12 02:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 14e80b86-c0ba-392d-a5cc-9f4687839f8c | -16.2961 | -52.9016 | 2025-08-12 02:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 15827500-82ad-3ec2-8761-f450753111cc | -7.1298 | -60.1374 | 2025-08-12 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 30a13341-aadc-30dd-80fc-bc7e30da2a22 | -9.7041 | -49.4825 | 2025-08-12 02:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 421acf68-91a2-3a23-8fad-9320336ed1d6 | -8.5211 | -43.3063 | 2025-08-12 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 03bfdc83-1875-33a4-901e-8e4889e72bfd | -3.8394 | -47.7436 | 2025-08-12 02:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| d01317bb-fc65-32b3-adfc-a04d21b1c3d0 | -6.5856 | -44.564 | 2025-08-12 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 7cbb496a-71ed-3b53-bf82-088f662b8248 | -22.9828 | -49.0361 | 2025-08-12 02:30:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 55.3 |
| f6a71310-1755-3b63-9227-ba64b1b574e4 | -8.5788 | -54.7162 | 2025-08-12 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| f84b867f-a42e-3441-9001-aaa78a4d44f9 | -12.7759 | -45.4445 | 2025-08-12 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 640ed056-f881-3adc-b3ac-dd500f290c5f | -12.5742 | -47.0006 | 2025-08-12 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| f00d012b-b440-3221-b0da-56071ec3d6bb | -7.1299 | -60.1182 | 2025-08-12 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 21ce543c-b194-357b-9cd1-627b629e2235 | -7.1483 | -60.1174 | 2025-08-12 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| d14d6ef2-9e87-3dd5-a585-daf1b97c2f07 | -9.723 | -49.4806 | 2025-08-12 02:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 42d9b91e-b32b-3e51-a3d3-c193ef80faad | -12.5746 | -46.9781 | 2025-08-12 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a39fa778-ac3d-3c91-b0bb-141be2183173 | -8.9401 | -60.7288 | 2025-08-12 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 9448f0eb-6913-3cfe-82b7-6695b9bd7120 | -7.1482 | -60.1366 | 2025-08-12 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 015b3c54-e9c7-3478-bc4f-b908d8fdc190 | -7.1298 | -60.1374 | 2025-08-12 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 584b68ea-d688-3708-a9d8-95e48bba164e | -12.555 | -47.0034 | 2025-08-12 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 5ac89e18-30f8-3f88-8f6e-6fe4a89669dc | -7.1482 | -60.1366 | 2025-08-12 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 20e1fc13-e54d-35ec-8ccf-9e535d7b7f26 | -8.5788 | -54.7162 | 2025-08-12 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e71f4590-f617-3e60-bbbb-1daf4fb01c98 | -9.723 | -49.4806 | 2025-08-12 02:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 972d95b4-82a2-3616-b21b-fa8606af14f6 | -16.2961 | -52.9016 | 2025-08-12 02:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| eef6ae05-c1c0-3736-9f6f-47365ab3ec38 | -12.5746 | -46.9781 | 2025-08-12 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 3118712b-52f1-3cad-ac70-9a4efa062390 | -8.9401 | -60.7288 | 2025-08-12 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e9043798-144b-39d5-8ed0-1d4427c2c498 | -16.2957 | -52.923 | 2025-08-12 02:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| b4464241-bc77-3da0-b5a2-fc9f4abcb209 | -7.1483 | -60.1174 | 2025-08-12 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| e6dd4ed2-782b-3e21-88f4-2553fdb4b0ab | -3.8394 | -47.7436 | 2025-08-12 02:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 7a0729b7-b173-34c9-a80c-859bc8997947 | -7.1299 | -60.1182 | 2025-08-12 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 3c0c5ebf-805b-3ea8-94f8-c9339933d975 | -12.5742 | -47.0006 | 2025-08-12 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| c4ab3b04-aaff-311d-8845-761ad3e6943f | -22.9828 | -49.0361 | 2025-08-12 02:40:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 60.0 |
| aef058c9-84f2-3c18-b3da-2bb2d1913987 | -8.5211 | -43.3063 | 2025-08-12 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 045ac458-fefd-3069-ab7c-0d16e25a1bfd | -6.5856 | -44.564 | 2025-08-12 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 7ee5aa7e-e77e-347b-89c1-b4ca63b69387 | -22.9828 | -49.0361 | 2025-08-12 02:50:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 9cb377ab-60e7-3754-bce8-326eaf3c08ab | -12.5746 | -46.9781 | 2025-08-12 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 5ee13731-13e8-3a83-bd7b-f16b8f546647 | -12.5742 | -47.0006 | 2025-08-12 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 217.4 |
| 60fdaaf9-ebae-3d98-bb16-a84bad160d71 | -16.2957 | -52.923 | 2025-08-12 02:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| fb990ca8-eb57-395d-915d-b2f137f10084 | -12.5554 | -46.9809 | 2025-08-12 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| e7b68d36-e42b-3382-83c8-a2b274d34f6e | -8.5788 | -54.7162 | 2025-08-12 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 3cfbca94-2a00-3963-b750-dd7144c5caa9 | -6.5856 | -44.564 | 2025-08-12 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| ac22d78a-22dc-3898-8510-5e87f4d63f7d | -8.9401 | -60.7288 | 2025-08-12 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 058e4876-7c30-32eb-9f92-2a6d86f30f6a | -3.8394 | -47.7436 | 2025-08-12 02:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 682083cd-890e-383b-be25-d231423bb3b8 | -7.1299 | -60.1182 | 2025-08-12 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 671f70a2-e2f9-3fdf-b8e2-b5a30818a97b | -16.2961 | -52.9016 | 2025-08-12 02:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 32d075f9-5994-38ac-93d9-f5b99d1f4c0c | -7.1483 | -60.1174 | 2025-08-12 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 57946d50-f5c3-3275-b40b-454fe1fab7fe | -9.723 | -49.4806 | 2025-08-12 02:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 524ef6f8-6b53-338e-a1b1-9ae5656d32a5 | -7.1298 | -60.1374 | 2025-08-12 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 733d2b6a-7037-3337-89be-144efc4a3ec6 | -8.5211 | -43.3063 | 2025-08-12 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| bdcab7a3-66fa-3442-8b7f-be263455c69e | -12.555 | -47.0034 | 2025-08-12 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 9c897c49-71fd-35e1-ac92-1d84db10d30e | -7.1299 | -60.1182 | 2025-08-12 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| f5795508-f9ba-32ce-a03b-2ac3ae365e40 | -12.555 | -47.0034 | 2025-08-12 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 5eae09fa-2c95-3a92-af97-74e5d35c52c4 | -16.2957 | -52.923 | 2025-08-12 03:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 91a908e1-699e-3750-a533-d2e9ab89d425 | -9.723 | -49.4806 | 2025-08-12 03:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 42.0 |
| a5e6118e-0e26-3b50-913a-3b4c816f109b | -12.5746 | -46.9781 | 2025-08-12 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| c44eb7d7-7800-332f-9591-936df9fcd1e2 | -8.9401 | -60.7288 | 2025-08-12 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| cc57014e-cd6b-36fb-9ab6-f8ce6859549e | -9.7041 | -49.4825 | 2025-08-12 03:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| cd9d24a7-d93a-3456-bc13-42962dbf8dfb | -12.5742 | -47.0006 | 2025-08-12 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 9edd3961-4452-3b6c-8def-b6d2b6c69ba6 | -7.1298 | -60.1374 | 2025-08-12 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 3589cfde-de18-3e36-99a7-fa0fb4d52d13 | -16.2961 | -52.9016 | 2025-08-12 03:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 8f4cbdee-6878-3800-94d1-ade2fe0d5c41 | -7.1482 | -60.1366 | 2025-08-12 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 551eaab1-00b0-3c21-aac8-9018b1b80abd | -6.5856 | -44.564 | 2025-08-12 03:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| c9e26580-e996-3242-ac72-d3cacae183e6 | -16.3153 | -52.9201 | 2025-08-12 03:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 4c03a0d0-bac4-3b38-8ebc-f2820b6cb374 | -8.5211 | -43.3063 | 2025-08-12 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| d6fc05b0-991e-3f7a-bbde-72665f9c218c | -7.1483 | -60.1174 | 2025-08-12 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 9f19e698-ec86-3810-b682-3008ae76a24c | -16.2957 | -52.923 | 2025-08-12 03:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 35b5cb4a-2e6d-3ddb-ad6a-5c888264f9cb | -12.555 | -47.0034 | 2025-08-12 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 9b6bf1af-8084-357d-9a09-94e3df4a4d35 | -7.1299 | -60.1182 | 2025-08-12 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d6e9afa3-453b-304a-95c3-62b2a61551e2 | -7.1482 | -60.1366 | 2025-08-12 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 6b4ddf37-52fc-360b-9b9a-61c9b354c117 | -6.5856 | -44.564 | 2025-08-12 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| fe5af6a6-178f-3977-b5d0-2960d5f1135d | -7.1483 | -60.1174 | 2025-08-12 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d93f9fb2-6d6c-335d-9444-458a2c135496 | -8.9401 | -60.7288 | 2025-08-12 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| d73548ff-e1a8-3748-a300-786165e2b61a | -12.5738 | -47.0232 | 2025-08-12 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 6e6b6248-bed2-3262-b494-0763e0e330bf | -12.5742 | -47.0006 | 2025-08-12 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 148.0 |
| e3a28179-86f1-3495-a048-136cbca9afe6 | -16.3153 | -52.9201 | 2025-08-12 03:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 9ac2a9e3-aa53-3fe0-8659-815dbeb0d72c | -8.5211 | -43.3063 | 2025-08-12 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 2e80a127-1fbd-3dde-bd6b-65cd05579f80 | -12.5546 | -47.026 | 2025-08-12 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 0bed6af0-8cb6-3190-a217-52ede3e9b6d2 | -7.1298 | -60.1374 | 2025-08-12 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| cf75a904-d2bf-33c4-94c4-bb5f0f4862ba | -9.723 | -49.4806 | 2025-08-12 03:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| c54247e9-a0a2-3d00-920d-aa5e9b5b05be | -16.2961 | -52.9016 | 2025-08-12 03:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| a8c4cc82-c074-38d9-aec6-0f616fe0c632 | -7.3016 | -39.64541 | 2025-08-12 03:17:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bc7d752e-3979-339f-af1c-8ef4a70537e4 | -7.23466 | -41.90714 | 2025-08-12 03:17:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ebe854fc-5320-3e54-9009-1929f24d4e51 | -7.3031 | -39.6408 | 2025-08-12 03:17:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README7.md)
