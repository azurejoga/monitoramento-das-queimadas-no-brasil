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
| 34a0d5dd-9f02-3609-abc9-bc1215d9fbd6 | -17.35438 | -46.70246 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a140845-eef3-39f2-8cf5-1d2fa3c2dc88 | -13.64953 | -44.26215 | 2025-09-12 04:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5572e651-a3fa-3043-bf7f-f0bc7b7e2c8f | -12.09157 | -47.59568 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 326be556-5968-3ff9-b852-b1584add832f | -14.16842 | -46.1885 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c50a045-85af-31af-9730-a462d9b7c31f | -11.51635 | -50.59657 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 583cd753-7424-3a71-a395-afe0964a46d0 | -15.92593 | -51.79567 | 2025-09-12 04:06:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aced8eb1-c867-3ba5-96ae-1af202ca435d | -16.83001 | -49.30851 | 2025-09-12 04:06:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7832d57-b60a-3d6b-accc-ab79bb9e1a45 | -14.17652 | -46.21064 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| bb643bab-b769-3904-9b77-27f7bdeb6a3f | -14.27829 | -45.06881 | 2025-09-12 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52c239a5-f10c-33c7-84a1-8e2531ec716b | -15.7826 | -52.23856 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 45d4792c-e6a3-398e-9e16-ce08f091faf2 | -13.90437 | -48.25975 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e0c9c4e9-aaf2-3a22-b16b-fd357f1eefb5 | -16.59752 | -49.81202 | 2025-09-12 04:06:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ce8f907-c777-37b4-9c9f-237f4fc4ee02 | -15.78811 | -52.24512 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5d27e817-f16b-3918-8ea1-ead9b67b7b0b | -14.33298 | -54.12125 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 580d8873-822e-39c4-8575-fc7f380dda05 | -17.75659 | -46.13846 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a9f3ea7-3a11-3f0f-b1f4-6f17f39ac407 | -13.26726 | -43.76468 | 2025-09-12 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1384aad0-3d95-35dc-ac9a-8de35e4a1a42 | -11.52207 | -50.39407 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 1ea8e5c3-861d-3756-9c89-728322e615d3 | -13.91283 | -48.23898 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dd46a9fc-ff7c-32e5-b8f0-ad25665273be | -16.42592 | -49.04691 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49c59d73-dfd9-3b4f-b9d6-c6ffd2d56614 | -11.73204 | -50.6247 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bd18119-298c-3d38-bbdc-bc228bdf1a97 | -14.26458 | -54.7886 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 179f4448-e041-3228-a965-0d465fa5a99b | -15.4864 | -47.34539 | 2025-09-12 04:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91f9b555-2ac2-3593-8c7f-53e48ce88c41 | -17.91376 | -45.90575 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 693999ec-e863-3a81-878c-7ddba4b93b34 | -14.11919 | -44.32284 | 2025-09-12 04:06:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d67e006-ac69-3c88-b3b5-d51e3c2488d4 | -13.90722 | -48.26915 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 8c2de364-0661-385a-b9ce-e5f476d1d6d1 | -17.79881 | -42.57101 | 2025-09-12 04:06:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ed30c80c-93c4-30c5-9b10-9b2d2772e383 | -15.53094 | -48.54559 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 923c8c09-6e75-3e4a-aba3-8cfa566b7ff6 | -14.45202 | -47.30745 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e994ac1b-fe9f-302f-8906-076e7c246bc5 | -16.6012 | -49.8182 | 2025-09-12 04:06:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2112bc2-462b-3394-b200-e664da222077 | -13.91367 | -48.23445 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d4328ad6-53f9-327d-b60a-a612b19c3b9e | -15.11987 | -48.6126 | 2025-09-12 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76f6fc8d-6ab8-36c8-8c27-d27cb45779dd | -15.53529 | -48.54669 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dfa481ee-19c2-31bd-8b33-7902347161db | -11.94724 | -51.18358 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e0005780-d487-34f3-b175-ac4ac94daac0 | -12.84166 | -47.95419 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ddcecf79-df0d-3035-8430-0856d0c258a9 | -12.8995 | -47.96397 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe92b9d7-7330-3fc2-9ff0-82e942e10da4 | -16.42682 | -49.04212 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1db070ee-fd18-3082-a4f7-29f40c1a8153 | -11.23016 | -54.89487 | 2025-09-12 04:06:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c0ed6afe-ff91-3ff8-97b5-560697b54ad0 | -11.3164 | -50.78277 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 533c49c7-cf6e-3518-8844-72c692b8cb13 | -12.88757 | -47.95401 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68c7bcc3-caf6-3256-afe1-c99912c09714 | -11.98374 | -51.14439 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b0f051d8-b735-3668-98a2-51ec52201fc7 | -13.31633 | -44.09398 | 2025-09-12 04:06:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c698736d-5c0d-3dac-bf8a-1bd8e6648169 | -13.38284 | -51.8246 | 2025-09-12 04:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 964660d4-15d1-3215-9f7c-b2c23e70f032 | -13.92194 | -48.23934 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09db4276-6a1b-3e1a-984a-bb6cfb92aec3 | -15.10867 | -48.00362 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbff65ef-edf5-3e87-bf81-5c1bd24d4990 | -11.50099 | -50.37637 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 680e1f20-2cf1-32d9-ba99-d308c40ac48c | -14.44014 | -52.9353 | 2025-09-12 04:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| feb4b50f-eeb2-3d96-9e56-54f0580c129e | -11.64315 | -50.58589 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f330a73b-814e-3fdc-82e8-a2633b62e05b | -13.908 | -48.26495 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 3f8e18a7-2c1c-3a8c-95a5-bb0924d31bf3 | -15.68728 | -47.01667 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 17260179-ffd9-3391-8b03-07fbe29ec627 | -12.82182 | -47.97472 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 56564d34-8f37-33f7-bac4-f56a100c8a00 | -11.02718 | -51.51777 | 2025-09-12 04:06:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2f36b44-5a17-36ab-bc1d-74dac6d4395f | -17.35788 | -46.68283 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39185ee0-d692-350f-92d8-2737c7fba12a | -12.82367 | -47.96441 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| aec4ff92-e896-331a-81d3-f4638a333c6f | -12.13811 | -44.86607 | 2025-09-12 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07215b79-0ff5-3073-82b5-e8ae4faecf50 | -16.41987 | -45.69859 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d10a8763-1bd8-3300-b5ff-0fc92b029907 | -15.07974 | -52.4362 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1bd62c55-5cd8-3946-8f49-1aa9a166128e | -15.6906 | -47.04419 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98553e71-e0c8-3456-9ea4-0ec701e024e9 | -13.32175 | -44.65469 | 2025-09-12 04:06:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ad5e69d-0c91-39dc-9340-0686244db8bf | -14.42253 | -47.32851 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfabd9b7-8c1a-3559-945e-4fc2ad0c4d1d | -15.10983 | -52.46282 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c369176-6d31-3448-b388-1283da565247 | -16.42802 | -49.02524 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b0a2dea-3bf8-3cc5-8699-edce7f92e35c | -12.58741 | -45.6798 | 2025-09-12 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28ce49d2-a10a-34df-a1c6-74e4b6433039 | -12.9819 | -48.00576 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18001f45-72f8-355f-9a54-e739d8eb1b5f | -12.87049 | -47.94716 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dd347eb1-2726-3f82-9add-657a84e65a6f | -15.78627 | -52.24868 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4aa80561-4f55-3260-8eea-553554be5cee | -17.81941 | -46.73916 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9271697-6d93-378b-a28c-272cb93565d6 | -14.44723 | -47.3103 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f666e244-a5fa-3802-8550-fbdc48caa0ff | -17.33216 | -46.67261 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6327f71b-c628-33b0-8169-da7901df2246 | -14.12513 | -45.37467 | 2025-09-12 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1917f0d9-bbe7-36b1-80ca-7f6c264c41d0 | -11.1888 | -55.08821 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e41f40cf-6272-3cc5-bd72-a8d88490c807 | -16.18472 | -48.71392 | 2025-09-12 04:06:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea9ad21c-e770-3f4d-b8ac-f01e3533d60d | -14.26586 | -54.78265 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bf22925-fdf5-3890-8b4e-4edf9f585780 | -11.10784 | -50.71757 | 2025-09-12 04:06:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61b21af1-5b37-3458-9c61-efc559a6b268 | -16.25122 | -52.65968 | 2025-09-12 04:06:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 952adc5d-b26d-3ac9-bd08-c83f718481be | -17.6678 | -46.68014 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1912c548-1e50-3a85-97e4-d04208319a46 | -11.9712 | -51.1496 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2817ffa6-a722-3a99-abe1-b48a33931973 | -15.08356 | -48.00711 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a8b0e0f1-bfb9-36f5-8557-9011bb07d868 | -14.18384 | -46.19196 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b34acb2c-d03e-35fc-a00a-314276d79bed | -12.99166 | -48.00264 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7288867-85bd-34bc-a62e-a4105c5e4d29 | -12.24197 | -47.33787 | 2025-09-12 04:06:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab6f1f1b-dec9-3e6f-b295-8cf1bc18f77c | -15.09788 | -48.01382 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f450486-55ec-3a97-8d04-ec6279b7cf57 | -15.24351 | -44.03795 | 2025-09-12 04:06:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35366b04-e1f8-33f0-8e26-fb7c6acf2819 | -15.52567 | -48.54946 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7959a66-7a7d-3cf6-bc69-510310c0f517 | -13.38695 | -51.82549 | 2025-09-12 04:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8be9ddf9-4f2c-30bb-b6c1-9fd1aaf382a3 | -12.58271 | -45.68403 | 2025-09-12 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99ed0abf-b626-31f8-ab85-699db5240fac | -14.42633 | -46.40592 | 2025-09-12 04:06:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7682e717-22b9-3d59-9d38-07fc79b11c83 | -15.53775 | -48.55086 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55464776-fd89-3d7b-b22c-88930606475b | -13.38617 | -51.82945 | 2025-09-12 04:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7a698800-aa9b-312c-aa82-a1b9b42b6ebb | -16.49261 | -51.9675 | 2025-09-12 04:06:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 363db913-b4b2-31c7-bc42-3fb81c4b3657 | -13.91824 | -48.23453 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d29276f1-b1a7-3600-82ee-3ad9b3e31e84 | -15.14819 | -52.47865 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef12cd52-9fa0-3287-87c9-0e78a724239c | -16.43154 | -49.03098 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6e00267-5a31-3f28-ada6-b7ed9fbaf351 | -17.13738 | -48.50346 | 2025-09-12 04:06:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b32472af-9ad9-38cd-808f-5f7c03b8fc7b | -18.02194 | -46.85766 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bad60dc4-9204-346d-b9c5-e7fbb0063247 | -13.36401 | -41.91478 | 2025-09-12 04:06:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 294c305b-ea4c-3d19-aa11-00a02934d3a3 | -12.82188 | -47.96178 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7d77d619-97ef-36c5-89d8-2178eb87c2c1 | -16.88454 | -45.75988 | 2025-09-12 04:06:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8bfc0de-7eb2-3c4f-9551-08799b881678 | -15.0893 | -48.01227 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0303953b-bb90-3c22-ab49-5f0af323d66d | -14.28193 | -45.06946 | 2025-09-12 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abf3a47f-1df3-3e6f-9fce-9e2f819d6a72 | -14.45488 | -47.31537 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README47.md)
