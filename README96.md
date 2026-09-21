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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3308685b-6dc0-3b33-b8fb-0d1dfd8943e4 | -5.37999 | -55.90088 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed4702a4-28cd-3bc3-922a-ee7597cd2451 | -6.10352 | -57.62389 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b02ec34a-c5c4-3e4d-9413-0ebb0f6feb65 | -5.83559 | -53.4851 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2cad5f3-8e6a-30e5-815d-609e076f8395 | -7.32741 | -55.60704 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b2ac76f4-115c-3e32-a67f-0dcc9ab5403c | -9.41155 | -65.92162 | 2026-09-21 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 337cd386-d980-31a6-85d7-fc5497fab439 | -11.02692 | -54.13998 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f137bba-cef4-33d7-b558-342fcaa823d4 | -9.17558 | -60.30457 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76370c25-81fa-383d-b58f-2f652533e4ff | -9.97972 | -50.25712 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1da45f04-f8c9-306d-a01d-ba5973c4b4b5 | -6.45544 | -59.98497 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a3fc8b1d-d9bb-3b3c-b75e-41cfc06282bb | -10.86939 | -54.07973 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b472489-f1cd-32f3-b635-a83d5cd6f4e4 | -10.39615 | -50.22766 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c9e93df-13b5-3ff4-b4e2-c862ec209879 | -6.40423 | -55.25297 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7b9a9ce-3d23-31a1-8046-a4b4b92e99ba | -5.81537 | -53.51642 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 106b43c0-4b08-3e74-8776-b7796bd87a97 | -10.38051 | -48.89879 | 2026-09-21 05:42:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ac30d68d-051c-33fa-b16d-b99607570c80 | -6.39897 | -55.257 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adbfdeab-3a45-3bc3-9ca0-22533151f0e3 | -6.99205 | -61.34457 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9fceb0e5-2526-3579-81cc-0eb08718d7e3 | -5.42224 | -60.21978 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 808da7ae-c006-38d0-b822-2e3244c07dd6 | -6.28496 | -57.74469 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 11d9964e-0d8b-3320-8d5a-921e2ed11789 | -5.88333 | -53.64046 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34f397a2-4b48-3941-a3a6-1cd47c84f3b0 | -6.73651 | -55.07278 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a476ea8-51ad-3f4d-814e-92c6e8fb4ae1 | -5.42281 | -60.21611 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59ae54d1-6a01-3b0d-a1b7-041b2ef41007 | -6.13168 | -59.96078 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18873929-d712-36ca-a419-a1559d7d412e | -10.38207 | -48.89682 | 2026-09-21 05:42:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d66fd693-281a-3c47-b494-9e91f7ace905 | -11.25349 | -54.14734 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c69e608a-cea6-3f06-ab02-fd2a74926058 | -6.14092 | -59.94675 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da69c19a-62d9-3413-b3f9-8aace9637fb3 | -10.86746 | -57.15841 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6def916b-65ce-30f5-9eda-71eec60191d0 | -5.82052 | -53.51709 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 129a0f20-6b84-3c85-9f78-8bf0102316e5 | -6.65338 | -59.96368 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa61451c-b3fb-3edd-a970-67c20f854786 | -6.7368 | -55.09066 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 324982a9-2718-3255-bfec-4c4c439d9721 | -5.22028 | -56.10712 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ab47923-b29f-32e7-b3fc-edcbd87a3ae4 | -6.64822 | -59.96774 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff6a32f0-9b2f-37c1-ad63-a235cd7ccc86 | -7.55313 | -61.32257 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cd376c2-bc06-3f65-93ad-80170443c9c3 | -8.7892 | -48.74594 | 2026-09-21 05:42:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8ce01f93-e3a7-39d2-b017-bf724ac1fa95 | -6.31405 | -59.96075 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99d001d0-491b-3c2d-8781-03b3af711c9f | -6.45661 | -59.97731 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1b8896d-b603-339c-aae0-da4749ab816d | -7.24975 | -55.59747 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 975981d7-6197-3ba5-812f-fc9a0a23880d | -7.58102 | -57.69334 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 32d86a02-1366-3a50-9413-03ac95b9dfa7 | -6.72053 | -55.08473 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6c02348-04cd-3f2e-a072-20187c0c310e | -11.17174 | -54.12182 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d805a306-ea94-3802-9c43-a29560da3a1c | -6.4275 | -59.97377 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20f7c4f2-b02d-337c-9f21-2f0fcfd6c8ed | -5.91959 | -57.67716 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b285857-8c9d-357e-84a1-316beba88603 | -10.76181 | -50.79223 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 61ea449c-2303-35ec-a078-458adbc537ea | -9.01773 | -49.82547 | 2026-09-21 05:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3fe354b7-90aa-3633-8793-0e85ba615df2 | -7.86672 | -62.53651 | 2026-09-21 05:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2c8d6c4-d7c8-362c-aea3-8e3897f5e8a9 | -6.28108 | -57.74411 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7ba4e49c-3460-355b-91f4-15ca92192714 | -7.5778 | -57.68766 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5c08c51-a39b-38de-b926-a170434ff391 | -5.92038 | -57.6741 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 103a1d04-19a2-35c3-aadd-11e264ef01bb | -6.44273 | -59.97514 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88283dd9-e6ad-3121-ba8f-ece3cdd43446 | -8.61432 | -54.59157 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5ee82eb-1df4-38a9-b209-bffd0a63a9f2 | -10.48757 | -50.28717 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8a5376da-8921-383f-9b8d-9b8887e2a45b | -10.20846 | -53.92198 | 2026-09-21 05:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3805e3a-83cc-33b7-99e0-f74c243f9e51 | -10.43183 | -50.2375 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bbab0dd3-ccd8-3eef-a353-4a9ecda80330 | -10.87923 | -57.16866 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7de66c07-724a-3c60-a91a-bed68f1d0468 | -7.81945 | -61.80631 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1b8fc51-91d3-31c3-a60d-bbeab1f332d7 | -9.56934 | -66.04997 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 779d25ff-04ce-363d-8694-e1a3e49260b8 | -5.84443 | -53.53295 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9025f75b-daaa-3f7c-90d9-5c33759e8fe6 | -10.77155 | -50.82159 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c578bf72-304b-3946-8c27-e087dd00af37 | -8.08053 | -55.34563 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 252a1354-dcff-3ca3-8d0f-e3aa551c7b3b | -11.09556 | -54.01654 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bf9e364-d278-37bb-947d-9ccffb3220a9 | -10.91798 | -53.95649 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27a9ea3b-da82-3ecb-950f-7a7f348bcac1 | -6.79716 | -58.79013 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f11d0211-ea9b-310e-9db4-d99faa5b1de4 | -8.8021 | -60.80059 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a3d72c7-dac9-312b-b881-3786b60129ef | -9.56789 | -66.05843 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68a9b364-f50a-3154-806c-7ece8518fdd2 | -6.94247 | -59.99861 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 157f2f58-5451-3b26-b9eb-0f39ac967fa3 | -5.87907 | -53.63376 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0961e520-e395-3b22-9ce2-232c825d933e | -9.54736 | -65.69417 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e54b3518-bc0f-3192-bae7-20185b803d63 | -10.88177 | -54.06767 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e2b83db-7ba3-362f-ad8f-cb1c1a16c553 | -5.84031 | -53.48882 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9616b8a-447e-3cdb-9a56-b9b14732c3ef | -6.13862 | -59.93864 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d0b3e5f-01b1-30a9-a2f8-b950587f8630 | -5.82096 | -55.70378 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5569e512-2646-350f-99e1-1cc009e95235 | -7.57855 | -57.68257 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5bd96d2c-52ae-39a1-ba5b-f924d86b1f0f | -10.38123 | -48.90429 | 2026-09-21 05:42:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17e10c25-7b4b-3fca-83c2-1e8a675377ee | -6.39501 | -55.25185 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba018e65-ee90-3e46-b424-4db11cb9ac55 | -10.46363 | -61.31115 | 2026-09-21 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f25c236-e0f3-302c-ac31-5127ff9bc57d | -5.75463 | -57.58043 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4b8f1ecf-80f2-3319-bc79-8f75883fa98d | -5.76632 | -57.58217 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 635b35e9-82dc-33e0-b232-d5e34d772e9c | -7.25176 | -55.58351 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c77e9a8c-1e0c-35fb-8cf1-0466dcd2cc28 | -10.92466 | -53.94723 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa8187bb-c87a-35b2-a5bf-7a18593916f9 | -5.20726 | -56.07735 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 722b8c98-16b8-3557-9c5a-c85bfae1755d | -7.33593 | -55.61238 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 96daa667-bd04-3d11-b8ca-7fbc3f486ceb | -10.9251 | -53.94383 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7e544d7-c7f4-30c3-b949-0d1cc57bafce | -8.77682 | -69.01945 | 2026-09-21 05:42:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c396343-470b-3e23-a75d-4a29c7f73509 | -7.38753 | -51.77373 | 2026-09-21 05:42:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8828d632-107c-3093-86e6-cc3b7ee1d854 | -6.16114 | -57.95406 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dcab2667-b134-3439-be59-2070f2e9b1df | -9.54712 | -66.00457 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f51306e4-8b81-3804-bb86-cec861acb90f | -5.83035 | -53.52159 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7196455d-1692-3b5d-ac72-ebc3f7db6973 | -8.24189 | -62.83634 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7b2059d-0162-3b4d-bf65-278787f7649f | -10.81591 | -50.77674 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 319ca761-dd6d-3581-b45f-fd2813950ddd | -7.87846 | -54.72742 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53e38fbe-db9c-32d3-8f47-30f6b2bff53b | -10.85983 | -54.11202 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46fe4225-2daa-39f9-95e0-06a6d04820cb | -10.91709 | -53.96331 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 950afde9-0e27-3947-b4ad-352ed0be2438 | -7.33245 | -55.21998 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70fc0974-7b0a-32d5-bfcf-71af70f9151a | -8.04679 | -61.32964 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6670589-c847-34a3-aa3e-d19f3bef982d | -6.06644 | -55.61766 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07ede266-f832-3434-8140-e33426258991 | -8.96863 | -63.5811 | 2026-09-21 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f80d2454-28f9-3c18-9370-e251d8c3d4c9 | -8.18188 | -54.72756 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15cce5dd-e33a-3a82-a15b-584d7a237635 | -7.57309 | -57.69214 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b1ba7288-34b1-357d-91d6-dfbd6b87b48a | -6.42082 | -55.01778 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea04807c-c3cd-3297-85a5-a8a811c2583a | -7.55538 | -61.33022 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a78b88da-c106-3b4c-b03e-cf886001044f | -5.21119 | -56.10982 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README97.md)
