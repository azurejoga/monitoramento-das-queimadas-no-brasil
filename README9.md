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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54423c57-0cfd-3d4d-a43c-7c7220169a09 | -7.13981 | -44.24622 | 2025-10-21 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5986619d-1b44-30f2-bb2b-9f6dfcbec675 | -6.65038 | -43.43774 | 2025-10-21 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0fac2a6-3ecf-3652-a1f2-7c601f28dd4b | -5.4348 | -41.0783 | 2025-10-21 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1bc3f989-280f-3d4d-baa1-0b06bd157fca | -4.56544 | -49.65643 | 2025-10-21 03:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8b308896-b141-35b8-92f4-0153e79a02e3 | -8.11846 | -41.1833 | 2025-10-21 03:53:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d505a398-c5e1-3d38-9c2b-7b219cafe361 | -5.43375 | -41.07523 | 2025-10-21 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 17806fdd-fd72-341b-b7ff-a93b6bbb9798 | -6.90042 | -43.58858 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cf7613b-62e5-350b-9dd8-914d1109bdf1 | -5.26318 | -50.23991 | 2025-10-21 03:53:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33fa2754-36c9-30c7-a6e5-f5e8c0dd204f | -8.0643 | -41.05289 | 2025-10-21 03:53:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0a433d75-1dc8-38a6-97d9-8f63d9956798 | -4.46779 | -49.10273 | 2025-10-21 03:53:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f15d0bd1-2d7a-31c9-b872-2494a92d1aab | -6.64753 | -43.42972 | 2025-10-21 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20212085-173b-3167-9c49-b5ee780b65b6 | -8.78251 | -44.21022 | 2025-10-21 03:53:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c443c36-cc29-3224-bed4-7ad12fb637cd | -8.26576 | -35.48112 | 2025-10-21 03:53:00 | NOAA-20 | CHÃ GRANDE | PERNAMBUCO | Brasil | 2604502 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c676c634-7752-329a-a96e-166d6a22ca6b | -7.11009 | -45.35422 | 2025-10-21 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3152015-72f9-3fc4-8b25-7199b0924ecc | -4.81638 | -43.54008 | 2025-10-21 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a5c9bbe2-80da-3d68-9274-e301000876ab | -7.20694 | -45.31273 | 2025-10-21 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0953850e-2290-3b20-a725-2933448dffc3 | -8.78187 | -44.21394 | 2025-10-21 03:53:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fd60f7f-fc49-3aee-a2db-6a7b63c8a503 | -4.47393 | -49.10379 | 2025-10-21 03:53:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d26fc089-f788-3429-8e6b-2cc33c1eb960 | -5.26401 | -50.23736 | 2025-10-21 03:53:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dad47aab-4ff0-3bb2-abb0-93121e91c9b4 | -6.39928 | -44.29483 | 2025-10-21 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4faeb127-df6c-3ae0-b6eb-65596286e6df | -6.8954 | -43.61809 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1873390-8a7d-3633-a415-c1ef028a9059 | -4.48408 | -46.47339 | 2025-10-21 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98a912a4-a087-3037-8341-e460e3cfa882 | -6.64761 | -43.60719 | 2025-10-21 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 311d797f-af67-3942-9c98-367acae7b268 | -6.64631 | -43.60698 | 2025-10-21 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 79a9b602-62c6-342d-984d-601f2c1750e9 | -7.61355 | -43.37182 | 2025-10-21 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 561f8ea6-2a47-3fba-bd06-8062fcef2cc0 | -4.81658 | -43.5391 | 2025-10-21 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2c196d7-ac0c-3da8-80cb-70716dcf19a9 | -4.24944 | -50.01002 | 2025-10-21 03:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f62f901e-d419-311d-8d77-25a2678e09c2 | -6.65159 | -43.43041 | 2025-10-21 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc2ba332-2a1b-3e59-bece-176ab8497ea7 | -8.44301 | -36.26274 | 2025-10-21 03:53:00 | NOAA-20 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 211791d8-4c0b-3113-8d83-d902a560fbba | -4.49447 | -46.47499 | 2025-10-21 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09905c75-f611-339f-bed5-55379c2e0878 | -6.89509 | -43.59517 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4921ba5-eba4-326e-8617-308b77b39382 | -8.20644 | -35.89264 | 2025-10-21 03:53:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7468d34c-eccf-3229-9caf-e715e0211a72 | -4.13896 | -47.66134 | 2025-10-21 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdf8c3b3-52dd-3d9d-93c7-9f4d7efc109b | -5.27053 | -50.23843 | 2025-10-21 03:53:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 163defeb-8936-3e3a-9827-728578cb191b | -6.69698 | -43.40936 | 2025-10-21 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2bbd8a7-be77-3304-804b-df8619893f42 | -6.57952 | -47.54361 | 2025-10-21 03:53:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e603aa8d-2d28-323a-ba85-61b3bbc55812 | -6.92496 | -43.59274 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c7829aa-3c60-3972-bc94-7f82400a1a5a | -8.11707 | -36.00758 | 2025-10-21 03:53:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| dadd3103-49a6-3a8d-9fca-ea188f5d4e58 | -5.83201 | -40.82595 | 2025-10-21 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 88acd064-872d-3c5e-a8ea-f26bcd0a2a62 | -5.427 | -40.88873 | 2025-10-21 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a1518199-4a41-348a-bcb1-27c64f39d27a | -6.89476 | -43.62184 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51f00532-35d8-3434-9d87-f4cd42526edb | -6.88217 | -43.59685 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cb5b723-b1c6-3069-93fb-2cd2027bfc07 | -6.69759 | -43.4058 | 2025-10-21 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 945be8cb-dd93-3a94-96f2-ffca72f7e161 | -8.2963 | -49.30868 | 2025-10-21 03:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c20ebd4-8a50-3402-8591-8a3d6e9cf2ac | -5.43549 | -41.07413 | 2025-10-21 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 75d7dd95-5e0d-38d8-a624-887f6ff73f12 | -6.98157 | -48.68418 | 2025-10-21 03:53:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f64edcfe-b32f-3086-b3b3-bbb6cec4fc4c | -4.48875 | -46.47731 | 2025-10-21 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43860a2c-d49c-338e-a2dc-20f0a2cdbeb8 | -5.84904 | -40.83286 | 2025-10-21 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 27549bf8-dc32-31d7-b376-d53ea7a4a544 | -7.14473 | -44.24306 | 2025-10-21 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad92b397-2ff5-3ada-a428-c158d824f537 | -6.98231 | -48.68009 | 2025-10-21 03:53:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 095aefc6-c21b-3120-a5dd-14e0894f9a75 | -5.58175 | -41.32137 | 2025-10-21 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 57d40e56-882e-37b6-8d89-772d2dac3f65 | -8.14612 | -49.4713 | 2025-10-21 03:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ada322bc-0f13-3cf6-9a4d-2d1e051d7e26 | -5.66224 | -49.80009 | 2025-10-21 03:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bca093e7-d250-3ec6-a99e-8e7fedcf181c | -5.42505 | -40.90079 | 2025-10-21 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a9cf6a6-0867-3642-85f4-89f982159111 | -6.89949 | -43.61882 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad6a6047-2a99-38fa-b65d-31e063bba330 | -6.90389 | -43.59293 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e9c0a0e-8a4a-3919-bb8c-1cbca8c1de80 | -4.48926 | -46.47428 | 2025-10-21 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 029aa739-3662-31ae-b3a7-3216e7b1a539 | -6.88658 | -43.62036 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d92eedf1-b936-355c-afe8-12912a903566 | -5.66857 | -49.80104 | 2025-10-21 03:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f381fab-edab-3698-b072-6ab17cb30c24 | -5.66492 | -49.80207 | 2025-10-21 03:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a585f78e-b48e-3bad-844f-5c2d10816bd1 | -8.84773 | -49.71545 | 2025-10-21 03:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbc9a932-d90f-3047-a6f7-37becc8331ca | -5.66945 | -49.7961 | 2025-10-21 03:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5458b57-2d14-3ca5-881c-092a31ccdc55 | -5.83555 | -40.82651 | 2025-10-21 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 990d60c7-7220-3929-99d0-edd4a6a15381 | -8.84856 | -49.71107 | 2025-10-21 03:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57b65aba-e4b3-3068-be7f-20345993bd54 | -6.92557 | -43.58911 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fabdc65-e2c8-3d9d-83fc-58bf13b6fbf4 | -6.88594 | -43.62412 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| beb4b2cd-7c79-3aae-b186-cf9ca80ace65 | -8.29551 | -49.31293 | 2025-10-21 03:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 983a22a4-fc29-3968-9094-93993a5b54ea | -8.26748 | -35.48004 | 2025-10-21 03:53:00 | NOAA-20 | CHÃ GRANDE | PERNAMBUCO | Brasil | 2604502 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 046ca0ca-0502-3ad7-ad2e-d889f81ba907 | -10.95756 | -50.31636 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4580fee4-bd7f-35f6-8cb7-57cfaef850b5 | -10.92266 | -50.32317 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd75de34-252d-35fc-a38b-d57563438b11 | -10.94212 | -50.3317 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5800127e-1278-33f7-9c48-22d57348462a | -10.94302 | -50.32723 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e2df72a-39e9-3441-ad8b-328b816ec9d5 | -10.94033 | -50.34066 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0872844-dc61-33d4-b734-558295c1f2fc | -10.94628 | -50.34187 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d01fc736-240d-3ae8-b7c2-2e5ccbe0c308 | -10.94298 | -50.34612 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c16b46d-6cab-309e-a987-da412ee0c5a5 | -10.92019 | -50.30407 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81f83004-8007-30f5-a521-98a7593b9e14 | -10.95667 | -50.3208 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cf648ed-764e-3bf9-a7d4-2d94ba80ac45 | -10.93023 | -50.32923 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f277122d-622d-38a9-ad4a-95516c3b1d43 | -10.93528 | -50.33495 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 021f8526-7813-3bfd-8cda-2178e1c3d7aa | -10.96088 | -50.31728 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c10c550-a3b7-32a2-9699-45a1579f5575 | -10.94122 | -50.33618 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01e24eb2-1c92-3c57-8b67-a08d3ffb8277 | -10.96003 | -50.32174 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbac53a2-cb52-33be-a0f3-b9c98a219809 | -16.79985 | -51.35618 | 2025-10-21 03:55:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b86a0777-18c6-34a2-9b28-661896a4fce4 | -10.93195 | -50.33911 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0f605d3-2a5b-33d7-a7e1-de804f8d0fa5 | -10.94471 | -50.3371 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2ada63c-dff9-3d9b-aa6a-bdcc9c4464a9 | -10.93438 | -50.33943 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d950dc6b-5e19-39f9-8a7b-31d4347c0355 | -10.93281 | -50.33462 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f6fd319-2593-3366-aa71-46b52f12b770 | -10.92933 | -50.3337 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 075580f9-4e45-3983-9e4f-8b097223276b | -10.94384 | -50.3416 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 650293cd-1dd5-3168-93ed-6519986ef8a4 | -10.92105 | -50.29963 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cb788ba-f43d-3a84-9ca9-57bb16499837 | -16.80071 | -51.3522 | 2025-10-21 03:55:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29de8e24-74c4-382c-8d30-bffc0f776035 | -10.92439 | -50.31423 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f38b65a3-21aa-3c2b-9993-4a4fd27a6e7d | -10.93702 | -50.34488 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 402479a0-bc28-3496-85ae-62e3d7a61fb0 | -10.92353 | -50.3187 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| befc0866-9686-341a-b8fc-c3879b95d63d | -10.94558 | -50.33261 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5240963-863c-3576-b6dd-f1d1cbc0f4ed | -10.93876 | -50.33587 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65edbcb3-3b26-369f-82e4-428e30238b05 | -10.93942 | -50.34517 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| feb805c5-1aff-3e5b-9cd3-b93662e180cc | -10.93789 | -50.34038 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe12da65-0e8c-3dee-ac25-67754367b7fb | -10.92526 | -50.30978 | 2025-10-21 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 354d3910-1b24-3884-937b-5586d67c0885 | -17.42846 | -55.05139 | 2025-10-21 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |


[Clique aqui para ver as próximas entradas](README10.md)
