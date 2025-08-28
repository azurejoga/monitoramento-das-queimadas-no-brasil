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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 306adf2a-a524-3122-a752-5ebe9cef51b6 | -7.38815 | -39.68661 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 42.7 |
| eca6ed3f-e583-3a3f-baac-0d6e4873ba6f | -7.62429 | -42.70715 | 2025-08-28 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c11c5c31-e23a-350a-8cfc-be59ab8d1da1 | -7.15676 | -44.14995 | 2025-08-28 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 390f6a93-54b9-3620-92e2-19c319cc9979 | -6.17424 | -44.06485 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba1e0786-f2fc-37bf-854a-52c79742e99f | -6.16596 | -44.07145 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e55fdb62-a13a-3008-9d5c-c6ae68370da8 | -6.52242 | -42.97193 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9576df80-24ff-3ee0-891f-faee1b8937bd | -5.68324 | -40.97649 | 2025-08-28 04:06:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d247497e-0e4d-3d98-a507-175267b787ae | -6.3066 | -42.48911 | 2025-08-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 95554157-cc82-3cd5-a60b-d53de7df19d1 | -8.27674 | -37.62092 | 2025-08-28 04:06:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9c722b2c-b9e0-3433-a4c0-37102a72d57c | -7.65321 | -42.6542 | 2025-08-28 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 720f595d-54d1-3f45-a621-843efc4cd116 | -6.18823 | -44.15592 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a5c5eb7-4e7e-3d76-a60a-b9ec1d6782fd | -6.12682 | -44.42109 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc733a4d-22f9-372d-8dd6-0c8f9623be26 | -5.0603 | -43.06153 | 2025-08-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 16e52de4-dd5c-3320-bad6-e8d030e7585a | -7.13383 | -43.68777 | 2025-08-28 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3e688d0-51cb-3ca6-b70f-35c3bf3ff60b | -4.74191 | -41.43256 | 2025-08-28 04:06:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aadf16cb-a580-3740-819b-b3135204994a | -6.08284 | -44.00223 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf295273-9755-3593-bbc2-fd86428d13b6 | -6.45276 | -42.42641 | 2025-08-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5356279d-6d0a-3d59-b76a-d0366e4dc2ff | -7.39159 | -39.68715 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 42.7 |
| 98a635b9-d9c1-3593-ac3f-5fd328a126a6 | -6.69866 | -43.09996 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d23734b6-8588-3496-bea2-418d045e96fe | -6.18278 | -42.99233 | 2025-08-28 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5e3f537-98ec-3a8f-816f-dc03a69f7d07 | -6.13039 | -44.42165 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fc56ce9-e5e4-3a29-adb3-d5fc1da065a8 | -7.39045 | -39.69469 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ebe11e28-5bb2-3eb6-9139-2d0af4a13b21 | -6.16149 | -44.05484 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 751ce798-1abf-3a36-9dbf-71ea4a27d615 | -5.54735 | -45.37196 | 2025-08-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd98e64a-69e5-34c8-8798-bcc7cd9bf96b | -7.55879 | -42.00663 | 2025-08-28 04:06:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 55a7891b-b7f1-3210-a1eb-0a366e7b8c83 | -6.18455 | -47.86149 | 2025-08-28 04:06:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c49917f7-e4b7-38c9-ae15-abd09332b70d | -5.91154 | -46.16354 | 2025-08-28 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28039518-f39f-383f-ba36-5868e311408f | -5.83796 | -45.30495 | 2025-08-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e739e7d2-c8e9-37d2-b68f-516069bdab5b | -3.75618 | -54.8163 | 2025-08-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 26cbd9cd-35cf-365b-9e29-2a4e85a84055 | -6.28104 | -44.47809 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13615639-3492-3f65-9a89-108f48364679 | -6.17775 | -44.06539 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57b3dfb7-e514-31eb-8acc-28c0e1e70f3c | -7.0807 | -44.30351 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82c87b88-523a-3512-b540-344be723ad6a | -6.48275 | -44.08475 | 2025-08-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35cf42b9-88fb-3a6a-857a-c8f9d1af859a | -3.76005 | -54.81764 | 2025-08-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ef6d72df-7e7d-3e61-8718-20d717fa0990 | -4.40145 | -40.48824 | 2025-08-28 04:06:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 75547ab7-6e65-3b92-b56e-766851a482c3 | -6.17203 | -44.0125 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0924a51b-c970-3ae3-9d47-94630a6637e8 | -6.99877 | -44.40761 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 231695ff-a239-307f-bcab-4e01e99eae70 | -7.3956 | -39.6839 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6e414b2f-9f24-3522-be80-acdc4935321e | -3.7529 | -54.81655 | 2025-08-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 505af298-b5e1-30a9-8d71-6df1b2dc8157 | -7.20308 | -44.06247 | 2025-08-28 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54060980-4984-3856-8a3f-61aa24c4e444 | -6.6992 | -42.96725 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2ad17164-288e-3fd3-aa85-e3b858a34c15 | -6.19946 | -44.15343 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 802a4132-d690-3de1-8e16-840f7003d55b | -3.76335 | -54.8173 | 2025-08-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ded6934c-3092-3d84-a1df-a72b0291daf7 | -6.51899 | -42.99346 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a80fc96-67b1-3c83-9951-9e86f05aef03 | -7.641 | -42.6666 | 2025-08-28 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b5fc9b7c-71d7-3143-887a-63e688c823bd | -6.165 | -44.05541 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 664726f5-6e03-3996-97df-b4e4bd5788b0 | -6.32406 | -42.87407 | 2025-08-28 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2a0c7d8-2636-312b-bf81-d12b2b17ec70 | -7.45866 | -39.96115 | 2025-08-28 04:06:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 626cbe1a-f5d9-3d21-8e50-c21219202294 | -4.47404 | -48.11526 | 2025-08-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6b86143-166c-3509-8bd1-a7155d377122 | -6.22547 | -43.36087 | 2025-08-28 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ef2b478-ebb5-3dd6-ae3a-67a1781f950e | -6.88115 | -43.60165 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 99ffc155-72e2-3766-b31a-0930392315e0 | -6.88498 | -44.39374 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbc23317-5996-3f5c-a8bf-1138920c8ccf | -7.43243 | -42.05464 | 2025-08-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cba2aa1b-5d0f-3b3b-ad0f-7ff4bfdf884e | -7.42582 | -42.05359 | 2025-08-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5778b60b-c89c-3fcf-9405-0be00a5b0b98 | -6.59393 | -45.9698 | 2025-08-28 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 595be876-8a8b-3980-b53a-f3b1999773d7 | -3.76199 | -54.82479 | 2025-08-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 77d34452-4bce-37af-b38c-5a5d9e6192fc | -6.49804 | -44.41217 | 2025-08-28 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 104d7826-2fe1-32a5-9355-89a6251d2d56 | -6.49995 | -44.40039 | 2025-08-28 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd99cf34-bb05-3f72-978f-c753c709b7e2 | -6.44119 | -44.58184 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60aeb9c8-d235-3b19-82fe-38c474158552 | -6.86106 | -43.61773 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63252296-3729-389f-aeff-f3b480f6facd | -6.16723 | -44.06372 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2745df7e-174c-3e3d-a125-d88618b6a609 | -7.42238 | -40.08007 | 2025-08-28 04:06:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d976060c-dc74-3cbe-8673-c84ff225e2d7 | -6.0816 | -44.00986 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31112f47-8109-3eec-907c-cf70f27349fa | -5.84122 | -45.30378 | 2025-08-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36ed45f8-8868-3688-886c-54c3d8ea9b77 | -6.05308 | -46.67652 | 2025-08-28 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45f4b818-d70f-3216-84fe-b80c2e679ed9 | -5.6871 | -40.97356 | 2025-08-28 04:06:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 01435100-2a39-350a-ba66-49c3d335e56c | -7.62261 | -42.7177 | 2025-08-28 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dc173191-23ec-3f03-b65d-c3c01b8cdd6c | -2.74508 | -48.56672 | 2025-08-28 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8a6e74b-3367-3ec8-b43e-3aa4980e06ae | -7.64488 | -42.66364 | 2025-08-28 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5ffc938a-52fd-303f-bcd4-1634818c7abd | -6.72005 | -43.09602 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad53fca1-b069-32b2-a9b5-67a7a8ca06c2 | -6.87431 | -43.6007 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79cfa3be-71df-3abd-9a59-d4b52c8f66e1 | -6.73419 | -43.07241 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35171eb7-4d81-3730-8674-11aa213c334e | -5.76382 | -39.20907 | 2025-08-28 04:06:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 55f9464d-bc86-3572-8407-2c1d6e1943cc | -7.29601 | -44.36067 | 2025-08-28 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90d27b16-fc9d-32e4-ad8c-6a9e1ed914ab | -6.1564 | -44.04206 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a1d5b20-a5a9-3413-a557-39789cebe29c | -4.80011 | -47.2622 | 2025-08-28 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cff9945-71b4-3cd8-b202-8996bfd85674 | -4.79078 | -47.265 | 2025-08-28 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e42c353a-648e-3ba6-9a0f-0e13c30e601a | -6.19402 | -44.16474 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84d6d7e2-03fa-3440-a00c-49ccb749ccf0 | -6.81412 | -44.36217 | 2025-08-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 132cf4dc-6176-3a48-b0b4-37005a60352a | -7.05059 | -45.87942 | 2025-08-28 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e36f645f-7b5f-344f-8543-1f41b1721078 | -4.78513 | -47.27225 | 2025-08-28 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 59b452db-489f-3ba1-a090-357bf69f5b97 | -6.51963 | -42.9678 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c36b722f-eca8-3cfa-94ce-cce14c717276 | -6.87133 | -43.61937 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23d41bcc-0a7e-333a-b80e-05564c4d1304 | -7.42527 | -42.05706 | 2025-08-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 37a5a2e0-7d32-39a1-8073-5cea948f54fc | -6.07707 | -43.99358 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71bd8c36-9535-3148-84b8-14cf6d7aa7de | -6.40665 | -45.22355 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f36cdf94-365f-3bef-b6a7-07b5a7a87be6 | -6.87468 | -43.61976 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 991efe68-d73a-39f7-8cf2-a4b92d41c9e6 | -4.78445 | -47.27628 | 2025-08-28 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 128154d6-3299-39b3-bc4e-19ad3203ef4d | -6.70802 | -43.14965 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d431dd70-4370-3910-bbd7-f6b721b8f71b | -6.44029 | -44.56494 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 016f0157-f85e-37cb-874f-6384c6642925 | -6.59588 | -45.96725 | 2025-08-28 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b60c5457-a0df-3355-a06f-5ce3568c2223 | -7.24371 | -39.17696 | 2025-08-28 04:06:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 31fe1da7-1923-3580-88ec-1a3bd1e79853 | -6.87651 | -43.60856 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d32f8c5-2b4c-3ce4-aa68-754360f4d370 | -6.43112 | -44.57609 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 587cb229-f361-3bd2-8285-b5731a367c7d | -5.45495 | -38.41408 | 2025-08-28 04:06:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cdff3521-92f9-3133-8fba-78e375e28d11 | -6.31383 | -42.48666 | 2025-08-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 68161d8f-9c23-3072-a648-f71165ed8c59 | -4.50899 | -42.06787 | 2025-08-28 04:06:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f4233237-5d15-3fef-9f4e-4aed7dc7b741 | -4.66667 | -41.02512 | 2025-08-28 04:06:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| fa3cd66c-44c1-336c-a1b5-7c015aaabd65 | -6.17361 | -44.06873 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8308244e-f57e-308f-860a-0b891354b9a6 | -7.29666 | -44.35984 | 2025-08-28 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README33.md)
