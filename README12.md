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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a91495fc-c21e-3e6a-b2dc-1a013ef80987 | -12.3611 | -53.15784 | 2026-08-10 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25230099-7932-3a74-9076-c28533cba5ed | -11.92265 | -55.90199 | 2026-08-10 04:53:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e485e05b-d3f5-3707-a25f-1446832ddddb | -13.85546 | -53.67329 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 326d3c7a-0c8a-386d-896f-710f4ad0089b | -13.86097 | -53.65952 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9bc4e14d-c27a-3922-b058-bbccc7ea2dac | -8.96032 | -60.54211 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 03b2baf9-f968-350e-94b0-1a26b9e5a21c | -15.05246 | -46.54814 | 2026-08-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d82c849-e240-34e2-8a78-6d4d92a2efee | -13.78408 | -49.72431 | 2026-08-10 04:53:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28b80bf3-437a-3ad1-b47e-43798c6d953f | -13.84862 | -53.89496 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fa9caea-d8ef-3207-a886-12ed85bf7586 | -13.63099 | -46.21712 | 2026-08-10 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 28cb45b8-aed1-311f-a3b5-88dca9830922 | -8.94806 | -60.52974 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9f211b82-c36d-39e5-8688-7075e842bc1a | -12.10649 | -47.19595 | 2026-08-10 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c05be21f-52e9-3c18-81dc-347016d22160 | -8.68926 | -62.86887 | 2026-08-10 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62cc618b-8999-3910-82c8-db6f0c98e630 | -11.91459 | -55.90837 | 2026-08-10 04:53:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b61d6fe2-5dc9-3924-96b7-eba0d85f87f8 | -10.06086 | -60.50375 | 2026-08-10 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30cb0827-3877-3473-b1af-c9d29ccf09f3 | -10.94084 | -57.11399 | 2026-08-10 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad196ed1-269d-3fe0-a540-8a8c6839b9bc | -11.22076 | -54.02595 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ed14248-8c56-3879-8fd8-25299d6181f4 | -11.04283 | -49.77356 | 2026-08-10 04:53:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bc2f071-595b-3557-bc54-53c653fde051 | -8.95738 | -60.60128 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fc18aac-197e-35ff-b116-224e3e21a75d | -13.84476 | -53.89798 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 579b9060-afec-3ca6-b24b-8787be97d6b0 | -12.35924 | -53.1506 | 2026-08-10 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62ecfa16-4a79-3d6b-a04e-58c48c68655b | -13.8006 | -53.91998 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64035865-e071-35fe-a0e2-328ac5955b9d | -8.95696 | -60.55013 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 11cce7f4-5c67-32f8-a0e3-927315518d0f | -11.22242 | -54.037 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10727609-09a8-3307-bd6e-c117e727fbcc | -14.34503 | -52.03805 | 2026-08-10 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce66de57-a0fd-38b0-9a4b-fc839936b42e | -11.83979 | -56.94532 | 2026-08-10 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9ae34db-6fde-3979-b02f-eaae11ccb464 | -13.8483 | -53.69778 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 08ac0170-53b6-3c72-be81-b679e225db35 | -8.8939 | -60.59175 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3fe38533-d6f6-3b89-9bfe-56d753ed697b | -13.85549 | -53.69531 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4b75bd96-243f-35c3-960a-286154b3be8c | -13.8571 | -53.66256 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0ce6fef-1c27-302a-a224-d8eced695078 | -14.3016 | -54.93651 | 2026-08-10 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fff18f4b-9f77-34ec-a8d4-60167903ccbc | -8.96163 | -60.5509 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 104561f8-ce61-304d-8f84-76caa07652a7 | -11.99224 | -53.45927 | 2026-08-10 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da96dd02-a322-3db3-9e5d-1fe360b9aeff | -16.06376 | -50.80484 | 2026-08-10 04:53:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62b2ff77-65bd-3f08-bd46-fdb65b9e7675 | -16.05968 | -50.80631 | 2026-08-10 04:53:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9f538ba-0d5b-3f9a-8718-435efe1917b8 | -12.10588 | -47.20055 | 2026-08-10 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| b80e1076-c23d-348c-a7eb-5f0e4db9454f | -15.03982 | -46.5705 | 2026-08-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| b06b016e-2d1e-34fe-a90b-2fb5c61bf58a | -8.68794 | -62.87603 | 2026-08-10 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b575f9a-9cc6-3884-b25c-973cec82f97a | -8.677 | -62.87409 | 2026-08-10 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae507678-b7f7-3883-b892-1872f45a07dd | -12.34705 | -53.16331 | 2026-08-10 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c3b23f6-325e-362d-81a4-b032e4dc69e3 | -8.95032 | -60.53371 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0ee38aed-8235-3f6d-85ef-d00cdff53d97 | -8.96074 | -60.56755 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ad695cdd-a298-3feb-8317-4c477f278872 | -13.78017 | -49.72375 | 2026-08-10 04:53:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 413b3bd0-1a44-34a2-a283-288f5176cd5d | -15.13383 | -52.69598 | 2026-08-10 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 743da24e-fda2-34cb-b67b-e6d3872bf39d | -8.95694 | -60.5617 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 707283fd-aea3-38fd-bef8-8fd4414ed713 | -14.41063 | -45.65302 | 2026-08-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc11b304-fd07-3fd4-a17f-a6bccc3117e6 | -11.62412 | -51.08934 | 2026-08-10 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b2e0726c-1de1-3f1f-893f-e35895fa210b | -15.17547 | -52.74523 | 2026-08-10 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 822472b1-7434-362b-aec0-514b65be1fb1 | -9.81697 | -54.89376 | 2026-08-10 04:53:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7b622c2-6c36-31f5-8ce6-1f584826ad5a | -16.44926 | -51.06041 | 2026-08-10 04:53:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 583dd033-d57c-3ad9-b5a9-a4c748ee4243 | -11.21966 | -54.03296 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 832c4c9d-a0cb-32a1-b5bc-36fbfd796fed | -13.74961 | -56.05109 | 2026-08-10 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6077696c-28ad-31dd-ab53-347e4c3d1264 | -12.09175 | -47.20316 | 2026-08-10 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9ae880da-3f23-3619-adac-9c91e3d0eb6f | -11.21911 | -54.03646 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 243047cd-086a-32b0-aa3f-1db712fde71d | -11.16856 | -54.80723 | 2026-08-10 04:53:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa125af7-8ca2-3c30-b7d0-41dcf391e5fe | -8.89477 | -60.58682 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 28609e75-c354-3e0d-a35d-55de27b99071 | -16.33302 | -46.89014 | 2026-08-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4861ff1-43c7-3590-9ba4-d0f1cad9e3ea | -9.81419 | -54.88961 | 2026-08-10 04:53:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14b73d88-210d-3cbe-aea6-f98c2ac3aa64 | -14.40141 | -45.64205 | 2026-08-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21d217b7-9b79-3308-bf1f-7534eb4e9c1b | -13.63356 | -46.22242 | 2026-08-10 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17b11b63-e0c0-3717-a61b-4e2f5febbfd6 | -13.63421 | -46.21727 | 2026-08-10 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa8cd332-3b1a-3678-8a41-8aa4da874d4f | -11.16913 | -54.80365 | 2026-08-10 04:53:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1de953e9-b8ba-334a-8626-c16b6a3f32f8 | -15.04544 | -46.5652 | 2026-08-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0e34b0ae-7ddb-3192-8c0b-6722c2052843 | -11.24209 | -54.87844 | 2026-08-10 04:53:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ed03943-41b9-3da9-8362-ba61fa8f6fff | -15.08245 | -52.68782 | 2026-08-10 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21b0e685-2bac-3100-9350-017a85e92dc4 | -10.93791 | -57.10907 | 2026-08-10 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 68d32773-b401-3a15-afb4-57a42fee9e39 | -13.86375 | -53.66363 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c2b73f13-8203-3a02-b258-991614da0b5a | -8.9634 | -60.54106 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 127255b5-799a-3239-a55a-210ddaac9a9c | -11.49003 | -54.60419 | 2026-08-10 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b02ec408-e219-3d45-a378-e52d2d4034e7 | -8.95186 | -60.53551 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1f27dc0c-50e2-3045-8602-776dfe826aff | -8.95717 | -60.57568 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b133d53-f9ee-35d2-9bf0-582882dedbbf | -12.19835 | -52.86477 | 2026-08-10 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1614f84d-fa65-3773-8aa2-cabc5a8a640b | -15.0469 | -46.55289 | 2026-08-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e63251a9-3efa-32f4-904e-974a01f51ac1 | -11.47268 | -50.55993 | 2026-08-10 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9ef745e-fe39-3b58-b9eb-ba5580702616 | -8.95987 | -60.56067 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1bf881dc-dcff-30d1-bfe8-9843da47271b | -15.08189 | -52.69167 | 2026-08-10 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c538008-1bc3-3e5a-9c98-09e2b8262d29 | -11.62294 | -51.09744 | 2026-08-10 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bab309b9-f754-3d57-841b-d698e2873c18 | -8.95784 | -60.54525 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2a24e751-54d0-3dad-84aa-32b5b0a4d93e | -16.4486 | -51.06512 | 2026-08-10 04:53:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b03105f-647d-35d8-8c66-c11c921da630 | -8.9434 | -60.52892 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b315a354-1c4c-379a-bc39-490ea82a5781 | -15.07582 | -50.37764 | 2026-08-10 04:53:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42be6b3d-7c1b-3df1-aece-a24d06f4225d | -15.04475 | -46.57091 | 2026-08-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c845c008-c214-3a8c-b293-07024ee43a81 | -15.05039 | -46.56548 | 2026-08-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e0197754-3407-3601-b846-e029fb85b54b | -10.07632 | -60.49919 | 2026-08-10 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a08b0db3-efee-392e-83d9-305811f4b430 | -8.89272 | -60.57113 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 5a53494b-9a16-3a5e-a37f-97d76f0ae7fc | -13.63528 | -46.22315 | 2026-08-10 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 00d37402-5eaa-338b-bc19-7e0da14eb5cf | -8.97362 | -60.5377 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0d550df-c150-39ae-9a35-4cfa9a222cb1 | -14.00983 | -53.84079 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eae8e069-7eec-38b2-95a1-294d12dd1409 | -13.85604 | -53.69172 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8aa854cd-5b9b-34a2-815a-3090721697bc | -8.89185 | -60.57606 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 559b724e-e7c2-3003-93e3-c07b0fbc9de2 | -12.00009 | -60.50895 | 2026-08-10 04:53:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c68e546c-0155-3f09-8a8a-1793a8ea4fd0 | -13.48989 | -51.80535 | 2026-08-10 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff3a07ef-891b-3683-912e-2fedccb810e3 | -11.47329 | -50.55566 | 2026-08-10 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed977750-02a0-349a-8222-54b50d5ee26b | -11.2136 | -54.02839 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6934fcd7-9e2c-39b7-b49c-c9879c048c46 | -11.20974 | -54.03136 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cd2b65a-581c-3eeb-ac4e-76ea47bcc05e | -11.84268 | -56.95007 | 2026-08-10 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a62e723f-ff1a-3cc4-b8d1-bd68318234de | -8.95559 | -60.59747 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4a1de8da-f3cf-3881-bc73-6874db690444 | -15.08588 | -52.68835 | 2026-08-10 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac5c3fc2-3612-3f2f-825a-2c6d97ba7c27 | -11.62353 | -51.0934 | 2026-08-10 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 167f3822-9617-3097-95fd-53d8c716332c | -14.00651 | -53.84025 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eead5a14-3425-3c94-8d90-b68eaef9cd9a | -11.92607 | -55.90258 | 2026-08-10 04:53:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README13.md)
