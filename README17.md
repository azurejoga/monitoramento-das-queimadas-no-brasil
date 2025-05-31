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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dde8d0fe-66f7-3ad6-b2ff-90dd33b9a2e5 | -8.47697 | -49.60616 | 2025-05-31 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6d66d22e-2019-31dc-9bb5-b5c02921df33 | -12.02223 | -49.51975 | 2025-05-31 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c2ec0a9e-b719-3552-b664-0966d3c3cd67 | -9.93265 | -59.9357 | 2025-05-31 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40086d3b-d37a-354f-b9d4-6e38ede0f1bb | -12.37584 | -54.16036 | 2025-05-31 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1ccceaa-4be8-3b43-a235-937c4874188e | -12.02117 | -49.52852 | 2025-05-31 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9216e6d5-96e4-3489-bd1a-2c49695f07c5 | -8.20406 | -49.80128 | 2025-05-31 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a007c3e3-afda-3c77-a1dc-51d2dd82f73d | -11.82533 | -51.27343 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2be2a783-e478-3533-a9fe-9d9d36c7db53 | -11.90815 | -54.8219 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f9b54c2-4d5c-367e-8c99-9cb215f6ccea | -11.90965 | -54.81843 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abf337c7-18c3-3215-963c-6b695768e0e0 | -11.91014 | -54.41928 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed6ecc0d-1e02-38cd-bb47-3483cc9a1d3a | -11.83652 | -51.27223 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9e003288-5941-30d7-9e1e-80db3a9d138b | -12.60928 | -56.01975 | 2025-05-31 05:16:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc6ca61d-dde4-3076-976e-32a24bb2e0c4 | -10.65181 | -49.434 | 2025-05-31 05:16:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e893741f-d680-3b1a-9802-4bc61a2b6f7b | -13.10461 | -52.28814 | 2025-05-31 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01524eb7-0302-3efd-bd95-9a5a52264a5d | -11.14255 | -53.92799 | 2025-05-31 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbb551da-7bfe-39aa-b126-b946d7544a05 | -12.10385 | -54.67053 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4592380-7db3-3d0f-8195-a0a0344adea5 | -11.13206 | -54.2195 | 2025-05-31 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e5f95a2-18b5-31b2-a019-99c2b153693f | -10.56291 | -59.20749 | 2025-05-31 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d813f55-511b-381d-89f9-7f2e5c07c1f4 | -6.63437 | -55.00873 | 2025-05-31 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ff795ff-c8f3-3e19-9077-29c552abf8bd | -12.01583 | -49.52341 | 2025-05-31 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 46c84695-d341-3619-ad34-e5c4a2276762 | -7.58609 | -45.8705 | 2025-05-31 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 382eee0d-96eb-3557-98b2-6ceec10b86f7 | -10.735 | -49.28685 | 2025-05-31 05:16:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8b4da54a-046a-3230-8989-09ee59d44c7a | -8.81136 | -49.83661 | 2025-05-31 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 180fc35f-3ac1-3aa7-afb3-eab05a602d97 | -13.09966 | -52.28745 | 2025-05-31 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39d60fb1-3948-340b-8e73-d816651fd750 | -11.7907 | -54.77917 | 2025-05-31 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36991aff-a9a6-37c2-808c-3d90d60c05eb | -11.82615 | -51.26702 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d9dddf0c-1031-3c8d-a62b-65c569769e09 | -12.37094 | -54.16401 | 2025-05-31 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceff302c-870c-3f7d-87d5-89a55e25bad5 | -7.55746 | -63.26823 | 2025-05-31 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e13c4a68-6eb2-3397-bdc0-e6205d557fc4 | -11.8321 | -51.26497 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 57f27412-7685-381c-afa8-08afdfd320b4 | -10.46464 | -47.94453 | 2025-05-31 05:16:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c0379945-91c3-361a-9cb7-9a3abb53f73c | -11.83131 | -51.27143 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a1cf9299-240e-3fa4-b98a-aabce78f144e | -12.08682 | -54.57749 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b45f53fc-ad86-3327-bdab-0343ba833f1e | -11.84175 | -51.2729 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3944ac70-cbf5-326f-aee1-39fd49d4db26 | -12.12285 | -54.59463 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70b9e62e-9b49-34b5-9010-98267d26f0fc | -11.89505 | -47.44949 | 2025-05-31 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3762ed1-e269-365a-b983-f239364875ad | -10.30284 | -57.14198 | 2025-05-31 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea63eabe-926a-3433-ac4b-a5b1e980ba34 | -11.9086 | -54.82583 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10b46d8e-f7e0-3280-84f9-a058b7dafe2c | -11.3642 | -55.12865 | 2025-05-31 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc1efa5c-c7d1-35c4-9c90-a7b9466f1055 | -10.82702 | -56.94629 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9bc76e12-0452-3944-b461-db1b7d6608f6 | -10.64023 | -49.43226 | 2025-05-31 05:16:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c5317f6e-9b8a-38ce-a79b-2ea0b7c8c6a8 | -9.39946 | -48.42606 | 2025-05-31 05:16:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00117e59-58ca-37f7-aa6e-9cf9d31457ae | -11.81685 | -58.86642 | 2025-05-31 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f0fedd1-51e9-3256-98de-2ba340c378e1 | -7.57997 | -45.86314 | 2025-05-31 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9fdbda11-8a38-31f1-a9bf-b9e4b45f54a4 | -14.07342 | -47.653 | 2025-05-31 05:16:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66e0be9f-3244-3c47-874f-7efb53061064 | -11.83053 | -51.27421 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6541d717-db08-34f6-a116-a82f1a356215 | -13.10059 | -52.28939 | 2025-05-31 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfbc6f13-9661-3b5f-9237-374e3c1dbcc1 | -11.45144 | -49.09925 | 2025-05-31 05:16:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec3d34be-7676-3131-9412-69e73d49da49 | -11.70166 | -54.55428 | 2025-05-31 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4514113d-a5b9-32da-9466-9ba3899e5a71 | -10.4599 | -47.952 | 2025-05-31 05:16:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c279b7be-bcc0-3333-90c4-b9b34ce26aea | -9.56254 | -55.00634 | 2025-05-31 05:16:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3da1c4f4-13d5-35f3-b8d8-b02c4f4fe0e0 | -10.38225 | -57.64502 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33950c2b-a895-38bd-ac30-7217b3ba71a3 | -9.52985 | -54.76479 | 2025-05-31 05:16:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 426df3cd-c36d-3e55-b6cc-cc5deef4be17 | -10.82997 | -56.951 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 45d6c776-bbe4-3012-8980-9469befb0ea7 | -10.82406 | -56.94162 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 84c2218f-b3cd-37f0-bd00-29846b6cdc93 | -11.83053 | -51.27786 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e8d77c29-5774-3060-aa65-6ebc225274e8 | -7.90061 | -61.52082 | 2025-05-31 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 583d86e5-b410-3f00-a369-60d4a2b959ea | -12.12232 | -54.5985 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c96e5f2-d324-342d-95e2-fe7a053792a2 | -10.45764 | -47.94885 | 2025-05-31 05:16:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b416d156-dcbe-3cfb-b7fb-737921968b88 | -13.63818 | -52.18053 | 2025-05-31 05:16:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bc05699-a9ba-3145-9564-32800ac99a35 | -11.33959 | -56.20164 | 2025-05-31 05:16:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e18067e-6456-3d23-837e-a84ac1ace53d | -12.02811 | -49.52045 | 2025-05-31 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eaba9570-2e62-3e12-bfb9-486d7bd2e091 | -11.91225 | -54.8225 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66614a46-19c6-3f73-9ddf-c53760bbc0f7 | -10.83792 | -54.01474 | 2025-05-31 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44e76574-ef9f-374c-ad5e-cf46eaa91a5f | -12.1049 | -54.66288 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f946745f-e1c6-378f-9bd7-914683c14036 | -11.64254 | -55.36761 | 2025-05-31 05:16:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdcc56c5-2baf-36aa-b68b-ea7adf861fdd | -9.51653 | -54.74436 | 2025-05-31 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ad5f749-db6e-34d8-94b9-c32c8f20b3ed | -9.68281 | -66.07111 | 2025-05-31 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a547cf9b-0dd7-362b-accd-aeda612b07c3 | -12.19468 | -54.26354 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe2b0316-fccf-36c6-95af-7b4509ec132c | -11.91859 | -54.42043 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0df2201-18fd-362c-b30f-bcc8901da70f | -11.83137 | -51.26778 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5bfd7337-56f1-3243-9fcd-998513e0d5ef | -10.64549 | -49.43737 | 2025-05-31 05:16:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d6b9f417-c38c-30d0-9eec-979e73265687 | -11.91914 | -54.41644 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8953c062-7bf3-3e56-a32d-cd8928df0621 | -11.91276 | -54.81878 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8610e8d-b161-3ae6-b697-ca8b5102d15f | -11.03821 | -53.999 | 2025-05-31 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9d3a749-ff4c-375a-9c28-4134d29ebf48 | -12.01477 | -49.53212 | 2025-05-31 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 50abf278-4977-33af-b06f-30f3adb870fd | -12.10021 | -54.66611 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2f09cab-ef4b-34c6-8c39-f2c311014aaf | -10.65129 | -49.43817 | 2025-05-31 05:16:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 884293ca-57fb-3110-995d-311b6e505bba | -12.02758 | -49.52483 | 2025-05-31 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eb52e60c-4262-3268-af90-91ed43ade35e | -12.19722 | -54.26722 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07bbb2b8-ef1d-3b52-b8ad-6bc9d23a1422 | -11.83613 | -51.27545 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f30b8b48-5e73-39f5-9207-4e824fa39691 | -11.14458 | -53.94501 | 2025-05-31 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11d67249-a97c-39c7-b1d2-f65efc210f4d | -11.90913 | -54.82214 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad0c8cbc-b745-376c-bb7d-9866aa61f709 | -12.10437 | -54.66671 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09ef64d5-fae3-3c7e-b90a-586ea6dd8a4d | -9.96516 | -49.81061 | 2025-05-31 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e9dab59-f6d0-3c1c-b71d-b2caea1cb3a3 | -10.73552 | -49.28262 | 2025-05-31 05:16:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8b275658-f719-350c-9f2c-84ba06e0aaa6 | -11.83095 | -51.27101 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 39048a1d-6724-3a6b-8b34-f0ba52137c46 | -10.46053 | -47.94673 | 2025-05-31 05:16:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 4c98e74c-ab34-3542-a7a1-93f79cced00b | -11.83092 | -51.27465 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c123ade8-8d44-32e7-bd2a-76f7addf7f2d | -12.19776 | -54.26314 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bceb447c-50ba-3933-b65d-ce4428eeeffd | -10.4583 | -47.94361 | 2025-05-31 05:16:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3556c849-45c8-3ae0-88b5-13647c7a9de5 | -11.90765 | -54.82559 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb30f237-72ea-3930-81b2-dd64474076c1 | -9.52907 | -54.77007 | 2025-05-31 05:16:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37fb14ad-ddca-3fb3-b545-eaca9207d600 | -11.83732 | -51.26572 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7a343f80-3484-3dcf-96dd-9974759ed506 | -10.55958 | -59.20696 | 2025-05-31 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2282adee-ccde-3a54-8bf0-4e9900dafcd3 | -12.45889 | -54.91668 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 979f1a10-23aa-362c-9894-43f2a07359d1 | -10.83633 | -54.01741 | 2025-05-31 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| afe05d13-512d-386f-93ef-b0247c22eb3f | -7.16531 | -55.44876 | 2025-05-31 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab398a73-8e17-3683-8ad0-77a89c462ac2 | -12.01635 | -49.51906 | 2025-05-31 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d159f16c-45a6-305f-8de3-e90e0f363d5e | -9.31609 | -49.48769 | 2025-05-31 05:16:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 781b2f04-9859-34c3-90a1-eb77037f6be7 | -11.44932 | -49.09674 | 2025-05-31 05:16:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README18.md)
