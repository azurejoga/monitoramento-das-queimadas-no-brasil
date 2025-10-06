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
| 4e0399d0-095d-37f2-8482-eba63061c87f | -10.69511 | -47.98024 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 153c9d10-d0b4-35d5-909b-4d633915c1b3 | -11.80404 | -45.1165 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7fe543d-a91d-3faf-8bf8-410ef88ee466 | -15.34312 | -47.314 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 89b8bc04-87dd-3765-b8d2-24d6a42bf76b | -9.67748 | -49.94913 | 2025-10-06 04:27:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37b6548e-4053-39ad-9053-507dcf03c8d2 | -11.52845 | -47.68129 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58840321-8f09-3d8d-9857-a0b96d001c16 | -13.09527 | -47.86873 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e91e4a8-6cdd-3b78-9895-ebf664150c68 | -9.67616 | -49.95727 | 2025-10-06 04:27:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ea759a1-e8ea-3706-a9ab-801d97face2b | -14.65571 | -48.35394 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57d451b2-c1e2-3804-b4ff-d63a446e7b76 | -11.14928 | -47.94986 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bdbce8f-5221-32aa-b019-afdfcce41bcc | -13.26734 | -47.81017 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5873d9f-3623-3318-ab49-e7380f5e3463 | -9.39115 | -45.86805 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fbc7a90-fae2-3005-a80b-2f51fe351b52 | -13.07988 | -47.88064 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ad1e8d5d-01f1-3f1a-91b2-45b55b52dbc1 | -15.44057 | -45.87435 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b13f962a-1f6c-3aef-aabb-90ef33cdc30c | -14.85925 | -48.33697 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a74d513-1db8-3a5e-bf82-466f8b4fa094 | -13.05495 | -47.90544 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b721d72-647e-3e6c-8c1f-83b6325c5473 | -10.62342 | -48.6851 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01f1ec5b-50b1-3ad9-a8a0-2b7bb2a56c67 | -16.02652 | -51.0341 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9e3033aa-0d01-3efb-9c43-c24a183bf3e9 | -11.15536 | -47.93283 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e5cd495c-01de-3705-9eaf-94ba31740588 | -14.53665 | -46.96205 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac5815a6-d498-3e40-83ce-e926092de35c | -15.5133 | -46.84462 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 882ce2fe-f981-31f5-bc4c-81f9b4c205e8 | -13.12599 | -47.99633 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2df37625-8d2f-373d-969c-2cf1abc251e5 | -13.71995 | -48.09411 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14fc426a-1375-381a-a3c4-ffa6cb6db2f3 | -12.48334 | -45.54394 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8664c136-9c3e-3004-9eb2-feafbf2082ae | -12.47477 | -45.55436 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 324de4b3-1249-38d5-a2d2-b94d9a64e54c | -14.91167 | -46.84132 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e63533e-8b17-341e-a3c3-8287fcfbbe3a | -12.16724 | -51.43214 | 2025-10-06 04:27:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ff77325-8fcf-3ac7-b0d9-3d1b2cef5d32 | -10.70448 | -47.98534 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 248b7a21-4b8f-32fc-b343-dcc4687e59ec | -11.48851 | -44.97425 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7ade88a-0802-30f9-bd43-9253aa37074a | -10.42514 | -50.34546 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26a2b04f-c1b4-39ad-bcd1-b01e55b9bfa8 | -13.73373 | -48.07102 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 428b8142-526d-37c6-b6bd-36a6410954fd | -15.49157 | -47.9234 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82a74615-53fe-3938-a878-035eff469089 | -13.35914 | -47.59447 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2edf1d33-360c-3c26-bd40-d679ab405c6c | -11.6616 | -44.26666 | 2025-10-06 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46dd2e7f-212c-38c9-9ab9-8abb092d7e03 | -14.6888 | -48.29403 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36638a4f-9b3d-39b0-957f-cd71f1eff67e | -12.91 | -47.28642 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e1b7ed84-1e90-334c-9f1e-d4507bd72145 | -11.83949 | -45.09324 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26436224-416c-349f-b4c3-3e5a95205edf | -14.92391 | -46.8286 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81535b7e-a346-3bf2-acb7-c1826ac4f9a2 | -15.50319 | -46.84299 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 423f04b0-f8d8-375a-9ead-248187db538f | -12.71616 | -45.86252 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d17ff402-292e-3306-ada5-a3c16ab84714 | -10.47523 | -50.44417 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93b13ba8-4926-3328-a011-1ee5a4cae07b | -13.56481 | -48.16952 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dccef4d-b822-3f11-8095-181ed80ceda6 | -14.68642 | -48.39534 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0500b99e-75ef-3740-b7d1-6f35017e4d00 | -15.35436 | -46.0512 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95856e3f-4aee-30c0-acff-731d12e3ec2d | -9.67911 | -48.39443 | 2025-10-06 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ff152ef-83fc-3893-89b6-59516a3e98aa | -9.16185 | -50.05616 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9686738e-02fd-385a-9686-65b6d11f11f4 | -11.57405 | -46.77669 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00d1dd10-95a5-3fd7-8c0e-9bdcd882ca1b | -15.55993 | -46.84348 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf9a4ec9-e765-36c9-b1c2-809cd834fb18 | -11.55694 | -47.0405 | 2025-10-06 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d6c89c6-e650-3912-8b1b-1a5d46718d44 | -14.61584 | -52.5019 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 04647ded-1457-305d-9a3c-722075b804e4 | -9.22944 | -51.83375 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa109528-f61e-38f2-bb17-4a0e87b4ae48 | -11.81045 | -45.12122 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0df1e6e-b10f-3248-94e7-500f365355ed | -12.9893 | -51.0526 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e83a999c-1ca7-381e-8e4e-07a41fb55f02 | -12.44679 | -45.57742 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ba198575-26b9-32be-b818-430bc7425886 | -15.24013 | -47.96671 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56dfa01e-fb0b-3b6f-8205-6af3bf315c16 | -13.12433 | -48.00689 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85a8bbff-34ef-3bfa-9789-f323feb34f28 | -10.43381 | -50.35975 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff3421a7-c738-3b0b-a48d-08d99af74c01 | -13.35584 | -47.59391 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6dcb415-bd77-3c23-9b4d-1b8eda24f96c | -13.30082 | -48.07582 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b523b7f7-a691-3e54-89e0-62502cf8c8ec | -13.07601 | -47.97009 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 177ed700-e35b-3c9c-9dee-37036129f58e | -13.32779 | -48.05494 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b5c5bcb-e000-33a3-9d3b-96789e1f2f4f | -9.62154 | -46.62436 | 2025-10-06 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67a77d76-8f1e-3a9d-b4f9-d7c35d588145 | -15.75262 | -46.27322 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 847e2506-29c9-3f7d-b111-e85f1a612ad5 | -11.18365 | -47.7325 | 2025-10-06 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d602a92c-868a-3196-b285-45184d48b249 | -11.1732 | -47.73441 | 2025-10-06 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f61f053a-b211-32be-abe4-721b1a7e6d34 | -11.15978 | -47.92634 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 132f8b53-58ca-330f-85c8-edcaac01c732 | -13.07988 | -47.94548 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48efac6c-7e73-324f-9d31-a10ed2f799d1 | -12.25145 | -49.20813 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcabfbb0-1044-3a21-ab58-4fd27a684d85 | -8.60987 | -54.96719 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 747e13ba-6eaa-3891-9fe6-fbc651c99977 | -16.29662 | -45.24063 | 2025-10-06 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4570784f-8819-35b8-ae0f-43215d64b5ed | -11.44171 | -55.04469 | 2025-10-06 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a5b2506c-be7e-39ec-9f1b-320652e6bd60 | -11.70558 | -47.50537 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fe25af3-71f0-3dc5-8084-d10d74320561 | -13.64383 | -47.29163 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 083948cd-1e43-3cad-b18d-29e705012285 | -15.23929 | -49.2868 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee20e131-856f-3eda-ac99-8f03e5d614da | -11.8029 | -45.12423 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 651d24db-a0e3-3f0f-975d-5b1327e62cee | -13.37717 | -43.62397 | 2025-10-06 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 195675cf-a3b7-3060-b3fd-ce8c9b0dfdf4 | -12.48508 | -45.55595 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 85885b24-d03a-398e-a3fa-a8abf4600a17 | -12.48564 | -45.55213 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3ff616da-4f25-392e-9c3a-5912c10edf9e | -13.69073 | -47.31767 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 27cf7d17-351a-3330-b449-0297fe85dfad | -13.63246 | -48.68943 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e9f669d-3602-3043-9c1a-26b41c01e508 | -10.39815 | -51.59363 | 2025-10-06 04:27:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95fb9148-e1e0-3ce4-82fd-6291fc5f70c1 | -13.49721 | -47.25024 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dffc258f-8bc7-302d-9c7b-04c932ebbcdb | -14.70022 | -48.37218 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 67683a61-7a6e-3399-adec-c2061ea2798e | -11.67202 | -47.48206 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9e8ab2f-efc0-347c-944e-875e0f2c0608 | -10.46774 | -49.10493 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bff9e599-504f-37b1-9703-3b282ec477c0 | -15.32275 | -46.36278 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd61443d-abfc-3de4-8e9f-90b5b795ab2e | -15.75204 | -46.25305 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b0945676-ca96-3025-b012-4b57dc939b4e | -13.61028 | -48.70047 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3b8a96f-7897-3560-b60c-5a6b1a62dc40 | -14.63813 | -48.33653 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f4caef9-d7ff-37c0-bc75-d3cd4cd48376 | -11.01481 | -46.52153 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 49fce2c5-5509-38cc-93f0-e7f3c0acb0c6 | -13.32284 | -47.1674 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b65f9b5-7e9a-3c08-9830-db2368a5f073 | -13.27939 | -47.6244 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2caed949-fc16-35fb-83e7-6dbaa9578f3f | -13.61086 | -48.69687 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 969c4456-7009-3a60-9587-7da841a9c47e | -12.44356 | -45.57769 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b9ee9db4-a3ae-3d17-b701-03fdfd9813c2 | -8.74118 | -50.66364 | 2025-10-06 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0badb260-0459-3345-b2a5-02fa66b87e9e | -13.11335 | -47.99064 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99f86fd1-fac7-3a43-9598-aa390777fd60 | -12.91568 | -54.72599 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2e97ec3-d6c5-31c5-bbd3-7bc0d7125400 | -14.65241 | -48.3534 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cb1fd52-fd8e-3020-93dc-854531e461f5 | -9.23003 | -51.83029 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 062d2ce6-cb5c-3ced-b7a7-007546895416 | -14.67653 | -48.3937 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 021dccdf-4ffc-348e-8eac-acd627b07cb7 | -16.42368 | -48.9901 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README45.md)
