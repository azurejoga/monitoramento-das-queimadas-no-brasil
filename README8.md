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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efe5c26c-5256-3ae3-85e6-93c8ae2e8533 | -2.6263 | -54.2747 | 2024-11-13 00:52:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d65884f-0fbd-342f-8935-f8ac1235da23 | 2.6936 | -60.950699 | 2024-11-13 00:52:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bd590353-2027-350d-9553-2853268d05cb | -2.6502 | -51.7197 | 2024-11-13 00:52:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c342cd7c-c94d-31e6-8a21-339fe79f1be4 | -3.142 | -53.2365 | 2024-11-13 00:52:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 826db84f-bddd-34f6-836e-38467fb72ead | -1.888 | -54.200401 | 2024-11-13 00:52:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c29083ba-bacf-3bcf-942d-09a81b3ed728 | -3.3329 | -56.9473 | 2024-11-13 00:52:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42a1c4e6-42cf-3493-8894-45cd14b4166a | -2.3896 | -53.7323 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2a25ed2-8968-3ee4-a5b4-78898b2b39b5 | -1.2128 | -51.777302 | 2024-11-13 00:52:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b7c8cd3-e819-3f06-983b-7a1f6a2bd6df | -2.3952 | -53.666599 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0e8ce6f-e783-391b-a5c2-8e42d2d282f3 | -3.1446 | -54.469299 | 2024-11-13 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7972c20-cf41-3def-ad47-1997ad1c92b1 | -1.3975 | -51.101299 | 2024-11-13 00:52:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f1b9e18-a4d9-3583-b665-f17287303d86 | -3.2213 | -54.852699 | 2024-11-13 00:52:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91163415-2011-3ba0-8059-8f6ccb9a6b16 | -2.2373 | -53.742199 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb966d1b-358d-39b7-bc8e-be58cb84f6ce | -2.0383 | -53.954601 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65dbcc88-39ee-3bdc-b42a-a9379cd78dbc | -2.3837 | -53.661098 | 2024-11-13 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8beb6724-52bb-30bc-a150-a6c2330175e8 | -1.4122 | -53.466 | 2024-11-13 00:52:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ae9bcf1-781f-3d29-bfb2-cd8627ec487b | -2.7254 | -51.8228 | 2024-11-13 00:52:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b19fa927-9315-31e7-b519-7fa56f1b8a60 | -1.6627 | -52.5357 | 2024-11-13 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 3e019518-c11c-3f4e-8bc8-cd117227df35 | -3.7666 | -47.4855 | 2024-11-13 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 1d27009c-9001-3e8a-93f1-9acfd360f09d | -3.5743 | -53.0015 | 2024-11-13 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 37c6826d-2ef2-338c-832a-4ff51b4c689b | -1.6444 | -52.536 | 2024-11-13 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 67851a9a-2274-3b91-ac8e-d127fdda7352 | -2.2296 | -53.7429 | 2024-11-13 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 2fe0ae9c-1d6f-369f-8447-634884e6d1d1 | -2.9925 | -51.0242 | 2024-11-13 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 7f0f1f4e-e3d8-371c-af5e-d4541b5c79b6 | -2.2295 | -53.7631 | 2024-11-13 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| cc2ae98f-9e10-3f96-a260-34975ec70f02 | -2.7033 | -49.33 | 2024-11-13 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| eb1b7800-c832-3b63-8575-0f0e731c85af | -3.4913 | -50.8421 | 2024-11-13 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| dc66041c-f2ff-3e53-958a-e5ac12e22d3e | -2.7033 | -49.3513 | 2024-11-13 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 329d1ed7-af4f-3162-96d5-5a4cf59c6130 | -3.1096 | -54.3066 | 2024-11-13 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| d891756a-3ff3-3321-81e3-ab04771f271d | -4.3433 | -50.4333 | 2024-11-13 01:00:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 35d10ae1-76f9-3391-84d2-29cd3efc6c46 | -1.8798 | -54.211 | 2024-11-13 01:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e82b9bc8-ecb6-3eb4-96e0-633c767a20b9 | -2.9924 | -51.045 | 2024-11-13 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 6d8db1db-f228-3629-b8b7-753cb2add171 | -3.0504 | -50.3332 | 2024-11-13 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 69099f6a-7167-385e-82d6-649f862f7cf1 | -3.5098 | -50.8415 | 2024-11-13 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 8b5b093d-ec65-3b3e-98c0-2dfaf782fee7 | -3.0689 | -50.3326 | 2024-11-13 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 5b3d9a3f-2c76-3b3d-b21a-d9e25793f913 | -3.6791 | -50.1653 | 2024-11-13 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 1aa60a6a-cfb4-3190-8540-484c1d74c232 | -2.7374 | -45.2877 | 2024-11-13 01:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| ada67f4f-74fd-38c5-8c48-20295b4d1170 | -4.6581 | -47.4216 | 2024-11-13 01:00:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 77215941-0b3b-3a42-b1ec-0226fb1cf7c2 | -2.248 | -53.7426 | 2024-11-13 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 191.3 |
| d4d18247-e852-35f7-a9be-8994d33b72e8 | 1.0663 | -60.5985 | 2024-11-13 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 0b67e07a-f41c-39f1-91e7-e0ea18adfb35 | -2.2663 | -53.7422 | 2024-11-13 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 8dd785ce-d30c-3172-9663-0b8f6ad83cbc | -2.2112 | -53.7432 | 2024-11-13 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 3ac6d902-cf84-30a5-bd73-d2cf861e6f71 | -5.3587 | -43.529 | 2024-11-13 01:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 3acc4406-b38f-3530-ae79-8396e9700f9c | 1.048 | -60.5986 | 2024-11-13 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 3eb0bd9e-765f-3a04-9532-120835c0dadb | -2.2479 | -53.7627 | 2024-11-13 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 1f8b1ba2-1eff-38fb-9bab-3de534159e5f | -4.658 | -47.4434 | 2024-11-13 01:00:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 8aafa168-cf04-3558-9dab-7d643ef20e51 | -2.1271 | -50.6912 | 2024-11-13 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| f8feb055-b07f-37d3-8625-d6b3c1f1044c | -3.5743 | -53.0218 | 2024-11-13 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 4d5680db-2ace-3efa-917e-f30563370847 | -1.6444 | -52.536 | 2024-11-13 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| b0eff31d-f60a-35de-ab67-634618c14451 | -2.7033 | -49.3513 | 2024-11-13 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 7a3d8238-a472-3054-afd2-3b0ae7b1a0df | -2.9925 | -51.0242 | 2024-11-13 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c717c8d0-f529-3dd8-a0f0-222ba4dec258 | -2.9924 | -51.045 | 2024-11-13 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ada9939d-d3d1-3bf2-a286-fbdfdf06e0ee | -3.1096 | -54.3066 | 2024-11-13 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 9647a9a6-4be1-3796-bd89-7f4147969649 | -2.1271 | -50.6912 | 2024-11-13 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 6cb0979e-faa2-3759-a9a1-f6ccb8e74063 | -4.6581 | -47.4216 | 2024-11-13 01:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| bbd35f8c-639a-3549-934e-b163503b40ae | -5.3587 | -43.529 | 2024-11-13 01:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 693b472f-ee20-3fae-8ea4-314bea781f18 | -3.5743 | -53.0015 | 2024-11-13 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 1bda08f6-326e-32d3-9795-8fb9d1282afb | -3.0504 | -50.3332 | 2024-11-13 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 579e8df2-6965-3dba-ae1a-f5d0f878c8f4 | -3.7666 | -47.4855 | 2024-11-13 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| cb4c20b4-c650-320c-b940-09356398fd64 | -3.0689 | -50.3326 | 2024-11-13 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 0274721e-f9d6-3965-b92f-59c4f978fd11 | -2.2663 | -53.7422 | 2024-11-13 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 0fe62292-f31d-354a-adaa-af03553627a4 | 1.048 | -60.5986 | 2024-11-13 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.2 |
| e37bfec9-af92-365b-8f02-10b5cc57f158 | -2.2296 | -53.7429 | 2024-11-13 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 62ca7394-e28b-366d-9abc-14b4f408ecf5 | 1.0663 | -60.5985 | 2024-11-13 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 120.9 |
| b430da00-5072-3ea4-8952-52c2a495660d | -2.7033 | -49.33 | 2024-11-13 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d3c55eb1-9968-32b8-b0f9-7c74f95e789a | -2.2479 | -53.7627 | 2024-11-13 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| c55d1263-c7cd-37e9-9cc7-4b0031ace134 | -1.6627 | -52.5357 | 2024-11-13 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 714c1e8b-d243-3254-bd96-4676b52997c4 | -2.6848 | -49.3518 | 2024-11-13 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 94875152-8d9f-3633-a962-2c7f0a66a938 | -2.248 | -53.7426 | 2024-11-13 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| aff531b0-b315-37b4-a2ba-1bcdcc6d0fab | -4.658 | -47.4434 | 2024-11-13 01:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 2eac8d77-87ec-3186-8402-ddaa416f61c6 | -2.2112 | -53.7432 | 2024-11-13 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| ed3a4178-a612-3b5e-b4ec-c118347f5710 | 1.048 | -60.5986 | 2024-11-13 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 2df78842-da57-33a3-9c0e-1d6ccf290cc4 | -2.248 | -53.7426 | 2024-11-13 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| f1236136-5876-390f-a37a-5bf126d495dd | -1.6627 | -52.5357 | 2024-11-13 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 23921b5a-75d6-3039-8a59-f43888329391 | -2.2296 | -53.7429 | 2024-11-13 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| c7fb275f-e42e-33b9-8a55-06571a81741d | -1.6444 | -52.536 | 2024-11-13 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| b4ba0bcd-fa9b-3761-a421-0a0df86a0894 | -2.1581 | -46.398 | 2024-11-13 01:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 392c8190-ca04-372e-9900-884e753fdc7d | -4.6581 | -47.4216 | 2024-11-13 01:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 38793d47-8eef-3da7-9234-9c55d46b86a3 | -2.2663 | -53.7422 | 2024-11-13 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| bdef6ba3-038d-393b-9b5f-026cdb4152bb | -2.9924 | -51.045 | 2024-11-13 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| c30cf188-b29e-361d-b3eb-ad089daabf45 | 1.0663 | -60.5985 | 2024-11-13 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 33b160a6-ea9c-3fc4-8baa-26c6d41b3c57 | -3.9483 | -48.1724 | 2024-11-13 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| d0a5f017-2695-3d2a-abc6-e35c432232e0 | -4.6776 | -44.5861 | 2024-11-13 01:20:00 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| ea0f3928-88c4-3a03-95a5-7ac33305f305 | -3.0689 | -50.3326 | 2024-11-13 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 16c8a8e6-305e-30cf-ab68-814eb0f3bc86 | -4.6778 | -44.5633 | 2024-11-13 01:20:00 | GOES-16 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| f2a7ecc1-0b3e-336a-b658-e2c942677930 | -3.7666 | -47.4855 | 2024-11-13 01:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 77da9ba1-7826-384a-b9d6-41626459d231 | -2.1396 | -46.3984 | 2024-11-13 01:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| f7e4522d-cb53-32f6-b03b-0d1a9ad77dc5 | -4.658 | -47.4434 | 2024-11-13 01:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 1a665038-6655-34ef-877e-db8a927af648 | -3.2495 | -43.2547 | 2024-11-13 01:20:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 8866b18a-43f8-36bb-8f7b-f34becc81309 | -2.9925 | -51.0242 | 2024-11-13 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 95125156-1054-3783-9eb9-66d58b6041bf | -3.4913 | -50.8421 | 2024-11-13 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 0ba7506a-6b2e-3c82-8bda-61f1832e968f | -2.7033 | -49.33 | 2024-11-13 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 2c48c657-7e8d-3ec9-9ef5-f591f37caccf | -2.1271 | -50.6912 | 2024-11-13 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 2134c62f-2809-3671-9ab7-a00cb4c9dbb5 | -5.9587 | -39.6837 | 2024-11-13 01:20:00 | GOES-16 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 48.3 |
| 6f0d2ce6-2f81-302d-a0cb-ebeefb0cb750 | -2.2112 | -53.7432 | 2024-11-13 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a24fa37f-3bcb-3628-b261-c31b5babce6a | -2.1395 | -46.4206 | 2024-11-13 01:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| ece83c90-c3be-3c41-ad40-a02a5e0feef9 | -5.9398 | -39.6854 | 2024-11-13 01:20:00 | GOES-16 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 45.6 |
| df857f57-ce56-3ea6-9f41-018d5f71a369 | -2.158 | -46.4201 | 2024-11-13 01:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 8e94791d-a29c-35b7-bcca-6eea9854ed46 | 2.689 | -60.9608 | 2024-11-13 01:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 5b4caf72-3530-3c2e-942c-85054d195077 | -2.7033 | -49.3513 | 2024-11-13 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 9aa48bfa-0355-343f-b0d5-e18afe985c6d | 2.689 | -60.9797 | 2024-11-13 01:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.6 |


[Clique aqui para ver as próximas entradas](README9.md)
