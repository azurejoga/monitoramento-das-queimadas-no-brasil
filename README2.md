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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46946935-0298-3ddb-82c1-816334eae041 | -7.07396 | -39.78801 | 2024-12-18 00:22:00 | TERRA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| d2bfe6e8-b8ec-3d92-adad-99789595d5a0 | -6.97895 | -43.56569 | 2024-12-18 00:22:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 2b5e3bf4-64b0-39f8-ae95-e18ab342cccc | -10.76099 | -40.34229 | 2024-12-18 00:22:00 | TERRA_M-M | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3809a533-1e56-3cef-b224-7c366e58d9b2 | -4.87831 | -41.4053 | 2024-12-18 00:22:00 | TERRA_M-M | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 438c274b-6bb5-39f2-a3ef-ae837e9b9b95 | -4.55049 | -43.29799 | 2024-12-18 00:22:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 10abc407-8a9e-32b7-b240-8367c1829fbd | -4.12804 | -43.57 | 2024-12-18 00:22:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 894d1206-05c3-35a1-9530-69b0687baa3b | -3.69529 | -44.64972 | 2024-12-18 00:22:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d13831ba-c4bc-3a84-9015-3873488368f1 | -6.96919 | -43.56703 | 2024-12-18 00:22:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 0f335c91-0fd9-3c36-bc0c-aa7ef1f69415 | -6.66486 | -39.23821 | 2024-12-18 00:22:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d2e804b6-8af5-3a47-9d9e-f0093d832867 | -6.08503 | -43.97346 | 2024-12-18 00:22:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 40f90d01-ca8a-31cf-9009-c20116cc768f | -3.06585 | -40.04076 | 2024-12-18 00:22:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 34.5 |
| 025b945f-9b06-3e72-a903-6194c2371060 | -5.34095 | -44.28531 | 2024-12-18 00:22:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 26e2962c-2cd9-3f2d-84ef-a8ad09583950 | -4.95672 | -43.71548 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| de981f04-d8bf-36ca-81f6-5f388048ba31 | -4.806 | -44.03119 | 2024-12-18 00:22:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| b1c51c99-384d-3dfd-8e0e-aa43d82f43ed | -9.0911 | -40.446 | 2024-12-18 00:22:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8cf0ea94-e244-3f01-8ecd-37c73451a2bf | -4.16499 | -43.83646 | 2024-12-18 00:22:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 139149ab-ee2e-31c1-bc74-2dcd637a78cb | -9.49775 | -36.04884 | 2024-12-18 00:22:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 6dfd9b57-592b-38b5-87f6-cadf2acd1c53 | -4.93879 | -45.09071 | 2024-12-18 00:22:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1e53d9c4-88f2-36b3-8ce2-569dee3cb63c | -4.00268 | -43.74943 | 2024-12-18 00:22:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fd9f422d-cc4b-30fd-8a69-b2e082a391dc | -10.17633 | -36.69189 | 2024-12-18 00:22:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 421655a4-a9e6-3845-a9c1-3fa17ea682b7 | -4.15149 | -43.56097 | 2024-12-18 00:22:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3635aaa3-1c93-3499-aced-f5d1b8ce2e91 | -10.25013 | -36.36535 | 2024-12-18 00:22:00 | TERRA_M-M | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| bfc4d91a-8b72-30fc-b582-2aba109c6002 | -10.17453 | -36.68013 | 2024-12-18 00:22:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 23331690-5c72-3f8d-993a-6fe7e32c1f61 | -5.92739 | -48.05502 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 168d560f-407d-3d54-b13e-4bf36d280fc4 | -4.00129 | -43.73914 | 2024-12-18 00:22:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ab0130ec-4fd6-3183-8f26-2086cf3e28a0 | -6.43109 | -39.67194 | 2024-12-18 00:22:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| cf97dc14-db1b-358a-8adf-34beb4559e15 | -4.10609 | -46.73193 | 2024-12-18 00:22:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 578e456c-43e8-3c25-ad1a-54b4fc4a9537 | -9.48678 | -35.87921 | 2024-12-18 00:22:00 | TERRA_M-M | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 9de5ee13-c22f-315f-a88d-63577f924b0d | -6.19581 | -44.42415 | 2024-12-18 00:22:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2378f71f-2cc0-3eb1-ae30-71ef1773b01f | -4.92925 | -41.31697 | 2024-12-18 00:22:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3a65d559-f864-3a49-a1c8-f534c1fd0e41 | -9.48707 | -36.0505 | 2024-12-18 00:22:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 0c404ea4-38ac-3c32-a009-a8d1c71ca757 | -9.48425 | -35.8854 | 2024-12-18 00:22:00 | TERRA_M-M | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| 3900b1aa-ba2d-3bff-90c9-4530a2fd79a6 | -6.97067 | -43.57795 | 2024-12-18 00:22:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 931e87eb-01c3-3526-bd13-ec194e2f5eab | -6.28084 | -39.58656 | 2024-12-18 00:22:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 2a0534d1-216f-3a18-803d-b4a2b4b21436 | -4.17429 | -43.97451 | 2024-12-18 00:22:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a1bb8f6f-38c8-34a9-8f4b-b91fbbe62cdf | -4.96632 | -43.71415 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 270.1 |
| 47e7887d-5067-3c15-b9a5-12c9ff1bb6f9 | -5.99856 | -41.58161 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 052d17b9-f714-3d4d-8229-f58f1c2808a5 | -5.80368 | -39.07566 | 2024-12-18 00:22:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1ab75c22-838c-39d7-b377-26d890b93b3e | -3.0776 | -40.05824 | 2024-12-18 00:22:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| dad7259a-6f06-3918-b0a6-3d556acb5fa7 | -4.1295 | -46.81364 | 2024-12-18 00:22:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2523d733-9a45-3dc2-99c0-d746f8179f6f | -9.52891 | -36.07905 | 2024-12-18 00:22:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 3755c2d4-e6d8-3a25-a65b-9b65c6199bc6 | -9.52502 | -36.08552 | 2024-12-18 00:22:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 40.5 |
| d0c497a4-d359-399b-879b-a938bb132215 | -6.05423 | -44.04571 | 2024-12-18 00:22:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7f9054a6-d659-3394-9831-8d6ca8479588 | -5.96997 | -42.31333 | 2024-12-18 00:22:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 6444789b-0a77-39e5-95cb-2c3322db24e0 | -4.96776 | -43.72461 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 464.9 |
| e70ad571-638b-329d-adf9-6be27ac9a4b7 | -5.93368 | -48.06081 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 3f37f685-9cee-3849-8b8b-a345b15477d4 | -6.0657 | -44.05584 | 2024-12-18 00:22:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d79f75f4-1d78-3809-aae7-9873c9fd80e4 | -4.60924 | -39.02552 | 2024-12-18 00:22:00 | TERRA_M-M | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 3c15149e-f68d-3473-b846-3e806d666587 | -5.9724 | -39.75003 | 2024-12-18 00:22:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| b4da6c1e-e90e-3352-b742-6578eee68c49 | -6.76195 | -40.12439 | 2024-12-18 00:22:00 | TERRA_M-M | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 350725b0-4ebc-36f8-8374-f49863f621f9 | -5.93026 | -48.078 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| f7594b8b-9476-3929-9b5c-56edbddade16 | -3.49811 | -43.35102 | 2024-12-18 00:22:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d93ab539-4dd7-30d7-b96f-8280ee8006be | -4.90932 | -42.09897 | 2024-12-18 00:22:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1d41d9b0-ee06-3e08-bf73-8ce99b325123 | -4.87708 | -41.39644 | 2024-12-18 00:22:00 | TERRA_M-M | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 37f0c94c-c15a-34f9-91a6-4e40bdb7b7a5 | -4.61387 | -39.01891 | 2024-12-18 00:22:00 | TERRA_M-M | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6a0cb190-491f-3986-a58d-a731077b6b00 | -4.16317 | -43.96525 | 2024-12-18 00:22:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 70245919-1c39-31eb-b43b-c78afdf4cb41 | -4.16463 | -43.97588 | 2024-12-18 00:22:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9558afd0-38c6-3b1b-8ebe-220d938f529d | -3.98834 | -44.17624 | 2024-12-18 00:22:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 71790001-6c08-3791-a39e-382ea31fcb20 | -6.55534 | -43.59188 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9c59bc54-a478-36a2-9f86-a188c52e95db | -5.13447 | -43.96185 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 3e2636f0-113a-3e6f-bb4b-ce3e4900a32a | -9.40023 | -35.69952 | 2024-12-18 00:22:00 | TERRA_M-M | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| 219205c0-1bce-38b1-b4de-db3154a2e28c | -6.43238 | -39.68111 | 2024-12-18 00:22:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4bd33fe0-c333-35c6-8d65-c970546b72f1 | -6.28989 | -39.58524 | 2024-12-18 00:22:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| ac69d8ea-c9f8-3e46-b80c-4b4cb1ec16a5 | -4.97593 | -43.71289 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 94b0c706-61f3-367e-80a6-0ecda0730029 | -5.93673 | -48.08369 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 40cf7635-5d0d-3601-94f2-bfc0143467fb | -6.75515 | -35.18045 | 2024-12-18 00:22:00 | TERRA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 78.6 |
| 3e0ed23c-9296-3c4d-82ad-6d2c802e75fb | -10.23984 | -36.36705 | 2024-12-18 00:22:00 | TERRA_M-M | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| bc722864-b0bb-310f-ada2-dd992fed8731 | -4.82592 | -38.37252 | 2024-12-18 00:22:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5e6198f5-f944-3369-aee3-724d61339c0d | -5.34173 | -44.2911 | 2024-12-18 00:22:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 11d1b3b5-d5df-3a6c-88f5-d9775bd81c39 | -7.20031 | -44.92895 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 68d635d5-8f28-3c34-ac40-a55758da3f84 | -4.90557 | -42.07182 | 2024-12-18 00:22:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c0aa3a55-03f4-32cb-8000-bdf0fbf355d2 | -5.73082 | -39.54116 | 2024-12-18 00:22:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 183ca668-b52d-33fd-aa35-eafc5a64d3c0 | -6.324 | -43.55429 | 2024-12-18 00:22:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 433827f4-6f3f-35ce-8f3e-651c75bb4d8f | -5.34331 | -44.30259 | 2024-12-18 00:22:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 8f8da45a-775f-3ff4-9104-7849ac4147fa | -9.87008 | -36.21899 | 2024-12-18 00:22:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| f86fea45-1629-3c85-9ea9-fbcd143ec7f0 | -9.53097 | -36.09232 | 2024-12-18 00:22:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| 3cbc3436-1de3-37ec-b453-25ba2fb67b1e | -4.45996 | -44.63816 | 2024-12-18 00:22:00 | TERRA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ad073425-78a9-36c5-96b6-b3d670ccfb3d | -5.95294 | -39.6775 | 2024-12-18 00:22:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 40.4 |
| cf4a8ee7-7d07-3a34-85f8-b68a71664d26 | -4.11861 | -43.57132 | 2024-12-18 00:22:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 01222e38-75a4-3112-9e51-00d575b6b496 | -5.99733 | -41.57267 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| fd8dcc76-edc0-3e56-b4f8-f5900f17a7b1 | -5.34247 | -44.29684 | 2024-12-18 00:22:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| e50476f3-3c61-3471-a292-9504a260dfbc | -6.18982 | -43.46027 | 2024-12-18 00:22:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a1fc8a59-5b01-3807-a34b-7fdb05032b8a | -7.70007 | -35.10777 | 2024-12-18 00:22:00 | TERRA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 29.5 |
| beba2749-8086-3818-b341-488b27e84def | -4.92039 | -41.31822 | 2024-12-18 00:22:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e7f3957b-93d4-3cc6-bf8d-ce0b05882f53 | -3.66677 | -42.03225 | 2024-12-18 00:22:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f27f5f81-b663-3eb2-b7db-57514a0665d9 | -6.36171 | -43.37147 | 2024-12-18 00:22:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 98c2fad1-d27d-317c-94b5-9e67dca83a20 | -4.22069 | -44.31098 | 2024-12-18 00:22:00 | TERRA_M-M | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0db080cf-da8f-3943-9964-3ce653e2296b | -4.38146 | -42.14505 | 2024-12-18 00:22:00 | TERRA_M-M | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| a7cdf550-7d32-3c55-b9ad-99d75bf6e570 | -3.06717 | -40.05015 | 2024-12-18 00:22:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 0cfc8673-8bbc-3f04-9728-a9b076154c7c | -5.81296 | -39.07436 | 2024-12-18 00:22:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7d872209-4436-397e-960f-afed618ee22a | -4.9692 | -43.73513 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9cd6a552-cd24-3c58-9cf0-4d213f288b66 | -6.21094 | -39.67848 | 2024-12-18 00:22:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| bc708b2e-0f91-3b16-924c-e06c8bc2b7b4 | -4.97738 | -43.72336 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 349.7 |
| 596c3c3f-81f0-3a64-b89c-dec1b8304d9f | -4.15285 | -43.57109 | 2024-12-18 00:22:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 992a17ff-6d20-3694-874c-16fdc8a08cbc | -4.95814 | -43.72591 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 687a9f01-a836-3ca9-983e-b783c0f7f856 | -7.25461 | -40.1601 | 2024-12-18 00:22:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| aaba02e4-1c8a-3eea-91f3-9c51a2c60d15 | -3.49678 | -43.34131 | 2024-12-18 00:22:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3ed0e78d-9810-3922-869c-dc0c14d31598 | -4.10055 | -46.72607 | 2024-12-18 00:22:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 227ad7f4-6ff4-323c-b967-8ed60e8d5177 | -4.93171 | -43.96864 | 2024-12-18 00:22:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 41b536ee-7e81-34c2-b22a-49bad643b047 | -4.12665 | -43.55994 | 2024-12-18 00:22:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |


[Clique aqui para ver as próximas entradas](README3.md)
