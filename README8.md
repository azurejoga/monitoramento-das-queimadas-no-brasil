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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 399bfb12-6ccc-39fb-a8fa-0c967f714c14 | -13.31989 | -45.36965 | 2025-05-20 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90bdd69c-7388-31f1-b41f-1c5ae838d871 | -13.94427 | -52.55169 | 2025-05-20 04:34:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a6a2d45-11b1-3751-a605-2de5fb1771af | -13.61232 | -55.45592 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11dd3eea-8f06-3cac-b8eb-10d5a0f2ee57 | -14.02024 | -55.13728 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfda24b7-39d3-3ed6-a644-b0677274e7f1 | -14.02776 | -55.11936 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d244faa-9c6c-3af9-9af0-020937ee4b50 | -9.54472 | -47.67334 | 2025-05-20 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7d330ff-8fc2-3833-9988-20f55ec6eb91 | -10.55248 | -55.62228 | 2025-05-20 04:34:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bc91fe5-b9ff-31f4-bea3-209e21a4f59f | -9.77406 | -50.88387 | 2025-05-20 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ca1a698-4c54-3193-8e6c-54081a8d3e87 | -13.90473 | -43.8023 | 2025-05-20 04:34:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e242cee-b639-3d83-bc77-5e894530b804 | -12.98812 | -46.32026 | 2025-05-20 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b887b5c-01a1-3663-8701-139feba845ca | -8.69735 | -49.02705 | 2025-05-20 04:34:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46883e9f-afa1-3c09-b560-5a845a0d90e7 | -11.23373 | -49.49569 | 2025-05-20 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cae431e2-1677-3304-a651-5b6343a5b1b8 | -10.60488 | -46.97755 | 2025-05-20 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b943db3e-6d30-3322-ae4b-d2b04219252b | -9.30185 | -47.52715 | 2025-05-20 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f40615ba-b9c2-3fdf-bb4d-99d74ae987d9 | -12.29013 | -52.47469 | 2025-05-20 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 673daac5-2442-3e42-8d69-204ea350301d | -10.7662 | -54.78221 | 2025-05-20 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f159fbe-45b2-30eb-9433-71df6e364181 | -12.29084 | -52.47045 | 2025-05-20 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fdde666e-fcc9-3639-8bd6-27c8d3d63f66 | -9.04119 | -47.76396 | 2025-05-20 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 816d65f1-2033-3c73-a6dc-45e24a73e26f | -9.20015 | -45.33961 | 2025-05-20 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ff7a626-d57b-3413-bd33-88a43d62f074 | -9.03895 | -47.75644 | 2025-05-20 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 645cdba7-3dcb-3532-ad82-babb92bc5348 | -12.43 | -43.72538 | 2025-05-20 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8b9faacd-fab8-352d-b283-d299042f64d9 | -14.03527 | -55.12458 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 652dafb9-e0f5-382f-9ac8-f096c4223dc5 | -10.58673 | -46.98246 | 2025-05-20 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 482adef1-a560-3e8e-8186-a9c7248e111d | -14.30629 | -57.76355 | 2025-05-20 04:34:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8886c3b5-b340-3a4d-8870-eefe377f0ee8 | -12.83392 | -47.39997 | 2025-05-20 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27a6257e-32fb-3a70-bb94-f9f1af86ae5f | -15.27699 | -43.07746 | 2025-05-20 04:34:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 11.9 |
| bba66694-0347-31af-a550-55ab8a8507ee | -10.34559 | -51.69268 | 2025-05-20 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fd843ae-cf64-34b1-94d6-1fecb3bd4bbc | -14.02054 | -53.02546 | 2025-05-20 04:34:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6310a3d-62cd-3fd0-971a-13bc5a0f3fc6 | -11.66523 | -54.94342 | 2025-05-20 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a82b2710-e2e4-3bbe-9c70-cd36cb141c38 | -14.02823 | -55.12265 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88f5c808-a49d-3a13-8ecf-f406fbcc8ff9 | -9.81127 | -48.03932 | 2025-05-20 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71a7b304-da5e-377f-abd6-d5a950d6a6f5 | -14.82239 | -48.40643 | 2025-05-20 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| baf89a1e-86bf-323c-ba00-0cce88ce6cfa | -13.02393 | -45.07644 | 2025-05-20 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 754ed43f-3c2c-373e-ab24-34024c41a16a | -10.35909 | -47.97131 | 2025-05-20 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28c514ba-95c5-3201-b343-a1e8d2dec3fd | -12.43413 | -43.72595 | 2025-05-20 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bd154252-4b6b-336c-8f41-7fb5c25637aa | -13.02776 | -45.07701 | 2025-05-20 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 99002e44-ec6b-3f53-b304-d73c0a9a186c | -9.01462 | -48.72134 | 2025-05-20 04:34:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98d65959-e9bd-3406-9489-a84efd80a178 | -12.29374 | -52.4753 | 2025-05-20 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f67b76a1-429a-31a5-95e7-c308686babd9 | -11.01083 | -50.75888 | 2025-05-20 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3e70877-9407-3360-93e8-b59bfcc1b9f8 | -11.69897 | -47.78947 | 2025-05-20 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92b1756b-b494-37f2-ba21-a2d4f1841864 | -11.29713 | -53.9775 | 2025-05-20 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 564d6970-84d7-39b9-8cfe-7f9cca3b9e06 | -12.42511 | -54.35489 | 2025-05-20 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47a77b04-1565-3c41-99ea-17680dcf99bb | -11.5163 | -48.58006 | 2025-05-20 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 965e6a48-0137-3101-8355-81e8fd140d4d | -9.95513 | -54.17298 | 2025-05-20 04:34:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec683d1b-98dd-3118-8645-ec5ecdd13104 | -14.65928 | -50.19516 | 2025-05-20 04:34:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a86255ca-061e-3b24-8ab2-131935837c9b | -10.75959 | -57.23328 | 2025-05-20 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 038bde88-e012-3307-8979-fa0f65c7b749 | -9.04504 | -47.76097 | 2025-05-20 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ceec2f9-ae0a-3cd4-964a-736a258ee8ee | -12.30095 | -52.47654 | 2025-05-20 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 556cb721-77ac-33bf-9d75-951094e2b21f | -8.99608 | -49.89013 | 2025-05-20 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e55b349-d88d-3285-bce0-b8fda4499299 | -14.66427 | -50.18504 | 2025-05-20 04:34:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4846f626-823c-3d3e-affc-d45025516ba1 | -9.05141 | -49.52108 | 2025-05-20 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3da032b0-acc5-3cca-b08f-7dfef831a00a | -10.07368 | -55.49217 | 2025-05-20 04:34:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c049a30-196c-34ca-8bd3-603c3e2a29ce | -12.12692 | -54.66679 | 2025-05-20 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 495708d2-44f8-3a6d-a65f-a0590f48f832 | -12.97957 | -51.93436 | 2025-05-20 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| eb94309d-7004-307b-ab3d-45f59d3904cc | -11.42312 | -44.7029 | 2025-05-20 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e038455-51a2-3668-8c88-3147a8f7235e | -14.0215 | -55.1369 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e703ca79-3bbc-3bb2-8b1b-db5b3176e24e | -10.35524 | -47.97429 | 2025-05-20 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a309ac74-02ee-3341-979b-82ca559d3053 | -14.02889 | -55.11894 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e221875-4b8b-31a7-9a7a-2e280937c611 | -9.03737 | -48.94234 | 2025-05-20 04:34:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b40f14d3-b576-338b-a16f-45cd14459083 | -12.13579 | -54.66451 | 2025-05-20 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b532e2c9-cf1f-38c4-a6aa-58fac030d1d4 | -10.76066 | -57.22747 | 2025-05-20 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43240bde-72cc-3f77-945c-7b7b61a6cf67 | -11.29314 | -53.97685 | 2025-05-20 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e0139bb-33dc-339d-a701-74dca32040fc | -11.36463 | -55.1162 | 2025-05-20 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 003d9ba0-ecc4-3220-9b46-fbd0e07df811 | -12.43827 | -43.72652 | 2025-05-20 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6724116-ba29-3b81-beb8-873e4d6c2d2b | -15.89341 | -46.00862 | 2025-05-20 04:34:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fa34bfb-d200-311f-8c94-03f517b18f01 | -15.21282 | -43.8214 | 2025-05-20 04:34:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbd39180-33f3-3388-864b-089a2f2e90de | -13.04079 | -53.72153 | 2025-05-20 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1dbcebfa-2070-31dc-a178-8209f8546adb | -9.04173 | -47.76046 | 2025-05-20 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35c86bdf-d331-33af-913e-e026c2c540e3 | -10.45868 | -46.45254 | 2025-05-20 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95e83345-77ef-3d3a-8701-6bf0d52b33a3 | -12.98515 | -46.31551 | 2025-05-20 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c5d57ce-5ae9-3b15-8b7c-351a69fc11a4 | -12.12823 | -54.65931 | 2025-05-20 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 082725b9-e59a-328d-a33c-3360644e1714 | -13.04924 | -53.71815 | 2025-05-20 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 837ded93-2333-30fd-a602-d7d4eb340754 | -11.00803 | -50.75461 | 2025-05-20 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fe7806f-71c3-30a4-b31a-05c75261133e | -12.29734 | -52.47592 | 2025-05-20 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 67e07dc1-1581-388f-9c44-9e338d911878 | -12.13168 | -54.66377 | 2025-05-20 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| adbe31bd-e968-3326-ae1c-59a70b37e714 | -10.82582 | -56.95574 | 2025-05-20 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39488a7c-d242-3067-afb9-5c7d09e28797 | -12.12888 | -54.65558 | 2025-05-20 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fd1c721-5889-3a59-8a2a-04184cde34ec | -12.28061 | -44.59417 | 2025-05-20 04:34:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 87b0cfd1-42ba-35b3-9628-477b74fa6111 | -11.41476 | -44.7066 | 2025-05-20 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea89ec94-a544-3bb6-8b5b-f3ea20f09154 | -11.51957 | -48.584 | 2025-05-20 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50e1eec8-f7e8-31c9-8cd9-6fd48520d47a | -21.24839 | -49.26703 | 2025-05-20 04:36:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 75750da3-4520-36cd-a4ed-8e9913ac66ef | -19.34319 | -54.1719 | 2025-05-20 04:36:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6cd882e4-8748-3a89-9da1-2a975dd338e3 | -20.22272 | -50.75077 | 2025-05-20 04:36:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5548cfd0-e129-35c0-b690-8184277633e1 | -20.1849 | -55.00671 | 2025-05-20 04:36:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 515f952d-0371-3f87-a7a2-72fe6d7cbec6 | -19.11193 | -52.68968 | 2025-05-20 04:36:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a8ac4cf-7b75-3bff-b75c-1b8e947e9efd | -20.41596 | -43.55185 | 2025-05-20 04:36:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6a288a83-ae18-3f82-bbac-d7c267396047 | -19.45483 | -45.30624 | 2025-05-20 04:36:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4495308-833a-3efb-8556-665d0cfd7590 | -16.22931 | -59.65194 | 2025-05-20 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f61f58ef-36ca-3b27-9594-d38332c50d65 | -17.00982 | -49.78023 | 2025-05-20 04:36:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff0d0eca-acc9-3781-8597-f4ac76002f68 | -16.22998 | -59.64862 | 2025-05-20 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c703d1b6-f227-39a3-ad47-038f015822c4 | -21.21803 | -48.61406 | 2025-05-20 04:36:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| d72a7315-d13c-3885-bee5-b54ccdacc18e | -17.6216 | -50.91637 | 2025-05-20 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b807bd21-74b7-3589-a60a-7026be8a560c | -17.0614 | -45.0278 | 2025-05-20 04:36:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cd064d2-da5d-3e42-8531-abbc2b162478 | -21.24782 | -49.27099 | 2025-05-20 04:36:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6070e353-27fb-3b4e-ab71-28c2e30e5645 | -20.62322 | -55.04244 | 2025-05-20 04:36:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef42683e-a0c8-37fd-95f1-61d537090d67 | -17.50459 | -46.73903 | 2025-05-20 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 51c5e53c-051e-3a56-b84e-fc74ae99bcf7 | -21.21861 | -48.60991 | 2025-05-20 04:36:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 423f0231-74e3-3403-83a9-37cfccf98bfd | -21.78508 | -52.73734 | 2025-05-20 04:36:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c41ba5d-1fd9-376e-87b9-13fccb53be6b | -17.50828 | -46.73959 | 2025-05-20 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7449109b-458a-3bc1-82b2-d9362c718a51 | -20.95915 | -56.60748 | 2025-05-20 04:36:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README9.md)
