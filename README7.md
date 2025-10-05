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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a4ce2b2-1548-3388-8d0f-1715ef54f3fd | -13.10769 | -47.83182 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dc924a44-531f-3012-bbaf-f3263f261586 | -13.11412 | -44.07281 | 2025-10-05 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| be484d44-dcf6-379b-8e49-146b66641ecf | -12.914 | -54.73738 | 2025-10-05 00:33:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| aaac7a27-cd9c-3ce0-997f-5c235b5f2ed3 | -10.34875 | -50.3815 | 2025-10-05 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b7c2b4d3-45de-35e7-bcdb-8cc43d3a1a52 | -11.55785 | -47.69717 | 2025-10-05 00:33:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3989afce-498f-392a-9752-cfe9c2fa9f27 | -11.5288 | -47.68309 | 2025-10-05 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3f0564c7-8048-31ab-983a-b53fdb26e5e5 | -15.98208 | -50.85656 | 2025-10-05 00:33:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e4f6f0c6-b0f7-31a2-a9c3-7ddb8069b9c8 | -13.26909 | -47.60273 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bbeb9c69-58c2-340a-8234-b20a35c56a53 | -11.51868 | -47.67537 | 2025-10-05 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 49913864-0794-38da-8807-9171859a018e | -13.12762 | -47.9757 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 77c266f5-48fe-3aaf-ba67-af66039b054f | -15.5494 | -46.83948 | 2025-10-05 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6c853c8c-e71f-323d-98b9-f8ddc2d02d6a | -15.29465 | -47.33087 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 43.0 |
| d2420ee1-570b-359e-aedb-091720d3ff54 | -12.30774 | -45.36636 | 2025-10-05 00:33:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0c59af28-e143-3152-825a-9de8bba430b0 | -16.33982 | -47.08955 | 2025-10-05 00:33:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2af7cfa0-b613-3328-b283-da3e99838247 | -13.64941 | -47.29988 | 2025-10-05 00:33:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5440d9e9-5976-324a-b7ec-14c16552e1d9 | -14.32336 | -47.7011 | 2025-10-05 00:33:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c6f14fa9-59d7-33fe-9210-8ed8f4587ecd | -8.85628 | -46.79299 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f6778281-797a-32ac-ba9e-d7fee68c9d8d | -16.34109 | -47.09868 | 2025-10-05 00:33:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a508391c-3e2f-36bc-b882-b3d35db66c36 | -13.52834 | -47.28723 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4893aefc-cb6f-3a99-85ed-4ae93048b3dd | -10.83441 | -47.9902 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 53bffc72-0756-3914-ae8e-08a5696e56f3 | -13.33961 | -47.5923 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0bc65d47-de05-3eb9-a4ad-ae958167cd94 | -11.07002 | -47.69845 | 2025-10-05 00:33:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4fc045d0-1ade-3c35-bc5d-e1167874018a | -15.3425 | -47.33625 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e4b98aec-655d-344f-80c2-f2056613bc11 | -11.12314 | -47.75502 | 2025-10-05 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9b02a19a-ab40-39f8-9187-ab4c6c7f1077 | -11.23149 | -47.80651 | 2025-10-05 00:33:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5585d1c6-34aa-3807-9b0b-2fd663f7231c | -10.94949 | -47.04916 | 2025-10-05 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 459c85e2-ad1e-3ff2-9dfe-9baab657ce52 | -12.69521 | -45.85189 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 0c9b5a76-403d-3c1e-ad0f-fa9c3b916e15 | -11.78704 | -47.55252 | 2025-10-05 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b8d86c36-c1e2-32d7-93a5-0badb2c9d7de | -8.38887 | -45.83739 | 2025-10-05 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5343ed46-e22e-3b1c-9b75-edbed48507cd | -15.3786 | -47.94092 | 2025-10-05 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fedada5a-0e59-31e1-bfc3-0c1ea7cac13b | -9.92809 | -50.89853 | 2025-10-05 00:33:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cd362f18-02d2-39db-94e7-7c287faaef2f | -15.9204 | -48.82648 | 2025-10-05 00:33:00 | TERRA_M-M | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f234db1a-b270-357e-9de4-a7ec8d0e5522 | -10.36809 | -51.23182 | 2025-10-05 00:33:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b96cade7-d53b-3e80-81de-37b901ad2968 | -13.21448 | -50.98768 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f8216a66-a69a-3e18-ae55-a867bd50dfc0 | -11.25792 | -47.78727 | 2025-10-05 00:33:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 96b0772a-1674-3769-b88b-b08e88b79cd2 | -9.35951 | -46.24609 | 2025-10-05 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3688f9a0-3fed-3b05-8820-4b2a832f554a | -15.91003 | -50.11233 | 2025-10-05 00:33:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 860606f8-526c-3853-aadc-d7007d832935 | -12.57916 | -48.15431 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b0c1d887-2a2a-3dec-a5d0-1135bcc81244 | -11.10858 | -49.86712 | 2025-10-05 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7fd282b8-8bc2-331d-a35b-cf9196c41267 | -11.82292 | -45.07822 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| bc3188ab-28ca-30e0-a7ac-de9e8e7a4a89 | -15.39879 | -47.95663 | 2025-10-05 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c7bc3236-d87b-307e-a400-c065076c3d72 | -11.80231 | -46.82122 | 2025-10-05 00:33:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 6a995dd4-6789-3ca3-8e19-dacef0139309 | -15.22944 | -49.29998 | 2025-10-05 00:33:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 53.2 |
| f70d4f1c-68bc-3a47-8943-965058a6c455 | -15.80843 | -46.27017 | 2025-10-05 00:33:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d1959bf8-c481-339d-b6b7-aa9b6b196ca5 | -9.11674 | -44.40678 | 2025-10-05 00:33:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| a9722db3-3515-3945-ba70-79668ad0c54b | -11.91256 | -46.24314 | 2025-10-05 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1adc002b-9325-3de7-bde3-33e6fa5d5aa6 | -9.41685 | -49.21366 | 2025-10-05 00:33:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| b6feac16-a22a-3611-80d2-5f8a2e921a9b | -13.7472 | -48.06883 | 2025-10-05 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9940d939-5e79-390b-bf5a-e1293a38e362 | -9.95266 | -43.77686 | 2025-10-05 00:33:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 8620d0e4-dd99-323c-9223-d490fafbeeb0 | -10.59963 | -54.35409 | 2025-10-05 00:33:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 2555d837-6df9-3f79-8ec4-731eeebdedb6 | -13.4351 | -47.27926 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 31fac1ac-a7e9-33cf-a74c-89cf551ccd11 | -8.74484 | -48.61288 | 2025-10-05 00:33:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 12.3 |
| cc68deb3-806d-3090-b5fb-36bd381fa1f3 | -12.2965 | -45.35704 | 2025-10-05 00:33:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 24af438d-f504-32da-8d30-92c610363553 | -10.49025 | -48.10152 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7be38f06-0a08-3066-a3fd-cf166f7b0437 | -13.49045 | -47.27453 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f260d1bd-9d05-33a2-a8a0-d6d9a95d02c2 | -13.30997 | -48.10854 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| f170db48-8ecb-32b7-8367-78b7e91a87e8 | -8.55815 | -46.27703 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 66a78cd1-58b4-38e4-b9b8-6eca2ac08fb6 | -10.59069 | -48.69605 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7754922b-06db-3dd0-9b1c-4a1bf469d5b9 | -13.3648 | -47.69298 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 83166634-61f4-300b-a6a4-58ccf46d8fe7 | -12.45922 | -44.74538 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 6c84cfe1-5eae-3dd5-970d-34c1f0adb6ac | -9.05323 | -47.01028 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 56532108-0ce4-3c7e-b95f-b8fca86369f9 | -11.3194 | -49.04364 | 2025-10-05 00:33:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 61d1844f-9685-3e9a-904c-b9a7c5190b09 | -14.33722 | -47.67134 | 2025-10-05 00:33:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 16251497-3587-32d7-a73b-9ea6d30cbbcf | -13.17051 | -50.87819 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2f081126-1af9-3af5-8012-3ce25fe10f1f | -13.31821 | -47.56779 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 34593cd1-1765-3d9a-9fa2-92b9abcd5fdc | -13.26854 | -43.60506 | 2025-10-05 00:33:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7e6a0539-8c44-3f43-981e-f3ec258a7833 | -12.55441 | -41.29705 | 2025-10-05 00:33:00 | TERRA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 21.8 |
| a743334b-4ab9-3d31-84a5-11e20d2580ee | -11.44886 | -49.72732 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 23442858-ef32-376d-a62a-d508b56c9227 | -13.69053 | -48.04948 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4769965a-93df-397c-8947-ab1b4db370e4 | -10.19907 | -45.52407 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 20b74d5f-c442-30b2-97be-b3638ce7e12f | -14.9182 | -46.87605 | 2025-10-05 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2200b896-702d-36b4-a4ec-89c3fbec53fe | -11.40153 | -55.17435 | 2025-10-05 00:33:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 368223b1-9224-34b7-91b1-7e686061a359 | -8.7949 | -40.58853 | 2025-10-05 00:33:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 2de75478-fdfc-346c-a9f4-2a7ffebd3852 | -10.68845 | -49.27842 | 2025-10-05 00:33:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0a62d9fc-5b56-3d8c-8c76-1ac2578a12f0 | -11.5179 | -46.76697 | 2025-10-05 00:33:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1f114b28-aca9-3235-a9dc-a6cc7f2c36f0 | -12.31116 | -55.1625 | 2025-10-05 00:33:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 3c87690a-74f2-3b55-9f16-b6570192f3e5 | -14.94092 | -46.84489 | 2025-10-05 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4489988b-58de-3f23-b486-dcb6acedd550 | -10.84955 | -47.96973 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 12d4a821-11e2-396f-bfab-eeef02acb8d4 | -10.84073 | -47.97106 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 674d92a5-6e76-3dc8-a00a-9f2e59e57b7c | -13.32703 | -47.56649 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f714470d-dbce-3024-b3c6-c0169a288279 | -10.20075 | -45.53521 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d50d3208-f9fc-373a-8d02-e10b6a12e7f3 | -15.20862 | -46.39137 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| eaa1ab45-5a88-3025-ba92-e4815bf143bf | -13.59458 | -48.16797 | 2025-10-05 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7fcf7775-5ae3-31fc-9458-369689c699fa | -10.84197 | -47.97995 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 74a4b2ee-c868-34aa-9e5d-3c868ab31b07 | -15.30012 | -46.32259 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3aa92e77-03de-3a48-837a-5be15ed38063 | -15.9899 | -50.91862 | 2025-10-05 00:33:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 4ad03103-17f6-3b43-9727-8c3fc02dfec4 | -14.42065 | -46.17347 | 2025-10-05 00:33:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 863d3eda-2824-31d8-ad79-214591cf9aa2 | -13.34847 | -47.57594 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9d3323b8-7665-3162-8a95-7fe5631640f7 | -8.85911 | -46.81266 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 0dee6c07-78da-34a4-8c9a-db61014231c9 | -11.91538 | -46.26253 | 2025-10-05 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| daf2726b-f0cc-38fb-a395-8183372a9190 | -10.19093 | -45.53643 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ceeb0aa0-9d0e-3bc1-abe0-c58c006c5447 | -13.92073 | -48.18804 | 2025-10-05 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 75c4cbd3-da7c-3cd3-8a06-058cc322b4d7 | -15.57077 | -48.20084 | 2025-10-05 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 52cc977b-30e3-38fc-820f-5c7655f41616 | -8.91048 | -46.59516 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a058bf13-c34f-3305-944b-6d15443e61e0 | -12.8219 | -46.85661 | 2025-10-05 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 6c43ac6b-8233-3577-99c4-218d9044240b | -11.51622 | -54.48419 | 2025-10-05 00:33:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 0a6056b0-6025-397e-a6ac-4ef8eb0fddcf | -14.59039 | -52.46753 | 2025-10-05 00:33:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| da4801e1-f7e6-3514-9fda-8fa2a644c77c | -14.64963 | -48.33088 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 2bd01a6c-545d-3419-b2b9-f8f52854e351 | -11.75992 | -44.72964 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| d37958b6-0f3d-392e-b62f-d73836fe1ada | -13.70488 | -47.35985 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 33.0 |


[Clique aqui para ver as próximas entradas](README8.md)
