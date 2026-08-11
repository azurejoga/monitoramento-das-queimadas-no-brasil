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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 549bac50-8cf1-3c7c-9010-55c2b39ccf44 | -10.1084 | -46.2018 | 2026-08-11 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 9066cfca-add1-3f1a-9f9e-c3cb0c41a83e | -14.6657 | -47.6442 | 2026-08-11 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| e7a61bcd-91c7-3b25-994c-0df8af1528b7 | -8.9602 | -60.4973 | 2026-08-11 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| bcf3779e-69fd-36e7-9e18-7f1ae119a1c7 | -9.3717 | -47.4897 | 2026-08-11 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 3ea32655-992b-36bf-9f2e-3da5482486b3 | -9.35 | -48.02 | 2026-08-11 13:15:00 | MSG-03 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b00ad740-7554-36cb-a51c-2c780c476b66 | -9.38 | -48.08 | 2026-08-11 13:15:00 | MSG-03 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3032b8c6-6c29-362e-a16b-e9334da434ad | -9.38 | -48.03 | 2026-08-11 13:15:00 | MSG-03 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34eb3bf9-1255-328e-a5cc-fbb28765b0ee | -13.8611 | -53.7845 | 2026-08-11 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| d1666560-d5f2-3f11-b1a8-5a83b90d19f6 | -13.5498 | -46.3074 | 2026-08-11 13:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 215.8 |
| 92dcc5ea-9079-3af0-87bb-939d3a65dd98 | -9.3909 | -47.4656 | 2026-08-11 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| f5941016-2c2f-301e-8c6a-be498c6d8163 | -14.2877 | -45.2835 | 2026-08-11 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 4b9db2fc-9a33-33b1-9212-2bd1ce89cfe2 | -9.3717 | -47.4897 | 2026-08-11 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 218.1 |
| c302af66-c3bf-3fce-ac7d-2c1de0205087 | -13.8211 | -53.8931 | 2026-08-11 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 16f9a3de-61a2-34ea-b90f-97dfb5d98203 | -13.8608 | -53.8053 | 2026-08-11 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 3066355f-5ba2-31f7-be6a-d013644e7859 | -9.3906 | -47.4878 | 2026-08-11 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 7964cf45-04e3-30a3-b173-88c2d254ba32 | -14.2559 | -51.9686 | 2026-08-11 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 137.4 |
| a993c58b-45b6-3083-8fb9-0cdbaa795b5e | -10.2268 | -45.8935 | 2026-08-11 13:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 975261c6-9bd6-3523-9509-e13a62021ab7 | -11.0294 | -45.6536 | 2026-08-11 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 007e5cb9-28bf-36f3-b1d1-8f72b2640a65 | -10.4237 | -46.6809 | 2026-08-11 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 46c934f2-b99d-3ad3-a942-03d42c881f72 | -10.2271 | -45.8708 | 2026-08-11 13:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 357.7 |
| 8a0842c8-b92e-3648-9b09-c9ccbcc5b6f1 | -8.9602 | -60.4973 | 2026-08-11 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| d8e2f5a5-478a-3a92-a161-3ec49aff5b3d | -8.96 | -60.5358 | 2026-08-11 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 1ceffaa5-1ea6-3efe-8f33-d71c12285c2b | -13.5498 | -46.3074 | 2026-08-11 13:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 335.0 |
| 1c0e81f6-4c93-3e29-85ae-1223061ceadc | -13.8403 | -53.8909 | 2026-08-11 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| de2d2352-461a-36ab-aa16-5a1aa81aa01b | -13.8608 | -53.8053 | 2026-08-11 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 126.7 |
| d2a90be6-319c-35dc-be4c-1eb02f723d13 | -9.3909 | -47.4656 | 2026-08-11 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 170.8 |
| ff402e0d-3ab4-3aef-bc5a-9b5a56a60b2d | -10.4237 | -46.6809 | 2026-08-11 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 49659beb-74c4-366c-bd66-6c3e6f5e6fe2 | -10.2271 | -45.8708 | 2026-08-11 13:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 277.2 |
| 6fba7ea4-9b1b-3a85-9509-25e24c3e548c | -9.3714 | -47.5119 | 2026-08-11 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| d734be2d-5f6c-3084-8391-9525868c348f | -10.2268 | -45.8935 | 2026-08-11 13:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| ecdf8a83-743b-3627-8c1b-2e1a73adda1e | -10.2275 | -45.8481 | 2026-08-11 13:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 9b9c29e6-ca6e-3f73-8e6d-fc9f1a4b10b4 | -14.2877 | -45.2835 | 2026-08-11 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| e6ba94b6-441a-302c-baa5-b4f6ed26d652 | -14.2559 | -51.9686 | 2026-08-11 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 419.9 |
| a7437fd9-c33e-3c81-b8db-0f816a69ce75 | -9.3717 | -47.4897 | 2026-08-11 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 345.6 |
| 9f5f9e2e-0ec8-37ef-a242-c299f5e5db0c | -13.8211 | -53.8931 | 2026-08-11 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 4ac9b423-3b88-3b6b-b077-5c38742e1f33 | -13.84 | -53.9117 | 2026-08-11 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 5c48036e-6ffd-33bd-8787-9b9bcf04e670 | -9.3906 | -47.4878 | 2026-08-11 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 236.3 |
| 348fa9d2-bbb7-3ecd-ade1-18fd6048a112 | -11.0294 | -45.6536 | 2026-08-11 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 9f56ee20-f16a-3b9a-b729-7ec022413587 | -13.8611 | -53.7845 | 2026-08-11 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 56dea487-1293-3125-974b-9f83fdb156a7 | -8.9598 | -60.555 | 2026-08-11 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| baef79cc-3f92-32f6-a393-564bb78ca189 | -14.2872 | -45.3069 | 2026-08-11 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| b9f835e6-2e04-3881-a442-ffd02b9f1836 | -8.9415 | -60.5174 | 2026-08-11 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 918a5e7e-e299-3d4d-992a-5c395c38492f | -14.2877 | -45.2835 | 2026-08-11 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 8e80ce7d-a914-3e0a-bd94-5e9da2de9416 | -9.3909 | -47.4656 | 2026-08-11 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 06ec2c19-6b3d-3662-8191-fc3451bfa965 | -13.8403 | -53.8909 | 2026-08-11 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 45cc8ad2-01c9-31c2-b3ff-4ba888ae7e6b | -13.5498 | -46.3074 | 2026-08-11 13:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 326.7 |
| 9b5fd7c6-2bd7-3881-a728-730c90262c8b | -14.2559 | -51.9686 | 2026-08-11 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 337.7 |
| 70ddf569-1126-3b37-b110-f3e55341901b | -13.8611 | -53.7845 | 2026-08-11 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 26e21094-0933-3d60-bef2-14743c7e08a1 | -13.8419 | -53.7867 | 2026-08-11 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| c20455b7-f723-33f4-bf28-21b2b62af49e | -15.0545 | -52.7122 | 2026-08-11 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| cdc86954-e33a-377e-a000-987c19f38dbb | -15.0541 | -52.7335 | 2026-08-11 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 5450ddfa-e7c3-38f4-9829-08ae3c971264 | -9.3906 | -47.4878 | 2026-08-11 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 161.1 |
| c92884e9-980a-357a-ad8b-9a0da988e4c3 | -8.96 | -60.5358 | 2026-08-11 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| f04a3049-8763-3d39-9805-6bc5522e55d9 | -10.2275 | -45.8481 | 2026-08-11 13:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 86e6e0de-33e4-3ffb-86a0-73c9a98c9ca7 | -11.0294 | -45.6536 | 2026-08-11 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 5992c503-587a-3e23-88af-88c7e6bc614c | -15.0739 | -52.7097 | 2026-08-11 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 133.9 |
| c99c01ac-16f4-3fb3-8a3d-8931059a8c15 | -15.0736 | -52.7309 | 2026-08-11 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 0895df13-87ef-335e-9863-4fde9cb0045d | -10.2271 | -45.8708 | 2026-08-11 13:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 500.7 |
| 702ceb5d-a37f-3c58-b2cb-e2195112c99d | -13.84 | -53.9117 | 2026-08-11 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 4f23cd23-8c8a-3b5c-9ed4-6505bf745b93 | -9.3717 | -47.4897 | 2026-08-11 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 181.7 |
| fd9062cd-e3bb-3740-923e-aa46a3cff384 | -8.9598 | -60.555 | 2026-08-11 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| bd2d0039-5fe5-34db-b0da-24f5833ef875 | -13.8608 | -53.8053 | 2026-08-11 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 33642d68-70e9-3a91-b71f-aef042630875 | -13.8211 | -53.8931 | 2026-08-11 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 120.7 |
| b5e99f7f-52bb-3011-a9c6-dddead3345fb | -10.2268 | -45.8935 | 2026-08-11 13:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 15320908-7da4-3086-8549-20d951c8b4ec | -13.5502 | -46.2844 | 2026-08-11 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 188.9 |
| 9a5f8646-bebe-32ec-a7d4-34cf8b64b6dc | -15.0541 | -52.7335 | 2026-08-11 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 38fe5767-0ee2-311a-8da5-71e3d2d05b20 | -9.3717 | -47.4897 | 2026-08-11 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 180.2 |
| e1e54efd-de83-303f-a551-1a2ef6d3347a | -15.0739 | -52.7097 | 2026-08-11 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b3fcd713-d024-367d-a6b6-5e6d9f4135ac | -13.8403 | -53.8909 | 2026-08-11 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d7ec57bc-211d-3d35-8548-41b6c838a181 | -11.0294 | -45.6536 | 2026-08-11 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 91e581c8-cd4f-3eeb-b9ea-29d28d07330b | -11.8669 | -48.0791 | 2026-08-11 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 75c111de-ab0b-353d-8159-ffccdc0787c6 | -13.6789 | -51.9575 | 2026-08-11 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 357b8004-2674-3fe6-8f7d-e2481f7411c8 | -15.0736 | -52.7309 | 2026-08-11 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 829dd788-3ea5-3199-8605-d76f32975dcc | -9.3714 | -47.5119 | 2026-08-11 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| bfac9c41-b3b7-3761-bf3b-19ddd9c5171a | -9.372 | -47.4676 | 2026-08-11 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 2a0c4dd3-25dc-3196-a5ca-5249d61bf4e6 | -11.0107 | -45.6333 | 2026-08-11 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 57758085-1de4-3da4-b172-72cb938287db | -11.8864 | -48.0545 | 2026-08-11 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 49850822-f6dc-3cf9-8910-6b9997e377e8 | -14.2559 | -51.9686 | 2026-08-11 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 220.6 |
| 3eaa446b-cecf-3814-8de6-6f27b8454e78 | -13.5691 | -46.3042 | 2026-08-11 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 104.8 |
| b34d758a-0aee-3654-91ea-d19f7d02faf7 | -15.0545 | -52.7122 | 2026-08-11 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| c94e9225-b59c-3e75-93ea-ab66396e59e7 | -14.2877 | -45.2835 | 2026-08-11 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 0b167ab8-489c-3155-868e-3b355cf40c6c | -11.7908 | -51.8189 | 2026-08-11 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 415.4 |
| 0b2b3e6a-e6cc-3961-b377-ff1c3fc9fd94 | -11.886 | -48.0766 | 2026-08-11 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 154.4 |
| d3093c82-ea20-38a2-9dfc-d79825983743 | -8.9415 | -60.5174 | 2026-08-11 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| fe2f927e-0481-3009-87ac-7f5efd6bbac3 | -11.7718 | -51.821 | 2026-08-11 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| e52ed270-fb72-3378-aa50-d83e4604f05b | -13.5498 | -46.3074 | 2026-08-11 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 357.2 |
| 4b3e0f47-f4b8-3e67-bb73-ce7c7c2fee53 | -14.6463 | -47.6474 | 2026-08-11 13:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 5cb1a6a7-5037-39a2-bdbe-df788b3ea704 | -13.8608 | -53.8053 | 2026-08-11 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f0167bbc-dca3-3f7d-95d0-fbbd2e664349 | -11.7905 | -51.84 | 2026-08-11 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 567.4 |
| ef4ca1da-32fb-3625-b999-2ec20d396a94 | -13.8419 | -53.7867 | 2026-08-11 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 9ce116c3-1cab-3fa5-a259-437718f02ab7 | -13.8211 | -53.8931 | 2026-08-11 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 3d46b77f-deff-3894-9cb0-3d32e10afbb0 | -13.84 | -53.9117 | 2026-08-11 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| f399db4d-d9ee-33de-9d9c-c896a0f9d5a4 | -8.96 | -60.5358 | 2026-08-11 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 1dcfdc70-2638-35ca-bb71-178e7a57eee2 | -13.8611 | -53.7845 | 2026-08-11 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 1a289a9f-b1ce-3a23-a0ba-45a0b049b646 | -10.2462 | -45.8684 | 2026-08-11 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| e9e1eb99-f453-3aa8-a837-d198f500ab14 | -11.0298 | -45.6308 | 2026-08-11 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| c1b2ac18-3fc0-3190-93ed-4b5f6198482e | -13.8211 | -53.8931 | 2026-08-11 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| b9c8d6a9-f50b-3dea-90a5-a28b9b03399f | -11.0107 | -45.6333 | 2026-08-11 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 217.8 |
| e9d6d375-829e-3d3b-b1d6-376c694cb504 | -10.2268 | -45.8935 | 2026-08-11 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 8100d07b-2cf1-3e1b-bd01-40f5b310e5e8 | -10.8259 | -50.3315 | 2026-08-11 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |


[Clique aqui para ver as próximas entradas](README34.md)
