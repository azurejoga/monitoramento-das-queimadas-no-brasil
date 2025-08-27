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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f9b4678-7c7b-3678-92c2-2163cc7ea360 | -12.74445 | -48.18399 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc53a2b4-e782-35ca-8b1c-2d09b82710b0 | -10.84085 | -54.01387 | 2025-08-27 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb8eea46-e944-3aed-807d-ce0cd01b2cba | -13.62249 | -48.2158 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fb658d4-0e8e-3ba9-add0-3d1fd8fcf30a | -13.4198 | -46.86325 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2c795c01-82a8-3d21-8383-af8f8e107cbd | -17.40718 | -44.77606 | 2025-08-27 04:27:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2355530-d372-3edf-9de4-ee5230e48626 | -16.7311 | -49.36103 | 2025-08-27 04:27:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a50dc1dc-da2f-36c5-a597-ab0b094da4c6 | -15.53964 | -47.38862 | 2025-08-27 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5a5c0d4-461e-3a8f-8fa5-5a8e036402e8 | -13.17076 | -45.29313 | 2025-08-27 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 55ceb151-6025-3dd7-a3b9-c5707e30cbc5 | -13.82324 | -45.88897 | 2025-08-27 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b4b22aa-dfd4-3023-b46c-5ccfea31a1b7 | -18.52933 | -48.92482 | 2025-08-27 04:27:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 598e81f9-5ed2-303e-b519-bc6a1b3dbc71 | -13.06802 | -46.30453 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ce2ddfe-d4b7-36db-ad44-dcfcafcc8aa7 | -18.15296 | -44.44294 | 2025-08-27 04:27:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d998713a-adba-3a64-9b16-2ac0851600ca | -13.07256 | -46.32715 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b6842e07-f528-37b7-9041-7be7acdfe0ab | -12.78549 | -48.11815 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3ee0424c-0484-3145-be63-b784bef41e7a | -14.76869 | -59.71634 | 2025-08-27 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c2e709b-e835-3b9a-b71c-36eed71c5c9f | -13.40199 | -46.91209 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b26983a4-2d3a-377e-a307-fedbc7454030 | -15.62093 | -52.71521 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 483559af-14a1-3ff1-b40e-22ddd328a230 | -17.21108 | -47.20779 | 2025-08-27 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb26632e-8849-3efc-b807-d41cea085be1 | -16.74401 | -48.5322 | 2025-08-27 04:27:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4ce7e43f-a1eb-3580-98b9-ff1490417e5f | -14.12831 | -45.40921 | 2025-08-27 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7402a60-2775-3020-a27a-04bd6cffce18 | -12.73063 | -48.18535 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35dce5f0-adcb-3d77-b41d-c653b21fddc1 | -11.33727 | -51.24443 | 2025-08-27 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| faed3649-cd47-3109-bef4-2fbf2379fc55 | -13.61093 | -48.20304 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 94ca9a84-5733-3fa2-872f-1de907e1a626 | -15.62125 | -52.73529 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 42d184eb-cfbd-306b-8066-97c00a8da093 | -13.43257 | -46.86132 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70ec50af-5985-3853-9ed0-22f17c4074ee | -15.51847 | -47.39265 | 2025-08-27 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31fc91ed-e528-312c-bf18-6d79834b33be | -15.82238 | -45.77013 | 2025-08-27 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45f5231b-4667-39df-b9b5-75a6e523fdbd | -14.52794 | -53.02762 | 2025-08-27 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91fd8a2b-2a9b-37a2-a8f5-159d5808b661 | -13.05452 | -46.30222 | 2025-08-27 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 383b1430-72a3-33fd-9b59-66a671260688 | -13.0059 | -56.89644 | 2025-08-27 04:27:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9074a865-df47-3942-9dac-42f016f8b5fe | -15.62594 | -52.73106 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4894010e-43ed-36ea-9fbf-aa5185b8c742 | -12.38934 | -45.00928 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fde79713-47ef-3044-a4b9-6f716fa01660 | -15.60031 | -52.70371 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a40c4f55-4a14-33d1-87c0-16a02ae68ebe | -12.74452 | -48.16218 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d21ccefb-de33-3b07-ac4e-01b41ee474ef | -9.40852 | -60.50826 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ab28aef9-9412-361b-a9ca-162578964275 | -12.93725 | -46.3364 | 2025-08-27 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5b913f4-3bbc-3430-afd6-69a5b462377c | -15.09493 | -48.54725 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0fea8186-fce0-3e94-bf6d-86e854ac0ba1 | -15.60242 | -52.71411 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9d561c1-f0c5-375a-9b52-452a634d1ddb | -13.39365 | -46.92177 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ed6728b-5016-3011-bc6a-836ff966b2d9 | -17.25746 | -44.88158 | 2025-08-27 04:27:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32d68b80-1a43-3463-9a96-f502720730a9 | -20.00855 | -42.13485 | 2025-08-27 04:27:00 | NOAA-20 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 88a54878-1caf-33bd-ade3-bfd9ff02fc09 | -11.29355 | -53.96357 | 2025-08-27 04:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1f9daeba-889f-3bd0-a729-2ee87935b74d | -12.75659 | -48.19325 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de5a5e2d-3fb2-37de-bac7-589c0b40c7cc | -14.13243 | -45.40569 | 2025-08-27 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26f8162d-26f1-3c8c-9162-3a770a8d5996 | -12.76046 | -48.19027 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 116c2f2f-6793-3462-8362-ab822b2f101a | -16.38369 | -48.81438 | 2025-08-27 04:27:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d82c03f-77a2-3c1d-8d4a-7588d96e1f39 | -17.26121 | -44.88214 | 2025-08-27 04:27:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 560579ff-d2a9-3791-bf00-70d9eab33a5f | -13.17135 | -45.28913 | 2025-08-27 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f056b127-35a1-3047-865f-d4b6598ddf28 | -12.7494 | -48.19569 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23cce6aa-320b-3e54-9a29-aa0cff7d0af6 | -15.66096 | -52.73289 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82acc004-a43e-3998-82c1-b9f6bbfb2322 | -13.6148 | -48.20004 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 34e0b823-9693-3934-a1e1-3417b7fa6338 | -15.63557 | -52.74312 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf6f3c32-1b09-3699-844d-8edf40ad02d1 | -12.89336 | -44.64085 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5b76294-eaad-38c8-86f1-eeadfadbe980 | -15.1034 | -48.72789 | 2025-08-27 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62601b7c-e246-3f54-83d3-ba9dc8b6f702 | -12.77214 | -48.15952 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 354e1e49-644e-3ece-95ce-561b049a49e4 | -18.93384 | -46.58249 | 2025-08-27 04:27:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a260dba7-f8ec-3140-9fc9-1bc0bd0da372 | -12.71581 | -48.15024 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f30946c-f6a0-32f0-b066-acc2776cbe28 | -12.3144 | -55.30643 | 2025-08-27 04:27:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa1e9c7c-79d4-3721-ad53-1b045f0d84de | -16.7407 | -48.53163 | 2025-08-27 04:27:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a30449f9-119d-3e8b-8aaf-0a7410a13199 | -16.65725 | -50.19388 | 2025-08-27 04:27:00 | NOAA-20 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f313e956-394c-3b0f-b1a8-28d74601e268 | -14.30317 | -60.3596 | 2025-08-27 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 774b8162-3f6a-37d6-927c-9fe7bde3eb82 | -12.76827 | -48.16248 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e4dd6b4-643c-3e76-b045-9d013136faa5 | -17.97179 | -48.05354 | 2025-08-27 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5cbb57e-f78a-3393-84c0-b8aa01fb1d02 | -13.0692 | -46.31952 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1376631-73d6-381c-b475-dd161a013881 | -12.80305 | -48.11371 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8f724e41-c5bf-38e6-aa30-b881319be017 | -14.84514 | -49.2154 | 2025-08-27 04:27:00 | NOAA-20 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d5c07745-37c8-319c-8a11-a369c970b985 | -9.41147 | -60.52932 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b22fc459-8b00-33b4-88f3-28715ee9b6ff | -13.22336 | -44.55015 | 2025-08-27 04:27:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd64d639-439e-3b55-ba16-907ae79ce0ee | -17.40736 | -44.77337 | 2025-08-27 04:27:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f4c9afd-c311-3075-b39e-870d25fa1cc6 | -12.4991 | -47.23921 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ab9d1cd-3b33-3f9b-ac93-21764c7a3a44 | -12.90536 | -44.65997 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 731a63b7-b475-3bee-abd0-77ad3b848289 | -12.24895 | -45.05434 | 2025-08-27 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb4ea404-8981-33e3-bdd2-49908b099b16 | -13.17809 | -50.59372 | 2025-08-27 04:27:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab97d136-b230-3cb8-baa1-32d4862b065b | -15.09733 | -48.72322 | 2025-08-27 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08b7c1d7-c988-3b19-8e18-c9529044a068 | -13.39476 | -46.91457 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18eeeca2-f949-3368-a0b0-e9ded3e1d5d7 | -13.22736 | -46.54628 | 2025-08-27 04:27:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eaffd0d1-d83b-3b4e-bda5-543d2d540119 | -11.8249 | -46.79469 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb4d8c64-eee8-349b-b8e2-6c3cc1441649 | -13.65138 | -45.7056 | 2025-08-27 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e283249-0690-3ae5-8fb0-332188e45fa3 | -15.10445 | -48.61453 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4623e254-f786-3585-8478-f958c1a5ac47 | -13.40588 | -46.93124 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e53601d-4a6f-316d-9763-cf67f3ba1731 | -15.60663 | -52.73505 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e6393df-99af-371c-a928-e7b61a5c601c | -13.05506 | -46.29867 | 2025-08-27 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2cd9446e-5d7b-3048-bce4-f8850a9117a3 | -9.40982 | -60.50176 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f1e2202b-7dd9-37de-97c6-e08a45de7558 | -11.81437 | -46.79665 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 625869f7-04cb-393c-bca0-f16dc9e85d22 | -13.62417 | -48.20519 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 338092bc-8154-3d07-a7e6-7c76ee1fd9bf | -15.61626 | -52.71932 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2826e1de-7dd3-3c67-93fa-dd1e8b74576c | -12.74339 | -48.16927 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 818946d1-43b8-3e3b-ba85-65f327764c2b | -15.65718 | -52.73212 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d407107-378a-3e69-be5f-7d3652275bd9 | -10.03113 | -59.3601 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4983ce5f-ef00-3dbf-b48b-39c70c4b0db0 | -9.40722 | -60.51477 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a2d9e1dd-d5b4-3e40-bdac-4e31b2e7462e | -18.14967 | -44.43785 | 2025-08-27 04:27:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dd3d720-d1db-36f6-b658-c7660af1e478 | -13.43388 | -47.00944 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66953985-cbd3-345e-8bd3-67a6fb7423b9 | -12.49965 | -47.23567 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e3da429-3d33-36e8-9ec6-86f1fa6ae2c4 | -15.41014 | -46.5975 | 2025-08-27 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ceed701f-1e55-38ed-837d-0453638de274 | -12.78055 | -48.10647 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 877fa92f-9553-353c-bc17-bf039beeabe0 | -13.47225 | -47.00446 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 905e6fc2-e45f-3b0d-8ab9-edfec1a0c126 | -16.38338 | -51.88711 | 2025-08-27 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a779658-7d81-3d35-8e36-bc92789579b6 | -13.07029 | -46.31926 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5580a132-e18c-37c2-97e0-373235cad222 | -13.38808 | -46.91349 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f0068317-f606-3a1e-bfb6-dd14ad0bb0f2 | -12.76934 | -48.17719 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README45.md)
