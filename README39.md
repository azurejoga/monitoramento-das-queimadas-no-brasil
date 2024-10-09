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
| b997f0e8-70dd-31a8-94aa-4d924ce0601b | -3.8196 | -41.5979 | 2024-10-09 01:25:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 152.6 |
| e77b4174-b5c7-3bd6-b49a-293d19061000 | -3.9021 | -46.4689 | 2024-10-09 01:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f598cad4-9358-3c0f-8dba-2e4ab74fbf8e | -3.9023 | -46.4467 | 2024-10-09 01:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 3add9fa0-d173-34d1-ae65-59706fc55d2a | -3.9207 | -46.468 | 2024-10-09 01:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 95a1f994-cb72-3ae5-a0ba-d0907ef40a7c | -3.9208 | -46.4459 | 2024-10-09 01:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 63d5c89a-56c1-3c59-aacf-dab8da961393 | -3.9393 | -46.4672 | 2024-10-09 01:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 2ba7928f-f7c0-3687-b09f-acfeb0072525 | -3.9394 | -46.445 | 2024-10-09 01:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 191.3 |
| 6817be38-aaaf-30c4-b183-85b5be9acc9f | -15.418 | -60.0051 | 2024-10-09 01:25:31 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc105a3e-99fa-30e0-ba47-c1e825c7bb93 | -15.4195 | -60.012199 | 2024-10-09 01:25:31 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e98bcfaa-ddb0-38e3-b32d-71f5486a0269 | -14.3354 | -57.576302 | 2024-10-09 01:25:39 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81aa5a0a-1b77-34c5-84ce-ae1df237de95 | -13.3017 | -53.704399 | 2024-10-09 01:25:41 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d54e4e2d-003c-3402-be8b-08fac5c498dc | -13.3048 | -53.717098 | 2024-10-09 01:25:41 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1561113-bc9e-39f4-ba63-e211290086e1 | -13.292 | -53.707001 | 2024-10-09 01:25:41 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bfa94943-d104-3090-a2d7-9da4ca4a42d4 | -13.2951 | -53.7197 | 2024-10-09 01:25:41 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f33a7db6-34c2-3572-be91-c97b336ba76b | -13.2822 | -53.709499 | 2024-10-09 01:25:41 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27fac971-4067-333d-ba43-032f9c7ff361 | -13.2854 | -53.722198 | 2024-10-09 01:25:41 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bae2290e-25c7-37cb-9152-2d63ffa45ee7 | -13.2886 | -53.734901 | 2024-10-09 01:25:41 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3aef5eb0-094c-309d-8391-850554caf4ce | -6.7613 | -60.0751 | 2024-10-09 01:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| c412825f-fcf1-3585-8eec-11b05be52179 | -6.7614 | -60.0559 | 2024-10-09 01:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 4dc90aa9-eef6-34a6-a233-7bfffa948735 | -6.7615 | -60.0367 | 2024-10-09 01:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| dcccffdb-aa00-39fa-b478-6f652ee667a2 | -6.7797 | -60.0744 | 2024-10-09 01:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ed53f8cd-edfa-3f79-b4bd-ae8a3d1695a3 | -6.7798 | -60.0552 | 2024-10-09 01:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 227.7 |
| 3072955a-457f-3ddc-919a-54c65dba4cf1 | -6.7799 | -60.036 | 2024-10-09 01:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 1f2090ad-3af4-3914-80bf-f28155e9050f | -7.0232 | -59.4111 | 2024-10-09 01:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| ac92a89f-02cf-3a5a-8b9b-71607436f08f | -7.1871 | -59.7893 | 2024-10-09 01:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 1ee2f477-4bf8-3e4b-8950-891566557d65 | -7.1873 | -59.7701 | 2024-10-09 01:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 1a108cc5-f96f-3721-9dd7-e56d9ee60094 | -7.2057 | -59.7693 | 2024-10-09 01:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 6bf0f004-2095-3653-9a5a-71a7d7244776 | -7.2435 | -59.633 | 2024-10-09 01:25:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 691acea0-86d5-3603-8a8f-8d59a6447c4d | -7.2436 | -59.6138 | 2024-10-09 01:25:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| b3752f5d-7f1c-3a84-972c-be4bb1b50d5d | -7.2619 | -59.6323 | 2024-10-09 01:25:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| b1954a97-eead-3c83-afff-4f79e77dcf66 | -11.9989 | -51.025002 | 2024-10-09 01:25:51 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c8651508-6fef-3a99-b67e-f7ec40a46cad | -12.0042 | -51.045101 | 2024-10-09 01:25:51 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4eaee45c-2c07-3b47-8a45-5a34db6653f8 | -11.9893 | -51.027599 | 2024-10-09 01:25:51 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2d0a710f-1aef-31cd-9496-834144c5b685 | -11.9946 | -51.0476 | 2024-10-09 01:25:51 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be6ab02c-2910-36ac-a49d-be94fad27c93 | -11.9796 | -51.030201 | 2024-10-09 01:25:51 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a12395e9-a5b9-32cd-bb37-c057ed3eaadd | -11.9849 | -51.050201 | 2024-10-09 01:25:51 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b46326b5-6af1-3385-8005-63f43e125c04 | -11.97 | -51.032799 | 2024-10-09 01:25:51 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2c5976a1-8664-33ba-bc98-833f97ca5dc7 | -11.9753 | -51.052799 | 2024-10-09 01:25:51 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e4901880-2312-345b-bd2f-704e2483b1be | -11.5469 | -49.891701 | 2024-10-09 01:25:53 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec04420f-c00a-379d-9fbc-1b3ca95857e1 | -8.4919 | -48.6476 | 2024-10-09 01:25:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 176.6 |
| ad47d3a8-4e59-395e-a09d-5d6aebb29359 | -8.4921 | -48.6259 | 2024-10-09 01:25:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 124.0 |
| a9811ece-2153-362b-b01b-0c01706f5993 | -8.5107 | -48.6459 | 2024-10-09 01:25:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 76.2 |
| ebfea083-b35d-32eb-ab9b-62584f176571 | -8.5109 | -48.6242 | 2024-10-09 01:25:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e320a554-9207-3594-8df5-a2c8982e90d2 | -11.5373 | -49.894402 | 2024-10-09 01:25:54 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd60be9f-74e8-3c0d-bd00-cba30a485538 | -12.67 | -54.705502 | 2024-10-09 01:25:55 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66523392-38c1-39aa-b86d-77bc9cd66899 | -12.6575 | -54.696701 | 2024-10-09 01:25:55 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59917e9f-3e50-32eb-9f84-bb7d9c19288e | -12.6602 | -54.708 | 2024-10-09 01:25:55 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3f44b0eb-979f-36b2-bbf6-cf4ffe21dd9d | -13.9095 | -60.211201 | 2024-10-09 01:25:56 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b126c189-47c2-3208-8276-989fc44d91b2 | -13.9111 | -60.218201 | 2024-10-09 01:25:56 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 485336e2-bad9-3d9e-b2a5-d7b45f0f13f7 | -9.5721 | -40.3475 | 2024-10-09 01:26:00 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 207ae733-a506-32a8-a014-576fa20db5c5 | -13.7391 | -60.606098 | 2024-10-09 01:26:00 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20276869-6723-34f7-9ba4-81c9407c28ae | -9.4635 | -66.7469 | 2024-10-09 01:26:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 679e5868-6fe2-3510-b174-af127907389a | -11.3183 | -50.945099 | 2024-10-09 01:26:02 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58df7a08-8cc5-348e-ae59-ba9c6e680cc6 | -9.9292 | -58.1301 | 2024-10-09 01:26:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 525c479f-8868-339e-8efb-5ec11bc10839 | -12.6064 | -56.501301 | 2024-10-09 01:26:03 | METOP-B | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41b65cb1-03c7-3f25-8974-1c999cf8187a | -12.6085 | -56.510201 | 2024-10-09 01:26:03 | METOP-B | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ee9d97b-08c0-39ef-a6c4-cc6cbfceb022 | -10.3656 | -64.8262 | 2024-10-09 01:26:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 979cc43b-7b02-3620-b6bb-1cfb4dcc0b21 | -10.3894 | -61.2502 | 2024-10-09 01:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| d703844e-1274-3df8-a209-ceefcd13577a | -10.3895 | -61.231 | 2024-10-09 01:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 6cdbf605-b519-303c-ae19-0369b80f51a5 | -10.4287 | -60.9979 | 2024-10-09 01:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 12e9c33a-3efb-3859-ad07-deb1696bf2f4 | -10.6068 | -55.9169 | 2024-10-09 01:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| ea361103-cd82-3733-a1fa-9163688df98d | -10.6253 | -55.9355 | 2024-10-09 01:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9add4d4c-f41b-3413-9f3b-820074f8a1d2 | -10.6256 | -55.9154 | 2024-10-09 01:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 174.9 |
| 9f4d49c0-a09d-3949-aaf0-17dda69b3c9f | -10.6258 | -55.8953 | 2024-10-09 01:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 6d2bf514-b410-32d8-813d-de1d10467963 | -10.6444 | -55.914 | 2024-10-09 01:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 38.3 |
| e39ef163-6de6-37f1-a0bd-77cf5b413647 | -10.6446 | -55.8938 | 2024-10-09 01:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| ee1a294b-133d-34a8-a0dd-87977978c29c | -13.5194 | -61.725498 | 2024-10-09 01:26:07 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c49e5e10-5e56-33b9-bb65-b09df3996a52 | -10.8754 | -63.9169 | 2024-10-09 01:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 109.7 |
| ee3752f1-59e1-3eee-8ac1-c9c8a59fca5a | -10.8755 | -63.8979 | 2024-10-09 01:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 4ff32156-63e6-39fa-9de9-b39862deecb3 | -13.1107 | -60.136299 | 2024-10-09 01:26:08 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62ad9bb9-2ded-3270-bfc5-8f059817516e | -13.1122 | -60.143299 | 2024-10-09 01:26:08 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b618fcb3-b8c0-3529-8fd2-e42bc5c137eb | -13.1138 | -60.150299 | 2024-10-09 01:26:08 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 176939ed-b0f4-3bc5-ad12-25e7abc47d35 | -10.8925 | -64.1623 | 2024-10-09 01:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 7d28ea8d-603f-3247-9480-e08720a38434 | -10.8941 | -63.916 | 2024-10-09 01:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 938222db-4c22-3637-9762-2e9b58a98d05 | -10.9112 | -64.1615 | 2024-10-09 01:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 111.4 |
| ca575330-2a16-3176-b6b6-555b545d71de | -10.9113 | -64.1426 | 2024-10-09 01:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 11294961-bccc-3b61-94d9-1659c3b4173f | -13.4503 | -61.881802 | 2024-10-09 01:26:09 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 154bd4e8-f6b1-3e3c-9d2d-c0682e1dbee8 | -13.4405 | -61.8839 | 2024-10-09 01:26:09 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3fb738dd-31b8-3c86-abab-45d2af753ff5 | -11.3283 | -50.9805 | 2024-10-09 01:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 121c63c2-be92-3769-902d-8c70fe239786 | -11.3286 | -50.9592 | 2024-10-09 01:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 72be7efb-b9fc-38f8-b827-117c940a2272 | -13.4241 | -61.9034 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d3c8cdb7-9430-3b98-8cca-0c0ae2703665 | -13.4258 | -61.9109 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ecac512e-ec60-3089-9e1a-6360b535049a | -13.4143 | -61.905499 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5b24ed80-d4d3-329c-b36e-21d3ba9b6582 | -13.416 | -61.912998 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 68d0617c-cad6-3db7-8a93-0f08755c1398 | -13.4176 | -61.920601 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 76d86b4a-d6a0-393a-97f1-8fc106627abe | -13.4045 | -61.9077 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9979cbc-5098-3fe0-bdcf-824aac2a5155 | -13.4062 | -61.915199 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fa20117a-e4f5-3634-ab7e-2beecb1622d3 | -13.4078 | -61.922699 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6afae81d-e599-3f8e-ac38-b516a874b161 | -13.3931 | -61.902302 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8b2a93ed-80c0-372d-9828-e738a1cb35e5 | -13.3947 | -61.909901 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f719a036-7aad-3bd2-8f3f-05d9519f665d | -13.3964 | -61.9174 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a4bf579d-bc63-3e2a-b019-e34b57dd89cd | -13.398 | -61.9249 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cffea361-b785-3ee0-b338-bb873face07a | -13.3996 | -61.9324 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff33d56-689a-3495-b94e-91f523dad9a1 | -13.4044 | -61.955002 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ee009728-fb52-394a-9a31-d39fc27b4265 | -13.406 | -61.962601 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 172680b5-12e0-31ed-87cf-8b89aaded45b | -13.3849 | -61.911999 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2ce717d3-fd74-3e05-a6f1-526555507077 | -13.3866 | -61.919498 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cfca98eb-fa23-3b08-82e6-f472365f5859 | -13.3962 | -61.964699 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2cf292a4-754d-3384-b369-1b808f857d1c | -13.3784 | -61.929298 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ae4fd3d2-cda9-3405-b7b7-33531daefd0f | -13.38 | -61.936798 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README40.md)
