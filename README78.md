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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a19a6c3b-a465-3dfd-b062-542bf83a3be3 | -18.02658 | -44.94796 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ff0bcacf-e551-3ace-b5c6-4ca861053741 | -18.55417 | -41.57904 | 2025-10-08 04:40:00 | NOAA-20 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1baa40a6-ebe7-3f74-825d-a44c4ca884b5 | -11.68434 | -50.9598 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| df845c6e-cae7-382f-b06a-4bf1822b819d | -14.62689 | -52.48027 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 594ff966-cbd1-3f1e-a41d-d4842815eed1 | -11.73636 | -50.93219 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| c92574e2-c1e1-3a5d-a61a-3427185edacc | -13.25587 | -48.04806 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e71de488-6ddf-3636-bb64-ded6577261b0 | -12.19319 | -47.78621 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e0c07f0-7c51-3ef3-a003-413ae3eb291b | -13.25657 | -47.79133 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15bb86b9-3dcd-33b0-9d1a-77df878c5125 | -18.18478 | -46.21314 | 2025-10-08 04:40:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79ffd0b9-9d16-3693-8929-778cd226dc44 | -13.00063 | -46.78651 | 2025-10-08 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 3d5b9b4e-4278-3327-b8c5-379296a0493f | -14.80059 | -41.633 | 2025-10-08 04:40:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7e29a4ef-8a30-3188-bbbd-2670bb9934e7 | -13.35706 | -47.55484 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7d8159b-6e58-361b-9841-4bbdf6c7b638 | -15.39706 | -48.00095 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3589bcd4-9688-3cad-80a1-e47ed9c50998 | -12.94505 | -46.85429 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89e7b11e-9897-3e18-941b-d3ff171c18f4 | -12.51775 | -54.72438 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee1aec77-bd98-3e2b-8c0d-a696e4dea783 | -13.22487 | -47.17278 | 2025-10-08 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9d337d12-1f4a-36f5-991c-f2da55783c0d | -13.79632 | -45.80342 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| acdd00f2-cdb4-376d-806a-e2e16c9e8134 | -12.63772 | -50.55926 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a92bf968-bc90-340d-9480-adfcd627308f | -12.78294 | -50.4999 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4890b157-4e17-3c5d-9d73-58de6d87668b | -17.55857 | -46.06733 | 2025-10-08 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3916a801-24fc-387f-8432-ae3496c6f8f0 | -10.87004 | -53.74102 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3ea417c1-6a42-3d5b-871d-32f9d8c58ebc | -11.38051 | -54.35543 | 2025-10-08 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd06e797-f091-3b7c-9748-924b859d7290 | -15.40195 | -47.99257 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c480d300-9937-3a0c-a9a4-628bfef57c20 | -12.29401 | -55.10341 | 2025-10-08 04:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9e61c85-dfd1-3d94-afd0-00076e845140 | -13.35998 | -47.5603 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5df942cd-0ca1-363e-be2f-d3332752e603 | -14.61743 | -52.47481 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 88a50a9d-0c07-38d8-8f3b-a39fef09eb63 | -17.38155 | -45.05757 | 2025-10-08 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fdb89a34-6e53-35aa-aa53-6b2cb0848192 | -11.81536 | -49.51657 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2310f520-04f3-3131-b01a-9774fda915c3 | -11.16824 | -54.86351 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 79d43030-6136-386c-86e0-1b5712b48d01 | -13.31324 | -48.02785 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 49650b81-a6c1-3c4e-8829-4d5ccb7d78bd | -15.64297 | -52.5697 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3840dbe5-5465-3ed2-9b72-7995d993a655 | -17.5544 | -46.06657 | 2025-10-08 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90ca6d22-8a5a-3512-8441-0c3fcdacc1c9 | -11.29645 | -54.88886 | 2025-10-08 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71a64923-77b5-32a9-8bba-b15776e73169 | -14.69639 | -46.0149 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1be07522-b126-32cb-9f94-af42cbd28996 | -13.79177 | -45.8066 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44c3aef6-e4b8-3b4d-a349-16cde6261929 | -11.71468 | -50.98285 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ca06bc1-1543-36de-b7ba-1aded6878d15 | -17.16457 | -56.60659 | 2025-10-08 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5fed6d98-9710-3eb6-b18d-8426e256c657 | -12.91149 | -46.84327 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 907adf8f-c542-3e27-a0a3-9c88ef049b41 | -18.17348 | -50.39403 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 668ec00f-24b7-3ac5-8ac8-4fe3f94ba70f | -13.20781 | -51.6516 | 2025-10-08 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6ce81661-6bd8-3a60-94df-5c9b17e83d2f | -13.7488 | -45.75668 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02b6081c-c09a-30da-bdf7-879bf50bd7c2 | -13.74808 | -48.65035 | 2025-10-08 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be8d29fe-0e73-347e-92e8-cb5a659c2e9a | -18.49651 | -42.9016 | 2025-10-08 04:40:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3e25882c-1f06-3bb2-8dd1-06d63e2b36f3 | -19.57632 | -44.65073 | 2025-10-08 04:40:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74f53d33-d707-3763-ba75-579a90fc81d4 | -12.42349 | -45.62523 | 2025-10-08 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d8c6925-09ef-30ca-9129-8a5a3c53ce15 | -19.57921 | -44.6557 | 2025-10-08 04:40:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f24aa30c-d4b9-3206-9796-00bd299ba060 | -13.80492 | -45.80093 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99fa4d14-0ee7-375d-b790-f49fe79d04d8 | -13.25722 | -47.78681 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35511a01-0220-3f6c-a06a-01743cc39d2d | -19.51048 | -44.07525 | 2025-10-08 04:40:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ed358262-44f5-3b6c-af3e-f39a21872fac | -11.6849 | -50.95628 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 9305fd81-7242-3a77-ac33-8331c597a3b2 | -15.63687 | -52.56491 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48fd283f-2fe5-3359-9df5-f8ce7c791bd1 | -11.87467 | -45.74871 | 2025-10-08 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4089624b-7685-3c57-9d38-26761e0940ed | -13.23598 | -47.79407 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26637e3b-e79c-3cd7-9092-e2b535658ef6 | -13.22697 | -47.19384 | 2025-10-08 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9741dd09-4de6-3831-a223-33ebcc4da450 | -14.90157 | -46.85416 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9be277f3-c46a-3c87-9b50-ecf11d1d0f26 | -12.32372 | -50.26645 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f45ac093-ff20-3812-9b49-daf176266b9d | -15.63508 | -52.5759 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48974871-743d-3368-a54e-d25723f52039 | -12.16042 | -51.44519 | 2025-10-08 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4059b0a6-d875-34f1-a56f-daa4e539d4fa | -12.15709 | -51.44464 | 2025-10-08 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83d82baf-c82c-3617-b395-1d2d9fc33913 | -14.3653 | -47.73005 | 2025-10-08 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2911f4fc-ebe7-3825-85d6-a05df8eb6cea | -11.87071 | -45.74816 | 2025-10-08 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed34eb31-d111-3276-b1ec-50eb505e4251 | -18.17406 | -50.39021 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eda40a50-c1d8-39e0-badf-8c15a373895b | -13.07084 | -47.93181 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6a5e352-b5c8-3675-9e62-53483ef72f06 | -14.92324 | -46.79445 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9b98b5d-f5b6-3431-b06e-6f833c2d881b | -11.26446 | -52.45869 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c098a143-a58d-3a29-9c98-605afdf00672 | -13.08498 | -47.93444 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17da92bd-dd0d-376e-ad57-f1b625a3f48b | -18.02715 | -51.15255 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4cdfd543-af31-3a59-bdfd-fadbf3df20f5 | -18.40922 | -45.21017 | 2025-10-08 04:40:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 57a02e2a-fe79-3dff-b7da-d3e07330a067 | -12.94532 | -46.84803 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2ab056f-71b2-3661-b7ad-ed146021ad68 | -13.34196 | -47.55663 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24b76833-c2d4-38bc-a5df-00677d579ddb | -15.86022 | -44.82887 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2221684b-b046-3a7a-9f4f-003865e895e4 | -15.31509 | -46.15982 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21813484-d62d-3634-af77-672f284351ff | -12.29185 | -55.10003 | 2025-10-08 04:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f02fd025-41ad-3171-af5c-df58bb1345af | -11.14069 | -54.88404 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dab81e1e-9000-3416-a6b8-921b8f57be6a | -11.70148 | -50.95899 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 17351f63-1786-3ad0-bde1-d8509b8b0594 | -19.13087 | -43.52239 | 2025-10-08 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 769f4d83-0a2e-3dd9-bbef-7723b43ed7d2 | -13.34129 | -47.56124 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2df692ae-77b8-335c-8007-b776e079b986 | -17.15037 | -43.44046 | 2025-10-08 04:40:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83eb1055-e1cc-3597-a912-601adb6abf5a | -13.75096 | -48.65485 | 2025-10-08 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14469c18-e69d-3ebc-9563-a1929b6f46e4 | -17.27961 | -42.65118 | 2025-10-08 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cee57857-f2c0-3cd5-8f9e-d44eaf18145c | -13.55712 | -51.80495 | 2025-10-08 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b56b6492-8032-3212-ae8c-6e525bc992e9 | -14.60952 | -52.48096 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81d75833-55c4-3e2f-adda-d4a9e0085853 | -15.07472 | -46.61998 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 192cc5aa-b8f2-32a8-aedd-03b5b7c3f564 | -13.0157 | -47.91116 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 41e18136-49bb-37a2-bb0a-8b297b1add5c | -15.6426 | -52.55072 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c416434-f719-36d3-a28d-3c64a0331201 | -15.30929 | -46.16622 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2cdfda2e-dcb3-35dc-b33d-61c0ca42539e | -14.53985 | -48.70051 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f9b32234-0f90-344c-ae98-a09eeb9d45b3 | -9.99198 | -60.01057 | 2025-10-08 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f128b859-27ff-3b51-82c9-bd97af2eb140 | -12.25091 | -47.86128 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e0fb076-90e4-37c5-91d5-00851c4421e5 | -14.62354 | -52.47967 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c44e8c1c-2df3-307c-ab57-337d1678db14 | -16.29111 | -45.24574 | 2025-10-08 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46df8bb3-cebe-3c04-a619-29320277fa77 | -14.71396 | -46.06837 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0993cf05-2031-3735-af47-b1a1532abbaa | -14.45006 | -48.7921 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fb26953-a975-35be-912e-3d346f20fc39 | -11.1773 | -54.88027 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 13205dff-6afd-3869-8803-9fb4e05b641d | -18.02439 | -51.14833 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2275006-234a-3dbd-ae70-6870e7224b50 | -9.88419 | -58.0341 | 2025-10-08 04:40:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c445cd40-9e5e-3f9c-9e54-b3667018f656 | -13.72801 | -45.69737 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6df03a73-334c-3510-ac21-de0f53d40a50 | -16.00504 | -50.82237 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59d02956-8759-3fe4-be70-0a68938e2abf | -15.27944 | -45.33875 | 2025-10-08 04:40:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f309ecd-cf6a-376d-9c63-8ba3bfceb2d2 | -11.33633 | -56.2016 | 2025-10-08 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README79.md)
