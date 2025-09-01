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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de2946aa-0a30-3af1-9522-7a4c901903fe | -7.0757 | -44.3606 | 2025-09-01 05:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| d0bd76c2-d3fd-30d9-bb37-31cdefbee4f5 | -11.0381 | -45.1256 | 2025-09-01 05:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.3 |
| ccfc0606-fbcf-38b5-bf92-ab3b6033b875 | -9.22952 | -60.26699 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7505635e-a896-3e9b-82e9-b3c5d8ef93d0 | -8.96725 | -65.97603 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f57d85da-d490-3e42-ac20-d3885f94b298 | -9.07581 | -65.42581 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 78bf6e08-7579-30ae-973b-29d365393448 | -8.26251 | -61.45849 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9b29cce-7b59-37c6-a925-68044d4b7a8b | -7.08469 | -63.20095 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3714b994-e8b9-350e-9edf-65ca90b3add3 | -8.65204 | -62.93032 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ab6ffec-3b94-3ad0-a0cf-dc1f3e418375 | -9.64495 | -63.11667 | 2025-09-01 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 137429b8-9433-340a-b703-c623a708255b | -8.74325 | -62.39967 | 2025-09-01 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5afa84a-553e-398f-86f9-a35565bcc6cb | -3.45078 | -52.72121 | 2025-09-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2318493b-8b7a-31d9-b66f-0ad55839c50d | -8.85096 | -47.50329 | 2025-09-01 05:23:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 80e725ff-0f7c-3f33-8cfb-6d446d10117c | -10.24353 | -51.11621 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7b9606e7-add3-3485-ad2c-8a99cd0c3b3c | -7.28356 | -60.64986 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 272ac69d-df64-30dd-847f-650af41b780f | -9.11688 | -61.21473 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a4f4aa6-efde-3fab-a04b-8629dbbdf81b | -9.93026 | -51.62531 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9681ca8-43d6-32d0-83e8-c346ab395c8b | -10.04431 | -48.1048 | 2025-09-01 05:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 27632f49-83f6-3a6b-bfc8-6c3242334c97 | -7.09162 | -63.13521 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a49d342e-d9a0-3894-ba24-fc75dee2c681 | -9.137 | -65.85286 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f5cc4464-0f27-3964-9209-0228f5f7a940 | -7.67713 | -61.09137 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca7eacce-e034-3b5f-909b-11c907883c94 | -8.73878 | -62.40625 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 728e5b72-d821-3cae-af4a-7c6619a2714f | -11.0767 | -52.06225 | 2025-09-01 05:23:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8b9aab2-9588-3f68-b93d-59b4ed04ebba | -10.05251 | -48.09076 | 2025-09-01 05:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 713751e3-6989-3c52-a3cc-a2d302833dbb | -7.59575 | -61.62982 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1478aae3-5ad2-37a1-85c7-934df469bfc7 | -9.83305 | -65.04878 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04284dc4-48c3-36ef-b52b-32b4ce783e80 | -9.15029 | -65.84496 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5dec980-0a4a-3a38-8f96-5468f2e9120f | -8.42986 | -62.29441 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddec1c00-da12-3171-986a-48bec6ad872f | -8.72591 | -62.42249 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3ccde98-6aea-3d68-8610-99981eebb542 | -9.07803 | -65.4358 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 75027391-0282-39db-8059-db3cdc4d421a | -8.73096 | -62.41231 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c41d825b-1f7f-329e-b683-d204fdb868c4 | -8.62349 | -62.58993 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5cc4979-3c21-3f99-a3d2-695170bd37b4 | -11.07626 | -52.06577 | 2025-09-01 05:23:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b362acbd-3509-3165-9ba0-6d67608ee609 | -10.05044 | -48.10926 | 2025-09-01 05:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 486ddff9-44ac-355e-bee8-35faad937936 | -11.0769 | -52.06372 | 2025-09-01 05:23:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2878a100-8590-309f-8302-f9f40e571161 | -8.69971 | -62.41465 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e28ed9d-ec9b-3e5d-a891-42e9eb320b5a | -7.59243 | -61.6293 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3f6f05e-5233-393a-ab48-4a99eff98b36 | -9.00725 | -65.69302 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b8a12f0-5aa9-3b04-90ba-34357a1e0215 | -9.86611 | -65.03188 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6cd906fa-c387-3138-b969-5538f6458917 | -9.13865 | -65.84297 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ed95246-ed80-3902-90af-06cc6641c7c3 | -7.69256 | -61.10088 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 199550ea-b178-3bfb-bc39-db751d644896 | -8.70028 | -62.41107 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82f201bd-3c80-31d1-855b-7724fce9f6c0 | -9.4434 | -60.57903 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20b5116f-9869-34a3-8843-7be04aa5b243 | -8.42652 | -62.29387 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6037eb5-d1de-3103-85f8-d8bd49d09590 | -8.9768 | -65.96729 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d899aeb6-db99-371b-a4f3-f8b09cf6734a | -8.74047 | -62.39557 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d493418c-8f68-3013-b53c-55aaa6fc8a51 | -8.84869 | -64.14487 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b01f9040-ad42-3dec-9b8f-e83070d4b79b | -8.24453 | -72.81722 | 2025-09-01 05:23:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b615caed-b4d3-3f86-85c8-1eff2916793f | -8.86169 | -63.02472 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4ca1311-0ccb-3a03-9fe9-5dcc10d0eaa3 | -9.44171 | -60.56796 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8140cf9-8951-3360-91db-e8756d645b84 | -8.62743 | -62.58686 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9afdd6b3-0869-3d3a-bff8-2e1569aeacbf | -8.72817 | -62.40822 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d6502c9-9294-3788-9927-2921a0b79f88 | -7.45213 | -63.16088 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75cd68a4-ce68-35f4-93f1-4a563ef15f52 | -8.96896 | -65.966 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a8f846e7-7b93-3b24-aa1a-866bb1d33bcf | -9.83156 | -65.05753 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b289b34-432e-3e19-abcf-301a5fdc3d4f | -9.13311 | -65.85223 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 277c0b2f-ed7a-35d9-aa06-5a22e197941e | -7.108 | -63.03247 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0dd7d2b-c720-3d82-acba-86f42ae31a3f | -8.63415 | -62.58793 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21983dfe-fef6-37b6-a21e-2a407a0d4f34 | -4.07748 | -55.79755 | 2025-09-01 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 643b8456-a542-3160-8362-aad91fc3efdd | -8.64957 | -67.24671 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1090fb9c-89ae-3322-add7-f85d41c8e3c0 | -9.14171 | -65.84855 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f7dab87-80ea-3a35-a860-5760e88b81d6 | -2.44966 | -49.36227 | 2025-09-01 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 24224b62-402f-3dac-91e4-b4d3e0379adc | -10.24241 | -51.1229 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 889522c2-cf88-32a4-98a5-497103861700 | -9.1229 | -65.53761 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e24a410-481e-397e-92c7-1923c8e121f3 | -3.63594 | -49.21124 | 2025-09-01 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e986688d-e87e-38a3-a138-9c14a196a249 | -10.04345 | -48.10878 | 2025-09-01 05:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3a8df8dd-e86f-37ec-b203-255fdba745e5 | -8.66449 | -62.9245 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f885412b-47fe-3666-b341-d6bbb8e42c1c | -10.0457 | -48.08848 | 2025-09-01 05:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95d8ec7b-fc52-3c8f-bd5c-200ad0aa78e1 | -7.5858 | -61.62824 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c4c60ab-1c9f-3343-a138-ff8977169f8a | -8.63577 | -62.59929 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff226fb8-ba86-3ac2-bc89-22d7abf9ae4d | -2.44322 | -49.36549 | 2025-09-01 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39f6b1b4-271d-3356-936b-45d308a0757e | -8.44304 | -70.13842 | 2025-09-01 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73ee7ce7-ee7c-3c03-a7a3-3620e5b41794 | -7.57094 | -63.40789 | 2025-09-01 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f71d45f-2f2b-3388-be00-c1fd98677e0e | -9.83965 | -65.05438 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5be2ef64-c2b0-39ed-a2c2-bc7459ef9d2b | -7.93354 | -63.00916 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8fa650a-53f5-39b7-8b06-40303d092c3c | -8.72982 | -62.41945 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4a313e0-5833-3f18-9afa-c58e5e7d896b | -9.07111 | -65.45387 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c24730d3-2f6d-3936-a750-320e57dd56a4 | -9.64461 | -47.8056 | 2025-09-01 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9f7181ad-a746-310e-9e73-181d679dc0d5 | -10.93073 | -50.85116 | 2025-09-01 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9b17b97-de70-3791-8924-4a231374168f | -9.27298 | -67.64513 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d11cfdfe-d0a3-3391-be1b-f66e95957a56 | -7.55716 | -60.87753 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a35ad8ca-093e-3f12-9286-f87bef962d40 | -7.28302 | -60.65332 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cf99f831-a776-31ef-8e31-b9e920646dea | -8.76259 | -61.43559 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| edcb793b-460d-3cbe-84d7-7d5149f15b22 | -8.7622 | -67.30018 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cf2a526-d312-36f2-a131-8c8a4e49898f | -8.65766 | -62.82975 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b9bbe9b-2bc5-33d9-95f8-f68e3da48ce3 | 2.89382 | -60.26584 | 2025-09-01 05:23:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c18f0fd-ef9d-3f31-aca6-2f4a1953ead6 | -9.64834 | -63.11721 | 2025-09-01 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a04278f-7bde-3f3d-8e08-22fbe8bcd94c | -9.82955 | -65.05001 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be6a8a2a-c8be-383c-a18d-5f92c876c35e | -8.08748 | -70.21881 | 2025-09-01 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 481c4102-ca5d-3f04-8714-6b87c6fe6d23 | -10.36812 | -52.29045 | 2025-09-01 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ab43ef9-bee2-3af9-bbc6-8d117347fbc2 | -9.11136 | -61.20675 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8300fc3b-2133-385f-8a79-20f2e0c66658 | -8.70362 | -62.41161 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb47c842-66df-33c7-a90a-1b580787e5bf | -4.08134 | -55.79815 | 2025-09-01 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5c73899-fbec-3557-b575-2fe7c8878e55 | -8.84092 | -64.14777 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d2911769-a0b9-38c8-81be-c87a9b880ffa | -8.67743 | -62.40374 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9d996f1-6844-33bd-badb-81ec510ca3af | -9.43832 | -60.54575 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0e9eb63-e04f-35f6-9f47-c43581c62d50 | -9.17371 | -67.56409 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3c814ae3-65ef-38aa-90b4-8108a4ef564c | -8.55566 | -63.00933 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ec36798-a247-3547-b818-8cac010547c4 | -9.28169 | -67.64661 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ca85e2e-efb6-3188-95a5-cf5ac2cdc446 | -9.07502 | -65.43048 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 275521b8-5e05-3ffa-90e3-d3805d6a1f81 | -7.07495 | -63.06219 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README76.md)
