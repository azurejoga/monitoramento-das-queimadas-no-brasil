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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 111882f5-75d7-32cf-8ffc-381c4273be62 | -9.02217 | -47.65101 | 2025-08-24 03:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d32406da-07b0-3872-b548-1002bbc9f827 | -10.80693 | -46.41996 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7587d3b-8372-3145-bdc8-b50858bf017b | -6.18509 | -45.43883 | 2025-08-24 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb7c40d6-c0c8-35d5-87c9-69189907ecbd | -6.82329 | -42.82573 | 2025-08-24 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 891acf97-f313-3a52-9ad9-b9449aca4c64 | -6.09583 | -44.69112 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d318ae8-9d45-32b6-8384-40e1f939623f | -6.23148 | -44.13195 | 2025-08-24 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3291204b-0cd2-3ae6-b662-6d5998bacd2b | -5.65773 | -45.14916 | 2025-08-24 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9a935289-2670-3b7c-8adb-e2b5e6853087 | -6.918 | -44.40074 | 2025-08-24 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13eeb48d-b5fa-34b7-ac01-819812b80526 | -6.5847 | -44.56766 | 2025-08-24 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e3eb433-74ae-39d9-9e0e-78206c56da0b | -6.91777 | -43.78391 | 2025-08-24 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbb9fdb9-bf4e-3bc2-a1b6-4c65729f0556 | -7.62636 | -45.23809 | 2025-08-24 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11012a51-7e75-3ada-9bde-a8855fcbe43b | -10.82207 | -46.402 | 2025-08-24 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10e6631d-7843-367f-98f8-44967dfc1dad | -5.6627 | -45.15396 | 2025-08-24 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a069d63a-02ba-37b3-a205-4f45721d347b | -13.13833 | -44.90305 | 2025-08-24 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7da9d96a-6541-3bf4-8ba6-b311feda1047 | -11.7877 | -48.7936 | 2025-08-24 03:45:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24c05142-0f07-336c-93f7-9c94f8ac414c | -11.28126 | -44.977 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39629e9e-81b6-3dd9-b9fa-3a3cca11eaf2 | -13.46615 | -47.0206 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f2733317-5fea-39a6-92a1-d47b456ada7e | -15.0056 | -48.48358 | 2025-08-24 03:45:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d507393d-a003-39f1-90b7-3826ebe058fc | -18.39453 | -46.84749 | 2025-08-24 03:45:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 282bbde2-33fc-391d-a3f7-6adef424f6d9 | -15.96766 | -43.01777 | 2025-08-24 03:45:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3147d9f-f59d-3554-ad57-c4bdaa72c9a8 | -18.39329 | -46.85339 | 2025-08-24 03:45:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5938d156-9320-3ff5-a4c9-0cf8fbfab8ae | -13.62095 | -48.17137 | 2025-08-24 03:45:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60b2df8c-27fe-3013-b567-4c36866e855d | -13.49815 | -47.0343 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7a07a8f-97a1-337a-b067-eb4cf62560ae | -12.72812 | -48.12717 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e653346-deb8-3bfd-9fba-9e2e65643847 | -11.31585 | -47.86034 | 2025-08-24 03:45:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f1b336fd-1e6b-395b-b327-5cec33862f48 | -16.79132 | -51.34919 | 2025-08-24 03:45:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 3a1f7332-5090-39f6-86c0-28b4262ad0b7 | -13.05281 | -45.23942 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a663bf67-28b8-3f9a-a257-5f503ac97465 | -16.78995 | -51.35529 | 2025-08-24 03:45:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 58a85869-5822-3350-bbc1-396a91630a94 | -13.47118 | -46.88669 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23f69698-51d2-3b96-b968-8615e8d951cc | -16.78966 | -51.3618 | 2025-08-24 03:45:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 950514e0-ca2c-3bf7-bdb9-8723b14ddd06 | -13.62183 | -48.16706 | 2025-08-24 03:45:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66ed5f64-dbb7-3570-bfd9-30d14b2ecedd | -13.46291 | -47.01612 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 857db41d-105f-31ee-bb0f-7e290dc1d6d6 | -16.78453 | -51.3532 | 2025-08-24 03:45:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 0f70121e-79ae-322b-875d-b830d6dfa7ac | -13.05051 | -46.32907 | 2025-08-24 03:45:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f29a5fea-fad7-3346-aa2f-2945a08f3a28 | -13.05337 | -45.23646 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72f29641-4da2-3fcd-878b-670a855fe653 | -17.60954 | -44.29934 | 2025-08-24 03:45:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afd2148f-9eaa-35ff-8f2c-6e66293a0352 | -18.70868 | -40.00859 | 2025-08-24 03:45:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| d98d46ab-6de6-39b5-8198-4bf07f916a40 | -12.9929 | -45.22718 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 672ed350-f233-30c9-b646-7daf128c8c80 | -11.32941 | -47.85577 | 2025-08-24 03:45:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0391aead-d071-3097-81dd-3c846fdedc6f | -13.33024 | -43.19564 | 2025-08-24 03:45:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9aee302d-e754-38aa-894f-39662275afa9 | -11.322 | -47.86129 | 2025-08-24 03:45:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f2bd758-9687-31b1-b163-ad47976a4bee | -13.48616 | -46.89805 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e584220f-b02f-378a-90f4-9f4c903054cc | -13.03675 | -45.21473 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d76499e2-1e43-3be8-a634-e1bbe3c9aea1 | -13.12468 | -41.05078 | 2025-08-24 03:45:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 19388a40-584a-32ac-8655-3bcd05055d74 | -15.04373 | -48.52217 | 2025-08-24 03:45:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 175cada6-4d6f-32b7-8c94-db14afb7e28d | -11.13623 | -46.33422 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1629433-9ee3-33cb-8eee-725409cfebb2 | -18.39472 | -46.85295 | 2025-08-24 03:45:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2405668f-5ecf-3b00-bf2d-c1f1735f05d8 | -17.59259 | -46.10593 | 2025-08-24 03:45:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28f1e7fb-039f-33c9-a08c-5e66de04a143 | -15.23889 | -43.85472 | 2025-08-24 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 541e84d6-56ac-3a3a-825f-2fe0429b8df9 | -14.81172 | -47.93643 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4c652354-073e-306f-9913-cb03f466bff7 | -12.72045 | -48.10339 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73db4b07-1bf8-3a08-bb2c-530a3192a2f9 | -13.04893 | -45.2325 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5f1684c-1fb1-39d5-9e3a-811d6b6d90ec | -13.04338 | -45.23444 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb985283-a0b5-3f39-88c7-0500cb71277c | -13.46558 | -46.88598 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f84c183a-9219-3d87-b424-fd7ff014285c | -13.46337 | -44.07306 | 2025-08-24 03:45:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e772cd5a-c043-3d4c-afe9-7eea730363c0 | -18.75471 | -45.09887 | 2025-08-24 03:45:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e851fb6-f503-305f-9281-c0b077a2fe95 | -13.03563 | -45.22062 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24f0edd6-c5b0-386c-85da-810c294e8d7b | -13.04727 | -45.21386 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a8b7c87-2630-36ca-8f70-0349500d2526 | -12.95905 | -46.32834 | 2025-08-24 03:45:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 133df049-fb7f-377a-9382-eb6fb95d8730 | -12.73171 | -48.13634 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fb6ee31-898e-36be-8497-13dcf17adf46 | -14.80613 | -47.93449 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 132e6ab3-9ebc-3059-9a2f-f42b9095859e | -13.04118 | -45.21869 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62f80b75-046a-300a-9d76-858d315b3d02 | -13.48693 | -46.89413 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae5bee94-9c2a-346e-a058-54f0eaa5ab38 | -15.70678 | -41.93058 | 2025-08-24 03:45:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c74d7dcf-eff4-304c-9b2e-8171357710a0 | -11.52272 | -50.49457 | 2025-08-24 03:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 41921d03-6640-3a7e-adf8-ac901910f2b2 | -17.60435 | -44.30291 | 2025-08-24 03:45:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 92.3 |
| e80a925f-a59c-3f67-aee9-53d658e52794 | -15.04489 | -48.51667 | 2025-08-24 03:45:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 803739d9-c446-3a3f-a40e-ebd2742844df | -12.55126 | -45.62891 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45e273a7-760e-3c34-b429-c1124f6289f4 | -13.35444 | -47.50341 | 2025-08-24 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9baff519-af22-383a-ac75-bf7f5da8468e | -17.40181 | -42.62242 | 2025-08-24 03:45:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4debf61d-0842-39f6-8663-42d5129e70dc | -13.03007 | -45.22261 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d67d5e74-fe32-3110-a89b-8831f281059b | -14.80561 | -47.93474 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fe851f22-1708-31c5-9d91-4830c29d1107 | -13.49002 | -46.9077 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16e1a795-aff7-3f49-ba85-1dac6816697f | -13.03451 | -45.22654 | 2025-08-24 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94284615-7fd0-3242-b2fe-97899fcce644 | -18.39651 | -46.84411 | 2025-08-24 03:45:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6567298d-17f2-3d06-98b1-dba842696bf1 | -11.13696 | -46.33048 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47b237c9-9dae-336a-b21b-9bf4faad1fa6 | -12.94941 | -46.29156 | 2025-08-24 03:45:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f3d5121-c54d-3c5f-8e25-bd804ca6ae78 | -16.7925 | -51.34948 | 2025-08-24 03:45:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 9460cac0-0106-3024-b526-ff477bda7a2b | -11.28417 | -44.96112 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 502e8b98-919a-3295-a7f1-952e96c05d25 | -11.13203 | -46.33424 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1959745c-24fb-3cc0-a232-c10e49c00371 | -14.87838 | -47.60401 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 948c0c4e-7e18-36fb-bb04-282ee62f3ea4 | -14.8812 | -47.60435 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f83be19-9990-3400-9f1f-2a1cf6edce7d | -18.60677 | -46.28743 | 2025-08-24 03:45:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e17944a6-66bb-37b3-93e3-4ee1c019a62f | -17.40844 | -48.11636 | 2025-08-24 03:45:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5260cf4e-cd3a-391e-bef6-6b71982377f9 | -12.9488 | -46.29471 | 2025-08-24 03:45:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b695a7ab-7414-3baf-8b54-e3a40437fa0e | -14.81656 | -47.94199 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 033bdb65-2691-3f4a-ab86-0e23bf26ea1a | -18.70592 | -40.0041 | 2025-08-24 03:45:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f9171948-20ea-3310-ab35-98c6a31a3e38 | -13.05191 | -46.32184 | 2025-08-24 03:45:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ced94c5-1033-359d-807c-407517e35d81 | -11.13758 | -46.33537 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a639e614-6ff4-3ba4-a0eb-db1e9eb72ce8 | -14.91557 | -44.85965 | 2025-08-24 03:45:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a44362fe-192e-3ee1-8764-b7a7cb65387d | -13.47601 | -46.89128 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0abbc77f-4650-3c14-b0bf-4b408242eb06 | -17.01352 | -47.95613 | 2025-08-24 03:45:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62015c9a-3856-3eec-befc-a933100c0318 | -12.72841 | -48.12132 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f78a6f8-c0fb-3a95-b0d0-22687c440584 | -11.28183 | -44.97387 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dd438b4-d888-3530-b79d-c32d3fcf5a4d | -16.79908 | -51.35181 | 2025-08-24 03:45:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b30b3aa-6d0e-3dc6-871c-77c9e384ad22 | -15.11092 | -48.65783 | 2025-08-24 03:45:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9ed4fd96-a992-3e56-a548-c67fd1f8b0fa | -14.80225 | -47.92439 | 2025-08-24 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 97213aa2-78a3-33e3-93d7-80dd1dda5bf2 | -12.7266 | -48.10406 | 2025-08-24 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 464bc969-7cbb-378a-b704-8fd69daaa524 | -13.16786 | -46.91681 | 2025-08-24 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b791df4-db23-361c-97ae-76382a168117 | -11.28069 | -44.98011 | 2025-08-24 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README27.md)
