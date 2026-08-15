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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78a37225-f025-39c2-9939-31aed9449ed6 | -9.56831 | -45.37689 | 2026-08-15 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b34e24e-475b-3c49-b4cd-f9c69890f306 | -8.71596 | -49.60246 | 2026-08-15 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71f6ac05-8302-3a23-8d52-a1629fc52ca9 | -6.40211 | -45.71843 | 2026-08-15 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d69ff1c-6d3b-3edc-9820-5d03bb47e1a9 | -12.71869 | -48.42653 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fb39b6a-09fd-3e2b-873f-9ecd5476c479 | -10.76159 | -42.09056 | 2026-08-15 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4c816501-6368-3f9f-8a64-f910c4ae3bf2 | -12.37855 | -46.42478 | 2026-08-15 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10120216-ffe9-3d25-b251-e7b5f631a131 | -9.11412 | -46.39758 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2e20fa4c-0f50-360a-b039-22c5dc6d35c4 | -13.68241 | -46.29824 | 2026-08-15 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f5952f7-0f91-36ac-b919-a1a39774893e | -10.6106 | -46.5695 | 2026-08-15 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd92791f-b199-32ad-ab4f-ba62ff96eb8d | -8.52666 | -45.32383 | 2026-08-15 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf09ccb2-4b4c-3973-80e3-c47271608645 | -6.91067 | -43.63168 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 097b04ba-aa84-3ea3-ae59-87269097b3a5 | -12.01515 | -46.42001 | 2026-08-15 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e30446bc-df12-3838-a259-94e9c30a7a3c | -7.96329 | -46.78488 | 2026-08-15 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 859670b7-c735-3f9c-b9b6-30bcb7fc83e8 | -12.0012 | -46.41378 | 2026-08-15 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c02b6f30-6f69-37b9-a84e-c481b897507e | -11.50297 | -54.64014 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52df83f6-5321-32ea-a231-f57d73afbf04 | -12.73035 | -48.43154 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b50b5e2-8d47-3819-9230-787a96e82823 | -11.58578 | -54.66872 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2a29844-7538-3960-888a-854ffc5b6fe4 | -11.40458 | -46.32442 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afa229b5-ed5f-3bd2-bc30-46ead819dc88 | -7.69293 | -55.16463 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 498d9edf-0b6a-3b7a-82f3-042bb32e85e2 | -7.72267 | -46.2411 | 2026-08-15 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e660c5d-da1a-3110-8d38-c76c0211d340 | -8.76246 | -47.45424 | 2026-08-15 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c62e35a0-707d-35b1-a35b-2ca01baa4f8c | -6.9209 | -43.63332 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 43c903c6-b707-317f-a6c0-ccc498e9d41a | -7.96353 | -46.78783 | 2026-08-15 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9c03aa4-fd2d-3988-9762-dff02e13c677 | -6.93955 | -44.54543 | 2026-08-15 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f1fcad2-278c-3d59-8b88-cca8419e7817 | -12.01145 | -46.41973 | 2026-08-15 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e621d162-47b7-37bd-9788-833f239b2c74 | -6.84141 | -45.36177 | 2026-08-15 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da1b3e1c-ce20-3952-9a4d-f297263f018c | -10.71808 | -50.54501 | 2026-08-15 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6339118f-5ec7-3538-b296-f4ec7da05dbc | -6.53002 | -55.17944 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8aaa85d0-cea4-3004-9170-9dd76a8fcad0 | -11.61808 | -47.7691 | 2026-08-15 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a226d850-617e-3ee0-a6e3-9b8d0eda9530 | -10.40154 | -47.978 | 2026-08-15 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d787548b-ddf3-32b6-ad38-dfafdcdcb9bc | -7.82188 | -44.11326 | 2026-08-15 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bb3f2ee-8f98-310f-b276-68bff56ddb6a | -10.48778 | -50.15989 | 2026-08-15 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a380810f-631a-349d-926c-9b3f821a3ee3 | -6.84594 | -45.3801 | 2026-08-15 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54f423d4-4a26-3afb-b9c5-1b2f0546db51 | -11.08514 | -47.22344 | 2026-08-15 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0199dcf6-7da0-3092-a9db-aa3e71bb22cd | -13.68523 | -46.25967 | 2026-08-15 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe4a6ca6-9103-353b-bcad-ddb46587c2b5 | -7.01347 | -41.43475 | 2026-08-15 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 57fc003f-5a27-37d5-a763-9707888dd8be | -8.75391 | -49.41589 | 2026-08-15 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66cae982-2ca9-3462-add4-364a0944724d | -6.93052 | -43.63867 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ddbc94cd-4e28-3ba5-8c3d-c1c10d90bf6f | -12.01436 | -46.42468 | 2026-08-15 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea350b07-a73b-39f3-bfb5-4a9844fb4806 | -11.49726 | -54.629 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0b70c6a-47b9-3d25-8294-0b567147bddb | -12.70074 | -48.45651 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47b3503d-a3af-3b69-93ef-dcc825edd631 | -7.81499 | -44.11221 | 2026-08-15 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cff4ecb-f207-36ff-9aa0-6f2fbc865414 | -6.83857 | -45.37888 | 2026-08-15 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c636e7fe-84b2-3eb4-9a6b-fd09f4192c15 | -6.54427 | -55.17525 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a4846b4-66ed-33f7-91b3-648bee6eec45 | -7.41119 | -41.92739 | 2026-08-15 04:14:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a0297d20-2e09-37e1-a2e8-98b547c4d55d | -6.92771 | -43.63441 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ba2ebe80-0821-342a-bfc3-89cf694ff997 | -7.45972 | -55.30368 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c8da350e-f9b2-30cd-bebc-ed847ab17196 | -7.2617 | -44.70289 | 2026-08-15 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c4172cc-01c1-31d0-9fdf-90828dcdee89 | -8.80197 | -47.92774 | 2026-08-15 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24d48020-c40d-3a97-9196-2f8031f0871d | -9.11059 | -49.26554 | 2026-08-15 04:14:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 66764a07-8ede-3f8c-87b0-8a3cca97467d | -9.11424 | -46.39561 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0427aa3-a321-39e1-936e-9f5c349d96ea | -10.41445 | -47.97652 | 2026-08-15 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d0f93b3c-1e43-3c89-bd46-f7a047b7cc9a | -9.58107 | -45.36625 | 2026-08-15 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e98d651-28f5-35b5-a089-213faf717074 | -11.40743 | -46.33211 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1cc18d34-7ea1-30a2-bff8-8625fdb01808 | -13.69161 | -46.26519 | 2026-08-15 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2962d099-b76f-3180-961a-44d19be479b9 | -6.8407 | -45.36603 | 2026-08-15 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23f66e47-b771-37f9-8a97-a4cd1ff951a0 | -11.59199 | -54.66989 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4df2af1d-f9da-324b-94d9-5b61e8e1f3be | -8.51882 | -46.52236 | 2026-08-15 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d9ab9a34-f8a0-3c8c-9709-d341409bd209 | -7.24896 | -41.10431 | 2026-08-15 04:14:00 | NOAA-20 | CAMPO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202133 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4da60760-c246-3f5a-8d2b-8f87a2d186d1 | -6.79349 | -55.83223 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ca99d1e-a1b5-39dc-9fdf-4942180ec9c1 | -7.01569 | -41.44219 | 2026-08-15 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 53bb47fa-95c2-31b1-8a02-4e9c3dda08c2 | -6.78947 | -55.85388 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a01a6988-a981-3fc5-9eff-d9bfcd9dfb6c | -6.91749 | -43.63277 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c236fcc7-f8b9-38d3-9465-92062d51b106 | -13.68807 | -46.26452 | 2026-08-15 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37c64d8e-7666-3f0d-b524-2a67cee17e86 | -7.61957 | -44.15065 | 2026-08-15 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b1586fd-7c46-33d6-82d5-ecdd329de3f2 | -6.37062 | -51.74522 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 68da682d-956f-3a06-aa95-69b0fffacd43 | -11.3397 | -46.22222 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 073dfc43-331f-38d6-b565-541a57aca16e | -12.72625 | -48.43105 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19a4299a-7e71-3874-9b4b-4a0d44227d79 | -11.49879 | -54.62873 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e17f62f7-bb16-30db-b185-356d9b766fa5 | -7.7257 | -46.24637 | 2026-08-15 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35ec00da-bb26-33f7-815f-a1f29c9c16fd | -13.55234 | -46.25136 | 2026-08-15 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c848c737-8cb9-34a1-b871-eb7968584016 | -11.39427 | -46.32086 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10b0dbb0-dbea-3981-97a1-63753255b186 | -13.53819 | -46.24865 | 2026-08-15 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ffefc9f1-3ef2-3950-a126-d27b21a1fb55 | -8.12256 | -42.56123 | 2026-08-15 04:14:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a398ab7e-a61b-3c30-ad7e-9d0ae956c9e2 | -11.49681 | -54.63872 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e5e7736-4a7b-3446-901c-bd2dd3a163b6 | -10.76214 | -42.08704 | 2026-08-15 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ce314938-80b2-35f0-a1ff-4fb5d9fb8394 | -9.1248 | -46.40213 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bde5f9d8-93ea-3fb7-bc63-056391dbc936 | -8.4543 | -45.11681 | 2026-08-15 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9128c2a-7b2f-3697-a440-639984ac0b39 | -6.9197 | -43.64074 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3045e48e-7359-323d-a283-09976d48d7e7 | -8.56214 | -45.34127 | 2026-08-15 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3a71341-b1f0-31dc-a1c1-2e76bfbb4051 | -6.92652 | -43.64184 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0e2cb4c2-d8d3-3404-93ff-fd9ea56d3e53 | -12.08435 | -43.179 | 2026-08-15 04:14:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 25a0fe26-1c4e-3d56-aef3-eb86a56f0452 | -10.41314 | -47.98397 | 2026-08-15 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 182f692e-a529-36b4-95c4-0840c5f01e00 | -11.72085 | -47.00877 | 2026-08-15 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e5d8b94-48e7-3ee6-b986-c093bbc1140e | -12.71807 | -48.43003 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3578ac46-6a11-38fc-a339-322cea42a493 | -14.75775 | -40.85575 | 2026-08-15 04:14:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 03e1ee17-5b40-325e-91cc-13b88ff66a82 | -6.53612 | -55.18034 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6db5f204-4aa3-3d5b-b485-dc4d6479981e | -11.50752 | -54.64182 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5789b925-d1a5-33e6-a7ca-4b51f86cbb59 | -14.6241 | -40.85686 | 2026-08-15 04:14:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4c537e10-3372-3526-bf20-059e392da07c | -7.81216 | -44.10791 | 2026-08-15 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1000d4e2-6fac-3472-aea4-2357e4a75b06 | -10.52853 | -44.85409 | 2026-08-15 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5fd8e4d6-b2f1-3d10-b383-a404b3102ce9 | -9.11336 | -46.40218 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e9af42d0-8101-37d1-ae3e-b9cfe06273c0 | -10.4138 | -47.98022 | 2026-08-15 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a43ad96d-af14-342e-ac19-be6e4d57e088 | -12.30355 | -49.34698 | 2026-08-15 04:14:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9293e115-728a-3504-8906-22a030db8858 | -11.67591 | -46.75275 | 2026-08-15 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae18528f-f501-34a7-90de-a9715f01c36a | -8.61035 | -54.67267 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c339be42-d87e-3364-8751-ff8a39fd4171 | -6.64392 | -51.9883 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8f1aad2a-3a21-3711-b881-635b46d0bdf1 | -9.11635 | -46.40761 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c928f073-9873-39b8-ac53-a106d0315eac | -11.40376 | -46.3316 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03d5b13c-3473-3d9d-a385-6178408504b0 | -11.72098 | -47.00628 | 2026-08-15 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README14.md)
