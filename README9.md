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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 392c2dff-ea67-3495-8b04-59ee571236ec | -3.3939 | -44.1492 | 2024-11-26 01:30:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 6c54344d-a80b-3745-8860-e67ca31c1461 | -3.2604 | -53.2746 | 2024-11-26 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 764dbc7f-9bbc-382d-8d48-14b2f9ae1c64 | -17.6453 | -57.5874 | 2024-11-26 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 23f2047e-3be3-343c-9e7c-97afec190015 | -2.5133 | -45.6092 | 2024-11-26 01:30:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 29e6bedd-a9af-347b-b254-a02e06f6bba6 | -2.8014 | -53.0227 | 2024-11-26 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| d805f89d-99be-3435-8971-a3943cc449dc | -3.1877 | -48.4172 | 2024-11-26 01:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| ffe036aa-ec62-30a1-9730-8172e4068e0c | -2.5319 | -45.6086 | 2024-11-26 01:30:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 111.7 |
| b68c7f0a-bc8f-3170-8e7e-174356821759 | -2.8014 | -53.0024 | 2024-11-26 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| c477cc6f-b483-3226-9556-ab2e60804f03 | -3.9267 | -42.401 | 2024-11-26 01:30:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 32.0 |
| cfa7d654-737d-314f-9a3a-4fa2ac408431 | -6.0862 | -48.0339 | 2024-11-26 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| d3cb803a-05a3-3611-916f-d8bf270487f2 | -3.2603 | -53.2949 | 2024-11-26 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 8cda8a19-9f15-33dd-9d66-1151c5ba1309 | -3.8691 | -49.1415 | 2024-11-26 01:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 7ecd0dfd-f445-3bff-bcbb-f043b14c15a3 | -2.8014 | -53.0024 | 2024-11-26 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| bfa861e2-2132-3d8e-907b-28947153d005 | -3.1691 | -48.4394 | 2024-11-26 01:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 2332c12e-24da-3e48-8be8-ee79cefc2877 | -3.6041 | -50.3991 | 2024-11-26 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| ce02d756-0800-31af-a8f4-ef9fb5f24c91 | -3.5857 | -50.3787 | 2024-11-26 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| dd59c62d-a2a9-3640-b4f7-9387ca3a3853 | -3.3938 | -44.1722 | 2024-11-26 01:40:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| aa278b0c-ef08-346d-8963-76c0506689b5 | 2.6718 | -60.4304 | 2024-11-26 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 3a9a869e-785d-3883-83ea-69ece728e85c | -3.9265 | -42.4246 | 2024-11-26 01:40:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 44.4 |
| 1e008510-eb27-38a2-8b11-cf2eb477ba1e | -3.1877 | -48.4172 | 2024-11-26 01:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 52b93f29-10c7-31c2-ac11-320d0e815974 | -17.6453 | -57.5874 | 2024-11-26 01:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 9ecd4c10-5803-3b29-abd6-d7a8293de38a | -3.9078 | -42.4256 | 2024-11-26 01:40:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 40.7 |
| ea81b3c9-ba2f-37e0-8add-12d111b9646a | -2.8014 | -53.0227 | 2024-11-26 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 72854135-8440-3229-b4fb-055c4cffc581 | -2.8197 | -53.0425 | 2024-11-26 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 5da27818-bc4e-32b0-8a79-47bb270d0752 | -2.8013 | -53.043 | 2024-11-26 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ffa5d4f2-409d-369d-b269-fe4939e91006 | -3.6973 | -50.2277 | 2024-11-26 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 7da1f293-8e95-3a38-824f-762ce35ba45a | -2.532 | -45.5862 | 2024-11-26 01:40:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 39.6 |
| c4f7ca55-c171-34d9-bf82-89c1b455ea38 | -3.6042 | -50.3781 | 2024-11-26 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 192.1 |
| 6873f15e-6b96-38f6-85b9-45b3381b3726 | -2.8017 | -52.921 | 2024-11-26 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 7bc9e554-bf9b-3083-bc25-81b90033aa18 | -6.0862 | -48.0339 | 2024-11-26 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 63df0c13-7c05-3301-b9d2-53ebc47894a4 | -2.8198 | -53.0222 | 2024-11-26 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| edf41dfd-c61f-311b-a35e-9835e30db2e9 | -3.1876 | -48.4387 | 2024-11-26 01:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 185.6 |
| 44dc53e8-f9c5-3b66-ae7d-4d7978e9e792 | -2.5319 | -45.6086 | 2024-11-26 01:40:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 43.5 |
| c2185d17-f55d-379f-8116-5402632faac7 | -6.0676 | -48.0352 | 2024-11-26 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 660a35f8-97c3-346e-9377-484d7b0f5ba1 | -3.5856 | -50.3997 | 2024-11-26 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5a670ed1-11ee-306d-a1ce-1f14fb895350 | -4.3231 | -47.5258 | 2024-11-26 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ba0043a3-138c-3b61-b0f6-8fdcc67a4515 | 1.4186 | -55.9057 | 2024-11-26 01:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| dde78a80-6cde-3a78-8408-32efcd90afbf | -2.8014 | -53.0024 | 2024-11-26 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| a2ffdfe4-bbb2-308f-8f5c-b7ea373eac8b | -3.3938 | -44.1722 | 2024-11-26 01:50:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 16cdb043-41f3-3ff9-93c3-085c6f3cfaaa | -3.2603 | -53.2949 | 2024-11-26 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 000cfb1b-35bf-313a-8616-cb3a10a9fc19 | -6.0676 | -48.0352 | 2024-11-26 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| bc3c6c8b-1330-3024-99c4-0a1aa16e31ed | -17.6453 | -57.5874 | 2024-11-26 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| a24ac132-6e9d-3e30-9ba7-1b5c1aaffb12 | -2.8017 | -52.921 | 2024-11-26 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d13ceea9-6e18-3ee3-87ae-4435ca5891a9 | 1.4186 | -55.9254 | 2024-11-26 01:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b9783813-825f-374a-b913-3a1cd84fad9d | -3.6041 | -50.3991 | 2024-11-26 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 9f220945-353e-32c7-9b5f-5f6d097fb5d7 | -3.9078 | -42.4256 | 2024-11-26 01:50:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 44.2 |
| bb3f7573-16fc-30aa-985e-9bb67e59e2cf | -3.1691 | -48.4394 | 2024-11-26 01:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 09000e15-b6de-3866-b5de-9489757625be | -2.8014 | -53.0227 | 2024-11-26 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| cd750cf0-f705-3c7e-bb34-597a14d75fa5 | -2.8198 | -53.0222 | 2024-11-26 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 42bac819-d8e6-34b8-94ca-786f9827bc20 | -3.1877 | -48.4172 | 2024-11-26 01:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| ea65201c-f345-3c5e-8128-28264619fe98 | -3.5857 | -50.3787 | 2024-11-26 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| e8fe45bd-761f-3f7b-ad98-ea8ca4bbc64e | -3.1876 | -48.4387 | 2024-11-26 01:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 246.4 |
| ea56d973-ca99-3d7b-be6f-c4271d59d77e | -6.0862 | -48.0339 | 2024-11-26 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| a9ee0bfd-e50a-3628-98fe-bd94ef1eb0ad | -3.1875 | -48.4603 | 2024-11-26 01:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 0326b07a-dde3-300d-b440-d11e2d71683d | -3.6042 | -50.3781 | 2024-11-26 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 185.2 |
| ff44e39d-5431-327e-b7e7-513847d7195b | -3.5856 | -50.3997 | 2024-11-26 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| f1969afc-2edf-3fd7-ba32-aacb4ed98c65 | -3.8691 | -49.1415 | 2024-11-26 01:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 46f24156-e7fa-3b11-befa-178b02d5e2da | -3.1875 | -48.4603 | 2024-11-26 02:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| fef1d24b-c954-3dd6-a1da-9eb2657056a2 | -3.5856 | -50.3997 | 2024-11-26 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 6c5d678b-35b4-349b-ae46-59632749a562 | -2.8198 | -53.0222 | 2024-11-26 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 1cdb6503-9a4c-3169-b95f-fd1c3bc0c7ce | -3.1876 | -48.4387 | 2024-11-26 02:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 204.9 |
| 4d8c826c-d481-3b8c-9e38-92b5b0e246af | -3.6041 | -50.3991 | 2024-11-26 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 3c48c1b6-d4d2-32cf-8e14-3083b2a8f1e9 | -3.8691 | -49.1415 | 2024-11-26 02:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 301263ea-ff09-3f85-bc69-f1d3e4729ba1 | -2.8017 | -52.921 | 2024-11-26 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d5d01fee-2eaf-3454-a05e-4bae54d0e56a | -3.9078 | -42.4256 | 2024-11-26 02:00:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 46.1 |
| a05bc6c6-9b4c-3de2-9930-c65e4fd30b1f | -17.6453 | -57.5874 | 2024-11-26 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 69396ed1-887a-3e5d-abd4-9ae23df0ed85 | -3.3752 | -44.173 | 2024-11-26 02:00:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e4fd44dd-a41b-3006-abd2-2b5eb09d18b7 | -2.8014 | -53.0227 | 2024-11-26 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 56f15904-829e-3a45-8797-480ea86c4c7d | -3.1877 | -48.4172 | 2024-11-26 02:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| ff363a67-4404-39d4-8598-9fcf0f7aafdd | -3.5857 | -50.3787 | 2024-11-26 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 3875d00d-972a-3e0f-a7c1-95e59fd17001 | -3.1691 | -48.4394 | 2024-11-26 02:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| fada7946-1683-3df1-9e07-cbf77efff4ce | -3.6042 | -50.3781 | 2024-11-26 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 87460279-e967-3e07-b12b-a6ea644ceed8 | -3.3938 | -44.1722 | 2024-11-26 02:00:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| d1cd3ef5-eab7-3160-98cc-f067bab6c67c | -4.0 | -48.09 | 2024-11-26 02:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ea70086-6797-3b88-a484-00b0ab6a09a5 | -4.0 | -48.04 | 2024-11-26 02:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d1ae89b-c923-304e-8057-d71cf08e0b6d | -16.08505 | -60.10758 | 2024-11-26 02:04:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7091badf-e2ce-3f05-af84-c8d469c3ebd7 | -11.9307 | -62.9284 | 2024-11-26 02:06:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e50fe3d9-6787-3820-8ac1-fc3fb2adca75 | -10.12015 | -65.02905 | 2024-11-26 02:06:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| abf05649-fc94-3fce-97a3-7b52e652fcc3 | -3.3752 | -44.173 | 2024-11-26 02:10:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| dd6c2bb1-d09d-3c18-9d7b-edfb7b68ae04 | -3.5856 | -50.3997 | 2024-11-26 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 22f57060-c9c5-393f-92d9-1585573f901e | -2.8014 | -53.0227 | 2024-11-26 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 221d37a6-e13f-3ac7-8c35-7551db12bc18 | -3.6041 | -50.3991 | 2024-11-26 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 76b8ed16-a02b-3a24-9017-ba2223dd3d9d | -3.1877 | -48.4172 | 2024-11-26 02:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 6a608c24-b2ff-3905-b306-2c207f059d99 | -3.1876 | -48.4387 | 2024-11-26 02:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 148.3 |
| bf44b48b-d78b-30a4-abd0-9b8f7ad90b86 | -3.9078 | -42.4256 | 2024-11-26 02:10:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 50.6 |
| ccc2da5f-9bee-3af5-be11-11807163417d | -3.1691 | -48.4394 | 2024-11-26 02:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| df0b9451-e376-3070-acd7-3f653495e931 | -3.2419 | -53.2954 | 2024-11-26 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 9598e3ad-fdbc-332f-95b3-4ad0ad64f91e | -3.6042 | -50.3781 | 2024-11-26 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| a0590404-71da-3e81-ad8e-06d6bcf5295f | -3.5857 | -50.3787 | 2024-11-26 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 7c0d4653-6db9-3c65-adf9-5bbdcebc30da | -3.1875 | -48.4603 | 2024-11-26 02:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| ecfd81c7-a3e2-303f-9e10-d8b0c8b5165c | -17.6453 | -57.5874 | 2024-11-26 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 400fdf59-8960-3086-b4eb-0d50955a1d08 | -3.3938 | -44.1722 | 2024-11-26 02:10:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 2ee4a6f0-c62e-3a80-811a-fea90e0bc86d | 1.94991 | -60.85761 | 2024-11-26 02:10:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e9b3bf5c-210e-31a4-9c15-b6aebf2dd8d7 | 2.69248 | -60.42551 | 2024-11-26 02:10:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 9dd2adc8-e1f5-3be0-aa68-767770138b95 | 3.81481 | -59.61237 | 2024-11-26 02:10:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 22.3 |
| da302570-9f4d-3c9f-a26a-4af443d149fc | 2.67734 | -60.42341 | 2024-11-26 02:10:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| e6579e80-54f2-3e34-942e-4adc00bb0c32 | 2.67533 | -60.44577 | 2024-11-26 02:10:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 23.1 |
| b7ee79d8-63a2-3024-84fd-0f7e5cd1d2a5 | 2.6793 | -60.41705 | 2024-11-26 02:10:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 921df623-1e26-3b42-b699-ff8055c9a51b | 3.82462 | -59.60834 | 2024-11-26 02:10:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 018f44b6-f9a9-37e5-8e8a-ab377286c445 | -2.8014 | -53.0227 | 2024-11-26 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |


[Clique aqui para ver as próximas entradas](README10.md)
