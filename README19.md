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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d8a45dd-d4c7-397e-b398-9987dac34589 | -1.49284 | -60.23091 | 2025-11-11 05:20:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90604712-f204-3c76-9404-68c10a85a592 | -4.72161 | -46.44589 | 2025-11-11 05:20:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d18688d9-27e2-31de-afa9-27af4aa75388 | -2.15376 | -50.70609 | 2025-11-11 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 36fd721b-6eb6-3be3-9fc8-9893c7891a3e | -4.2572 | -48.57989 | 2025-11-11 05:20:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03572473-f8e5-3132-ae1f-680a33279b31 | -3.56219 | -55.47803 | 2025-11-11 05:20:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6afcc9a5-25ac-3b98-93d8-48eca4e001e2 | -2.71987 | -48.34523 | 2025-11-11 05:20:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cad38a2-e9dc-3deb-8a57-1765ebd4619f | -4.14272 | -50.64802 | 2025-11-11 05:20:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8b2e521-8553-34fa-8d5f-c1918b1498e2 | -4.20567 | -50.62991 | 2025-11-11 05:20:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8add60ca-517d-38f8-a0f7-3a63748522c8 | -3.56325 | -55.47952 | 2025-11-11 05:20:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04bf3c24-b016-3452-990e-2383f11c3b65 | -1.84707 | -56.28589 | 2025-11-11 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28e6c209-2d5b-3c90-a41d-b508231dee4f | -15.55072 | -55.23133 | 2025-11-11 05:22:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4247057-1361-33bf-b1ac-0c1956968c59 | -15.55155 | -55.23322 | 2025-11-11 05:22:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47cceb9e-41e0-3b9d-abcc-dcce870abb56 | -19.79633 | -58.0266 | 2025-11-11 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ef294fb5-90ad-33a0-809f-b972f8497e76 | -19.79947 | -58.02994 | 2025-11-11 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 469fe54e-933f-3936-911b-ec6791fa3693 | -19.79633 | -58.02455 | 2025-11-11 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0b3ac56d-7754-352f-b802-33099c487cd7 | -18.39493 | -54.98957 | 2025-11-11 05:25:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 92de2ca9-c6bf-321f-829a-e0167c863b5e | -18.3966 | -54.97566 | 2025-11-11 05:25:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bdc1d54-a473-3e52-91a9-7ebf583b4ae6 | -18.24733 | -51.27473 | 2025-11-11 05:25:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e00b5fb6-eb12-3cae-9226-3d188a3ef60c | -3.92098 | -42.8906 | 2025-11-11 05:25:00 | AQUA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| aa183af6-0051-3907-8030-8c1586123ac0 | -20.10422 | -54.65939 | 2025-11-11 05:25:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0092a33f-4fd2-34fa-8e26-49d6dfd2f566 | -19.75919 | -58.01611 | 2025-11-11 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 8fa9dbc2-0c01-3575-86de-3af900a46622 | -19.81773 | -58.03761 | 2025-11-11 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4eb237b8-c080-318a-9c4e-40fa11008574 | -18.38878 | -55.00283 | 2025-11-11 05:25:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e36d3a32-f2b0-3242-95dc-73fdfaea67f0 | -19.76363 | -58.01185 | 2025-11-11 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 81b52191-c35d-399d-8eea-161363d2908a | -19.81081 | -58.03165 | 2025-11-11 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 1ebdba17-86b5-3781-8609-55f796d0727d | -19.76428 | -58.00703 | 2025-11-11 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 50dd9bfb-5a60-3b53-bd00-3b8120200e4d | -4.71019 | -46.44864 | 2025-11-11 05:25:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 142438d1-c9fe-3da0-ae30-21a275bbb023 | -18.39437 | -54.99421 | 2025-11-11 05:25:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 63aede2d-7339-31e5-a46a-8c9a46cdb35e | -20.10607 | -54.65556 | 2025-11-11 05:25:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 438abf97-c241-3e03-b3e2-789086a73d57 | -17.80618 | -51.73875 | 2025-11-11 05:25:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc2860f7-f548-3897-9547-729e8ddb915b | -19.79255 | -58.02604 | 2025-11-11 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| c8222c6b-6b2a-39bb-aa88-462a118bb04c | -20.10949 | -54.65509 | 2025-11-11 05:25:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a66d6382-165c-34d2-b606-55ebac24fbe0 | -19.80011 | -58.02717 | 2025-11-11 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4504dd6e-6198-3f20-9c11-e8ab633e6ab9 | -18.47784 | -53.40448 | 2025-11-11 05:25:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 14.6 |
| de95a9e2-4e8a-3d6b-8e01-7200b5c08787 | -18.47288 | -53.40366 | 2025-11-11 05:25:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 74c32e2e-b924-36c3-a495-cc98d1c8d9ef | -17.56087 | -54.02001 | 2025-11-11 05:25:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce622073-2a73-3e05-926d-48fdad0ee07b | -19.82151 | -58.03819 | 2025-11-11 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ca72352f-471e-3650-9e25-12bc12fa601c | -3.96262 | -43.76826 | 2025-11-11 05:25:00 | AQUA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 75aebb39-af8e-3324-bf46-d76b8b115961 | -3.91801 | -42.90987 | 2025-11-11 05:25:00 | AQUA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8b4d28d7-dbd7-3128-824b-263f8bda1926 | -20.1089 | -54.6601 | 2025-11-11 05:25:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3dacf151-4f3e-33bb-a923-dcc3fbd21859 | -18.2456 | -51.27467 | 2025-11-11 05:25:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc263f18-cbe8-3418-96e8-4f79411f56cb | -20.10551 | -54.66056 | 2025-11-11 05:25:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7cbb89a9-cf78-3b1f-9c2e-151ed9667dca | -18.39156 | -54.97969 | 2025-11-11 05:25:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87cb2d00-1740-3004-b949-196423f0b2b9 | -18.24605 | -51.27051 | 2025-11-11 05:25:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6daca516-a05f-31f5-97e5-972c0c895125 | -18.39212 | -54.97506 | 2025-11-11 05:25:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff126d02-d19d-3a34-bb32-809ec0be9705 | -18.39101 | -54.98433 | 2025-11-11 05:25:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84e12d9b-8302-3da2-9306-d0a7ac9f7cac | -18.38934 | -54.9982 | 2025-11-11 05:25:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 77331630-9a2b-346c-ab46-ba5dd240b3ec | -18.39549 | -54.98494 | 2025-11-11 05:25:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1dc80629-376d-3467-8647-d9112cec3808 | -3.92041 | -42.89783 | 2025-11-11 05:25:00 | AQUA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 4c069edc-ca72-3a6d-8531-61f0a333d47f | -4.90692 | -44.31467 | 2025-11-11 05:25:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| fe9af37d-ad98-37f4-85dc-780a32f9d1a6 | -17.12999 | -55.74313 | 2025-11-11 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e0114d75-2411-32e0-9fed-8d12e4871f83 | -4.71927 | -46.44506 | 2025-11-11 05:25:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 56f68b8f-ed1b-327c-98d3-a6383306df34 | -19.78877 | -58.02547 | 2025-11-11 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 75c7ff15-3035-3c97-b410-2bfcee6a9b67 | -18.24774 | -51.27056 | 2025-11-11 05:25:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b2f332c-d0b1-3fad-9856-92833a1f2334 | -18.47847 | -53.39888 | 2025-11-11 05:25:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 63293e97-5581-3f6b-9bcf-e5f345498f03 | -17.8007 | -51.73772 | 2025-11-11 05:25:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 888b3617-9540-31ed-84ff-7eda9f1a7a29 | -18.48345 | -53.39958 | 2025-11-11 05:25:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8714b0a5-28bc-3c75-bf11-69ffd03ad978 | -21.34511 | -55.98313 | 2025-11-11 05:25:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bdfb803f-5e52-3352-8d4e-6573cb05fa1b | -19.81837 | -58.0328 | 2025-11-11 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6ae90631-5962-3445-939c-192451829a6e | -17.80655 | -51.73533 | 2025-11-11 05:25:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51a2329b-2900-361d-93a2-40cc0e7c0df3 | -26.60849 | -53.16283 | 2025-11-11 05:27:00 | NPP-375D | SANTA TEREZINHA DO PROGRESSO | SANTA CATARINA | Brasil | 4215687 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f370daf6-f0b4-3c02-b455-17b8c4c4cc6f | -26.61053 | -53.16608 | 2025-11-11 05:27:00 | NPP-375D | SANTA TEREZINHA DO PROGRESSO | SANTA CATARINA | Brasil | 4215687 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e3b6409a-647a-3ad9-9f5c-93d2a0e59720 | -22.03497 | -56.0569 | 2025-11-11 05:27:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c8ca613-8066-3768-8e6c-a6fdac157f4b | -22.66172 | -54.87785 | 2025-11-11 05:27:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3eeef6f8-5b61-3b0c-b91d-9c296b109bf5 | -10.49757 | -44.9254 | 2025-11-11 05:27:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 27.8 |
| dc999ba7-ba43-35ba-b317-1c9ebd9159e0 | -22.67412 | -50.44486 | 2025-11-11 05:27:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7196023c-899b-3568-b106-26abb4f127e6 | -11.04558 | -45.3881 | 2025-11-11 05:27:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c1dcb3c7-5af7-39b9-88dc-c105093e77f7 | -26.61087 | -53.16219 | 2025-11-11 05:27:00 | NPP-375D | SANTA TEREZINHA DO PROGRESSO | SANTA CATARINA | Brasil | 4215687 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bef76ab2-4aab-37cc-9348-90b61d957243 | -10.49556 | -44.93029 | 2025-11-11 05:27:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 85ae2bb3-846c-3cfb-96eb-831c5bae03ac | -12.33648 | -43.65615 | 2025-11-11 05:27:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 27d6f09e-8ebe-30d2-9e11-32861b3aa429 | -26.61402 | -53.16411 | 2025-11-11 05:27:00 | NPP-375D | SANTA TEREZINHA DO PROGRESSO | SANTA CATARINA | Brasil | 4215687 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ad06178a-37bb-380a-89b3-c6431ca9afad | -22.68043 | -50.44552 | 2025-11-11 05:27:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c0ca90c-108a-388c-83e2-dbc1d89102ac | -3.9236 | -42.8952 | 2025-11-11 05:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| bb1563f4-84f8-3283-b7d3-24bd1117204e | -3.7003 | -42.7426 | 2025-11-11 05:30:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 2df14953-f3e6-3469-ae36-8aa0cbe1c5e2 | -4.7204 | -46.4497 | 2025-11-11 05:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 00ce0625-e75d-36d0-a0cf-5ee39445d829 | 3.53254 | -51.77912 | 2025-11-11 05:37:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a66bf8b3-f05e-3240-85ac-28d5cef96415 | 3.53863 | -51.77789 | 2025-11-11 05:37:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c17a72d-3b89-3ae9-9971-ba9194d08df3 | -1.64439 | -52.05396 | 2025-11-11 05:40:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f97b2ca9-5cea-3e14-bf6b-cb8e12996d90 | -2.09987 | -56.64277 | 2025-11-11 05:40:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b82d2ad-abac-371d-a4cc-ac2088fc9c8d | -2.10118 | -56.64064 | 2025-11-11 05:40:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb0eb186-32ce-3d75-9b2d-763af336f291 | -1.64487 | -52.04975 | 2025-11-11 05:40:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a73d4ae3-19aa-36e6-bdcf-c49f22ddb6d7 | -1.63754 | -52.05432 | 2025-11-11 05:40:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bfcc73c-dba5-39ff-9ec3-5be5195d232f | -1.63788 | -52.05308 | 2025-11-11 05:40:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58932e26-41cb-3ac5-8239-3cd84d7ddaf7 | -1.64404 | -52.05524 | 2025-11-11 05:40:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b72112e-6353-37c2-8292-e787f6700dcd | -2.10035 | -56.64593 | 2025-11-11 05:40:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba1e29e4-c1fb-3ae2-9152-d1350aaacb27 | -2.10066 | -56.63746 | 2025-11-11 05:40:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 758b1885-7f85-3927-a4d4-7103d48c992a | -1.63836 | -52.04883 | 2025-11-11 05:40:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ace0ad8-3c89-373f-9ce6-74a20ce4f499 | -3.2249 | -61.23972 | 2025-11-11 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14c32e74-ebca-3c3e-899f-082f9a34df7d | -18.3889 | -55.00263 | 2025-11-11 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e6ac79e-b0f0-3876-9947-5e6b6cab9a28 | -18.39415 | -54.9854 | 2025-11-11 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 981bdd5b-d23a-30f2-af04-67f89ced1c1a | -10.05008 | -67.81013 | 2025-11-11 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a9d0091-8c05-3948-a4be-d6509f47f04d | -18.39362 | -54.99147 | 2025-11-11 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2812d4ad-7b52-3bae-865e-b787a0a0858d | -18.38588 | -55.0029 | 2025-11-11 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ca9d453-aeaf-3e5e-98f4-595546773937 | -9.72085 | -67.4786 | 2025-11-11 05:44:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51221455-f766-3f21-95ce-f0c9d3b5ea13 | -9.66721 | -67.51081 | 2025-11-11 05:44:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edb78435-236a-3645-96ed-db6bf125f25e | -18.39118 | -54.97843 | 2025-11-11 05:44:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73d0e1a1-c3ec-32ad-8100-1492292b1a33 | -9.7169 | -67.48167 | 2025-11-11 05:44:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc30eb4f-d983-30ba-ae57-8935637814de | -9.78611 | -67.9423 | 2025-11-11 05:44:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 676de74e-7df0-3542-bd84-788ece2cc8a9 | -9.72027 | -67.48223 | 2025-11-11 05:44:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14348a91-7e48-395e-996e-842d9ae30fe0 | -18.39468 | -54.97932 | 2025-11-11 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README20.md)
