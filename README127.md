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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5107a0d5-2a38-3947-a4cd-4edc33b68e4e | -13.8979 | -48.2804 | 2025-09-13 13:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 7aac0bfd-39dc-30d4-8a6f-74a2099ccbf5 | -15.1748 | -52.4839 | 2025-09-13 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 197.5 |
| 34fde782-09f3-3f25-9781-df58f1a14c04 | -11.1896 | -51.419 | 2025-09-13 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 154.8 |
| e6abf52f-90e7-3ba5-a4a7-35a370dc8ee6 | -11.8853 | -50.5554 | 2025-09-13 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| ca5fb7cc-057e-3fa5-aab7-a18fec58a89b | -15.0436 | -50.1337 | 2025-09-13 13:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 0f941f58-61cf-352e-96a2-07fe477363ee | -14.2097 | -46.2209 | 2025-09-13 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| d0f1c7db-150b-385b-b81b-04c03ebf1e50 | -10.8567 | -48.1827 | 2025-09-13 13:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 2ff8d00d-cc13-3a9f-9aee-c8cec652c51a | -12.104 | -47.6039 | 2025-09-13 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 139.7 |
| ec815d95-4bee-3afb-bbba-2b914b826a61 | -12.5979 | -45.7021 | 2025-09-13 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 98e1f0b7-367d-3abe-b555-d0e2039c3a0f | -14.2092 | -46.2439 | 2025-09-13 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 1132af74-b566-37b4-a927-24e139e4832e | -17.4346 | -49.2258 | 2025-09-13 13:20:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 133.5 |
| a340ac3c-14d5-30d0-808a-4138e057f79c | -9.2658 | -59.3997 | 2025-09-13 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 182.4 |
| 48219ea6-6a91-37ea-b4d2-6f3165f2549d | -15.1165 | -52.4918 | 2025-09-13 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 2d1aefe4-2073-3c26-9334-ffabcca22bb4 | -13.203 | -51.7406 | 2025-09-13 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 215.3 |
| af7fd384-9f84-3b69-8c83-8fb153ce812f | -13.2414 | -51.7359 | 2025-09-13 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 8799e26d-ba12-3cfc-a881-c8a514a5277a | -11.2882 | -51.1334 | 2025-09-13 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| be72c023-e1f8-31c5-91c8-14077ef22ead | -19.3417 | -45.1132 | 2025-09-13 13:20:00 | GOES-19 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 97.7 |
| ffa228b3-2519-379f-8007-6ebd1d8ba8b1 | -15.1554 | -52.4865 | 2025-09-13 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 234.1 |
| eb39ce53-b50f-3da9-8c2d-242065a16671 | -13.2341 | -43.7554 | 2025-09-13 13:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 230.9 |
| dc888987-525f-3e5a-a643-367caa62d57e | -12.1236 | -47.579 | 2025-09-13 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 304.9 |
| 89cbdf51-102e-3ff8-aa45-d02ebdc474d2 | -7.7282 | -44.8496 | 2025-09-13 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| b47dcc6c-ff68-3da4-8830-e1615d700088 | -11.4696 | -50.389 | 2025-09-13 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 3df5276c-9e7c-3214-9b4d-5ba64e9a52c0 | -9.2656 | -59.4191 | 2025-09-13 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| ee26745a-a4a1-3a2a-b488-0f67463a2067 | -11.3923 | -50.4833 | 2025-09-13 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 3d86bbbb-4904-3b6d-94ec-592e7dbd7d00 | -14.29 | -46.0924 | 2025-09-13 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 1f6c67b1-8a82-32b3-a746-d05f50ccb3c2 | -13.2535 | -43.752 | 2025-09-13 13:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| f7d32cfe-50ae-3ea2-8ce8-4f22843823cd | -14.4588 | -47.3174 | 2025-09-13 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 40fbd9da-6788-3c37-8929-cc49d7f67bd4 | -17.4142 | -49.2519 | 2025-09-13 13:20:00 | GOES-19 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 42d26a05-ef49-3400-99bb-683ce71b69e4 | -15.4713 | -47.3256 | 2025-09-13 13:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 0db09a0c-3fde-3c6b-a79f-0c160d0d0c49 | -10.8785 | -45.5597 | 2025-09-13 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| c1742dac-62fa-3218-8e27-aeefcdafd00f | -14.4394 | -47.3206 | 2025-09-13 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 205.3 |
| f2f78c6e-c62b-35e3-8564-ce8c5907a108 | -12.1044 | -47.5816 | 2025-09-13 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 234.9 |
| 4ac9b5f9-e027-3e5b-a86a-f18c4a9f9d4c | -14.4389 | -47.3432 | 2025-09-13 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 58957004-47ec-3ce9-b887-a8295b397694 | -10.3699 | -50.507 | 2025-09-13 13:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 77fe368c-a4e1-3963-aa92-5a5090b336a4 | -18.0065 | -46.9499 | 2025-09-13 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 99.6 |
| f6134fe0-2955-3f28-9fd9-d76612844c8f | -12.8259 | -47.9486 | 2025-09-13 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 63f0fb11-ed41-34ce-a3d5-1cc6e50435e5 | -10.7664 | -50.5299 | 2025-09-13 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| e1e18ec9-15f3-3255-bbe0-62b7a2b98d27 | -11.3926 | -50.4619 | 2025-09-13 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| f5dcf906-ff35-3382-b648-1b5d05fa9479 | -14.2088 | -46.2669 | 2025-09-13 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 8fffe2e0-15eb-31f0-9c11-a1a7ad2dcadc | -11.7826 | -47.402 | 2025-09-13 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| c83f2e84-c988-3f3b-9572-3181173727d1 | -12.9402 | -47.9991 | 2025-09-13 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 6255315e-66c7-3ffa-8ef6-df925c3d14e0 | -12.9595 | -47.9963 | 2025-09-13 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 36fc7523-6853-34ed-81d5-008c5f9f36e3 | -12.8263 | -47.9263 | 2025-09-13 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 89ea0e8c-a635-32f8-8759-b2ece1215517 | -14.4199 | -47.3238 | 2025-09-13 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 1eebe432-7070-363a-a81e-8e40d2d2f971 | -17.4137 | -49.2744 | 2025-09-13 13:20:00 | GOES-19 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 6f6b8f39-d3d6-35a8-b60b-c9bbf6a6485f | -14.3095 | -46.089 | 2025-09-13 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 210.9 |
| 6d73bfa9-470b-347e-9a7c-96ccfa194b7b | -12.8452 | -47.9459 | 2025-09-13 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| c4cccf0b-6aca-3e80-9754-9e40660dae61 | -14.4364 | -48.4421 | 2025-09-13 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 648315c7-0a77-363c-9ce0-840ab94c72fc | -15.0432 | -50.1556 | 2025-09-13 13:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 3543f4fe-d110-3900-90f9-afaf0530d8f6 | -12.9591 | -48.0186 | 2025-09-13 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| fa96acd0-fcc6-3591-a1c2-7cd0e2bfe17d | -16.3422 | -51.5217 | 2025-09-13 13:20:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 4125c4d6-5673-345a-b324-ec263363687b | -7.2131 | -43.8396 | 2025-09-13 13:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 261873a5-ca01-370e-a85c-3e4435c71dc1 | -13.9168 | -48.2998 | 2025-09-13 13:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 3d0b7926-08d3-387d-a6de-238895579e1a | -7.3954 | -44.3539 | 2025-09-13 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e3560ac3-7582-3017-b613-5cc100a54c8b | -14.0072 | -44.7733 | 2025-09-13 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 904251e2-b7fc-3ee8-a930-dc505ec948d2 | -14.2905 | -46.0693 | 2025-09-13 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 83d9319f-a73c-3980-98db-7a1694297eba | -15.4517 | -47.3291 | 2025-09-13 13:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 135.9 |
| ecaa6ba3-0c8c-3c96-8bd0-90c8d8f09b20 | -13.9379 | -48.2076 | 2025-09-13 13:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 8b01ff7c-4412-3919-b990-07793184b804 | -13.9172 | -48.2775 | 2025-09-13 13:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| c0b79cfa-0000-321b-9eda-10dd6bc4bfb7 | -14.2905 | -46.0693 | 2025-09-13 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 7702573f-001b-3520-955d-98e0e8b36d42 | -14.4398 | -47.2979 | 2025-09-13 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 244.6 |
| 47df9dc7-a4bc-3535-bd5c-49ab7d5677ee | -12.8263 | -47.9263 | 2025-09-13 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 7b1c2dc3-dcf2-3f7c-adee-0a9b03af72d2 | -12.9402 | -47.9991 | 2025-09-13 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| adebccf7-dac9-301d-ab66-50d92442fa7a | -14.2088 | -46.2669 | 2025-09-13 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 133.6 |
| e5df7300-caf3-33d9-b384-d70f9504ec61 | -15.0432 | -50.1556 | 2025-09-13 13:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 1082f7a6-18d7-32a4-a54c-de70e5bcdaaa | -14.3095 | -46.089 | 2025-09-13 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 0387ae3b-c643-3140-8cae-4abf7db44ab6 | -14.4394 | -47.3206 | 2025-09-13 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 06d194f0-d0b1-377f-b0e1-ba0bb5efb880 | -10.7104 | -50.4718 | 2025-09-13 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| dda4a96f-1681-347b-8451-9a5919b34175 | -10.3699 | -50.507 | 2025-09-13 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 55b0439d-934c-3e74-9c42-a01eb65acb3b | -12.8259 | -47.9486 | 2025-09-13 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 71f1aa6c-7221-372e-a0a9-6b7138ad5935 | -9.2658 | -59.3997 | 2025-09-13 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 170.6 |
| 80fc21c4-f831-3b17-86f9-891d8b4b6362 | -8.9176 | -46.1565 | 2025-09-13 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| d6b05dbe-d6b4-3f01-b03e-6b6e9fce0e4c | -15.1748 | -52.4839 | 2025-09-13 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 111.3 |
| c63e6e96-f0b0-387d-a662-7916a067b1a3 | -11.8698 | -46.7627 | 2025-09-13 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| d363d4d6-a7d5-3054-90ad-651ead28fe89 | -13.9181 | -48.2329 | 2025-09-13 13:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e9d7d9f4-a69a-3bb1-8da4-d73262114dfc | -12.104 | -47.6039 | 2025-09-13 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 8c60570f-b8fd-30b9-aff3-666a449623e8 | -11.8853 | -50.5554 | 2025-09-13 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| aa19f7ea-2755-390b-8c4f-b49acb4cadb7 | -15.8845 | -47.2286 | 2025-09-13 13:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 5561a8e2-3d21-397c-8ff3-896e1ecd6d00 | -11.1896 | -51.419 | 2025-09-13 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| f59de4f6-31ac-3892-b88c-2a8bd072f92a | -9.2656 | -59.4191 | 2025-09-13 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| a96a7c46-7e77-30a6-afc2-14a375d6b1f8 | -11.1259 | -51.9309 | 2025-09-13 13:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 220.1 |
| edd00242-cb24-3543-86d3-8cdf3cb59363 | -18.0041 | -48.6451 | 2025-09-13 13:30:00 | GOES-19 | MARZAGÃO | GOIÁS | Brasil | 5212907 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| ee31b45c-28ee-3f96-a1d6-9214eee506b5 | -12.8452 | -47.9459 | 2025-09-13 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 202e29aa-f14e-3570-8526-c9236380f9ec | -11.3831 | -47.3429 | 2025-09-13 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 6e4021ca-08e6-38f5-ae37-ee56c17fa9dc | -11.8284 | -50.5406 | 2025-09-13 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 15fae427-b787-3060-9698-4857e51a421a | -11.3926 | -50.4619 | 2025-09-13 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| c8a32fa7-c88a-3ab0-a49c-48f1a740282f | -12.8456 | -47.9236 | 2025-09-13 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 0c5d90e1-2ef8-39e6-a889-a6767715c33e | -13.203 | -51.7406 | 2025-09-13 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 208.7 |
| c31908d6-a12b-3759-890b-7c027ea82c36 | -11.885 | -50.5768 | 2025-09-13 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 360d6f3a-f850-3ddc-98cb-35d7ed2cfb7b | -10.3509 | -50.5089 | 2025-09-13 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| a4a31e2b-0541-3127-95cb-c400d13e95b8 | -11.3923 | -50.4833 | 2025-09-13 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 9938cc92-0868-3da2-ab87-df86bb610375 | -14.29 | -46.0924 | 2025-09-13 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 3b282bc5-a4fe-3430-8727-bf01700709c2 | -15.0436 | -50.1337 | 2025-09-13 13:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 124.1 |
| e0843cec-0bd9-33df-a5de-4ecc9dce9461 | -10.7474 | -50.5319 | 2025-09-13 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 7e43fadf-ff81-3d2a-b29d-3093fb854d6f | -13.9379 | -48.2076 | 2025-09-13 13:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 467a9e1a-bf20-3d41-8c73-5eaceea5e136 | -12.5791 | -45.6821 | 2025-09-13 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 5f7e4fa8-e5e4-35b9-b9c3-e32110030f09 | -7.4513 | -44.3946 | 2025-09-13 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 9ee75f5f-d98b-324f-8b08-ce8fe45dc210 | -14.4204 | -47.3011 | 2025-09-13 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 128.2 |
| f1ae25b2-3c45-30b3-a099-302844decab9 | -15.1554 | -52.4865 | 2025-09-13 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 158.3 |
| e3d1d32e-246f-3869-991f-4cd7f16c8525 | -17.4142 | -49.2519 | 2025-09-13 13:30:00 | GOES-19 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 109.1 |


[Clique aqui para ver as próximas entradas](README128.md)
