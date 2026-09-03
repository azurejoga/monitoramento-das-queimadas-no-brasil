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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 398a32bc-7299-3134-b5e7-518e880e8068 | -8.4488 | -54.6644 | 2026-09-03 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 326219c5-3890-31e5-9738-1780c5a1caf5 | -3.0164 | -61.4848 | 2026-09-03 15:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 8cc60b32-33df-327f-a17c-bffab6450974 | -3.6215 | -60.585 | 2026-09-03 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| a39bc903-1923-3889-8e62-55fac046bf25 | -8.6853 | -62.9307 | 2026-09-03 15:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c2e8687d-aaad-3dd9-838f-2e0febf29f66 | -3.1815 | -61.1424 | 2026-09-03 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 1135e99c-d059-34c8-9acb-2e06c040f68f | -6.9656 | -59.7984 | 2026-09-03 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 6d700091-541b-3292-ad3d-ce5e1453567b | -6.3892 | -45.489 | 2026-09-03 15:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 185707f2-0904-3e85-861e-f98f9d68a8da | -7.3118 | -60.5897 | 2026-09-03 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 94f45038-e1f7-3cc1-b6ce-b0bf89a7f1dd | -7.0613 | -59.2165 | 2026-09-03 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6ce0dc6a-d82f-34d3-80bc-a79cb36f2b90 | -9.4728 | -45.6206 | 2026-09-03 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 57bfe309-51e4-33e7-97bd-869531dc44bc | -12.9036 | -45.8152 | 2026-09-03 15:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 15109d21-d71c-324b-b623-bafb25e5fe7b | -8.799 | -62.4905 | 2026-09-03 15:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| f810ccd5-4ced-3216-9a56-790d46fd8391 | -9.9915 | -46.4184 | 2026-09-03 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| af593ea5-7903-3e0e-b45c-7196cdee225c | -11.3334 | -50.618 | 2026-09-03 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| e1fd9421-5cfb-3de2-9ff7-d6e2359f2ee9 | -11.3527 | -50.5945 | 2026-09-03 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 1695aaf4-5f9f-3eec-9715-d282e89d1f20 | -3.6232 | -54.5931 | 2026-09-03 15:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 5d079c13-acf2-3444-a7ea-c850328383ea | -7.0242 | -59.2374 | 2026-09-03 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 770eee85-52ab-37cb-b510-bf6827beec5d | -11.4902 | -50.2796 | 2026-09-03 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| b6a7e751-97fa-371d-aef7-40fca4d1532d | -10.7621 | -50.8495 | 2026-09-03 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| fb439e1e-f680-3d97-850a-a98af7edc7a4 | -7.0427 | -59.2366 | 2026-09-03 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 6fbdcae1-025f-3cc3-b12a-b96658baa243 | -8.911 | -62.372 | 2026-09-03 15:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 6efd1d1b-a7ca-37d4-bb10-2c972b828558 | -8.9111 | -62.353 | 2026-09-03 15:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 9b5f9860-2661-3b52-9bb3-cc46d0ff24fa | -3.6216 | -60.547 | 2026-09-03 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 6b60a3b2-81ee-3189-b0e0-c6561a24f5fd | -10.9592 | -50.2744 | 2026-09-03 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| ec0c5412-4154-3d73-8d3a-191cbf55be4e | -3.1996 | -61.2177 | 2026-09-03 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 54a4cd2e-003f-3275-85bc-0110e70b5391 | -3.0347 | -61.4846 | 2026-09-03 15:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 3a0c5430-b379-33a4-afa4-8ed32f911da6 | -7.3117 | -60.6089 | 2026-09-03 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c945abb7-11fd-3b8b-acf2-a084f1bee410 | -17.0878 | -56.8534 | 2026-09-03 15:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 166.8 |
| ec84e4d6-a38e-31aa-97a0-9c25d291d434 | -7.3671 | -60.6067 | 2026-09-03 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| bb33de97-a325-355a-bffc-cbc393b96fc6 | -6.8172 | -59.9578 | 2026-09-03 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 5822ee8e-6617-3b06-859f-bec2415c4894 | -7.5703 | -57.6962 | 2026-09-03 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 6f5ec77a-8bab-3157-bb65-33c3e45f3337 | -5.4553 | -60.0626 | 2026-09-03 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 215b39d0-6ea9-3428-88e5-0954d0ce6720 | -12.1508 | -47.1058 | 2026-09-03 15:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 84afdf92-2287-317d-9bdd-fd12409360be | -11.4898 | -50.301 | 2026-09-03 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 2aac6209-16b9-34f2-a93d-a79e08c30924 | -7.5659 | -61.362 | 2026-09-03 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 71160c87-65b5-3c4d-a8ab-a2b31b69856a | -10.8249 | -45.3382 | 2026-09-03 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| fbb71887-781a-359b-a0f9-cf0981d7bfc3 | -9.4342 | -45.6704 | 2026-09-03 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| bd486111-d307-3c84-9f18-412413775002 | -3.3503 | -59.4657 | 2026-09-03 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 32624fe3-e880-3e5e-8916-14e716bcaa79 | -8.6317 | -62.5732 | 2026-09-03 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| db534d4d-30da-3399-818e-cd35ef75fd75 | -8.7615 | -62.5679 | 2026-09-03 15:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 9d4b2e96-dd36-34c9-8b0f-f0fe6cb2fb36 | -10.2212 | -50.3303 | 2026-09-03 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 85124165-3358-38ae-bf50-cfbd211b09b9 | -8.1345 | -45.4923 | 2026-09-03 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| ebd45ab8-8acc-3524-9bb0-fab2c8fe1cae | -1.4752 | -54.8157 | 2026-09-03 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 72083ea6-1d4f-3b9c-b565-4419c8b4a39a | -7.0428 | -59.2173 | 2026-09-03 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| bce7ad09-c096-38ed-b65d-ef4af0ba15f1 | -7.0786 | -56.5213 | 2026-09-03 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 13037d25-1dc3-342a-a5ef-abbc0bfdf14b | -12.1462 | -44.1725 | 2026-09-03 15:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| a99f5062-9d0e-3b72-818c-564425c73018 | -6.7451 | -59.6533 | 2026-09-03 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a176d5f2-c805-3fed-b1ec-5418f0dd63ce | -3.3872 | -59.3692 | 2026-09-03 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| b0332d21-3ec3-3790-8140-817402b0cb7b | -6.9872 | -59.2582 | 2026-09-03 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 747c9458-ea04-318b-a0ff-af53ae7fce20 | -9.4159 | -45.6271 | 2026-09-03 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.3 |
| aa6b9562-2a4f-3d40-81ac-ade1d3bd56f5 | -7.7522 | -61.0878 | 2026-09-03 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 80102661-dac6-3811-adc9-39e3fcc5d742 | -3.1815 | -61.1613 | 2026-09-03 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| a72d9498-9283-3487-8772-f66bc1b29793 | -7.3301 | -60.6081 | 2026-09-03 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 85264d78-395f-382e-b7d1-9cc6d231bc4f | -11.3524 | -50.6159 | 2026-09-03 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 3f006c0b-6799-329d-b646-d7671612acc7 | -11.4708 | -50.3032 | 2026-09-03 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 7f3cb983-ca97-397e-9ee5-14e291557827 | -3.3685 | -59.5036 | 2026-09-03 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| b86e0f21-5f6d-3050-ac15-40f8b3a7f520 | -3.3504 | -59.4465 | 2026-09-03 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 77d8592d-455b-3814-a59b-5755cf7dba98 | -6.9516 | -59.028 | 2026-09-03 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 3d533263-605d-33e5-ad9b-d7f29cc1cef2 | -5.3264 | -60.143 | 2026-09-03 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 45dc22be-f7eb-3b33-af0e-23bc8ad38b38 | -13.3817 | -51.3566 | 2026-09-03 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| bd986b45-b04a-381a-b085-c70ed2a95d66 | -9.6676 | -47.9429 | 2026-09-03 15:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| b244b34f-2a1a-3234-b67e-5ba0f894a45e | -17.0875 | -56.874 | 2026-09-03 15:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.2 |
| 3b24a369-ea01-3d51-bdfe-5b1f4538877b | -3.6215 | -60.566 | 2026-09-03 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 158.7 |
| fb0dd780-399d-3283-8cc0-4bb00a385dac | -10.8826 | -45.3075 | 2026-09-03 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 358.0 |
| c34f311c-b7e6-39da-ba1a-31736f4dd82d | -10.5254 | -50.1709 | 2026-09-03 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 4a8c9214-ad15-3ba8-bdab-1b64a75bbf4c | -3.2486 | -47.2438 | 2026-09-03 15:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 5c379266-7755-3862-a353-a8094af49de7 | -14.2537 | -52.0964 | 2026-09-03 15:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| ab066e59-af96-3ba2-ac42-575dc8afd09d | -10.7463 | -50.6172 | 2026-09-03 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| fdd3c2c8-0c7d-3a3f-964f-ceedf2bac38b | -6.389 | -45.5116 | 2026-09-03 15:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 76eb8f8a-285c-3065-8869-2ed0ef719ae5 | -8.7967 | -62.8885 | 2026-09-03 15:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 7057baee-b804-329b-b6e3-3c8fd2f7acb1 | -11.2126 | -46.1066 | 2026-09-03 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 54a09093-6c5a-3d9a-8b3b-b46f5723be4e | -17.123 | -55.9194 | 2026-09-03 15:10:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 6c0fdc6b-8431-37ed-8e99-cb16093e5796 | -9.4538 | -45.6228 | 2026-09-03 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 55d6ccfd-88d0-3263-a063-c51a9a94f820 | -7.1123 | -42.7727 | 2026-09-03 15:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| ef9bf185-9663-39cd-875d-ef624161ec6c | -9.6293 | -54.3158 | 2026-09-03 15:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 2cb77970-5b76-3648-bfa8-8df7bf983084 | -14.5758 | -53.5948 | 2026-09-03 15:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| e225d24b-fa68-3a2a-abfa-21f91a422336 | -7.0416 | -62.9702 | 2026-09-03 15:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| dbc23074-5353-3221-9349-7f7118b62486 | -7.0058 | -59.2382 | 2026-09-03 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 7074eb76-c656-3790-80b2-08d198fef626 | -10.0105 | -46.4161 | 2026-09-03 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| fafa802a-0d46-319d-92c4-933ee0fa1760 | -10.4634 | -46.5638 | 2026-09-03 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 5b2a1b57-7ed7-3193-90a7-98d6f0b78697 | -17.1227 | -55.9402 | 2026-09-03 15:10:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| f72a12c8-2c55-3543-b327-2703793c2ef8 | -12.9032 | -45.8382 | 2026-09-03 15:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| c562bf95-199b-3cad-844c-7da5e5d33a96 | -11.63 | -49.05 | 2026-09-03 15:15:00 | MSG-03 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11b9b69f-0f64-3dca-bb06-05e8689e704c | -8.948 | -62.3894 | 2026-09-03 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 4990be77-34b3-3b10-a86d-c051d1a1593e | -8.9111 | -62.353 | 2026-09-03 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| fecf8d2e-9e2f-3589-a137-fd1b6e4709de | -6.8203 | -59.4001 | 2026-09-03 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 433461af-ee04-3fe4-ace1-5dbec4f6e171 | -11.7532 | -50.4851 | 2026-09-03 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| f69f5d13-6912-3a9c-bc8f-9bf57bfd1c11 | -14.5758 | -53.5948 | 2026-09-03 15:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 871ccb17-b2b4-3776-a5dc-aa565ace80a2 | -9.6676 | -47.9429 | 2026-09-03 15:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 875531f4-faa6-3402-b894-9612ad3db507 | -3.1997 | -61.1988 | 2026-09-03 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 1bc551fd-7f44-32d0-ba58-5280e28c3420 | -6.8062 | -58.6469 | 2026-09-03 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| e774d3a8-d6a6-3804-9977-bb594a3f8506 | -10.9592 | -50.2744 | 2026-09-03 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| bfafab2e-9f62-37a7-bd82-2dc699e92bba | -8.7613 | -62.5869 | 2026-09-03 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 6b8752de-1fe8-3996-a587-d0e459dfeafd | -10.2212 | -50.3303 | 2026-09-03 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 0704a2d1-d20c-3a15-aac0-c0a35f34125f | -9.7401 | -58.3971 | 2026-09-03 15:20:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f29e1f72-1a69-31a7-9eb7-c23f5469872b | -10.5278 | -49.9993 | 2026-09-03 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 41408dd5-aa73-3963-8424-5d847054ed0b | -6.7123 | -58.9412 | 2026-09-03 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 8b93885e-dae6-329e-9092-e360b37c0adf | -14.4007 | -52.5226 | 2026-09-03 15:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 5d27c5cf-292c-3243-991f-8ceffd057ca1 | -3.6232 | -54.5931 | 2026-09-03 15:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| fcce0b21-c8f0-3e06-8d6c-c6d04de0ef93 | -3.3685 | -59.5036 | 2026-09-03 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 154.5 |


[Clique aqui para ver as próximas entradas](README65.md)
