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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e19c2c1-cbea-3cc8-b6c0-dda5dd078ea1 | -11.49219 | -49.17006 | 2026-08-19 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 748a87e3-f1ea-34fd-ae74-9aa081dd31a4 | -10.93957 | -57.10633 | 2026-08-19 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 757a1260-fd31-3729-9e19-1d4ae0800cf9 | -8.56253 | -55.2516 | 2026-08-19 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 898cc869-3ce8-347a-9cb9-d3a83e8237f8 | -13.27381 | -51.64695 | 2026-08-19 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1f36445-8c46-37a9-a3d7-64752e59c631 | -11.16576 | -49.62053 | 2026-08-19 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b34ce440-618e-3bd7-b914-a6538595a506 | -9.40424 | -60.57116 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e40d32d0-0f51-31b6-9180-8267f29247e2 | -9.17152 | -59.7046 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f44c9f8-0dfb-3acc-8e1f-ba859db2b69d | -11.12411 | -47.25365 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6b6aaec-8cd8-3b9c-afe4-682fde4a8d91 | -8.58151 | -54.7734 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28a15251-bd96-320e-bb16-8d29e6ec27f4 | -15.27353 | -56.50446 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 570105c4-2990-36b4-b480-0339b1b717d0 | -8.89728 | -60.56662 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa7283ba-b6cd-3b03-9a03-bdf91a869eb6 | -11.5059 | -46.64089 | 2026-08-19 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 508d931d-0316-36b7-b41c-5cc50d6c8d16 | -11.11898 | -47.26437 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d25d2414-44b5-3048-b300-7ef319727f21 | -8.54629 | -54.7196 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2697033a-61ac-337c-9721-aaff34243e8e | -11.2307 | -55.07125 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b01d07bd-ce40-3c77-8fad-b379ed4bb0c0 | -14.45504 | -45.62252 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b6ef39e-7202-368f-9add-9e4ed41cc903 | -11.3191 | -55.23293 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8dcd3d7-6fe5-3359-94de-8eee0af8f601 | -16.07772 | -48.01193 | 2026-08-19 04:40:00 | NOAA-20 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e0301665-eb18-3a9f-97bb-5b22a1494877 | -8.54555 | -54.72379 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e716f129-455e-3353-9646-27673c4f4794 | -7.4288 | -59.79059 | 2026-08-19 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f512546-80f7-38d6-be96-c31d4733f816 | -8.56056 | -54.76527 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 598ab67a-f140-3119-88b7-315ec4957baf | -8.53828 | -54.73275 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2ceeb9b6-5021-3d20-b3c0-0832fc42227a | -10.67693 | -48.99874 | 2026-08-19 04:40:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 181926ee-cdfb-3fc7-9a6b-b12b8f385e4b | -8.55849 | -54.75166 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b71a54a-5fe5-306f-a44a-ef37e05243a9 | -15.31366 | -56.45873 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b73288da-89e9-3b79-a4dd-72d7c62db82c | -9.40438 | -60.58849 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a52073a6-9f5f-332b-ade9-e8952c0243b1 | -8.55413 | -54.75102 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94b7881a-8b24-3ddd-af35-7818f08b3a56 | -9.98464 | -53.93846 | 2026-08-19 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47bd1a77-9eb5-3a9a-a309-9aa32e6e5340 | -12.23658 | -43.15361 | 2026-08-19 04:40:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 880ded7e-db1c-3e42-8460-6a0cce5de8b6 | -11.11105 | -47.27058 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0d713b2-0503-339e-aef2-06a9f97ee6e7 | -9.72827 | -46.79115 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d776d02-9a54-3b60-b6fc-cac57ef593cb | -8.5417 | -54.77067 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8fd5bad9-49df-3a75-93b2-1c2c172ce820 | -11.163 | -49.61647 | 2026-08-19 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 22411dcb-c961-3461-823a-0f4281ec20c8 | -9.73002 | -46.77983 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53c6175b-fdc8-38b6-9886-68cbfc967282 | -10.63444 | -51.62288 | 2026-08-19 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ba31540-8387-3680-ba9d-dd71a896548f | -14.74326 | -48.74228 | 2026-08-19 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9f407cb-8c9f-3bfa-9090-74955aaf8af4 | -10.1074 | -54.28946 | 2026-08-19 04:40:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5f73367-7f91-3859-988c-cb76b58de557 | -8.57797 | -54.74252 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 377e6772-b2ea-394c-9e4d-9734cc4c299d | -8.57865 | -54.7642 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 92ea8e8e-31e4-30cd-9f78-ab7c5ca7b79a | -8.53906 | -54.75438 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9118dbe1-0463-3c53-927c-c6fd7bffab4e | -8.54405 | -54.73219 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ed02f932-d106-3eb3-b414-8b4c27246f34 | -8.58372 | -54.76076 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 09e50ced-524e-38ac-905e-caabbfae2931 | -8.54118 | -54.74191 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff6e3c13-d4d2-3a47-9680-9167749e3248 | -9.06375 | -50.85423 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49a626d2-fbc5-372d-9695-af61bce28103 | -7.59943 | -60.9629 | 2026-08-19 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43e9d118-56b9-3b55-af45-8b882e3636f0 | -9.40114 | -60.57206 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd67ddc3-7a74-3f6a-91da-d240a8840b9c | -12.88949 | -52.8259 | 2026-08-19 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 247b966c-7d99-3d1f-a8b5-880221ef004b | -13.26011 | -51.6445 | 2026-08-19 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a2e8efd-5a01-3a30-be6e-e846b228f8e6 | -8.49336 | -54.86411 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c74da356-27c3-375e-8525-3dc8d11dd5da | -9.40015 | -60.57706 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1da61772-049d-343c-95bd-d54c93d613da | -12.24358 | -43.16738 | 2026-08-19 04:40:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| acd45f96-9ca7-355f-8956-3c76c9de174d | -9.44432 | -60.29369 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a831f893-d5db-3919-a64c-ec389b63390d | -8.55187 | -54.76381 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf9b42b8-c9b8-319d-b0a0-a884ea61879e | -9.06999 | -50.81586 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cda6aa2d-b5d0-3003-b4e7-42497ae4206d | -8.98701 | -50.70136 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 476e18af-2795-30e3-a12a-fb4750bf6a9f | -14.48724 | -45.67171 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f7ff49a-ff7a-35f7-9724-44b87caeeff8 | -8.21614 | -55.02876 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9c249f4-a93a-3730-ae3a-0182fff4160a | -8.21691 | -55.02435 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b58304bc-cee0-3bbe-a868-6ba01569105d | -15.3153 | -56.45008 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06a84cd8-3f4d-3bc0-934c-1f22e96da15a | -8.54469 | -54.75377 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e3bfaa0-8219-318b-b203-8c2c1d911277 | -11.22853 | -55.08339 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e3b1951-27eb-32a5-bb32-f3011391e5a0 | -11.11558 | -47.26377 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2081e5d-797e-384d-b6ab-e4eb965e4770 | -12.78689 | -48.42286 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5788c657-c5b5-3b9b-bbba-64e0ea28e6e7 | -12.05962 | -55.4443 | 2026-08-19 04:40:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1b95b8d-ac03-375b-97f5-ccbca21ee4f9 | -8.53257 | -54.76624 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 518b4a44-cccf-3abb-a83b-4ee87a60633f | -13.26354 | -51.6451 | 2026-08-19 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47e5deda-d836-3599-8bd1-d9f4d3c66c6f | -11.23142 | -55.06725 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19f41070-9410-3501-bd99-f05afdc5ed72 | -11.68994 | -54.56057 | 2026-08-19 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 391d0e52-ec6f-3d2a-b0a1-d731992788ee | -8.5621 | -54.75654 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d8026581-08d4-3cb8-9a65-b1728bd16da6 | -10.90684 | -50.28224 | 2026-08-19 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75985adb-da49-357a-84e1-173aa71793fd | -12.5155 | -47.84134 | 2026-08-19 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45189843-c1e4-38dc-990c-75c184b83b5c | -14.73655 | -48.74119 | 2026-08-19 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93154ab7-4b51-3613-902e-6ac0e9f0138f | -11.11165 | -47.28966 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0373f75e-40b0-31d5-a1ef-87b20faa16a3 | -9.49401 | -51.67429 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 53dd69b9-3380-396b-95c3-f036b938a395 | -8.57357 | -54.76763 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 43e0d94a-08fb-3f2a-b3b5-c6aff687e74c | -8.53972 | -54.72428 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cea9fb2b-8d94-3510-b446-9486fd87a3b2 | -10.91077 | -50.2792 | 2026-08-19 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39b0e1b8-981e-39da-89dd-44a4e4dce457 | -8.53972 | -54.73142 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d38ca1b0-4e5d-3fd5-a2fe-ad90debf27b9 | -14.48657 | -45.67654 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a58088a0-e2fc-336a-b6b1-f0ca2cb92656 | -10.12007 | -45.75436 | 2026-08-19 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a912c994-d40e-3979-b434-121fc7739fad | -11.22261 | -54.0056 | 2026-08-19 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 885759ca-4ec2-3c14-816f-9713cc00ff52 | -14.89276 | -49.30739 | 2026-08-19 04:40:00 | NOAA-20 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5bf9bbd-5662-3bf2-b63b-e9d36edfe9f3 | -8.5469 | -54.74133 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dcc03c1-3eb8-31d8-81b4-1230e15858b3 | -11.12353 | -47.25743 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5db65402-1fd7-30b4-8639-b142a20736d4 | -10.51597 | -50.79169 | 2026-08-19 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bae6e942-1ec2-3f9f-8e71-611ee120cd75 | -8.55697 | -54.76024 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3cd04efe-df71-3528-9bbe-a39dc0f18ebd | -8.57149 | -54.72853 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 14d65b5e-2a60-352f-9f22-8631b095bc96 | -9.06593 | -50.81902 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6aa8b1fa-bd89-37ea-8862-a0a62f40533f | -9.17235 | -59.70027 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f905a15-3696-3541-9a04-419d390384e4 | -8.54043 | -54.72007 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| be9b6740-1ecf-3d05-9ea0-701e790d2071 | -9.47851 | -51.59754 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9d5db6f-a743-3daa-81e3-e35ebb221501 | -8.56359 | -54.72272 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1bb79889-c286-3599-9e32-46fbc43f8d3d | -8.53685 | -54.74115 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 671cfe99-b0a0-3ccd-8b1f-878a812ccf30 | -9.10795 | -60.39012 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c67806ab-9f98-37be-9bb4-c0edebfb0b99 | -12.75344 | -48.43983 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37be07bd-5924-350f-bb20-a51c02607c3c | -14.04518 | -52.32866 | 2026-08-19 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3887b9d3-c06b-3e51-ac6f-3a2a62889c71 | -11.23707 | -55.06014 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45d0444b-5263-31ee-9857-612e8e0817a6 | -9.0551 | -57.0686 | 2026-08-19 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e401e12-3e2b-3d63-ae73-fd2e6400fcad | -8.54753 | -54.76303 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 876bdd62-a2a5-3be9-ba3d-42ece070f6b6 | -15.27726 | -56.50316 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README40.md)
