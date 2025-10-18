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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56c1ae63-e4ec-32e9-9e4f-a9fe612ab402 | -11.204 | -47.8318 | 2025-10-18 02:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| ff6f230e-9e4a-32a9-874d-d40a92001244 | -11.6109 | -44.0678 | 2025-10-18 02:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 224d4dc8-469b-3904-aaf7-998f4b1246ac | -10.5128 | -43.4525 | 2025-10-18 02:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 383f689e-11de-347a-a4a7-e0a46b980254 | -11.6104 | -44.0913 | 2025-10-18 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| cc19782f-371c-3a10-8333-3ac0f47a2627 | -13.4663 | -43.7617 | 2025-10-18 02:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 3cafdcbb-6d9f-3cf2-b802-126ea5d16774 | -8.6223 | -40.1809 | 2025-10-18 02:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 84.2 |
| cf7afc4a-85ed-3872-9b4c-2a41faca2711 | -10.1718 | -44.5264 | 2025-10-18 02:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 42fc8eb3-b03c-3c7e-a674-6b6bddc252e0 | -13.2296 | -43.9692 | 2025-10-18 02:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 4a6128f3-c950-3228-9252-68f03b296f3e | -10.1528 | -44.5289 | 2025-10-18 02:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7f3daedb-3162-3d68-b1b4-2164d27a429c | -6.5259 | -44.9114 | 2025-10-18 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 956.3 |
| 0b7b339a-fffc-3efd-a73c-8b5f56b80982 | -5.0214 | -46.032 | 2025-10-18 02:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 990f40dc-2602-3211-ab49-3ece218c5f77 | -6.5261 | -44.8887 | 2025-10-18 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 629.4 |
| 61ded7df-c9bf-3840-8bfb-6ba0fb71e97a | -4.4445 | -43.2397 | 2025-10-18 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| bdc24834-25b0-3557-b295-46e2ca7aa8f6 | -6.5071 | -44.913 | 2025-10-18 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 213.6 |
| 49a8d64c-9411-361d-9fbe-23f0f94aaf0e | -4.0007 | -45.5054 | 2025-10-18 02:10:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 10bd04e9-004b-3f5c-8d7d-4555cf993e6a | -12.5944 | -52.8223 | 2025-10-18 02:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 110fd0d2-a5fe-3526-9ed9-95b70302a200 | -10.4937 | -43.4552 | 2025-10-18 02:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 29098acb-2603-3e9d-b87a-7f71ec89e743 | -6.5074 | -44.8902 | 2025-10-18 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 149.0 |
| a3e5db09-54d4-3bde-860e-9c31a5c218e1 | -15.038 | -46.6041 | 2025-10-18 02:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 7e6ed6eb-c0eb-306e-adc2-30ebc8ecbafe | -19.1114 | -57.5486 | 2025-10-18 02:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 66049adf-3783-37bb-8350-abd06a6633ed | -8.6032 | -40.1834 | 2025-10-18 02:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 186.7 |
| 63a40dc2-94a5-35f7-a473-324ec60df2bb | -4.4446 | -43.2164 | 2025-10-18 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 254cb25a-d6e2-3b0e-b978-fc9ebf50be07 | -10.4941 | -43.4315 | 2025-10-18 02:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 5193b247-65fa-393f-b512-8b133c7a8386 | -8.6029 | -40.2083 | 2025-10-18 02:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 113.2 |
| ba02f873-a267-35d0-80ca-05fb190654e2 | -5.0029 | -46.0108 | 2025-10-18 02:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 489a39a2-ff37-36eb-af55-bc7b605ed79e | -6.5257 | -44.9342 | 2025-10-18 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| f7ae11c6-28e0-3738-8e87-640376661b69 | -5.0215 | -46.0097 | 2025-10-18 02:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 5bc799b5-0825-3ec0-a01b-0d0986c07c9c | -12.6135 | -52.8202 | 2025-10-18 02:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 2ddbfe16-ecc5-32df-9f8f-42ef09571ca5 | -6.5446 | -44.9099 | 2025-10-18 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| e9f12b3f-7ed5-3125-82c7-82232a2e53db | -3.1616 | -50.2458 | 2025-10-18 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| d8420d49-a7b7-3134-9262-5ff279299b6d | -5.0027 | -46.0331 | 2025-10-18 02:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 2e4993e9-ae2c-356a-accb-7896c42ab1e0 | -18.3934 | -55.477 | 2025-10-18 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 1090f7da-82be-32ec-a3f2-95ae272d83d3 | -11.204 | -47.8318 | 2025-10-18 02:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| c3a969d6-c1ad-3e82-88b9-e67583bf2dab | -10.4937 | -43.4552 | 2025-10-18 02:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 357d7479-a28f-32cb-b027-803433a3d74c | -8.389 | -46.2333 | 2025-10-18 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 73980ff0-8a34-31c0-b5ff-7b5c4e07abf6 | -11.6109 | -44.0678 | 2025-10-18 02:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| c03de04b-aded-31d5-9970-0afdb826db67 | -6.5259 | -44.9114 | 2025-10-18 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 621.3 |
| 697b6ddc-ae86-325c-b2e1-ece6fb3a9b2b | -4.4445 | -43.2397 | 2025-10-18 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| a5a6c1d6-e460-3d5e-a6ae-c6928e7d9cd5 | -4.4632 | -43.2386 | 2025-10-18 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 7256d415-2f6b-3bf5-aab9-d5423f6397f8 | -6.5446 | -44.9099 | 2025-10-18 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| a9d6c9b6-4bad-34cd-9b03-ddf644aecdfb | -6.5261 | -44.8887 | 2025-10-18 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 515.6 |
| 7b179594-5303-3ea7-91f6-cc0df0339fe9 | -12.5944 | -52.8223 | 2025-10-18 02:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f7850d4d-50f9-3ca4-a087-94011f0768ff | -10.4941 | -43.4315 | 2025-10-18 02:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 03212057-2031-3f24-8053-fff7cacde919 | -3.1431 | -50.2464 | 2025-10-18 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 815819bb-fbf3-39e3-bdbf-4f19c496d031 | -5.0214 | -46.032 | 2025-10-18 02:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 148.1 |
| d73147cd-0053-3228-8760-1b04e28d0b3e | -6.5071 | -44.913 | 2025-10-18 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| b6b011c7-6103-390c-b7bd-782a1affa6ba | -10.1528 | -44.5289 | 2025-10-18 02:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 406ccfd7-d333-3a51-9c1c-7a837814eb8e | -8.6029 | -40.2083 | 2025-10-18 02:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 125.1 |
| 276e2562-5d28-32e2-85b0-778d05692048 | -5.0029 | -46.0108 | 2025-10-18 02:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 129.8 |
| b51a8d88-f2c7-3340-84a5-dd11953b3c60 | -6.5449 | -44.8871 | 2025-10-18 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 76ba6ba2-979d-38cd-b536-bfe47d31d868 | -11.6104 | -44.0913 | 2025-10-18 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b43988cf-df8e-396f-8440-04ecbf080753 | -10.1718 | -44.5264 | 2025-10-18 02:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| c97b41d9-4a80-36f4-9de3-8de462ccfbe0 | -5.0215 | -46.0097 | 2025-10-18 02:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 238.4 |
| d8e9e85c-ace1-35bd-b493-59112bfc4232 | -8.6032 | -40.1834 | 2025-10-18 02:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 146.8 |
| 76367ada-d989-3e4b-a373-24ff4f02eb0c | -6.5074 | -44.8902 | 2025-10-18 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 5bec90a1-4320-340b-9b6e-ca15cdc2e682 | -4.4446 | -43.2164 | 2025-10-18 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 3f644534-3d64-301f-9c4b-7458cfc53fad | -12.6135 | -52.8202 | 2025-10-18 02:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 67d6495e-b916-30de-89e9-509c84ce36bd | -5.0027 | -46.0331 | 2025-10-18 02:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 67da0934-adb0-3d09-8c4b-047cfc1861cd | -12.398 | -47.2056 | 2025-10-18 02:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 823b5dec-91a6-3b76-91dd-78ff008d15c8 | -11.6297 | -44.0884 | 2025-10-18 02:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 37b35606-0ebc-3151-96f0-963a1de3425f | -10.1528 | -44.5289 | 2025-10-18 02:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 36e96924-eae0-35d0-98de-0a225f1b3d5f | -11.6109 | -44.0678 | 2025-10-18 02:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 7e63f992-adb4-3ea8-9a1f-b6ad9716439b | -6.5259 | -44.9114 | 2025-10-18 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 4dfb133a-9a38-396b-a13f-fe88507960f4 | -4.4632 | -43.2386 | 2025-10-18 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 582cdae2-6089-3409-88db-eea6bbc1526b | -8.6219 | -40.2058 | 2025-10-18 02:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 35f9945c-cf5f-3bd2-9787-679c2cb6b952 | -4.4445 | -43.2397 | 2025-10-18 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| b85b3350-2ee7-31a4-83a3-24698f0b177a | -4.4446 | -43.2164 | 2025-10-18 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 5fb606be-3f8d-3603-b9a5-e088a9150e8e | -5.0029 | -46.0108 | 2025-10-18 02:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 92.3 |
| de962e13-b3fe-3bee-9ba6-56fae19fa6e8 | -6.5261 | -44.8887 | 2025-10-18 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 251.0 |
| 0ade9916-18dd-3dc1-87d3-b81377ce3702 | -11.5917 | -44.0707 | 2025-10-18 02:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| f9ba6078-8d3f-3960-a8da-378146e2939c | -10.1718 | -44.5264 | 2025-10-18 02:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c582baed-79b8-3210-ae38-fb9f6829b8ae | -10.4941 | -43.4315 | 2025-10-18 02:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 4c8b6acf-54f8-34e8-8ef8-dd6035fcb948 | -6.1368 | -44.4629 | 2025-10-18 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 4e0a787f-2188-3537-bb72-e3382c7516da | -13.4663 | -43.7617 | 2025-10-18 02:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| aae15cfc-7771-389b-aa54-e7b68f27c87a | -14.2577 | -51.8619 | 2025-10-18 02:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 711ba4da-dee9-3a0e-9d18-d18277e4f61f | -8.389 | -46.2333 | 2025-10-18 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 08710dfe-dfb0-3823-b851-9b7b3a269f69 | -12.6135 | -52.8202 | 2025-10-18 02:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 0cc3ecf5-e81f-3c1f-ba47-5c2f5326a382 | -12.6138 | -52.7993 | 2025-10-18 02:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e7a69b9d-f579-335f-a4d3-1aba280db665 | -6.5449 | -44.8871 | 2025-10-18 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 54f37439-0430-3d35-9968-5f6bd292d119 | -5.0214 | -46.032 | 2025-10-18 02:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 140.1 |
| ea940e79-16ba-3c94-afa9-0574b76c118c | -11.6104 | -44.0913 | 2025-10-18 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 148.2 |
| d43ebaf2-4336-3963-ae94-072be034b095 | -8.6223 | -40.1809 | 2025-10-18 02:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 76.5 |
| a816c846-f951-3125-80d9-a4c32755ee5c | -10.4937 | -43.4552 | 2025-10-18 02:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 2bc5b346-3f5e-30cf-b8c9-53833b4b623c | -8.6032 | -40.1834 | 2025-10-18 02:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 118.1 |
| 02669c13-2b29-371d-aaf8-bfbcde935064 | -11.204 | -47.8318 | 2025-10-18 02:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 4fad3071-9fb0-3796-92c8-ae4e0200abe1 | -6.5446 | -44.9099 | 2025-10-18 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| a2777b09-38d4-32cd-b9fe-fc79c1d3bfcb | -10.9564 | -45.4579 | 2025-10-18 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 88a96273-da9b-35e3-97f9-ed8ac555bec1 | -8.6029 | -40.2083 | 2025-10-18 02:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 112.1 |
| 10ce79b6-99b3-33b5-9b93-e8470b56a53e | -3.1431 | -50.2464 | 2025-10-18 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| c0002dc7-d069-31d3-95d7-147fd89ad042 | -5.0215 | -46.0097 | 2025-10-18 02:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 239.7 |
| 66838c6e-3718-30af-a3f3-4aab4f671b40 | -5.0027 | -46.0331 | 2025-10-18 02:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 932552ea-b342-3075-9984-7f9295464462 | -11.5917 | -44.0707 | 2025-10-18 02:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 39cfe931-dd76-350f-bd6a-c2377c1da1a1 | -11.204 | -47.8318 | 2025-10-18 02:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 5030b02b-a7c1-37b3-a84c-6a9741732d74 | -12.6138 | -52.7993 | 2025-10-18 02:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| a13dd58a-eb44-3a26-8a8b-f51e94c45cb4 | -5.0029 | -46.0108 | 2025-10-18 02:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| ae0c1527-9da0-3dd3-8509-3a6d50b34aee | -5.0214 | -46.032 | 2025-10-18 02:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 3abba57b-75a2-3bcd-b1f2-66e0137da650 | -8.6029 | -40.2083 | 2025-10-18 02:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 0c30481e-ff56-3875-8807-f026b4334eeb | -5.0027 | -46.0331 | 2025-10-18 02:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| aa9bfc00-6196-3032-ae47-4df617c8a448 | -10.1718 | -44.5264 | 2025-10-18 02:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 631d0f22-3396-33d6-9993-ba0fc1be5c65 | -10.4941 | -43.4315 | 2025-10-18 02:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 160.9 |


[Clique aqui para ver as próximas entradas](README10.md)
