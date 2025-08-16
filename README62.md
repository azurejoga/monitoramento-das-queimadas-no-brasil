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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a3bc8b3-2162-31d7-a265-91fa7797fed3 | -14.94002 | -54.69814 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 974a9a61-b0d5-3391-813e-b1f306a2b910 | -13.44228 | -56.68967 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c973ea9d-c6cb-39b6-b1b3-f8683c1994d7 | -11.35292 | -55.42529 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cc24904-de31-3cfd-85ae-357a604168f3 | -6.66593 | -58.82041 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 340e0e8a-e6a3-3055-bb72-4c232319ba1c | -13.11668 | -57.13946 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 519d45de-de2c-3e74-afb4-9dd7f16c391e | -13.44435 | -56.67414 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b37423cd-aed0-3885-bfe5-ad2e5dbf2a13 | -12.89036 | -62.09417 | 2025-08-16 05:25:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2328ff7d-2e12-38c0-9e13-c3b18d2ff285 | -6.08111 | -59.94493 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73febae8-b940-3d6d-bf9d-a25a7c159d95 | -13.12899 | -57.17029 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e995aa57-6063-3552-bfbe-2cacda65b05e | -10.09594 | -68.45704 | 2025-08-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8b929ac-9263-3cd4-9ebf-89a486089357 | -13.13302 | -57.17088 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08ce1c27-058b-3108-8e12-95c094f4a074 | -6.07894 | -59.95884 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b43bf9f-2a4e-336b-ae0f-1b712a1a32ee | -16.24859 | -51.12784 | 2025-08-16 05:25:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15eee679-590c-39df-abfd-07a4ac9e1122 | -10.40148 | -64.50344 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d78f5a9-8693-37d3-a5af-0c2ac7dc09e2 | -14.95562 | -54.7333 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 35f8789f-f80b-39d6-90c3-cde314bd2b66 | -15.97649 | -59.52034 | 2025-08-16 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62d7578b-9593-376b-afa7-cccb3f49eef7 | -13.47935 | -61.00198 | 2025-08-16 05:25:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ceda38f-ad78-3199-a7ce-d58568e504b6 | -5.45303 | -60.13493 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c62836f-cce1-3588-aaea-69929370fe00 | -11.34644 | -55.40661 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c947d275-84d5-3d99-accc-e70bed4552fa | -6.66251 | -58.81988 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99eee5f6-25fd-3b4c-b38d-140aaf7c2f5e | -6.66194 | -58.82361 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5a6f4b5-d1dc-3ae3-8461-0961b2d34bbf | -14.93786 | -54.75825 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c7838f73-5538-3358-b2aa-fb6aea6a34ab | -14.86648 | -60.09034 | 2025-08-16 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 26768419-8486-316e-b568-bd3f8efa22f6 | -14.93458 | -54.70232 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| eff9e2ca-7c00-30cb-b54b-4aeb2e8ee8ce | -13.4851 | -56.6561 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6778810f-b4d4-3719-bba7-cfb3c047d388 | -12.78595 | -60.15794 | 2025-08-16 05:25:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b28b9a5-4cc0-30d4-b186-23cc89978b82 | -6.14557 | -57.93532 | 2025-08-16 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44471e8e-f154-3a38-877f-676ab822dde4 | -5.57469 | -52.04963 | 2025-08-16 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6be0f029-009c-3a35-8f78-a1e7b5c699ad | -16.23661 | -51.12139 | 2025-08-16 05:25:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 407d7d1a-c7bd-349b-94d3-1e5c67320f16 | -11.36116 | -55.43082 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30a32a67-ffc4-344a-835e-2e9a830b8396 | -11.34737 | -55.43322 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e309ebe7-71cf-3055-b228-d89996e67586 | -16.22374 | -51.12384 | 2025-08-16 05:25:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6e04054-4788-3c12-8d03-6e62ebd584bf | -14.94532 | -54.7369 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 263cca37-90c7-3c47-bf72-38aef2ec88a6 | -13.43812 | -56.68904 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bc10a3a-bebc-3cf0-8e37-0ec37a7bc9c8 | -5.5696 | -52.04882 | 2025-08-16 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddc8ce37-857e-37ec-91c5-9a1204a6d336 | -13.12166 | -57.13292 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 801b562e-9a9e-3726-9c22-adce3b5be255 | -14.53089 | -48.57752 | 2025-08-16 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be1e3a88-28c7-3306-9405-450ffd5a5ab7 | -13.43863 | -56.68518 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9604ffe6-cb05-3a27-bec7-874c9ced235f | -14.93881 | -54.7084 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0b84993a-d7c1-33eb-8414-2b3b907e85ec | -14.86356 | -60.08575 | 2025-08-16 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e330b12-64d3-362d-b44c-ff31582b7beb | -6.1385 | -57.93428 | 2025-08-16 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e18e9b7-a67a-3a9e-a1e7-b6c0ee72b80a | -14.53257 | -48.59177 | 2025-08-16 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7aa30982-eb21-30b4-86c6-dc875b99a319 | -6.71163 | -58.81915 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04cb5679-d04d-3b85-9165-9d105e71686c | -11.36174 | -55.42649 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74c0638b-b4ee-30e5-909e-6c0efa63f7f3 | -9.53496 | -66.14682 | 2025-08-16 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d440ef07-2cd1-32ce-ae62-efacb50d3618 | -6.07508 | -59.96182 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45940ff8-af87-3d0a-8307-14e5fcd673b8 | -13.45894 | -56.66055 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a17ab1b-c01e-3bbb-b6e5-697db08ad365 | -13.00274 | -56.87444 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57de93b1-3445-3ad3-863e-cc124dad0ebc | -9.41377 | -68.55156 | 2025-08-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 311877ce-dd9c-3c8c-adbc-06991b6daafe | -6.65851 | -58.82308 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5d35a14-99be-34e7-bfa8-4a63215b234f | -9.91197 | -66.79141 | 2025-08-16 05:25:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fb93f45-7eb0-386e-8c92-5c993adfa77c | -12.13392 | -54.66759 | 2025-08-16 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abf5e7af-6808-3140-b761-0e20624673e0 | -6.70315 | -58.85218 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e15bf662-93e9-3858-a559-d6631ffab1fc | -16.22994 | -51.12491 | 2025-08-16 05:25:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b367c1d-fed0-3e86-84bc-49866eb80fb2 | -13.43915 | -56.68132 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d829985c-1b21-3c29-b081-fb8875ff7ec7 | -10.47827 | -61.31713 | 2025-08-16 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46b0f6c3-5f30-35f2-a59f-1a2b382a2a19 | -10.67078 | -60.77415 | 2025-08-16 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c8a0f60-2c2f-3968-976e-e9b93caa3f47 | -13.12118 | -57.13652 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e0100e7b-7be1-3dd2-b476-0a4390676e76 | -6.13203 | -57.9293 | 2025-08-16 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0fe7527-30e3-3fc7-a5a5-4271f830f1e0 | -13.4799 | -60.99833 | 2025-08-16 05:25:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e35db19-5796-302e-8c32-04ca99982436 | -6.70764 | -58.82238 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c202181b-995d-370a-9647-ae6e32f5e154 | -6.07562 | -59.95834 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c9bfe35-9678-396a-bf02-04c91c4591b5 | -13.4355 | -56.67679 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 618ad277-1ff4-3377-90d0-99afb6de7073 | -6.44354 | -58.25922 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa011ecc-08b3-3222-96a9-3b8515c62008 | -6.6968 | -58.82455 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbb1e080-858e-3286-a265-bddb6210ca82 | -12.29692 | -50.00858 | 2025-08-16 05:25:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf3ca110-0b08-3379-be7f-aaa1d381d017 | -16.24327 | -51.11798 | 2025-08-16 05:25:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1eca5983-2c0d-3dc7-b2f2-73c986934642 | -13.44383 | -56.67805 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0ff2c6f-d5e1-3f88-bb8a-380f6bd50f70 | -5.45026 | -60.13096 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7828c81-6477-325d-baf6-9bdd30f0307b | -6.64613 | -59.08524 | 2025-08-16 05:25:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63a1dd84-5d0e-30d3-aa78-34c28e36e83d | -10.47496 | -61.3166 | 2025-08-16 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37f87cfd-8a66-3ece-ae06-ad91f8a676dc | -14.95017 | -54.73767 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 8a1c9464-abcf-384f-b574-8665b1518f27 | -11.35085 | -55.40725 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4446115-e521-3382-9c6e-ff575bca64cc | -14.96581 | -54.73079 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d13d48d8-8c9b-389c-a7f7-96c06648823d | -13.1257 | -57.13347 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14cc064f-f3b8-3eb5-a2d3-a8b6ca1d3a55 | -11.35467 | -55.41227 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76c9b319-05b5-35e4-a8f3-429af95e390e | -13.138 | -57.16433 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7847bf73-20da-3d16-ae73-6748c4016dfb | -14.94759 | -54.75937 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 484aa0bd-37cd-33d6-8c46-bfe9c4ef79a5 | -7.53159 | -50.52671 | 2025-08-16 05:25:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b306520-0f19-3f2e-b19d-15debc9e1984 | -11.66003 | -51.62535 | 2025-08-16 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22202c6a-a4aa-32ff-853a-c79a7be4f400 | -14.53024 | -48.58456 | 2025-08-16 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e4a1aa1-8603-3b6c-b2bc-7d28a7808a77 | -13.12995 | -57.16316 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f43b3663-0f57-3dde-9ea0-e2bded114e24 | -26.10629 | -53.34409 | 2025-08-16 05:27:00 | NOAA-21 | MANFRINÓPOLIS | PARANÁ | Brasil | 4114351 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 59c4ea86-b5b0-3eab-8eee-6d320da736a9 | -23.67997 | -51.64458 | 2025-08-16 05:27:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 850d00a7-4478-3071-a673-735968b7c285 | -23.68636 | -51.65252 | 2025-08-16 05:27:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 27e6c537-dd79-362d-b702-57bb09628e30 | -24.92042 | -52.36443 | 2025-08-16 05:27:00 | NOAA-21 | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f11b0185-a4e4-33a0-8bc2-bdb2dec9a3f9 | -23.68024 | -51.64633 | 2025-08-16 05:27:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 8ceac5af-b2fc-3a6d-a708-f7c8cf9f6d2c | -21.06138 | -50.30596 | 2025-08-16 05:27:00 | NOAA-21 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d4632685-e680-30e4-8c3a-22d248b1f80a | -23.68678 | -51.64677 | 2025-08-16 05:27:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 401a539e-0142-3fb1-b5e7-ba7ab5dbb95c | -23.67983 | -51.65195 | 2025-08-16 05:27:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| a8afab44-6383-3dc5-9589-6e687b67ce2d | -23.68613 | -51.65075 | 2025-08-16 05:27:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 69c0dd13-e94d-3b41-85b4-18ac563347e3 | -21.06068 | -50.30572 | 2025-08-16 05:27:00 | NOAA-21 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9ebfeb82-cdc7-3d59-9297-d0f298f638f9 | -23.68575 | -51.65646 | 2025-08-16 05:27:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| d2794849-c144-3838-947d-62347ec7eaf3 | -20.1358 | -54.42519 | 2025-08-16 05:27:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80d5c36c-7a2c-3977-ae43-53ef7b0c7bd2 | -23.67959 | -51.6502 | 2025-08-16 05:27:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 054c3784-cf17-3da0-984f-8f10a1576ce2 | -21.06759 | -50.306 | 2025-08-16 05:27:00 | NOAA-21 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c7f66b52-80ec-3664-afb3-60e174f02e28 | -29.39472 | -50.48207 | 2025-08-16 05:29:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 44c6fc24-6491-335c-b02e-937e73c0a4e3 | -8.9893 | -61.7024 | 2025-08-16 05:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 39.3 |
| ec423446-c4ed-36c9-ad97-56daf7eaf6f2 | -8.9892 | -61.7215 | 2025-08-16 05:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 1d3c7fed-b2b4-3a19-b91d-d33e8e494545 | -7.4983 | -63.8199 | 2025-08-16 05:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |


[Clique aqui para ver as próximas entradas](README63.md)
