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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b842444-47f3-3dd4-8f8a-e99b61139fb6 | -9.80701 | -61.19988 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4bfdef7-1b72-3060-8069-9e6706974ffc | -9.08958 | -65.73572 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fd3c8890-9cf6-3fde-8bc0-a64866cec9e0 | -9.54399 | -62.3997 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 39c00c11-a00f-3491-b637-93cc1b3bc636 | -7.39989 | -62.28707 | 2025-08-28 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d5703308-4d0b-30d4-b3af-396f2ab7caf1 | -9.40517 | -60.52659 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05090d8e-dfeb-3293-aeb8-436efbed7e1a | -9.11348 | -65.78498 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1163ce52-b59b-348a-92ef-3883966224d6 | -5.99717 | -57.85295 | 2025-08-28 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ce73f53-5518-3304-87e4-f627bd63c8a0 | -9.12825 | -65.77963 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 78b449c6-9d14-3eaf-a3ea-3c38aa2c40d5 | -9.789 | -64.25275 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8168353-8322-3e12-abe3-b989429da04a | -9.73142 | -64.90109 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b4adb730-dc9f-3a39-a42a-83522979bec0 | -10.02989 | -59.36245 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d741c7ba-077e-38be-a0c6-d23f740a5d21 | -8.95379 | -65.95978 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92ce8bf5-f3d8-3f4b-b08e-beecd8660dfe | -9.1988 | -60.28783 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a232bc7-b7ea-38e8-8684-93f569ea6c90 | -8.95944 | -65.96813 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7c3bacc-57ea-3962-8479-518e8f7e1feb | -9.47192 | -62.38169 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 557b7445-2896-3087-a82d-235a00b8c644 | -9.5393 | -62.40642 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43cfaa9a-3b91-3970-94d5-9bd838cebd52 | -9.08845 | -65.74313 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94c868e3-41f3-3b24-bc75-39f25d88c31f | -9.54444 | -62.39974 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 789464c1-4b6d-3746-b3f9-c35c187f1e69 | -9.53983 | -62.40277 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 648c90a9-1da7-3928-bc9f-ac02cd0c6cce | -9.40386 | -60.53627 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ee65cf4-2640-3c16-a1aa-460774520081 | -9.41444 | -60.52791 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08f4779b-d23d-3b81-88e7-f6b713512984 | -9.1396 | -65.28731 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 094015d0-20a5-30b9-a592-92a3af690562 | -7.60041 | -63.34623 | 2025-08-28 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d95e2929-f3b9-3aa5-8fbc-21e6df2c75f1 | -7.46825 | -61.39144 | 2025-08-28 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50d9cb00-2df9-3433-868e-7a0ce60c3a5b | -9.18942 | -60.80413 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fd5e1b9-9bb8-38d0-8de0-580b559b57cc | -9.2531 | -65.90438 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59ac39b8-29d1-351c-9688-e18e524d90b1 | -7.46401 | -61.39083 | 2025-08-28 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a83f1ad6-9901-3d85-a715-7a89e6bb1af3 | -9.78836 | -64.25708 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a21af87-ff52-37f7-b3d3-cf7b1f3a9728 | -8.94418 | -65.95456 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87de24ff-72dd-356b-8d5d-41a44d923cb1 | -9.12654 | -65.79077 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 812ce381-2f9b-3f3a-9556-415adf6c09c8 | -9.08158 | -65.71935 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fe45987-df0c-35eb-95c7-0ce4919bfe86 | -9.18176 | -60.85902 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa00ce41-d4e3-3ac8-8d81-34c81f20d775 | -9.48211 | -62.39814 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 885125ca-1f68-3ba0-a7c2-75f98f799fe5 | -11.22434 | -55.06853 | 2025-08-28 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c218f941-ddad-32a5-94a3-288da0d18011 | -8.95096 | -65.95561 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f36269c-17ea-347e-b4ee-a21aae6c12c2 | -8.94701 | -65.95873 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 785e4c17-7a41-38d3-a76d-65dfbc9e8be8 | -6.94863 | -60.07906 | 2025-08-28 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bbaba65-821a-3da9-a764-53abcdc5c807 | -6.00308 | -57.85704 | 2025-08-28 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aac4c41f-2cf3-3011-a761-2fb29be72dbf | -9.48724 | -62.39138 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f5c176f-32c3-3736-86ca-5f3796a7967c | -8.92831 | -65.92218 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fff014c-67b7-3d20-9c4e-bef29c68fd06 | -9.13791 | -65.78491 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dd067d9-0c9f-3da3-adba-de003ae56f10 | -8.65234 | -67.26976 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba333346-6c04-3cdd-862e-88d32a5cda3d | -9.07015 | -66.06735 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8275888-3db8-3bd7-af03-dd798ee66f78 | -9.15973 | -62.36038 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2f95b5f-1db8-379b-8727-d5d3d06f2255 | -8.99732 | -65.41836 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c47465b5-1637-33c6-bdef-a66c5f80bbb9 | -8.93231 | -65.9415 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66d206b1-f996-3ca6-813b-c54a1805aaa0 | -9.13677 | -65.76961 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a5cbff0-b98e-3768-9ece-8471acac7b5d | -9.01243 | -65.68983 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3a807c7-7944-36c1-be72-5fe466476b96 | -7.56881 | -63.86299 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42266f86-24e6-3d95-b8fa-33528fbd80a4 | -10.47303 | -57.93787 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| ade97a7b-47a3-3b32-bbb7-b0438e5dc56a | -9.40845 | -60.50242 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2d0467f-2c82-3dce-a964-be36c433bf7f | -8.93458 | -65.94932 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 373244e9-c89f-327b-8ef9-db80428f5802 | -9.40315 | -60.5066 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7894c2be-5c0a-311a-b8cf-a03f1db1a038 | -8.34806 | -62.94061 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25c1495f-844a-3750-8516-e6a6555ef899 | -9.53219 | -62.39793 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd263a17-0b4c-3aa4-8d75-b9a927cb988e | -8.88076 | -62.47794 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb2c7f15-3ebf-3b2d-bc89-96c9cfdc422a | -9.13734 | -65.76589 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce7a4236-0c3d-3898-9e98-6e46183dcf03 | -7.39589 | -62.2865 | 2025-08-28 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 360c0d28-1acc-3249-bb74-76dc190ab7a3 | -9.45544 | -65.42034 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7b8034d-d554-3dee-a14a-b76b1fede6b6 | -9.22117 | -60.8083 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af887421-edef-3bf3-9046-23f484d380cd | -10.46503 | -57.95662 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ce443dab-cbff-38c6-b9bb-76260cda05c3 | -8.47361 | -63.93095 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2be03869-7c3f-34c4-9c36-a9c444e8523d | -8.9317 | -65.92271 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f8218b6-c4e2-3c35-aad6-0593c4e804d7 | -8.09614 | -71.24779 | 2025-08-28 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df400607-8611-3efc-b377-aa9f500e12b3 | -8.64848 | -67.27271 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88a6d823-b131-38fc-9d87-36a8a5aa7bfe | -9.13052 | -65.78758 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0892d342-dae3-3301-a8f1-ffc88b86ca04 | -9.07127 | -66.06009 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 682d12e5-c006-3bec-a0af-07f2449e12b4 | -9.16622 | -59.56088 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7ff0fae7-1254-36c0-87b3-73d6945e0b91 | -7.46287 | -61.39876 | 2025-08-28 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc766c7b-08b0-3849-a732-fffe52b68fdc | -10.46977 | -57.93434 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74225012-3a28-3fed-8b26-0bc8f755b6e8 | -9.12768 | -65.78335 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2b36e277-5c79-37b8-80e4-c56d62b8d7bf | -9.03405 | -65.73116 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03835b46-0285-38cb-877f-688ecb96adf4 | -9.11705 | -67.70399 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb0d8c10-fb35-3f34-9b2c-f0ac44f8cc3c | -9.01983 | -65.68715 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 472e9f9a-3c3a-358e-bb09-0d170458b87b | -9.4908 | -62.39564 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e537ed1-e8f0-3d25-9b10-740d9d892e8e | -9.55144 | -65.69019 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39cc69d3-97ab-3b19-a77a-ded9bb6cfe6e | -11.23258 | -55.05688 | 2025-08-28 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ff9b5cc-6e7a-3850-96f9-35959fc3c1b5 | -7.39873 | -64.3428 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9c2c37f-dd3d-3e3b-bb9b-09bba0e9da13 | -9.19395 | -60.80477 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1846dcd-6414-3c8a-b4d3-7f77f74b551b | -9.01869 | -65.69463 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3a6c954-4e9f-3413-a097-2aeeeffa634f | -11.2263 | -55.06929 | 2025-08-28 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 422b155a-7a00-36e2-839a-7d523e68202b | -10.07943 | -62.89578 | 2025-08-28 05:48:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4948626f-2525-3b4b-9c72-38cb285db9dd | -9.17973 | -60.80743 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 404f408e-8f6e-3b49-88ad-ade5658238a7 | -8.34417 | -62.94006 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d792799-bd80-3b7a-a27c-b8d9b398e50a | -9.06733 | -66.06319 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d612d263-78ae-3c55-a481-c4a7d419b57c | -10.31737 | -62.62428 | 2025-08-28 05:48:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0c6ef98-e28d-3345-b0db-d8e0c26b5967 | -8.9617 | -65.97597 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d17490e-6c0b-3884-af1a-bbfbef70a193 | -8.95832 | -65.97545 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8752c05d-6251-39fa-8580-cb6b379d3441 | -9.05167 | -65.73011 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbe5603e-ff04-3cb0-85c3-e043b18c956c | -8.95263 | -65.94466 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c19efb68-05fd-3885-a458-6e6009ee7ad0 | -8.57826 | -70.11756 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46347f20-d1ce-365f-9213-6393b2fdbcc1 | -7.54329 | -63.85915 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fb1feb5-1d82-36fe-beba-0062b9ef1205 | -8.91278 | -60.7141 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e2afc7b-1a74-3746-94bb-4b4375312f19 | -6.24161 | -60.01603 | 2025-08-28 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce6abc81-66b4-384e-93e3-a06c0c4f7b78 | -9.47107 | -57.844 | 2025-08-28 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2fd9d9da-c794-32f2-ba3e-b7549207d032 | -10.46646 | -57.94499 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18ae9a63-0897-39fe-86ec-9f6d0b72bc3a | -8.84569 | -69.11069 | 2025-08-28 05:48:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f0a77b7-d031-3df6-98ba-a5decbac93bb | -8.84998 | -69.11101 | 2025-08-28 05:48:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 884c3e28-9eb0-34c7-a663-07c8ef4f3d45 | -9.18425 | -60.80807 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9e97400-46bc-386b-992a-6cbfa7b5fce2 | -8.51772 | -69.79804 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README82.md)
