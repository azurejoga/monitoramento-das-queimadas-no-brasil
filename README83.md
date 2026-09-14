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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9599ef7-8f43-3c0b-8b89-c492d4d802c4 | -16.65294 | -41.15306 | 2026-09-14 15:46:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 0550091c-f23b-3ba0-aab2-07a1cc3ee447 | -11.21402 | -43.44911 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1fea4ce3-cff9-3b55-9e2a-9c66c1c24af2 | -11.49951 | -45.75423 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 30a8a230-549c-37fe-a12f-19e017f287d0 | -14.06171 | -40.75193 | 2026-09-14 15:46:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 60bd6ffe-460f-3763-a869-1a2d08aaceb3 | -16.51266 | -42.49117 | 2026-09-14 15:46:00 | NOAA-20 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2e6f82b-f349-3440-8c97-a8e4dea0c120 | -14.20675 | -42.1057 | 2026-09-14 15:46:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bf03dcec-9d1c-3afa-9021-e85ad49d7731 | -12.83591 | -40.32456 | 2026-09-14 15:46:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| fd0a169d-e938-3c96-a3e4-dff7a69ebd04 | -10.32565 | -45.29714 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 8a74960e-74e4-31ca-94ca-20cc8cc24903 | -10.30209 | -45.33041 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 877acb3b-dbab-3406-bcad-c79d699271b8 | -14.35381 | -41.43024 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3f7325d1-840e-39e0-8ae0-c8626a285481 | -14.34787 | -41.42774 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 50.0 |
| abc60322-1929-3108-992e-70b2adfbcc99 | -14.34273 | -41.43227 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 50.0 |
| 5f646301-16a7-3337-abea-f38113c225c6 | -16.00298 | -40.68477 | 2026-09-14 15:46:00 | NOAA-20 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 19fb48be-117f-3816-a25d-88bf21d838c4 | -14.27638 | -44.79044 | 2026-09-14 15:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c0cf45a4-368c-34dd-8201-f0061140a12c | -11.50587 | -45.76675 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 7338a138-6986-3920-b7f6-9faab454a240 | -12.64042 | -40.904 | 2026-09-14 15:46:00 | NOAA-20 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 487fdf32-be98-3831-bd5e-51ef28291c66 | -11.56135 | -42.83062 | 2026-09-14 15:46:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3505cb89-24c2-3602-abc4-807842bd1c1f | -11.56311 | -42.8312 | 2026-09-14 15:46:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ace3adbc-a988-3fa4-85fa-84e12b743743 | -15.02292 | -41.45755 | 2026-09-14 15:46:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a908a150-5fbc-3556-9ecc-7effe2301a2d | -16.48306 | -43.42058 | 2026-09-14 15:46:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| adffb9fb-4405-33be-bf4e-dd55c8ce3549 | -11.1139 | -40.47768 | 2026-09-14 15:46:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 31.8 |
| 2e950bae-efbe-38ac-bf3c-0ef85e360da0 | -13.43886 | -43.82642 | 2026-09-14 15:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 0fc7ff02-8713-3eea-b7e6-e2cc397fa4ba | -11.33079 | -41.4887 | 2026-09-14 15:46:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bbf960e7-4473-33e1-bdd3-2e7a8c08c816 | -15.32649 | -42.49554 | 2026-09-14 15:46:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c94ff2cc-fc22-3fda-b522-3c549b984298 | -12.39522 | -44.39199 | 2026-09-14 15:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ce39e9bf-3ea4-3670-ae11-22be61d7dcc6 | -10.3173 | -45.28421 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 91ed7b1e-2e2d-3523-988c-ae673185068f | -10.81606 | -46.25865 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 906d42d6-671e-34bb-93ba-b3395b3f70f7 | -13.52421 | -44.6235 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 809641d3-30ec-3bc2-8bb7-167eecf96ddb | -9.26569 | -35.62318 | 2026-09-14 15:46:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| ad6c7b3b-7fc6-32ad-a78a-205dd81f50e2 | -11.29873 | -41.60474 | 2026-09-14 15:46:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8e6bafff-9d67-3e17-a8a1-390adfd51409 | -14.38462 | -45.25361 | 2026-09-14 15:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 973cd7fa-c63f-36a1-bb29-e0c87462b9ca | -12.83625 | -40.32737 | 2026-09-14 15:46:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 4e691c2c-88b3-3bce-89da-fc5068f0a079 | -10.6526 | -41.47351 | 2026-09-14 15:46:00 | NOAA-20 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 8ce4a840-9e8a-3e29-a1ad-c0cfa6574b1d | -10.83052 | -46.29551 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c12f7ff9-045a-391f-9e86-1b5c954b15fb | -11.1136 | -40.4754 | 2026-09-14 15:46:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 31.8 |
| 7c305d4e-6ed8-326c-a1a7-6c55bef43d3c | -16.3054 | -40.51609 | 2026-09-14 15:46:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 57e72ac9-71b7-3763-aca6-0d4b36e150ea | -11.18023 | -42.79276 | 2026-09-14 15:46:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 79810d36-8f13-3896-8df1-2be49ce0b311 | -13.4377 | -43.81574 | 2026-09-14 15:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 97e45c58-3d3a-3821-b04b-882e04fc3d70 | -11.25896 | -41.08181 | 2026-09-14 15:46:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 06a486a2-e640-32a4-8c57-ca0a613fa53f | -11.23251 | -43.44407 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dc66bf2a-083f-3bc7-bb8d-449b7b100809 | -13.2299 | -40.17902 | 2026-09-14 15:46:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ada72af9-d78e-307c-bded-ee7f4def6948 | -14.04086 | -43.84995 | 2026-09-14 15:46:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6e322d89-72cc-3a23-bad4-f0c1974d25df | -14.61382 | -44.6095 | 2026-09-14 15:46:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d2c7ec2-afd8-3f06-b8c9-2699148c4f9a | -10.31875 | -45.29665 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 445bcc79-79f5-3375-ad06-39c8cd16b098 | -16.53287 | -39.81461 | 2026-09-14 15:46:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f3400002-7197-323d-beed-ac69b3d11cf7 | -12.03179 | -40.04105 | 2026-09-14 15:46:00 | NOAA-20 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 165edb74-8ced-3cc4-8fe9-dfbee60c3046 | -14.35995 | -40.43783 | 2026-09-14 15:46:00 | NOAA-20 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4d480f63-05c8-355c-a763-9c855ef72d96 | -11.18069 | -40.52084 | 2026-09-14 15:46:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 28.2 |
| aba93831-e9c7-3cb5-ac99-1cb92e4aa667 | -14.38703 | -45.25376 | 2026-09-14 15:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 378f4c9e-e523-3e3b-913f-caf3276be6a9 | -11.18174 | -42.80541 | 2026-09-14 15:46:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 4e640cdb-7d3a-3477-9fb7-34ed767b9769 | -10.60067 | -41.27874 | 2026-09-14 15:46:00 | NOAA-20 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 0dff51f5-7eac-3a48-b3d4-6943508cbc7a | -11.25958 | -41.08152 | 2026-09-14 15:46:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 9e2084d7-40db-3f69-ba1f-6ea3e4048c93 | -16.43951 | -42.02612 | 2026-09-14 15:46:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 8fedd8d4-668c-3762-a8ef-9d3a976da3c1 | -10.78045 | -46.30426 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 112f6e38-25c8-3959-95a1-28a472202986 | -11.50653 | -45.75336 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| edfcbbfb-674e-3d37-9ee7-286b91d90e43 | -11.82583 | -40.6667 | 2026-09-14 15:46:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 33e00da6-8ccd-3a7b-86c5-7e260cd081b1 | -11.49736 | -45.75394 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e33ad070-c84b-3fc7-9ec7-b3ec1abf363f | -15.99936 | -40.68713 | 2026-09-14 15:46:00 | NOAA-20 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 24babeb4-5569-3298-a731-39e23f5017b1 | -12.37937 | -42.40978 | 2026-09-14 15:46:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e007d8f2-decc-39cb-bb6b-61763f5945bf | -14.16921 | -44.54311 | 2026-09-14 15:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5579a16e-48f8-36a9-a249-8003eda49c43 | -12.47799 | -41.4243 | 2026-09-14 15:46:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| f9a89a26-17eb-3048-beb0-9da18866f44b | -10.80106 | -46.25475 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 20e1eec8-462a-3e00-9ea6-ce90135dffcd | -12.47761 | -41.42111 | 2026-09-14 15:46:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 298d9e69-c3a3-36d4-aa68-f9f1f5dc7baf | -12.1302 | -44.20727 | 2026-09-14 15:46:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 38036a68-3c08-3392-baf4-895027835408 | -15.36323 | -40.86371 | 2026-09-14 15:46:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6e3681e5-1a76-3842-a30c-1c5b3d355de6 | -11.2397 | -43.4527 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| c50bca0b-8238-322d-9708-3a7b921dea20 | -10.63936 | -41.45467 | 2026-09-14 15:46:00 | NOAA-20 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8e937e24-7817-3a06-a5e5-fd0f090d8878 | -10.65665 | -41.47332 | 2026-09-14 15:46:00 | NOAA-20 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 2a55fb60-cdf8-3819-b15f-b051d5377f4f | -14.49394 | -40.30277 | 2026-09-14 15:46:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 0420a2f4-eb5a-39f6-be8d-515f0531437c | -11.52067 | -45.77186 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 29f2ec32-9f75-3527-b302-9c298391ee08 | -12.12956 | -44.2017 | 2026-09-14 15:46:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 865db5b1-0ce8-39af-bc1b-d12085bec6c1 | -14.49021 | -40.27048 | 2026-09-14 15:46:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 828c8104-48f3-3e89-9d8b-e32c7469d2f3 | -15.51927 | -43.84375 | 2026-09-14 15:46:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3ef2e258-3d69-37ad-962e-9066929f28b2 | -15.51437 | -43.86169 | 2026-09-14 15:46:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 3a3113c2-1fbf-380d-9b46-c4359753802e | -11.2458 | -43.45196 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a0e6992d-af90-3a7c-a8f3-489a91d3a7e7 | -14.62498 | -40.73687 | 2026-09-14 15:46:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 57ed8595-fe47-364d-abe4-1bff6d57a38d | -16.30303 | -40.51918 | 2026-09-14 15:46:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| d378e4b7-5825-31cb-956b-b2cc179b53a9 | -13.96772 | -42.45392 | 2026-09-14 15:46:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 29ebe616-edd9-35c9-8ee0-e23acf910816 | -13.27955 | -40.33076 | 2026-09-14 15:46:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 1bca86aa-3243-3093-bb87-65891dbc9e56 | -14.50008 | -40.8566 | 2026-09-14 15:46:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| c12b29ca-932e-3b4d-8743-ceb490c28461 | -14.38194 | -40.34602 | 2026-09-14 15:46:00 | NOAA-20 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0a18119d-e3d7-3804-9e0a-934c540e7eb2 | -14.4997 | -40.85327 | 2026-09-14 15:46:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| bde56e85-3dbb-372b-b586-9ac694c3b945 | -17.16974 | -41.41839 | 2026-09-14 15:46:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 09e4a793-a255-35d9-a504-b241b9d82e7d | -11.2329 | -43.45159 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 7ef587f7-044e-32a0-8cef-b0f02300f74b | -15.99892 | -40.68298 | 2026-09-14 15:46:00 | NOAA-20 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| a73c32eb-51f4-3ac0-8587-9ef26b97df35 | -14.38399 | -45.24714 | 2026-09-14 15:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 77fe1494-0bc1-3954-8b99-7dba2eb76afc | -14.45358 | -41.99703 | 2026-09-14 15:46:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e7edfaf0-604c-3686-8b56-72da4f117a4e | -10.30376 | -45.30894 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7de093e6-3d2b-3743-bb65-152fffc7f5af | -13.55757 | -42.41174 | 2026-09-14 15:46:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| fdd78ba4-32f8-3a7b-a45e-be23433e6e1c | -12.22969 | -39.29585 | 2026-09-14 15:46:00 | NOAA-20 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 17ddf08d-a16f-375d-b34e-7bd1ebd48329 | -13.9604 | -40.70716 | 2026-09-14 15:46:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 43875876-b124-3b5a-861b-07712cb70832 | -11.23916 | -43.44801 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| b1e69240-fb8d-35bf-b407-d7f94717ccef | -10.78844 | -46.24324 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| ecbf3c17-380b-3e51-9db7-a64070ab4f3e | -14.46684 | -41.34871 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| ac61bb9f-1862-3cb2-a487-826c307b98f6 | -11.23233 | -43.44691 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| e99ca1ce-670f-3e6c-8b52-edaf4357da14 | -16.05889 | -40.48288 | 2026-09-14 15:46:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6421a92f-de2e-312e-bd7d-12df9d2186b3 | -14.98561 | -41.03793 | 2026-09-14 15:46:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7efbb6a8-1afd-34da-bc42-e4349b64a588 | -10.65309 | -39.46948 | 2026-09-14 15:46:00 | NOAA-20 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 8848e122-8328-3013-b200-57a3f72a938b | -14.44471 | -40.84947 | 2026-09-14 15:46:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d0f25385-fbe3-34f4-98df-a76a50bb18be | -12.37378 | -39.59035 | 2026-09-14 15:46:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |


[Clique aqui para ver as próximas entradas](README84.md)
