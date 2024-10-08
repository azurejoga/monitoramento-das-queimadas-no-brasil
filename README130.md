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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e514066-eb57-398a-9525-29c411730e9c | -12.57295 | -53.05913 | 2024-10-08 05:33:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 7096cbc4-d400-3e4f-a37b-ba107ed0a295 | -12.57124 | -53.06982 | 2024-10-08 05:33:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9fa863cb-85a3-380e-a5c7-fcc6c32819eb | -12.58256 | -53.06065 | 2024-10-08 05:33:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| cde50396-a12d-3045-ae05-e5a0bf7073e4 | -18.98496 | -50.20124 | 2024-10-08 05:33:00 | AQUA_M-M | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 779a8fb9-8068-3ca3-89eb-dca45c726439 | -18.55402 | -52.63375 | 2024-10-08 05:33:00 | AQUA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| deb83e7f-c482-3db4-9734-dda700f7ab00 | -18.50114 | -53.43601 | 2024-10-08 05:33:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 24.7 |
| d3e51de0-9248-30b4-9358-1fe9b0f85df7 | -18.49955 | -53.44596 | 2024-10-08 05:33:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 91269884-29fe-387a-bc08-d65758e841c3 | -18.49796 | -53.45589 | 2024-10-08 05:33:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 42aa9209-98f4-3f83-8caa-b6aef1fc59ae | -18.49638 | -53.46581 | 2024-10-08 05:33:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 517b3310-6435-31a3-99c1-2645128d0a35 | -18.49316 | -53.48589 | 2024-10-08 05:33:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 02ee8f9a-53b9-3f41-89e3-973477d758b6 | -18.49201 | -53.43439 | 2024-10-08 05:33:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8173bda5-f3a1-3762-950e-0153408de372 | -18.49042 | -53.44427 | 2024-10-08 05:33:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 27.0 |
| db3c44e9-0e17-3a5b-8c15-41021be71e36 | -18.48883 | -53.45417 | 2024-10-08 05:33:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 27.4 |
| d9fe39cc-58cb-349c-b172-4aa668889f68 | -18.21042 | -54.4487 | 2024-10-08 05:33:00 | AQUA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 48a9da96-3200-3505-9d69-b397d42c873c | -17.71484 | -53.03696 | 2024-10-08 05:33:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c9a6b61a-59c2-3b1d-b228-f5092eea3444 | -17.67096 | -53.0197 | 2024-10-08 05:33:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 02fa0b16-68b4-3a38-bc72-f3dc15bddf8f | -17.66943 | -53.02944 | 2024-10-08 05:33:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 741583ad-8119-3c08-b62f-faff350198f3 | -17.66036 | -53.02789 | 2024-10-08 05:33:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 398504d5-72e5-3a8d-8efc-a2d6bb5f6f87 | -17.16442 | -51.68924 | 2024-10-08 05:33:00 | AQUA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fbb5f2ff-3ff9-3f3d-8207-bd15baed6038 | -17.16303 | -51.69847 | 2024-10-08 05:33:00 | AQUA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e5b9d894-4ed7-3862-8a92-f97dd43ce370 | -16.88438 | -47.13042 | 2024-10-08 05:33:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4c45a4f8-2cfc-3eb8-8dce-ae2f09e93a1e | -16.59015 | -46.48188 | 2024-10-08 05:33:00 | AQUA_M-M | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 273fdf83-0330-3c2a-80f8-26dd316a57be | -16.57156 | -46.449 | 2024-10-08 05:33:00 | AQUA_M-M | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 0e0821b2-d2ec-3dea-b543-2a8bd24bec13 | -16.56969 | -46.46403 | 2024-10-08 05:33:00 | AQUA_M-M | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 32bc5abc-f9be-3c1d-8ba8-055ff52c1f07 | -16.10794 | -50.22664 | 2024-10-08 05:33:00 | AQUA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 78469b20-3b67-3c21-86de-181011daf1bf | -16.10306 | -50.19719 | 2024-10-08 05:33:00 | AQUA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 345085e3-bd8c-33e0-ae79-eac741ed008a | -14.81527 | -50.80391 | 2024-10-08 05:33:00 | AQUA_M-M | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8cf7e3f8-d8a9-35d4-ad9e-211a56191ff4 | -13.2329 | -45.52948 | 2024-10-08 05:33:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| afe26903-421e-3bc1-94d6-4f285a027b7f | -21.97181 | -46.5485 | 2024-10-08 05:36:00 | AQUA_M-M | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| dba96ed6-e397-3d89-b8f6-397b7723dfc7 | -21.85116 | -48.41425 | 2024-10-08 05:36:00 | AQUA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 36040ad1-7f72-38a2-b29e-1bd72e46f6ce | -21.84945 | -48.42779 | 2024-10-08 05:36:00 | AQUA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 15.5 |
| dc0a9054-b743-3afe-b024-9e97fbfcf0b5 | -21.5839 | -47.91654 | 2024-10-08 05:36:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 7e096f31-a046-37f0-988d-bfc47bec675d | -21.39895 | -55.68214 | 2024-10-08 05:36:00 | AQUA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 018d03cb-03af-361e-ab0d-da8e650d77f1 | -21.34258 | -54.63731 | 2024-10-08 05:36:00 | AQUA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c3059ba7-dcac-346d-ba16-78c81adcd373 | -21.07133 | -47.22404 | 2024-10-08 05:36:00 | AQUA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 4f9ac64f-5f91-3976-8018-f024f94e6781 | -21.06009 | -47.22194 | 2024-10-08 05:36:00 | AQUA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 13.6 |
| aec036ed-1ea5-36c0-b410-bb35584c4ea7 | -20.42799 | -47.63936 | 2024-10-08 05:36:00 | AQUA_M-M | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 15.9 |
| c04d50e7-022b-323d-80e8-3aabb8ba0bb2 | -20.42628 | -47.65353 | 2024-10-08 05:36:00 | AQUA_M-M | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 583d74c4-d98d-3afc-a043-6985b656d221 | -20.4255 | -48.81291 | 2024-10-08 05:36:00 | AQUA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 48d63113-fc42-3aa2-9ab5-d720502e7b08 | -20.42459 | -47.66756 | 2024-10-08 05:36:00 | AQUA_M-M | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bfda68bb-d8af-33b6-80cd-36c7393d09e5 | -20.41549 | -48.81141 | 2024-10-08 05:36:00 | AQUA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 59.7 |
| c298f170-b729-35ab-8daf-2987d16b51c2 | -20.41391 | -48.82351 | 2024-10-08 05:36:00 | AQUA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 73.8 |
| c08ebe16-b505-324f-8b77-4326282ec118 | -20.40861 | -48.78571 | 2024-10-08 05:36:00 | AQUA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 98ffafed-1a68-3895-9bfc-8e8d15fce867 | -20.40854 | -43.92307 | 2024-10-08 05:36:00 | AQUA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.0 |
| 557ca2da-75e1-34ab-aeb6-237dd6c8b2b9 | -20.40612 | -43.9472 | 2024-10-08 05:36:00 | AQUA_M-M | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.5 |
| 2231e922-8a32-3058-9a1d-ecd90f78f6ed | -20.40547 | -48.80996 | 2024-10-08 05:36:00 | AQUA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 11724590-e321-340f-88bb-1592df091b28 | -20.40389 | -48.8221 | 2024-10-08 05:36:00 | AQUA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 6c559bfe-d0cb-3e4c-a025-3f12c66c250a | -20.40232 | -48.83416 | 2024-10-08 05:36:00 | AQUA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 62ad34ea-c2b7-3623-b331-bd7b130f0814 | -20.40076 | -48.84622 | 2024-10-08 05:36:00 | AQUA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 365974cc-2a6a-3c20-8c62-c40b4bb2dd76 | -20.39388 | -48.82061 | 2024-10-08 05:36:00 | AQUA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 43b2e456-1f8e-3c6d-bf99-d7b3869281dd | -20.39231 | -48.83277 | 2024-10-08 05:36:00 | AQUA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 64685f9a-5b82-3c75-90de-0c24bc5c9670 | -20.38232 | -48.83125 | 2024-10-08 05:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 3036e53f-3efd-34c3-84ca-9f57e5abfd4e | -20.3792 | -48.8555 | 2024-10-08 05:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 3173b944-1142-319e-8c35-25114f4009f0 | -20.37385 | -48.81784 | 2024-10-08 05:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 37018852-ed3a-3a48-9106-48a4d5f51699 | -20.3723 | -48.82992 | 2024-10-08 05:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 483.9 |
| 2f0a20cf-e504-3504-8dcf-41baa6fc1e97 | -20.37075 | -48.84207 | 2024-10-08 05:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 555.5 |
| d8a92fd6-dade-3721-ba3d-ab9bb408d6a7 | -20.36691 | -48.79218 | 2024-10-08 05:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 516ed631-3f3a-3470-8c2e-8c405e7c6fbc | -20.36537 | -48.80429 | 2024-10-08 05:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 665b0223-a275-39be-b068-23e3c99f9121 | -20.36383 | -48.81646 | 2024-10-08 05:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 85.3 |
| f38a49bc-f3fc-3a69-a62a-c3742dee705c | -20.36229 | -48.82857 | 2024-10-08 05:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 458.4 |
| ba8f94c7-ae10-3c97-930d-7484ba854fc2 | -20.36074 | -48.84067 | 2024-10-08 05:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 290.6 |
| 9c972e40-37ac-3bf5-bd86-d5643092de73 | -20.35922 | -48.85267 | 2024-10-08 05:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 609.6 |
| 5f4753f6-a434-3dba-9fd7-fb8db661d5b3 | -20.35074 | -48.83933 | 2024-10-08 05:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e137f32b-73a0-33da-a992-bfd741316b26 | -20.34921 | -48.85135 | 2024-10-08 05:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 24bd21dd-41e6-3ac9-a024-01048920327f | -19.72512 | -50.37366 | 2024-10-08 05:36:00 | AQUA_M-M | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 1a50a470-a4ca-3466-a2fb-5dab639e4682 | -19.72373 | -50.38361 | 2024-10-08 05:36:00 | AQUA_M-M | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| e4ec834c-c8f1-312d-9ff0-9ba0b7282597 | -19.71596 | -50.37225 | 2024-10-08 05:36:00 | AQUA_M-M | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| a5fd3f35-d934-3f75-a29a-54fda5441976 | -19.71457 | -50.38222 | 2024-10-08 05:36:00 | AQUA_M-M | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| e4fc2695-d044-3193-9787-9678585658fb | -19.39611 | -51.69473 | 2024-10-08 05:36:00 | AQUA_M-M | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f0be0e1a-85a4-387a-809d-8380b324ee56 | -18.91119 | -54.56609 | 2024-10-08 05:36:00 | AQUA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dda5688e-30c6-3077-99eb-f03a9ecb8bbb | -18.89863 | -54.46291 | 2024-10-08 05:36:00 | AQUA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 81d4341d-b99e-385b-85f9-75b26fb7e4d3 | -18.61476 | -57.23679 | 2024-10-08 05:36:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.5 |
| 0490a0eb-7e41-3d10-a153-7033db9396c6 | -18.61177 | -57.25331 | 2024-10-08 05:36:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 82481dd8-30d6-3c3d-8d39-7dcf7e315a05 | -24.25081 | -54.25108 | 2024-10-08 05:38:00 | AQUA_M-M | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 827374e0-0c7f-39a1-8ee8-fdf905eede71 | -24.24926 | -54.26103 | 2024-10-08 05:38:00 | AQUA_M-M | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 16d61dc7-bb23-3edf-9fb6-57736dbf3a8f | -20.37 | -48.86 | 2024-10-08 06:03:28 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e1a73766-ec19-3930-abce-ca42485aa41a | -20.34 | -48.84 | 2024-10-08 06:03:28 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ada8b08b-1aa6-36fa-9a71-255a97e7b539 | -4.90692 | -65.32629 | 2024-10-08 06:14:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d10f1140-5126-3a88-a775-b710670981f6 | -4.90617 | -65.3315 | 2024-10-08 06:14:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1193f37b-411a-3c55-bb39-d34440ad8ad0 | -2.4379 | -66.47485 | 2024-10-08 06:14:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5ab86b8-ec9c-3240-81f1-35e95c5b59a2 | -2.43364 | -66.47421 | 2024-10-08 06:14:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ebb767b6-1073-3d5f-8444-4145c80d8808 | -9.02364 | -60.43311 | 2024-10-08 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 853e166c-976e-3535-8d0a-014903e8f33e | -3.89275 | -60.59421 | 2024-10-08 06:14:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea46f319-e278-3793-9645-5c7c4c422b7a | -3.88631 | -60.5932 | 2024-10-08 06:14:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33c9d423-179c-324c-9115-f586c4702461 | -8.61176 | -63.09803 | 2024-10-08 06:14:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85f0d9b6-f37c-3650-8511-029fb7e17966 | -8.60536 | -63.10143 | 2024-10-08 06:14:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 045c4c23-b5f8-3b0b-b7ab-a1cb95729307 | -7.75466 | -72.26547 | 2024-10-08 06:14:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d5051c8-998d-3320-ba17-9683893f338f | -10.21702 | -69.06078 | 2024-10-08 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcda804f-29ef-32c3-b4fc-d4cc15a42f55 | -10.20379 | -61.95983 | 2024-10-08 06:16:00 | NOAA-21 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 53af5bb9-0039-3f05-8458-fbeb1d3b26c2 | -10.61656 | -64.42789 | 2024-10-08 06:16:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9ce2599-cd9c-3988-ba2c-70774466d85d | -10.61612 | -64.4314 | 2024-10-08 06:16:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae80423e-de64-3bcc-99ed-75329d1867e3 | -10.89966 | -63.91442 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ccde724-74a4-333f-9175-c0e71d26c40c | -10.89813 | -64.15793 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 22.9 |
| ea7aff9f-2fed-33e5-86f8-2823d696ac60 | -9.16611 | -68.32458 | 2024-10-08 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdfc2451-1916-3fb0-a4e2-5511d9ef857d | -9.88117 | -60.30861 | 2024-10-08 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6da60cc8-672f-3907-8a01-c5e1f8fb3a31 | -9.87411 | -60.30769 | 2024-10-08 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74f2925f-00d3-3873-8538-40722f7d6142 | -9.81279 | -60.46427 | 2024-10-08 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ff7b3aee-19f8-3cf1-a61b-6070249fd50c | -9.8081 | -60.44359 | 2024-10-08 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b9759e38-f26c-36e0-ae6d-0e163f520e7a | -11.26331 | -60.38869 | 2024-10-08 06:16:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 406339f7-42c5-3e18-b1dc-7f10a68d5edd | -11.26268 | -60.39452 | 2024-10-08 06:16:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README131.md)
