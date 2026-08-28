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

## Dados Diários - Página 168

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bca1cd1-82d4-3a9a-b55b-dcd56473e341 | -8.8184 | -49.6308 | 2026-08-28 19:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| cd73ba2a-cc5c-3c42-a946-b7403fc31d85 | -13.471 | -57.0373 | 2026-08-28 19:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e3f71061-785b-3085-a282-67795c13902d | -8.0548 | -45.8616 | 2026-08-28 19:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 3f6f66ea-ea01-374f-aa71-713e6ace569a | -14.9193 | -56.3237 | 2026-08-28 19:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 237.7 |
| 1412884a-fe0e-3524-b348-fd0f0995c21d | -4.3021 | -59.4826 | 2026-08-28 19:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 0a553b7e-cf2f-37f8-b8f2-a93cc9c4aa16 | -6.8357 | -59.9571 | 2026-08-28 19:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 958e7630-4d0f-37c8-a988-8eaf38ff0e2f | -7.5479 | -61.2866 | 2026-08-28 19:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 03f05c44-e10b-38b3-a99a-e838cff07929 | -8.6486 | -62.8565 | 2026-08-28 19:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 2b0d5016-cbf3-394f-a7b2-74a21061e0e0 | -8.6487 | -62.8376 | 2026-08-28 19:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| fcdafe9c-edc5-34c8-b114-1c111abdb3ed | -10.3391 | -49.9762 | 2026-08-28 19:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 16b1ef78-86e5-3ed3-b291-6cc4c2ecfb62 | -8.6694 | -49.5369 | 2026-08-28 19:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| d5679d20-6f10-3caa-af87-e4ac7cf30390 | -4.1696 | -42.4346 | 2026-08-28 19:00:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| 7bfebbd0-e794-3e7e-a4a9-68ef4d1ba3a5 | -12.9244 | -59.8843 | 2026-08-28 19:00:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| d816561b-6c92-3ab4-b607-75db2c008fc3 | -14.1835 | -52.8456 | 2026-08-28 19:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 110.7 |
| e965d79c-bbde-3e36-93b7-6910b89bb692 | -8.1432 | -64.0053 | 2026-08-28 19:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 107.6 |
| ab31a3c6-13fd-3e04-8efa-6d909d07445c | -3.2361 | -61.2359 | 2026-08-28 19:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 74596a7e-a61b-3cb5-8927-acc6beafb2f6 | -11.6212 | -54.5947 | 2026-08-28 19:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 3c8d0640-00cb-34d0-8c52-02e1a48f6a05 | -14.6024 | -53.1508 | 2026-08-28 19:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 365902fe-b57f-37cf-962d-41dddd95d580 | -14.8821 | -52.608 | 2026-08-28 19:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 342.1 |
| ed20df14-d6c5-3182-ad84-4bf9a837767b | -7.5478 | -61.3056 | 2026-08-28 19:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 164.5 |
| 6a2babba-80f9-3c7b-818d-73d8734551f0 | -8.0551 | -45.839 | 2026-08-28 19:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 5428b064-a1f5-3c82-a160-7dc3f989fd07 | -14.9 | -56.3257 | 2026-08-28 19:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ed74ce5f-b15f-3580-8f1d-366e8ddca354 | -6.8941 | -59.3971 | 2026-08-28 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| bf6c26a0-4133-39c1-ba58-28b7918a6332 | -13.6185 | -45.7688 | 2026-08-28 19:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 7f91cb45-e0a1-369c-8b9d-943693d43531 | -9.9708 | -53.9419 | 2026-08-28 19:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 164.8 |
| e81e3f3c-7734-3c5c-829e-aae2db3e3151 | -11.2493 | -45.0501 | 2026-08-28 19:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 757efbc3-c58b-3719-a506-9c3f9d45ab61 | -6.894 | -59.4164 | 2026-08-28 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.8 |
| ef5946f6-24bf-3018-8703-740f2229306c | -6.8756 | -59.4171 | 2026-08-28 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| d248fc42-cd6f-3071-89d6-7902bc622115 | -6.5865 | -55.4346 | 2026-08-28 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 21d07fdb-292a-3a79-9cef-c19adf56b736 | -13.6572 | -47.737 | 2026-08-28 19:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 152.2 |
| d2a50eea-4904-3ac5-b582-9cbef3b11e5c | -9.1525 | -49.9639 | 2026-08-28 19:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| d660fb81-3891-3a74-a20e-2b97ce6a2578 | -8.0739 | -45.8372 | 2026-08-28 19:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| e1c03b09-f45e-394b-9b21-a5bb6638ed66 | -4.924 | -55.7645 | 2026-08-28 19:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ae51f2e3-8fb9-3cb4-ae73-c1e2d9549ffe | -6.2693 | -53.1322 | 2026-08-28 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| c2d64c0d-8f38-31ee-8e3a-ef154bd65c7b | -8.1617 | -64.0047 | 2026-08-28 19:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 22ed11f1-c030-30f7-b78e-fdbccaf110f2 | -8.87 | -66.8935 | 2026-08-28 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 3cb44c2c-5875-3cc3-9af8-f74ca2c585cb | -8.4524 | -70.7897 | 2026-08-28 19:00:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 440d42ca-21d0-3173-9eb9-bd5e42c3479c | -7.5662 | -61.3049 | 2026-08-28 19:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 138.3 |
| f3beaefe-f496-3161-9178-dd29d861f31b | -6.9521 | -58.9506 | 2026-08-28 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 193.3 |
| 398f7312-bb98-3c8c-9aff-4e9672203e5c | -14.8817 | -52.6293 | 2026-08-28 19:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 312.8 |
| a23cf08f-5d91-32f6-a92c-269b9d5e089f | -7.2817 | -49.8627 | 2026-08-28 19:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 6d9b1bf4-e010-3847-b359-df1090853897 | -5.9465 | -44.7974 | 2026-08-28 19:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| e7820333-e1fa-3fd8-9070-9de9d2a936a6 | -9.0014 | -57.5388 | 2026-08-28 19:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| f93ffa58-0d4b-3d69-879f-4ce4106e7510 | -8.93575 | -71.31827 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 80ddb99c-0c14-3b56-af45-1fde86d6a95f | -8.00979 | -70.88811 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 26.3 |
| c4534400-5372-3370-b919-0558832903df | -8.60245 | -72.91991 | 2026-08-28 19:08:00 | NPP-375 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 9.6 |
| cf52e93e-2cc5-35b4-b822-2bd635f777d8 | -8.03489 | -72.4056 | 2026-08-28 19:08:00 | NPP-375 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d30a7271-7d83-3b08-b757-761f46eb67bf | -8.14517 | -70.63168 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 1fadec3a-488f-39b6-90e1-7e38656ffd8f | -7.93098 | -72.45797 | 2026-08-28 19:08:00 | NPP-375 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b4f1321d-651d-3933-a749-3cbf1f43c3b5 | -8.56782 | -72.4118 | 2026-08-28 19:08:00 | NPP-375 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 6e1d5fd2-4829-3ef5-874f-ffebc9e019c2 | -9.42516 | -70.57779 | 2026-08-28 19:08:00 | NPP-375 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 9974cfd4-a580-3584-ba17-92a9b76614ea | -8.94631 | -70.70568 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d30ca8b4-3ded-3ec7-94dc-87738c6ebde3 | -8.01061 | -70.89252 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c17cc85f-8ba4-321e-b2fb-fbc8f9279b84 | -8.38119 | -70.8491 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 51c915f6-8cf0-39ea-9bd4-3b23f29b7916 | -9.07218 | -72.26154 | 2026-08-28 19:08:00 | NPP-375 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 20275fd3-74d7-387d-b992-5dc08fe6d960 | -8.39445 | -71.02945 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d1b6f249-a916-363c-a350-18e207daebec | -8.60934 | -70.91976 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 52c6dbda-4adf-3586-a70f-eb9011614ebc | -8.60739 | -70.92069 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 1714a3af-d4d7-3c3c-8b5c-fef336f838cc | -7.69907 | -71.39191 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d91dc9c1-10aa-3af7-a524-ff07ade56eed | -8.9191 | -71.5173 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a6cd80fd-4094-3423-80f9-7ec4d0c56b83 | -8.37999 | -70.84983 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 19.0 |
| f73e051b-2535-3d94-be65-9c97f561fdef | -10.91094 | -68.46111 | 2026-08-28 19:08:00 | NPP-375 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b80ab17-1939-31ff-8d79-92164cb3008a | -8.3752 | -70.85027 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 49cfe613-ddaa-34e2-9ee3-ac26457e8ec4 | -8.8797 | -71.49577 | 2026-08-28 19:08:00 | NPP-375 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b578520-e34a-3614-a4aa-45857ce773f5 | -10.19953 | -69.3596 | 2026-08-28 19:08:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0e84c85a-cc06-3d75-a813-5cea77596769 | -10.05843 | -68.83949 | 2026-08-28 19:08:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 4c61c3eb-d5af-38b0-b1f3-d5d8ae7c2e54 | -9.20214 | -72.63564 | 2026-08-28 19:08:00 | NPP-375 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26c93b34-fc86-3e51-88fe-327044761c6c | -10.28366 | -69.10948 | 2026-08-28 19:08:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0b219057-9486-3a20-b15e-58cd4a3838cf | -8.61518 | -70.95036 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 3dbff885-f832-3644-a6a7-48dc322c662a | -10.28994 | -69.10576 | 2026-08-28 19:08:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ce22e1c7-ce11-378b-aa85-7a9d3b593cb6 | -8.45374 | -70.59915 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7b45ef93-ccf2-38cf-807e-eff807fc41b9 | -10.5525 | -69.87491 | 2026-08-28 19:08:00 | NPP-375 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9595df5d-24b5-3c4d-910d-975c532dcff7 | -8.36172 | -70.75018 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 26168078-bfe0-30f1-913e-7d05beb44564 | -9.33712 | -68.88442 | 2026-08-28 19:08:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9fb25a00-3139-3877-9293-a5e0d6f3a649 | -8.63319 | -70.71796 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ac023499-4f78-37ac-b29a-0e275db28e87 | -8.60705 | -70.21399 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d30c2d02-10dc-3a79-974a-165c6075b298 | -10.27623 | -68.86138 | 2026-08-28 19:08:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 96a5611e-9b62-3e34-9304-d74700e5fb19 | -8.84653 | -70.84472 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0ec677aa-4f76-38af-9ac6-145179a049b9 | -8.70255 | -69.49595 | 2026-08-28 19:08:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a79bb0b1-6e29-3b57-a252-e4c94ed88ca5 | -7.76299 | -70.74471 | 2026-08-28 19:08:00 | NPP-375 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 87f5f552-7384-308f-a1eb-61450dc73942 | -10.05566 | -68.8373 | 2026-08-28 19:08:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 1882b133-0149-3aa6-b7a4-baa1a1ebd84b | -8.61256 | -70.91531 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 36392a1b-34e1-3269-b2cf-7b2f0da6ccb3 | -8.92269 | -71.24873 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bdc39d83-3478-3700-b753-7352eb83a553 | -8.21611 | -70.5066 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b197c832-6360-3b6a-b7e4-1bc8a46e7dd7 | -7.87529 | -73.02973 | 2026-08-28 19:08:00 | NPP-375 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 63978749-f54f-3d10-a054-2986458d7128 | -8.94713 | -70.71002 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 69f89439-1d65-30de-bde0-1490c079e328 | -10.28141 | -68.86334 | 2026-08-28 19:08:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0fe2e643-acb9-3244-928b-fbe5221b7726 | -8.24779 | -70.09705 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 2bcbf76d-7a60-33e7-9360-cdc920b9cd36 | -8.37503 | -71.02404 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b13acf74-2fa9-3860-b873-6357d1c10726 | -8.61221 | -70.94695 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a62e7f38-341f-363d-ac95-f92b1fedd1db | -10.05073 | -68.83501 | 2026-08-28 19:08:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 5c1eb7de-f98b-39d9-9420-c2946b9a0655 | -8.34829 | -70.84636 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 49e0bdc0-47fc-394c-8219-d681cb4aefdb | -8.03018 | -71.24526 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9a8133f-b679-3623-ac22-bce472888162 | -8.37472 | -70.13667 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 31.1 |
| fc73cdc1-7127-3e16-a9bb-657ea90de687 | -9.0283 | -70.9135 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d92fc8ad-fe10-3b7b-89a1-6fe89dfd8141 | -8.49613 | -70.31746 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d752fde9-8596-3d1f-81ee-a2afe864b612 | -8.43509 | -70.33376 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87f240ff-24bd-3141-a544-da1cffcbda2a | -9.07729 | -72.26284 | 2026-08-28 19:08:00 | NPP-375 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 28.8 |
| f82a2a3b-126a-385a-8e3e-a9dad418343a | -9.17782 | -70.89416 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6c95a5fc-7b45-3d9d-bfcc-c4675e387253 | -8.89657 | -71.42677 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README169.md)
