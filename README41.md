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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c765eb1-d53f-3c6a-a07a-c25c05b98a80 | -14.9117 | -46.81041 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21f2d911-b5b1-32ae-9095-00e590fa9f40 | -13.37969 | -47.75372 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23d4b95c-bfa9-3546-9e63-716c311fb998 | -14.8412 | -48.46213 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ff61acc-c722-3674-8d8b-3fe46f6fd91f | -13.35898 | -47.60143 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cd4472d-5221-3638-a60a-f86c7155c610 | -14.43655 | -47.97258 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6de1ab5-2349-3875-a378-069f6cba0218 | -14.26748 | -45.91533 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 85252e10-d741-36cc-88d0-f5144f712185 | -16.19868 | -59.33978 | 2025-10-10 04:53:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a3b14eb-d5ab-3b88-b7a3-6c0e5f3d37c9 | -13.34901 | -47.74848 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 296c3795-4494-3c40-ac99-9b62535cc9c5 | -14.98769 | -47.19695 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2402cd0-9866-3523-a74d-ca19c019732a | -13.38024 | -47.74955 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f8b0bc2-5434-312b-98a9-80f5f45e9f9c | -11.75897 | -61.06721 | 2025-10-10 04:53:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f035d5d-e9db-30c4-9f79-c73f3c8db210 | -15.43087 | -47.98281 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 56ed6b29-997d-3f22-bcf0-6bca5a5e5390 | -13.27021 | -48.03264 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ec9809d-b29b-308d-9b62-f20826ccdd0f | -16.00215 | -59.54182 | 2025-10-10 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c83ca2a6-b0ac-3447-ae31-ae9ac7913d14 | -18.74238 | -48.08191 | 2025-10-10 04:53:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ea85c3d2-89b4-37a5-8b35-8899fa4766ec | -15.42915 | -47.98441 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 77b69d7b-803f-36ea-bf8b-d75e624fe548 | -14.23869 | -49.0859 | 2025-10-10 04:53:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53167cce-8745-3dc0-9272-231d5936a2b6 | -13.84677 | -45.85385 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 592df581-dddd-389a-aa34-a8e0172717c3 | -13.23145 | -47.61654 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bc5e862-938d-325d-bc09-2aef4adf47dc | -14.26735 | -45.87444 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2c8c5cc3-5320-38d4-a0a3-896505a3c934 | -17.93109 | -45.03393 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d47abe4-727e-3ec5-875b-8d9e80bf5af3 | -17.89908 | -57.49891 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7890d61b-145f-3b8c-9109-ff1c3e36b6d9 | -13.26534 | -48.03615 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 818e1b80-4313-31ae-b3b6-9e9e3cc6e71f | -16.27621 | -47.17299 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 697bff2f-7ee5-3664-abd3-37f9ac94279e | -16.54324 | -48.89593 | 2025-10-10 04:53:00 | NOAA-21 | LEOPOLDO DE BULHÕES | GOIÁS | Brasil | 5212303 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69cddf73-0773-332c-994a-7833847a11a8 | -17.08244 | -45.48986 | 2025-10-10 04:53:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f74a1ff-54db-32b0-8d76-5535719fa39c | -17.21297 | -47.65527 | 2025-10-10 04:53:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 546ab4ad-f3ee-389a-be60-3c4e3fc05471 | -15.91386 | -43.29121 | 2025-10-10 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bbeab222-0be7-3c4f-a95a-1dd31b9e258c | -14.43599 | -47.97688 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74b48dd1-6bdd-3caa-8b81-2cc90388161e | -13.28384 | -48.01229 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11d469df-4820-315f-b825-70432c160be5 | -17.69108 | -48.63689 | 2025-10-10 04:53:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20fa6933-960f-3921-9278-2a17fd75278c | -15.28338 | -46.14999 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd03e83d-cad6-30a6-b5ce-7a257b3bc3a7 | -14.26972 | -45.89709 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1616570c-7f27-3413-9b88-18e03a501462 | -15.00118 | -56.81985 | 2025-10-10 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5835a7a-1523-34b6-9bf4-c43c4caa2a4c | -14.37386 | -46.00498 | 2025-10-10 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f13ff271-4540-3917-a452-87fb6457cd43 | -15.00764 | -46.28665 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a6e905da-0fe1-35dd-b34b-3911b3caa8cd | -15.24192 | -46.37128 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bd19e1c-f520-3241-9b98-3ec984da372b | -13.26503 | -48.02183 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 178b2914-a54c-3872-a7f7-c817feb5c9ce | -14.43543 | -47.98113 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17cf725e-fb09-3dff-a53f-ec664828a2d3 | -18.07572 | -44.4711 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaf55b38-3729-30b2-8e24-acb2298a1550 | -17.8501 | -57.5792 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2bed67f7-4753-3dd3-8d16-11c51a7a393a | -16.29356 | -47.14881 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a969f783-379c-3764-9dbd-97a58825f9d1 | -16.00993 | -59.54321 | 2025-10-10 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8221a8a2-6094-3903-960a-cef740b3d9f3 | -14.68464 | -48.06773 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbf625b4-2207-3135-af58-315b7377563f | -15.97599 | -59.5311 | 2025-10-10 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e0c09fa-8679-35fc-8ebc-3de58bb70273 | -15.47499 | -47.98075 | 2025-10-10 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b495c2a7-cbd8-34bf-a822-54052f172169 | -17.93747 | -45.02705 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 17d69dab-fdbc-35e0-85c0-b92e4ad67443 | -17.88682 | -57.50867 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 3a101ba1-eaf4-3e09-b454-8d532451f2aa | -14.94245 | -46.76176 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46fcdc25-7560-3a4d-b412-ffe00f9bf677 | -14.26696 | -45.87764 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3c6d2109-74ce-3dde-95fc-5bf90a60c423 | -15.17053 | -56.83648 | 2025-10-10 04:53:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fd7b993-d092-3537-8a1a-fffbe35c6905 | -18.01799 | -45.01868 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4d965b7-8807-3165-b04b-e7c7cbd2eef1 | -13.32336 | -48.4726 | 2025-10-10 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f616e80-842a-3137-bc62-407accee680c | -14.6896 | -48.06376 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 326e99d0-94ba-3eed-b5ec-ec85322f689c | -18.10461 | -53.34901 | 2025-10-10 04:53:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3647aafd-f8df-3c3f-bbd3-c2497b5a1047 | -17.08901 | -45.47988 | 2025-10-10 04:53:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 605e2f4a-1b27-344a-92a4-a04597020824 | -17.38928 | -46.87669 | 2025-10-10 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c75f7031-9460-3ee4-a684-3eea949bbcc6 | -15.09647 | -46.61112 | 2025-10-10 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0798f323-1ac9-3293-a5a3-c556037b96f6 | -16.00903 | -59.54827 | 2025-10-10 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4da7b17a-6ba3-3246-9dd4-ab146e16c6b5 | -13.23643 | -47.61292 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de617bf8-2918-38f2-a190-82644c94513b | -17.93304 | -45.0147 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 10ea7d4a-7df6-3b80-9b7d-186616efb365 | -17.93387 | -45.00648 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ea8e9827-add0-3a62-96ce-c41314252df0 | -16.27624 | -47.16735 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f6e3a9ab-3ba8-3529-b7c6-77c83abfbae4 | -16.00689 | -59.53776 | 2025-10-10 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9781ac35-f8d9-369d-827e-6df249c2bc23 | -13.31283 | -47.99255 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0510c07e-ceed-397d-9bb2-24308f29fece | -13.28917 | -48.00513 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0371d6ef-c05e-392b-9dc6-7e7780441686 | -13.2737 | -48.02275 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ebd739a-7746-38e1-abfd-0f419855e75a | -17.84664 | -57.57866 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6bafd688-9e6d-333d-83bb-b520ee9b513e | -16.74221 | -43.97264 | 2025-10-10 04:53:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 838fdf2e-ceaf-3c74-bf5f-44c1f8a6d0ae | -15.40716 | -48.02603 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69fc0e35-0b21-33a0-876c-b26e57e10280 | -14.38463 | -46.00053 | 2025-10-10 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e9fd948-2d3f-3bd3-9638-350a10dd055f | -14.26859 | -45.90628 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b741c0d-a41b-3963-a016-f9a1ce60988c | -14.43601 | -48.01088 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c373ab6-ed09-3a77-ad34-626ffba150bd | -14.93631 | -46.77169 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 03e1c76c-bc4b-3668-ba58-2ae6fa1ec5e9 | -15.46231 | -48.5315 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00ca79f2-af9e-3b17-9e64-918604f590a2 | -13.83318 | -45.79737 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 137d4eec-3c97-36ba-bf23-d5ce1f79ff3b | -15.11918 | -48.71473 | 2025-10-10 04:53:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cebde233-5239-30e5-8838-b278aa1192c3 | -19.10023 | -43.88131 | 2025-10-10 04:53:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b21480c6-efaa-3461-84b7-b625966001da | -13.34839 | -47.75331 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1f26adc-7ca1-353c-978f-539c1ee9adf2 | -13.29491 | -48.48537 | 2025-10-10 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7da78c85-683e-3827-a30a-10fe7eda32a9 | -14.95076 | -46.7692 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 938d517d-c65d-353c-b98c-038e195c3445 | -15.4066 | -48.03035 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d5fd38e-dd97-3b3a-ae63-ba7bdcbc204b | -13.25187 | -46.47713 | 2025-10-10 04:53:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e02ebb25-5dba-3fbf-9120-19f28c7607a3 | -14.68574 | -48.05896 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc5a1b9a-18da-3943-8d74-40c07655448d | -14.27254 | -45.9159 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05c3753a-dc0d-3f55-b822-c6792220c71b | -15.09582 | -46.61658 | 2025-10-10 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1e19bb4c-e7b3-3442-be3e-b95bed207e28 | -18.53523 | -45.07369 | 2025-10-10 04:53:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f16e39c6-e619-3578-ac7d-4ca4b08495c4 | -13.84713 | -45.85089 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db6e1b84-1ff5-3b88-bf8b-37003fe84d5b | -16.1299 | -48.44238 | 2025-10-10 04:53:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dc036f8-086d-3a68-b93d-50947dae36ee | -15.21509 | -46.38532 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a68bd5db-0faa-3d83-886c-fba9c9237f00 | -17.90403 | -57.51161 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e5a9240c-5441-3d6a-891e-610d374c0a59 | -14.92986 | -46.78045 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 27b3196b-f504-3851-8d91-7f7081faea13 | -13.52918 | -48.11881 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c54cec1d-3552-3e19-9b6e-1321a3d6065d | -16.20152 | -59.33751 | 2025-10-10 04:53:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a17337af-5bb2-3591-9a4c-f40f25493dcf | -14.67635 | -48.0626 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 07caaeba-5261-3526-b3ae-1cd116acbe5d | -17.38995 | -46.87059 | 2025-10-10 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c4a7270-0db1-3be2-be2a-f407e1db5c7c | -16.05159 | -48.06789 | 2025-10-10 04:53:00 | NOAA-21 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53e3ed68-30f1-31a9-86df-f6ca7fa9ffcb | -16.27742 | -47.16249 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb0a8152-fa20-33e5-806c-f963d7d824f5 | -13.28145 | -48.45857 | 2025-10-10 04:53:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3472dfa6-0ac3-3729-a034-2d7e461c0fec | -14.84169 | -48.45832 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README42.md)
