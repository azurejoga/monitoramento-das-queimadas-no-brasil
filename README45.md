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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1a0dc63-eef9-3743-ad45-7443853025b5 | -16.5345 | -57.2259 | 2024-10-06 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 0668258c-d3f5-3a32-b451-8015366df4ef | -16.5147 | -57.2486 | 2024-10-06 03:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 0f075a9d-6af2-3acc-837a-9d1e1a14c95d | -16.6398 | -55.5452 | 2024-10-06 03:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 6480853a-044f-37f5-8923-14ad6321dcbb | -16.8241 | -57.438 | 2024-10-06 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.9 |
| c70a5843-5263-33a8-9670-83f322830546 | -16.8238 | -57.4584 | 2024-10-06 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.1 |
| 3902ab57-98c7-3964-ad13-6b43d2fa0bc9 | -17.0885 | -56.8122 | 2024-10-06 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.1 |
| 8d6e35eb-1906-32bd-8de2-9454c6a8658d | -17.0207 | -55.0371 | 2024-10-06 03:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 60286668-bb70-33f2-914f-71c7a00ccc1c | -17.0203 | -55.0581 | 2024-10-06 03:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 501.9 |
| de844e4f-afbe-33b9-a6d6-75b7e0ca467a | -17.02 | -55.0791 | 2024-10-06 03:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 192.8 |
| db3e5b3f-b424-3374-b310-0d9f5e2a15d6 | -17.001 | -55.0398 | 2024-10-06 03:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| c5dae5e9-c202-3f2d-b298-0f85da2439a8 | -17.0007 | -55.0607 | 2024-10-06 03:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 286.7 |
| d0e1eaec-5562-3359-a032-4fbdd9164890 | -17.0003 | -55.0817 | 2024-10-06 03:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 143.5 |
| a737b96c-a3f4-3587-9990-4afca3828011 | -17.1375 | -57.4221 | 2024-10-06 03:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 2b2e2dad-187e-36fb-be00-297dd7b6777b | -18.659 | -57.2552 | 2024-10-06 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.0 |
| dad3315c-fcfe-3d43-b7a2-606f42449240 | -18.6586 | -57.2759 | 2024-10-06 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.8 |
| 697d9391-8ff6-314a-bd09-17beabe8b652 | -18.6387 | -57.2785 | 2024-10-06 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.1 |
| 6c7c8249-56ba-3ad6-8078-35e483a6410b | -20.6024 | -49.3591 | 2024-10-06 03:37:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 00e234b9-f968-3fbc-b812-b9cef8bf9a93 | -20.6018 | -49.3821 | 2024-10-06 03:37:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 79b96441-8613-3e84-bb42-e021ae419ff0 | -20.582 | -49.3635 | 2024-10-06 03:37:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 271.0 |
| f5ea7888-bd74-397d-86d5-3a685438af0d | -20.5813 | -49.3865 | 2024-10-06 03:37:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 624.0 |
| 5d698973-6fba-3606-bf53-92b9a7f0f999 | -20.5807 | -49.4095 | 2024-10-06 03:37:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 45354934-6da4-3b16-a5a3-a9043f227dc2 | -20.5609 | -49.3909 | 2024-10-06 03:37:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 1a3e8476-617e-3302-ab7e-95f39106b037 | -21.5218 | -50.9088 | 2024-10-06 03:37:05 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.2 |
| 4b213e72-daa4-31b4-9797-c3dd9b0f8365 | -2.8165 | -48.7082 | 2024-10-06 03:45:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 305b646b-85b4-3645-a3fc-9258731ff9ae | -2.8166 | -48.6867 | 2024-10-06 03:45:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 6d81cf29-cbf1-3c65-a57d-0cf9685cf3b5 | -3.1128 | -48.6346 | 2024-10-06 03:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| da5bad67-eb98-3e18-9a96-0f2aca3654e2 | -3.1129 | -48.6131 | 2024-10-06 03:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 6e67d27a-28cd-38f4-92eb-689ab1f71bef | -3.113 | -48.5916 | 2024-10-06 03:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 142b3ef6-7613-327e-b7e5-865b52f364a2 | -3.1314 | -48.6125 | 2024-10-06 03:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| fb8af8a6-110b-3d04-8cfe-59e12aa66554 | -3.1315 | -48.591 | 2024-10-06 03:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 0358f403-6491-3312-8aab-497161ce39a0 | -3.8464 | -46.4714 | 2024-10-06 03:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 67cf9e26-6d4a-3baf-ba94-7c0555ace665 | -9.3278 | -46.5385 | 2024-10-06 03:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 44147bd7-8a65-3523-a554-0c001a2b60dc | -9.3467 | -46.5365 | 2024-10-06 03:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 48d7fa78-7064-3685-87bd-0858183d97b7 | -9.3835 | -51.0881 | 2024-10-06 03:45:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 85a40532-f0f1-35eb-9e42-c3b2928660de | -9.6691 | -47.8328 | 2024-10-06 03:46:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| fcf9816b-1430-3333-a6bc-ead5a73a9b13 | -9.6694 | -47.8108 | 2024-10-06 03:46:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| e8b732e3-9070-3e94-b699-cba94d2edfd7 | -9.688 | -47.8308 | 2024-10-06 03:46:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 8f64075a-2fd3-3fbe-a7f0-c41b60a81f87 | -9.6883 | -47.8088 | 2024-10-06 03:46:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| d729c4c3-dbd5-3d6a-b2f8-81dbf52458ba | -9.7069 | -47.8288 | 2024-10-06 03:46:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d6e7d397-1d73-33b9-8752-ab889d6ad560 | -9.7072 | -47.8068 | 2024-10-06 03:46:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| d42ef13b-b9f0-34cb-8fd5-87b93b7ba308 | -9.6778 | -64.6457 | 2024-10-06 03:46:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| beee9db4-df91-3c88-944a-026af1e64701 | -9.6779 | -64.6269 | 2024-10-06 03:46:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 98.6 |
| d32f7d8b-57c7-3c5c-9495-71e2f2725450 | -9.6964 | -64.645 | 2024-10-06 03:46:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 70ebb5a1-024f-373c-bf5d-1a56a8558b10 | -9.6965 | -64.6262 | 2024-10-06 03:46:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 73a3919e-94a8-3a83-95ed-2425b22fc5b3 | -10.2148 | -48.0149 | 2024-10-06 03:46:04 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 32639825-f1c7-3e50-93d5-ad68a8b2c339 | -10.2337 | -48.0128 | 2024-10-06 03:46:04 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 1a94f89e-b669-3d72-8253-7f9778c79b8c | -10.4427 | -50.7123 | 2024-10-06 03:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 71a339be-2fb2-38d8-b7d6-0b4e618c3100 | -12.6089 | -53.1338 | 2024-10-06 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| e329edb1-3b91-3111-b62d-95e670c38ef4 | -12.6092 | -53.1129 | 2024-10-06 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ecb56dae-7555-3fc0-b9c9-09b9d9fd3f3c | -12.628 | -53.1317 | 2024-10-06 03:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 49ea55ba-b86d-3076-a476-419d733940b2 | -12.6283 | -53.1108 | 2024-10-06 03:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 2c27c9dd-730b-3a9b-b05b-b2e77a6eb176 | -12.6532 | -54.0415 | 2024-10-06 03:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ea98e0a4-28f4-3079-81e2-b0741d181d88 | -12.6535 | -54.0208 | 2024-10-06 03:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 49ac28a6-6f30-3b68-8cb8-6298d35e1067 | -12.6726 | -54.0189 | 2024-10-06 03:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 812d3881-0775-3ea2-a023-3b6ab884848a | -13.3786 | -61.9582 | 2024-10-06 03:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 26d23d80-a0fb-328e-80a8-b5e15843ed9e | -13.3976 | -61.957 | 2024-10-06 03:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| c375965d-622e-31c6-882a-88ba8ae335c7 | -16.3761 | -57.3867 | 2024-10-06 03:46:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 9482ef00-b1a2-30c9-a9ff-e5b42da860f1 | -16.3764 | -57.3663 | 2024-10-06 03:46:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 42909716-ca05-3442-87ec-dc57164c8c98 | -16.3959 | -57.3641 | 2024-10-06 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| c3cb0525-41d9-3f21-855a-341c5fbcde2e | -16.5147 | -57.2486 | 2024-10-06 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| ed6f17dc-c757-34fb-b2f2-7802f9640ba4 | -16.5345 | -57.2259 | 2024-10-06 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| c6d68c60-0b65-3539-8426-2f9e8f8fd14f | -16.554 | -57.2237 | 2024-10-06 03:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 171.2 |
| e40c9752-c893-3090-8140-144444bffc5b | -16.5544 | -57.2032 | 2024-10-06 03:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 191.2 |
| 584d582e-8430-3f0c-b94e-51ff06f562a4 | -16.5736 | -57.2215 | 2024-10-06 03:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| f40cf30a-c4c7-30e9-bf82-b5413178684e | -16.5739 | -57.201 | 2024-10-06 03:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| e3b07a22-2322-303e-be2f-f86f6f855aec | -16.8238 | -57.4584 | 2024-10-06 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.4 |
| 59901fb8-9d9e-3820-aefe-e9e69125bf9a | -16.9711 | -56.8058 | 2024-10-06 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| a4995300-fc7e-338a-b6f1-944a30139eb8 | -16.9714 | -56.7852 | 2024-10-06 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 45a35992-bd0c-34e3-b39a-e7ce888b2603 | -16.9717 | -56.7646 | 2024-10-06 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 134.1 |
| 14d836fe-d9b8-3fa2-95d0-5bfe97020ae2 | -17.0003 | -55.0817 | 2024-10-06 03:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 403.5 |
| c88a87c3-21bd-381c-a074-c87275c23324 | -17.0007 | -55.0607 | 2024-10-06 03:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 687.7 |
| 58edd6a0-fa9b-3bd1-a67b-bc2a5e8952a6 | -17.001 | -55.0398 | 2024-10-06 03:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 131.1 |
| c3e99b55-9989-35f7-9455-97a0d1fdd581 | -16.9903 | -56.824 | 2024-10-06 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.3 |
| 29ac6015-d05e-38c0-92d4-51e7bca3f454 | -16.9907 | -56.8034 | 2024-10-06 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 60f81174-afea-3b36-b7e4-2723bd42054c | -17.02 | -55.0791 | 2024-10-06 03:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 288.2 |
| 4c691967-4cf0-314f-8192-d06085eca3b3 | -17.0203 | -55.0581 | 2024-10-06 03:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 501.2 |
| 66b2ae8d-13ba-33c3-95ed-d11c484ba44d | -17.0207 | -55.0371 | 2024-10-06 03:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 907228f2-2cf3-3b4a-8ef7-17bcd3db17a7 | -17.01 | -56.8217 | 2024-10-06 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| e44a3b63-6a5c-3b6b-9a7e-5f216daf18f5 | -17.0688 | -56.8145 | 2024-10-06 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 87857fa6-b81a-33ad-9733-c28d93550582 | -17.0885 | -56.8122 | 2024-10-06 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.7 |
| bac824ff-7582-3236-90d3-0a481b79cb44 | -17.1081 | -56.8098 | 2024-10-06 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 54dca327-7e20-33b1-a2ab-dcdcc3c76df6 | -17.1182 | -57.4039 | 2024-10-06 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 7438209a-2a16-3385-b787-1014ec7427e7 | -17.1375 | -57.4221 | 2024-10-06 03:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 1c51f25a-2a5f-35d8-8b17-3c53b1341bf7 | -18.6387 | -57.2785 | 2024-10-06 03:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 168.2 |
| 70ae2c80-9b74-33cb-a16c-966e2602a0a9 | -18.6391 | -57.2578 | 2024-10-06 03:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 6eb419b9-1fe3-3ad1-96cd-eb47ecc09c2c | -18.6586 | -57.2759 | 2024-10-06 03:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.4 |
| 21caaac8-577b-3b97-84e3-3b27f1d671e5 | -18.659 | -57.2552 | 2024-10-06 03:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.8 |
| a45a5777-3b71-3374-9a4c-a18a055e5f39 | -20.5118 | -47.485 | 2024-10-06 03:46:59 | GOES-16 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e8404a4f-062b-3689-9b55-e78302c31f9a | -3.54906 | -42.65841 | 2024-10-06 03:51:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b90b64f-c986-3142-8670-86a006d1fb6d | -4.00365 | -43.26159 | 2024-10-06 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cdfb931-89be-38be-b61d-a94b4148f114 | -3.99945 | -43.26089 | 2024-10-06 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99f3f406-ef7d-3060-8a8c-735de3955c42 | -3.99883 | -43.26476 | 2024-10-06 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 272b299d-2d60-3bc3-b737-14c3e231052d | -5.07081 | -37.71655 | 2024-10-06 03:51:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e18f87cc-a806-3265-8f28-17801648e20f | -4.05868 | -38.21746 | 2024-10-06 03:51:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2c8d5cce-7b57-3bcd-8766-3dd8ebb0f165 | -2.92212 | -40.45149 | 2024-10-06 03:51:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4fdf0dcd-1f56-350f-a323-bfa948f2a9a6 | -3.3182 | -40.00418 | 2024-10-06 03:51:00 | NPP-375D | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 91cd93c4-1034-31c5-9a3e-6f101d293f64 | -2.92576 | -41.46463 | 2024-10-06 03:51:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c34d1eb8-2416-331a-83a9-9708842b1f85 | -2.92501 | -41.46924 | 2024-10-06 03:51:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 76bc91e8-0f13-3b55-8ff5-e7fff88a7aef | -2.80659 | -41.80201 | 2024-10-06 03:51:00 | NPP-375D | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80c647d1-88a3-3055-b56b-81edbb2671da | -3.80464 | -41.59589 | 2024-10-06 03:51:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README46.md)
