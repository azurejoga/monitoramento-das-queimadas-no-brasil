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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fccad3d6-5c86-3677-a2b5-04415513289c | -10.876 | -50.8163 | 2025-08-22 11:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 73147fee-b7b5-3f3d-beaa-6ff04d83678f | -10.8571 | -50.8183 | 2025-08-22 11:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 157.1 |
| da34a957-c371-36e2-9145-ca6447cbe9d5 | -14.5063 | -48.8307 | 2025-08-22 11:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 962b3458-eb89-37fb-a0a8-c4ea987ffed6 | -12.3129 | -50.0097 | 2025-08-22 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 6139cc72-68a0-3174-af66-9919602a8841 | -12.9921 | -45.2252 | 2025-08-22 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 227.9 |
| 4f87600f-1414-31f3-9a3c-60b7c0cef7ea | -14.4869 | -48.8337 | 2025-08-22 11:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 47a5f085-3a89-3a28-a6f8-79218b6aae6d | -12.9925 | -45.202 | 2025-08-22 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 169.6 |
| cf9bff23-b308-3d0e-9a65-f767bab5cbc4 | -6.52026 | -43.86763 | 2025-08-22 11:53:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 79435384-83cb-3f63-89dc-81661f77a934 | -6.12231 | -44.38405 | 2025-08-22 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| de40c57c-f61e-3abc-94f0-e72bca78f4b6 | -6.51844 | -45.53804 | 2025-08-22 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3a7904d2-87a6-38f6-8ef2-7117acb84a74 | -7.04017 | -44.62386 | 2025-08-22 11:53:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 451f6afe-6f75-3355-8e66-89ded286bf45 | -6.93962 | -44.2837 | 2025-08-22 11:53:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 28645512-7b86-3333-9e4c-1c59a8599712 | -6.44165 | -44.52969 | 2025-08-22 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 67121a14-d97e-30fa-ace0-fd68693f164e | -5.79481 | -45.07877 | 2025-08-22 11:53:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 148223f4-ae92-32d0-80aa-1f21c2a36177 | -7.03821 | -44.63661 | 2025-08-22 11:53:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d96dca8c-1a37-32bb-b2c0-0291a85f73f3 | -6.0385 | -42.8387 | 2025-08-22 11:53:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| ca8866a9-1d4f-3be7-8625-a0aedb84e766 | -7.54728 | -37.51697 | 2025-08-22 11:53:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 74309252-945f-301e-8a58-adf1d29c6ea1 | -6.15792 | -45.03856 | 2025-08-22 11:53:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2efaae41-8e84-3419-885e-b47972dff485 | -6.3204 | -43.76488 | 2025-08-22 11:53:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fc6bf5a3-2103-370a-9ca1-053c8208e14d | -6.42248 | -45.48662 | 2025-08-22 11:53:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| d01feb1f-7606-37c7-98dd-8d2b478b57f8 | -7.09616 | -43.71897 | 2025-08-22 11:53:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 20180db4-4e78-3538-8b9d-4158ecf5bbf1 | -6.42519 | -45.48026 | 2025-08-22 11:53:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 531d6b2f-310b-368b-a280-3ae7add99fe7 | -7.16757 | -44.67703 | 2025-08-22 11:53:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2ead72b2-f817-3dbc-b7df-882ba56d3892 | -4.7222 | -42.12189 | 2025-08-22 11:53:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 1a78f36d-33df-32ec-a02c-7ccb693e20de | -6.42289 | -45.49569 | 2025-08-22 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| f660295b-7e92-36d5-9e7c-ef9924f1cf78 | -7.0996 | -43.69621 | 2025-08-22 11:53:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 9d9e67d7-9784-3dd0-897a-e9df6934c30f | -3.23104 | -42.11992 | 2025-08-22 11:53:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 79cf0f61-c93d-3286-8c77-7a6bb3785dba | -3.22958 | -42.13013 | 2025-08-22 11:53:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c3412461-ebfc-3ccc-a5b5-97b5768bf545 | -7.09788 | -43.70758 | 2025-08-22 11:53:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 375.5 |
| 24c37f88-a9c6-35e6-ab4b-ca3a083b2376 | -7.27849 | -43.66656 | 2025-08-22 11:53:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b4f8b819-038d-3bdd-a974-feed26ccbc2b | -6.11568 | -44.39003 | 2025-08-22 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| b9a06735-3179-3544-8f32-bf65793ef254 | -6.7798 | -39.18795 | 2025-08-22 11:53:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 6d733959-4f97-3d9a-8bf8-abf974a1b688 | -6.73165 | -43.14064 | 2025-08-22 11:53:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a676ba6f-9655-3976-91ad-ae242617cbc6 | -6.04222 | -44.44584 | 2025-08-22 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 779cccdb-7f17-33b0-af00-d285c154b2a7 | -3.52367 | -39.31863 | 2025-08-22 11:53:00 | TERRA_M-M | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 8509dc7d-fa8d-310e-8d05-8bda0388ee93 | -7.14035 | -44.17511 | 2025-08-22 11:53:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d112d85f-f499-3418-99ef-a7376a2a39eb | -6.73323 | -43.13009 | 2025-08-22 11:53:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 8ef7cdd3-7083-3ca7-90ef-65a6df31980f | -5.80398 | -42.61797 | 2025-08-22 11:53:00 | TERRA_M-M | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 910b39ee-ae03-39c0-98be-6c8ac81749ea | -4.39992 | -44.08424 | 2025-08-22 11:53:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 5d20d5cf-9370-3b96-bb9a-02dd9582fa5c | -4.72638 | -43.60117 | 2025-08-22 11:53:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 576e72a5-c57b-30f8-a3e0-828f224949d7 | -4.49172 | -43.31901 | 2025-08-22 11:53:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e2688c9f-bbcb-3cdb-9846-7ee239001445 | -3.4313 | -43.35032 | 2025-08-22 11:53:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d58f063d-6b9e-30dc-84c7-c9b09d71a3ac | -6.42006 | -45.50203 | 2025-08-22 11:53:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| edb3c0c0-5536-3e21-b25d-757e2270ff99 | -6.52203 | -43.85589 | 2025-08-22 11:53:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 4115a24d-69fb-38a1-8902-ef9dbe0d62e5 | -5.63302 | -42.59141 | 2025-08-22 11:53:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 05ffb7b7-055e-376e-8ac5-d564bbd3a777 | -5.58001 | -45.20344 | 2025-08-22 11:53:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7b34a149-e419-3036-8fed-5a262db99ba0 | -3.70606 | -42.19382 | 2025-08-22 11:53:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 9729b72c-e6e7-3a83-a9c2-8507e0e4d02f | -6.3222 | -43.75317 | 2025-08-22 11:53:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 88e85239-cdb6-3338-bc29-8756b1d83850 | -6.44361 | -44.51666 | 2025-08-22 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c1065539-11f6-3063-afe7-fd78711f6e19 | -6.4521 | -45.52268 | 2025-08-22 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f831f1f9-2bb6-3f31-a68d-e7dfe7b9ab3f | -6.12034 | -44.39677 | 2025-08-22 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| a9b1747d-3668-39fc-9be1-2446f747d0c2 | -6.30045 | -43.89525 | 2025-08-22 11:53:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 1e4969ac-a09d-3094-ba5d-69a923caac6e | -5.63451 | -42.58126 | 2025-08-22 11:53:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 74e28524-b6e3-3a3f-82be-c6f8fce7cc13 | -7.05076 | -44.6255 | 2025-08-22 11:53:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| f5ad7e4f-2bb4-3734-a7ac-10e492b02cf9 | -6.02742 | -42.84775 | 2025-08-22 11:53:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 9c637c5c-9cf2-351f-b5e4-5b244b62a090 | -7.16958 | -44.66367 | 2025-08-22 11:53:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 69ee23f8-3951-3c65-946a-8b1f27bc14d6 | -7.61012 | -45.25747 | 2025-08-22 11:55:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d249f099-7580-31c1-8127-ad9a029cba46 | -8.79461 | -45.42009 | 2025-08-22 11:55:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ee664340-2b13-38bb-be1d-d0c06a36a46f | -7.65372 | -46.24364 | 2025-08-22 11:55:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 5d6f41ec-76d4-38a8-8c55-27cf56b7b749 | -7.86439 | -45.40233 | 2025-08-22 11:55:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9f9ffbc6-f239-31ad-ac37-15ea41a3d940 | -8.77963 | -46.69773 | 2025-08-22 11:55:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 0ff8aa02-a7f1-3015-8998-8015fb381e6a | -7.93934 | -42.65601 | 2025-08-22 11:55:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| de77bf7f-a3ee-3c9d-83c0-d9963e4204c1 | -8.86833 | -45.46625 | 2025-08-22 11:55:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2aa6dcb1-25ce-30c5-9054-cb10c763a107 | -7.63657 | -45.23181 | 2025-08-22 11:55:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 6935f955-2d53-324b-94ae-be3471b430ce | -8.82055 | -45.32387 | 2025-08-22 11:55:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5172663c-0968-30ee-a5ab-7416c50d557e | -11.3425 | -40.68858 | 2025-08-22 11:55:00 | TERRA_M-M | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| e462e5b2-eec6-36ce-8d7d-dd793192507f | -10.39511 | -42.58257 | 2025-08-22 11:55:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 90c0233b-c733-38f1-85af-27eaae681499 | -7.64757 | -45.23341 | 2025-08-22 11:55:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d5a7ec5d-8539-3141-963b-7084e1b57926 | -8.30517 | -47.28807 | 2025-08-22 11:55:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| e9f6a50e-a200-3e6a-8c19-bc154cbc6a9f | -9.63616 | -48.3295 | 2025-08-22 11:55:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 33d3699d-a13a-3808-a2d7-630b992903d7 | -7.25701 | -44.69573 | 2025-08-22 11:55:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5051c57e-e408-3288-b308-f35ed9ae999e | -7.86393 | -47.00607 | 2025-08-22 11:55:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 799142d6-c5e5-3823-9e6f-9e227d5ed4c6 | -7.64539 | -45.24786 | 2025-08-22 11:55:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 98f3403c-6313-3a0e-8cdd-4e8e852f3b8f | -7.65629 | -46.22709 | 2025-08-22 11:55:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 4d897590-0ce2-3225-91b7-79b08c34d6ba | -7.29605 | -44.54939 | 2025-08-22 11:55:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8ee77162-01d8-31a6-81d9-2a1817983ac7 | -9.34313 | -48.26338 | 2025-08-22 11:55:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| d575bee8-bf71-36c1-b05b-75c05430f7d5 | -11.42397 | -38.39555 | 2025-08-22 11:55:00 | TERRA_M-M | OLINDINA | BAHIA | Brasil | 2923100 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 1f02dc79-b4f4-32d3-9c1d-44afa26ec15f | -8.45549 | -48.24302 | 2025-08-22 11:55:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| fe9eadc1-f82b-3f42-82e6-7ee9b113660f | -10.57252 | -44.79008 | 2025-08-22 11:55:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f9fd968e-deff-3e64-aee4-773a74535dae | -7.63436 | -45.24634 | 2025-08-22 11:55:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 30.0 |
| bf1e6965-41ae-3c01-ab3b-2e19bf97aa69 | -7.94858 | -42.65742 | 2025-08-22 11:55:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| cac373c4-c8c3-35af-a585-12f194a13082 | -8.75299 | -45.47116 | 2025-08-22 11:55:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 11b7108f-b429-3972-80c7-cd5042b7ef4a | -7.4676 | -44.45104 | 2025-08-22 11:55:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 0d8ada1f-b87e-33e8-aaa1-8c718fd3d1a8 | -9.37218 | -40.80082 | 2025-08-22 11:55:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 192d08e4-1f8e-3f2c-970d-db5db7e881a0 | -7.85329 | -45.4007 | 2025-08-22 11:55:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3b2a2a46-d7a9-3445-8bff-421b9e90ee20 | -7.29949 | -44.55616 | 2025-08-22 11:55:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bd86e4c5-92a4-3f57-aa6e-6d31a79557c2 | -8.46138 | -48.25015 | 2025-08-22 11:55:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 10508f7b-09cc-39bc-9581-389f0378947e | -15.13852 | -48.10028 | 2025-08-22 11:57:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 6c210940-16ed-3213-94d7-5757678726bd | -17.40112 | -44.24593 | 2025-08-22 11:57:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a69f8eb3-813e-32c2-8aa7-92476a5010f0 | -12.99544 | -45.23278 | 2025-08-22 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 67671765-a87c-3124-b2a4-1ac852972b49 | -13.17811 | -43.78357 | 2025-08-22 11:57:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 295cd9b8-8e85-32a2-b4ec-5c68c61e9b11 | -17.6842 | -44.4467 | 2025-08-22 11:57:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0443ec39-d0c4-3525-85c7-41d399fee863 | -17.54872 | -42.7467 | 2025-08-22 11:57:00 | TERRA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4fb0a3ee-fff7-3a40-a98f-58fe7714ac0e | -14.77008 | -45.43032 | 2025-08-22 11:57:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 32fef5e3-edbc-37a5-986a-3b0b9fb066ee | -13.74555 | -44.70674 | 2025-08-22 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 973670ba-7656-36de-8d17-5e283e8f460a | -14.42777 | -42.19914 | 2025-08-22 11:57:00 | TERRA_M-M | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 636053cc-8655-3da7-a2ec-459d2d40dd4e | -11.80064 | -44.93555 | 2025-08-22 11:57:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 44.9 |
| a2ded754-1029-3c67-8488-9bd139f92aae | -17.79784 | -45.37604 | 2025-08-22 11:57:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a53f4d85-0151-3e93-af65-9e36439b3db6 | -12.57689 | -41.27512 | 2025-08-22 11:57:00 | TERRA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 2abe9d05-4f8c-38dd-a552-4eee788f3bb8 | -12.93052 | -46.17104 | 2025-08-22 11:57:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |


[Clique aqui para ver as próximas entradas](README65.md)
