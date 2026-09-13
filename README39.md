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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 378d18f9-de3f-36b8-9953-847a7c282c32 | -9.371 | -50.10376 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 55d0fe1f-d686-3101-9b6d-0bf5661bc39c | -10.53596 | -51.29964 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0477687-1dc9-3c48-a4e9-ab9c50c6d92e | -10.6903 | -54.16946 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ad81e6fb-a238-36b0-9d74-3ef65a7140cd | -6.30035 | -59.95304 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22dd0032-ab21-3e79-9be0-7898299ed6da | -10.47059 | -48.64931 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49ce61ec-7086-3c2b-a3cd-97d5f4ed1b12 | -13.48836 | -48.48794 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f0f665c-c773-3694-976b-ec9fe24935d7 | -11.98526 | -48.64412 | 2026-09-13 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a66a532-d0f3-3c4c-8e03-30256b209582 | -5.96651 | -57.7748 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9d93e6ff-13e5-3183-ab47-f03a3729c160 | -7.46611 | -46.14391 | 2026-09-13 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61efce8b-5475-30a4-bed0-d7386a2c4466 | -7.96078 | -43.9977 | 2026-09-13 04:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90a40b0b-e275-3c8a-a066-b8898833e712 | -6.28726 | -59.92508 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dde70e30-d282-3ab6-aa78-51038c083509 | -13.48422 | -48.49146 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47fa55ca-d546-3b2b-bede-7c9450eeb27a | -6.64612 | -58.82347 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54539613-7a79-3170-b862-8c194fbabe5b | -9.89226 | -47.58595 | 2026-09-13 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e73201d-7c66-3f90-af7c-6b3c262c0fb0 | -10.30767 | -45.27936 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c2a94de-9338-30a4-919f-1d97330b8cba | -6.66991 | -58.87728 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ca8644f-3c40-333e-943b-e8bf16971a48 | -6.28648 | -59.92545 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8f112fe-40af-374b-b3a6-11519ea601b4 | -10.45295 | -48.65498 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ded73159-bcb8-3c7e-9cd3-2e82eefc368d | -7.86571 | -54.69961 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffc3a987-f7b6-35ad-877d-3e29a6c8f00e | -10.50803 | -51.30231 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fa6d27c-b8b9-3a14-8668-85ba99bc6f0f | -6.28143 | -59.92413 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55e74851-aeaf-3ee9-a492-d61d8169a6e8 | -6.30951 | -59.96376 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a3fae83-4bf9-3084-9ee3-ad3a7645f151 | -6.78317 | -59.8485 | 2026-09-13 04:51:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b83c734-f1f4-3b01-86c4-2b2f52150b2b | -13.3487 | -51.80058 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8ba4924-6b1c-3472-8b8a-0a80641267fb | -6.59182 | -58.87075 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fbb950d-aa4a-30f8-bc72-cc554ec2bda6 | -10.94844 | -47.90959 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01cbd0d8-a091-3983-9280-82fa8294246c | -6.61116 | -58.86309 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41ac6406-1f99-3309-abe3-55c3390dd69b | -14.9113 | -44.67113 | 2026-09-13 04:51:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd884b8e-85b3-3cc5-8586-ebc343c507a6 | -6.60702 | -58.85516 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f036ac9-39b4-3e71-928d-0f5361752e08 | -8.21217 | -47.86907 | 2026-09-13 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 070fa9b8-349a-30ae-861f-1e14cb91f605 | -11.24303 | -54.12923 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6ecf9eb-4d90-3693-b556-fbf24baf1ebc | -10.22132 | -45.1886 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd885bd6-5efb-3265-80be-d81c77813308 | -11.57684 | -46.99053 | 2026-09-13 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| edeb2070-fe26-3c6c-9c27-8c7765812c3f | -6.28424 | -59.9376 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a89e7ba0-4004-3cc2-8e6b-23cc6e5aee07 | -13.59986 | -47.88451 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b081547e-26f0-307d-b256-5cd5199bacae | -10.94544 | -57.18941 | 2026-09-13 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| db4594fd-5a50-3af9-91b5-aa52ff8e21f0 | -8.05231 | -54.85172 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67ad8870-5970-3829-b6d3-3a19c79ec911 | -9.55801 | -51.36406 | 2026-09-13 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c9805d3-f217-3c29-a90f-cc34364ba6c3 | -13.45714 | -48.47924 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 33c051c3-be28-31d3-b30c-4adc06874cad | -10.47574 | -51.37406 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1495501b-2318-36e8-837a-9a51ede43bd7 | -6.30017 | -59.94904 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac3a3500-20e5-3909-9e42-96fedc2fa829 | -6.66868 | -58.88424 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84cf7afc-f9f8-3d2f-9d5e-8dd7539b7520 | -7.86656 | -54.69456 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 313977ec-c5b2-3c5e-aba6-3d5bf9937555 | -7.87379 | -54.70813 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58b5143e-7651-3a4e-8244-869706740c63 | -6.37494 | -58.29474 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be3f3f8e-e5b0-387d-b363-e1d69729760b | -10.54475 | -51.33031 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e54ea5f1-54e3-3c74-b84c-081ae1fceb78 | -11.96159 | -49.77375 | 2026-09-13 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d59a4917-fffd-34ea-8d73-6ee10a8a88d0 | -10.52459 | -47.90517 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f717d7bb-d9d5-305c-b12a-397be7a1e10e | -7.87198 | -54.71854 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52b190aa-3f40-3a90-b036-a5d88c028199 | -7.52907 | -47.33493 | 2026-09-13 04:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f5b7a88e-cd75-31b8-b4e9-05b720f685f7 | -14.62134 | -46.94763 | 2026-09-13 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9177d9e8-8041-3d7e-8332-8143e0e6ef60 | -6.67591 | -58.87485 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e00a785c-97d1-3204-9bee-e83d1dc66907 | -8.571 | -54.57257 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68bfb0f4-878b-3fb0-9313-3f72673d6642 | -7.86978 | -54.70745 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0086432-4db1-3b07-b467-c05c52baa940 | -6.37549 | -58.29156 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 651e2612-f2b9-37dc-ac30-a883434b3016 | -10.47909 | -51.37462 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c4b95f8-323e-3661-ad85-88edd612f016 | -6.77441 | -59.43137 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c698f6fa-2dc0-33db-b40c-7fe9a0282036 | -10.52519 | -47.90119 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d102ee35-7de4-3145-b336-e471a53809f9 | -11.24443 | -54.14318 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05348b06-c92b-3835-aa80-c5f029170694 | -7.64226 | -47.18694 | 2026-09-13 04:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4fa06ca-d4b1-3fc8-8900-857bbfe523aa | -8.74763 | -46.43227 | 2026-09-13 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61fdf004-e638-38dc-9fa4-81bfb67d1d36 | -10.53608 | -51.38406 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d43f1c3b-55e6-36b3-8c07-0ed7410a3fbb | -8.28704 | -39.9706 | 2026-09-13 04:51:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cc8fc04c-a672-3d5a-bb2f-fccda8b24931 | -12.65174 | -54.69268 | 2026-09-13 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6ff8858-258a-3500-9ee1-fb92a1b5fe40 | -7.86885 | -54.70549 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2af29612-8947-3b57-b15c-136a9fb9d487 | -13.46067 | -48.47977 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51f7554d-b295-3f4b-980a-e34efe436c6c | -9.38847 | -57.30147 | 2026-09-13 04:51:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 86eae6af-b534-3b96-b9c9-f0d85324709d | -9.38313 | -56.99059 | 2026-09-13 04:51:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 588f400a-7e60-392f-b8d1-398472ef1e86 | -6.96114 | -59.74906 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9c27f512-c4f8-382d-9fce-9f7384d31b3b | -6.08778 | -57.90817 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a992f1c2-9198-38f8-83d0-e1ed9cc8d754 | -7.87284 | -54.70624 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c842e25-7cc0-3dba-afb2-601b0de9ed62 | -7.46544 | -46.14832 | 2026-09-13 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d89d99d6-4621-32ec-8cd0-f5103408f641 | -7.48874 | -49.57792 | 2026-09-13 04:51:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f2982ea-7a93-3405-9c0c-8b1b0f283f76 | -8.06082 | -54.85398 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34187a38-e310-3b89-84cb-d45432aaf321 | -8.05077 | -45.5522 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f909664b-0e24-36a0-a816-8031ff37822e | -10.20857 | -45.27601 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 409fcf4b-b211-333f-8ffc-269b2ba1adc1 | -13.31413 | -51.72515 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d61c6cc3-19d5-3225-8f16-2413de62dc83 | -8.05693 | -54.84887 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73d8461a-01ee-38db-9a5f-f38029b958e9 | -8.28139 | -39.96986 | 2026-09-13 04:51:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6307b428-ce2e-38c3-ad3d-4f6207f4bedc | -8.11591 | -54.79841 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ac8ae33-2436-3096-a3d0-fd7c67cede2b | -7.86798 | -54.71787 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73ff8456-5691-3192-86b4-d2f886af9014 | -8.81782 | -61.40664 | 2026-09-13 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f65f50b-7448-30fb-b7e6-63f4e31cb2c1 | -7.95652 | -43.99698 | 2026-09-13 04:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6dbdbfb-149c-32dd-aba9-7c08c530ab07 | -11.18338 | -42.78975 | 2026-09-13 04:51:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 667c443d-0f0b-3145-a217-4261766b6553 | -10.72651 | -54.00264 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23dc533b-3dfd-3f31-b537-784b0d82b412 | -9.58103 | -55.15976 | 2026-09-13 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbcab4d1-e274-30da-a7c4-08872f33ddd2 | -13.3341 | -51.62218 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 97c5aa93-3666-319a-b67f-baf7f126b854 | -11.24671 | -54.12989 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fab132ca-be44-31bf-96db-ece805d3718e | -10.30966 | -45.29412 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 695aa528-cd84-39fe-8e74-066d45033a74 | -7.52497 | -47.33829 | 2026-09-13 04:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da493547-4f75-3851-a1c9-b414cd0ef6db | -7.97102 | -43.98711 | 2026-09-13 04:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 208b74c9-4e97-3269-813b-31d745a1cc98 | -10.21668 | -45.19186 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba45941d-508c-31ae-9d9e-611c9683009d | -6.30542 | -59.9584 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdf29cb4-6881-34b7-a665-c52877abc6eb | -13.61807 | -47.88507 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c6960a11-cdc3-3c70-b9a3-67d3b9c3a16d | -6.30981 | -59.96769 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1fba7b2d-b1f7-31bc-a09c-bab60ededce8 | -10.27975 | -45.32941 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61df66fc-8b7c-35ba-8263-f71544cd3c2b | -6.76884 | -59.43027 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a00183da-b5ea-3e54-9391-acf32cac6e85 | -13.34434 | -51.78516 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fea5c851-0044-3164-b639-9cc90c8bdd6c | -8.60789 | -55.22913 | 2026-09-13 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a09527b-72ee-3311-bcf1-02e9aebae894 | -7.86446 | -54.69068 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README40.md)
