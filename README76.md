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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e603574-0bdb-3732-af1b-06ef853275ba | -14.85451 | -46.68527 | 2025-09-07 05:14:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f8c6dac5-b10d-3094-bf48-2aaaf36ab337 | -14.3516 | -60.32692 | 2025-09-07 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a0ddaf0-4c22-3c2e-86c2-461116f3e4e8 | -17.40501 | -49.31211 | 2025-09-07 05:14:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 92fbacaf-e5ea-3068-bae6-6eb1af04d79e | -19.4702 | -47.76708 | 2025-09-07 05:14:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae5a1283-0a62-3685-b3ac-23e6a30f0247 | -13.82483 | -56.07327 | 2025-09-07 05:14:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e13af9a8-ae1a-3f8b-aac5-d6a34571fc27 | -13.9366 | -54.01868 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64561471-ba72-30b0-9e56-1ef729f06e3d | -14.49174 | -53.24156 | 2025-09-07 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b68cc7a9-25fd-3cfb-b690-4adb10f9cef4 | -14.34939 | -60.31937 | 2025-09-07 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 805360d5-1d84-39b8-85ca-34d8f70c2b0c | -13.90873 | -54.0108 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 17c6e742-b20b-381e-ae49-8b477b434249 | -14.56483 | -49.12633 | 2025-09-07 05:14:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1eb0476-148e-381f-804a-2ed3955b3972 | -15.70715 | -47.512 | 2025-09-07 05:14:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2c0d99c7-9cd5-3be0-83a2-3283be1824c8 | -14.92806 | -55.89747 | 2025-09-07 05:14:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28d3e4f3-8be8-31f3-88f0-be3f44bba096 | -15.06774 | -50.07749 | 2025-09-07 05:14:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e76f91b-1b8d-3fb3-9104-9a6d44578588 | -15.70035 | -53.5823 | 2025-09-07 05:14:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 09540076-3131-3015-89cd-c396f66d2ca4 | -15.13286 | -52.35653 | 2025-09-07 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78dad707-e09a-3a56-a42e-bdea21d89f1e | -15.18428 | -47.97 | 2025-09-07 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86c3ac00-637c-378c-9c5b-96c9855aaeea | -16.30033 | -58.10061 | 2025-09-07 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5fb872fc-6b45-34bc-86b4-3af3a62279e6 | -12.41299 | -63.89796 | 2025-09-07 05:14:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4f55b74-fa1b-3687-80e2-858e8b5b383b | -14.53839 | -53.15399 | 2025-09-07 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15d03d1c-826a-3433-b870-8b12c9ab911c | -19.4697 | -47.7727 | 2025-09-07 05:14:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| facc0ad9-2ec8-3c3a-bad2-f6461255ba8c | -12.35666 | -63.64236 | 2025-09-07 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a64370d-f48c-3114-bbb9-271f24d28789 | -13.93708 | -54.0151 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f44a437-050c-35bd-9056-46d36ee5cfe0 | -15.57438 | -52.90419 | 2025-09-07 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 11d14855-54eb-3b50-acfa-ae8ef917ec73 | -16.93956 | -45.77943 | 2025-09-07 05:14:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8dd2de42-4721-3a82-a2fe-9218b9d4d1f4 | -16.94791 | -45.7656 | 2025-09-07 05:14:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1ba39fdf-04ec-303a-888d-546a6c55b757 | -13.94019 | -54.02273 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ffdbf391-a26f-3993-8988-7d25c884eeec | -15.17719 | -47.97845 | 2025-09-07 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f4d9108b-4d43-3893-9ed6-9718557b73d1 | -19.88375 | -57.90108 | 2025-09-07 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 752e529f-9ea7-30ac-b2ad-b6892daad287 | -19.89079 | -57.90221 | 2025-09-07 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4b3fa81e-a7ee-392e-b2bf-fe59ce00a444 | -14.58735 | -48.07737 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68cd160d-a278-37cf-9c0b-d6ea95087c2f | -15.06808 | -50.07444 | 2025-09-07 05:14:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e62d6058-4053-3ad6-8646-2b361ce1dd8a | -14.58614 | -48.10478 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22a5e283-8d1a-36a0-9851-3a21c5904d9a | -16.94132 | -45.75847 | 2025-09-07 05:14:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0d3d44f9-9cde-3f1b-8d85-db47b2eb353c | -13.90307 | -53.99091 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a73b1516-e143-3b57-9e3d-e922ca0e014e | -15.07344 | -50.0752 | 2025-09-07 05:14:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afcd7694-0133-3568-aeb9-da163b36da2d | -14.45532 | -48.45874 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0316984-ae1f-3436-969a-f6e5a4c5fc2e | -14.88865 | -55.80715 | 2025-09-07 05:14:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 091e1b26-b003-3f96-8006-899c17dbd170 | -16.28496 | -45.68553 | 2025-09-07 05:14:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 74887712-c763-397e-9380-b84ea26efea1 | -14.47597 | -56.80518 | 2025-09-07 05:14:00 | NOAA-21 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abd35f52-527b-35b2-9c4e-e298f9a043df | -13.90257 | -53.99472 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa478e59-c6b9-3fd0-8e79-1a272083e7ac | -15.73408 | -47.02458 | 2025-09-07 05:14:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ba03e231-2f57-36ee-8746-21737949e83b | -19.58664 | -47.40149 | 2025-09-07 05:14:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac364380-fc1d-3c2e-858a-091cf77569fa | -14.5704 | -49.12793 | 2025-09-07 05:14:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a496ad7d-354d-36bc-90a2-b7bfbce976f0 | -13.9316 | -54.02519 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7bdd5e8c-c767-3f1a-89d8-1eb89c1be970 | -16.29018 | -58.12225 | 2025-09-07 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f03bf563-e9f3-3c32-b2dd-bc5477f827dc | -20.54136 | -46.44625 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0b9b2a87-1000-3b3a-a941-3966a14bd109 | -19.47721 | -47.7606 | 2025-09-07 05:14:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c585ab1a-ff77-3bd5-ad0d-cefef1933430 | -15.76539 | -53.65067 | 2025-09-07 05:14:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 208674fd-add6-3c13-85e5-41ee87e45bff | -14.42727 | -60.19282 | 2025-09-07 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab75fad2-a7f2-3d37-bad0-018f7ff22e1c | -16.94075 | -45.76531 | 2025-09-07 05:14:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b34bbd62-8359-321f-aa07-a42385af3c22 | -20.83029 | -49.42214 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| c72dccab-ed1b-3076-bf92-87f32b6f075e | -14.34712 | -60.33354 | 2025-09-07 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b19759a-9aa1-349b-9f81-15021cf22288 | -15.70307 | -53.5607 | 2025-09-07 05:14:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6356fb73-96f6-396b-ad19-b21ccd8f296c | -13.894 | -53.99703 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6fc61a78-04fa-3127-9eef-2371bd69b669 | -14.48745 | -53.24091 | 2025-09-07 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95ce1884-29fe-3dab-a221-8591ea3d9c59 | -14.44323 | -48.45996 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0a0a63a-9a44-345c-96ba-2cfd79f8066f | -12.41238 | -63.90147 | 2025-09-07 05:14:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f450d864-a2fe-3ce7-9e7a-0c93ceb56de2 | -19.06581 | -46.78291 | 2025-09-07 05:14:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c15f6080-d9a8-3c46-a74c-7d367790ead3 | -22.21692 | -56.1969 | 2025-09-07 05:16:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e432ba12-3492-3758-83da-bf8686fd853c | -24.14875 | -49.51299 | 2025-09-07 05:16:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7c83294e-2ebf-3c7f-a6cd-2f35919b69f7 | -22.70404 | -53.24922 | 2025-09-07 05:16:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| c0e9d9d8-f98d-39a2-a574-804da1a0ca0e | -24.14918 | -49.50736 | 2025-09-07 05:16:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43c811a9-73fe-3d57-9756-04dd381014df | -24.14299 | -49.50714 | 2025-09-07 05:16:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 437963c9-a69e-36fa-acd6-2b7c7e50650b | -22.69923 | -53.2486 | 2025-09-07 05:16:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 46a93e66-d53e-3f9e-baca-f503df89d556 | -12.948 | -54.7724 | 2025-09-07 05:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 79d3232d-58d9-3de2-bf23-1f21f474a331 | -12.9482 | -54.7519 | 2025-09-07 05:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 148.2 |
| e8b78958-a5f2-31f3-94e0-334b9018e915 | -12.9292 | -54.7538 | 2025-09-07 05:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 195d55a8-d29b-3cb3-9eb3-2afa7c436db3 | -12.9289 | -54.7744 | 2025-09-07 05:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 8bc15ffb-c6f8-3a6e-b4f3-5f1dd54f26a2 | -12.9482 | -54.7519 | 2025-09-07 05:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 79a57a81-f348-34bf-bf7f-20728f88457c | -12.9289 | -54.7744 | 2025-09-07 05:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 150.0 |
| 1eb9205f-bfb0-3c48-9dbe-442d9ee8307a | -12.7153 | -56.5632 | 2025-09-07 05:30:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| eae896b1-0421-3111-99e6-fb8b9cf2ad9e | -12.9477 | -54.793 | 2025-09-07 05:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ee3c54ec-72fd-38e3-8b7b-bb86e5844f53 | -12.948 | -54.7724 | 2025-09-07 05:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 204.9 |
| ac3562c3-76e3-3bc2-b022-d8d664384bc3 | -1.94174 | -56.59318 | 2025-09-07 05:36:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c7005e6-087a-3ea7-b15c-fbb7738de84d | -2.43004 | -49.30722 | 2025-09-07 05:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23ecbcbf-9cda-3821-9a65-db9fa5ad7b6c | -2.43102 | -49.30048 | 2025-09-07 05:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8e9f235-9219-35e3-ac28-e4e41373f6d0 | -2.42699 | -49.30142 | 2025-09-07 05:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2b80295a-71ac-3f82-bb5b-162551573580 | -2.82032 | -49.19621 | 2025-09-07 05:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 048b1e89-5103-30ec-8616-ec7d2a0b1c60 | -2.43302 | -49.30918 | 2025-09-07 05:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e6b0122e-0037-3c26-9620-a8df6ae2bed8 | -2.43708 | -49.30832 | 2025-09-07 05:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d536e8d3-4c94-3c0b-ba1e-c1a8f7783aea | -5.86398 | -57.77268 | 2025-09-07 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 760fcc98-dda9-3d9a-8fe4-ea3546da09c2 | -7.38967 | -59.66192 | 2025-09-07 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4862145-c573-3c19-92c3-cb51e8a0d21c | -8.6211 | -54.65225 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fb3fb97-86a6-31b3-b81d-44c8b65b8636 | -8.6912 | -54.66883 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62f7a1c8-ad1b-3319-8c7c-4aa803572011 | -5.79265 | -57.55669 | 2025-09-07 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7fda4ec-cd8b-30f1-8891-6b5a90345a97 | -6.84443 | -52.85518 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b3ac93a-bb6a-3ac6-9f60-66f6a50b3de8 | -8.07607 | -52.3841 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0d8f5487-643a-38c0-801f-fae0b7689c92 | -5.85601 | -57.76772 | 2025-09-07 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bd25373-2da9-3ae5-b992-76863707a49d | -5.78893 | -57.55201 | 2025-09-07 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b627043e-7712-36dd-a641-0ea4fd2d5ee6 | -9.39404 | -54.76736 | 2025-09-07 05:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe3f4930-a305-3e09-bdbe-60be0f4d1001 | -5.8554 | -57.77181 | 2025-09-07 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33fb2278-cc72-3854-acce-c701e2cd64fa | -3.24449 | -50.79924 | 2025-09-07 05:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 319e0ada-fffc-39f5-82ba-24a42529be79 | -6.28127 | -53.44347 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc8d053f-38f1-36ea-aee2-f1230a443777 | -7.68466 | -50.30965 | 2025-09-07 05:38:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 654cb258-3e2a-356c-a514-7450de411505 | -3.20681 | -54.9642 | 2025-09-07 05:38:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 980a06b2-81d9-3346-b19c-a2035011b525 | -5.95061 | -53.80263 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b87958b6-adc6-3670-a180-37dba13f86be | -6.84624 | -52.84172 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2135d5dd-31b8-3c61-b75d-a03217cad51b | -5.90079 | -51.94395 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88edee44-b4da-321f-9f16-098ee78864cb | -8.34795 | -52.55575 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25323868-4275-371c-a85a-18c579cef6c4 | -6.27088 | -53.43383 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README77.md)
