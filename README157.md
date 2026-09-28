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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16293b98-e275-38fc-aa51-06958bbf83a6 | -11.52252 | -47.39093 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 146.4 |
| b8301b60-4866-3187-abea-558bc80b82ec | -7.68838 | -54.85444 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 3ba31506-c31e-3e14-bb76-a10d02131275 | -10.88802 | -50.68567 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 96404194-b26b-3ac5-871b-e89039e8e1fd | -12.44244 | -56.50827 | 2026-09-28 17:09:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| e457b9ad-625b-3d21-b4cd-ec98922f23da | -8.09071 | -54.75072 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 39b0e147-d60e-3cd5-9d6c-5fa8365b2677 | -9.3499 | -46.54255 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 257e584e-acd1-3db2-a99a-cbde67644d15 | -8.64418 | -49.48214 | 2026-09-28 17:09:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3441eb59-c120-3e88-80ae-5a1a2be90a42 | -7.27611 | -45.33646 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f969ae4f-a8c6-39c5-861b-730ec02c3f38 | -5.73335 | -43.28602 | 2026-09-28 17:09:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| db4555ae-89d1-3f94-ac0d-953321b3f648 | -8.93093 | -45.05706 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a4984cfe-5000-3d95-9dad-8277052a8fa6 | -9.46205 | -45.96609 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7bb5018b-8a8c-39bc-ae9e-e3568f7359ca | -11.65245 | -50.68034 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b62ef4ae-ae54-3198-b90d-ce3f4d9171a0 | -6.75584 | -59.63405 | 2026-09-28 17:09:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 46ac9b8f-9555-3480-b7ae-aab5b4d227de | -6.22232 | -53.23605 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b65f8d8c-d6ed-3412-8bb6-e1695c814fd8 | -9.07829 | -49.87214 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 528e5a67-b36c-31b8-9b35-f08dc7091459 | -11.87465 | -50.89138 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 6c654dde-ea06-38e0-a239-b88e7d4bef9a | -7.45591 | -45.80721 | 2026-09-28 17:09:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d7ec1a20-0a34-3987-9e96-c0484466c55e | -7.02074 | -44.61776 | 2026-09-28 17:09:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1a0c7f19-ecec-3cdb-8275-9989bf2e1a6e | -10.82215 | -60.7315 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| ec3ecefd-6e1b-32f4-b6d9-dcf5a8514688 | -8.18847 | -54.7887 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| d1d91995-250d-3599-9874-db6d60edeac8 | -8.85894 | -50.65727 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ba2bc6e1-e21a-3151-a36c-8fb1e309fba7 | -5.77019 | -49.2467 | 2026-09-28 17:09:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 420037e1-b308-306c-b45b-fecf1cb90447 | -6.65138 | -55.09768 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c09fc595-c7a2-32e1-856f-6dc855551553 | -8.66973 | -45.37558 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 6aef9dcb-a872-3da7-888d-196e9fa99951 | -10.26754 | -44.63007 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 182.8 |
| cdc5f6ae-2206-34b9-aa07-b6fd1c4591e4 | -10.90685 | -43.86436 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7c37e114-60f0-3bcb-bc75-0e7737659abf | -7.27936 | -44.30947 | 2026-09-28 17:09:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d9f0438a-e479-3e9c-be85-a200a16c41ae | -11.55053 | -47.38353 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3cdd85aa-8523-3738-924f-5d796b7c19ff | -10.83199 | -60.73874 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6b6701a9-db94-33cf-9dd4-ae5d14afaa02 | -11.17865 | -44.80518 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 639f4eef-b56c-37bc-8080-1c4bac24b630 | -11.09406 | -61.33299 | 2026-09-28 17:09:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 44ffe928-fb66-37bc-9106-3e00aab22d6d | -7.23196 | -55.58274 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7831d5fe-2c06-3dea-9435-eb14684b608e | -11.87166 | -47.09528 | 2026-09-28 17:09:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5192d3f5-2533-3197-be73-e0422f5bfa76 | -11.16145 | -50.06127 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| c08974cf-839a-3005-a53a-45449271702f | -8.73797 | -44.90575 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 2f86c389-edc7-38f9-a5d3-d004ba98fdbb | -11.11872 | -43.31989 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 4abffdc6-e8f5-3288-9446-a5d0a0765132 | -10.70177 | -44.42606 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 438a7686-8cce-39f1-bb10-23f0cd270213 | -5.9995 | -52.76868 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| e3fd697d-73db-3d00-88c9-eef24b3f9ef0 | -11.2123 | -44.80556 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2a7feca9-079d-3373-853b-d160f12bf4c9 | -9.02754 | -50.80677 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9de52722-ef9d-3ce1-8501-cbdef865f789 | -5.83606 | -53.84108 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5311b90f-45eb-3a18-8412-1c8da5e309c5 | -10.72472 | -53.99442 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a8837642-5a9b-3d9e-a9de-0762d565240c | -11.13041 | -50.05455 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 00437a5e-9746-3d41-aabf-eaaaa9ca33c3 | -11.07862 | -48.89323 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 73d37adc-d351-3b6f-be45-f0be9c218d1c | -10.75252 | -54.08707 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8e61d849-7917-3adc-8af5-dddd606370a9 | -7.82638 | -55.13367 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b3353e70-69bc-3591-bc06-f137186450db | -8.27583 | -54.71828 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 699c5ab6-0550-3887-a000-2f70640dd005 | -10.20775 | -50.0013 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c6215e44-a947-3746-b733-4be720d1fe32 | -8.27371 | -54.70438 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| e5bbd8a8-6fbe-3d98-a0dc-a253392c8826 | -7.33019 | -42.08594 | 2026-09-28 17:09:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 6b323d79-3ec3-3764-8730-cacd13a3bfb6 | -11.47453 | -49.74621 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| cac3502f-a266-3eba-a2a8-940b625f7e33 | -11.57544 | -45.47104 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 83a46edb-6bba-37f0-b73a-e0d495b7eaa3 | -6.15404 | -52.89651 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| f336d551-007d-3417-80aa-1f2bc14ff98b | -5.41596 | -45.89079 | 2026-09-28 17:09:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9bb2e65c-c8ba-3658-ab7a-de6bcd7b6e48 | -11.8494 | -50.85146 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 8c071075-c49e-31de-9e22-d940b5c4e388 | -10.71364 | -44.42769 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4c619e4c-ed8d-3d5a-9192-70c887c50c18 | -11.52343 | -47.38873 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 236.4 |
| 4b089f49-eb5b-3485-9f33-52b5062fee29 | -11.86795 | -47.10099 | 2026-09-28 17:09:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 1c82dd1e-48b6-3f7e-8198-c053d4c4a151 | -9.77326 | -44.84327 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 75f253f9-4034-32bb-8067-44e50034b57d | -10.95661 | -43.87472 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 9d08df0b-54c0-395c-8792-b87861ea62fa | -11.34335 | -47.33677 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ac8abcf2-1d07-34a5-9445-6b76064c001e | -11.55221 | -47.39283 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 6d6bc159-5482-3512-b62f-45d206ac6259 | -6.13906 | -53.05891 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 3b6708d6-6b3b-38d9-bad9-62c0190f5b44 | -11.13359 | -50.07391 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 895f3622-439a-3a1a-8b39-607420904c9d | -10.26678 | -44.62606 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 32d2ff80-04d0-353f-abf3-19bc12d3a51d | -10.45807 | -45.09101 | 2026-09-28 17:09:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bb058457-eabb-373d-b5f1-d1867a63e8d9 | -8.2898 | -54.74048 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| b853d88a-fde0-371c-a53f-4d9cabe6d17e | -9.07488 | -49.87634 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 1ef52899-cc7c-3a63-9357-b3eb3332a207 | -12.59293 | -51.96339 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8638c2f1-2933-3359-bdc8-40854c468e76 | -8.01274 | -44.97673 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2af3c2b8-d41f-3a17-9050-8367fd0af4f8 | -4.94388 | -45.10804 | 2026-09-28 17:09:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 5895bd0b-91c1-3752-b7bd-34702a8d239b | -6.64861 | -55.10165 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4f59ac91-b3cb-3b3c-bb3f-7f0accd51172 | -11.52991 | -47.37977 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| b2ff23f4-9d79-3141-bfdd-00353b187c36 | -11.86377 | -50.89325 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 796ac3a5-7a7e-3397-abb2-dcc7ec394920 | -6.86911 | -43.86996 | 2026-09-28 17:09:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ca5e9e06-e875-39dc-9bbe-32dc83d2de21 | -7.45117 | -64.39664 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 15135a6f-5320-324a-8e13-afb68fc78bae | -7.86656 | -54.72992 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bc931fdf-2441-3bfe-8441-64b80f69090a | -11.15459 | -48.3338 | 2026-09-28 17:09:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f7f45fd7-3774-3ed9-ad59-b74c75da1136 | -11.45654 | -44.92222 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1d1a8d49-b31d-3219-a6ce-461230fe1fcb | -7.30498 | -43.3132 | 2026-09-28 17:09:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 9a9517da-8121-3fc0-84ce-26777f2aca79 | -10.2178 | -49.98926 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c9f36142-3bce-3a78-a1d2-225ac4e54bf2 | -7.98055 | -67.24235 | 2026-09-28 17:09:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d86721a8-7259-3246-a372-65c2f649a252 | -10.7218 | -50.47679 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 79a2f10b-df0c-3491-88ae-9c820ea07f8d | -8.37179 | -45.48151 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3b066daf-abae-3292-95f1-8d9a4792b757 | -6.97297 | -52.13715 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e7975ce7-ccac-34f6-bef0-bd83022ee3a7 | -7.76677 | -54.78811 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f8db8bb5-82ec-37d2-9b4d-0b7b845f1072 | -10.77477 | -48.74847 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1dae2063-9d8a-398d-97f5-776ebe944d88 | -8.19116 | -62.88056 | 2026-09-28 17:09:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.7 |
| e6471739-8cd9-3c99-9c5f-322027dac929 | -11.05341 | -42.992 | 2026-09-28 17:09:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| a28bc4b4-b8dc-37c1-9943-a0ab7defea5d | -11.58392 | -45.45935 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 021301ad-0bf9-3977-b72f-3cb8ea8d8d1d | -7.33865 | -54.9922 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e6223446-616e-3ee7-af9d-16a7268322d0 | -11.84634 | -50.90065 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5d3f1eae-56e4-3a7b-81b1-018ba992c361 | -9.1167 | -49.90527 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 81754089-47b8-3592-afdf-631b96f75e49 | -12.61415 | -51.96376 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bc82e2ac-3cda-35e2-a561-13c1e2fd6653 | -8.85951 | -46.59919 | 2026-09-28 17:09:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6494d9b2-76b7-3046-a862-7e2c0145a563 | -10.20301 | -49.99696 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ab4bd72d-adfa-359b-9f0a-9f44d5f56b78 | -11.38966 | -45.39992 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 042fb8a3-95ed-3158-95ac-c405c55fad83 | -5.57458 | -45.30181 | 2026-09-28 17:09:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 0c65e152-0a44-3b5e-9e7e-6f0f6107787d | -10.07381 | -48.7678 | 2026-09-28 17:09:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| dc6960bc-d628-3d96-bb58-2d12e910427c | -11.38297 | -47.40106 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |


[Clique aqui para ver as próximas entradas](README158.md)
