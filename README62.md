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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3353d2c4-7b3b-305a-bf60-8099a6baf056 | -13.42952 | -47.97894 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d45191e5-2b5b-327a-8202-9b03376e1e9d | -14.91789 | -46.72309 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 037f2c9c-21c1-3b40-9d49-ef4731dd69e2 | -16.34677 | -46.40901 | 2025-10-18 04:32:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 746c890b-a6fe-36ac-99b4-f1f4b8e56d04 | -18.09589 | -42.44804 | 2025-10-18 04:32:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5bcef084-4e92-3bd5-a680-6b39138a2e35 | -12.68657 | -45.47636 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c282cd37-11b3-3a12-bb0b-31ff480bc779 | -10.75467 | -47.88676 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c23b9b2d-6196-314d-b175-cce0cc110e8d | -10.97564 | -47.92258 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae1f3b8b-fa20-3a6c-a244-5f3c976c4b92 | -17.5014 | -43.46363 | 2025-10-18 04:32:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a18a39df-ec1d-3ff5-a1d8-bbc9bec8da2c | -11.57346 | -44.66247 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6716610-3d4f-389e-81c5-9db0b0dd86bf | -11.3682 | -44.2827 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ca8d431-e7b3-3d27-8761-41a8667d9793 | -18.40417 | -41.82959 | 2025-10-18 04:32:00 | NPP-375D | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 076d40b4-c5d9-320d-a86d-a9d318eacaeb | -11.11343 | -47.44282 | 2025-10-18 04:32:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0ac3cf7e-ef5f-3ee9-a73c-f9e375c3c7be | -11.19976 | -47.83271 | 2025-10-18 04:32:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d0417111-24f9-3c30-b7d4-ccf81264754f | -12.53562 | -48.70999 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 702a55c8-7adf-3520-b369-42e9e5fb2e5d | -16.58731 | -45.67788 | 2025-10-18 04:32:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ba3064f-39f2-3eb0-9b30-b3e30d7c7b74 | -13.77148 | -48.2325 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e007202-8bf4-3e51-850f-46ed4a80e036 | -12.79016 | -48.63298 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 158a0b84-678d-3211-a5ac-d02ab8508f49 | -11.35224 | -47.27971 | 2025-10-18 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8ead51e-351f-3638-a60a-3e45b3c6223c | -11.47864 | -44.01157 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f13c6a78-0e0a-33e6-9366-450f87f76337 | -12.17517 | -45.07074 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78d3a567-bdfd-3337-9903-d6ab2b5b22fd | -10.97785 | -47.93017 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc2f6ed0-7f72-356a-b4c5-e58fe34df61c | -14.92229 | -46.71603 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7160ad1a-f1ce-3564-bd1a-b96fbf4eb560 | -11.36945 | -44.27424 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a7238bc-06c3-3f9f-9827-774b61a702eb | -10.94092 | -47.57015 | 2025-10-18 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f28d61e2-2607-3e9f-8f9b-aa325cff2bca | -14.73855 | -47.42056 | 2025-10-18 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d31d5fef-7eb2-318c-af77-394958ba211e | -11.49006 | -44.16416 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c5f5d03-82bc-33f5-b6cf-314125b51fc5 | -13.41986 | -43.75259 | 2025-10-18 04:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2518aa01-2293-3cd3-8dc6-7f6b4de469a5 | -13.68934 | -47.72339 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72eb1845-cee9-3d2d-8de2-d9cb345d05de | -11.20421 | -47.8262 | 2025-10-18 04:32:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 44dd0f35-7ccb-33fd-9b30-a3ce377e7c12 | -13.44789 | -47.92736 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec02ad48-6185-33ba-bdf2-a0c98b2b64a5 | -15.58595 | -44.51321 | 2025-10-18 04:32:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b86b72b7-1703-3e1a-91be-5f0e8e5783ff | -16.53289 | -43.67885 | 2025-10-18 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bfdf4bd-b70f-3ad4-b685-e4014dc3a8dd | -11.35889 | -47.30244 | 2025-10-18 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79c33855-72a4-3d03-8ad3-89cf15c87af0 | -13.48445 | -47.95526 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5f40b1b-081e-3e87-bdc6-f475017045d4 | -10.91963 | -47.98264 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 565b4e78-31c1-3b2d-96b8-68721e754fa3 | -13.41299 | -48.59699 | 2025-10-18 04:32:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bcb82ee-0161-3e81-ad4e-eb43c13aa86a | -14.92243 | -46.71617 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 487e524b-8410-32ba-ae84-fe8775c49283 | -17.98628 | -47.8833 | 2025-10-18 04:32:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac5b38cf-f281-30a9-959e-c7660f595361 | -13.02661 | -47.27229 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c968492-d407-3016-be06-147019736e46 | -12.99409 | -47.293 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76199c1b-f85e-334b-9170-8157bc282430 | -13.5334 | -48.00383 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8ad9b3b-6eeb-3993-9218-b5e31b2e8ea5 | -13.04206 | -46.96341 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 528bce08-c1b7-328a-9ed2-c56ad5a4ab31 | -11.35556 | -47.3019 | 2025-10-18 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e81eb544-d2fc-3fb6-96fc-fc9de61104a0 | -12.17456 | -45.07485 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28f6a1f4-1362-330f-823e-e5677361600b | -11.40764 | -44.26967 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc22b23b-a776-366e-ba91-efc9d819c2f3 | -11.56989 | -44.66192 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e081eaca-2c93-311a-b230-cf5d89b581c7 | -13.45949 | -43.76547 | 2025-10-18 04:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b1e8af4-8447-3266-bddf-b9ddccbe0347 | -13.21282 | -47.85639 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d580b45-1c21-355c-83de-a0ce6eae66dd | -11.67956 | -43.90195 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04f58549-ef39-3e4a-ac99-197dedbf20c1 | -14.92286 | -46.71222 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d185bdb4-d2da-3785-aff9-259f0ab1ebe9 | -12.31251 | -47.83644 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 666cca87-668a-3928-8fde-fef581a136d3 | -13.51153 | -47.99978 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aea19e11-660d-337d-b852-d220991e0517 | -12.92132 | -48.57759 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3d55bc2-4f40-3345-a9e1-f3fd4d845bb4 | -11.35131 | -44.2715 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| acc796df-98f4-3b55-b39a-c4c8b9922f54 | -14.06593 | -50.0478 | 2025-10-18 04:32:00 | NPP-375D | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c00c7c5a-f172-3589-94a1-eaa16aec5b68 | -11.38223 | -44.26316 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e69bc295-813c-3c29-8400-77bc596b7af9 | -17.49731 | -43.46289 | 2025-10-18 04:32:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f1373d9-15ae-3ada-8c26-d08b4acf5144 | -13.44917 | -48.11331 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2179e82-c8e5-3bc6-940c-b5b8c9852099 | -15.05415 | -48.73819 | 2025-10-18 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08e20ac9-ac90-3f2c-8dfc-0e6ffe7458d7 | -10.47911 | -49.36992 | 2025-10-18 04:32:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f21bf0e1-27e2-34e4-a275-3351d13dd742 | -11.50665 | -44.05154 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3ac659a-dfa4-3386-a424-ef43f259779d | -11.1092 | -47.65853 | 2025-10-18 04:32:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60b39f9d-7b65-3507-93ff-181c7281d429 | -14.75966 | -48.19652 | 2025-10-18 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6e900cb-f425-3d76-b3bf-94bc8d7be342 | -15.55759 | -42.34283 | 2025-10-18 04:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ba1e458-455f-3bb8-b49b-ed740e53249f | -11.35017 | -44.25398 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efccb824-bd86-38a8-9ad8-2ccca4d1fb3e | -13.13041 | -48.03192 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03bfff2a-6c2f-3d3b-bcda-b6667defa6fb | -12.46134 | -45.46678 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46bfc5ab-93ed-39b8-b028-d29272193e53 | -13.43894 | -47.98413 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f44f967-1b64-3343-9948-b2405b5424b0 | -17.49778 | -43.45927 | 2025-10-18 04:32:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1114e674-cd47-346c-a08b-bc00b4dc2a9d | -12.1534 | -45.07165 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a4e2edb-b1fc-3660-a953-c041abec2045 | -13.70765 | -47.71545 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66d9799e-e1ae-32c4-810a-54f4f42ee5ad | -12.1581 | -45.08878 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 164dd60b-8323-3603-821c-7164f61e7b75 | -12.36493 | -47.17741 | 2025-10-18 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbd7498f-ffb6-355c-9b69-41c04c292388 | -11.50213 | -44.18356 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3030afbe-4912-377a-ba28-b7cc786373a2 | -11.48517 | -44.27272 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32cd25f2-4a72-30c9-9dc2-781ebf15b746 | -11.37255 | -45.26717 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9d974f7-bd21-3adb-8e40-c27984541fee | -14.26423 | -51.86354 | 2025-10-18 04:32:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5415d45c-76cd-347b-b97b-1bc7468c792d | -10.93162 | -47.84312 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce44873b-21a5-3664-9c20-1c67e2929f76 | -18.43126 | -43.72959 | 2025-10-18 04:32:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d31d552-4915-34d7-a106-2da1f02d7b55 | -11.47496 | -44.01102 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bde643c-d757-351e-9925-d626168480de | -13.0376 | -46.94795 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d220b5e3-7f41-3266-b3e6-872777953453 | -14.92568 | -46.71661 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5327d360-c106-36f0-9920-ddec04e9b58b | -12.52346 | -46.77444 | 2025-10-18 04:32:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16b0446e-453d-3ed5-9cbb-08e414fe0a19 | -14.74859 | -48.18007 | 2025-10-18 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ce3f998-eae5-3b4c-a958-964542de514d | -11.58765 | -44.05257 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9ea4dd82-e7ed-340f-a03d-0f7b01286b5c | -10.91416 | -47.6741 | 2025-10-18 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20ad76d1-340c-348b-8a80-dc5127b806de | -13.43837 | -47.98769 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41975c4b-416f-3072-b2b2-d25f00146aa9 | -12.17104 | -45.07431 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9235c76-a524-3601-bfb1-500bdd128461 | -18.77177 | -44.46208 | 2025-10-18 04:32:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 547305be-86c9-38d7-b252-3f16a2228571 | -13.52372 | -48.00908 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1a6b96f-8133-315f-836b-5ba5d4088612 | -13.07704 | -43.0589 | 2025-10-18 04:32:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 4fc951f7-54f7-3f69-8480-e0a86b40f5f3 | -14.70998 | -48.31641 | 2025-10-18 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d31abbee-80ae-38c0-b89f-559eed7bebe0 | -13.07915 | -43.06067 | 2025-10-18 04:32:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 872617ba-e2eb-34bb-902f-f35469eb8c14 | -10.9315 | -47.56503 | 2025-10-18 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35336f43-0891-32a4-9891-da6180d4e78e | -11.20642 | -47.8338 | 2025-10-18 04:32:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 32ab5265-3078-3a5f-b590-1776fdaea317 | -13.03605 | -47.27759 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 67ef16e5-5afd-38e4-99eb-d20b7f86dfbf | -11.36394 | -44.28639 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54cc5ee0-2deb-30c4-bff5-539df5aa466b | -13.51706 | -48.00798 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4698fce7-5187-3e2c-bf17-e2e1bd39494c | -15.05849 | -46.61454 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7437ae0-c051-376e-bd51-bb6917e6824b | -12.49548 | -45.49994 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README63.md)
