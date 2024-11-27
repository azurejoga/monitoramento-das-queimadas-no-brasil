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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82d6b554-bf23-39f3-a3d4-07152a5a80c4 | -4.0495 | -46.6831 | 2024-11-27 11:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 6c6ef62b-47ae-3a0a-8bae-47a40832e3dd | -3.57793 | -41.95171 | 2024-11-27 11:53:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 407e2a8f-11e5-388b-b557-e74c42d538db | -5.35684 | -35.62002 | 2024-11-27 11:53:00 | TERRA_M-M | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 193ecb41-b7b9-3b7b-a258-2dc7875e8405 | -7.35036 | -38.81142 | 2024-11-27 11:53:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 7ac18bcc-c5e4-355f-b312-cb643c5a11fe | -5.4527 | -43.24981 | 2024-11-27 11:53:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| f432aa6d-3ef7-3fb0-abba-ae24424196bd | -6.36701 | -37.97952 | 2024-11-27 11:53:00 | TERRA_M-M | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 0e329b40-279e-3b34-8902-843a70d40d82 | -7.96545 | -37.21332 | 2024-11-27 11:53:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 3933ab65-ad0b-3fd6-9502-57ebe9255ebb | -7.73859 | -35.10202 | 2024-11-27 11:53:00 | TERRA_M-M | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 47.3 |
| b1d036fa-cb9a-3649-b6df-6e3003fd9f94 | -7.33156 | -37.56586 | 2024-11-27 11:53:00 | TERRA_M-M | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 23d5ee6b-cd5d-3633-a39c-be82b608a44d | -8.86523 | -35.15265 | 2024-11-27 11:53:00 | TERRA_M-M | SÃO JOSÉ DA COROA GRANDE | PERNAMBUCO | Brasil | 2613404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 5ed12f80-b55c-3626-b4c6-0746f2a6fdbf | -7.67205 | -37.63127 | 2024-11-27 11:53:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 491b5510-ae14-3f16-bc5e-594d47f1093e | -6.20427 | -37.37851 | 2024-11-27 11:53:00 | TERRA_M-M | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 30b91fdb-b9e5-3ce9-b619-e7481ba23d7c | -7.32125 | -37.25627 | 2024-11-27 11:53:00 | TERRA_M-M | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 696d85cb-b739-3164-9210-4bf1b29eb243 | -4.36281 | -39.39292 | 2024-11-27 11:53:00 | TERRA_M-M | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 30.7 |
| d4cf0894-8c15-3ddb-89f8-3b8fc4241696 | -7.61764 | -36.69217 | 2024-11-27 11:53:00 | TERRA_M-M | COXIXOLA | PARAÍBA | Brasil | 2504850 | 25 | 33 | nan | nan | nan | Caatinga | 19.0 |
| c5f0418f-ac04-3e01-a422-d1133a608dab | -7.13734 | -37.56668 | 2024-11-27 11:53:00 | TERRA_M-M | CATINGUEIRA | PARAÍBA | Brasil | 2504207 | 25 | 33 | nan | nan | nan | Caatinga | 8.0 |
| fe0f75a5-be7b-3550-9c4b-e31afc316e58 | -4.19277 | -38.82761 | 2024-11-27 11:53:00 | TERRA_M-M | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 21.6 |
| ddb2a192-0174-35f3-b17a-8058745de9d2 | -7.73732 | -35.11092 | 2024-11-27 11:53:00 | TERRA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 88214c6a-ce28-3675-810f-6d5d9a947e5f | -6.3336 | -38.20588 | 2024-11-27 11:53:00 | TERRA_M-M | MARCELINO VIEIRA | RIO GRANDE DO NORTE | Brasil | 2407302 | 24 | 33 | nan | nan | nan | Caatinga | 44.0 |
| 87648b1a-f058-3cf8-b732-6eb1e4274ded | -5.37583 | -35.61366 | 2024-11-27 11:53:00 | TERRA_M-M | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 22.1 |
| c20b7204-999b-3240-b0ce-dc1e1a0e39fa | -7.72847 | -35.10967 | 2024-11-27 11:53:00 | TERRA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| cea21ee3-093c-32c5-af7b-70f2d0ac183e | -6.79322 | -38.30046 | 2024-11-27 11:53:00 | TERRA_M-M | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 19.6 |
| f911b202-3091-3b8d-aa79-f35444d097b9 | -6.44166 | -37.53765 | 2024-11-27 11:53:00 | TERRA_M-M | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 33.6 |
| 7f070930-d282-3805-8463-f62cc5e687fd | -3.27085 | -43.04095 | 2024-11-27 11:53:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| d735eb5a-9813-36f8-bd4d-d001a5b8c398 | -7.97375 | -37.1567 | 2024-11-27 11:53:00 | TERRA_M-M | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 4a185b3a-cd9e-3a08-a86b-c3ec2dfb1a52 | -5.42139 | -37.60833 | 2024-11-27 11:53:00 | TERRA_M-M | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 8b0a26b6-0d27-3863-a89f-deefbeb23e2e | -7.68963 | -37.51358 | 2024-11-27 11:53:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 11.9 |
| b97827d0-5da2-31c8-8ac0-fa4c7afcc38d | -5.36698 | -35.61241 | 2024-11-27 11:53:00 | TERRA_M-M | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 23.9 |
| fc44559b-fce2-3a80-b18a-96d6112fa010 | -7.30363 | -37.56205 | 2024-11-27 11:53:00 | TERRA_M-M | CATINGUEIRA | PARAÍBA | Brasil | 2504207 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 7847e0d3-48d3-3303-89ec-d875daf1c1e3 | -8.41975 | -36.50628 | 2024-11-27 11:53:00 | TERRA_M-M | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ff2992ae-5397-3580-853a-9f47983c488b | -6.43081 | -37.54627 | 2024-11-27 11:53:00 | TERRA_M-M | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 10.8 |
| d0c497ab-99a3-342a-9d86-328267eeff1e | -6.25079 | -38.14281 | 2024-11-27 11:53:00 | TERRA_M-M | MARCELINO VIEIRA | RIO GRANDE DO NORTE | Brasil | 2407302 | 24 | 33 | nan | nan | nan | Caatinga | 28.7 |
| da1c6e93-d6e7-3efc-b4a4-5453027d0c5f | -7.69887 | -37.51496 | 2024-11-27 11:53:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 15.0 |
| ba205522-cdf3-315a-a98f-66685c4f2573 | -7.72974 | -35.10077 | 2024-11-27 11:53:00 | TERRA_M-M | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| f0d975a8-ad74-3e6e-9ef1-d8e80a658554 | -7.30515 | -37.5519 | 2024-11-27 11:53:00 | TERRA_M-M | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 32.3 |
| d217e597-fae0-3c28-b5fa-36ede8ee3ab1 | -7.14844 | -35.73056 | 2024-11-27 11:53:00 | TERRA_M-M | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 8.4 |
| d52eaa65-4191-3358-a809-c5e4cd98a2ed | -3.58148 | -41.97009 | 2024-11-27 11:53:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| 6dcb1d1e-27f8-3ac2-a3cf-af866e9ac673 | -5.76972 | -38.07463 | 2024-11-27 11:53:00 | TERRA_M-M | POTIRETAMA | CEARÁ | Brasil | 2311231 | 23 | 33 | nan | nan | nan | Caatinga | 22.0 |
| eb99cf00-44fe-33ce-bc01-8996430609f2 | -7.67058 | -37.64114 | 2024-11-27 11:53:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 67f3a0b2-4adb-3303-a45e-c72108398156 | -6.44019 | -37.54768 | 2024-11-27 11:53:00 | TERRA_M-M | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 7b79c227-d3e4-3825-bf3e-9f23d33f0be5 | -6.43229 | -37.53627 | 2024-11-27 11:53:00 | TERRA_M-M | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 53a34865-9ecc-321d-ae43-a88290f878fe | -7.9124 | -38.00417 | 2024-11-27 11:53:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 673ab1d1-1ffe-3757-9668-92b36be6d88d | -8.42106 | -36.4973 | 2024-11-27 11:53:00 | TERRA_M-M | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 968765fa-5206-3415-ba7b-5adc48dc1e74 | -7.99448 | -38.82165 | 2024-11-27 11:53:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 2be6384b-0214-3979-bb13-8617e0911ffd | -6.79019 | -38.30474 | 2024-11-27 11:53:00 | TERRA_M-M | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 6f76b880-9458-31a0-9bee-25b14687351a | -7.40985 | -37.53292 | 2024-11-27 11:53:00 | TERRA_M-M | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 12.3 |
| e955c4a4-56ff-38ed-bf41-75c4f26a95be | -6.92858 | -38.08434 | 2024-11-27 11:53:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 6600ab62-b446-3006-a428-a20207bd4f64 | -6.20577 | -37.36858 | 2024-11-27 11:53:00 | TERRA_M-M | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 3eb52533-9910-311e-a3f5-8ed59c1e2dac | -5.36569 | -35.62126 | 2024-11-27 11:53:00 | TERRA_M-M | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 01fd0ba3-2e46-3151-8f7b-3f610b851ce4 | -8.42043 | -36.62598 | 2024-11-27 11:53:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 5c3a0d1f-8f15-31c9-b08b-e19d429f75e5 | -7.60251 | -35.07938 | 2024-11-27 11:53:00 | TERRA_M-M | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 70.2 |
| 5514ae6f-071d-38b8-bd9d-ab99b5692585 | -5.9788 | -45.3621 | 2024-11-27 12:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 5256a16d-5711-3c49-a8c6-7d29c0366372 | -3.4 | -42.05 | 2024-11-27 12:00:00 | MSG-03 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 078d1093-81cb-3184-94e3-c4bea942f64b | -3.5732 | -42.1116 | 2024-11-27 12:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 129.9 |
| b81739a7-081a-35d0-81fe-ce0bf36db489 | -3.5921 | -42.0869 | 2024-11-27 12:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 40c48907-52a6-3df6-84a7-a25786fdcc54 | -3.5732 | -42.1116 | 2024-11-27 12:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| 7742a4f8-a1ae-3c2a-9183-0e1a473fbc26 | -3.5742 | -41.9452 | 2024-11-27 12:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 6e1fd241-27b9-30ed-94fb-b55a2818bcca | -5.3823 | -42.9671 | 2024-11-27 12:20:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 3c90c5b6-d8ba-3d03-8f8d-735df614a6c6 | -3.0393 | -48.5082 | 2024-11-27 12:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 4a89bf01-3a10-3495-8772-a5ccecc6e2f6 | -4.3005 | -48.1998 | 2024-11-27 12:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| afeccd6b-effb-30ce-a266-3ee2ef030c29 | -5.9788 | -45.3621 | 2024-11-27 12:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 2d2c86d1-717e-3a65-a238-88aad9fc44eb | -3.5741 | -41.969 | 2024-11-27 12:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 93bcb3ae-7385-3681-8193-65ba766aaa40 | -3.5742 | -41.9452 | 2024-11-27 12:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 0f01758e-c7d3-39de-b4d2-fc28af97be92 | -4.1417 | -43.8135 | 2024-11-27 12:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a4e453ca-710a-33c2-b7c0-9041bb2f6fd5 | -3.5742 | -41.9452 | 2024-11-27 12:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 56e58ac2-c4fd-3a1e-85f8-082359fa0042 | -4.3005 | -48.1998 | 2024-11-27 12:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| c93ae76e-f0e0-3a19-8554-a8dafbfb55d8 | -3.5741 | -41.969 | 2024-11-27 12:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 1af5bc1e-1d71-30df-a66c-4467b3b49e6d | -5.9975 | -45.3607 | 2024-11-27 12:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 0260b77f-c2bc-3022-838f-b3b83b2b4ef1 | -5.9788 | -45.3621 | 2024-11-27 12:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| f2edfa1f-3b78-33d9-a589-e6081562ceb4 | -4.1417 | -43.8135 | 2024-11-27 12:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 4dc1197d-62ec-3f28-acfb-b60618772637 | -3.5741 | -41.969 | 2024-11-27 13:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 115.0 |
| 4507fa95-12d9-32ed-a3a9-a3ee1b3a108e | -3.5742 | -41.9452 | 2024-11-27 13:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| ec4f9d7c-014b-307c-b9a1-288a934dc3a2 | -4.1417 | -43.8135 | 2024-11-27 13:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 0e956fe8-7274-3171-b54a-93052a28902a | -3.4989 | -42.0441 | 2024-11-27 13:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| 1c3d30f4-ece7-32ef-a1ca-481179b70ac7 | -3.499 | -42.0203 | 2024-11-27 13:00:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 376.3 |
| 438b9dac-80df-3be4-85c8-32e52636ab45 | -3.2692 | -43.0441 | 2024-11-27 13:00:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 55b884e2-bdfd-377e-8f4a-761218568e94 | -3.51 | -42.02 | 2024-11-27 13:00:00 | MSG-03 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 114013d2-44db-3286-9edb-7b5fce964ad1 | -6.12 | -43.95 | 2024-11-27 13:00:00 | MSG-03 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c171b6f7-0b5a-3b52-968d-055aae50b2be | -3.0489 | -42.3254 | 2024-11-27 13:10:00 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 147.0 |
| ebc50c68-86d3-3032-a508-886127331f5d | -3.5742 | -41.9452 | 2024-11-27 13:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 134.1 |
| 643e73bb-280d-3605-a9a4-f5d3ad9691f5 | -1.5786 | -48.6513 | 2024-11-27 13:10:00 | GOES-16 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| cb81ee5d-4c07-3e73-86b2-5f640a099e21 | -4.1419 | -43.7905 | 2024-11-27 13:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 17ed2054-14f2-38f8-a76d-a7c8950f5e6d | -3.5741 | -41.969 | 2024-11-27 13:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 117.5 |
| 3d40c33e-3b31-37a1-81be-d609ae1c9ee9 | -4.1417 | -43.8135 | 2024-11-27 13:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 5c3886fe-731f-3286-b104-cf1f9c8e0372 | -3.2692 | -43.0441 | 2024-11-27 13:10:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 073679c5-ba53-3f41-9e5e-7d173d8ab2bf | -3.499 | -42.0203 | 2024-11-27 13:10:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 181.9 |
| 2ede95f4-44ef-3881-b3c9-59234a34f16f | -3.0489 | -42.3254 | 2024-11-27 13:20:00 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| a73a3583-471e-3c3a-934e-fd3a095824e3 | -4.1417 | -43.8135 | 2024-11-27 13:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 76db5c75-1ef6-3547-ac71-40e2cebf3cb2 | -3.5742 | -41.9452 | 2024-11-27 13:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 153.4 |
| 5aa1ad01-99f7-3a09-9675-2c491cc981ba | -4.1419 | -43.7905 | 2024-11-27 13:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 482cc8df-46a7-3dda-84cf-cbbf6952e905 | -3.499 | -42.0203 | 2024-11-27 13:20:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 107.4 |
| e8744600-82df-3461-8b70-08e3567460fc | -3.7994 | -44.9285 | 2024-11-27 13:20:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 1621d416-7e0c-3ee3-a680-8ed84d7d6a7c | -3.5741 | -41.969 | 2024-11-27 13:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 140.4 |
| 778aeae4-6d95-3990-8611-9a52b4d64ec6 | -3.2692 | -43.0441 | 2024-11-27 13:20:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| ba4feb26-82e4-3621-b3b9-b48079534d3d | -3.5929 | -41.9442 | 2024-11-27 13:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 4409b806-75a5-30e3-9439-4733c30c750a | -3.1246 | -42.1327 | 2024-11-27 13:30:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| a4700a31-b5f2-37f0-8f1f-96b4392e0f1c | -4.1417 | -43.8135 | 2024-11-27 13:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 84b19427-05fd-3c00-8098-0b4f0d6c1842 | -4.1604 | -43.8125 | 2024-11-27 13:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 279f37b5-f036-3fd5-b5fd-13b7896fdeb6 | -3.5741 | -41.969 | 2024-11-27 13:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 121.6 |
| a8c354f9-7a14-3e6d-b7ea-4a631f8358af | -3.2556 | -42.1031 | 2024-11-27 13:30:00 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |


[Clique aqui para ver as próximas entradas](README84.md)
