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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1429f160-b76e-3b31-b165-86e751a4d4ca | -13.3361 | -54.32 | 2026-07-22 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| ea857ca7-8c5b-3c83-b846-51fbe7d474b3 | -17.5748 | -47.4996 | 2026-07-22 00:00:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 5d1a986a-d3b3-37e9-8430-a661d2205e19 | -17.5748 | -47.4996 | 2026-07-22 00:10:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 67ecded5-265b-3353-90d8-0f81c43172d7 | -13.3361 | -54.32 | 2026-07-22 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| e2ad0687-f449-31c1-9686-c850f8831d70 | -17.5947 | -47.4956 | 2026-07-22 00:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 5c21dffe-1656-3977-b8e5-9890d28d4f9d | -17.5748 | -47.4996 | 2026-07-22 00:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 731535ae-ac15-320c-84cd-5875f35e0d56 | -13.3361 | -54.32 | 2026-07-22 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 5adcd310-509e-3bdc-adf4-25f5614d54c6 | -13.3361 | -54.32 | 2026-07-22 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| e4490a43-f2d4-349e-88e7-0ec7eb76b06c | -17.5748 | -47.4996 | 2026-07-22 00:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| b38e86d1-a822-38dd-8af6-47752fa89350 | -17.5947 | -47.4956 | 2026-07-22 00:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 729784e5-5d50-3846-b8d6-ebcf76aa48ce | -17.5802 | -47.494801 | 2026-07-22 00:37:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bf29510a-6a91-35f6-a0c3-219d3d36c159 | -9.2609 | -59.803699 | 2026-07-22 00:37:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 556c3952-ab13-3dfa-955a-5b12b03a7b46 | -13.3404 | -54.3008 | 2026-07-22 00:37:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6367493a-d09e-353c-a931-418228c33fd0 | -6.5986 | -51.695 | 2026-07-22 00:37:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d73e7d3a-6291-3e8e-90ff-1c2829f8c853 | -21.267599 | -49.577599 | 2026-07-22 00:37:00 | METOP-B | ADOLFO | SÃO PAULO | Brasil | 3500204 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5df8845d-d063-30f3-bad5-43c6b76b9068 | -13.3239 | -54.3195 | 2026-07-22 00:37:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2978e2f2-da8e-32aa-99b2-f8c15fbcce49 | -12.1381 | -48.247299 | 2026-07-22 00:37:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30b896ca-4a68-35ec-b1f5-0d0b31fef1ca | -13.3306 | -54.303101 | 2026-07-22 00:37:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab21d335-d918-39c2-876c-2c01621f7cd8 | -2.1583 | -53.638901 | 2026-07-22 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cac64e74-c4c3-3620-b2f0-343e6ba5fd9d | 2.5242 | -60.643002 | 2026-07-22 00:37:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5d5d917c-76e3-383c-b13f-60bb123f396e | -8.7317 | -54.615601 | 2026-07-22 00:37:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 424d8070-2248-36c9-b035-815e0c2aae1a | -12.5212 | -48.250099 | 2026-07-22 00:37:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bcd75f9a-6fed-37dc-aa0c-d63a9bb9f5d4 | 2.5225 | -60.650501 | 2026-07-22 00:37:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e496846f-3706-3548-8898-8dc464638787 | -11.3323 | -47.9995 | 2026-07-22 00:37:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f8e4ce4-ceb1-3311-a14e-432ca18023ec | -18.538401 | -56.8008 | 2026-07-22 00:37:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 72341231-7122-3121-a062-5ff126682c34 | -5.5479 | -48.719898 | 2026-07-22 00:37:00 | METOP-B | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7002bd2c-35c0-368e-894f-732cbf2481c7 | -18.536699 | -56.792198 | 2026-07-22 00:37:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3a2eaa63-a347-3fbb-92d3-9c758973703a | -17.567301 | -47.484699 | 2026-07-22 00:37:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0d959981-009d-3b1f-963a-9ca525743610 | -13.3208 | -54.305401 | 2026-07-22 00:37:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c086e76d-95a3-3eae-ae8d-f94ab4cdfafd | -13.3337 | -54.3172 | 2026-07-22 00:37:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1cee0e48-f26a-3cb1-81e3-d2cb0c44703b | -13.3224 | -54.3125 | 2026-07-22 00:37:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52e5180d-4ae7-3834-b835-77a17004e9d2 | -13.9894 | -49.583801 | 2026-07-22 00:37:00 | METOP-B | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7da6bb5d-f8ea-3ff4-9bf0-f94a176c1c5e | -17.573799 | -47.510201 | 2026-07-22 00:37:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 560a5923-1d64-3f1a-bb2a-fdb45cc9d08a | -13.342 | -54.307899 | 2026-07-22 00:37:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9db1838d-7d1e-3859-9ba9-8592db3b763f | -9.4797 | -57.309101 | 2026-07-22 00:37:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96a0b54a-9796-3752-b98a-a31bd8250882 | -8.7301 | -54.608501 | 2026-07-22 00:37:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f71821b-c7c7-33e9-84bf-950f5f625b64 | -9.1002 | -59.387901 | 2026-07-22 00:37:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d53839a8-fce6-32f8-b4e5-e321d422b266 | -8.7524 | -49.0769 | 2026-07-22 00:37:00 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f494885-8113-3178-a8f1-83706fa2d92d | -10.144 | -55.390202 | 2026-07-22 00:37:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d93641e3-3bb5-33e7-b4d8-d9ea0158c760 | -12.1416 | -48.261101 | 2026-07-22 00:37:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9ce72fc-06fc-358a-8b40-2548e5bb97a4 | -13.3435 | -54.314899 | 2026-07-22 00:37:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aac95aa7-76ab-3589-ba0a-cd50a0ac9023 | -12.4503 | -46.510799 | 2026-07-22 00:37:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 118fa262-1b5e-3463-a089-6f57a0c49c8c | -17.5769 | -47.481998 | 2026-07-22 00:37:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 511dfbdc-3f02-360d-98df-c9e6fa3ea252 | -13.3322 | -54.3102 | 2026-07-22 00:37:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7a1629f-c15c-36e7-b78f-510d31de6481 | -12.1346 | -48.233501 | 2026-07-22 00:37:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8a50b0e-1bd3-3005-84f7-470d0deb134e | -12.46 | -46.508202 | 2026-07-22 00:37:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 158fc96c-85d3-355f-9ad2-287774e84911 | -6.5432 | -55.145199 | 2026-07-22 00:37:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e94ef1c-a8e5-34fe-a675-2ee323ae2ce9 | 2.5144 | -60.6408 | 2026-07-22 00:37:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0404fe54-7ef3-3e03-9574-b2424907835a | -13.3314 | -51.576199 | 2026-07-22 00:37:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2a79dc5d-5185-37cd-8d63-6ada01557db7 | -11.6321 | -48.5378 | 2026-07-22 00:37:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2542f26-37e3-3fac-ad43-691766527ccd | -17.570499 | -47.497501 | 2026-07-22 00:37:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0694e25c-083f-3bc0-b74c-3d1af1412e2f | -12.5177 | -48.236401 | 2026-07-22 00:37:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19216d7d-7d1e-3b17-8a60-1d470a45e409 | -2.1604 | -53.647701 | 2026-07-22 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6aff260a-f69f-3f9c-b9ec-cca6886642e2 | -17.5576 | -47.4874 | 2026-07-22 00:37:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be89e4fe-5091-3083-8306-fb254201403c | -17.847099 | -52.4771 | 2026-07-22 00:37:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b15389da-a57a-3cac-aecc-88a551ae233a | -17.5748 | -47.4996 | 2026-07-22 00:40:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 295429a4-74be-3f70-9650-5d7c369dd2db | -13.3361 | -54.32 | 2026-07-22 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 84d6454e-453d-3be8-80aa-9e8013bda403 | -17.5748 | -47.4996 | 2026-07-22 00:50:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| c210a783-df01-3c05-8e4d-8e3733ebee77 | -17.5947 | -47.4956 | 2026-07-22 00:50:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 018089df-7893-3e26-9905-0982e22d68a6 | -8.7497 | -49.0782 | 2026-07-22 01:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 0f72bb37-8fd3-3e0e-bb38-e0c0ea6135ba | -13.3361 | -54.32 | 2026-07-22 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| ce35a7d8-d362-32c7-90ac-e7f3a8ee1561 | -17.5748 | -47.4996 | 2026-07-22 01:00:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 778308f9-a9cc-30e0-827f-695e3a32aa4c | -10.6422 | -47.480598 | 2026-07-22 01:03:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4006697-1b63-3ee7-84d5-65683515a0a9 | -19.511999 | -49.681999 | 2026-07-22 01:03:00 | METOP-C | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 324b99bf-f3d9-3aa6-9c86-ed2f3081f964 | -8.7642 | -49.0924 | 2026-07-22 01:03:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 088cdaea-e71b-3fcf-81d1-75ce7c79386d | -8.7591 | -49.071602 | 2026-07-22 01:03:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d8fa6b44-2ee6-34de-9035-56ed5b4081f4 | -11.6367 | -48.540199 | 2026-07-22 01:03:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e2ac8fa-2421-3ddc-b381-226bdf191523 | -8.7342 | -54.626202 | 2026-07-22 01:03:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd5028e1-6b94-30c0-a814-bb8ce399e3cd | -13.3357 | -54.3055 | 2026-07-22 01:03:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6639855c-9105-333e-8f26-3cf7c3a5dced | -18.5336 | -56.813599 | 2026-07-22 01:03:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 924bf832-295c-3881-902e-c62c351908db | -18.5315 | -56.802799 | 2026-07-22 01:03:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c316146c-b92c-3c6f-9a64-b1de7e069f58 | -17.573299 | -47.504398 | 2026-07-22 01:03:00 | METOP-C | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| adfa0e3b-7c4e-3b61-83e2-984c1bfb6702 | -17.8423 | -52.482399 | 2026-07-22 01:03:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1a6f4bd9-e1bb-34ff-8126-4239bee71e10 | -13.3373 | -54.312698 | 2026-07-22 01:03:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b03bbbf-c152-3dbb-b8b0-c040dc942cea | -5.5603 | -48.7216 | 2026-07-22 01:03:00 | METOP-C | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab3ed0b2-7240-3555-8e92-955c59a0acfb | -13.3291 | -54.322201 | 2026-07-22 01:03:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29c98a00-43c7-312a-9174-359c548766c0 | -18.681499 | -52.651901 | 2026-07-22 01:03:00 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 94ba9d87-9f0f-38e0-97bd-1be36a0dfd67 | -17.583099 | -47.501801 | 2026-07-22 01:03:00 | METOP-C | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1ceaae40-5866-3454-927c-213993a4ae53 | -12.4664 | -46.508499 | 2026-07-22 01:03:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b4ad11b-8ab8-3b8f-9d36-8c634b8e2bee | -17.5709 | -47.494499 | 2026-07-22 01:03:00 | METOP-C | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| de5bd382-8fef-341f-b11b-b84ff0369446 | -18.5434 | -56.8116 | 2026-07-22 01:03:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5561a60f-76c5-3d1c-90f0-217a156aa34c | -12.5278 | -48.251202 | 2026-07-22 01:03:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75bc7ba1-28e3-3d9c-b13e-c17075c07b0b | -13.3389 | -54.32 | 2026-07-22 01:03:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cae67f74-bd04-3981-b311-a052b1ed4f95 | -1.8232 | -54.475201 | 2026-07-22 01:03:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb6cab3c-d2aa-304a-9775-4530ad184bae | -1.8248 | -54.482201 | 2026-07-22 01:03:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7a9098d-b030-3d12-a742-c9bb415e7b21 | -22.641399 | -47.9319 | 2026-07-22 01:03:00 | METOP-C | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c164004e-11dc-30c2-8042-ea15e4a2da3f | -7.0145 | -45.419399 | 2026-07-22 01:03:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e212d0a-e9b2-33b7-86b2-729d5f24be7e | -14.0002 | -49.591202 | 2026-07-22 01:03:00 | METOP-C | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1ac64b08-7eeb-37b8-bdde-10ee890a0dbd | -12.4698 | -46.521801 | 2026-07-22 01:03:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6d02b32-297e-3954-91d8-abfebec98fee | -1.815 | -54.484402 | 2026-07-22 01:03:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1cb0a2c-cb15-3968-aeca-6cb7dcc398c8 | -19.5138 | -49.689701 | 2026-07-22 01:03:00 | METOP-C | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 010c2940-5df9-3b7e-9d4f-85ea59bc4d14 | -17.5807 | -47.492001 | 2026-07-22 01:03:00 | METOP-C | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e1fa5f8e-f781-3a97-aff8-accebae204d1 | -17.585501 | -47.5117 | 2026-07-22 01:03:00 | METOP-C | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ffc32df1-780d-37c2-abb8-ef5cd4fe60f8 | -11.3394 | -48.002201 | 2026-07-22 01:03:00 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e69c92af-8b5b-3cd6-b304-c227985aa99d | -12.1442 | -48.248001 | 2026-07-22 01:03:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6b64838-7ae1-3e53-a72a-47e1aa8bfb6a | -10.6325 | -47.483002 | 2026-07-22 01:03:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e9f7be8-f8b9-35f4-ba76-0c6ac43da3cb | -1.8134 | -54.477402 | 2026-07-22 01:03:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8107c41e-20e5-3908-bab6-96a94c95c59a | -13.3275 | -54.314899 | 2026-07-22 01:03:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7a8e60c-6f5d-3757-8a92-b25660e93ef8 | -6.5452 | -55.151798 | 2026-07-22 01:03:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f8cb5ff-600f-33e1-9cf6-0ec507609d62 | -17.843901 | -52.489601 | 2026-07-22 01:03:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
