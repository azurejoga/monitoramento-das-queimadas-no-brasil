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
| 00762dcb-ad70-35ac-8b50-fd2175a94a5d | -10.3435 | -44.807499 | 2026-01-15 00:16:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ee726775-65e2-303a-9d9d-26fd0f2df250 | -6.8862 | -42.837502 | 2026-01-15 00:16:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0724549c-7f5d-35a4-9666-3960f759e458 | -14.1705 | -43.703701 | 2026-01-15 00:16:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad9d3541-4eb3-326a-a947-6be477edf645 | -7.2374 | -43.053799 | 2026-01-15 00:16:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cf32eca4-d41c-3b13-9d2e-14ac9bf0cc56 | -14.4007 | -44.5714 | 2026-01-15 00:16:00 | METOP-B | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1628aaff-1a97-3e6b-b519-27d307f08bdf | -7.234 | -43.039902 | 2026-01-15 00:16:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 102000e5-135d-3359-9baf-a76f47d84578 | -10.599 | -44.968498 | 2026-01-15 00:16:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 07eed241-426a-3ef2-b40c-88d17b5f1bc6 | -12.0921 | -45.294899 | 2026-01-15 00:16:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ec43b42-6c5f-33c9-93e9-8d2a1125fffb | -13.7438 | -43.651001 | 2026-01-15 00:16:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b28dddfd-0ff7-31e5-83f9-0ffc04b5c85c | -12.6601 | -46.748798 | 2026-01-15 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b29ebcf-878a-3ff6-afb1-89256676cac4 | -7.2471 | -43.051399 | 2026-01-15 00:16:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6a6718d6-0df3-3e02-b86a-65e72af4171e | -7.0505 | -43.942001 | 2026-01-15 00:16:00 | METOP-B | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 334750e9-340d-3f47-8ba5-5d1bf2626736 | -12.124 | -45.560101 | 2026-01-15 00:16:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cfe234f0-305f-335b-b055-a9caefbd2e7b | -12.6618 | -46.756302 | 2026-01-15 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 726923aa-0ed3-304f-98dd-a1e7e189231e | -12.5064 | -43.666199 | 2026-01-15 00:16:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c13ab93-8492-3e5d-9597-7e4ed0a60c5f | -27.7841 | -50.5084 | 2026-01-15 00:16:00 | METOP-B | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| df1beae4-6081-3bf5-ac58-b4aa5752946a | -14.7694 | -45.9147 | 2026-01-15 00:16:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f678c752-1f79-3147-9f63-a93e9315e11d | -12.126 | -45.5686 | 2026-01-15 00:16:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 735d0514-f183-3708-bcd4-10b799e2ce8e | 4.0578 | -61.4661 | 2026-01-15 00:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 40.9 |
| d9d40108-3f8f-3566-9223-ae6252a69c96 | -7.2411 | -43.0428 | 2026-01-15 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 09b08e4d-6a69-3df2-8c86-0e62225cd06c | -4.372 | -37.8918 | 2026-01-15 00:20:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 77.9 |
| f7cb3bd4-cf7e-3a76-b6cc-372950ebf0ab | 4.0578 | -61.4661 | 2026-01-15 00:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 2aaf65fe-81eb-39a7-8e23-246e6598d901 | -7.2411 | -43.0428 | 2026-01-15 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| f3af557b-383a-3e0c-8d1e-79ce2f04670a | -4.372 | -37.8918 | 2026-01-15 00:30:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 83.4 |
| d4b43c11-e6de-3754-bb07-a948d89871a6 | -4.3718 | -37.9175 | 2026-01-15 00:30:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 80.6 |
| c59cd9e4-f7d4-3ae6-aba7-96d8d51e1127 | -4.372 | -37.8918 | 2026-01-15 00:40:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 8998571e-3420-3b0b-bb07-ce8fb7621cc1 | -4.372 | -37.8918 | 2026-01-15 00:50:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 71.3 |
| d42e7d24-6911-3de5-a612-baf80d86ef8d | -4.372 | -37.8918 | 2026-01-15 01:20:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 3385daa2-c01d-3091-b237-cfe204fdf9ec | -4.372 | -37.8918 | 2026-01-15 01:30:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 68.9 |
| d6621601-8387-3f0a-bd99-1aceb39f7627 | -4.372 | -37.8918 | 2026-01-15 01:40:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 9a32fea7-8a5a-3cd3-801e-4d03a259e121 | -4.372 | -37.8918 | 2026-01-15 01:50:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 82.7 |
| cf430153-78d1-3427-a67f-354d71e87374 | -4.3718 | -37.9175 | 2026-01-15 02:00:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 40e8ea18-4690-313c-8789-244b5024471f | -4.372 | -37.8918 | 2026-01-15 02:00:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 1211e22a-5723-3c4a-9375-4a6892532dfd | -4.372 | -37.8918 | 2026-01-15 02:10:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 79.8 |
| b3f21c47-be5c-3317-b1cd-935161a54be4 | -4.3718 | -37.9175 | 2026-01-15 02:10:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 21b71709-02b9-3760-baf6-284ddc4dc5f0 | -4.3718 | -37.9175 | 2026-01-15 02:20:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 80.5 |
| ae931f69-d690-3e98-be55-4d8439a9b1bc | -4.372 | -37.8918 | 2026-01-15 02:20:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 402f1b5f-4660-3037-8f7b-0492501d1ce2 | -4.372 | -37.8918 | 2026-01-15 02:30:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 49215cb2-a7a6-333a-9734-1b72116b0a5d | -4.3718 | -37.9175 | 2026-01-15 02:30:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 69.9 |
| c9c10627-e9c8-3416-afed-0a8cba558170 | -4.372 | -37.8918 | 2026-01-15 02:50:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 114.8 |
| e5d898fd-48bb-3e8c-ab33-cfbb7a8d60d0 | -4.3718 | -37.9175 | 2026-01-15 02:50:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 81.5 |
| 5d24cb72-c364-3770-829c-9f571b6472ba | -4.3718 | -37.9175 | 2026-01-15 03:00:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 5fe3cd9e-07c7-3909-953b-5127a43b40a3 | -20.41 | -57.8323 | 2026-01-15 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.8 |
| 2b08c96a-6f1c-3524-ac08-6a5dd53943bb | -4.372 | -37.8918 | 2026-01-15 03:00:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 106.5 |
| 39584472-1feb-382d-8df0-8979cc387699 | -4.3718 | -37.9175 | 2026-01-15 03:10:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 99.2 |
| 020ab731-84bd-3ab3-baa8-936a49c86a76 | -4.372 | -37.8918 | 2026-01-15 03:10:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 124.2 |
| d404af6b-c533-3e3b-9232-4c5c74639522 | -4.372 | -37.8918 | 2026-01-15 03:20:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 753c7da9-7ead-3340-ba99-03ce3976bede | -4.36782 | -37.90407 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 27.5 |
| e371c943-7e6a-35bb-b99a-1ce8555c2bf4 | -7.22828 | -43.05565 | 2026-01-15 03:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 15b81ef9-ecef-3a08-aa71-6bd49e6357d6 | -4.37326 | -37.90503 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 27.5 |
| d15a1cbc-7736-3684-b2ce-c04a243b632b | -4.36878 | -37.90433 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 25.3 |
| b1a08f53-7219-3a5f-9b65-830edeb1549d | -4.37543 | -37.89832 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c91742b5-bb8c-373c-83ba-816d1e3febf3 | -5.90104 | -42.55143 | 2026-01-15 03:21:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| beee01d7-4041-328f-9f37-c3fc2ce5f714 | -5.0229 | -37.54351 | 2026-01-15 03:21:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 73702f96-84c4-3701-ae8e-118ae8369fe8 | -5.89402 | -42.5499 | 2026-01-15 03:21:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e1cb5887-fe2c-386a-ad1a-0ee9d7cdac6c | -7.22486 | -39.94911 | 2026-01-15 03:21:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 48d7616d-9b9f-38cd-93f3-1d5c3edeaf32 | -3.23402 | -41.80258 | 2026-01-15 03:21:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5aab6bdd-ac5c-34e0-b00f-ab47c040e922 | -4.36723 | -37.90758 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 288254e4-fd9a-312c-b91a-e751496c2101 | -4.37384 | -37.90154 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 94c323fc-481e-3cdd-982d-628401561239 | -5.01763 | -37.54268 | 2026-01-15 03:21:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 11.1 |
| c290b1e7-e53a-3a81-bcbe-95d0a0573308 | -2.98497 | -39.96686 | 2026-01-15 03:21:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c7abec97-d90b-3828-a54e-e7b3900ba1bb | -4.37482 | -37.9018 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1226aa45-9c12-36c4-abe3-4edcc5ddeb6d | -3.23025 | -41.80837 | 2026-01-15 03:21:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fc2b2728-91d7-33e7-a6a5-bbda58043905 | -4.36211 | -37.91036 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 001a034b-f389-3930-97ac-1df6c13352ca | -4.37361 | -37.90878 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a3e302b4-257e-3089-a550-ce96cda47782 | -4.36237 | -37.90316 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 509b3806-a4b5-3147-b2c2-71f8f02e0887 | -7.86099 | -39.10004 | 2026-01-15 03:21:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5a021ddc-7ebf-3eaf-9078-b196137425d7 | -4.36817 | -37.90782 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 25.3 |
| ea563d35-f4ce-37dc-8643-cac6822809a7 | -3.24108 | -41.8037 | 2026-01-15 03:21:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6b0bac97-b1d3-3b43-8050-deb2be774ada | -4.3684 | -37.90058 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| dd192c3c-7547-3e88-8754-cbfd7fae644f | -7.24669 | -43.05249 | 2026-01-15 03:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1f40c070-0778-3b28-a155-8989b44d03f4 | -4.36999 | -37.89739 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 55.5 |
| 4ea478e0-8125-34ac-a5d3-f88483a76ef6 | -5.01819 | -37.53947 | 2026-01-15 03:21:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 90f7b8ec-ba8e-3771-be92-f990a80eda56 | -4.3715 | -37.91557 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 505758c9-49c2-3e61-b2ae-063f3535d243 | -4.37442 | -37.89806 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 5c0c4f37-86a6-3765-b5df-e83d39ab65c1 | -7.86167 | -39.09629 | 2026-01-15 03:21:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| edea14e6-33ed-3d14-b4c6-3361f85cd829 | -4.37208 | -37.91206 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 94eda79d-fb06-3dfa-8ffb-7c3b6b309b08 | -7.24387 | -43.05132 | 2026-01-15 03:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| cf09d251-4444-3c19-a928-659150cf0e6e | -3.23852 | -41.80279 | 2026-01-15 03:21:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0c98e691-af56-3c1a-87be-4806b53df42f | -4.36898 | -37.89711 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 2d85568d-381f-378b-9d46-169f0f7eb42c | -4.37422 | -37.90528 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 68ec11b0-1e61-3e5d-be26-a3575df02f51 | -4.992 | -37.09849 | 2026-01-15 03:21:00 | NPP-375D | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4efdd239-f35b-3419-aa72-774b843debec | -4.37178 | -37.91927 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a4cf9571-d86a-34ac-94c3-0ce59b10f707 | -3.23286 | -41.80925 | 2026-01-15 03:21:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b547a90d-1a88-3200-ad37-903650d75c48 | -7.25098 | -43.05272 | 2026-01-15 03:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 2d674a4f-e6d1-36a8-a34a-04e2a9e68ed1 | -4.36664 | -37.91108 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7f884212-7549-3339-bbd6-7ecb6d826264 | -4.37091 | -37.91907 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a20859d1-7cbf-38f3-8dda-a00a790f993c | -7.22142 | -39.95108 | 2026-01-15 03:21:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fd0eb537-b8c1-3ca0-bae0-9af36a4502dd | -4.37267 | -37.90855 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 678b272e-62be-3517-b2b5-a478288afcca | -3.23145 | -41.80172 | 2026-01-15 03:21:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8ea16897-abe2-3392-8de4-bcf172b7ba2f | -7.23957 | -43.05113 | 2026-01-15 03:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 93c511b8-6c5f-3595-b641-8ff9681e607a | -7.24529 | -43.05956 | 2026-01-15 03:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 17a01d0b-bcf8-32a0-96fb-adbb4f55155f | -4.36178 | -37.90663 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 400d7485-9b07-3df8-a57c-defcc754d513 | -4.36755 | -37.91132 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 79af6288-0e1e-36f5-b560-a21f0e51f2e9 | -7.24252 | -43.05841 | 2026-01-15 03:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c22f463a-d492-316c-a0dc-b8c2b07da586 | -7.2354 | -43.05703 | 2026-01-15 03:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 089ac186-ee5b-3e47-8287-201da345bd11 | -4.36272 | -37.90689 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 269e1275-0aa3-3a17-a861-3867889c6b66 | -4.37239 | -37.91577 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 11bdf321-3452-3c03-93ce-45ae9c191df3 | -4.36694 | -37.91483 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7b2b009d-ea21-3aee-a620-26d0dd381661 | -4.373 | -37.91228 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README3.md)
