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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51c80aa0-f716-3638-bdfe-074d0ff04d5a | 1.94171 | -60.85477 | 2024-11-13 01:43:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e9ef8d93-6c45-3eb8-9b75-2f886c7e015e | -1.88185 | -54.21029 | 2024-11-13 01:43:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| f549f01b-4d83-356b-b98d-a5c85958834f | -3.12647 | -59.01593 | 2024-11-13 01:43:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 674c1756-7690-3357-988e-c029bd08e3d1 | 2.69162 | -60.96992 | 2024-11-13 01:43:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3ead5012-3afa-3ad5-883b-5fad19515b8c | -1.52195 | -54.99282 | 2024-11-13 01:43:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9c749870-b641-39e3-99d5-0a3486dbca09 | -3.15527 | -59.15361 | 2024-11-13 01:43:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 84020821-04fb-30ef-8539-a966cebff7ca | 1.11307 | -59.18966 | 2024-11-13 01:43:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9cbd5d1c-318c-3914-abd7-cf1ba604d08a | 1.05623 | -60.59645 | 2024-11-13 01:43:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 1d2663c9-5717-3422-949b-29beafdf0d24 | -2.40197 | -53.73529 | 2024-11-13 01:43:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 105e3cb3-cc46-3ab3-b3cf-74a74bee74ce | -2.2078 | -53.75414 | 2024-11-13 01:43:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| aa3d738b-5e28-3501-96ae-e7e6235716c9 | -1.77079 | -55.62306 | 2024-11-13 01:43:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a8235504-f260-3527-a63b-a8e79cb4864c | -2.25104 | -53.77005 | 2024-11-13 01:43:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| bdd004ce-0953-3b8b-9945-bb38e202a411 | -2.20464 | -53.73273 | 2024-11-13 01:43:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 891ae445-41ec-3756-9d74-34bcc5ac23bb | 1.06389 | -60.60661 | 2024-11-13 01:43:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| be7e4e6a-e0e1-3b56-a02c-fd9ccc8ee403 | -1.88065 | -54.1967 | 2024-11-13 01:43:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| f28ef5ed-5db4-357d-89e9-a891e2f3f577 | -2.24793 | -53.74852 | 2024-11-13 01:43:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| d6d07f8f-df8a-3635-8dc9-990159fdd9d1 | 2.67105 | -61.18423 | 2024-11-13 01:43:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 90153d78-079e-339b-a326-2764428c9fe0 | -2.68471 | -57.37463 | 2024-11-13 01:43:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fca4b2e3-0761-3945-a09b-2655b45d4d67 | 1.06513 | -60.5977 | 2024-11-13 01:43:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2ed614c9-a3a3-384a-b2fc-624618e809e3 | -1.76853 | -55.6072 | 2024-11-13 01:43:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2ade2268-e971-3baa-88c6-291ab0c5f0d3 | 1.05499 | -60.60535 | 2024-11-13 01:43:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.3 |
| dbeda18b-2f9d-3cb4-aa2d-27e83bc184ca | -1.88347 | -54.21672 | 2024-11-13 01:43:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| f3c74ec8-37c2-39e0-88cb-3bd4636e5a6e | 3.16584 | -60.66661 | 2024-11-13 01:43:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf904f58-bf12-31f0-831e-0ce2bb31d1da | -2.69468 | -57.37321 | 2024-11-13 01:43:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a36aa78c-460e-3a4b-989b-1d0ce676a1b0 | -1.42073 | -53.4824 | 2024-11-13 01:43:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 32641072-442e-3130-b622-1a21b1433414 | 1.05375 | -60.61426 | 2024-11-13 01:43:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6cd974eb-0168-3832-baf0-d508adc51c0c | 1.13939 | -60.59631 | 2024-11-13 01:43:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c91b1935-8592-38c8-b7c0-53757723c413 | 2.67227 | -61.1754 | 2024-11-13 01:43:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 61415947-394b-3071-9085-dbed61ddab72 | 1.0486 | -60.607201 | 2024-11-13 01:49:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| be51c65f-773e-3000-a04c-3e7895cddcf0 | 1.0714 | -60.597401 | 2024-11-13 01:49:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9c7972f1-f81b-39d0-b19c-0c569a926127 | 1.0681 | -60.611599 | 2024-11-13 01:49:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d6ad66d1-961a-382c-88fa-3a854fb78488 | -6.79 | -58.792 | 2024-11-13 01:49:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f83d0ba8-ade8-3353-80e9-cb37a0e88392 | 1.0551 | -60.6236 | 2024-11-13 01:49:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 13af0420-7f8d-3f02-a012-aeb26f11d33b | 1.0519 | -60.592999 | 2024-11-13 01:49:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dec06f07-7fbf-31ed-8ced-86f08d0c5607 | 1.0584 | -60.609402 | 2024-11-13 01:49:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 102a9c48-39a8-33d5-aca1-a8ad374df1ab | 1.0617 | -60.5952 | 2024-11-13 01:49:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 33e170b5-5ab4-3305-8f41-88dda9d69868 | -2.9925 | -51.0242 | 2024-11-13 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| edf26c98-81c7-3493-8e0e-41850c4fda93 | -2.1396 | -46.3984 | 2024-11-13 01:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 7c4165b6-ee07-375d-b363-ae456ba56d12 | -3.1096 | -54.3066 | 2024-11-13 01:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| acbc0aac-d9df-334c-be3c-f764c935140a | -2.2112 | -53.7432 | 2024-11-13 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 577ae79d-6736-3ed5-8142-7232369f8591 | -3.7666 | -47.4855 | 2024-11-13 01:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 908ec75c-c5e9-3f9a-a132-431e03305fc6 | -2.158 | -46.4201 | 2024-11-13 01:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 213488b0-22d9-3c34-8921-6f35903c82e2 | -3.3519 | -48.9475 | 2024-11-13 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 9de091bb-eaa1-3e82-9e43-5f419ced421e | -2.7033 | -49.3513 | 2024-11-13 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 63d2b86a-181b-3e48-9723-8f261c26177f | -1.6444 | -52.536 | 2024-11-13 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 481f6b2c-3e42-3ad8-8b65-d57c93f54848 | -2.248 | -53.7426 | 2024-11-13 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 6ef7abe8-43e0-3b88-a56b-c88ee7fd176e | -2.1395 | -46.4206 | 2024-11-13 01:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| a76a1a63-ed88-3585-8a53-da8ba956833a | -10.7425 | -49.5244 | 2024-11-13 01:50:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| daffa270-d04f-32ce-87ea-318dfe866caf | -1.6627 | -52.5357 | 2024-11-13 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 25b9810d-dc1f-3dcb-aa75-69d3431a4acd | -2.7033 | -49.33 | 2024-11-13 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| f9b039fd-8b33-3287-b436-99a945af5083 | -10.7235 | -49.5265 | 2024-11-13 01:50:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| b3e121e4-9d23-37ba-8077-d73a569e97e9 | -2.9924 | -51.045 | 2024-11-13 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 52f91af9-3383-3fb2-8ef2-f2a7c5f21c65 | 1.048 | -60.5986 | 2024-11-13 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 2915c784-3543-3e35-b35f-9f1c5e1616e3 | -2.1581 | -46.398 | 2024-11-13 01:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 305b0cb2-f2af-3665-9d08-ca8f60866ae4 | -2.2479 | -53.7627 | 2024-11-13 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b24a42a6-1f9b-35e0-8306-cb769879fcc5 | -1.6443 | -52.5564 | 2024-11-13 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ab726a6f-efc5-3bc9-894f-9d316d24e168 | -5.3587 | -43.529 | 2024-11-13 01:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 254848c3-3e75-3573-97eb-21b6bcec40bd | -10.7428 | -49.5028 | 2024-11-13 01:50:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| d14186c6-101b-3707-a360-71b63b9ebba7 | 1.0663 | -60.5985 | 2024-11-13 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 2e058fde-442d-378b-842a-863825f950c9 | -4.6581 | -47.4216 | 2024-11-13 01:50:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| d3e243cd-f5c1-34b8-900a-f7e2faaa030a | -1.6627 | -52.5561 | 2024-11-13 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 4c11d2cc-f267-398b-9bf3-41e9ec91d929 | 1.0663 | -60.5985 | 2024-11-13 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.8 |
| be36bbdd-d0e2-35f0-9d24-b241880d1fca | -3.5098 | -50.8415 | 2024-11-13 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| c31a3a3c-9b86-3db9-a724-d7c8a4527817 | 1.048 | -60.5986 | 2024-11-13 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 44d025d6-2dad-3d1c-b3ac-9e7ca5cc5e40 | -2.248 | -53.7426 | 2024-11-13 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 11ac6655-4254-30e5-b83f-207283d18e27 | -3.9483 | -48.1724 | 2024-11-13 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 06d59ef0-a525-34e9-8cee-71fb9776c5d3 | -2.1396 | -46.3984 | 2024-11-13 02:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 92cd1835-a706-3053-bc25-22aca5b4648c | -2.1395 | -46.4206 | 2024-11-13 02:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 2d75851c-495c-3033-913f-784de290ffe1 | -10.7428 | -49.5028 | 2024-11-13 02:00:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 30ab780a-5846-3974-9c67-ac22c3fc5698 | -2.2479 | -53.7627 | 2024-11-13 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| c87b9db7-a329-31ee-9097-8a3975832435 | -4.658 | -47.4434 | 2024-11-13 02:00:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| db50d303-f362-34a7-8239-eeabe27f29b1 | -10.7235 | -49.5265 | 2024-11-13 02:00:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 416f94a9-5791-30ff-a80a-a86ce3554788 | -3.0504 | -50.3332 | 2024-11-13 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| fa74382c-0e42-3b40-8528-4c971af593a1 | -10.7425 | -49.5244 | 2024-11-13 02:00:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 6cb0fd77-ab6e-3bcc-b4f1-a6e6143e4433 | -1.6627 | -52.5357 | 2024-11-13 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| a806a807-3991-3707-a445-fa03feb74611 | -1.6627 | -52.5561 | 2024-11-13 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d3e96dd7-14a5-3bfd-86a9-1957507bae82 | -1.6444 | -52.536 | 2024-11-13 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 21d0db85-dcd2-3a68-8d67-b6f5628e9c52 | -2.1581 | -46.398 | 2024-11-13 02:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d71a3a49-55eb-3004-ad0c-1f057bd9f745 | -2.9925 | -51.0242 | 2024-11-13 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 62518003-7650-3c10-88fc-d787f41a6ed7 | -4.6776 | -44.5861 | 2024-11-13 02:00:00 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 3f7fc1f9-2fbf-3005-9c3c-d4f215ef11f7 | -4.6581 | -47.4216 | 2024-11-13 02:00:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 19668c17-29fd-3d11-82ee-ea52358609e1 | 1.048 | -60.5986 | 2024-11-13 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 7f0be245-496e-38f9-8e13-505815e1a374 | -2.2479 | -53.7627 | 2024-11-13 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e33aae52-ed7b-389b-a885-4e5d7ba196b7 | -1.6627 | -52.5561 | 2024-11-13 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| a4ed2139-e55d-383b-8ba3-de13a1edca19 | -2.9925 | -51.0242 | 2024-11-13 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 8569a2ed-ff33-3941-b30a-48d758ea62a2 | -4.6581 | -47.4216 | 2024-11-13 02:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 9244e339-3001-37fd-8098-3ddeeffb7484 | -2.9924 | -51.045 | 2024-11-13 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 1a689af9-e71f-34bf-8a75-faa2fd454b25 | -4.658 | -47.4434 | 2024-11-13 02:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 53d26c8a-886a-3fa4-9ae8-d4d9298e43c9 | 1.0663 | -60.5985 | 2024-11-13 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.4 |
| c6158eac-8ef0-3128-97f9-fff3344693eb | -10.7235 | -49.5265 | 2024-11-13 02:10:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 3fafd173-c11c-3148-b981-27f708efd977 | -3.9483 | -48.1724 | 2024-11-13 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| d0e51942-36e6-353c-a8ee-862ae1a1c67e | -2.1396 | -46.3984 | 2024-11-13 02:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 1d34c2aa-8803-344d-adfb-f63b994eda8e | -2.7033 | -49.3513 | 2024-11-13 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| cf9c831b-290f-351c-88ce-04d79002b97c | -1.6444 | -52.536 | 2024-11-13 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| fb66a0b0-96a9-3e16-9dc1-c03177142d88 | -1.6627 | -52.5357 | 2024-11-13 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 0896280b-d460-32e1-ad85-3295981adf6d | -10.7425 | -49.5244 | 2024-11-13 02:10:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 05777d34-3f58-3176-a682-143e21b7e60c | -1.6443 | -52.5564 | 2024-11-13 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 51b22c31-7465-3849-a734-b5710f3336ef | 2.689 | -60.9608 | 2024-11-13 02:10:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 35.3 |
| b7d0f532-e5eb-323f-b92c-9e58a26efd42 | -2.248 | -53.7426 | 2024-11-13 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| cb16a521-d95d-3f43-b819-febe04fae399 | -4.6581 | -47.4216 | 2024-11-13 02:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |


[Clique aqui para ver as próximas entradas](README11.md)
