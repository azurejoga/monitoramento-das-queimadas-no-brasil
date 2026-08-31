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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf1a9faa-0261-3062-b48e-b7e7c8938121 | -14.68815 | -54.90819 | 2026-08-31 05:38:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39634730-937a-3277-b3e1-37e945d57d6e | -15.6147 | -56.40249 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f636a471-f224-3641-8d2a-78485fed9a48 | -14.23624 | -52.85905 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aff07959-2561-3a90-8233-7d52739db248 | -13.96758 | -54.40031 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9177f04-3c15-312c-983a-5f45d419c7c5 | -15.02472 | -48.16652 | 2026-08-31 05:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6537af1a-38ba-397d-b2d1-9f27fcbfc4e5 | -13.45917 | -57.04426 | 2026-08-31 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5f39dac-a6da-345b-aa8e-0e1e80349a7d | -14.42754 | -56.27349 | 2026-08-31 05:38:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e1f69590-8944-3387-8166-1eec00e279eb | -15.63449 | -56.38773 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 847373ae-3cf6-3d58-beef-415fc32c1c8e | -14.58614 | -54.08235 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b833506-b112-346c-96b0-fa0550ab94c1 | -15.55463 | -56.28057 | 2026-08-31 05:38:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 989c4164-6a60-3d52-a568-adda6eff6270 | -14.57924 | -54.08738 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15bf5897-3872-35be-8a93-b5593e3eae34 | -15.2361 | -53.87539 | 2026-08-31 05:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a6a5dc7-c24d-3da5-bf00-91e88bbcb395 | -15.63175 | -50.09502 | 2026-08-31 05:38:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fe916ba-c69c-3379-a994-33c56b1eaa9a | -19.14301 | -57.39395 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| cb7c576a-3160-39a3-8590-014218247d93 | -14.38838 | -52.56543 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 760ae788-941b-37bd-bdff-641f438058d3 | -14.4329 | -52.52462 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f410ed78-53d0-3afa-8b2d-f2bd1e5ca119 | -15.63287 | -50.10097 | 2026-08-31 05:38:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6f7faf9-e7e0-3ded-a702-0feac7ca3336 | -14.46581 | -52.19921 | 2026-08-31 05:38:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 102a0677-b9fe-3b18-b2fb-07304794493e | -14.43846 | -52.52559 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8438c8db-ec53-30de-97c7-56bdc5c4cc57 | -14.60303 | -54.10294 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 70f00377-d51f-383c-b808-da093e765584 | -14.44241 | -52.52034 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 31f6b320-c149-3736-a7f7-d1085f08758a | -14.45109 | -52.54385 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 460aa49b-8ba5-33f5-bcae-830ac48aa027 | -19.12688 | -57.41772 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| f0499953-7c3d-3d14-861c-5d7b142db8fc | -14.44401 | -52.52666 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8588a88c-2097-3e6b-8e72-36bd7632bcd8 | -14.38977 | -52.55356 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9dc5f87-4f64-3f72-a943-834a98a406c6 | -14.18412 | -52.87874 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3561f878-d852-32c7-af0f-0101733032a6 | -15.2329 | -56.38987 | 2026-08-31 05:38:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fd60af2-7c8e-3ff9-90b4-025c16787dda | -14.30418 | -52.90387 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3a21bb1-652c-3cdd-846e-7836676b8d93 | -14.17295 | -52.87505 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c396e81-7fe4-3d4c-8861-f6b5455d9214 | -14.13114 | -52.80759 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bed5594-3de4-3299-9765-788d1e0f8b69 | -14.60158 | -54.11494 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| db7df074-20fc-3e84-9ea3-ff845f17c83a | -14.39663 | -52.5434 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95296dd4-0830-3c50-b275-f2dcf7118c02 | -14.21599 | -52.84261 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb0a25e2-a01d-34f3-9c0a-f827f980792f | -13.4724 | -57.0387 | 2026-08-31 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 609f07d9-ae7c-37d0-89bd-c288acd08541 | -15.87048 | -56.49227 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbe9b620-33cb-3782-bdee-2864417d6c83 | -14.22611 | -52.85093 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0b994b53-00ee-35c8-b05e-ac0536bbc3a1 | -5.2546 | -55.9303 | 2026-08-31 05:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 9fb37300-6457-31d7-b9bc-4b09884fc3b9 | -5.2547 | -55.9105 | 2026-08-31 05:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| f501a9b0-ab08-38ab-8b20-edef02a6e7c5 | -6.622 | -58.5965 | 2026-08-31 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 7ca19629-b890-3fb2-ac55-4219b46d6064 | -6.6036 | -58.5972 | 2026-08-31 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 641d468b-507d-37a6-9282-5ca5e09834bb | -5.2548 | -55.8907 | 2026-08-31 05:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d09b3e38-4e3d-304d-b0ec-f0aceb54842f | -7.9236 | -44.2558 | 2026-08-31 05:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 609a31e1-1a03-31bd-96bb-9d636611d2ca | -6.6035 | -58.6166 | 2026-08-31 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 264ea90a-f9ce-37d9-b55a-8e8fb16bb305 | -5.2362 | -55.9112 | 2026-08-31 05:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 24b0091f-29f6-3df7-99cf-1c352dae4795 | -6.1294 | -57.6833 | 2026-08-31 05:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c37f8406-6a1c-3478-b519-1ed22b73e755 | -14.4007 | -52.5226 | 2026-08-31 05:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| e8425547-1b81-3245-a6ba-3ff017386d83 | -22.04644 | -56.0915 | 2026-08-31 05:40:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| baef2a4b-47bd-3ecb-adf3-e0e768671a72 | -22.04703 | -56.08609 | 2026-08-31 05:40:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c7c26c9-f708-3b26-b4d4-c1d223764d3f | -5.2548 | -55.8907 | 2026-08-31 05:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 17952609-7d9d-37f1-b221-d4fb2ed8450a | -6.6036 | -58.5972 | 2026-08-31 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 4b6cb34d-9617-37d1-a1ab-75e7c92e6356 | -6.622 | -58.5965 | 2026-08-31 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 05f86f9a-643a-3181-b197-7fe53646f273 | -5.2547 | -55.9105 | 2026-08-31 05:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 1619e795-4ae5-3028-8646-d97dc90b3504 | -20.2631 | -58.1437 | 2026-08-31 05:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.4 |
| ff334ff0-e1d9-3d2a-a147-9d8ded609564 | -6.1294 | -57.6833 | 2026-08-31 05:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| ecc75744-5d4a-3c9c-849f-a67d9aaed991 | -6.6035 | -58.6166 | 2026-08-31 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b5a7a227-64db-38b1-a795-c62e175bcc8d | -14.4004 | -52.5438 | 2026-08-31 05:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| db03da64-ab53-3459-99ab-5921b271b220 | -5.2362 | -55.9112 | 2026-08-31 05:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 24bc2776-3088-3075-b903-a946f66130e4 | -14.4007 | -52.5226 | 2026-08-31 05:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| a854271b-5c26-31a8-8d5b-e441abdbbd08 | -6.6219 | -58.6159 | 2026-08-31 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 66ad3279-5248-374b-a9f1-25a4bccae62a | -6.92072 | -55.71909 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5bd7ca8-3ca8-3b8c-a458-c4372b473390 | -7.55618 | -61.32553 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45f7cd48-7078-331e-bb9b-97500d259336 | -6.15049 | -57.88577 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62bf1a95-04a6-3ea6-96d2-6031bfb9bee9 | -7.4378 | -61.42617 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d7d49b0-daa7-33d2-a3bc-672e4c26714d | -7.53026 | -55.33038 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6e237b3-e3e3-3d4b-b06f-3aab5d9cefa8 | -5.24888 | -55.90561 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 11eb32e7-6808-3251-ae7a-ce0a671e739b | -7.57308 | -61.37661 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba2ff143-de27-346c-8fb7-659404108124 | -6.92204 | -55.7093 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1208c3ba-935f-312d-8fb1-5097228315ed | -7.33922 | -60.5952 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4cd5ca17-64f8-3f0e-a203-5c3998b3295b | -6.60779 | -58.60063 | 2026-08-31 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 507480a9-7868-3ac3-9099-0fc989b0f970 | -7.24055 | -64.72881 | 2026-08-31 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f83be653-80f0-3d28-bd12-5d06c0f0a0f5 | -7.62013 | -55.29382 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4dafaa17-d024-3e5d-8f17-df5d4fa00134 | -6.76987 | -55.64085 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8aa0859c-6ca0-36e5-8068-d325f82c7897 | -7.29983 | -60.58059 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8638d86e-223c-3539-bbf4-a310518e8ed5 | -7.84632 | -62.31742 | 2026-08-31 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb1786dc-ddfb-3176-b1ff-607e2012b1be | -7.25553 | -60.63371 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 640e0cf6-6db4-36f8-a71f-2dca74c6afba | -7.52293 | -55.32834 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b600cc1-b6fc-3c00-aae8-88be2326b577 | -5.25019 | -55.89664 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 08857467-0a21-3e75-844e-a2746392e25d | -7.69187 | -63.32647 | 2026-08-31 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cccfba45-3ab7-3a4a-be98-fd1824bba4d7 | -7.52268 | -61.37475 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69daf8ed-0dc5-3d17-a0f4-337db5e2a595 | -6.60309 | -58.59682 | 2026-08-31 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 26447860-9eda-3b14-a874-15493b42d1e0 | -7.2992 | -60.58499 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef32eae8-c9ee-344f-94fd-83a6b9c74825 | -6.93697 | -55.64605 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32e62adf-bcbc-3c8a-bf12-fd9bcfe77ff7 | -6.15379 | -57.78266 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab3c5d1a-35df-3750-818e-9c4760fe2868 | -7.62049 | -57.62167 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d7c2234-81c8-349b-8396-fe8fc599204e | -5.47822 | -57.14295 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c0d98da-47c2-3b99-b452-1b3233afbc3e | -7.92406 | -61.33642 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4fa387ef-0345-3bc5-a48d-fd644d0d2e4e | -5.24954 | -55.90111 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 495d2d77-0624-38d5-bec7-b36ef1746c3a | -7.57252 | -61.38067 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cf36bbc-4822-3133-a8e4-04aba144c738 | -5.57907 | -60.23407 | 2026-08-31 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5fafdba-ed26-3a3a-ba4a-25532820a4bd | -6.86961 | -59.47503 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 532a56dd-4912-34b1-97dd-cb393634b996 | -7.55799 | -61.31316 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e0c6015-cae5-3628-943c-dd2e8e175254 | -7.30308 | -60.59008 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 667e31cb-634f-31f3-980c-bc44e28e3140 | -7.57107 | -61.35974 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7f9f7f17-cf89-3c5f-8c3a-c15bf590de43 | -7.51635 | -55.27938 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 854d6197-e53c-3d93-9aa0-a7cd787bf77b | -5.48936 | -57.14441 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c6d9194-734b-3ea1-a55d-63433fb2f2f9 | -5.48272 | -57.15105 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d887c9a-2f1e-36f2-b4da-470d832bab60 | -5.25423 | -55.91099 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bfa3f040-b26d-37e2-b01f-5af29bcd62a5 | -6.93207 | -55.6352 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 09987d0a-157b-3afe-9d55-d7340f93f951 | -6.80406 | -59.45787 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9711a18-38a0-361a-8cc6-35be91b4bbd9 | -5.57669 | -60.23033 | 2026-08-31 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README71.md)
