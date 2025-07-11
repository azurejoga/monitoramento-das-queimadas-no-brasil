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
| b5d00bbd-49ab-3ead-a2b2-6ea4160bdc47 | -5.42257 | -43.18993 | 2025-07-11 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5c8bbd8-8d76-3dc6-ad7b-7ec27b02f6f4 | -6.28837 | -44.23283 | 2025-07-11 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81c8f726-9972-3113-85ca-4daa02eb5ddd | -4.23535 | -47.26157 | 2025-07-11 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcac25f9-9b38-379a-ae28-85d5ceabfc6a | -6.86977 | -42.78702 | 2025-07-11 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f5bd3c10-054e-3a29-a912-1dde3f438d44 | -6.72497 | -44.3334 | 2025-07-11 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| df811ae0-b8d4-3116-8f69-1f7cce9c23b5 | -7.20563 | -43.11337 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a2853ef0-f658-3b91-8f0e-51f186c88232 | -6.27277 | -42.37504 | 2025-07-11 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3d95811f-05f4-3872-a06e-a82be3af6526 | -7.19721 | -43.12299 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a941ebb3-1eff-3441-9092-4dc3284df9b8 | -6.87346 | -45.23205 | 2025-07-11 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 683917f2-44d3-3260-89ae-a9faf1879f79 | -6.51833 | -43.33283 | 2025-07-11 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4545cfa9-d621-3c47-95be-2998d64e4b87 | -7.19164 | -43.11477 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5e8998c1-14c4-3bea-b13b-e4578005cc62 | -6.98756 | -44.45553 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0109456f-6e84-36b6-a384-8f5df3d47d5a | -6.50527 | -43.34943 | 2025-07-11 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e12f17b-6b26-37d9-9665-60919903370f | -3.74783 | -47.10625 | 2025-07-11 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d9901d4-e68f-33c3-ba81-b985b47965f8 | -2.44414 | -47.46555 | 2025-07-11 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f078a685-3e86-31f6-b279-cf22a3fafa56 | -6.07873 | -44.86897 | 2025-07-11 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83eb564f-6392-364c-aaa0-968ee7269c42 | -6.72433 | -44.33733 | 2025-07-11 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1066a1a5-e55a-3a22-ab14-1fcfa44e3d62 | -6.14734 | -45.90664 | 2025-07-11 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 945d880e-0209-30fd-9bde-8a472cf13557 | -6.88483 | -44.0644 | 2025-07-11 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfd5a4c4-5cd2-3513-8d76-7a207beea5c4 | -6.98746 | -44.45895 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4df9867e-3fd5-36ab-822b-86e2a8c45150 | -7.19329 | -43.12603 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 55ea2a2a-34fc-3faf-bced-3d2a2e8aeed9 | -7.72193 | -41.35135 | 2025-07-11 04:06:00 | NOAA-20 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ddc8354b-51c4-353f-9e2b-f96b3d255472 | -6.7793 | -42.9943 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c9cdadc4-708f-3d36-8b1f-b1d1016365f9 | -6.98811 | -44.45501 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e4d6cfe-3557-36df-80cb-00569923d928 | -6.87787 | -45.2282 | 2025-07-11 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b6e5e42-6283-33ed-b2d4-c1aaf11f4543 | -6.8514 | -42.79494 | 2025-07-11 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9eae286d-d534-3fc0-8b4d-f03d7558734f | -5.20394 | -37.66559 | 2025-07-11 04:06:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab2164ca-d5fd-3c73-9e4d-40c8f0ad433c | -3.22291 | -42.13053 | 2025-07-11 04:06:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60847329-fe32-390f-935c-06ff8802907c | -7.18829 | -43.11422 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0ad79209-8756-377a-97c3-f2b929f3b626 | -7.20114 | -43.11996 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 92b2f4d5-0c77-3557-98b3-93686a96e23d | -6.70457 | -44.32605 | 2025-07-11 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 758262f4-a754-3974-bf86-77c29e1eb15b | -6.44493 | -43.81116 | 2025-07-11 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bcda439b-bc00-3227-a492-1f687762e0ea | -6.99645 | -44.44829 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3dde284e-333f-3a79-b5f7-076ebf9c1b37 | -6.61562 | -43.01573 | 2025-07-11 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92f0e502-332a-328d-b3b3-dc8e2a2310ce | -6.85084 | -42.79845 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bbcd6fb3-fabe-3788-8e5b-ed4e5be000b6 | -4.54583 | -48.01244 | 2025-07-11 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3b7eca9d-4330-31cf-9d1e-a907785bb0f5 | -5.6206 | -46.24282 | 2025-07-11 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a258822-06c2-384c-806b-7ed5a0494863 | -6.7083 | -43.87714 | 2025-07-11 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df6fd6cb-2fac-3943-8f63-87c68e9168a9 | -6.27996 | -42.37261 | 2025-07-11 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 33c5e22a-3bed-38be-942f-0c04586e702e | -7.04856 | -43.28731 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cb62647f-d917-3fcb-b0b6-d8e3bd70d38c | -6.64976 | -43.19068 | 2025-07-11 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f53e30e4-7adf-3feb-8e0e-41fe993e73e6 | -6.08305 | -44.86535 | 2025-07-11 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ba3fe5b-1473-394f-a051-33fcba776e10 | -4.55111 | -48.00861 | 2025-07-11 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59504738-76ee-3ae9-b2a6-9e75e82ef756 | -7.36069 | -43.39655 | 2025-07-11 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a89fb01c-afdd-3e42-a50e-eb6151ff96b0 | -6.73605 | -44.62262 | 2025-07-11 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| accf1fa3-23c4-312d-a94c-7f84c0889059 | -7.11035 | -40.38791 | 2025-07-11 04:06:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 853fb655-3bb1-34a6-8900-d68a0201a187 | -7.18897 | -43.358 | 2025-07-11 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cfa9d0ee-7db4-3132-af80-0ab480263597 | -5.91098 | -45.57613 | 2025-07-11 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55ce7ef0-fabc-34ba-bf70-38ca5fba0173 | -7.1109 | -40.3843 | 2025-07-11 04:06:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d9691908-c6c8-3943-a4cb-7fd332e1506e | -5.91436 | -37.39345 | 2025-07-11 04:06:00 | NOAA-20 | AUGUSTO SEVERO | RIO GRANDE DO NORTE | Brasil | 2401305 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fb77f9b6-de34-3fee-ba04-95c4fd4f9895 | -7.31907 | -38.13568 | 2025-07-11 04:06:00 | NOAA-20 | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a0a3e26d-9958-3e7b-9d0b-e6c9a3ecb67a | -6.9576 | -42.72515 | 2025-07-11 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f632113c-45d8-36a0-9a40-2d85c6459741 | -3.75079 | -47.11507 | 2025-07-11 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d965694e-7487-3bc5-8043-77c75aa3d03a | -5.41917 | -43.18938 | 2025-07-11 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de0a85bd-4d1e-3cf1-a91d-cb316b6c0226 | -6.68715 | -43.92027 | 2025-07-11 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3590923d-905a-3db8-a59c-d5a8ca58bba9 | -7.1065 | -44.36995 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66915e5c-b191-3b86-ad2f-7aef41ad7130 | -7.00804 | -44.04044 | 2025-07-11 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f61a240a-935e-3b6b-a268-ae932dbde8d8 | -6.27719 | -42.36863 | 2025-07-11 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 12ef3ae6-0c12-358d-8ee9-37151240412f | -8.07424 | -34.97635 | 2025-07-11 04:06:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cfc3e3de-c360-3193-bfff-29bdc005e982 | -3.74647 | -47.11441 | 2025-07-11 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb1927fc-00f8-3ebc-88ed-772627a26dfe | -6.10941 | -44.81808 | 2025-07-11 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72202e1d-a37d-3e8b-b13f-3b814010b633 | -5.5566 | -43.8895 | 2025-07-11 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89e74f4b-37b9-34e4-acff-1349cb980a63 | -6.51145 | -43.35429 | 2025-07-11 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c924781a-04a1-3cb3-b54e-098e57baf9db | -6.99164 | -44.45555 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8722ba3d-5b26-35a7-b427-1029749237b4 | -7.19234 | -43.35854 | 2025-07-11 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 444b5da3-1173-3df0-8cbd-a5dd8d05937e | -7.19279 | -43.3772 | 2025-07-11 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f26af1e2-3872-3909-be68-ce8cfe2ac6d5 | -6.67603 | -46.3068 | 2025-07-11 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 339b6a5f-202d-350a-8b0f-45641b112058 | -3.75147 | -47.11097 | 2025-07-11 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1a497649-b5ba-3997-b7f1-da9b1cca4d68 | -5.75052 | -40.44864 | 2025-07-11 04:06:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 19ea3ace-419f-37f8-a726-1b36ee0a1cbe | -6.86089 | -42.77839 | 2025-07-11 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 619f08f2-ab2b-3fa9-95a0-c8d4fef4911b | -6.73342 | -43.89682 | 2025-07-11 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e26ab6cb-041f-3aea-a87d-4576c197a797 | -2.4434 | -47.47013 | 2025-07-11 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3114b035-3642-32e2-9ded-0d808c1d2f1e | -6.15715 | -47.27581 | 2025-07-11 04:06:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ffd0391d-1ca3-3238-9c0e-03eca57a2fe4 | -6.12347 | -45.9077 | 2025-07-11 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c1f7cf1-fb08-3406-bdb1-8b9662042af9 | -5.5525 | -43.89279 | 2025-07-11 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fd3211f-f9ec-319a-9bfa-9a9f509fb63f | -5.54306 | -43.90717 | 2025-07-11 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4332e509-a38d-3ee1-bab7-36dfa238c448 | -7.20506 | -43.11694 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 13cfd61c-2b1c-3390-bdc3-a7540f0c292c | -6.36617 | -43.64854 | 2025-07-11 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a6a5229-6b51-33f9-8e53-bb987d13fc2f | -6.23518 | -45.44527 | 2025-07-11 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65976a72-72a2-39e6-a522-2e13c73bf3e1 | -3.58163 | -49.43604 | 2025-07-11 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 242e999a-aeb3-307f-8901-4a99b5201219 | -5.61721 | -46.2452 | 2025-07-11 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec52fa03-3dad-3715-914b-83046b7344df | -6.1578 | -47.27193 | 2025-07-11 04:06:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2896258a-357d-33ff-a70a-da0a718f388c | -3.78566 | -47.09156 | 2025-07-11 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6267970-cc5c-3a06-a8e6-e73a8c5cbe0d | -4.78449 | -45.34747 | 2025-07-11 04:06:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 285b995e-b847-3244-9ece-981709bc4c74 | -5.42562 | -43.25832 | 2025-07-11 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2c6911b-e0ff-3587-bf86-2bd651160018 | -7.04913 | -43.28369 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 072f9b3e-a8d9-39ee-b56f-6cd7637594c1 | -6.50806 | -43.35371 | 2025-07-11 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5e4201a-c9c0-3ab9-8803-5361e4cb7902 | -2.99145 | -47.45258 | 2025-07-11 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae860474-3a93-390a-82f9-146501d8fe32 | -5.55475 | -43.9011 | 2025-07-11 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a8973c11-b75f-37e8-8de8-878de3cf0552 | -6.08236 | -44.86954 | 2025-07-11 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5269b121-d4e9-375b-90ce-6199d94228fc | -5.42281 | -43.25407 | 2025-07-11 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 053489aa-131d-34f7-83b6-c879c9251924 | -6.07942 | -44.86478 | 2025-07-11 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 997d18f5-bfa7-33fe-b558-29cb071c98a5 | -7.0865 | -44.38251 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95bcc372-31a3-39c1-91f0-b4005ed68719 | -3.66205 | -48.31885 | 2025-07-11 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 687f31e3-8bc3-345f-b116-087c13e57b67 | -6.27332 | -42.37158 | 2025-07-11 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 285139b3-e216-3c3e-b2ea-5391c9c98b92 | -7.36011 | -43.40018 | 2025-07-11 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cae1842-6e4b-3a56-aa38-043e7d3d9627 | -4.31122 | -47.7593 | 2025-07-11 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d41e47a-1437-3dcc-9cdc-408a750c8249 | -6.44214 | -43.81098 | 2025-07-11 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d67fcd3c-806e-3bc7-8069-1a871706dde1 | -3.75216 | -47.10688 | 2025-07-11 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d8a0c687-6aa7-3624-add2-aca54f0423a8 | -5.4194 | -43.25351 | 2025-07-11 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README11.md)
