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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f5749bd-cc24-365d-ac31-ae909ee30a09 | -8.53702 | -54.82927 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 035def0a-d2c8-3bcc-bea1-d53cb6e06c99 | -9.06246 | -60.4364 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a56e8f5-0d32-3390-b226-a80b7555de88 | -6.87488 | -60.01025 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51b09ec2-ea9e-3462-86e7-1bc78f5c4efd | -8.53648 | -54.85411 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99718d0e-74cd-32c8-a45f-bb60b11e1a15 | -9.13728 | -65.95336 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8276d967-019d-33c3-a7e5-5d9fb0b03263 | -9.40942 | -65.94581 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03eec8a4-d345-37c5-a157-9d30651678b4 | -9.67551 | -53.59873 | 2026-08-23 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8582f9d-a154-3463-901b-86776271373e | -9.59281 | -60.50951 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 723f9fe9-5019-36a3-a4de-c277faba54b7 | -7.01087 | -59.55682 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0637783-c233-3ebd-8db3-d377ab553eae | -8.09955 | -50.05696 | 2026-08-23 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6f34f67e-daab-3102-82a6-c89c353856ca | -6.88473 | -59.03656 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f3106cd-7565-39aa-a90e-a3ffc1cd6b7c | -6.51568 | -51.4508 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 230cbcb8-3a15-3097-9ed8-c388f9ff2553 | -9.1432 | -65.95448 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5608ea4c-5eb7-3a29-a3de-599bc2609072 | -8.57725 | -54.78938 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83fbcbcc-15ab-3a49-8e4c-946941f4074e | -9.0352 | -60.44689 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| beaa8470-5476-3d2a-bfb9-12f65715948e | -8.52545 | -54.8381 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c9f865e-74cf-3bce-9813-f2e6d192179b | -9.10256 | -61.59331 | 2026-08-23 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c13da2e5-89a5-3b31-a087-01199ae56570 | -11.46567 | -54.31791 | 2026-08-23 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2297ee48-2224-36c3-943e-2858bfa6f6c4 | -9.58998 | -60.50132 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a42bbd9f-4acb-322a-a1b0-b91671fb3b5e | -11.1598 | -54.00957 | 2026-08-23 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1e6fc24-d3f7-318c-811f-67585b7d268e | -6.3787 | -54.9427 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77be149a-c4eb-3692-b642-e407825d1d7e | -7.01608 | -59.55039 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4dd6650-fea0-3f90-b9e7-a9eb562d0dae | -6.96026 | -59.06712 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89699881-4637-346e-8dd6-f9067ac93a21 | -6.25561 | -55.41467 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff53b38e-a156-311e-a392-97b0cc48891b | -7.18467 | -42.75281 | 2026-08-23 05:04:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3a27d80d-cc97-30b2-a7a1-172b574ab31a | -9.04603 | -57.07322 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3762a16-5f29-3ff8-8719-eb283fc0c558 | -8.63181 | -54.70196 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 033635c7-c0ea-33d5-a6fd-5ac70cdcd907 | -7.18239 | -55.42224 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db6d3994-7287-3536-bddd-ca9cb2029861 | -6.76081 | -58.68756 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 312c5a95-6706-3fc5-b7d7-4da5bbd7b89a | -6.91826 | -59.43777 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1fbe3c1-3c44-35e4-935f-b60c79d05348 | -6.20227 | -53.08821 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 469f857e-ea35-35be-b351-54fb71dbfeb3 | -9.42236 | -51.67139 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68c751dd-2874-3220-a38e-9d99383fc7a8 | -8.91853 | -60.72212 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 674554fb-91d9-3a34-a418-244b1b05b78d | -7.67028 | -63.33168 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 261894a3-6961-310e-8d00-0a84e17f8744 | -6.96193 | -59.05721 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69a59493-0a36-35ce-a134-a60d7510d1ad | -6.79413 | -59.80606 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a50d49e1-c370-384d-8b00-ed1d9de81cfd | -8.81476 | -46.62015 | 2026-08-23 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 957c5524-9fff-3bc3-91c5-2004540fb7fa | -6.8622 | -59.0276 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9013be42-9725-37ab-83f8-a43d6e44e15c | -6.94995 | -59.0807 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eaf270b3-7721-31a0-978f-39306f882afe | -7.74348 | -46.17393 | 2026-08-23 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2efaa63-f73e-3244-8fbc-c80634434780 | -6.70627 | -58.73199 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 42c577bb-1356-3c49-b509-341fe8827117 | -9.12703 | -65.9565 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 110e007b-c17b-3777-a947-d8583fbd18f4 | -7.77504 | -61.07193 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd0ee19c-f7ed-317a-8d14-6554d69b57ba | -11.20565 | -55.04907 | 2026-08-23 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa6ce8f9-fc8d-3201-93c4-e971426bcd6a | -6.2015 | -53.52568 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fab984f9-8e6b-31ef-9c0a-bb934aece127 | -9.17224 | -59.45639 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18251bbd-6069-3ab3-8b99-1ba8977d6d10 | -6.07213 | -44.89779 | 2026-08-23 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b509571-a218-3513-b711-e33852d4c5cc | -11.20345 | -55.08475 | 2026-08-23 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46edbd2c-be80-3eb1-bf1f-fd60dcff3a18 | -6.80521 | -59.43946 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 067608c6-0a6f-31bc-a563-5a0d3bcfde34 | -6.84033 | -59.95164 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81cb99ec-5f55-3f2a-bd54-2161baaf3993 | -8.93533 | -60.72518 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 913e20e7-cf85-39cd-9b74-15e1eba25db9 | -6.37483 | -54.96705 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c37d5b7d-be2c-3f25-8154-2bf01b9d43a3 | -6.87562 | -56.63774 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ae1fdee-e3c6-3267-8313-c59921837888 | -6.88698 | -59.04716 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e26af7d4-bd93-3b3b-9ce1-1358c8a18008 | -8.53647 | -54.83274 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0809239-11f1-32e6-a579-0b1652ca2c9a | -6.68628 | -58.73367 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2cc65215-f828-307e-a614-97d480210dbc | -5.84583 | -55.71878 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdea887b-a291-3b2a-b5d9-bb1494b0be11 | -9.86114 | -60.11278 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14a3608e-277b-371b-b9e2-04131445b009 | -9.16837 | -59.45572 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b52442d-abfd-33f2-a78c-fb90e8f16da1 | -11.94129 | -45.52089 | 2026-08-23 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61ad724e-5e67-3ea6-91a8-196d7cb84a03 | -7.6851 | -63.33759 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1dfc89ee-4768-3795-9545-a4fad24f0cf2 | -7.37191 | -55.67696 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54683516-016d-3f7e-a0bf-c713e85f1dc0 | -7.01238 | -59.59721 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54bf06cf-9e25-3704-9d73-5817046e12e4 | -6.79156 | -59.42286 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c5d08dc-4a9e-38e0-a9f3-f7232825444d | -10.46404 | -49.96772 | 2026-08-23 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 145dea80-a88e-32b1-af89-c8e258dfad19 | -4.53207 | -55.52915 | 2026-08-23 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15246d42-9d95-33d8-831c-0683a937665f | -8.09065 | -47.262 | 2026-08-23 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 05ede26a-8d09-3429-9e7a-78f89aeee588 | -8.81558 | -46.61861 | 2026-08-23 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86becfdd-ef2d-3547-96c7-d3cd2ee7f510 | -9.21 | -60.89483 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf140e0f-043f-3ad5-8f93-c18abb3d529c | -6.86137 | -59.0325 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c66c735-94b7-38d6-8294-0a58a4433f4f | -9.162 | -59.46967 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5738ff02-4699-34df-8307-4331e5f94a82 | -10.4477 | -50.46972 | 2026-08-23 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a5531a73-bb76-35ba-a19e-a72cb48039a2 | -6.79462 | -59.60154 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66fdba6b-cedf-3db3-827d-e6aba668d82f | -8.52489 | -54.82021 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 313606dc-1379-358e-8d62-a48873049053 | -6.423 | -56.18288 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 877b6e66-f28a-3b65-b732-1e047f571498 | -4.93059 | -55.77838 | 2026-08-23 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 286250c0-db5c-3e5a-ae94-e6e31223b630 | -6.79582 | -59.59435 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df3b3cb4-4285-3ec9-a6ec-c82fa0ee0fe0 | -6.97196 | -59.06909 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29adcec7-54e5-3e78-aafa-f6d9e2bdabfa | -4.93117 | -55.77474 | 2026-08-23 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4175f340-10c1-30dd-bbc2-485b4f7fb617 | -9.1519 | -59.69262 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50ac800b-6936-3f28-ac9f-9e79f94bbd06 | -9.98948 | -53.94466 | 2026-08-23 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e7d8c23-cca0-3941-b74e-a0fe79278c41 | -7.4382 | -59.7958 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dda8c2d8-7469-319b-b723-1db49ecb8a98 | -9.78799 | -46.61865 | 2026-08-23 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 45fc570b-7e5e-3403-b7f4-6b47f3b3e74f | -6.93867 | -60.08773 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0da35db4-d97e-35a2-9ccf-ecf386da174a | -8.35143 | -46.50282 | 2026-08-23 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59994aa5-4df5-3bf2-8ae8-f5d3a42ca924 | -6.76009 | -58.66798 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11514ee8-4b4b-37f0-b802-4cea62c7b54a | -8.08925 | -51.66327 | 2026-08-23 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a97de147-3948-37e3-b502-f449a781681b | -8.53318 | -54.85358 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8e3e54d-5629-3bf7-90ef-1d76016c750a | -9.1256 | -61.59269 | 2026-08-23 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e82b5d82-e3be-39f7-b0b5-acd1068f164f | -10.4553 | -49.97025 | 2026-08-23 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6a4fd7a-48ee-3bd2-81bb-8eafcbd5ee44 | -8.91363 | -60.72528 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dd1b7ef-a301-3e35-905c-3f31024c57bb | -6.78473 | -59.41465 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e69367f8-9154-3b13-9429-861000d5c8c9 | -9.85597 | -60.11901 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7042db2-e8b7-3d45-ae1d-55fb1e3f7d3d | -8.70482 | -62.89956 | 2026-08-23 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c02c8ce-15ad-3218-aa8d-391b904b96b3 | -9.04218 | -50.86172 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd32da8a-5666-3c39-95c2-082dd3013799 | -6.12661 | -57.84401 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8a06bd95-2fac-3a23-9ba1-7de8e6df2849 | -8.08585 | -47.26149 | 2026-08-23 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b2d40f0b-8ea5-3afe-84aa-90020bd25f7e | -8.96148 | -50.75573 | 2026-08-23 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4dedc134-bb96-3e40-aea3-2a571c9743f4 | -6.76467 | -58.66393 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c04a2d24-2a5f-3a62-9301-6c6cbc79dff5 | -6.12506 | -57.83033 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |


[Clique aqui para ver as próximas entradas](README50.md)
