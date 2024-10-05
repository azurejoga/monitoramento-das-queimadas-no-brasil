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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c539abd-ce21-3699-8427-8ca12d36fcf4 | -11.89428 | -56.9331 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0699b5dc-968f-3156-a5f2-33a934e214bb | -11.89391 | -56.93993 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b9d9bdb-f8e8-3177-9ab9-9a7c9bb8d193 | -11.89354 | -56.93732 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c19e67ff-6121-3908-8d83-9d18849b971e | -11.89313 | -56.94414 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72c5bd33-0bb1-3676-9c62-33f74ce88a6a | -11.8928 | -56.94154 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43dad4ca-aebf-333b-8fa2-f9bf67ef3085 | -11.89236 | -56.94836 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0f3d6708-2e1b-3985-946a-d22df8888a76 | -11.89206 | -56.94576 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6fc40f3-c5d1-31a9-add2-207452c81c44 | -11.89131 | -56.94999 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e62fe762-eec3-381c-a2b6-1bb4f19a5930 | -11.89034 | -56.93492 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 565bf03b-ddd9-3855-9fea-3e5d395bc8b9 | -11.88956 | -56.93915 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6034d9ec-fa0c-3dac-b2d3-97bb1e31feb5 | -11.8892 | -56.93652 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79c646b8-4b31-39c9-afbd-1e513f0041a3 | -11.88878 | -56.94337 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c9bb890-c7b8-3606-91cf-fb409fa47927 | -11.88845 | -56.94075 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f248a0ac-aaa1-3f65-aafa-028a9ca43b67 | -11.88801 | -56.94759 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd714f1a-68f1-3427-b57b-3c6a9b45f723 | -11.88771 | -56.94497 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6f07ade-ccb7-3037-ad30-14d2c98bd8cd | -11.88696 | -56.9492 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db061ac7-6ffd-3ff9-a942-dd67a5725f4c | -11.88262 | -56.94835 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 2d3e4c4a-b342-3acc-9ac1-9d0d57d6d906 | -11.87828 | -56.94749 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| b6f3b168-2cba-31fc-be68-549cddea9309 | -11.82391 | -56.58954 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 790a7cdb-eb20-3626-8212-3bc722c1c171 | -11.8232 | -56.59359 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a9544d2-c7b2-3406-903a-94417b9efdca | -11.82248 | -56.59764 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eac84283-73b7-3f28-bfb8-fc56a2b1fccd | -11.82177 | -56.60171 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7af04ebe-358d-3182-b258-155f82dd7553 | -11.82105 | -56.60579 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92b2fcf7-ee95-3ade-bf81-9da0543e8bee | -11.81823 | -56.59686 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5450632c-6dbc-3509-964f-314f932cb9ae | -11.81751 | -56.60093 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71f26d97-8180-3f97-8fe7-9fa19e148e43 | -11.81679 | -56.605 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f987971-c2d3-32ab-8e55-217d8afe9077 | -11.81254 | -56.60422 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27bbe629-c2d6-3cf6-b9af-82fae70b8d72 | -11.48974 | -56.79608 | 2024-10-05 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c20b1fae-f1d5-38f1-9f7d-04a446491a9a | -11.48897 | -56.80026 | 2024-10-05 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37502584-4ad3-3b7a-803d-eacb7f411d2d | -11.48837 | -56.7975 | 2024-10-05 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74f0f7a2-c703-30c3-9836-5df37dbb443e | -11.48764 | -56.80169 | 2024-10-05 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4e0be1c-43f2-3ba9-b361-30896720fecf | -11.48464 | -56.79947 | 2024-10-05 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 965bc58b-3dfc-3bc6-88d4-c9b0709e67ce | -11.32988 | -56.23646 | 2024-10-05 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1c1b66b-451a-36da-b255-c2f56d59af0f | -11.3257 | -56.23564 | 2024-10-05 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e1ad86c-4283-3eda-b6dc-a9009baf795f | -11.32501 | -56.23959 | 2024-10-05 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6b8eb33-8224-3567-b354-df162f116db2 | -11.90462 | -56.95501 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcd9f634-0c92-3657-933f-9841da0eb7f5 | -11.88723 | -56.95179 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 160422a1-33a3-3475-ab06-ddb855d6285e | -11.88645 | -56.95605 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44dac5a1-294b-35d5-afca-cbdf190a66b5 | -11.88621 | -56.95343 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f1e527b-5f5b-3279-8409-854cb0b0a7e9 | -11.88566 | -56.96036 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f800aa59-cd63-328b-a32e-e1911d94ecab | -11.88546 | -56.95773 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d044d39f-0442-3040-ba5e-b2f3e077c569 | -11.8847 | -56.96205 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f8995fc-9706-3c6b-a989-dc0be1bfb7cd | -11.88187 | -56.95261 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| f4d7e62a-177d-3e41-873e-8d94304de8d1 | -11.8811 | -56.95693 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 284e498d-b183-3c89-ba81-5dc742eb2fc7 | -11.88034 | -56.96127 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 42a6cd68-c795-37b6-a012-23b92f835113 | -11.87958 | -56.96558 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f3e9407-a8d9-3964-a699-692719dc5c22 | -11.87752 | -56.95179 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| c720ae2a-c0d3-376b-ae86-9008a23af0c1 | -11.87676 | -56.95611 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6814a1e0-782a-33e1-a94c-4725fec4907a | -11.87599 | -56.96045 | 2024-10-05 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2acdb1bd-d401-3911-8860-4dabb95b84e2 | -7.52105 | -63.26629 | 2024-10-05 04:38:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 1d70b0fb-878d-31b9-a169-b52890c135eb | -8.83356 | -63.0313 | 2024-10-05 04:38:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0907a30a-1103-3d82-b5f3-bf9be93b831f | -8.83239 | -63.03748 | 2024-10-05 04:38:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f777e5b9-7e56-30aa-8b54-a95a35d1cbe9 | -8.82855 | -63.03032 | 2024-10-05 04:38:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29ad3cf6-f503-387c-bed4-a04ecd5a7a26 | -8.82734 | -63.03645 | 2024-10-05 04:38:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68e18a1d-f34a-3cc0-9a69-dcde556f8135 | -4.70695 | -55.98935 | 2024-10-05 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76df7858-a4fb-3ad3-bda7-4caa018e1be7 | -9.72624 | -56.98501 | 2024-10-05 04:38:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78be17fd-06c9-33b1-9a73-8dd4b40b9598 | -9.72567 | -56.98263 | 2024-10-05 04:38:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef7faceb-3530-301f-a1ac-f1a2bc39f708 | -9.72173 | -56.98411 | 2024-10-05 04:38:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51636afa-6ae9-3611-b286-54e8ae3e56ab | -9.64512 | -57.20152 | 2024-10-05 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9f7ceff-c77f-3f5f-8c10-dbae5c3fc224 | -10.13237 | -56.76806 | 2024-10-05 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bbec1eb-a59d-340d-a20d-3c21fb53ad1e | -10.12874 | -56.76283 | 2024-10-05 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e77fa29-b449-32ac-b856-a4a7250cd674 | -10.12795 | -56.76725 | 2024-10-05 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b614cc5a-091c-3c44-b051-196634a1ca14 | -5.79125 | -57.52992 | 2024-10-05 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7f27bb24-1a41-3ae0-a3ad-7e2911426129 | -5.79074 | -57.53287 | 2024-10-05 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| adc3c328-53c7-30a6-acb1-be862a035e84 | -5.73198 | -57.54333 | 2024-10-05 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cb3d398-e22b-3cf2-800d-cfda34410460 | -6.96506 | -59.07422 | 2024-10-05 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 89afc160-6436-3dad-9317-309b2cf37208 | -6.96497 | -59.07085 | 2024-10-05 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6fba5795-6bc9-36cb-a05f-7a064db8c54a | -6.96434 | -59.07446 | 2024-10-05 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 82494b32-0d60-32c7-af44-c84e02ee8199 | -6.96026 | -59.06963 | 2024-10-05 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7b22eec0-7ba3-3c8c-bb22-f9c2e279538c | -6.94924 | -59.06423 | 2024-10-05 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 19aa9508-7fe9-38c0-b9de-73245782c6f8 | -6.94862 | -59.0678 | 2024-10-05 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6332347a-0928-36a1-99f8-99ce4e602072 | -6.94315 | -59.06687 | 2024-10-05 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cb34c80e-4942-3085-bea5-3da252e3dd93 | -9.89124 | -59.5018 | 2024-10-05 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fd17ab30-19d0-3d30-aa2f-eb2ec8a4f046 | -9.8859 | -59.50079 | 2024-10-05 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60584d5c-d010-3cfc-b2dd-506d4f38cee6 | -9.88527 | -59.50425 | 2024-10-05 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec92d963-bc47-3f95-bd3c-6fd314065dde | -9.88465 | -59.50761 | 2024-10-05 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92c9b409-ea39-315a-b42d-5c3e6b36e54e | -9.87993 | -59.50323 | 2024-10-05 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 740f6f9c-6a76-31a5-85a7-a0ed85640150 | -9.87931 | -59.5066 | 2024-10-05 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 797831a3-3dfe-3140-b872-c712b8924fb5 | -9.80324 | -58.98122 | 2024-10-05 04:38:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0e050bb-79c3-3ffd-aa5c-0842671a1f10 | -9.80267 | -58.98429 | 2024-10-05 04:38:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca07a1e4-41dc-3eba-8540-e184a978e9c9 | -9.79752 | -58.98324 | 2024-10-05 04:38:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d60ced42-bb1f-365a-9175-dfb98d1ecdfb | -9.79693 | -58.9864 | 2024-10-05 04:38:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54bdf039-3314-361f-ba00-b3620f53a46d | -9.79633 | -58.98959 | 2024-10-05 04:38:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81fde29b-f83e-3d58-8680-b1dd8f2aacf1 | -9.79532 | -58.98904 | 2024-10-05 04:38:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cd57cb3-59e6-32f1-983c-10f8f15bbb87 | -10.36336 | -58.88197 | 2024-10-05 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd67221c-18c5-3a26-b986-530110bc1f76 | -11.37232 | -59.19371 | 2024-10-05 04:38:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e28cd03-8e76-35d1-bca4-27cc47ce3cac | -11.37173 | -59.19679 | 2024-10-05 04:38:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d8d8f9b-817b-3604-8391-a9b64bb95dc8 | -4.28798 | -60.02089 | 2024-10-05 04:38:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 544a351a-66a4-3005-ae5a-5fa2850a8e25 | -4.28192 | -60.01985 | 2024-10-05 04:38:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1778e531-30cb-318a-819e-395e889785e2 | -10.38052 | -61.1769 | 2024-10-05 04:38:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1de717b1-0cbe-33c3-8fba-b73db720d11b | -10.37379 | -61.18008 | 2024-10-05 04:38:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78370e6b-cef0-3018-b6bb-b63e162a9aff | -11.18666 | -61.28899 | 2024-10-05 04:38:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc33ad37-c103-32d0-affe-9b5c0ea012cf | -11.18583 | -61.2933 | 2024-10-05 04:38:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eacd1de7-0eed-36c6-b904-1fdf9d862204 | -11.18553 | -61.28813 | 2024-10-05 04:38:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80a31351-4c9f-3e3d-9cc5-d40b75abd006 | -11.18467 | -61.29243 | 2024-10-05 04:38:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f0ae602-6260-303b-8229-4fbc36f2898a | -7.27634 | -61.08968 | 2024-10-05 04:38:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d2d5b17a-3cd1-3257-bb6b-4be925ebc8e6 | -7.27544 | -61.09452 | 2024-10-05 04:38:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fe1b5a97-d9cf-3766-976e-cb226f30b980 | -9.17316 | -62.2975 | 2024-10-05 04:38:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08113c32-1c28-3443-9ea6-e2c859e8ba64 | -9.17212 | -62.30296 | 2024-10-05 04:38:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30f1f245-3d09-3784-bdb6-43cda3bfdbf0 | -14.19671 | -46.47847 | 2024-10-05 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README113.md)
