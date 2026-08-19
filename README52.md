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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55492385-c9b8-30a9-9e9d-5c854e790696 | -6.80673 | -59.45564 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ece4203-deed-3df8-925d-d79bea6ffcc1 | -7.61124 | -60.95997 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b8a3819-140a-3086-a7c9-f0cc79635d17 | -9.42649 | -60.45609 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dab43090-9e5e-3480-af66-f2890299cfb6 | -7.6101 | -60.94559 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b58ad29b-3476-34d6-a88d-43a1f58135e6 | -9.4292 | -60.43841 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3307fb17-410a-3616-aebc-96566390d859 | -8.89954 | -60.59002 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdaa7fd4-2e2a-3636-89ce-0ba00735ca29 | -6.76215 | -59.14682 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11e0f2ca-186f-3c65-8522-a283df7c0b4b | -6.88253 | -56.43012 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa8b3fdb-61f1-337a-a80b-bc3cbb82c518 | -8.52995 | -54.74375 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87963d2e-1abb-30cd-be3b-9214ee40e16b | -6.74869 | -59.16708 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39cbc441-481b-3fcd-aa57-74dae736d2ef | -9.41758 | -60.44745 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d6330076-631d-3549-a6c5-4f8e92fdeb88 | -6.89071 | -59.03891 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f8783ae-a5c2-3c3f-a193-88c7514e17de | -6.84773 | -58.99546 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bc803b7-45d9-3acd-828b-ea85a1e5c4eb | -8.96338 | -60.52812 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8225aa5-4055-334f-8719-1ec8454a7164 | -9.17829 | -60.83097 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a9b0bc6-2923-3828-be88-128e12c010e5 | -6.60688 | -58.39278 | 2026-08-19 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f73ae281-c08f-3e0a-b9c2-00342c7b22da | -8.54118 | -54.72778 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 417af671-b16f-3b3b-b86f-25e1af22ed0a | -8.55943 | -54.72607 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 41c90b34-2f78-3a74-9356-f20e0cfaa734 | 0.30439 | -60.44549 | 2026-08-19 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22e22287-b8c9-375b-b06b-495bf91e02f0 | -6.88509 | -59.05305 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 317a96ab-02c6-355c-8c34-b0fc4d93933f | -6.85957 | -59.03794 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0a051c16-4d1c-3926-96c8-b8bc5fc4ec88 | -3.42905 | -51.51231 | 2026-08-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae06a555-0e33-35b2-a12d-08edc8fedef1 | -7.4334 | -59.80314 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3170aa0-9c65-3d4b-adca-9d04287674ab | -6.89133 | -59.05775 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fb7cc5b-df5f-39ed-bf3b-9e4462ce11d5 | -9.42633 | -60.41263 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0f6cf3a8-6699-3b5c-9e3c-97e7e9862051 | -6.75372 | -59.15673 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d2d22c9-c0fc-3369-8d54-462862b68b16 | -9.41253 | -60.59111 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f25b0567-825e-3a1b-9420-8ff903ef361e | -7.57042 | -55.56619 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6adf3dc6-2ddb-3c08-af6b-a53dd309b484 | -9.40974 | -60.58708 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7341c393-d395-3f76-8bbf-fe5b1bdc3182 | -8.54254 | -54.75009 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fde5b503-c078-3415-bff8-06c5daf859b5 | -9.39278 | -48.23927 | 2026-08-19 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 29ecf4b4-c162-3315-83a4-13d7a3bea174 | -8.95751 | -60.58825 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0aa4e7fd-bb40-3f9e-8180-72f81bf25c91 | -9.42409 | -60.40503 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cea70298-87ca-34be-822b-5ec0f99cba84 | -6.85624 | -59.00804 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8d31b7a-1390-382f-9a1d-24d18fc0ada4 | -9.01477 | -60.5038 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 081a5bf1-44a2-3ed8-8bb1-412ead1a9c52 | -6.99802 | -59.0474 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 898c4f40-c409-36e1-ade7-9c202843b13c | -9.1775 | -59.70179 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 862b1bf4-73e4-3686-941f-1215cd5598bd | -3.09961 | -61.20998 | 2026-08-19 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81c00292-c3bc-3bed-9487-7c527174f32c | -8.54681 | -54.71979 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7d1c953b-47ff-352c-850d-4a0297c01a9a | -8.55062 | -54.72474 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 690133ab-21b8-3af3-b0fd-bee33431dc5c | -6.612 | -58.95605 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 059b050a-e9a5-3725-bdbd-644128dccd6e | -3.4308 | -51.51308 | 2026-08-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57f2792a-482b-3241-9d3c-2e224cfb0279 | -8.94452 | -60.51797 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d518516f-12dd-32cb-a138-6137b374b564 | -8.5462 | -54.72411 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1e7f7da7-e86d-3349-b240-dfdf863e9a96 | -7.54005 | -55.5731 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa293119-e3f4-3b31-8d9d-b7b7119da3d5 | -6.77175 | -59.15199 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a00009f3-2cda-3cba-a60b-712d93bac1c3 | -8.57007 | -54.68289 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4565c267-9f02-3733-b5ec-838aa3990101 | -6.70639 | -58.9361 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f68a7d76-d639-3416-905d-cc48b4c8a3b7 | -8.57643 | -54.76553 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9c7a0a4d-59f7-3aac-9b55-716888e06e95 | -7.07288 | -56.66153 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e770171c-4e69-3288-a750-1aca9ccbc3a6 | -8.07902 | -61.36157 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fab1efc0-77df-30e8-b046-bdf76e858f7e | -3.10409 | -61.20339 | 2026-08-19 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db6a4bc3-dc8d-3cbf-b4d5-aa2345adc489 | -8.56262 | -54.73534 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c3aef43-2977-3d19-841e-d7870146ad09 | -6.84264 | -59.006 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3d56579-2584-392f-990e-dbfb46ee582c | -6.6459 | -56.3515 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9689f59-d33b-331d-9118-a4d2b57a5132 | -8.58084 | -54.76617 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ba78947f-6ec0-31e8-9b36-b5faa447c2c7 | -9.40472 | -60.57549 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b2eb263-570c-313c-9389-faf00246819e | -9.42254 | -60.43737 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b08dcc79-4d0b-3b1e-8c70-1104a7fba960 | -9.20158 | -59.47194 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac1c02cf-4013-3834-b873-04b785722129 | -8.54694 | -54.75077 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 175d9609-9fb0-342d-a693-45e45e783f83 | -6.85115 | -59.01854 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca0fa09b-0ef7-382a-ab76-47c9ce68600a | -9.40139 | -60.57497 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2e18ddb-dab6-3b4d-af98-a04ea38d98f9 | -6.7013 | -58.94666 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4ffabcba-c9fd-3dd1-b406-f537b911e873 | -9.17073 | -59.70075 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a438cac4-3916-3b1f-ba62-89247aff2561 | -9.42641 | -60.43435 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cecb9e84-7659-3b51-936a-b2c0d19984ad | -8.55572 | -54.75224 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48768e9e-d2ed-3030-bc3e-6cc78bf9f7b0 | -8.10333 | -51.66282 | 2026-08-19 05:23:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7c79e0be-97ef-31c1-9b9a-dbfe23d6fc3b | -9.21215 | -60.81107 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d015dad-7d34-3c7a-a1af-b427c8a2dfa8 | -8.57496 | -54.74324 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d295e85b-5204-3ef6-98aa-9e0b735723f5 | -8.53177 | -54.73075 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5dbc7072-307c-3961-9322-6ed23de0a4c9 | -6.73479 | -58.58584 | 2026-08-19 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09fcc597-e4f7-341c-82df-1d1b348b612e | -8.54559 | -54.72844 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 60f4f0ea-458e-3180-8850-fdc6623ac1fc | -8.57261 | -54.69387 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd8923a9-7372-3734-89cd-a1d5b891fd2f | -7.0472 | -59.84129 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11ff7fe8-7862-3afd-bc8e-4df111f76235 | -8.5645 | -54.7537 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b132ee5e-51da-3363-93fb-31367cf6f43d | -7.4613 | -59.99907 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a015749-7382-30f3-b6fa-5ffc4ad7a4a3 | -7.54098 | -55.59581 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6fbf568-e62b-3b7e-8e85-dab40a35ddce | -9.22433 | -60.82014 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 819ccaf4-3628-392b-99c1-a34226abece8 | -8.56149 | -54.7748 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8510b46a-c3d4-39c6-b82c-2e56a9bf2d4e | -8.53998 | -54.73635 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56aa9d6e-4523-3c30-a54c-7be00ada15c6 | -6.43082 | -60.06755 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94046474-7458-3b7c-9025-238208511c69 | -6.96092 | -59.03469 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0332f8a5-ad9c-3dca-8ad4-8820aa4965f6 | -6.88731 | -59.03839 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9e0fd0b-32d1-302a-9696-ec721082e33a | -8.53557 | -54.7357 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f3def87-c9db-3834-8ba7-3f576bf906e1 | -7.53595 | -55.57245 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 531344d0-9cf3-368d-9a60-2907a32fa6ae | -8.58266 | -54.68626 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b257a97-e7f5-31c5-8cae-8c124989980b | -8.54756 | -54.7464 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 720d0101-f96e-3da9-9c97-e418854a9de4 | -6.80727 | -59.45206 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f95514f-bd37-3198-995f-522171d63c4e | -7.04775 | -59.83777 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16ed76a4-4d69-313f-b0af-ce4752d36cb3 | -8.58211 | -54.69346 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64aacd58-a5f1-3f6d-a8ba-d60629eb4ddb | -6.99067 | -59.05003 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f04c06c-9d36-3b3a-ba3a-3b99ed7d8e4a | -8.54439 | -54.737 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ecb350c-b664-35a3-9471-c0a2e8810e86 | -6.78488 | -59.44896 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79faf01b-3068-38e2-a607-0900db73ad45 | -9.25189 | -59.81408 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac5e6f56-ad4f-3df7-8111-4753a6f54b38 | -8.56579 | -54.74469 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 073e5d84-a202-3694-9c27-de33592b1d30 | -9.42967 | -60.41315 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a70b40fb-add5-3ef3-9577-89be5d2ad07d | -8.57115 | -54.73818 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 156c9ba5-b34e-3c3f-b06e-573ac69e0587 | -7.60132 | -60.95842 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99918d5b-71e9-35b9-b8e1-9d4408c3ee45 | -6.84489 | -58.99128 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 474c8d91-f8e3-3177-b920-be41851fd36c | -8.56849 | -54.72453 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README53.md)
