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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fb8a94b-20ea-3115-85ca-6b760b59ccba | -13.90364 | -45.84137 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 14573ff4-1e14-369a-ba6c-19e380d470ed | -13.90135 | -45.83316 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c7e4fb88-4968-3d4b-bbdd-9ddf1704f815 | -13.90078 | -45.837 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6125414c-ee69-36bf-aa3a-c045489ee631 | -13.9002 | -45.84084 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c80253b1-ea2d-3a15-bb7e-b0be9ac67aba | -13.89849 | -45.82878 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f63c90d0-297a-3792-911a-407f22be0be9 | -13.89791 | -45.83263 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 662cbeb6-206c-3bc3-9fa2-1d10145891c7 | -13.89733 | -45.83647 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b1dfd689-0f21-39a3-9613-d1e78164fdd3 | -13.89675 | -45.8403 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 86a43d7c-9694-3136-850c-056d2263962a | -13.89446 | -45.83209 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c074d2fd-e63d-3d1a-846b-293050703922 | -13.89388 | -45.83593 | 2024-10-15 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1bd5efe-020c-31f4-803c-d9fb35bc51c1 | -15.26118 | -46.03514 | 2024-10-15 04:27:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 562d5bf5-8204-3742-9a0a-95daccdd86a4 | -14.75042 | -48.3651 | 2024-10-15 04:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db483807-96af-3e82-9580-4a5f61eb9151 | -14.34664 | -47.07749 | 2024-10-15 04:27:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0e144fb-29d3-3ff4-9c64-4bdd2edc8916 | -14.11746 | -46.98219 | 2024-10-15 04:27:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9e8c38e-a4a9-30b8-8cc9-d4166a3ba6bb | -14.11411 | -46.98165 | 2024-10-15 04:27:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1da822a-c933-340c-aa91-a21b15416d09 | -23.51352 | -51.41407 | 2024-10-15 04:29:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0bd090a0-7cb4-3017-9594-67033e2ab6f8 | -22.00194 | -54.6474 | 2024-10-15 04:29:00 | NPP-375D | DOURADINA | MATO GROSSO DO SUL | Brasil | 5003504 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7a05f06b-6e64-393a-81b3-0a874c167384 | -21.66481 | -56.02468 | 2024-10-15 04:29:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 949ff6c0-972e-399f-bd36-7a062e989a89 | -19.54576 | -56.98514 | 2024-10-15 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 16b591d0-0406-3b0a-b7ec-f7b34507628d | -19.54471 | -56.99039 | 2024-10-15 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a47e2bb7-ae3f-3bf6-89cb-f86df6abf0a4 | -19.54001 | -56.98932 | 2024-10-15 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3d3686d8-8943-35ca-86a2-f0a56910ec84 | -19.54107 | -56.98406 | 2024-10-15 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a2a22400-a136-3eca-85bf-53b504168048 | -22.90243 | -43.75611 | 2024-10-15 04:29:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| abab049d-5bc5-3919-b5ee-8628c738d77b | -22.90099 | -43.75275 | 2024-10-15 04:29:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 78df321d-6fb3-368c-8965-aefd728c6469 | -22.90047 | -43.75706 | 2024-10-15 04:29:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 36ce03a8-3808-3859-a706-d0c3b185b011 | -22.72963 | -42.89477 | 2024-10-15 04:29:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 272daec7-8982-34fd-b6cb-c6e0bbc641d9 | -22.72907 | -42.89969 | 2024-10-15 04:29:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ff238ddb-849f-3677-a9d4-76c4421a31e0 | -24.24231 | -50.73826 | 2024-10-15 04:29:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7d694d44-0ae6-368c-a697-a50c5e571dad | 1.0016 | -52.2164 | 2024-10-15 04:35:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 4b9d1d4f-e8c1-3ff2-a0bc-14b67d2cb9ef | -3.1099 | -54.2263 | 2024-10-15 04:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 768a3215-153c-3469-a279-d8dfea204b60 | -3.1283 | -54.2259 | 2024-10-15 04:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| a7e97de0-962b-3d1f-aa34-426deef8a62f | -3.9289 | -48.3458 | 2024-10-15 04:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 04e6bb9d-d77d-399c-8f06-c7a402b03373 | -3.9078 | -42.4256 | 2024-10-15 04:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 4ab3c591-e599-3440-8d78-fb2323bb159c | -3.908 | -42.402 | 2024-10-15 04:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 134.3 |
| 7153a830-91c6-3f9a-8a61-f3f328413fd9 | -3.9265 | -42.4246 | 2024-10-15 04:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| 6b6b3b08-a19d-32f1-8b5e-a3bcaf0ea205 | -3.9267 | -42.401 | 2024-10-15 04:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 173.6 |
| 6b7f8438-07b6-35ac-9219-47d02be79435 | -6.5505 | -48.2408 | 2024-10-15 04:35:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 116.6 |
| f062c875-3d52-333d-9f35-5faf2c47faf0 | -6.5691 | -48.2395 | 2024-10-15 04:35:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 248.5 |
| cd022011-7c09-3902-b5ff-28a90e9d0ced | -6.5693 | -48.2178 | 2024-10-15 04:35:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 6055e02c-b629-36bd-8297-805d4af094ae | -6.5878 | -48.2381 | 2024-10-15 04:35:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 9a48b37c-1f62-31a2-a6e9-547de429962e | -9.01 | -54.5042 | 2024-10-15 04:35:57 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 7ec19ba6-de5f-3ee9-bf7a-04b30bd4034a | -10.3711 | -61.1935 | 2024-10-15 04:36:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| d2e367ee-fd94-30ca-b4e2-287dfb81f3c2 | -10.3713 | -61.1743 | 2024-10-15 04:36:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ba0f656b-b2c4-3244-8268-e42a90d552fe | -11.6915 | -65.2432 | 2024-10-15 04:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 87b92c45-6657-3b08-b4d3-8fbc4b04049a | -11.6917 | -65.2243 | 2024-10-15 04:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ade3dbe9-d3d0-38be-8aef-911cb76461ce | -12.515 | -63.263 | 2024-10-15 04:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.3 |
| cf9932b5-463c-30e3-bb3c-336f7d9695d1 | -13.888 | -45.8388 | 2024-10-15 04:36:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| af730a36-47d7-3d33-a2a4-a2d05ac18f63 | -13.8885 | -45.8157 | 2024-10-15 04:36:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| f3df0f09-c3af-31e4-8b93-319717bd26dc | -13.9075 | -45.8355 | 2024-10-15 04:36:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 243.6 |
| f248e0a5-9107-30b9-989d-84326c35b058 | -13.9079 | -45.8124 | 2024-10-15 04:36:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 281.3 |
| c2050376-f60c-3e5a-8d40-54104f97e76f | -13.9274 | -45.8091 | 2024-10-15 04:36:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 200.6 |
| ee8eb86a-dfe9-3a3f-be2e-f07db2d2e415 | -13.9269 | -45.8323 | 2024-10-15 04:36:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| e50cb1b7-65c3-34f1-a135-e05bf92c09a0 | 1.0199 | -52.2162 | 2024-10-15 04:44:57 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 862529a2-cd1f-3018-aa63-3738dc485ddd | 1.0016 | -52.2164 | 2024-10-15 04:44:57 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 72be6fc2-b72c-3ffb-b8ad-65f70c4790cc | -3.1283 | -54.2259 | 2024-10-15 04:45:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 7cdbe5c2-aff3-3530-8e7d-5ab3bbc613b8 | -3.9289 | -48.3458 | 2024-10-15 04:45:25 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| b141707f-74ea-3a1b-a639-a36efc342a9e | -3.9267 | -42.401 | 2024-10-15 04:45:25 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 225.1 |
| 116a22f6-9eda-362e-b613-5190033225e8 | -3.9265 | -42.4246 | 2024-10-15 04:45:25 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 1c23a190-50ff-3e95-bd08-3078eeeb99ce | -3.908 | -42.402 | 2024-10-15 04:45:25 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| f9a1091a-405d-330e-b255-f82959c89fde | -6.5691 | -48.2395 | 2024-10-15 04:45:40 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 176.2 |
| 7c68f98d-99ea-3175-be7d-2793a40adf3a | -6.5693 | -48.2178 | 2024-10-15 04:45:40 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 40d0c037-d696-35d2-ab00-d4b1091ed455 | -6.5878 | -48.2381 | 2024-10-15 04:45:40 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 94.9 |
| e3f44fab-f7b4-33b6-a4bd-a107e2bfc0aa | -6.5505 | -48.2408 | 2024-10-15 04:45:40 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 77.5 |
| a9cbfc24-071f-3d8e-bce8-4f689c280f28 | -4.2307 | -40.39198 | 2024-10-15 04:46:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 123ec05c-468f-3488-b708-1ca585492ece | -3.924 | -42.40638 | 2024-10-15 04:46:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 63be95bb-26e8-3f16-9cc9-b6039d96bcd7 | -3.92346 | -42.41 | 2024-10-15 04:46:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d73cd041-26aa-3045-92b7-243039808538 | -3.17609 | -43.25125 | 2024-10-15 04:46:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3767517-246b-394d-9ba5-30eb1a9aa934 | -3.92293 | -42.41362 | 2024-10-15 04:46:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 0d340e05-2253-3910-b756-2369a22aedb2 | -3.9224 | -42.41726 | 2024-10-15 04:46:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 45f2817f-e534-3f8d-9ce7-5615b69713a9 | -3.91847 | -42.40556 | 2024-10-15 04:46:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 49.8 |
| b901408a-5d5b-3ae5-83a8-2080086697ae | -3.91794 | -42.40918 | 2024-10-15 04:46:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 49.8 |
| 0479dbcf-e9f3-3289-b6c3-139bc206a845 | -3.91741 | -42.41282 | 2024-10-15 04:46:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 52.6 |
| 82c66baf-8bcd-344b-946d-e42aa652770f | -3.91688 | -42.41645 | 2024-10-15 04:46:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 52.6 |
| 819fd333-b893-3d52-b59d-4d901d447830 | -2.81516 | -45.28795 | 2024-10-15 04:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9524d183-a0cc-33e1-b9ad-84737f6dc9b0 | -2.81071 | -45.28727 | 2024-10-15 04:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc7e3925-9c01-333e-9af1-6258cde91ec3 | -2.11933 | -46.05657 | 2024-10-15 04:46:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08f2af71-6f9c-320e-8ff9-d02a802cb430 | -2.11873 | -46.06041 | 2024-10-15 04:46:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fa67cb3-4819-3e3b-825f-cb5848598178 | -3.31239 | -47.01169 | 2024-10-15 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b76c439c-7de9-38c6-9048-0fa74cdbb9b9 | -3.06072 | -45.95469 | 2024-10-15 04:46:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 939daa60-847e-3faf-b32e-e7d4837250fa | -2.96857 | -46.95025 | 2024-10-15 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2cd0e1e-b86a-3190-a6d1-6c1fe39c7598 | -2.78086 | -47.29016 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15454643-da75-3693-8225-6cf2d24a0e88 | -2.71689 | -46.71085 | 2024-10-15 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 108e2917-8668-3cab-aa30-d82f62b100a0 | -2.57924 | -47.06341 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 542752e3-fffc-3aaa-998e-0886ffba16fd | -2.5753 | -47.06285 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| beb71c40-c4ef-3b25-82b7-2f90311c2b1a | -2.34407 | -47.26017 | 2024-10-15 04:46:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 429d4d71-8309-398c-b6be-72beb33349a1 | -2.33152 | -46.48161 | 2024-10-15 04:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6d59627-8ac5-3391-9ba1-e2d90834cfee | -2.33096 | -46.48523 | 2024-10-15 04:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f650ee6-aaaf-31f1-a01e-e5b4c4cc63e4 | -2.32965 | -46.68151 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ea39d3b-4009-382f-9f4c-a3757c77832d | -2.3291 | -46.68502 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08c71866-dd17-3550-a874-b07ccbb30d85 | -2.25316 | -46.75198 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93087fd9-87b1-38eb-af90-c1e7985e4e3c | -2.25264 | -46.75543 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8d1c8ed-5d26-3f4b-a542-ecf0c961175c | -2.25211 | -46.7589 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 269ae103-a749-37df-961d-c979ee29d53d | -2.25106 | -46.76584 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e9c2480-6548-3f4e-942d-82d6d3ce696c | -2.24759 | -46.76177 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c96f2526-aee4-3f33-b60d-8398c2dc59bf | -2.24707 | -46.76523 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7b3e445-0977-34ca-aac0-2b00b5edb5c4 | -2.24151 | -46.77497 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ac3c551-479f-3798-8592-b5b1bed63576 | -2.23752 | -46.77435 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43317345-f3b1-35fd-8a50-16c3ac8e121f | -2.22768 | -46.77275 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46e3cac0-00d8-30fe-904b-8a98d3104352 | -2.19202 | -46.73904 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93944ee2-f502-3132-a4b7-867d4bb6aec7 | -2.19149 | -46.74249 | 2024-10-15 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README53.md)
