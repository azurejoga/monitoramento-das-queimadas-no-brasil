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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53a8f221-0809-3509-8fc2-666829450417 | -11.27442 | -54.04498 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa81e056-d27c-3a4b-af7a-e521c568c0a3 | -11.02656 | -57.21161 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2eaa3307-3044-3244-b3d2-01cc2028cca1 | -15.63935 | -45.9261 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef5442cf-09b8-39a8-b1ce-6e1324538e4a | -17.29367 | -46.03541 | 2026-08-29 04:34:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8643662-4ab0-3f25-9818-2a8f5456b73d | -11.48232 | -46.93671 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76c5ec12-4f3d-3dec-9825-a6176241f171 | -11.24244 | -53.9978 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fdb4b4f-6235-3d34-8cda-85c384b269ee | -11.04203 | -57.22887 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 44e195ed-72f6-33dd-a6b7-616fb72c9959 | -12.43068 | -43.41417 | 2026-08-29 04:34:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a016ae2-c183-3f52-a46f-0e07b163318c | -11.04524 | -57.21428 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3955f605-54e3-3889-9d61-dba0ac0ee90e | -14.75689 | -48.74908 | 2026-08-29 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04abdcf8-a1d6-3bca-b76c-dee14040938c | -12.18819 | -50.56413 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4769d637-8ec6-37f4-8eb8-ae6d4860a4d2 | -14.43252 | -52.58413 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b296a4c9-a3a3-383b-abee-8dabd1316f9a | -12.38051 | -48.18826 | 2026-08-29 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7b2b872-0908-3b54-9b51-0b27e8b553e4 | -13.93788 | -43.9957 | 2026-08-29 04:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb6e88ca-a9d9-363f-9c09-668bdc2e3060 | -11.04344 | -57.22357 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d0204c7-db32-3fde-a680-d70879222772 | -14.91832 | -56.33641 | 2026-08-29 04:34:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 67402a01-b1c3-3726-96d1-417468067d55 | -14.41294 | -52.57152 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00b3c312-9655-39c9-8491-597b7d86cc0c | -10.89027 | -50.50048 | 2026-08-29 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a31cd3c0-d615-389b-b6ef-c55d1e6e3a83 | -14.90084 | -56.33989 | 2026-08-29 04:34:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5043f161-d97a-3e77-a67c-253e977b93c7 | -11.71045 | -54.54332 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9ba59e2-d18e-34a4-af34-3d3959217c8d | -14.18863 | -48.75624 | 2026-08-29 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ddf9101-6393-3755-aa32-abd79a7a710e | -11.18063 | -51.29108 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07e41b04-3bb2-37ad-96cb-fb68326663ed | -11.48538 | -45.06549 | 2026-08-29 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f2579ee-1a58-3c1d-aceb-9a88a1ec9dad | -11.27164 | -54.03248 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| baed3478-27e9-378d-998e-4de5fbdcbcc0 | -15.36949 | -52.67952 | 2026-08-29 04:34:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4e6ccf1-29be-340f-b321-8ef3be20cd2b | -11.02206 | -49.683 | 2026-08-29 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 959c54d6-43bc-36c3-b6a8-651f7fbee515 | -11.02581 | -49.68365 | 2026-08-29 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 213a49ca-fa60-3b38-9ac9-0109095cc4a6 | -14.15455 | -52.83899 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1350b4a-d846-35b3-9244-be0fa8ba9531 | -10.88633 | -50.49978 | 2026-08-29 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| febe4c43-3989-3002-9ad3-4b4824393f73 | -11.80667 | -47.21605 | 2026-08-29 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9d14fdb8-e6cb-31f7-abfa-8b279de832f4 | -10.75753 | -53.97848 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf94c7fb-3484-3eed-83c1-577d453efaa6 | -14.91902 | -56.33294 | 2026-08-29 04:34:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dab6cd6d-bee5-3299-855b-c210f3efe422 | -12.19854 | -50.55077 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d5e67fd-fb6a-36b4-9c9b-563dbe4ebafd | -11.23897 | -47.0482 | 2026-08-29 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88e634c8-9bcb-332d-b239-241ddc000897 | -11.71721 | -54.53534 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a11d1d3-47a8-3c19-aaa3-1130c9d65520 | -11.04387 | -57.21975 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a61cbf5-a9f6-321d-af16-74386e15b2b8 | -11.18015 | -51.28256 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cda14fa-ffdd-38ab-a15b-6447b7eed1b4 | -11.78011 | -47.65575 | 2026-08-29 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1672facb-31fa-3671-af75-0463f65c17a5 | -12.42358 | -43.41309 | 2026-08-29 04:34:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 239591e5-0ca6-37a9-b93a-6b388db71b7a | -11.02985 | -57.22657 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6737ba17-e8cd-3929-a609-404eb77e146f | -14.40722 | -50.05044 | 2026-08-29 04:34:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d91fb0f5-10a7-39c2-9cd6-864c7363d387 | -11.04481 | -57.21506 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a8a3988-6b12-3ea0-b97a-2aedc150c923 | -14.19545 | -52.86011 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce90826e-b6d9-3e92-8e5f-e2468a5805bf | -13.65168 | -47.75475 | 2026-08-29 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16aa9e8f-eabf-3bf0-9fc8-ff9111b105d3 | -14.12088 | -44.2174 | 2026-08-29 04:34:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e0c2c8a-ae15-3dec-a8c5-26feecf42c2a | -14.40798 | -52.57456 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a24dab1-c32d-379d-b4a8-c09b46882304 | -17.51061 | -40.25936 | 2026-08-29 04:34:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e08c33ad-d1b9-3197-a8df-c2d047299cb9 | -14.76034 | -48.74963 | 2026-08-29 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1b9b61d-5636-3658-a5f5-60b6cf41c6d0 | -11.0276 | -57.24003 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4301cd8-d074-3a74-b2ba-56f9c6e4a962 | -10.88295 | -50.5022 | 2026-08-29 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 324363f2-6d6f-3426-b948-6ba575f7d7f3 | -10.53672 | -50.77702 | 2026-08-29 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70e3be09-ff49-3abb-815f-3db8c52e7394 | -11.2305 | -54.00694 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cec1bafc-fb68-33fa-93e9-1916ebd46970 | -14.90691 | -56.33751 | 2026-08-29 04:34:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e024c067-ae53-3102-8840-1e969f2d2cda | -10.80986 | -50.64259 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 209d4d50-c14f-3a3e-ac5e-3f32ef9c8608 | -11.22905 | -54.01163 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 524546ec-d1b8-3781-b71a-fc0c1b3865fd | -10.75799 | -54.03174 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff41f598-c5b3-30e5-9fe4-2de86dd93984 | -11.23647 | -54.00238 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12c56493-14a9-3880-9325-69a391c04b86 | -11.03077 | -57.22201 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2e3d1f49-4e32-30bd-8a8f-95a1d03ac93f | -14.4283 | -52.58322 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ff34c48-bc63-3fd9-95ce-04f38dfaa6c0 | -15.57712 | -56.28799 | 2026-08-29 04:34:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85999023-73da-31b1-9211-d6bf2be48e18 | -11.03213 | -57.24655 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 479a3d90-3530-3114-acf8-4a52b4213eaf | -15.64634 | -45.93401 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 602b63ce-567c-3644-9ab0-384e8f560b43 | -11.03122 | -57.25106 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 51c486de-0289-302d-af08-72de85f81b8c | -14.91233 | -52.61837 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83560440-0580-35a7-a682-0ae2cadc52dc | -17.2412 | -46.92083 | 2026-08-29 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d35ef38-bf78-3722-88f1-7b0d697b0fb9 | -11.22824 | -53.98813 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55979544-6884-35ee-9c53-07e6828176c0 | -17.27568 | -46.01715 | 2026-08-29 04:34:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbb3c6a9-b71d-351d-86fd-bcc5d64278eb | -11.70653 | -54.53631 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1c5734d5-840a-3cef-9afb-9f43bb4548ca | -15.5609 | -49.95618 | 2026-08-29 04:34:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcf4e20e-9a91-3ae4-a4fa-f523c73da0bb | -11.29135 | -54.03638 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89b1da8b-7be0-30ce-b415-d6435ac14d39 | -11.28044 | -54.04012 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2094db4-6d60-3cf0-8a47-983cff8c82fd | -10.75695 | -54.0374 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5dd46ae-d19f-39a2-8744-910dc841ecec | -14.19973 | -52.86124 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1526d523-9dc8-3070-b2f9-29bef44369e7 | -11.26281 | -54.02509 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0622801-6497-3cf8-b9a5-281e0a1597c1 | -13.66142 | -47.73762 | 2026-08-29 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4551fc08-78cf-3a15-b51c-21218c9616df | -11.26174 | -54.03079 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e1fec61-53ca-3b33-ba58-6cf5d8bde8d0 | -14.97991 | -52.60239 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b4e8e50-e8c6-32ae-80f2-541b95790871 | -12.24537 | -50.53397 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67916738-0b71-3427-a6d4-af00a80a03cc | -11.17738 | -51.27435 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72860121-3a0e-38d8-9b71-467b818b1e61 | -11.61232 | -46.72729 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87e919bc-d970-37dd-ae46-75f5b3443927 | -17.24396 | -46.92501 | 2026-08-29 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85cf654f-6dc7-3cbd-b444-dc136f8ee0f3 | -17.27906 | -46.01771 | 2026-08-29 04:34:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54a4cc6d-3335-346e-8b41-36366e399fcd | -14.93646 | -56.3296 | 2026-08-29 04:34:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 878bbc31-e944-396b-ae43-32506014dfc8 | -17.39808 | -41.59598 | 2026-08-29 04:34:00 | NPP-375D | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a813d205-9c92-3b5f-a59f-cfe2bb5a44e1 | -11.03686 | -57.22314 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d7cb3f68-870c-3dd5-9840-1fab405b9f37 | -13.16915 | -55.65934 | 2026-08-29 04:34:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 37dc5382-b92d-3e7d-b690-b8e92acece30 | -14.90155 | -56.33636 | 2026-08-29 04:34:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c8203a7-d524-36dd-9e05-49126dc686fa | -13.65529 | -47.73278 | 2026-08-29 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8740216-9276-35f5-8025-06cdacecb1b1 | -11.2337 | -53.99011 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32f830ce-6f52-3e91-9009-b36db0fba94c | -11.03308 | -57.21194 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1c8294b1-67a7-3405-91d0-33bea247b05f | -11.19586 | -55.09415 | 2026-08-29 04:34:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4a9a68d-4dca-396d-bcb9-521448394400 | -11.19056 | -55.09318 | 2026-08-29 04:34:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0908bee8-6a7c-3e19-a2f1-e1ded5c7e6f8 | -12.22434 | -50.54026 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3246c223-cca2-30df-9339-1d67627737b0 | -14.93717 | -56.32606 | 2026-08-29 04:34:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f766f329-6cc1-3ad1-a679-c08fba96d0e9 | -14.9081 | -52.61765 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f3ac19b-2bc9-30f9-8a18-940c047769f7 | -11.02201 | -49.68024 | 2026-08-29 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77f32c76-e917-3e56-9782-2c55f94b67b7 | -11.71329 | -54.52833 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55cdf0bb-4dab-35bc-aa4a-4758483e77f2 | -16.73579 | -49.28771 | 2026-08-29 04:34:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 764eeead-4047-3d34-9257-b09233366894 | -11.23704 | -53.99575 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 958ddf68-8f49-3a51-a408-1404683fafd3 | -14.94252 | -56.32722 | 2026-08-29 04:34:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README37.md)
