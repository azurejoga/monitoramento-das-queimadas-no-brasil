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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee6db4ab-28ad-37ae-bed3-64621296b526 | -12.98726 | -49.4414 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 661bfb2f-e25e-3584-9a9e-ef1996b89653 | -14.5868 | -48.24915 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d7b7230-041c-3c46-9370-dc198f959ca9 | -17.18424 | -43.38957 | 2025-09-28 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7033185e-894f-3899-8981-af86a40b1d0e | -15.33524 | -47.89451 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 833d9112-bd71-3612-84e1-d166438fdc69 | -13.76716 | -47.8698 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4511503a-2658-35e1-9e1d-1f5ef1c3a01c | -13.26294 | -48.45591 | 2025-09-28 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b580d190-e13d-30b9-9009-d8f1d386fcd1 | -16.58924 | -50.66363 | 2025-09-28 04:27:00 | NOAA-20 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 6cfac6ca-fe99-3569-8c4a-1d10d56c6364 | -18.19026 | -53.32696 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a01f0a8-6d92-3de7-bfba-698564d0839c | -17.18015 | -43.38925 | 2025-09-28 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7727110-ff3f-3f76-bcda-6c04dcb1dcd0 | -15.02647 | -46.97156 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be26bc33-0bdc-34ab-a118-dd6d4597bdc8 | -13.61605 | -48.07421 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 414b0bde-906c-3985-9717-f9e9dd36a1a3 | -19.98831 | -42.34412 | 2025-09-28 04:27:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2dc86e4c-dd7d-39d5-9fd7-7741b861d1a2 | -15.28969 | -49.47911 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90d2aa63-9d9b-3aaa-8860-a2c6d417cecb | -17.72838 | -46.70192 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7543e9f-fb4e-3abb-ba40-e712b9d5b6d6 | -15.19201 | -50.09568 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 91d23167-0415-3029-9613-64048265236a | -13.6331 | -48.09523 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92214f09-49a2-3707-bc7e-90895f03969b | -15.02982 | -46.97211 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 336fdfbf-d7dc-35cd-99eb-96629bf6fe47 | -13.61519 | -47.32219 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97adcfe1-c3c4-3142-b17c-690950689256 | -15.58416 | -42.41026 | 2025-09-28 04:27:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4307dc8-6cab-3619-9d99-464a4e67721b | -14.87831 | -47.97248 | 2025-09-28 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8370a012-09fe-30bb-bf50-af4041ab3db4 | -19.7503 | -50.09904 | 2025-09-28 04:27:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d345bad2-0fd3-30c0-9a47-acf53c9535cb | -15.53282 | -42.3407 | 2025-09-28 04:27:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47780cf2-12ff-3913-810c-d92a719347f4 | -15.20398 | -44.00634 | 2025-09-28 04:27:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4a4fc23-2bfe-363d-bcc3-c667f0c9f6f8 | -13.75056 | -47.88885 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 10da3b14-c365-3f68-af8d-7d7634081dc7 | -15.43779 | -48.21473 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 281aceee-5bcb-3af8-b9a9-84d3df9bc4d1 | -13.6088 | -48.09845 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7b55747-ce80-35a1-b127-c268be87c340 | -13.34503 | -47.29287 | 2025-09-28 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb53ecd1-9acc-36e9-90a0-3c6437bfcf42 | -15.02703 | -47.14704 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09f8f107-3445-38b3-b2a7-66519d12d7b3 | -13.58291 | -47.31319 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 641b42ef-18e8-3b76-9208-d4adcca9f829 | -13.60276 | -47.31663 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0050cc3-7f0c-3691-99b1-b966f00c06bf | -19.49747 | -41.09933 | 2025-09-28 04:27:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 86b86990-f310-3c50-b8c7-ebebbb58980b | -14.49471 | -48.55171 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6490d188-4fcb-392c-917c-0a5900aeda85 | -19.24959 | -44.08508 | 2025-09-28 04:27:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 623fbc4f-e189-330f-a181-2845ca94dc5b | -14.44639 | -46.36705 | 2025-09-28 04:27:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f3974b7-4929-3fd8-bfcc-587cd53849a8 | -15.33192 | -47.89397 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1931d86-cebd-3681-969a-e90d50f43d62 | -14.54152 | -48.40572 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0c48d82-4061-3a62-b298-52e799ea723b | -13.29421 | -50.68571 | 2025-09-28 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cf5091e-0b1f-34b9-b613-5868a01d79d8 | -13.29281 | -50.69394 | 2025-09-28 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8d8de31c-f0ae-34e9-9632-6d7b95f85176 | -13.37524 | -47.92148 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0766d5d8-1cf1-38b6-9b9e-6a72370fafa6 | -15.15211 | -46.41762 | 2025-09-28 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59b329e5-de93-3e1e-a549-543b919a838d | -18.36929 | -47.5467 | 2025-09-28 04:27:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d087a00-a380-3552-ba5b-c5fa976f2956 | -13.80076 | -47.91531 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed9bc46b-5dc9-38eb-abe4-7667171cc56f | -13.58622 | -47.31374 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 053e90a5-bd06-36a0-8547-d72854166386 | -15.43174 | -48.21006 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb6bbf5d-de5d-3f6d-8b04-dbb87e498dae | -15.15147 | -46.42496 | 2025-09-28 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 848a00c9-ffbd-30e5-993a-b0e06808d6fa | -15.01016 | -54.98486 | 2025-09-28 04:27:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbcb5812-ed1e-3c72-ad3b-11442ac31d39 | -12.99005 | -49.44573 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a3f9fe9e-75d6-3b59-b004-01e378d5b8c8 | -13.60801 | -47.3246 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba02df85-0a58-36e4-b783-3548894d715e | -13.63429 | -48.06632 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eadc5946-81d5-35af-be96-adf403e43762 | -15.90079 | -46.2051 | 2025-09-28 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bef285c-1aea-3713-9851-de8873d2a41d | -15.08763 | -48.32516 | 2025-09-28 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aff09ed6-4981-3423-a773-2796f87ebc33 | -14.62453 | -43.8784 | 2025-09-28 04:27:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84565cb6-0cad-3d49-9a93-10e0321070e0 | -15.4649 | -50.22842 | 2025-09-28 04:27:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d2b6d56-ad92-3c7c-8562-69c682f8d88f | -15.22409 | -48.06288 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 760db8fe-79ca-3f00-8b68-cbb36c8eb985 | -18.10519 | -42.19164 | 2025-09-28 04:27:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 816a605c-aae0-3f58-824b-33542f850be6 | -13.58893 | -47.29622 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 718221d0-3edb-37a7-ae1f-67d9351af932 | -13.78699 | -47.89487 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5b34d903-2488-3098-95b9-a5b358b815bc | -15.80987 | -56.42285 | 2025-09-28 04:27:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 99f1b133-2860-3bf4-b4a1-ef62c1616367 | -14.70859 | -49.14474 | 2025-09-28 04:27:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca461822-5cfa-3753-84a1-ae99b3372e08 | -19.64186 | -46.09562 | 2025-09-28 04:27:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96985054-5dfa-3c41-8493-758e7121d525 | -15.08263 | -48.33529 | 2025-09-28 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6ffd843-f3e6-353e-9b8c-ecd48baea7e3 | -15.05559 | -42.33905 | 2025-09-28 04:27:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 196daec2-2f68-39ef-9a60-9132476ae86c | -15.37686 | -48.57802 | 2025-09-28 04:27:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8bc3fc39-0dbd-3c75-9897-1569bd78201f | -13.71229 | -48.34414 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3358908-2d35-3843-b8f8-bf0fa7b6e471 | -13.64147 | -48.06388 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faedee9d-f2fb-3879-9a5a-1f484ebdbc0e | -14.53764 | -48.40873 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e679f41c-f826-3340-a9c4-c3f2751c8931 | -12.65139 | -51.6599 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca157efe-97b8-3741-9947-92f515f26be7 | -14.77737 | -45.64509 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b171ca24-633e-32b7-bc1f-29c64aa386c6 | -13.7985 | -47.92941 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8fff3f0-cc3e-35a9-8953-8b514e696382 | -17.67408 | -48.7846 | 2025-09-28 04:27:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14c0150b-2bee-30e1-982b-f3f2780b2a9b | -15.28237 | -49.48169 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4304fc36-25b7-3587-93a8-e092a42aea41 | -13.76054 | -47.86871 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7919932f-ddf8-3ff7-b2c0-01a958a473f3 | -13.77434 | -47.86736 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7897f24b-1925-34ee-bde3-367f00bbd7a8 | -12.23068 | -60.8511 | 2025-09-28 04:27:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c6fc6b35-45c1-3b32-bc84-67c7ae686b69 | -15.23715 | -42.71542 | 2025-09-28 04:27:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c8e05a9e-0744-324f-8428-20b2dba570ea | -19.7966 | -44.04859 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ed11adb-03d0-3ed2-9a36-c4d36a8c9144 | -15.52856 | -42.34016 | 2025-09-28 04:27:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86d4f124-b1f0-342b-9c8c-430fa3555ad5 | -14.25389 | -44.77753 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3732255e-893c-33e4-b844-0761fce1567f | -13.60221 | -47.32016 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0012152-4ad1-3bb7-bcf1-1cc49cbcd705 | -13.5749 | -44.44145 | 2025-09-28 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89654de7-290e-3d94-97b4-6eb3edf35a4f | -14.81611 | -45.45406 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bae1e445-b117-39c2-a450-950032b06bd2 | -16.23593 | -49.7014 | 2025-09-28 04:27:00 | NOAA-20 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd8971f2-1035-3ce7-9851-ceb81b3f216d | -15.80769 | -56.43372 | 2025-09-28 04:27:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f1ff076-dc5a-3ae8-8158-33140c465cda | -16.9703 | -51.28286 | 2025-09-28 04:27:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d16211e9-82be-36e5-a30c-b7a1aff9a3a5 | -15.28515 | -49.48582 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f054380a-af78-39d3-8297-a84c4a120bdb | -14.77245 | -48.19192 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 22cb978a-8360-3a24-b843-0230a5e00854 | -14.40237 | -42.48696 | 2025-09-28 04:27:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 098e0033-10a4-3b4b-9527-8c07663262e8 | -13.58839 | -47.29974 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d4137f8-d0ee-3244-9b0b-fdb5c2bff96b | -14.57962 | -48.25158 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13a46785-dc41-3f2b-bdc2-5e0b8dd27e5c | -18.19597 | -53.3172 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 98fc1c89-c064-3ee6-9e7e-4baaeb960e86 | -14.77389 | -45.69306 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08b1e81f-74df-31ac-a94c-11f47efc8cc2 | -14.8911 | -45.55965 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8743750d-519e-3b76-bce7-6e800c51a17c | -15.53886 | -47.91659 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eed78132-1fdf-37f8-bba0-d2a95dbac51e | -13.0296 | -49.46025 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 91d9b334-186b-3d3d-b884-402c4359b12a | -13.58511 | -47.32087 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9bc8e16-7766-388e-b85d-27fdfe2bb0c0 | -19.67691 | -43.72397 | 2025-09-28 04:27:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8d3b2ef-9a88-330b-a113-fb5a4c0b0c9d | -13.32736 | -47.31895 | 2025-09-28 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 195a97fc-a5d4-30c0-b25e-7de583d1e25e | -13.75112 | -47.88531 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1773e87c-b68b-31c6-a5bd-f436c5b0bc12 | -15.20985 | -50.15799 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3c4855f5-b64f-314b-8314-554ba1ab2963 | -13.5967 | -47.29009 | 2025-09-28 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README76.md)
