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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b3e52d2-8868-3dac-bf28-d5ea445fd56f | -10.19452 | -44.90337 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6e89aaaa-975a-3440-9282-33f8bb321b9b | -15.02827 | -42.33383 | 2025-09-30 03:28:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1a235b18-4078-3620-9b89-7f3c93c0e5d5 | -14.7465 | -45.6656 | 2025-09-30 03:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| bf56a428-01d0-3603-a95a-18699f6d9032 | -11.1546 | -54.126 | 2025-09-30 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 210.0 |
| bd66a245-1edc-3d2d-9074-5a315dcff0a8 | -4.9102 | -43.4666 | 2025-09-30 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 97f54ac7-ae99-35ae-8792-ee5b78837398 | -10.2041 | -44.8915 | 2025-09-30 03:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 07534a01-925d-3b34-8f83-69aaa8d0f824 | -14.5522 | -48.4684 | 2025-09-30 03:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4092b6f0-9bb4-3a39-95a8-7bb4f48effc5 | -14.5323 | -48.4938 | 2025-09-30 03:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 72c43957-4ae1-3fa4-81bb-6aa0faffd569 | -4.8915 | -43.4678 | 2025-09-30 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| b71686a2-3013-3637-83d4-6e3ce7cc8fcc | -11.2707 | -47.2236 | 2025-09-30 03:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| a3eab2c5-0c00-3c30-9619-f6dada9bd77a | -11.1735 | -54.1242 | 2025-09-30 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 83793537-0eb3-3652-a384-b568fc6260dd | -5.5241 | -43.8878 | 2025-09-30 03:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| bd17268b-833c-32b2-a09d-95af8fde81fe | -14.5137 | -48.4522 | 2025-09-30 03:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 3d3be974-954a-3101-bd15-01820eaaa3bb | -11.1548 | -54.1054 | 2025-09-30 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 53b7ccd8-bdf0-396e-930e-48f6e7d4f074 | -13.1966 | -50.9525 | 2025-09-30 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| bd096a14-f6ff-361c-99b9-3eec7fa5f89b | -11.2516 | -47.226 | 2025-09-30 03:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| c3827436-dbe3-3037-bde8-8558ca1dc6d2 | -11.7519 | -44.7461 | 2025-09-30 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 1a669fd6-0ecd-31e9-82e3-4653cc097f7c | -10.1851 | -44.8939 | 2025-09-30 03:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 213.3 |
| 4d9744fd-24fc-3695-a842-36ada81b9da4 | -5.5243 | -43.8647 | 2025-09-30 03:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 92b5c124-7615-3a39-a964-5c12d214f45c | -13.2158 | -50.95 | 2025-09-30 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 132.5 |
| c7918e0d-9cf8-3803-94f6-35aed6219a6c | -12.8429 | -47.0063 | 2025-09-30 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 183da057-3768-3b57-a164-d9c42d350418 | -10.1855 | -44.8709 | 2025-09-30 03:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| c5ce5cad-bd63-3add-889a-6540fac886d4 | -14.5327 | -48.4715 | 2025-09-30 03:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 97401031-ad3d-31aa-a795-3eabbf681ee9 | -10.1847 | -44.917 | 2025-09-30 03:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| e849b54a-62dc-387f-b1ff-219f42a874d4 | -14.5517 | -48.4907 | 2025-09-30 03:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| aa713ac0-507c-3852-a100-d6f68c653484 | -16.3926 | -47.04037 | 2025-09-30 03:30:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cac62bf0-7bd1-3af0-8726-3207d4109e8e | -15.85086 | -46.24393 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0589de5d-3408-3900-8482-9afe618c097c | -20.05449 | -41.33232 | 2025-09-30 03:30:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 62ddec43-7af8-3452-939d-9b41e915f63e | -15.3808 | -47.07993 | 2025-09-30 03:30:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73195024-9516-3126-94c2-bd9b432552b1 | -20.28812 | -46.23856 | 2025-09-30 03:30:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d3d5578-f745-32b2-b20c-a43db72ecf3b | -17.17205 | -42.83886 | 2025-09-30 03:30:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 27e58bdf-8aab-34ca-8c83-9ae1592ff890 | -15.86025 | -46.23374 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| afc06792-1958-3870-a3df-5c387a57bdf5 | -20.61411 | -46.19248 | 2025-09-30 03:30:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f46d5be2-6559-36b8-9e43-e902ed61531f | -15.68922 | -46.26078 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95b8962b-1249-3aa9-98d0-b2c576f28c37 | -19.85478 | -42.58625 | 2025-09-30 03:30:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f2944044-8415-3473-bc87-01810d317271 | -19.94155 | -41.64049 | 2025-09-30 03:30:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 087f8d8e-9e7e-3eea-b870-fa7e0af371da | -16.40648 | -47.0442 | 2025-09-30 03:30:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c476a760-aa4e-3995-9c55-6c15554c6b72 | -20.62211 | -46.18616 | 2025-09-30 03:30:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba76bb15-feb7-3a8b-b72d-6aadc2a1abfd | -15.85362 | -46.23351 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f73afde9-d734-372f-b872-21f9f8f745bf | -19.85549 | -43.81143 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 376c12b4-76c0-3b93-8d8b-d818b433988b | -19.7638 | -42.15479 | 2025-09-30 03:30:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2714afd9-ac3b-39c3-b9b8-c64a757956f1 | -19.59746 | -45.89341 | 2025-09-30 03:30:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c863740d-4320-33f9-a037-9ac0c8486075 | -19.97978 | -41.9109 | 2025-09-30 03:30:00 | NPP-375D | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 261be22e-16ba-3ed6-b4a1-f1c856a8d29a | -19.8499 | -43.81422 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| badbd8f7-1cd1-3da7-8266-b8a6bf42097c | -19.60177 | -45.88923 | 2025-09-30 03:30:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea0d9651-a036-3648-9f53-c3dfb13a6260 | -17.72517 | -46.63948 | 2025-09-30 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0a6bad13-e797-3721-a01a-7b74090a7aa7 | -19.60266 | -43.82208 | 2025-09-30 03:30:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20a2d8d8-7f1f-3af4-a170-aeea1a2d4c4e | -16.42656 | -47.02096 | 2025-09-30 03:30:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8477a7e3-175b-3bc8-b0ae-92d251bd86cb | -20.61637 | -46.1827 | 2025-09-30 03:30:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81c7b39d-613c-3aef-953a-1142526a2aed | -17.61423 | -40.67768 | 2025-09-30 03:30:00 | NPP-375D | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e7a2f387-dad7-3ec6-ae1a-f2a34c1ce94c | -16.42474 | -47.04802 | 2025-09-30 03:30:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8693c22-3298-3c50-8401-82b0d1e5e7f4 | -20.41721 | -43.35955 | 2025-09-30 03:30:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| b2e7dfe7-b1c8-3854-8e16-ffdc6d8a19d3 | -15.92375 | -46.20678 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cf7087bf-f0d3-3fff-a008-832262eaa8ef | -19.84825 | -43.81821 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| d7d22ac2-df1f-3109-b080-82bd025073eb | -19.55192 | -44.95452 | 2025-09-30 03:30:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78932d4f-ada4-3716-a91d-752a3a8469cf | -21.73576 | -44.61905 | 2025-09-30 03:30:00 | NPP-375D | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9c0afaa0-c215-3975-bf47-4c7096806aac | -19.8515 | -43.80676 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6dcb3a3a-d46c-346d-b981-a20510fdee5f | -15.62642 | -46.25443 | 2025-09-30 03:30:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b478f4b8-edb5-3569-a3af-23c27b220ce9 | -17.39082 | -47.16158 | 2025-09-30 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 433a7a6a-2014-35a9-97f4-dd4ad101c9ec | -20.0485 | -41.32957 | 2025-09-30 03:30:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 771193bc-e2f8-36c2-b0cb-37171ead82c1 | -17.71941 | -46.63997 | 2025-09-30 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 37afee61-f64b-3efb-a069-afb4a62493b3 | -17.40124 | -47.13769 | 2025-09-30 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4cb797f-2949-3348-a463-bc7fc62a740b | -20.04374 | -41.32905 | 2025-09-30 03:30:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 42c95120-8080-3f30-96a7-1bec2bef300b | -18.47515 | -44.0265 | 2025-09-30 03:30:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d8d5ce00-191a-3991-9e2b-ea7267852779 | -18.77017 | -39.7671 | 2025-09-30 03:30:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3bd78429-02d0-32d8-b847-c8b2235a8873 | -19.76342 | -42.15529 | 2025-09-30 03:30:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9ad31ccc-a10f-3d7b-a78a-7b4308d72fa8 | -15.8596 | -46.23851 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8926635f-6fdf-3173-b9f2-4a15c901e9f5 | -20.41946 | -43.34919 | 2025-09-30 03:30:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| c41246c0-f6d1-347a-840b-de220f3792fe | -15.38268 | -47.07177 | 2025-09-30 03:30:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c0e3822a-92df-3041-8d89-8823e46962a0 | -18.05724 | -43.65683 | 2025-09-30 03:30:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 843c3814-3077-369e-808a-db309364ba9b | -19.19257 | -40.87875 | 2025-09-30 03:30:00 | NPP-375D | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 020b6a2c-027d-3db7-86e8-f2c144d46e8c | -20.02302 | -41.43714 | 2025-09-30 03:30:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9095d51c-a19b-3fc7-a417-a541eff4c365 | -22.01722 | -42.21357 | 2025-09-30 03:30:00 | NPP-375D | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a2cb67ae-e4b8-3718-b1f6-0d1c2afcbb65 | -20.05794 | -41.33107 | 2025-09-30 03:30:00 | NPP-375D | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 57898d8e-f688-3a63-bb5a-7e81289e4118 | -16.40746 | -43.12185 | 2025-09-30 03:30:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81e47f57-0abf-32d9-8d95-7f2261b08cd8 | -20.04492 | -41.33146 | 2025-09-30 03:30:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| d391d5df-a634-3fd2-8de9-3066a5607198 | -20.74716 | -47.14951 | 2025-09-30 03:30:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2368c9e2-6ddb-3beb-bc29-b8c23412af4b | -18.05432 | -43.65739 | 2025-09-30 03:30:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b6c137a-c5e6-3787-b106-9d32a403ea51 | -15.62444 | -46.26224 | 2025-09-30 03:30:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 475a1bc7-bf6a-3e5b-9a3a-d0b783cbfdd1 | -20.61126 | -46.19199 | 2025-09-30 03:30:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6dd05b1a-9607-3222-acba-002b0cf74683 | -20.39141 | -43.68442 | 2025-09-30 03:30:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 76c00b27-e974-334a-a750-e9172a4e1473 | -17.39047 | -47.15237 | 2025-09-30 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21b613d9-2f31-3c22-9aa0-a9698c3886e0 | -20.61522 | -46.18768 | 2025-09-30 03:30:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b410c34-2521-3135-93e7-02e57c150bbb | -15.87873 | -46.21459 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4fcaa32e-d125-3eca-a6af-bb0c2b83df6f | -19.8546 | -43.81549 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| aab2913d-d7bd-342f-af57-6850122dd094 | -19.60465 | -45.89068 | 2025-09-30 03:30:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84696d33-4a64-3afe-8fd8-86bcde6b4136 | -19.59718 | -43.82076 | 2025-09-30 03:30:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5c41290-4102-36c3-993b-2860b521642f | -17.71242 | -46.66978 | 2025-09-30 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f2c3185-e07e-35b5-a6da-23c800517923 | -17.39526 | -47.1321 | 2025-09-30 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 001f2444-f22a-3d8b-8285-9704c9405956 | -20.42238 | -43.36116 | 2025-09-30 03:30:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| c6885e0d-e7b7-3353-bf4a-4cfbe3ded5e3 | -19.84995 | -43.81056 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 9dd3f7dd-c53e-3ac7-bbf9-4505d979f8b4 | -21.62286 | -44.06575 | 2025-09-30 03:30:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 75259c16-7695-33f5-8e09-c654998f745d | -21.89446 | -45.75793 | 2025-09-30 03:30:00 | NPP-375D | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 0374dc80-e6e2-32de-b3c1-c015279c9b3c | -18.12856 | -47.79255 | 2025-09-30 03:30:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07963a49-b1a2-3a9a-9ae8-2b9c0ea1d49c | -21.61753 | -44.06437 | 2025-09-30 03:30:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a6238a49-3ea5-34fc-ae4b-6d100f263528 | -19.94633 | -41.64147 | 2025-09-30 03:30:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| feafbd6a-3b53-32dd-8768-f8fb70e36b99 | -15.38805 | -47.08115 | 2025-09-30 03:30:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f102e2da-e7e4-3166-b8a6-ece683fba91b | -16.428 | -47.03415 | 2025-09-30 03:30:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5d13dd0-09ff-337d-8544-8a64ad6e3852 | -21.04525 | -45.68315 | 2025-09-30 03:30:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8cf5e809-a2f9-34af-ad48-30828359e5cf | -17.39963 | -47.14454 | 2025-09-30 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README20.md)
