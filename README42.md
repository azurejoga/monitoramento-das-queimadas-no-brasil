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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dbb4dfe-7d8d-3bb7-8edc-3c2427c58112 | -17.91031 | -57.51639 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| ed8ee1b7-50df-3f6f-b85e-6912f42834f1 | -17.9034 | -57.51534 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| faffa525-8a75-3bea-b51c-a8eac6f982d6 | -13.8432 | -45.84127 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82889d7d-6ee8-34ef-8df7-7f2d69c744ac | -14.07881 | -50.15783 | 2025-10-10 04:53:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2eac6a0-bfd5-3e84-b02b-9f591d293c3e | -16.29644 | -47.08222 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37ff334c-538f-38a7-ae26-f7b1223f67ac | -15.0873 | -46.60503 | 2025-10-10 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ed296b29-84fa-3342-9e74-3fa41652c00e | -17.83053 | -57.65268 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d5f187f2-effa-3d31-b925-fbf0fce50cf4 | -17.84888 | -57.60743 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 41ba4a4d-3337-3081-8ded-a493427be26a | -13.29402 | -48.00163 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d1d6868-810d-3fb3-b26b-d44cfd4c9e79 | -13.31448 | -48.47522 | 2025-10-10 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68763a08-4fca-34a3-81e5-a1cf1cb72fad | -17.82413 | -57.62748 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 543b7c6f-9f2b-3d31-9cc5-afa992a4b4dc | -15.90106 | -48.15645 | 2025-10-10 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88d43857-79ba-397b-af42-bd1343cacbf2 | -17.84531 | -57.58653 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 05144885-a565-3a01-8f07-b1c941a8e4f3 | -15.46662 | -48.53204 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f20e4719-1796-36dc-a119-85e466d83b7f | -15.11935 | -48.71291 | 2025-10-10 04:53:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a020c86-4993-3176-b2b8-7847e308c064 | -15.23572 | -46.38106 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a18745f6-063e-394b-9a3e-9aeda628a3ab | -14.73285 | -48.36311 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d853fd1c-46b7-3580-9b15-c6079a21b269 | -15.00052 | -56.81975 | 2025-10-10 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28f85d9b-ab42-3f6b-a7d3-c83da4dcf789 | -17.84427 | -57.6556 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0ac265c4-d1ff-32e1-a618-635f56ac81bb | -15.41105 | -48.03096 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1adabe3-be6d-34f1-9816-16a6db8b37c8 | -14.93171 | -46.76471 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| aac2e54e-d75c-3401-aecc-040d886d0c2d | -14.4316 | -48.01043 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bd5cce04-b6af-3198-ba9c-d07bd57f6567 | -13.31942 | -48.00944 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7be393ad-99b6-32de-81a6-9a385bc677f5 | -17.84496 | -57.65152 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8adec773-0c09-30a6-b2c6-250050bdf277 | -13.35974 | -47.63054 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 887a0508-6610-3efb-b79a-0797f6a07557 | -13.8421 | -45.8501 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cc672f0-6962-3fa2-b748-f18e04ee4330 | -17.94882 | -45.02726 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e733a282-eb91-3391-bb16-1e379b52a515 | -15.29404 | -46.14648 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 062ebc69-d598-312b-a4c0-3f6822f83e37 | -13.36273 | -47.74638 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f0181449-7b36-38ee-9dab-e9209dca132f | -13.24706 | -46.47657 | 2025-10-10 04:53:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 482b199b-a487-3123-9766-9d9f57698b65 | -13.3306 | -48.48263 | 2025-10-10 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61cd3ea2-dc4b-32c4-beab-ba888b97c110 | -17.3763 | -46.90339 | 2025-10-10 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 028341e9-6a5f-3db8-aea0-8cdf95260cb3 | -13.33111 | -48.47871 | 2025-10-10 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7c37f8e-2e76-38e4-b3e0-309a41819e31 | -14.84971 | -48.4639 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a9d9f2a-8c16-31a4-962a-b4b22772d1bb | -14.42779 | -48.00536 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a5c3fe2-aa8c-3825-8240-750428aa4dfd | -17.21765 | -47.65586 | 2025-10-10 04:53:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e526134d-932c-37bf-bfc4-371f9467bc13 | -15.46177 | -48.53561 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fb93ab3-4a16-3331-8631-3388f7130d53 | -17.82641 | -57.65598 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ffd19688-d9a6-3916-9bc5-1d396a1e244e | -15.97989 | -59.53175 | 2025-10-10 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52f2198a-12a3-3008-95a4-3270addbde2b | -15.97011 | -59.5414 | 2025-10-10 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7d61dd03-4bcf-36c0-b313-edd87192eb76 | -16.00804 | -59.5538 | 2025-10-10 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 69ba73dd-531e-3b93-95f2-546b675fca9f | -13.27188 | -48.02031 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc8eb09f-12a3-3fed-9e48-76e17bb5aa97 | -18.04789 | -44.98609 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8bed1544-ad29-39c4-83b5-165298e8c7a7 | -18.78504 | -44.61485 | 2025-10-10 04:53:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b164f827-8c5c-3ae3-ae8e-34c39563a51f | -14.26773 | -45.87125 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90f712b5-a212-393f-9a3f-50505054128c | -17.38768 | -46.87517 | 2025-10-10 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a318876c-a205-367e-805e-679613d614fb | -16.26848 | -47.15593 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 77d73d6f-3f5b-37ee-8d38-198b8c6da0b8 | -13.25603 | -46.48291 | 2025-10-10 04:53:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29087637-3685-3e7f-bb80-47d1008d386c | -13.84284 | -45.84418 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1783f01-53a7-3c22-b98b-032491786632 | -14.88668 | -48.24166 | 2025-10-10 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 50d180be-3a62-33e6-bff1-71c501cea18a | -14.93037 | -46.78 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 81b5a99f-7a01-3de0-8a5e-8f19a7a8aa80 | -16.74345 | -43.97996 | 2025-10-10 04:53:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c93505f6-0970-3a33-b135-a8674afadb3c | -14.93101 | -46.77491 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2ca9a995-b850-3085-9b83-fc0d0d395a65 | -17.99378 | -44.97819 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c512c81-48f0-370d-8ef3-60c5e8b915c1 | -14.68519 | -48.06334 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28775c3b-b740-3fc6-8e9c-8b27c44c33ab | -17.97845 | -48.55315 | 2025-10-10 04:53:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b78a6869-0237-31fc-a617-2e6219169544 | -15.42578 | -47.98701 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f9ca7cc1-df73-369a-bf45-2f1e817b6cef | -14.9364 | -46.76649 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 80f803cb-2014-3680-823f-371c9c2441ca | -17.94921 | -45.02343 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e20acbce-6c86-3d8d-8da0-1e2e1529ef62 | -16.00604 | -59.54251 | 2025-10-10 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68fab19f-8e2b-3deb-bc4d-be1cf929e488 | -15.75662 | -48.98544 | 2025-10-10 04:53:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9f27d855-4b48-3c48-bdb4-d1034cd69b6c | -18.78541 | -44.61367 | 2025-10-10 04:53:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce28f47c-7f9e-31be-a2cb-555ca18f62d1 | -13.80939 | -45.82405 | 2025-10-10 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3900ee4a-b44e-3209-87e1-149141f019ef | -15.28839 | -46.15091 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 332fc6cc-eb56-317e-ab48-dff1150bb2d8 | -17.93709 | -45.03082 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d355a98a-3080-35d1-92af-e5575407d2e1 | -17.90252 | -57.49951 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c457837d-c1ee-35bd-a5ff-266222599be2 | -17.8276 | -57.62803 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 06a2343d-6a40-3623-8190-b359a9c0e95b | -17.9723 | -48.5668 | 2025-10-10 04:53:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e4efb40a-07dd-3426-8426-0a4fffe5f5aa | -14.2701 | -45.89396 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5849fd89-d97b-3d12-a144-f31b2a24e679 | -13.232 | -47.61219 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebe5054a-6064-382e-b6c2-672b62dd9205 | -11.71662 | -62.97785 | 2025-10-10 04:53:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1da492e-3499-3493-95d0-7c1334ce6b04 | -14.88723 | -48.23736 | 2025-10-10 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3dece812-a7bc-3a37-bcc5-2c4238d472f5 | -17.84598 | -57.5826 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6d32e9e2-2d0c-3533-8bb8-11a2670e4e67 | -15.09155 | -46.61088 | 2025-10-10 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 786abcae-6507-3119-95c0-072a9b42c76e | -12.09341 | -64.23567 | 2025-10-10 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c3bb3ce-bf14-3037-938f-2c244e22668d | -17.8257 | -57.66011 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2e9c4650-f0d6-3b21-8330-b1b035a96e3f | -17.99539 | -44.96287 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21aeb6c9-f31a-3907-8e0e-bac086a817d5 | -16.66909 | -47.60289 | 2025-10-10 04:53:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3246b03-dfa4-3288-8e7e-9287fce79b77 | -14.93575 | -46.77203 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e316bc5d-fa00-341a-878c-1cfc5c982691 | -18.10857 | -53.34591 | 2025-10-10 04:53:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f179dcc-ab72-30df-9ada-29a195965c75 | -17.88569 | -57.66337 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5bf8601b-d990-311c-bead-87375a106cba | -14.39393 | -46.00483 | 2025-10-10 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52468b22-a8d5-3f52-9620-65bb3d9f12a5 | -14.44047 | -48.01099 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbe5f716-486b-3920-b373-9d3075878368 | -13.27421 | -48.01876 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 930ab99c-3a15-338b-a4a4-dfc3c252532f | -18.04829 | -44.98216 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ac1d1e15-d7a6-36aa-b83f-ba11a820082c | -14.42454 | -47.99596 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc5e17ec-ab0b-3f4f-8599-a197289e48a7 | -17.93184 | -45.02662 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1ca0fe65-766a-332e-b690-240321ecae51 | -13.83768 | -45.88589 | 2025-10-10 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97905f5b-4296-392f-b859-aac50b31e828 | -17.38439 | -46.90285 | 2025-10-10 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 239bfdda-56ae-3285-88e0-7f928422cc46 | -15.46995 | -47.98468 | 2025-10-10 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 252975b8-6078-3275-9fb7-baa98d4356ab | -13.37915 | -47.75787 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de5591f3-c4ae-3623-afbe-d4a20fb04160 | -14.84545 | -48.46303 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 737063dd-1fe6-3c86-85ec-1256db36cda4 | -17.94357 | -45.02296 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fcf03b1-496b-3e7e-8175-c6cfbdffd32d | -13.36207 | -47.75143 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 02258cca-57f7-3d88-83ca-c243fb8ccd33 | -14.38426 | -46.00013 | 2025-10-10 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdd8ca22-4334-3794-8d56-3a53793834a6 | -16.43954 | -47.80927 | 2025-10-10 04:53:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a58cf109-bccb-3069-bbf4-4443a727cbdf | -14.44894 | -47.98056 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a60a648-932a-3db5-bfb5-e6ce3d0774f8 | -13.31395 | -48.47932 | 2025-10-10 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 063c1ef4-fc50-3ee7-9060-d223fd65ea0e | -14.99236 | -47.19765 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 24afecff-8a42-3c1a-b54a-a6dbf6ed3786 | -17.84772 | -57.65629 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README43.md)
