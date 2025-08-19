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
| 0cf36c23-d59a-39b4-9f9a-303a25439044 | -17.335 | -47.17579 | 2025-08-19 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02926ba6-54d8-38ce-a3ed-46f84e4a4702 | -16.47644 | -45.0933 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94bdde69-1904-32a2-9232-d1bddb2e4f67 | -13.18793 | -54.94334 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51d8afac-e37d-3246-b09e-9cc9b5c0978a | -14.62164 | -54.90157 | 2025-08-19 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ac66e7b-480e-36b7-ae66-435331ef1fee | -15.74775 | -46.61781 | 2025-08-19 04:55:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8e1c628-305b-38ee-a390-fb0325b9e1d0 | -13.354 | -54.40932 | 2025-08-19 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64f814df-b231-344a-893b-f11fe8e4b999 | -13.47996 | -47.07909 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86c21723-8334-379f-a73d-b28caff02444 | -14.97798 | -54.81054 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da1659a0-19fd-3f48-ba2f-1fdc618b7f30 | -13.24957 | -50.79831 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4542c8ad-095a-37da-a3e7-6fcbbb7c0ea0 | -13.86887 | -45.54503 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aeeb3aa5-2d6b-3df3-b091-32bd42d3f743 | -14.86391 | -48.07162 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45dd269f-1876-3f43-a352-6fc229b09877 | -12.98766 | -56.84558 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e26da12-74c3-30e2-a453-71a324c03a4a | -15.04452 | -54.82164 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4233c7b2-401b-342e-80db-a9c3f326f4e9 | -13.16668 | -54.94718 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fecf75f1-5eac-3617-b43e-cd61abcc20ed | -17.42006 | -46.70301 | 2025-08-19 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6218e4cd-af0e-3b81-aa0b-2eccb3fba39a | -15.76822 | -48.18006 | 2025-08-19 04:55:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bfeb242-f673-3a43-8269-2d7c4d3a1236 | -12.97979 | -56.85747 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7848fdb-4b27-370f-b8ca-ac2113ea3a72 | -15.01572 | -54.80949 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 36137c61-990d-3699-9b58-103213274524 | -17.40375 | -46.7129 | 2025-08-19 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e57e38ef-12c9-362f-882c-1a279738164a | -14.97189 | -54.80584 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c78fcafd-1d19-3f8d-b494-2e09c6b5a169 | -14.84821 | -48.05831 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c13d4d53-8281-3c19-864e-5fe05900461c | -16.71257 | -47.62719 | 2025-08-19 04:55:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d64121d-dbb0-3b33-bfc5-c583029af2dd | -13.35011 | -54.41232 | 2025-08-19 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fed3bd1b-1507-3584-adee-db6c3b1a4132 | -13.14672 | -57.15564 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c1f0f75-19c4-3073-b708-14d745c88ab7 | -12.50701 | -57.78429 | 2025-08-19 04:55:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e611962b-eba0-3508-b974-a7d9b94ee057 | -13.00398 | -56.83587 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a3b5c5b-4e1d-35c6-9571-23865f202c39 | -13.31252 | -50.80149 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 817e47af-196f-376a-8311-4149b8c22ac0 | -14.50722 | -45.94478 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ddfaccf-4a75-3798-8d56-ccf7cb7c8db9 | -13.18479 | -50.75783 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c518644e-8aea-3733-af09-5985e07e1740 | -13.15677 | -54.92331 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f64c119-196a-384a-b5b5-99942fccb22e | -15.03349 | -57.18747 | 2025-08-19 04:55:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fb6acf86-c838-3e27-b108-22511c24d44f | -12.99481 | -56.86812 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 628c8056-6420-33ef-bb3a-809153b48bcd | -15.39857 | -49.13091 | 2025-08-19 04:55:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f133532d-46a9-3896-981e-4cb277aa95e4 | -15.15837 | -48.77801 | 2025-08-19 04:55:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e977d148-28d3-373e-a823-8a37a1f63b88 | -14.86723 | -48.04562 | 2025-08-19 04:55:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b20af502-c4f4-32f7-af10-ce9343248b13 | -14.9891 | -54.80505 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4754a566-cb2f-3f4d-bcaf-42bca5d3ac36 | -16.4756 | -45.10062 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef10ecf8-7632-3d34-961d-8c7cf2d53562 | -14.84697 | -48.06453 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3708b22e-579d-385d-a2eb-3ab06c2378e6 | -13.18459 | -54.94278 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af810c85-b210-3cac-86d7-49eecc185408 | -12.97403 | -56.848 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5dd6115-32fe-3fbe-90cf-43950847bf46 | -14.96752 | -54.79039 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a131e7b7-6566-34af-875c-c18797ddad01 | -13.3028 | -50.81752 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 40b4bb1a-e43d-326a-8526-fcf136be3856 | -13.28524 | -50.81049 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c28e534d-9186-3d03-8f24-24d5c3a2291e | -13.29614 | -50.81214 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b3f7bf0-453a-3706-af26-88a7661bad5b | -14.97683 | -54.8177 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e118d3b-b382-3b72-b0dd-1b7052da2f41 | -14.98853 | -54.80864 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6e052b31-e5fb-3c9f-a949-e228bae6caa8 | -17.88819 | -48.60506 | 2025-08-19 04:55:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6313a020-a373-300b-a97f-0c3eaee946b1 | -13.01179 | -56.83305 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93b4fd93-a3f5-3385-9f5e-8becc6b0033d | -12.98335 | -56.8581 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 384a36d2-5833-32ab-af0a-f392073ac82e | -15.02846 | -54.81528 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4d87def-cb13-32c2-bbb5-e631f6124454 | -17.64109 | -52.20405 | 2025-08-19 04:55:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85925469-8124-346c-b88e-1900e7b15c5c | -15.0218 | -54.81419 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a3a6e473-005c-39ca-9ec4-d178906667bd | -14.97408 | -54.81356 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80d4def1-a28c-351e-90c5-59f24b4b8ceb | -13.85939 | -45.53745 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d98af115-c758-38c6-bd32-c1d4d8b29876 | -13.13301 | -57.14876 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47cccba2-3abb-3ca5-a8f5-c51ac3daf481 | -13.25496 | -50.81224 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42d53cc8-cd63-327a-84cc-48da305b1483 | -14.85025 | -48.07384 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99ccca88-5b0d-3503-a251-eec0253b6e07 | -13.00684 | -56.8406 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 913c35c1-098f-3a0d-846b-2c4c84d423a7 | -14.98642 | -49.56223 | 2025-08-19 04:55:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8813b29-e8bb-38f4-94d6-78b6661f6031 | -12.98198 | -56.85729 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a7d520d-aa0b-3d73-99c5-bcb2f26a83f9 | -13.16289 | -54.92802 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a341fad8-3baf-3416-bd9d-92dcdfa09c88 | -13.55441 | -47.01084 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7725353d-7126-30a1-86f2-e9ef626ccde3 | -13.18904 | -50.75409 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 832cf3e4-ec20-322d-ad64-1625784e09e2 | -14.31231 | -53.38002 | 2025-08-19 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6416d7e8-0409-38a8-9316-ffb0713af49e | -13.18549 | -50.75548 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 481d0474-24b7-33df-a267-8f0c0e153131 | -15.07931 | -55.42004 | 2025-08-19 04:55:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c4aae399-292a-3e8c-8418-86004a04f904 | -15.55351 | -58.70246 | 2025-08-19 04:55:00 | NPP-375D | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0ba2dee-b452-36eb-b7ba-fc1ca046815c | -14.98073 | -54.81468 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca5731f9-7f0b-3216-9d34-6867864adc08 | -13.14784 | -57.1543 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0d7b722-4055-3db2-be20-d9d5271dddd6 | -13.00043 | -56.83522 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dab8126-906f-344c-aa0b-2c2f4a99645e | -14.9774 | -54.81412 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71ae2f82-7d4b-32ac-9ebd-c30c672439de | -16.47723 | -45.08654 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6ad7820-b9d1-3327-9131-38b17a671e6a | -12.97693 | -49.36181 | 2025-08-19 04:55:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9fea9e64-1688-373e-9c79-054ce1933036 | -14.30951 | -53.37585 | 2025-08-19 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b4e12370-87cb-32a4-97c5-668e3173a7b4 | -15.02627 | -54.80754 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ba4098d-391a-3bd1-b99e-881a0a023f97 | -14.62818 | -54.92477 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65adbe50-1eb0-3373-8790-4abd96bc40bd | -15.01962 | -54.80645 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce13c6ff-91c1-3540-ba6a-5743ccbb870d | -15.75389 | -46.60834 | 2025-08-19 04:55:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f408c2a8-0c8b-35ed-bf32-80633ae8c817 | -15.19935 | -48.75791 | 2025-08-19 04:55:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5181f22d-23cf-343f-8ad7-060bfc62f86c | -13.16231 | -54.93163 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8589b55f-d85d-3b56-abbf-21c88f1cc2e0 | -13.31191 | -50.80577 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e9d1e34-76e6-3dee-a425-70f4c0803abb | -14.84644 | -48.0687 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61592f26-5bcd-389b-9beb-4ca6db742170 | -15.08266 | -55.42063 | 2025-08-19 04:55:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7655a141-eb56-38d6-a9fc-62f6d2699e86 | -14.4522 | -53.02898 | 2025-08-19 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcd56cac-b139-3dd3-8fc3-c3135070b179 | -13.58825 | -46.99514 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22887adc-80ed-3a2f-86b5-01dae05ecea9 | -13.6204 | -46.88962 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8274fd42-443a-33a8-a8d7-85410963d2c5 | -15.79303 | -48.22987 | 2025-08-19 04:55:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8511e59b-556a-369c-bffe-a25502e749c2 | -13.1854 | -50.75353 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f89e2ac1-d100-3649-81b5-154fbef4cbbb | -14.50793 | -45.93886 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ed55971-7922-34a4-ba13-a749890f04ed | -12.98608 | -56.84166 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ec7c075-8ded-3bb1-a243-f245d8281fbe | -16.47762 | -45.0829 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8b90159-cd3f-3448-938c-22236e0f5c39 | -13.46554 | -47.05508 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e8d57e3-b569-3ce5-ba7a-6703bbe6b142 | -15.80128 | -48.27087 | 2025-08-19 04:55:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b12c3cdc-fe86-335a-a30b-46845157faac | -17.4847 | -45.85722 | 2025-08-19 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58559417-13e9-317a-a6ee-8013b7af7510 | -13.86373 | -45.54446 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cda4c45d-113d-3379-a1e0-85fb6c9c612f | -13.18952 | -54.94309 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b97a064-e485-3f0e-aff0-1a08ec3e8c91 | -14.84589 | -48.07308 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e56c8505-9cd0-3836-b43c-bf1205fad9db | -14.62209 | -54.92007 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33b1ca40-b0a7-3e95-aec2-b9f4a4698fa1 | -15.76765 | -48.18447 | 2025-08-19 04:55:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b7817d9-922d-3c73-b39a-a7da58081b6d | -13.4814 | -47.0766 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README43.md)
