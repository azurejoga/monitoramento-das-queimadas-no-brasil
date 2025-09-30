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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e5f8b74-b09e-3991-b35b-870c9d1e34bd | -14.68515 | -48.17242 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e5aadcc-3be5-38a0-9f73-9255b01bbdee | -13.81349 | -47.9581 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b71afa16-f907-3f51-bf7b-da0ab843757a | -13.37525 | -43.72663 | 2025-09-30 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c60a6e0b-6482-3360-ad74-53a9daa61612 | -14.50802 | -48.42406 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28e27a74-dab8-39d0-820a-ffd5ce923570 | -15.30161 | -46.41121 | 2025-09-30 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75b81dd7-9003-3089-8498-3b13477b85d4 | -13.74014 | -47.90639 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2b827e1-c6fa-3811-8210-259db74bee18 | -11.87717 | -48.05019 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12bf82a1-1224-3cfc-99fa-95addd29498c | -18.46376 | -43.24957 | 2025-09-30 03:49:00 | NOAA-20 | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6da1e7c8-b289-3b26-a74f-f5fc57d2a9e5 | -15.85802 | -46.24436 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85aa2f1f-bac2-3061-ab27-9487940a874a | -15.33217 | -47.92664 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e054c76-2703-39ec-9b3d-e6ed56a9612e | -17.85282 | -39.70032 | 2025-09-30 03:49:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 83915c87-e91f-37d7-a41a-e1ea6fa104ec | -6.08312 | -42.44286 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fbb765d0-7aa3-359b-b454-4de1d6d3530b | -6.7666 | -37.89503 | 2025-09-30 03:49:00 | NOAA-20 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 89a771b7-d686-372f-a8b4-c7bb9a47972e | -5.7091 | -42.67497 | 2025-09-30 03:49:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 30c19db3-dcba-3040-bfa5-a7bb21b816a1 | -18.12369 | -47.78563 | 2025-09-30 03:49:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cc03c12d-ba1b-3d8b-80c3-5c6c9c327b07 | -12.75254 | -46.86758 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21ce3c7a-43c6-3a87-af9b-2a0f8c991da6 | -6.37162 | -45.62724 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6a9b3f8-01e4-33c5-bdfa-28e4885a2985 | -13.20646 | -50.95428 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 5738a5a9-d625-3e54-a78f-7b0af22a0025 | -6.3694 | -45.64018 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2153515b-39e8-3b3a-871f-827d1c13f3aa | -13.7832 | -47.94194 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 80a778cf-493c-3c9f-b692-1365c21ead18 | -13.21415 | -50.95012 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 835ef685-ecdd-3751-bd86-d199e27db880 | -15.90508 | -46.22382 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1b71d590-7127-3a03-8af5-32eb16daf5eb | -16.85385 | -41.14325 | 2025-09-30 03:49:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ca161e16-7bd0-3d9b-b51b-d75b7871fae4 | -11.75872 | -44.74385 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 368019a8-5740-3e4e-b3f9-b23aebeff518 | -7.51758 | -45.44057 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 655374bf-ddc8-36d9-808e-f541c6fed590 | -6.04927 | -42.46724 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 68081a26-8049-320a-8c30-e73422b763b9 | -15.3918 | -47.07022 | 2025-09-30 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f68ec0e-990d-33f9-a537-cd6027c6c6d9 | -13.7159 | -48.64475 | 2025-09-30 03:49:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f391eeda-9df1-3a9f-95c5-d4062b0a4081 | -12.83993 | -47.00333 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d1b98e2-8c60-3fb3-bc64-9fcffa422e64 | -7.28603 | -42.849 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d3f2970-0c9b-38b9-af03-77b1b47b42c1 | -14.38066 | -47.13791 | 2025-09-30 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 255f2d04-72f9-38fc-8607-da1072789199 | -18.70756 | -43.19003 | 2025-09-30 03:49:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e73dfb86-259a-3fb9-9783-ca40232ade47 | -15.04078 | -46.98944 | 2025-09-30 03:49:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89d75405-9319-31cb-a98c-add668a67c23 | -14.54751 | -48.48447 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ba858d12-266b-384e-bdfa-db2db76e3962 | -15.49797 | -48.55507 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 50bf9fe8-33d2-3adc-b216-19a4484f602d | -5.81779 | -42.85818 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3bf5443d-f171-3413-ab1d-aeefe2b398a9 | -11.19944 | -47.22123 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 587b8def-7f23-30c6-94b1-fc4a4bb80223 | -6.11803 | -43.21988 | 2025-09-30 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 98e0d24f-ae19-36d7-83b7-fb494221d4bc | -6.09526 | -42.65725 | 2025-09-30 03:49:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7a2a3331-fc1a-3f58-ae7a-8a33ce4c7446 | -17.17314 | -42.83886 | 2025-09-30 03:49:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ebf9cca5-347d-3ec4-8d8f-1223b272306e | -13.00568 | -49.43994 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25887f5e-b769-307b-80b3-4208ba630c31 | -5.85069 | -50.07132 | 2025-09-30 03:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8489ef7-0e8e-3e28-8005-d098e1470335 | -18.30379 | -43.26703 | 2025-09-30 03:49:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 727bd7d2-33c4-321d-a3e5-92ce9992861c | -5.21622 | -45.23103 | 2025-09-30 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a8976909-5c1d-33d1-b659-feab85194522 | -13.07509 | -47.07417 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7abf77e7-96df-3e0a-914d-d8f488e7efe9 | -13.72701 | -48.64761 | 2025-09-30 03:49:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eef5fce4-4dde-3fcf-93e8-dbee0ffcd355 | -13.36812 | -47.32275 | 2025-09-30 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 072e0eeb-253d-3943-9650-f10753d457ae | -6.07499 | -42.61984 | 2025-09-30 03:49:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 636275aa-ba6d-3015-976d-22478b983eb4 | -13.81258 | -47.48951 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8dd87e4b-0ca8-3ee2-8da0-716f68fcfbdb | -6.10347 | -43.47338 | 2025-09-30 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2df7b7cd-2d11-313c-a798-a01a62b3d7b8 | -11.69325 | -44.31079 | 2025-09-30 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a7ddf01-706c-3183-b785-2fa4b8e14c7f | -12.84014 | -46.97508 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d3e79d1-358c-397e-bd78-a2ca8a59c666 | -15.77546 | -43.67564 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e293738e-4ab3-3e2e-9f59-31c8fc9e7dcb | -12.66407 | -46.874 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f9b2c86-7cfb-35e1-ac32-5feaac1e1f9a | -16.40422 | -43.72394 | 2025-09-30 03:49:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61adc9bf-86a2-355d-9ded-85173195c040 | -5.69325 | -42.6023 | 2025-09-30 03:49:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 55413081-15e6-36bd-8d19-9a32f4c33261 | -18.05977 | -41.67468 | 2025-09-30 03:49:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 16d19981-cde3-3b58-8be8-5f3f6d08c23a | -12.86444 | -46.90503 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21465cef-a933-3730-9e39-ba7ed1aacd68 | -14.61247 | -48.30157 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf38bb1a-76e5-3d98-a60a-18622516a9b8 | -6.36745 | -45.62012 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1f4429a7-08ea-32d9-bebe-efca1eea963e | -12.23186 | -47.8 | 2025-09-30 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d4fe880-9711-35d3-9ed9-09f547902408 | -13.82101 | -47.47378 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65575fbc-6525-326c-9b64-2d355f586dc9 | -14.72789 | -45.22263 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f26c2bd0-d60f-3877-be3b-20aef8cdeceb | -17.49589 | -43.48187 | 2025-09-30 03:49:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bdf198e5-4bda-3cf7-8f1a-a076e8b6ab36 | -6.05216 | -42.47023 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6182b554-c9a2-37cd-9caa-a3a8ab3d2577 | -15.2816 | -47.85507 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0ea3cf86-1c99-336c-b797-045dbbc16fce | -14.54469 | -48.26647 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e02e7315-7b9e-359d-b4df-b2bf1ea9f9d0 | -6.15227 | -43.89896 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 248fe0b0-0259-3cad-8e37-28bcc8e179bb | -13.40542 | -47.54767 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fa09691b-8362-3b47-ba43-704c29cf8a7f | -11.66104 | -45.32346 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23cfd3ee-b8de-35fb-9186-429340d5263d | -13.7533 | -47.92413 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7a88d99-a871-3e19-b312-05589fb90d5e | -7.79481 | -42.51313 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 41151e06-e016-3b7d-a560-33c7cd8198ab | -15.66162 | -45.24732 | 2025-09-30 03:49:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20952ad4-1d70-3760-b9eb-77e6f1a25e12 | -13.62972 | -42.53719 | 2025-09-30 03:49:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 10ca895e-b3b9-35a1-a199-d71b9a646005 | -12.74518 | -46.85114 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 063f475e-cd46-3dbe-bf95-1df118cdfc4c | -12.82307 | -47.00771 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dbecb011-b26f-3703-94aa-616a3a2b1c48 | -12.3683 | -43.20441 | 2025-09-30 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6df470c8-d316-32d2-a8f6-b808071c436a | -6.79517 | -45.9766 | 2025-09-30 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1bf50561-8eca-390c-8b02-c86fa30f450c | -14.5126 | -48.46001 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6838409f-98cc-32e5-b02e-394a86dcab63 | -13.62902 | -48.03057 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 816a1274-6252-3df3-8eb8-e9a6ce979279 | -14.7012 | -48.23115 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8dc812dc-8c0d-3a06-bc8f-06d49da540b7 | -13.39133 | -48.07546 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6d68eb1-4115-39e7-81da-ea14f8a78171 | -15.12566 | -48.38929 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff27ec5b-f7d8-368a-b055-31f3a27caffa | -13.35238 | -47.84365 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ca89565-8c9c-3309-8725-64fb125c2de3 | -19.30432 | -43.81581 | 2025-09-30 03:49:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 521eba18-6328-387a-944d-2d66998f3b62 | -13.57014 | -48.0946 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba062f9f-2efc-3353-b517-9b71a25ead40 | -16.52699 | -49.43629 | 2025-09-30 03:49:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9042403-d9ed-3f4f-bad9-faeabb3b6481 | -19.33221 | -43.81205 | 2025-09-30 03:49:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 394ca4ba-99fb-3090-96e4-24586b5ebd67 | -13.23623 | -48.45485 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 85820e8a-2909-3011-8913-a0cfb98ff261 | -12.95011 | -48.40709 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12ddcbef-eaa4-3a6c-b056-a42b72cd8893 | -15.2303 | -50.09357 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8ac3752-5b89-341c-9979-fd8bafb61114 | -13.80645 | -47.96548 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c09911e1-8b86-3db8-a89b-3da69fef95e0 | -14.50846 | -48.42459 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51ef7dc7-fdf1-3f85-8de2-c4afbfc96d59 | -15.06803 | -45.05362 | 2025-09-30 03:49:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf592216-b965-367c-b6d4-460a90d3d3cc | -13.65169 | -48.05801 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de352e46-8379-3fdb-b679-88a16b5701b3 | -16.52781 | -49.43239 | 2025-09-30 03:49:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 416aad47-c492-3aa6-ab3d-ac096d1ce783 | -12.36765 | -43.20806 | 2025-09-30 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fabf4e76-98d2-36f1-8a81-cda924393cc7 | -15.87438 | -46.20911 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2ae2915-5476-3952-902a-b2c43eac5b11 | -5.75093 | -42.66521 | 2025-09-30 03:49:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9114ea1b-c929-3d8f-a4ef-6cc0a2fe91dd | -12.89145 | -46.76623 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README31.md)
