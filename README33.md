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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 798a7856-3695-3c3a-b901-ab4e49117f1b | -9.89361 | -45.82919 | 2026-09-19 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28b0dd85-d86f-3d34-83b9-eb881629c871 | -9.68336 | -48.3269 | 2026-09-19 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d26606d8-17fd-3566-a070-0d3cdbdac8c9 | -6.00749 | -49.17117 | 2026-09-19 04:02:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 975aa05b-2055-3020-849c-0460b88e12ae | -8.81727 | -46.94461 | 2026-09-19 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24fbef1c-0960-3e05-8f22-411a34ad0967 | -9.88931 | -46.55553 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d80ffbdf-4fc8-3c00-8d1d-9a67d1ddb370 | -3.85049 | -50.01001 | 2026-09-19 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3611f962-ba71-35fd-af31-69f433888932 | -9.78545 | -45.05831 | 2026-09-19 04:02:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 86e39157-d14d-3fed-8d47-9debe03f75ed | -9.35235 | -50.11652 | 2026-09-19 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6d48c81-01be-33be-abb0-67f7d2c7583e | -5.13741 | -39.18145 | 2026-09-19 04:02:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 484dbff0-3354-3c46-bdd9-681ecf6c53a4 | -8.08345 | -50.965 | 2026-09-19 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 61e8051f-97ba-3b14-8e1f-f12888077d56 | -7.12507 | -42.07818 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9c11a9d5-d148-3eca-bc72-b6379df30f1f | -6.26431 | -41.66452 | 2026-09-19 04:02:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 184623de-461c-302b-8698-03bd19340f5c | -3.36441 | -50.4568 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1b8e39e-a477-325d-ab9a-0c409f0a8689 | -10.40039 | -48.34054 | 2026-09-19 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12fdb852-9e97-3c1f-84fd-c4147a2a2560 | -6.92225 | -41.70156 | 2026-09-19 04:02:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bf4a0b30-3bea-3563-b338-ce93a6c93aa7 | -8.6153 | -54.60253 | 2026-09-19 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1e6f63ca-066f-330b-a768-44524655e5c2 | -7.75606 | -46.7209 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f96120d-a6c1-3989-af30-94ddd26cb0da | -10.20318 | -46.59374 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff267e3c-2ee4-36af-853c-b5c558d99f47 | -2.81877 | -50.47764 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 707f16e9-d69d-3f74-ae52-888cb6cc1003 | -3.02307 | -51.19617 | 2026-09-19 04:02:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd2431b0-f071-3f2a-ad0e-06267818376d | -8.2346 | -45.6018 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1c25dfc-7605-3d9c-a289-759c7400830c | -9.04467 | -48.72426 | 2026-09-19 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d64b3866-a535-31a7-8a5c-51f340225e9f | -7.08121 | -40.08889 | 2026-09-19 04:02:00 | NOAA-21 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 59a7a43b-f56c-346e-9c3d-af8957fc6fc2 | -10.07351 | -45.6455 | 2026-09-19 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90fd94e4-8c71-3812-b7c8-012f1c4bf54b | -8.65986 | -45.44616 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d2581be-5bc9-3d91-a98e-3284eb7f9002 | -8.45464 | -45.7091 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7448f6d2-bcb4-3ef4-b337-1d336bc1cefe | -8.81291 | -46.94387 | 2026-09-19 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe97da4b-f144-30eb-a595-a190c97d744a | -5.14468 | -45.77082 | 2026-09-19 04:02:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8e613061-26d9-3137-9f16-d9c8e32713d5 | -8.77491 | -48.66838 | 2026-09-19 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3030feca-677c-3665-91e0-af5a68a05892 | -8.6792 | -45.42839 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc876850-81e1-3e2c-809f-f15d6fc8583b | -7.77829 | -44.89564 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c98c2dd-31c6-3f70-b376-9eb212ec924b | -2.66053 | -49.48459 | 2026-09-19 04:02:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d5225e48-997b-3ac7-947c-c6734a60256c | -2.81425 | -50.46724 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6c0ce44a-1bbc-3799-8742-2fdbb7a5be6a | -8.771 | -48.67528 | 2026-09-19 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1cffc0b0-6121-3bc0-9b41-7477b1e70665 | -9.79545 | -48.33429 | 2026-09-19 04:02:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| da8b0a39-4c09-34b1-9706-623decaab2ca | -7.75533 | -46.72514 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70473f6f-332f-3772-a6b5-90d9322241e7 | -10.13462 | -49.15466 | 2026-09-19 04:02:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57163d50-c351-30f7-be30-d7f7eb2008cb | -6.09018 | -44.3066 | 2026-09-19 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2a5648b-9813-320d-9b06-43b88d1530c3 | -3.36663 | -50.4435 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2247e95-ab9d-3a28-a6f4-21954ffe95b3 | -9.19589 | -45.77925 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a77cf99-67bb-31d7-8fe9-9718e396624d | -6.99081 | -42.17123 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 74767d1d-0447-3aa9-8d31-9c03dd9eee8a | -7.78139 | -44.89362 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b72f7db-c304-3e61-84a4-4fa69ceba117 | -9.03968 | -48.7524 | 2026-09-19 04:02:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70120e51-fa6b-3440-8b8c-33145a20ace9 | -8.67355 | -45.32099 | 2026-09-19 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c749f93-576f-32f2-ae66-d357564de1f0 | -10.59162 | -46.54313 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be372771-641f-329c-bbe4-8200d412e990 | -9.79645 | -48.32882 | 2026-09-19 04:02:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 09b48a15-da04-3e97-9034-a82b63f9fad8 | -9.04079 | -48.7177 | 2026-09-19 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 464e18fc-b9d6-3934-a54d-2cab66222e43 | -8.77876 | -48.68828 | 2026-09-19 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 22.7 |
| cfef1946-e9f0-3271-991c-2a64987abdf3 | -8.60901 | -54.61528 | 2026-09-19 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7dd2d03a-a164-31ed-9703-253e85db0d89 | -8.77318 | -48.66328 | 2026-09-19 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e5ea9ecb-74a2-34b0-8c65-1c7994da4dcd | -7.19098 | -50.8352 | 2026-09-19 04:02:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ca4e4055-9a20-300b-a68f-5c8ab77c47e9 | -8.24547 | -45.6109 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bdfdf9e-52b6-3278-95fe-ad6d9b30a342 | -9.88454 | -46.55019 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5263efc4-a258-3c24-bc7d-a1dd4b0d66c9 | -7.63547 | -45.82496 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98b70b6d-8839-3455-85bf-6c8a11276100 | -7.60722 | -45.42789 | 2026-09-19 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 01b98f96-16e6-30eb-b8b4-9e2911a9c11e | -9.80236 | -46.09816 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77585f53-fff6-3785-988f-d7bbd749cba5 | -8.87941 | -45.94158 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 395df451-0453-37f7-9e3b-f61fe6f48898 | -9.76025 | -45.06857 | 2026-09-19 04:02:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ad1b834c-0aba-386a-8ea6-f19ca77b243c | -3.35898 | -50.46327 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5c0b0d29-acd1-3ee9-b4bc-5af64e5b0b80 | -5.33244 | -48.98853 | 2026-09-19 04:02:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 060fe7e1-225f-373a-8550-614bde85fe9f | -8.36286 | -47.2385 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aab23bd2-3f3b-3225-84df-f07889f59637 | -7.7944 | -44.84774 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3b1e9dd5-8ff8-30aa-b752-2020140c24cb | -9.2401 | -46.20453 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0a9e9234-c834-31fe-85b4-4576934e89ec | -9.05248 | -48.73717 | 2026-09-19 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d45705fd-3d31-3d63-9ecf-75daba58e9ae | -9.61145 | -45.89425 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2f4cc04-ac0a-3517-bde7-66c9362e66a9 | -6.95006 | -43.10345 | 2026-09-19 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a75a227-c4f8-3ac6-9cd3-27a4b0219d09 | -3.3358 | -50.11917 | 2026-09-19 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0df72b38-a638-378b-8143-1234acf21752 | -10.31453 | -45.31349 | 2026-09-19 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d2f1475d-f7e9-35f6-b3ff-82e9e8e61eec | -7.78328 | -44.83345 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd4a941b-8c4f-354f-b009-5d897bb51790 | -8.61098 | -54.58741 | 2026-09-19 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 25a7dc66-2cb5-3621-a80d-59e524772d7e | -9.23949 | -46.2081 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9fbd29e7-6c4f-389c-9a78-d34fa5384a2e | -4.55455 | -42.97423 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5231904-cd57-38cc-8944-1a7232cc8e10 | -5.56586 | -48.45223 | 2026-09-19 04:02:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e987a823-81ff-34d4-ad71-f36cb3c053fc | -2.8226 | -50.46144 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| af54bf56-7842-360a-b02b-fa4b7bd28663 | -8.99042 | -50.17092 | 2026-09-19 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efa62d07-1ab6-365e-b570-632ecb223dc4 | -8.77113 | -48.66104 | 2026-09-19 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 39eb52df-f4cd-30ce-8aa7-989934f4569d | -5.07178 | -44.85452 | 2026-09-19 04:02:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27a0d487-580c-3818-acc0-05171798a6cc | -9.9061 | -46.53347 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 509d8310-81e1-3d20-9b15-a9d514374e2a | -6.985 | -42.18564 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aa533f38-d1e0-3b90-b977-5864b6ba4502 | -3.33067 | -50.11376 | 2026-09-19 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19005705-aa78-3686-925d-13657a474fc3 | -7.40506 | -49.84908 | 2026-09-19 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e31f7b74-e720-3c10-a19e-7af8e5d3872c | -9.74609 | -46.08398 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3443d04d-0874-3927-a4c8-81e339ef79d1 | -10.53373 | -46.75092 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b2cc43a-aac7-3e67-8ad7-153063596cfe | -10.20905 | -46.5952 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1e12f00-2d2f-3609-906c-95431d350e51 | -9.91094 | -46.53035 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 924aa9fd-5173-3f20-8cac-3b67eade8827 | -9.56704 | -45.44793 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 403240f7-5108-387c-9967-92fdb8bc5c35 | -10.09624 | -48.4192 | 2026-09-19 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59e08680-10f9-372c-b8b3-4754a9fb6cfa | -6.02692 | -51.76969 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9134ab39-e543-3401-aea0-03b8fe4d4df8 | -4.57376 | -42.94717 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5078df5b-0208-3b55-8e4f-dbf91f032210 | -7.3263 | -45.33012 | 2026-09-19 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ea4e59d-2580-3dcb-8f9e-0deeb268383e | -9.70555 | -45.98038 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 102cd75b-8550-3da1-b3c1-9ae22c00d543 | -9.90883 | -46.59108 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 786b064b-fcd3-35de-8d52-ae6fbb0344b1 | -4.27423 | -46.53644 | 2026-09-19 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c10cad9-4679-3289-ba2a-8dfb84c2464a | -6.96384 | -42.56195 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b6075b5e-72cc-3ffa-ae5e-19eacd738013 | -7.37725 | -38.98697 | 2026-09-19 04:02:00 | NOAA-21 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0e3198b3-af03-3b40-9cc1-4021c508fb2c | -2.82486 | -50.4786 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 69e7ada5-9fc5-3ae5-874c-d920b74723a7 | -4.54957 | -42.98206 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ef52db9-64d8-35b9-8954-daeb5ea921c2 | -10.53865 | -46.60246 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7043bc8-c937-3a00-b6b3-e628ec99ee09 | -3.04226 | -46.92782 | 2026-09-19 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2b44c16-2eb3-3d4a-b7c9-2a0704a13014 | -5.23334 | -47.56211 | 2026-09-19 04:02:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README34.md)
