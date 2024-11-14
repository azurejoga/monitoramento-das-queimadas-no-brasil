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
| f84f6e0f-30d2-36c5-9062-7885af0ade39 | -2.8002 | -51.8036 | 2024-11-14 01:28:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30ade6df-9257-33df-940b-162aaf96f5a5 | -17.5637 | -57.556099 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0021c2c-b8bf-3ec4-a5cc-801a6986bbaa | -17.501699 | -57.555901 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2d4f38d1-d2ec-33c7-95fd-abaa969315cc | -17.490299 | -57.551201 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a7dbbfeb-613e-35a0-8fbc-4851cd70ac8c | -1.7287 | -52.193199 | 2024-11-14 01:28:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d343c452-5bd2-33ac-832c-5c7f2cd9f3bc | -17.627199 | -57.5634 | 2024-11-14 01:28:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7b70314b-7ea2-34fc-b2fd-40856b0b9aa9 | -17.187099 | -57.488098 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3355937b-0f8d-39da-8e03-ecfd18fb545f | -1.7338 | -52.2145 | 2024-11-14 01:28:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0106e68c-a6e9-30b3-b607-ec52b83b56b7 | -1.5995 | -52.595001 | 2024-11-14 01:28:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72fbe5ab-10e5-33f2-b744-1ac10f72e3d8 | -21.7715 | -56.446499 | 2024-11-14 01:28:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 471aac84-985c-3f7c-91d2-8cad956c3e1d | -17.5425 | -57.5536 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fe60393e-e0c8-3a67-bc76-2ea8a7f58987 | -17.506599 | -57.577499 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 32d5f297-feda-3e2f-b5dc-339a462602c8 | -17.562099 | -57.548901 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 70f71d39-68fb-394e-9939-bdc6543f5af4 | -17.5343 | -57.563202 | 2024-11-14 01:28:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c1133ca1-b39d-3701-9b04-22cbcc1fec6a | -3.0356 | -45.1193 | 2024-11-14 01:50:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 449231f3-b4e2-3ddb-9ab3-c46dc340670c | -17.6263 | -57.5486 | 2024-11-14 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| a68c4855-81db-3425-bf05-31cc52f1b987 | -6.5216 | -35.194 | 2024-11-14 01:50:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 49.3 |
| e802ea22-e3c4-3d7b-9903-26502e515bb7 | -3.0543 | -45.096 | 2024-11-14 01:50:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 7c12c4bb-ba6c-31f9-b2bc-8f02735cc8eb | -17.6079 | -57.4688 | 2024-11-14 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.9 |
| e4ef3ac7-b58a-3490-9e55-9eb724e8318a | -1.829 | -52.1649 | 2024-11-14 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a84c5986-4873-39de-8085-81bbbbaa94e1 | -6.0472 | -44.0331 | 2024-11-14 01:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 3ba39003-b569-3776-a34c-70f9fa49b9d1 | -2.1953 | -46.3528 | 2024-11-14 01:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 0178a856-e813-336e-8886-836995fc3332 | -4.5614 | -48.0141 | 2024-11-14 01:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 664b7299-3f84-3b91-90d0-a9cbe4fd64ca | -1.3894 | -51.1197 | 2024-11-14 01:50:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 7b4b59a6-bc08-3a91-9462-685f8c50bb40 | -17.5872 | -57.5328 | 2024-11-14 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |
| 12ed1eff-92a1-3230-a402-5faf2f594693 | -1.8105 | -52.1857 | 2024-11-14 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 251.3 |
| a4020a55-7dd2-34ad-ad1b-a00fd6f538b7 | -3.0541 | -45.1186 | 2024-11-14 01:50:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 2ad2253d-b99a-3110-a7d4-6ec9f7202ee4 | -1.7922 | -52.1655 | 2024-11-14 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 346.1 |
| af54d1fa-8a56-3774-b1b7-efea7726831b | -3.7139 | -50.6255 | 2024-11-14 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| a6be2f33-58cd-356a-9cba-fbc874dfd884 | -3.0523 | -45.5237 | 2024-11-14 01:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 4a02f206-a5ee-3441-85a1-e50b0f3e7a93 | -3.0357 | -45.0967 | 2024-11-14 01:50:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 138.7 |
| a8d59b49-f56f-39e2-ac1e-33101da21047 | -1.8106 | -52.1652 | 2024-11-14 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 363.7 |
| 2b6d4cdf-2283-3f29-8ee4-dd5574da39b3 | -17.6076 | -57.4893 | 2024-11-14 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.8 |
| 17d4a999-4de5-30f4-98ae-9939cf584c40 | -6.5407 | -35.1917 | 2024-11-14 01:50:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 81.7 |
| e03ec4fe-8ea8-3254-a891-4b9dba2d5ea1 | -4.5429 | -48.0151 | 2024-11-14 01:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 10d0f3c7-e3e6-3261-8416-74b8fc1d1246 | -3.714 | -50.6046 | 2024-11-14 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 29fcdf11-47aa-39b6-a59e-1888eb4bed29 | -1.7921 | -52.186 | 2024-11-14 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 221.3 |
| de918c35-adeb-3b68-8c1d-11936c44ee78 | -17.5869 | -57.5533 | 2024-11-14 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 142.7 |
| c637b0fd-de75-3697-b831-b5fcc92b92e9 | -1.2228 | -51.783 | 2024-11-14 01:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 5a5f145b-18ba-3401-83dc-48a363f41818 | -2.8791 | -51.7932 | 2024-11-14 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| b2723e02-1005-3a2f-9886-e4e6c362b23d | -1.4078 | -51.1195 | 2024-11-14 01:50:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 664778fb-e088-3db4-8dde-688dd23b580d | -17.6066 | -57.551 | 2024-11-14 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 9a895c23-13d4-3908-8ff9-073f4da400da | -17.5675 | -57.5351 | 2024-11-14 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 8b6853c9-822a-3bc0-8240-a15586500025 | -2.675 | -47.0003 | 2024-11-14 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| c0fd4656-e8c0-3f44-9c99-b0f001e9a74d | -17.2543 | -57.4698 | 2024-11-14 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 0f327549-8d8a-34d8-8cda-4b8ea746c1fd | -2.2729 | -45.347 | 2024-11-14 02:00:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 3e796cde-45a5-3abd-8383-efeca0eb0a14 | -1.7922 | -52.1655 | 2024-11-14 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 228.9 |
| 4a4e883f-726a-36f3-a627-7cb8718e4aae | -17.5869 | -57.5533 | 2024-11-14 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 140.3 |
| c839cb68-0496-3ee6-822a-2f66d0311c31 | -1.3894 | -51.1197 | 2024-11-14 02:00:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| adddfdcb-fefc-3040-a161-ec8a6ce46c7a | -17.6263 | -57.5486 | 2024-11-14 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| a1198030-a50a-3e74-82fb-1c9d44b4a036 | -3.0523 | -45.5237 | 2024-11-14 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 35220723-6e67-33cd-87c0-10de649c3fbf | -17.6066 | -57.551 | 2024-11-14 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| c8e4954b-5254-371d-af26-c9591b9138ce | -2.8791 | -51.7932 | 2024-11-14 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| feb2b373-f925-3238-a611-a43cbb4c904b | -17.5872 | -57.5328 | 2024-11-14 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 1cb23aef-6234-3403-b70b-0fd540385f0f | -1.7921 | -52.186 | 2024-11-14 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 5c1da736-0059-3b80-a3e9-0ff42685d3d0 | -17.2543 | -57.4698 | 2024-11-14 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.0 |
| a0950006-92e1-3423-903d-0c58ace0c39f | -1.8105 | -52.1857 | 2024-11-14 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 249.8 |
| 56fe74bd-fa69-36bc-a717-e3e3724bede7 | -17.5675 | -57.5351 | 2024-11-14 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| c7e9bb65-b490-3f8a-a63d-9e0141ca2272 | -1.8106 | -52.1652 | 2024-11-14 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 448.0 |
| 9df5e86b-7a80-30e2-aa22-ffb0408ddb2b | -4.0003 | -45.5728 | 2024-11-14 02:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 3d4a9b00-01d8-389d-8607-e80743861441 | -3.714 | -50.6046 | 2024-11-14 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 808c22c7-83b1-336b-899c-7b75a6e7b05e | -2.1953 | -46.3528 | 2024-11-14 02:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 0593af67-03a0-338c-ab2b-918d39bc0501 | -3.0356 | -45.1193 | 2024-11-14 02:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 7b1e799c-482f-381a-bfd0-de199263625f | -3.0357 | -45.0967 | 2024-11-14 02:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 133.7 |
| e3c16eb1-c3cd-3ce3-89e4-51675b0b4851 | -6.0472 | -44.0331 | 2024-11-14 02:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| ac758ba0-60ab-39b1-bb30-40a3a9170c5d | -1.4078 | -51.1195 | 2024-11-14 02:00:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 9e2a9fc6-1271-3112-bfb9-f6d4c99e45e1 | -1.81 | -52.17 | 2024-11-14 02:00:00 | MSG-03 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5da6329-00cd-3bd6-ae4d-5ef6c772c679 | -1.78 | -52.17 | 2024-11-14 02:00:00 | MSG-03 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc7630f0-715f-3c2c-ab5e-d40b9690dd88 | -2.2729 | -45.347 | 2024-11-14 02:10:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 811181c8-4522-3d9f-bfe5-22ecb5850604 | -17.6079 | -57.4688 | 2024-11-14 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.8 |
| 4dc179f7-2755-340e-be88-06ce1a61a7fe | -2.8791 | -51.7932 | 2024-11-14 02:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 4509e180-437c-3275-8f75-c48c2f1c60d6 | -17.5675 | -57.5351 | 2024-11-14 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 0db045e9-0168-34e5-9662-312730ecd173 | -3.6402 | -50.5863 | 2024-11-14 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| ede051de-d326-3dc9-977a-5b2f959cca5e | -1.4078 | -51.1195 | 2024-11-14 02:10:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| dcdf7a8a-30eb-380c-880f-63f8e25d8560 | -4.3754 | -48.0882 | 2024-11-14 02:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| e74ed699-63a1-3397-9793-f69afbaabf39 | -3.0523 | -45.5237 | 2024-11-14 02:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| df46ade8-a90b-3b11-be46-5fe6db0bd5a6 | -4.0003 | -45.5728 | 2024-11-14 02:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 6a24fdb1-9f5b-3efc-ac2b-cc997b903596 | -1.8106 | -52.1447 | 2024-11-14 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 07aae21e-f174-3ad4-8b05-a2ba878c4051 | -1.7921 | -52.186 | 2024-11-14 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 508311de-60e0-3ebc-a12b-56d5bc37629f | -1.8106 | -52.1652 | 2024-11-14 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 379.7 |
| 0b2c2f43-1080-34c6-938b-63995e4f80de | -17.6263 | -57.5486 | 2024-11-14 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.9 |
| 2b433824-796a-3848-abe0-8777b1889c3b | -3.7325 | -50.604 | 2024-11-14 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| ff024c9e-730e-35fd-ac3b-7670417e51ec | -17.6066 | -57.551 | 2024-11-14 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| f15efecf-e9a3-3449-804c-1c8882a65613 | -17.2543 | -57.4698 | 2024-11-14 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| aa84a186-ae85-3204-837c-15f2afb20767 | 1.048 | -60.5986 | 2024-11-14 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.3 |
| e1469ec3-6208-3378-ad81-58fff88b24e5 | -17.6076 | -57.4893 | 2024-11-14 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| 084b2313-2e43-3ef0-9b21-9979f9ca24f4 | -6.0472 | -44.0331 | 2024-11-14 02:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| d38b7b60-6d4e-3efd-b440-082b1b989fd0 | -3.714 | -50.6046 | 2024-11-14 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| c05c270c-6a26-3d6e-8e95-167165f8ecbf | 1.0663 | -60.5985 | 2024-11-14 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 67ca6f38-e366-3beb-8fef-7df8627529a7 | -17.5869 | -57.5533 | 2024-11-14 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.8 |
| 3807ebb5-d1c7-32b0-a3d4-7bf4110ea4ac | -1.3894 | -51.1197 | 2024-11-14 02:10:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| afcf18a5-f163-3f57-98f3-8c474fe6a2d2 | -17.5872 | -57.5328 | 2024-11-14 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 2189bd42-f599-36ab-b680-c82e02ca9dbf | -1.7922 | -52.1655 | 2024-11-14 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 175.1 |
| e2e5e9e3-a6a8-3ac4-b528-7d3bf73ee0ad | -1.8105 | -52.1857 | 2024-11-14 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 274.3 |
| ce1aae61-7ed5-328e-b702-1566c50601d1 | -15.23018 | -60.23352 | 2024-11-14 02:17:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| f481660d-78cb-3cc3-87e5-d6bbf0f9b04d | -17.57161 | -57.54333 | 2024-11-14 02:17:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| b4407e51-340f-310c-98a1-622a7261e15c | -17.60382 | -57.49428 | 2024-11-14 02:17:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.9 |
| e8ba11c8-becb-3f8e-a2e0-80b1d28239fb | -17.59028 | -57.46539 | 2024-11-14 02:17:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.1 |
| 82788045-9ccf-3951-9995-cd75d254a1c9 | -17.59701 | -57.50091 | 2024-11-14 02:17:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.2 |
| aea7c5d8-f9b5-340c-b4be-a71f0246c64a | -17.5672 | -57.5557 | 2024-11-14 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |


[Clique aqui para ver as próximas entradas](README16.md)
