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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23bd7be9-a218-3b72-a6e7-cb29c26cddee | -13.9902 | -56.8058 | 2025-05-13 02:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 2ff703eb-5e90-3d01-9783-b898a5ed5b94 | -12.1544 | -48.019 | 2025-05-13 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| b43ec98b-4935-3934-8ef6-3b60e6a43ffb | -8.07 | -43.1216 | 2025-05-13 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 9a0ecb04-b851-3242-9a89-04121bde367f | -8.0889 | -43.1196 | 2025-05-13 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 0080f015-953d-3df5-8bb9-6e394fa527a9 | -13.9902 | -56.8058 | 2025-05-13 02:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| e4c3fa5a-fbd7-36c3-b5ee-cc48a62fe5e3 | -8.07 | -43.1216 | 2025-05-13 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.2 |
| 29b4d00e-2981-3458-9b6c-245765a4588f | -13.5683 | -52.8783 | 2025-05-13 02:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| d7ecd4c5-ac47-3e25-a298-aad593b501b2 | -8.0889 | -43.1196 | 2025-05-13 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 09a13034-fd1a-32e9-91a1-0da18c93d106 | -13.971 | -56.8077 | 2025-05-13 02:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| edc9fba6-3245-3409-b1ef-8fcf6e14566b | -13.9905 | -56.7855 | 2025-05-13 02:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 026877bc-5cd7-351d-978f-3756ac27c37f | -12.1544 | -48.019 | 2025-05-13 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 0415df7f-ed37-3cd2-b955-1446ce781123 | -8.07 | -43.1216 | 2025-05-13 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 1e986024-7c5f-369e-8b6b-4c1f19660b6b | -12.1544 | -48.019 | 2025-05-13 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| d589186d-e487-37d3-9f73-f7111111d786 | -8.0889 | -43.1196 | 2025-05-13 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 3286ea87-8d70-35ec-8505-ba0fcbc2f391 | -13.5686 | -52.8573 | 2025-05-13 02:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 05d177a5-6336-3c3b-9e0c-9b0db2520bff | -13.5683 | -52.8783 | 2025-05-13 02:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| d1643510-e0c3-3ccf-ade1-3a486bf73e76 | -12.1548 | -47.9968 | 2025-05-13 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 46b7a44b-7916-303e-9861-c0263e6f32eb | -13.9905 | -56.7855 | 2025-05-13 02:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 0622b7fd-b70d-359c-a73a-232cd78b0731 | -13.9902 | -56.8058 | 2025-05-13 02:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 7498ff6f-1a5c-355f-9047-a6a928c228c6 | -13.5683 | -52.8783 | 2025-05-13 02:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 42cd44d8-81c7-39ea-9edc-6bd9bb42e698 | -13.971 | -56.8077 | 2025-05-13 02:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| fea777a9-0560-37f5-b964-feab61ebc9f6 | -12.1544 | -48.019 | 2025-05-13 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 83c5105c-6e25-3ac0-8bf3-f31404d43702 | -13.9902 | -56.8058 | 2025-05-13 02:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 9017512f-b913-35c6-90e5-15c158d1e19b | -8.07 | -43.1216 | 2025-05-13 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 48ea155b-8efb-3400-9416-da4d222bb54e | -13.5686 | -52.8573 | 2025-05-13 02:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| cca7c796-767b-3e29-9e95-e420478fca74 | -8.0889 | -43.1196 | 2025-05-13 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 9871e431-f064-371d-95e5-e4f63303710b | -8.07 | -43.1216 | 2025-05-13 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 122.0 |
| ec336a32-7a44-3f6a-9fd2-6abef369568e | -13.9902 | -56.8058 | 2025-05-13 02:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 5784de02-5d0d-3784-9668-cd8be87131e2 | -13.5683 | -52.8783 | 2025-05-13 02:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| c1d70130-2041-3502-a97f-d9c9d5c37fcd | -13.971 | -56.8077 | 2025-05-13 02:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 45209a7b-cf1b-3937-b55d-efb7658eee19 | -8.0889 | -43.1196 | 2025-05-13 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 516d3a55-51e8-32fa-87c3-0a17725dea87 | -9.4773 | -40.3116 | 2025-05-13 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 6622f8ef-c7e4-3bf9-9801-925003727cf8 | -8.0696 | -43.1452 | 2025-05-13 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| a1ab2651-2816-3834-bd47-f3949ee1b542 | -8.0889 | -43.1196 | 2025-05-13 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| a4152065-666d-3e57-95a8-1f18db805986 | -8.07 | -43.1216 | 2025-05-13 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 132.5 |
| a7088e79-8ad4-3fbe-a18e-5efb24689db3 | -13.971 | -56.8077 | 2025-05-13 02:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 87a93e30-bc18-38bf-92e5-5d86dd643fcb | -13.9902 | -56.8058 | 2025-05-13 02:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 63eddf52-cf81-3a5d-9251-ea188274900e | -13.5683 | -52.8783 | 2025-05-13 02:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 253b7b34-adb2-311f-bcab-5340fa34be72 | -9.4582 | -40.3143 | 2025-05-13 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 7112c802-ae13-3cd3-a314-0dafa536fbd6 | -13.971 | -56.8077 | 2025-05-13 03:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 249048be-7430-30e4-8168-0e0499f73a18 | -8.0889 | -43.1196 | 2025-05-13 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| 1a748f6a-c60d-3d9c-8d52-6edaa467949a | -8.07 | -43.1216 | 2025-05-13 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 131.7 |
| 55d8c23a-9368-3a30-8d1a-857713fe9f14 | -9.4773 | -40.3116 | 2025-05-13 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 156.0 |
| 12d90ed3-477e-31e2-83d0-87f7db5584e1 | -13.9905 | -56.7855 | 2025-05-13 03:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| c83cebac-3005-3b7b-9677-e362ed6508ee | -13.9902 | -56.8058 | 2025-05-13 03:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 5e712fa2-a8e0-3788-8f3f-cf9e2978e19d | -13.9902 | -56.8058 | 2025-05-13 03:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| b8fcb606-017f-3c2a-bce6-c84dd52e8bf0 | -8.07 | -43.1216 | 2025-05-13 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 127.4 |
| 74d299b5-2f97-3742-9397-cbe33dc93dbd | -13.9905 | -56.7855 | 2025-05-13 03:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 4a0e4cd0-1918-3e73-a862-31e80595a013 | -8.0889 | -43.1196 | 2025-05-13 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 7bc22ee2-e3c6-3866-8284-864fe99a1f00 | -13.5683 | -52.8783 | 2025-05-13 03:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 83eaf3a6-48b0-324f-b842-0a3ffb990fe9 | -8.0886 | -43.1431 | 2025-05-13 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.6 |
| 2c1f786c-a45f-3fb5-871b-e670c95550d0 | -8.0889 | -43.1196 | 2025-05-13 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.1 |
| f9111626-1615-3412-8674-0ca4683b7dfb | -8.07 | -43.1216 | 2025-05-13 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| 20383853-5bc5-3f7f-8576-7ae64d400bba | -13.9902 | -56.8058 | 2025-05-13 03:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| a9bffe35-a633-32eb-9c09-d6708ac0eaba | -8.0696 | -43.1452 | 2025-05-13 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| 4b25943d-5eb8-334f-9115-b79dbcc27d93 | -13.5683 | -52.8783 | 2025-05-13 03:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4d1369fd-af17-3eb8-a5fe-eb6a3e0117a1 | -7.10928 | -36.49183 | 2025-05-13 03:21:00 | NOAA-21 | JUAZEIRINHO | PARAÍBA | Brasil | 2507705 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4c788b73-faed-349a-924d-fef392942a37 | -6.65318 | -41.99422 | 2025-05-13 03:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5a45d423-9931-382b-a893-859c9184bbf3 | -7.17921 | -35.93294 | 2025-05-13 03:21:00 | NOAA-21 | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6f924c23-6690-3084-8e16-6600d9d682db | -7.47748 | -34.84209 | 2025-05-13 03:21:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 730e2ab2-e05a-30a1-b9d8-e33e485a4a4e | -3.77334 | -41.65971 | 2025-05-13 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aaa5deaa-819a-3722-97e8-74608dbc46f9 | -3.77968 | -41.66075 | 2025-05-13 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 65f93d52-008a-3f71-85ba-b14f46335619 | -6.64613 | -41.99786 | 2025-05-13 03:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 38f00123-8200-37b5-813e-c93cb9631987 | -7.31573 | -35.29847 | 2025-05-13 03:21:00 | NOAA-21 | PILAR | PARAÍBA | Brasil | 2511509 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| fa3956b8-96b3-30f3-a449-be9240d12126 | -6.64729 | -41.99809 | 2025-05-13 03:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 78e74cda-288e-3c98-bb9d-125340d747fb | -6.65431 | -41.9945 | 2025-05-13 03:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dc26a052-6fa7-3d16-bbea-754707c20bd6 | -11.79064 | -44.27626 | 2025-05-13 03:23:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35338dbf-7f04-3431-af12-23681830bab8 | -11.80328 | -44.27771 | 2025-05-13 03:23:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 50774285-feae-304d-a7e6-a13e0fadabf3 | -8.07013 | -43.13282 | 2025-05-13 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.6 |
| f0fda7fe-c1a5-3b1f-a348-b48ff5ae0b74 | -8.07117 | -43.12721 | 2025-05-13 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 44.1 |
| 0ad89e4a-01a9-3ce3-90d9-dae2ec0daef8 | -8.07723 | -43.13243 | 2025-05-13 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 9a8da593-4f80-31ad-9abd-1c3061ed9939 | -8.49305 | -36.58946 | 2025-05-13 03:23:00 | NOAA-21 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 94b5aba0-6af5-3d10-96ff-cd72497151ec | -9.58153 | -36.85943 | 2025-05-13 03:23:00 | NOAA-21 | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 661ffaa3-8f08-3779-b97b-133433df63e5 | -9.47234 | -40.31461 | 2025-05-13 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 61944838-6dcc-3498-95e2-ad11d1c376f6 | -8.07183 | -43.12567 | 2025-05-13 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 0ba11994-0403-3b5b-98d2-587dc3b35e34 | -9.21764 | -36.87675 | 2025-05-13 03:23:00 | NOAA-21 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8ced1ef6-c585-32e1-9cf5-4ae0d2108d1e | -8.07076 | -43.13121 | 2025-05-13 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.7 |
| d1e9a25b-3825-3543-975d-79932b55a338 | -9.47295 | -40.31131 | 2025-05-13 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a9f5aa83-8ea4-3e79-82f0-729f909b262a | -11.79715 | -44.27752 | 2025-05-13 03:23:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7dd0d84-dcbe-323b-bb5f-17b0fb8ff957 | -9.21833 | -36.8728 | 2025-05-13 03:23:00 | NOAA-21 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b8c4d65c-8343-32a2-85a9-f6536dc5ec10 | -11.80365 | -44.27888 | 2025-05-13 03:23:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5db44ede-15bb-3f00-8805-d6e53946138f | -8.07829 | -43.1269 | 2025-05-13 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 9e73143e-5172-3d4e-b005-1906af6ff20c | -14.17966 | -45.47176 | 2025-05-13 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84ace50b-fc6b-384f-9628-8623457ae6e6 | -14.66012 | -45.12481 | 2025-05-13 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14ed372b-6e1e-329d-a80c-ce82f56094a5 | -14.19296 | -45.47485 | 2025-05-13 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f234ede6-21ee-3d40-bd0a-f881b4965bbe | -14.185 | -45.47932 | 2025-05-13 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 344b789a-017d-3086-97b7-ba37529c545e | -14.6599 | -45.12889 | 2025-05-13 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf0a091d-9eb1-3cbf-874a-af6f9a80e41b | -14.18631 | -45.4733 | 2025-05-13 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee0df0e6-bac1-3afe-827c-a7772888c6d4 | -14.18097 | -45.46575 | 2025-05-13 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 289460f5-dd8a-3dda-85cd-33ffaf1fd4ac | -14.19165 | -45.48085 | 2025-05-13 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2028ad88-fdb5-3672-9ef4-30e99412646c | -19.15944 | -47.81823 | 2025-05-13 03:25:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d165844-a71b-3039-8f30-a7efbbe67c7b | -14.6611 | -45.12323 | 2025-05-13 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61cb2e23-d037-3218-878e-9745ba3294f1 | -14.66659 | -45.12629 | 2025-05-13 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9336b20-5b34-389e-9297-edcf906fa822 | -14.18761 | -45.4673 | 2025-05-13 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a7a3de3-6e9f-32c8-99ae-62aec89245cc | -20.18369 | -46.54754 | 2025-05-13 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08885f47-5f79-3008-9470-e26badb6e301 | -20.22082 | -46.74141 | 2025-05-13 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8c33e59-5c09-38a3-8316-8a479eb09f64 | -20.22042 | -46.74034 | 2025-05-13 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e13e2f4a-9d93-370e-bbb9-17bd1b63afd2 | -20.22211 | -46.73605 | 2025-05-13 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9481094-9bef-35f7-b9d5-e23285467d69 | -20.21009 | -46.75547 | 2025-05-13 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffdf5c45-2cf7-3d0c-b3a5-b53e9883fa10 | -20.18394 | -46.55299 | 2025-05-13 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README4.md)
