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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 872a8680-0385-39f2-8dea-ddded4af288d | -15.06143 | -54.51514 | 2025-12-02 04:59:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a9abec9-f539-3f30-bbb8-ba22b13c3034 | -11.12261 | -54.64706 | 2025-12-02 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e7c0c5a-dc06-3311-9d2e-f94513424f94 | -11.67286 | -54.58168 | 2025-12-02 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0dba6d17-3f65-3ff3-9cf4-74a4191891d2 | -12.0442 | -54.23965 | 2025-12-02 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0d7e2662-1420-3245-bc32-cb6a6887c15d | -15.12303 | -52.94694 | 2025-12-02 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1f87aba4-0bdb-33e2-a756-070e6a105b27 | -13.0413 | -53.7097 | 2025-12-02 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87b49326-d25a-3182-8004-545b07f3f742 | -15.06087 | -54.51888 | 2025-12-02 04:59:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31b43642-1a8d-337f-9f70-5fc0cf20429b | -11.67673 | -54.57864 | 2025-12-02 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 324c7164-55d5-3ca3-85f9-cec2e6ebc3a2 | -15.97528 | -56.62253 | 2025-12-02 04:59:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4a4d45b-405b-38d2-ae2e-fc837410625b | -12.04982 | -54.24795 | 2025-12-02 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5579558b-6714-3738-b486-12141a241eaa | -13.0373 | -53.713 | 2025-12-02 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a237591-6239-32db-8ae7-9b210994db4d | -11.12756 | -54.637 | 2025-12-02 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ac27d76-fdb0-331a-8c0c-b76b612c5e11 | -11.67564 | -54.58575 | 2025-12-02 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 184e54a3-d976-3e00-8ca9-2235bd6b1670 | -14.07521 | -56.16313 | 2025-12-02 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e6483bc7-c3f1-3c6f-876f-567ad1e95ba8 | -11.12037 | -54.63948 | 2025-12-02 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f159d1b-8593-3f4d-817c-dd9abe7e5d4b | -14.60471 | -56.03979 | 2025-12-02 04:59:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aef34f89-b400-3575-913b-fb6a930662e1 | -14.9504 | -53.06213 | 2025-12-02 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e4bc321-1012-37bf-b6b0-091aef38386e | -15.12727 | -52.94314 | 2025-12-02 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 988c8d98-5676-3c0c-bd10-aa9eaea8ea92 | -11.43804 | -54.87065 | 2025-12-02 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5299f2c-771d-38c4-9724-c75f3e6807b9 | -12.51661 | -56.90994 | 2025-12-02 04:59:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d4864ae-c448-337e-b40a-a4a5f3765162 | -12.04085 | -54.23913 | 2025-12-02 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cdc8ab96-6e84-32ed-8bd3-dae79645a453 | -12.04756 | -54.24018 | 2025-12-02 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9e5d24bf-1135-3a08-8da6-beb8dc33fcb1 | -13.20356 | -53.15133 | 2025-12-02 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fde14b11-77e4-3d15-8216-d66de4e6d630 | -13.88161 | -56.20424 | 2025-12-02 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4061ce2a-c31a-31ed-8cb2-b2bf3b25ff61 | -11.12899 | -53.93841 | 2025-12-02 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 720cf717-b23e-387b-91e9-e0ffbf415c3d | -11.67619 | -54.5822 | 2025-12-02 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f57f2893-1d19-3e8a-ab08-73d4221a503d | -12.04646 | -54.24743 | 2025-12-02 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bfc6e2a-4053-3667-bd72-e75b42178c86 | -11.43418 | -54.87363 | 2025-12-02 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2ff0e24-42c5-3feb-8903-08df49397f3f | -11.07873 | -54.77721 | 2025-12-02 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8c8ed0b-13f6-3673-bd95-8665516fa17c | -14.07465 | -56.16668 | 2025-12-02 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 88f9c3aa-a428-3e34-baec-b320b232245d | -13.04473 | -53.71023 | 2025-12-02 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d9bccf2f-64df-32f2-99bb-1075e5633d14 | -15.11941 | -52.94639 | 2025-12-02 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b340368e-b241-36d9-9898-d9bd862aa8cb | -12.40362 | -54.89085 | 2025-12-02 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 432a8424-a450-393b-b7e7-4f94b9af3eda | -16.1301 | -58.2455 | 2025-12-02 05:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| e6987532-56b3-3c56-86bb-4dcd23ff0724 | -8.1633 | -43.2055 | 2025-12-02 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 2e2756ee-d971-333f-bda7-218e45b1804a | -8.163 | -43.229 | 2025-12-02 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| e0a45f89-952a-3426-9051-4cfc2618ae2a | -8.0513 | -43.1001 | 2025-12-02 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 202.7 |
| 1333eb6e-9d18-3aed-abc2-e479f141c78b | -3.2565 | -45.5607 | 2025-12-02 05:00:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 9ea1f144-90e9-31d0-9375-9c298bdcb98b | -17.55998 | -57.1829 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 64b176df-cd46-36dd-a1c7-7ae9760c6ae3 | -19.78703 | -56.68019 | 2025-12-02 05:01:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fe59ef77-1f98-3624-aaf1-c0a6265083cd | -17.51361 | -57.19744 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 2ce3b111-e91a-31d6-810f-d0fb6f67d8c2 | -17.51029 | -57.19687 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 9658487d-fdf0-31d2-b8ba-da73dcc97f9b | -21.62079 | -56.13583 | 2025-12-02 05:01:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0363032e-d2f5-3860-a013-56200659bcf8 | -17.5351 | -57.21229 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 94a8c32d-4f26-39cd-8897-273ebda7186c | -16.76234 | -55.10774 | 2025-12-02 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| fd968318-0c71-3272-b1fe-a54b3ad2bbc7 | -17.52298 | -57.20277 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bb806875-86d5-3b0c-abb4-d489983a2fa2 | -16.76571 | -55.10829 | 2025-12-02 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| dc943a6d-9e9e-3010-983c-6698ea8d75c1 | -17.74976 | -57.25294 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 10e9f183-b444-3ed1-8b00-8ba1b46680da | -19.77756 | -56.69748 | 2025-12-02 05:01:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3595af8b-3c81-38be-832a-ee43bd52e792 | -17.54575 | -57.18811 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e8cb7d64-51b1-3eb4-b2a0-15ef208bce41 | -19.7876 | -56.67651 | 2025-12-02 05:01:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3642e3d6-904c-3448-97b8-60b96083e40d | -21.62137 | -56.13193 | 2025-12-02 05:01:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f588351-63aa-3764-9c3d-58f4a4b34fd4 | -19.77813 | -56.69379 | 2025-12-02 05:01:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9a3d312e-f5d2-3549-bd26-bf56f375e3ec | -17.52184 | -57.21001 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1bd04f1e-5ee7-3774-b63b-d74352d09a8a | -22.12393 | -55.92643 | 2025-12-02 05:01:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa1c9cb3-0d1a-359a-be68-fc422cb065f0 | -17.55078 | -57.17782 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 285eaa97-e2cd-3d48-a503-8691234694e7 | -17.50755 | -57.19268 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c0ac60dc-e454-3647-964d-aef4c331c678 | -17.55667 | -57.18233 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 58b8f2cd-351d-3209-b513-a59f01e095ea | -17.55147 | -57.15194 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 0d62e82d-cd66-3d8b-bc1f-2886e3dd074e | -16.26358 | -57.33288 | 2025-12-02 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| de32fb59-9de3-3797-801e-76da6be7796b | -19.78258 | -56.68699 | 2025-12-02 05:01:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| cab2767d-443a-30df-a6b8-eea8dd909aa9 | -21.62418 | -56.13641 | 2025-12-02 05:01:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6938c5c5-a928-3fac-ba1f-3cb7807694d2 | -17.53019 | -57.20029 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8f9e916d-36a2-34fd-94f7-70a1af86961f | -21.62476 | -56.13251 | 2025-12-02 05:01:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0de4b345-c82a-38c7-b83c-13068c5b4cba | -17.51087 | -57.19326 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d637d321-9ee0-3bcc-88a9-16a8bb5d18cb | -16.33431 | -57.56974 | 2025-12-02 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| df6ab759-7a2e-3065-bd1a-ce26e148d171 | -19.78647 | -56.68388 | 2025-12-02 05:01:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0c5e040e-9ab2-3865-b9cb-42b211e4a88e | -17.49429 | -57.1904 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 274caffd-4025-3d98-a50a-2f2191b74086 | -19.78208 | -56.668 | 2025-12-02 05:01:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6addb630-01ab-3d8b-a2b3-6f2b47af8275 | -17.73376 | -57.24646 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6bd67fbd-03d6-3f64-bfb2-5d330536dcaa | -17.55724 | -57.17871 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4e41174f-c9d1-3873-b524-2a991dae9b2c | -19.78817 | -56.67282 | 2025-12-02 05:01:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0c584cd1-9de4-3144-86b6-3d3dd4f993a5 | -16.26025 | -57.33231 | 2025-12-02 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b7b3d615-6b9b-38b1-b1c3-34062b5ccdb3 | -17.51303 | -57.20106 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 1f056d09-1baf-3254-b8a5-1c76f8377690 | -17.51246 | -57.20468 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| fe5498db-b837-3d49-8199-42ba35e1ae55 | -19.78201 | -56.69068 | 2025-12-02 05:01:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 69734497-1ff8-34b4-a04d-a9ad27355b5f | -19.79093 | -56.67708 | 2025-12-02 05:01:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5577f5f9-443d-3779-9bef-8471e9a79a8b | -21.62561 | -56.13171 | 2025-12-02 05:01:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d5c2df90-241e-35f2-aad1-08a72738cee9 | -17.4976 | -57.19098 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| bd30d9cc-8361-3b6e-88b6-74777e0c12cb | -17.50972 | -57.20049 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 854fb2b4-4121-32bf-8417-415d8c56fb61 | -21.62505 | -56.13562 | 2025-12-02 05:01:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d42d446-1fcf-39d4-8ccb-ba6403ec9ad6 | -17.52904 | -57.20753 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 09d40978-a6c3-3be9-92f0-e0090ddf8282 | -17.50035 | -57.19516 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 147f951f-c806-3d98-adc3-2fc8a0bfe842 | -17.50366 | -57.19573 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f2ce6333-2fe7-3b1c-aba1-8f7b019bc0f8 | -19.78591 | -56.68756 | 2025-12-02 05:01:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 16db3258-2a5c-3fa7-864c-53baaace673d | -17.51852 | -57.20944 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| b2f950a1-9e6e-3793-9a36-b0a0a91d6f67 | -17.53178 | -57.21172 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 4ef74785-98c0-3e2a-95dd-97df15a43b43 | -17.5509 | -57.15555 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 4caadb25-45fc-3724-a0cc-b252909f09ce | -17.52847 | -57.21115 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 91669f17-c3d3-371f-bed6-4077df6e3aca | -19.77424 | -56.69691 | 2025-12-02 05:01:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 934770fa-7633-3643-938d-e48af800b04a | -17.5633 | -57.18347 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5e47f748-38d2-3a93-9b80-6d8f5e92f14a | -17.51578 | -57.20525 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| c314fba3-7646-38ba-a802-b0673172503a | -17.50092 | -57.19154 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8e0f98dc-2490-3039-b6d6-62cc4ada5cad | -17.50698 | -57.1963 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 16f9f5ef-9161-31fc-bf31-cf99facb8134 | -17.55393 | -57.17814 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 348bce0e-934a-3593-beba-07fdaf6421de | -17.49097 | -57.18983 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7f793755-1db8-35aa-9586-602db950fc83 | -21.62844 | -56.1362 | 2025-12-02 05:01:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ed9c746-cb70-3ba4-93bc-85e58565c5a7 | -16.33097 | -57.56916 | 2025-12-02 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 082f2e6f-9d40-3e51-b1a1-8d5ec86e15e3 | -17.49155 | -57.18622 | 2025-12-02 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 52f2b8e8-2b65-3b88-bc2c-46dc6cc316d7 | -16.12229 | -58.24089 | 2025-12-02 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |


[Clique aqui para ver as próximas entradas](README16.md)
