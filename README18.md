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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf2c83c5-01ce-3025-b7c4-0124024f8251 | -12.63783 | -46.88789 | 2025-08-20 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57a3f468-a267-36bb-ab0d-d4adaf6db9f8 | -14.99537 | -54.81836 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36eb5386-bfbc-3022-87d7-6c9c68e3fca8 | -12.97442 | -56.86014 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5a7bb610-203f-38ea-ad08-879bc78de236 | -16.4813 | -45.09628 | 2025-08-20 04:10:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc7c831b-fd0d-3e68-a1bd-10e8df858408 | -14.16164 | -45.28279 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eaeabe26-f071-3a19-969e-5e3970a58c8f | -11.77481 | -47.56556 | 2025-08-20 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 524aea9f-ef70-3284-bf60-72c837c36ebd | -11.09771 | -44.80968 | 2025-08-20 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 316fc543-de62-38b8-9fa4-a37c9c4f2bf6 | -15.37547 | -39.17374 | 2025-08-20 04:10:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 057e05e3-412f-3558-a7e4-b87fdeadc4d9 | -12.63485 | -46.88297 | 2025-08-20 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56e5f969-ecaa-3023-b174-e49c5fd8e47c | -18.34738 | -44.0309 | 2025-08-20 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4814862-83c3-346e-81bd-1a599598577b | -14.6266 | -54.89038 | 2025-08-20 04:10:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afa62ed3-a36e-3199-90f3-78930cf97f1c | -13.56511 | -47.00112 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9085ca35-72c8-3f6e-ac4c-271c20fe9f75 | -13.18518 | -46.87362 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e67b53f-fbca-335f-8971-a58668c64789 | -14.15423 | -45.28542 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 931e18fc-926a-33c9-91b2-d4751dcc949b | -12.98439 | -45.19818 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 47e96549-2bd1-389a-b869-f8bee3050330 | -15.64792 | -52.68649 | 2025-08-20 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2eeb7c0-6ea5-385d-8536-f43f110bad6f | -17.55951 | -44.48396 | 2025-08-20 04:10:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2eda052a-8da8-317c-ab15-a288ebe5a71f | -14.24445 | -43.30817 | 2025-08-20 04:10:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e38eb134-691e-3d73-aa7d-1ae14b925335 | -11.19347 | -45.06128 | 2025-08-20 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6be5d20a-5fa7-37fc-bdaa-a9b937e10221 | -15.3504 | -47.26638 | 2025-08-20 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3aae272-9c99-35ac-8d35-1f3415b257ec | -15.65125 | -52.68496 | 2025-08-20 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acc18c57-4e0b-3032-83ee-7f0b8b816c8f | -13.40237 | -46.3665 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4fe811bb-566b-3815-9949-bb8546943ef9 | -12.92003 | -46.10286 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b974484-f9c0-3699-a939-514bb507a99a | -13.00743 | -45.18649 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45b3f1b7-917e-3dd1-86ca-b24a47cbcf4c | -13.19973 | -50.7444 | 2025-08-20 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c026412-e1b2-3ba5-8eb0-c5dd2433a54a | -13.39113 | -42.04762 | 2025-08-20 04:10:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6564a145-669b-3f9a-9487-82e1de56efcd | -13.18506 | -46.8965 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ae8c766c-32ec-3a5b-9148-dae93d7f25ed | -14.88252 | -48.06699 | 2025-08-20 04:10:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00a8bda2-cd97-36cb-b78c-e5eb4b40d95f | -15.02247 | -54.83532 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fc2c251-09ae-3dc8-9cd9-b3730be08b30 | -14.7067 | -45.83869 | 2025-08-20 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a128b96f-c0d5-3967-9e70-da5376f9395c | -13.73842 | -52.01304 | 2025-08-20 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7cb20b42-63c9-3ba1-8600-685092ae6717 | -12.97907 | -56.87118 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5f3da9d0-0d00-3cee-8b20-38301a117a4a | -13.33869 | -54.42864 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 795a0f0b-fee0-3445-8eda-43911cc37390 | -13.35294 | -54.40626 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01d727d0-cc56-34dc-891c-320530340233 | -13.34703 | -54.40511 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45e943e8-cdbb-3527-a612-32632d2b78ab | -12.9716 | -56.87316 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba0d1298-2bc9-30c7-a70e-46c754a74e3b | -13.15952 | -54.93841 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89651ef0-e41b-3775-8696-b64cbe8ecd57 | -12.98719 | -45.20255 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fae16ce1-3164-3629-a907-971d77be7c20 | -13.61449 | -46.89021 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7952409a-7d68-3e1c-afcb-55f4cc2e0526 | -14.1683 | -45.28811 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76a5233e-2029-3470-bff9-7274aff640d4 | -15.54581 | -42.28058 | 2025-08-20 04:10:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 966b6154-317c-3e0f-94e3-f0a0c6118f46 | -11.3146 | -44.92309 | 2025-08-20 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4971455-7eb3-372b-9eb8-3689c2a39705 | -12.66958 | -44.95242 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eeb628a6-6241-3865-8d2d-99c4e684b69f | -13.74341 | -52.01429 | 2025-08-20 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fa7085d-bfcc-31fb-9fa4-120dd7edc105 | -15.87524 | -50.65929 | 2025-08-20 04:10:00 | NOAA-21 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ea340a08-b405-3e21-becf-64fc5aa87dcc | -15.40913 | -46.59454 | 2025-08-20 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c63b8ec-2c18-3dd4-b31b-c707d8137182 | -15.00319 | -54.81048 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1ac24222-e042-3c16-a95d-bba81f49d046 | -12.22308 | -53.60236 | 2025-08-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b28ee5c-43ab-3b6f-b33a-5b8d0e980230 | -12.87512 | -46.0658 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9ce8623-4f95-3005-900c-4b2271fc2f07 | -14.89324 | -48.08607 | 2025-08-20 04:10:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53b11315-44c2-3587-86e5-4b717d411900 | -13.00526 | -45.17832 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1176ecd4-efa5-3132-ae78-c52efe392834 | -15.42784 | -46.72114 | 2025-08-20 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aae15f97-bbc6-3e27-8520-239551ce28e3 | -13.5587 | -44.45849 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88af26f0-f9ab-3de1-91ac-5b2b9bc6c529 | -12.99061 | -45.20313 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 652dc5b5-6396-3a91-b616-ee87e49524b1 | -12.94235 | -46.16129 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1bdf4ce-cef7-3765-9a7d-ec8431b5877e | -14.35294 | -51.99513 | 2025-08-20 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95f1c0bc-f20e-3232-957b-559fc68c7882 | -12.9058 | -46.10058 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a4302b9-0a9a-32ee-9c1d-925c46ce9180 | -15.00434 | -54.81459 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9c07b143-8a71-3c60-b71f-a34950ed4aeb | -12.94664 | -46.15762 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eaf8d708-f04e-37a9-a9ef-b7a617d6400e | -12.97301 | -56.86665 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0cd5029-7452-36d8-9848-da073e9a8412 | -15.00338 | -54.81924 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 62b04243-8522-3ea7-b605-f62cfe1ba825 | -16.48189 | -45.09262 | 2025-08-20 04:10:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f22ec72a-0b98-3d72-b706-8af455df8fbf | -13.02977 | -46.79527 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4e61eb53-961e-329b-a51a-04d855fbe727 | -15.12727 | -48.71544 | 2025-08-20 04:10:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02b79016-f814-3a9f-8779-038d9073d5dc | -16.30997 | -50.18339 | 2025-08-20 04:10:00 | NOAA-21 | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0735a025-433a-3ae5-a0be-396fac32b207 | -14.98757 | -54.82615 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 66424cc0-2708-397c-a60a-759e3d9fcb7f | -12.61759 | -46.89457 | 2025-08-20 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27837911-3126-3696-87a1-6463b2cbca25 | -12.99619 | -45.21189 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 460e329c-f237-38ae-906b-32da449bad27 | -12.09344 | -47.9107 | 2025-08-20 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c44fc38-9d87-3ad0-9d0f-2f34e76c9099 | -14.15824 | -45.28222 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d47285c1-7484-3357-9647-4eef6e26c33b | -12.97362 | -56.863 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b2bc3b9-3862-393b-8b46-21de4817d107 | -14.61586 | -54.91222 | 2025-08-20 04:10:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e4035930-ec38-3bb9-b2a0-8f7f37431779 | -14.15701 | -45.28976 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb1baa27-855e-34b5-ac14-4b0049f6ac52 | -16.31074 | -50.17926 | 2025-08-20 04:10:00 | NOAA-21 | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ab195ee-01e2-3c8d-b848-361a7a936ab0 | -12.23374 | -44.63206 | 2025-08-20 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d23a8be2-7594-3716-8009-0fac0a3e226f | -13.87832 | -45.57625 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57ee10b1-8dd3-3d89-acdd-b7568d6cde47 | -13.18884 | -46.87438 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f44790a9-ced1-35c6-99d1-e706c82fc654 | -13.4844 | -47.05721 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aea8b6de-94b7-3a6a-adce-857500cd848b | -13.15072 | -54.91845 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5ca8822b-1e66-3416-b88e-cc810d43ea4f | -17.41376 | -46.69508 | 2025-08-20 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f830dfb-5fa5-354e-918a-3288bb1e9587 | -15.42854 | -46.71696 | 2025-08-20 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1039d324-eae8-3d0c-b159-26b2d26deb91 | -13.14924 | -54.92615 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8185bb77-044e-3108-9d7e-e1e2079cd50e | -13.15852 | -54.9434 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a469d2fb-df32-353a-8954-8c80ab35418a | -11.09428 | -44.80911 | 2025-08-20 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 785a8571-d226-36c5-8ebe-269cba980aa8 | -15.54189 | -48.56749 | 2025-08-20 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9fc487c9-4af2-3764-91d6-eabfc78e0c93 | -16.74131 | -50.0457 | 2025-08-20 04:10:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 479b7238-ed63-3421-8867-d85f9372e38f | -14.89583 | -48.07156 | 2025-08-20 04:10:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 80dfcb46-933b-328b-8fa1-df17387a29cf | -13.32703 | -40.34076 | 2025-08-20 04:10:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 41182dfb-40a3-3510-8ebb-74077814a2c9 | -12.97769 | -56.87778 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a4d0884e-b7ea-3474-9484-24eff4c22824 | -12.49565 | -44.78925 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e55b582-54ee-39db-b498-cc4b93d2f355 | -14.45875 | -48.36943 | 2025-08-20 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0bce8b2-ef0a-3b69-b959-eaf1edc9d2d1 | -14.89117 | -48.07553 | 2025-08-20 04:10:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4c58144-67d1-33a8-a4e4-a8d03aa68e54 | -13.14868 | -54.92825 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 66247806-4ed0-3fb0-a795-4cea02a5302a | -14.74308 | -46.29819 | 2025-08-20 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd94f5ea-cf4c-3d69-a8b5-c7dce2a8d1ec | -13.1749 | -46.88943 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a50e4a27-53ab-30ef-a2fe-dc8cc548f46d | -13.58646 | -47.00935 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfd2a0aa-521f-369c-84f5-241f58b7cedb | -13.14115 | -54.93469 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| adf707c9-76d6-3869-a907-c06f0afe22b2 | -12.6661 | -45.81854 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 499b5e2d-7589-3f79-bec3-502c4a5967ea | -10.47159 | -48.35389 | 2025-08-20 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4575ee2e-6e40-3a15-8bd7-62f64cfbc247 | -15.00246 | -54.82375 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README19.md)
