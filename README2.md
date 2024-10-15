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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b3325bf-b97e-34cd-86d4-7866d90705e4 | -13.2609 | -41.951401 | 2024-10-15 00:15:01 | METOP-C | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| af1545bd-5c90-374d-967a-1f90faf16176 | -14.0956 | -46.170898 | 2024-10-15 00:15:02 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d633ce4-a07a-3b91-a461-f3edda26edfc | -14.0986 | -46.185902 | 2024-10-15 00:15:02 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a88f63ec-547a-33a7-b232-81bb7439f4f0 | -14.083 | -46.158001 | 2024-10-15 00:15:02 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cb463be0-45ce-3a88-8419-d4ab3624c8bf | -14.0859 | -46.172901 | 2024-10-15 00:15:02 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0205e88d-05b7-36d6-9a2e-34702b26d318 | -14.0889 | -46.187901 | 2024-10-15 00:15:02 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 93a22043-c937-36da-b8e9-5c56c8d2d74c | -1.5309 | -54.3559 | 2024-10-15 00:15:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| cca1bced-78d5-38e2-8433-4c9d8a46c0c6 | -1.531 | -54.3359 | 2024-10-15 00:15:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 3167c302-7bd2-3f45-b802-cb73b64ad050 | -1.5493 | -54.3357 | 2024-10-15 00:15:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| f4845215-ae80-3d65-8510-4ef5f6ae04bd | -1.8762 | -47.8272 | 2024-10-15 00:15:16 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| cfbbce22-474c-3b8c-bd93-276fd4b6213b | -2.4418 | -50.2447 | 2024-10-15 00:15:20 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 0cf2541a-ec8c-37e9-86d5-2fe90051b568 | -2.4419 | -50.2237 | 2024-10-15 00:15:20 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 729d9d7e-c541-3665-bd3f-b532c2496e3f | -2.5027 | -48.567 | 2024-10-15 00:15:20 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 1e2c8ebd-09e4-3c59-b15b-e2249ede77ea | -2.5028 | -48.5455 | 2024-10-15 00:15:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d7d5144a-319a-3fc0-ba3a-fcf7897acf49 | -2.6496 | -54.6172 | 2024-10-15 00:15:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| b7e00405-4bbb-3bdb-b5b4-9b246eef4c49 | -3.0397 | -53.2603 | 2024-10-15 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 9a056122-fce1-3a50-b1fb-914f48a7b7d4 | -3.0581 | -53.2598 | 2024-10-15 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 4bee52f5-f653-30bc-9aae-788044557d00 | -3.1099 | -54.2263 | 2024-10-15 00:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| d348d5bb-305c-3d7b-80f9-4d709d850afe | -3.1282 | -54.2459 | 2024-10-15 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| d0e4d898-2322-37f5-b954-815222fdc3c8 | -3.1283 | -54.2259 | 2024-10-15 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 8c6c02db-f919-32aa-852c-5df0a4cb0f7d | -3.4408 | -49.7308 | 2024-10-15 00:15:25 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 1f894d30-0d57-3b82-9ff1-c0d8887d56a7 | -3.4883 | -51.5483 | 2024-10-15 00:15:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| bc9fa73a-5a28-3a30-a147-f0b5c32b90bd | -3.7218 | -48.9979 | 2024-10-15 00:15:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 3222c88d-6eac-31a5-b25f-7441d3288834 | -3.7219 | -48.9766 | 2024-10-15 00:15:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 1cea30b6-c8ff-3225-bad0-9e9611cabb29 | -3.7403 | -48.9972 | 2024-10-15 00:15:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 193.9 |
| 7c1e6456-5b44-3dc2-b001-d6ffcd357249 | -3.7404 | -48.9758 | 2024-10-15 00:15:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| ead7f3ae-7948-3841-93f3-3510f4cccb48 | -3.8199 | -55.9977 | 2024-10-15 00:15:28 | GOES-16 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 948014a7-4b7a-352a-9c3e-5d42b821d861 | -4.3774 | -47.7627 | 2024-10-15 00:15:31 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| f803a759-3feb-3000-829e-bf6f6ee1153e | -4.3959 | -47.7618 | 2024-10-15 00:15:31 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| d62f943c-8760-34f5-8a19-d37fad0d7e5d | -14.0732 | -46.159901 | 2024-10-15 00:15:31 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be5db5c3-34fb-384b-8c52-8ac026e1da88 | -14.0761 | -46.174801 | 2024-10-15 00:15:31 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 18b8313d-3c45-3ae2-9be7-89707c5bb228 | -14.0791 | -46.1898 | 2024-10-15 00:15:31 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 595eb2fe-71a7-3ef4-94b6-56283faffa40 | -14.082 | -46.2048 | 2024-10-15 00:15:31 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b6db3857-1e57-3971-885b-dbfacdfd75ea | -14.0634 | -46.1619 | 2024-10-15 00:15:31 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e67869f1-1894-30ca-bdbf-3a6be171e3fc | -14.0663 | -46.1768 | 2024-10-15 00:15:31 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8938c655-e45e-3dd5-a117-23b1e9d58ce6 | -14.0693 | -46.191799 | 2024-10-15 00:15:31 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b77817bf-9f7c-3f80-898c-a3d058fcce73 | -4.7224 | -46.1608 | 2024-10-15 00:15:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 0011ec14-d4c9-3191-9a42-9e824a13f70c | -13.1886 | -42.477299 | 2024-10-15 00:15:33 | METOP-C | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6a84ff28-bd34-3c80-86e7-e30030c7a346 | -13.1904 | -42.486 | 2024-10-15 00:15:33 | METOP-C | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 436163ee-ca1a-3ae9-9041-566f5f6a2913 | -5.2261 | -43.7238 | 2024-10-15 00:15:35 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 50fdfa7c-4c31-396a-b221-d12e9182a869 | -5.1983 | -44.8497 | 2024-10-15 00:15:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 0652fe00-fb0b-3c2b-b061-bac808d21aff | -5.217 | -44.8485 | 2024-10-15 00:15:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 171.7 |
| b9d8dbf5-5ae1-3774-abdf-1f04b1d6d459 | -5.2982 | -46.3936 | 2024-10-15 00:15:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 40a0a679-affc-3167-8a97-84e8c7a74bf2 | -5.5356 | -44.7359 | 2024-10-15 00:15:37 | GOES-16 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 90ed63a7-05e8-3c47-81ac-f4e251fd2309 | -5.5358 | -44.7131 | 2024-10-15 00:15:37 | GOES-16 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4e7b5718-f4d5-3408-bc06-6c82cce6dba1 | -5.5543 | -44.7346 | 2024-10-15 00:15:37 | GOES-16 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| cb854cb2-2bfd-3028-809e-35847b1d167a | -5.5545 | -44.7118 | 2024-10-15 00:15:37 | GOES-16 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 2452ec87-d2ae-3f8d-a8e0-a9a837541ddd | -6.4268 | -49.6028 | 2024-10-15 00:15:42 | GOES-16 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| ba0157e3-01ad-3821-9558-dbeef9c2db4e | -6.5505 | -48.2408 | 2024-10-15 00:15:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 2153e811-035d-34aa-8676-d23124ee31e4 | -6.5691 | -48.2395 | 2024-10-15 00:15:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b6cc75cf-0cb2-3d81-a27c-74c757dcfc69 | -6.6325 | -60.0416 | 2024-10-15 00:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 2ff533ec-12bc-34b5-b2cf-1491848b3b6a | -6.6326 | -60.0224 | 2024-10-15 00:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| cc5ae067-2033-378b-81d6-1bd09ef90a8d | -6.6511 | -60.0026 | 2024-10-15 00:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| fbe68ab2-490c-3839-9ad3-a18e26bbd6c9 | -6.7285 | -59.3267 | 2024-10-15 00:15:44 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 2f72c524-9bf2-34cb-9409-69e00401598e | -12.8664 | -44.602901 | 2024-10-15 00:15:46 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3b15a535-096b-30ec-b9a1-b764153f93a2 | -12.8687 | -44.614201 | 2024-10-15 00:15:46 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 518879f0-f736-390c-8d28-5e82367f8a84 | -12.8566 | -44.6049 | 2024-10-15 00:15:46 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e156322-0484-34c6-b336-dc561daa9b34 | -12.8589 | -44.616199 | 2024-10-15 00:15:46 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e3150580-8c18-315f-9575-aef68e92b48b | -12.373 | -42.735699 | 2024-10-15 00:15:47 | METOP-C | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cf34100a-e031-350e-b97d-3c837b669b29 | -12.3749 | -42.7444 | 2024-10-15 00:15:47 | METOP-C | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ceb60a1f-c978-3771-b8c3-de5a8a91bd33 | -7.528 | -49.4817 | 2024-10-15 00:15:48 | GOES-16 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 793b1a3a-f70e-32b9-9cca-bf82a83240cc | -13.5923 | -49.777 | 2024-10-15 00:15:50 | METOP-C | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1fe2ede7-d2a1-3a3e-9697-e237e57713aa | -13.5827 | -49.778801 | 2024-10-15 00:15:51 | METOP-C | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6d4db472-6d94-3353-860c-6c486d013490 | -8.4639 | -47.822 | 2024-10-15 00:15:54 | GOES-16 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8a8b3fe2-4dc1-3c3e-bd15-9e836a3ae59d | -8.4642 | -47.8 | 2024-10-15 00:15:54 | GOES-16 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 4d3f05f7-6056-3146-80d3-8a472dd11642 | -12.0941 | -43.205299 | 2024-10-15 00:15:54 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cbdd74de-1364-3f4f-a129-89ac4f56f2b3 | -8.9141 | -47.9103 | 2024-10-15 00:15:56 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 380161d0-c330-32ff-8cf4-793d994a426e | -12.0764 | -43.8955 | 2024-10-15 00:15:56 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 074bb5fc-846a-3119-ac6b-124086bfb4d4 | -12.0841 | -43.8834 | 2024-10-15 00:15:56 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9125a750-4993-3bdc-9f11-ec9d36ea3f88 | -12.0862 | -43.893398 | 2024-10-15 00:15:56 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd0612e4-9777-3492-a0fe-723913abc6f9 | -12.0722 | -43.875599 | 2024-10-15 00:15:56 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db74d74e-1daf-3335-b577-4f54db35c627 | -12.0743 | -43.885502 | 2024-10-15 00:15:56 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0816a1c5-8fbc-3c14-827b-a1a2a0a26671 | -9.0852 | -47.7836 | 2024-10-15 00:15:57 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 9c52e2a0-7f60-33cd-b3c1-3101fec0523c | -9.2549 | -60.8863 | 2024-10-15 00:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 5f6e2885-aa8b-3f2c-a916-945c160c06c2 | -9.3493 | -63.5846 | 2024-10-15 00:15:59 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 5bf68541-97f9-3bfa-b946-5e080d0e4920 | -9.3494 | -63.5658 | 2024-10-15 00:15:59 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 014f549b-0354-33d6-820d-b6e2fb530d37 | -11.883 | -43.802601 | 2024-10-15 00:15:59 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2259aa64-9ec4-34f9-ad86-11cf3d0a95ed | -11.8851 | -43.812401 | 2024-10-15 00:15:59 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ca5f4dc-9353-3020-8d1d-ac1bc0d0bcd1 | -11.8871 | -43.822201 | 2024-10-15 00:15:59 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96883d75-2e1d-3124-8e44-fa042255d377 | -11.8732 | -43.8046 | 2024-10-15 00:15:59 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4ef28948-5d10-3e07-b496-580650dc9e21 | -11.8753 | -43.8144 | 2024-10-15 00:15:59 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6a8bef28-8a7c-3cc4-8403-7f39fa375206 | -11.8773 | -43.8242 | 2024-10-15 00:15:59 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7f4a268-806d-3308-b6dc-29399955f709 | -9.6878 | -46.476 | 2024-10-15 00:16:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 9b17688c-19b2-3814-bbd7-cb180c2877c4 | -10.0409 | -36.395 | 2024-10-15 00:16:02 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 6bf18c66-7201-3f2c-ada1-73e2a9e2c71b | -10.045 | -36.411999 | 2024-10-15 00:16:02 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 5b206d5c-e218-3ae3-97a7-fc3478b00fde | -10.043 | -36.4035 | 2024-10-15 00:16:02 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 00f3249e-3ae3-3209-9a92-c9bb322f6fc6 | -10.0495 | -47.6589 | 2024-10-15 00:16:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 15f03399-1141-39f0-ab98-bfcdb3303096 | -10.0227 | -54.3457 | 2024-10-15 00:16:03 | GOES-16 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 8df53b1f-2c9a-3eb2-97ba-d6e93deeee55 | -10.0415 | -54.3442 | 2024-10-15 00:16:03 | GOES-16 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 0e9334e4-f041-3935-aa2d-f87276b2885d | -10.0417 | -54.3238 | 2024-10-15 00:16:03 | GOES-16 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e84fa842-1127-3828-8b31-a4ccb76e8120 | -10.1447 | -46.3102 | 2024-10-15 00:16:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 2f9e83ec-53c9-3abf-8393-27d589fbad33 | -10.164 | -46.2853 | 2024-10-15 00:16:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| e65239fe-5a54-317d-9766-977d659fb6a0 | -10.3954 | -44.8206 | 2024-10-15 00:16:04 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c8d0d7a8-a10c-39ef-ae63-0332ca31cad8 | -10.3524 | -61.1946 | 2024-10-15 00:16:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| ad06a64d-28e7-322c-9061-1ef46f829efb | -10.3711 | -61.1935 | 2024-10-15 00:16:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 229.2 |
| 0653eb19-e208-3b55-a9bf-63e05604633c | -10.3713 | -61.1743 | 2024-10-15 00:16:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 770573ca-be0a-3d96-9623-1c8ac6f3dfa6 | -10.3898 | -61.1925 | 2024-10-15 00:16:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 1a299469-95e1-3c66-94f0-7b2ca57bbe51 | -10.822 | -49.256 | 2024-10-15 00:16:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 3b3625ec-a7b5-3cd1-a5f9-65002d02a770 | -10.8224 | -49.2343 | 2024-10-15 00:16:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| c16ddded-fedb-3148-8c49-2648abfb30fc | -10.841 | -49.2539 | 2024-10-15 00:16:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |


[Clique aqui para ver as próximas entradas](README3.md)
