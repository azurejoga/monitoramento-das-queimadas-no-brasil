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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a3ce959-5f95-395e-8a71-c3f4a6b6a8de | -7.7364 | -44.1592 | 2025-06-07 04:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 11d1cde4-3783-3e9b-8062-a4ff6a203e17 | -7.7176 | -44.1611 | 2025-06-07 04:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 2aac2831-b66a-3040-9f4d-39f3c489b67e | -6.9602 | -42.9052 | 2025-06-07 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 44.1 |
| 4e67a5b1-4cbe-3cc6-910b-60ac168ef579 | -7.7361 | -44.1823 | 2025-06-07 04:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 98923548-8acd-323e-88fb-1963160d64fa | -5.6567 | -43.7161 | 2025-06-07 04:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ece05f63-3c90-3b23-95b3-58a7e176af55 | -5.6379 | -43.7175 | 2025-06-07 04:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 7ba71eee-1904-3b8f-972a-985bab2f5124 | -22.5675 | -42.16894 | 2025-06-07 04:00:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 84f99ef2-a4d2-3190-8186-e28f7697c3ee | -22.56808 | -42.16522 | 2025-06-07 04:00:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 590fe84c-b388-389a-a4d8-7e1330585f6b | -23.40801 | -46.55563 | 2025-06-07 04:00:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 06238212-3be4-37d8-95cc-5f2c2cf9ec81 | -22.57081 | -42.16954 | 2025-06-07 04:00:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0feb144e-6244-30c6-814e-6a8a542d9717 | -23.34018 | -46.77456 | 2025-06-07 04:00:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cff79480-c68e-3ebb-9293-10ba6dac5bb5 | -7.7176 | -44.1611 | 2025-06-07 04:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 03d745a5-f134-3540-9d5d-d12c4854e379 | -7.0169 | -44.5954 | 2025-06-07 04:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| a6329139-0db0-3466-aa5d-c1d64e498166 | -6.204 | -43.3241 | 2025-06-07 04:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| a705676c-c657-3954-9da9-cf986687d5ac | -7.7364 | -44.1592 | 2025-06-07 04:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| ea6fb944-29c3-3e6d-b5cf-88efcbbc548d | -6.9602 | -42.9052 | 2025-06-07 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| c0683836-fca2-36a7-b4fd-1894dbdcffb0 | -5.6379 | -43.7175 | 2025-06-07 04:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| cc71126a-df6d-39c1-8b78-584133e4ad42 | -5.19033 | -43.31716 | 2025-06-07 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94b8e42c-f44e-3831-80dc-965edb6b511e | -2.9188 | -48.23739 | 2025-06-07 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 89816795-b1e9-37bb-b6cf-5614d8acc3c9 | -2.44308 | -47.47821 | 2025-06-07 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bacbc6e-79f7-3402-a735-34716b86c913 | -4.49765 | -40.63058 | 2025-06-07 04:19:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c636c88b-46e8-3915-894e-ce48fd54939f | -5.19088 | -43.31359 | 2025-06-07 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3224fc45-08c7-36b8-9b25-3b0de680a1d6 | -4.49696 | -40.63501 | 2025-06-07 04:19:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1dacd315-6ad5-3e60-9bfc-3fe26d87e942 | -4.66628 | -41.96259 | 2025-06-07 04:19:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 366fe3ac-1557-30cc-a408-1d36eb2bfc02 | -4.75648 | -45.30782 | 2025-06-07 04:19:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b32d4541-5b14-34c0-8f3d-70edd3db0172 | -5.18936 | -43.31353 | 2025-06-07 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e5073ec-5066-3f50-8ca2-ab2c99a97317 | -5.1888 | -43.3171 | 2025-06-07 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a281ddc3-e755-3bdf-ae86-fa617f7f8d32 | -5.19369 | -43.31768 | 2025-06-07 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 319efff9-b2b4-322b-bd7c-fe7695898273 | -4.66978 | -41.96313 | 2025-06-07 04:19:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ca5168bc-be19-3495-9dc5-d070ec479ad0 | -4.67037 | -41.95927 | 2025-06-07 04:19:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| df80e835-ba18-3121-8745-35f36d8ed328 | -4.75983 | -45.30834 | 2025-06-07 04:19:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aac23946-1078-3929-a2cb-0549eac07caf | -4.8596 | -37.60976 | 2025-06-07 04:19:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8fda7799-64f7-3851-96ec-ae8a658dbf66 | -5.6379 | -43.7175 | 2025-06-07 04:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| e300f4f3-ce33-3e05-a2b6-dd0f43bca376 | -7.7176 | -44.1611 | 2025-06-07 04:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 3d225fef-d38d-30bc-982a-feeecaa3249a | -7.7361 | -44.1823 | 2025-06-07 04:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 2fa6b2de-daa0-3f01-80de-41099e9f6736 | -6.9602 | -42.9052 | 2025-06-07 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.1 |
| 5135479b-476c-3b64-988f-8cf5f85bb9fb | -7.7364 | -44.1592 | 2025-06-07 04:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| dbb512ef-7737-3a09-9249-196be67118c3 | -6.9414 | -42.907 | 2025-06-07 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 42.5 |
| af6ebce0-7a01-34b7-9d6c-005c840d73cd | -8.59302 | -45.87457 | 2025-06-07 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e07c8e1-1f5b-3875-9947-63fc6986b9e3 | -7.18515 | -42.82074 | 2025-06-07 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 182a7226-29fc-30d9-9b4d-a49d52a9a2e6 | -10.65695 | -49.36625 | 2025-06-07 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c79de2b-8380-3efd-9100-53270714dd50 | -7.0139 | -44.61528 | 2025-06-07 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea90a211-aade-34ac-9143-90ec4b68676a | -11.78317 | -47.40496 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d805d676-7296-319b-9e35-be9b3e0a6182 | -12.38815 | -47.31742 | 2025-06-07 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 265cfb92-608f-3798-8ca3-5e5989df5e91 | -6.8136 | -45.0033 | 2025-06-07 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bf0cd25b-39ca-37dc-bc0b-7f8c74097c75 | -6.45199 | -45.72074 | 2025-06-07 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c39cf61c-45fb-37cc-8375-3f1b8b186f1b | -7.80418 | -46.49818 | 2025-06-07 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33dcb493-c35c-307d-998b-4b4a57686eec | -7.73041 | -44.16406 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5459a4c6-f696-387e-bca6-741f26f78afb | -9.06921 | -47.14174 | 2025-06-07 04:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d699c5f-d5ff-31ae-b780-3ace51a18da5 | -6.29475 | -44.21664 | 2025-06-07 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74205f55-72b8-36c5-8f34-002869bfdccf | -5.78375 | -43.61958 | 2025-06-07 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34aef872-b175-3c9e-8a60-1c0a7045be57 | -11.13904 | -53.94333 | 2025-06-07 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8c0aa04-6aad-35aa-b957-c84cf44ce144 | -9.07605 | -47.14288 | 2025-06-07 04:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 10680e6a-12f4-345c-854f-b12f28800258 | -7.73935 | -44.17269 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d3d71648-b21d-3608-9e34-1c18a617b280 | -5.7832 | -43.62311 | 2025-06-07 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66155732-11da-3629-94ca-cdf735ccddca | -7.02106 | -44.59144 | 2025-06-07 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48152223-613d-35cf-997b-a30577fa13cb | -6.81693 | -45.00382 | 2025-06-07 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 656b253c-db04-3c01-96be-1efc9a960c6f | -10.87652 | -49.553 | 2025-06-07 04:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f63a7fe3-8f6f-3d66-9dbe-2ae8ce7cb0af | -5.64811 | -43.5982 | 2025-06-07 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72503386-72e7-33da-81fd-a80a1355376c | -6.95913 | -42.90713 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.9 |
| f4ad9ea1-9739-3234-9406-ab26ddd2da6f | -8.17766 | -46.50216 | 2025-06-07 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49318a3f-a181-31c0-95f2-f173331ca4c6 | -6.20364 | -43.32581 | 2025-06-07 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b9707e5-1b1d-317e-865c-57f53298a6e6 | -7.71927 | -44.16956 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e7a3cd4-fb08-3700-8463-ecd6b882693a | -7.73321 | -44.16812 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4f128ab5-7429-3371-b452-96232d54654c | -7.72986 | -44.1676 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4d61a8eb-a81a-32f8-9b02-da2aa2d683b2 | -5.6405 | -43.71252 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e147a7c7-6ee5-35b5-a8a6-26ccf0162f31 | -8.06974 | -46.84424 | 2025-06-07 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f47bfe4b-384f-36b2-a364-c2e891515f2f | -10.73565 | -47.61451 | 2025-06-07 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b36887e-653a-305b-9d61-48f9660e422f | -7.72762 | -44.15999 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f8e05249-e5ec-3132-a38f-f8e6f31bed73 | -6.96315 | -42.90393 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.9 |
| d05ea7a1-ab58-3c38-88a8-93ead22f088c | -8.44607 | -46.48188 | 2025-06-07 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7deba214-c5b6-3a19-a9d4-dd8f117af1bf | -6.60113 | -44.18243 | 2025-06-07 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afbbe681-883d-3e59-a3f4-9a004acccd8a | -11.78436 | -47.39762 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a5e84b3d-0761-344a-ba3a-886fcd687e3a | -12.38874 | -47.31379 | 2025-06-07 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e0953e8-c3a5-372f-92d1-3a59f3c80f66 | -11.14326 | -53.92058 | 2025-06-07 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21a8d4d8-7dbe-39d8-a175-e1a94ec49ebb | -5.64384 | -43.71305 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8231c489-fe64-32f5-aaa3-cecc352b9791 | -10.46445 | -47.9465 | 2025-06-07 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d845719b-51c8-36aa-905c-b03baa7601bd | -6.94717 | -42.80133 | 2025-06-07 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 99f4cddf-2657-3aef-b0fd-b9ffa107a21b | -12.26962 | -44.58516 | 2025-06-07 04:21:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7da873c2-73e4-3965-b031-95aaf116cae8 | -7.67817 | -46.09112 | 2025-06-07 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce191712-9047-3fc7-bc9c-accd762f7685 | -9.40399 | -48.44338 | 2025-06-07 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d1511924-5bd2-3a24-93ba-97185fc5f1f8 | -5.64609 | -43.7206 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 41fdb6de-02db-3680-85ed-9846852cc4f3 | -9.50168 | -40.37328 | 2025-06-07 04:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 638541ad-39cb-3717-bf51-136880ddb3c5 | -11.90471 | -44.8757 | 2025-06-07 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5abbb44c-8f89-3963-8131-95e5e657cf61 | -12.53848 | -45.41721 | 2025-06-07 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbd30874-863c-35f3-a345-c435457c7719 | -12.4736 | -46.34385 | 2025-06-07 04:21:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96f9020e-aae9-39b2-814c-b25fc03dc9c4 | -9.07948 | -47.14344 | 2025-06-07 04:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8805cf21-1083-34e3-8737-ebc9a1684516 | -7.02439 | -44.59196 | 2025-06-07 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29f97d9d-ac77-331f-9b1f-c1d68044a7f1 | -7.72151 | -44.17716 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22a5686b-a731-3b4d-acdd-7166423c3c1a | -10.30068 | -57.1413 | 2025-06-07 04:21:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e947a2e-c3b2-3f28-9f65-128b4ce89030 | -6.28937 | -48.50444 | 2025-06-07 04:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 13b65cb4-addf-30a6-9e5c-39d05ad33527 | -11.81654 | -44.26485 | 2025-06-07 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d1305d2-97b4-3625-a639-0a1c6b3cbb57 | -9.40468 | -48.43923 | 2025-06-07 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2e345e8a-2ce6-35e7-a4f2-14ad91e692ba | -10.6299 | -49.43533 | 2025-06-07 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfa86f01-da9b-3220-974d-80f1d1f2f595 | -7.18111 | -42.82398 | 2025-06-07 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b00baac8-ea2e-3b34-b0c3-6759f2cf87bc | -6.21173 | -44.50645 | 2025-06-07 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6334be83-dd24-3bf6-93e7-c02dffc03015 | -6.66174 | -47.73483 | 2025-06-07 04:21:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b28db5d-3e92-3151-9744-1d5b118b8b08 | -9.60998 | -49.01744 | 2025-06-07 04:21:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5666d450-006e-37c2-9265-7a68f6957f6f | -7.731 | -44.18226 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a98dad9b-ec75-33bf-8f39-7483f8a3b453 | -8.17428 | -46.50161 | 2025-06-07 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README12.md)
