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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac259d1d-4a74-385e-8436-cba352a4f195 | -11.42643 | -45.61385 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2cbb87d7-9e40-39b6-b770-b34b7b8a2630 | -15.23811 | -44.03851 | 2025-09-13 04:08:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b7919c7-251b-3ddc-b1c4-e7e938f8cab1 | -9.02088 | -47.0751 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e4f6c7f-cbe2-3f0c-a5ed-0ec9a924c9fd | -10.64396 | -48.97857 | 2025-09-13 04:08:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9673ccc-6c0f-36b8-80ce-d2446c0a9eb3 | -9.90218 | -51.8867 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb341fb4-3de4-3c89-9e2e-5d7046606cf7 | -14.18763 | -46.2696 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 87fde1f9-c54c-3c2c-9617-80b72b05222b | -10.70656 | -50.50193 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7e3a09b-2223-3be5-9851-6123fe7fb909 | -11.4466 | -43.57399 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7eb0821f-5cc1-38ab-b86b-2f97e6f0ab90 | -11.0919 | -51.44416 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8e0c4967-7bb8-30be-accc-3fe05f7900a6 | -9.97018 | -50.29956 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 07d53d80-3831-388f-9ce4-b9f5c675869a | -9.49271 | -55.97058 | 2025-09-13 04:08:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8647ac8c-7a92-313b-8c73-74def89cdf7c | -8.49225 | -45.1374 | 2025-09-13 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6422bb0b-8774-3268-99a2-962f336481db | -14.70006 | -45.14748 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 598b036c-4aa2-3e98-893c-152f843ff180 | -13.91689 | -48.2746 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d1de0dc1-0796-397c-becb-e5c5a2cf0a27 | -11.27461 | -51.13327 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75af3560-734a-3673-bebb-f5d11e71bb2b | -9.49814 | -50.90319 | 2025-09-13 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d1d7d51-c595-3a01-9a0d-66f71fde897c | -14.21672 | -46.29259 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1c387a52-991f-3af0-904c-435116f424de | -11.84836 | -50.5702 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a670c2fa-5967-3c4e-83cd-953ff25c0da0 | -9.90686 | -51.89182 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3df65521-de84-3f93-8106-f51386a42e17 | -8.24472 | -44.35579 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2547fd72-41fb-3b58-861f-36d767bfdf4e | -11.85149 | -49.77793 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3c2b07ef-27b7-38cf-9e2c-4b6c021988ce | -11.86283 | -46.7631 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32ff2f82-36a3-3b6e-b06d-cc8e62386420 | -9.65462 | -45.80936 | 2025-09-13 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c30ffd4e-2fa3-3efe-ada6-1b43f15aae8c | -12.95387 | -47.99752 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d64e529-8020-3ef7-bad3-90ae6ae4485c | -9.02724 | -47.06172 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06410cd8-f12e-37a1-a3f0-b64bda1b17aa | -11.86658 | -50.57932 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cfa79658-ebb7-3d80-9f48-39b04156ae09 | -12.82418 | -47.9536 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d53c568c-455c-39f8-a35b-ad491cee96b1 | -9.5148 | -54.67273 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f45278d5-a4e6-3f27-9582-e361441a96b4 | -10.01456 | -50.388 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a01cac80-c142-30f1-a4c4-6b2d01a7a55e | -14.19542 | -46.28836 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 037d64f8-9a76-3616-a102-7f58636ddf64 | -14.20961 | -46.26968 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d76c23f-b3b7-3352-9c5e-04585262776f | -10.37123 | -50.50176 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c9764bb4-65a0-32de-a736-b80dd5113476 | -9.02784 | -47.05813 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59ee63a4-a3c1-3c40-a531-72a547c389df | -14.21954 | -46.27597 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 36009ca5-75a4-30cc-84db-e2837f6de27e | -13.9255 | -48.2254 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 79abb206-3416-37c8-8b7b-53891424977a | -11.13416 | -45.23417 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1521b6ea-333c-31cf-9731-efccc773ef24 | -13.08253 | -48.2647 | 2025-09-13 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| b3db7f01-08a4-336a-9b83-5f5c531f7838 | -9.49739 | -46.42345 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a60cf724-9726-385b-a5e9-e548b3b9f28e | -8.48144 | -45.14971 | 2025-09-13 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f95a03ca-71ba-35df-980e-899c03370dbf | -8.94093 | -44.44624 | 2025-09-13 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc3c74f2-cf44-3c54-80fc-f3186f1fcbfc | -13.00532 | -46.74522 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| abd1f58d-27f1-3d20-b4a7-7356b5d2d22f | -12.12545 | -47.59779 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f6fa00c-3a7e-3ed2-b31a-3d99478a78d8 | -10.50294 | -51.55167 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca2dc13b-3497-3f70-84c0-c4413e1442fe | -13.24704 | -43.76466 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6373e33f-81f5-3c70-abfc-66833d84bac4 | -11.99589 | -47.76308 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bc15f7b-3990-3ff9-a9b5-cf5b7a1887e9 | -10.51051 | -51.54367 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e7aefa8-5bca-31d4-ab7b-f65254c49e45 | -9.79375 | -48.90625 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9ab926b-66a1-3413-928d-9ce1444d29bc | -12.91249 | -54.74853 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2281f29-9cdd-3fea-a3e0-2c1fa46d2cca | -10.10346 | -45.50079 | 2025-09-13 04:08:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f19681d7-1f45-3644-9dfb-dae655f2adb3 | -12.0877 | -44.90192 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7caa7831-ef7a-369d-98b7-e93aa0f3578c | -14.19404 | -46.27497 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 27e17309-9fa6-3a9f-9c0b-6d8503c26fdd | -14.20879 | -46.23158 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 475e3db1-9c61-3415-9e59-9737b10adce9 | -12.39478 | -43.82175 | 2025-09-13 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d618a63-bd8f-3829-9f5a-c7828d1cc062 | -11.27982 | -39.22393 | 2025-09-13 04:08:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aef38a00-9f16-347c-afc6-46390a047198 | -10.3279 | -48.82181 | 2025-09-13 04:08:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6204f4dc-2716-3aa3-90b4-fb63c1f54d09 | -11.48632 | -43.70456 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b0ba9fd-00bd-3ec0-832b-8e62cb7eb5f9 | -9.95861 | -50.38889 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4aaa2cbf-387c-3462-8067-b8cccc55940a | -13.21809 | -51.74435 | 2025-09-13 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49dd099e-9a3c-3be0-94b4-5ad02e115c10 | -11.11809 | -50.70193 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03abbfe4-c4f3-3cd8-8a7d-50d3dd433fc3 | -11.84552 | -50.55859 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 5c11565b-edb2-30bf-a873-cbc1933da802 | -14.2602 | -45.04641 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9f76236-f9a2-35a6-8534-e325deb32f98 | -9.73854 | -48.09177 | 2025-09-13 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47e02569-3cd5-3910-9e25-b597e44ba9bd | -14.26936 | -45.03584 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4c06439-3e2e-3b04-87ff-56a20f75202e | -9.51779 | -54.69176 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b4e33fea-9e3e-3cea-8480-18568bbfc03e | -9.75514 | -45.39012 | 2025-09-13 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b37abad-348c-30b4-89a2-1ac34e8d8399 | -14.4402 | -47.34334 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 492843a2-d7f8-393f-89e2-14031e3e6819 | -14.28255 | -46.07571 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 47a096e1-9c7d-3a4d-a129-e4c8bbab1119 | -12.10365 | -47.58329 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3fd0aa0a-79cf-39d7-b767-f5de0a84ecb2 | -8.08695 | -50.18952 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87840980-2a92-3fd8-8274-31d638aeffe3 | -10.50206 | -51.52785 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f915639-7dde-3793-947a-cc3a6d84fdfc | -10.70274 | -54.44629 | 2025-09-13 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24daff92-f0ba-3062-95f7-839927d51eb5 | -11.84356 | -50.56926 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2f1589c2-4aa7-3ad8-af0e-2728297a8e8f | -14.41626 | -46.39914 | 2025-09-13 04:08:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da16b3d9-7ff6-3b8b-93c5-8f5efc3d2dca | -11.84541 | -50.58625 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77e15308-e820-3b11-802e-8901019f3115 | -13.12231 | -41.0515 | 2025-09-13 04:08:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 035f9dab-266b-3369-9ac3-085546c43c27 | -11.14186 | -45.2313 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a2db20f-0035-304b-b0f0-71b8690225dc | -12.9024 | -47.95231 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e0a1ee4c-6aaf-361b-9635-68e0da4587ef | -9.79339 | -48.8987 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 100115e1-b3ed-3def-bbc3-069f7126a81c | -11.18068 | -51.42595 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 14fd6f70-ea4e-325e-913e-f7c982bdc9a3 | -10.70461 | -50.50031 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d7eafb4-4921-3b70-952a-482f9e4d5e3e | -10.09185 | -47.20169 | 2025-09-13 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f39becaf-6694-34b1-907b-c92f05625b1d | -11.18647 | -48.35575 | 2025-09-13 04:08:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06d4f087-cf09-3ce5-aaff-f5cdb98dd88d | -12.12876 | -44.84122 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dc539914-d63c-3951-8f69-0fd57aa34cd4 | -11.72025 | -46.6678 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4d2f5e4-ba95-3a06-bd85-c28305333a97 | -9.24033 | -51.2207 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bf5a654-6d62-35f8-811e-b366ca41245d | -9.73476 | -46.89461 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 758b5bb6-3e35-30e7-8244-9f9e725c4178 | -12.09177 | -44.89867 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb87a149-0eaa-3125-aca9-15c3883bd61e | -10.74536 | -50.53799 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f1cec5ac-0bcf-3976-a2c4-abb83d6831cf | -13.52095 | -44.1121 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53d84e2c-1710-3fee-9a9a-ebde2d4e66bc | -9.24142 | -51.24468 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbcbce8f-27e8-346f-ac84-bf675912f079 | -10.39373 | -48.59831 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d526326-2dd4-3d9b-a006-b76e3e4a2b92 | -13.26926 | -43.75375 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d6c930f-c1b8-39d3-877a-a5c86020126d | -8.94028 | -44.45019 | 2025-09-13 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a94346a0-47d6-3a72-a2ba-5ecb5bc898ec | -10.66231 | -46.28393 | 2025-09-13 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ebc47eca-40cd-34d3-99e3-03b490b667b1 | -15.83297 | -42.6017 | 2025-09-13 04:08:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fb49e6ea-c54b-3fc0-88fb-641b59aff481 | -9.91771 | -51.62064 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb3f45c3-918d-3934-bf9e-9f6b9aa7c4e9 | -10.7806 | -50.55116 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9f0933e-2b5f-3f95-8439-5ebe0817e0c6 | -11.21619 | -54.99491 | 2025-09-13 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a082b2d8-ba9d-34ff-9227-3c3175ba3a60 | -14.19617 | -46.26253 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72377fb0-766f-327d-834f-6aaaa0114f29 | -14.2061 | -46.2688 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README47.md)
