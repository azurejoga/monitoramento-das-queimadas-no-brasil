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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6872ccaf-60f2-36e5-83fe-6dd509571dc6 | -9.11437 | -61.60146 | 2026-08-20 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 47e7073e-e839-3b59-9d98-06d2152cc719 | -7.36109 | -55.51213 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cc6c348-759a-3140-874a-c9179a90db8b | -13.4815 | -51.44181 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b5bc00b-0266-3d29-9890-7efdf9c08105 | -11.1789 | -54.8024 | 2026-08-20 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 242f4036-6586-33c6-afd7-bb7c7d90b72c | -8.58679 | -54.73503 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32eaed0f-5606-37b8-bbd6-e1af282a067d | -8.57681 | -54.77847 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca406513-fca1-3f7f-8265-dd793a67f721 | -13.45257 | -51.42932 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4815f724-4b26-31c0-9038-43b0d686e8d0 | -7.86803 | -63.76197 | 2026-08-20 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d00f7ae-a0b9-3b2a-8a91-9940883cc073 | -9.11778 | -61.60572 | 2026-08-20 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9924655c-0641-3c33-b91d-4c52c9f03c42 | -8.6822 | -54.65568 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94c0f3c4-3451-3afe-a18c-dead8e3c6ce4 | -10.8384 | -57.52378 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd9ff4ce-ebee-3d2b-aed3-2837910c588f | -10.78919 | -50.3084 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8402bf86-ec59-356e-95c8-29605d624164 | -10.39938 | -61.21274 | 2026-08-20 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1cf85c8e-1aa2-34bb-bfef-02896b1e5423 | -9.12972 | -51.15163 | 2026-08-20 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c4ec802-e130-3414-bc91-1fc014a52ef0 | -10.55899 | -56.33035 | 2026-08-20 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b5eef8b1-6ea7-3fa7-97e4-3aefb5edf8c8 | -13.44576 | -51.80903 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b90982c-a5dc-3fbb-83a0-ab188c127fd1 | -7.53492 | -55.5752 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56e14702-5801-3077-a674-a350d84f66ab | -9.54819 | -56.79516 | 2026-08-20 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd9a9e1a-6367-3b06-a1a6-1bc01d205e12 | -13.40533 | -57.04497 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ff57d2b-fe17-31b9-8e8b-9491a76227c7 | -7.82558 | -61.60185 | 2026-08-20 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0273eaf7-133a-3a5b-8d8a-430decfff538 | -8.67424 | -54.63934 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| bcda1a00-0025-31d5-b970-823835c36dec | -11.83001 | -58.83615 | 2026-08-20 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f94c38f8-e0d1-3f2f-aa95-215e0cd8f06b | -11.19881 | -54.01584 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4753123b-4d19-37e6-9bc9-ce4d05a770df | -7.53505 | -57.65377 | 2026-08-20 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88f4b4c9-23dc-340e-befe-8af375ebb4b6 | -8.68048 | -54.64408 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8dc7619-30f4-3805-a65e-fe91006aa609 | -8.71697 | -49.61084 | 2026-08-20 05:06:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 257a17ab-c407-33f1-9c16-0447dd7f9545 | -14.44626 | -45.62428 | 2026-08-20 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dbcbba7f-e06b-3bbc-a123-5a8482147839 | -9.12181 | -61.60639 | 2026-08-20 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f59120b-a9a7-39c4-a297-fa546da2aac2 | -8.5351 | -54.8614 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f423c38-393e-3641-850f-2524f96c2b7e | -8.09985 | -51.67219 | 2026-08-20 05:06:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 16141d2d-b0c7-3c9c-b5e5-8c9b42b6fea3 | -11.43096 | -47.24419 | 2026-08-20 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 770d1113-3a15-3c0a-810f-aae5747d212a | -8.56522 | -54.66396 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7ee4124-c885-332c-9bc9-18a54983c3da | -8.10198 | -51.65738 | 2026-08-20 05:06:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09d7b822-3c3c-3ca6-b02d-4be36ec2ae98 | -8.55842 | -54.66293 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c0d7a0c-cad3-30a8-861c-8bd37bbdb37c | -7.41726 | -59.99527 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 656c54a0-6002-30c0-a75c-67596c6c1703 | -7.39893 | -55.53202 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccb14556-6dab-3258-ab3f-ae1b79cdb5c0 | -9.38755 | -60.5528 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aeed1a65-f342-3e25-8d1c-650ed40c6937 | -8.67483 | -54.65831 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68f745dd-0e42-329a-a54f-f8842454c321 | -8.58963 | -54.73925 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0dc2ba40-6865-3bd1-bca5-53546d91cafd | -9.22423 | -60.81238 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e41a769-4211-371c-9f52-6541c5e3ff36 | -7.43081 | -59.7875 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f513322-1be5-3510-a04c-9b33480b93e2 | -10.63126 | -51.61514 | 2026-08-20 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d00f5827-1218-34af-83e8-559ef2d71348 | -8.61275 | -54.72396 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc833519-aa05-34dd-8669-e46551e18b6b | -9.38752 | -60.55612 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90962bb6-44b6-3aa0-b576-72b5213ffd01 | -8.58697 | -54.78003 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dfc8fe6-2315-38cf-b8d9-5fc68e80c45f | -7.37849 | -55.53241 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0a169eb-6947-30a1-8c5d-70fb772d8c45 | -9.02395 | -60.49695 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 96371297-a983-34f6-b1f3-9f2db27142eb | -9.39507 | -60.55409 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4b9bd7b-947d-3b54-ae55-766cb3ce41bc | -8.49684 | -54.86298 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26af41ad-fe98-3f0c-aa62-154aa0376b76 | -11.21957 | -55.04957 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2f29926-767c-3d0b-8e05-0fc8b76718f0 | -12.8493 | -48.42059 | 2026-08-20 05:06:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d31c7c8-7175-388d-8ec4-4a9381365d65 | -6.86035 | -59.02927 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce9a5bcd-1c84-32c4-a428-6ba412129c49 | -9.39583 | -60.54948 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afb5fe8d-cc24-3825-9fb1-ba32a435e3bd | -12.04862 | -55.45346 | 2026-08-20 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92af1348-f23e-38cf-8ef5-bb2869065b02 | -10.32845 | -57.5642 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2495c429-f28e-39a8-9253-a5c8b0a04b1f | -9.39802 | -60.56266 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12bdfe23-4b33-3d57-9879-3bce475b95d1 | -8.51373 | -54.86553 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| babb6b28-c6c4-3f53-8f45-bd8db63c7fd1 | -6.80049 | -59.58084 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0af68f8-44df-3217-a0e5-1399143dc58e | -7.77184 | -61.15937 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b8e8577-ad08-3c70-af56-24259e27cb46 | -7.87666 | -63.76878 | 2026-08-20 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3c5ff2c-71a0-3df7-abc6-f615e0236905 | -10.75598 | -50.35343 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9459e3c4-f709-329f-922a-96c98409594b | -9.10712 | -60.93418 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e00f806c-7e8e-371c-b94a-a69d9c71664b | -8.56297 | -54.6787 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7bcbce4-7cb5-3756-b474-b42c51b4eec6 | -9.28484 | -56.89214 | 2026-08-20 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bb9c573-a797-3802-90af-6acc5e32ff11 | -8.56126 | -54.66713 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 951acd0f-12b1-3506-acaa-e977e95e8acb | -12.49566 | -54.74648 | 2026-08-20 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11ee3458-a097-3e3f-9e3d-1fb4279536b6 | -6.88834 | -59.03808 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a5bfe5b-85d4-3578-978e-edeeb711f57f | -7.01614 | -59.5458 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5176fefc-b731-341c-933f-f0b58d094a5f | -11.19504 | -54.81269 | 2026-08-20 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b93c83be-dba1-3f99-890e-d23c095fa588 | -7.868 | -63.76559 | 2026-08-20 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e25d1c74-e0e1-387f-9e3d-7e2bccf358be | -13.44719 | -51.43699 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 338e2118-d383-3a53-84e8-e1e42a5f1c2b | -9.47374 | -51.63789 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 902bfe3a-1db5-3fb4-a53a-269e7943f4aa | -11.81679 | -44.81374 | 2026-08-20 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40c3e09b-fdf1-37a1-b258-811b624e03b1 | -10.10755 | -54.28432 | 2026-08-20 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19542ea3-a322-3517-9dd5-ab089861fbd6 | -14.44737 | -45.61368 | 2026-08-20 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 901d69dc-d30c-30cb-8bb7-81fa092c027f | -7.43235 | -59.8014 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e256a060-432e-31d5-963f-642312f25072 | -6.95786 | -59.05309 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c31b134a-0c11-33dd-969f-f2c151ca8b92 | -8.57265 | -54.72905 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7114dc3a-cfa3-3fb0-b657-7fe06bc75cc3 | -10.83559 | -50.30136 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8622911-6397-3ab4-a390-e3227ea9f9ba | -12.38355 | -46.45397 | 2026-08-20 05:06:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 12b63fd5-7fc2-3847-a538-0f37b05885bf | -12.84332 | -48.42619 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2d2ab8a-a2a6-39a3-847c-22efa663b9f3 | -8.57372 | -54.67657 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb0ccaab-0695-3ee5-9939-c413aeca7112 | -9.39431 | -60.55871 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c8b9bf9-c46d-3287-85c0-fa0f4ec526db | -12.12559 | -57.21029 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 522081af-5d9f-314c-80f8-39bf3c762451 | -12.24621 | -43.17315 | 2026-08-20 05:06:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 7370ef81-96f0-3a0b-8fe4-6946230a1717 | -9.17113 | -57.01001 | 2026-08-20 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ff6fb7d-7793-3eed-be80-6952fb6eaaa5 | -7.57024 | -55.5664 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc0172e2-3932-37fe-8c67-b2220b8df28a | -10.75153 | -50.3528 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dd871415-6db9-32aa-b92f-072fa9073dff | -11.22242 | -55.05387 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd0eb3de-02d3-3b38-a27d-616ecc3e8fff | -9.208 | -59.77499 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f006c8db-ee3b-3c66-8ae1-09d91cd72192 | -7.60273 | -60.9471 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e73f1817-6156-3f3e-969d-b30b6feaf1c8 | -10.77968 | -50.31158 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 8a6b37ae-d8a8-32ec-9c44-431298c9d1e5 | -8.55978 | -54.81308 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f558784f-a8b3-305a-bc0f-4fa0a36a1635 | -12.05258 | -55.45028 | 2026-08-20 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a4d16a4-ebb8-3d28-9d54-07630f95cf80 | -9.15765 | -59.55701 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d62d7334-bc2c-3cff-88f0-71b46a25188f | -8.02386 | -54.0061 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e3c25d6-8e43-3202-ad1a-8ea1fdf751ae | -11.20119 | -53.99931 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04bd9cfa-fc63-32b6-8db9-3bd043799e0f | -13.45248 | -51.79005 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0977bb1-4d5c-39c0-b213-45c2610e6094 | -8.53625 | -54.87651 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8694794-7a1b-3d8d-b207-da2ac2c3ca13 | -9.12244 | -61.60279 | 2026-08-20 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README49.md)
