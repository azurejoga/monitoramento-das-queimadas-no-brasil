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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fd96481-c0ab-3fbe-9c95-0cfb3df54cd3 | -18.6695 | -47.36338 | 2025-09-15 04:53:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 944dce33-70ac-35d6-aad2-618db249e95f | -23.25009 | -49.5148 | 2025-09-15 04:53:00 | NPP-375D | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 46ed1c1c-5484-361e-bfa4-a96d2e232baa | -22.66079 | -53.11242 | 2025-09-15 04:53:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 79693c1a-bf63-34d1-bef9-6fe5d86616af | -21.63522 | -46.81121 | 2025-09-15 04:53:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a7daa287-e71d-3f2e-950d-6f2331eb62c6 | -18.62875 | -47.33032 | 2025-09-15 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 07ef054d-8fd8-302e-a07a-6e67119452e8 | -18.15751 | -49.20782 | 2025-09-15 04:53:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2a1c7470-c64c-38a8-bcbb-3bcf28bf5037 | -18.15877 | -49.19819 | 2025-09-15 04:53:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2a8832d0-cc0a-38ae-a7a1-74a1fcf4e1f0 | -23.60703 | -47.3816 | 2025-09-15 04:53:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cc0e5431-12e5-3f5d-8752-14cb35c28a40 | -22.05176 | -56.0887 | 2025-09-15 04:53:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85189c9c-559e-32eb-9bf2-c0f615aaa22f | -22.20574 | -48.3546 | 2025-09-15 04:53:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ba185a8-98f0-3949-9ed3-80fbc9f4f6a7 | -20.51125 | -55.63512 | 2025-09-15 04:53:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff133f6f-ae68-370c-8aea-206704b9b154 | -22.04902 | -56.08419 | 2025-09-15 04:53:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce08a51b-2171-3f58-b86d-1517bc1ff269 | -20.95976 | -54.98378 | 2025-09-15 04:53:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9410a7b-f3c5-313f-8c4d-84418efedb56 | -20.52077 | -55.64072 | 2025-09-15 04:53:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9aa619b5-a9d0-392f-97ce-0347f0346fe9 | -22.66105 | -53.11774 | 2025-09-15 04:53:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2ce28e26-62cd-3870-ae72-72b76d3cf9de | -22.04838 | -56.08804 | 2025-09-15 04:53:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d568748-a67e-3524-85f4-db69c0d3e479 | -20.32749 | -58.08533 | 2025-09-15 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f5ed4dfb-7e14-3aae-a7c0-df46f2615205 | -25.19359 | -51.37305 | 2025-09-15 04:53:00 | NPP-375D | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f73ee34a-a566-38be-bec9-dd348df3ea96 | -22.99322 | -49.94104 | 2025-09-15 04:53:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 276af242-3a2a-3c0e-aa51-aeffd294686f | -20.23434 | -46.17475 | 2025-09-15 04:53:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7c001bab-9033-3596-9b4c-c307a3beec9b | -18.59107 | -47.20478 | 2025-09-15 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed834914-c561-3769-9a6d-baed28747bc7 | -25.17701 | -50.07592 | 2025-09-15 04:53:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ac22bafa-3630-38d9-9af8-3580256083f9 | -22.28856 | -49.04197 | 2025-09-15 04:53:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7520ed37-b9e9-36c9-9dce-daf901110327 | -21.9238 | -46.60566 | 2025-09-15 04:53:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 443f4905-d95d-3b24-9991-d7812625e3e1 | -19.62553 | -43.73882 | 2025-09-15 04:53:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c04053ba-8aea-3afd-a95a-fd6798caac03 | -19.97882 | -46.76291 | 2025-09-15 04:53:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e68c384-70bb-3407-98eb-26a3c838d74e | -20.8577 | -46.21425 | 2025-09-15 04:53:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6813255-65f2-3ac4-80fd-b84370416d51 | -22.99511 | -49.9402 | 2025-09-15 04:53:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a54d9831-8c9e-3d29-afd9-62d5f448920d | -19.00741 | -46.24706 | 2025-09-15 04:53:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e0a2c34-1868-3d48-9387-1479a8e924a6 | -23.24559 | -47.10469 | 2025-09-15 04:53:00 | NPP-375D | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9f0e3a6c-a581-32bb-ac71-da2db25a970f | -21.92317 | -46.56579 | 2025-09-15 04:53:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 84338856-266c-3028-a086-d614ef34391f | -22.20086 | -48.35849 | 2025-09-15 04:53:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d7eeb01-4618-3ed0-bdb8-06ade2fc2427 | -21.76208 | -48.12425 | 2025-09-15 04:53:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e253c56-331c-3474-880c-60715448955d | -20.82212 | -45.60522 | 2025-09-15 04:53:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ed47c9f-d303-394b-b415-22e6537de051 | -22.17974 | -49.61519 | 2025-09-15 04:53:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 04af8078-621b-393d-92a9-f2ff1f1742ee | -23.47211 | -47.37366 | 2025-09-15 04:53:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 965b8688-1d6a-38b6-8fae-a1ec3e9d2353 | -21.11904 | -45.95744 | 2025-09-15 04:53:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0d7c818a-0f4c-3067-a8e1-b80ad044a9d2 | -23.14133 | -49.63407 | 2025-09-15 04:53:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4416c643-0380-31a6-868d-2edf15b8d9b0 | -20.0455 | -46.16683 | 2025-09-15 04:53:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a007873-8a66-34fe-9d96-5f56f42850e7 | -18.15719 | -49.20617 | 2025-09-15 04:53:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ed11ef17-28ae-3499-8eb5-064bbfd47f0f | -23.25118 | -49.51494 | 2025-09-15 04:53:00 | NPP-375D | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 51839f4b-84be-3c81-896a-ab3ad5db5b48 | -22.2755 | -56.04649 | 2025-09-15 04:53:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4459ac2-2992-31fb-b817-222db2ca6b74 | -22.99047 | -49.94484 | 2025-09-15 04:53:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e298000d-60f1-3912-99e3-395a206d6a15 | -22.65881 | -53.10925 | 2025-09-15 04:53:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 796e4545-853d-3c2b-800c-524dd049a481 | -21.6299 | -46.81566 | 2025-09-15 04:53:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e897b883-57c5-3bdb-bc22-09045f95dcc9 | -18.60052 | -47.20142 | 2025-09-15 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd9f08c3-f5ab-3edb-ab2a-181ada40b24d | -22.66989 | -53.12208 | 2025-09-15 04:53:00 | NPP-375D | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 14fc7127-605e-39bf-bebb-48161a431cb0 | -22.61483 | -54.92542 | 2025-09-15 04:53:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 99b518c9-1280-3881-9838-ab007c0f11ca | -22.66305 | -53.12091 | 2025-09-15 04:53:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 464421ae-7d8e-3d87-b0d8-9ff6930e887f | -20.5214 | -55.63689 | 2025-09-15 04:53:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 50da5484-d047-32b8-a110-317c8ce34c1b | -20.51802 | -55.63629 | 2025-09-15 04:53:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc094cdf-56c5-38a7-b1e9-a07da8b896af | -22.04354 | -56.0752 | 2025-09-15 04:53:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| befd45ac-c8af-3807-9af2-fe86d725d6d8 | -22.66647 | -53.12149 | 2025-09-15 04:53:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a239e3f9-9b6f-3914-95d0-250ab834882f | -18.15785 | -49.20134 | 2025-09-15 04:53:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 72f6d163-4807-3453-919a-a56efbff93e5 | -20.40981 | -54.63106 | 2025-09-15 04:53:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cfeb8950-5ef1-348b-ad3d-9c667de75184 | -18.75332 | -47.02483 | 2025-09-15 04:53:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ea6a843-0006-3b14-b57d-86afdb5296b0 | -22.91198 | -51.14517 | 2025-09-15 04:53:00 | NPP-375D | PRIMEIRO DE MAIO | PARANÁ | Brasil | 4120507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 717085e5-608c-346a-91b8-abda4504cce8 | -18.97583 | -48.58539 | 2025-09-15 04:53:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| cd3cc8fa-c1e2-3123-9081-f6adef868a11 | -18.96053 | -48.21334 | 2025-09-15 04:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fedb3bc1-9890-31ce-931f-abe3c5749488 | -20.51526 | -55.63192 | 2025-09-15 04:53:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01fe76fc-12b4-368e-9a86-7ee2648a7ec1 | -23.48206 | -47.36972 | 2025-09-15 04:53:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 88ec5377-6ade-3bec-9859-104b4e98e2e2 | -18.57871 | -48.15152 | 2025-09-15 04:53:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 738aa58a-8cf1-342b-ad38-5677df54a75e | -20.51463 | -55.63571 | 2025-09-15 04:53:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46ab4fd6-c59c-3ab9-b06b-03541441b381 | -18.58341 | -48.14811 | 2025-09-15 04:53:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f78dbf1-67f9-3aac-b197-86e710acc897 | -17.75025 | -51.88457 | 2025-09-15 04:53:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4c68c6a-e359-30c4-9c4f-794d6d13c58b | -18.89363 | -50.15841 | 2025-09-15 04:53:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad8868d1-2484-37e2-8624-d5b5288f1146 | -18.44879 | -47.2024 | 2025-09-15 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fa5d0fa-0d43-3bd2-9c05-015c1f18eac2 | -18.47554 | -46.94337 | 2025-09-15 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76fea8c7-3900-3a6b-99c4-f910583d2183 | -18.15427 | -49.20226 | 2025-09-15 04:53:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eb842860-ce12-3cc2-a647-bad761d504e2 | -18.44936 | -47.19774 | 2025-09-15 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 210a645b-69ad-3f39-9564-63ed3d09be35 | -20.93604 | -47.01462 | 2025-09-15 04:53:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c1d2a35-591c-325a-820b-3c19d1dcdd1c | -18.59997 | -47.20588 | 2025-09-15 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0e31711-07b2-37d8-84a0-f55d41e32128 | -22.30118 | -47.95352 | 2025-09-15 04:53:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ead278b-4804-3d1c-94dd-e006d01df030 | -20.84852 | -56.89841 | 2025-09-15 04:53:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 877f1b30-c259-393f-ab70-ef6c19c49d8c | -23.4768 | -47.37429 | 2025-09-15 04:53:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| db93760e-493a-357b-a449-d84260fd727d | -23.23658 | -51.00763 | 2025-09-15 04:53:00 | NPP-375D | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c1372d77-7e9c-3e34-8672-8fb08d696ffe | -20.52415 | -55.64134 | 2025-09-15 04:53:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d0f4d8f-e1e4-3922-83fe-5c0caac6caf5 | -22.20199 | -48.34917 | 2025-09-15 04:53:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efb555ef-41c9-3e02-8e73-9c31bca94d7e | -23.60626 | -47.38021 | 2025-09-15 04:53:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cb0734fa-322d-351a-a2a2-2f9b5bf18b00 | -24.84191 | -50.35165 | 2025-09-15 04:53:00 | NPP-375D | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 321c511b-af35-3ba3-81a2-44b0e2121e3b | -20.2337 | -46.18024 | 2025-09-15 04:53:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0378fe92-746f-3e20-a3a6-dd0cf328ab1b | -22.18089 | -49.61657 | 2025-09-15 04:53:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5b581159-c63c-3c3e-9aa1-1c89c4f645a0 | -24.22484 | -50.92795 | 2025-09-15 04:53:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ddcb338c-c840-373e-81e6-26fc2a1c246b | -20.42063 | -54.5418 | 2025-09-15 04:53:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04e7766d-8c25-320e-8dc5-cea1df53151d | -19.74355 | -45.12567 | 2025-09-15 04:53:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 67c93693-db00-3535-bd6f-e5059d65f3a1 | -22.65822 | -53.1132 | 2025-09-15 04:53:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d6ff31ff-8f02-3597-9b3c-f3c994331a2e | -20.96309 | -54.9844 | 2025-09-15 04:53:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ecefdc9-4edf-3ebd-a0b2-c86df2466d5d | -22.19657 | -48.35762 | 2025-09-15 04:53:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ba1a57b-5935-38a2-8751-a91d268a432e | -18.15814 | -49.20299 | 2025-09-15 04:53:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1352a5bf-43e9-348c-8d6d-e4070f23c24d | -22.99116 | -49.93944 | 2025-09-15 04:53:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 022fa6e6-ed8d-36eb-886b-27f3ddc8bcf0 | -19.62598 | -43.7344 | 2025-09-15 04:53:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 475f1068-089f-3732-8e74-ec6dc105170a | -18.4705 | -46.94719 | 2025-09-15 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f994ab19-2a31-3f5b-b485-d90631b47efe | -22.22454 | -48.61213 | 2025-09-15 04:53:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d79b52e8-9a86-3998-b497-35234ea4e9a6 | -22.21005 | -48.35534 | 2025-09-15 04:53:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 370148a5-dc07-3f4d-a0b6-ea4ff10c55fd | -20.52691 | -46.86919 | 2025-09-15 04:53:00 | NPP-375D | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 01a8303c-336e-38a5-86e1-141ccde5c6ef | -23.72446 | -47.35414 | 2025-09-15 04:53:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7e5549df-95b9-3125-9f4e-1f9673ae9aa0 | -22.99718 | -49.94176 | 2025-09-15 04:53:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d3bdd9e1-9837-32dc-ab04-a299d8ca48cb | -22.66021 | -53.11637 | 2025-09-15 04:53:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a2604bcf-5aee-3fc3-9636-f9773fde6faf | -18.16201 | -49.20371 | 2025-09-15 04:53:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 08672a68-0f83-32f7-be3e-81f855784c23 | -23.47794 | -47.3639 | 2025-09-15 04:53:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |


[Clique aqui para ver as próximas entradas](README55.md)
