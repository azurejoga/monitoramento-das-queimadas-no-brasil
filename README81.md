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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f75bb6f-2f1c-3ce7-8fd3-ee75316a22c3 | -14.63024 | -52.48088 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 18fbc89d-0f8e-3615-8b94-10e31df55d8e | -11.16869 | -54.88383 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d561e5ce-32db-3bad-b06e-eddd84bff97f | -17.29007 | -42.65276 | 2025-10-08 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb3cf865-6f74-34a1-943e-4e8b91be13ad | -14.25682 | -45.86049 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71fa5512-4d16-3f4c-9431-50d13f09b5d5 | -13.74896 | -45.75625 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b71244fe-2ceb-3f80-9f71-ff61aa4a4121 | -17.29754 | -58.06435 | 2025-10-08 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2257a814-3203-3a95-8a6e-62b760f2f19a | -17.15866 | -56.59467 | 2025-10-08 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 603a08f2-a49a-390d-be5b-56acd1f559fc | -17.43224 | -45.80986 | 2025-10-08 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9bd373e-313d-3f50-bc1f-433c1fa31908 | -14.71405 | -46.00604 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a037022-8e25-3808-a700-f8871477c2fa | -12.94398 | -46.85729 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 00a9ff66-deb8-3644-9cb5-01677897cc1a | -11.14002 | -54.88229 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe0ff579-c9d8-3a9b-a8a6-82c68b9b6681 | -11.17684 | -54.90594 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f19a1ca-a9c7-322f-909d-f6724bdb3a6f | -14.92254 | -46.79957 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc3eda2e-bcc4-3cf9-a7bb-cf34d9482377 | -12.49222 | -54.715 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28cc8994-1561-325f-8995-378514c40f17 | -16.18291 | -51.74546 | 2025-10-08 04:40:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09c057f4-c87e-3acb-9691-fe433eca36fd | -12.39511 | -51.12661 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 96adcf86-9ab4-37a6-8369-2719fa8ba60b | -13.32446 | -48.02559 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 496a7761-ff6d-3b7d-9daf-0414bf49fbbb | -11.44833 | -50.21885 | 2025-10-08 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5a145f0-0eaa-330c-a1a8-53372d3fa3b5 | -18.00821 | -44.30688 | 2025-10-08 04:40:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1b19c623-02aa-30e8-a315-61f2634f23aa | -15.6298 | -52.5449 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb891d0b-2ade-3f4b-a017-b38e795df055 | -12.39398 | -51.13368 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e369d19d-7e1d-39b0-b353-79c4959160f7 | -12.93579 | -46.86087 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6676adf4-0be9-3b28-b0d2-607ddae351e3 | -14.60644 | -52.08436 | 2025-10-08 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11a83680-6507-3ac5-a437-5990917e6cd8 | -13.72342 | -45.67028 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5737feff-e03a-3b0a-a886-84449731b0ca | -14.83609 | -48.42412 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94d5f8ac-0f55-3642-a64f-a63dfb3e3cac | -14.71106 | -46.08998 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 784761b4-98ae-309a-844d-668990a655c1 | -12.63716 | -50.56278 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a3456b47-d6fd-335e-bf33-99faab4ccaff | -13.09278 | -47.80688 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ffafbeee-6a24-3d2f-ba31-00058ef1c4b2 | -16.13256 | -47.91475 | 2025-10-08 04:40:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 94166fdb-eb0f-3dfe-9adb-7e2f3a67349a | -13.21087 | -51.69614 | 2025-10-08 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0651dab6-7656-3bd5-9f88-9c6c246cf4e6 | -12.4028 | -51.1424 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc3bbfc7-b885-3122-8aa7-faa96bc115c9 | -11.73187 | -50.96037 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b663691-75ea-33f9-a971-ec9295ca903a | -18.02936 | -44.9628 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 67f0d16b-58b2-398b-af2b-af56e00ef7e2 | -13.20304 | -51.7022 | 2025-10-08 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac65a062-1141-35a4-ac5a-a8f3a7867f81 | -13.06603 | -47.93982 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 878e0b1b-ff08-37d3-8b12-58415537c75f | -11.4544 | -50.20184 | 2025-10-08 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86d8eb1d-d2f8-3499-afb5-d0816caf8fbe | -11.3625 | -55.18233 | 2025-10-08 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56011e93-4fad-34e5-9905-626bea76a7d4 | -16.06356 | -47.77353 | 2025-10-08 04:40:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f622af34-d4b4-382c-bd45-62876ae45974 | -11.14222 | -54.89289 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 059e3698-de32-3ead-9668-6e0c617f68b6 | -13.8234 | -48.01868 | 2025-10-08 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e350d5dd-b8ab-3409-b030-271e2f98b155 | -15.95244 | -42.60794 | 2025-10-08 04:40:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 93970994-8176-3fcc-9406-026f463a3b14 | -11.52057 | -51.49366 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d44c5b4-f34e-30fc-9a52-9cb2272cf84a | -12.863 | -42.62936 | 2025-10-08 04:40:00 | NOAA-20 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a6da4375-0899-3d1c-a7e0-c4d43b574709 | -15.29212 | -56.91986 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b767c0e0-ae9f-3cfd-84be-5aae42dad914 | -13.32147 | -48.02126 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6ee00918-9fc5-38e2-acb6-48b1e508a943 | -15.79596 | -46.24798 | 2025-10-08 04:40:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0a82167-886b-34ee-9a49-ae940ff05f97 | -14.36341 | -45.2372 | 2025-10-08 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f14fad1e-3311-39ec-9fa6-5017d5cfcbfb | -14.25223 | -45.86377 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a3c4b88-d9f3-3507-aeb4-8c663a5b6a43 | -11.95777 | -51.45899 | 2025-10-08 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c4f7896-ec5d-3ebe-908e-0a05707edbd3 | -17.26936 | -58.11995 | 2025-10-08 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| aef5e72c-6c0c-346b-b576-99ecac37c6d6 | -12.02467 | -45.20947 | 2025-10-08 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6d892fb5-b919-31a3-846a-a4161bc4ca1f | -15.38569 | -46.27644 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27b4453f-f4fb-3e6d-a89e-c1bcce379740 | -15.64141 | -52.55811 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d255b062-e070-3eb7-9837-278873d4307a | -11.18244 | -54.89668 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cf9970bb-a1e8-3857-8bfc-b793fb2e768c | -15.38482 | -46.28278 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37a55bf2-219c-33c3-8db7-efa7b63a275b | -13.29091 | -47.16048 | 2025-10-08 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a04c5fda-e0db-3bdd-b1cd-cd01c0547138 | -14.38001 | -46.02517 | 2025-10-08 04:40:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5ae61e2-1f06-3d1d-b532-7d18543bc9df | -18.02382 | -51.15199 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad52ce6b-849a-3136-b17b-038091845d4f | -13.80037 | -45.804 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2155b38-4fc0-38e1-933c-f63bdde5074d | -16.06591 | -47.77088 | 2025-10-08 04:40:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecf2eaee-80ce-3b16-9fc1-00a4a323c383 | -13.39883 | -46.70247 | 2025-10-08 04:40:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62545260-892f-3371-97de-426e393d741f | -13.31793 | -48.02063 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6a832b92-df5c-3229-8ceb-3cbf9a2005bf | -17.38045 | -45.0668 | 2025-10-08 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3dbd48a-500a-31c4-922b-d8974f0ba4fe | -14.61348 | -52.47786 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8c88f31-91c6-3ec3-8337-c52dfcd76291 | -13.25941 | -48.04865 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec00b5bd-8e84-35b2-a6c4-5572a29874bb | -13.02814 | -47.90049 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d6e7fd5-2384-3590-800d-f82e02111e19 | -13.28757 | -48.47337 | 2025-10-08 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02e5b76e-1f35-33aa-aa08-462a5c0d32d4 | -12.39342 | -51.13721 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21ad6168-cf10-3c65-85ad-8dd49619ceb4 | -19.33092 | -46.04294 | 2025-10-08 04:40:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b20f0df7-acdd-326d-a4f3-ac44149ca634 | -15.61381 | -52.57972 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6157c6a-84a1-3522-9281-e54f48bb7add | -12.5519 | -48.17267 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d8a3e35d-3f00-3edd-82f7-9ea257a0e181 | -11.74686 | -50.9303 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| ce7de87f-e8ad-3892-a791-785da62c3540 | -16.5927 | -46.55095 | 2025-10-08 04:40:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b1288f1-0ad2-3ce2-9cf2-b7cbefbb8300 | -12.22982 | -43.77825 | 2025-10-08 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4317cd33-7ee5-3d58-b068-4e2dbf0113fa | -15.98938 | -50.94541 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9bd5d801-831d-333d-90e4-e8e9695bc5ae | -11.13142 | -54.8859 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1ce2503-be8c-3ddb-8b7f-e13bb15c4efd | -17.48733 | -43.33544 | 2025-10-08 04:40:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd46de7f-62c0-326d-aedc-f011b190189f | -14.71829 | -46.03599 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fc3180f6-a4f0-3ace-949e-9032006e52be | -13.25273 | -46.47302 | 2025-10-08 04:40:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81174ec4-c5b2-37d2-bc2e-927007fab78c | -12.01799 | -45.19706 | 2025-10-08 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39776ea0-cb30-3cad-b3c4-aef6ac4e9e31 | -11.11633 | -54.03669 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4e824544-6c24-3c9c-a236-1e7962891f6a | -18.06545 | -44.47313 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5216408a-66df-35b5-a567-f61f4547c6d2 | -15.39946 | -48.01028 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ae49040-4385-3e9c-be9d-e78705cb3d7e | -14.70499 | -46.01218 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5400d6b1-1c46-385d-aa1e-a1399a12e9e2 | -14.79735 | -41.62946 | 2025-10-08 04:40:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f8c74305-5adb-3387-a244-6fbe7500bbbc | -14.70045 | -46.01533 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0ec91c54-85f9-3d7b-b764-5d3ea6b754a6 | -12.50055 | -54.71175 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 30fd46e2-4b0c-3666-ae9b-9a7f1ef07726 | -12.95863 | -46.83567 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f5c5247-f228-371b-b108-f7e0ea721c8e | -18.40582 | -45.2006 | 2025-10-08 04:40:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83944600-a4e4-30dc-85de-2c2f6112a69b | -13.28149 | -47.56448 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe505275-36ff-335b-b00d-5a6f6f18d956 | -11.1618 | -54.87757 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| baf39d6c-31c5-3182-b40f-9265c255921e | -17.38099 | -45.06223 | 2025-10-08 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b76b4354-9379-3da9-a54d-9b2b6d491fe7 | -10.96959 | -54.14655 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1741bd2-2231-3d63-8208-e870a96cd684 | -11.72198 | -50.93706 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 1a909e54-4e91-342c-87b1-a345b8fdf23d | -17.13853 | -45.79035 | 2025-10-08 04:40:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53ef986b-fa10-38be-8b6a-c4540cb3c483 | -14.72234 | -46.03651 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5dcecee2-e878-3a38-afc0-e043086c635e | -13.35344 | -47.55423 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b84a7969-26f9-383d-a576-e2c29a16083e | -17.13848 | -43.45668 | 2025-10-08 04:40:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 230c1a86-3098-3604-a44b-f6ada744fd2a | -11.74961 | -50.93437 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2121ca1e-1d34-38ad-90a0-25706cb65702 | -14.71 | -46.00553 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README82.md)
