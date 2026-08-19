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
| d5821616-13ec-3826-a006-e5407223b1be | -10.91562 | -57.18284 | 2026-08-19 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58b92be9-f540-387f-a671-663692f426a0 | -11.16188 | -49.62351 | 2026-08-19 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4c830b5c-a7dd-3202-81a6-35c4e6aa8a10 | -8.55854 | -54.72607 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3ffc212d-3077-3261-914f-2752da3ca260 | -11.72037 | -54.62327 | 2026-08-19 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d510433-c3e3-3a2b-817d-b799312705df | -8.54978 | -54.75032 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2f21a99-193f-3ed6-b26c-2647aa76f154 | -8.52955 | -54.73833 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bae1731-d7f7-3248-9fad-2e1cbd5626ba | -8.54904 | -54.75449 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0782ac5f-25c6-30e8-8fc8-6af42312355a | -9.45675 | -51.61881 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de2ab917-0a45-3455-8ce9-2ceeaba10f49 | -8.53675 | -54.74813 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0487ff85-ca88-3507-904f-b4fdb89f767f | -11.69808 | -54.56203 | 2026-08-19 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72978450-09f0-3311-b943-ccdb9f617fd3 | -8.56645 | -54.73183 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c947a4c-e797-339f-8743-ff96e2e42f59 | -12.51889 | -47.84188 | 2026-08-19 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 703c1542-afc9-3297-b1e5-b2eb2e9dfd00 | -10.81775 | -50.30074 | 2026-08-19 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0bad586-8717-36e9-8bd2-162fbd240b6d | -12.24957 | -43.15586 | 2026-08-19 04:40:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8bcf4c77-a4a4-3c7a-8452-9239b8bc7f8d | -12.47255 | -54.18239 | 2026-08-19 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b375e39d-38dc-3b3f-93ba-fa91b6fe8c0e | -9.49618 | -51.6831 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86d797ba-aff7-33dd-b280-f5e7ec454fe3 | -11.15913 | -49.61944 | 2026-08-19 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1652f0cf-1870-3fe7-85db-e67c02a70069 | -11.71019 | -54.63298 | 2026-08-19 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5060f32-45b9-3213-9ad2-c07af6fe1985 | -12.76182 | -48.45224 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b99cbed-5be9-3efc-ab24-83f79fd7c030 | -8.57506 | -54.75916 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| adcf97dd-b417-3557-8121-8cf0ab3a2a11 | -8.53764 | -54.76277 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab980867-2353-3e2a-b05f-4abddea398f0 | -9.00903 | -60.51052 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa598eb8-0fc6-3980-849c-275e7c5cd97a | -11.62051 | -46.90975 | 2026-08-19 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1cc07b9-0a9a-373b-b52e-7bb6b1a10079 | -8.53835 | -54.75858 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a93c214f-d5e2-3167-a21c-b5fd358c3e85 | -9.01245 | -60.50965 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5b764a6-5e03-3ac1-a004-21c9f7e09819 | -10.28356 | -48.23816 | 2026-08-19 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ebcf424-990f-387e-9b9e-4f7132e222c6 | -8.53897 | -54.73565 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1133b72-370c-374c-9a18-09195be49796 | -8.54109 | -54.74887 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c141850c-de83-3daf-b45a-a53e73953cdc | -9.0712 | -50.80845 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f21e3b5e-51dd-3e3e-b969-2ec5eb2a8c03 | -14.49174 | -45.66744 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f0805ad0-68a3-3379-aa8c-f46e8f3ab6a4 | -8.55631 | -54.73867 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6b2b5e2-7062-313c-85e3-fd0d7fe2e1a7 | -9.39694 | -48.24155 | 2026-08-19 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3081357-fe68-3465-96c1-40d997e491c8 | -12.8382 | -48.42362 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e346a24f-90fc-382b-8da9-ca40fdd5af97 | -10.93955 | -57.11877 | 2026-08-19 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 049f2048-3c95-329e-97ab-9dc93769d18b | -11.2138 | -54.00934 | 2026-08-19 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69950c40-405a-33bc-ba74-96bc62a18a30 | -9.50732 | -51.63879 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f4d1e6c1-a5b4-3ea8-a452-5f8b03f708ed | -8.56787 | -54.74916 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e122199d-62d5-33cf-b10c-04198a31b905 | -9.398 | -60.56987 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc32b596-31dd-34ef-8e21-60499688d0fc | -11.19233 | -54.82184 | 2026-08-19 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c7024c9-d04d-3223-8f37-9d93480e9ef5 | -14.24437 | -51.90872 | 2026-08-19 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73471eb8-d7d2-3638-8072-4fad2968a4c8 | -15.77689 | -55.57319 | 2026-08-19 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91cc8075-7194-3401-84dd-b65724d93699 | -7.60716 | -60.95825 | 2026-08-19 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b50aca58-076f-36a1-8ad8-6b3db30e7051 | -9.9942 | -53.95473 | 2026-08-19 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e7b1765-7b5f-3b01-a1e3-a536370f663e | -8.54035 | -54.75302 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dcbcdfeb-d975-3344-ac94-26d280979452 | -11.21945 | -55.06089 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a920249-927c-3109-b1bd-fc4b89d94013 | -9.45895 | -51.62752 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 329b20d1-877c-3eb2-99d6-7b79daa8208c | -15.24976 | -56.45756 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e225f00-589d-3c78-8376-be324eda8c8e | -8.55621 | -54.76455 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e9e10e7a-0d84-32a3-b4d4-06bbbf8ec868 | -9.08371 | -50.8769 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7ae3961-e189-3b93-ad00-b1508f73817c | -11.23636 | -55.06408 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad859bd7-0849-3b88-896a-aa9e8485bf14 | -8.57436 | -54.73765 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecd2a725-b89e-3f4b-a19e-5d27151b9b56 | -8.57301 | -54.69454 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2218316-a3f6-398f-863a-379853f567db | -12.37575 | -46.45035 | 2026-08-19 04:40:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 891d4fa6-8c06-365b-8acc-a4969d9ff201 | -8.57223 | -54.72432 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e3b2df3e-2634-3162-83e5-858729880da9 | -8.61762 | -54.71976 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64bc8a69-fc94-3b45-b057-35ce14dc56a6 | -8.4948 | -54.85572 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1f98f07f-d067-35dd-9a6b-ef4e9d57991b | -9.49489 | -51.67568 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1b3c7109-f243-3b9a-97f6-bbb3c6d05369 | -9.15792 | -59.71109 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a237343c-41d0-3f62-b3bf-351ec90fac1b | -8.56139 | -54.73521 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52cd3a93-8885-394d-988c-346409fd286e | -10.12328 | -52.12024 | 2026-08-19 04:40:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9283fc2b-61bd-3b37-9022-7b5edbdeb1e3 | -12.80422 | -48.44386 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8097eb7d-b307-3ae4-b8a6-3a5ea8b6312f | -11.31431 | -45.21608 | 2026-08-19 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2cf1baf6-ff8a-3ea9-8591-406b1f47ea2c | -8.58519 | -54.72679 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6dfe094f-076d-373b-9b54-5a4ea41d303d | -8.56565 | -54.76176 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 46cb7055-1c2d-3d28-bae4-21c0100bf32d | -15.2808 | -56.50834 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d3c1804-bdb0-32fb-a4e4-1f7c47c4dd26 | -9.05967 | -50.85748 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b359f7c-f59b-3b3c-a251-9e211ad93742 | -8.54183 | -54.74472 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6864f96-b51c-30b9-9220-8378cf925c8c | -12.52567 | -47.84294 | 2026-08-19 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3c3c1a0-fead-3760-94a7-47b61da55f1f | -14.45054 | -45.62682 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99774507-4161-3587-93ab-32b7ec6d4e4d | -12.51326 | -47.85613 | 2026-08-19 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4af1cf5e-e0bf-3198-94d0-6889823201e0 | -10.51876 | -50.79601 | 2026-08-19 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed93f7d4-9674-31a9-b5a4-16389bb2c282 | -8.55705 | -54.73446 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59b8e118-3c1d-34d1-b1fa-b358ecf62119 | -11.3225 | -45.21258 | 2026-08-19 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae51ced9-329c-3ae0-80e4-5bf640ec208b | -10.12066 | -45.75037 | 2026-08-19 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12c6929a-f3c7-374b-aa58-f6484d85dcf7 | -11.19719 | -54.81871 | 2026-08-19 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c01bc2ae-ce9b-38e8-bdb5-7b3c16015670 | -15.71104 | -47.80047 | 2026-08-19 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9df88e5f-7ed1-3ac2-ab2e-0b46d08171f5 | -11.05493 | -46.51233 | 2026-08-19 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 60643e0b-7039-33e7-86b8-a7a1afd94302 | -14.2178 | -52.91573 | 2026-08-19 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 14c2a933-70df-3279-8b60-e0ea0a162d0c | -8.89927 | -60.55638 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d52920cd-a019-3034-9a80-0dd3f64e0872 | -12.701 | -48.51925 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b375145b-ad67-32d0-9fe0-0c5876791e05 | -8.5794 | -54.73434 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b96dbdf-9295-33d7-a002-004cad914d91 | -11.92649 | -49.9851 | 2026-08-19 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9dbafb4e-a691-3b53-80ed-b1e4f52fbc06 | -8.54197 | -54.7188 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 03ac69e9-ddf3-3b1e-ad87-20b7605c8c8d | -9.72799 | -46.79088 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d095607-d198-3f68-81ef-ec068d4b69c8 | -12.35608 | -51.21103 | 2026-08-19 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51cdd319-169a-3460-bac8-8e72d9492211 | -9.47669 | -51.63068 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c59fe4dd-69cb-3740-935b-73da6f11ac74 | -11.47003 | -46.56368 | 2026-08-19 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 460a45e7-48bb-3b1a-9f92-90b8ee70397d | -8.58159 | -54.74734 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 44b4ce69-e34d-3db2-a519-21dd95a744e0 | -9.0775 | -50.81326 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8f401d6-d659-311a-bd5f-e790c02eed9f | -10.11281 | -54.2826 | 2026-08-19 04:40:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25b45b6c-0ff1-33fb-9bb8-4a47b5e0db32 | -9.46606 | -51.62875 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c67d1903-27ab-336a-a799-fb41e6a9341f | -8.57015 | -54.68553 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f5b6333-ce94-38fc-9871-4aa288dd4c1b | -11.05437 | -46.51605 | 2026-08-19 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a87231f-f190-3e67-9205-5e0571e85a34 | -12.37219 | -46.4497 | 2026-08-19 04:40:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad838baa-d730-31fc-ba57-9706fc64d25d | -8.57229 | -54.69867 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10c044c3-041f-3485-b223-d78cecd56b59 | -11.71903 | -54.6307 | 2026-08-19 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecc92b6e-3a6c-37bd-8677-801e5a1f250d | -8.50358 | -54.85711 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3175e384-0409-38ed-9dd9-b6824cde4fa8 | -11.24445 | -54.82601 | 2026-08-19 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 120e2611-5fd1-3be3-a1e6-f549819a3d8c | -8.56656 | -54.68066 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abc97cc3-e30b-32fa-b433-de2ce60cbc68 | -12.50648 | -47.85507 | 2026-08-19 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README46.md)
