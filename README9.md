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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82685c72-984f-3171-a8a9-8b63ee33f07f | -13.92612 | -54.60785 | 2024-12-19 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ebd4c7da-53a8-33e3-b2dd-89cd795292ea | -19.35958 | -49.19633 | 2024-12-19 04:10:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abb07997-0cb7-36be-b576-7de3f50ac26e | -12.23371 | -54.31657 | 2024-12-19 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f566165-d1ad-38a0-904f-a2fad41b1c27 | -17.61062 | -42.55704 | 2024-12-19 04:10:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dbf920f0-e8b5-3d6d-b9f4-3fd0641fd3ed | -13.9193 | -54.61068 | 2024-12-19 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ca9cecd-49f7-3d96-8e3e-d04a60dbde7f | -17.66548 | -46.68156 | 2024-12-19 04:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7145faad-69d8-31e9-8c78-be5c0f1f3c3e | -13.31307 | -52.43678 | 2024-12-19 04:10:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cad533ab-57db-3501-815e-36988c008f6c | -17.75148 | -42.89242 | 2024-12-19 04:10:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b54ec23-c36c-3d7f-87b9-be891b75c374 | -13.92053 | -54.61327 | 2024-12-19 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 42aff905-d1dc-38fd-a152-d6cfbc96c899 | -13.91957 | -54.61788 | 2024-12-19 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9ca5792d-f0cf-367a-8c41-5d20a20cc27b | -12.23463 | -54.31194 | 2024-12-19 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fae59661-48c6-3b6a-a615-d2f0f55c9a28 | -19.67879 | -45.91002 | 2024-12-19 04:10:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee47a2ff-7647-3cc9-b0ab-57c3250fa392 | -12.22862 | -54.31048 | 2024-12-19 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cfd4b2a-f498-3270-a9ee-aee7d1811df5 | -13.92436 | -54.61655 | 2024-12-19 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ef22dcbc-a04e-3f4b-b15d-029361008248 | -12.23475 | -54.31448 | 2024-12-19 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b56e800-2af6-3df4-a9f5-f21d41149c7e | -13.92018 | -54.60638 | 2024-12-19 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d7c31a9f-b4fc-3d9c-b6d3-2df09ab3d557 | -13.92232 | -54.60473 | 2024-12-19 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9b06005a-ed38-38d5-8656-52c84dcfcc08 | -13.92647 | -54.61474 | 2024-12-19 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 04b0534e-309f-38c1-ac7c-e2ffcbe8f3a8 | -13.92144 | -54.60893 | 2024-12-19 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad1f2b32-adfe-39a1-9627-1ed50d50d622 | -13.31242 | -52.44007 | 2024-12-19 04:10:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0e9abce-6de1-3c05-97c6-42064ccc5278 | -17.97443 | -54.0063 | 2024-12-19 04:10:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7c9fa8c-69c4-3797-9dfd-67ffe43c6089 | -12.22165 | -54.31382 | 2024-12-19 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d151014a-bc2a-3c69-a3a2-4886b5d40127 | -16.51026 | -52.44075 | 2024-12-19 04:10:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7da52f24-4996-32d1-b5ce-1e1ce54c1ded | -19.06359 | -52.88937 | 2024-12-19 04:12:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d1e10773-a289-3825-be1b-e9c3edc8ced5 | -23.70414 | -46.36733 | 2024-12-19 04:12:00 | NPP-375D | RIBEIRÃO PIRES | SÃO PAULO | Brasil | 3543303 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1df826f0-e231-35bc-b24b-72e3e945913c | -18.73615 | -56.55711 | 2024-12-19 04:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| ec49f537-4824-3ba5-bafd-05f0b05d9d1d | -19.12305 | -53.45709 | 2024-12-19 04:12:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd163472-9c83-376d-8f41-17495623df15 | -20.77878 | -49.85734 | 2024-12-19 04:12:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 1786e780-7e40-3c32-9293-45917d7f44ca | -20.04844 | -54.90194 | 2024-12-19 04:12:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bc975a4-53a6-35a7-9a62-d430fe7a9c2a | -22.19945 | -53.15976 | 2024-12-19 04:12:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| db72e960-cc98-3954-86bd-9bba93c76f5f | -23.51993 | -46.97367 | 2024-12-19 04:12:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6fdb5682-76b1-358e-9e38-dc737142520b | -23.34009 | -46.77232 | 2024-12-19 04:12:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| af8f5530-46f9-3c91-85e9-b01370a7516e | -21.59503 | -48.49178 | 2024-12-19 04:12:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fa24ade-2d19-397c-9070-a566a4f1d4b1 | -19.12519 | -53.46141 | 2024-12-19 04:12:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cae41cfc-3f5f-3907-8326-9355b140f5c8 | -21.3352 | -49.21293 | 2024-12-19 04:12:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e410fac1-5bc6-38ab-bedd-76bb9e322cfa | -19.12241 | -53.4602 | 2024-12-19 04:12:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9376fe57-22dd-3efd-874c-fddfb91bfbad | -22.20057 | -53.15433 | 2024-12-19 04:12:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9702316b-00f0-3302-8f17-83a38530c0de | -23.70684 | -46.47775 | 2024-12-19 04:12:00 | NPP-375D | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0f67f752-53d0-3493-8fb1-b849481356e5 | -22.54979 | -48.36776 | 2024-12-19 04:12:00 | NPP-375D | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ad454c6-7e4f-3442-8b23-67c9bc1851d9 | -20.77976 | -49.85207 | 2024-12-19 04:12:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f7f4c66b-96ac-3fda-b321-7ca22cd0b40f | -20.04926 | -54.8982 | 2024-12-19 04:12:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47ffabd2-225e-3de3-8101-faf60c8267e9 | -23.32271 | -47.62567 | 2024-12-19 04:12:00 | NPP-375D | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b6c4ea1d-9982-376b-b2f2-46e31636151e | -23.04571 | -49.8953 | 2024-12-19 04:12:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 30657551-0040-36cc-a056-d70798aedaa4 | -21.33145 | -49.21211 | 2024-12-19 04:12:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fb25c450-9e55-3bba-ba71-bd826f0e47b9 | -20.76287 | -46.76896 | 2024-12-19 04:12:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 74fbc1a3-a06c-3cf1-b1a5-15328d46f77c | -23.70225 | -46.36769 | 2024-12-19 04:12:00 | NPP-375D | RIBEIRÃO PIRES | SÃO PAULO | Brasil | 3543303 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 45ce896e-b7d1-3f57-a39b-b34cd6cdc639 | -19.12584 | -53.45831 | 2024-12-19 04:12:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8ae2f05-3fc4-3a9d-9c5f-820dedea8213 | -21.59864 | -48.49249 | 2024-12-19 04:12:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c62060ff-230b-3892-bb4e-8e1e9ea8dc46 | -22.25389 | -50.04129 | 2024-12-19 04:12:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 236cb391-66ea-31a3-a527-89bd965a5fa6 | -22.54624 | -48.36702 | 2024-12-19 04:12:00 | NPP-375D | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66c0c92d-ed1d-3b85-89a7-81e03e94f5b7 | -18.74114 | -56.56364 | 2024-12-19 04:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0fa95b61-af40-34de-9e07-9c6f8881d8dc | -23.40686 | -46.55572 | 2024-12-19 04:12:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b5437853-da7c-344a-9231-910f4dde74f5 | -23.32614 | -47.62638 | 2024-12-19 04:12:00 | NPP-375D | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e68c37a1-2df9-3986-a6c0-9b4ee5e753ae | -23.7035 | -46.47712 | 2024-12-19 04:12:00 | NPP-375D | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 87ffb66d-6740-31fe-9b00-7bcee46f121d | -23.59282 | -47.43734 | 2024-12-19 04:12:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 35fb4171-b68c-3f42-9299-fa156bdbb98d | -9.68648 | -36.17845 | 2024-12-19 04:14:00 | AQUA_M-M | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 111.7 |
| 6b6cf06f-c2be-39c4-9f0f-706e027165e3 | -9.66845 | -36.19993 | 2024-12-19 04:14:00 | AQUA_M-M | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| e13dc4f8-0e5e-3a8d-abc4-1fd8951371a4 | -9.68234 | -36.2027 | 2024-12-19 04:14:00 | AQUA_M-M | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 107.1 |
| 66ef867a-8936-3d54-8da3-1dc038e90056 | -28.15035 | -51.85472 | 2024-12-19 04:14:00 | NPP-375D | SANTA CECÍLIA DO SUL | RIO GRANDE DO SUL | Brasil | 4316733 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 841a466c-6a48-32cc-be3e-bf0a5a164398 | -28.5859 | -49.44149 | 2024-12-19 04:14:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4984bde0-7fb9-39d8-af83-cd61c57cd8e6 | -3.2383 | -45.4941 | 2024-12-19 04:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 545b6943-b706-35d0-b290-3a2dfc6ff25a | -3.2197 | -45.4949 | 2024-12-19 04:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e1fa33be-4e92-3817-a2be-6aa2f95e5ab1 | -0.36895 | -48.50192 | 2024-12-19 04:27:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3c417f7-44cc-30be-b2bc-c5b24dd583f0 | -0.36147 | -48.50459 | 2024-12-19 04:27:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea934925-a254-33ca-92e7-578cab67e7cc | -0.3655 | -48.50138 | 2024-12-19 04:27:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 415462b2-24c9-3ab9-a54f-8b5ddbed238d | -1.75402 | -45.82487 | 2024-12-19 04:27:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c9380dd-c3bd-30a4-aba9-3d6bd9272d17 | -2.10418 | -45.67056 | 2024-12-19 04:27:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd3d20ee-d221-33b6-8b64-69d94c70cf03 | -1.78615 | -46.80921 | 2024-12-19 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dab898b7-8ced-3fd4-a201-27e7b07bc7f9 | -1.76022 | -45.58902 | 2024-12-19 04:27:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95a09041-bb69-32b5-af20-fabd3d806203 | -1.4683 | -45.74135 | 2024-12-19 04:27:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c3d4dc1-1b2b-363c-ba24-2befd78a7d37 | -1.83017 | -47.11149 | 2024-12-19 04:27:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 621f085d-228f-3ff6-a877-9016b679bbac | -2.31085 | -45.06791 | 2024-12-19 04:27:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 074a7c3d-5c7e-3292-a8b3-a00c2201f658 | -1.83348 | -47.112 | 2024-12-19 04:27:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38eae5d6-6058-324b-839e-ce8eb9e17564 | -1.75735 | -45.82539 | 2024-12-19 04:27:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22fea7d5-2fde-3c01-8dbc-7221aaa596aa | -0.36836 | -48.50567 | 2024-12-19 04:27:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe248591-edd9-31a0-91e0-bfb221c64e39 | -1.91082 | -46.10219 | 2024-12-19 04:27:00 | NOAA-20 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d02082d7-9ad0-3db8-9796-140866d6e4b4 | -1.75457 | -45.82138 | 2024-12-19 04:27:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9dbbbe6d-ccd9-3fdc-b955-18c114353f63 | -1.75347 | -45.82836 | 2024-12-19 04:27:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11d8d26c-5d36-31b2-8aa2-663242bf4a6e | -2.11424 | -45.69376 | 2024-12-19 04:27:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b509ca64-ebaa-3790-8919-d8f12b282d08 | -1.60217 | -47.17855 | 2024-12-19 04:27:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3b9ef0c-e1f4-3a14-a5fb-324d597d83bf | -1.7823 | -46.81213 | 2024-12-19 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d9b5786d-7b50-347d-9552-0785e1ae8b76 | -1.7579 | -45.8219 | 2024-12-19 04:27:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e5fafc1-3f8a-370c-8de7-c022214e5c53 | -1.87065 | -46.33648 | 2024-12-19 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6d26a89-43e3-367d-ae51-4b5b08d69690 | -1.83072 | -47.10804 | 2024-12-19 04:27:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d7ff217-49e9-3698-b43d-3838c5753b29 | -1.78891 | -46.81316 | 2024-12-19 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 64dd8ffb-c991-3a05-b62d-7cf644b79530 | -1.47186 | -45.93403 | 2024-12-19 04:27:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c630613-c4b0-3927-ba87-050b9e86d005 | -1.78561 | -46.81265 | 2024-12-19 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 67e7c4c5-17c1-307c-acc0-31ae375dc3e9 | -1.7568 | -45.82887 | 2024-12-19 04:27:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17e488fe-36ba-3043-b82d-0eb505a7c43e | -1.30018 | -47.7562 | 2024-12-19 04:27:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 25302c0a-aaa8-3615-9f61-dd0844962c29 | -1.60548 | -47.17907 | 2024-12-19 04:27:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b822932-d6fd-3f1d-9c7f-ce97288f0846 | -1.47163 | -45.74186 | 2024-12-19 04:27:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4417a9ca-5c93-30ae-b062-00621a7b8828 | -1.37958 | -45.95901 | 2024-12-19 04:27:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6909495e-27aa-3a51-9cd9-427b86faccbd | -4.15542 | -48.62813 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dacc47c-65dd-3281-bacf-8befc8d1e719 | -5.41618 | -47.57011 | 2024-12-19 04:29:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1dc3e7ee-4fed-39ae-8456-bff076b09f42 | -5.82784 | -35.48369 | 2024-12-19 04:29:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7aa8354b-dd78-3cee-b7b6-125443c5dd1d | -4.32923 | -48.30242 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7d7ef57-21ba-3a56-a9fd-adbc0696583c | -2.92423 | -45.24662 | 2024-12-19 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee213e38-be0b-3353-bb16-b0a93e77f013 | -5.62322 | -46.96484 | 2024-12-19 04:29:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0caa08e-b406-3798-a226-5350337d9f0d | -5.33713 | -37.45376 | 2024-12-19 04:29:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ca1b581f-62fd-3061-a74b-db2aef8671e2 | -4.6079 | -48.78688 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README10.md)
