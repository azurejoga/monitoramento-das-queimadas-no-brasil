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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d7dfb01-41b6-33f9-aeb2-1c8884e976c8 | -22.09027 | -48.22989 | 2024-11-26 04:21:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1c30e5a-b3af-348b-9f2c-5e54fa595def | -20.31272 | -45.58395 | 2024-11-26 04:21:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23e9bc9a-09e4-3bbd-9eb7-3287d718c7f3 | -23.74934 | -49.01631 | 2024-11-26 04:21:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f01d89f1-209b-3ac3-ae6f-fb4b53c37ce7 | -17.64406 | -57.59111 | 2024-11-26 04:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 70adda8e-2a75-3084-b2e5-a7b3031a992f | -21.37986 | -48.63083 | 2024-11-26 04:21:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92e7f238-5bde-300d-b716-e5d90a3357f7 | -17.65238 | -57.59082 | 2024-11-26 04:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| d0761eaa-5fdf-3ecc-9617-bbb3a910ae7c | -22.78508 | -43.75739 | 2024-11-26 04:21:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5be8e11c-8d5d-3ff7-a9a1-43fc9ac1f257 | -20.3258 | -48.83287 | 2024-11-26 04:21:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51af9ec9-3a34-3c29-b55c-ea67833ce1a4 | -21.33445 | -44.95446 | 2024-11-26 04:21:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 65c3f7d4-0cd9-38b6-a409-29e9ee25ce3b | -20.47823 | -48.72118 | 2024-11-26 04:21:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f7e570c-9230-37f2-b6c6-b80fcf301fb5 | -17.64745 | -57.58479 | 2024-11-26 04:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 0968bd9a-759a-3366-b347-aee3b7270e68 | -20.35811 | -45.91176 | 2024-11-26 04:21:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 982fa738-d794-34e9-8fb6-e3bcd36987e5 | -20.95455 | -47.17051 | 2024-11-26 04:21:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e13784aa-4a12-369c-b8eb-aacb5f25a25d | -23.33017 | -46.12366 | 2024-11-26 04:21:00 | NOAA-21 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 34c987ae-4972-3e36-93ab-a11fb4c1350c | -20.76582 | -46.77067 | 2024-11-26 04:21:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c0102fb9-dd52-3384-851f-0e630f3c4453 | -20.31959 | -48.82755 | 2024-11-26 04:21:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1522bfaa-d97e-391b-b9ca-40466c76cb88 | -28.58463 | -49.44313 | 2024-11-26 04:23:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2f2053a7-518f-3308-910d-eb75f6b69c09 | -27.17486 | -50.83832 | 2024-11-26 04:23:00 | NOAA-21 | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 359f6cc9-32a9-36e1-b2a1-96d22e0574ce | -3.1876 | -48.4387 | 2024-11-26 04:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| ed620f5d-17cd-3294-945b-7fcff4cf29e0 | -3.3938 | -44.1722 | 2024-11-26 04:30:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| bdf266a4-1375-3b33-b304-ebc7056b983d | -3.5857 | -50.3787 | 2024-11-26 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 8b461bd8-07a2-3e07-a669-b6e41ed041d8 | -17.6453 | -57.5874 | 2024-11-26 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 26f7615d-d086-359b-8b0b-bb87388c5fc1 | -3.1877 | -48.4172 | 2024-11-26 04:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 5dcce2ee-d4ee-3db7-bd0f-6463e6d784d8 | -4.5375 | -43.304 | 2024-11-26 04:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| a96d29c7-88cf-3d6f-ab6d-20260133cb07 | -3.1691 | -48.4394 | 2024-11-26 04:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 20deba90-1e91-3645-830c-bbfcaea9f4b9 | -2.8014 | -53.0227 | 2024-11-26 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 561646bb-0a8f-3ca4-a017-5c15181ffba0 | -6.0862 | -48.0339 | 2024-11-26 04:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 1f05876e-a6ec-3a31-adce-0fb34e972779 | -0.9863 | -51.72036 | 2024-11-26 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae6b3627-9512-31ad-94c8-dced9e3abe7b | -1.8246 | -46.28773 | 2024-11-26 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7a51428-da2b-35eb-a596-cfe29378beb5 | -0.09818 | -51.75101 | 2024-11-26 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6968cacf-e0c4-3f69-bac5-b03f09303cf2 | -2.09459 | -45.97037 | 2024-11-26 04:36:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66a3daf4-d2df-33fb-b80f-3b7638934ed3 | -1.11126 | -47.78538 | 2024-11-26 04:36:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d459470b-b539-3464-bdc4-474b943b60a4 | 1.8298 | -55.97581 | 2024-11-26 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dbb2e06-6896-31bf-814c-469d4fc4229d | -1.13315 | -48.33572 | 2024-11-26 04:36:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f5255c4-737d-37ad-8e75-7091bdc9791d | -1.31503 | -51.7516 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6ba046a-39dd-3a32-895f-70b020e36a35 | -2.1809 | -45.6012 | 2024-11-26 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32f81de1-b222-3857-a5f9-93a2459e69c1 | -1.43175 | -47.31977 | 2024-11-26 04:36:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7494a715-7cbb-3007-9fd6-64bf2866ff8c | -1.73474 | -45.69086 | 2024-11-26 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9091c707-b18e-3b31-8f91-07ce3145d9dd | 2.68222 | -60.42446 | 2024-11-26 04:36:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ce8e6e34-0a4e-319c-9fd9-64d0e7264c00 | -1.50286 | -47.47024 | 2024-11-26 04:36:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0609e583-eea9-340b-9e4a-d67be2011685 | 1.94528 | -55.74191 | 2024-11-26 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3fde847c-c78d-361f-893f-c3abfe14300b | -1.58656 | -45.46249 | 2024-11-26 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e9574d45-1644-3d7b-aaa5-358c5434ea9b | 1.83493 | -55.975 | 2024-11-26 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f0fb988-5f34-30da-b6ea-4dcd77f8ac19 | -1.31374 | -51.74901 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 579540e5-5beb-3a1e-a9aa-5b4c5343becb | 0.95066 | -50.75544 | 2024-11-26 04:36:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c22f944-a463-39a1-b867-35f999e62c6a | -0.87511 | -51.72537 | 2024-11-26 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 494af4a9-c720-39e1-8f4c-ccbf44dff8af | 0.94746 | -50.73485 | 2024-11-26 04:36:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a613d419-f4fe-3a5d-b224-5ef8f572fba0 | -2.22045 | -46.38892 | 2024-11-26 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c014505f-6ce0-3e50-beba-479c3d433353 | 4.2331 | -60.07992 | 2024-11-26 04:36:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0162ad24-2a4d-3c0e-aac3-71452af67b3e | -1.13592 | -48.33967 | 2024-11-26 04:36:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c554777c-66e6-3309-be8f-00ac83ec672a | 0.98387 | -50.06586 | 2024-11-26 04:36:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 402e7c24-81ce-3a24-b6f2-73cd44006d62 | -0.87429 | -51.72288 | 2024-11-26 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63e95ea0-1bf5-36c0-b7e2-93a1054c5099 | -2.24664 | -45.48327 | 2024-11-26 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8327e4f-8a52-3a02-a2af-7c97007df614 | -2.15352 | -45.57286 | 2024-11-26 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfb47fe6-c28f-3393-9b77-5e83e5b099f6 | -1.18621 | -53.88295 | 2024-11-26 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 787e1ee0-2de6-3237-9038-e493d5e862f4 | -2.19095 | -45.60688 | 2024-11-26 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c0d9543-e398-3e83-a3eb-93c033b07a6e | -1.0456 | -51.74133 | 2024-11-26 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f52b919-0063-35aa-90f9-fe28fd0ad511 | 0.6951 | -51.44149 | 2024-11-26 04:36:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00910d73-a99d-3473-8423-5db523e292a5 | -1.54662 | -48.28762 | 2024-11-26 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 868813f2-042f-399f-a96a-d37f8a271f43 | -1.93314 | -45.75949 | 2024-11-26 04:36:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cce895f0-9d97-3218-83dd-7e3dea1a5b2f | -1.31207 | -51.73536 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d195c39f-aeeb-31d0-8ae4-7e5be2ea8f0d | 0.9445 | -50.73952 | 2024-11-26 04:36:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdda17f3-eecf-39a8-bb86-aba08fc3edf8 | -2.17734 | -45.60064 | 2024-11-26 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48f5fef5-989e-39cd-b9b4-0cca12a7de77 | -1.67388 | -45.80244 | 2024-11-26 04:36:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e975b7b0-50f1-394e-a07a-c221041f716c | -0.7526 | -47.26777 | 2024-11-26 04:36:00 | NPP-375D | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e317c297-6610-3327-b494-7ca0b9b0f61a | 1.82467 | -55.97668 | 2024-11-26 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80cb35a3-f1a4-379b-9dd4-0b252b0874a9 | -1.39677 | -52.55513 | 2024-11-26 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63870364-4e25-3bc3-b04a-f904df0442fc | -1.29357 | -51.73244 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 713d5d1b-5a56-3f63-bb43-4c6afd03cb74 | -1.10498 | -54.14933 | 2024-11-26 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08640611-3650-38e3-815c-8df39bfef743 | 1.99863 | -50.80325 | 2024-11-26 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3feb782a-9811-3916-a1fa-6bc3f2b543db | -1.31573 | -51.74726 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f98f72f5-927b-3e35-972a-9f7c60db2840 | -1.30399 | -51.73854 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00c5b7de-9cf9-334a-a4d8-a0ff292f283b | 1.94065 | -55.74559 | 2024-11-26 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41d3d23f-2e6e-3794-a0bb-30e1a869eb89 | 0.96906 | -50.13147 | 2024-11-26 04:36:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50159659-b0f8-35b9-90ca-fc8301072a15 | -1.56094 | -45.67353 | 2024-11-26 04:36:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe886c1a-ef90-305d-a057-e93d52de4c39 | 1.99564 | -50.80807 | 2024-11-26 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33a71d8e-f843-3429-9f52-f2d3b948ecb4 | -1.56447 | -45.67406 | 2024-11-26 04:36:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf3f8ba9-9dac-34b6-adff-58024d3ec42e | 0.66963 | -50.79475 | 2024-11-26 04:36:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3297c093-c812-394c-b790-aed71b05cc37 | 0.67388 | -50.7983 | 2024-11-26 04:36:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65abe3fa-2a29-38c6-add6-3213f0b4f1a6 | 0.9481 | -50.73896 | 2024-11-26 04:36:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c0551f2-b973-36de-b915-38bb5d488f07 | -1.27511 | -52.16712 | 2024-11-26 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07af701c-af20-33a7-b7fc-2221ef92c632 | 1.83445 | -55.97193 | 2024-11-26 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4256ca23-3d03-3d22-b1df-6c7d2b3c01ef | -1.10794 | -47.78487 | 2024-11-26 04:36:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f12c277-0609-303a-86f2-56ddf6ff0bb7 | -2.17853 | -46.38625 | 2024-11-26 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fa1013c-7a9d-34a9-abb6-3f3bd27a3f7f | -1.67108 | -47.95052 | 2024-11-26 04:36:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1caaddb7-568b-3445-9b39-e4123827a3e4 | -1.31071 | -51.74408 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 876e2178-ad59-32fc-81de-077708068c7b | -1.13261 | -48.33916 | 2024-11-26 04:36:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e4e6369-dbce-3f9f-81a6-01cb67fb8747 | -0.878 | -51.72347 | 2024-11-26 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c41ef8c7-d8c8-3566-b102-ba465dd49da1 | -0.75484 | -47.27527 | 2024-11-26 04:36:00 | NPP-375D | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d19630b-3376-3a10-8587-1c15b69d0b95 | -1.13653 | -48.35741 | 2024-11-26 04:36:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87f25afd-a1a5-3e87-9fa7-8af6b5d040a0 | 1.8242 | -55.97362 | 2024-11-26 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa15165d-fe9f-3167-9d4a-4a2ecc123f0d | -1.06183 | -52.42131 | 2024-11-26 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dae2eca-1227-3218-8149-05eaa845f9b6 | -1.30097 | -51.73362 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1b35030-99b5-3464-8664-1e37a62ffe13 | -1.71694 | -46.21824 | 2024-11-26 04:36:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d05e0a3e-61ca-3b3b-9089-abb79bcd6359 | -1.56386 | -45.67797 | 2024-11-26 04:36:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c2c658b-742c-3916-806f-7f651ef4f3cb | -1.86924 | -44.7644 | 2024-11-26 04:36:00 | NPP-375D | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43654fa4-5387-36fa-838e-0bdc32e386b2 | -2.1874 | -45.60632 | 2024-11-26 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 250aaa48-bf35-30a7-9d2e-db99e997b799 | -1.60703 | -47.38602 | 2024-11-26 04:36:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66a0ea14-0434-33cb-9b59-5d5ff59a8a28 | -1.70937 | -46.2439 | 2024-11-26 04:36:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13132fdd-94f8-3375-a81a-339eaed92a45 | -2.32712 | -46.12617 | 2024-11-26 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README21.md)
