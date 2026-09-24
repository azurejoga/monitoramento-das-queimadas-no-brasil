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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f255d91-79e2-381f-b748-98bfccb98095 | -3.6763 | -60.5839 | 2026-09-24 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| e86aa66c-a60e-33ab-850a-b708d47a1d73 | -2.1119 | -49.5143 | 2026-09-24 00:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 747a0f7c-bec7-37da-88f4-79b96a4a071b | -3.1637 | -54.6054 | 2026-09-24 00:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 51a223c6-ed84-3431-b4b3-53c4016d70c9 | -12.0727 | -50.7474 | 2026-09-24 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e399f95a-5400-32ed-acdb-02d9ae27c952 | -5.7756 | -45.0826 | 2026-09-24 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 7d043b68-98e9-3a6d-ba57-2ce1273edd66 | -9.8491 | -48.4927 | 2026-09-24 00:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| c0a20eb6-f428-393c-adb3-39851c4670bf | -3.6946 | -60.5835 | 2026-09-24 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| ecd9ae4f-9410-3eb5-9c86-9a9ccf5d9f72 | -15.5686 | -42.3547 | 2026-09-24 00:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 97.3 |
| c79632da-26c7-3111-b63a-553034b9951a | -11.247 | -51.3706 | 2026-09-24 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| eebb0d00-91fe-312f-84f2-15d19b984c62 | -4.118 | -51.0903 | 2026-09-24 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| e409d7e8-2f2b-3fbe-811a-91644d18b4c4 | -6.4487 | -59.9526 | 2026-09-24 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 914049e3-dd82-367e-b534-8e252a9e37b2 | -6.5962 | -59.9279 | 2026-09-24 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| a0da82c4-d16b-38b3-ad95-574dedebcb4b | -2.1303 | -49.5139 | 2026-09-24 00:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 49bda431-1366-3f81-be60-fde1b2e5bce3 | -10.4233 | -49.3432 | 2026-09-24 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 060d6023-0537-3db2-a2cd-0fea9b39e4a2 | -6.789 | -48.6779 | 2026-09-24 00:30:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 37d3542c-15df-321d-92cd-42700b12243b | -3.6947 | -60.5455 | 2026-09-24 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 79b05e7a-5e8c-33f1-b0b8-0405dd954052 | -12.4216 | -46.9551 | 2026-09-24 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 296.1 |
| 732069ef-4f1d-328e-b929-e0f1c0b5c8b7 | -10.2827 | -49.9606 | 2026-09-24 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 1590842f-dc93-32d2-a2ea-58bc98032218 | -3.6947 | -60.5645 | 2026-09-24 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3faddd88-47cb-3ec0-b132-97f1a47b163b | -9.0158 | -60.5138 | 2026-09-24 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 72c0edee-4682-3091-90e2-97d3024811cb | -8.2616 | -54.7776 | 2026-09-24 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e0cdab01-76d2-3545-b281-9a23d8164b2a | -10.0917 | -46.0458 | 2026-09-24 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 67828015-5f72-3469-8ecd-6c7edbfd445e | -15.2517 | -43.2501 | 2026-09-24 00:30:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 135.0 |
| 325b8603-7c50-3fb7-a760-828719291121 | -11.9583 | -50.7607 | 2026-09-24 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 246.8 |
| 5e4f8fda-be68-32ef-8840-ba91f1c52ec8 | -6.7211 | -44.1618 | 2026-09-24 00:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| d08ad810-6485-3228-bdc9-1d3fed7c14ee | -15.2314 | -43.2784 | 2026-09-24 00:30:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 0248b160-b0b5-369b-9fdb-6464f8091a40 | -11.958 | -50.7821 | 2026-09-24 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 993e0356-0266-319b-a064-e3c9b4d90a28 | -15.2511 | -43.2743 | 2026-09-24 00:30:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 143.9 |
| 77fbd4bc-dc57-3b18-9150-6a29736a1f3f | -5.6016 | -60.1919 | 2026-09-24 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 475a385a-f237-3bf5-b5ff-3effd4533b42 | -13.4732 | -46.274 | 2026-09-24 00:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 54.9 |
| b59a3351-bb3e-37a4-b50b-c510410241c2 | -10.9115 | -53.9429 | 2026-09-24 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 1aa440c2-3064-3119-928a-c2ce30713806 | -6.4302 | -59.9724 | 2026-09-24 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| cf19a4a4-ccb5-34cb-813e-ccaa0cd3abb3 | -2.1118 | -49.5355 | 2026-09-24 00:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 7b19ca04-55b7-3096-aaaa-ea2f453ffc95 | -12.422 | -46.9326 | 2026-09-24 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 043f9a92-84b0-34e8-9a5b-8112774c84ce | -6.4303 | -59.9532 | 2026-09-24 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 392115cd-3310-36e1-87fb-def00f207448 | -3.4387 | -60.5695 | 2026-09-24 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 616b868f-73cd-3d89-a953-082164003755 | -4.2951 | -49.1234 | 2026-09-24 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ed41bd15-f1a9-33de-a08b-8f678374401d | -13.78756 | -54.06344 | 2026-09-24 00:37:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| ccebd43a-a0a2-3230-9f9c-faf075904878 | -14.46736 | -53.64338 | 2026-09-24 00:37:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 9f14b7dd-54aa-3e71-bcb6-a5a589a8ad37 | -13.79608 | -54.06889 | 2026-09-24 00:37:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4ea33f3b-3135-395f-97d5-ab9ca99a1971 | -13.79414 | -54.05652 | 2026-09-24 00:37:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 34.2 |
| c617e901-8f1c-3b49-81c6-01c27d0c7a59 | -14.47292 | -53.64857 | 2026-09-24 00:37:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 18ac7133-a93b-3619-972b-cc7391e93d98 | -14.57611 | -54.13294 | 2026-09-24 00:37:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 64d5eaaf-63e0-3b53-8569-fe7935b761cd | -14.56407 | -54.12231 | 2026-09-24 00:37:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4003a8b0-71f1-3bfe-93a6-27eb5d8f871a | -15.46611 | -47.90275 | 2026-09-24 00:37:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 07a67006-d4c2-3696-a5f1-6d7c041fe382 | -17.5899 | -54.04879 | 2026-09-24 00:37:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9154ee5b-1480-3e9c-a82a-71647e0af765 | -13.78565 | -54.05087 | 2026-09-24 00:37:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| edfd43e0-8d6d-3563-b040-8fec8e3db85a | -13.79785 | -54.06168 | 2026-09-24 00:37:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 825aa0f8-c81f-3623-bef9-179b0a8834c3 | -14.47085 | -53.63499 | 2026-09-24 00:37:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| d63f6ab0-b41f-37f1-9f5b-deb569b9047d | -1.8237 | -55.719601 | 2026-09-24 00:38:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1274c9a7-6c99-3a5a-9699-c53e711dd57e | -3.5524 | -43.465698 | 2026-09-24 00:38:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ea687fe-6072-3030-bb69-d1edae7a12bb | -11.2404 | -51.354698 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 984c1179-755f-32f0-a8e1-10ef5baad2fa | -5.32 | -43.404099 | 2026-09-24 00:38:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5793f96-15d8-3565-aad0-751861a45936 | 1.5795 | -55.920399 | 2026-09-24 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b31ed7f-13dd-3a39-8183-6a51b18d7b68 | -2.1694 | -48.3148 | 2026-09-24 00:38:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db1b9e17-1302-3f41-822d-b48b1bbf8c64 | -1.9461 | -50.214001 | 2026-09-24 00:38:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a098e2a-3fed-390f-96cf-394fb8760a4d | -7.2724 | -45.542099 | 2026-09-24 00:38:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d7831a5-558a-34bd-8ba2-b610d9111a8d | -9.8391 | -48.483601 | 2026-09-24 00:38:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c366b387-eac0-3e8b-a6ce-0a7d3e15d957 | -16.242701 | -42.966499 | 2026-09-24 00:38:00 | METOP-C | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 862678f8-4400-35f9-83ae-fdf1c89767c0 | -15.564 | -42.344002 | 2026-09-24 00:38:00 | METOP-C | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4604dad0-3f98-32e3-8106-ed8e28a66938 | -10.2728 | -49.968601 | 2026-09-24 00:38:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2761e12-ebd0-3b4d-8edd-17172ebeb50e | -3.1506 | -54.604698 | 2026-09-24 00:38:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 451842ff-4657-3ff7-aa67-0973ad9a1125 | -5.7758 | -45.1049 | 2026-09-24 00:38:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b772eb17-0e03-3c61-a8ac-8b028823ad7e | -12.0854 | -50.756001 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5f361c0b-1eab-3084-bc82-a706c9b0fd82 | -11.3633 | -43.370899 | 2026-09-24 00:38:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 290b6039-e6fa-38e7-bc5b-ef96e39d6a61 | -1.6305 | -54.915401 | 2026-09-24 00:38:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0a1be21-9fd3-310e-971d-6b1ac1a18d26 | -4.4232 | -55.073299 | 2026-09-24 00:38:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9b5b65d-f0a0-3ba9-bf2c-b7644c4ff30f | -13.7001 | -43.067101 | 2026-09-24 00:38:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dcd6815d-e4a7-386a-bfc4-6c244130fa06 | -10.0847 | -46.0429 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd0d86b4-98a9-32f9-901a-aeb45198614b | -12.1714 | -47.358299 | 2026-09-24 00:38:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20a1c8e7-2751-3407-8a15-e6be27f59e7a | -9.4032 | -40.2892 | 2026-09-24 00:38:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 06d71948-1122-3bf5-b1a1-5b4a58749e52 | -11.7888 | -50.997601 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 026519e4-f512-3b8a-91a7-7941c419f5e6 | -1.2706 | -57.022202 | 2026-09-24 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68238ca3-ddab-3758-9e98-f38036be3ae3 | -3.1669 | -51.361099 | 2026-09-24 00:38:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58419c71-015c-36da-870f-61c70cee8d77 | -1.2193 | -54.554298 | 2026-09-24 00:38:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa0583e0-bb0b-324a-aa19-97b8bb8445b1 | -13.3822 | -41.3106 | 2026-09-24 00:38:00 | METOP-C | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7d810f03-68b6-35a3-87ce-2592b8267fb5 | -9.8438 | -48.5047 | 2026-09-24 00:38:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e23ba15-5d68-320a-8fa9-66b6a28c479f | -8.7228 | -47.6087 | 2026-09-24 00:38:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11553eac-d73e-37f0-935a-94f50ec91ef5 | -8.2674 | -54.764301 | 2026-09-24 00:38:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e9d302c-0f44-3905-918c-60476fb6565d | 1.6072 | -55.890099 | 2026-09-24 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06e7e745-0d27-36b9-8364-4dd5be0c1ffe | -5.1909 | -44.682201 | 2026-09-24 00:38:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96fd31ef-332c-302a-b291-8e251c9a8a46 | -2.1172 | -49.5219 | 2026-09-24 00:38:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 733053c0-7315-37bf-ab4d-c63bbe1dd191 | -1.3539 | -49.1633 | 2026-09-24 00:38:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad76b6ad-8b0b-34a8-96cd-bfdf495e7793 | -9.8454 | -48.5117 | 2026-09-24 00:38:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c9525ed-2222-38f7-baf6-e423f007036a | -10.9292 | -43.843899 | 2026-09-24 00:38:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ae0b2e19-779a-3667-80a9-18ee29985e71 | -6.4339 | -48.467201 | 2026-09-24 00:38:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f3268a47-8723-31e9-b4a4-e292974e0aac | -11.007 | -49.709301 | 2026-09-24 00:38:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 552db410-6286-3631-b420-45b34e75a0ee | -5.7912 | -49.174099 | 2026-09-24 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0a2de78-7ffb-37d2-afaa-ae014f55e6e2 | -10.2826 | -49.9664 | 2026-09-24 00:38:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ebb3717-0388-358e-a1c8-19dafd53575e | -11.258 | -51.341202 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9c5af110-5b99-3611-8803-f093a66dad96 | -4.1108 | -51.073399 | 2026-09-24 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 362c20a8-1dca-3e62-8ba3-c02c1ca50fdb | -3.4439 | -50.090801 | 2026-09-24 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff66ec1e-93e9-347b-91af-9b64e92776f0 | -5.8471 | -49.872501 | 2026-09-24 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3fe6946-9c0f-346b-8578-b1957d8a3c93 | -7.4762 | -44.569901 | 2026-09-24 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 995f5ec2-10f7-3166-bc2d-8cda1fa6f433 | -6.4324 | -48.4603 | 2026-09-24 00:38:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| bc92b934-a1a2-31d9-babb-ac3d35ccc970 | -7.4219 | -49.823101 | 2026-09-24 00:38:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46791a07-44d8-3696-b500-5009fd986807 | -11.1272 | -48.303799 | 2026-09-24 00:38:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83f5ddd9-4a4f-3d9d-a4fe-da7323d2645b | -13.656 | -43.355999 | 2026-09-24 00:38:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dc28c050-c8d1-3886-a325-15af0932af52 | -3.7873 | -52.417599 | 2026-09-24 00:38:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf4b9a52-ba69-3732-aa07-97b54cfdadaa | -4.8151 | -43.534302 | 2026-09-24 00:38:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README11.md)
