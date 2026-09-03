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
| 50bdf6a3-e068-30b0-b9f9-3f820befcec3 | -5.5647 | -60.2312 | 2026-09-03 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| a95bd21b-bb9d-379c-84f2-3d636c21d587 | -6.6541 | -59.4452 | 2026-09-03 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 93786411-fe6c-39e9-862c-daf7ead6e4e5 | -6.6542 | -59.426 | 2026-09-03 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| acc30d75-4785-32a9-8c78-3ef9a9fdd493 | -6.654 | -59.4645 | 2026-09-03 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| e5578bcb-13e1-3d5c-84d5-24bcaa2abb03 | -6.3237 | -56.0434 | 2026-09-03 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 21ef1a17-47b2-3f2e-a034-f65a257baefe | -3.2485 | -47.2657 | 2026-09-03 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| c0432ead-a56e-3a26-bf07-8af32c6c8535 | -6.6357 | -59.4459 | 2026-09-03 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.2 |
| f9e920ba-4522-3053-8b1d-5555fdb8ed38 | -12.4033 | -44.8089 | 2026-09-03 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 218.8 |
| 1c24f64a-d9d7-31a9-8f7f-12794a67dca9 | -12.4225 | -44.8059 | 2026-09-03 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 3ba4589f-d20b-3c4d-8621-5e9165ea5ebf | -18.7962 | -48.9186 | 2026-09-03 02:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 3f5d000a-3285-3a31-91fb-c10a5665053a | -6.6358 | -59.4267 | 2026-09-03 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 25951944-db45-3eb3-b3db-2869e7871362 | -12.4037 | -44.7856 | 2026-09-03 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 5dc98459-4987-3dbb-9e07-954342f1e045 | -6.3236 | -56.0632 | 2026-09-03 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| c39ccfe7-4f66-3da9-9e7d-9f6faa3f630b | -10.8826 | -45.3075 | 2026-09-03 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 48e98c7a-6031-3c88-adda-28f5bd85837f | -18.776 | -48.9226 | 2026-09-03 02:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 152.1 |
| f04a1dc5-c12a-3958-a91a-29fa59ab5e6a | -10.9815 | -45.0874 | 2026-09-03 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| b5211618-c458-355a-9e0d-7e8f31b945be | -7.2926 | -60.7243 | 2026-09-03 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| b2f3c5e0-d320-3f2c-b141-ae758e63a678 | -8.0737 | -50.9656 | 2026-09-03 03:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 9a00ca43-6352-302e-a5e5-8e27176b5aff | -3.2486 | -47.2438 | 2026-09-03 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 1dd7ddfc-d8ca-33f0-9581-eb9c1a3ef67a | -8.0924 | -50.9642 | 2026-09-03 03:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 8185f352-b250-3124-9f42-cd700d63a306 | -6.3237 | -56.0434 | 2026-09-03 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0ff5e6b1-0193-3454-a664-955ca8a4b084 | -6.6357 | -59.4459 | 2026-09-03 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 7d7b4b58-d0ac-3b87-90e5-82db307947bf | -8.4675 | -54.6631 | 2026-09-03 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| a478e490-4456-3680-bce5-75f12e686fd8 | -6.6358 | -59.4267 | 2026-09-03 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 1dc533fc-fbc8-3795-8734-4af9ae681206 | -6.6542 | -59.426 | 2026-09-03 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| d04659bc-ae08-3d57-ab1e-406430f636d4 | -18.776 | -48.9226 | 2026-09-03 03:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 8defaeeb-4300-3c13-a7ae-8d27168ef941 | -3.2485 | -47.2657 | 2026-09-03 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 05254d5a-6bba-3c0d-a7b1-eab3936e401f | -18.7962 | -48.9186 | 2026-09-03 03:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 51.6 |
| fe056414-e3ab-37d5-9ddf-b99fc40b9dc4 | -6.3236 | -56.0632 | 2026-09-03 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| b9a85e35-53f3-38ed-ba5a-cea5e1dde18e | -6.654 | -59.4645 | 2026-09-03 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 1538c14f-71a6-325f-877e-32ec15892451 | -12.4033 | -44.8089 | 2026-09-03 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 213.8 |
| fa8552a8-ffdf-34df-a621-5f238f1e94e9 | -6.6356 | -59.4652 | 2026-09-03 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| f3749b6f-75a9-3da7-a5ca-f2f7bebed83d | -12.4225 | -44.8059 | 2026-09-03 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| a177ad54-b5ae-38c0-b123-e38b3f8d76dc | -12.4037 | -44.7856 | 2026-09-03 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 47ae695e-b998-3ade-9c93-821a42d31444 | -6.6541 | -59.4452 | 2026-09-03 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 150.1 |
| b959ab55-bb4a-396a-98da-f91e62c70355 | -8.4677 | -54.6429 | 2026-09-03 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 642db6a7-da01-301e-ab14-bd0267aa91ea | -18.7967 | -48.8958 | 2026-09-03 03:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 63bfc8e4-9dfa-3c7f-9630-7b0e59074565 | -10.9815 | -45.0874 | 2026-09-03 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 3d987501-0158-3752-acf0-913b66e235ec | -6.3052 | -56.0442 | 2026-09-03 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 3d7b09c2-180c-3acb-8e42-5f01eb41530b | -10.8826 | -45.3075 | 2026-09-03 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 9e538967-6681-3b6f-8c3c-f6043f108a86 | -11.0006 | -45.0847 | 2026-09-03 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| c78ccd0e-719a-344c-a3a5-ce2f636e51b9 | -18.7766 | -48.8999 | 2026-09-03 03:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 801e291a-fb34-3289-aed5-5e0b8e367187 | -12.423 | -44.7825 | 2026-09-03 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 1774f4ec-d2d8-3356-8676-f34a29783de4 | -18.7967 | -48.8958 | 2026-09-03 03:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 87da639e-d84e-37f6-a50e-c63d506c6a5b | -6.3237 | -56.0434 | 2026-09-03 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| afdbabf1-3c27-3129-bdcf-d553f6055390 | -6.6358 | -59.4267 | 2026-09-03 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 95b77927-60bc-369d-89ed-39328d000dd1 | -6.6541 | -59.4452 | 2026-09-03 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 48dbb7e7-edf2-304c-8fca-289b3b3ce38d | -6.6356 | -59.4652 | 2026-09-03 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| ec228296-96a4-3e46-80c2-a9be113a29f5 | -8.4677 | -54.6429 | 2026-09-03 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| fa9db245-f834-3d09-9e1d-0a16a69837cf | -6.6698 | -59.9443 | 2026-09-03 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 8209737a-9dcb-3b45-8030-512021419cfc | -3.2485 | -47.2657 | 2026-09-03 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 35af4f29-4cdd-3e1d-b84b-ab7b30fd2243 | -18.776 | -48.9226 | 2026-09-03 03:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 10db5399-bddc-320e-91fc-85294dd4b2b8 | -18.7962 | -48.9186 | 2026-09-03 03:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 4c4b0971-17d3-3221-8e78-72570081f213 | -6.654 | -59.4645 | 2026-09-03 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| e49cbaf6-28ba-352e-a650-9e1b4cb2d333 | -3.2486 | -47.2438 | 2026-09-03 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 43a34268-0aed-3c57-a204-827891046303 | -10.8826 | -45.3075 | 2026-09-03 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b90db361-979b-3bc5-9d1d-287ae85807ba | -6.6542 | -59.426 | 2026-09-03 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 3aadcb45-4018-3059-89bf-3f9a3a576f57 | -11.0006 | -45.0847 | 2026-09-03 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 7032eca1-3e4d-3c17-81a1-99dd954fc5cb | -6.3052 | -56.0442 | 2026-09-03 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| a4c44472-0290-3b8a-8f38-ec549d5b4b86 | -8.4675 | -54.6631 | 2026-09-03 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 95608e11-ce37-3d3d-85b1-3df4eb9a4974 | -18.7766 | -48.8999 | 2026-09-03 03:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 76.5 |
| b0905ec7-1d87-3408-a117-0e41a064be55 | -6.3236 | -56.0632 | 2026-09-03 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 90f3a6a9-6a97-3fc7-abee-367b1e6be079 | -6.6883 | -59.9436 | 2026-09-03 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 72cc2dd7-50fe-38a6-9ef8-106849115f3e | -8.0924 | -50.9642 | 2026-09-03 03:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 36f7f49f-c5b9-3c59-8336-886d2fca8964 | -6.6357 | -59.4459 | 2026-09-03 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.3 |
| e474323a-ea75-3ccb-93ed-333cc6235ea6 | -6.3051 | -56.064 | 2026-09-03 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| ca8858dc-f56d-3c34-bcd6-fb3aade91e22 | -12.4 | -44.79 | 2026-09-03 03:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e5f7264e-f22c-348a-be71-ceced561a710 | -13.41252 | -42.49628 | 2026-09-03 03:17:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7295a875-ff20-3273-83e7-714b5f20c56c | -3.96385 | -40.05425 | 2026-09-03 03:17:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fc5f63ac-1fa4-32d4-9a0f-2a755e66ea94 | -3.96274 | -40.0606 | 2026-09-03 03:17:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e9f54a94-4170-30af-83bd-d45d0850f9b4 | -13.41122 | -42.50228 | 2026-09-03 03:17:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 49421171-e163-37fb-a0bd-62e55214829f | -13.40576 | -42.49482 | 2026-09-03 03:17:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6b810c1f-4594-30f5-bb6a-5aa39319cdc4 | -10.17645 | -36.25155 | 2026-09-03 03:19:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 63eb07b4-1cfc-35fe-89a8-8162262a1149 | -14.21064 | -42.04094 | 2026-09-03 03:19:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8b32413a-33e0-374a-a3df-70b9b568d5c6 | -14.20934 | -42.04687 | 2026-09-03 03:19:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 70e41d1c-8b58-3f93-8a54-7da28457bf04 | -10.17905 | -36.2528 | 2026-09-03 03:19:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 664fca50-f382-3e2a-b1bc-11a45f2ae7f8 | -14.21075 | -42.04438 | 2026-09-03 03:19:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 07f41a81-c79f-31e0-a981-7405f8311755 | -11.2966 | -50.5367 | 2026-09-03 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 75e66cb3-f7a2-3de0-bc0a-9bd811dcf0b7 | -6.6542 | -59.426 | 2026-09-03 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| c5d835c4-e4ac-33b0-9347-6f6c89c4babe | -18.7766 | -48.8999 | 2026-09-03 03:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 30e38e99-4f29-3af1-bdd1-3dee80148067 | -8.5916 | -67.1788 | 2026-09-03 03:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 1c7f1b92-c441-34a8-8331-62a5fd29d6a4 | -6.6356 | -59.4652 | 2026-09-03 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 9c188f3e-0015-3664-a020-beed184a0a49 | -6.6698 | -59.9443 | 2026-09-03 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| f24cce24-b145-3eee-a5b7-50b7bf01988f | -6.3236 | -56.0632 | 2026-09-03 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 4bb711af-998f-3091-be87-8768e890f908 | -6.7648 | -59.4408 | 2026-09-03 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 50adc86b-ebc3-3914-9a38-8e349a6defe9 | -6.6357 | -59.4459 | 2026-09-03 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.1 |
| bec7fb00-dc60-3e2d-b5c5-aa002906ae40 | -8.4677 | -54.6429 | 2026-09-03 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 7f1c78e9-9a34-38c1-95cc-1c6965136047 | -6.3237 | -56.0434 | 2026-09-03 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 9aca1241-f075-3116-a297-cd5d7a80d077 | -3.2485 | -47.2657 | 2026-09-03 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 1401a3e6-a461-3291-ad49-178a504bf3c6 | -7.2926 | -60.7243 | 2026-09-03 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 0752e271-5f70-384f-9bcc-6e447943d69d | -6.6358 | -59.4267 | 2026-09-03 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 48c4fd59-0ecf-3f81-9500-4a61f1bc2b4a | -6.3052 | -56.0442 | 2026-09-03 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 8701a34a-6a79-3c56-86e6-951fdaed31ce | -3.2486 | -47.2438 | 2026-09-03 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| b9c62041-0c63-3baa-8765-a5e65f90664e | -18.776 | -48.9226 | 2026-09-03 03:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 6ed85e04-87d2-35e5-9d33-2add0aaa1181 | -6.6541 | -59.4452 | 2026-09-03 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| e15bb9a1-4891-32cd-a751-9dca9189d653 | -18.7962 | -48.9186 | 2026-09-03 03:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 50.8 |
| e01ec65a-12a5-3b69-b881-41826c77dfa4 | -6.6883 | -59.9436 | 2026-09-03 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 68a38eaf-f528-3ced-bb34-a5e9c2f99995 | -10.8826 | -45.3075 | 2026-09-03 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| b538dd2e-6a18-319b-aa61-e2d51a114156 | -11.297 | -50.5153 | 2026-09-03 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 3381e124-0b6c-370c-be43-bc913cc29d41 | -6.654 | -59.4645 | 2026-09-03 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |


[Clique aqui para ver as próximas entradas](README16.md)
