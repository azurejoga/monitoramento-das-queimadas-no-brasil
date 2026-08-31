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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eaaaba76-1c6b-3e99-94ce-40311da4ff79 | -8.9368 | -50.187302 | 2026-08-31 00:11:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3526f21e-fc35-3616-9b64-731e2be1278c | -18.3013 | -43.233501 | 2026-08-31 00:11:00 | METOP-B | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3ae628de-0b0d-30c3-b691-227f1f14fcf2 | -18.282801 | -52.691299 | 2026-08-31 00:11:00 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 995df446-64c7-3314-8d50-0f81a8928ece | -6.112 | -57.662998 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fdb27a3-d49e-3fb5-9aed-463b37b3cb30 | -7.2886 | -52.358101 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f843f249-78f6-36a3-8121-8bc5b2e7f4ca | -14.4458 | -52.544102 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e5d58df-1776-31a4-bfcd-b324b5366c0c | -7.318 | -60.578899 | 2026-08-31 00:11:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 800ae5f5-1874-3cbe-98fb-34e0a9267492 | -10.798 | -50.652401 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 57e9035e-11b0-364d-a470-12ecb2b41e4c | -12.9485 | -45.939301 | 2026-08-31 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76fee882-f30e-3c71-9702-d14c23d356a6 | -11.3397 | -45.1586 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0fe5552a-9879-32d6-b921-27726c17e1ea | -15.0618 | -48.389 | 2026-08-31 00:11:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 10f02058-0057-3809-8ea9-21d5903d9529 | -7.6164 | -57.614101 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e78b379-d692-31a1-9fb0-37a445a52450 | -7.2852 | -49.846401 | 2026-08-31 00:11:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c191f79-dad7-326c-86cf-56bda76aeb75 | -9.1865 | -51.550999 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed05f72e-c782-3910-a442-0c8b5851f118 | -11.2184 | -45.082699 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8255eb6b-73aa-34a6-8bc1-3326e3a28187 | -15.2052 | -46.234501 | 2026-08-31 00:11:00 | METOP-B | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f01bf480-9fe6-3c34-8f99-67c33d802a67 | -9.1522 | -59.338799 | 2026-08-31 00:11:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54cb21ab-052c-3d30-b920-bad8132c0ab6 | -7.0584 | -52.712601 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2ab56fb-80e6-332d-aab4-69ad2a6ef149 | -12.7786 | -46.451401 | 2026-08-31 00:11:00 | METOP-B | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71f78c8f-9e14-3ac4-95c9-63291ae05a61 | -7.1102 | -42.7561 | 2026-08-31 00:11:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 526e5f1e-0c2c-33b5-a2e8-e84d80c806ea | -11.7895 | -47.668598 | 2026-08-31 00:11:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3bf6ba57-23a1-31e9-9cf4-5c6d5b4c7553 | -15.6221 | -56.411098 | 2026-08-31 00:11:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 90392315-7e37-3d43-8798-f242342aa8a1 | -9.1947 | -51.541302 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4efeff9e-0f71-3a35-9d00-a1ff1ff114d2 | -4.1429 | -60.694901 | 2026-08-31 00:11:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 477b893e-7ae5-3d99-934b-978cb18f1362 | -14.5873 | -54.113701 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3b4cce85-8835-3da7-939a-443548600dcb | -1.8828 | -48.8325 | 2026-08-31 00:11:00 | METOP-B | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 644009cb-3381-3640-a147-abc0d4ad8624 | -10.7214 | -50.631199 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 70602baa-a802-32cd-8093-b18d6e204282 | -9.6614 | -50.858898 | 2026-08-31 00:11:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c18d71fa-c72c-310a-8e42-f2977565c179 | -8.3918 | -44.999802 | 2026-08-31 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b148ddb5-9d19-3a77-ba69-7ca5f65c4dc0 | -8.2365 | -54.942902 | 2026-08-31 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eab89dc3-420a-352b-83a3-b95c55d860c4 | -10.7322 | -47.959999 | 2026-08-31 00:11:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abcab76f-43eb-3940-b4ab-cbc947b1df56 | -10.7516 | -54.0341 | 2026-08-31 00:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 433caf01-7f80-3fb5-b8fc-e34e2576d31d | -7.3276 | -60.577 | 2026-08-31 00:11:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f99b5600-988e-3e5a-bafa-6407516fdb52 | -15.3607 | -52.6805 | 2026-08-31 00:11:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9c692a99-b5d5-361b-a7df-be5fd6caf32c | -11.3266 | -45.1903 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 286e3f59-7b8c-3e34-9f95-7c7a21d15da8 | -15.1938 | -46.229401 | 2026-08-31 00:11:00 | METOP-B | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4cf27826-77fc-3156-b293-33145a7dda72 | -13.1971 | -44.0714 | 2026-08-31 00:11:00 | METOP-B | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1b2d211-9bb2-3e21-8065-a65a4258d56f | -7.531 | -55.324001 | 2026-08-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1721aaea-3aeb-3602-aa4b-625537f183b1 | -10.7405 | -54.0606 | 2026-08-31 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 95d54238-7042-3054-a0fa-044d164cbe50 | -6.2537 | -55.4308 | 2026-08-31 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 5a6f743c-ab38-3b06-a10a-1a0eeb89de47 | -15.9077 | -56.233 | 2026-08-31 00:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 14fc679a-39cd-3b2b-afe4-cbb3c657324f | -7.2933 | -60.5905 | 2026-08-31 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 166104fa-ec6e-3077-ba36-e5c6ac85821a | -10.7621 | -50.8495 | 2026-08-31 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4d0e6687-f8bd-3c4e-bdc2-009baba3a871 | -6.9367 | -55.636 | 2026-08-31 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 381bec8b-95c6-3b63-9fa9-b5381fcd33ce | -7.3119 | -60.5706 | 2026-08-31 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 38b72b9a-6700-377a-a62f-b1fe5081db78 | -14.6064 | -54.0921 | 2026-08-31 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 1331f470-34dd-32c8-98b2-3e3db615b545 | -5.2546 | -55.9303 | 2026-08-31 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 4a4d8d2e-a345-3f37-b185-9d7298d7115d | -10.781 | -50.8475 | 2026-08-31 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 8e1fb267-ec61-3b0d-98f8-4ff411379335 | -15.908 | -56.2125 | 2026-08-31 00:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| e48ab89f-f5b6-3fac-966d-ff755b764b26 | -7.3118 | -60.5897 | 2026-08-31 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| d39953ac-e661-3752-a16d-bb7b644da55e | -10.7596 | -54.0384 | 2026-08-31 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| fca1d3a3-d79b-31f9-975a-c055c8b686c2 | -7.532 | -55.3441 | 2026-08-31 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 47a3c4b6-05c7-3b46-a5a0-5f9edc84083e | -6.9176 | -55.7166 | 2026-08-31 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| bdc9af75-d344-3204-9280-22b6bc804d72 | -14.1831 | -52.8667 | 2026-08-31 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 25e0174b-3669-3149-8c86-a0f9fe8ab387 | -7.3302 | -60.589 | 2026-08-31 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 51e46694-d3e6-3eef-b7a7-45d3f3cf3c9d | -1.6042 | -54.415 | 2026-08-31 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b84acc6f-2cd0-3b08-aacd-f141d5164cef | -4.85 | -55.8266 | 2026-08-31 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 23060e09-f02c-3c33-86de-8e7ed9c78681 | -10.7407 | -54.0401 | 2026-08-31 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| f6c6f660-24cc-3ba2-8dd6-e71be256ac0d | -14.2021 | -52.8854 | 2026-08-31 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 9c6ec251-d456-3f06-88e1-f11802034939 | -10.7618 | -50.8707 | 2026-08-31 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 4d223c2b-4f33-384e-aee0-432ac86e0648 | -18.2908 | -52.6602 | 2026-08-31 00:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 373f483e-3e4d-37c6-805d-aeb43063845c | -14.6061 | -54.113 | 2026-08-31 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 97df4b7b-9f18-35e2-ba7c-8bd4d9bc1235 | -5.2362 | -55.9112 | 2026-08-31 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 70277096-4e78-340f-87e7-fb198bb85d4c | -5.9451 | -57.6906 | 2026-08-31 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 31183f04-bb21-39e8-84cd-7f26f0253126 | -5.2548 | -55.8907 | 2026-08-31 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 254.8 |
| 02aa11f7-9005-37f6-9470-599dfbba46f7 | -8.9481 | -62.3704 | 2026-08-31 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 4105f1cb-ba4d-31a7-9c7b-e9472e9d0999 | -19.154 | -57.3978 | 2026-08-31 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| f0566161-a996-3f91-99ca-b8e8350b5f91 | -11.3423 | -45.1982 | 2026-08-31 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 171371f1-d726-36f0-aaa1-577471db47d2 | -4.1515 | -60.7068 | 2026-08-31 00:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e29dba7c-b138-3b00-9692-5396959410e7 | -5.2547 | -55.9105 | 2026-08-31 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 370.8 |
| 2151e857-d283-34d5-b8ac-f6877456ea2a | -8.799 | -62.4905 | 2026-08-31 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 1799e329-43e3-3369-9df5-5b2d0d6bd42a | -7.7034 | -63.3249 | 2026-08-31 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 4ae5d931-663f-3154-9d53-14a41205e3f5 | -11.2294 | -45.099 | 2026-08-31 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| c995b88a-d95a-3018-8bc2-ca98aa815834 | -11.2103 | -45.1017 | 2026-08-31 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| dd8883b2-3af4-3b74-b7ae-d993258c8954 | -6.6036 | -58.5972 | 2026-08-31 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 5ddefba3-4334-369b-a184-328a6196f0b1 | -18.2904 | -52.6818 | 2026-08-31 00:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| b8eca155-0cab-3b80-bba3-fab6c5edc21e | -15.4231 | -52.7049 | 2026-08-31 00:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 593d4f46-4954-3d92-9a33-006d5911da74 | -10.7807 | -50.8688 | 2026-08-31 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| e5c11fb5-7066-3b0d-8355-c5801ddb67e7 | -14.1828 | -52.8878 | 2026-08-31 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| f2149c42-65b5-3c55-a05f-0b3b7a88f023 | -5.2363 | -55.8914 | 2026-08-31 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 16272941-7b29-37eb-a5df-b731604652d4 | -5.2546 | -55.9303 | 2026-08-31 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 2b2d02f0-8f17-3c1f-a468-0c5e65d44471 | -1.6042 | -54.415 | 2026-08-31 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| ade409ac-f602-367d-a4bc-d96d5307b06e | -6.9367 | -55.636 | 2026-08-31 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 01d83e1c-c425-3600-9769-cda0a14430e9 | -5.2548 | -55.8907 | 2026-08-31 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 212.6 |
| d2fe1b8f-c4e8-35b3-ba34-4b3608b71669 | -10.7407 | -54.0401 | 2026-08-31 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| c77341c3-b713-321f-aa18-b6c63ece699d | -6.9361 | -55.7157 | 2026-08-31 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 376b45fd-ec28-32b5-9139-a91293b35f93 | -11.0747 | -51.5153 | 2026-08-31 00:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 49eeba35-531e-38c4-8dad-c96c949e4c4f | -18.2908 | -52.6602 | 2026-08-31 00:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 7d738393-3569-3a77-b17b-7b356ac37c84 | -5.2363 | -55.8914 | 2026-08-31 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 171a7bdc-ff24-3d1f-9165-c3b3f63933c5 | -6.8991 | -55.7176 | 2026-08-31 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 64dd6324-72f8-36a9-98db-d2d71d40341c | -15.4231 | -52.7049 | 2026-08-31 00:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b0c5dbe8-6ebe-3f1c-ba08-f834fb56e4f0 | -11.3423 | -45.1982 | 2026-08-31 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 0939f5c9-672a-3fea-88ee-9da4cf19bf2f | -14.6064 | -54.0921 | 2026-08-31 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 2f33789e-bc93-38d6-a523-4e8e6da1ea77 | -5.9451 | -57.6906 | 2026-08-31 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 99f210f1-8b39-3f2d-9e04-b68683c43d51 | -18.2904 | -52.6818 | 2026-08-31 00:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 5f35a645-5abb-3485-a0d8-7deb1dbb706c | -6.6035 | -58.6166 | 2026-08-31 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 13e7d25f-6ab9-3791-a95d-29f8de1aeadc | -6.9548 | -55.6948 | 2026-08-31 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| e7ca6a9f-c524-34c9-8905-2a43b83bde0b | -6.6036 | -58.5972 | 2026-08-31 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 38e5a7d7-db3d-39a9-8408-5f21ee0d2c0b | -8.9481 | -62.3704 | 2026-08-31 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| b82867b1-c6c7-33cf-ad7e-c5b5620192f4 | -4.85 | -55.8266 | 2026-08-31 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |


[Clique aqui para ver as próximas entradas](README8.md)
