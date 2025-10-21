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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9094155-974c-3a68-9b9c-06f39edb7634 | -17.4148 | -55.04752 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5d90b083-2931-3ac6-a3b9-901bfbf073b2 | -17.68402 | -52.24358 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5e6659cb-ba31-381a-831b-b1151b4fe86c | -17.68236 | -52.25473 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9e64ce5e-1dec-3fa4-838a-05871ada9aa3 | -18.17901 | -52.97261 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 201a8ba8-b9bf-386b-b5ce-90f806e1976e | -18.80394 | -47.01408 | 2025-10-21 04:49:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d698ce9f-dfb2-3b51-a958-3b6a5a5499b1 | -16.06709 | -56.86512 | 2025-10-21 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2360d9b7-70a0-384c-8f83-8bd218bacf4f | -16.69255 | -52.88988 | 2025-10-21 04:49:00 | NOAA-21 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cf21c9f-2646-3945-9456-0123926313d5 | -19.34106 | -44.69116 | 2025-10-21 04:49:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 347c6cc9-4dbe-3936-a63a-8671d2d549bd | -18.18344 | -52.96588 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ec67f6e-2c54-32ba-b388-6b5a61ccaa8e | -20.95356 | -45.81643 | 2025-10-21 04:49:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f511c460-3a8d-3f39-81f9-34c7f34f5481 | -18.87138 | -51.51664 | 2025-10-21 04:49:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78c2dbfc-9e35-338d-8312-b05d2f164288 | -17.40898 | -55.06194 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2e07f85b-7e60-32d4-857d-ee8c6a000104 | -16.36611 | -51.43704 | 2025-10-21 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff507d6c-875d-3371-b5d7-215a6dc57e1f | -16.53771 | -53.72762 | 2025-10-21 04:49:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ea40c06-2e51-3fff-9b67-f8c37593238b | -17.40561 | -55.06134 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2c4bfdaf-6c9c-3492-ba1d-c8ec41a43f5a | -15.72574 | -54.56263 | 2025-10-21 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6d004533-5469-37fb-803c-2fd2792e2ebe | -15.13749 | -55.37537 | 2025-10-21 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7961f60c-5947-365a-b19f-894c99e4e1c1 | -17.41817 | -55.04812 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 00896d29-b3d7-340f-bc9a-8e0ce2b0f0d8 | -16.24555 | -52.54727 | 2025-10-21 04:49:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8848de94-b34b-30d0-bb79-ba38a050ba80 | -17.41235 | -55.06254 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 780040d7-e2af-3dd4-93bb-8c681384d0ba | -19.16266 | -50.83394 | 2025-10-21 04:49:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5060296-6fe6-3df1-9c9b-9b74f482de85 | -17.68406 | -52.26639 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f949b9db-97fc-3ad6-a100-29000f0090e3 | -18.59155 | -51.71415 | 2025-10-21 04:49:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43d319c2-2a87-3c6e-a038-e8cc3733f10d | -17.40959 | -55.05819 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 78cf22de-660b-3d00-baae-c3ae7a9dfd21 | -19.09298 | -57.53383 | 2025-10-21 04:49:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 081f7bdd-b0a6-3646-8876-fa4fa61399cf | -17.43623 | -55.0436 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 327b497b-146f-3be2-bd38-c7722d6ce297 | -20.43153 | -48.03291 | 2025-10-21 04:49:00 | NOAA-21 | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b70ad1c8-3fed-3da9-9811-114fba603383 | -19.08825 | -57.53954 | 2025-10-21 04:49:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 09d018b2-cf9f-3106-8ef6-fbc3b6aae9a6 | -17.42093 | -55.05247 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d4405945-facf-3d1c-940e-10654ff10826 | -18.19283 | -52.97117 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0d1bbbb-84d2-3d72-a411-49a623c2cfc8 | -17.41021 | -55.05444 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e97cc14c-e2c9-3e86-9324-36a7df6384f3 | -3.4968 | -45.8195 | 2025-10-21 04:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 156.5 |
| b0a1aa4e-142a-348b-84f1-6b3daae8a24b | -3.5154 | -45.8187 | 2025-10-21 04:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| cde833e1-4967-3600-80de-7d635d44b6ee | -3.4967 | -45.8418 | 2025-10-21 04:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| f653c78a-cd02-37b9-944b-982dfe395901 | -20.48216 | -54.75759 | 2025-10-21 04:51:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81138a92-dcba-3ecc-a707-9d6e49eb3235 | -21.44374 | -57.61335 | 2025-10-21 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62d51f4b-a297-3845-b8a4-0949a23d8acc | -21.36436 | -55.92948 | 2025-10-21 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1669d68-cd68-3468-9df8-5e3f704a8149 | -20.48395 | -54.6823 | 2025-10-21 04:51:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 13.4 |
| cbf2fb96-b4a9-39d6-976e-2676b7ba8432 | -22.30304 | -51.50657 | 2025-10-21 04:51:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 8aa1eacf-b55f-3bae-9092-f24524934ec6 | -20.48454 | -54.67863 | 2025-10-21 04:51:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 512349d4-5839-35bc-8060-2114495d6e86 | -21.14672 | -50.46473 | 2025-10-21 04:51:00 | NOAA-21 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| da6b1cf2-151b-3a22-b17a-04702ca63c36 | -20.92494 | -55.7818 | 2025-10-21 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9372fee7-4f70-35f9-bb9e-e54db79594f9 | -21.14156 | -55.73626 | 2025-10-21 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93fba7a8-7abf-372e-871a-35e38627f864 | -33.05401 | -53.16195 | 2025-10-21 04:53:00 | NOAA-21 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 279c94fa-50aa-36cb-a820-cfd4367fe0e2 | 1.7302 | -55.7049 | 2025-10-21 05:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| ff3009b2-b5a3-319a-8acf-f5c97f945366 | 1.7303 | -55.6851 | 2025-10-21 05:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 93c38b19-fb74-3451-8935-1fe120a59e1b | -3.4967 | -45.8418 | 2025-10-21 05:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 25c67dd4-f120-3905-a5c7-89671ddee895 | -3.4968 | -45.8195 | 2025-10-21 05:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 129.2 |
| eac681c1-89e5-3643-be2a-a58d9633f6d0 | -3.4968 | -45.8195 | 2025-10-21 05:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 3c8ae19d-7723-3a80-8eaf-2d2a5f9383e6 | -3.4967 | -45.8418 | 2025-10-21 05:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| a58ba9e3-8459-3de2-b1ad-5de1fdbd4169 | -2.22429 | -48.36957 | 2025-10-21 05:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc50ab10-1a46-3f00-a723-4a7a101f0d27 | 1.72175 | -55.6835 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc71c7a9-c460-3a58-842a-73bc4432e2ff | -2.87607 | -50.72511 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8ab44e5-a3cf-3f52-8df9-2da2a81b8b4f | -3.5072 | -45.82349 | 2025-10-21 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7a60aabc-8d36-3585-8f6b-85ae23c74734 | 1.72452 | -55.67954 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4ca7b45-faf7-3ef0-9c47-14a21f0d27b1 | -2.79499 | -48.88964 | 2025-10-21 05:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90028b05-4c72-3786-abbd-5ab08a5757f8 | -2.77177 | -48.02214 | 2025-10-21 05:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d0269d7-a64b-3c1a-a0fd-46e71d4ac7c0 | -2.19225 | -54.47908 | 2025-10-21 05:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 415f084c-db92-32d3-8a46-d831231ab9c2 | -2.90779 | -48.98384 | 2025-10-21 05:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f54d18f3-0909-3d66-a521-29bd3ef0cca4 | -2.69445 | -49.55086 | 2025-10-21 05:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b268b8f0-95c5-3f58-9506-f9a96b6c10d8 | 1.70098 | -55.72206 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3dd61ba-68f3-38cc-af75-4d39f97852e5 | 3.99005 | -59.71651 | 2025-10-21 05:12:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8e7bae1c-af97-37cb-8149-fc6ee79e5671 | 1.7104 | -55.71706 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 586c949f-8300-388f-84a2-695c0e54e617 | -3.50115 | -45.82259 | 2025-10-21 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6b00524a-3b57-3ba8-8421-d7690b7a6c05 | -2.16679 | -53.48829 | 2025-10-21 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9205a116-cffd-324d-9f02-c6d2342fbf22 | -2.86504 | -50.73994 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cfb07df-0e5e-3347-9cc4-641df98e853f | 1.71951 | -55.69091 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 89ae35a4-9e6d-33f9-a657-89e1e7aeb1d1 | 1.72615 | -55.68987 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68da900d-656d-3b35-b692-33e2cff5362e | -1.19663 | -49.07904 | 2025-10-21 05:12:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82452784-fd84-3481-8b4d-1d1d829117c3 | 1.71094 | -55.7205 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fa15599-b29b-304a-a700-c6f5d2f0f272 | 1.72507 | -55.68298 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 430306bf-4bb0-34a5-a98f-d22f119747ce | 1.71372 | -55.71654 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| df54bd96-4863-321b-88d3-1165e26ad75e | -2.25214 | -51.91448 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35ef095f-f390-3e6e-a43d-c5ad1b4be0b8 | 1.71377 | -55.69536 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa0c4f41-5bdc-3130-aaa3-4789988b15b9 | -3.12552 | -45.27169 | 2025-10-21 05:12:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12ce3778-ed2b-334e-ba42-da7f84cef048 | -3.50588 | -45.8325 | 2025-10-21 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 50b1b010-8d5c-35e0-9205-43462caec0ad | -2.87177 | -50.72445 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66bb4ff6-0748-31dc-8602-5615609bde87 | -2.80307 | -51.34655 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f2ba322-7ff3-31d6-9c47-57098ad4a93a | -2.71834 | -48.34161 | 2025-10-21 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bb355e6-a8da-37c3-9fe8-42c5fe94fd50 | 1.76653 | -55.6871 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 542cf9e8-51d8-36d2-b2d9-450cc4cbda25 | 1.71565 | -55.68798 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 42395969-f235-3b33-8b29-d4c82e34acb8 | -2.86265 | -48.56765 | 2025-10-21 05:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c6bcdc7-a903-3577-82bf-aaa8bbb6c29b | -1.62503 | -47.05478 | 2025-10-21 05:12:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1140ca49-efcb-3a96-89ff-98e13bf7608a | -2.77224 | -48.01907 | 2025-10-21 05:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c3e22a3-5b14-3338-9550-1081f260fe49 | -2.16614 | -53.49239 | 2025-10-21 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68f8d7d2-3436-372d-84d7-6631cc6f08dc | -2.69774 | -49.5494 | 2025-10-21 05:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c78e1f7-96b6-3ff3-814a-b28d1e11e314 | -3.22297 | -46.78394 | 2025-10-21 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f77749ee-cddd-3e2e-990f-ae09257417d1 | -2.2245 | -48.36908 | 2025-10-21 05:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f64c8d6c-e4f4-3f06-b26f-13ae2bc7b3ce | 1.72398 | -55.67609 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 736074be-d6e6-3551-b98c-58c82753722d | 1.74999 | -55.6685 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ffa9c71-9aa4-33b3-b633-97cfab01f394 | 3.86726 | -60.08549 | 2025-10-21 05:12:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a81d9d70-60f9-30dd-ace0-3c453f98ddb1 | -2.78971 | -49.61889 | 2025-10-21 05:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c71fc9b3-bdac-340c-8791-5efb0948b4ba | -3.08818 | -49.50425 | 2025-10-21 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e5e5b7c-cd9a-3de7-aca5-ed6c398c900d | -2.44534 | -49.3703 | 2025-10-21 05:12:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1998ed7c-6b7f-3c41-ba08-a694fd7965de | -1.62557 | -47.05126 | 2025-10-21 05:12:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 00dfb9e8-d8fb-392b-8cdb-5d93ac13711c | -2.84254 | -51.36383 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6d4d0a1-eea3-3c1f-b6c9-e386f76c0903 | 1.72111 | -55.72237 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ceca0fa2-c056-3dfc-a65c-101638720a29 | 1.76158 | -55.67728 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f7f1154-b2f9-35ed-b022-6240e9e81d19 | -2.86565 | -50.73591 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf16802b-453b-305d-9c12-2e27f4edb6fd | -3.49984 | -45.8316 | 2025-10-21 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.9 |


[Clique aqui para ver as próximas entradas](README18.md)
