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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 115f2cc9-9411-3123-876b-9b4f9fec3d25 | -16.69799 | -51.57768 | 2024-11-01 04:34:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e828a04-2059-3af7-9d94-5cd20d540ea3 | -16.57455 | -52.41013 | 2024-11-01 04:34:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a251e45-56eb-36b2-9c42-9890b986193f | -16.3147 | -53.28876 | 2024-11-01 04:34:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17204c60-f5fe-311a-9dda-e6617ac2e104 | -17.44135 | -52.4166 | 2024-11-01 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c876ce3-c66f-39ea-bd23-29c80589b92c | -17.23957 | -52.17299 | 2024-11-01 04:34:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfa3510f-71ab-322f-bce8-8c7ed8c6c109 | -17.57839 | -53.42062 | 2024-11-01 04:34:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a97a973-1244-3e3c-bb2f-beb8a55cfeec | -17.16905 | -53.4529 | 2024-11-01 04:34:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5e613ac-d4b6-3db1-af11-3d00b864c710 | -20.47576 | -53.67606 | 2024-11-01 04:34:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c0fe276-9b89-33e5-9f92-98a36e42b8b6 | -18.02494 | -54.68399 | 2024-11-01 04:34:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e3fb5e1-7bde-3601-a4ab-0f8b6b9dc47f | -18.02487 | -54.68668 | 2024-11-01 04:34:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1f37c8a-9c73-3a39-8ee8-64aa91f5c494 | -18.02411 | -54.68873 | 2024-11-01 04:34:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7441590-490e-3fb6-bbd2-a07a3da28d87 | -17.8372 | -54.31495 | 2024-11-01 04:34:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db6d2d3e-d1b3-329c-9461-f921804de2e0 | -17.59941 | -53.73997 | 2024-11-01 04:34:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0b18b94-d5d1-3807-8168-bafc1beab42e | -17.59582 | -53.73925 | 2024-11-01 04:34:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8eb5aa03-2d35-3a59-be24-0e31c36c18f0 | -17.59508 | -53.74351 | 2024-11-01 04:34:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e2fd50d9-838a-39b3-8218-eddeeb07d2fc | -17.59434 | -53.74778 | 2024-11-01 04:34:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 524cbf61-572f-3531-8e19-ffb096695961 | -18.60363 | -55.47231 | 2024-11-01 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2557e4f8-a991-3472-b9d3-771d9dd68fd4 | -15.03862 | -55.71597 | 2024-11-01 04:34:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddabaec2-dcc9-3a44-97d0-d52acfb2f8bd | -15.18459 | -55.8212 | 2024-11-01 04:34:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e378ac7-b568-3bd7-9ecd-8460c24c38f9 | -16.56416 | -56.25156 | 2024-11-01 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 91c15d4d-eb73-3cfb-90eb-ba36960e50d9 | -16.56339 | -56.25562 | 2024-11-01 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 039986ef-1f7f-370c-a693-d48172ded78b | -19.47979 | -56.72234 | 2024-11-01 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a3f8ee77-eb6f-3cc2-8cb7-c1f5a9d8c34d | -16.48633 | -52.56178 | 2024-11-01 04:34:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fbe6a0e-765f-3a35-8a55-128a4892086c | -16.57521 | -52.40625 | 2024-11-01 04:34:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1629451d-45e5-3e3c-83e1-766161b19d73 | -16.92965 | -57.6579 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b6f8336b-b446-3383-a529-dad477495331 | -16.92835 | -57.65954 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b8e76db7-f601-3e6e-a3ce-68e36febbdc8 | -16.92507 | -57.65691 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e344a827-dcc5-3586-9b3a-98dd30d57576 | -16.92413 | -57.66186 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5c71bae4-71a1-3072-a882-ba820964fc99 | -16.92377 | -57.65856 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0f596e38-c825-3829-99c1-092035e7186f | -16.92048 | -57.65593 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9ce9606f-bdec-357b-911c-e2d4cfd48bca | -16.91954 | -57.66087 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8673ca5e-4f3f-32a4-a59d-e8b8c2a411e0 | -16.91919 | -57.65759 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 54a539af-69a8-3a93-959f-9356bc62d736 | -16.91191 | -57.5268 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 69e33a61-3c59-37fe-8511-31f4debc3048 | -16.91098 | -57.53164 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| e618138e-697f-3a56-9d40-7c5e2e76f445 | -16.90923 | -57.51614 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e5016882-9fa9-3144-8dcc-a246873e0023 | -16.9083 | -57.52098 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| e8add6da-53c6-3ec2-8283-69af7562d2df | -16.90737 | -57.52583 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 3726143b-4f51-300d-893d-eb30b9e348f7 | -16.90376 | -57.52002 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| defdc8d1-5721-37bc-86f2-621062a5e07d | -16.90282 | -57.52486 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2d1fb7c2-2427-3cc9-85dd-250b74b61c5c | -16.90014 | -57.51421 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b830de14-315d-3920-bda3-b41833d12f80 | -16.89921 | -57.51904 | 2024-11-01 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1e1d8c60-3e6a-32c3-8e19-467c22c0f184 | -16.8325 | -56.70343 | 2024-11-01 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1f6057ee-14d9-3040-96da-33ff70229a22 | -16.82818 | -56.70253 | 2024-11-01 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3dcdc2c6-75f1-3900-a5c6-303ca08489fe | -16.8255 | -56.69303 | 2024-11-01 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 56209db4-4644-335d-82fd-4ba799797ada | -16.822 | -56.68783 | 2024-11-01 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7530965d-9739-3016-a41f-2504eb4988c5 | -16.82118 | -56.69214 | 2024-11-01 04:34:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1f021142-c8ae-3c1b-b421-60597cc6788f | -3.0353 | -49.4901 | 2024-11-01 04:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| ee1e63ef-d09a-3d84-ba4b-76f3cc0ee236 | -3.0354 | -49.4688 | 2024-11-01 04:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 85ddfb95-434b-3205-9142-0ad8fc89e0d8 | -3.0538 | -49.4895 | 2024-11-01 04:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 802ea1fa-f083-3751-95b7-25c2a8ff339f | -3.0539 | -49.4683 | 2024-11-01 04:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| c1c20049-c180-33c0-a87e-79fdaec60bdb | -3.5631 | -47.3847 | 2024-11-01 04:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 78322e89-7063-36d0-a631-1ab8256da515 | -4.3867 | -43.4757 | 2024-11-01 04:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 758ec494-fd9f-3f34-b4c7-5ed64e40217c | -4.4054 | -43.4746 | 2024-11-01 04:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 0c52ef89-dea2-3f6a-aa4b-65e3d4836d19 | -6.1041 | -43.9593 | 2024-11-01 04:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 32993794-40dd-363f-9a1d-5fd320997afd | -6.1229 | -43.9578 | 2024-11-01 04:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| eefb196a-7f82-389b-8c94-67715e8fb862 | -22.89886 | -43.75127 | 2024-11-01 04:36:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 31040b2d-4c13-3fec-b8c1-a4ac6e155ae5 | -23.72241 | -47.42445 | 2024-11-01 04:36:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| df65f32a-43a8-3806-94a6-e95f2781c324 | -23.59334 | -47.43909 | 2024-11-01 04:36:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| af39b139-70d6-3130-ba15-a465fd4129ec | -23.35723 | -47.93309 | 2024-11-01 04:36:00 | NOAA-20 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fef13c5e-0751-343b-8b39-610be5bf6d2a | -22.5059 | -47.70256 | 2024-11-01 04:36:00 | NOAA-20 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b64e181b-e4bf-365b-9210-d9ef257a68e4 | -22.50528 | -47.70734 | 2024-11-01 04:36:00 | NOAA-20 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 851e4ceb-bbd9-3303-8106-a592bd28e7e7 | -27.11077 | -51.06813 | 2024-11-01 04:36:00 | NOAA-20 | VIDEIRA | SANTA CATARINA | Brasil | 4219309 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 796b05f0-2568-3246-8958-3b48c5750cef | -27.13796 | -51.90384 | 2024-11-01 04:36:00 | NOAA-20 | CONCÓRDIA | SANTA CATARINA | Brasil | 4204301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 43093735-785c-3a02-b06c-56e7372369c6 | -22.05599 | -52.78434 | 2024-11-01 04:36:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 782dc0f0-0d7d-339c-be01-21367167298d | -22.05536 | -52.78813 | 2024-11-01 04:36:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 295d9b4b-9b06-37ed-9624-028ae087d47f | -22.05404 | -52.7843 | 2024-11-01 04:36:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 693f4edd-71d9-39e5-86fb-f8f0e694b9d5 | -22.05342 | -52.7881 | 2024-11-01 04:36:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e020cc36-198c-3e79-8328-04eced9467b2 | -21.56132 | -54.2087 | 2024-11-01 04:36:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7e69cb7-2504-339c-8079-89f40c8e692e | -21.55781 | -54.20801 | 2024-11-01 04:36:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c363fd1c-9747-39fd-84f1-b7b469e43053 | -9.9001 | -64.8065 | 2024-11-01 04:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 5591a394-64a5-3a0b-ac6c-71b215d035f8 | -9.9186 | -64.8246 | 2024-11-01 04:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 3dec5502-766e-36ea-bb38-494aa63c07a2 | -9.9187 | -64.8058 | 2024-11-01 04:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 1373923b-be0e-31e1-bb2c-a13b660a42a5 | -28.58518 | -49.44152 | 2024-11-01 04:38:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a0a35e58-097d-3518-a972-1785f53aa051 | -29.1852 | -51.77811 | 2024-11-01 04:38:00 | NOAA-20 | ROCA SALES | RIO GRANDE DO SUL | Brasil | 4315800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1f83027d-5d4d-36e4-b909-8a830a1943c0 | -29.81433 | -51.17606 | 2024-11-01 04:38:00 | NOAA-20 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| f6f26cdd-518c-398f-8663-514195eaa7ba | -29.87638 | -50.90454 | 2024-11-01 04:38:00 | NOAA-20 | GRAVATAÍ | RIO GRANDE DO SUL | Brasil | 4309209 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f13df692-4f8e-3e54-9eaa-0a9f61fab134 | -29.47639 | -51.96347 | 2024-11-01 04:38:00 | NOAA-20 | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 081738e9-2254-3600-898b-9a2717fc1e64 | -29.4758 | -51.96758 | 2024-11-01 04:38:00 | NOAA-20 | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f6fc6d87-b227-3b5f-9984-114926b4f8e8 | -3.0354 | -49.4688 | 2024-11-01 04:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 56d79d98-83a8-371d-a32e-2d5ba1cd6623 | -3.0538 | -49.4895 | 2024-11-01 04:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 938212e1-8d68-31ba-b38f-022a53310f63 | -3.0539 | -49.4683 | 2024-11-01 04:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 0429370e-18a2-3339-9654-6bcc40b3a027 | -3.5631 | -47.3847 | 2024-11-01 04:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 6976d8f4-62bf-317b-a36d-7147b6372a30 | -4.3867 | -43.4757 | 2024-11-01 04:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 0f7e7cf1-9ead-39dc-8938-df0f73a30547 | -4.4054 | -43.4746 | 2024-11-01 04:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| f400dd62-9be4-3c25-8b1b-3a81fb63bc35 | -6.1041 | -43.9593 | 2024-11-01 04:45:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 20d099e9-1636-3dde-b5d5-25da46197b9b | -9.9001 | -64.8065 | 2024-11-01 04:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 0b9e42f1-e6f6-3061-87ba-452e1f45d688 | -9.9186 | -64.8246 | 2024-11-01 04:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 97b7f1c6-4846-3795-8ae8-c05f045b402f | -9.9187 | -64.8058 | 2024-11-01 04:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 2decfba6-589d-38e5-be45-97adfd77c573 | -19.4882 | -56.6017 | 2024-11-01 04:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.1 |
| 2371ec9d-acf7-39c3-8474-e90b9557dfbf | -19.5059 | -56.7249 | 2024-11-01 04:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.5 |
| d4e4b446-9b86-3690-a4d0-1295d9a9ed48 | -19.5063 | -56.7039 | 2024-11-01 04:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.4 |
| af0f369c-cecd-342f-b62c-a2e8c2d688c6 | -19.5079 | -56.6199 | 2024-11-01 04:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.6 |
| d3c3c35b-eba8-3d8b-9b81-2533c77c4236 | -19.5083 | -56.5989 | 2024-11-01 04:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.8 |
| d1350ea6-a2b4-3280-a04e-855dc8a24764 | -19.526 | -56.7221 | 2024-11-01 04:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.9 |
| 087517b7-9804-3aae-a09e-9e561b0b1daa | -19.5264 | -56.7011 | 2024-11-01 04:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 03590301-3327-3d54-be30-ba1459669104 | -19.5461 | -56.7192 | 2024-11-01 04:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.1 |
| ea6356e2-c60c-3bfb-9e1e-2a138978a6e5 | -3.0353 | -49.4901 | 2024-11-01 04:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| b26af8b0-ad57-3b56-89d9-2c83598a7d8e | -3.0354 | -49.4688 | 2024-11-01 04:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 5075c868-91a7-3c40-b976-28783cfabd99 | -3.0538 | -49.4895 | 2024-11-01 04:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 42cea994-e037-3d5b-a588-e6f31ccdd7f5 | -3.0539 | -49.4683 | 2024-11-01 04:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |


[Clique aqui para ver as próximas entradas](README43.md)
