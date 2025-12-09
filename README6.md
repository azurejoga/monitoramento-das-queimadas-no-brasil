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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7633b84a-99b3-3766-93a2-6de223e7f832 | -5.71015 | -42.06854 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d98377af-af81-320e-99cd-414c682fc11d | -3.33294 | -42.83862 | 2025-12-09 04:25:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 824d9fea-2d97-39dc-9252-3f4d4c5ddf03 | -7.86607 | -38.7299 | 2025-12-09 04:25:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| a04feb8d-1769-3dc1-97b3-80cd7cc7bf3a | -2.10607 | -45.95464 | 2025-12-09 04:25:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97d64175-d1ef-384f-9562-96ba59c6a46f | -5.82467 | -39.20731 | 2025-12-09 04:25:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b0e80eca-b139-3988-8ac1-aa7b6988dd11 | -1.87641 | -54.68378 | 2025-12-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5293b04-90e2-3e50-820a-d0723b5bbf18 | -1.06903 | -47.11831 | 2025-12-09 04:25:00 | NOAA-21 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a846ce01-fdc0-3712-b842-c6130fc54802 | -2.41617 | -45.7766 | 2025-12-09 04:25:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23102c70-a5ed-384d-ac62-d455599b8741 | -2.26056 | -46.46401 | 2025-12-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a40a9003-b403-328b-a2c2-d78f63908ec4 | -2.10553 | -45.9581 | 2025-12-09 04:25:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37d9860f-c22b-3456-9fb4-01bd25807f16 | -1.78307 | -46.19209 | 2025-12-09 04:25:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba324451-e5b0-3bde-9bea-ab9a077bdde5 | -2.09007 | -45.79581 | 2025-12-09 04:25:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6caf9166-b9d1-3ee9-80c4-b2cac9bd982e | -2.58016 | -48.17971 | 2025-12-09 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 15d74ace-213e-3eec-838a-a2ace7f4cc9e | -5.15327 | -44.09871 | 2025-12-09 04:25:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0ee58cba-ed4a-3104-ac71-13f9c45e1144 | -3.62892 | -42.36514 | 2025-12-09 04:25:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9b72c148-f8cb-3f8d-a995-8b113a3a3c58 | -5.68869 | -46.16707 | 2025-12-09 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7688fddb-24fb-3116-a823-14c51b777ac5 | -5.71084 | -42.06672 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 85f34f8a-0704-3cf1-9f51-dd169cacfda4 | -4.40516 | -44.3146 | 2025-12-09 04:25:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5193252e-25b5-3283-bc44-0ca9cd106d4e | -2.27118 | -46.05113 | 2025-12-09 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d3754c1-aba8-3d57-94ea-a96143ca94ca | -5.04119 | -43.59933 | 2025-12-09 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e005ac0-f984-335f-be55-0886cd577a39 | -2.91173 | -45.91494 | 2025-12-09 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 852cf11e-85d1-37a4-a8e9-29628078442e | -3.3114 | -44.37793 | 2025-12-09 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21e4def9-a3e2-37bc-9131-45666c69a661 | -1.67322 | -45.78708 | 2025-12-09 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37a57f6d-a043-3ac5-856c-39aeabdc1a53 | -2.39242 | -46.47054 | 2025-12-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5787a8b-5d47-31c6-86db-17ce6da4509b | -4.1808 | -43.83149 | 2025-12-09 04:25:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 069823a5-2824-3b91-ac89-0b4419c28fe6 | -4.48311 | -42.99143 | 2025-12-09 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 922650a4-4d57-3065-84a8-4c7f40ac614f | -2.09061 | -45.79237 | 2025-12-09 04:25:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dad4548-bdc0-3ca7-984b-3b8c51516c3b | -3.43348 | -41.65343 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 8249b11d-9b30-3694-bde0-7f33cf480df3 | -3.36924 | -45.83877 | 2025-12-09 04:25:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 683e4fd7-e34e-3b92-b184-e78030b8435b | -2.31918 | -45.55026 | 2025-12-09 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f18f8c04-089a-3080-9c4e-da81e7bf4643 | -0.30556 | -51.68506 | 2025-12-09 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43523982-cd84-38db-91bf-57759be03f21 | -5.70943 | -42.07598 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 67528daf-b8cc-35ce-b1c3-b46189da7bb1 | -1.55283 | -46.46924 | 2025-12-09 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 495c260b-f95a-312d-890f-7b1c48389ac7 | -2.11059 | -45.36252 | 2025-12-09 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff7439ae-a04b-3a7d-b402-b5c04ab8c650 | -5.71014 | -42.07135 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b9dab03b-987f-303c-aef4-382fe598ef61 | -3.4184 | -42.89524 | 2025-12-09 04:25:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db9290f9-11a1-30a8-a21b-dbedd602571b | -3.81919 | -45.68117 | 2025-12-09 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2382c19-f135-3378-a2c7-a778b9946499 | -3.43795 | -41.64944 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8dc70d29-3d3e-39a7-9fdb-65bdad537071 | -5.15669 | -44.09924 | 2025-12-09 04:25:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 947e9cdd-a260-3002-9f88-de6410e86879 | -5.36143 | -44.72937 | 2025-12-09 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6b32b97-22c2-300b-90cd-7bc5fc94a10c | -5.26072 | -37.71886 | 2025-12-09 04:25:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0cec934e-4ee7-3acc-9b64-aafcfef7b0f3 | -2.58078 | -48.17575 | 2025-12-09 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e09f39c5-3c1b-343b-9dc9-313c5e164b7c | -6.05411 | -39.43777 | 2025-12-09 04:25:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 376a09bc-f90c-38b4-855c-fa7c486f59da | -5.70634 | -42.07076 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 851dc162-e87b-3e73-a0ac-a4cafc9275b7 | -3.21514 | -46.06179 | 2025-12-09 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1785c932-b925-3094-8110-e43bc02b12c8 | -2.91835 | -45.91597 | 2025-12-09 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e96037ca-41fe-335f-8ad4-1e6b99b1ef48 | -1.96481 | -46.44292 | 2025-12-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94dbd58a-fe27-3bdf-827d-fb9866e06dbc | -2.05703 | -46.50473 | 2025-12-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 652cb540-62fe-3543-8412-24dba7052e8b | -3.62828 | -42.36941 | 2025-12-09 04:25:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1314a539-9482-3492-962a-a4a3ca938825 | -6.07274 | -41.50408 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 938bf0b1-feb4-3cc0-89b9-db01652bd5f8 | -3.81642 | -45.67722 | 2025-12-09 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8404b40-82cd-3cb5-92db-984bbf30b53c | -2.32863 | -45.57633 | 2025-12-09 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7676bf4a-0f45-37eb-81d2-35464794a77d | -2.05814 | -46.49768 | 2025-12-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7ae2f00-2e22-3b79-a012-29ee2811a5e7 | -2.05759 | -46.50121 | 2025-12-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e33c6ee-a7e6-36e8-9170-7cae2485d38b | -2.24807 | -44.831 | 2025-12-09 04:25:00 | NOAA-21 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed108daf-eb8a-3b83-9e88-8c0f8804631b | -3.43587 | -41.66315 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 0fcc2ffe-d2a5-3a37-9fe0-6ae2ba2faf9a | -5.71149 | -42.05927 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eec4fcce-47a9-3cfa-9e10-e15faa4bdaf8 | -2.74359 | -45.31797 | 2025-12-09 04:25:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20752edd-5af1-3865-9048-28f273e4d77e | -4.07915 | -43.85442 | 2025-12-09 04:25:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 672c5e5d-4707-3d0a-831a-4325b98a8663 | -3.66618 | -43.55156 | 2025-12-09 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc55c6e1-1a69-3dc0-aeb3-64295cd474b7 | -3.09519 | -45.20056 | 2025-12-09 04:25:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 234379ff-8ca0-3230-bbf9-5a8b72ce3ad8 | -3.4321 | -41.66257 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 03bc2658-e212-369d-8404-b72e53ad6f31 | -5.72511 | -45.03642 | 2025-12-09 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e720ee9-7eda-3fe8-a955-7422fef69de7 | -2.30711 | -45.56246 | 2025-12-09 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9921dfb9-33a1-3b1a-9830-c1b99d24e463 | -5.71154 | -42.0621 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3e45b263-a308-3096-b067-e2d35935d07d | -5.71082 | -42.0639 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f03560bb-1c1e-3a16-a5e8-8abd606ce228 | -3.42524 | -41.65683 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 612bdecf-cf8b-3305-becb-14b337704a0f | -3.62976 | -42.08988 | 2025-12-09 04:25:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9a7fd12e-3a78-3e3c-8f0a-fdcf8b1c06df | -2.09338 | -45.79633 | 2025-12-09 04:25:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f68218df-bbf9-3ca8-85f1-b8dc7035e4f6 | -2.10728 | -45.36201 | 2025-12-09 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b389e520-0590-3ebe-a6d5-e90e624a1524 | -3.28251 | -43.42557 | 2025-12-09 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2e8517e-c237-3710-8f0c-bafed0f1667f | -3.43417 | -41.64886 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f42961a2-0cbf-3367-aaa7-d3fc199c5618 | -5.72125 | -42.0494 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 23126b35-6a57-3065-8f34-ce3a3a1cb1fe | -0.30466 | -51.68218 | 2025-12-09 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 25f80e86-ee04-3a6a-a3a0-0d677dee15cf | -3.95748 | -41.52308 | 2025-12-09 04:25:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7f7cc64a-a048-3022-8a7c-8436773866c3 | -2.77659 | -54.52327 | 2025-12-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bf53d1e-e67b-3e7d-b940-53bb2e5eed54 | -5.87526 | -41.31938 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf78a4ae-d0d4-3976-8c4f-502f7b270434 | -2.9145 | -45.9189 | 2025-12-09 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3908df0a-76fe-3c26-8bdb-b1f684ae5fdd | -6.31626 | -37.70471 | 2025-12-09 04:25:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 104d21ff-5c4f-311f-b617-eab73304071c | -2.78563 | -42.48878 | 2025-12-09 04:25:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e748746-2fa9-3923-94b6-467d74b5daf2 | -4.18194 | -43.82407 | 2025-12-09 04:25:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02b517c3-3d25-3e98-978e-c2dffc416861 | -3.87879 | -42.51632 | 2025-12-09 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 89aca821-436b-38e1-9a03-e3f10e7cf55a | -5.72045 | -42.05116 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 901116a6-d633-3579-a073-cfac4abb54e9 | -3.19724 | -41.50127 | 2025-12-09 04:25:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a51a46b2-be33-397d-90ee-789c84a3c872 | -3.96054 | -41.52049 | 2025-12-09 04:25:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ed29561a-88d4-3b0a-b10a-3cb1a742ee3c | -1.87583 | -54.68726 | 2025-12-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6108cbf5-0b43-351c-86e8-973b75c2d9c9 | -2.37519 | -45.71388 | 2025-12-09 04:25:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8afc0b1-913c-3983-ab48-dfa16a0bc266 | -1.10103 | -52.23613 | 2025-12-09 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af136b0f-292d-3e51-852f-291c818c8b8e | -6.3167 | -37.70163 | 2025-12-09 04:25:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a040d014-bd31-355f-937e-41169fd99c20 | -1.10567 | -52.23693 | 2025-12-09 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eebfbacc-f0ac-31ad-8ace-73d7ac826d6a | -4.18423 | -43.832 | 2025-12-09 04:25:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04435387-735e-3736-ae9c-76f904650818 | -5.70564 | -42.07539 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0a1ed2fa-6e8c-38a9-8e82-31f7e94faf25 | -2.95462 | -48.06253 | 2025-12-09 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7bb1032-5980-300f-9fde-f946251773c4 | -5.70705 | -42.06613 | 2025-12-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 2c4ae95d-f8b5-3b30-9fc3-89d29b90fb1f | -3.44242 | -41.64546 | 2025-12-09 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4b2f4a86-3f02-3acc-b6ac-b6c4b64439ea | -1.52377 | -45.80622 | 2025-12-09 04:25:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0931bcfa-abbd-3cf2-8ae0-3f017ccbfcc7 | -5.0377 | -43.59882 | 2025-12-09 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9c1dc1b-f598-31bd-9974-c956d001b947 | -2.75786 | -45.16174 | 2025-12-09 04:25:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0df458d3-9d58-3705-bce9-820342049f0f | -4.82418 | -42.98109 | 2025-12-09 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b92fe11d-4179-3874-8a2e-1c14a3a0064c | -4.92926 | -38.75165 | 2025-12-09 04:25:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README7.md)
