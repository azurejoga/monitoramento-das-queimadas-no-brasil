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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59a244c0-ca67-3cae-9164-a7737805ad1d | -8.88217 | -60.74492 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 779edcfc-05a0-3f64-8142-f0891ec6654b | -9.64907 | -64.9514 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a04b7a4-5a8f-37ac-b163-0099fc8c1fea | -10.34989 | -58.04129 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 139e8b21-3016-38ed-b460-11eeece98366 | -10.63916 | -69.0542 | 2025-08-29 05:29:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cc28af3-b147-3dc3-a3a0-07992f941d0d | -9.47619 | -62.38221 | 2025-08-29 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e948707-cb48-396f-b942-05e905b3ea57 | -10.45936 | -57.94458 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c9f994d-d897-3ebb-b8f8-836ef687fba7 | -10.84681 | -60.82233 | 2025-08-29 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87c86c2e-6ca1-3198-b9d5-377749ce0464 | -10.93675 | -63.63034 | 2025-08-29 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 802a1869-0882-3d6c-b5f1-6da49284a422 | -8.53706 | -70.74859 | 2025-08-29 05:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f869fd31-0ec0-3348-a7bd-8d3027749cb2 | -8.96192 | -65.94883 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0c7a5c8-5ee5-323b-8ff2-1e488c6aa927 | -9.88707 | -64.69874 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93a65a83-2e8b-32c5-9911-043cd73073ec | -8.8806 | -62.47711 | 2025-08-29 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b34a576c-4338-3ba2-acf4-38aa9f229bd8 | -9.11333 | -65.78079 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3d61db4-2d98-314b-a2b7-2b29cfb15604 | -9.10158 | -65.74095 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 725ebf2f-8950-3294-b757-b5ee5c6e0073 | -12.66478 | -60.2644 | 2025-08-29 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0f9a0ad-b74d-3010-a1ef-c259b9b20fb0 | -7.41912 | -70.15472 | 2025-08-29 05:29:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0ef884b-ed3c-3aa4-8893-5d722ccbf84c | -9.47028 | -60.31185 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b6c9105-460c-30a0-bcbe-e900aacd1521 | -9.13563 | -65.80148 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3a5ae01e-f29f-3d68-b815-54f0ed23cec8 | -9.17045 | -60.78446 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3154200-fe3b-3368-afa6-2ed17d813e8b | -9.24473 | -59.78893 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cca229cc-8be3-3229-aafd-267d34da7fd6 | -9.12559 | -65.79555 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33828eaa-b069-3970-ad75-ca908df462c9 | -10.3649 | -57.82285 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4916ff42-e3da-34d3-a11f-96d89d16d481 | -9.45206 | -60.56021 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 9fe3a834-a571-3753-aaf8-6d1404c6b7d1 | -9.37436 | -63.50029 | 2025-08-29 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22b4b3f4-be16-3610-932e-e0ba3463bf24 | -12.61898 | -57.01244 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57c42ea1-ec98-33d4-aad0-81b783ecc0f6 | -9.1645 | -59.57324 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed70be3a-f505-3382-bbf7-e44c1d1a6abd | -8.9497 | -65.95538 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 36bd3c8e-765e-3682-85dd-f3b5c1d21f36 | -12.62343 | -57.01306 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8acd556-8191-37a2-bb7a-953d6f01c072 | -9.1295 | -65.28958 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3e20c26-8acf-30b0-ba17-0ef6e86e954a | -9.77212 | -64.26064 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 9118c719-b0cd-34e4-b53d-d96eed2ddabd | -14.34389 | -53.33255 | 2025-08-29 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ba372175-85cc-33b0-b334-45684c19145c | -9.16575 | -59.56467 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5935fccb-b940-34cf-93a8-a7fd22903289 | -13.01142 | -56.91388 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 768fc2cc-5aef-37fe-a320-898534ab6add | -9.15003 | -59.57084 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1b3e1d0e-5d7c-30ab-988a-2114c73bc900 | -11.22943 | -55.05883 | 2025-08-29 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ba4e1962-41be-31e2-8a2f-c428ce3fa19f | -10.45583 | -57.94032 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58823e91-a195-347b-9301-58edc05c4211 | -13.36632 | -51.7689 | 2025-08-29 05:29:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1a6070b-a25d-38b6-b049-ec48d6c8f381 | -9.31601 | -57.69669 | 2025-08-29 05:29:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7496298-9d0b-34c3-a564-78ce4600b7a8 | -10.45267 | -57.96228 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab4b7d29-25d2-3473-9cd7-4fd5be2d50a4 | -11.31532 | -55.2232 | 2025-08-29 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 660cf98c-052c-3299-84f8-8a060db74b23 | -7.54373 | -63.85389 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da6876e9-9dbe-3667-a213-c3a3cb691d69 | -9.71473 | -67.57274 | 2025-08-29 05:29:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d30e7e38-b340-3488-b843-a961a17105a3 | -12.22797 | -64.22627 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f067b7d4-7237-32b0-b73b-dbe467fc1478 | -9.28455 | -68.25941 | 2025-08-29 05:29:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64ae6f93-b907-30b0-bbc0-01d5d0c29ae7 | -9.54858 | -65.69055 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 727b4f12-9e82-35dc-8ca7-a4c4b8bb5050 | -12.42975 | -63.91822 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e3b134c6-6028-34dd-964d-b92b78dd5fae | -9.21421 | -60.86411 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6de75e56-7410-3658-9636-957af40f34c6 | -10.37147 | -57.83511 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 470a3117-eeb2-34ad-aeb2-9eded1dd8200 | -9.12201 | -65.79494 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9d9aa67-4221-3f30-97cb-d32c06ea4598 | -10.44915 | -57.95802 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50617365-fcbc-37a6-9c35-1d8c123fdc34 | -8.95843 | -65.96983 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73d13baa-ebb4-300c-80ea-b9e4ecba59de | -9.31495 | -57.70391 | 2025-08-29 05:29:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d326d30-b679-3718-a0f2-6f18e6fc0378 | -9.10907 | -65.78432 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f93cc7e-870b-3ea6-82f7-35537b0105ad | -9.11622 | -65.7855 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4d6f0f7-5308-3d2f-87fe-8791e0b842be | -9.54122 | -62.39963 | 2025-08-29 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be15e6a6-7b6c-3356-8892-12de129733c7 | -8.58281 | -63.92859 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e8d74b9-6447-3cbd-a93c-e086bf8cba72 | -8.94829 | -65.96381 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f16742a7-9788-33cc-89c6-43d180612b8e | -7.5629 | -63.84219 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0255fa0-520d-3df8-8715-04f6e75c092b | -10.48114 | -57.96901 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e851d5f-6be1-36f6-b2b5-5ce5000bc0b1 | -9.08732 | -65.73855 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd69ec1b-3856-3766-96c9-6cda19f3bc42 | -9.77328 | -64.25344 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a3d12030-2f86-31ab-839a-fa81a2ba6098 | -8.90047 | -62.48026 | 2025-08-29 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67970b6c-45e2-3a6c-93fd-79b02cb07d31 | -7.62298 | -60.85202 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 061fe4df-08af-3dfb-8e9a-18584f9a7c66 | -10.47344 | -57.96486 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c753c2f8-8c3a-3cc2-8d42-1a6fdbd01a3e | -12.22465 | -64.22572 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70a5cb5d-0b99-3a61-a32a-3b6ab50d4c85 | -9.11265 | -65.7849 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9cb87c5f-3456-341d-8ac9-4307e2cdc078 | -9.77445 | -64.24623 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 50db84f7-405e-334b-9089-b0dbaea0b6ef | -9.17463 | -59.45267 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae8ec9af-c911-3921-a4b7-190b2dbe1c0b | -11.22369 | -55.06399 | 2025-08-29 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8fe7c59-e809-398c-970a-851821c6e8db | -10.17266 | -68.15517 | 2025-08-29 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2105d7d-c43f-39ae-b211-bd3757b8ba7d | -8.88617 | -60.74169 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a6a6a1a-627b-3223-98b5-082f45a01f2d | -9.24507 | -64.41435 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d7a0f37-bc92-3416-bca6-171b8cc5f281 | -9.13496 | -65.80559 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3eac4fc1-7c41-36e2-b70d-3453768165ca | -9.16284 | -60.92529 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50606b34-255b-30c7-9f71-8e42e1051351 | -13.00571 | -56.92249 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5274310-085e-3864-b590-f49b4eae4421 | -12.61837 | -57.01698 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1708a937-a8aa-3d3c-ab94-1f88e71be312 | -9.12181 | -65.77386 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 03e8f31b-b720-3fef-b028-f5e57d98f08e | -9.15634 | -65.77834 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 35cdbe4e-02b5-3cf2-aa8c-14097e9fd2b4 | -8.53214 | -70.74767 | 2025-08-29 05:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eb79ab28-4d6d-3803-ad85-97acad29f1fc | -9.13206 | -65.80087 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f1f5dd8-6a98-3177-9d9b-d64b9a300ecb | -9.23816 | -59.78372 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0aafaeca-9a7c-3b68-8390-738421a30e35 | -9.16212 | -59.56415 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b20358a0-c7f6-3051-b11e-eedb5e23082f | -9.16567 | -65.78834 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24b634c1-3482-31bd-b6a8-0cd78ed304a8 | -7.54269 | -63.83892 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0048510e-4f52-33cd-a587-4686999c6274 | -10.4693 | -57.93483 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec9d388f-1138-3b4e-88c5-f7b25e75a0de | -9.15885 | -60.9285 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13bda989-a8ef-3fab-b511-924735ab5680 | -9.15065 | -59.56658 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 566ba9f8-49e6-32b1-9bec-9b1338829dd4 | -9.10871 | -65.74213 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a7570f9-76ba-3f0b-9b22-f26189c348c3 | -8.89684 | -60.56178 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f54718e4-3c44-3d26-aed2-1216192ac15f | -9.1512 | -59.5882 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c90c305d-691e-3c29-99f7-f980ecff1b0b | -9.45263 | -60.55637 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 1165e832-13fe-3721-8db9-fdd2ceb1eac8 | -9.7654 | -64.25954 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 456e08e8-3f6a-38a0-93ab-9554dc51b8d8 | -11.38066 | -63.27131 | 2025-08-29 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42bd62ad-ad07-3be4-9f6d-4e8cf55e073e | -10.07573 | -62.88899 | 2025-08-29 05:29:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aad7dbac-5fed-3dc8-855a-46389a958661 | -9.78337 | -64.2551 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 033b7579-5893-3b3c-a9cc-6e8a5c12fe78 | -8.69969 | -64.21047 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd863911-aaed-3fd7-9e64-0deda054c150 | -9.48592 | -62.38369 | 2025-08-29 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 776282ed-09fc-3166-b809-34bd417b7cf6 | -8.69458 | -62.47229 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d01f172d-0445-3ae5-8e28-af0caa70dc1b | -7.89876 | -61.52232 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 136687c6-62d0-3bc5-ab06-248c99b61d1b | -14.312 | -51.89661 | 2025-08-29 05:29:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README85.md)
