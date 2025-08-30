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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 246aa6c5-3575-3a32-9ddf-861b36e21ff5 | -11.33095 | -43.60878 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a53df30a-91c2-3301-8eef-ddd2d21c6825 | -12.93546 | -48.1179 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e482d72d-4bd6-3d0e-b19d-2fcaa299dbe8 | -11.84977 | -46.37649 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7c67a24-4b08-3349-abb0-acec2e4ce87f | -11.41118 | -44.68425 | 2025-08-30 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec241092-a50f-33f8-9529-dfed1fc87267 | -12.40571 | -46.47478 | 2025-08-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 797248be-0324-3c0f-9062-cf23d628a472 | -12.8416 | -48.13314 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 66781111-4da2-3ceb-a155-d0d8a8c22d48 | -13.35437 | -51.77565 | 2025-08-30 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6571ffbd-7cca-3ff5-a322-7123b1734179 | -10.0174 | -48.0652 | 2025-08-30 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1378c9ce-0545-313f-994c-813ad5e617f7 | -9.60188 | -45.76537 | 2025-08-30 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c453815-6a19-3122-a356-708b3d9d5f6d | -15.36899 | -44.28555 | 2025-08-30 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 33ca285e-0ee6-3c9d-91ba-5fce80f2a47c | -11.30898 | -43.61323 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cd964c0-de65-3505-83d0-97e00cc6bc68 | -13.53156 | -46.94932 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 4acd87bc-bffc-3b90-a2ee-75fed05d8b4c | -12.85554 | -48.15495 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7fcdf0f6-b9f5-33e1-ba6a-ca5cff4522b3 | -10.72214 | -47.00568 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e2d6a58-83c8-31c4-b554-2e24c55e52f9 | -10.36495 | -59.21144 | 2025-08-30 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 45e925a5-92ad-32cd-8b7a-ad912ec9dda7 | -12.8867 | -48.15975 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 335d382b-c3ad-32f0-8460-cb3590524be5 | -13.41276 | -46.94806 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c728eb8-5491-31da-86c4-4bfe9f4764c8 | -10.38525 | -57.82702 | 2025-08-30 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ba8ab64-ebf8-38da-be67-9a0b98c6ab93 | -10.37797 | -57.83064 | 2025-08-30 04:21:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83890348-2995-3e20-9d77-002005a836b1 | -11.85415 | -46.39162 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1cc39a4-ad8b-3418-b49d-d817df13b305 | -14.00478 | -44.59021 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca0ea9c8-04c1-38c0-a2a3-7e0317de7792 | -13.40061 | -46.96051 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d413f481-f38c-37cd-a8d9-1f7b98e22364 | -11.86454 | -46.45462 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7522b93d-4b29-34d1-8fec-1d2bd68a08d1 | -12.69604 | -48.1432 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cafc900a-46ef-3d67-b276-84e8d0542c2c | -13.38678 | -46.96198 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e803051f-a09c-3412-a401-0df49838a6c3 | -11.30426 | -43.57276 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc05d88e-20f3-33c3-8188-be6a50da47e9 | -13.42657 | -46.94669 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b8142fb-bc7b-3459-9ee8-1052a8c60e7c | -11.62068 | -47.30084 | 2025-08-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dd8e1c6-663c-3804-a1be-40d7c3e28854 | -13.46413 | -46.94539 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87b4e189-6b2a-3ef0-90cd-a486082cd51c | -10.49073 | -51.63515 | 2025-08-30 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 279b4e84-c995-34bc-ab69-304522e36aef | -14.00304 | -44.57829 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b1265cb-4cb5-34ba-aa1f-0de21d0a1f56 | -12.38757 | -45.00599 | 2025-08-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe6e4f85-a102-338c-a266-c887d2ded3ed | -16.41192 | -45.65225 | 2025-08-30 04:21:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b8c9b14-8ca2-36e6-8da3-4af7c52374bc | -11.29616 | -43.57955 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a46432f-f43f-35f4-a930-75014f28976e | -13.51447 | -46.95009 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bf2f1f6-4afc-3241-a4fc-2a5cdb0d5025 | -10.02629 | -48.09842 | 2025-08-30 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc72bd8a-3d44-3c2c-9e0b-149847de1b63 | -13.39284 | -46.9666 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afa2830c-75a8-3b65-9c66-c3a693b2a260 | -11.08724 | -45.13498 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b1d8620-32aa-3510-8c32-656e58514e54 | -10.37439 | -59.20028 | 2025-08-30 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cf81e2d9-55de-3a14-b1a5-32f588ceff4b | -10.07636 | -58.36542 | 2025-08-30 04:21:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d9cabe2-2241-3c72-a278-190a6cb2d7b6 | -11.31599 | -43.66198 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9f27373b-d999-331b-9639-5a2b62317205 | -15.17602 | -48.02841 | 2025-08-30 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 331dcec9-a1a5-3b5d-840f-8d8b9884732a | -14.00213 | -46.3341 | 2025-08-30 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 932f9de1-4bec-34c4-89b2-44806d1dcf89 | -14.00268 | -46.33055 | 2025-08-30 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bab90f73-71a9-3d15-afa2-a2b08674fb4a | -8.83265 | -47.48277 | 2025-08-30 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a9a47c3-9991-3cca-862f-71986b766652 | -11.07334 | -44.60262 | 2025-08-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f588ef21-f956-36b3-9de2-98d45a3c1e4e | -12.93425 | -48.12533 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8bfc125-adac-3366-8602-adb910b0b0a0 | -11.32116 | -43.65094 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30ecba4f-dfd7-3a66-b1ae-2f35f8871f18 | -11.29804 | -43.63938 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a3369dc8-9993-3475-b065-a132e39cd344 | -14.99582 | -46.7011 | 2025-08-30 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e585d7c9-1d07-339f-9053-3bf2dca3892d | -12.84912 | -48.17295 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6084cbe0-8f27-394f-90fa-40e59a35c662 | -13.39729 | -46.96 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0bfe6f0c-c944-3003-b484-b160a90886a2 | -13.57577 | -46.9059 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b24eda95-7b87-3ca6-bb49-b1d3ae38d879 | -13.63122 | -48.18729 | 2025-08-30 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0b83c2a0-a6b3-37d0-85d5-f54e43ea4ec6 | -11.91351 | -44.2602 | 2025-08-30 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f01f3066-4461-3951-94dd-8360c584f43c | -14.24143 | -48.06241 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b531573d-f70f-3901-a639-ea725b077c91 | -15.23869 | -48.25764 | 2025-08-30 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73f2747e-0582-3d9b-9b1b-ca261723912c | -12.84036 | -48.09776 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f399a41e-37a9-3d05-ac52-effc57605381 | -14.85545 | -46.77227 | 2025-08-30 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fa16c3d-ca8d-3af5-810f-007f89490be3 | -13.3761 | -47.00764 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d98cefc1-5e6d-3c73-bf1b-53baafe15de2 | -10.54159 | -56.38711 | 2025-08-30 04:21:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9f33cce-f368-350e-8d85-e8b7a76dc5b2 | -13.37327 | -47.0254 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d905d3f-f4f2-37e5-b4c9-5103e1e66366 | -13.46963 | -46.95353 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9390fa1c-ccde-3307-96dd-333d34fc3902 | -12.9231 | -48.10813 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bf90a41-3598-3086-83bf-7ebc4bfcdf11 | -13.36985 | -47.00313 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 331205d4-3172-3443-8e2a-e205c4703acc | -13.36991 | -46.98125 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1561f4f3-44f9-333f-8448-04bc60d6ea42 | -14.02238 | -44.5423 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| faf2d643-a888-3c64-be54-980ef2807a52 | -13.3641 | -46.86757 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c50a1679-e358-3e29-9079-b63135138266 | -13.54148 | -46.95102 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 426b9a4d-87ad-33fd-8667-35182b384410 | -13.59953 | -46.8844 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63ff24df-ad60-38a3-9b10-fcc753ce6970 | -13.45694 | -46.94791 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf581a71-c5e4-3d5c-b899-e88a05b4e6d2 | -10.02212 | -48.05809 | 2025-08-30 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6ae2edf-ce06-3712-b41a-9b2d9f87374a | -11.15192 | -47.14949 | 2025-08-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c222f67-5538-3d46-b3d3-d25485613eb4 | -9.5796 | -54.47326 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 626b07d3-84e0-35c3-931a-509d69b39395 | -9.70652 | -49.46758 | 2025-08-30 04:21:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d5e26b66-e05c-34d4-9292-ec5744efa432 | -12.65545 | -48.19834 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dde7a844-0dd1-3abd-bdcd-2c6b9cfb9d47 | -11.74075 | -51.75566 | 2025-08-30 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b7f2361-a4e1-3cce-9e9a-596c3e9ee946 | -14.59589 | -54.49216 | 2025-08-30 04:21:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50e39deb-3ffb-3d38-9a03-b12269a56e1e | -11.82925 | -46.46331 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 7f0fbae1-6875-3515-8324-b1f9026bab58 | -12.32292 | -42.85725 | 2025-08-30 04:21:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a2e26c6e-3ca5-318f-b55c-bb1f23c35614 | -14.00815 | -44.56741 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad93df8b-db80-387a-afd8-016c0cae9f60 | -13.35968 | -46.87406 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e4a2828-b8e3-3e53-9009-a5f330197a5c | -13.69076 | -46.91051 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 914737aa-38cf-32be-bd19-2c75175d10b5 | -12.69421 | -48.15439 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b0be302-c512-355d-a26f-38e0fe339bda | -11.57325 | -46.36014 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 399e605b-49a3-3063-8dcc-f9ecfb2ba9ca | -13.19412 | -45.29134 | 2025-08-30 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d7c6617-a3b6-3fe3-bf68-51d661b8bf25 | -14.32456 | -51.95336 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36cfa466-3f5c-31f0-9257-e8b7043e6621 | -14.99307 | -46.69699 | 2025-08-30 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fb266a7-cbcd-3b06-ab8b-5d741e8db5c0 | -8.51195 | -54.71634 | 2025-08-30 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5973ed76-e165-381b-ad61-99d294647151 | -9.50934 | -54.44151 | 2025-08-30 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7703bc0a-c38c-3f21-b128-9755954447d0 | -11.94219 | -46.69523 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a60eed1-14c0-39ea-8bfb-b42ddf2a751c | -11.38068 | -54.34988 | 2025-08-30 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bde864b4-47f4-31b4-9929-f7ebd151bfa5 | -11.25277 | -45.00895 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e3badc4-8e83-327e-9310-7cda1f96a275 | -11.22278 | -45.00433 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a671451-e3f4-32cd-9fca-e5a6fccfc286 | -9.65547 | -54.43902 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0f88f51-7f37-3a2a-811d-bdb845e2e76b | -11.89462 | -46.71644 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ad4043e-3aa6-39f6-b945-5809ada19014 | -10.69226 | -47.06358 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4d10e9c-c960-3eeb-a1ec-93b55be963ca | -16.26371 | -43.61604 | 2025-08-30 04:21:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8db2c18b-e665-31b8-b9f1-a5a890652a4b | -11.85912 | -46.3816 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca5e9740-60c8-398e-962d-3aebb72cbf87 | -11.14408 | -47.15559 | 2025-08-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README28.md)
