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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b62666cc-2a24-37ea-ab5a-4c19563415d5 | -9.843 | -65.0528 | 2025-09-02 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| b3710d5e-b520-3c11-a323-7ba956d5e8ab | -6.4029 | -58.2173 | 2025-09-02 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 192.3 |
| 280a3eb1-81f5-3ee9-a399-5c5d9e956ad9 | -11.9811 | -45.8629 | 2025-09-02 00:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 24cebc2d-54c7-3721-9645-d1968bb674f6 | -7.5292 | -61.3254 | 2025-09-02 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 129.4 |
| d415cdea-e754-3ce7-9e39-e1dbf5069c98 | -11.6647 | -57.3533 | 2025-09-02 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 18429e86-340b-3009-ac4d-33edc9463167 | -8.6487 | -62.8376 | 2025-09-02 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 3935d29d-87e2-3056-98cc-7ea7c1dca599 | -8.6966 | -50.4508 | 2025-09-02 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 42f83617-a900-32fa-b21c-b27df02454c5 | -7.5477 | -61.3247 | 2025-09-02 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 272.5 |
| 818acd98-6eae-33a0-8e90-d77e66682d5d | -8.6969 | -50.4296 | 2025-09-02 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| f666f558-4776-31cc-a861-76b1b86bf7c3 | -11.1037 | -44.6315 | 2025-09-02 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| c81db477-aa72-3ff9-a915-669a222ca6b9 | -7.5476 | -61.3437 | 2025-09-02 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 258.0 |
| a8b96855-eb13-3c7f-a78b-68f3a6ef7fb0 | -9.8616 | -65.0522 | 2025-09-02 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 34256ea7-d6fd-3bdc-83c4-5d94f7b39113 | -9.1267 | -46.044 | 2025-09-02 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 1222564e-214d-3306-ae96-66f5264332ca | -10.4314 | -54.7597 | 2025-09-02 00:00:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 3354780a-4850-308d-af9c-e9140a404be5 | -10.4502 | -54.7581 | 2025-09-02 00:00:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 79d931bf-6bd8-3d78-8e86-680bb16a0a27 | -11.9619 | -45.8657 | 2025-09-02 00:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 3a768ba0-c0e0-3d27-abbb-9a118677c48f | -9.8805 | -64.9951 | 2025-09-02 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 3fae5513-6d0a-3f42-a9a5-2b6d6401e0ce | -14.2687 | -45.2636 | 2025-09-02 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| e726eef6-d36a-337f-b535-7cda32f22023 | -10.062 | -48.1197 | 2025-09-02 00:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| eb7ab5a6-5649-3461-9d19-c36fcf6a0bcb | -6.4236 | -43.8869 | 2025-09-02 00:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 9f6d4f55-ab61-30d5-ae7e-275f8a930fe5 | -14.2692 | -45.2403 | 2025-09-02 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 8892df0a-7638-3379-be85-4cf6c6e32fe3 | -10.0617 | -48.1417 | 2025-09-02 00:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 265ce784-876c-3036-901a-055d2bc736a8 | -7.6598 | -61.0915 | 2025-09-02 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 24a4aa89-4b3b-3428-982b-d1406f902653 | -8.6673 | -62.8369 | 2025-09-02 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 108.8 |
| abb702ed-3ff3-3193-b0fc-9ab47cf21b41 | -20.1403 | -49.1622 | 2025-09-02 00:00:00 | GOES-19 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 061c8558-aff3-3a88-82f9-8f38f0442760 | -14.8509 | -60.0459 | 2025-09-02 00:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| cd642160-fa5c-3240-8d5f-eccc781aa822 | -9.7485 | -48.9598 | 2025-09-02 00:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 35fbaae2-11af-3eac-b4ea-1c8e1c0caf01 | -9.1207 | -61.4864 | 2025-09-02 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| bffcb9d0-536a-3c69-97ee-addc354d4fbe | -11.1041 | -44.6083 | 2025-09-02 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 37.0 |
| cbaa66ec-cf74-368c-b004-b9fa3e63b794 | -3.2305 | -47.135 | 2025-09-02 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 96da916e-12b9-3cd8-8e21-f7822623bfc6 | -6.403 | -58.1979 | 2025-09-02 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 176.0 |
| 6ffff5ae-5e5b-3735-bfa3-c31d7dddc4df | -7.1328 | -35.1167 | 2025-09-02 00:00:00 | GOES-19 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 70.3 |
| e2369992-8774-3100-969d-44c70b4c92e6 | -11.7993 | -46.4114 | 2025-09-02 00:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| be48c39e-bf8f-34db-a2fc-ed242a299516 | -9.0799 | -65.4349 | 2025-09-02 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 7fc48fb5-5223-35da-bda5-bea2ae8a870c | -11.4251 | -55.1826 | 2025-09-02 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 1188ef3d-cbb9-3325-8930-3b202633a736 | -11.0718 | -45.3964 | 2025-09-02 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 60820a78-3517-3782-996d-8be075eccdb4 | -8.6674 | -62.8179 | 2025-09-02 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 57610325-5062-39db-96c5-11752442a693 | -7.6783 | -61.0908 | 2025-09-02 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 9f3d56bb-2c60-3962-b448-d79baf9e9b9e | -11.6644 | -57.3733 | 2025-09-02 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 42fad68a-29f3-3441-9c9f-ceaf94bb89e2 | -8.7154 | -50.4492 | 2025-09-02 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e4de2dc9-26d7-3137-a4a2-e71fc077f3ec | -10.4312 | -54.78 | 2025-09-02 00:00:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| f60ed725-7219-39b2-8915-bc3e08272df0 | -11.0526 | -45.399 | 2025-09-02 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 05adbc54-f120-3c5b-bbf5-4a482314ff4b | -15.5666 | -48.3469 | 2025-09-02 00:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 4b2943c3-2bb4-3ed9-9eb9-4c062c7b81e0 | -10.45 | -54.7785 | 2025-09-02 00:00:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 4e39a9ce-4eb1-3c81-bd69-8e8b166199fb | -9.8617 | -65.0334 | 2025-09-02 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e58e1e1d-1bf9-3ff6-8a6c-ec7df7d996dc | -8.7156 | -50.428 | 2025-09-02 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 8a1b40f3-0652-3bd0-9a53-10ff1ffb238a | -9.8804 | -65.0139 | 2025-09-02 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 1a95cc55-43ec-3cc4-83a4-e17b935f96fd | -7.5291 | -61.3444 | 2025-09-02 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 2715bbbb-52b0-375a-b24f-7f79f9532295 | -11.6458 | -57.3548 | 2025-09-02 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 082a00f2-bfac-3aa8-81bc-0cdb5821bf24 | -23.23584 | -49.50546 | 2025-09-02 00:07:00 | TERRA_M-M | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| dc958d3a-abe4-3103-a139-75738e1cdf1b | -21.473 | -47.42904 | 2025-09-02 00:07:00 | TERRA_M-M | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 759193eb-1b36-3132-a7a6-2d86f96f599b | -23.23863 | -49.54168 | 2025-09-02 00:07:00 | TERRA_M-M | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.5 |
| 803c20e0-0f1e-3f3b-b25d-2bd6c01d462a | -21.46679 | -47.42314 | 2025-09-02 00:07:00 | TERRA_M-M | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 5850450e-69a2-3f98-a4aa-c0d550ac3740 | -23.22474 | -46.68504 | 2025-09-02 00:07:00 | TERRA_M-M | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 46.7 |
| 5f9eb157-2d99-307f-a6f8-076196e7b418 | -23.22806 | -46.6911 | 2025-09-02 00:07:00 | TERRA_M-M | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.5 |
| d3e1f9f9-8ae5-3a67-83b4-da7fc0345d3e | -23.22851 | -49.5115 | 2025-09-02 00:07:00 | TERRA_M-M | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.9 |
| 3ab15740-095e-340a-85e9-7fdc3cd27d32 | -21.95558 | -47.51537 | 2025-09-02 00:07:00 | TERRA_M-M | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 23.0 |
| b1715540-d2d4-3a6e-9304-8dae9a7c9331 | -14.60639 | -48.0716 | 2025-09-02 00:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9c7b5c36-107c-35c8-95db-5ed16c6975c2 | -11.37958 | -43.62682 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a1fe9efd-1d33-3b30-8221-b5334a7de4eb | -13.32949 | -40.34509 | 2025-09-02 00:09:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 52f56e2c-1c64-37b7-b2ea-5292d179f295 | -12.77082 | -47.65606 | 2025-09-02 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 544c9884-9c52-3921-8752-799add6938a4 | -14.49586 | -45.94485 | 2025-09-02 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 63f4db74-2e86-3722-b6de-45252dfa17e1 | -11.67013 | -52.21434 | 2025-09-02 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2577.4 |
| f1ef75c8-ba16-3cd4-bdd7-0256a713cb35 | -11.10142 | -44.63907 | 2025-09-02 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 7c4a3e89-b030-3792-9827-24fd5d9cdfbc | -12.44289 | -48.71896 | 2025-09-02 00:09:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 4cde7228-1372-3918-981c-7a836ea045c7 | -11.28223 | -43.65656 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 11634957-79d2-35e9-bd64-17271cd61a4e | -11.64564 | -52.18453 | 2025-09-02 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 823a7cc1-e92c-390f-933b-2b83cc3359ae | -11.7957 | -46.41783 | 2025-09-02 00:09:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0d29a714-7e5e-30d9-8b7b-ae72000f2df2 | -11.30186 | -43.59559 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0bac1c12-8b32-3b80-b155-969bf6466b0f | -11.38107 | -43.56863 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2037e901-60fe-31e0-84fb-ebd31ba7036c | -13.89372 | -48.10114 | 2025-09-02 00:09:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| b645a0da-b53a-38df-bd0d-db90c647d82e | -11.97718 | -45.87899 | 2025-09-02 00:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 3e57d8a2-673b-3a7f-96c1-60b64bf663e7 | -11.66708 | -52.22194 | 2025-09-02 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2117.9 |
| f082df18-ec56-38b5-bbea-deb181707f48 | -11.90256 | -44.89185 | 2025-09-02 00:09:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 51dc41b7-50d9-3b4e-a719-ed50dffa45a2 | -13.53331 | -46.99572 | 2025-09-02 00:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 84cd575d-40e0-3a8d-9b09-4e9bc28a696e | -10.28335 | -47.54043 | 2025-09-02 00:09:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6d6611d3-5fa3-318c-b78f-72581c9a3e9a | -15.12963 | -48.10323 | 2025-09-02 00:09:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 35.3 |
| c9313d1b-7204-395b-977d-469eae0930ee | -11.372 | -43.56989 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6fe76b56-19a7-3d99-b0d4-efdb653cbe34 | -12.46339 | -43.19866 | 2025-09-02 00:09:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 37f6c2ec-49ae-3372-8d25-d7f4c3dfaa40 | -11.80044 | -46.39481 | 2025-09-02 00:09:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 054a6038-80e0-33a0-8c56-38fb108b1ae2 | -11.67432 | -52.25424 | 2025-09-02 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 94660e4c-f71a-3258-8ef0-ba84e3cce49a | -11.35862 | -43.67852 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e46e05c0-9d04-302a-8817-598a11a3050d | -10.27302 | -47.53113 | 2025-09-02 00:09:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| b566764b-285b-348c-bcf2-8ce4a40b4f23 | -11.9635 | -45.85477 | 2025-09-02 00:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0b62afac-830b-3bcb-8ab9-7463ad109654 | -14.26177 | -45.25328 | 2025-09-02 00:09:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| ef18c8be-d01a-39a3-844d-b7e1b49ddc6f | -15.11907 | -48.11004 | 2025-09-02 00:09:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 461dc283-a34a-312f-8f7d-05df27fee0f9 | -13.32722 | -46.9725 | 2025-09-02 00:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4737f085-bd0f-3570-88ad-337ddda6554f | -15.67462 | -48.21989 | 2025-09-02 00:09:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 9255d672-2de1-3861-ab96-70ba39f36163 | -14.59336 | -48.07248 | 2025-09-02 00:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 39.3 |
| aec6c1ab-e27e-375a-9146-3c57d0cbba30 | -11.37831 | -43.6173 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f654cd78-dff5-3eb1-8ccc-a0233b96cebe | -12.44202 | -48.73575 | 2025-09-02 00:09:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 8f1d5f62-58a6-3863-9cd5-1a44bd8e852f | -13.59338 | -42.49569 | 2025-09-02 00:09:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1f15deb8-29ac-35bd-a6f2-6a549eeaddd5 | -12.8716 | -48.0498 | 2025-09-02 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 371f679a-6501-3f7e-974b-9cd8ab51a88d | -15.80262 | -43.56376 | 2025-09-02 00:09:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 879702df-6a7c-3e3a-892e-f8eeb0c73657 | -11.37705 | -43.6078 | 2025-09-02 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 13637b95-49d5-3053-9bae-fc981d6f2b5d | -15.43252 | -43.32272 | 2025-09-02 00:09:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 18.2 |
| ca8e3dc2-7c55-3ed5-b7cf-79dd1837b238 | -12.44548 | -48.7406 | 2025-09-02 00:09:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 201f0386-3183-3def-b178-822620c9967e | -15.78974 | -42.13463 | 2025-09-02 00:09:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 5f976ed6-d4dd-3351-988c-5bec71b00522 | -13.76031 | -43.76914 | 2025-09-02 00:09:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 02dba330-f456-386f-89e9-499983611508 | -10.75873 | -49.58259 | 2025-09-02 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |


[Clique aqui para ver as próximas entradas](README2.md)
