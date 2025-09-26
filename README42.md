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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0d80ac8-fa49-3a7a-8264-39ceca58d7a3 | -7.30922 | -45.7618 | 2025-09-26 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d65f1133-7e28-358f-abf4-c4ef8b305c8e | -11.62448 | -44.44263 | 2025-09-26 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41ea49a2-20bb-3d71-b07c-2fbf619f5405 | -13.33404 | -47.88775 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88bf3fb5-a549-3363-bbcc-b74f6e9281be | -9.11302 | -48.89771 | 2025-09-26 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 067375dd-52ca-311e-b7cf-cb09d9fa849e | -13.84908 | -45.62184 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01f92d6b-7f88-3918-8cb1-c9b03266eb79 | -10.00836 | -44.1707 | 2025-09-26 05:04:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8300ae53-166f-30be-934f-f2ef93d020be | -8.08042 | -55.22256 | 2025-09-26 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df227933-a80b-3772-ad0b-77885c5610d0 | -10.18258 | -49.51149 | 2025-09-26 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 393c9f21-f4e8-36ab-b68d-3ba74e7b8e60 | -6.77617 | -55.48595 | 2025-09-26 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6836faf8-6a47-3b08-8174-059ec25984ba | -9.67491 | -46.0344 | 2025-09-26 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59691c0e-10b1-3c1a-8f44-12b20dae9b69 | -9.69264 | -48.94175 | 2025-09-26 05:04:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e907fb1a-4db2-35b5-92dc-d51f9ff52826 | -10.39401 | -46.13915 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68fa3a88-a9c7-3d9a-916f-bd6fd3215cad | -12.07314 | -47.99364 | 2025-09-26 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36616ee4-bfc1-33c5-9b38-eb8db857f0be | -11.24452 | -45.54333 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f2deb66d-7663-328f-bab8-bfd9980964eb | -11.95922 | -47.88375 | 2025-09-26 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e7c7cf29-e904-32a4-a300-5ce0e5e0ac5c | -10.39933 | -46.14397 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7ebedea-225b-3d8f-9543-c4ca1d7d99df | -10.40386 | -46.15332 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 09deb12d-edc9-38fe-b041-11c55d4497df | -12.0681 | -47.99182 | 2025-09-26 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdf4c25a-441b-331a-af17-bd20576e278d | -12.07335 | -47.99259 | 2025-09-26 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db004e70-c021-3548-952a-b5bb04fe2ef4 | -13.84715 | -45.61917 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36fc86f6-14c0-3989-8e8e-41be15cf8782 | -13.84338 | -45.61605 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 493a2175-3566-33b4-a395-7f902a9cf6ca | -11.01583 | -44.3507 | 2025-09-26 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7406aa2f-4809-38df-82e2-76c95874f10b | -13.85652 | -45.61229 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17024dd3-e5fe-30f7-8e77-679c35053ac4 | -13.74474 | -47.8782 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 267719b7-8163-3293-b9b3-454c672d84f1 | -11.61267 | -44.42971 | 2025-09-26 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1c8e673f-e2e7-3d4e-b7f5-b62e30a8c655 | -11.77038 | -47.56133 | 2025-09-26 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3f6cfd1-64a1-3f06-ac31-c272a054bfdf | -13.84771 | -45.61398 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3a71461-94b6-3d7c-aed4-15b6385f3294 | -12.73711 | -47.07273 | 2025-09-26 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f6a0041-fd69-38fd-89f4-03b092cb32f1 | -10.39784 | -46.15612 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e82c355b-dd81-3bbd-9c01-bdf4bf0eb659 | -13.85025 | -45.61157 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c315d74-82f7-36d9-8746-050a760a5aee | -13.32866 | -47.88701 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c445752-a200-397b-8dc8-2c68c354b05b | -11.24396 | -45.54802 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4acaa8ad-3364-3540-8a37-6a10cd01cca7 | -9.94973 | -46.28109 | 2025-09-26 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d8fab56-1d20-3ec2-9f75-4003e41a92fb | -13.64583 | -48.08739 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cb95ab9-8e26-3f5c-ad71-318c06101582 | -11.66962 | -44.44753 | 2025-09-26 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbf114f3-b492-33cd-9c7a-dc285c6178fc | -13.69923 | -51.15408 | 2025-09-26 05:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b825dec7-1f79-3974-ab71-6840513f39d9 | -11.22136 | -45.57602 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fcda038-fd76-3e66-bc70-d09917e0470a | -11.65818 | -45.35858 | 2025-09-26 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 794dea4d-20f6-3aef-a5e3-fd1999cf621a | -6.34667 | -56.20533 | 2025-09-26 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44bcf3ac-3290-337c-8112-2cd8317993d6 | -11.21591 | -45.57021 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| edd379d7-a255-374a-8a16-3a7f2a06421e | -10.80316 | -45.38021 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6ab5950-eb06-32fb-9f00-847f55d08fd9 | -10.00781 | -44.17933 | 2025-09-26 05:04:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5318215a-0cc6-39ea-ab3e-2bbaa1639cf5 | -11.0221 | -44.3481 | 2025-09-26 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4fdc56b-3c52-33cd-bffa-93b375fcbb58 | -10.03093 | -51.40962 | 2025-09-26 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a76107d2-3e01-394f-a265-7594214769f1 | -12.07354 | -47.99033 | 2025-09-26 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25e5246c-b9af-3621-bd51-39ffd9926e01 | -11.02147 | -44.35363 | 2025-09-26 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfb1382f-a5bf-3592-8241-5f805c207836 | -9.94412 | -46.27951 | 2025-09-26 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 079bfb64-05a0-3f61-b4b8-47b6c5925213 | -7.68097 | -45.99492 | 2025-09-26 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b482a93-74c3-37a2-93ec-3925352ac6cd | -10.62248 | -53.89237 | 2025-09-26 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2fed1b7-fdc0-34a1-8605-11aabd66236d | -9.70017 | -48.25295 | 2025-09-26 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3db52330-d331-37af-b3cf-676d72f96c3f | -10.11953 | -45.31404 | 2025-09-26 05:04:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a8956b3-b7f6-3cb8-bd56-baeb5c53ae54 | -7.67532 | -45.99406 | 2025-09-26 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2b9a339-a527-3ec0-8ef1-51abd32978cb | -10.40211 | -46.16937 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6fa93ff-5696-34bd-b364-1455d68cd221 | -13.69536 | -47.9711 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c2e8004-a755-3171-b22b-7946abdf72f1 | -9.47294 | -48.23546 | 2025-09-26 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2fe5ea8-2ed7-35cb-b0c0-70faa224a7e2 | -12.06909 | -47.98294 | 2025-09-26 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 886b6074-df84-3a6d-bbc5-be0794ae82b5 | -12.73667 | -47.07654 | 2025-09-26 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 770b5e00-c89f-3491-82b1-79f1de77d585 | -7.80894 | -55.22292 | 2025-09-26 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ee3559e-96a8-3e4c-92cd-851b81553713 | -9.98063 | -49.25401 | 2025-09-26 05:04:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb64328e-24ba-3055-b2d1-37f6f2bb30b7 | -11.43053 | -44.97458 | 2025-09-26 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bac4652f-5acd-3604-a98d-2d24aa8315d4 | -10.79702 | -45.37951 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f78d78b-4dbc-33c6-97fc-3d7ebf20e940 | -8.62668 | -50.01486 | 2025-09-26 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 110e2ae8-42f7-3043-8581-dfc33fe8a645 | -10.80763 | -54.13155 | 2025-09-26 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96546365-3a20-3bc6-9b9b-74016b426c10 | -6.99457 | -46.99593 | 2025-09-26 05:04:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2582f6eb-324a-3565-a2c8-43cba133b707 | -7.67481 | -45.99791 | 2025-09-26 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a21d15fa-5450-30bc-a61c-dad9c47827ad | -9.9834 | -49.25179 | 2025-09-26 05:04:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9891f015-33e3-350a-b91c-1203849bc67a | -11.02238 | -44.35146 | 2025-09-26 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ca04f8e-c881-3b78-bb02-79cc06c4597f | -11.67698 | -44.44881 | 2025-09-26 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c17b9525-c1fc-32be-8681-9cacf48d49f9 | -13.85344 | -45.61981 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eac8ccc7-7228-3004-bf23-01384fd31c17 | -11.22181 | -45.57821 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 291ddd8b-b943-381a-a725-6bc5a2357bfb | -10.39275 | -46.14795 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93c6df8c-8d69-3008-97e4-7e430cabe0f9 | -9.69674 | -48.94756 | 2025-09-26 05:04:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6b7d72b9-daf3-3774-be41-1c891c1776f6 | -10.79727 | -45.3768 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d564cc3-0af2-36b2-8534-8336e97c9666 | -13.85398 | -45.61472 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97665ed1-73ab-33a4-bf7a-2ab279d843c7 | -10.40332 | -46.15747 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b23ead64-790b-3536-bd1d-8082bfb22614 | -13.84397 | -45.61086 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8db58512-2147-3a17-be39-c53b6edb6a77 | -8.19524 | -46.38936 | 2025-09-26 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 656430bf-2c7d-338b-a798-37ee6ddf0bbd | -11.04325 | -45.88439 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c93a9a33-7fe2-3c4f-9bae-c6b32cd5b8ba | -10.40416 | -46.15272 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8c80f314-43ed-3c20-9639-6e9f06db6e7c | -9.67516 | -46.03168 | 2025-09-26 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| abf8b19e-da3e-32c7-860e-5e671fc1fc48 | -9.11372 | -48.89252 | 2025-09-26 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f46b085-66df-3e83-a67c-381283d515c9 | -11.95964 | -47.88049 | 2025-09-26 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 948605bf-ba63-3f91-b900-9e83cd216145 | -8.71521 | -50.05574 | 2025-09-26 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 803fb8d2-50a1-3740-92af-ef70bcc85bfa | -10.40689 | -46.17842 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 157a5f57-560c-3261-bfe2-a86ebfbc3464 | -10.3938 | -46.13982 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7771fc25-e73a-3815-84a6-791febf5435a | -9.6933 | -48.93669 | 2025-09-26 05:04:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| eae3644d-b5e5-3cb3-ae44-fdfe2e479357 | -10.10124 | -45.31152 | 2025-09-26 05:04:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1273f1c-f5e3-3666-8cdf-2dfa8577eee5 | -12.13179 | -47.9522 | 2025-09-26 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3287545-8b2a-3f33-b5f3-21ff5478da05 | -10.62662 | -53.88887 | 2025-09-26 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0f912e2-04b2-3826-af32-c504f7492bd5 | -10.54801 | -47.51756 | 2025-09-26 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45e0a931-bf6c-344c-b886-65e9846fd11d | -8.0832 | -55.22662 | 2025-09-26 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fe8473f-e486-35ea-a2c3-55fe2414cf8a | -10.40065 | -46.17796 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d54cae10-1393-3ca9-8127-a563aaea7d8d | -13.75063 | -47.87493 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96b8d6b8-4df9-3376-a7ea-c87c0a128602 | -11.64713 | -45.34502 | 2025-09-26 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a96ba81-48b2-3e05-99fc-027667df0679 | -10.39804 | -46.15269 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a3346abd-b6a1-359e-ab91-9adcef2e22c6 | -7.31439 | -45.76657 | 2025-09-26 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 285a3822-1d87-3290-92d5-5d7141fb42b7 | -10.54227 | -47.52018 | 2025-09-26 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4d07af8-e95f-31e1-8368-c82e7f34e81c | -11.2373 | -45.55193 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bc75f04a-940c-3d82-9983-1bfa8a5cafa8 | -7.30763 | -45.77351 | 2025-09-26 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac7a8d67-ca19-3635-bb47-afc7df813131 | -10.00704 | -44.18178 | 2025-09-26 05:04:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README43.md)
