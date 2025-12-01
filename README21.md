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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12a966ec-1039-3a48-a23e-29739a0217d8 | -20.04662 | -57.44311 | 2025-12-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.2 |
| 493ce50e-871c-366f-8e6e-fd82cd368a95 | -19.98032 | -57.39194 | 2025-12-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.1 |
| 3b6f8fea-0c70-3e18-8fb0-a3a3daf49c44 | -19.59939 | -54.24371 | 2025-12-01 12:40:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 1d861554-6909-35f0-9175-c4f44346b0d4 | -16.75771 | -48.91692 | 2025-12-01 12:40:00 | TERRA_M-T | CALDAZINHA | GOIÁS | Brasil | 5204557 | 52 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 1b79ba55-b15a-316b-b639-0b6d83346193 | -17.51525 | -57.20081 | 2025-12-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 406008d3-6de5-3b14-9680-2cb1026f0374 | -17.53656 | -57.18397 | 2025-12-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.8 |
| caa2dd53-79a6-3bb4-ac79-1584b52168cc | -17.50763 | -57.18943 | 2025-12-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.6 |
| 5622a43a-dd12-32b0-a919-9c2cae99877d | -27.80526 | -51.12952 | 2025-12-01 12:42:00 | TERRA_M-T | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 0039130c-bcfb-3d17-84ec-c0069282ee6c | -27.80707 | -51.13643 | 2025-12-01 12:42:00 | TERRA_M-T | PINHAL DA SERRA | RIO GRANDE DO SUL | Brasil | 4314464 | 43 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| cf670bcb-6cb4-32d9-894c-d3b7f961c56a | -19.975 | -57.3912 | 2025-12-01 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 189.8 |
| 5059dcdd-0381-3339-8266-abb62724153e | -20.0343 | -57.4457 | 2025-12-01 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.7 |
| f3025edc-6356-3b1e-98a6-ba34d0a06e3d | -19.9548 | -57.394 | 2025-12-01 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 175.6 |
| e4b39857-0380-3ac4-9994-70e0693daa57 | -20.0343 | -57.4457 | 2025-12-01 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.8 |
| ddd139af-d52d-3f2f-ad02-b105a160edcd | -19.975 | -57.3912 | 2025-12-01 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 148.2 |
| 8e3682d8-0076-3e72-b8c2-863d4d3fd803 | -19.9548 | -57.394 | 2025-12-01 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.6 |
| 77797067-ddbd-3d6a-bee1-b103a53133d6 | -20.4076 | -57.9577 | 2025-12-01 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.0 |
| a6b54e70-318f-3bd7-a8dd-fb795b8c5979 | -19.9343 | -57.4177 | 2025-12-01 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.0 |
| aedc4390-00c6-367b-868e-213aae3dcbe8 | -19.9347 | -57.3968 | 2025-12-01 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.6 |
| 78a68c2c-b629-391e-b93e-4ebb50740dfa | -19.9343 | -57.4177 | 2025-12-01 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.1 |
| f9b83f18-fccb-385d-bb29-6cb7a0de9139 | -19.9347 | -57.3968 | 2025-12-01 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.8 |
| 59bc623a-cac1-3406-bd6c-e20399cc116f | -19.9548 | -57.394 | 2025-12-01 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 170.8 |
| 37a2a53a-0b7e-380f-9152-b82e42e6223c | -19.9746 | -57.4121 | 2025-12-01 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.3 |
| 0b9199a5-3ae8-3626-b281-a253a0247b9f | -19.975 | -57.3912 | 2025-12-01 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.7 |
| 7bf42538-c90f-339b-970e-afddcef1ae57 | -20.0343 | -57.4457 | 2025-12-01 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.0 |
| 633c6237-e24d-39f6-970a-7c838965ed63 | -20.4076 | -57.9577 | 2025-12-01 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.7 |
| f6de8c46-3696-33a3-9bde-adc81eaac077 | -20.0343 | -57.4457 | 2025-12-01 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 190.4 |
| 08f3d3b6-6e6a-3e9a-ace3-dad5c4240b05 | -20.3874 | -57.9605 | 2025-12-01 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.8 |
| d712cdce-648d-32ee-8224-125f0cc4df9e | -20.0339 | -57.4666 | 2025-12-01 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.3 |
| 82b9d695-9d38-3369-93f7-8a84c120f11c | -19.9548 | -57.394 | 2025-12-01 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 153.3 |
| 22b81adc-446f-3e8b-8e6f-2c1d82e36480 | -19.9746 | -57.4121 | 2025-12-01 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.7 |
| 32dd51b8-7f2b-3086-ac45-fe68111323cb | -19.975 | -57.3912 | 2025-12-01 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.5 |
| 056c0a64-891f-387b-9440-4aa77630f8ca | -19.0522 | -57.5148 | 2025-12-01 13:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 95.0 |
| d7b5145b-57c2-3e73-aaa9-74b9fc6c0bc2 | -20.4076 | -57.9577 | 2025-12-01 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.0 |
| fa410ab6-d89c-31c7-ba88-ff5f27b51ed5 | -20.408 | -57.9368 | 2025-12-01 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.1 |
| 07a036a7-b63d-3a24-89e2-ce65b36d30f2 | -20.3874 | -57.9605 | 2025-12-01 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.9 |
| 9b19b581-4f91-3e82-984e-f5007f1648f1 | -19.0522 | -57.5148 | 2025-12-01 13:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 99.9 |
| 891b4eb3-ee3b-3424-85b9-736816417609 | -20.408 | -57.9368 | 2025-12-01 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.8 |
| 2e6f37a1-a4b9-3686-b77e-f0b3195279b2 | -20.0343 | -57.4457 | 2025-12-01 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.8 |
| 51a049ea-79ac-355d-a7ee-02f24abd3d3d | -20.4076 | -57.9577 | 2025-12-01 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.2 |
| 240b2fd8-1bb6-344f-8da2-7f2358cc58a5 | -20.4283 | -57.9341 | 2025-12-01 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.5 |
| 6e873428-cc60-33ee-9098-9b5b2f3d5b53 | -20.0545 | -57.4429 | 2025-12-01 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.3 |
| b7877226-a767-37db-9512-022d56ad3f96 | -20.408 | -57.9368 | 2025-12-01 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.1 |
| a7b04646-622e-32ec-940e-ac3a97ce9cdd | -20.0343 | -57.4457 | 2025-12-01 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 219.9 |
| 8b4d16ca-4422-37e5-b586-86cba7978bfd | -20.4076 | -57.9577 | 2025-12-01 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.1 |
| 66c01d66-01e4-3a5c-9fd3-3f996c72949e | -20.3874 | -57.9605 | 2025-12-01 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.1 |
| 89158897-7660-3cc6-9018-c88f7ae9a783 | -20.0339 | -57.4666 | 2025-12-01 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 158.4 |
| 96acd3d4-1b03-3a1c-8cf4-e5d2b8a1bff8 | -19.0522 | -57.5148 | 2025-12-01 13:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 104.9 |
| b785128e-fbb3-3570-8920-5ac79326de32 | -20.0343 | -57.4457 | 2025-12-01 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 180.0 |
| 2a1251d3-3a9b-3d9f-9210-d3bee17c7486 | -20.0545 | -57.4429 | 2025-12-01 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.9 |
| b1aba12e-75df-3a70-aba3-11b6f92ad781 | -19.0522 | -57.5148 | 2025-12-01 13:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 104.8 |
| bf885daa-a9f7-3a14-a321-c9f52976a369 | -19.0522 | -57.5148 | 2025-12-01 14:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 110.8 |
| 7a388de3-0385-3797-9509-c838659552b5 | -20.0343 | -57.4457 | 2025-12-01 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 174.6 |
| 2a91ee60-b873-3d05-ae20-c21273de9b90 | -20.0545 | -57.4429 | 2025-12-01 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.2 |
| 0900b052-11a1-3d0a-84bd-cf5f5f8701e2 | -20.0347 | -57.4247 | 2025-12-01 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.3 |
| edde72eb-83d4-3b74-b5d5-f2fc61f09a7e | -20.0343 | -57.4457 | 2025-12-01 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 199.6 |
| 67dba652-d73f-3c9d-980a-097697102d12 | -20.0545 | -57.4429 | 2025-12-01 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.3 |
| b3cd0b52-eca0-32fb-be0b-612bb02896b8 | -20.0339 | -57.4666 | 2025-12-01 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.1 |
| 75caa02e-dfd6-3624-a9f8-a601037e9399 | -19.0522 | -57.5148 | 2025-12-01 14:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 114.3 |


