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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80f18f11-f968-394c-8a0f-e46df67d8b7d | -8.34047 | -50.87448 | 2026-09-22 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a57335ec-093f-383a-9df8-bd419584ac99 | -8.25587 | -55.25522 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 162825b7-9a3b-3185-9e45-e2328475eced | -6.58114 | -44.1557 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 93ca8ce6-99bb-332c-a7c1-c4cbfb450ad0 | -6.75103 | -59.11268 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5d3a26a-0626-35c7-89fd-2964c1752149 | -5.46055 | -60.14566 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95ad20a5-ef8f-3210-8e2a-fcc29e211a78 | -6.577 | -44.15748 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9089e4a7-493f-3cf6-8ec5-ddcb2113b1bb | -10.6953 | -48.71899 | 2026-09-22 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f1badb99-beff-3940-b178-254e95517b38 | -8.81642 | -45.36979 | 2026-09-22 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8366a6f3-f9fc-3293-9480-b68321e52bc6 | -8.35097 | -50.8725 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28b1053c-20c4-33cc-ae57-dbc5616416b7 | -6.0408 | -53.27844 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdd14b53-fc9b-35c1-86fa-4996b1f4a1ec | -6.1379 | -59.94781 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 967c1f63-0bcd-3bba-b623-9114e1302351 | -3.04001 | -57.41877 | 2026-09-22 04:46:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6249784a-51bd-3c15-8af7-aae0a1d0b2e1 | -3.06731 | -54.41648 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8a5b490c-c6d7-3d8c-b924-47e5160218ab | -5.72878 | -53.46801 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bc93f00-b94c-373d-83d8-b2de5d223cc5 | -3.40449 | -59.58479 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f647460c-5d6a-384b-a25f-a3301372a6f2 | -4.65212 | -50.99301 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28ca1e7f-394e-354c-a59c-5200c0aee722 | -4.27997 | -56.25698 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48b961ce-34ee-3744-872b-3d5b6203c5fe | -5.88907 | -52.28264 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91ac358a-a86f-35c8-aff9-db01e1190c32 | -6.03975 | -57.82429 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4a0baf3b-7cbc-32ae-8954-d1a1297e5409 | -3.902 | -51.89019 | 2026-09-22 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9834066d-7d4f-35ff-a7fa-1be801528c0c | -10.68917 | -48.70961 | 2026-09-22 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b640c486-1fea-3690-8ac9-ffccd012eeb1 | -4.51846 | -55.76234 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e7c5e65-2698-338e-9eff-ad3db99a6f7e | -6.6191 | -59.92118 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 08c4ff36-fee3-351e-aafb-f79f56d0099d | -3.37984 | -50.40601 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 433255e3-77e9-30d3-9a2d-8cbd7104b874 | -9.72454 | -47.76579 | 2026-09-22 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee9ffb92-6c4d-34fe-bd40-80f5690d07a9 | -10.458 | -51.274 | 2026-09-22 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1baf4f09-fc33-3049-b7de-6fd7a4fd45e4 | -8.43542 | -45.81559 | 2026-09-22 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9854773-c228-3240-a518-608787da6471 | -5.83629 | -52.11874 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab6565d4-2b2d-31b8-95b9-3fd3232aff5a | -7.82589 | -45.25683 | 2026-09-22 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f26069a0-a1a7-39c3-8ec4-45846df7898e | -5.21093 | -56.10135 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5543eae1-76cd-3e8b-b06d-70b2285c9e3c | -5.81412 | -57.73956 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c90dbfd2-78aa-3250-bbff-bf84ff97e167 | -4.95884 | -55.82724 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d156417-efcf-37f4-b33f-5f1b8b7a5928 | -7.33631 | -55.60526 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 478097e8-0ab8-37cf-b38d-9f3d36618df6 | -3.40503 | -59.58152 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8884289b-031e-3d12-b958-0c55b54e1f8e | -6.73221 | -55.07237 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b366ed0-c8ba-3b63-a4a4-4240e0f73a60 | -9.6772 | -54.34225 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eff11fce-62a8-320a-8fca-af75bebbb872 | -5.75654 | -45.09373 | 2026-09-22 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 538a151b-89ef-3382-bc36-8f130d157121 | -9.55894 | -46.54814 | 2026-09-22 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49ed8191-7031-3807-b02e-8df7de37c973 | -9.55441 | -47.95232 | 2026-09-22 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5837f56-1cb5-3648-9e14-4bcfabff29c2 | -3.06256 | -54.41769 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 47b305a8-599b-33d7-9c84-94db55e673e8 | -9.48373 | -54.44328 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6f5aedd-bfb8-3daf-aa12-5f05de704402 | -7.33173 | -55.60923 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8a8122a8-1181-34ce-a4e2-6050661004c6 | -5.96304 | -51.94125 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f4a03026-4a32-35a5-85ef-667f4947a826 | -7.23849 | -55.58686 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6de7dc9b-1570-3ef0-b923-873e8786fd60 | -6.00211 | -45.2457 | 2026-09-22 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ebffff4-d68c-32e7-bf26-679dfb4a66bc | -6.62314 | -59.92828 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4e0eecef-2c55-3fb4-b54b-419605a172a7 | -6.45793 | -59.97137 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a64c2d1c-add0-3a38-9b68-17c2a7fdd60f | -5.6238 | -43.37093 | 2026-09-22 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c915536-9328-3bd9-adbb-c77648425bd0 | -4.86914 | -55.83772 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2173222a-c8a7-321c-922a-227d556923f7 | -5.3073 | -49.07526 | 2026-09-22 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9acaac63-c690-38c1-ae63-9890fcb15e17 | -6.97399 | -42.13347 | 2026-09-22 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 68863371-523f-3675-8387-8ed28e507c5c | -4.27345 | -55.43985 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e588514-3451-3ce3-ac76-de4ac022b675 | -5.78205 | -43.77571 | 2026-09-22 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce8801be-f4a0-3e8a-a72b-29524a92fe4d | -3.06771 | -59.30434 | 2026-09-22 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 40a96dfd-fc07-31a2-824a-e26b299959f5 | -4.07216 | -56.22673 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac2b6c9d-d82f-326b-9c62-846d1b56a344 | -6.65792 | -50.93841 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4af51267-7504-3da0-90f8-ec40f038fbac | -5.93332 | -59.97907 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38a7248f-4283-381b-b802-60b2e4d2352b | -9.2421 | -57.14518 | 2026-09-22 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dde179bd-8398-3c65-aba0-712c5a7d6daa | -8.83765 | -50.49055 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bff0ab92-9d3d-31bc-b3e5-1f2eb09337d5 | -6.08201 | -57.62674 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| af8a740d-831b-37bc-b86d-a3f99480133b | -8.41616 | -46.86233 | 2026-09-22 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 188320ca-14bc-3d06-a1cb-c1d092361cf0 | -9.75395 | -54.29907 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46a4e0e3-ff05-3d2c-ac7f-4b66f9d214c0 | -5.89518 | -52.15686 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47bebe31-a5c9-3b08-80e9-a077e6dc7dd2 | -9.60708 | -43.93217 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e1fec48a-ee62-3b07-91aa-6f57a1cca45d | -3.5844 | -50.6421 | 2026-09-22 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 662e2524-9ab7-33a9-bdeb-ceebb33e9025 | -6.56744 | -44.90242 | 2026-09-22 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cac712cb-ec91-3b98-9730-80bfda7fe086 | -8.31636 | -44.74364 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e801f5a2-5879-3200-9617-8db155049cb9 | -9.69422 | -54.32516 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe104835-7b26-3cd6-a12e-34c8e327f8aa | -7.29295 | -59.52435 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f92144fa-1815-3e5b-a10f-801056f08a82 | -5.78675 | -43.77641 | 2026-09-22 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c7637500-247e-30dd-a08d-3e15139025e8 | -6.92296 | -59.63041 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 058b7011-fd6f-3f32-9c4c-5073178e9efb | -8.79064 | -44.29436 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e600cae5-13b7-34ea-9964-448aa172f82d | -8.78656 | -44.28885 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 53358462-9223-3ffd-a864-13f542cdd00e | -4.60827 | -55.75241 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1d56572-f673-35d4-8722-80f1c5a023a9 | -8.18693 | -54.77918 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4741df53-bbdb-3903-a9d8-c53550a169bb | -9.15519 | -50.01336 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b25d9274-f572-3490-8dbc-591d1e51c913 | -8.31663 | -44.74527 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee68e931-0a7a-33f8-bad3-a04161d7391d | -3.39879 | -59.52013 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 87c2830f-1c7f-3953-87e3-f474565ce425 | -3.45838 | -50.60082 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c9496ab-6d35-3b54-bb6a-4e056efcf035 | -3.87321 | -51.18736 | 2026-09-22 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2197f92a-564a-302d-abcb-66b82728c952 | -6.45992 | -59.99077 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| af8aea4e-f6f5-3bbf-8873-81d3b2621205 | -9.67499 | -54.3339 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6653eeff-d740-3dd9-82f7-8df9422e9ef0 | -6.79672 | -59.13708 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16cd0572-9b29-3207-bffb-4f1af6e35186 | -5.85312 | -49.78847 | 2026-09-22 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9ca3dce-a329-3dc6-a71a-a289a351f2ad | -9.28316 | -45.92797 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7299cc1-832d-3682-8043-34af0173d448 | -8.8343 | -50.49003 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f176a7c2-8231-3086-ace7-0e510d2ff62a | -5.37631 | -55.90751 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 993ef1b1-afb5-3c06-b80b-e5ff3d028704 | -3.68425 | -60.57581 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0240bb52-0543-300e-a56d-e5e9c463bdd0 | -8.62644 | -54.61983 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb95f7a7-41c0-31d0-ae70-02ee05db7394 | -5.45684 | -60.14424 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eeb26d6b-58bd-3e9e-881b-5c0fc514ac0b | -9.62522 | -43.94611 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 84c00019-fcfe-35ab-8215-b98960915c13 | -3.3411 | -59.87173 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22ca3dcc-65bb-326a-8b5d-a01f6947c90e | -6.8384 | -55.53997 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c4e9bb1-f8a0-3050-9a7c-edac0fffa592 | -4.14251 | -51.0992 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dae0180-4f2c-3db8-b64e-977c83613f51 | -8.102 | -55.34509 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adbe4d0e-6c92-38e6-8f93-abb5fb95405f | -7.3453 | -45.3437 | 2026-09-22 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7e7fbba-5255-3fbd-bf63-34186dd47244 | -7.29103 | -59.52777 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 255ed67a-9e5c-3c5f-8dc0-30c54db9f936 | -5.87572 | -52.1286 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d8d2441-55e1-36b4-9c94-196c9dcb462a | -3.72228 | -60.57618 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb54720c-d7e0-3bf1-8264-e197ed222a5a | -3.39245 | -59.52576 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README66.md)
