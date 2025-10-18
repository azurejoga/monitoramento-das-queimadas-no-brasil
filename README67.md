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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d49bcb4-f15d-37c9-b423-683ff0540ae3 | -8.10896 | -55.09012 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb926658-dc78-356b-8107-675e406bf3fc | -8.15732 | -49.29449 | 2025-10-18 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aefdc62b-da33-3a43-b320-7212712765ea | -3.15201 | -50.24797 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 302f5328-3711-3dec-b1e9-9266b28955ee | -7.75105 | -42.51783 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 041ce18f-5e7b-378d-a08b-8e0ce498b95e | -4.40136 | -43.44251 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b353db8-f7d9-3d90-b700-acaa92c8c36e | -8.6104 | -40.20434 | 2025-10-18 04:49:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 86b5b888-a700-3988-bc2c-c19ee4b96086 | -5.37617 | -46.00597 | 2025-10-18 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 028d4733-88bd-38ee-8c5a-6b3d2a440be4 | -3.84778 | -41.56776 | 2025-10-18 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f4f75fd6-a390-35a4-8d21-77a13e6b2fe1 | -6.77094 | -50.36158 | 2025-10-18 04:49:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cb14242-4bad-3b0b-8265-80e3589ee8e6 | -4.88114 | -46.70671 | 2025-10-18 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df8563e2-3d07-3c30-a2c3-4a382f2a8083 | -3.58991 | -43.04972 | 2025-10-18 04:49:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f129f3c0-9059-397e-888b-2c83d11b4f9e | -7.80454 | -54.93585 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b46e161e-5638-3058-b6c1-3b4668fb523d | -8.2431 | -44.01323 | 2025-10-18 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cf5e60b-2c0e-3cab-a324-b3195cd49c8b | -5.00823 | -46.02667 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a98337c3-85b5-39e3-8793-4b473ceb1823 | -5.20759 | -46.19648 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e4a52df-c40b-3e0b-a883-c8b1dffd3223 | -6.67579 | -58.7461 | 2025-10-18 04:49:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d87de4be-9664-3689-a305-bd62608f1046 | -5.17331 | -46.19122 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53ae684f-9c65-3713-aae3-139be10015a5 | -8.36581 | -46.26574 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 833eabb6-2abc-303d-bcee-8ea36d50ad90 | -5.92859 | -47.31989 | 2025-10-18 04:49:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5b49a74-6182-368f-a299-792fe20dd5a3 | -7.39441 | -46.97265 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf41d6e0-73cd-32c3-8544-be157f4e5f18 | -8.19976 | -43.31112 | 2025-10-18 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 939babe6-f335-33e2-9eb4-0c40902b2e93 | -9.24562 | -44.35073 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b1b9367-e671-33e7-9b43-8a4c159fc843 | -7.66607 | -44.62768 | 2025-10-18 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 458772d5-4861-3363-803f-0a12928c605b | -3.85942 | -52.23068 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93c3727f-3c75-331e-9e3c-cb8e65d847a3 | -8.5542 | -50.08054 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebe1c5f4-bdea-36ce-b300-753b6d8771e3 | -6.36333 | -58.2101 | 2025-10-18 04:49:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c29af63-02eb-3db8-b781-f3026cb01dd7 | -3.91054 | -52.3381 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f351114-9fd9-3da8-ae83-a1e10e5f322e | -9.7236 | -44.53975 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa2c64f0-026d-3db7-953f-9f1b5d18cbd5 | -5.30012 | -44.84851 | 2025-10-18 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87d8a959-43af-3fd1-88af-0762073f7f98 | -8.36197 | -46.24533 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 082ddfcc-f265-33ce-981b-0e116e579b0a | -6.31666 | -40.95265 | 2025-10-18 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7488e72f-c77d-378f-9b81-1f8315c4ade2 | -7.53536 | -50.41565 | 2025-10-18 04:49:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f1daf54-3aee-35d2-9c03-b7e85618154f | -6.3733 | -45.7793 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3388bc76-4d93-3828-b22e-24aadaa7ee97 | -3.24898 | -45.97321 | 2025-10-18 04:49:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e63f7c46-a55d-3faa-a04b-a4fc6e796a44 | -8.82558 | -50.05239 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6965aaa2-a24e-375a-9c48-6298fe533e2f | -9.71956 | -44.57024 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba1ed76d-608c-3c8d-9b6e-5d127596a632 | -8.82833 | -49.67955 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60a8c5f7-13ac-35a5-a07a-175b5d02d270 | -5.45516 | -45.41435 | 2025-10-18 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 39a01889-5aa2-3cc6-8aab-88e131b8ec17 | -4.44758 | -43.23489 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 46f5d8bd-cd81-30ff-98ae-3522c4512480 | -6.34702 | -45.75471 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 687a0267-c891-3d6e-b26e-6087e52aaed9 | -6.40609 | -47.21487 | 2025-10-18 04:49:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c97c870-a4df-3e50-a4e2-99d49b1ea861 | -6.97795 | -44.87295 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c543eedb-0dc9-34f4-9387-3c07864c8ef2 | -3.75794 | -51.28019 | 2025-10-18 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6469aaee-dc38-3629-a312-a8ba7b651a11 | -8.23331 | -44.00331 | 2025-10-18 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f37f8c2-c8ca-3d6d-a43b-cb1db229a648 | -7.7276 | -47.63788 | 2025-10-18 04:49:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2752158c-64ec-3f47-9a34-fe924273a2b7 | -3.39884 | -59.42612 | 2025-10-18 04:49:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcb6b46c-4042-3a5e-a79f-c2dda20964ed | -8.47653 | -44.18462 | 2025-10-18 04:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c30480dd-1110-332c-9e39-7576d070b161 | -8.24243 | -44.01424 | 2025-10-18 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 77807f00-aab5-3719-93fe-c5ce72d55794 | -6.14271 | -44.455 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 887b53a2-8675-37f2-a39c-f160e07d2891 | -2.96041 | -48.58927 | 2025-10-18 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 579b9d5d-12c3-327b-96fb-5557b7366e2c | -3.13853 | -50.24588 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07b3031b-2e13-35e9-b811-dffa07a2bebf | -6.99909 | -46.99228 | 2025-10-18 04:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb81cc30-073c-3f00-9833-a84d9d16a726 | -3.49139 | -42.73128 | 2025-10-18 04:49:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 69f64214-ccd3-3077-a1e6-23d6b9c04bf0 | -6.21226 | -55.66861 | 2025-10-18 04:49:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a7dac68-56da-3a32-9323-b4fdac77bfea | -4.45186 | -43.24195 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cc51a876-3fc3-31d9-a985-ff9d342cc16c | -7.44286 | -43.75895 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f308cf84-863f-3b99-a292-656f42a2534b | -6.46762 | -44.14024 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd1db254-eb08-3145-8157-6f19b5eb221e | -6.37153 | -44.70819 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5c26a15-bea3-3f17-90d3-fb7dcddea580 | -3.49188 | -42.72792 | 2025-10-18 04:49:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d5ddfbea-a00e-3f3d-8aeb-943bee727b38 | -2.87125 | -50.74018 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e8a844c-13c2-33d6-aab4-5df14f0efd17 | -3.821 | -51.69997 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a348f920-95e2-3228-9c2f-53602194bc89 | -7.58674 | -44.98575 | 2025-10-18 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee3b1967-2649-3270-acc5-7b16c502e40a | -8.53813 | -49.59972 | 2025-10-18 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 329ee824-f834-35d8-ab7b-a4861c60f070 | -7.85026 | -44.14328 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a571beac-2264-33c0-ad42-0411ea0d4be0 | -3.49718 | -42.72873 | 2025-10-18 04:49:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 138d0f14-23e5-303f-8e6c-6788c0a47867 | -7.49009 | -47.0326 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23cef747-34da-30f5-bbe0-883958d4554f | -7.34923 | -43.85674 | 2025-10-18 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6650c00d-ca84-3747-8da0-e7a53ad5ee6a | -3.34974 | -49.25213 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80506621-3e34-312c-98ee-906886d7ac23 | -3.85985 | -51.90635 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffb2b786-233f-379f-8a6c-bd79eaefbf9b | -6.60585 | -55.0124 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fe90dd6-b407-3f46-984e-0640e65fbe22 | -6.98944 | -45.20218 | 2025-10-18 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddf966ed-139a-3896-8bed-2659501c0703 | -8.54208 | -49.52196 | 2025-10-18 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 460d69c6-201f-381e-9586-c370b900ca88 | -5.01693 | -46.0276 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e0ce69b8-14f6-33c8-85be-fd1594ef7a6b | -3.47119 | -50.02285 | 2025-10-18 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2b6a207f-ae00-3c30-910a-3223139ef46d | -6.2605 | -44.342 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 71f8318f-8739-3395-8b00-2bfd660080a4 | -3.12896 | -50.21865 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1ec6bcb-0107-3898-9499-fd8cdd1d7ac9 | -8.36573 | -46.20308 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8018acd4-6c1a-39ba-bafd-0ef56ad95aac | -5.17207 | -48.60291 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbef26f4-7a29-3d51-8d88-eae6d54fb2f7 | -1.42094 | -60.40025 | 2025-10-18 04:49:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3512b078-d15e-3400-a3f9-212cb51cad7f | -3.80269 | -51.64425 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| da9c920d-0475-3f7e-922a-c0182f76108f | -8.19383 | -43.31379 | 2025-10-18 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c2637627-ed1b-31e3-8ed1-27e53691c2f4 | -5.90933 | -44.76297 | 2025-10-18 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d552f236-8212-39cf-91e8-3969aff44f1a | -6.2597 | -44.34059 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bd89efe4-e1ad-3054-bdba-37e5f7765f24 | -5.99684 | -43.12302 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 46842336-2af5-3600-acbe-bf538aed2867 | -5.72047 | -49.31759 | 2025-10-18 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb7b240d-a231-3882-8fb1-d726cbf184f5 | -5.73592 | -47.476 | 2025-10-18 04:49:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed248cb2-bc44-3528-9a1e-e6b01685e21e | -8.44138 | -44.17149 | 2025-10-18 04:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42b73867-5ccb-3447-894d-f73db40c69b1 | -3.14096 | -50.45053 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68988f2c-04e3-35ac-a03d-d7a9a331f5af | -4.93729 | -47.3013 | 2025-10-18 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a2f78f7-811f-376a-bd35-d2fb2d997167 | -2.68596 | -55.76413 | 2025-10-18 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2aedace-4f33-30a9-b241-17f97de9562c | -1.9422 | -56.85391 | 2025-10-18 04:49:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b99b439-d812-30cd-bc91-6c4bb3b46e71 | -8.87685 | -47.97039 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54783a13-781d-353f-97c1-2356daab0627 | -7.01421 | -55.26252 | 2025-10-18 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f79c8962-67df-324e-96a8-cd125be99d0b | -5.58236 | -44.18335 | 2025-10-18 04:49:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c660909e-da7d-337e-a7eb-b5c806086639 | -3.06506 | -43.21513 | 2025-10-18 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b302de8-39e9-32ef-aa4b-2466215d0971 | -2.80762 | -48.66275 | 2025-10-18 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b72c6c2a-964c-349d-8068-67f9956611c2 | -3.9495 | -52.22049 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69ce7301-e07d-3ee2-a1a9-8eb6b15ce613 | -8.60445 | -40.19769 | 2025-10-18 04:49:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 604cda0f-9e0c-30e6-bba3-13281847c49d | -9.11799 | -46.61995 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d398b250-e7b9-3f9f-8cc7-cca39cd0e564 | -7.79859 | -54.9352 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README68.md)
