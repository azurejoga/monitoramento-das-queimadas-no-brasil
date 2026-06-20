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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3ee7e68-12dd-36e4-802d-f0f30c011285 | -11.62784 | -50.39769 | 2026-06-20 00:24:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d4298351-6f8c-31b2-bef0-81eca787255b | -10.46719 | -49.10055 | 2026-06-20 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f3d4ddd3-0fe3-3f63-89ca-674d49e9b2f4 | -11.30225 | -54.73571 | 2026-06-20 00:24:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 80f5b6ae-6653-3fa9-8f67-a6a8bbf1801e | -7.52726 | -49.64384 | 2026-06-20 00:24:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1818aae6-e4be-359f-a8a5-93a7fb77e14b | -5.81223 | -45.07864 | 2026-06-20 00:24:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 645d2cf4-2a3e-3c0c-aa3b-7755a6879d5a | -10.12111 | -52.19633 | 2026-06-20 00:24:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 551fb594-d3da-3989-9c01-97187b2c4236 | -13.11614 | -53.78059 | 2026-06-20 00:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| bf91ecdc-c10f-30df-918f-70ea66b3070c | -11.89043 | -43.83434 | 2026-06-20 00:24:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 4e4609cf-de81-3c7f-9679-2b5c20e66570 | -10.04925 | -48.09679 | 2026-06-20 00:24:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d7207737-b93f-3f38-98e3-bb32ad4c4bb2 | -12.55692 | -45.02401 | 2026-06-20 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| af6089f2-1d81-3360-8d37-d003ab165652 | -10.58873 | -51.77953 | 2026-06-20 00:24:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 557b5d2a-e42e-39eb-a500-d993341ed3e9 | -8.63977 | -47.75966 | 2026-06-20 00:24:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| e0baac85-7972-3874-9c25-2c1ee616bcbe | -8.65126 | -47.75793 | 2026-06-20 00:24:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 338cfbbc-08b7-38f4-8f85-caec891ee281 | -11.06365 | -52.48207 | 2026-06-20 00:24:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 91bf61b1-10b4-302c-adc1-2c92c141da13 | -13.51941 | -54.42137 | 2026-06-20 00:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 39661d31-3fb0-32a7-ad0f-93ab1520d6ef | -13.12507 | -53.79354 | 2026-06-20 00:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 5295f590-3ae9-32e2-b763-5f064d7408b4 | -7.36438 | -49.86078 | 2026-06-20 00:24:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| ffbb33d0-e059-301a-b0f1-cb11868f7c45 | -12.92261 | -49.48778 | 2026-06-20 00:24:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b32837da-b530-3f7c-9c0a-cb0a5801e4d6 | -10.46542 | -49.08877 | 2026-06-20 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d38869ff-04e2-364a-a050-c036b7ac4baa | -13.19578 | -50.34108 | 2026-06-20 00:24:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 57f2efc6-eba6-3334-b2db-26c28424983c | -13.30162 | -45.21888 | 2026-06-20 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 54bf68f7-8352-31c5-8731-3b3772af1d3f | -9.749 | -47.86697 | 2026-06-20 00:24:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c5974d06-49d8-3f50-b32b-c5db4c35e564 | -13.10692 | -53.78193 | 2026-06-20 00:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 26185b10-6f48-3d23-bf8c-8f5f63550dad | -11.06242 | -52.47313 | 2026-06-20 00:24:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 11eb611d-afb1-37c7-962f-fc75bbde0ace | -10.59569 | -44.32876 | 2026-06-20 00:24:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| ee49d08b-c844-385f-a6db-e0cff9eb3e33 | -12.65775 | -47.67929 | 2026-06-20 00:24:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dcddb642-ee04-323c-b68f-0a7cbb8cc477 | -7.29421 | -55.31009 | 2026-06-20 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1fef9cf9-11b0-3cdf-bdf8-a4c4dc72ec98 | -11.3589 | -52.95341 | 2026-06-20 00:24:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 23df6b58-6817-3b5b-9ca7-95c19bf3ce71 | -12.54799 | -45.03123 | 2026-06-20 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 4ea2a652-b5ed-3817-8092-77bc5ee8a6c6 | -8.98165 | -47.96796 | 2026-06-20 00:24:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a61d4dcd-32ef-3e52-a1ac-d57c6fc75b71 | -9.7199 | -48.89503 | 2026-06-20 00:24:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dac08d24-0f2d-3563-a711-b39f379baea9 | -4.34929 | -47.76989 | 2026-06-20 00:26:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 13f2641d-8717-3797-afd4-819332e474eb | -13.2066 | -50.3492 | 2026-06-20 00:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 140.1 |
| f08847c7-5d71-37e6-a8f1-561e16339a1f | -13.2069 | -50.3275 | 2026-06-20 00:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 8e95a45c-55b8-389f-b6e8-9ad7d8cc62cd | -13.1874 | -50.3517 | 2026-06-20 00:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 4815d937-1c9a-39ce-824a-166954306cbf | -8.6526 | -47.7602 | 2026-06-20 00:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 1dad7862-e675-3842-b442-4df8bc62047d | -13.1339 | -53.7625 | 2026-06-20 00:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| d9a29855-930e-3fe4-98d1-f0b54fc9eadf | -9.0155 | -63.5411 | 2026-06-20 00:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 74.6 |
| d5ff6c83-1b3d-387a-bb19-0c88fc5e688e | -12.5531 | -45.0174 | 2026-06-20 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| f0534c97-2fd6-33e4-9cb1-a8b9bbb19596 | -9.034 | -63.5404 | 2026-06-20 00:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 6c098a23-26b3-32d4-9361-656ab774f32e | -9.0154 | -63.56 | 2026-06-20 00:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| d784b24a-01ab-3b74-8375-d35a915ae239 | -13.1145 | -53.7854 | 2026-06-20 00:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 41886b34-dd67-3a72-867b-fd5231db733b | -13.1336 | -53.7833 | 2026-06-20 00:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 174.9 |
| 5771a52b-c7d9-37a6-aa90-bc4c2e18e310 | -9.0339 | -63.5593 | 2026-06-20 00:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b426bf50-ac2a-3dcc-9c09-6e448c26d87c | -13.1333 | -53.8041 | 2026-06-20 00:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| ca6b033d-36a5-3e5d-97f2-414cde3a94f4 | -9.0339 | -63.5593 | 2026-06-20 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 40.2 |
| db3036ff-0f6d-371b-9077-f990eff981bf | -5.813 | -45.0799 | 2026-06-20 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| f670daf4-ec33-3192-a63c-7aa3d13e016f | -9.0155 | -63.5411 | 2026-06-20 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 71.9 |
| df171dfa-f1e8-3436-b4a7-f1a09c511cec | -9.0154 | -63.56 | 2026-06-20 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 95311aa3-8c1e-3559-be50-a8a112e0a1cd | -12.5531 | -45.0174 | 2026-06-20 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| d073a9e3-7994-3139-9433-ba89b2f3d481 | -13.1336 | -53.7833 | 2026-06-20 00:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| b6fb2237-b065-362f-9642-08e8bfc58051 | -9.034 | -63.5404 | 2026-06-20 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 249ef552-f5f5-39eb-bfd1-1cb62c55ecc2 | -8.6526 | -47.7602 | 2026-06-20 00:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 4f617083-38d8-36f4-a9fa-20689fa879b0 | -13.2069 | -50.3275 | 2026-06-20 00:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 07b8a382-2236-31f1-9d76-8858063351e6 | -13.2066 | -50.3492 | 2026-06-20 00:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 97.9 |
| fb2a3816-c5a1-3fd1-840c-db65f04588e1 | -13.1333 | -53.8041 | 2026-06-20 00:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 408cea24-8b87-3e7c-a74b-23daad81f17c | -13.1874 | -50.3517 | 2026-06-20 00:50:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b2e859f9-03b0-3ae8-ab91-960ca37ee415 | -8.6526 | -47.7602 | 2026-06-20 00:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 921676bb-a182-3e8e-8c7e-f90b60563c60 | -13.2069 | -50.3275 | 2026-06-20 00:50:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 64f6797a-7acd-34ce-afcc-b55950b78424 | -9.0155 | -63.5411 | 2026-06-20 00:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b4f99ae1-d40f-3a5d-8fc8-deb4b1fba7bb | -9.0339 | -63.5593 | 2026-06-20 00:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 34.9 |
| cb14e521-266a-3d7c-bb2a-27c3a0e9b1dc | -13.1145 | -53.7854 | 2026-06-20 00:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| d25f9ef5-47d8-3db7-b5e3-d75fb861e73a | -9.034 | -63.5404 | 2026-06-20 00:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| f646504e-ef37-3b5b-b375-e1a7c5b1c768 | -12.5531 | -45.0174 | 2026-06-20 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 6cc1a456-ad7c-35c7-b509-17857ba520d9 | -13.1336 | -53.7833 | 2026-06-20 00:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 55fa62dc-d73b-3e1f-80f1-ffa138630959 | -12.5339 | -45.0204 | 2026-06-20 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 2bf44dbd-d0c7-3617-8087-88ef513b6bd3 | -13.2066 | -50.3492 | 2026-06-20 00:50:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 109.7 |
| daf3da42-b245-384f-8e30-06073efe4aad | -9.0154 | -63.56 | 2026-06-20 00:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 74ca5b9a-f120-3895-9dfe-738dbd8effb3 | -13.1339 | -53.7625 | 2026-06-20 00:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 146265de-db71-30d5-9ca9-9fd14fa20f4f | -12.5536 | -44.9941 | 2026-06-20 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| fc75b65a-3f22-3f7c-9a62-d8600f3996bf | -8.6526 | -47.7602 | 2026-06-20 01:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 0bbbb0c3-c3cc-3063-9f5f-efe381906112 | -12.5531 | -45.0174 | 2026-06-20 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.2 |
| f976e135-8e27-3981-bb83-9ce1a2c23b24 | -13.1148 | -53.7646 | 2026-06-20 01:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| ec2f7058-0c71-35f6-a34c-2179d2255785 | -13.1336 | -53.7833 | 2026-06-20 01:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 199.4 |
| fcef7dc0-8707-3fc2-a618-749770e8d0cc | -9.0339 | -63.5593 | 2026-06-20 01:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 707b4108-cb09-34c7-a4b0-ad35132bd824 | -9.0154 | -63.56 | 2026-06-20 01:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 5fbddbfa-819a-30b7-977c-e32a81aa52ae | -9.0155 | -63.5411 | 2026-06-20 01:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 8b79a81d-2709-3722-86c0-67a7ad6e6c4f | -13.1339 | -53.7625 | 2026-06-20 01:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| c2f637e1-ec7d-3468-a8ca-723674bae729 | -13.1333 | -53.8041 | 2026-06-20 01:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 669a6272-95f7-3abf-8fa9-022e4ec20a1e | -13.2066 | -50.3492 | 2026-06-20 01:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 2f7cd4f7-4f22-34d6-ad20-01cd40e19560 | -13.2069 | -50.3275 | 2026-06-20 01:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 45329bad-2f90-37c1-90a9-85a593858aa8 | -9.034 | -63.5404 | 2026-06-20 01:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ddadec90-06a1-381e-841c-5140d0cf1e2f | -13.1145 | -53.7854 | 2026-06-20 01:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 894b7828-e1a8-37cc-aaed-dda370bdcb1e | -9.0155 | -63.5411 | 2026-06-20 01:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 58513c97-009b-3c78-9671-b38907d5ba78 | -12.5531 | -45.0174 | 2026-06-20 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 9ff31e4f-76c6-324d-96c9-a9dfce4bc145 | -13.1145 | -53.7854 | 2026-06-20 01:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 473a2a65-eac6-3927-b19d-b05c97e6e2a2 | -9.0154 | -63.56 | 2026-06-20 01:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9beb966b-8308-343a-8bb3-63d1431f5ae9 | -9.034 | -63.5404 | 2026-06-20 01:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 6e97ef93-7d4c-3d7f-a12d-c12dcd2486bf | -12.5339 | -45.0204 | 2026-06-20 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 3eb7619b-284b-30a1-8a21-d894d36ba7ff | -13.1333 | -53.8041 | 2026-06-20 01:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 36a5f645-5d45-3e32-96cd-0c8e55352a18 | -13.1336 | -53.7833 | 2026-06-20 01:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 48b277e4-af15-3d65-9505-f90235fe9476 | -13.2066 | -50.3492 | 2026-06-20 01:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 9b7c4420-a963-3fef-9062-d75571d4fa70 | -8.6526 | -47.7602 | 2026-06-20 01:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| aba927f8-5e8d-3269-83e2-aad4ea3e1b0f | -9.0339 | -63.5593 | 2026-06-20 01:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| a5ed8204-d03a-3567-84c9-83a2cd83ccce | -9.0154 | -63.56 | 2026-06-20 01:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 231ab1e5-742c-36dd-b03f-d1577668d3ea | -8.6526 | -47.7602 | 2026-06-20 01:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 6aad6a93-dbb4-33cb-8389-5dc504c6c714 | -12.5339 | -45.0204 | 2026-06-20 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| fd1bf303-e331-3788-a61e-85b0826d8eca | -9.0155 | -63.5411 | 2026-06-20 01:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 5e327b59-235c-347b-8fd0-0108f1099f3f | -13.2066 | -50.3492 | 2026-06-20 01:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| b968ce41-9b16-3c10-8a52-70cb636c30cd | -9.034 | -63.5404 | 2026-06-20 01:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |


[Clique aqui para ver as próximas entradas](README3.md)
