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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75e801c9-68c0-3d85-85cf-3d1a9f986d6a | -20.26777 | -47.95073 | 2025-09-27 04:49:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 5e751add-e029-3e9f-89ab-bbaf542e6999 | -22.59288 | -48.58463 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9b4907ba-78ac-31e3-96a0-a62a9bbb5173 | -22.88424 | -51.23827 | 2025-09-27 04:49:00 | NOAA-20 | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 497cda3a-1856-34d2-9697-6f17c94a98c7 | -22.94988 | -49.89762 | 2025-09-27 04:49:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6e0ddce6-2a44-37a5-8929-17833118e25b | -19.63427 | -45.57513 | 2025-09-27 04:49:00 | NOAA-20 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d50dd90f-f9c4-359f-aec7-de69df279fbe | -19.05125 | -48.13227 | 2025-09-27 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f603666-cc24-305f-9db1-08640270290a | -17.1804 | -56.37963 | 2025-09-27 04:49:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| dce7e338-deec-3af0-ac6d-f3c08c1c460a | -20.7348 | -57.78001 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2230e1c4-eb6c-3b7a-84f2-4d8c53063e0b | -22.88487 | -51.23364 | 2025-09-27 04:49:00 | NOAA-20 | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ef7f484e-af64-3253-becc-ca85d71597cf | -22.27614 | -56.04973 | 2025-09-27 04:49:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b032a2a2-9e4d-32c5-bcab-10a1f9939df0 | -18.29206 | -57.09583 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d43e2d67-e0d1-3bf1-9009-e1435ffcbc79 | -18.18959 | -53.33155 | 2025-09-27 04:49:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbf27598-7a0d-3636-b7ce-8ff48ba13fa2 | -19.69621 | -45.89463 | 2025-09-27 04:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7b73e2d-82ec-3103-a0a4-aa5838846550 | -19.05491 | -48.13686 | 2025-09-27 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bc8b7928-f45f-3011-98c1-75a65293ead2 | -19.93315 | -43.61997 | 2025-09-27 04:49:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6df8f523-ba60-3ba9-89af-a8bdabe72501 | -18.32226 | -57.11789 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 0208960d-ced6-3d30-8978-5f5c246d4b8e | -22.5856 | -48.58094 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 336b6c21-f218-3784-a8d9-6a4d7561dd74 | -22.61215 | -49.03144 | 2025-09-27 04:49:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 405df858-cf7d-355b-9258-e4991d63b93a | -22.50328 | -52.98625 | 2025-09-27 04:49:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 1ba196de-b154-392c-ae82-cc8ea6a48c1c | -20.31986 | -47.13394 | 2025-09-27 04:49:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bb5c2ce9-adfe-3811-b389-1012ceaa52a4 | -22.58439 | -48.58335 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 589afa1e-db89-3368-b4d2-dc589faa2d0d | -19.05075 | -48.13626 | 2025-09-27 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1b7ce4d0-f3be-3fdb-bc64-76c23744b65e | -22.49423 | -52.97665 | 2025-09-27 04:49:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f89bb217-8b1f-3c48-8fb9-981af74f3a6a | -15.82981 | -59.61406 | 2025-09-27 04:49:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da944cfa-ebe5-3696-b73a-651477337bba | -18.32588 | -57.1186 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 03971d05-75da-324f-b479-1cd962e93925 | -22.16253 | -52.9041 | 2025-09-27 04:49:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bdf26b04-c0d1-32ed-a97f-36e4a618911f | -22.52768 | -48.73983 | 2025-09-27 04:49:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef332226-de88-3298-835a-6c92cc05cb20 | -20.98877 | -50.00972 | 2025-09-27 04:49:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 803eaa04-583c-3302-ab7b-b29e882b7291 | -18.18077 | -53.32267 | 2025-09-27 04:49:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc2bc5d6-147b-3155-bcdb-2699c0287cba | -17.17758 | -56.37478 | 2025-09-27 04:49:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3f4c1a60-6dbb-363a-bcd7-d9e3c37381d6 | -15.90499 | -59.32961 | 2025-09-27 04:49:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d92f567-298f-3a10-a158-04ed1bd29eec | -22.22606 | -49.72418 | 2025-09-27 04:49:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a00781b8-4bf9-317d-9876-a87b74b80133 | -18.29644 | -57.09473 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 85ac0fe2-5b69-37ab-a506-77bb4f633857 | -22.58766 | -48.59246 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 5ac43d3c-0242-3fea-aa9d-f426aff869fa | -22.58405 | -48.59367 | 2025-09-27 04:49:00 | NOAA-20 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 398d416e-d429-3c75-bb46-9cff0294a33f | -20.99705 | -50.00605 | 2025-09-27 04:49:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 87df7d3e-bfda-3ccc-beb5-c06b97156869 | -18.29567 | -57.09653 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c494bb90-de73-32e4-adcf-54194457ece0 | -20.89007 | -56.6039 | 2025-09-27 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a3e2132-1378-3cb9-af13-06d6e1694991 | -16.75615 | -53.35771 | 2025-09-27 04:49:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fdaf239a-f680-3433-9a27-acccc8727712 | -21.0047 | -50.00711 | 2025-09-27 04:49:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 35f80923-b31a-33d6-878f-9bc0d57f3aa0 | -17.57735 | -53.44835 | 2025-09-27 04:49:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09904c2f-fa04-321c-8dae-aa7ed84264bc | -22.26351 | -49.56729 | 2025-09-27 04:49:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3834453f-519d-3418-8df9-a5b476e16723 | -22.87993 | -51.24245 | 2025-09-27 04:49:00 | NOAA-20 | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0ba69d8e-78d2-3624-a24f-95aa47cd3ad3 | -21.48441 | -46.91138 | 2025-09-27 04:49:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1c848ae4-d051-38b5-9eb6-d2a6bad2229a | -20.12999 | -56.85701 | 2025-09-27 04:49:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eedf69cb-c9e3-3920-be17-25840254be5e | -18.3251 | -57.12299 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9ed15027-8e4c-3097-8a24-1a858f91537a | -20.72597 | -57.78749 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 69ab6ab3-9aa8-3305-82b5-1179711faf6c | -17.17968 | -56.38381 | 2025-09-27 04:49:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b197f794-04d9-300f-bbcb-b1e2b24eb50f | -22.59384 | -48.57624 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 00bb6dec-5678-3b02-850d-3155f212f4d1 | -22.58814 | -48.58826 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| fa84aff3-9bf4-3ad6-8b7f-65420c1dbda6 | -22.6158 | -49.03595 | 2025-09-27 04:49:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd44554f-8f11-3940-8d8e-da0ff9fd4d87 | -17.73464 | -46.71037 | 2025-09-27 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ded81a2d-d351-3c6d-98e5-d60fc38e61cb | -22.73319 | -48.56086 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a8d34db-6d8f-3422-990d-ba0c14652acd | -21.24642 | -48.5821 | 2025-09-27 04:49:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e3671198-793e-36f0-91e2-cb54834f198e | -18.29361 | -57.08965 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 94e0aeee-e8f2-3894-967c-9f3a97e5424f | -18.30806 | -57.09245 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 72cc33e4-b399-3d95-8044-93d7a69a3ba2 | -18.18352 | -53.32682 | 2025-09-27 04:49:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a2d2454-b82d-36da-925e-80de0cadb749 | -15.88367 | -59.32527 | 2025-09-27 04:49:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78fb98cc-30d3-336e-b1fa-e453f9cc0c79 | -22.72243 | -51.38691 | 2025-09-27 04:49:00 | NOAA-20 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5eea8448-22a0-33e2-a034-7199540c8216 | -20.16694 | -46.20451 | 2025-09-27 04:49:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63e284be-cd91-3775-8e91-e56e8b4eecdb | -21.00022 | -50.01149 | 2025-09-27 04:49:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fd456973-6d26-32df-b47c-0403618d1ff1 | -22.52818 | -48.73567 | 2025-09-27 04:49:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8db3e14-163a-3518-856c-3d57f13392fb | -15.90997 | -59.32661 | 2025-09-27 04:49:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0e2f258-776e-3e88-848c-ffe51e1e02d9 | -22.13705 | -50.02108 | 2025-09-27 04:49:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 682f073e-22fd-3ff7-84cf-23909216cf12 | -21.27262 | -48.33077 | 2025-09-27 04:49:00 | NOAA-20 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fd83f8c-c125-3956-afd4-a70a002d99e0 | -17.18467 | -56.37611 | 2025-09-27 04:49:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6318b11a-ff63-3477-8d72-49e771904e15 | -20.8836 | -56.60759 | 2025-09-27 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 528b286d-6fe0-37a6-9e9c-c52c0c407a14 | -20.99323 | -50.00545 | 2025-09-27 04:49:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 79432ce8-b640-3a9c-b4f9-f47d5a10d1be | -16.75946 | -53.35828 | 2025-09-27 04:49:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b15cce4c-7e0c-35a9-af75-2dd3792a3e97 | -15.92738 | -59.48251 | 2025-09-27 04:49:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f3148102-f3c0-3a46-82bd-cb0b82be6040 | -23.7022 | -51.71478 | 2025-09-27 04:51:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 69.5 |
| bf3c5415-caca-30de-a2e3-1540e0708de3 | -29.95135 | -51.61574 | 2025-09-27 04:51:00 | NOAA-20 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 39e88fcb-56db-3e78-be47-0eebc7c63573 | -24.07169 | -54.10225 | 2025-09-27 04:51:00 | NOAA-20 | TERRA ROXA | PARANÁ | Brasil | 4127403 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5ca32072-5872-3b91-b110-481f947521fb | -28.45664 | -49.66279 | 2025-09-27 04:51:00 | NOAA-20 | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 99f1816b-d81c-3a09-9b68-26e9a63d4603 | -24.55872 | -50.68835 | 2025-09-27 04:51:00 | NOAA-20 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7bdf64a6-45d6-3b30-9b1e-48a91d73e613 | -29.95167 | -51.61461 | 2025-09-27 04:51:00 | NOAA-20 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 1c0290ab-73ef-3260-b00e-d761a53345ab | -24.89373 | -49.58543 | 2025-09-27 04:51:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fd4df230-e14a-3942-934d-c203e47ddbea | -23.69858 | -51.71429 | 2025-09-27 04:51:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cb519096-851c-3cf7-aceb-ddc1ebe96feb | -30.40148 | -54.26599 | 2025-09-27 04:51:00 | NOAA-20 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 26552478-e86e-3641-a2e5-bac850254765 | -23.70087 | -51.71758 | 2025-09-27 04:51:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 37.1 |
| f265dda7-d2bb-333a-bac3-7e564ef2bf9d | -30.39285 | -54.25084 | 2025-09-27 04:51:00 | NOAA-20 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| fb0b9ea1-4349-3808-84e9-559228dba81d | -25.65099 | -52.16206 | 2025-09-27 04:51:00 | NOAA-20 | CANDÓI | PARANÁ | Brasil | 4104428 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 954efd73-6abd-3960-9051-2a5bb15d10b3 | -24.55487 | -50.68782 | 2025-09-27 04:51:00 | NOAA-20 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c82aa178-4198-3b71-a64f-01cab07ec94c | -27.93848 | -51.58258 | 2025-09-27 04:51:00 | NOAA-20 | TUPANCI DO SUL | RIO GRANDE DO SUL | Brasil | 4322186 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 76538cdb-ddca-345a-bf5e-c60372627f14 | -31.69575 | -52.54129 | 2025-09-27 04:53:00 | NOAA-20 | CAPÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4304663 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 26b04253-e3e9-3b6f-8d38-0ec3e2d6aaa1 | 4.74084 | -60.59359 | 2025-09-27 05:31:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1c54282-1a7e-306d-bdcf-4b56c143d41c | 1.04525 | -60.53917 | 2025-09-27 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34ede05e-3685-3967-85de-dd489c9d8e71 | -0.17896 | -60.68992 | 2025-09-27 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 156550b4-7a94-3190-bcc6-e61ade6bd0ce | 1.04582 | -60.54278 | 2025-09-27 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2088fe31-08e2-331e-b097-1d95d74a921c | 1.04245 | -60.5433 | 2025-09-27 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de1ac7cf-16d5-36af-a054-f4b80df0e3e7 | -1.44012 | -60.36754 | 2025-09-27 05:33:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ea6ac80-9c85-392e-96fd-fa51c3a23c46 | -4.59214 | -50.65556 | 2025-09-27 05:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 971c2349-f417-3265-ad40-9cdbf76cc8b0 | -4.5913 | -50.66162 | 2025-09-27 05:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5b1b0e13-9371-3c79-b7f7-4eda6df49673 | -1.13169 | -54.21284 | 2025-09-27 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf5eeee9-f688-3f10-a4ab-3bc83a135351 | -1.13217 | -54.20977 | 2025-09-27 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db3f46ec-2c49-3269-803e-f1dc1d4c8292 | -3.33613 | -50.24823 | 2025-09-27 05:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5e891d40-8602-3da5-8536-acf1a61d9cff | -2.69915 | -60.96292 | 2025-09-27 05:33:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a8dc837-fbbc-3404-ade5-9e800dc21033 | -3.33376 | -50.24877 | 2025-09-27 05:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 990530e4-60ac-3f07-9104-f408ef2baf65 | -9.50116 | -54.47231 | 2025-09-27 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 613c1511-faca-331c-80d7-11748b469bbc | -4.6484 | -50.968 | 2025-09-27 05:36:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README57.md)
