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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 223dc8dc-6d87-3a6a-89d3-04b1d55cad70 | -8.44587 | -70.11984 | 2026-07-16 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0dd1fff-15df-39d4-8006-877612a145a7 | -9.45581 | -63.87521 | 2026-07-16 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 61f545a9-5694-3abb-b57c-af9bedc3994c | -1.64015 | -54.46233 | 2026-07-16 07:09:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 04c732b4-d31e-365e-8026-1323b78dbc16 | -1.63884 | -54.47102 | 2026-07-16 07:09:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6bad70b6-477d-3dbc-824f-7a8b3e8b81df | -22.24862 | -56.00827 | 2026-07-16 07:14:00 | AQUA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2d44f2b1-315f-3f52-aa3b-66095cc20984 | -22.25011 | -55.99694 | 2026-07-16 07:14:00 | AQUA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 3dabea8c-646f-30b0-9d64-b9608305b170 | -4.79657 | -37.32535 | 2026-07-16 11:42:00 | TERRA_M-M | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 2817a16a-c640-342b-ac7a-786b6d268f56 | -11.78639 | -47.0863 | 2026-07-16 11:45:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 17c56bce-444f-3e23-8948-c2358d37ebeb | -8.70178 | -39.72068 | 2026-07-16 11:45:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 634a4784-ce9f-38e2-9961-7d48e08273a1 | -11.79525 | -47.08761 | 2026-07-16 11:45:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 562ef3e2-be19-3263-8441-d5498a356ced | -9.05492 | -44.831 | 2026-07-16 11:45:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d0a98a34-620e-3992-b9e1-0c83a1d2dce9 | -13.25537 | -45.11176 | 2026-07-16 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| bc08da68-a876-3e67-bfea-b0a2f41179a6 | -13.534 | -47.76011 | 2026-07-16 11:45:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 83fa7b91-f8f2-3d0d-a723-5b60cfeaa9c0 | -11.78507 | -47.09536 | 2026-07-16 11:45:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 93707669-a307-3bcc-97b3-7b6ced3b8efe | -12.46107 | -49.58492 | 2026-07-16 11:45:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d22da989-bee8-3587-bf02-bb19cebe34f1 | -13.25406 | -45.1213 | 2026-07-16 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| e28fd62d-e2f3-3334-95a7-b0dc32d821fa | -12.45864 | -49.58955 | 2026-07-16 11:45:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1f7cf6d0-8c7f-3066-9daa-a83e97ec587d | -7.92789 | -43.31258 | 2026-07-16 11:45:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 8630d75c-be5c-3d3a-8a60-db9f41480952 | -13.07997 | -48.33327 | 2026-07-16 11:45:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 87e8d5e5-fa86-3878-99bb-b621ef30a07f | -13.26827 | -45.15254 | 2026-07-16 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 55bb2c73-c690-3215-bc90-f157b52094fa | -10.66494 | -45.1852 | 2026-07-16 11:45:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 06da49e9-890b-3e1a-a5ab-a4d866fa8bf3 | -13.26182 | -45.13219 | 2026-07-16 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ea0a2b0c-9b17-3af7-a6de-2885ebcd711a | -13.44375 | -43.85569 | 2026-07-16 11:45:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| becfbdf1-13f8-3827-aeda-048fac557713 | -13.08141 | -48.32357 | 2026-07-16 11:45:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8cd391a2-b79c-3e5c-9e69-55b144b18611 | -13.05406 | -45.23626 | 2026-07-16 11:45:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4927282b-cc94-3d59-b2ed-32646726d7ed | -10.70379 | -48.4665 | 2026-07-16 11:45:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 6bdfcbe9-8e7d-33ae-a064-cc2b8f252ccf | -14.14388 | -46.27356 | 2026-07-16 11:45:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 45a0f5ec-bf25-3b80-97d7-27cfe9d8eaa5 | -13.05276 | -45.24571 | 2026-07-16 11:45:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d1f9659-007f-36fa-b48b-6c3a3c9b155d | -10.12895 | -40.49999 | 2026-07-16 11:45:00 | TERRA_M-M | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b5285561-c21d-3cfb-82aa-3951decf3f31 | -13.44521 | -43.84468 | 2026-07-16 11:45:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 73144e77-1a9a-30e1-9a04-875203280c29 | -10.66366 | -45.19433 | 2026-07-16 11:45:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| a09f09fe-612a-39d4-8c28-1a24d0f5f67b | -22.25602 | -55.99361 | 2026-07-16 11:47:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 5a132073-c849-3507-9848-fbfe68c8ba1b | -20.34156 | -46.61984 | 2026-07-16 11:47:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0230acbe-4d09-3c1f-88d9-e582c8179622 | -16.89277 | -46.79086 | 2026-07-16 11:47:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f1175c8f-f776-36e2-98a1-6226e0d11cb6 | -22.26502 | -56.0031 | 2026-07-16 11:47:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 29.0 |
| b83391f4-728b-3313-8bd1-083495f9519f | -22.26483 | -56.01941 | 2026-07-16 11:47:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 238be21e-f0e1-3dae-a6aa-35debb3254e0 | -19.30769 | -47.44299 | 2026-07-16 11:47:00 | TERRA_M-M | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 785403da-9766-37c4-a0cd-8b85bd1a2b5f | -16.12211 | -47.85704 | 2026-07-16 11:47:00 | TERRA_M-M | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 01a8578b-9a44-33d0-91a5-e72b2c74b6ba | -16.90163 | -46.79218 | 2026-07-16 11:47:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 58e41288-99a4-3b44-bdb2-5be6330b87f1 | -15.99905 | -46.72001 | 2026-07-16 11:47:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e71aabe2-b551-33ab-b695-84f0a3fa88ce | -16.38529 | -45.10581 | 2026-07-16 11:47:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1b4a12a4-d665-3a06-8229-594d29c08d97 | -16.12345 | -47.84787 | 2026-07-16 11:47:00 | TERRA_M-M | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 67bbfdd0-b72e-303a-8a94-a768e467fd5d | -17.57204 | -46.5425 | 2026-07-16 11:47:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f3aad4cb-7f3f-3b0f-8abe-a7cbaa45e910 | -30.70571 | -52.56563 | 2026-07-16 11:49:00 | TERRA_M-M | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 6.0 |
| aeecdc71-895c-3e1f-9b1a-bbbea800a4d3 | -30.6966 | -52.56371 | 2026-07-16 11:49:00 | TERRA_M-M | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 16.7 |
| f0fa56d3-1049-3f8d-aa6e-2a37aa26c334 | -23.8637 | -53.9569 | 2026-07-16 11:49:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 43e39946-df29-30eb-9afb-e7e0048eb649 | -30.64695 | -52.75749 | 2026-07-16 11:49:00 | TERRA_M-M | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 7.5 |
| 795ced19-ee01-3a9c-81a4-f0943c70467e | -9.45822 | -63.85671 | 2026-07-16 13:23:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 20.9 |
| ca0dc0fa-9b0e-3038-bfb1-ab3ae19bb2cb | -9.45567 | -63.87745 | 2026-07-16 13:23:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.4 |


