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
| e999a138-6cfe-3db4-9b73-2124ddd345ce | -7.89927 | -50.36354 | 2025-06-04 04:00:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f3c31673-66e0-3c9b-9464-e95c7867c39e | -10.60724 | -44.76518 | 2025-06-04 04:00:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 150f62d9-b92c-3ace-a08f-62a47fca734d | -7.22559 | -43.12588 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cb8cda17-60f8-37cc-b153-4446a68426df | -8.96899 | -47.96863 | 2025-06-04 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83cc2737-ea9d-3c4f-9996-3db59f017a20 | -11.62905 | -41.83549 | 2025-06-04 04:00:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e55f8969-a9d9-378e-a20f-1cdc61a92ce8 | -8.07273 | -43.11491 | 2025-06-04 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 869d24af-6d70-3f99-aa6a-61506fd838ff | -9.40037 | -48.41988 | 2025-06-04 04:00:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cec6b56-c332-379b-a82b-ab0ae00528d4 | -10.05014 | -49.66074 | 2025-06-04 04:00:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8a78570-4e69-31f0-8b86-79b42ca9dbd4 | -11.62961 | -41.83194 | 2025-06-04 04:00:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f6aef88d-10a8-3d24-8fb2-a7130b2ef913 | -6.86476 | -47.84447 | 2025-06-04 04:00:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37c052da-be7c-3915-9786-285cb8c59bed | -10.61098 | -44.76583 | 2025-06-04 04:00:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6fcd4fea-9632-3166-9ccd-08331d2b9aef | -6.8638 | -47.84991 | 2025-06-04 04:00:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef9bb210-2166-3ed6-90d8-b545e824e5dd | -8.89577 | -44.77775 | 2025-06-04 04:00:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73e73d09-dcf5-31a4-927f-03cac269d606 | -7.00968 | -44.59799 | 2025-06-04 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 37326413-f748-3a51-81a0-0bd8b2ec6d49 | -7.14612 | -44.03833 | 2025-06-04 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b952141d-0526-316f-b18a-a5bf336887d6 | -10.608 | -44.76062 | 2025-06-04 04:00:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05799c2b-7353-3df8-8210-e619ebd3cb49 | -6.68964 | -43.68405 | 2025-06-04 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82d5cabe-c46d-3992-92f4-ab781b3a40f6 | -6.21214 | -43.33504 | 2025-06-04 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6d448f67-6d6b-3d8c-b596-58d6f22f00e7 | -10.05262 | -44.64705 | 2025-06-04 04:00:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e8afd65-8635-32e5-a334-4f15cfa8f699 | -10.69502 | -37.0485 | 2025-06-04 04:00:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5b7b958e-2618-3e88-9f23-98e1916616a0 | -8.47255 | -46.48451 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c767ed9a-6b19-3d35-ab88-1ce136cda85f | -9.3139 | -49.49054 | 2025-06-04 04:00:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ed637dbc-b937-3573-a319-01769cc5c580 | -8.75593 | -49.76712 | 2025-06-04 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ed81458-e2dc-308f-bba2-c265c02d4c4f | -7.98144 | -47.23225 | 2025-06-04 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69ec9c54-2abf-3194-bb81-ad94c89fafb4 | -8.22494 | -45.70433 | 2025-06-04 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc721d22-4f2f-37f2-bf3c-01702f5fdf48 | -9.04381 | -47.02481 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a705e87d-53f1-3e9a-adcb-c79adbdca531 | -5.18297 | -48.07769 | 2025-06-04 04:00:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36a158a1-1709-398f-a456-4230c4d3af96 | -9.04305 | -47.02921 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fade3fc6-20ad-319d-903f-0f7e614847bf | -7.98311 | -47.22272 | 2025-06-04 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c4ff460-6bfa-3519-adfa-b828ff0fecb5 | -7.98512 | -47.23816 | 2025-06-04 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95a138b8-e326-3ccb-96f7-e800ca287344 | -7.55072 | -45.83593 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3ac7224-b246-3b48-8e33-644927d4c4e9 | -7.21842 | -43.12471 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 29983575-1eb4-3e37-b022-c40fca1364fa | -17.75179 | -42.89384 | 2025-06-04 04:02:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 019726af-57a6-3084-9fef-69333f6a7976 | -12.28195 | -50.10948 | 2025-06-04 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bb4308e-3fff-35c7-bff1-21e4af4c6b47 | -10.86989 | -49.55243 | 2025-06-04 04:02:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b55ca1f-d938-32ee-beb8-d4b675b96b81 | -14.01598 | -55.12342 | 2025-06-04 04:02:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7edc552-70d2-30d9-9cd8-8bf4885bde6b | -11.89421 | -54.79227 | 2025-06-04 04:02:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 388355cd-d250-38b7-992f-9b0e934303a8 | -17.00042 | -45.9257 | 2025-06-04 04:02:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ca3c2d7-9bf8-36e3-b7b9-f41a89bb5f40 | -11.90359 | -47.4471 | 2025-06-04 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33a7f0f5-dbef-3f84-9f83-7a3e5110ad9c | -14.71205 | -45.08815 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ea583b5-cd24-321c-bba3-b8d617a14fcc | -11.53415 | -47.31504 | 2025-06-04 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31999059-dd45-32ac-b8dd-4581b0da5a24 | -14.71565 | -45.08884 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76c87d56-c74e-3d64-9253-f9e6d98416ce | -14.81141 | -48.46319 | 2025-06-04 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0868201c-73a4-37a7-8971-662af220fe1a | -11.5349 | -47.31088 | 2025-06-04 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e213e172-7c2a-3cfc-8902-1fe255ed11ae | -11.80189 | -48.28037 | 2025-06-04 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8a2b1da-9425-31da-a18e-2a70614dc8bc | -11.83617 | -51.29209 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1453670f-875b-3e1f-bf19-8165c3736db5 | -17.77611 | -42.80515 | 2025-06-04 04:02:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a15c8db7-efb3-389a-b760-c4280fe46d28 | -16.02797 | -43.67827 | 2025-06-04 04:02:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e938ca7c-b545-3e37-a5bc-33e031341aea | -13.42935 | -47.53461 | 2025-06-04 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06e7136a-7d1d-3198-8806-07870996433b | -17.09515 | -43.80481 | 2025-06-04 04:02:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e12e5e4f-4ff0-3ab7-aee2-680e10bfa2e6 | -12.28916 | -50.10819 | 2025-06-04 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f7ec291-205b-3941-b2c6-6a83b02d072c | -11.91683 | -54.81992 | 2025-06-04 04:02:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d59c8de-58b4-324b-accd-7510e85e1469 | -11.90188 | -54.78876 | 2025-06-04 04:02:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d85e948b-f091-35c7-b2ac-bd058600febe | -11.80648 | -48.28123 | 2025-06-04 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3e60631-09f2-3b41-8908-1a0f354a6c09 | -14.72066 | -45.10323 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c68a0db-f9b6-385b-bb6a-177a505e7981 | -15.26838 | -51.47965 | 2025-06-04 04:02:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 182adacf-651f-3761-b526-b2631ff043e7 | -14.72177 | -45.10171 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 578efe62-268f-3ec4-90d9-30ed9349c459 | -14.71779 | -45.0982 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c911ae9-53b9-3208-9b1a-065a5f9c051d | -12.33283 | -45.7486 | 2025-06-04 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b8d6e97-ba07-3568-91e8-408a41a25ede | -10.49247 | -53.654 | 2025-06-04 04:02:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c6cc7ade-a797-37f0-a00f-c911f894afbf | -11.40059 | -52.94569 | 2025-06-04 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1abf7791-b742-3709-ad56-75768940f943 | -14.71419 | -45.09751 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4ab3e44-29a8-3e5a-92ea-9f2fca12f3c3 | -14.71706 | -45.10252 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed11e9c0-286f-3968-ad4c-f05ec511e512 | -15.26906 | -51.47618 | 2025-06-04 04:02:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28368f73-dfab-38a6-8d0b-d2939fc55ed1 | -14.71532 | -45.09601 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e104a653-923f-3306-9924-b8f5f589de53 | -19.83806 | -40.07983 | 2025-06-04 04:02:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1691d310-38a4-3958-a54a-5c3fa6583db2 | -11.83452 | -51.28861 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 234dea59-9d5b-38b9-b7de-fa29076512fc | -12.27858 | -50.09904 | 2025-06-04 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2152e5be-395c-3a12-a24d-0ab48f8e79cc | -12.27154 | -44.5904 | 2025-06-04 04:02:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7ddd4c0-9de1-35ee-a20d-5a3dd34c233e | -11.57714 | -47.45436 | 2025-06-04 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4160d7fa-732d-3084-a961-2f9166cb7e3e | -11.9033 | -47.45419 | 2025-06-04 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 050b7f18-6d8f-3b50-8b4f-d723abc095c9 | -11.83376 | -51.29247 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e56f08e1-c89c-369f-ac08-352628ade28c | -11.91822 | -54.8133 | 2025-06-04 04:02:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e74ac9a-396b-3ae5-a64d-306434eff25c | -14.72139 | -45.0989 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 21701473-56e3-3bd2-891e-5f32b40da5e4 | -11.83764 | -51.2844 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3b43cfe3-cf43-3fcb-9039-040425939055 | -14.02817 | -55.13244 | 2025-06-04 04:02:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64780d90-1752-3acd-9904-591f744273f8 | -14.71608 | -45.09169 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 17ac74cb-ca5e-3075-a88d-8df06065ccbe | -13.09199 | -52.02525 | 2025-06-04 04:02:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33be80ac-d539-38e2-835d-f137328d0e84 | -12.36976 | -54.166 | 2025-06-04 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 461b1069-0861-32a2-a633-800720c58557 | -16.67938 | -43.8827 | 2025-06-04 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3864d5e-3ff1-3f9d-8f92-29bb194b6458 | -15.07972 | -48.94563 | 2025-06-04 04:02:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f09d4235-98d3-353a-ad51-15477ef74d8b | -15.2715 | -51.48006 | 2025-06-04 04:02:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a6b84ac8-c861-3779-bf76-20b56d928b6e | -11.90409 | -47.44991 | 2025-06-04 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2b3d399-25f6-388b-82ee-4bb904139998 | -12.28342 | -50.11029 | 2025-06-04 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ac9e6f6-b956-3668-a30c-edaf5a8a7404 | -14.72212 | -45.09457 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aa9c51d-bac1-3ec1-b78c-aa9690787d95 | -13.09387 | -52.02107 | 2025-06-04 04:02:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66c65527-de12-3d9b-ba1b-1ec427483056 | -14.71852 | -45.09387 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b085617a-a668-3bf8-b228-fdfa53195df4 | -14.71382 | -45.10461 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7dc5c9c-b17c-363c-9531-cf77a624094a | -12.64963 | -54.11833 | 2025-06-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0898cf90-d243-3739-a598-f101860802fd | -11.82814 | -51.29149 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e21d1a8a-9a6f-3740-9587-9a78cbac5e7b | -10.49401 | -53.65964 | 2025-06-04 04:02:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f8b1d783-8c5d-3a1b-a67c-4dd0463c0c46 | -14.63262 | -47.73928 | 2025-06-04 04:02:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| defd934b-c949-312c-a738-c3ba678e28ee | -13.09279 | -52.02119 | 2025-06-04 04:02:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 022e54e7-df72-318a-89bc-162bf1e3cf1a | -11.84012 | -51.28966 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f3b0ab31-101e-3b52-b8fe-926d8647af17 | -11.84103 | -51.29706 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3342bab-c2be-3307-8437-b21437b77f65 | -16.30968 | -49.90986 | 2025-06-04 04:02:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0400ee6d-e92d-349f-9285-27e158ca7c21 | -11.89265 | -47.45827 | 2025-06-04 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 982f7010-bddc-3d2a-9e73-23eaf0a5e0c5 | -14.68361 | -52.68328 | 2025-06-04 04:02:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 316a79f8-90e3-3604-a0b8-da88ff971f6f | -11.83691 | -51.28823 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c447529a-3125-3c5b-98a1-e1885ee45566 | -15.26768 | -51.48318 | 2025-06-04 04:02:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README8.md)
