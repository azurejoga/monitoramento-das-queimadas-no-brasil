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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7692898e-7130-3b77-a630-9c1f1c4446a5 | -13.38945 | -42.39466 | 2026-06-20 04:10:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6e78a038-a362-394e-8f01-ef441820009c | -12.66202 | -47.67906 | 2026-06-20 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b9c34ce0-e1fd-3faf-8a6e-0608d8b3fc30 | -12.55038 | -45.02299 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5dc8a199-7c19-3051-838f-e26266fa83b2 | -14.90985 | -51.9976 | 2026-06-20 04:10:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8ac0f6a-0475-32a8-9f0e-ec7dc5f77e95 | -17.45128 | -47.16075 | 2026-06-20 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d37bdf69-5c92-3f97-93e2-1eb0ed277534 | -17.60504 | -44.61202 | 2026-06-20 04:10:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a13033b-9812-38b9-ac72-ebe577a15fce | -12.79082 | -44.47799 | 2026-06-20 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9597418-0293-39e6-97a5-ae03dafa9fa3 | -12.79359 | -44.48225 | 2026-06-20 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec111e14-4eb7-3ccb-8bde-724315a30f43 | -12.7954 | -44.47117 | 2026-06-20 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 357f2f9b-2cf7-3993-ad82-8e3c74ac5d64 | -12.91516 | -49.48094 | 2026-06-20 04:10:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd08b6ca-4357-350d-b16c-526415b0a931 | -17.69413 | -40.1606 | 2026-06-20 04:10:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c1604822-6331-3b27-8d7f-41559d54d5d1 | -13.2991 | -45.21824 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa4aacce-7b14-3dfa-9db9-7f26bec19d56 | -13.12584 | -53.79204 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d8bb143d-9b3b-3b40-a423-7e868115b071 | -14.86046 | -48.1075 | 2026-06-20 04:10:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 815728a6-470d-3871-a25a-d8a475596cf5 | -12.78165 | -44.49165 | 2026-06-20 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8913bdf-21f8-317e-a3aa-d9f24136c0d8 | -13.38723 | -42.38704 | 2026-06-20 04:10:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| fe42e947-3b17-396d-b5c6-9cfad6cf6d68 | -12.79202 | -44.4706 | 2026-06-20 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95acddbe-251f-3d4b-98fc-dc99520c6780 | -12.3173 | -46.73771 | 2026-06-20 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ae2eecf-1b1c-34ce-9885-6d2ccc270048 | -13.12671 | -53.7877 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3376fd10-4a56-3948-a4ed-008fb64ccafd | -12.52269 | -48.29722 | 2026-06-20 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20093080-440a-38f3-abec-8b12d55bd4b5 | -14.91436 | -51.99655 | 2026-06-20 04:10:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57e37080-34b0-3af7-b520-8b9d1e3e8408 | -12.31355 | -46.73706 | 2026-06-20 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdc48604-1029-3a68-bb70-547069179a52 | -13.29756 | -45.22208 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98df0936-d3f2-3d79-b323-2651494398ac | -12.5482 | -45.01467 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 39de28eb-fb9d-3290-a5e5-1f2639c6922a | -12.86384 | -44.36914 | 2026-06-20 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 572e46a6-2d5a-3a72-9d0d-99a54688a4e6 | -12.51858 | -48.29644 | 2026-06-20 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9074b045-94cd-34ac-81a5-4a98d4719180 | -15.64666 | -42.0342 | 2026-06-20 04:10:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 075a4745-15f3-39c6-b8d3-3cabd4d0d719 | -13.13339 | -53.7845 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c8fbf683-f66d-3722-afa3-38903d1dab7c | -13.28939 | -45.21262 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b56714f-f98d-3ed3-bd24-5e32c75af615 | -13.29438 | -45.22543 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 837e604c-c168-357f-84cf-f4760dc92385 | -14.91375 | -51.99961 | 2026-06-20 04:10:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e466adb-b33a-3e13-8397-500123b10523 | -13.13922 | -53.78559 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dbf7dff1-e552-3c18-abc8-516240405ba3 | -12.55163 | -45.01527 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a19ea795-ed0c-39c0-9c7d-c451ce12740c | -13.38614 | -42.39413 | 2026-06-20 04:10:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 74cbcadc-0b31-35f1-9ae3-c9ac75b891c3 | -13.11913 | -53.79535 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc637024-3de3-31c5-9341-7f750ca726df | -12.13206 | -45.00267 | 2026-06-20 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dab61275-d3b3-3e80-870b-2c83806fd073 | -13.29784 | -45.226 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edfb2023-e8f5-3d2b-9ed5-e50e0c5f97a2 | -13.12497 | -53.7964 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 889412b7-3f8a-33ba-a16c-5495699ac299 | -11.44778 | -47.39965 | 2026-06-20 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b59359c6-4d62-37e6-bab5-a875daf4fa09 | -11.89011 | -43.83553 | 2026-06-20 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| de01c64c-cbc3-36d3-a173-427e064eabc4 | -12.55101 | -45.01913 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8511b5ab-4531-3cca-bb1c-4bbbba52f87e | -11.45163 | -47.40092 | 2026-06-20 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 188e7290-1e44-3472-a0c5-d21d56661cf5 | -13.38999 | -42.39112 | 2026-06-20 04:10:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 06f6d291-2d30-3dd0-8323-f20e8ce381cc | -13.29821 | -45.2182 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af2c5bb5-e0a7-349b-a120-404bd079b521 | -13.19511 | -50.34429 | 2026-06-20 04:10:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 10fb6a86-d073-34d0-bd8a-cb528813305e | -12.5435 | -45.02179 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| ceb2a395-3280-3326-b347-8c62a07e9d68 | -13.13319 | -53.78329 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 82d7966d-8ac0-3851-8757-8ed5ff402fe3 | -13.29502 | -45.22155 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17a75f86-ddd6-35ff-b826-b232c7179479 | -13.83585 | -44.77465 | 2026-06-20 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7553776-dbca-3d98-b8c3-14746eec469e | -13.13902 | -53.78437 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4ebc8837-1990-3e2d-882e-1c3b2a581aef | -12.78961 | -44.48538 | 2026-06-20 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce0321a8-26d9-3863-9d92-ef018ba90577 | -14.06198 | -44.47902 | 2026-06-20 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 652d0d86-6788-34ca-984b-0e852a046e37 | -12.91877 | -49.48617 | 2026-06-20 04:10:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 701cd82f-b980-3f3c-87f5-7bf4a9712097 | -12.54631 | -45.02625 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 146c1fd0-e395-3578-ad75-27775228b196 | -13.20536 | -50.34092 | 2026-06-20 04:10:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0a77a001-f4ed-3ef8-9d37-ab255f98d000 | -13.29002 | -45.20874 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3788c971-7583-36ca-99c1-4a652c7fb64b | -17.44771 | -47.16005 | 2026-06-20 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27beabb9-cab4-3eeb-9edf-3091ff5c4263 | -13.30166 | -45.21877 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 481ffe4f-499c-3533-b1b9-9fad2fbfc5a0 | -13.13231 | -53.78753 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20b90993-d309-3208-a1b3-7f4d46afb8fa | -13.29347 | -45.20932 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ebcfe03-1f07-3712-aec6-2f77a0fb1bf5 | -17.35035 | -42.62749 | 2026-06-20 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ddb55c92-e2b2-3b3c-8359-af9446772c28 | -13.12173 | -53.78231 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4aed5eab-8c58-3e8b-b057-c19195e09014 | -12.66242 | -47.68226 | 2026-06-20 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee01e6a0-9579-39a7-868c-ccb060347b8b | -13.29847 | -45.22212 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aef82194-c6ff-3b70-b34e-58b1d3aa49aa | -11.66529 | -56.7639 | 2026-06-20 04:10:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d0bc8092-dc6d-3b11-bb7a-a281af254f6d | -11.22253 | -46.76509 | 2026-06-20 04:10:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 493c7bdd-2463-3f64-b87f-f015ec9eeb03 | -11.81686 | -47.34287 | 2026-06-20 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acae34c9-3f09-3416-b0b7-b03d764ada5d | -13.56146 | -44.68657 | 2026-06-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57c3ac91-16ab-3ba4-8b5e-945b68bdbf44 | -13.38283 | -42.39359 | 2026-06-20 04:10:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| aee750d6-3bd5-3953-9941-159ac935818c | -12.54694 | -45.02239 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 5146e4ca-e4fa-3956-9104-fbcbc9631f0a | -12.55508 | -45.01587 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8180c4d4-b252-3809-a2a5-55f3072531f9 | -14.85777 | -48.12285 | 2026-06-20 04:10:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68f9750b-716e-3a52-8081-d307e50d86d3 | -12.54132 | -45.01348 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| db8c0233-58ef-3057-a659-c4787e492116 | -11.89069 | -43.83192 | 2026-06-20 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 882a5095-b624-3af9-a78c-eed750dcffe5 | -17.45636 | -47.15282 | 2026-06-20 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65d8367a-7df8-3673-8594-e928026c7419 | -12.54287 | -45.02565 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 25ce57d7-0a66-3d60-902e-99a3794d91f9 | -12.91958 | -49.48173 | 2026-06-20 04:10:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b1377e4-7433-3ca3-8719-d1e9bd3048ec | -11.89403 | -43.83247 | 2026-06-20 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 014185ae-7ca3-3671-b6ca-d0b3259af4a5 | -13.38668 | -42.39059 | 2026-06-20 04:10:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| db1585c4-592b-3c0c-aa42-f1e1fe4ec073 | -13.29284 | -45.2132 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cedb949f-5fcc-3669-8466-b9d6c97ac380 | -14.85867 | -48.11769 | 2026-06-20 04:10:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d56dada0-4e34-3ad2-aaf5-666be2e50b7d | -13.29628 | -45.21378 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27dd751f-6724-39a5-8504-c5eeb1bf943d | -13.2922 | -45.21709 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bef91b33-254c-31cd-a5b0-dbded2f49dcd | -13.12756 | -53.78339 | 2026-06-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99efa8ac-57d4-36c5-90da-24b75343c9f1 | -13.29886 | -45.21432 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6d9f925-4011-3558-90de-8f22dd94820d | -13.29692 | -45.20989 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ad6896b-f40c-36d0-9150-48b6209b352f | -15.81546 | -41.89661 | 2026-06-20 04:10:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f388107-6ae3-3d1d-a479-6a91489a7501 | -11.63221 | -47.87907 | 2026-06-20 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2ce8b0b-0fa6-38d1-8ee2-8f83dbf10425 | -12.54757 | -45.01853 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f103f204-64b0-305a-9193-f56bebfb521a | -12.54412 | -45.01793 | 2026-06-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8a160118-f930-399a-81ad-09cdcf717883 | -13.29565 | -45.21767 | 2026-06-20 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1b8a54e-4f31-3f7b-acef-c0dbcbad2472 | -12.79238 | -44.48965 | 2026-06-20 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e6777cd-4c71-3209-b1f2-d915d7cbbf09 | -13.19976 | -50.34513 | 2026-06-20 04:10:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 619400d5-9289-345e-a5d9-d35abb6234ca | -17.3509 | -42.62378 | 2026-06-20 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 06cca728-ebaa-3680-98b1-25c3f58b2b63 | -13.38338 | -42.39005 | 2026-06-20 04:10:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| a1f56b34-5359-30b3-bb20-d2e5f0b69ecc | -12.13739 | -48.26673 | 2026-06-20 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f519dc29-7a5c-32d0-9d6d-490045c3e38a | -13.20441 | -50.346 | 2026-06-20 04:10:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e0dcd02b-d37b-3db8-85bb-69c991a86ff1 | -12.66331 | -47.67704 | 2026-06-20 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b72b1943-0388-30c8-b01a-ae8fef515dd5 | -12.78226 | -44.48795 | 2026-06-20 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3350c737-d976-3961-8b58-f6d0b19adf4e | -14.86431 | -48.10853 | 2026-06-20 04:10:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README6.md)
