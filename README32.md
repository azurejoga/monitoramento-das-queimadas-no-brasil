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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 199a0565-a031-3118-b440-1864c22aaaf2 | -3.48653 | -44.57726 | 2024-11-27 04:18:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7927e889-9b37-32fd-89e7-668969919b4b | -3.15445 | -49.24328 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76c62124-2664-341a-8734-b749c0f00fe7 | -1.79399 | -52.73969 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a228614-5615-3a13-a219-902657a79867 | -3.38175 | -45.85154 | 2024-11-27 04:18:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40d6c7cf-3f4b-3f06-a3ee-1c9187211533 | -3.88497 | -43.15976 | 2024-11-27 04:18:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1950cc5d-b376-3be0-82fd-35bce04fb76b | -3.8974 | -50.11104 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2332cd61-6217-346e-a861-39582d7e5f60 | -4.14916 | -43.80653 | 2024-11-27 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ead67353-b5c0-3900-a8ac-cdee9b30ea36 | -4.30855 | -48.08424 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8cd6a689-28f1-3349-bfd3-07379376d0f1 | -2.32205 | -46.11723 | 2024-11-27 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a8b4968-7a1c-39c9-82e7-22d69e8e872b | -3.28505 | -51.15675 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2154f5fc-3858-3410-9b51-d1999f3bbb13 | -3.6855 | -50.22549 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c16f97bf-6f3a-3e59-9f9d-007da2b267ae | -1.7988 | -52.74396 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5b5b606-8d5f-3e3c-b7ad-14b3ee47e34d | -2.42438 | -48.54609 | 2024-11-27 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ce0aa24-b77e-3d58-abad-64818a249731 | -2.94012 | -49.1299 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9cfc235-3124-3be1-9cfe-be68dbb0b8a5 | -4.49988 | -46.59807 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac139913-5604-3573-9d69-7d0ebdcfb082 | -2.9337 | -48.63371 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3327ba18-78e0-3f69-b58b-69ec2ae8f7ab | -1.9897 | -53.29525 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f589e03d-d8a5-3d06-ab0b-56fa9b368bcd | -2.80229 | -54.13306 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7fd5ab3d-8472-38f4-8737-dce4951a11f2 | -3.23473 | -50.17949 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f3b8639-0761-3b0b-bf7d-9728c145ce72 | -2.93724 | -48.01895 | 2024-11-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77fa6193-7c0e-3922-8578-cf4d9b0a41f9 | -3.97171 | -48.08959 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 63108ace-f837-3f9e-9603-0eb338da6cf7 | -3.93964 | -46.89314 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4bad834a-e483-3f98-bafd-f475b6f140f2 | -3.3356 | -46.68023 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c8411952-8fd7-3cb0-a54e-a6bc154e585b | -3.53878 | -44.92986 | 2024-11-27 04:18:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51dd1340-0964-3e35-8765-c2f2c50123c5 | -2.83464 | -54.11767 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ddbd6c66-a402-39e5-965f-2a2ed77d527f | -4.66112 | -45.04121 | 2024-11-27 04:18:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34ac2133-a435-34e8-ae8c-7f6e21d91cf9 | -2.57392 | -49.09138 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6f5c803-907f-3711-9682-b25c1c7de17f | -4.18047 | -48.62436 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a81b98ab-53e5-3f94-8e47-4400eea7ad38 | -3.26968 | -50.62307 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cb32aed-4788-3b34-aaa1-83a48131be18 | -3.45894 | -50.8396 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2f262bd-f166-3df3-947b-9b768f7e09ed | -2.83692 | -46.82709 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 302c7c4d-bf06-34a1-9659-3b33ed414df1 | -3.10967 | -53.26424 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 704c9372-68bf-3f73-9e62-d4a8616e8825 | -3.76969 | -52.09363 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03df000f-d51a-364e-893a-38efdd50bb3c | -0.90692 | -48.05626 | 2024-11-27 04:18:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c887d901-e06e-3249-992f-695effbdd127 | -4.18329 | -48.62661 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 401fe8bd-26ce-3ecd-a6bf-bf973da20d95 | -3.43561 | -54.53954 | 2024-11-27 04:18:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c012f2ef-437f-302d-a360-71fc84af47c7 | -1.7715 | -53.62154 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a6ad010-615f-37ee-b530-55cd6a98b0e5 | -2.11638 | -46.45786 | 2024-11-27 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| b0235947-197c-3b8d-8084-93b6f614c5a3 | -4.48711 | -45.99574 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8906020e-bc50-3a9e-bb96-df5672881917 | -4.22348 | -46.88336 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 539cc6ac-388a-3789-8806-ac3ac3b22bc6 | -3.78585 | -50.13237 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 497e1e90-7e86-31eb-b991-3276a447380e | -2.8074 | -54.13823 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2c900a54-4487-3cfb-8a77-a628761c33c6 | -3.10477 | -53.25987 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c3a49aa-df27-3c5f-9edd-cb675fa13a0a | -3.82069 | -50.63415 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f789710e-3348-3117-9eba-35471998e5b7 | -4.30405 | -48.18325 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50663d03-a576-37aa-bd1d-4611e85c02b1 | -6.09242 | -39.41365 | 2024-11-27 04:18:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4087327e-a460-35c5-bf3c-519d65eec89a | -3.11504 | -53.27076 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54755a1a-7e11-3602-952f-9649fe278c24 | -2.83757 | -46.82297 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0775920d-a4c2-3079-a9a1-f17e4660c050 | -3.96923 | -46.73367 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 071cf884-f04c-30e1-9ef1-5b8066351708 | -4.08361 | -49.73724 | 2024-11-27 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 957c12d8-059b-3225-9562-1e3ec7e04091 | -2.28358 | -47.39837 | 2024-11-27 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4dcd13a1-a37b-3d65-a98e-4b75b6a93c56 | -3.12783 | -50.25648 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1ac5f50-3112-38ae-a260-e15a4dbc32e2 | -1.64151 | -52.49807 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f31055c5-f785-3690-b296-95c3006a2ce8 | -1.95991 | -54.13568 | 2024-11-27 04:18:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d37dd15-ae10-3131-9f00-8c7bde23725d | -2.79707 | -48.68452 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 197f05bd-6eb9-3a94-89f0-cc0ea6518cde | -3.17285 | -48.44199 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| e6603f99-1194-3660-9b0d-407d709c3e31 | -3.75585 | -51.59061 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b761eb1b-3ebb-37d7-9d22-4b3099f296c8 | -5.30169 | -44.43681 | 2024-11-27 04:18:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2b60056-0282-3699-aeec-201333715203 | -3.12439 | -49.21933 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb307f12-4ef1-3c6e-a32c-2401653d00f1 | -3.10838 | -53.27692 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d670a102-6716-3f2b-b72d-3a73986b815f | -4.17967 | -48.62936 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2174e659-ae72-344d-ab27-b5536ae8505b | -3.84866 | -51.38385 | 2024-11-27 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3d9356d-f092-3b87-9c96-e2d943d6d76c | -2.95699 | -48.61628 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 915307c8-a91b-349c-beba-e533a00e0dcb | -2.82058 | -51.79853 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08630251-8049-3b22-8714-f93c9e6ab516 | -3.84391 | -51.38307 | 2024-11-27 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6d8c4c1b-a948-3527-b06b-c3b4ee8d288a | -4.05364 | -46.68229 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2eba1b41-2ca3-3623-b0fb-b7caaba4f4b6 | -2.53362 | -47.32967 | 2024-11-27 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bbbe226a-cbea-3216-a1f1-273be226e2e9 | -2.82818 | -54.12076 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 213d26cf-97fe-38d0-840d-4063be9b60a4 | -4.00613 | -50.3516 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6533e808-b814-35fe-b877-c409e0795604 | -1.51723 | -46.07283 | 2024-11-27 04:18:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1447049d-dde9-340c-84af-ac89abc35253 | -2.9364 | -54.79368 | 2024-11-27 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b6f385e2-c2c0-3106-9fa6-a686d871c2fb | -3.83922 | -46.53344 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f50aa19-5ef6-3b03-95b2-2b5dca1fce38 | -3.25109 | -46.42013 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59854832-8234-3838-8d15-ae1cbba26298 | -5.19042 | -37.97729 | 2024-11-27 04:18:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3de1543c-4697-3262-acf0-94e19f183257 | -3.23136 | -50.31192 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6efad7e4-1c94-34e4-ba7c-7a54d107a019 | -1.51785 | -46.06889 | 2024-11-27 04:18:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b45c0373-5d79-38cc-90fd-716e8a065214 | -4.22151 | -48.66339 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4d41f71e-b311-3774-974b-84a52b5f5f0f | -4.20794 | -50.89998 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 866d4148-c4a1-381b-836e-def58c399fc6 | -2.60019 | -54.2087 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 796f780f-f02f-30a5-b9d4-feaaf393767c | -3.45816 | -50.84435 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0032ec44-48f3-3286-8939-e47629994853 | -1.29374 | -51.72945 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8e53aaf-971c-3746-9f5d-55575779a44d | -2.61015 | -51.80286 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9aff4eb0-5216-3593-84f0-f05e040e6a1e | -2.94371 | -54.79193 | 2024-11-27 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5171a6d-e664-3682-a9e4-45bb99944509 | -4.91713 | -47.85979 | 2024-11-27 04:18:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a895eff1-a55b-34a4-815c-5c495b52507c | -2.6901 | -45.65776 | 2024-11-27 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 5c64d602-f710-3a43-afb4-b9e77e38794b | -4.22162 | -50.90227 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0354c12-8e76-3f25-b376-a548bc9d433f | -4.22771 | -50.20446 | 2024-11-27 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d7397478-4113-3b9a-8058-fe12762d3e20 | -1.50893 | -47.27096 | 2024-11-27 04:18:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c67b9dd4-e70b-3dae-b1ee-f8248a094855 | -3.89976 | -47.74627 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7eaedb9c-ce48-329f-9d44-bcbc76e0c6a1 | -3.56285 | -42.0401 | 2024-11-27 04:18:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 46872b43-5733-3376-bb9f-a6585ce743b7 | -4.14041 | -43.84058 | 2024-11-27 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd6e8044-08f7-30b6-84c7-79395a449311 | -1.19688 | -51.76095 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1793d8e3-94b1-34b5-ba54-41e94ebc3380 | -3.11169 | -51.25881 | 2024-11-27 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0f73c3a3-24fc-314f-881d-652e3b1bfce5 | -3.84783 | -51.38895 | 2024-11-27 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02023355-90f2-31d3-ae78-c7fc52718bf9 | -2.71624 | -48.66783 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90e6ee1a-0e39-3adc-8c85-8b53144416b1 | -1.63815 | -45.70007 | 2024-11-27 04:18:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4be51075-3e0f-3147-a34f-cad973817f6f | -3.51418 | -50.30753 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aac336e3-78d0-3f74-b5e9-43adbcff4b25 | -3.97407 | -46.7262 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab8cc090-2945-3998-89e5-248b79678bc0 | -3.67465 | -53.65917 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b72fb67d-7888-31ea-8fd3-2744f6da9878 | -3.1011 | -50.36456 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README33.md)
