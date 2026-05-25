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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea51bad9-7fdb-3df1-8343-3b326c9b20f7 | -7.39812 | -39.75577 | 2026-05-25 04:29:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8abbe3a1-3c6c-3cd8-a91e-2fd9a88503d2 | -11.21469 | -53.83079 | 2026-05-25 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aeb4f70f-996a-35b8-a368-13c4d2424ef1 | -8.10986 | -46.90439 | 2026-05-25 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06b7b6ae-f4f6-3c2a-9621-b4993f85d1a7 | -8.26414 | -43.93146 | 2026-05-25 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10b267e8-17f2-3a62-b0a9-58081f9dfc43 | -11.45952 | -46.69514 | 2026-05-25 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1b176b4b-0bbf-34e2-9553-fff8231d24fb | -11.0691 | -46.5146 | 2026-05-25 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79e174c3-d96a-3391-8f72-caf1ad2fb98d | -7.73022 | -47.2423 | 2026-05-25 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b273eeda-18d2-3778-81b3-7dc849c51e90 | -8.98835 | -46.82893 | 2026-05-25 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f67a58be-fc56-3cbe-b0f9-3ad2e3844808 | -11.43754 | -52.93114 | 2026-05-25 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6e04189-4b01-3195-94c7-a426572d0617 | -6.13648 | -47.87891 | 2026-05-25 04:29:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f29e427-833d-34a4-8fb6-438e719a5be2 | -9.44016 | -48.19407 | 2026-05-25 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7435553a-d5b6-374f-85c6-6df07ff2ceb4 | -7.13379 | -44.06838 | 2026-05-25 04:29:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b617e373-6ad0-3f2c-9825-915da948be04 | -8.72559 | -48.32132 | 2026-05-25 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4da7216e-ae09-33e5-b95e-e0791991e0c4 | -9.31557 | -50.63406 | 2026-05-25 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9947c437-a182-3b6a-a9fd-67e9ebee53d7 | -11.4634 | -47.40052 | 2026-05-25 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8afe74d8-0ed9-3bc7-b338-e484f866cb5f | -8.10927 | -46.90807 | 2026-05-25 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b2f6afd-9323-3046-9d31-69b3b9ed7ccf | -11.46401 | -47.39679 | 2026-05-25 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cd94c22-b48e-3a30-adcc-d7c2367dc3a7 | -11.36257 | -52.9555 | 2026-05-25 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| bab7e5d3-a676-3593-b611-ec9ada8aea65 | -20.0161 | -44.23683 | 2026-05-25 04:32:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 815d9143-9df2-33c0-9edc-6a2c81f3c455 | -12.55472 | -48.35339 | 2026-05-25 04:32:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29ddcac6-4dd1-3932-ae7a-7eb5528788a8 | -13.39916 | -46.60635 | 2026-05-25 04:32:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5ac94fb-590c-3b30-b30e-faf4c4de7718 | -11.54446 | -56.94118 | 2026-05-25 04:32:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9701c63f-9b22-334e-b33f-e2955a305aaf | -11.54616 | -56.93245 | 2026-05-25 04:32:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 091e88dc-f4b8-3d08-bd58-88fe3ccc04a3 | -12.88883 | -58.20108 | 2026-05-25 04:32:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5df0f221-ade8-373d-a08e-2de9712595e6 | -12.88989 | -58.19603 | 2026-05-25 04:32:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f493face-bf0f-3055-9dd7-05e9df7743ac | -12.34034 | -48.23178 | 2026-05-25 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d8a52af-9d19-323b-8d5e-f21907cf94b8 | -11.54912 | -56.93555 | 2026-05-25 04:32:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9aca6197-6f1a-3115-8e73-c4521025ef0a | -11.54531 | -56.93679 | 2026-05-25 04:32:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01364b81-8170-3617-b4c6-eccc4993ae6f | -14.73466 | -52.69301 | 2026-05-25 04:32:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b981fae-8cf9-3ffb-bad0-3d27457cd529 | -17.68185 | -47.76603 | 2026-05-25 04:32:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e7aae79c-9eef-30d7-8dbd-fef52bcfc5b4 | -12.88617 | -58.19653 | 2026-05-25 04:32:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3eb6af27-a514-35f9-9f8c-9bf986bc70b6 | -20.01745 | -44.23449 | 2026-05-25 04:32:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b8a20910-5743-3954-a070-e0b87c32d82a | -18.09269 | -46.87828 | 2026-05-25 04:32:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cceab435-c803-364d-97e7-db6e094974a1 | -13.5296 | -46.71548 | 2026-05-25 04:32:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4ec46ccd-ede7-3142-809d-a4a4a08e7265 | -19.69154 | -44.92402 | 2026-05-25 04:32:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0e24447-d3c3-3e15-91b0-7f9f3e3c8b29 | -12.34097 | -48.22796 | 2026-05-25 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b920fd42-2e84-3d08-8d17-cc5e5e210e99 | -12.41258 | -47.49498 | 2026-05-25 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58fc8452-442e-3e51-9efe-aaf5945b879b | -11.54824 | -56.9399 | 2026-05-25 04:32:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ef220b2-5498-37df-abd6-8f08eec311a5 | -12.89234 | -58.19796 | 2026-05-25 04:32:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac5925cc-ce46-329e-9414-2d7041e6ab20 | -14.76045 | -52.66839 | 2026-05-25 04:32:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8af4f953-4e3b-3f7d-bb7f-9a4e9e4813c6 | -13.53294 | -46.71603 | 2026-05-25 04:32:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f603d265-5819-3c58-a037-ed54d07dabea | -13.40152 | -46.60639 | 2026-05-25 04:32:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| caf15683-4b5e-3504-9291-a34c84c42da2 | -13.97634 | -53.88032 | 2026-05-25 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebed6dfd-33b1-3cd6-b740-9ea24622d584 | -20.01682 | -44.23917 | 2026-05-25 04:32:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8ef8b56c-5c92-3353-ae3f-909841ca004b | -19.69445 | -54.74142 | 2026-05-25 04:34:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f29ae57-97cd-38a1-96e1-e9a34ec7a10b | -23.77047 | -54.5104 | 2026-05-25 04:34:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 51f4df45-006f-3ea1-8387-00aa39aaa68f | -23.76643 | -54.50956 | 2026-05-25 04:34:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9d1cfbce-06b0-365c-a709-62c774673321 | -21.51702 | -41.32968 | 2026-05-25 04:34:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d77b5c14-1946-3c5b-9e25-811f0de834de | -30.13627 | -52.55667 | 2026-05-25 04:36:00 | NPP-375D | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| dcbecd99-1753-3964-8119-b1b4e893f673 | -6.07765 | -44.01053 | 2026-05-25 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53a88c4e-fff1-39d3-be43-ec4b2baee73b | -6.51736 | -43.68213 | 2026-05-25 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ddeb444-eff8-34e6-b3a2-0b3068faf0bf | -4.38194 | -43.29078 | 2026-05-25 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ad8dc64-861e-33ed-b4f1-c07e83cbe284 | -4.38462 | -43.28865 | 2026-05-25 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d644d61-3529-3cfa-ba39-1d03f74a3bd5 | -5.35131 | -45.18704 | 2026-05-25 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25d9f63f-ab01-3691-9ed6-cfd39df17aef | -7.6297 | -56.08697 | 2026-05-25 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 163f4cb6-e5b7-34b3-8134-c6a369042a39 | -8.62161 | -45.00589 | 2026-05-25 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 894a4cac-7c7f-3c0a-9f2d-90612d7c70f5 | -8.72662 | -48.32853 | 2026-05-25 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bbc31f3-d458-3bda-982a-b559b99329e7 | -8.99129 | -46.8271 | 2026-05-25 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16505658-92f4-365f-9c89-3d5ed9f8189f | -8.72082 | -47.91241 | 2026-05-25 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78690d77-7654-369e-b986-e9b1526dbb03 | -8.72425 | -48.31951 | 2026-05-25 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95c2f7de-9441-3245-895f-9599706716e5 | -8.72363 | -48.32373 | 2026-05-25 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 805ec1cb-acf0-3071-a98c-447b69e99cc6 | -8.72786 | -48.32008 | 2026-05-25 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f22c1f1b-85fb-32ea-9273-e6a117584cb8 | -8.10823 | -46.90008 | 2026-05-25 04:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c21d3e92-0f8a-324a-b9f0-7e9c2adebcc2 | -8.72601 | -48.32558 | 2026-05-25 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 138c22f5-a98a-3600-bc91-f11ac2008d43 | -8.72666 | -48.32137 | 2026-05-25 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1039f937-1438-3009-8ba2-e2f0e247041b | -8.86366 | -46.93565 | 2026-05-25 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e5c71a6-9310-3c55-a1bb-694ac492fdc3 | -8.72305 | -48.3208 | 2026-05-25 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78b3575c-deec-3fe0-87c0-55be7258be07 | -9.31593 | -50.63137 | 2026-05-25 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efe4601b-99d8-3d6e-9ac7-9f56650ccbe2 | -9.31537 | -50.63493 | 2026-05-25 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b00dc702-34f8-360c-a3a8-13a708d88cb6 | -8.72724 | -48.3243 | 2026-05-25 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f154affd-42b1-3137-a108-deb672581989 | -7.46166 | -49.73979 | 2026-05-25 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dbf0f85-e34a-3aff-9c66-ca24086a124e | -8.61717 | -45.00525 | 2026-05-25 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 635cd60f-012c-3713-bd82-d4e32a508de7 | -7.73008 | -47.24075 | 2026-05-25 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ee4a4c4-e09e-35d6-8653-9922b8669a39 | -7.73387 | -47.24131 | 2026-05-25 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cf2f1da-78e8-3188-b9fe-b00f801d6dc9 | -8.7224 | -48.32502 | 2026-05-25 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a9bde3e-1f95-366b-84fb-0f74f3d7804f | -8.26475 | -43.92911 | 2026-05-25 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc8db017-8fa3-3349-a694-608670db9431 | -8.10749 | -46.90512 | 2026-05-25 04:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f07427f-656a-3ed5-85e5-ac5a0f5b426a | -8.26 | -43.92836 | 2026-05-25 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06bf3182-eb87-388c-9f37-8acddb2ea4d3 | -11.948 | -49.30121 | 2026-05-25 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d724206-48b1-367a-bbbc-c59caa67c7ac | -15.08449 | -57.63918 | 2026-05-25 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6a7d119-e2f8-3640-a1ca-9a938da9e620 | -11.27721 | -53.96677 | 2026-05-25 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0065a1a-e106-3a3b-aa84-17a14546fc8b | -15.10365 | -57.622 | 2026-05-25 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 331a6cea-91a9-3fa8-81e0-4421f884354c | -11.94562 | -49.29242 | 2026-05-25 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32eecd94-fd84-3b06-9774-351f691b5821 | -14.76199 | -52.66717 | 2026-05-25 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3c40f90-db39-34d9-8f7d-db4ad3eb5f25 | -11.55282 | -56.93992 | 2026-05-25 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90718e69-eb71-319d-a427-7d3a499323d2 | -12.34055 | -48.22784 | 2026-05-25 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3821340c-d33f-356e-beca-50efd2bceb2f | -12.30131 | -47.90667 | 2026-05-25 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bb549ce-0b21-341b-9b45-b3fb922526c2 | -14.75368 | -52.67676 | 2026-05-25 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aee55277-3179-3853-83db-7958a07cc57d | -11.54889 | -56.93917 | 2026-05-25 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f64906ea-f9d9-3f9f-98af-15c870cadfe5 | -12.89256 | -58.18153 | 2026-05-25 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebbb888b-1969-3590-98eb-e02f75e55179 | -11.55497 | -56.951 | 2026-05-25 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cffbd9c3-42de-3042-b099-6d0791ba625b | -11.5471 | -56.9495 | 2026-05-25 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5da1b2a4-c2d4-3a90-8958-742ce1f13871 | -12.41447 | -47.49543 | 2026-05-25 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9397a49-e4d1-36d5-b467-ca7331a17cd8 | -10.86958 | -53.73522 | 2026-05-25 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd6a0b8d-5288-3f36-b85e-5b753275cb32 | -10.39908 | -49.4418 | 2026-05-25 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1ec18b9-739d-37cb-8d86-c4285e58196d | -11.17262 | -55.91728 | 2026-05-25 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5ec445c9-9d4b-3215-b467-54b063a761f0 | -11.54585 | -56.93328 | 2026-05-25 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce742984-4fdc-3ec1-a2bf-819e1018e03d | -14.73432 | -52.69181 | 2026-05-25 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77efde20-93a2-3877-930d-9cd0d2fbc926 | -11.94859 | -49.2971 | 2026-05-25 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cade1be0-61d1-3d3f-bbc4-8a968849b716 | -12.54082 | -57.16105 | 2026-05-25 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README3.md)
