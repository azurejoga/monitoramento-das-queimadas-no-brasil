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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40e164d9-49d1-3813-aa19-7064cd080c0c | -18.77806 | -48.91077 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6939a762-bd1b-37b5-8552-ea4f3954d411 | -18.16952 | -51.79787 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 25a7d619-0b2c-39a6-a445-b553a6a0ef88 | -17.08264 | -56.85144 | 2026-09-03 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e374e50f-3c6d-33b6-8432-596225977bbc | -18.13848 | -51.80911 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 325c8dde-21ac-3c95-a6fe-a3627e2cfa03 | -18.13353 | -51.81668 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d189343a-52e3-3658-aabe-c2e8cf7fa5b6 | -17.4865 | -47.85081 | 2026-09-03 04:42:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 030cc518-820e-34b6-bc24-07da91ee139a | -19.09349 | -48.49204 | 2026-09-03 04:42:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d10e902-fd15-36ed-ba9c-ac04a136803f | -17.49043 | -47.84767 | 2026-09-03 04:42:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16976160-1d6b-3d7c-84cc-db4941c6eff0 | -17.48986 | -47.85138 | 2026-09-03 04:42:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00f11edd-2482-3985-8746-95c576852905 | -18.16107 | -51.80471 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0fdaeb02-1236-39f1-8aa3-eb8f80bc0687 | -17.15542 | -50.28133 | 2026-09-03 04:42:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 02c07b12-e0c4-39e8-9a9f-bcd03f3ebe84 | -18.82411 | -47.60161 | 2026-09-03 04:42:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a23b0f4c-5ed3-39e5-8da2-ad8345a1e545 | -18.78082 | -48.915 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45a8a294-0feb-36d1-a524-2fdf3694c6d2 | -18.14058 | -51.81799 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fd14c10a-5bbe-3411-82ef-fb8cac16b0df | -22.85554 | -42.04078 | 2026-09-03 04:42:00 | NPP-375D | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 313b3023-d64e-3505-be3d-30e6b924fd27 | -18.84623 | -47.14286 | 2026-09-03 04:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e99fcfd-dc30-3522-bf01-1d212d8e5b2a | -22.38796 | -53.59412 | 2026-09-03 04:42:00 | NPP-375D | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 666e4ceb-2593-3b28-95a7-665b896afb52 | -19.19116 | -46.84303 | 2026-09-03 04:42:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44195e2e-c78c-3fb1-8a73-8f03755d4c63 | -19.27855 | -47.2575 | 2026-09-03 04:42:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60899b35-3287-36d1-a92c-af0929827c71 | -19.35911 | -47.09522 | 2026-09-03 04:42:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c1613d1-ed43-3864-ae33-db68c958968d | -18.17304 | -51.79852 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 45d8c924-9ff3-3c08-8765-fd0b033e6d90 | -18.77968 | -48.92231 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb82398b-2dbe-3c66-887c-d65a2e3f634d | -18.84969 | -47.14344 | 2026-09-03 04:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee2994a6-01f7-3ba4-be9e-7ddb5a56cb51 | -18.13705 | -51.81734 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 699bb717-e5e6-3f04-a61d-7907c59552ce | -17.08636 | -56.85794 | 2026-09-03 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9bf87af1-1320-37b9-89b9-8d06e6c0abc5 | -20.9673 | -47.41178 | 2026-09-03 04:42:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8eb1f580-c3c8-3a33-8584-13b115898230 | -18.78139 | -48.91135 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ceb9293-4219-3ab0-b167-d5b978600f52 | -17.09117 | -56.859 | 2026-09-03 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c3dfaad5-0000-32cb-af5f-f8f5af94e29a | -23.13861 | -48.6778 | 2026-09-03 04:42:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bbd4c28a-39a8-3f0e-8008-01008d313e70 | -19.0892 | -57.36726 | 2026-09-03 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0de7ca7f-2660-34f7-9dd1-85d2380c6fa1 | -17.48371 | -47.84655 | 2026-09-03 04:42:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdb57ae8-0bc0-3516-a31d-1644b37f5c14 | -17.08922 | -53.46701 | 2026-09-03 04:42:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 990e1192-0047-36a3-8022-b7780bceadf3 | -18.13424 | -51.81256 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b939f76-fea1-3c07-a58a-9acfb57f2535 | -18.142 | -51.80978 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c02e4b00-e870-379c-b383-a6451db3a303 | -20.86138 | -57.7145 | 2026-09-03 04:42:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 768e768e-8ae7-3274-87ae-e7ed8025174c | -18.53243 | -46.82427 | 2026-09-03 04:42:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 874073ea-8eff-3e20-a6f3-235fca6f9117 | -19.35623 | -47.09062 | 2026-09-03 04:42:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b50f94e0-91d1-3290-98c5-ef1083d7a0e2 | -18.77749 | -48.91443 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4161bd1-7aac-3e2d-8b10-87e92b8a79d1 | -18.16389 | -51.80947 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1d64a6ef-54f9-3063-8399-0079fa516db0 | -18.77864 | -48.90712 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54d8eae5-5fd3-35b1-b2bb-ec09285cc629 | -18.51554 | -48.23419 | 2026-09-03 04:42:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b82049a9-0de6-3b24-a640-1701d357b486 | -17.48707 | -47.84711 | 2026-09-03 04:42:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15d29a7a-feba-301a-95e6-21931dfa5dbd | -17.08417 | -56.86892 | 2026-09-03 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ab302305-44c0-3bb3-8e65-c73bd2e6f842 | -17.08527 | -56.86342 | 2026-09-03 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d18e7c73-030e-3eeb-ac90-b3246f858403 | -18.74699 | -47.4439 | 2026-09-03 04:42:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 00d4185f-30ec-3e36-a77d-987940f4d10c | -17.08534 | -53.46621 | 2026-09-03 04:42:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adc6cf2f-51cd-37c1-998c-4b29326146b5 | -18.1653 | -51.80128 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ace7cbf8-d986-3886-972e-79182de17361 | -17.07893 | -56.84493 | 2026-09-03 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4ec0f146-fc69-35a5-89d5-4810c2b523ef | -17.18729 | -54.30063 | 2026-09-03 04:42:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff665e72-ffc3-37af-8f21-c49dec54de11 | -18.16882 | -51.80194 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 24373afa-f089-31c2-a6f3-1cfed2ed7dc6 | -18.14129 | -51.81389 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a5c8cd06-40bc-356e-a4f6-5d613978139b | -17.31636 | -49.61787 | 2026-09-03 04:42:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7a1aaa96-671f-3de2-855c-bd6f830f4d18 | -19.35563 | -47.09467 | 2026-09-03 04:42:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27f48704-5cee-3e62-85d0-29b7f3121431 | -19.09089 | -57.36465 | 2026-09-03 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1a340122-a747-3fb3-ab52-3f2390d5bb06 | -18.16177 | -51.80062 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1ff5055d-658a-304f-8f89-5cd9d09d2b1d | -18.77608 | -48.91104 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86499ca5-9089-3804-ac8b-46f248ca030a | -18.78025 | -48.91866 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 506e641f-7dcb-30aa-836a-c2c4d68a2791 | -18.84254 | -46.44493 | 2026-09-03 04:42:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a81ae9e5-ef2d-3c6d-9a1b-e9fb70fd832e | -18.77692 | -48.91808 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d71402c8-d97b-3bc3-8da0-f8dfed6fe918 | -21.89939 | -55.37201 | 2026-09-03 04:42:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc1a2cd5-f515-31c5-9e80-2e731c0cb94c | -20.40013 | -47.1563 | 2026-09-03 04:42:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56c9ef84-d835-343f-9467-0daf55e9db42 | -17.15355 | -50.29254 | 2026-09-03 04:42:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 395c76f1-7632-3e5f-a80b-8f1bee4501fe | -18.14482 | -51.81456 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 81c26c9b-f548-3792-b135-8375279078f6 | -18.77493 | -48.91834 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc7445ce-9b61-32ec-abb7-878abe9e059d | -17.09226 | -56.85353 | 2026-09-03 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 34641221-1549-3c17-8b1b-9f205459d63c | -18.78301 | -48.92288 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aec2ffed-b572-3575-8464-be20d0e7bf82 | -22.43401 | -49.7671 | 2026-09-03 04:42:00 | NPP-375D | ALVINLÂNDIA | SÃO PAULO | Brasil | 3501509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4c46c476-191d-3f73-ab50-bb142f4c8bab | -18.83543 | -46.44383 | 2026-09-03 04:42:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 71359b32-37cd-3146-8c6d-da5d7179a282 | -18.166 | -51.79721 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b2acc5d-937a-3ed0-b97a-469bdc1b04f6 | -18.1646 | -51.80537 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8aaa981f-fd7b-3598-815f-6e6632f8f1b2 | -21.89536 | -55.3712 | 2026-09-03 04:42:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3e34dc7-025a-3c9a-abb2-a128006b7199 | -18.83898 | -46.44441 | 2026-09-03 04:42:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fe0e34d4-42dc-357f-b56c-b03c72b622e4 | -22.43068 | -49.7665 | 2026-09-03 04:42:00 | NPP-375D | ALVINLÂNDIA | SÃO PAULO | Brasil | 3501509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c818dc91-66df-32f1-b418-edebde76e2e3 | -18.77666 | -48.90738 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c37638c3-35a7-3f33-bc39-4379b7ca95c2 | -23.0499 | -46.57203 | 2026-09-03 04:42:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 967026f4-ddb9-32c8-ae97-e1ad9a78c484 | -20.14244 | -54.68983 | 2026-09-03 04:42:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c07c4aa-e0bd-32bf-97e7-c4f48af5edef | -18.82752 | -47.60218 | 2026-09-03 04:42:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 032bf971-c163-35cf-bdb0-f8e9e543ca98 | -18.78358 | -48.91923 | 2026-09-03 04:42:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7df369d9-aec9-337d-a4c0-96ed08cdc637 | -18.16247 | -51.79654 | 2026-09-03 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4072f75a-7623-3a22-bb58-597f2b0cf8e3 | -27.03101 | -52.66503 | 2026-09-03 04:44:00 | NPP-375D | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 06f65923-ac5e-307b-878b-6bcaef46eff8 | -25.38749 | -52.11385 | 2026-09-03 04:44:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0c6ac4cd-f55a-35df-9f3b-080e2f82ba6b | -25.38413 | -52.11314 | 2026-09-03 04:44:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 094a2f70-fb2f-3af4-897a-cea21729109a | -29.71907 | -51.10291 | 2026-09-03 04:44:00 | NPP-375D | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 3808546a-3b0f-3170-b4cc-4ecbb5c387e2 | -8.0737 | -50.9656 | 2026-09-03 04:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| bf691bc7-5e0a-37f3-8921-299b84baf694 | -6.6357 | -59.4459 | 2026-09-03 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 1cadd968-53cb-31c3-b51d-ebf63361c51c | -6.7648 | -59.4408 | 2026-09-03 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 5c4e6c5e-1c7e-34e5-89e5-63af1352f500 | -6.6883 | -59.9436 | 2026-09-03 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| d4ab7277-8075-34f1-860f-e0c99d51b488 | -7.566 | -61.343 | 2026-09-03 04:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 35e6bd8d-4bdb-3c8f-a933-d90085b1e1df | -8.0924 | -50.9642 | 2026-09-03 04:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 35a4ed19-6255-3df0-b901-beb775bb0888 | -6.6541 | -59.4452 | 2026-09-03 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| d37d0be4-22bb-32f3-ae61-a20e4d1aaca7 | -3.2486 | -47.2438 | 2026-09-03 04:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 76e63c41-5b92-3d3b-ac7e-af1f8582403f | -6.3052 | -56.0442 | 2026-09-03 04:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| f2622380-3094-3910-befd-39cf54c0148b | -3.2485 | -47.2657 | 2026-09-03 04:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 8adbbf28-f7aa-39cb-9ef7-8888ec6a406d | -6.3237 | -56.0434 | 2026-09-03 04:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 32b5b682-00ea-3752-b143-e3d16c3701f1 | -6.6698 | -59.9443 | 2026-09-03 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d1517983-949c-3469-a161-4846d850f62c | -3.33734 | -42.80807 | 2026-09-03 04:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46d509d3-c09c-377d-ba42-9ffaf21f4ef3 | -1.35744 | -54.63342 | 2026-09-03 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22e48964-30d8-3839-84d8-45814cfd0504 | -3.18694 | -48.01968 | 2026-09-03 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39e48897-6a87-386a-98ae-402f2bbad066 | -1.02549 | -53.72161 | 2026-09-03 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 686b7840-5141-32c8-a267-7c7ab9ad0703 | -3.93179 | -49.05194 | 2026-09-03 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |


[Clique aqui para ver as próximas entradas](README32.md)
