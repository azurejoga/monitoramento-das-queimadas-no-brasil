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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc8cb9af-965b-395d-ab03-ff57d6419a70 | -8.89167 | -66.83412 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 749ef2b4-9d3e-3c14-a2e4-2984dce7fb6a | -9.07967 | -65.49732 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 590d6e28-6da8-3a69-93db-785c8ec2dddd | -6.7347 | -56.33959 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 940585b9-f9ce-3d35-8e4d-c2343ec83242 | -6.42752 | -53.56282 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a6cb435-9277-3392-ac25-64aadceb0b1a | -6.15718 | -57.7838 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7c43bd90-5ade-367a-9d8e-f3e298e92830 | -7.18504 | -60.68603 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8028c0b2-fa55-304d-8872-a6794200e303 | -6.35624 | -55.86078 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8457ecc0-ffc0-38c3-b6c8-7d0183c5ab27 | -6.81747 | -59.67577 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c07c4f63-9274-346d-aa64-1b24a3d6110a | -7.88837 | -61.67737 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4052f467-8106-3b9e-8712-2548abe0ad50 | -8.94629 | -63.30131 | 2026-09-01 05:36:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8fd9541a-e358-371c-a168-3102c8f3417b | -5.85418 | -57.56025 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 55fca969-2442-30bb-8578-17808c16f35e | -10.34731 | -50.01158 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73d930ad-cea9-3558-958b-2d6206ce2842 | -6.61998 | -58.38462 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7cc0fe7-34a2-3300-b51f-4c0b38a7eee5 | -9.61593 | -68.60004 | 2026-09-01 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e12ac69a-37d3-393d-8261-d6f720a2b7ea | -7.56888 | -61.37246 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ee7173b-25b3-3780-81f2-a27bdb972ed7 | -6.4271 | -53.5658 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a675b453-58f1-3526-b272-e1ed311dbc30 | -6.77467 | -59.43441 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a918c44-0676-30e3-a4a3-9b636f2ec199 | -6.70494 | -63.18804 | 2026-09-01 05:36:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a979245d-fb8c-347a-be70-94ad4751cfdf | -7.73153 | -60.97978 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8492ad48-0eb7-34d6-ba66-cbd0f9c9c208 | -7.63204 | -55.2973 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46ae63ba-aeff-375c-98ca-1933b1412d32 | -6.60199 | -58.60477 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb10bbd6-bb45-387d-aa32-810b7fe06fdd | -7.53366 | -61.37794 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e86270a2-6abc-35fc-946b-f72a1e54c447 | -5.4872 | -57.1481 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f40c75ca-3ae6-34f7-836b-220d847a10a3 | -8.03545 | -61.73251 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29c29cb5-c79d-3dc7-a541-54ca3812e814 | -10.35587 | -49.99999 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34b9e658-ff77-372b-accf-3027bfff8efd | -9.05315 | -60.44614 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6922202b-a5bc-3a0b-996d-3efe9443fea1 | -6.20987 | -53.5871 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cbf023b-4f9c-384d-872c-28b88151cc9b | -8.72435 | -63.75506 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce8fd46e-4609-3915-a699-6c7259d04005 | -8.59913 | -63.85838 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49bf03c2-92e3-3ba0-803f-16920a3af291 | -8.13266 | -54.9659 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4f98f1bd-737f-32ea-9db3-806c50262fc5 | -7.34358 | -60.58862 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a940f8b5-8da3-3031-91fc-6ebf0bf417da | -7.84551 | -62.31633 | 2026-09-01 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3afd83d-8ddd-3e62-b5f3-2276616d3969 | -8.94425 | -62.36918 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e9c7855-2704-3b5e-bc6e-945a1100021a | -6.95011 | -55.64252 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ff99189-3d3f-38d1-a097-6b853482a2c2 | -8.58869 | -66.97315 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58d5b5c4-877d-35dd-b24b-7ac65a3da7da | -7.5667 | -60.45655 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f93a4340-1843-3a0a-8125-acef6a212aea | -7.8595 | -61.1448 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cc20c3a-6683-3bb5-b91a-ec5a3206b394 | -7.30486 | -60.56758 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1e6dd6b-7a7c-3622-83f0-3d4819cb8d32 | -9.25593 | -59.55737 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cd6e034-3153-391d-9703-fbba4ba4b632 | -9.15149 | -60.94309 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| badec6fe-657f-3b14-b51e-481e7b758167 | -5.94654 | -57.6922 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d59d0068-4af6-37d7-aa8b-7d9eb5380993 | -5.8856 | -57.75391 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31aa9bab-ff5a-395e-afd6-f0b2b18ccbeb | -6.25443 | -55.43917 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25565d94-db9f-313e-b872-d2295ac308c3 | -8.45395 | -70.58836 | 2026-09-01 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d7e9c07-290d-3168-9b74-fb26c22795d2 | -11.10712 | -51.5411 | 2026-09-01 05:36:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b84d98c6-d2d6-3287-84b9-811765886456 | -5.87289 | -57.78046 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 029436e9-768c-39d8-9eee-9d5938e3b810 | -8.26999 | -54.92617 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 179a1e63-3f65-3c95-b699-6307d790a6f9 | -7.57876 | -60.4701 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49b49159-cb31-3a12-88ae-17036a56c479 | -8.78708 | -62.48388 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8b605ef-14bf-377f-a688-65930bc7ae4d | -9.17817 | -59.62911 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9332edce-9226-3906-ab28-3e75800be25f | -7.19641 | -60.68021 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07971f03-96b5-319e-ac2c-78ed223cb2f5 | -11.17606 | -55.09201 | 2026-09-01 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e10edb83-1ba8-3159-b5b2-144995620e14 | -7.9139 | -61.3382 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bede8ba6-6000-37d8-b741-10358689a6f6 | -6.94692 | -55.63258 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf7bdbe9-ffcf-31b5-86a0-31e9d4134bcc | -6.11829 | -53.55083 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48eb385a-19c9-3658-a312-96a4739b6453 | -6.80532 | -59.5678 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c7e57d9-9b10-3734-bc57-9629182c8d1a | -7.18959 | -60.67912 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 122db538-b9d5-3cfb-9527-6f08fc6d0dfc | -9.79653 | -60.1669 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 043ef008-141f-3fb0-b129-4445bfaaab2e | -8.81122 | -62.35172 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5187b75-36fe-3513-b3a2-5b96b07bb80a | -6.15328 | -57.78327 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 448d32dd-60fa-30f3-b311-e2f9e35e450c | -6.67365 | -58.74547 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32f11208-00cb-351d-a08f-d819cf19a29c | -11.10653 | -51.54623 | 2026-09-01 05:36:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 25e12083-446c-3c57-bc52-d74b641c8e59 | -11.24773 | -54.01042 | 2026-09-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55e0d8a9-bcba-325f-97b8-3533381d3560 | -8.80586 | -62.49402 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed7e7d69-728c-3fde-8ace-d63d65ad85d3 | -7.53646 | -61.38205 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3081673a-88b5-35d2-84af-93b7cccd398e | -6.18489 | -57.7323 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 3601e851-c0b9-3c2b-ab7b-d4b53c40ec29 | -8.63151 | -69.51801 | 2026-09-01 05:36:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69b1fbf3-1f02-3b6c-a01e-8748a83d6a5b | -7.56663 | -61.3648 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13fc8caa-3dac-3c2f-8493-52ce70ea538e | -7.58391 | -60.48252 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72d400a6-8c79-38dc-8a9e-30bf73a300a8 | -9.05135 | -65.40793 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e6c0173-d1a6-3cad-b4a8-112df5d7f320 | -10.75339 | -54.06627 | 2026-09-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 047297cc-f0b5-3b95-886b-d30b391f9527 | -8.0349 | -61.73605 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0118ae8a-28cd-3f1e-b401-ad42d2627844 | -9.71679 | -64.99427 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a139ea5-6439-3b51-a538-f8ae4d2850ad | -7.57498 | -61.31115 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6562a9b9-2698-36e4-b9b0-3a9acad6f190 | -7.57273 | -61.30346 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30cf146e-9bf5-3a0b-bd8d-cb0906f9dd4a | -10.82844 | -50.71917 | 2026-09-01 05:36:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5abf37a3-9b99-3ff1-af00-7008ee56c860 | -6.81761 | -59.441 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed28770c-bd19-3350-bf86-1bca3c8fc93e | -6.9417 | -55.63655 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a32135c-3bda-3d75-9491-0ab5befda22e | -6.13143 | -56.38427 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bba99bd-01b6-315c-b9c5-afb17fbb10ae | -6.7589 | -56.33699 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66690f0f-74a2-3bd2-9ec7-643d70600adc | -8.79261 | -62.49191 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf496d35-eb5b-39de-92db-673272f17ce3 | -9.02795 | -65.45731 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7acdfed-02a6-3fe3-9e5a-401fcfafaf7a | -7.5776 | -60.47765 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 033144a4-8d9c-37a1-87d9-edd271006928 | -9.06596 | -65.40636 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38b5ac26-93cf-31da-b556-69430652b891 | -6.81005 | -59.77249 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f1d1c4f-946e-3643-be68-41122f5ecfa8 | -7.35476 | -55.19367 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d2264f2-bd97-3c0d-b0b8-93cceb74c4ad | -11.24437 | -54.01055 | 2026-09-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd11e49e-f263-3555-9da1-4d76f14096d7 | -6.13142 | -55.6434 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2edefea2-4370-31da-aeb8-3df414b079cb | -8.68021 | -62.81614 | 2026-09-01 05:36:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f0d7288-44bb-3cbb-998c-90aea1956666 | -9.03815 | -65.39458 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d9325b9-8ece-3c0f-8952-6c75973614cc | -7.58793 | -60.47934 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d35bf3c-7f7e-3391-8b92-028f6a0b7d87 | -6.88351 | -59.40809 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24ba6cf0-fd93-35ad-ad30-84fa7e29bfc6 | -6.95147 | -55.63326 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e36d8cb-0445-34c7-aa47-080ea6abea83 | -9.20771 | -59.55458 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8d10749-7d29-30ea-b9de-4d756b50290b | -9.38943 | -60.56998 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 188085e5-8c25-3221-946d-7be990c0b874 | -8.56433 | -63.1827 | 2026-09-01 05:36:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96c252e3-3586-3452-b63d-dcc7d69ed809 | -8.60327 | -70.2166 | 2026-09-01 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ded4eeaa-c2eb-3a27-8a95-7dc8d1f06772 | -8.27558 | -54.92164 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c1b014fb-cf2f-3e65-8819-eab4df7a2e51 | -5.87816 | -57.7776 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fb585f2-b5f4-3242-a304-30f20e6b29ef | -9.16066 | -60.28819 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README77.md)
