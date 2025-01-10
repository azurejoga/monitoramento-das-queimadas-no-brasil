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
| 0c708c62-4438-3f1f-8ba0-97c2021b44d1 | -7.80044 | -35.16515 | 2025-01-10 04:18:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 14ff3d43-fdc3-393e-aa13-e10f0d749548 | -7.39416 | -42.77654 | 2025-01-10 04:18:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 14313707-f4ab-3b83-8f44-8428b97ba2c1 | -3.82991 | -45.35953 | 2025-01-10 04:18:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6a4ac2b-3aa3-3239-8a47-1bffdf4db8ba | -7.80461 | -35.16588 | 2025-01-10 04:18:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1a4eda73-2dcc-35d2-82d5-74b044445601 | -9.87555 | -36.30035 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 43a7b701-2626-3858-81fc-f63333163461 | -7.53438 | -35.29934 | 2025-01-10 04:18:00 | NOAA-20 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 447143fc-810b-3351-bd71-db20e33fff61 | -9.87872 | -36.29214 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| ec3f879b-e6b6-37a3-baa9-b38e737656bf | -7.53387 | -35.30305 | 2025-01-10 04:18:00 | NOAA-20 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3c288a34-e280-39a5-9eb6-347dcc5ebcd1 | -8.42497 | -35.23822 | 2025-01-10 04:18:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ee116a9a-e037-3530-9126-66bb4b2da697 | -2.79469 | -54.17286 | 2025-01-10 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd726ef1-ef54-35e4-a226-6b2c36a2d4fc | -8.42336 | -35.23615 | 2025-01-10 04:18:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a96c876c-974e-3ce7-81fe-93dd6988b28d | -9.88132 | -36.29768 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 196893a3-01a9-3161-982f-64663c1442a2 | -8.42445 | -35.24205 | 2025-01-10 04:18:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| dd0cd53a-3cc7-3b63-9626-189f796a5cf6 | -8.41932 | -35.23772 | 2025-01-10 04:18:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a2ce871e-53dd-3759-82ee-8db86a1e3524 | -7.52841 | -35.3018 | 2025-01-10 04:18:00 | NOAA-20 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c5885dfe-70e9-3e79-b6b9-86c462db1251 | -9.8809 | -36.30107 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 24904c2f-564b-38a5-b5f4-55e7c8a9ced6 | -7.79992 | -35.1689 | 2025-01-10 04:18:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 049d2892-9d9b-30b4-a563-a52ae2919017 | -8.41881 | -35.24148 | 2025-01-10 04:18:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6e035a11-7a8c-394a-8ea9-2b1d7dedf53f | -9.87292 | -36.29482 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| c6ebe111-a834-392b-9e22-477bdfda8096 | -8.42287 | -35.24 | 2025-01-10 04:18:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 6d6864ad-93f5-37ea-97bb-b686be3eb856 | -9.87684 | -36.29015 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| ebe7eb17-e0f6-363a-b2df-edd59d78b30f | -9.87827 | -36.29554 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| d1f89e33-2d43-3112-8737-0549a1462817 | -2.6619 | -54.83144 | 2025-01-10 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77523997-0268-3adb-9238-9a4b9543168c | -9.87781 | -36.29892 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| dac560a9-60c5-3c14-815b-122c6fd90195 | -9.87641 | -36.29354 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 29069631-fac6-37e0-9473-6116467638a1 | -9.87598 | -36.29694 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 463da176-f38a-3288-8a53-4c2c7f272735 | -4.77441 | -38.55199 | 2025-01-10 04:18:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e60619f-b1f7-33d6-a035-55afd2869248 | -3.09844 | -54.59846 | 2025-01-10 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a67adfad-b23d-38ef-8832-d5ff4d6f1ee4 | -2.66116 | -54.83593 | 2025-01-10 04:18:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff79562d-48e9-3780-b4e7-e4ec9055f876 | -9.88361 | -36.29625 | 2025-01-10 04:18:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 29eeee4f-d4e4-3354-bac9-0e0361e81ce4 | -9.8725 | -36.2972 | 2025-01-10 04:20:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 109.9 |
| 2fefe1fb-e237-3fca-b3bf-46d95d53d6b4 | -10.62599 | -37.06286 | 2025-01-10 04:21:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 769db224-6ac1-3d52-b68a-64a636940933 | -10.6256 | -37.06584 | 2025-01-10 04:21:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fbb16b1f-0293-3993-9916-0f63d8a50571 | -21.30637 | -52.06486 | 2025-01-10 04:23:00 | NOAA-20 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56232a4e-b5ab-327c-95b8-202a261876ab | -19.20688 | -50.52652 | 2025-01-10 04:23:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e382a28-4389-3305-b5a7-a507505ea4f4 | -21.30912 | -56.0292 | 2025-01-10 04:23:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4dedaefc-606f-367d-ba08-db2b094699f2 | -23.59161 | -47.44022 | 2025-01-10 04:23:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 03971064-4762-3087-9010-a3bda24d8301 | -17.65865 | -54.17308 | 2025-01-10 04:23:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e918aaa8-d989-37c2-bed8-979284a86e49 | -21.40195 | -48.66198 | 2025-01-10 04:23:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4617bfc3-10e4-365c-b757-836bf927e96f | -21.56626 | -54.20512 | 2025-01-10 04:23:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e23d4df-52fe-32fa-8245-872f71d623f7 | -29.2044 | -51.50281 | 2025-01-10 04:23:00 | NOAA-20 | GARIBALDI | RIO GRANDE DO SUL | Brasil | 4308607 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1436992d-59a1-3769-957a-8e520aa01bad | -23.35201 | -48.52586 | 2025-01-10 04:23:00 | NOAA-20 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4ff6d881-44df-3cb1-8527-64392f274f8e | -17.65954 | -54.1685 | 2025-01-10 04:23:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99e68678-53e2-3e4a-9cc3-f9c0c778dce8 | -20.87887 | -49.86766 | 2025-01-10 04:23:00 | NOAA-20 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e0875ea4-348f-3118-b2d1-59304bf50095 | -20.97817 | -49.77764 | 2025-01-10 04:23:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 245916ec-f3c3-3470-a69d-68fcc9243447 | -20.52915 | -49.60822 | 2025-01-10 04:23:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bbba7a3-52f9-300c-ba30-de3896721e5f | -19.31912 | -54.96228 | 2025-01-10 04:23:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbcf068c-984e-375c-9fc9-ef987a74eb9f | -19.31901 | -54.96147 | 2025-01-10 04:23:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1cc5676-a0af-3fe7-a817-4917fe96250f | -22.01342 | -49.1243 | 2025-01-10 04:23:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31c67fc9-8cdf-32d5-86f7-75c2ed9311ed | -23.35474 | -48.53022 | 2025-01-10 04:23:00 | NOAA-20 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| dc3e47f4-0ce9-3944-b2e1-ea79b7ac846f | -23.61084 | -47.54279 | 2025-01-10 04:23:00 | NOAA-20 | SALTO DE PIRAPORA | SÃO PAULO | Brasil | 3545308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 33cc7c78-135d-390e-ad00-991d0229f1e8 | -29.9585 | -51.17559 | 2025-01-10 04:23:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 0c793ed9-1148-3e5e-bb5e-35f94d602cc5 | -22.7856 | -43.75965 | 2025-01-10 04:23:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f57e3b66-45ef-323b-9987-5b744ff90529 | -20.76464 | -46.76976 | 2025-01-10 04:23:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e3d971ea-5755-369d-b68e-9a6d55b030bf | -22.5991 | -54.89059 | 2025-01-10 04:23:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d7717b97-be27-3114-9419-507876ecc467 | -23.10252 | -52.0977 | 2025-01-10 04:23:00 | NOAA-20 | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ec71e810-7171-38c2-a27b-5ab45d7e02ea | -19.47093 | -46.60603 | 2025-01-10 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 17ef4162-dfea-383e-8e2d-438901e03102 | -21.30552 | -52.06953 | 2025-01-10 04:23:00 | NOAA-20 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da6d6879-37a8-3f01-8ed7-f408cfbec4dc | -23.98326 | -48.91786 | 2025-01-10 04:23:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28bf4364-de57-33ea-a542-8fc4c2f8f2c7 | -19.01982 | -57.62489 | 2025-01-10 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7d095013-df73-3998-af3b-1b2c29962b62 | -20.309 | -45.58436 | 2025-01-10 04:23:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebfa9a14-559f-317d-b442-6eb2d3444222 | -20.87822 | -49.87155 | 2025-01-10 04:23:00 | NOAA-20 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4c5e9386-fd70-3694-8c1f-3b7f3626b87c | -20.97882 | -49.77376 | 2025-01-10 04:23:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 896a88ad-4c95-3ad5-b276-3ae96cecd5d0 | -22.01403 | -49.12056 | 2025-01-10 04:23:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| abc84bb1-2205-30e2-b128-724c5f21a3da | -22.67652 | -42.85355 | 2025-01-10 04:23:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0a10d679-3856-3793-b7d5-906bd7a00a57 | -20.29993 | -55.69812 | 2025-01-10 04:23:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3121dd4c-7b60-37b1-89a1-4b93a192f55d | -20.97543 | -49.77311 | 2025-01-10 04:23:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a7913b71-0ca7-34ed-acfe-4b2487b3406e | -18.60584 | -55.49725 | 2025-01-10 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 556acf23-0f6c-3567-82d0-233ca26b376f | -23.02318 | -52.62531 | 2025-01-10 04:23:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 48edbc19-93f4-3ad0-9c15-fa616aa10788 | -20.98156 | -49.77828 | 2025-01-10 04:23:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| d11c86c9-fbbc-36e7-9104-95ac2c3605ee | -23.70407 | -46.47688 | 2025-01-10 04:23:00 | NOAA-20 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a0d141bd-697b-3f0f-9585-95fd9c0ded3c | -22.54848 | -47.25861 | 2025-01-10 04:23:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70753b4d-b674-3c6f-95e3-edf6e3e64e05 | -17.65511 | -54.16753 | 2025-01-10 04:23:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df3c0f21-c542-3f17-a52f-579c2e89c40e | -21.56212 | -54.20419 | 2025-01-10 04:23:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aef99c8e-b63b-3436-b876-1c35ed9c0f71 | -23.70615 | -46.47625 | 2025-01-10 04:23:00 | NOAA-20 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8ca35aa5-b5c7-3ac2-8aaa-96ebdda15267 | -28.83634 | -51.83254 | 2025-01-10 04:23:00 | NOAA-20 | VISTA ALEGRE DO PRATA | RIO GRANDE DO SUL | Brasil | 4323606 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ae0179a2-006b-315c-815a-96f317127a36 | -20.9822 | -49.77439 | 2025-01-10 04:23:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 06150113-68e1-3df2-a145-3e59dc38b7ad | -29.8265 | -51.88559 | 2025-01-10 04:23:00 | NOAA-20 | GENERAL CÂMARA | RIO GRANDE DO SUL | Brasil | 4308805 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| dc3d0d85-c2a3-3f85-bb22-50f32ddd1d18 | -23.35143 | -48.52961 | 2025-01-10 04:23:00 | NOAA-20 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 088562a4-a7b8-39ee-a877-85c298184f0d | -23.02494 | -52.62295 | 2025-01-10 04:23:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 669a5cbb-b541-3762-afa7-81d6369e3823 | -21.30267 | -52.06414 | 2025-01-10 04:23:00 | NOAA-20 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad1ec541-b476-302a-9bea-b5f0d7bbe9c7 | -20.301 | -55.69283 | 2025-01-10 04:23:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e232531b-a00f-34e9-9649-48c9b4030fb8 | -17.65421 | -54.17213 | 2025-01-10 04:23:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 983ec7d0-b47d-3cc2-b95a-c59e548187ed | -22.67605 | -42.85749 | 2025-01-10 04:23:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7331f3bb-76a2-3d3f-9009-b28c3bab273f | -21.1937 | -44.93645 | 2025-01-10 04:23:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0ba9dd53-2d11-3fe4-aabb-6fe26bb2b195 | -30.37393 | -56.16107 | 2025-01-10 04:25:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 0307de16-9800-34a3-b0a4-21b10e126fe9 | -31.35346 | -53.19032 | 2025-01-10 04:25:00 | NOAA-20 | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| a30c5cbc-f2db-3922-bca6-4fcb46ff60f3 | -30.36878 | -56.16597 | 2025-01-10 04:25:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 3ef4094e-f1a2-30b2-9238-e5638708fe7c | -30.11315 | -52.08176 | 2025-01-10 04:25:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 190624a8-7968-3a97-8e43-fc1db25cbb88 | -30.46062 | -56.39835 | 2025-01-10 04:25:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| c8ad8237-7292-3aaa-b983-7f514f2e2072 | -30.35744 | -54.2654 | 2025-01-10 04:25:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 48e25f3c-1d80-3687-8aed-254511b3d4b4 | -30.37787 | -56.16212 | 2025-01-10 04:25:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 83b4aec8-0b9c-3001-8614-185d658d0a30 | -30.55502 | -52.88494 | 2025-01-10 04:25:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 42a69716-8ff0-3b35-9944-f334dd771b4b | 4.13403 | -61.0184 | 2025-01-10 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c69a0a26-19f1-3b28-be54-ba4124022d85 | 2.84864 | -60.64171 | 2025-01-10 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9c65500-c191-3d54-af56-0fd275793e85 | 4.85313 | -60.52993 | 2025-01-10 05:08:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e4e0857-8048-3d01-a1a7-f22887483ac4 | 4.13463 | -61.02245 | 2025-01-10 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fec439c-086c-3ca5-807c-7a32c54cb315 | 3.39024 | -60.20255 | 2025-01-10 05:08:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bec562d8-b095-3289-aec5-716e1178c2df | 2.36641 | -60.15597 | 2025-01-10 05:08:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26ab9142-1409-39a4-ae78-0967cf3044cf | 2.56507 | -60.6951 | 2025-01-10 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README5.md)
