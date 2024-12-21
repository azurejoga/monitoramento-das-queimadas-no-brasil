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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 259fcb90-07ad-3696-99dc-ebe57268b1b3 | -1.87946 | -45.55443 | 2024-12-21 03:53:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d3f73c4-4ada-31c7-b5a3-6d150967c7df | -4.24666 | -41.92256 | 2024-12-21 03:53:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7036e15b-cb06-3668-ab97-652b7ff894ad | -4.57338 | -46.7551 | 2024-12-21 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8076a4a-687d-35ca-a2c5-01e3cc79389c | -1.56324 | -46.78152 | 2024-12-21 03:53:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2629e4ba-0194-35dd-9db0-15400ea4c6a7 | -7.32027 | -39.98467 | 2024-12-21 03:53:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5030e1c3-2e65-362f-a2e5-8ef67c2d571c | -1.86839 | -45.55872 | 2024-12-21 03:53:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bb30e70-81aa-3184-953d-81b0d970503e | -5.11144 | -43.32007 | 2024-12-21 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d18fd0f-a126-3167-a0ba-03a551c65422 | -7.84447 | -38.41865 | 2024-12-21 03:53:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 80fe3f8c-f50c-3131-a1eb-3c3b2f7f3edb | -2.67717 | -46.91868 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c945934e-c692-3f91-b8ca-e3029a7bf666 | -1.99483 | -44.53616 | 2024-12-21 03:53:00 | NOAA-20 | CEDRAL | MARANHÃO | Brasil | 2103109 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71c0f93e-cb64-314c-b202-41ffb185b6cc | -3.30878 | -42.26866 | 2024-12-21 03:53:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d1751cf-8567-395e-a0b8-8979a5a41dac | -5.91541 | -43.48219 | 2024-12-21 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| af65a822-c7e6-3ada-af86-f77e1b8e05f4 | -5.61788 | -35.3555 | 2024-12-21 03:53:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fbb74c17-ca44-3b1c-be47-e421606793fa | -5.37007 | -36.7203 | 2024-12-21 03:53:00 | NOAA-20 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3a876689-efe5-3460-b369-c64992ac02a1 | -3.24274 | -46.02449 | 2024-12-21 03:53:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3811aa66-1db5-3dbd-8585-86170b871976 | -5.11082 | -43.32376 | 2024-12-21 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92c9f6ec-53b5-3141-9f91-3645999553c8 | -1.87899 | -45.55741 | 2024-12-21 03:53:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 536e8390-c6c7-3492-a24b-501c36b0a9c7 | -2.84923 | -46.7337 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93216a31-0315-3b74-9fbd-51c12b5496cb | -4.85499 | -41.34855 | 2024-12-21 03:53:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c8b11063-bd37-31ee-95d8-dc22c017d621 | -15.38805 | -39.38733 | 2024-12-21 03:53:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 758cfb54-500e-3718-aafb-3995bd0453cf | -7.31631 | -39.98775 | 2024-12-21 03:53:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 17115c0f-ba5d-34d0-b2a0-46f5882910e6 | -5.43847 | -46.2902 | 2024-12-21 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f829f7d1-3224-3bd9-bd5f-6d39adbc8634 | -7.6872 | -35.25927 | 2024-12-21 03:53:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| e0581791-ccfc-3e52-bc8c-4434e2ae7f09 | -12.38733 | -39.37006 | 2024-12-21 03:53:00 | NOAA-20 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 33f32a70-778f-3eaa-8a13-23d9898e8435 | -8.87936 | -41.09879 | 2024-12-21 03:53:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 70558024-4c3c-3af1-bbf4-4b68174fa1c5 | -6.76038 | -38.09839 | 2024-12-21 03:53:00 | NOAA-20 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c105384e-d004-3cd0-a1d1-a02bdcc95e1b | -1.88404 | -45.55823 | 2024-12-21 03:53:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb94ec7a-a60d-3e32-88ea-076c33639ae3 | -4.57394 | -46.7518 | 2024-12-21 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26b4a9b2-5295-35b2-9b90-fa47f95ffaee | -4.30757 | -39.28492 | 2024-12-21 03:53:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f393e57e-d7ee-3165-9eac-ac2c114a9e1a | -3.9686 | -43.04385 | 2024-12-21 03:53:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66a81ab2-3f04-3f10-9456-c2832903ff02 | -4.92977 | -41.32466 | 2024-12-21 03:53:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f479d7f5-87c2-38fc-ae63-951cf9d18e6d | -12.92172 | -40.58619 | 2024-12-21 03:53:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 89226d9e-b88c-3e0d-a93a-cddd92eb4191 | -6.23041 | -39.28023 | 2024-12-21 03:53:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 08031a8a-ab15-3e27-99d9-5830022dbce6 | -7.89801 | -35.24516 | 2024-12-21 03:53:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3f17f164-6987-3c4f-aee4-665113096171 | -2.55226 | -46.88428 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cab849f7-e0d0-3fb5-a96a-54441a77d673 | -8.84239 | -38.76609 | 2024-12-21 03:53:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a0b9dd6-f640-3e2c-8486-5a77872518a2 | -6.41646 | -43.78291 | 2024-12-21 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b78fe088-f45d-380e-9738-fa7f09fc4bc8 | -5.93459 | -35.62675 | 2024-12-21 03:53:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0404e3f2-56bc-337c-b6a8-9b10f4365c67 | -11.00102 | -44.34453 | 2024-12-21 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad79802d-67f7-3d8f-b8dd-3e71fb9f8a5b | -3.29031 | -42.52923 | 2024-12-21 03:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f55907f0-c739-3def-b7ef-7106547cf253 | -2.44304 | -47.48636 | 2024-12-21 03:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f7fc94e-2a1b-3459-a6d8-dc493b8713b7 | -2.76196 | -47.39794 | 2024-12-21 03:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c19676f-bbb9-330e-8aff-b3d8d7381c0f | -5.17668 | -37.58725 | 2024-12-21 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 9256aa67-c0a5-3294-98e0-aeaec076e6ce | -3.24223 | -46.02749 | 2024-12-21 03:53:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36dbcdbd-441c-35a9-a160-7b7b7883944f | -2.55169 | -46.88781 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7b9ae8a-6050-39f9-b480-173bc8fd4b82 | -12.86036 | -38.36762 | 2024-12-21 03:53:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3a36cd0c-8f77-3f6a-8f1f-e6e4e34a961d | -6.20508 | -39.92061 | 2024-12-21 03:53:00 | NOAA-20 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c5789ea9-4c7c-354c-94f2-11ea31ad1a6b | -7.18497 | -36.62847 | 2024-12-21 03:53:00 | NOAA-20 | SANTO ANDRÉ | PARAÍBA | Brasil | 2513851 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5b095737-1087-38f4-b904-7e8f7b19f759 | -8.16608 | -37.68532 | 2024-12-21 03:53:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e5d0881f-5b1c-36f9-8ea3-8f0b9ccc0346 | -4.1364 | -46.4684 | 2024-12-21 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2495c01-130f-3b37-acc4-e3a391196642 | -1.56441 | -46.77429 | 2024-12-21 03:53:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 64d8247e-256c-3f69-9275-9e55f6c5ad75 | -5.57429 | -42.94159 | 2024-12-21 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c0ccd673-f61c-3c99-a23a-d536a5de2ea4 | -2.70541 | -46.14121 | 2024-12-21 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc765804-6fa4-37d6-a747-c588d6c991d3 | -2.55289 | -46.88513 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 813277aa-7ded-37be-8de0-8af4ed58888e | -2.54742 | -46.88425 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a4480ed-80cf-375a-8566-fce31c2ea2b8 | -5.93109 | -35.62621 | 2024-12-21 03:53:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 04eed29e-f9c0-3feb-beba-0d5af4f9d9a2 | -3.95231 | -46.41567 | 2024-12-21 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1a1917c8-f537-327b-b9e7-1f701bb7ff42 | -1.50686 | -47.27468 | 2024-12-21 03:53:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 80132590-cad7-34d3-b4a7-f242af6cb5f0 | -5.1756 | -37.59417 | 2024-12-21 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2fdca057-1e7e-35de-aabd-c9b5233cdf77 | -5.82299 | -39.21581 | 2024-12-21 03:53:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 7b96c219-aa9d-3d4f-8dc7-a0eab19270ce | -11.85785 | -46.95224 | 2024-12-21 03:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 267ed325-2ec1-3c05-a112-ee688bc39902 | -5.33059 | -38.0992 | 2024-12-21 03:53:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a3343d57-60a6-3809-b2fb-a3bc8f56190d | -3.31013 | -42.2665 | 2024-12-21 03:53:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d33b656-51e7-3c6c-8baf-4e914144f573 | -2.67411 | -46.93684 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5d92e51-732c-3cfc-89af-5e53dbaa0adc | -2.70235 | -45.57346 | 2024-12-21 03:53:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9d7124f0-b18d-3817-b804-eaefd1b83846 | -2.61419 | -47.46584 | 2024-12-21 03:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11e092f9-7a42-3c37-9b72-898b4db3088b | -3.09194 | -44.87611 | 2024-12-21 03:53:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b0d2808-cf7a-3450-ba73-2f2b1f94e6cb | -5.61435 | -35.35496 | 2024-12-21 03:53:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 23e613e8-70c3-38e2-8e26-2df3769bed73 | -3.90475 | -47.15947 | 2024-12-21 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 554ed513-d770-33b2-a8a9-ebc98d8e79bf | -7.68657 | -35.26355 | 2024-12-21 03:53:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 472c9fa8-23bb-3fda-80f6-1795d16dd45a | -3.99873 | -46.55359 | 2024-12-21 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3e41ff2-d5fc-3b53-9556-0239fa35b467 | -6.98424 | -40.00351 | 2024-12-21 03:53:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e43185d8-6461-3800-9d8a-94fbe801bbb3 | -0.8567 | -47.13739 | 2024-12-21 03:53:00 | NOAA-20 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7168bbea-f51b-3c2a-898c-ce54a0647063 | -14.91635 | -42.27924 | 2024-12-21 03:53:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3f4c331b-058b-3d38-9118-a56408456386 | -2.66922 | -46.93247 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80a22161-b739-3a98-a1ff-0cf6ca8a2945 | -1.87297 | -45.56252 | 2024-12-21 03:53:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab85ff11-fc7b-3413-895b-3152fa6c5508 | -1.56267 | -46.78508 | 2024-12-21 03:53:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2b2f1d0-310d-3fea-8e24-b5beb8cf3c2b | -4.24361 | -41.92421 | 2024-12-21 03:53:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3f0c239b-c9b9-3502-904e-7dd48422a29a | -4.1359 | -46.47145 | 2024-12-21 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf1a220e-68c3-3c38-aea7-cba18a6ef059 | -5.3667 | -36.71979 | 2024-12-21 03:53:00 | NOAA-20 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4737b1e1-bde1-38eb-a1cf-def5a17dac4f | -5.7657 | -35.57047 | 2024-12-21 03:53:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 63a59d04-7c98-315c-8320-cde29049dce1 | -4.85937 | -41.34463 | 2024-12-21 03:53:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c909a19-88ee-3542-be27-b0631a0126f2 | -2.50895 | -48.05996 | 2024-12-21 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4cceb7d-437f-31d7-9402-c658542bff30 | -4.58126 | -38.60595 | 2024-12-21 03:53:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a1ea4093-6fc6-3af2-9537-7b2929756a95 | -4.58162 | -40.31753 | 2024-12-21 03:53:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ff8f4f0-ff84-3ab8-9636-cb625aaf2773 | -4.00065 | -46.98975 | 2024-12-21 03:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b01a7b0-1a35-3a73-afcf-432e610d6379 | -1.80527 | -45.44288 | 2024-12-21 03:53:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82abc537-723c-32b4-a728-8799b757cf97 | -8.12264 | -38.76523 | 2024-12-21 03:53:00 | NOAA-20 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 0d10ac83-f117-3064-9d1f-d5385ec17054 | -6.21095 | -38.52533 | 2024-12-21 03:53:00 | NOAA-20 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4cdd0114-087b-3048-9f1d-c401e43275c8 | -5.24754 | -41.39818 | 2024-12-21 03:53:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| adf56e52-1563-3c21-874a-582158e7a97a | -3.24733 | -46.02837 | 2024-12-21 03:53:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d04961a0-5969-342a-b21f-f2434192f892 | -3.46006 | -42.01029 | 2024-12-21 03:53:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2c4b11c4-5a57-3d0a-8763-4e6cee8e2c50 | -3.99349 | -46.55276 | 2024-12-21 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2049dcbf-46d2-3024-87d8-3ee502d0553d | -3.0866 | -46.56733 | 2024-12-21 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67488627-e90a-3145-8a7f-f2d53a7036d9 | -5.81964 | -39.21527 | 2024-12-21 03:53:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 461f78ab-b16c-38d9-82db-638363b3e92a | -3.83525 | -41.56862 | 2024-12-21 03:53:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 15e71fb8-e0d6-3748-89a4-50f2918dba43 | -4.93204 | -41.33385 | 2024-12-21 03:53:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f3355d45-d7b6-3355-9453-8f2e3501e6a6 | -4.92612 | -41.32406 | 2024-12-21 03:53:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cb207dca-902a-3ca2-89e5-68cbe32988cf | -2.54678 | -46.88338 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8df98ec9-866d-3bd0-a8ed-860f440baac0 | -7.3254 | -39.97433 | 2024-12-21 03:53:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README5.md)
