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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57f20434-432f-352d-9658-4a3301745cf9 | -3.53964 | -43.55835 | 2024-11-11 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 214383bf-1283-3455-b796-d62b6c900585 | -1.40419 | -52.37819 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f79f9e72-d635-3442-9bf0-88906b1f8983 | -2.12841 | -48.55788 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbaa7cd4-7a25-3d47-974a-18207a7466ff | -2.17264 | -46.70733 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3f1822c-fac4-3489-a5d1-205e7ad931f1 | -2.56785 | -47.33477 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dc536d5-7fec-3d26-b3d6-992f475b38e6 | -3.20028 | -46.50357 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cbd3bae-9dce-394a-852f-67ec328a2298 | -2.18985 | -46.57546 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42a56aed-8b4a-314c-b044-7a86f8c5423f | -3.95362 | -46.70901 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8372767-453e-3db3-95bb-a3ba7af4f6ac | -3.47457 | -53.48969 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59d7f0b7-998f-3def-93dc-687229a10558 | -3.38316 | -45.27993 | 2024-11-11 04:18:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f1c43c7-3b62-3ff7-8389-3097d2778ee4 | -2.541 | -47.31247 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ead3b0f-384d-387c-b7d3-707abd1b1b78 | -2.36766 | -48.56823 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c65d1db7-79fd-3608-bf65-7c7fe78d08a6 | -1.63549 | -52.5407 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d423a7e-07da-3045-9ea7-3c8bdd470431 | -3.539 | -43.17068 | 2024-11-11 04:18:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbbb3fa5-d9b5-3084-b658-b9c2a2727c40 | -3.94665 | -49.00267 | 2024-11-11 04:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 61da0c34-0fa7-3901-9677-0d60643b1fa6 | -3.26348 | -53.70069 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd617d2d-5480-372c-88e2-9f213f18472e | -2.75419 | -49.34813 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3a514d8a-2bf4-3ced-bd25-f37d24413272 | -2.2718 | -56.16972 | 2024-11-11 04:18:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dc87ffb-4fc6-3dfe-a921-d552a155190e | -1.39584 | -52.36985 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49052fec-2cd2-3fc0-95eb-9ebc39f9e79c | -2.68789 | -46.82076 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e0e9420-4300-371a-b11f-a190d4aacf0d | -3.24239 | -45.37637 | 2024-11-11 04:18:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b51ac061-a9c1-3ced-af1c-fb0ef142122e | -2.18637 | -48.37886 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6580de6a-e7cb-3799-9074-96df63e9ed0c | -2.60356 | -51.71527 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 890c9ec0-c130-361c-a4bb-0470e0290924 | -2.35606 | -46.79766 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44695493-d4ba-3ba9-9c7e-109b971c59a9 | -2.64851 | -46.78945 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33c14e69-d0cb-309c-b539-18feec0de910 | -2.36411 | -48.51434 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14e640af-7bf4-3eb9-b886-50f324683911 | -2.26767 | -53.75109 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b3417153-787d-3b3c-a6f5-32b55b5d1d2b | -1.44434 | -51.67277 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b6fe716-ca8f-39cb-9dfc-eb6a9e0616f3 | -2.0837 | -46.53878 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e62dd16f-b580-3c58-9fa9-28e42be15c3b | -2.13098 | -48.56576 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfe45d36-55a0-33d9-b29a-93f021346104 | -5.37826 | -42.76537 | 2024-11-11 04:18:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c7bc269a-c6e9-39bd-980f-780846796a90 | -2.21188 | -48.37244 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f14a14b2-1052-3a8f-ba4a-86cc102c213a | -3.7381 | -44.53452 | 2024-11-11 04:18:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1045e95-af3a-31e1-9138-ac0c9bf1249e | -4.02456 | -46.96239 | 2024-11-11 04:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7842d57-f8dc-31eb-810b-2d10d3e19a9e | -2.2127 | -48.36735 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b69507a0-1f01-33fe-b865-2681389cc0eb | -2.22204 | -53.67125 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 477b3c2f-db41-3c10-9a20-dee33b792712 | -2.20791 | -48.37181 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25a60092-900e-3b9c-88a9-dc4e0146a6d1 | -2.87295 | -45.37123 | 2024-11-11 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b1b542d-57b0-308f-9451-2f222aa3e48f | -2.73885 | -45.97765 | 2024-11-11 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef23d61f-4a66-3b4d-b941-bd1879582654 | -2.16241 | -46.42612 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c60e148-5298-34be-813b-7120466d85b0 | -4.68028 | -46.41066 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c21c9cc6-06d3-357c-be3a-e8e14dcdcbf2 | -3.247 | -46.48221 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 503ab660-a42c-3fe1-b520-e1769a6db065 | -1.40242 | -54.49854 | 2024-11-11 04:18:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf08b688-a937-331b-9529-bf9313285478 | -2.89893 | -46.83053 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 263f891b-c2a4-34b2-90bf-1deb67e01346 | -4.58511 | -47.0681 | 2024-11-11 04:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24383281-d8fe-354b-a224-edf8a43f17b1 | -2.29193 | -46.77612 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 305a2441-e38b-3bf8-bf5f-95a608cb04ea | -2.57332 | -46.54038 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 186ee607-11d0-3c04-927d-1cffbe8d83aa | -2.36461 | -46.79055 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eab2919d-0185-3733-8cd3-0a52e75a014f | -2.40647 | -46.29985 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00f4f157-fd54-35df-ad23-101cdbb4a226 | -2.87491 | -46.65958 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39ffa5bd-e13e-30fb-b194-0afb53915c9c | -2.41826 | -46.52237 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a552b413-54af-39d4-9187-b29a552899d4 | -2.87411 | -45.36397 | 2024-11-11 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a97ab91d-c65f-3a62-990d-013150ad9ca3 | -2.37717 | -50.33902 | 2024-11-11 04:18:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd9869d3-186b-3f73-84ce-e311e562e1d2 | -2.2222 | -48.85086 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9a276a7-d838-301e-843c-245f6569cd74 | -3.02541 | -47.97095 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 66f76df8-dfb2-314c-b470-20f4c877c187 | -2.4189 | -46.51834 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bb34e850-6627-3f9d-ab88-b4e92627b867 | -2.11945 | -47.8979 | 2024-11-11 04:18:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46cb1916-eba5-330b-af47-9b4e0ddc3a3a | -2.75325 | -49.35599 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e13b62ba-2e7a-36b7-9a21-254ca0bfdd3e | -3.60427 | -44.26535 | 2024-11-11 04:18:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6fa4a93-a0b2-3fdb-8eba-0957b97d0cfe | -1.227 | -51.75436 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fb521af-ca5d-302d-b404-c037f6daed3f | -2.60844 | -46.16247 | 2024-11-11 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1366edf-333e-3953-b25d-d5db1050314f | -2.09344 | -46.52364 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93a5faa8-d28a-329b-af1b-1c4c5849a839 | -2.57826 | -48.13608 | 2024-11-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 344a0895-5797-3401-82d4-1f14ccb09d5a | -2.46254 | -50.39274 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 985700a0-9414-3267-beae-019b63d6c006 | -1.47838 | -52.09095 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fcaf405-2482-3f87-8b7b-e8554513f438 | -4.62085 | -46.68987 | 2024-11-11 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 659a3a96-6ab7-3dec-86f0-327024d45e80 | -2.30245 | -48.45704 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72a0dee0-1035-3ba4-bf71-5a4b8af97563 | -4.67886 | -46.37531 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb92f4bb-b91a-3b29-9bf9-95c3186b88d8 | -2.62616 | -46.16836 | 2024-11-11 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 676c9635-9df2-3462-9401-bc8f53e0888f | -2.8195 | -46.65211 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 863bf1d7-a641-3939-8364-a9b0979302b9 | -4.70825 | -46.39161 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 169ab0f8-07ac-36a6-b15c-0c72d7ced867 | -5.09159 | -45.54007 | 2024-11-11 04:18:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcfdd811-06a3-305b-b248-a697aab5e9b1 | -1.39998 | -52.37085 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 14dd79ae-3690-3a00-9909-b50eec09c964 | -0.64772 | -51.71344 | 2024-11-11 04:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5d7d4644-5989-326d-817b-81ab3eefd00f | -2.22246 | -50.85823 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a20eecc9-7cef-35b7-930c-5d852a303e73 | -2.17309 | -48.32277 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 080830fe-91df-3d28-bf3c-7402ad8c6fb2 | -2.73945 | -45.97386 | 2024-11-11 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 079cca79-405d-33d8-99d5-9ff9c3009b80 | -2.05709 | -46.13956 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| def6f552-4e06-3ec9-8926-abffe69e3fc1 | -2.34235 | -46.54887 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c45398d9-9f97-3881-97d2-6b2cb123416f | -2.40655 | -46.50404 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00998067-83b8-3a15-82bb-568e667330e8 | -0.14496 | -51.40107 | 2024-11-11 04:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77a74112-f6a1-3b83-85a6-545df75af74a | -3.01656 | -53.26104 | 2024-11-11 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7433d1d-a9e3-31bb-9cf5-c49434c82d4b | -1.1791 | -52.0836 | 2024-11-11 04:18:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84adb241-81e0-344e-b133-05bac0b06fef | -3.23446 | -45.38253 | 2024-11-11 04:18:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee1cade0-7ac1-3303-a9a3-61c2aebe8674 | -2.94931 | -52.57312 | 2024-11-11 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0781563c-e1c2-30bd-9d4c-97b21d8b24be | -3.00122 | -46.93862 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfc65595-14d3-3082-8ef1-9fec00cab647 | -2.10125 | -46.52071 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86bb2ace-6adb-392d-a1a3-2eca1990a9eb | -2.87634 | -45.37177 | 2024-11-11 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 5a890118-e7be-3c11-88d8-6bf20cf6218b | -2.70001 | -46.81434 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2485bbd-df61-39fd-8516-e71315b18a5d | -2.2497 | -46.50932 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7058c64c-dea9-3874-ab71-1e124aa0bf18 | -3.23679 | -46.54556 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20c7bcfd-ab28-3c8b-ab5d-cb9ca38a5c96 | -2.60345 | -47.73606 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00e1c41b-c126-38c1-afc8-4a48e5ade6b4 | -2.39551 | -46.78273 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2994c45e-85bd-3fd1-b98b-14c0cf605298 | -1.98089 | -46.81068 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15f365b3-bb1f-309a-8a18-51422a051c34 | -1.35196 | -49.08205 | 2024-11-11 04:18:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bf342f2-9c98-31ce-9f45-d9a0b599aedf | -3.14382 | -54.47893 | 2024-11-11 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e19a2772-c413-3a6b-bf8d-5b23c9b59859 | -3.14311 | -54.48317 | 2024-11-11 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e8511777-cb9f-391c-83e8-9cee4afc45b2 | -3.14116 | -45.96907 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da4b784c-5263-3a7c-a430-524c9575873f | -2.26069 | -48.74229 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0132687-efee-31e7-8fe4-8d6eb528ea92 | -3.52861 | -45.70814 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README37.md)
