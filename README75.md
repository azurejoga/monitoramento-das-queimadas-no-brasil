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
| e3cd07a3-718a-3c0d-b2bc-c9fbebef52b5 | -13.25271 | -51.80245 | 2026-09-21 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a52f44f-0efe-346c-9e07-25cdff29c50f | -9.07779 | -61.36041 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 481ae1f8-99bb-3d3b-aa3d-ad207b8a7541 | -10.87827 | -53.96496 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d83baad2-7c9d-3a5f-b6de-a147fc16188e | -10.92182 | -53.94196 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ed41b12-90cd-35ea-9adc-55f97d2698eb | -9.556 | -66.04113 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ba0937e-0df6-3dd7-ae7e-98aadaa75ad4 | -6.45423 | -59.97164 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d45bcf8b-7076-3955-813e-0ec31a242c20 | -10.54054 | -57.44083 | 2026-09-21 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e01e29d-db1e-3b84-a516-0c67e94e29dc | -11.95713 | -46.50524 | 2026-09-21 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6eef245a-86e2-3f3b-aa47-bf6f70d2e2da | -8.28796 | -50.92621 | 2026-09-21 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 798b4255-08eb-3c1f-a7c3-2af4200e2b59 | -10.4204 | -50.23643 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fb2eac5e-1a81-3b6b-8936-3939fb6f7d49 | -9.55412 | -66.05125 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 611db18c-e28d-3242-ba5f-be611c5eea6a | -7.58476 | -57.68533 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9621eaf9-8f70-3e21-8e20-264318f11a4d | -10.88066 | -53.97379 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e175702f-7cd4-36da-8133-e13e241fef21 | -11.09863 | -48.30632 | 2026-09-21 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 53e32c70-970a-3296-897c-8a982a81d3ad | -10.10214 | -69.13013 | 2026-09-21 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27485ef6-cd04-3b3a-88d3-2f492364d48f | -7.04321 | -62.95889 | 2026-09-21 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a76b2e7-b328-386c-9505-480021e5ddca | -9.27028 | -46.19381 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa99f636-354d-31d1-9cde-d1f821247ade | -8.77805 | -44.27684 | 2026-09-21 05:06:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a255403a-0e47-37f9-a514-4e14646d7b25 | -9.02307 | -49.82631 | 2026-09-21 05:06:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd830a5a-faa2-3569-87ec-44fa5dd8767c | -9.35959 | -60.3175 | 2026-09-21 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e71d0309-116b-31b1-97fc-8b9914b1d49b | -9.67996 | -54.34276 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ab5669d4-5161-3ceb-a2ec-0c73905835a4 | -6.4467 | -59.97039 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d499f91-4f40-3dad-ae85-9d9ed4b58674 | -8.35305 | -50.85494 | 2026-09-21 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bcca75b-abd4-3c47-804b-9095290d0a15 | -9.45 | -45.40147 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 11d9ccbf-b120-394c-8e93-40ed178c0b53 | -10.89344 | -69.3475 | 2026-09-21 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2cc1295c-72f4-38e0-9a65-eda54bc86684 | -9.98269 | -50.26289 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 919bac56-e2da-3d2c-a4d2-979cc4f6c38c | -6.44672 | -59.96767 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f3ca21e-8eb6-3278-9e60-fd38a01a1bd7 | -11.71098 | -54.55496 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d9f8a38-c7f4-3b61-adfe-80321a378339 | -8.74004 | -52.35385 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b695a3c1-9272-30e4-878a-23b9e51644bb | -6.44523 | -59.97694 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e074bd4-25f8-34e0-a0c0-645f74e36aea | -8.1778 | -54.73066 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9b4612c-3a5b-3e92-a6ff-e2f4dae71502 | -10.98391 | -50.59009 | 2026-09-21 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91a3229a-6412-3f1e-b6b3-0b59e3110d2c | -12.02959 | -51.49729 | 2026-09-21 05:06:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a70035eb-27a7-361d-bc04-a77ae46e9b35 | -7.32915 | -55.21679 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4366622e-b460-38fc-ac05-7b253da1ad84 | -10.76601 | -50.8164 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c4a1713-1920-31d6-aafb-975c6dfdc22d | -8.18174 | -54.72753 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c04a644d-7bb5-3409-8b6c-35d5d037beaa | -7.39963 | -55.22406 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbca72d6-3e6c-3e86-bcd1-24de997a8ac4 | -10.87237 | -54.08186 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eaae9f97-3a93-39db-9a51-783a369247b1 | -6.77992 | -58.60938 | 2026-09-21 05:06:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc4742ab-3235-316c-86e8-32a1d4d1153d | -10.6893 | -54.14783 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77a4a9e7-0fa8-3ab7-8e19-2e4d439a6606 | -9.54945 | -65.69652 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0534ed0f-eb71-3462-8420-0e73659a9503 | -6.77965 | -58.90669 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe85c195-30c3-3d5a-a8e0-06e7fa4b0a36 | -7.34527 | -55.2228 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9fb0d075-a489-3b21-b6e7-2d49b01a1635 | -12.81248 | -54.04824 | 2026-09-21 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b22f43fa-eb84-39d7-8a2e-7ce8035541ea | -11.25365 | -54.14809 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c498562-2144-3ee1-9ad3-5abb2d3e3d85 | -10.58529 | -57.48105 | 2026-09-21 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bef6107-e39e-3d04-928f-d765c8419be0 | -9.26554 | -46.18471 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1626d9e2-6f2d-342c-8287-a42ac69257b3 | -10.10961 | -48.43724 | 2026-09-21 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dae4cc9a-de36-3dfe-b237-462d50eb411e | -10.86944 | -50.92865 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1537a9e2-3e57-3077-8d16-a5b1781efea4 | -6.44221 | -59.97172 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80c3216a-943d-3e78-a364-9992913532b7 | -9.4484 | -45.40945 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| e481e747-bc8a-3898-a7d8-e67c55523ec4 | -9.27396 | -46.21141 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5295bbc-87d2-30c8-8ee1-8a3a6f481aca | -10.38376 | -48.90757 | 2026-09-21 05:06:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2196b687-413d-3927-98fc-a38fb066126b | -11.27805 | -54.13076 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 539a8587-940a-34cf-8619-abf0fd30d713 | -9.15694 | -60.80294 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ad8d2a3-8c63-3ba1-9e2e-2ca4d8ccdc85 | -11.72267 | -54.57297 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22fa5ff5-dd6a-3faa-8a86-fbaeeb1335f7 | -10.32963 | -55.3559 | 2026-09-21 05:06:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25a37d9f-29e4-384f-a9dd-034ef93db440 | -9.7605 | -46.05994 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e16a2ac4-bbb6-3e5a-8046-31ddaa5cf09e | -11.07999 | -54.02742 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 232f51bd-8523-3e09-81ba-fcd227ad4f89 | -7.32743 | -55.20572 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f4ad7d3c-227a-3d4e-9c58-1f90694aeaea | -11.05639 | -54.90984 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d4da69b-6797-395c-9363-4daf88c5282c | -11.71858 | -54.5764 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c5c5d4d-5ee3-3de5-930b-db6b9a748d55 | -13.61471 | -46.91727 | 2026-09-21 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fe18345-916b-30fc-adf7-1c799b9f5d97 | -13.86881 | -48.58795 | 2026-09-21 05:06:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7027d14-b54e-3dec-b4a4-1ddb177260d1 | -7.58755 | -57.68946 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 772d8bfc-c388-37b4-9df7-feeefb83bfcd | -11.08252 | -54.02701 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be71d756-006b-39e6-b947-795cd5696974 | -9.68401 | -54.33947 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c631ae94-bdd6-394e-a5b0-154b57133388 | -10.83849 | -50.89883 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fdca4fbf-ce9d-3b18-9e03-8ac336042458 | -6.46024 | -59.98201 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38406022-db49-3368-ad4b-61701d46019a | -10.83165 | -50.78742 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ee6e5f81-d904-3429-b17d-2ae69a036125 | -10.88423 | -53.97432 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4e98a3a-8470-3884-8766-9164bce11ad1 | -9.4561 | -45.40237 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 7696c8fa-69d6-3f27-a3a6-9c58968986d3 | -9.44281 | -45.40968 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 93fae5e0-7d55-34e1-85a9-47ab0e23c7b3 | -11.75483 | -54.57382 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80d470e3-4313-31ef-b60b-056c623675f4 | -9.46162 | -45.40797 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 48265dbb-00c3-38fb-9b41-8b3d901a3999 | -9.02758 | -49.82693 | 2026-09-21 05:06:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d90e4c5d-a80c-35cf-9519-334b78647417 | -8.16835 | -54.77028 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46b696fb-038d-307c-b22e-35c325721c7d | -10.75399 | -56.0024 | 2026-09-21 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 59f10890-61b1-335f-8537-b5b3a0af8a27 | -10.76277 | -50.7928 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aed51972-419a-31b4-9117-f5a96707c1be | -7.25147 | -55.58735 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc695b37-7c95-3145-92b4-aa1ef4f9a361 | -11.62831 | -47.77478 | 2026-09-21 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f2b9456-425f-3f74-bef0-babdbe4d4281 | -9.2986 | -60.53556 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea254657-3ff3-3087-bd16-75dc0df190f6 | -10.86823 | -54.08541 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b27eb4f4-6d63-345f-8959-ec4799a84768 | -8.18685 | -54.7395 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a19ddbbd-42fd-35cf-a515-6dec407f05b6 | -10.41922 | -50.24545 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2ea54e54-e98f-37ac-a7ff-784f142c82ae | -12.11289 | -47.04412 | 2026-09-21 05:06:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 737d216c-56b2-34dc-99c4-d58a469ea659 | -9.67012 | -54.31335 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af7f3b5b-8843-353b-ae84-3d54f2d0f594 | -8.23805 | -62.83839 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 310987cd-16af-3fa8-ad24-2cd52da9fcd5 | -7.58198 | -57.68118 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 50d5f761-480e-3218-9fff-cb8017e4b9e0 | -9.37283 | -47.77665 | 2026-09-21 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 258c4df5-5e78-3694-9dbf-dfdb3270a7c0 | -9.67417 | -54.33398 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af42f5db-2bd3-3758-b738-d3536d931f22 | -11.71975 | -54.56849 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5431cfe-cf77-3654-b840-9f11559a9ff4 | -9.80939 | -48.30652 | 2026-09-21 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52160bb2-4b9b-3f49-a936-af55adc39fd6 | -12.83019 | -54.05777 | 2026-09-21 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 67b8ced7-292d-33b7-86aa-83cfd352d7bb | -13.72236 | -48.79221 | 2026-09-21 05:06:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 074f4aa8-f602-3549-a033-b50055b40dde | -10.41145 | -50.23514 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| fa233c42-0b6e-36af-b4e0-80c58fde5953 | -11.02263 | -54.1446 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 588fe2cd-1708-3dd5-85f9-933cd13c0df7 | -11.27866 | -54.12666 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b65b830-3f71-319a-ae37-c4b97357b712 | -9.98603 | -50.26612 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 040bc03c-6c16-35f1-ad66-a1f25fd154af | -7.5807 | -57.67688 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README76.md)
