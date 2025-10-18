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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f317b8e-5ca6-3807-9612-e10612920520 | -7.35681 | -43.85453 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74bfd513-7349-3907-bef7-a34f8986fa39 | -10.53829 | -44.0605 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f3ffdf1-b4b7-39d8-8c63-5f55986263b5 | -8.60786 | -40.19051 | 2025-10-18 04:02:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 187b3150-25c1-346a-b142-8bafc12ff0f5 | -8.64915 | -47.0833 | 2025-10-18 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 325ef07f-3b9b-3774-96f7-4d7807feeca0 | -10.88538 | -47.89858 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 878ca72b-4de0-3df7-875b-e1382c17d001 | -7.36683 | -44.2352 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d88816d-6993-38da-851d-553d60a57367 | -8.46249 | -44.16729 | 2025-10-18 04:02:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1fcd6f1-3edc-370d-bad4-853873113823 | -8.09048 | -45.44923 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6a198f20-2092-39e7-9889-fb430024db73 | -10.697 | -44.55159 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70825bb3-6924-3c96-ac6c-91948e3e2e8a | -7.3449 | -43.8573 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ffedf66a-3e34-3371-b0e2-caada8793d54 | -10.91674 | -45.41202 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f6f43c0-d8be-3832-908d-664b61d10716 | -7.83191 | -44.12432 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2336acf1-fbc1-3e0d-af31-261009c7293b | -11.60392 | -44.07363 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 230a6e53-eb05-3cf8-b9d2-e2ab315b3478 | -6.89419 | -45.44675 | 2025-10-18 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7533271a-2f98-30ef-b3e9-13e2c86aa6e2 | -8.48279 | -40.617 | 2025-10-18 04:02:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 705d32c6-2a1d-363b-84e4-6d35e8f576b2 | -7.84897 | -44.14387 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd2e712d-a2ad-313e-87db-4667f3803d88 | -11.48736 | -44.27346 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 06e80361-0441-396d-a89b-c9faa978cd78 | -11.85745 | -45.44732 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72f3410e-cbbe-346d-97cb-65102ebf6793 | -6.96516 | -47.1229 | 2025-10-18 04:02:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74be8194-c0d2-3f05-b6e5-9694d8c9047c | -11.58604 | -44.04939 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9939bace-6378-3238-a956-04e13090ea41 | -13.52014 | -48.01176 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5289049a-36dd-32ca-bf55-07a0113a2acf | -10.71614 | -44.55046 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc239b55-a562-30bd-b0f6-049e136a6b76 | -10.70658 | -44.56244 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f712d0d-7cc7-343d-88a6-566a19a6079b | -9.21648 | -40.77808 | 2025-10-18 04:02:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| da10d7cc-1711-3095-9f19-9b1f79487316 | -12.2429 | -49.37282 | 2025-10-18 04:02:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 383df654-67a2-3179-b5c9-d5a60bbbdda7 | -10.42592 | -47.74416 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a0c7caa-fc54-3f5b-8910-e58cc369fab8 | -13.19655 | -40.49157 | 2025-10-18 04:02:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e7234c1a-7d75-34d8-9913-ac793270969e | -11.57226 | -44.66224 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c94a200c-1275-307e-895f-e5e08227e529 | -10.52315 | -43.8864 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc3e586f-c1d4-396e-9f23-28ce0cee4446 | -8.14191 | -41.18081 | 2025-10-18 04:02:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b01e9537-b4b3-3769-ab78-df7776a78814 | -7.62586 | -47.8343 | 2025-10-18 04:02:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db2be2d4-3df4-3a2e-8668-07c91db627fd | -11.36452 | -45.25802 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56ce1427-32bb-3d02-9808-32cef3a4dca7 | -13.71169 | -40.98959 | 2025-10-18 04:02:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c8cc4883-fb12-35d9-b83d-f7a40719a5ce | -10.25252 | -44.04493 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ef3211f-c69b-3826-a76a-c7391d8afd58 | -9.9103 | -48.13974 | 2025-10-18 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b0f14f37-f3b9-3dac-9c60-af08e2e93963 | -10.46362 | -44.12312 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10f189b5-4729-3c3d-b661-3c52f1336d1b | -8.58265 | -47.02705 | 2025-10-18 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e25eeae5-12f2-3858-8a99-cbc8dab78d7f | -12.50974 | -40.82156 | 2025-10-18 04:02:00 | NOAA-21 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f3abc0e4-d217-3912-804e-d83b1857abbb | -13.44949 | -47.92611 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fe52500-5375-3cc6-b7c8-81e3a3deaf20 | -11.60828 | -44.09133 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4c3d86dc-bc49-3ba3-a889-f8d6cc706861 | -12.39075 | -47.20265 | 2025-10-18 04:02:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5e78520e-0d97-3911-b482-45d9c242c54a | -11.49368 | -44.23557 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cbad20bd-202a-350e-9fdd-86fd127c35d6 | -7.18046 | -42.17796 | 2025-10-18 04:02:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b451ac2d-53ae-3a90-9d0d-d6cae2573a10 | -10.2527 | -44.05865 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4771f83b-3a87-3ef6-a4b9-43b9b592d56f | -8.44297 | -41.44992 | 2025-10-18 04:02:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 28c8f71c-ddba-3e90-8427-dcf476651b0e | -10.23238 | -44.04681 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3d34e439-51e4-3e62-87e8-5da0e948ee4f | -10.52385 | -43.88226 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa315faf-c4d4-3a30-9b04-8499c05cae10 | -10.235 | -44.89619 | 2025-10-18 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88931c66-a80e-3bc2-ac73-f73729fc697f | -11.49341 | -44.17093 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45f7a9e0-bf9f-3e14-bc3e-5ace2fc7b989 | -12.68881 | -45.47785 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 850dfc6e-36fc-3320-bdd5-9065eea492d5 | -13.72791 | -48.11574 | 2025-10-18 04:02:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a83b9519-9682-3340-a1ab-1787108d617e | -10.24182 | -44.05707 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f2742fd8-ec27-3216-a6ce-f4b549287f73 | -10.96418 | -45.46031 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3f0a4b8-0598-3da9-ba52-251ca700ff7e | -13.77303 | -48.24266 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 234c60fa-5a10-3c11-baf0-2c6ea12f88b7 | -13.22252 | -43.98241 | 2025-10-18 04:02:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f480f3ea-0466-31f6-9d5a-ba1bf7b9c05c | -10.0884 | -47.65052 | 2025-10-18 04:02:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7d9cc3f-03f6-3491-8cee-f393de30f517 | -7.14127 | -46.40895 | 2025-10-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8131d37-f855-3f37-b70d-69e3f023620e | -10.70289 | -44.56178 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb7327fd-b79f-3c5c-94ae-8880bed96e16 | -8.24167 | -43.32082 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 979ea13a-ebdd-37e0-b9d5-110312376a6b | -13.77435 | -48.23198 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a008091f-5acb-3c75-9232-1053d9059bf8 | -8.33763 | -49.96757 | 2025-10-18 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9fc1951-aeed-31a0-852b-84591236bd24 | -10.16824 | -44.53803 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 524dc974-946c-33ca-9fa5-6a3ea19b14cd | -14.3868 | -40.77559 | 2025-10-18 04:02:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4b8507b1-e1b5-37e5-806e-88b4df445d91 | -7.76719 | -42.4848 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1b232ee4-7637-35f6-ad30-5fd6cb0abd08 | -9.37412 | -43.76486 | 2025-10-18 04:02:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4dd5f642-b6e3-32b5-819d-0e085d451888 | -12.15256 | -45.08095 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff8ddd65-5fee-3c0b-818a-8b3ff0835932 | -10.14021 | -44.5338 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c6c90b41-d002-331f-af3a-b38b56ed4377 | -10.34078 | -47.76898 | 2025-10-18 04:02:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b3762c1-58ec-31bf-a221-7600bbc20676 | -10.30221 | -44.03627 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 722cab3b-2ab1-3b87-8bdb-681f95939530 | -11.49699 | -44.17154 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2b6eafa-3a0a-3962-9570-f2e09baa1a1f | -6.42042 | -47.02565 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51a45216-6d8d-3b43-a20b-d76245fd7d3b | -13.43911 | -47.98289 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e56c0dc-4e93-399c-b4f3-7bef79be53ec | -8.20378 | -43.30624 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 82e209a7-02cd-309c-8391-9a1be27be143 | -10.9545 | -49.77239 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1797f162-d650-3910-b9bf-23006d9c0bc1 | -9.72638 | -44.54095 | 2025-10-18 04:02:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e67af389-1bad-39fc-bb75-8773f5d26f3b | -13.76742 | -48.24449 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 846cc2d6-78d3-3144-a945-8ad3038ad184 | -8.10327 | -45.44741 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2f8f6000-062d-3c67-8535-c847166ff722 | -7.36382 | -44.22979 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d604d0c9-bf40-3076-bbf0-89b62f4f9768 | -10.99766 | -47.89962 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 932ffb12-f80b-32a0-9cc1-a814d7021ce7 | -7.18329 | -42.18227 | 2025-10-18 04:02:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6160e663-73b2-3a6f-9922-bb5ade738e8a | -8.55668 | -50.08015 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c57cd63-5523-327b-8680-e859563dea82 | -9.50892 | -47.26927 | 2025-10-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 570d9dae-9436-3003-9a87-ff216b607d0b | -13.19549 | -46.41873 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fcecf74-ef16-34ff-baf1-770e697ea95a | -8.36372 | -46.21445 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79363f92-81b4-31c5-abd7-2e90a4c3f057 | -8.22535 | -47.84693 | 2025-10-18 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83ab78eb-3ccf-35de-a24a-c62f69f1148f | -9.75539 | -43.95901 | 2025-10-18 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 32854aae-3fd4-371f-b56a-b905fe6520c0 | -8.36273 | -46.24329 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44ee6e7a-1fd0-3222-92b6-19f4a94c12d6 | -13.03064 | -46.94596 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a4a777bd-3437-3188-98a9-080ae65d64ef | -9.04075 | -46.97211 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3d636ea-f540-3f5f-a495-379f446b3410 | -7.16035 | -46.21397 | 2025-10-18 04:02:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d719b2fe-6987-3912-b042-b37d99429333 | -10.25323 | -44.0328 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7fffa79d-2f4e-38bc-8d88-b0f4fbcf6e10 | -12.31339 | -47.83716 | 2025-10-18 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2018d0ba-2181-3ce7-a3ae-648f5a61a9fe | -8.56162 | -44.57739 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d78080e-36c1-32ef-9a6c-8f01f8522005 | -13.77185 | -48.24526 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8a3b5e27-595d-38ac-a992-0e4365e5487f | -6.42708 | -47.29654 | 2025-10-18 04:02:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 378f837f-3289-3a54-b099-20bc7bcd744f | -7.47523 | -42.74455 | 2025-10-18 04:02:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7d7e3c27-eb06-3c74-9a79-c04242376e16 | -12.63931 | -44.14095 | 2025-10-18 04:02:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 620337e6-1608-3737-bcb4-dfa6c5ecc324 | -10.5781 | -47.39947 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5e91e471-b8d3-338f-b444-2d887ab8a544 | -8.27469 | -40.59826 | 2025-10-18 04:02:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ec0b5d8-51d7-342e-b355-edbbc033a8b9 | -13.48917 | -47.95985 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README26.md)
