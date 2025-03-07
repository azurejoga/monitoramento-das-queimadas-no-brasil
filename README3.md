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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bf11291-f947-335d-b05a-8ebf7037f45f | -19.70212 | -44.7752 | 2025-03-07 04:25:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a62ba3d7-15a6-35ee-994e-ef1c944120b2 | -30.37203 | -51.97168 | 2025-03-07 04:25:00 | NOAA-21 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 8.6 |
| a0c8cddc-73c0-3612-8ecd-de980be94fb9 | -19.69796 | -44.77893 | 2025-03-07 04:25:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d36064c4-351b-3b95-a2d7-216551a259f0 | -28.58525 | -49.44335 | 2025-03-07 04:25:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ad168e03-058c-356e-89b0-fccb06ea9df1 | -19.22024 | -43.22808 | 2025-03-07 04:25:00 | NOAA-21 | SANTO ANTÔNIO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3160504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| eb05000f-04ad-33e1-adae-93a1936f10e3 | -19.6787 | -45.38091 | 2025-03-07 04:25:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c6b68d3-4179-3f56-8039-0cfa048c399a | -27.68707 | -48.75145 | 2025-03-07 04:25:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d78d3656-6db3-3ed2-ab44-ba79bebcd0e6 | -25.19366 | -49.32708 | 2025-03-07 04:25:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0f3ac47c-9c31-3d19-97d1-c8ca982f52d1 | -19.22089 | -43.22306 | 2025-03-07 04:25:00 | NOAA-21 | SANTO ANTÔNIO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3160504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4e1a75f6-179a-3c30-966d-9e6cc9b4cfb1 | -18.9779 | -52.31059 | 2025-03-07 04:25:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cd134fc-7cc4-3c98-bdd3-46a40f3d9572 | -19.53431 | -47.35172 | 2025-03-07 04:25:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a23ee00d-a66e-31fd-bacd-b08917401dc4 | -18.91219 | -39.94023 | 2025-03-07 04:25:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e814a634-ec29-3af5-8bf6-2f3a7f5653c2 | -26.95004 | -50.77081 | 2025-03-07 04:25:00 | NOAA-21 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5e8c8d48-cc5c-3806-a2ae-0e72fcbcbeba | -23.73667 | -53.2457 | 2025-03-07 04:25:00 | NOAA-21 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 22280405-0884-36e6-9c9a-ea77da5ae34d | -29.58139 | -51.98457 | 2025-03-07 04:25:00 | NOAA-21 | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a15eb49d-8b54-33d5-b24d-bea4cb2018fa | -28.08799 | -51.44646 | 2025-03-07 04:25:00 | NOAA-21 | CAPÃO BONITO DO SUL | RIO GRANDE DO SUL | Brasil | 4304622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5f8e492f-02c2-3254-911a-6318e93a7ea5 | -18.98175 | -52.31136 | 2025-03-07 04:25:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab8cd3ea-e697-3bda-859a-42e00961034d | -26.67019 | -50.65103 | 2025-03-07 04:25:00 | NOAA-21 | TIMBÓ GRANDE | SANTA CATARINA | Brasil | 4218251 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b5b4cbd5-f053-3fbe-8b57-62dfd959c279 | -29.77956 | -51.17491 | 2025-03-07 04:25:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| dc0323cf-694d-3d48-a5d8-7e34b02b81bb | -26.78382 | -51.28376 | 2025-03-07 04:25:00 | NOAA-21 | MACIEIRA | SANTA CATARINA | Brasil | 4210050 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 01febb16-fd7a-3628-9f82-43dec6e5378e | -28.9391 | -51.40096 | 2025-03-07 04:25:00 | NOAA-21 | NOVA ROMA DO SUL | RIO GRANDE DO SUL | Brasil | 4313359 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e4e79e1-84bc-36b8-b34e-6d0ea30003de | -25.32296 | -52.02056 | 2025-03-07 04:25:00 | NOAA-21 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c8497d98-ddc4-369e-bef7-730c872832b7 | -27.59186 | -49.97551 | 2025-03-07 04:25:00 | NOAA-21 | OTACÍLIO COSTA | SANTA CATARINA | Brasil | 4211751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ebe6d533-eca2-3657-8040-d3bc47c3be9f | -27.72287 | -50.07273 | 2025-03-07 04:25:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 805f23c1-9c00-37b9-bd80-3c9381f6a9d1 | -19.53375 | -47.35538 | 2025-03-07 04:25:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb744fd9-d395-3c2d-a58f-f54783ee46fa | -19.531 | -47.35115 | 2025-03-07 04:25:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8d199547-9a93-380c-b71b-5af734db0d0c | -30.36868 | -51.97095 | 2025-03-07 04:25:00 | NOAA-21 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 8.6 |
| 1eab438b-0abe-3342-9c7a-5c244faa1057 | -23.79387 | -47.81834 | 2025-03-07 04:25:00 | NOAA-21 | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cd2f54e4-14ba-3f6e-b163-12810f33b286 | -19.58707 | -44.8746 | 2025-03-07 04:25:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0088c17-8ef7-33a6-a250-65e7771ca62c | -24.6627 | -51.14942 | 2025-03-07 04:25:00 | NOAA-21 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 07bed8d8-5c23-3dea-a5a9-32767ebbedf2 | -27.01926 | -50.84566 | 2025-03-07 04:25:00 | NOAA-21 | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e03c0732-7e26-3773-acdf-4cdfe86233d8 | -27.59517 | -49.97617 | 2025-03-07 04:25:00 | NOAA-21 | OTACÍLIO COSTA | SANTA CATARINA | Brasil | 4211751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3696062c-9326-3d44-8efa-6ebebda7411b | -30.85131 | -52.22359 | 2025-03-07 04:27:00 | NOAA-21 | AMARAL FERRADOR | RIO GRANDE DO SUL | Brasil | 4300638 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 70e841a2-36c4-3074-9cb4-61eb760c0c12 | -30.30106 | -54.99281 | 2025-03-07 04:27:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| e1211cc6-c0a1-3a09-af6b-5a3474ebc07d | -22.60225 | -42.0853 | 2025-03-07 04:46:00 | AQUA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 94099181-d031-3500-9c4e-b4269ddf100e | -12.49286 | -46.91907 | 2025-03-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15ff3d6d-8f84-3729-a1e3-406d1555e917 | -10.71839 | -42.33152 | 2025-03-07 04:46:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a75a9bb8-d553-350f-bacb-784898a74d7f | -12.90796 | -45.07285 | 2025-03-07 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6b6334f-8a4b-3094-98d4-9de30e8bc56f | -10.39383 | -47.99033 | 2025-03-07 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23aa95a0-3104-3585-9e2b-7108b660fc34 | -10.71322 | -42.33186 | 2025-03-07 04:46:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9cf20a21-cb47-3986-a787-02be07187b3d | -11.82361 | -47.08077 | 2025-03-07 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02450084-f7eb-3363-93c6-7af5309aaaef | -10.7243 | -42.3333 | 2025-03-07 04:46:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3fabe124-21cd-3c9e-b6d7-44d6c0eaf65f | -12.84974 | -43.82961 | 2025-03-07 04:46:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 361b154a-77ad-3675-82a9-5a4806efefbb | -10.53409 | -44.66544 | 2025-03-07 04:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6230fb26-c1d9-3679-ac0a-33bdd7a69283 | -12.91136 | -45.08373 | 2025-03-07 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be8ffee3-f2e7-37b8-a9e2-cdc9076962d9 | -10.71369 | -42.32819 | 2025-03-07 04:46:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 59b1f428-b7a5-3efe-bda3-97a9263d672c | -11.82769 | -47.08136 | 2025-03-07 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1abad529-257c-355f-9583-5f7e47907c9c | -10.39826 | -47.98637 | 2025-03-07 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca72b040-8679-374d-85ed-ee21fbce0d20 | -12.27469 | -44.98419 | 2025-03-07 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 67cef121-f576-3527-ad86-1ea7f320c61a | -10.72438 | -42.32859 | 2025-03-07 04:46:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7522bfb9-1d84-3de8-b67f-555111b80b98 | -10.66142 | -44.40225 | 2025-03-07 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4de88d49-5bb0-3f6a-88e4-6356308acd50 | -10.39448 | -47.9858 | 2025-03-07 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb312e3d-2a62-3394-961d-da8a8e57e746 | -11.57592 | -47.63345 | 2025-03-07 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8b00006e-65a3-3092-82fb-1bd9c5844528 | -10.71284 | -42.33079 | 2025-03-07 04:46:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0b209596-f4cf-3c10-8181-5291757ff870 | -12.90729 | -45.07797 | 2025-03-07 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61956ea0-6360-3147-8654-161fc6b0c1f7 | -10.39762 | -47.99089 | 2025-03-07 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d9bb5fb-cae3-36fb-9478-f8134f7eae89 | -12.84459 | -43.82892 | 2025-03-07 04:46:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71f6b01a-105f-3dad-9a40-c5de3b7a7bc6 | -12.47468 | -46.91714 | 2025-03-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ec27421-fdd3-3c65-bf50-f5f3288b2e50 | -10.72393 | -42.33226 | 2025-03-07 04:46:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c702fcad-e3cc-391b-b230-394c56d7029e | -10.71876 | -42.33257 | 2025-03-07 04:46:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b58e4e87-027c-3cb2-8650-8e69f24f1268 | -12.90661 | -45.0831 | 2025-03-07 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e36d098-598a-3855-b8de-2820c7632ca8 | -12.84419 | -43.83205 | 2025-03-07 04:46:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e67177db-fb91-3366-a63a-3a0ee28a3153 | -10.53881 | -44.66609 | 2025-03-07 04:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08d9067a-e8a9-3614-a6d6-0c7aa4545b91 | -12.47622 | -46.91665 | 2025-03-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4ce9115-a63a-33ca-b155-ff0679ad3905 | -12.30511 | -47.27142 | 2025-03-07 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c64a3aaa-2e41-3bd9-a253-421f7ff0397e | -12.91203 | -45.0786 | 2025-03-07 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95bb9724-2b42-33e8-aba4-4836d1e4b6a2 | -12.30157 | -47.26725 | 2025-03-07 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 528043f5-4f40-365a-a935-7d2fb1c24445 | -10.72477 | -42.32963 | 2025-03-07 04:46:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2bfe23fc-1e31-336f-8018-932f9bac53cd | -15.29384 | -47.88054 | 2025-03-07 04:48:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e7cde70-b7ad-39e2-9d08-50ef9e115b21 | -15.56903 | -46.26934 | 2025-03-07 04:48:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03ddc498-8500-3417-9b66-98e28e1fb4be | -13.53657 | -47.93255 | 2025-03-07 04:48:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bccb053f-494b-3eb2-9d1f-d219db7087cd | -15.07972 | -48.94654 | 2025-03-07 04:48:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 460c6aec-b54c-319b-b359-70f318788879 | -18.60933 | -44.2607 | 2025-03-07 04:48:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a80dfddf-3bc1-31c8-8579-ea74332af89c | -16.10168 | -60.05304 | 2025-03-07 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8066ab4-f504-3e9f-b728-2a258810ef69 | -15.29793 | -47.88098 | 2025-03-07 04:48:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71868cc8-1d91-349f-bc9b-8393dd87ca4d | -13.54051 | -47.93322 | 2025-03-07 04:48:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1747845f-dc87-353a-9873-78864e84b104 | -12.77538 | -48.19564 | 2025-03-07 04:48:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7501333-6e09-3c29-a7dd-e73d7b3716b3 | -16.03897 | -43.80669 | 2025-03-07 04:48:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 897eb002-0d51-3d0c-8f9a-567dca40a184 | -18.61009 | -44.25352 | 2025-03-07 04:48:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 25b489c7-8bb6-3eee-8388-03fc38117fc3 | -16.10978 | -47.98119 | 2025-03-07 04:48:00 | NPP-375D | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6fbea109-0d0c-375e-9c67-6aaf2e4120e6 | -19.21951 | -43.22373 | 2025-03-07 04:48:00 | NPP-375D | SANTO ANTÔNIO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3160504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6960a16a-1702-39bd-8ce7-92a241f3910d | -15.29434 | -47.87683 | 2025-03-07 04:48:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a84e990-649f-3995-89c0-f8429f4e02aa | -13.72377 | -47.70837 | 2025-03-07 04:48:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8cca2ff-1295-304d-9ed9-576478bd476f | -16.04438 | -43.80722 | 2025-03-07 04:48:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9f2e941-1f17-3a16-b090-ae96e357559f | -13.36264 | -47.02385 | 2025-03-07 04:48:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2bde392-23b7-39e0-8e2e-c6cd7935d780 | -13.72775 | -47.70923 | 2025-03-07 04:48:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ec40531-2a1a-3cae-b1fb-1a0ddf78275c | -18.6097 | -44.25712 | 2025-03-07 04:48:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 862bf638-2606-3b0a-96c3-1892403d9506 | -15.07593 | -48.94595 | 2025-03-07 04:48:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d8904c6-0fe7-3e1b-b030-365a3e45bbe5 | -16.10613 | -60.05391 | 2025-03-07 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a9cce6b-9cc6-3e57-9886-358b9d83c431 | -17.72025 | -54.08549 | 2025-03-07 04:48:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eca34519-ad1f-3b1e-bf02-a91cce94ffc7 | -19.89641 | -43.96275 | 2025-03-07 04:50:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 5e9f7d1d-e137-30b0-9b50-4ec1f39aa724 | -24.93636 | -50.93056 | 2025-03-07 04:50:00 | NPP-375D | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1bdeb3ba-8d24-3f4c-b385-ec7784c97171 | -23.73586 | -53.24318 | 2025-03-07 04:50:00 | NPP-375D | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| fd8c1a92-c6de-3db3-bfac-d51612da85a4 | -19.6967 | -44.77668 | 2025-03-07 04:50:00 | NPP-375D | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 576cb29d-13a6-3b76-8e07-6d69dabe526e | -19.67973 | -45.37796 | 2025-03-07 04:50:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6432a206-f54e-33b3-b786-f20a4b374e98 | -21.58509 | -57.58123 | 2025-03-07 04:50:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f71ad22-c7d4-3327-9950-04c29ca45ec8 | -25.32353 | -52.01823 | 2025-03-07 04:50:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 056572b0-4ac6-302a-9585-f1e30c998bca | -25.14472 | -51.34687 | 2025-03-07 04:50:00 | NPP-375D | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| afb132d0-19e7-3a34-81c7-d48670a063ee | -19.53072 | -47.35228 | 2025-03-07 04:50:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36d5580f-9035-3655-932a-0d8086847b08 | -23.19873 | -50.80843 | 2025-03-07 04:50:00 | NPP-375D | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README4.md)
