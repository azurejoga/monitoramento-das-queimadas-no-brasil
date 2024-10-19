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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b2a1262-d600-3cfa-8746-dc681835f0a8 | -11.27225 | -54.23119 | 2024-10-19 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05ecce21-5394-3aa6-89f1-c77c5c99cea5 | -13.1379 | -54.92512 | 2024-10-19 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dff540df-ebe2-3a74-8403-6e145e0b6a04 | -12.50337 | -54.43204 | 2024-10-19 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8845a060-4d4e-37c2-a360-5c328bf3de37 | -12.50004 | -54.43149 | 2024-10-19 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f2d4552-34e1-3e23-ae54-29697244df56 | -12.49947 | -54.43504 | 2024-10-19 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40cd25ef-572c-31fb-99a4-290b164eabaa | -12.47156 | -54.48151 | 2024-10-19 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e0f65af5-2c37-335d-9448-08076a0e4a6c | -13.81875 | -55.23434 | 2024-10-19 04:51:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22aeee41-58f0-3a2c-99bf-dcbecbfcd835 | -11.9128 | -56.19191 | 2024-10-19 04:51:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5919fbcd-c57f-3020-bb7b-8792d2ea27f9 | -11.91214 | -56.19585 | 2024-10-19 04:51:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 021857e2-80ce-33bd-bbc9-ce161afa5799 | -11.9093 | -56.19131 | 2024-10-19 04:51:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76db3794-8c99-374e-a0ee-dfac178422f4 | -11.90865 | -56.19524 | 2024-10-19 04:51:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 316d1fef-97d5-38c5-9744-cdf211b25a44 | -14.35563 | -57.26293 | 2024-10-19 04:51:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1ef35d7-3fd0-31c3-a6b4-f7fd3139689f | -9.35575 | -57.60495 | 2024-10-19 04:51:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba25f446-54a7-3479-ad3e-2f418649e21c | -9.35268 | -57.59941 | 2024-10-19 04:51:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8066a1ec-c752-33e4-8889-5a5b5b117643 | -9.35186 | -57.60427 | 2024-10-19 04:51:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1be2e058-4e4f-37bd-9f74-e2ebd478fe7e | -6.78127 | -59.35674 | 2024-10-19 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05f93a2c-e511-3c56-9f3b-87340f7a69c4 | -12.16761 | -62.14711 | 2024-10-19 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66af616f-6ef2-3136-8860-5b8c7ea97768 | -12.16649 | -62.15298 | 2024-10-19 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0d8670f-d900-37a4-99fe-b5ced51490fe | -12.16149 | -62.15212 | 2024-10-19 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1e8de8b-d5f9-3338-86af-1eec93fff8a7 | -6.62596 | -62.93215 | 2024-10-19 04:51:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba978e34-a77f-3d40-8295-9cc04cde789c | -6.62578 | -62.93339 | 2024-10-19 04:51:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b37eaf74-9947-34e7-94b9-ebfd6a6eb16b | -6.62523 | -62.93619 | 2024-10-19 04:51:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30fe4a30-bb4e-360e-8b01-1234da144472 | -6.62507 | -62.93745 | 2024-10-19 04:51:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36bab1cf-8d6c-35b7-94d0-a15e79d80a3e | -6.62449 | -62.94023 | 2024-10-19 04:51:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69c51f90-ca77-3386-a923-5c19b6c97cf3 | -9.06532 | -63.66488 | 2024-10-19 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 578d89ff-cfe0-3223-91e5-99de8824e29d | -9.06452 | -63.66527 | 2024-10-19 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87fc8589-8280-3f37-b337-f398d6aa1ab3 | -9.05875 | -63.66789 | 2024-10-19 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d9d2cac-324b-3eb1-8192-96a391fa5127 | -9.05793 | -63.66828 | 2024-10-19 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7133eefd-ba0c-3f39-935b-4e0cc8d83625 | -9.70212 | -64.19283 | 2024-10-19 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a402690-660b-3bf0-b150-81461b377044 | -9.70109 | -64.18645 | 2024-10-19 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d7d4884-7970-39ea-8ebc-c82fa80f4e32 | -9.70026 | -64.19087 | 2024-10-19 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7145fe4-9e75-3b2e-bfff-66b2eac62d82 | -9.69943 | -64.19529 | 2024-10-19 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7336fd0-f7b2-3333-a5bc-9ada940b31aa | -9.69705 | -64.18724 | 2024-10-19 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce7666f0-6c67-30bf-9ace-1473b819ac2a | -9.69618 | -64.19166 | 2024-10-19 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89ad99ec-fdb6-3c26-a069-d3d8860f29ec | -9.69532 | -64.19608 | 2024-10-19 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6618bd5c-8ef0-31a3-8a62-56dd768d74fb | -9.69432 | -64.18967 | 2024-10-19 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dba88866-5424-3e8f-8551-3a06d9f560d5 | -9.69349 | -64.1941 | 2024-10-19 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fc49ee0-bd8f-384c-9af8-eed914c969a3 | -12.01117 | -63.51339 | 2024-10-19 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70daf75e-db32-3779-bdad-c778f892cb95 | -9.59723 | -64.56977 | 2024-10-19 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dff1d047-c2a0-3f38-9989-e84ba1f85844 | -9.59115 | -64.56851 | 2024-10-19 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ed389d1-5597-383f-94a2-569fa55262b6 | -16.81638 | -51.60707 | 2024-10-19 04:53:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd455324-c3f1-3212-a929-0c9659e7e4cc | -18.00027 | -42.59641 | 2024-10-19 04:53:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| d164ef2e-d53d-3201-980c-8325ae6275ec | -17.99373 | -42.59591 | 2024-10-19 04:53:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 351a4427-fe2c-3f74-b2c9-bc29980bb704 | -17.97334 | -42.0276 | 2024-10-19 04:53:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e4058b09-614b-314e-9481-3bf1a6783009 | -16.86804 | -42.10822 | 2024-10-19 04:53:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 89ba4452-e3c4-3f4b-9529-4e2e7db55d88 | -16.86466 | -42.1079 | 2024-10-19 04:53:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 01e784a0-b33a-3215-87c9-df46e1f9aef2 | -16.86142 | -42.1074 | 2024-10-19 04:53:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2997228d-b38c-39e1-bec7-88524bc8d6d5 | -2.9489 | -52.9174 | 2024-10-19 04:55:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 1fce9e8f-2307-3cad-9efe-0babceccecc9 | -2.9489 | -52.897 | 2024-10-19 04:55:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| b9480fb2-dd68-393e-bea2-03d3b7a8b6b5 | -2.9673 | -52.9169 | 2024-10-19 04:55:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 9811d3e7-50f6-30a6-9687-ddee1e252b1b | -2.9673 | -52.8966 | 2024-10-19 04:55:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| d9e558e3-f2ce-3e97-bb2d-89bc3d14132c | -3.4202 | -50.2164 | 2024-10-19 04:55:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 3147140f-b742-333f-aae7-f5c9c4f9df0f | -3.4203 | -50.1954 | 2024-10-19 04:55:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| b8376c62-a0ad-3a54-bbb1-c80882d498ae | -3.4387 | -50.2158 | 2024-10-19 04:55:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 13b56158-8b51-326e-907b-0fadb2044dbb | -3.4388 | -50.1948 | 2024-10-19 04:55:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 8fc844bc-9bbd-3f6c-a13d-bbc8e4c90ec2 | -4.706 | -45.8493 | 2024-10-19 04:55:31 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 220.2 |
| 8b35ac9b-59ae-3578-9dd6-dfadd757fa63 | -4.7061 | -45.8269 | 2024-10-19 04:55:31 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 254.6 |
| 1dae8511-6dff-31d5-aa0e-80060b70d3e6 | -5.5716 | -44.8927 | 2024-10-19 04:55:36 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 9a33a23c-2556-38ae-a47f-a122c4c2c88b | -5.5718 | -44.87 | 2024-10-19 04:55:36 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ee8a0900-f5c8-36e4-98f2-e1dfc69238ae | -9.0344 | -67.4641 | 2024-10-19 04:55:56 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 9f505666-e571-35d9-a5f4-f06332b31343 | -9.0345 | -67.4455 | 2024-10-19 04:55:56 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| d051708a-6f96-3d82-8f62-410007e7c029 | -9.053 | -67.4636 | 2024-10-19 04:55:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| f60b8b73-f534-3c92-b7b8-df6bb91b17d8 | -9.053 | -67.4451 | 2024-10-19 04:55:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 95298a06-0675-349a-a8f7-7405c78d9d3c | -12.5147 | -63.3014 | 2024-10-19 04:56:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 8274904f-7259-33ce-b28b-60155e2321bb | -12.5149 | -63.2822 | 2024-10-19 04:56:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 44392e53-e5cc-3482-a4bc-410f3eb7aecf | -3.4388 | -50.1948 | 2024-10-19 05:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| a3d3492d-de42-356a-a531-213ede97a30c | -3.4387 | -50.2158 | 2024-10-19 05:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 7977bf3f-331c-374c-8085-027b80c1afeb | -3.4203 | -50.1954 | 2024-10-19 05:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 3ea0771a-40d5-349d-9484-d3ea609efd5c | -3.4202 | -50.2164 | 2024-10-19 05:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| bcbae29c-56db-3cc9-aeed-ca19905e13ff | -4.7061 | -45.8269 | 2024-10-19 05:05:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 252.8 |
| b2e7e871-0df8-35ab-bb33-e1f5a08fd186 | -4.706 | -45.8493 | 2024-10-19 05:05:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 217.4 |
| 8cbe21c2-1a35-3f8b-a8c8-f49299235f4e | -5.5718 | -44.87 | 2024-10-19 05:05:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 5bc30708-a5d5-3f67-af4c-d0a9b75e225d | 1.72971 | -50.99559 | 2024-10-19 05:12:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6cbe7de-9a4d-336f-a8dd-23ed84cc895d | 3.05346 | -51.46864 | 2024-10-19 05:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca49e8bc-02a7-3c07-8043-71eed8b2cf04 | 2.77972 | -51.41905 | 2024-10-19 05:12:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d445e55d-5223-3743-bb28-87b808d1387d | 2.48189 | -50.98943 | 2024-10-19 05:12:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b36a4279-e746-3e33-88b0-5083d9f74716 | -3.95875 | -65.25153 | 2024-10-19 05:14:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 418df88e-14af-3c3a-8596-0cc4f1d119b8 | -3.95798 | -65.25619 | 2024-10-19 05:14:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| feea50ec-3c97-3155-be5b-f3a8345c4848 | -4.7154 | -46.03675 | 2024-10-19 05:14:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cdaf70e0-0ec4-3da8-b54d-6d42fd6eb4aa | -4.71127 | -45.84808 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a9a7b663-beb9-3b5b-8874-ee3103570072 | -4.71043 | -45.85393 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f5cf56f3-cdf5-3789-83fb-e8bb8199dff3 | -4.70858 | -45.83882 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 8797c42f-b397-36f7-b821-c3e40a5344ef | -4.70774 | -45.84497 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 229eec68-cb9c-3618-a14c-3db913e4844d | -4.70693 | -45.85091 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cf50e871-95ca-36d8-a1bf-14acd8375f28 | -4.70632 | -45.8348 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| cd2de6f7-585b-3944-9a0a-76c9fa992dec | -4.70615 | -45.85659 | 2024-10-19 05:14:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 37bdcecb-08c9-33e8-b127-37f9882198ea | -4.70548 | -45.84066 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| f7275324-1131-3508-8ca3-2ca4d20c1228 | -4.70462 | -45.8467 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 987ab613-b770-3bcb-825b-e44f4979ce2a | -4.70377 | -45.85261 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c461c451-dc53-31e3-b2a2-63884a5018d4 | -4.70264 | -45.8321 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ff9c2240-f142-3da7-ba8f-b7ec0ca9661c | -4.70188 | -45.83765 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 765c73f9-2f2c-3115-84b2-ba1c5ec0d4a3 | -4.70108 | -45.84355 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 3cb10fb1-5721-3b8d-a23d-2644ba956fed | -4.70028 | -45.84947 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 637ea7ce-453d-3d47-8ef4-8751d932675d | -4.6996 | -45.83386 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| ee006b20-512c-37a6-9a80-de3430db4908 | -4.69949 | -45.85525 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 45376d7f-b028-3241-9b9a-ea2fc526aca4 | -4.6988 | -45.83946 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| d1e9dee5-fbb1-32b0-a9a1-3e66d60a045b | -4.69797 | -45.84526 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 8b89cd70-d590-3d4b-90fa-194fb150291c | -4.69713 | -45.85117 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b13c8290-3ffa-3cd9-b590-9a9b44907142 | -4.69439 | -45.84238 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 44.8 |
| fa9a66ab-43a9-309a-a496-881843746cfc | -4.69361 | -45.84817 | 2024-10-19 05:14:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 35.6 |


[Clique aqui para ver as próximas entradas](README38.md)
