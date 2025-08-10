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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c3d26e6-4adc-3bb4-bb4d-c928355d2bf8 | -7.0799 | -59.1964 | 2025-08-10 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 26ff2451-8d1e-3ad1-a0e9-97f663208fda | -8.9399 | -60.7481 | 2025-08-10 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 171.1 |
| 542c6d6c-c7d8-3302-9ed6-6502d3683447 | -9.3622 | -61.5133 | 2025-08-10 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 8e7d2437-cdd5-3195-8a71-ee7ba3011549 | -8.5792 | -54.6758 | 2025-08-10 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 67cd64a3-682d-3504-ad87-faa56ffff08d | -9.3808 | -61.5124 | 2025-08-10 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 655f2319-250a-36f3-a7c3-f371bf9c28e7 | -8.9398 | -60.7673 | 2025-08-10 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 1151c810-0a8b-3c55-b3e3-ac111fc676c8 | -8.9213 | -60.7489 | 2025-08-10 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.1 |
| ae21d778-0f91-33c1-bbe1-83f2133cf138 | -9.362 | -61.5324 | 2025-08-10 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 145.6 |
| f81e9083-77e0-364d-b2fe-ed4636a0d3a2 | -8.5605 | -54.6771 | 2025-08-10 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 0cddd1c8-e414-3ffd-bf95-7e91fb753ea1 | -8.9401 | -60.7288 | 2025-08-10 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| bd358eb3-5632-3d1c-9cf9-ca3f93703146 | -7.0615 | -59.1779 | 2025-08-10 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 0b44f024-6371-34e4-97a3-5b3b6b385910 | -9.3806 | -61.5315 | 2025-08-10 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 168.5 |
| 3e6eb9b1-a9ae-3c60-a6c3-91bb0373f53f | -8.9215 | -60.7297 | 2025-08-10 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 29b229ec-d682-3fb3-9874-0626cdf3fa2a | -8.9401 | -60.7288 | 2025-08-10 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| da97d65d-cbc6-35ae-a641-95278dbaf855 | -8.9398 | -60.7673 | 2025-08-10 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| a33e6843-a76c-3695-a4c5-cfb1e9dc3637 | -8.9399 | -60.7481 | 2025-08-10 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 47df410b-22ec-3d90-b2c4-746e85d38273 | -8.9213 | -60.7489 | 2025-08-10 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| fb330190-35cb-3766-b34d-42becaf75903 | -16.393 | -42.5379 | 2025-08-10 02:40:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 3373b294-ba1d-3d2f-a430-3fe45459c16a | -9.3808 | -61.5124 | 2025-08-10 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 26633977-b0be-339c-8b31-cbe5892b306a | -9.3622 | -61.5133 | 2025-08-10 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| ae897e5c-f851-379a-aabf-38516e4e54e9 | -9.3806 | -61.5315 | 2025-08-10 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 138.3 |
| ad89d7f4-db8c-344d-ac1d-02d724a3cc60 | -8.5604 | -54.6973 | 2025-08-10 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 04aabfc6-3463-34ea-94e5-91c48e688ef7 | -8.5605 | -54.6771 | 2025-08-10 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e8567638-efb9-365b-8652-ef451082479a | -8.9215 | -60.7297 | 2025-08-10 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 4cd8a2cb-b79a-3569-9ec6-07a270f027ff | -9.362 | -61.5324 | 2025-08-10 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 168.0 |
| ad98f5ee-6297-366b-a1d3-9eeb423b0381 | -9.362 | -61.5324 | 2025-08-10 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| ceb21ee7-4485-34eb-893d-99fd9bcbeada | -8.9399 | -60.7481 | 2025-08-10 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| f48539e7-a95f-39f0-99ab-ff7265a52a7e | -9.3806 | -61.5315 | 2025-08-10 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 170.6 |
| 44ead64a-eb62-35e4-8aff-133808876219 | -8.5605 | -54.6771 | 2025-08-10 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 750b1e99-df00-3ed6-9f95-ed248426e61e | -9.3622 | -61.5133 | 2025-08-10 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| f72e1246-caa8-3448-adc0-3d4d7ccc9589 | -8.9213 | -60.7489 | 2025-08-10 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 36478c60-c72c-3274-87bf-153815b1dd4d | -9.3808 | -61.5124 | 2025-08-10 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 483c6479-ab17-39d1-a686-4b267b9311d1 | -8.9401 | -60.7288 | 2025-08-10 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 349c7ebe-0676-3f78-918a-2162ce689204 | -8.5792 | -54.6758 | 2025-08-10 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 23404f1a-78cd-3840-928c-d76171ab97d9 | -8.9215 | -60.7297 | 2025-08-10 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.3 |
| a306003b-b803-39c2-8ad1-25c39aa3f753 | -9.3622 | -61.5133 | 2025-08-10 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 9e2bef11-942a-3b5e-97aa-93e9ffe96503 | -8.5605 | -54.6771 | 2025-08-10 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 65fd3b93-3fa3-3913-81a9-e01e3bfbe244 | -9.362 | -61.5324 | 2025-08-10 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 150.6 |
| db6fc7a7-46e4-3e80-ba8a-ec516df53789 | -9.3808 | -61.5124 | 2025-08-10 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8d77d35f-14c7-36c5-93fe-2052dc7b5463 | -8.9399 | -60.7481 | 2025-08-10 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| e85302b6-2b40-387d-a22a-299e7c063f80 | -8.9401 | -60.7288 | 2025-08-10 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| f445a719-1947-377d-bd11-ebc72066f686 | -9.3806 | -61.5315 | 2025-08-10 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 145.2 |
| a8c0d408-2973-3829-a3b1-3f4e56a3ecc4 | -7.39172 | -39.67979 | 2025-08-10 03:04:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c3fe63d7-a2bd-3c83-82d3-fb5b01b85542 | -5.34671 | -36.13474 | 2025-08-10 03:04:00 | NOAA-20 | JANDAÍRA | RIO GRANDE DO NORTE | Brasil | 2405108 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1b36a1ec-a1eb-371e-9728-9c6202185719 | -5.34597 | -36.13898 | 2025-08-10 03:04:00 | NOAA-20 | JANDAÍRA | RIO GRANDE DO NORTE | Brasil | 2405108 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a4bd3bfe-1427-3523-8350-0d0034d0446e | -12.57655 | -41.28564 | 2025-08-10 03:06:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 75a0cfbf-131b-39d8-a47e-4eb76ad916e8 | -16.36726 | -42.54212 | 2025-08-10 03:06:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 84c18478-8f39-34d8-a1dd-9f40bbf47a36 | -16.37291 | -42.54972 | 2025-08-10 03:06:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e5e193e7-3723-3af8-bab4-a745634e0f75 | -16.36945 | -42.54798 | 2025-08-10 03:06:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8f05357c-59fb-3b28-9ab9-64b390d79359 | -16.368 | -42.55435 | 2025-08-10 03:06:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e3570e7-903b-3dc1-8dfa-c8b6970d9959 | -16.38309 | -42.53794 | 2025-08-10 03:06:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a2627c56-2538-3c5c-b314-99e98f739d5c | -16.3709 | -42.54161 | 2025-08-10 03:06:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 859018f7-95e2-3280-9f0a-7fb7aff54a09 | -16.37592 | -42.53682 | 2025-08-10 03:06:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c066a4c3-a74e-3977-86c2-940234d74039 | -16.37443 | -42.54322 | 2025-08-10 03:06:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2b896bf4-d94a-38f1-acca-e548e6669530 | -12.57108 | -41.27686 | 2025-08-10 03:06:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| da2cbc84-c2f7-3733-b553-33ea20e49b1c | -16.37232 | -42.53534 | 2025-08-10 03:06:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a6d704d8-c097-3ea0-aac4-d28195d748c6 | -16.37738 | -42.53055 | 2025-08-10 03:06:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d3d5dc6c-835f-37cc-8f96-a6e1c410b06a | -12.56952 | -41.2841 | 2025-08-10 03:06:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7e5d79aa-4b28-3433-bbaf-1a5b18655811 | -19.40405 | -43.35442 | 2025-08-10 03:08:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21590284-6434-35e9-b886-0a33de685b86 | -18.55947 | -43.43946 | 2025-08-10 03:08:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 087eb393-7c12-3a2d-a269-a3fa5003b7fc | -19.40238 | -43.36139 | 2025-08-10 03:08:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 613457ab-0f23-3819-bd24-1286684c284d | -18.55255 | -43.43696 | 2025-08-10 03:08:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4080db44-4fa8-30ed-a05a-b96863ce77f3 | -17.51303 | -41.73729 | 2025-08-10 03:08:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e10c5b20-1c22-36d5-9fff-c882f656c962 | -8.9399 | -60.7481 | 2025-08-10 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 67ec858f-ffdd-3113-899c-34e193d7e2fd | -8.9213 | -60.7489 | 2025-08-10 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 180ca1d5-adcb-3bbf-875f-ef4eecdc4c36 | -9.3622 | -61.5133 | 2025-08-10 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 6f10122d-f87a-38ed-8dee-be988fdbfa9e | -9.362 | -61.5324 | 2025-08-10 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 00493775-d3ad-303a-82ae-3672c229a477 | -9.3808 | -61.5124 | 2025-08-10 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| cc669268-0133-3f19-8b9a-3ac4b1daa4e5 | -9.3806 | -61.5315 | 2025-08-10 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 167.3 |
| a2852fc3-3ad5-39c3-bd7a-247bd9626239 | -9.3806 | -61.5315 | 2025-08-10 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 157.0 |
| d6fd2642-31cc-3056-92fc-7b605e1e5f8f | -9.3622 | -61.5133 | 2025-08-10 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| ca1c74cc-2f5f-3655-a76a-becc5834a570 | -8.5605 | -54.6771 | 2025-08-10 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c87c6e64-dd6b-3554-9043-e852143200c2 | -16.393 | -42.5379 | 2025-08-10 03:20:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 52.5 |
| b15874a6-d575-387b-b11c-d4bce1a10dba | -9.362 | -61.5324 | 2025-08-10 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 035d9fa2-dd2a-3368-85b4-abcbc99ff870 | -9.3808 | -61.5124 | 2025-08-10 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| f12e006c-7293-3af8-b438-1d44d988e02d | -6.548 | -42.7547 | 2025-08-10 03:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 48.7 |
| f43fb68e-fc9c-3472-b5f7-0b9ba2e223aa | -8.9399 | -60.7481 | 2025-08-10 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| f31e3803-fa57-303e-ad64-c664b31a1588 | -8.9213 | -60.7489 | 2025-08-10 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 38dd3965-a8ff-376c-8dd5-d2ac9030ca93 | -9.3622 | -61.5133 | 2025-08-10 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 8528ce20-6bf9-3f0b-8269-664825a9cfff | -8.9401 | -60.7288 | 2025-08-10 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a08fbe3e-be07-3f40-942d-0473c9778804 | -8.9215 | -60.7297 | 2025-08-10 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 11eee22d-a981-3e2f-9cf7-5304ed913ddb | -9.362 | -61.5324 | 2025-08-10 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 168.8 |
| 38a14bf3-a494-3268-b9f2-c228fdf1a58a | -6.5477 | -42.7783 | 2025-08-10 03:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| ded51103-51a7-3224-b805-9fafb2b0c13a | -9.3806 | -61.5315 | 2025-08-10 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 131.7 |
| c3a8ece3-02ad-3068-b0c2-e442994bcf6d | -9.3808 | -61.5124 | 2025-08-10 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f6b8d87e-8cfc-36b5-a5eb-39e15441c517 | -6.548 | -42.7547 | 2025-08-10 03:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 51.2 |
| 91af60b0-137a-3768-9cbb-9aa8a3e73f63 | -9.3806 | -61.5315 | 2025-08-10 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 47605925-7729-3d14-a843-3e451a197184 | -16.393 | -42.5379 | 2025-08-10 03:40:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 12485d13-fee2-31fd-8f47-fc5f0393d624 | -7.0799 | -59.1964 | 2025-08-10 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 3c873355-e877-33da-8179-1b77cda0ce5d | -7.0614 | -59.1972 | 2025-08-10 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| bf4da124-dda0-3309-825b-0987042168bc | -8.9215 | -60.7297 | 2025-08-10 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f5f59b8b-554c-3bc9-8b26-7a0d5412a083 | -6.5477 | -42.7783 | 2025-08-10 03:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| 95954f8e-0b92-3d35-a82d-31cb646a4629 | -9.3622 | -61.5133 | 2025-08-10 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 3c7d4d0f-adc6-3888-874d-72adfa4ac538 | -7.08 | -59.1771 | 2025-08-10 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2ff8739f-1d6b-383f-9182-a58df5f0dffb | -8.9213 | -60.7489 | 2025-08-10 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 75bd9447-0605-3439-a987-e00568c6795b | -16.3731 | -42.5425 | 2025-08-10 03:40:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 73b7ec5b-dcfd-364f-89d3-7e5d9713d774 | -8.9401 | -60.7288 | 2025-08-10 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 6e79b5e6-8fd7-3088-b326-e98c373d5579 | -9.3808 | -61.5124 | 2025-08-10 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d1e3c65e-ac19-37f6-9464-b81ee25472cb | -7.0615 | -59.1779 | 2025-08-10 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 0b23f28e-e5e3-3c9c-829d-5e0bebd02ae3 | -8.9399 | -60.7481 | 2025-08-10 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 165.3 |


[Clique aqui para ver as próximas entradas](README7.md)
