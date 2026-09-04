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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f88b6a6-f0bf-3573-8ba5-04ac5b656e37 | -6.6697 | -59.9635 | 2026-09-04 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 195.4 |
| bb48d6f7-26d6-32db-b0ae-0c06ccde37f4 | -10.6169 | -50.3963 | 2026-09-04 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| a50642a8-2f69-3014-b900-2337161180f6 | -6.6698 | -59.9443 | 2026-09-04 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 5d96e0bd-943b-3bc8-a774-3a49796a852e | -6.1361 | -59.9063 | 2026-09-04 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| f40af766-f091-3f30-bf72-21eef117f984 | -14.5631 | -52.0557 | 2026-09-04 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 0a2c4ede-61f0-386a-8981-23a239b7e9bf | -11.2106 | -51.2688 | 2026-09-04 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 33172a1e-7226-36f0-8ffc-f55e920b55a2 | -15.2275 | -56.3716 | 2026-09-04 15:10:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 69d473b3-4471-3551-aa1a-8f977ead5e43 | -8.9428 | -63.2797 | 2026-09-04 15:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 37e2ce90-c0e3-3256-b61a-6586637d6d34 | -15.2672 | -53.8642 | 2026-09-04 15:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 52be5dbc-a545-3a49-81f8-57f9ed9c4798 | -17.0881 | -56.8328 | 2026-09-04 15:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.5 |
| b56f10e5-a856-310a-9377-8826f3bde1de | -17.0878 | -56.8534 | 2026-09-04 15:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.6 |
| e08be070-664a-395d-9c9d-d42da58fe576 | -6.6696 | -59.9827 | 2026-09-04 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 168.5 |
| 7887c132-1f45-3468-997e-887619ccc255 | -11.8252 | -46.022 | 2026-09-04 15:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 970f32b5-9dd8-37ff-8748-1524345d0861 | -4.6669 | -55.635 | 2026-09-04 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 174.9 |
| ab923c41-1df1-3b7d-a4f1-31df55818a75 | -17.1074 | -56.851 | 2026-09-04 15:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.7 |
| 896a9050-325b-338c-a1aa-cbabfc32411e | -3.3 | -57.8875 | 2026-09-04 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 23d2c2e9-d09b-3d2a-acdc-ba61612ae481 | -3.7645 | -61.7548 | 2026-09-04 15:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 104.5 |
| e3283c9f-ba7a-3f3c-ad43-a74103e6f51c | -3.3504 | -59.4465 | 2026-09-04 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| a7387184-ee8d-38e6-8bfa-d34b29e5ec50 | -17.1427 | -55.9169 | 2026-09-04 15:10:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 35135c79-4fd6-3264-be6b-67abaef299a0 | -11.2317 | -53.9958 | 2026-09-04 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| a15b82ec-5462-38ea-8b26-32f9d17be5a0 | -4.4087 | -55.7823 | 2026-09-04 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 1b0b657a-5134-38a0-9e3c-07f8acc37299 | -8.8645 | -68.4849 | 2026-09-04 15:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 2d78e076-c0a1-3020-b9a5-b46bae318d06 | -11.2314 | -54.0164 | 2026-09-04 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 0dba6375-93eb-3b42-bca1-16f8c8ae7e59 | -14.1363 | -58.8577 | 2026-09-04 15:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 3ade9963-f908-3166-be6e-20bd07717b6b | -13.967 | -54.395 | 2026-09-04 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| fa5a9219-e227-39d7-acd0-8d2fab0cc668 | -4.6297 | -55.7353 | 2026-09-04 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 6364edb2-7687-3d94-8933-ddda9325fee5 | -6.688 | -60.0012 | 2026-09-04 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| b1b7c786-4f5e-33e3-8758-681eeb96a3cb | -14.1366 | -58.8378 | 2026-09-04 15:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 1b8be5bb-5584-3400-b2b3-8f87e8ce2559 | -6.6015 | -58.9651 | 2026-09-04 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 50d2021b-60c3-36f2-91dc-e043542c6bc5 | -3.6216 | -60.547 | 2026-09-04 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 973173af-5a21-3cab-8eb5-e993f0814f3d | -6.6883 | -59.9436 | 2026-09-04 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 5fb538ec-98db-39f0-9213-d8c098fe1ba9 | -14.5634 | -52.0344 | 2026-09-04 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 41f3900a-3052-3cb3-95ae-cbc02a27f45e | -13.9477 | -54.3971 | 2026-09-04 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 998a7f1f-3273-3921-be9c-26166c3a4a28 | -19.1 | -57.33 | 2026-09-04 15:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dd445628-bfe5-3149-ba5c-c71a2040ba02 | -17.1074 | -56.851 | 2026-09-04 15:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.3 |
| 8d2e3e32-652c-3792-98ef-b614abaf01a7 | -6.6015 | -58.9651 | 2026-09-04 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| bdf1605d-e32f-31e2-a8b8-8a2147a29628 | -17.123 | -55.9194 | 2026-09-04 15:20:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 21706b65-a806-3608-baf7-ff7f712a65da | -6.1175 | -59.9452 | 2026-09-04 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 5e050356-66be-37c2-9ed5-219d993ae601 | -11.2317 | -53.9958 | 2026-09-04 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 35735ddd-dd41-384a-b5d3-1ecc0387b1f2 | -6.0807 | -59.9465 | 2026-09-04 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 27cc523d-b143-3758-87c8-7ad097c1f907 | -6.6697 | -59.9635 | 2026-09-04 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 163.3 |
| b9c2a5b0-d392-3353-a9ef-35c2800315c4 | -6.6696 | -59.9827 | 2026-09-04 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 1839940b-32f7-3a62-a7ce-18b7f56c5233 | -15.2278 | -56.3512 | 2026-09-04 15:20:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| d12f696c-734d-3434-80d5-cb29b5224642 | -11.2314 | -54.0164 | 2026-09-04 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 02c17ec4-1a9f-38ca-8c98-5bf32e5f960e | -6.1361 | -59.9063 | 2026-09-04 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 545e86e0-2810-34df-8c69-f1aae01b6750 | -10.7463 | -50.6172 | 2026-09-04 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 31a3122f-57ae-3177-bb84-b0ce894273fe | -14.098 | -58.8611 | 2026-09-04 15:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| b0d29cf9-4f88-3fae-8a49-c51cb620e793 | -17.0881 | -56.8328 | 2026-09-04 15:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 175.9 |
| 7bbebc88-9f62-3436-9436-ca57d7f3db09 | -15.8336 | -46.0196 | 2026-09-04 15:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 5a70e042-af0b-3a07-85de-c7dcf0f43041 | -17.0878 | -56.8534 | 2026-09-04 15:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.4 |
| af2dd059-9b82-3fbe-a2f9-85f3426fd1ac | -4.6297 | -55.7353 | 2026-09-04 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| d0dc4fef-3a14-3c1d-ab88-18917f793245 | -3.2341 | -50.558 | 2026-09-04 15:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 586fd50e-be8a-326c-baca-19288d2c30c4 | -6.1361 | -59.9063 | 2026-09-04 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| a9f6ce99-b3f4-3b9f-b37f-ba38a69a3844 | -13.4511 | -57.0995 | 2026-09-04 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 202b37da-630e-34c7-bf03-c52f0054e068 | -11.2317 | -53.9958 | 2026-09-04 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 29a3e7b3-5eb3-30ca-a0b6-a28d3ea7d848 | -3.234 | -50.5789 | 2026-09-04 15:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| b9eaec67-a50c-3f49-8eb1-aef54d840b29 | -20.8573 | -57.7072 | 2026-09-04 15:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 107.7 |
| 42584244-e3b1-36cb-af90-a018ab253458 | -11.2314 | -54.0164 | 2026-09-04 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 900c5a87-9b51-3eee-9db5-b6572471c657 | -6.6766 | -58.7299 | 2026-09-04 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| ebc5dab2-57d6-3441-bf78-2644cecfeee6 | -15.2275 | -56.3716 | 2026-09-04 15:30:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| a0623478-4f54-3513-902d-9029f17bd10a | -17.1427 | -55.9169 | 2026-09-04 15:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| c55e015f-62e8-3c7a-9b2c-d46a7e90a0fe | -6.6697 | -59.9635 | 2026-09-04 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 12ca4689-009b-36f5-9ed4-bde0410f6f52 | -12.3798 | -53.1793 | 2026-09-04 15:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 3e08e3a7-9455-3b43-8557-329c1a0c9c70 | -2.9886 | -57.9132 | 2026-09-04 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 1460099a-9cd1-30a3-9d93-a5a82ab76124 | -8.9428 | -63.2797 | 2026-09-04 15:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 15b793ab-f0e9-3ba5-921e-238b51a531e9 | -3.1462 | -60.6317 | 2026-09-04 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 967275f4-551b-3e9a-8f16-98fb617ce2fa | -6.7648 | -59.4408 | 2026-09-04 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| a32f2e5d-b15d-3064-93fb-1a1c03ec1ea2 | -9.5306 | -68.6366 | 2026-09-04 15:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 61c2aeeb-00b7-390f-9934-9e456fc859fd | -13.4575 | -51.411 | 2026-09-04 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 7a7e0df5-f2b9-3bc7-aa6d-870d9457ea26 | -3.7462 | -61.7552 | 2026-09-04 15:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 8829b411-3527-30ec-96d3-2c9ac8153e58 | -20.8776 | -57.7043 | 2026-09-04 15:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 1d76e9cf-d143-311a-976e-5691798d786f | -14.5755 | -53.6157 | 2026-09-04 15:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 507ceb37-4ffa-33df-b583-b6934b90992d | -13.9477 | -54.3971 | 2026-09-04 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 489817db-f9e7-3c74-ac37-d1e09ed4a7ea | -3.6033 | -60.5664 | 2026-09-04 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| fcc3a418-b2e9-30fb-9849-a63fc20f68d0 | -13.967 | -54.395 | 2026-09-04 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 7d2c69ae-6776-3354-a27f-88f87bba0c89 | -15.4994 | -53.8973 | 2026-09-04 15:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 39.5 |
| a9a78540-def2-3798-af70-a53eac52f38f | -12.3605 | -53.2021 | 2026-09-04 15:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 43f6a055-a60f-38ce-aa05-267119222b7b | -3.3685 | -59.5036 | 2026-09-04 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 7ec414c6-1090-3ccf-a0f4-14a0fe0e47b9 | -3.7645 | -61.7548 | 2026-09-04 15:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 37eaa75a-2e36-3277-9c3d-0b859a98ab68 | -3.3871 | -59.3883 | 2026-09-04 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 41745df8-d7d6-3bab-9065-0435fe5a9fec | -6.0806 | -59.9657 | 2026-09-04 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| dda45e30-02db-30e8-b790-e885f6a47d8d | -3.1462 | -60.6317 | 2026-09-04 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| f46978cb-b6be-398e-a0cd-3df4ce2e6128 | -3.5162 | -59.0405 | 2026-09-04 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| bb734973-1020-3da2-9a52-7f5efaa6fb9c | -12.1363 | -54.3202 | 2026-09-04 15:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| b45bf138-9859-3b71-9be1-8345e4584132 | -6.384 | -58.2958 | 2026-09-04 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 198d9d7e-2ffd-3a03-87e4-4f974aae08bb | -20.8776 | -57.7043 | 2026-09-04 15:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 108.6 |
| 15b14641-9060-3692-818e-84621f29e8ff | -4.4855 | -55.0848 | 2026-09-04 15:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 989eb02e-5566-3253-aa75-c9eca945225f | -11.2126 | -46.1066 | 2026-09-04 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| bfda97dd-0e98-3ca3-b871-5e00c1f9a2cd | -3.7828 | -61.7545 | 2026-09-04 15:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 8b5a33ea-5d73-306a-bd44-0e4b6c25697e | -13.967 | -54.395 | 2026-09-04 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| cf146413-0697-3ace-9d4a-789cc844fddd | -3.2341 | -50.558 | 2026-09-04 15:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| e839c611-9fea-317a-b220-2cff14a039fe | -3.3872 | -59.3692 | 2026-09-04 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 98f09816-ab59-3706-be19-f137b655d0a0 | -15.5192 | -53.8737 | 2026-09-04 15:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| f720a80b-3571-3585-9fb5-98a33639a76b | -3.3685 | -59.5036 | 2026-09-04 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 9feeaae7-5791-3bcd-98fd-db0cedab6c20 | -13.4516 | -57.0592 | 2026-09-04 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| a197a26e-0d62-33ea-9e63-c07b124b4117 | -9.0981 | -65.5091 | 2026-09-04 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b1801af8-e577-3bb2-a444-e4c9ad410924 | -6.0807 | -59.9465 | 2026-09-04 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| ca063c2c-36e6-31d6-93b2-dc950cd4db1d | -1.6206 | -55.5482 | 2026-09-04 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 2113baa7-bb24-308e-807f-3f46eb612402 | 0.1931 | -51.5218 | 2026-09-04 15:40:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 9eb31651-9e99-3b73-98e5-bfd1d43f654f | -3.6033 | -60.5664 | 2026-09-04 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |


[Clique aqui para ver as próximas entradas](README46.md)
