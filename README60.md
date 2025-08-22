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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08b6e83f-a8d0-39d3-b330-354821bafd6c | -14.7592 | -56.02727 | 2025-08-22 05:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d71ca826-7be6-3ac0-8143-9071b0b0b52d | -13.37385 | -47.48846 | 2025-08-22 05:42:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 295fdc47-6333-32f6-ae6a-4ec42bef6660 | -12.99689 | -45.22607 | 2025-08-22 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 55fedbde-859a-3fa2-926a-7b69d77c7cb0 | -11.12193 | -44.71721 | 2025-08-22 05:42:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 76885da8-0dd1-39a1-a99c-cfbc5ba70562 | -10.72886 | -48.22916 | 2025-08-22 05:42:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 1d92df88-30fd-354e-8096-dd870c33789b | -13.36291 | -46.25915 | 2025-08-22 05:42:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c0fb3e6c-fe69-3e67-b692-fd6e6265752b | -13.01916 | -46.33135 | 2025-08-22 05:42:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cb91657f-c5ce-3aed-a94e-53a6541ae41f | -12.95183 | -46.28518 | 2025-08-22 05:42:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| fa7d5884-9733-336d-809b-65429c5392fe | -11.81077 | -44.2553 | 2025-08-22 05:42:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 8e7c3c15-3ae8-3d54-a600-63373887d49f | -12.95038 | -46.29443 | 2025-08-22 05:42:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 156b3a0a-01f7-3542-82f3-348bf3e70de4 | -14.88551 | -47.95355 | 2025-08-22 05:42:00 | AQUA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 7a4e78d3-54da-3838-91d3-489eba7faf81 | -12.00097 | -44.65832 | 2025-08-22 05:42:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 033ce36b-67f6-3fda-a4b4-6ecb38f46633 | -12.93232 | -46.17782 | 2025-08-22 05:42:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c242ba8d-0550-3f4f-82cc-522eda4a6f0b | -13.37786 | -47.49442 | 2025-08-22 05:42:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8814dde3-c50c-34e3-aef8-df35095fb4d9 | -14.82783 | -47.92581 | 2025-08-22 05:42:00 | AQUA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 920d7e14-2293-3fd8-8005-6f9e2360e5df | -16.78577 | -47.65717 | 2025-08-22 05:42:00 | AQUA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a482679e-192e-37e1-a0c7-699e075c6cb4 | -11.31956 | -44.94071 | 2025-08-22 05:42:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a29a773f-e180-32a1-b000-1b7ae9db2706 | -10.86608 | -50.81831 | 2025-08-22 05:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 33755772-91d4-310c-a242-f7605a848b02 | -11.99962 | -44.66724 | 2025-08-22 05:42:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 5d4bbd98-6f8c-3398-9b42-9f56a034d727 | -10.28437 | -46.77261 | 2025-08-22 05:42:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4943fbd8-fe3f-3a18-9e46-12e33040d076 | -13.03125 | -46.31361 | 2025-08-22 05:42:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1cdcdd38-6db4-3747-b32f-d53d7f70ea04 | -12.95627 | -46.25691 | 2025-08-22 05:42:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fe37f7c4-2a68-3acd-9375-3bb50e4b7d49 | -15.88713 | -43.45642 | 2025-08-22 05:42:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 43.7 |
| b611f058-827e-3696-aa92-e88a22c5d367 | -10.86266 | -50.83853 | 2025-08-22 05:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 39.9 |
| dae61602-d919-3599-a5ae-2695e6f26add | -12.96531 | -46.2584 | 2025-08-22 05:42:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 6fc285e2-6336-32af-853a-d2e4e4ecd157 | -11.31074 | -44.93937 | 2025-08-22 05:42:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a955bcd4-920c-39b5-a633-89a45e6439df | -13.14437 | -46.88658 | 2025-08-22 05:42:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a2d5b713-4ecd-3d15-b65a-36ff7c36f66b | -15.15442 | -47.95181 | 2025-08-22 05:42:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| a020ad6b-f240-390c-b8d5-ad8944410359 | -15.88854 | -43.44645 | 2025-08-22 05:42:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 27.8 |
| b2cfeab2-efaf-31e1-b7b5-d72cc66aec9f | -13.0057 | -45.22744 | 2025-08-22 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d9a9f608-95a5-3238-8017-a8d50cc66557 | -14.88734 | -47.94245 | 2025-08-22 05:42:00 | AQUA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5937f8ff-0445-3575-a970-e74f34637f62 | -12.92478 | -46.16673 | 2025-08-22 05:42:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| deb249c0-b0d2-3e3e-85ec-5a8258f4d81d | -13.45997 | -47.04839 | 2025-08-22 05:42:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 90a05401-cc72-3e32-a77c-54542f3199db | -12.92332 | -46.17613 | 2025-08-22 05:42:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4b73b547-5def-386b-84bb-0b8e94ed006c | -13.02823 | -46.33278 | 2025-08-22 05:42:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| f5f165ca-5ee1-3368-82a9-b238ad05ff63 | -10.86379 | -50.82542 | 2025-08-22 05:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 2fc17277-6965-3b3d-94fb-dc0b23099365 | -15.89633 | -43.4578 | 2025-08-22 05:42:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 0406d200-c454-3fcd-a1d0-b30d065aab6f | -12.99551 | -45.23508 | 2025-08-22 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 4d28bdc0-7db1-39c3-b461-e8a31b0226ac | -13.02975 | -46.3231 | 2025-08-22 05:42:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7494dbbe-a731-39dd-ad15-7d433e4f5e4d | -14.89328 | -47.96632 | 2025-08-22 05:42:00 | AQUA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3ecd61e5-e84f-3ed2-8905-6be44ec1dc89 | -13.14269 | -46.89716 | 2025-08-22 05:42:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e9d5357b-a111-3a81-b372-1d2bdcb71b73 | -13.65112 | -45.70739 | 2025-08-22 05:42:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d6f329dd-bc63-3e33-ad5c-4f7f4fa90758 | -11.30937 | -44.94834 | 2025-08-22 05:42:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ffb2d525-8728-3239-a141-6eb0efc8dbff | -12.99826 | -45.21706 | 2025-08-22 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c51d385f-c790-34eb-96ad-7db9d63d321f | -15.89774 | -43.44784 | 2025-08-22 05:42:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f98e77b4-8880-31bc-b30f-861ebc7c8b13 | -12.95478 | -46.26643 | 2025-08-22 05:42:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3b253906-54bd-350a-b7ca-a70bdc005e7c | -23.19922 | -46.85373 | 2025-08-22 05:44:00 | AQUA_M-M | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 5c054ad0-d330-3021-8eb7-980c51e013ee | -20.23872 | -46.69636 | 2025-08-22 05:44:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ebe25533-c95f-3edd-adf6-bfb88dc772cc | -23.20968 | -44.89619 | 2025-08-22 05:44:00 | AQUA_M-M | UBATUBA | SÃO PAULO | Brasil | 3555406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 63e31382-098a-3da8-9171-7154087dfc21 | -23.29121 | -47.46901 | 2025-08-22 05:44:00 | AQUA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 6574f4d1-8b66-3f78-a344-f3369081cc2c | -20.24407 | -46.60147 | 2025-08-22 05:44:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1de0a905-98f3-3e73-8fd5-9de45a9ff344 | -20.23386 | -46.60932 | 2025-08-22 05:44:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7a5b2118-41df-3f7a-81f5-05489bf9de88 | -19.67301 | -48.98439 | 2025-08-22 05:44:00 | AQUA_M-M | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 24.6 |
| e1acf758-0a6e-3eb8-b068-bcf265821297 | -20.2946 | -46.63583 | 2025-08-22 05:44:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 314c372e-a0f0-3f54-b716-2cc4bb483bef | -23.30003 | -47.47056 | 2025-08-22 05:44:00 | AQUA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 6d546239-0f21-38e0-9d88-06ee11598676 | -20.26729 | -46.56713 | 2025-08-22 05:44:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a150428c-b2ec-3196-993d-ec661fe06384 | -18.88091 | -45.0215 | 2025-08-22 05:44:00 | AQUA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a6915040-1374-3781-80e2-b068fedc86b4 | -20.35973 | -46.5034 | 2025-08-22 05:44:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ff429516-bd15-3633-8bdc-ea1d6de928f7 | -19.68255 | -48.98612 | 2025-08-22 05:44:00 | AQUA_M-M | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ab15f7d1-dbf0-3427-8fcf-28e266693782 | -19.97394 | -44.92208 | 2025-08-22 05:44:00 | AQUA_M-M | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4627d04b-002a-385d-b79e-7588c5ce5be3 | -20.23527 | -46.59999 | 2025-08-22 05:44:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3618c4ba-8e05-3e68-bc98-2d47d57a8f1d | -21.23762 | -44.58247 | 2025-08-22 05:44:00 | AQUA_M-M | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| d2e04013-b77a-3580-8e0c-06a997402996 | -20.30339 | -46.63734 | 2025-08-22 05:44:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ed78b213-6b0a-3fcb-9a76-ad646893053a | -22.78281 | -44.78819 | 2025-08-22 05:44:00 | AQUA_M-M | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 0473a809-9319-3655-b8fb-d5880aa8a486 | -18.88229 | -45.01194 | 2025-08-22 05:44:00 | AQUA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b02cd849-d505-3b01-a6ef-745022241f75 | -20.24265 | -46.61081 | 2025-08-22 05:44:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| da4148d5-ec98-334c-a27e-b88645ad1780 | -15.8955 | -43.4523 | 2025-08-22 05:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |
| bba4b7d3-6318-3f3b-825e-08de6d84fce0 | -7.05419 | -59.82766 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f91dfdc-569b-39e4-acf5-39f65ced807d | -5.88098 | -57.75791 | 2025-08-22 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0cd6f221-9bce-3991-8a72-52c76e6d035a | -7.05364 | -59.83177 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fffb638-b244-37f9-b5f5-bc03f54af140 | -7.05474 | -59.82364 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9a940ab-4f85-34f0-938a-fb54740f4e9f | -7.5105 | -63.83195 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| daa15bbf-d6d0-3ab8-8834-a5c14d682627 | -6.89695 | -59.89636 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dae820c8-6d43-3a17-92d8-6437a9244ee5 | -5.44498 | -60.18071 | 2025-08-22 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f43dd9ac-ece2-3d1a-97ef-c0bae2553ebf | -7.55148 | -63.85336 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b079cc41-dfea-34d8-8b62-180cc9e2ff0a | -5.80415 | -59.22536 | 2025-08-22 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58fbbbcb-d6bd-37f3-9fe1-550669922f86 | -7.30546 | -59.63129 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 65a25ef7-5ab2-3406-998d-6b419a63a101 | -7.08778 | -63.08443 | 2025-08-22 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e3fdda2-ca95-37e0-9b2c-d03fd580f7d4 | -6.89706 | -59.89371 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebbd7ac3-12e5-34b3-a0dd-0d4292c71d43 | -7.50539 | -63.83577 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a72252d9-faf0-32b4-946d-593f88c23628 | -7.29364 | -59.62954 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 381d9b95-84de-3daf-8a3e-1f7b0aa33c0d | -7.43932 | -60.62896 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7908a311-5ff3-3cdb-9a77-b90d63c3c43f | -6.5736 | -59.87563 | 2025-08-22 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 414727d7-b035-3a9d-b86c-039d88c33552 | -7.58549 | -63.44215 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3053b1ed-55ca-369e-a1f1-d59c44143f4d | -7.94155 | -63.04594 | 2025-08-22 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8386a804-e5ee-3ad5-8cdb-c28ae15f8894 | -5.80181 | -59.21741 | 2025-08-22 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fdef00cb-e2ef-357b-b815-eee7d77c7529 | -7.5858 | -63.44063 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 054f8cb3-17ff-30a9-bc58-813d4a164e3d | -7.93752 | -63.04021 | 2025-08-22 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4f105fc-a0db-3267-9938-e3f0dbf04282 | -5.8053 | -59.21683 | 2025-08-22 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a351943e-a2d3-3136-a287-7ffc7ede81c1 | -5.43941 | -60.1799 | 2025-08-22 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd78b3df-ab8c-3d5f-9693-4497e3a0d11e | -7.55979 | -63.85904 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b8d49ff-a8cb-34d4-b751-769a0a1e3733 | -4.0945 | -60.66542 | 2025-08-22 05:59:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8659fbad-5ee8-3beb-bb64-604d7666a24c | -7.55719 | -63.84513 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c57c6690-1f5d-3715-a057-3d76e9336d91 | -5.80777 | -59.21826 | 2025-08-22 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48bb183a-2e9a-3e33-b839-22546207057f | -7.54763 | -63.84829 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 064e9aaa-8bb7-384d-bf9f-ed71b4d42675 | -7.58649 | -63.43588 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 041b387e-e814-3896-b659-1ce820a4f500 | -7.05308 | -59.83595 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0e2b544-ed60-35f1-94cd-df4c288f5776 | -5.8012 | -59.2217 | 2025-08-22 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e0f0ac1-baae-3987-b5ff-4ba518671132 | -6.62799 | -58.54136 | 2025-08-22 05:59:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6a2ea0b-1595-3b20-bbf5-e729e46807b3 | -5.43332 | -60.1828 | 2025-08-22 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README61.md)
