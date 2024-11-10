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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c47d5fbf-e75e-3b63-ba9a-fe2f2b4ff805 | -2.0953 | -48.8338 | 2024-11-10 12:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 7b36b5bc-c846-304c-90f3-c300b8d203c6 | -1.476 | -54.2965 | 2024-11-10 12:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 3fce840f-2948-37a5-9124-2be63d776bd9 | -23.9089 | -54.083 | 2024-11-10 12:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 100.8 |
| 95c286a3-bff6-3292-8a4a-1078bc1a6451 | -2.0954 | -48.8125 | 2024-11-10 12:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f7b4611d-dd09-3e87-be7d-ea16d3dc1118 | -4.3979 | -41.8987 | 2024-11-10 12:50:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 1e497733-a265-3124-a6ba-3f2d3fdd99c9 | -3.9955 | -46.3981 | 2024-11-10 12:50:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 689a7e17-5c4b-3f4d-9607-2c408035b787 | -3.4015 | -50.2801 | 2024-11-10 12:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 313.6 |
| 779b4788-fc63-34d6-b2fe-108b2796c868 | -23.9095 | -54.0606 | 2024-11-10 12:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 112.7 |
| c2c1d482-8f46-3d17-b55f-ede339e43f2f | -1.8403 | -55.6442 | 2024-11-10 12:50:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 65c864ed-327b-37d4-b936-98877486b68b | -4.1099 | -49.1315 | 2024-11-10 12:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 23a6e993-9e07-39b2-ac90-6800acae76de | -3.9669 | -48.1716 | 2024-11-10 12:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| eef02bdd-2548-3268-b2bd-0b4c1bca09e4 | -1.476 | -54.3166 | 2024-11-10 12:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| c6bb6457-63fa-3935-ad49-181b910802ac | -1.8017 | -48.0666 | 2024-11-10 12:50:00 | GOES-16 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| f7c5cead-d5cb-3dc2-ac80-6ba68f26ae56 | -1.5299 | -54.9941 | 2024-11-10 12:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 804ed47c-154e-3eb9-bc19-6981db636785 | -17.6069 | -57.5304 | 2024-11-10 12:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 307.6 |
| e9185071-451b-3c6f-8f35-627520da756d | -17.313 | -57.4834 | 2024-11-10 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 3bfacf21-cf6e-3b7f-b877-83a0e184e211 | -6.1366 | -42.5544 | 2024-11-10 12:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| 267e6319-b9d8-3581-8b9c-50c64b06d599 | -5.9788 | -45.3621 | 2024-11-10 12:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 69e6c494-6d5c-3922-b756-9fda97c8cdb2 | -5.5795 | -43.9761 | 2024-11-10 12:50:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| dadd57bc-5926-3d79-9f6e-2d6e1b8316ad | -3.9953 | -46.4203 | 2024-11-10 12:50:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| b8ef8b7b-ef86-3f6e-8248-03d9cefc7311 | -1.5116 | -54.9944 | 2024-11-10 12:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 636462bc-78ff-341d-b5be-63c7fa5b119c | -17.2933 | -57.4857 | 2024-11-10 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.0 |
| 91500d9a-2dd9-3fdc-a00c-c93844274267 | -6.1363 | -42.578 | 2024-11-10 12:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 379.8 |
| c5f39df0-e702-366d-9303-d0e1d68bbb28 | -5.5608 | -43.9775 | 2024-11-10 12:50:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 027b3fb6-a3d9-3707-99f1-21d1cdd137eb | -4.4349 | -44.6229 | 2024-11-10 12:50:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 1f0e6d46-7649-32c2-841c-371668ae0e17 | -2.0656 | -46.3339 | 2024-11-10 13:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 9dc9a38a-91c2-3c0a-9651-65420cd0a403 | -2.6388 | -46.7597 | 2024-11-10 13:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f663ad98-4ae0-3b56-8aae-73737cdb59b0 | -1.8017 | -48.0666 | 2024-11-10 13:00:00 | GOES-16 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 3679bd50-e353-367a-8495-5b5727f8eb3f | -1.5116 | -54.9944 | 2024-11-10 13:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 0ab69c93-6480-336c-a960-a1a037ec0f48 | -23.9095 | -54.0606 | 2024-11-10 13:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 151.6 |
| 26c81819-461f-3739-b476-f989d4753e34 | -2.931 | -52.7753 | 2024-11-10 13:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 97062a72-3e57-35f7-a539-598f9dc045a0 | -5.5795 | -43.9761 | 2024-11-10 13:00:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 140.5 |
| fda4854a-9cac-3202-9324-1ba6875c160a | -2.2804 | -48.7226 | 2024-11-10 13:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| b5a2af62-d135-3e8d-8c97-86744e24537e | -3.9953 | -46.4203 | 2024-11-10 13:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 114.2 |
| d859eb63-7984-37fe-bdf5-6784269e190a | -3.9955 | -46.3981 | 2024-11-10 13:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 77879019-9ed0-3b29-995e-8145418a997b | -4.0913 | -49.1323 | 2024-11-10 13:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 18a99509-211a-382b-8588-197caaa5bde2 | -17.6083 | -57.4482 | 2024-11-10 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.9 |
| 84c1b70d-5c59-3a96-a7cd-e1acf838f3dc | -4.1244 | -43.6064 | 2024-11-10 13:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 14371fc4-853d-3f2d-be5e-fc62fe779b76 | -3.9483 | -48.1724 | 2024-11-10 13:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 426fc137-8a71-3eb8-b2ea-b23eedc00b94 | -2.8605 | -51.8349 | 2024-11-10 13:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 29cd3f98-e975-3452-ac97-f163ec60847a | -17.6073 | -57.5099 | 2024-11-10 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 369.5 |
| 31dcb812-9bc9-3a66-90b9-cd54aa0c26f1 | -3.9485 | -48.1508 | 2024-11-10 13:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 83b83783-224a-3e12-a6af-ef805b6fd908 | -4.1246 | -43.5833 | 2024-11-10 13:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| ef9f4d07-b11c-37fd-b187-216a1ac104b1 | -5.4548 | -43.2426 | 2024-11-10 13:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| bbadc1f5-f4c7-36ad-a38a-973540863f26 | -5.5608 | -43.9775 | 2024-11-10 13:00:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 4099f365-0657-31c9-a5e0-433e917f6e34 | -23.9089 | -54.083 | 2024-11-10 13:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 229.1 |
| c5b1ac1f-53db-3597-8e16-341a1e2e9fd2 | -17.2933 | -57.4857 | 2024-11-10 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.2 |
| 7d736365-9447-31cb-92e7-610b6db493c5 | -2.0953 | -48.8338 | 2024-11-10 13:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 957f90d2-1fe2-3932-abb0-e0de44b15936 | -6.1366 | -42.5544 | 2024-11-10 13:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 56c444ed-d1b1-3cf6-b559-c7f4bd87b236 | -2.0954 | -48.8125 | 2024-11-10 13:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| ee0bcc12-c240-3e2f-9ece-a4ebeb5f1b3a | -2.0655 | -46.356 | 2024-11-10 13:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 5615324d-f896-3509-a05e-0b87f25537c2 | -17.6069 | -57.5304 | 2024-11-10 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 301.7 |
| f1bd81cb-aba1-3dac-abbd-abb8e57af1e0 | -2.2803 | -48.744 | 2024-11-10 13:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 0fe01be6-2054-38ab-8582-98ae1d17e4cb | -1.5299 | -54.9941 | 2024-11-10 13:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 2bddf88e-444f-3e5f-a6a4-1f02a1646798 | -2.0664 | -46.0899 | 2024-11-10 13:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 372b8c1e-abd0-3526-9d0d-a45a99dd4c9b | -6.1363 | -42.578 | 2024-11-10 13:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 322.2 |
| 7d41fe37-be95-37bc-a749-efa815b29b77 | -4.4349 | -44.6229 | 2024-11-10 13:00:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 760c2458-c665-391a-a978-c3291e46518c | -3.9669 | -48.1716 | 2024-11-10 13:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 9b4fa5d4-4901-373f-a808-3d3c53ffa968 | -4.1099 | -49.1315 | 2024-11-10 13:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 139.7 |
| 32a001e2-51d0-319e-88ba-9f797ef61a24 | -3.4015 | -50.2801 | 2024-11-10 13:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 262.6 |
| ade03822-bbb8-3ede-b18c-da4c4895b94a | -6.16 | -42.53 | 2024-11-10 13:00:00 | MSG-03 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 21f299c3-bcd7-3b64-9701-67d2e6ee6e1a | -6.13 | -42.57 | 2024-11-10 13:00:00 | MSG-03 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 369b9381-cf0a-36c9-a00d-33cba2af93a8 | -6.16 | -42.58 | 2024-11-10 13:00:00 | MSG-03 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d51f6710-df1c-3620-8595-f7cddbfd7d58 | -6.16 | -42.62 | 2024-11-10 13:00:00 | MSG-03 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 95722f26-a5cc-3450-9335-4fef5ca13633 | -8.84 | -47.7 | 2024-11-10 13:00:00 | MSG-03 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d30cd8f-91d8-3e6c-a42a-5399f2c2bc5c | -8.39 | -44.16 | 2024-11-10 13:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8b1695a7-248a-3875-b434-7adacedd1a84 | -8.42 | -44.12 | 2024-11-10 13:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6ad47aa3-9f9f-32a4-ab8a-cfd25293bc3c | -8.39 | -44.12 | 2024-11-10 13:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bfd3d518-a384-3b81-be95-bc74360a7446 | -6.1366 | -42.5544 | 2024-11-10 13:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| c97334d8-5b58-352a-aa01-f678815b71f6 | -23.9089 | -54.083 | 2024-11-10 13:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 227.1 |
| f00f2962-d375-3e07-844a-0436034e6911 | -4.4349 | -44.6229 | 2024-11-10 13:10:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| e4f5938d-8b5a-3ffb-8b50-962c5ceff183 | -3.9485 | -48.1508 | 2024-11-10 13:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 900680ce-91eb-3ad1-8e36-b42c4e3c1044 | -5.5608 | -43.9775 | 2024-11-10 13:10:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 87dd391d-d2a8-3045-b2e7-fafd193e0395 | -17.6069 | -57.5304 | 2024-11-10 13:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 331.8 |
| 8a73e7e6-c861-3234-a57c-65ab8d7a2138 | -4.1099 | -49.1315 | 2024-11-10 13:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 3d5f3b47-f5cf-3758-8a6e-969015dc470e | -5.66 | -43.344 | 2024-11-10 13:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 3a0d8408-f7dd-39ab-a5ea-55acb0b04ba4 | -6.1363 | -42.578 | 2024-11-10 13:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 341.4 |
| 5121c5a2-00ac-3783-8f82-e83c531219b1 | -5.4546 | -43.2659 | 2024-11-10 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 150e9ff9-14b5-3da6-b2d8-1f8fb87a47e7 | -2.6388 | -46.7597 | 2024-11-10 13:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e3597fb6-262b-3c54-88ad-87a28acb28b7 | -2.0953 | -48.8338 | 2024-11-10 13:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 491595a8-337f-316e-b94d-1e77f2fa8611 | -3.4015 | -50.2801 | 2024-11-10 13:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 304.7 |
| 4fd30900-7d59-3f38-a59f-e1603e9f9e22 | -5.455 | -43.2192 | 2024-11-10 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 0ddb0e14-a897-3cc3-bd34-dda9c7abbc95 | -2.0656 | -46.3339 | 2024-11-10 13:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 60eae1ec-8b17-3d93-bf93-8c4a82727aa3 | -2.9494 | -52.7748 | 2024-11-10 13:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 0b93921a-ff8f-39eb-94cb-3bcb75fc094c | -3.9953 | -46.4203 | 2024-11-10 13:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 14d867c3-f2a9-348a-9575-3f922801d975 | -3.6325 | -41.5839 | 2024-11-10 13:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 7c385731-28f0-331c-b4f1-5bf26c0b5aff | -3.9955 | -46.3981 | 2024-11-10 13:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 5949b90c-c334-391b-b2ef-fa48529662db | -1.5116 | -54.9944 | 2024-11-10 13:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| b7f6c07b-4de9-39af-85f0-ec8405189401 | -3.9483 | -48.1724 | 2024-11-10 13:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 20c7114d-54dc-3cb2-9072-94618c52a02b | -3.9669 | -48.1716 | 2024-11-10 13:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 515abe7b-31b1-34cd-833c-cddd8caacfd3 | -4.3978 | -41.9226 | 2024-11-10 13:10:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 78be4015-8639-3da9-b47f-9f33624a21af | -1.5164 | -52.1696 | 2024-11-10 13:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 29318dc2-144c-3e9d-82d9-008e88a13a74 | -2.0478 | -46.0903 | 2024-11-10 13:10:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 4c29b657-ffb9-3bc9-a4fd-5691c7a453d6 | -2.8605 | -51.8349 | 2024-11-10 13:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| aeb820a1-71cf-3002-bc80-129c6c952ce2 | -17.6083 | -57.4482 | 2024-11-10 13:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.8 |
| 4a155652-67be-3578-bff3-8dbc00a7723b | -4.3979 | -41.8987 | 2024-11-10 13:10:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 120.1 |
| bce5b85e-c269-3a85-bc38-026f6f9981cd | -5.9788 | -45.3621 | 2024-11-10 13:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 60d50a69-e1ee-3114-a1a5-f6419a93d588 | -5.4548 | -43.2426 | 2024-11-10 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 4e01a23e-5c9d-3cb0-b2f9-6824354bfc14 | -17.2933 | -57.4857 | 2024-11-10 13:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.4 |
| d841f863-e2cf-3ac6-bac9-78ac6776a1dd | -2.0655 | -46.356 | 2024-11-10 13:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |


[Clique aqui para ver as próximas entradas](README128.md)
