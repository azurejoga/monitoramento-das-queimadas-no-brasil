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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bb51c2f-032e-3179-b588-82efcaaa54d0 | -12.78048 | -48.38274 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abbf060c-5f41-3746-944b-2015141e11bd | -10.44897 | -50.47066 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7248cd7a-96f0-3ddb-bd5c-266345bd82db | -9.2109 | -60.89646 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3db110bc-e89a-3d2d-8645-f6cd1a6c53a7 | -16.67435 | -49.32368 | 2026-08-23 04:46:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49ca478c-4464-3b36-b9d6-37fbdd35b49c | -7.44424 | -59.77696 | 2026-08-23 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f59cba3a-f1da-349c-b3fc-b06a6a7e1e72 | -10.70989 | -47.73687 | 2026-08-23 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c1c4505-28d5-32ec-94ef-abc93be4284a | -14.97669 | -52.66746 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da47c10c-1db7-32b0-adb3-8956365fad00 | -10.52288 | -50.76908 | 2026-08-23 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab48d364-e400-3384-aee7-557327ae2b93 | -14.52057 | -52.00525 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ce6edc3-58e2-3fff-ad0d-ec8063cbb3a2 | -9.40498 | -60.31757 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59d916c0-70e8-3ec8-a583-b93a63ed15c8 | -11.84839 | -51.67152 | 2026-08-23 04:46:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06ec8b2b-332f-3b0d-9b2f-4585157ec622 | -13.8892 | -54.00645 | 2026-08-23 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc37df61-3454-34d9-9131-2f87b71b5f55 | -12.58805 | -47.88141 | 2026-08-23 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4aba6795-50ac-3320-9d4d-36c76541342e | -12.74345 | -48.41057 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c31cc6da-63ce-3188-89b0-60656b669519 | -7.43717 | -59.78053 | 2026-08-23 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 255d30b8-9e91-34d6-a510-6ca70d51bc04 | -13.21409 | -51.43107 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25d0a3e2-4e9f-3594-a443-65bfd098ab22 | -13.89196 | -54.00491 | 2026-08-23 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c51013bb-df11-39cc-90ef-20fca7c14972 | -11.05461 | -49.50958 | 2026-08-23 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa5104bb-eb93-3b05-869c-16df022f2411 | -9.21624 | -60.90339 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c424b28-eb46-3e30-a6bc-8422c6c6944d | -13.8881 | -54.00434 | 2026-08-23 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03f91268-f7a6-3eec-a0bc-a09de59c924f | -9.42921 | -51.61462 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce509618-e98b-37a7-bfbb-25c76e139628 | -10.38182 | -50.41117 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09c691e0-5199-3c08-911f-d8666c49eedb | -12.40533 | -42.90018 | 2026-08-23 04:46:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 369e850b-f1d4-3599-97be-b6e4d5200159 | -13.53864 | -48.18744 | 2026-08-23 04:46:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a2088ea-bb72-30ac-babf-3450a1fd5d3b | -8.20308 | -54.98551 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6e58069-441d-3afa-81cc-4087178259d9 | -15.34117 | -52.77483 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aecf7bcf-7c0c-380f-8d19-0e3ac584da61 | -11.21434 | -55.04499 | 2026-08-23 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5ec56ab-275d-35ab-8c6a-b47d08aae2c1 | -9.1655 | -59.46534 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a1944c9-7b65-3a02-8f9f-6a6a176de560 | -9.42373 | -51.66865 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51c4dc40-924d-3e6c-b7a5-03ac46381d7f | -7.61402 | -61.61274 | 2026-08-23 04:46:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55fa081e-5897-38f3-a0eb-f9dd4569527a | -14.40062 | -52.93248 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 720f08f0-a108-3646-bd86-5329c9e31b8c | -9.45305 | -56.90326 | 2026-08-23 04:46:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9dec61e-74a6-324a-8125-d6d9e2289668 | -12.00671 | -53.42184 | 2026-08-23 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aaf70596-5e39-35d2-8a6b-224b462d96ce | -8.53052 | -54.84705 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3103c365-bb17-34cb-af53-cab4bd8e7936 | -8.92553 | -60.71611 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a21e9fd-c137-3622-8042-16b4c73111eb | -15.25135 | -52.83534 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df350c96-c49a-36c8-a78c-5eafb5a7fac2 | -10.68316 | -47.72183 | 2026-08-23 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab896a4b-a945-3c68-bb0a-be0daa9a2315 | -9.10875 | -61.59566 | 2026-08-23 04:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| acd7d5c7-714b-3867-b48f-0d6a8cbf967e | -15.25063 | -52.83954 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 276495e6-f9fe-3f16-b01a-cecb8d212dc5 | -11.16189 | -54.01431 | 2026-08-23 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e819290-b1e8-3d6f-997d-43f417035d73 | -7.62214 | -61.60783 | 2026-08-23 04:46:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1eacb6d-d43a-3044-9419-e35dd3c34a7a | -9.80023 | -46.60963 | 2026-08-23 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59458f7a-46e7-347f-a574-d5d8595efafe | -9.04603 | -50.88033 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8dbbdb36-2e55-3957-ab9f-feb5e2c89fcc | -9.4195 | -51.63952 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3068a6f5-a563-3a3a-bc03-3ef264616557 | -8.5423 | -54.83136 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fcba4ea-5612-313e-b434-6837eecef39a | -9.42006 | -51.64682 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f118e8a-92d4-370f-8e50-2ab6d3d2f26e | -15.25347 | -52.84433 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c79e5995-0dd3-3ce5-9d6c-bb41fae9829b | -9.4251 | -51.62789 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 907b00e7-d973-3923-88f5-ba1ae5b91e96 | -8.55337 | -54.84623 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fcc88f6-4b25-3618-9cba-d11cc3ff4d7a | -12.64833 | -47.64712 | 2026-08-23 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37dfef50-4107-303c-93de-5310ecf31e30 | -12.07096 | -50.59933 | 2026-08-23 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 652bd9b0-c0ec-38f3-9399-46aa29037117 | -9.44774 | -51.59202 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0241708f-2e84-3d6b-a231-133bcfa49526 | -8.59798 | -54.71631 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc7f085b-0949-341f-8872-b22ddd6f5ffc | -16.04975 | -50.44002 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 49b4fd69-e120-3565-80b6-9eeb2cddef6a | -8.58854 | -54.7188 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15fb99cb-2a13-308f-bb41-1cb84157fc27 | -12.72778 | -48.40081 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ba91eee-849b-3c82-b6e8-8939cf80b4c0 | -9.44208 | -48.236 | 2026-08-23 04:46:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 554173dc-c24e-3a11-a2f7-337f68b64d5a | -13.68581 | -51.85283 | 2026-08-23 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0eb8ad51-3558-3da9-8784-bb0118708691 | -14.36307 | -51.777 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 767ae0ce-09e3-3fad-948b-ddad2a8ba01e | -16.3972 | -51.33315 | 2026-08-23 04:46:00 | NPP-375D | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f397609-8d5a-3852-aea1-8b165e6b2b8c | -13.52913 | -40.64266 | 2026-08-23 04:46:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8df30497-4300-3eeb-9096-f53207c6df61 | -10.84222 | -50.99136 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28cb2cf8-7d6d-3e3a-9db7-e12316ad6ee8 | -14.95759 | -52.65138 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d7cffb1f-f1e2-379a-ae99-ef60f7543a3e | -14.34934 | -51.77459 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86efa1d3-6462-381a-8f74-be0480f0cf6b | -11.60979 | -50.55663 | 2026-08-23 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7a3d4330-3a4e-3181-bfdf-373407b0f727 | -14.96963 | -52.66618 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2aa9199-b9f6-39d4-bc26-8a53da539948 | -13.56068 | -44.09903 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 731cfe0e-5fcd-3261-b72d-9b736ac9dc28 | -10.80787 | -50.96998 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5c9c3a3d-3c13-321e-bcb9-121111773cc5 | -8.96533 | -50.75724 | 2026-08-23 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9600bd52-0e9c-341f-8b38-c8cb242b9447 | -12.23777 | -43.12248 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dc1f1fe5-fc8e-3217-ba8a-2c5827e0e729 | -13.19696 | -51.4281 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52ef5f26-0254-3fba-a055-874142caf5fd | -14.56751 | -49.15907 | 2026-08-23 04:46:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34165f78-c9cc-3ecb-a061-56283c4f5c69 | -12.5632 | -47.93033 | 2026-08-23 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96b12a61-9219-3cd9-be10-479ff5b224f7 | -9.41883 | -51.64363 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6816bb15-900a-3a44-abc7-8aac0eb6c1d3 | -8.19712 | -54.98056 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6109369e-1706-3422-b41b-5c4a71f24458 | -9.42711 | -51.62699 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7780736e-73c5-3fa4-a406-080af6c734f0 | -10.70316 | -47.73577 | 2026-08-23 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a388805a-07ac-3358-accf-58d2121c35ab | -12.23008 | -43.17052 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a99c9c94-12af-3f00-be35-1beac1620890 | -9.02445 | -50.74395 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b110b89-de16-344c-8f54-6d2d5bfbd577 | -9.16714 | -59.45671 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ca704f0-db87-3eb6-8a87-47a2f9640c80 | -10.45651 | -49.96959 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 999f5d9e-1263-355a-9c04-6341d7d75da5 | -7.62263 | -61.6073 | 2026-08-23 04:46:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ea222b2-1fab-34e2-96a3-f48dd0615d33 | -12.73505 | -48.39826 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ff0b40e-6e2f-3b27-9efe-7a52b105ecc2 | -12.73378 | -46.44994 | 2026-08-23 04:46:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd4e2afd-75c5-3fa9-bc6a-0bf3947c8d85 | -13.15179 | -51.42418 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 897ec598-8b1f-32de-b7f1-801045471df1 | -12.72444 | -48.40023 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| af055f3c-9bdb-3276-8a24-d725bf79f5a7 | -12.66795 | -42.29316 | 2026-08-23 04:46:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3bfc7da6-a32e-3830-969a-f59195227ae7 | -10.81661 | -50.95979 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1d95755-e5e2-340b-aafe-4fae1df5bcd2 | -8.89732 | -60.54556 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e71d160c-a61b-3041-9cb2-572e8205f3da | -10.44557 | -50.4701 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b00ab52-8985-3614-b852-26b1888f9b8f | -8.98264 | -50.76025 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 35abde4d-752c-323c-ab05-498f6a3a2878 | -12.84976 | -48.46811 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf627665-8999-346d-ad91-728e096a5412 | -9.17815 | -59.4633 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3a3f44b-2dd6-3b1e-a5cd-0b6ea1c494ae | -15.30633 | -53.79616 | 2026-08-23 04:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b4c85ec-9661-3d39-9b29-2182cc7326dc | -12.59144 | -47.88194 | 2026-08-23 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43bcc907-f98e-36f5-a1ef-95f263e9b50f | -9.23176 | -60.38841 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09821c62-a073-3d77-b5b1-dc3676b673fc | -13.16765 | -51.43472 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56fd1d80-108b-389d-8998-5f30d22a6aaf | -14.35964 | -51.7764 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9cb9430-1215-340a-99f3-e93993af80a8 | -9.43277 | -51.60348 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 113369a5-0f7f-3a54-bd41-0d7dbddf9c8c | -12.75017 | -48.41159 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README33.md)
