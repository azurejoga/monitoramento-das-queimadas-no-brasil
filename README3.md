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
| 0217cd4f-2abe-3c74-b283-02ae4ff52c09 | -19.40071 | -53.34977 | 2026-04-18 04:44:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 469ccfc3-e45b-372a-8438-954d4907d671 | -17.57644 | -46.60545 | 2026-04-18 04:44:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c15c6fb-ff80-34f1-8def-d9159ea66e2f | -18.07517 | -52.78178 | 2026-04-18 04:44:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e09966c6-05b1-37e7-91fc-d1f0ac1d3e74 | -20.1556 | -46.71496 | 2026-04-18 04:44:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11f80db4-9afb-3181-acd0-a1c6b153acb4 | -20.15982 | -46.71549 | 2026-04-18 04:44:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d4e8527-9697-3027-981a-94a3b2b465a2 | -19.39798 | -53.34549 | 2026-04-18 04:44:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 139c9962-e72e-31e3-8f03-e30a3660fa79 | -18.07237 | -46.3706 | 2026-04-18 04:44:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b72846f8-664a-36a0-9854-14faf9233459 | -17.56474 | -46.63091 | 2026-04-18 04:44:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61cb9405-f807-365e-9de2-63dd28367f5e | -16.14215 | -43.55518 | 2026-04-18 04:44:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e195c7f0-3af6-3dc7-b44e-e1e09b0ffaf5 | -20.16726 | -46.72446 | 2026-04-18 04:44:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b287d8db-0cc4-3866-bc11-d39f91b4a2f4 | -20.16353 | -46.72004 | 2026-04-18 04:44:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38a43db5-1e23-33f4-8fed-c2e6f08640bc | -18.94488 | -53.45575 | 2026-04-18 04:44:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ecb2108-7d4f-3d17-9f51-e7c825d73514 | -20.16005 | -46.71405 | 2026-04-18 04:44:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 88c45f83-c610-3091-81af-b235fbb17a17 | -19.40011 | -53.35346 | 2026-04-18 04:44:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b3754fb-7455-366a-bb6c-470dab74f24a | -20.16378 | -46.71864 | 2026-04-18 04:44:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 946d9c77-5027-3c63-9052-d88d5b0ea36a | -20.16404 | -46.71602 | 2026-04-18 04:44:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb0ad3c9-7166-31c0-8e2c-cabceb47ab4f | -16.14025 | -43.55455 | 2026-04-18 04:44:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96bc1f39-a830-37d7-86e6-a961e666b654 | -23.65465 | -48.00418 | 2026-04-18 04:46:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fcc6799-ff92-3e0b-8016-8b154c9cc092 | -20.62678 | -51.70628 | 2026-04-18 04:46:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a6441c5-7346-36de-8941-24a50c86f881 | -23.64602 | -48.00687 | 2026-04-18 04:46:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 63192407-1eed-3786-94c6-227aeaa92e2f | -20.63242 | -51.6918 | 2026-04-18 04:46:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eec47a88-cd1a-3ff0-8ee5-6d1c1783ef53 | -23.65417 | -48.00805 | 2026-04-18 04:46:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6df7bf01-1540-3a55-8994-fed50cadca79 | -21.71191 | -48.42508 | 2026-04-18 04:46:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09e2853b-a59d-339b-881e-700c91442d2a | -26.48226 | -48.79546 | 2026-04-18 04:46:00 | NOAA-20 | ARAQUARI | SANTA CATARINA | Brasil | 4201307 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 524808b0-669e-30cb-b6a5-39f5c4024d9d | -21.87998 | -47.14679 | 2026-04-18 04:46:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9d20d70-124c-33fb-8a61-848eb320917c | -23.65372 | -48.00697 | 2026-04-18 04:46:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25f8b83a-92e3-33d1-8e38-18ece6352c99 | -23.6496 | -48.01135 | 2026-04-18 04:46:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3efc8bfd-5c71-3ef6-9f37-a5fa581c9045 | -21.39796 | -49.0013 | 2026-04-18 04:46:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 656385c1-439b-3e21-a284-28517e74983f | -22.32286 | -48.23352 | 2026-04-18 04:46:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99761128-d1ba-3780-8f5a-6346ab7f8f15 | -23.65009 | -48.00745 | 2026-04-18 04:46:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09d65b9e-a5ca-35e1-8298-f8ca80436ac3 | -22.32215 | -48.23899 | 2026-04-18 04:46:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f35d1ff2-8940-332f-8dd9-de9d9b7dd6ff | -22.16573 | -56.21471 | 2026-04-18 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ef1f366-ae24-3b2a-a3ea-46d3549669d0 | -21.88047 | -47.14273 | 2026-04-18 04:46:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a0fdedc-f3cd-3286-93de-b95ae9ec45ff | -23.27158 | -55.1872 | 2026-04-18 04:46:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dd51d713-6ecc-31c1-9fdf-7fd0f93e5ad1 | -22.00927 | -53.50688 | 2026-04-18 04:46:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 458e8481-b851-32af-9c2a-d8d4f2a4c1fc | -26.47823 | -48.79485 | 2026-04-18 04:46:00 | NOAA-20 | ARAQUARI | SANTA CATARINA | Brasil | 4201307 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b09403b4-35cc-3f41-90a1-da2b7c13f19c | -25.98725 | -51.70162 | 2026-04-18 04:46:00 | NOAA-20 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1435f1ca-2cbc-38f7-b568-0956c2f0ce6d | -21.19245 | -48.60735 | 2026-04-18 04:46:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 6b4be009-48d0-3f19-93e8-ac8e5ccf778a | -23.65058 | -48.00357 | 2026-04-18 04:46:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9bf5c7f-c3de-3979-a603-14a7bb397423 | -20.63692 | -51.68483 | 2026-04-18 04:46:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99dc4619-f693-3e82-9249-73866f5cb4fc | -21.69854 | -56.306 | 2026-04-18 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fc72589-e0d9-3309-882e-a3248e654ade | -22.96472 | -52.69659 | 2026-04-18 04:46:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| e60a9063-74ec-34f6-8f4e-bdbc88bb3420 | -20.19237 | -50.55949 | 2026-04-18 04:46:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2d947e04-7b64-3ce6-8a6b-c973484dfba1 | -23.26819 | -55.18652 | 2026-04-18 04:46:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b8b50fc4-f51d-3d48-a9a8-a8be0eafc259 | -20.62736 | -51.70252 | 2026-04-18 04:46:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a47054c1-a661-3e71-b361-d6d336836828 | -20.63577 | -51.69237 | 2026-04-18 04:46:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| e2315d3e-d9cc-3a6f-8049-28dde8837600 | -21.03754 | -48.55139 | 2026-04-18 04:46:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f7e727b9-9700-3699-a1bc-6fbf7d368f79 | -23.64699 | -47.99907 | 2026-04-18 04:46:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc807e39-21b3-363a-8a92-a054a58a435c | -20.63128 | -51.69933 | 2026-04-18 04:46:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40406861-5380-3aa7-8a76-8c143dd3bd35 | -20.62621 | -51.71004 | 2026-04-18 04:46:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 88c52a00-3d89-37bc-a880-459e09e9d6f4 | -23.65106 | -47.99969 | 2026-04-18 04:46:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 183ff889-34a4-3f00-9cc7-ff7754a5065e | -23.6465 | -48.00296 | 2026-04-18 04:46:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1983dab5-d388-3cb1-917e-5a4e4e61f6f2 | -21.69775 | -56.31042 | 2026-04-18 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31984a7b-9139-3f94-9deb-e2f19b53ae1b | -28.69262 | -50.16928 | 2026-04-18 04:49:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 83b8e0a9-c430-3386-a72e-b58c4aec74ba | -29.85637 | -51.19464 | 2026-04-18 04:49:00 | NOAA-20 | ESTEIO | RIO GRANDE DO SUL | Brasil | 4307708 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 5b53bbc2-b093-3c5e-ab37-878d2f501313 | -14.82416 | -59.83451 | 2026-04-18 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aec39b33-6e55-3502-b7e8-7afcd9d0f0cb | -21.7031 | -56.30764 | 2026-04-18 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a3517a0-15c8-37e8-857c-487ddc006e2b | -21.70277 | -56.31091 | 2026-04-18 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82fcf4da-47c6-37d4-bc37-e40d8d2709e6 | -21.6979 | -56.30709 | 2026-04-18 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6646f519-46a9-3984-b439-370ee58c25c0 | -22.96311 | -52.69579 | 2026-04-18 05:33:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ca761b38-c726-3f37-9c03-8766bd0925fa | 2.94319 | -60.18102 | 2026-04-18 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da704217-a601-3847-b179-12b93dc547a0 | 2.94758 | -60.18026 | 2026-04-18 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 648deec3-c6f6-3f9b-a861-d484ff71f721 | -23.64414 | -51.68346 | 2026-04-18 06:27:00 | AQUA_M-M | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e952911d-a05d-3c52-a465-ea27f07e5ddb | -15.95082 | -52.81618 | 2026-04-18 12:44:00 | TERRA_M-T | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |


