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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8fad929-c140-3151-9769-ccfb43739390 | -13.88762 | -48.3565 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e33184ff-b083-332f-909b-45c07332e364 | -7.03273 | -46.6305 | 2025-10-24 04:19:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6309b80b-eb6d-351a-87c1-745f7d70d41b | -8.33084 | -46.245 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be31bf04-804f-3fbf-ac33-50ae75aee23e | -7.73462 | -47.01228 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9efd190-7332-3b04-a23c-a612e0415455 | -8.56458 | -44.86258 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f23e9ed-20e5-3dbc-9e19-0d5adf66e3d7 | -7.68811 | -42.24294 | 2025-10-24 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3ea0b79d-b6a4-330b-8cb1-4beea401e668 | -6.28135 | -47.01138 | 2025-10-24 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ac30913-4cd5-37c5-85e6-6e09512ba25b | -11.49106 | -54.02066 | 2025-10-24 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca793ca0-5af9-3d5d-9270-751d4ec5f13a | -6.81032 | -45.45371 | 2025-10-24 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5d5d3b3-04b9-3533-ab22-c0fb062efc23 | -14.42956 | -50.95837 | 2025-10-24 04:19:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f0ba420-b62d-3c48-a5b5-3408e50af3b5 | -7.29806 | -46.94135 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cffa94d5-f8a5-3a42-92de-eade98e30749 | -13.72665 | -48.37406 | 2025-10-24 04:19:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b75d7bcb-ef5b-3ac7-be34-71e6b3badcb3 | -19.96214 | -44.04594 | 2025-10-24 04:19:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 3afee60c-efdc-3cea-a797-eeb2e1ef5e3a | -17.6543 | -46.67094 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b68a471b-e186-3af6-a6ca-0583d247948b | -12.7268 | -46.95632 | 2025-10-24 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62a878bd-c98c-307c-951d-20f36e75a8f7 | -14.21 | -48.35058 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3fef387-e5b4-3830-ba12-a5190a349ae3 | -12.95167 | -48.50374 | 2025-10-24 04:19:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f35bd89d-ee26-396c-a643-ef9440a2da0d | -7.49237 | -47.02914 | 2025-10-24 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 06984b18-ce19-37af-b367-e5274aaf2465 | -14.77259 | -44.96832 | 2025-10-24 04:19:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e037c6f-ff9e-3b14-bdda-02c2b523eb0a | -16.37472 | -47.41376 | 2025-10-24 04:19:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e06d81e7-ae3a-32a0-ad65-8101dcbed9ee | -13.89638 | -48.39346 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccfe7051-0c9c-3dae-81ec-a136a2d003f7 | -5.62327 | -50.01104 | 2025-10-24 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a8ecd43-b774-3424-b8d4-a83fe6c86258 | -7.53631 | -38.55104 | 2025-10-24 04:19:00 | NPP-375D | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d386b052-57c3-3961-86aa-683f3b30ef94 | -13.0446 | -43.37861 | 2025-10-24 04:19:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25561c05-b158-3f5a-b450-cd073fc575f1 | -16.13051 | -54.00843 | 2025-10-24 04:19:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f65f38c4-69d5-34a3-bfc3-9766eb4ec0d9 | -7.46722 | -44.60865 | 2025-10-24 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59332215-4177-3541-8d8f-9099dab439e9 | -7.82528 | -45.37785 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3def35b5-7a9a-3293-a9f4-4a0b8750c5ae | -17.93383 | -52.69284 | 2025-10-24 04:19:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bc07eb7-77e8-3ecc-a3da-327583d28d95 | -7.0793 | -41.59404 | 2025-10-24 04:19:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| de3a804c-dada-327c-85ff-14fa5227af9b | -13.88605 | -48.38753 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 846907d6-4def-3423-a7b2-f43b2f9f3009 | -17.31448 | -43.60214 | 2025-10-24 04:19:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 523b8626-d569-3ae5-b50e-36aea1871607 | -20.3597 | -45.79863 | 2025-10-24 04:19:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa510d45-9c6e-39bd-8785-ff92ae4e5f13 | -8.34059 | -46.18505 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d020ae39-5ef1-3e9b-a474-6fc8cf8ba1a5 | -13.19811 | -47.75762 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24881d8b-24f4-3ce8-9a2b-85f0afcd5af9 | -14.03573 | -48.73081 | 2025-10-24 04:19:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dc1adf9-ac9a-391d-843f-efb2a2d16f44 | -16.82007 | -45.71021 | 2025-10-24 04:19:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6392c07-2345-3c2e-8b3a-115623bb1a40 | -18.34749 | -51.70773 | 2025-10-24 04:19:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94ffb6ae-c801-3abe-89de-8df189793647 | -12.77471 | -47.3837 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| af6962fb-d5cf-38a8-bff7-8aeb7d3c4fdf | -11.4815 | -54.01133 | 2025-10-24 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cba40c69-9197-3f03-80b0-c81fd11b3a91 | -15.1874 | -47.08792 | 2025-10-24 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49ae67d0-44d0-3d8d-bde2-6d29c49fa690 | -14.4395 | -50.95193 | 2025-10-24 04:19:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18c67dd8-fdf9-33c7-847b-6ec8edd81f8b | -13.91184 | -48.3695 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 060d5379-1562-3c04-89dd-d4452a662086 | -8.31786 | -46.7834 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01f7e863-4cd2-32e6-9d1c-839b925f1c44 | -13.33704 | -47.9492 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b26b6f2-3e4e-3f49-a957-2221eadf0673 | -13.35651 | -47.96626 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d880c70-cce6-3a26-861b-d623bea51682 | -15.49354 | -45.98661 | 2025-10-24 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b57d4fb8-88ab-335f-887f-6f031b0d39d5 | -20.48597 | -44.37173 | 2025-10-24 04:19:00 | NPP-375D | CRUCILÂNDIA | MINAS GERAIS | Brasil | 3120607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e19ed2f1-7523-3265-a26e-27ec75f994d0 | -12.83144 | -48.63931 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de2f66df-5024-3bac-96e7-a3c43ca07efa | -12.76899 | -47.37432 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e46b83e-cc74-353e-9e55-a15c6a2c01a4 | -14.92696 | -43.44598 | 2025-10-24 04:19:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 059fda6b-36c6-37cc-bafd-3f4f3901a96b | -19.93517 | -45.76874 | 2025-10-24 04:19:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b098450-5891-31ac-9dfd-e1be169ce384 | -8.32954 | -46.25299 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3be3b508-fc02-36c0-a2a0-d2cde04cffec | -13.36608 | -50.46672 | 2025-10-24 04:19:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9900b98-3eb2-3541-a7f8-d983cabfdb6e | -6.77693 | -45.48362 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| e83c5364-0af5-393a-90da-6afe3df2db62 | -15.35674 | -48.09605 | 2025-10-24 04:19:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7779fd6a-d309-3b6d-bdad-051acd1499c9 | -18.34825 | -51.70377 | 2025-10-24 04:19:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78b32c8b-c6c0-3866-a24d-cda0121cf599 | -6.9839 | -47.36252 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05ec398c-499e-3463-97dd-adb9085487f7 | -7.07252 | -41.66065 | 2025-10-24 04:19:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f246f069-151d-3da4-9c1b-d620790f1dfa | -19.32829 | -46.49041 | 2025-10-24 04:19:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 852711c5-6fa1-3025-b443-7c372a253662 | -14.44024 | -50.9479 | 2025-10-24 04:19:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61cc03de-719c-3f03-a683-aa274b32793a | -12.41779 | -54.36275 | 2025-10-24 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d4fc55b-d67e-3fcb-adfc-43329c899129 | -7.50207 | -48.01596 | 2025-10-24 04:19:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3a62c5a-df71-32f3-b633-ecc7cd46c2a5 | -6.99771 | -42.79393 | 2025-10-24 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 73348dce-530e-3a8a-8a60-38944461e48a | -8.64722 | -44.78744 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 857d5d54-4352-30a5-9a7a-5ff720ac9d22 | -18.91788 | -47.21873 | 2025-10-24 04:19:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 169a1da8-b13a-3ae7-97ed-cbfee563c47d | -6.27682 | -47.0153 | 2025-10-24 04:19:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61f73086-cae1-37c3-8f01-6cf6f2e62ed4 | -11.89215 | -51.52877 | 2025-10-24 04:19:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 221f2d82-4b77-3c37-806c-4da91a0c1d5e | -13.34784 | -47.97348 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 294e7275-de4a-30e5-af83-6c9b60e1a67d | -8.06666 | -47.12954 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1216e6de-bcd0-3471-980a-9a66ce1d81f3 | -7.77919 | -45.40114 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df8e0cbf-7db8-3cdb-bbcb-25b46db4fcf9 | -13.88462 | -48.37389 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c64cf996-a6fb-32d0-987d-baefb874d68a | -8.12008 | -47.04723 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e43b61d-9209-344a-bf14-55eeb9065794 | -6.92247 | -44.01689 | 2025-10-24 04:19:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4b0cea36-bf44-3d3f-96cd-861700b05600 | -8.32181 | -46.25584 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7b39c6ec-7dc7-3dd2-87af-04f863c0252c | -7.30104 | -46.94635 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15f883ca-0c6c-31ba-a6ac-8e2126b08f75 | -6.44 | -45.66573 | 2025-10-24 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 34a70de8-db14-3047-8fa7-e0a6cc524edc | -8.631 | -40.96491 | 2025-10-24 04:19:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2885f6f1-3aa9-3a07-86ce-14f11b3b38f6 | -14.46554 | -47.91181 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19208894-861c-39ae-ac14-7bfe8d283648 | -8.65 | -44.79158 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d75e9da-9324-3055-bb54-a4b7332a1187 | -13.77308 | -48.34673 | 2025-10-24 04:19:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 701311b9-4b10-34cf-86b3-c350b41ce683 | -8.20221 | -46.98545 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 41068fcd-5f71-32a7-a870-42e8f8a13b24 | -14.52114 | -47.95189 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0bdd6e8-c095-32b2-8282-e8bfd131a5e0 | -7.82184 | -45.37732 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 897d4686-b17b-30a9-9547-18239e7374dc | -6.69045 | -45.85685 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 101a186d-6cd2-371d-ab53-28af6b5d72d6 | -13.06982 | -48.20156 | 2025-10-24 04:19:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a7e3034-91ca-3fb3-9460-74e1db312a25 | -17.60279 | -46.62784 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b991c31-4dea-3d07-ae97-0693e9155284 | -7.23936 | -45.26195 | 2025-10-24 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72825f54-5fe6-39b7-b69b-acb35ebfb3df | -12.82096 | -47.23758 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19b28fcd-4418-3854-852f-1770fe651638 | -6.92303 | -44.01338 | 2025-10-24 04:19:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 16bf9e2d-19b1-35ad-9bf3-7921ac155c0c | -6.60047 | -48.77035 | 2025-10-24 04:19:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff71b9d3-3f8f-3a6c-96fb-fae484a0a5f1 | -16.64521 | -49.31296 | 2025-10-24 04:19:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10beedf0-4b8c-3e30-9b53-1ac760865d6d | -13.61698 | -47.05331 | 2025-10-24 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53cf7265-5dc9-3c1c-b1ae-c262597d9c8a | -14.20561 | -48.35423 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4aeb7cd6-663a-3a35-82f4-f22cf564e6c7 | -15.66589 | -48.84061 | 2025-10-24 04:19:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a11b7b45-0aba-39d1-9631-b8c1ddfc2eb1 | -12.67129 | -48.62708 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bddfcdd8-ddc7-386d-b5ef-e260e71def3b | -11.55352 | -54.51369 | 2025-10-24 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7086646d-d6c0-325a-b37f-9f734d15e7ce | -7.65964 | -47.41568 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba070f5a-6abd-3156-861e-8abf63f7b87f | -16.50243 | -51.47564 | 2025-10-24 04:19:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16c40419-1e5b-3995-97f8-7970c5e4f0d0 | -6.0807 | -49.37657 | 2025-10-24 04:19:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20d0eabc-0da0-3411-beb0-efb7b0bec210 | -6.43585 | -45.66906 | 2025-10-24 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README29.md)
