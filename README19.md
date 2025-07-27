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
| c956cce7-db12-3296-aaa2-68448e9be4d8 | -12.03942 | -45.84919 | 2025-07-27 04:59:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 161e5ad0-fbf8-346e-bc92-4e5d4cad6bc0 | -12.68415 | -46.98552 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c899163c-9e84-3228-8eaf-20ceb6b53c6c | -13.08842 | -47.36882 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3d5535d-ce6e-31cd-8edd-6368a1f84307 | -11.30166 | -55.11948 | 2025-07-27 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f625adb5-47bd-3bcf-b883-d1f2950d0a66 | -7.90194 | -63.52537 | 2025-07-27 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5794ef66-0026-3ea4-920a-9749de463ae7 | -8.97762 | -61.51343 | 2025-07-27 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaee83c3-7e4c-3eda-8076-2d6d89aec0c3 | -11.97631 | -46.70606 | 2025-07-27 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14c08da4-f040-35df-83f9-db182b326586 | -8.68442 | -64.22579 | 2025-07-27 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b05f1b2-7acc-332a-ae3c-f0c7a86a662a | -12.68529 | -47.0182 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c1e6118-1bc7-340d-bb30-5887b655c251 | -8.07878 | -63.86503 | 2025-07-27 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74cac3b7-2387-3471-9f0e-a736ae2dd680 | -10.04451 | -59.10408 | 2025-07-27 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee530335-ca76-318b-bf8b-792c41762074 | -13.71741 | -45.66658 | 2025-07-27 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2ee6d02-a595-346c-a5cd-a73b90db6d39 | -15.19099 | -43.27989 | 2025-07-27 04:59:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d072c371-3fc5-31fe-aed6-c97344dae4d3 | -10.29721 | -57.04994 | 2025-07-27 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8cf3f4c-87ca-3548-9bbf-38edcc4b9862 | -10.04077 | -59.10346 | 2025-07-27 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7378b02d-9098-37fd-86e5-34de723e4a6f | -12.68212 | -47.00165 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 580fa503-a457-3008-91cf-4b5de57c3ba6 | -12.0454 | -45.84623 | 2025-07-27 04:59:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7009d346-2646-3e7a-9c8e-c5f20694b56d | -12.67665 | -47.01915 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1f6e4232-ef03-32f9-8ba4-b9f24ac33e5f | -12.67615 | -47.00732 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e794fcd-3141-3458-abab-f213816382d0 | -13.72177 | -45.67952 | 2025-07-27 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee2d2062-3fad-35f7-bfb7-aef76dcc3f01 | -10.84028 | -46.68762 | 2025-07-27 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d10bb4c3-7348-3c9b-8823-d3ecbec57858 | -13.08182 | -47.3376 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cbfddc2-daf6-31e0-9828-deb5ba3b8b24 | -12.71122 | -46.28125 | 2025-07-27 04:59:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 369b9b42-2dc1-36c0-b6bf-fa4894d35f1e | -11.10953 | -45.12311 | 2025-07-27 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fde29b63-cfba-340e-96cb-d7aea9c5f207 | -10.04373 | -59.10866 | 2025-07-27 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2086b6e3-9d31-3016-9356-3f0cc6b30830 | -13.10064 | -47.35309 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e69ad36c-a0d4-37db-b48f-70762c37ec4c | -10.04309 | -59.10588 | 2025-07-27 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7fa0eb84-75eb-364e-9a39-d0d5ed09a673 | -12.71058 | -46.99898 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f3164e5-d6e9-357f-9156-e423a2a7c86d | -11.94134 | -63.85102 | 2025-07-27 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e166260-9075-3f78-b49e-5828b51efaf8 | -13.13922 | -47.33325 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ceabb7c-33b4-338b-958c-07598acc81dc | -13.09389 | -47.36623 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7beb37bc-ebe0-3e2e-9b91-39f7ae9ff3dc | -13.12598 | -47.35697 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 57a8c6da-4d56-3cb1-8be1-251c7d0e43fb | -12.68406 | -47.0009 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71202dea-19e7-3fc9-a5f6-c47ce9fc7241 | -12.68168 | -47.00516 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b712728-6d77-38a3-8f14-b6ae3fa385dd | -13.0964 | -52.13757 | 2025-07-27 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e412d4a-722f-30ee-9223-d2feb8994048 | -11.30111 | -55.12299 | 2025-07-27 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d847fcab-1b1e-3902-ae51-f8b4f6466acf | -13.13958 | -47.3303 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4755c632-aed4-3cbf-80d5-434e4dbf6ef0 | -12.70957 | -47.00733 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2df6ee83-5fad-3df5-bbcc-dc95251cfa7d | -13.72224 | -45.67537 | 2025-07-27 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3aaf9f49-9bf7-3fb3-8b43-188eb7a57b93 | -11.2978 | -55.12246 | 2025-07-27 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e727c224-352e-3f0d-b07b-53c40b251fce | -12.70545 | -46.99792 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eeb2613b-00db-37ff-ba0a-363904eec1b3 | -12.71092 | -46.99619 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 857c8b95-579d-399b-8d2e-84105e63c472 | -15.99708 | -42.64993 | 2025-07-27 04:59:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| aad9a204-06ea-3252-ae77-fdb15985471b | -8.07291 | -63.86739 | 2025-07-27 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba23a7cc-9a9f-3ca9-868b-e813b03d8cd9 | -11.97591 | -46.70919 | 2025-07-27 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 898dca58-32be-3c16-89a7-4bf94baed549 | -11.93641 | -63.85011 | 2025-07-27 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff2af8b6-4af0-3fdd-b789-512e71dc29ac | -10.28035 | -64.4564 | 2025-07-27 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbd3b9f1-8436-3fcd-8bec-b4c828d458d8 | -8.60984 | -64.03994 | 2025-07-27 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77ea3005-d23c-32de-a0f2-e4f32936a940 | -12.68216 | -47.01694 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cc8c4f1b-b046-3359-8f8e-d7ae1300fd01 | -9.02758 | -59.76427 | 2025-07-27 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 70dbde26-dd7f-380a-adb9-46591cccbdfe | -13.09268 | -52.137 | 2025-07-27 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab1552d4-b2c7-3f41-89bc-ed6463923a71 | -12.71609 | -46.99689 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 901f4321-7b3f-31da-be5b-e0820fd0bc6f | -12.00757 | -45.83339 | 2025-07-27 04:59:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bc40d3c-b051-3f7a-b7e4-efbad8b6f421 | -11.97106 | -46.70556 | 2025-07-27 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9251f844-0585-313f-a5b3-08277438c083 | -12.67864 | -46.98748 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6a0f0c0-89ea-3765-be48-c375fe115230 | -11.52153 | -54.6844 | 2025-07-27 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b87b50a-51e5-3686-a0c1-0b1a054a0cdb | -11.96545 | -46.7079 | 2025-07-27 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85569310-294a-3e57-966c-da4836cb216d | -6.6575 | -58.8468 | 2025-07-27 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 39804a86-eb40-3f86-879f-1181589407f8 | -6.6389 | -58.8669 | 2025-07-27 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 4229c873-1e73-3825-b49c-7ffd16fcb88a | -6.6206 | -58.8483 | 2025-07-27 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 89221e26-a9e3-3ab5-947a-69bb78eb5e98 | -6.639 | -58.8475 | 2025-07-27 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 772fe4a9-2133-376c-a146-b3bcdad4f69a | -17.9778 | -53.17292 | 2025-07-27 05:01:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f21bcc12-e473-3b38-af65-d4dde1456430 | -21.42192 | -54.13293 | 2025-07-27 05:01:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 407ffa8f-5997-3477-93dd-13ca8c7489c5 | -17.99335 | -53.17047 | 2025-07-27 05:01:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff9c6b06-ec0e-3d9c-92fd-309cb6cb3e05 | -23.06873 | -49.67032 | 2025-07-27 05:01:00 | NOAA-21 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0c66e246-18e6-399a-bd6a-9c401c54f0c4 | -18.00013 | -53.17646 | 2025-07-27 05:01:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f376120-6139-34f7-ab1b-b2d8ebf133ad | -16.39938 | -52.74482 | 2025-07-27 05:01:00 | NOAA-21 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cd82e7a-3ea6-3563-89fe-01631188622a | -16.40977 | -48.92576 | 2025-07-27 05:01:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9c8bf2a0-2e48-3355-99b1-3eddf6599ccc | -17.54051 | -52.55501 | 2025-07-27 05:01:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98c56071-4f1c-319b-9e8b-30a1920713b2 | -21.6067 | -57.57789 | 2025-07-27 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66c744db-86d2-34a7-a9e1-5540a62f96f1 | -18.22277 | -54.54681 | 2025-07-27 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57e8f2b7-4095-3a00-8559-7269ce9287f7 | -17.99771 | -53.16639 | 2025-07-27 05:01:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89d33870-be76-3a8b-bb0e-575b4a4ef977 | -18.0045 | -53.1724 | 2025-07-27 05:01:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17a330ca-cc92-3936-ba5a-7faac304e662 | -17.2449 | -46.91086 | 2025-07-27 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03208c62-612d-3ad0-be6d-7590e57a756a | -23.0678 | -49.66941 | 2025-07-27 05:01:00 | NOAA-21 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 849f9fac-4619-3c30-a56c-5503f57510ea | -18.00385 | -53.17706 | 2025-07-27 05:01:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 24dfe517-0c85-3d39-b251-2888c8ee8138 | -21.61001 | -57.57848 | 2025-07-27 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d13b560b-d302-3085-aeaf-99be27dbf588 | -16.25092 | -58.39642 | 2025-07-27 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f0fc2097-9a65-3552-a69c-b9411622add4 | -16.49034 | -51.3101 | 2025-07-27 05:01:00 | NOAA-21 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea8a2ea8-e548-3826-b7e9-54898077a91d | -18.00078 | -53.17176 | 2025-07-27 05:01:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22f0fb0c-bad5-3b06-8ec4-f91fc1eb4dd1 | -23.07216 | -49.67575 | 2025-07-27 05:01:00 | NOAA-21 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 962d7429-028f-390b-8dcc-4be7b0b3640e | -17.98832 | -53.17945 | 2025-07-27 05:01:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a152cdfd-bb09-3c9b-a8f0-be445cbed456 | -18.98746 | -48.42068 | 2025-07-27 05:01:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5bdeecd-aae0-377c-82c4-62ab1bfcf539 | -18.39762 | -53.32073 | 2025-07-27 05:01:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac76dbfa-6a90-395f-bd17-c33a19c35cc1 | -16.40505 | -48.92608 | 2025-07-27 05:01:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c5c7d4a-1406-3567-9626-47819075c1c5 | -19.3003 | -49.66889 | 2025-07-27 05:01:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ca6fa6ec-fd99-3ce6-b756-a73394fa284a | -21.9957 | -57.61049 | 2025-07-27 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ffbe87b-3483-38f9-b0d0-ffc4397f4548 | -18.39452 | -53.31561 | 2025-07-27 05:01:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 472877cc-9039-3964-bc37-0dd4d51389e4 | -21.33621 | -55.63536 | 2025-07-27 05:01:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7d8ea9c-5f74-32b0-af98-9b89b6da1bb1 | -21.3405 | -45.63633 | 2025-07-27 05:01:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 74b2fa87-6721-3ded-acb2-12da51d563d6 | -16.48627 | -51.30944 | 2025-07-27 05:01:00 | NOAA-21 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35ca6445-0968-3660-b65a-b65ebb4be220 | -18.39825 | -53.3161 | 2025-07-27 05:01:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d37a9269-e502-32ba-8b63-e89f6de0468e | -18.99261 | -48.42104 | 2025-07-27 05:01:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9c5cc8be-2cca-3fcc-aa57-3633bb22d5b4 | -18.22626 | -54.54737 | 2025-07-27 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa63db8b-db09-3ce8-9e76-444c97cd7edc | -17.98897 | -53.17466 | 2025-07-27 05:01:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a455380a-4540-395c-a193-6761cd358772 | -17.99204 | -53.18001 | 2025-07-27 05:01:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32b6feb9-c518-3e82-aa0a-bc10a331099c | -17.99269 | -53.17525 | 2025-07-27 05:01:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b8784b3-7186-3159-a6d2-24556212b4c6 | -17.98459 | -53.17887 | 2025-07-27 05:01:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 85e64c6e-4aa7-3823-bcef-ff41172e5248 | -23.06593 | -49.68725 | 2025-07-27 05:01:00 | NOAA-21 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c7bed42c-469a-368e-b7bc-ec3d550b093d | -17.98525 | -53.17407 | 2025-07-27 05:01:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README20.md)
