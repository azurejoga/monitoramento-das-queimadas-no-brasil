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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a37dc8d4-011d-3e6a-807b-1a8f130f159a | 0.6159 | -51.7676 | 2024-11-17 07:40:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 8a42ee09-10de-3663-a64b-0dc15c0882ff | -3.295 | -45.2895 | 2024-11-17 07:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 122.5 |
| fe789981-af6a-3079-81cd-078738c1c935 | 0.6159 | -51.7676 | 2024-11-17 07:50:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 65.2 |
| f2a7cd29-729e-3ad3-8445-994f7cd8a2c7 | -3.2949 | -45.312 | 2024-11-17 07:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 123.8 |
| de48d30b-85a3-3168-8773-8356f31b6c80 | -17.6059 | -57.5921 | 2024-11-17 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.8 |
| a6755cb9-a3e0-36b7-b57e-014d03052e6c | -17.6063 | -57.5715 | 2024-11-17 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| 598af1ae-24df-3b0e-acab-67f42417f19a | -3.2949 | -45.312 | 2024-11-17 08:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 58.1 |
| e207bc38-bc37-3f87-9bca-8a4a90115ae0 | -3.295 | -45.2895 | 2024-11-17 08:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a51c166b-c88b-3b44-8453-fcf2266d4fbb | 0.6159 | -51.7676 | 2024-11-17 08:00:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 22a4ec17-752e-36eb-89ff-518fe36c05ee | -17.6063 | -57.5715 | 2024-11-17 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 85746b90-d044-3ad9-bf37-b9849c5e0188 | 0.6159 | -51.7676 | 2024-11-17 08:10:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 58.9 |
| b3970215-9f0f-380e-a184-88d8e2c98e02 | -17.6059 | -57.5921 | 2024-11-17 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 132bb7c9-68a5-3038-9a67-63c179238e0e | -17.6059 | -57.5921 | 2024-11-17 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.7 |
| 7aed70c0-6626-3d32-aacc-7255b0654d0a | 0.6159 | -51.7676 | 2024-11-17 08:20:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 1ce6a346-b12d-3ef2-b45c-c8201a318559 | -17.6063 | -57.5715 | 2024-11-17 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 20b99b7e-7b5c-39ec-bb2a-7f84deddb04d | 0.6159 | -51.7676 | 2024-11-17 08:30:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 17a39fa4-e5ed-3c1e-8dbf-4d8bc3541a23 | -2.9253 | -44.8293 | 2024-11-17 09:40:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 168045c8-1560-37f6-a098-9d5be801ea35 | -2.9253 | -44.8293 | 2024-11-17 09:50:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 132.9 |
| ea207a9b-8dda-3782-af63-3181d645aed5 | -2.9253 | -44.8293 | 2024-11-17 10:00:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 174.3 |
| 01bb633b-611d-3d20-9260-0de19d4b8a7c | -2.9253 | -44.8293 | 2024-11-17 10:10:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 181.4 |
| 41a48c78-7677-3f38-b4ab-5dff262c8e6c | -2.9253 | -44.8293 | 2024-11-17 10:20:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 192.7 |
| 23cc4db0-9d89-375a-bfe4-ace398150d81 | -2.9439 | -44.8286 | 2024-11-17 10:30:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 2a0bd5d6-67df-38d9-9593-c92db9bd7915 | -2.9253 | -44.8293 | 2024-11-17 10:30:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 1d5d5269-4a29-3d1c-a37d-67e64a35b0ba | -2.9253 | -44.8293 | 2024-11-17 10:40:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 139.5 |
| dfa9f1c4-eb84-3b03-b4d8-8b79154e941d | -3.5377 | -45.1214 | 2024-11-17 10:50:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 183.2 |
| aaa8815a-870d-341d-83ec-8d7977992c77 | -3.5378 | -45.0988 | 2024-11-17 10:50:00 | GOES-16 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 151.1 |
| a93f3243-d91e-38e4-aad8-ec5058e2331b | -2.9253 | -44.8293 | 2024-11-17 10:50:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 8fd1e7e3-aeca-35e1-a42c-247cbe2121e2 | -3.5378 | -45.0988 | 2024-11-17 11:00:00 | GOES-16 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 45d691da-7964-3526-b447-56a088f71e3d | -3.5377 | -45.1214 | 2024-11-17 11:00:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 207.3 |
| 9f8fffc4-3781-3387-b685-3c14f9627def | -3.5377 | -45.1214 | 2024-11-17 11:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 194.3 |
| 9b035757-62c8-30ea-b103-8b874fb12249 | -3.6639 | -42.5799 | 2024-11-17 11:10:00 | GOES-16 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 104.6 |
| c0555ae6-77fc-351e-af9c-231be9165284 | -3.5378 | -45.0988 | 2024-11-17 11:10:00 | GOES-16 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 5c7a2536-d773-320c-8691-9a3366588c22 | -3.55479 | -42.10256 | 2024-11-17 11:46:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 462.2 |
| 36051f92-8746-39bb-9626-0d319c08d2bf | -3.58075 | -42.04112 | 2024-11-17 11:46:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| a2b047da-7d5a-34a7-afde-c370dcdcb54c | -4.10983 | -38.89418 | 2024-11-17 11:46:00 | TERRA_M-M | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 73ef0600-42b6-3858-bc93-98f18af8f1b2 | -4.44292 | -42.89802 | 2024-11-17 11:46:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 4a7b37fa-1151-373e-9a20-99ad5cd0b7c5 | -4.11237 | -38.87733 | 2024-11-17 11:46:00 | TERRA_M-M | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 234dbacf-a41f-34fc-9e8d-d17beaa17012 | -5.4659 | -38.37072 | 2024-11-17 11:46:00 | TERRA_M-M | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 374859dc-e4a3-3cfb-8bfb-c2726bb2eb17 | -3.56137 | -42.09755 | 2024-11-17 11:46:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 557.5 |
| 5df832da-e5b8-3cc5-b82c-154e74b4fbed | -3.589 | -42.62849 | 2024-11-17 11:46:00 | TERRA_M-M | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 241.1 |
| 18721268-f644-3eac-b340-67abdf010843 | -8.22166 | -35.26956 | 2024-11-17 11:49:00 | TERRA_M-M | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 8557a5f6-d879-38bd-be28-1eeaef95f242 | -6.36021 | -38.31708 | 2024-11-17 11:49:00 | TERRA_M-M | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | 35.1 |
| b22a3d44-7633-3cca-b089-b0c0771f6d6a | -6.35819 | -38.33625 | 2024-11-17 11:49:00 | TERRA_M-M | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 09464cc3-294d-3784-b31b-d181e8c60bec | -7.07424 | -35.41105 | 2024-11-17 11:49:00 | TERRA_M-M | GURINHÉM | PARAÍBA | Brasil | 2506400 | 25 | 33 | nan | nan | nan | Caatinga | 16.9 |
| b53b1f03-1019-3879-82f0-37f354e7c011 | -8.5143 | -35.04039 | 2024-11-17 11:49:00 | TERRA_M-M | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 44a0f08e-6f6e-3cf8-9ca4-87901f754d6f | -8.43717 | -44.19242 | 2024-11-17 11:49:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 440706e7-87d8-30f8-9a20-ae0cbe6f2084 | -7.14252 | -36.98243 | 2024-11-17 11:49:00 | TERRA_M-M | AREIA DE BARAÚNAS | PARAÍBA | Brasil | 2501153 | 25 | 33 | nan | nan | nan | Caatinga | 15.2 |
| bdbc2476-84f9-3e4e-a2dc-9c3ff5e98a7e | -12.72412 | -42.31677 | 2024-11-17 11:49:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 31.5 |
| 8df9606d-bc4f-335b-b59d-4a91f19745cf | -8.43458 | -44.18427 | 2024-11-17 11:49:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| d3a6be1b-f50d-3ec1-8772-43eddaaf1e3b | -8.45404 | -44.19595 | 2024-11-17 11:49:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| f1aed513-6524-3fad-950f-da7df8e5d3a4 | -6.86187 | -37.54086 | 2024-11-17 11:49:00 | TERRA_M-M | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 13c1c94c-c69d-3c84-8cdc-1b47531981bd | -6.00212 | -37.13272 | 2024-11-17 11:49:00 | TERRA_M-M | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 24.3 |
| a5e91ea1-08bc-3386-9bc0-f43112227bb5 | -7.08339 | -35.4124 | 2024-11-17 11:49:00 | TERRA_M-M | GURINHÉM | PARAÍBA | Brasil | 2506400 | 25 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 8896a73f-a716-34fe-9ada-ecbd9782c9b6 | -7.14428 | -36.97091 | 2024-11-17 11:49:00 | TERRA_M-M | AREIA DE BARAÚNAS | PARAÍBA | Brasil | 2501153 | 25 | 33 | nan | nan | nan | Caatinga | 21.8 |
| e7684e52-1e43-3dcb-9e3b-ac69934e8f01 | -6.35818 | -38.33059 | 2024-11-17 11:49:00 | TERRA_M-M | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 0b898d38-fb65-37f5-9cb6-74166aac5130 | -6.36032 | -38.32263 | 2024-11-17 11:49:00 | TERRA_M-M | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | 80.2 |
| e6a68e31-d70b-317e-9853-7c9a472ee72f | -7.80324 | -38.01331 | 2024-11-17 11:49:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 375d83aa-64ef-3167-9918-5233622eb8e3 | -8.45149 | -44.18753 | 2024-11-17 11:49:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 2d2cacdc-0178-34f9-bf21-27f1fa5b29f3 | -3.54 | -45.1 | 2024-11-17 12:00:00 | MSG-03 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6ed5ca43-99de-376e-8f10-4dcf565c6a8d | -3.56 | -45.1 | 2024-11-17 12:00:00 | MSG-03 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2d5b17ec-8bd8-31e8-ae16-6ea03b2428af | -8.28 | -45.97 | 2024-11-17 13:00:00 | MSG-03 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4bb5e4ea-d1e1-30ca-bc53-6313190ab66e | -2.6 | -47.52 | 2024-11-17 14:00:00 | MSG-03 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f4c6232-fc93-3b7a-a4bb-f659f6352735 | -2.57 | -47.57 | 2024-11-17 14:00:00 | MSG-03 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b327df73-28dd-3f61-b2db-026f1be35910 | -2.6 | -47.57 | 2024-11-17 14:00:00 | MSG-03 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 087981f7-dc4c-380d-9b7e-4c7aca7494ee | -2.57 | -47.52 | 2024-11-17 14:00:00 | MSG-03 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |


