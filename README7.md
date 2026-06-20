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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 590f5c62-fbe3-345b-b17c-eafffa5bfc56 | -12.86071 | -44.36984 | 2026-06-20 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b1fb029-b16f-3eaa-9290-7475ca4ef2ec | -10.90291 | -46.32833 | 2026-06-20 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17c4e232-cb69-363d-ae98-b272e83b1990 | -8.95098 | -49.84637 | 2026-06-20 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97be8773-3af7-3647-8353-0bed38466079 | -10.76541 | -54.10735 | 2026-06-20 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c54081d7-45e1-3121-a63c-5459eb84955f | -12.13406 | -48.26601 | 2026-06-20 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0753e8a-baed-3866-a226-e97eb589b29e | -11.63176 | -48.53954 | 2026-06-20 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b743b987-8b18-382e-9f9f-9ea0c2eea912 | -13.83069 | -47.12604 | 2026-06-20 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f115d421-8191-3727-95b4-ef458e95b72e | -13.38288 | -42.39352 | 2026-06-20 04:44:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 1b7a2d13-f47b-33a7-abf7-f533088f3d98 | -12.54124 | -45.02588 | 2026-06-20 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| f0115df6-8614-3344-9720-90d623312c3e | -11.45027 | -47.40058 | 2026-06-20 04:44:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cdda9ca-5511-313a-96bf-11b745eaf259 | -13.19527 | -50.34466 | 2026-06-20 04:44:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ffe9c99-73a2-339b-936d-564096123d88 | -12.31732 | -46.73956 | 2026-06-20 04:44:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d68b2ba5-ab08-31fa-b034-f1b3016df5a0 | -11.64874 | -52.86547 | 2026-06-20 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cecabfe-768e-3db0-bc88-189f0beb7cf2 | -12.43355 | -58.4002 | 2026-06-20 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f079f5d-66cb-3f2b-814e-c5ed692da9e8 | -7.80534 | -46.45782 | 2026-06-20 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbf0b3ab-ae3d-37ab-b3e5-4d5b94cdd3d3 | -11.19816 | -46.56844 | 2026-06-20 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a0a69cc-008a-3a03-932d-a6db9a98ccd5 | -12.42462 | -58.41838 | 2026-06-20 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a50f54a-db69-34b4-a73f-9907e8e2e3e6 | -12.78332 | -44.48049 | 2026-06-20 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b210383b-8dfe-3f33-8815-4388e0898cbd | -13.20253 | -50.34219 | 2026-06-20 04:44:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 376db3c1-0778-3a95-8e78-6b089df76721 | -12.31437 | -46.73498 | 2026-06-20 04:44:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 450557ba-b039-3611-818d-450da34c5317 | -8.64914 | -47.76479 | 2026-06-20 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25fd3264-c9f5-392e-a0b6-f1db8a4ea6e8 | -8.65193 | -47.76886 | 2026-06-20 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b95c30ab-c547-3c57-a76c-fb85e5b8aaab | -13.38107 | -42.39145 | 2026-06-20 04:44:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aba0494e-c9e9-3078-b46d-ab18eb67115f | -10.60246 | -44.32019 | 2026-06-20 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a9bf06c-d1f8-39fb-aabe-1f4571dd9813 | -13.20195 | -50.34578 | 2026-06-20 04:44:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d7141c10-d6b8-3ee8-92ba-cc7765bbe02f | -11.44226 | -47.40702 | 2026-06-20 04:44:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ed492da-b322-378c-9199-edf7b2d64348 | -12.78737 | -44.48108 | 2026-06-20 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6167606c-4e8e-3662-a697-94ee9da7a97b | -11.66949 | -56.76503 | 2026-06-20 04:44:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfd2d104-7454-39c7-9f67-0fdb81df19d4 | -10.87992 | -46.34261 | 2026-06-20 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 849606cf-410e-3437-9871-c003671cca82 | -12.54514 | -45.02641 | 2026-06-20 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 8a50fe01-ba75-3dd0-b272-ddf4bc7c47fd | -13.19135 | -50.34769 | 2026-06-20 04:44:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 655d0194-cea8-3c10-8f1a-a4a6fc7a9e9a | -13.29172 | -45.21049 | 2026-06-20 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40707c6d-b828-384f-a970-72a898a95743 | -12.54585 | -45.02146 | 2026-06-20 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| c3d1b665-1aa6-3b8e-abff-a4d739cf81d5 | -8.63796 | -47.7485 | 2026-06-20 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fc6ac29f-ed4d-3783-92ba-12b92cc2f57b | -10.77872 | -54.10238 | 2026-06-20 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cb579d4-e6ac-3453-b428-10f40ce926b8 | -14.06199 | -44.4788 | 2026-06-20 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1efa4f7e-b31f-352e-a2a6-8d595efae69f | -12.92019 | -49.48561 | 2026-06-20 04:44:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bc70ec7-a9ab-3cbe-beab-ebd6e6b1fd80 | -14.856 | -48.12133 | 2026-06-20 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3d6a598-1f4e-3cbb-aebc-5aa9a28c614a | -13.29561 | -45.21109 | 2026-06-20 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1586cb39-8586-3da8-982d-03e5d85a6fce | -12.9141 | -49.48097 | 2026-06-20 04:44:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98d124ca-72d2-3445-9d24-cf6c46d9e7b3 | -7.29583 | -55.32111 | 2026-06-20 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1977e178-4aa7-3576-9806-fdf112d03bb1 | -10.23183 | -46.51341 | 2026-06-20 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eae8757a-a9b1-3ae7-878e-750e15cb700c | -11.06458 | -52.47684 | 2026-06-20 04:44:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f5e588be-5dd2-3f77-a159-a3a7cc69a41f | -12.78884 | -44.4703 | 2026-06-20 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f532153-af59-3b34-95af-ad436523ebec | -11.63231 | -48.53597 | 2026-06-20 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d856d1e2-325c-38b1-a7be-9d722e6d119b | -13.2942 | -45.22092 | 2026-06-20 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a18d296a-1961-3235-8327-674d07ac7114 | -11.88901 | -43.82949 | 2026-06-20 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dffdae43-2be5-344d-81a9-b3695dd80d36 | -9.71868 | -48.88385 | 2026-06-20 04:44:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13a3712c-f814-34cd-874f-3fe95387bffc | -13.3882 | -42.3892 | 2026-06-20 04:44:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 4d3277bc-674c-3b7c-b94b-62af24b3c286 | -10.76944 | -54.10803 | 2026-06-20 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a61e65d7-4a50-322e-a19c-95a1ef05b5ca | -11.81422 | -47.34129 | 2026-06-20 04:44:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdd41e46-1d6c-3dfe-9b47-61cd1bc506c3 | -11.03426 | -45.07815 | 2026-06-20 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b75bbe5-a349-31b7-ba71-52fcd1a70a48 | -10.93703 | -46.44085 | 2026-06-20 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d96ed56-651f-3659-ae28-fc033b5dbe6c | -12.55365 | -45.02253 | 2026-06-20 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 079e1c8a-1efc-355c-a830-c34ae2b7ce5e | -9.01456 | -40.99129 | 2026-06-20 04:44:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9c6b89e6-14e0-33a9-a9b3-1eec21c20ee3 | -14.33445 | -47.51448 | 2026-06-20 04:44:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fae9669d-64f0-3f7a-bf29-b786e6dab66e | -12.5154 | -48.29629 | 2026-06-20 04:44:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5aa36ab7-6234-3a44-a85c-6f72a60c3329 | -9.7454 | -47.87356 | 2026-06-20 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67616fb9-337c-362b-a90d-6e6a9df2a1de | -11.19051 | -46.57129 | 2026-06-20 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08241592-8073-35a1-aab1-15dc27c0b650 | -13.19861 | -50.34521 | 2026-06-20 04:44:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 85423594-b227-3f36-a32b-878636d33eb4 | -12.91743 | -49.48152 | 2026-06-20 04:44:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48156b33-44ad-32fe-b138-cc224c82068d | -10.76882 | -54.11158 | 2026-06-20 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eeb62daf-26ea-3026-b9d8-5f65579a3957 | -8.64804 | -47.77187 | 2026-06-20 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6403bbce-4287-37e9-95bc-a794d791cd73 | -7.36518 | -49.86319 | 2026-06-20 04:44:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dd7e11c-bee0-3e3c-ae78-c58936e11d8a | -11.81767 | -47.34183 | 2026-06-20 04:44:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e841d3bd-bec7-3d1d-afd7-3f1e2877827d | -12.79141 | -44.48165 | 2026-06-20 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fc3a3ef-cc72-3e81-a865-3ef5e1f38e23 | -12.54655 | -45.01651 | 2026-06-20 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| debe6286-530c-3a9b-ba82-d18e11ffd344 | -11.63511 | -48.54008 | 2026-06-20 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b301f603-9e14-39b8-8e73-5b1d897a74de | -11.8311 | -47.09759 | 2026-06-20 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b576fdc-1bb9-375c-a39a-278fb4859c1c | -12.91799 | -49.47797 | 2026-06-20 04:44:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 564658f7-63ac-36f2-90c0-5f59a429f7fe | -7.29666 | -55.31637 | 2026-06-20 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 60aaaee9-6e3f-3c55-bd46-2cd949e9e7aa | -11.19873 | -46.56463 | 2026-06-20 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41326bde-bce5-3f7d-b7ab-b9c3093554ff | -11.06822 | -52.47749 | 2026-06-20 04:44:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f8e2f35-9c3b-3101-a8c8-61b540c1e81f | -13.30235 | -45.2196 | 2026-06-20 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3daadede-9bc8-333a-a454-741a577db528 | -11.89318 | -43.8301 | 2026-06-20 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c149a89d-330f-3477-a55c-32fd213d0673 | -13.29102 | -45.2154 | 2026-06-20 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05752943-80f5-3861-8d5b-7978b523904e | -12.55436 | -45.01759 | 2026-06-20 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 442c472d-10d3-399f-9e14-466245b62eee | -11.80164 | -52.51217 | 2026-06-20 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2a06e081-aa7e-3d81-b5b4-7d0ccd219396 | -8.6402 | -47.75611 | 2026-06-20 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ef094bde-7439-3be6-a2b2-e34e87f1fcbd | -13.19469 | -50.34824 | 2026-06-20 04:44:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b6ce938-0d16-314f-8419-24b4d28f78ff | -9.62134 | -48.49108 | 2026-06-20 04:44:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e29a9529-d086-3a70-9af3-d5f347e51302 | -9.74876 | -47.8741 | 2026-06-20 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d3f10e7a-872b-3d20-be0b-7fb7e53ec815 | -13.29737 | -45.22647 | 2026-06-20 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fc6b035-a632-307c-9a8b-760f0267e7ed | -10.57328 | -57.32337 | 2026-06-20 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0299dca0-a361-308a-8d55-cab1244c0f47 | -8.64465 | -47.74957 | 2026-06-20 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 747fd460-dcde-3337-ae0c-8603cde18f3c | -9.16212 | -47.24813 | 2026-06-20 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd1e5a9e-7259-39a8-9a38-7596557e9605 | -8.97867 | -47.97554 | 2026-06-20 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98f6917a-fea6-3b1f-8f02-595355817cfb | -11.88712 | -43.83384 | 2026-06-20 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 565a6e7b-40d6-3972-99a3-992940f90a60 | -10.90626 | -56.85714 | 2026-06-20 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90f3944c-5650-3eda-bf1d-0020940a4df4 | -8.65528 | -47.76938 | 2026-06-20 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e02397bc-95e7-30fe-8b51-6ba02ff6166f | -8.65138 | -47.7724 | 2026-06-20 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf950841-d47b-3b1a-82b4-8e23134cd8cd | -12.79092 | -44.48524 | 2026-06-20 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0931c865-b009-3a40-b237-d7daebf91457 | -13.30196 | -45.22216 | 2026-06-20 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa972e91-bc28-3f72-8325-e26e51a8fdc3 | -7.79846 | -46.45671 | 2026-06-20 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bca89210-d034-300c-97d5-497530b6293b | -10.54839 | -53.7341 | 2026-06-20 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08823fbb-4e59-3e0f-b436-367b0cb2677c | -9.10408 | -49.65797 | 2026-06-20 04:44:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ad05c20f-213f-361c-a098-49caabbecf41 | -9.20568 | -58.06339 | 2026-06-20 04:44:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8fa1a9e-b051-33c6-b2ff-cd2b601da0d1 | -11.19462 | -46.56794 | 2026-06-20 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcde92e7-0f11-3981-a2f9-6ab125eab41f | -10.12077 | -52.17829 | 2026-06-20 04:44:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcee3cd4-fc2e-3717-924c-eac848afddfb | -7.8019 | -46.45727 | 2026-06-20 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README8.md)
