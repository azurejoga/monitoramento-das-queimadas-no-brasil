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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 835e888f-fa2c-3ecc-af78-4c9bb2a417df | -11.41969 | -46.10697 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa2a9fc0-f8a4-3d4e-b45a-3aa4a4b3c098 | -6.98228 | -39.11159 | 2025-10-27 03:42:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d3a63871-dfec-3401-9b41-3e24cd39c0f9 | -10.33411 | -47.22546 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7967d560-82a3-341a-9000-ee0278c04291 | -7.2357 | -44.98627 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 376e7c41-74ab-38ab-b824-c3cf1537eedf | -11.06953 | -48.34803 | 2025-10-27 03:42:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd2d555b-bef8-3c38-97f9-2c032d14c5e6 | -6.82992 | -44.0019 | 2025-10-27 03:42:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de755940-fa9c-3514-bd2b-e21aa708d19a | -8.21048 | -43.8048 | 2025-10-27 03:42:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 218d84ab-6c1a-38eb-bfce-14a6db929eb8 | -7.91935 | -45.6647 | 2025-10-27 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29288b08-1f93-3eec-add9-dd148a2c0d49 | -7.33387 | -42.45142 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9df79b03-8e73-3315-a38d-8cf36cd7e12e | -10.35112 | -47.17115 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 546ccc58-fd25-3a2f-9f6d-cad6f0598849 | -10.41094 | -45.30827 | 2025-10-27 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b3e02bf-1b33-3636-abbb-e0342ed1ec83 | -6.49516 | -42.2169 | 2025-10-27 03:42:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3fc3ef13-edc6-3231-af3f-6841032698eb | -6.12737 | -42.45178 | 2025-10-27 03:42:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 22cba4c8-d176-3782-bc8f-8d04204b012b | -8.32155 | -46.17834 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f31e379-917e-3d2a-8e64-a04f2e100575 | -10.79093 | -44.87569 | 2025-10-27 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c09bc7e-7492-3d93-a379-23af66a6346c | -8.69628 | -44.43999 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 587f87bb-b056-3285-a5d7-c79ea1d37258 | -9.58625 | -44.94603 | 2025-10-27 03:42:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d038710-43af-3268-81e5-20b50bda11c0 | -7.77074 | -45.3909 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 549a26ee-005e-3db0-9b65-ebb73a7e2d61 | -9.99653 | -47.1966 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9eabbba-ce6d-3d37-87ad-2ff5a38bd142 | -11.79047 | -45.25942 | 2025-10-27 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61f800b6-e2f8-3610-952b-375298cf2366 | -7.59748 | -45.69109 | 2025-10-27 03:42:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 860b263e-5ec7-3f72-89e5-9a07eeeb7888 | -7.83114 | -46.50055 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 88d4eaad-ae45-3cbb-bc97-35665b82cdaa | -9.22938 | -45.84166 | 2025-10-27 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe5f3b83-2162-3b62-b558-bede9d1cfe6e | -7.84905 | -46.47097 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfdb788b-bc4b-3e8f-b7a3-bf463087f409 | -6.37723 | -44.26827 | 2025-10-27 03:42:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c16d20fc-5980-36d5-97a0-57c613346d7b | -7.82368 | -46.44074 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37fa8177-81be-3d3d-acaf-5c5787452030 | -10.91772 | -48.02735 | 2025-10-27 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0feba6a1-16d7-3735-9c4c-6734066d4adb | -8.70085 | -44.44422 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfba21b8-0158-3681-bbb5-3f324ca63387 | -8.52608 | -45.56451 | 2025-10-27 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 93eb0099-3996-3077-8cfe-f4575523ca68 | -8.11671 | -47.03218 | 2025-10-27 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01906bb1-e2ec-3dfb-a106-bfe6bca8d132 | -10.50459 | -47.67709 | 2025-10-27 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 079ac534-8745-3d55-85b1-a3244749bba3 | -7.79845 | -45.38457 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7c53fea-1598-3a2d-86bf-ef75e8a8367c | -9.57975 | -45.18637 | 2025-10-27 03:42:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 312b3c14-9cac-3e2d-a1c5-6f82d7cdc7df | -6.44859 | -42.35078 | 2025-10-27 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3c5940eb-c351-3b7d-8350-ee3dd3903572 | -8.06781 | -46.95974 | 2025-10-27 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1bef4c5-57ae-318e-b3bd-8f21da9d8801 | -7.34026 | -42.44235 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7cf0c8f8-f25a-3883-beec-0516b8acc9da | -8.06636 | -42.49335 | 2025-10-27 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d0dd8aa5-3bd8-3890-9148-f482294ba710 | -6.25327 | -41.84022 | 2025-10-27 03:42:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 54d61de8-49cc-3867-81f5-198d68fa4d95 | -7.78307 | -45.37377 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28bb0f79-f070-3aa9-80b1-48b66f32fea8 | -9.82551 | -46.932 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6dee2db-036a-394f-b4ef-2e9333dcadd6 | -8.83142 | -45.41793 | 2025-10-27 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff5709dc-d83e-3891-bb07-22383d784813 | -7.5994 | -45.68692 | 2025-10-27 03:42:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8a308de-b860-3117-b609-d6bea996dbaa | -10.35352 | -47.19053 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb238591-ed48-3549-b046-73325134ccf4 | -5.65426 | -46.46335 | 2025-10-27 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7bf8912-babb-3e0d-8655-444844c78348 | -10.83045 | -47.63049 | 2025-10-27 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a0972c7-4a93-3311-856f-8be9e9d4f693 | -10.68101 | -47.84095 | 2025-10-27 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2fc9e3aa-152d-3ffe-8d73-42fe31d50f35 | -7.96196 | -45.47828 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1a58f973-61b7-38d9-948a-f404c671c579 | -7.77148 | -45.40497 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ae578c3-9f5f-3bbe-afc5-c4f2a62d6d1a | -7.68192 | -46.34532 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2288c3c0-aca6-3e55-ae52-90127a5c4be3 | -9.18437 | -44.57603 | 2025-10-27 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18f5a09d-7a9f-31a9-90b1-97547b0e6485 | -6.99909 | -47.00417 | 2025-10-27 03:42:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f482dc12-d5b6-30ed-9398-4ff49884e935 | -9.05972 | -45.10761 | 2025-10-27 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95de2193-ce79-3c89-9db1-a306dde028ba | -6.17895 | -43.7404 | 2025-10-27 03:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 761f578b-2d28-38b3-b71f-d3057c987470 | -8.06872 | -46.95495 | 2025-10-27 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 251efe1f-4cdf-34f5-a4da-e2dd3f7bca40 | -7.83211 | -46.42873 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eee31228-00d2-3ec1-b202-b9b971ddeb79 | -7.85083 | -46.46136 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0921a241-f912-3871-a6e4-8d107cc59778 | -10.92123 | -48.02676 | 2025-10-27 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd66c930-5cf3-3ba1-9ac9-12c304e352cf | -7.76372 | -45.39777 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c8867dc-f680-377d-985d-d5ad807a7aac | -7.83713 | -46.50177 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 883ce461-0276-39e8-aa42-041a9c2b2569 | -6.81641 | -41.56284 | 2025-10-27 03:42:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 72d6f2a8-5bc5-3c08-b7e2-50f8640bf762 | -6.4558 | -42.33665 | 2025-10-27 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 323c2890-f5a2-30f5-9c57-8841f5b99cf8 | -10.34736 | -47.18078 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d33990e9-ecbf-37ab-96d7-64a5afb6badc | -9.58802 | -44.94302 | 2025-10-27 03:42:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d973087-228a-353e-9ebe-817adb48d4a6 | -10.31369 | -47.19371 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| abd23a7e-d0dd-39ff-beca-ebb9c976c51e | -8.95965 | -47.19495 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 30e5c4a3-1079-39fd-a2ee-25fbfc9840f4 | -8.66968 | -44.75927 | 2025-10-27 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f73778c1-42c2-3bf8-8aae-b9a19f288bef | -7.76997 | -45.39519 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2a6455c-6242-349c-a70b-70970ac08f04 | -7.25013 | -44.96935 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89438cf8-1c0b-36fb-99e8-dc85dcdc96d0 | -8.32234 | -46.17408 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3af68054-bfef-3af7-aebb-0d6ed41f75e5 | -6.88286 | -45.14963 | 2025-10-27 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f234757d-3d4b-3a07-9c99-441cc29bcde2 | -10.75244 | -44.2019 | 2025-10-27 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| aed2e3f8-54d6-38e2-b0c3-ae47e99d262b | -10.07217 | -44.86569 | 2025-10-27 03:42:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8396e69-2ab5-3690-a0b8-aed27baf2678 | -10.31727 | -47.17517 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90f69b14-38cf-3a3d-91e5-63d3dfcab536 | -8.09888 | -47.05831 | 2025-10-27 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 917eb042-a403-3648-be6f-0172a9ae06c8 | -8.02983 | -46.75671 | 2025-10-27 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4d3d08cf-1f62-3475-9ad5-a6155ce5281e | -7.24356 | -46.96766 | 2025-10-27 03:42:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c3063602-7c98-3899-8685-bf14475ca7b6 | -7.95948 | -45.47479 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f87829ce-5b13-3842-97d3-7b64f5364606 | -7.84823 | -46.40863 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5bb2540-611c-3fbb-9a9b-2b59fafc722e | -11.42377 | -46.11563 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d0bf46f-ca11-3771-90cf-6285618ec268 | -11.7892 | -45.26098 | 2025-10-27 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 005a0ac5-df54-3a5d-a787-8e602ff725aa | -7.33194 | -44.02984 | 2025-10-27 03:42:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ddd0b53-2bf8-3dc4-96b4-3b45ead7e5af | -7.24648 | -46.96589 | 2025-10-27 03:42:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a1b95f9e-8357-3f41-a196-4e285b812f84 | -9.22858 | -45.84587 | 2025-10-27 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3762051b-b498-3cd6-850a-91feb6751128 | -6.87937 | -45.16891 | 2025-10-27 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a2be8e2-6109-398e-a8d7-b4d747ce78e0 | -10.32304 | -47.21825 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d299f1f-c4c6-30cb-8ac7-53028aa437c9 | -7.96655 | -38.28113 | 2025-10-27 03:42:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fa6cfaa0-e882-3dc5-a2b3-5585437813f7 | -8.12208 | -47.03756 | 2025-10-27 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12061291-6dfd-3ee3-89ad-6f1a5e470cda | -10.31704 | -47.2088 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b2eef69a-2230-37f4-995b-c41b60f8e645 | -8.88302 | -47.99725 | 2025-10-27 03:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2dbc14de-6364-3dd3-9590-8adc9e90ffc6 | -9.86238 | -44.8883 | 2025-10-27 03:42:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9323e12-c543-3efc-b236-f82d27306bcd | -7.82692 | -46.48986 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b765d8e5-ec0b-326d-ad4a-e3538719764b | -9.89282 | -45.75981 | 2025-10-27 03:42:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6056d5d-e9c9-3019-abf3-5fed0fea0050 | -7.83201 | -46.4959 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ef2eeeaf-cb30-3ccd-a5f3-adb66574340e | -7.95878 | -45.47865 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d0666236-2244-33c4-9a2b-2e9b4bbb4070 | -7.863 | -45.71494 | 2025-10-27 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17e4fd5a-5628-387e-b7c6-2fee58f95e40 | -8.32913 | -46.17008 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6099b4d2-7fa5-327d-8626-2ce63b811a39 | -8.96056 | -47.19006 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e8c18886-2e28-3278-ae3e-bbe0946ad2f6 | -6.78496 | -41.00036 | 2025-10-27 03:42:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ed53f7f8-f783-34f3-9bdb-9ad57447faa2 | -6.88707 | -45.15833 | 2025-10-27 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac7c4102-1524-316d-baf4-756736c6354b | -7.92007 | -45.66073 | 2025-10-27 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README22.md)
