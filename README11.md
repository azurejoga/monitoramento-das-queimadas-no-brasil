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
| 34abd91f-b63a-3a24-836f-9fb1368e6870 | -6.55027 | -44.47571 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 90f1c0f1-4384-31c5-b211-57cfe41e4f47 | -4.78723 | -45.33492 | 2025-08-18 03:53:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15098d31-bc58-3ed7-b6ad-4a2a6a0cee16 | -6.42402 | -42.49743 | 2025-08-18 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a9bb6e68-04a3-3428-af2f-63cfe2330ecd | -9.49073 | -40.37342 | 2025-08-18 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 106.5 |
| 6415de9e-c168-3d0a-b773-d07d56b50b7f | -7.54998 | -45.44565 | 2025-08-18 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a184d9a-8647-3c89-bd44-7b1d28f89fd4 | -7.55341 | -45.43464 | 2025-08-18 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f11b74d7-f47f-3446-9e0a-2232c0f8fdb6 | -7.14508 | -44.1963 | 2025-08-18 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 134342e7-82a9-3cac-b751-4ced5b7f021c | -7.50581 | -44.9858 | 2025-08-18 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d5b67455-adf0-32a1-a23e-a021504dc1df | -6.55709 | -41.81678 | 2025-08-18 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ba6f52be-857a-32f7-8105-d1bc1a046955 | -7.5182 | -45.46848 | 2025-08-18 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 00cbfaa8-254a-3125-a2de-6892de6a3df8 | -7.54777 | -45.43133 | 2025-08-18 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12084a28-1bde-3c4f-89f4-7f53f00f4f5f | -6.14963 | -42.70652 | 2025-08-18 03:53:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cedc36bb-44cb-33c4-9c41-2e70927448ea | -7.55151 | -45.43661 | 2025-08-18 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89e13698-9162-38b5-af12-fad41f2d6608 | -8.03455 | -47.68096 | 2025-08-18 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65d8785e-0208-325d-986b-7f39072c70af | -8.03511 | -47.67776 | 2025-08-18 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65ae57c2-d65c-3d13-9ece-92155cc3f97a | -8.2232 | -47.30101 | 2025-08-18 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85f92f32-c90f-3480-a97d-338cca989805 | -7.42484 | -44.90405 | 2025-08-18 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1141e2f4-470b-33c8-b78b-c9d6947499f2 | -8.21811 | -47.30026 | 2025-08-18 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b24a90ed-b7d6-333f-9529-1bb5eb32dd14 | -6.56516 | -44.46605 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f5908d90-2fdd-3290-9fd9-750ec368a517 | -6.55525 | -44.47241 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 723b8fbb-a19d-3dfd-8f86-338b0b26dea6 | -7.80116 | -45.16136 | 2025-08-18 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a028dfe2-6c7d-352f-9880-acfe813ee15e | -6.431 | -44.77419 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d5fb81e1-e317-3245-97aa-f0debe2c0a46 | -6.55883 | -44.47726 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a7d31bc-fc3c-3e80-89a6-95b23ebd2dab | -6.42515 | -44.78205 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca80305b-e55e-3664-8dd7-44e04f0bb7e3 | -5.98532 | -44.12602 | 2025-08-18 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3431b523-3746-37fe-834a-034611f0229f | -6.09576 | -44.59621 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 704a4c69-5943-3b41-8521-d1e360a31b5e | -6.1579 | -47.27665 | 2025-08-18 03:53:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fa6dd91-c7e8-3a64-a995-13abe235f35f | -6.08051 | -44.6066 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba47ba27-302d-3cb0-8084-d1a4dcf01770 | -6.05475 | -44.12496 | 2025-08-18 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be6727f3-e381-3aba-94f0-51838440d1bf | -4.91467 | -43.24234 | 2025-08-18 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e7498f71-c31d-3eb3-8e23-1afdf9345822 | -7.28198 | -43.68658 | 2025-08-18 03:53:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75b47442-19b7-3123-8cb2-c58af7a2b660 | -9.49325 | -40.3699 | 2025-08-18 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8872f113-685c-33e0-84fa-63e47dc7cbd7 | -6.10011 | -44.59702 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c96f87ae-8e72-3f2f-9801-5f8684503434 | -6.52398 | -43.42993 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 88cce8a8-aebd-3057-8b77-754f845805c5 | -7.1444 | -44.20024 | 2025-08-18 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 724c04dd-e2f5-3215-a508-75a5a52c811c | -5.10032 | -43.78883 | 2025-08-18 03:53:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 511d2400-6a9f-388b-9672-e0a81d86f8b8 | -7.42415 | -44.9081 | 2025-08-18 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7878426-81fc-3981-b353-a6d3b19f9979 | -7.3521 | -43.84167 | 2025-08-18 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f967680c-bc63-37e5-85d1-c375d5289f66 | -7.55181 | -45.44363 | 2025-08-18 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7e7dbbd-817c-3777-8587-ba3d266ced83 | -7.57103 | -45.16004 | 2025-08-18 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2495996-7f8d-3f7d-93b3-3294dc76bd99 | -4.77318 | -45.32029 | 2025-08-18 03:53:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34456641-00b0-3df3-a824-d0f373ffabf8 | -5.98372 | -44.10975 | 2025-08-18 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cde518bb-5a78-3644-9f3f-92ae2a027c3c | -6.56021 | -44.46919 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a7da4696-4d51-3c64-849c-956abbfb44a8 | -6.54792 | -43.02496 | 2025-08-18 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c5301b2-23f8-3f2f-b121-d88db919550d | -6.56805 | -44.47499 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 777010ab-4784-3672-9d44-9bc216d51239 | -6.67428 | -41.76522 | 2025-08-18 03:53:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5a82253e-9db2-3a54-9f99-2af499eb8e00 | -6.4288 | -44.78717 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d4ecf28-859a-3613-94cd-1590b77c1994 | -6.95314 | -41.73041 | 2025-08-18 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 43528123-1db6-3256-9bd8-eb9b52ab7595 | -8.4978 | -44.73709 | 2025-08-18 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62afc028-21d5-3f4d-9c97-c64245d3402c | -7.82721 | -38.41548 | 2025-08-18 03:53:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f0a571a-1474-334b-9fc3-44e20ec17fe9 | -7.01388 | -44.2785 | 2025-08-18 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9601a170-6a0d-394e-bcea-6a284221a1c8 | -5.3449 | -41.2568 | 2025-08-18 03:53:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4daae5d0-9c11-3d92-b0fa-1e44f73290ce | -6.55731 | -43.01467 | 2025-08-18 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 445ca7e9-0718-3d35-bcd9-a90f5ea374a7 | -6.42588 | -44.77774 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6099dac4-f3a9-306b-b125-9ad041fb4abf | -5.98993 | -44.09868 | 2025-08-18 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae4350a7-ea89-34d3-bc65-a680a3137290 | -6.43025 | -44.77863 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1303e7c4-9cd7-3d3d-bc51-f77a071ba78b | -4.77402 | -45.3276 | 2025-08-18 03:53:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5a7b295-b47b-3fd8-8635-623c0f43c08a | -7.286 | -43.68728 | 2025-08-18 03:53:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17d0cf76-9208-3d12-9b0f-22988a324b55 | -5.99417 | -44.09924 | 2025-08-18 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8c76502-baba-358b-a0ca-6661122e18fb | -6.63824 | -43.88767 | 2025-08-18 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a92ff699-f986-3dbc-a3f2-07d0bf8c03f3 | -3.58951 | -47.52856 | 2025-08-18 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65b8d4e5-27a6-33ac-a25b-aee23f7e5582 | -6.15786 | -47.27703 | 2025-08-18 03:53:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8722a84b-5dc6-3484-90d5-8a4745e6ad78 | -3.38365 | -47.61168 | 2025-08-18 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 679ffe98-1585-3e74-af14-04e121e6ac97 | -6.98446 | -41.62863 | 2025-08-18 03:53:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 75031fa4-d0d1-3c65-a7d1-77bdd86a98a5 | -7.42509 | -44.90673 | 2025-08-18 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d2b2630-4eae-3b7f-94b4-867add0b3c61 | -5.98241 | -44.11751 | 2025-08-18 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 737b2553-c176-334a-b4b4-af33589f29e6 | -5.98175 | -44.1214 | 2025-08-18 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee50897d-23a3-3a93-be15-049856b66f6b | -3.22053 | -46.81443 | 2025-08-18 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6aaf17c-6c4e-39aa-be52-800e4c1f5b58 | -6.15735 | -47.27987 | 2025-08-18 03:53:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b169b6c2-e292-3b2f-b051-0e3388f9b7ae | -6.39826 | -44.24936 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0520c37f-7848-38e5-9029-5e67e85a78b2 | -7.01806 | -44.27934 | 2025-08-18 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93603bc6-b6c5-3946-bf6f-5e042768aa76 | -7.547 | -45.43587 | 2025-08-18 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b9d578a-620a-3014-80bd-54dffb80ac66 | -5.7618 | -46.67095 | 2025-08-18 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2df535bf-c1d7-351a-a5e7-f04da0b566bb | -5.76129 | -46.67389 | 2025-08-18 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58085089-0c77-337b-bcab-8692dfff2f34 | -7.60882 | -43.82868 | 2025-08-18 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af861b59-0487-3e5d-bfec-cefba386256b | -6.52829 | -38.8121 | 2025-08-18 03:53:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2ac37aab-cf6c-3e67-830d-bfa5856cbedd | -6.87724 | -43.12313 | 2025-08-18 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8a75bb8-340f-33d5-9411-bb594a74368f | -8.23983 | -47.86135 | 2025-08-18 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17f68650-6c89-350a-8acb-f9a9318edb33 | -7.5489 | -45.43388 | 2025-08-18 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48fafdea-e919-3814-aac5-ab1ea7f853dc | -6.95563 | -44.23673 | 2025-08-18 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60a34222-ea21-3dd3-bf64-2100dcf442a7 | -8.10614 | -42.35219 | 2025-08-18 03:53:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d85c0339-69ff-36f7-92e9-720b7212b9bb | -4.21976 | -41.77028 | 2025-08-18 03:53:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0c0e78d6-ce40-35ea-b2d0-49f864d1b6fe | -6.82535 | -39.89314 | 2025-08-18 03:53:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ba107300-0de1-37bd-83a2-00ca4932f9d5 | -6.43318 | -44.78801 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 51140bc7-8357-3149-b868-f21f1e8dd1cc | -4.29969 | -48.06513 | 2025-08-18 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13cade5b-a770-3630-9323-686f07bbdb56 | -6.55953 | -44.47319 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 09ab7b90-3cd3-38a6-92f9-3e3fdd31d222 | -6.77943 | -41.53012 | 2025-08-18 03:53:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3860ff37-1ae1-3dfd-8f4b-7f16a58cb66f | -7.1968 | -43.96841 | 2025-08-18 03:53:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e7f35b6-1155-3087-801d-673a52129bd2 | -5.10452 | -43.78951 | 2025-08-18 03:53:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53655e3b-1a87-3fc9-8009-51cdf10404fc | -5.36823 | -41.22673 | 2025-08-18 03:53:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f59ccd55-bf32-320c-96b1-acbf04171765 | -6.5638 | -44.47403 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| af391589-8f73-3677-b944-c3794cff20f4 | -7.34865 | -43.83732 | 2025-08-18 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10b68856-e3aa-3b90-80d5-61edde41d6a7 | -6.9063 | -39.55261 | 2025-08-18 03:53:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 5940eb98-9c9f-3a16-a9f9-861759ac2355 | -6.09142 | -44.59534 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de95a8e6-886a-3b33-889c-dfae831f0ffb | -6.55456 | -44.47643 | 2025-08-18 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1ac42ba3-ab4f-31a1-8b13-02687b7f9754 | -7.5481 | -45.4384 | 2025-08-18 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8a94d88-bac8-3c4f-a613-1c751179eab2 | -4.77873 | -45.32826 | 2025-08-18 03:53:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c37ffab4-4d96-3cd3-a04f-992c27e775e4 | -5.99795 | -44.12852 | 2025-08-18 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 36b2d2b4-b106-3ec8-b32d-9246d7f29221 | -6.87961 | -44.65914 | 2025-08-18 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5762119b-6ae8-3793-8dda-51e47b9af0bf | -4.29403 | -48.06409 | 2025-08-18 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README12.md)
