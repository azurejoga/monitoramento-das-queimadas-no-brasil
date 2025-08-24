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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c422b56-703e-3e51-b529-e43f4968b3f0 | -9.1536 | -59.464 | 2025-08-24 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 208.7 |
| 92e56035-8367-35ed-81f8-24d11e68618d | -9.1535 | -59.4834 | 2025-08-24 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 166.9 |
| 90295cee-1b30-3bd9-9b8b-18859e3fba66 | -17.5975 | -44.3027 | 2025-08-24 01:30:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 4eeaef85-cb55-34fb-b793-95c6e0e638d6 | -9.0046 | -65.6988 | 2025-08-24 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| b33808cd-b92a-30f1-b6b0-6ed81c402321 | -20.3396 | -51.6839 | 2025-08-24 01:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 108.8 |
| c3447db2-c724-3fd6-83ef-1a69f3a39370 | -9.0246 | -65.3807 | 2025-08-24 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 0f6ae2b3-6e5f-36ae-a954-7fbec064a826 | -11.5242 | -51.8896 | 2025-08-24 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d71ae446-f658-3421-8fd8-2e881259389a | -20.3701 | -46.7433 | 2025-08-24 01:30:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 5ec62cab-96d0-3d84-9a02-566cbc7f5d91 | -9.0232 | -65.6982 | 2025-08-24 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 47631e70-a4b6-3484-b3c3-f49768e43ff1 | -8.6131 | -62.5929 | 2025-08-24 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 60e72179-78cc-3dcc-8ce2-beaa8dab2338 | -11.5245 | -51.8685 | 2025-08-24 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 176.1 |
| b0165f91-b9f7-3577-a60c-20d5a490456f | -16.7965 | -51.3637 | 2025-08-24 01:30:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 1713f081-5536-3c3e-8d8f-1e1680d5c152 | -5.4365 | -60.1588 | 2025-08-24 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| c3cc926f-cdbf-3b03-93f0-f89ea4b7ef5b | -9.1538 | -59.4446 | 2025-08-24 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 5ff13dc1-9151-32b1-8dd2-8e76a5221983 | -14.5266 | -51.9328 | 2025-08-24 01:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d3a7ad66-80ed-33e9-bacf-0af203ac08fe | -9.0231 | -65.7169 | 2025-08-24 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 7abea55d-51c4-316b-b840-6d83ed666672 | -11.5247 | -51.8474 | 2025-08-24 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| e97cfe6b-913d-3984-8b3f-da6cdfb74637 | -4.9605 | -55.8226 | 2025-08-24 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 37b23802-ab60-3992-86bd-91f7bd26a951 | -20.339 | -51.7062 | 2025-08-24 01:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 876aed33-de95-37c4-8754-8d5f014c3cd7 | -5.4026 | -44.9952 | 2025-08-24 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| bd5b1cce-9ac2-3c8f-a152-41fb4ea24658 | -10.6012 | -50.1629 | 2025-08-24 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| a6187433-9c16-395b-9a32-f3bf582f2205 | -9.1441 | -60.7765 | 2025-08-24 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 8663ce96-61ae-3e62-a3b5-cea48f5a2acb | -17.6176 | -44.298 | 2025-08-24 01:30:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 88.6 |
| d34f483c-cc08-3e6c-a98a-1b78c3117ac1 | -9.1721 | -59.4823 | 2025-08-24 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 617fa910-5f3a-35ac-a36a-a54c82f9f7dc | -20.278 | -50.8948 | 2025-08-24 01:30:00 | GOES-19 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| fa504e5e-2b7b-36ad-8416-880e8f23ad23 | -17.6183 | -44.2738 | 2025-08-24 01:30:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 32d96cdf-e4e1-3147-9bc6-21832be01ed5 | -3.5994 | -47.5359 | 2025-08-24 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 01132022-e2f5-3cde-81ee-675ebd61695b | -9.1722 | -59.4629 | 2025-08-24 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 238e85c0-2bf7-373b-93c3-d803f50c399e | -9.0416 | -65.7163 | 2025-08-24 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| ad326e04-7b29-3a01-8656-728ec13b77c2 | -20.3594 | -51.7023 | 2025-08-24 01:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 120.4 |
| a1b230c0-a135-3706-a460-b0e54b134ea9 | -9.1533 | -59.5027 | 2025-08-24 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f7164979-16d5-3fea-99ae-ca6328891735 | -17.4045 | -42.6186 | 2025-08-24 01:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 8be70cf4-e896-3b38-993d-33303e67c533 | -16.797 | -51.3419 | 2025-08-24 01:30:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 107.9 |
| d6ed2247-74ad-3bad-afc6-182ea94f617d | -10.6015 | -50.1415 | 2025-08-24 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| ee00918d-ad3a-36f1-bf8b-8c37cb36e9ae | -5.4182 | -60.1593 | 2025-08-24 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 7b014878-0587-301c-917b-de10c58e500e | -5.4181 | -60.1784 | 2025-08-24 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 42eb6a4e-0ed6-3401-8de4-acd49805553d | -5.4364 | -60.1779 | 2025-08-24 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 65cf7fc3-f7bf-3df9-b6c2-a773a2098d15 | -20.2984 | -50.8908 | 2025-08-24 01:30:00 | GOES-19 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.5 |
| be6ab2c8-c7e0-3cf7-8af0-6b7d6f0d2518 | -3.5994 | -47.5359 | 2025-08-24 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 2c98fec4-5847-3927-af95-4a3d4633fb27 | -9.1535 | -59.4834 | 2025-08-24 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 156.6 |
| 12eefa85-e052-3fa0-97ba-c66246e86efd | -5.4181 | -60.1784 | 2025-08-24 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 77f0f4b1-32ff-3603-867f-736c073a8bee | -10.6128 | -44.3284 | 2025-08-24 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| a3c47e61-f8bb-3048-a639-a1a22382028e | -11.5055 | -51.8705 | 2025-08-24 01:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 0a22d177-ccc5-3d2a-9cc3-f393f1506fb0 | -9.1441 | -60.7765 | 2025-08-24 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e76f7838-98fa-3b83-bd3a-be34fff8b6be | -20.3701 | -46.7433 | 2025-08-24 01:40:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 824c65ed-6895-351a-9ed9-6be38e00721c | -9.1536 | -59.464 | 2025-08-24 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 189.0 |
| 59eb085c-0ffa-3c67-8d2b-78be60679d8b | -17.5975 | -44.3027 | 2025-08-24 01:40:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 9eceba1d-0035-390b-8269-ccf9d310d26f | -14.8153 | -47.9343 | 2025-08-24 01:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 586f2d31-efa9-3333-8314-5f7f7bf3b737 | -9.0046 | -65.6988 | 2025-08-24 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| eeb515dc-55de-3e0c-89b4-5811451dfe87 | -9.1998 | -60.793 | 2025-08-24 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 7966ef3b-1f55-3cda-a8c2-853e8017d641 | -9.1533 | -59.5027 | 2025-08-24 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| ed4bea08-ff50-3213-9cf1-c66f561e2536 | -17.6183 | -44.2738 | 2025-08-24 01:40:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 1b04cfcc-29a7-3c98-bab1-bce68f3f919a | -9.0416 | -65.7163 | 2025-08-24 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a444a0da-5467-39ed-9494-23c3aa11b8a8 | -10.8078 | -46.4083 | 2025-08-24 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 8ecd4798-5a4a-36bc-b736-0d1a8aff31ca | -20.339 | -51.7062 | 2025-08-24 01:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 9fe7a7c5-b44b-3a21-9989-2ad1d4e3e94b | -8.6131 | -62.5929 | 2025-08-24 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 96965405-fc7d-3323-908b-111cff05eea3 | -10.6012 | -50.1629 | 2025-08-24 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 45864edf-e916-38c8-863f-832ca32b7c19 | -17.6176 | -44.298 | 2025-08-24 01:40:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 2370292c-5862-3b1a-b7a4-c2bb91648486 | -3.5995 | -47.5142 | 2025-08-24 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 6e400900-9ff6-3595-a264-9e06907eda4a | -4.9605 | -55.8226 | 2025-08-24 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 7fd0926f-d745-3df3-b18a-7d605c5b672f | -9.1722 | -59.4629 | 2025-08-24 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 154.8 |
| ffad69ee-89a6-357d-b0a1-6bff3dc890ae | -10.4164 | -47.1732 | 2025-08-24 01:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 923e574d-6990-3c17-bdae-73eb53d6ecc6 | -16.7965 | -51.3637 | 2025-08-24 01:40:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 9de9e47a-4b39-39cf-9c41-790cb89ee80b | -5.4182 | -60.1593 | 2025-08-24 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 5ccec6b8-5423-335a-ab6e-7a582284dab8 | -16.797 | -51.3419 | 2025-08-24 01:40:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 3f8008fc-417c-35e4-a4af-f2d55637dc97 | -9.0045 | -65.7174 | 2025-08-24 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| cbf2d9fd-a69d-36ff-80c0-bde9f453aa50 | -20.3396 | -51.6839 | 2025-08-24 01:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 77e417e9-b118-36b4-9bf8-2afe1c991c69 | -5.4364 | -60.1779 | 2025-08-24 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 636f507d-edfc-3814-a71b-293c7e4351cd | -9.0231 | -65.7169 | 2025-08-24 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 109.0 |
| f282898c-ff19-3e44-8237-7d8f316af846 | -11.5245 | -51.8685 | 2025-08-24 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 0f42550a-86b9-3744-8b36-12612ac6ac10 | -9.0232 | -65.6982 | 2025-08-24 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 18fad600-eb44-3657-a0f2-ebb45c04e545 | -9.1721 | -59.4823 | 2025-08-24 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 55ffbe28-3e3d-3464-aed5-58a8c0915e89 | -20.3599 | -51.68 | 2025-08-24 01:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 220443d6-ee62-3337-af22-b5ef9f51fd24 | -10.416 | -47.1955 | 2025-08-24 01:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 361ac26e-584f-3ebe-a116-e95b91eb855d | -10.6131 | -44.3051 | 2025-08-24 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| ba73fab3-2e28-3b0e-b13c-103a67e79025 | -20.3594 | -51.7023 | 2025-08-24 01:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 08a551db-0a1a-31e3-9930-b0b4f61029e2 | -9.1538 | -59.4446 | 2025-08-24 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 19c125b5-3238-30ab-b11e-68737fb427e3 | -17.4045 | -42.6186 | 2025-08-24 01:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 89f0667c-8e2c-30b1-81db-dda50db81fd2 | -9.0045 | -65.7174 | 2025-08-24 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| d443324e-b1f2-351f-930e-30a25eefe734 | -20.3599 | -51.68 | 2025-08-24 01:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 184.4 |
| c4c4bb9c-81ad-37a9-b6c0-8fb6f10430cc | -10.8078 | -46.4083 | 2025-08-24 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 05d30777-4933-3b4c-9435-575f6e4046b4 | -3.5995 | -47.5142 | 2025-08-24 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 1f7a57d6-165c-3d60-ac40-b5e8c02e8b70 | -11.5055 | -51.8705 | 2025-08-24 01:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 683eb16a-c3dc-3bb2-a4dc-cb24d4efe59d | -11.3368 | -47.8595 | 2025-08-24 01:50:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 40658aaa-06b6-3ef1-88c7-8ae7d675fcef | -8.6131 | -62.5929 | 2025-08-24 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 31f435c8-fc04-3dc2-9def-e2b825e935d4 | -17.5975 | -44.3027 | 2025-08-24 01:50:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 50.6 |
| d7adf897-10f9-32d1-a247-cb78e6ac8299 | -17.6176 | -44.298 | 2025-08-24 01:50:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 9a86613a-1a78-3270-bab2-dc769c473d0c | -5.4181 | -60.1784 | 2025-08-24 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 9e657944-1ee3-3d86-bdcf-b97f37b46d15 | -9.1536 | -59.464 | 2025-08-24 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 180.5 |
| c7b12829-1ac0-3cab-874d-2acf291cbec7 | -9.1441 | -60.7765 | 2025-08-24 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 129542bc-efd6-342f-b42b-f229696ee974 | -9.1538 | -59.4446 | 2025-08-24 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 22ca5269-ffd5-3cee-b586-cfdf51537b47 | -9.1721 | -59.4823 | 2025-08-24 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 91a87298-422d-3e2a-93d4-9a1c9c891cc7 | -9.1998 | -60.793 | 2025-08-24 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 573f1942-65c2-3872-80a6-647496f1524c | -16.797 | -51.3419 | 2025-08-24 01:50:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 92.8 |
| a2038655-30e3-3435-945f-10dcaabfcded | -14.7958 | -47.9375 | 2025-08-24 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 2a932d7d-f45e-39e4-84d8-a0ebf137527c | -17.6183 | -44.2738 | 2025-08-24 01:50:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 1bd7d6df-6344-3fed-b1f3-96fe8db9e6e1 | -9.1533 | -59.5027 | 2025-08-24 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 86219355-b1b9-3e69-bb13-4a2d2f234757 | -9.0416 | -65.7163 | 2025-08-24 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f74ad3f3-7331-3f0d-9df5-8b5efdfbf751 | -20.3701 | -46.7433 | 2025-08-24 01:50:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 01fb6561-625f-3f75-afbe-2ea1514e784c | -20.339 | -51.7062 | 2025-08-24 01:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 73.9 |


[Clique aqui para ver as próximas entradas](README17.md)
