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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bb10a9b-a581-35a4-90d7-f33fe21a759f | -9.26337 | -50.69267 | 2026-08-01 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54de64af-cdf0-3238-b241-262a9d01307a | -7.29994 | -55.31919 | 2026-08-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9b43e278-6fd9-3a42-bf4d-6459856bedce | -12.81161 | -47.17085 | 2026-08-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 398ace6c-1c29-33d2-93c4-f91991641dd5 | -11.77463 | -50.16822 | 2026-08-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c81d32e3-cc3e-3604-af30-7a1a9e3520b6 | -14.0779 | -46.23631 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80affddb-a606-3821-9d72-79349fbac1f6 | -11.22713 | -54.83894 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d59d8294-2ee2-3559-b32c-82edd222a48a | -14.34601 | -48.04296 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2134920b-03e0-3348-b456-08dd19042ad9 | -14.07131 | -46.27878 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| b4142aee-1bbc-36bc-89ee-609f6b54f474 | -14.07461 | -46.25753 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28a6a618-d383-3f36-b173-64265da09740 | -12.61301 | -44.61863 | 2026-08-01 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 552354af-39e7-3839-854d-7d689d5878e8 | -14.07958 | -46.29102 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62c3442d-78e3-37f5-a755-1d79f24f1bbe | -11.24296 | -54.86901 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bf56b0d3-bf36-300b-a6b4-139a54a37e99 | -14.77434 | -48.30247 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4220e903-d6e6-3acb-a328-4cfa9cb0157d | -11.77001 | -50.17231 | 2026-08-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c0b2231-e591-363c-bb0b-ca83c223afb8 | -13.93768 | -49.28824 | 2026-08-01 04:21:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40bfba12-c50b-3e38-b268-f172acb559b9 | -14.832 | -48.51027 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d64293d-f39a-32c9-9437-37a4881d4140 | -11.25 | -54.86038 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| ef92e8f2-778d-3bc6-933b-0daee7f077cb | -12.61074 | -44.61077 | 2026-08-01 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31d7fff2-d910-3b99-94f9-cd72c48eddfe | -14.07736 | -46.23985 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da4e85aa-1bc4-3ef6-aadc-0f7898537909 | -13.26141 | -54.3653 | 2026-08-01 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2857e70-784c-34db-8c1d-545ae8b21388 | -11.13899 | -49.90498 | 2026-08-01 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d770181d-3265-3d1c-bb00-fd56130a54dd | -8.18812 | -55.43852 | 2026-08-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 296267f5-43ff-357b-bbff-f56275c86ad8 | -22.34391 | -42.57201 | 2026-08-01 04:23:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f85f77e5-87ad-38e5-a270-eb85dfa1cb4e | -20.51701 | -48.86246 | 2026-08-01 04:23:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ed547473-71e5-3bcf-8799-eb4096868bd8 | -20.04193 | -44.1996 | 2026-08-01 04:23:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 35b531ee-bc8e-38d0-8ec1-436b87ff57c6 | -20.11249 | -50.74424 | 2026-08-01 04:23:00 | NOAA-21 | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.5 |
| 4f4dac9d-0bf2-37ef-b727-b5ca8ce881e8 | -20.38638 | -47.75012 | 2026-08-01 04:23:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2fdf992-8503-3994-ba0c-6f4c0e2cd9bc | -16.3968 | -53.34655 | 2026-08-01 04:23:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f3b7e3dd-8ad8-3e67-94ac-59e5e850c5ea | -18.48547 | -51.69492 | 2026-08-01 04:23:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd303ed4-0679-32c1-a7d0-ed03a66d208b | -18.51421 | -42.89174 | 2026-08-01 04:23:00 | NOAA-21 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 24ed38b1-9cc5-380d-9619-c967b0cbf7ab | -21.41406 | -48.07091 | 2026-08-01 04:23:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9613fd2-fade-3441-b99e-2deac784e803 | -19.30232 | -47.44182 | 2026-08-01 04:23:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c0dfd7ab-fe8a-39d1-b43b-6d61d9b3a17b | -17.79177 | -44.24026 | 2026-08-01 04:23:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ded1333a-c34d-361d-b0c3-7d4632c42445 | -18.51279 | -42.89459 | 2026-08-01 04:23:00 | NOAA-21 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4fc8cdd9-193d-31f6-a1a8-328f93945545 | -20.51641 | -48.86619 | 2026-08-01 04:23:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 17d6b925-39b0-3f6c-bd57-0fe6de324d81 | -20.52529 | -51.44569 | 2026-08-01 04:23:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f49e58e4-f793-3559-9298-0bf2a1283d53 | -16.18814 | -47.93047 | 2026-08-01 04:23:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 86483b53-b813-36ea-9ed6-6f100b141b7a | -17.39886 | -47.33184 | 2026-08-01 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06003dc9-16c2-3b3e-903c-5fe6cef7b72b | -17.05483 | -45.87082 | 2026-08-01 04:23:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccc2e9bf-a32a-3962-b15b-ab32f426e053 | -16.04956 | -48.52742 | 2026-08-01 04:23:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c44b020e-091b-33a7-b463-ebb526d56769 | -20.88153 | -48.98462 | 2026-08-01 04:23:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c4a1779c-f46a-3a6c-8525-556f6b20ae2e | -16.04838 | -48.527 | 2026-08-01 04:23:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 142db819-dcc5-3f0b-9a59-d813ca551b3d | -17.43209 | -42.63659 | 2026-08-01 04:23:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ca07c111-7506-38ce-a651-c8df26c2c242 | -17.41975 | -42.64 | 2026-08-01 04:23:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e523456a-7a26-3e48-afc6-fea37f1d2559 | -22.75433 | -42.87786 | 2026-08-01 04:23:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5823bd15-137e-360a-9ea6-b9354aa3250b | -17.89818 | -44.30712 | 2026-08-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a442a67c-7a16-300b-887a-b801046045ba | -17.04862 | -45.03048 | 2026-08-01 04:23:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17157fcb-e62f-3ca0-9c75-044610542ad4 | -22.12673 | -43.25314 | 2026-08-01 04:23:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 7597dddc-a25d-37ff-8f5a-ed66209a8f8c | -17.00577 | -48.28447 | 2026-08-01 04:23:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef3cd2cb-6e18-3c46-8a9b-ebdcc50b2f97 | -16.63789 | -49.53876 | 2026-08-01 04:23:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e344ef6-758a-39bd-8de9-84e5a9a395b1 | -22.23285 | -43.11908 | 2026-08-01 04:23:00 | NOAA-21 | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 91d2d52b-0dbf-30d6-be52-7c9f74032ce7 | -16.43382 | -51.0906 | 2026-08-01 04:23:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4d8919ff-0c06-3841-80de-126fdc7085b6 | -22.34796 | -42.57373 | 2026-08-01 04:23:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| adc8ca42-0d68-3280-b62b-c68f2bfc17cb | -17.05372 | -45.87824 | 2026-08-01 04:23:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e67128c3-931e-3ba4-8ec8-a5ac6a580e67 | -16.33 | -48.06696 | 2026-08-01 04:23:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26f3859d-03e0-3b27-ac28-c14e5848bb50 | -20.99109 | -47.46354 | 2026-08-01 04:23:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df546be8-5cf7-3e36-92a0-9dccc2363080 | -18.48375 | -51.70448 | 2026-08-01 04:23:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ae8dce24-a6e9-3522-9ec2-1ae77387b92f | -15.92078 | -48.32162 | 2026-08-01 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed2d8011-34a5-3063-8f7b-831436637c04 | -18.49625 | -51.61326 | 2026-08-01 04:23:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 772f8922-89b3-39fa-8d0d-f3671d7777e7 | -22.13074 | -43.25359 | 2026-08-01 04:23:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6a8bfac3-1202-3d37-b3bc-aeb8c4f4495d | -22.23332 | -43.11531 | 2026-08-01 04:23:00 | NOAA-21 | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 799aff79-6308-3c5d-8711-ffda29564c09 | -20.7042 | -54.58829 | 2026-08-01 04:23:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a2fd9ca-5efa-3bc3-9eb4-db04388b740b | -20.27009 | -44.52457 | 2026-08-01 04:23:00 | NOAA-21 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 77b8b29d-a29c-3b2b-abaa-465edbb2e6da | -22.67514 | -43.7883 | 2026-08-01 04:23:00 | NOAA-21 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6a072297-2e06-3c32-90ca-b49600d4d569 | -17.90176 | -44.30767 | 2026-08-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4128fb1-7e9c-3c63-a269-74d50ca2b242 | -20.70334 | -54.59268 | 2026-08-01 04:23:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55f83bcd-3952-39e6-9eaf-522830a3092d | -19.20829 | -46.10822 | 2026-08-01 04:23:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2dbdffc2-12a3-3ddc-8c6d-4ec97ce47a2d | -20.52608 | -51.44122 | 2026-08-01 04:23:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8e2cc19a-c5f0-3c95-bc82-a23cde7988da | -18.38685 | -47.20905 | 2026-08-01 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9b7f7371-1d27-3fbf-a61f-906b5887a8e6 | -16.40773 | -53.34735 | 2026-08-01 04:23:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 567feaf4-d06b-3d5b-979b-25864b39d049 | -18.48172 | -51.69414 | 2026-08-01 04:23:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bf80f538-9c6c-3ec0-8bf4-637f8a4e7a20 | -18.97771 | -41.03227 | 2026-08-01 04:23:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| da908b83-e984-34cc-8c71-5831635834eb | -16.59507 | -49.26259 | 2026-08-01 04:23:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02a473d6-2f75-3272-95da-da1512069d17 | -17.06269 | -45.88728 | 2026-08-01 04:23:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0373cc59-98a4-3ec2-a5b6-2937be8d556a | -19.20092 | -49.62153 | 2026-08-01 04:23:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0084dbb-b906-3c1f-9a75-1ba7cca12500 | -15.57605 | -50.27057 | 2026-08-01 04:23:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ac3273c-8529-3172-961b-aa836d75a818 | -16.45187 | -48.79408 | 2026-08-01 04:23:00 | NOAA-21 | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14b91da6-3f0f-3cfa-be15-c9c9a58f20a4 | -21.25987 | -49.15309 | 2026-08-01 04:23:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 7a9407c7-569b-39fe-8046-1e50173d9db7 | -16.40692 | -53.35165 | 2026-08-01 04:23:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba35a118-a7f8-3d22-8d83-981d01e29b6f | -17.42364 | -42.64055 | 2026-08-01 04:23:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 139e52ab-3675-31a9-bc96-9561b2447142 | -20.59829 | -45.13183 | 2026-08-01 04:23:00 | NOAA-21 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c8ed783b-f44a-3b39-b27b-cd9e9b39c3d8 | -17.42753 | -42.6411 | 2026-08-01 04:23:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dbcbd09c-7e88-3f75-a589-954cf95665c5 | -21.2632 | -49.15371 | 2026-08-01 04:23:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 66c0a174-3447-3168-8f41-38eea0ac8e97 | -17.42888 | -42.63097 | 2026-08-01 04:23:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44df2194-b2e6-367d-8fd1-d69e07367224 | -17.8976 | -44.31136 | 2026-08-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d35aa7e8-30bd-3908-8ce4-65658f4d4dd4 | -17.43277 | -42.63154 | 2026-08-01 04:23:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97d1c187-34a9-359e-b41e-d57c8685db7f | -18.49541 | -51.61798 | 2026-08-01 04:23:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 720e1e2e-4719-3e81-a1a6-ef61f284ca37 | -17.04806 | -45.03437 | 2026-08-01 04:23:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be39e843-2dbc-3122-b209-265bdf8c44fb | -16.40538 | -53.34834 | 2026-08-01 04:23:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 692ccba0-ca46-3354-90f6-c1920baad727 | -17.05709 | -45.87878 | 2026-08-01 04:23:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2fa819c-2132-3eec-b12e-170d05949146 | -21.65865 | -45.90694 | 2026-08-01 04:23:00 | NOAA-21 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| f2bbb489-a717-3669-a1eb-946e8769f5ef | -19.23227 | -56.75711 | 2026-08-01 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 730d970b-b7ee-3735-b8ce-cbe7bfbd3368 | -17.42431 | -42.63546 | 2026-08-01 04:23:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b74de070-b45d-3e2e-ac68-1fef98a217b6 | -22.12879 | -43.25177 | 2026-08-01 04:23:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 9b89236e-8011-3315-8e22-aba2598a469b | -19.91083 | -42.2494 | 2026-08-01 04:23:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3eb642c4-ba4d-3afe-8262-c12774ae158b | -18.48461 | -51.6997 | 2026-08-01 04:23:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 986caa5b-8868-3180-9d29-d8e01d0c57ed | -17.42821 | -42.63601 | 2026-08-01 04:23:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9f9604b5-125e-39f2-98da-5911ab81df84 | -21.42713 | -45.479 | 2026-08-01 04:23:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 091e304c-1148-33cc-98e1-b670ad20a7ab | -21.24139 | -49.16124 | 2026-08-01 04:23:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 063577ed-6b03-38b8-817f-e123efead744 | -21.41463 | -48.06722 | 2026-08-01 04:23:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README15.md)
