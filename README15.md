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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdd1b0c9-810b-35c9-b46f-282a156fda9d | -10.45529 | -45.17275 | 2025-08-09 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4a75492-a2c2-3d9b-947b-9c5e3c19434b | -11.73759 | -44.95786 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f8409fc-3977-37d6-9dd0-001153948820 | -12.68867 | -48.20206 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 358664e9-e051-39bd-9c30-76878c442a96 | -10.63294 | -44.75948 | 2025-08-09 04:17:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34ee3e06-acfe-389c-8a6e-f4d84975e62a | -14.50502 | -52.12105 | 2025-08-09 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50f0583f-de23-3df6-a086-4076b61f711c | -15.17953 | -48.71325 | 2025-08-09 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6a055a2-5922-355b-b545-96dc05dd610b | -19.81517 | -47.06594 | 2025-08-09 04:17:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 76.2 |
| fb1200bd-3d50-3d34-a307-87452ba283c7 | -9.86819 | -49.96383 | 2025-08-09 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afee618b-356f-3d07-85d4-987844293a02 | -12.04823 | -47.50611 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1a47a12-6720-3c80-9226-1fb1279f09c8 | -11.37963 | -54.35188 | 2025-08-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66604243-cdf3-3c63-822f-f36c0378f40f | -12.71156 | -46.37361 | 2025-08-09 04:17:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d229444-d7c7-328a-983d-f9ae11c6d58e | -11.74201 | -44.95135 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77fa2011-45c2-3978-90d1-11f871d7a7ce | -16.31886 | -49.03926 | 2025-08-09 04:17:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ebdf9c6-ffae-34f5-9c12-342b81f9b6c9 | -11.79669 | -44.92764 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| accdd940-f10b-3cf7-b6e7-6668514d81a2 | -11.21081 | -45.31759 | 2025-08-09 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab9da4e3-deab-3508-8409-5b468c560675 | -12.68502 | -48.20145 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c7b10964-c3d2-3856-b059-6e5b80cd014e | -11.40244 | -42.29498 | 2025-08-09 04:17:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cffa1d95-1f45-3741-b6d1-25f9e7080e2b | -11.93154 | -44.54617 | 2025-08-09 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 946152ac-1f2b-38fc-b7ad-d7b536223217 | -11.74588 | -44.94835 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69db1d8f-7414-38e5-ae77-14b6410569cf | -10.82957 | -49.37914 | 2025-08-09 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 258f54b1-d4f1-3c0f-b66f-9604a3cb6d3d | -15.67419 | -48.11163 | 2025-08-09 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ac866d0-1d9d-37ba-acf4-9b2454459023 | -10.83359 | -49.37985 | 2025-08-09 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 621306ac-11e8-3f2b-83fc-6542697d4b78 | -13.04851 | -43.85163 | 2025-08-09 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ead9f6f3-fdca-31b7-b319-cea7aec34b9f | -11.03765 | -43.09181 | 2025-08-09 04:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4698d10c-77a6-321f-b403-9f1837588fac | -14.96804 | -49.55643 | 2025-08-09 04:17:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1aa52e6e-307a-3c3c-ba60-1bc7ab7ed3d6 | -14.36858 | -51.11381 | 2025-08-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0dbabde-1687-3803-be5b-c240761b4f0f | -12.03729 | -44.01899 | 2025-08-09 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d0d1e22-3af4-3442-a645-84014435578a | -11.73865 | -47.48963 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abfc80f6-a6a7-3d58-8078-32603bc76ceb | -16.79026 | -47.51743 | 2025-08-09 04:17:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2dd6090d-44e9-3d74-97aa-2b12cf4190a0 | -9.01739 | -51.11113 | 2025-08-09 04:17:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33ec939c-a3ce-3a3a-bd01-b26a1ff5e73a | -9.86613 | -44.70375 | 2025-08-09 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4694e06-56d4-3ebe-ba3a-f9c9fc0f6e48 | -9.01547 | -51.10351 | 2025-08-09 04:17:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27497cf0-2ed4-3def-9133-88530177edc8 | -12.4058 | -47.78251 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4216eda3-540f-35eb-86bb-af272b6ff481 | -16.79367 | -47.51801 | 2025-08-09 04:17:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63aaf059-b7d6-3899-bf08-4f3e2187b090 | -11.963 | -45.74306 | 2025-08-09 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6ac2bb9-6794-38aa-b455-fe571447d333 | -14.16316 | -43.66943 | 2025-08-09 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a898c91d-a160-3f37-8dff-f7a92bbbf717 | -13.04642 | -56.84999 | 2025-08-09 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fd8cf47e-2c50-38f0-8902-2a4fc7a65312 | -13.63318 | -49.01538 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b86e8409-a3dd-373b-b799-5f2704fb2712 | -13.62985 | -49.0111 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e24ad0f9-e54e-3359-9674-816181e6cec8 | -13.62515 | -49.01593 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 553f1183-320f-32d3-ba12-372ed499e02e | -9.88123 | -47.40623 | 2025-08-09 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f5c0372-618e-3422-a030-3861c042f4dc | -14.61536 | -47.14993 | 2025-08-09 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72ddfa52-ca0f-3b41-b38b-b1a4e52d6ba6 | -11.8 | -44.92817 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afd91977-47fc-319c-8956-391c8348fccb | -10.60577 | -48.36073 | 2025-08-09 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 7ebf7f86-e3fc-379a-bbe4-eb2817cdd70d | -14.49685 | -52.11464 | 2025-08-09 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8d1eb1e-4482-3613-ab65-96c7935ce876 | -14.53038 | -52.11843 | 2025-08-09 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e13f7a4-2dfd-36b1-a78a-b013de154fe3 | -10.44974 | -44.34613 | 2025-08-09 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4aef6f69-7f8e-337d-8203-885c363e6a2a | -13.78123 | -48.88213 | 2025-08-09 04:17:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4060ce34-ee6e-3cf4-a7d7-98e7785faa0b | -10.62962 | -44.75895 | 2025-08-09 04:17:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48a66e2e-9bd6-3a69-8c44-824268b0e071 | -11.77583 | -47.39909 | 2025-08-09 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d9dda41-3de7-39a0-97ea-f68cceb2e6d2 | -13.62897 | -49.01628 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe3cebdd-4285-3244-82fc-68465f73f78e | -10.45897 | -48.81118 | 2025-08-09 04:17:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6d72366-a2db-3e1c-ae80-7f171c1fbb2f | -10.45253 | -44.39313 | 2025-08-09 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ef0895d-96b7-36fb-9c8d-7329c87a8dcb | -16.802 | -47.53115 | 2025-08-09 04:17:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b61fe7f-fa75-3e1b-acd0-1ccf1db88f76 | -10.00365 | -48.12876 | 2025-08-09 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cfc5d450-b863-353a-a390-b827653a4b29 | -12.09973 | -44.73205 | 2025-08-09 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1ec420a-32b1-3be8-834d-6457c7affa29 | -11.77752 | -47.56459 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18da3d66-6963-3f64-ab8d-ef4df3264691 | -16.74664 | -40.58517 | 2025-08-09 04:17:00 | NOAA-21 | FELISBURGO | MINAS GERAIS | Brasil | 3125606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6d4bc42b-4ff1-319f-a18a-560a9e15fb87 | -12.41229 | -47.78789 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d398737a-0640-3c60-80f5-a496c66a5208 | -16.61903 | -49.02253 | 2025-08-09 04:17:00 | NOAA-21 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41839649-bd49-3b93-9c93-ecac5079963e | -12.10028 | -44.72853 | 2025-08-09 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f582800-81aa-316b-be05-745dc0630f93 | -11.09243 | -50.50136 | 2025-08-09 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b3e595ab-6cb5-3e8a-8e6d-27211a2d3b08 | -11.32944 | -55.22108 | 2025-08-09 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc8872b4-d0ba-354d-8112-ff752948fc65 | -14.3575 | -47.0946 | 2025-08-09 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f362240-5cd3-362e-beb2-0aa6715b003e | -20.87545 | -48.45232 | 2025-08-09 04:17:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e887e02-3541-307f-b248-3bb27ddc59bc | -11.74366 | -44.96244 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc9b8e4b-3c52-3e15-bf0b-102a51d50730 | -16.68246 | -47.61705 | 2025-08-09 04:17:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c34f93f9-5d1f-3388-a0e4-a5ecd80aea49 | -13.05295 | -43.84498 | 2025-08-09 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9680e93-7c59-3167-b448-6e78d5fea4ca | -14.35345 | -47.09782 | 2025-08-09 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efc892ad-6086-3b93-b30f-db26faf9066f | -13.61104 | -48.985 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5cdd0a7-8a81-3c15-b68b-256dffcff7e6 | -12.68511 | -48.19994 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ffc67e5e-6da6-3e0b-a9c4-cb33e750979e | -13.17955 | -43.68379 | 2025-08-09 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d8d7051-ceaa-31be-9a80-0a2ce19cc78c | -9.86116 | -44.69214 | 2025-08-09 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4da5495e-a101-363f-952a-def2df8211cc | -14.50693 | -52.1189 | 2025-08-09 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 410f8207-37ff-31b1-9fd4-b8d22e1f8ac3 | -12.56569 | -47.10817 | 2025-08-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a91f43d6-9cd1-3a53-8743-dfdf0cb3a07c | -14.49879 | -52.11254 | 2025-08-09 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82bcf6f1-7530-36b4-ab94-ac67493d6632 | -12.03674 | -47.51381 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53cabffa-8feb-36a6-8e5a-3edccae17fbc | -11.93816 | -44.54723 | 2025-08-09 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6416f7e8-a0e9-344d-a035-611c8b89cc56 | -14.37357 | -51.11052 | 2025-08-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7695708d-ae45-35ad-9fcf-b00f96b15eb9 | -16.79429 | -47.51421 | 2025-08-09 04:17:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d57fb081-050f-39d1-a8cd-21f1d1e19fe7 | -12.55937 | -47.1032 | 2025-08-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e4a0c66-4456-3f45-80a0-fbc923844fe0 | -13.18345 | -43.68071 | 2025-08-09 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f64aca30-8606-319e-8066-d417ced1d589 | -22.14965 | -49.4498 | 2025-08-09 04:17:00 | NOAA-21 | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d9fa8112-04a7-3a4f-822c-ca774bbd124b | -12.5665 | -47.12471 | 2025-08-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e917fb39-8fb4-3da1-ac3a-932d38efd447 | -20.72521 | -42.76384 | 2025-08-09 04:17:00 | NOAA-21 | SÃO MIGUEL DO ANTA | MINAS GERAIS | Brasil | 3163805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bb84465c-cc1e-3405-a842-888458f54188 | -12.03318 | -47.5132 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f1625b5-bc14-30db-9b3e-16d65831bde9 | -11.92387 | -44.85454 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d13b40e9-fe06-3788-a17b-f1df91a51b57 | -9.88208 | -47.40553 | 2025-08-09 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4945ce58-8e5c-3379-a088-04471d9509e1 | -13.07187 | -43.82924 | 2025-08-09 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c5c4944-e2fc-3e0b-be2d-abb15ab0a1df | -13.61405 | -48.99006 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebb49495-d1bd-39ec-81d4-be70d25aaf7f | -11.74477 | -44.9554 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79723e0d-bde5-328f-a9b7-0cc95601e6c4 | -13.55291 | -55.25356 | 2025-08-09 04:17:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 82770f77-0915-31bc-8ac4-17f5ed7dc140 | -16.25272 | -48.44807 | 2025-08-09 04:17:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b8486347-adac-3b56-9461-a10f665d17e5 | -13.63225 | -49.02059 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bf84219-53dc-3ab2-b863-d5e4ae4aa36a | -19.81127 | -47.06902 | 2025-08-09 04:17:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 9c02bc14-5338-31b9-8bc4-024280924b63 | -13.63489 | -49.845 | 2025-08-09 04:17:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e41822e7-c9f3-395f-a399-b5f091a883f8 | -14.11162 | -45.4101 | 2025-08-09 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7ee2af8-bd21-3f4b-9b42-7b1f81897f31 | -17.34686 | -43.18495 | 2025-08-09 04:17:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c6aac2f-230a-3331-950c-591ec3a2b69e | -20.57596 | -41.68913 | 2025-08-09 04:17:00 | NOAA-21 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| edbf620d-a406-3536-b17f-55e5e3ea4e6d | -13.60649 | -48.98893 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README16.md)
