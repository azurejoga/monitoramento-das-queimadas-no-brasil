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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a372e17-c274-3c87-b382-6f79b1874ba0 | -10.7969 | -69.30833 | 2025-10-10 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b313f98f-68b5-3f8e-aa20-2e05b3d44faf | -12.64652 | -62.1035 | 2025-10-10 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 086a8415-519b-3f76-8461-16e702662c04 | -9.43944 | -68.81618 | 2025-10-10 05:42:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 454fdfe0-602f-39fc-a361-2f137037196c | -9.6476 | -66.9418 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bfa3e9c-75b1-3ae8-a1f9-6190ff615802 | -9.6043 | -67.1663 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c69de3b-e516-3ef7-95d1-838f6c5993d8 | -10.4601 | -69.23029 | 2025-10-10 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 155e941e-e184-35bc-81f2-2883bc7400bb | -10.46674 | -69.0559 | 2025-10-10 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 667b0ba1-5c90-3ede-8b2e-40de527e3579 | -9.46083 | -67.11339 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 220d38b8-e938-3e47-bffa-5d3452eec8f9 | -8.93442 | -67.48466 | 2025-10-10 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f035534f-5e10-30ce-99bd-0b3bf03a186c | -10.94179 | -68.3382 | 2025-10-10 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f618e956-0318-3e7a-b164-e86d7a8bf934 | -9.68667 | -67.45531 | 2025-10-10 05:42:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f938c53-5355-3a0d-87ec-659ca9f07fa2 | -9.64091 | -66.94072 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a887d361-efad-3cba-9e70-050857964459 | -9.66987 | -66.82508 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 506e4162-888b-3859-b16c-65092544a2fe | -9.66654 | -66.82454 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20a5761c-365d-3ff5-9002-0dad6ec8675b | -9.79663 | -65.05652 | 2025-10-10 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6457d648-8d72-37fc-ac73-bdb5e84e1fba | -9.6693 | -66.82863 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20875c85-a4de-34b3-bfb2-30f701971c14 | -10.7933 | -69.30772 | 2025-10-10 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eac29226-ba96-3eab-8252-642ed63c6108 | -9.60766 | -67.16685 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65ba7f1b-8d88-331a-aad2-9552dec0f689 | -10.63091 | -64.83611 | 2025-10-10 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dd1e4b3-6582-3d66-9758-d02cfc0cf857 | -9.95437 | -66.76979 | 2025-10-10 05:42:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f1a2080-aaab-3122-8536-a078ebbb1d76 | -10.63296 | -68.9686 | 2025-10-10 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41d6b8d8-52b4-3c67-b5b8-458b4d6eaa44 | -12.09399 | -64.23219 | 2025-10-10 05:42:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1111fc80-5442-3281-a02e-3d5e1c89764c | -12.09053 | -64.23165 | 2025-10-10 05:42:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b3f6286-97e9-37eb-bc3b-b7aa92411c68 | -9.01387 | -68.612 | 2025-10-10 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fae3a191-f7b2-33a8-9f4c-f985f8ba7224 | -11.76028 | -61.0688 | 2025-10-10 05:42:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68cb5805-391f-35b7-9830-d3fd4d215129 | -9.60489 | -67.1627 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec5da138-368b-396e-8aed-0279365cc445 | -10.00877 | -65.17697 | 2025-10-10 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5ea2fbf-0096-3742-adb5-975a2f7e5f84 | -12.08995 | -64.2355 | 2025-10-10 05:42:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fe7f8f0-cac5-31a0-9fde-7cffbb6a869b | -10.51283 | -69.27694 | 2025-10-10 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 885e288a-a0e1-35da-aba0-84d406678691 | -12.58802 | -62.96376 | 2025-10-10 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f050bf7d-3109-3b06-b18e-34e2d037b269 | -11.16694 | -61.31047 | 2025-10-10 05:42:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c3b1747-56d2-3d74-b287-b2d35fe280d2 | -10.95276 | -68.33615 | 2025-10-10 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 79901b2a-7cc9-3c3e-a922-ee666fc13d3f | -9.4371 | -68.81713 | 2025-10-10 05:42:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8779612c-4e1f-3bb4-a3f8-f3da5f4ac6dd | -9.68389 | -67.45107 | 2025-10-10 05:42:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c71a362-098f-3f50-974a-c72a22eed45e | -9.66263 | -66.82754 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d7d978d-29a5-3360-a5c9-72c9a06b8d97 | -9.66539 | -66.83163 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f6ebb8d1-d821-3aaf-a95f-ed59e37cb762 | -10.46729 | -69.19548 | 2025-10-10 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b75f362b-09e8-3a4b-be3b-fb6f0deadb8d | -11.76079 | -61.06509 | 2025-10-10 05:42:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f816aaaa-afbc-3a0c-8f08-b5906d563a71 | -9.95105 | -66.76925 | 2025-10-10 05:42:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15f31964-2638-3aa5-bc17-f7d1c7cc3efd | -8.7196 | -67.05294 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac5ccf35-440c-385a-acee-5d55682892cf | -10.90976 | -68.25861 | 2025-10-10 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df28d17c-2ffa-39f6-8d3c-e3e5f8f137bb | -9.95161 | -66.76572 | 2025-10-10 05:42:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2be0ca6-293b-394a-84fe-73771a20cb13 | -8.72296 | -67.05349 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02f56107-1427-3d12-b9a5-e41262ec9701 | -9.43856 | -68.05213 | 2025-10-10 05:42:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c233eea8-643f-3005-92f8-29ee1d68d35f | -10.08459 | -67.53477 | 2025-10-10 05:42:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9cf23be1-79f1-3835-b316-151338b9b89b | -9.23057 | -67.6048 | 2025-10-10 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e8ac3e8-b806-3541-bb3f-4dab4066abd8 | -10.82285 | -68.23354 | 2025-10-10 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbff6089-2adf-32cf-9331-42c2da21cb5c | -9.67995 | -68.5727 | 2025-10-10 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7247a361-2277-3086-a04a-072cf2793330 | -9.80596 | -64.97455 | 2025-10-10 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b03f4d2-d3e2-3e08-870e-3a0db148ce4d | -9.97831 | -68.76424 | 2025-10-10 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bf21e01-2cbe-3e72-92cf-d0a737022ed4 | -12.44567 | -62.03155 | 2025-10-10 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c13be0de-29b6-3ee5-ba2a-3bd61a06dcbd | -9.64149 | -66.93715 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6b407f6-bec1-3842-a055-aa31fc8408c5 | -9.87758 | -62.41009 | 2025-10-10 05:42:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d126069-04e6-3613-b38d-1c0dc369fd81 | -8.6273 | -64.08009 | 2025-10-10 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad211d99-64f6-3bd7-8c2d-caa067e9d64c | -9.62022 | -67.51633 | 2025-10-10 05:42:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 833f14f8-6b08-3f99-b87e-58be93976db4 | -10.09832 | -67.22815 | 2025-10-10 05:42:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab8884b7-c59b-3dff-bc30-172e4e4ad513 | -10.08349 | -67.53499 | 2025-10-10 05:42:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fb9c7af2-247b-38e2-8e35-0b0ebbaa7a19 | -10.82003 | -68.22917 | 2025-10-10 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 3bd2126b-c2d2-3efa-b2b6-d484fe258d82 | -9.11758 | -67.71683 | 2025-10-10 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| accf57c0-387e-3412-a17f-19f4f58231e6 | -10.82347 | -68.22974 | 2025-10-10 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5470ddaa-90f5-3c17-bf68-441f57b210fe | -9.67133 | -67.19959 | 2025-10-10 05:42:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69448146-28fe-399d-8a31-de5a6832ce4b | -9.79157 | -63.17704 | 2025-10-10 05:42:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f84484a3-de45-3d34-b8c9-d20705be2dca | -9.66596 | -66.82808 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a4dd314-209b-3f28-9613-1ea069a801da | -10.84156 | -68.8488 | 2025-10-10 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6c065df3-dc19-3415-aab0-58925ae4e873 | -9.64368 | -66.94482 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c14d0c2-3a3b-335b-a6cd-0d07b74e1dbe | -9.79216 | -63.17303 | 2025-10-10 05:42:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93aba116-808b-36bc-8c5e-9ad2dca45dec | -9.45748 | -67.11283 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f3f820c-27ac-33df-8155-8a67cf737356 | -9.63638 | -67.39484 | 2025-10-10 05:42:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aacca0e4-58de-35a1-b838-b1af6b1d2cda | -9.39858 | -68.23186 | 2025-10-10 05:42:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9ebc04e-a03c-3d74-ae69-daff31117d3d | -9.68946 | -67.45952 | 2025-10-10 05:42:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7491fcb8-d3a9-3f13-ae74-74eb171b169c | -10.17926 | -64.94959 | 2025-10-10 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d7e2a6f-6696-3b6c-924b-2bdbec8bf91c | -10.75431 | -69.17762 | 2025-10-10 05:42:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a91ff3d3-853f-39cd-9b41-93c6e5888aa1 | -9.87693 | -62.41445 | 2025-10-10 05:42:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5f6fe63-5f32-3335-9f3f-811e2603454f | -9.43587 | -68.81557 | 2025-10-10 05:42:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3e08171-61c2-302e-aa68-d5e0aa4f1c03 | -13.01152 | -61.43641 | 2025-10-10 05:42:00 | NOAA-20 | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1deb1bf6-dd56-38de-acd9-4d2d0e21a666 | -16.20045 | -59.33904 | 2025-10-10 05:44:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58266b21-bd2f-3b0f-bdf8-c805fc7c3f43 | -17.89372 | -57.66827 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 34e481b0-13d9-3e9a-aa1c-7c408cf465a9 | -17.90897 | -57.5267 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1a8d1084-65b9-35ca-a2b0-caea06f3ec5a | -16.00385 | -59.55315 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25566c98-2631-3b61-bdcd-0a4f28c10011 | -17.8879 | -57.51047 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 91eefdb1-ecc1-356b-ae10-731a1f370ffc | -16.00451 | -59.55197 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8182db36-7bce-3c1f-942c-54b9704f4526 | -18.03752 | -57.56186 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fab1f1b5-6fdf-3e55-ac7d-f5b00e17774c | -17.89972 | -57.665 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c6a32340-10a9-3268-86f4-525a6db93863 | -17.84563 | -57.58808 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f84354cf-b784-3712-814c-2cf991b19b15 | -17.82128 | -57.65928 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3d1dc223-5fb5-3169-be68-2d433a344b0e | -18.0322 | -57.55815 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f740e7d6-d054-34fe-8c97-3adc7374aa21 | -16.0092 | -59.54909 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| aec286ff-8a24-3750-a05b-77a676a6f6bd | -17.89841 | -57.66371 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3e21e311-4a76-3d2d-85da-4f3d7229effe | -17.83264 | -57.65861 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3986fb1f-2f76-3728-b4d6-ca729a06ecac | -18.0289 | -57.55505 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d119c52e-8145-3d74-9272-623270e97908 | -18.03914 | -57.56565 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0cc93cfb-2afc-340a-af92-c64a58acfecb | -18.03423 | -57.55844 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c6cb4c54-b428-386b-9cc0-c8a3b242455c | -18.02921 | -57.55215 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c8f687e2-bc52-3c45-996a-fa16323a06fc | -18.02684 | -57.55487 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b14e0f0d-7073-3ca9-af1c-c8ba1d5bbeac | -18.03253 | -57.55494 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 757a8076-57a6-3b90-a58a-b275bfd1c12e | -17.82697 | -57.65881 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| aca0f3b6-2719-3593-bd8d-aaf729afca5b | -18.07258 | -57.55323 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 40621293-43b6-3c74-98f4-ad225fda3268 | -18.02714 | -57.55193 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1b06c9e2-fb4f-3eb2-b209-1ffa6788d2fa | -18.05475 | -57.56039 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b251dc4c-17b2-3473-99bd-0f440d487116 | -18.04282 | -57.56572 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |


[Clique aqui para ver as próximas entradas](README49.md)
