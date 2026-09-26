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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73887019-dcc8-3a1a-8246-db51df8471c2 | -1.3008 | -49.0826 | 2026-09-26 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 77a431b9-2872-3392-b06b-50a551cf2c6f | -1.3008 | -49.0613 | 2026-09-26 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 73fa8fd8-64b1-3b62-97ba-4d657ebbe56a | -11.9392 | -50.7629 | 2026-09-26 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 512ade23-fa70-3f1d-9f77-195a62a2e4e7 | 1.6199 | -56.002 | 2026-09-26 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| ab6a6de0-ca9e-3141-8575-69348f26bd8f | -11.9011 | -50.7673 | 2026-09-26 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 0cd325bd-1a2c-3cb0-aeeb-7306f6253571 | -12.3286 | -50.2234 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 5cd85e3b-5a02-3eea-9bd4-8f531d96e06d | -11.9396 | -50.7415 | 2026-09-26 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 159.5 |
| d3d3d45b-c026-36bd-99b0-6f647366578b | -12.0789 | -50.3396 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.7 |
| bf74dc9a-f3b1-347d-9e74-5a3b514196bd | -11.6916 | -50.7913 | 2026-09-26 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 1a94a46a-11c5-3ede-9df2-516d93aa4b49 | -11.7487 | -50.7848 | 2026-09-26 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 8195c656-3480-3ddc-a009-6c9fbcf1abd5 | -11.6954 | -50.5345 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 143.5 |
| be0a4c68-6459-318a-9326-fbcd9630fca6 | -12.8059 | -54.0255 | 2026-09-26 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| fd1fb152-614d-323a-8c71-c5b11ef875b8 | -11.8472 | -50.5598 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 73288a6f-5256-3020-aef1-b7b035ee4d2a | -11.7843 | -50.9512 | 2026-09-26 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 33813576-ae0b-3260-a328-32b31cb0541a | -10.6928 | -60.7322 | 2026-09-26 16:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 58a2208c-dec6-37d4-8a3a-8e315361a801 | -12.2241 | -50.815 | 2026-09-26 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 4d16b116-c296-35d4-a7ba-a25d444a9df3 | -12.1293 | -50.7835 | 2026-09-26 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 153.9 |
| a5473e38-4dd0-37a3-b2fc-7573c7a98d09 | -11.9402 | -50.6987 | 2026-09-26 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 4c40cf61-e8f4-3091-b14b-cf07c5ce0bba | 1.1316 | -51.185 | 2026-09-26 16:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 88.0 |
| de93675a-2753-3f87-b63e-ff9b293643f7 | -12.0609 | -50.2773 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 1b1495c5-53f7-3621-8a57-c36a01c803f8 | -11.7297 | -50.7869 | 2026-09-26 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 132.6 |
| f36013b8-fb71-37a9-bb3e-b17156798f0f | -11.6508 | -50.9875 | 2026-09-26 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 55f36cf4-a1c7-3755-92a0-c5c3ea8e771c | -12.2807 | -50.8511 | 2026-09-26 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| a867c7d3-467f-367f-becc-0ed05f8421bb | -12.0793 | -50.3181 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 9c6ec6ff-8195-3d3c-bdcf-44a9ad39f0ea | -12.0418 | -50.2796 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 354018bc-3b6d-36a3-b6a4-5957b67d915a | -12.7958 | -50.8742 | 2026-09-26 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 1b18093d-b4b3-3f17-ab57-877677440aa0 | -12.0414 | -50.3011 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 172.7 |
| d28f5418-28f6-3d3b-b129-a0698cb64c31 | 2.4396 | -50.976 | 2026-09-26 16:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 85.6 |
| b23671ee-7b7b-3db9-9e71-7fa3dd89facb | -12.1099 | -50.8071 | 2026-09-26 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 9cb65221-3945-3338-b3aa-e6298b674bcf | -12.0599 | -50.3419 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 164.7 |
| ca6c2f12-6d49-3b86-8485-ae0b8847cf7f | -12.3099 | -50.2041 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| aa765fdc-ed88-3353-8395-c8be868edf8a | -12.022 | -50.3249 | 2026-09-26 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| ebdc80c4-c2fb-36a7-a790-6e2c1fad8ef0 | -10.7114 | -60.7505 | 2026-09-26 16:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1bbac479-f349-325f-94c9-2c0c4664c6a6 | -8.36 | -44.2 | 2026-09-26 16:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e9bdbd9d-49e3-3429-a87c-76b587b04ec3 | -11.88 | -50.53 | 2026-09-26 16:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0954116e-d5cd-3770-af66-2975de97691e | -8.36 | -44.11 | 2026-09-26 16:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8ffefac9-60f0-3b34-af08-085c92e2863c | -8.33 | -44.11 | 2026-09-26 16:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8420b6a3-9452-3afd-943f-22d39a4b43c7 | -8.33 | -44.15 | 2026-09-26 16:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 24b79222-9442-3c74-99c6-7ce59ffc985c | -8.36 | -44.16 | 2026-09-26 16:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 40a8b79a-7afb-370f-a63c-c5895ce4d923 | -12.1106 | -50.7643 | 2026-09-26 16:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 80b91db6-2674-3313-9827-95e4b0d74b82 | -11.6954 | -50.5345 | 2026-09-26 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.7 |
| dd6ea996-774d-3c0a-9cd7-4dcb86730b75 | -1.3008 | -49.0826 | 2026-09-26 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| d7b6df1f-198d-3545-9745-ae3a2f8b7eef | -12.2827 | -50.7226 | 2026-09-26 16:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 143.1 |
| f084310d-f11a-3804-b33a-a528ad29eecf | 1.1316 | -51.185 | 2026-09-26 16:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 4a4cd080-5e59-38c4-91dc-e0b8e35b2d51 | -12.2636 | -50.7248 | 2026-09-26 16:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 6bc4574b-b2b1-33be-a79a-0462faba314b | -11.9011 | -50.7673 | 2026-09-26 16:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 87a41ab0-480a-390e-9eac-95a0994c2e25 | -12.0414 | -50.3011 | 2026-09-26 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 3c9fb754-24d5-38fe-86ed-c81762de1098 | -1.3932 | -48.9961 | 2026-09-26 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 11adddef-8eb7-3d35-82ff-bd2d9a382896 | -12.7958 | -50.8742 | 2026-09-26 16:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| bc161505-e956-3cb8-96fe-604edebdaebe | -12.7767 | -50.8766 | 2026-09-26 16:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| b6db7b04-a4a4-395f-9cf4-00f5c92f7d49 | -12.0605 | -50.2989 | 2026-09-26 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 2becf45c-16bf-3bef-b86b-464b3de7d298 | -12.2254 | -50.7294 | 2026-09-26 16:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 124.0 |
| bbd93bd7-fc75-3a61-bdf0-8c4ec9a827ae | -12.0408 | -50.3442 | 2026-09-26 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 778b0ecb-365d-33be-89c6-51a89c4866a0 | -11.9583 | -50.7607 | 2026-09-26 16:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 47846ccf-cbf2-314f-a739-7bf01f9fbc86 | -1.2085 | -49.0838 | 2026-09-26 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 9405b286-1419-3922-9364-b17805a73551 | -1.1715 | -49.1268 | 2026-09-26 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 62569e3f-33f9-37ca-8208-132b53829932 | -10.7115 | -60.7312 | 2026-09-26 16:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| ceb078b4-2451-3b6d-8b33-143a199db0b6 | -1.3932 | -49.0387 | 2026-09-26 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| e2878530-a2c5-3e56-90a6-88ec14179a9f | -1.4116 | -49.0384 | 2026-09-26 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 51e4831f-3350-3451-a20e-2be566c98e7f | -12.0599 | -50.3419 | 2026-09-26 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 158.4 |
| d9172863-568a-3725-a4c3-b13883702bd6 | -1.19 | -49.1266 | 2026-09-26 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| aa4157de-e1ca-3552-8eb5-0b7a2fd9ec85 | -12.8059 | -54.0255 | 2026-09-26 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 4a7e94e5-3a3e-3ea5-9b61-1f77abc1b53a | -1.3008 | -49.0613 | 2026-09-26 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 146cd3de-5b83-380f-b55d-1aa9aad87054 | -12.0803 | -50.2535 | 2026-09-26 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 88b8cbcd-9374-3d73-8f9d-9c620e890998 | -11.7094 | -50.8745 | 2026-09-26 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| b277a4b3-2ab4-323d-8183-19f47be49ee7 | -12.2445 | -50.7271 | 2026-09-26 16:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 5ebc72f3-cb0c-3739-a9d3-38cd0627434f | -1.2086 | -49.0625 | 2026-09-26 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 195f2393-c019-3097-98e7-da34937c49d5 | -12.1952 | -52.7821 | 2026-09-26 16:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| f643b8ec-6a2f-3317-8a96-1d5ab9d4cc24 | 1.1316 | -51.185 | 2026-09-26 16:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 104.4 |
| e473f77e-870e-3dae-bc5e-03990030906b | -12.2636 | -50.7248 | 2026-09-26 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 140.1 |
| efa04d7f-0600-342b-9a2b-bad92ccdb3b7 | -12.022 | -50.3249 | 2026-09-26 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 27c3fe53-538f-387f-8c14-bfd28bf3f2ae | -12.8059 | -54.0255 | 2026-09-26 16:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| c07fc44c-ddf0-3ed7-b37a-01e5f3eaa07b | -1.2086 | -49.0625 | 2026-09-26 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| aae9798d-1f04-3c5a-b2a9-e11aa41ce1cb | -1.3932 | -49.0387 | 2026-09-26 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 2d8ac5a2-3261-3277-98fe-c3c6deab1b38 | -12.7958 | -50.8742 | 2026-09-26 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| f7ca1c25-113d-3f0c-9c32-1f769b29ccc6 | -12.2445 | -50.7271 | 2026-09-26 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 81366682-28f5-3269-b84c-ef0cacf67219 | 1.5835 | -55.8448 | 2026-09-26 16:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 5a896556-4eef-33d9-91c2-f0cd658c09ce | -11.8559 | -49.979 | 2026-09-26 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| d3bc811b-4e7b-34fe-89f8-6c93c7f1b8db | -1.4116 | -49.0384 | 2026-09-26 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 82fc3265-66d1-3aa7-85b1-79b2da331566 | -1.3008 | -49.0613 | 2026-09-26 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 4c57b2e9-8c30-3d38-85e0-326a84c1add9 | -12.7767 | -50.8766 | 2026-09-26 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 5ba8b801-eed4-3502-9eb4-b64781ce66d6 | -12.2254 | -50.7294 | 2026-09-26 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| f4d698d3-56d7-3cfd-800b-a0f1feec9718 | 1.6018 | -55.8643 | 2026-09-26 16:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 8b9148df-ddf4-37e8-85a7-afaf0aa35395 | -1.2085 | -49.0838 | 2026-09-26 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 0162b81f-0ac5-3d07-a945-8f606e977c84 | 1.5649 | -56.042 | 2026-09-26 16:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 5ce81cf9-9760-3dce-a75f-f86d9a0cbedf | -1.3008 | -49.0826 | 2026-09-26 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| ee6da18d-30d3-3be8-886c-1131e9a8b11b | 2.145 | -50.8784 | 2026-09-26 16:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 1ebcb91b-6b20-31d6-9b55-2e0cf6119824 | -1.19 | -49.1266 | 2026-09-26 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| ffefcf96-c666-3c09-ba4e-39dce91c7870 | -1.3932 | -49.0387 | 2026-09-26 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| d19f8de0-dc78-38da-9ea6-c5dc46e2ab72 | -12.2254 | -50.7294 | 2026-09-26 16:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| d195225a-b8b3-338c-8e65-2a483b927d46 | -12.2445 | -50.7271 | 2026-09-26 16:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 2a740d5c-420f-3863-8db6-7e4319ee3617 | -1.3008 | -49.0826 | 2026-09-26 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 83e3b8fc-bc40-3471-92db-d51d297489c5 | -1.3932 | -48.9961 | 2026-09-26 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| b64c17f3-e650-33c6-8042-b06614ac6cd0 | -12.2827 | -50.7226 | 2026-09-26 16:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 910efa91-91d1-3e45-852e-d7d10524d356 | -12.2636 | -50.7248 | 2026-09-26 16:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 147.0 |
| a12c6f01-4318-3367-93d0-f59981e5135b | -12.7958 | -50.8742 | 2026-09-26 16:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 44912d82-298f-3f62-83a9-d989bf11855d | 2.145 | -50.8784 | 2026-09-26 16:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 18b9223d-2ce7-3945-bb05-29c3e5e7012e | -1.3008 | -49.0613 | 2026-09-26 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 5b39f600-e700-3131-afc7-794e5b9a4fba | -11.8665 | -50.5362 | 2026-09-26 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 192.0 |
| 3d6cbad4-058c-3e63-966b-f0fa8feb40d4 | -1.3932 | -48.9961 | 2026-09-26 16:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |


[Clique aqui para ver as próximas entradas](README41.md)
