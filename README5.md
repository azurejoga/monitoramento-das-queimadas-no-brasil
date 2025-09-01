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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9773b8dd-87fe-343c-95fc-cfff0c077d27 | -12.93153 | -56.98903 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 45dc8cde-ddb8-3d68-9cb4-536ee75dcb81 | -15.80482 | -55.91687 | 2025-09-01 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 6324eac0-0ba2-3e1e-b53a-4f0bab639355 | -7.70106 | -61.48663 | 2025-09-01 01:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| d1a631ef-9e4c-3bb1-bdd1-2c288c3125ce | -14.42374 | -51.66669 | 2025-09-01 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 8a69e9de-b30a-38d4-9f58-eb82320b4cc0 | -7.28673 | -60.65517 | 2025-09-01 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 7367a717-22eb-3e6a-b6c6-3935cd08005c | -12.91649 | -56.94505 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| a41aa107-2b96-3a81-ac2f-7bcb38aeecb3 | -11.6548 | -57.35788 | 2025-09-01 01:09:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| de9ea110-fd7e-3a05-bf98-e6cc2567b729 | -11.82259 | -51.47042 | 2025-09-01 01:09:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5a4183d5-82fe-356b-bb59-27b36777fab7 | -15.23207 | -53.80217 | 2025-09-01 01:09:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 52b17d62-e6e9-3f33-90a4-8f67c4360945 | -11.02945 | -47.01365 | 2025-09-01 01:09:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 1eabedf3-b684-3961-bf9d-a2f8f3903567 | -11.7973 | -46.42955 | 2025-09-01 01:09:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| ab06aa87-fc2c-383b-8cc9-f34735e8908f | -6.4415 | -55.61925 | 2025-09-01 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 11721b07-85c7-301e-bdfa-eadc132a73d4 | -14.75213 | -46.76387 | 2025-09-01 01:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 5b270714-9c9a-303d-a714-cf2798483af8 | -12.92658 | -56.9528 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 539.0 |
| fa3eafc4-44c0-3a07-8146-207e6a161b4b | -6.44297 | -55.62935 | 2025-09-01 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a35141cb-9f25-3817-9f94-ba5d7733177f | -14.59564 | -54.48555 | 2025-09-01 01:09:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3a703873-d62a-353c-88b2-b36e9b280221 | -10.04886 | -48.08871 | 2025-09-01 01:09:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| c8f70150-9de4-36ed-9b61-835a9fd4ea52 | -12.98471 | -54.75767 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 585f6eec-911b-38d9-b14e-7235dcb8e144 | -9.31014 | -59.20936 | 2025-09-01 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e31a82db-c71c-3189-a763-19b5fe0ad22a | -9.45134 | -60.57566 | 2025-09-01 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 1f1900a8-62b8-3581-acdc-6940e4678b57 | -11.58746 | -55.55373 | 2025-09-01 01:09:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 875e0bb7-94e6-3b4f-8077-c5179b5d3677 | -8.7343 | -62.41319 | 2025-09-01 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 53b2023e-391e-3aa4-bb30-53c2ac7aa52f | -6.83922 | -52.8159 | 2025-09-01 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e47421ce-6d22-356b-af9f-baa1eede2a6e | -12.57425 | -48.19122 | 2025-09-01 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 2184c793-974d-3741-94bf-0557038932d3 | -12.2274 | -50.16869 | 2025-09-01 01:09:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 9a9c44dd-12de-3946-b8df-839a5b091c1e | -6.34435 | -58.18637 | 2025-09-01 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cc261c95-2b71-39e7-9525-7bd348071ea9 | -7.58945 | -61.63058 | 2025-09-01 01:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| ca6bed93-3900-3349-973d-50502f5608a9 | -7.70384 | -61.47902 | 2025-09-01 01:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| d889d7c0-0e7b-366c-ae62-1ad74a32764d | -12.44603 | -63.92948 | 2025-09-01 01:09:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 27.6 |
| db0f3692-7ef4-3106-b635-62e42527789a | -7.09567 | -63.13852 | 2025-09-01 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 779fd478-fb59-3a73-988c-6eb918a65719 | -14.49845 | -53.15978 | 2025-09-01 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fa31ed01-9d64-35a7-b03a-e0c87c4a16d1 | -10.12563 | -58.02142 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 130f0423-9145-3492-bec0-7bfb3b56b407 | -8.55522 | -63.00615 | 2025-09-01 01:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e5cdb514-4fab-3eee-9bce-947f541f8938 | -8.54961 | -63.01334 | 2025-09-01 01:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 9542dad2-f41a-3bdc-80ce-bdbfdb9c0d6b | -11.03107 | -47.05685 | 2025-09-01 01:09:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 372.8 |
| 5a260cfc-2ea3-32cb-b70f-6eaa46bd0384 | -6.84147 | -52.83115 | 2025-09-01 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 6c8cb782-a704-326e-9a8e-eae214bee94e | -11.52419 | -54.46762 | 2025-09-01 01:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 17aa8200-1336-321c-b7d5-f64955338038 | -7.06632 | -63.06569 | 2025-09-01 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 915cddb8-e985-3aa4-9a35-63da72da147f | -13.02752 | -56.8861 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6d5b762c-c58b-3103-a35c-ee9f3e3834e9 | -11.07597 | -52.06317 | 2025-09-01 01:09:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 7519e05f-2f3f-3136-a663-45096296dd98 | -7.08355 | -63.19683 | 2025-09-01 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| dd259db3-98d9-32f2-9fee-21839f3b9a7c | -12.91773 | -56.9541 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 283.1 |
| 1b2bc6e0-0572-30c1-b1b2-5466f41064e2 | -12.92268 | -56.99033 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| b56711cd-0766-3320-977c-ec60546ddfe2 | -9.59527 | -54.48869 | 2025-09-01 01:09:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1d603054-a142-3617-84f5-486e0b175e38 | -7.27694 | -60.65649 | 2025-09-01 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 5fe33873-30f5-3500-9588-7dbdd9e16f7d | -7.07723 | -55.42048 | 2025-09-01 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 61762db1-d426-3c37-a37c-19e47d2aa12a | -7.69946 | -61.47401 | 2025-09-01 01:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 9f91b6d2-9b3b-3346-af52-773c68ad2ec1 | -7.66522 | -49.85767 | 2025-09-01 01:09:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 73bbaf7f-fb6f-366a-8abd-969d2c2b6fa2 | -14.76793 | -46.76132 | 2025-09-01 01:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 8e3b8543-e7e6-372c-9044-3f8b5e67b2bf | -11.07663 | -52.0695 | 2025-09-01 01:09:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8280ba97-ca81-3510-80ea-6994d4f552d4 | -7.73343 | -61.57318 | 2025-09-01 01:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c234af49-679a-329c-9341-9a809988bbd6 | -12.90764 | -56.94635 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 77874523-22cc-3d08-b755-6b77b0502034 | -12.22689 | -50.16232 | 2025-09-01 01:09:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6da9d852-1e13-35fe-baba-549059cc6a5e | -11.81428 | -46.42612 | 2025-09-01 01:09:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 41428f6e-dd05-3912-b39b-fde81011fbf0 | -7.69342 | -61.48045 | 2025-09-01 01:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b3b74b7d-50fb-3e78-bd0b-4e82d7f6243b | -6.33414 | -53.43942 | 2025-09-01 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 121eb03f-a42e-3e15-9e2f-5972584aa055 | -8.72291 | -62.4148 | 2025-09-01 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| c5e00ec6-f753-3b6d-8e32-6051db3741b8 | -8.73234 | -62.40783 | 2025-09-01 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.6 |
| d9b4181a-adca-3897-84fe-f5fb6dc6c7c4 | -10.28467 | -54.25095 | 2025-09-01 01:09:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 40537c5e-9933-3ca4-a61c-2fc149cc962c | -12.43232 | -63.93105 | 2025-09-01 01:09:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 2cd3b6ff-5aeb-3720-95e2-75ab24c0a03d | -14.42788 | -51.67468 | 2025-09-01 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 845fc4a2-dcd6-3704-89ca-abcd20ff6853 | -12.5746 | -48.19654 | 2025-09-01 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| d489086e-6310-3a48-9bea-0c016adb91d7 | -12.92781 | -56.96185 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 020ec786-f115-38dc-9a00-c7cc8418db25 | -6.85063 | -52.81426 | 2025-09-01 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 3983bc2e-4a45-3ee3-b177-0148ab8abf04 | -9.21441 | -47.11393 | 2025-09-01 01:09:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| b07ab341-e82f-3b3e-a15c-8804de64c94d | -10.88015 | -55.76617 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7bb60dd7-7864-355c-bb7a-5b265c3c08ec | -10.05423 | -48.12104 | 2025-09-01 01:09:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| ad8204cd-ead9-356b-9fc8-914d8d77352e | -11.81687 | -46.41919 | 2025-09-01 01:09:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 42.4 |
| df1f7fc0-fb75-3b69-8999-153f4e444d28 | -14.71284 | -49.44466 | 2025-09-01 01:09:00 | TERRA_M-M | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| bb4e80bb-c5a5-3b13-850f-23e407df7bd4 | -7.66217 | -49.86375 | 2025-09-01 01:09:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 31d46dd4-16f7-30ff-9336-e72f74efd666 | -8.73232 | -62.39802 | 2025-09-01 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.7 |
| fd25489d-1109-3b35-ba6e-42f30039b055 | -7.0951 | -63.0392 | 2025-09-01 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 8ec66525-ddc6-3971-b101-4e200300c4a9 | -11.51475 | -54.46909 | 2025-09-01 01:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 3ebbbbb6-680c-3777-b7aa-83d6df99f0b8 | -8.74374 | -62.40623 | 2025-09-01 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 9961f80a-e18e-3a30-ba23-ea18ef290a5d | -12.57912 | -48.21905 | 2025-09-01 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 05141dc2-8853-337f-984b-f1a108becf67 | -8.55732 | -63.02316 | 2025-09-01 01:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 853d462f-541c-3555-abf0-d29a6969a028 | -12.91896 | -56.96315 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 5d939c59-417e-3f1a-9acd-48b7d8279e92 | -9.27943 | -47.10781 | 2025-09-01 01:09:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| b9ae2985-a91d-3649-babd-22e387b60b37 | -6.34507 | -53.43773 | 2025-09-01 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| eb1bd479-9066-3fe7-8c33-88674af19951 | -7.2882 | -60.66616 | 2025-09-01 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 7ca31a93-d421-326f-b116-7f9fee07ccc8 | -9.4413 | -60.57699 | 2025-09-01 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3711e894-0c68-349e-a31a-11320e1420cc | -7.27548 | -60.64556 | 2025-09-01 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 51b2bfcb-22cd-3465-990f-35cb842f48a0 | -10.87884 | -55.75687 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| bb5a7b2b-b635-3d1a-b103-8a02db5b2319 | -11.03611 | -47.05033 | 2025-09-01 01:09:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 258.1 |
| 527a2117-5fe1-3297-94ac-02789436c036 | -13.01743 | -56.87835 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ed6d8edc-9a35-3306-b029-40c159343620 | -12.56437 | -48.22159 | 2025-09-01 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| d2acf73b-d4c1-32ab-bd10-ad4c8fcb83e8 | -6.43671 | -55.62632 | 2025-09-01 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 1a37446b-0f8e-3ef7-a28c-63b7c59f0f2b | -10.0387 | -48.12394 | 2025-09-01 01:09:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 9ff9b83a-ea77-3986-810c-ed0723da55cd | -9.87414 | -65.03641 | 2025-09-01 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 50869eef-0303-32ee-bae8-4ec8b73e383a | -6.43528 | -55.61621 | 2025-09-01 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 92a23226-0094-3875-8624-5b1d8ebc8fca | -14.77428 | -46.76654 | 2025-09-01 01:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 96c03b7d-b90d-3d87-88a1-9b4da4915b8f | -14.42561 | -51.66066 | 2025-09-01 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f03bd68b-cb9d-34a5-b348-bbb362fa91d9 | -14.60477 | -54.48415 | 2025-09-01 01:09:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3bc53157-e3ed-315e-8a46-1d9c90e1be46 | -15.23052 | -53.79189 | 2025-09-01 01:09:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8bd37f24-736e-3225-89cc-caccdc48d37c | -10.04309 | -48.08213 | 2025-09-01 01:09:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| da7dbf1c-1065-3423-9525-3cf45366ad19 | -12.93542 | -56.95151 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3d342e4c-2769-35b8-8cb5-0df43498fde7 | -15.81365 | -55.91553 | 2025-09-01 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a5cd07e9-694f-3bcd-898f-eb8a77875698 | -9.86239 | -65.03105 | 2025-09-01 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 337d8d6f-dd60-3df6-9815-e84817aaad65 | -7.07802 | -63.06417 | 2025-09-01 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bd821863-5c7c-345e-abeb-2e8f0eda8cf8 | -8.74186 | -61.8561 | 2025-09-01 01:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |


[Clique aqui para ver as próximas entradas](README6.md)
