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
| 0a374ef2-57b7-3069-8600-760811795abe | -12.68078 | -58.09522 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54c46005-0ddc-3315-8984-a67478c7d2d9 | -12.6591 | -58.09074 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbfbac9f-84f5-3348-8545-6f9de909471b | -16.68082 | -43.88469 | 2025-04-30 04:36:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b837cfa-76d1-31ab-9815-fa4384aade09 | -12.66542 | -58.09203 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 894998b3-19c9-3f57-84e7-7c3e6d3e2ad7 | -12.66418 | -58.09834 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 254250df-c010-330a-9b03-31d97f235574 | -14.01611 | -50.73287 | 2025-04-30 04:36:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 658fea16-eed8-3b19-91ac-b6bbce752228 | -14.0167 | -50.72923 | 2025-04-30 04:36:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d25f11e-5ec1-3262-a0b6-801d8ccc51d6 | -15.16913 | -52.97498 | 2025-04-30 04:36:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f501dbd-1c03-3a13-b61c-e103a54ad778 | -12.10777 | -51.39581 | 2025-04-30 04:36:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea78ba32-ed02-36d6-8616-9390de1febf1 | -12.35347 | -54.51474 | 2025-04-30 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16d0289d-44c1-3e6e-a53f-bbb2097d43dd | -12.1043 | -51.39521 | 2025-04-30 04:36:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23571697-73d1-3b96-a707-eacfc5dcf966 | -15.19713 | -51.56407 | 2025-04-30 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 404e54fd-a186-3289-b06a-22385c4b9cd1 | -12.66357 | -58.10146 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8758a8a-0dad-30d0-9216-61dac2935383 | -12.35284 | -54.5184 | 2025-04-30 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 978ee64a-72b1-3db4-8569-832af023493e | -14.86962 | -49.0661 | 2025-04-30 04:36:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23a68616-5503-38ad-a73d-6a626e35218a | -13.82339 | -42.6954 | 2025-04-30 04:36:00 | NPP-375D | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4e10714f-de44-3866-8969-7828f72cc3be | -12.6648 | -58.09519 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11b21805-ccbc-3a44-bd27-3d81a1511330 | -12.68198 | -58.08903 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 792bfa0a-e6d5-323d-ba80-3916bd387efa | -11.49598 | -54.57212 | 2025-04-30 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 408d5f44-3307-3c9c-ad13-8134fac0cd1e | -15.20054 | -51.56467 | 2025-04-30 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce823b22-9865-3722-a0f8-1d317b8e365c | -16.21059 | -48.98928 | 2025-04-30 04:36:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1f4cd5d-e68b-3a63-97d6-4a9afb841148 | -12.68138 | -58.09212 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccb53566-fa96-3afc-995d-fab0caea170a | -12.6603 | -58.08437 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 994ccb78-4a0b-3e7a-97ba-35e30ec14d92 | -14.85886 | -52.84531 | 2025-04-30 04:36:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73cee13a-e067-3fdf-aed2-2739466c709d | -15.07718 | -48.94394 | 2025-04-30 04:36:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 334f7b91-797a-387d-8ceb-06d56887e9d8 | -12.66303 | -58.09812 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c6f77e2-b7ee-3143-ac7a-7f3bdcb00156 | -12.66244 | -58.10124 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9c918c7-937a-3ae3-8d77-f38eef9008ce | -14.85527 | -52.8447 | 2025-04-30 04:36:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 62b93a0a-45ac-3670-ab27-a9465ab3d1c8 | -12.67959 | -58.09499 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b976935a-de35-3aa2-8e80-4b6d557b444b | -12.66422 | -58.0918 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3595199a-6d9e-3af7-8101-50a463153ee3 | -12.66363 | -58.09497 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20ff1c8e-57b6-3977-854c-e3e244e6d5b5 | -15.56907 | -47.85345 | 2025-04-30 04:36:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6cc64fb-72d2-3b12-943e-d3f38729f0fb | -14.59428 | -50.61355 | 2025-04-30 04:36:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e077ba47-94ec-334c-8c88-add1ee022f7b | -12.67689 | -58.08786 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 61bd09b8-0012-37de-a0f3-3c762d548616 | -12.6597 | -58.08757 | 2025-04-30 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7be0cb3a-96a7-3dce-9c7a-7c3863b89a18 | -21.23681 | -47.62203 | 2025-04-30 04:38:00 | NPP-375D | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c95af0ec-9149-334f-a91d-4b0843aa1006 | -20.47582 | -53.67543 | 2025-04-30 04:38:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44470f22-9262-3167-b77f-f7bb0ec76311 | -20.21141 | -46.04015 | 2025-04-30 04:38:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4965a259-13a0-3c8f-a2e0-c025f255e3ad | -23.3398 | -46.77061 | 2025-04-30 04:38:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 635b4d21-af3c-3063-8671-c44a5987d24e | -23.59251 | -47.43711 | 2025-04-30 04:38:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a585bc6b-be9e-308e-b040-617547e70ffb | -19.45177 | -45.30676 | 2025-04-30 04:38:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21d66431-6ecf-3a70-b76c-66d4d25ef112 | -21.57473 | -47.28156 | 2025-04-30 04:38:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7104232e-80fe-3054-9292-105e4e63bbaf | -24.24173 | -50.73789 | 2025-04-30 04:38:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 668c5842-8a21-399c-8650-810c5e64e71e | -20.07618 | -44.30421 | 2025-04-30 04:38:00 | NPP-375D | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a1a15763-a20b-3652-8f1f-31dc85cc220b | -21.19336 | -44.93853 | 2025-04-30 04:38:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6619c211-9068-33bd-9d00-ad03b9a47bc5 | -17.47981 | -57.8158 | 2025-04-30 04:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5aed2996-3afc-3cbf-a8d2-88f63604bdf6 | -20.99567 | -51.79283 | 2025-04-30 04:38:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8ef04ba1-9b76-3191-b876-1d6945e3d78d | -28.58652 | -49.4397 | 2025-04-30 04:40:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cb79715c-6022-30c3-9614-023086a0343f | -29.35783 | -51.90646 | 2025-04-30 04:40:00 | NPP-375D | ARROIO DO MEIO | RIO GRANDE DO SUL | Brasil | 4301008 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ae38df50-6dbb-3b6f-b50e-697b828b974c | -29.35443 | -51.90582 | 2025-04-30 04:40:00 | NPP-375D | COLINAS | RIO GRANDE DO SUL | Brasil | 4305587 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dca7d246-dc49-38b4-86f3-ed2cf03de27e | -30.15104 | -52.02479 | 2025-04-30 04:40:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 2d5d00b6-2bb4-3af4-bd2d-523418485a99 | -2.62849 | -51.95304 | 2025-04-30 04:53:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ee9ac4f4-f130-30a7-8385-e8bd9dee1890 | -2.62512 | -51.95251 | 2025-04-30 04:53:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f549a173-cd31-3ddf-8c81-82a27e5b833f | -8.47409 | -49.85579 | 2025-04-30 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11c96d88-a0e7-3358-be40-7ac941b63499 | -8.90194 | -44.78617 | 2025-04-30 04:55:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d72c8599-8dac-3c9c-95cd-89bfa56a6410 | -8.95191 | -44.23496 | 2025-04-30 04:55:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de543187-b973-3d8f-83df-13da4ff52a02 | -8.22028 | -49.73512 | 2025-04-30 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cf43e74-2500-36c4-930e-c551b24371f4 | -8.89633 | -44.7855 | 2025-04-30 04:55:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73c139d0-25d8-3918-b68c-3bc959b09d18 | -4.13098 | -54.89782 | 2025-04-30 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12417408-f5d0-3fe9-810a-5fa25d0f7013 | -6.63053 | -48.01562 | 2025-04-30 04:55:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9801c8b7-618d-3fac-aef9-a4ed87d27e5c | 3.15314 | -60.27094 | 2025-04-30 04:55:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec610690-cdec-38f5-92d9-127b201db31a | -5.83057 | -44.43867 | 2025-04-30 04:55:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9a34273-ddaa-383f-a22d-6a23e7ebfcf3 | -8.94611 | -44.23409 | 2025-04-30 04:55:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| acd33de0-d0bb-3f02-81f1-85fb6cd171df | -8.9003 | -44.78325 | 2025-04-30 04:55:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a7b9ee8-994b-3075-9b02-0c3b26dd9587 | -7.08045 | -44.38121 | 2025-04-30 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e8b53b8-b452-3e4a-b82f-3fc0573aa4a3 | -7.08555 | -44.38578 | 2025-04-30 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 666b0e2c-e73d-34c7-aef7-93c0a2d90a55 | 3.92878 | -59.91523 | 2025-04-30 04:55:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 831296fb-1eec-342a-91ff-3b455187327c | -7.06815 | -44.3876 | 2025-04-30 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1064800f-c79c-3224-8807-50811895b659 | -8.21859 | -49.7358 | 2025-04-30 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1202a70-bb33-3d6d-bc07-60fb892d9979 | -6.62994 | -48.01966 | 2025-04-30 04:55:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55dc1c22-77c3-39de-9350-fbfce11bd116 | -2.53423 | -53.95574 | 2025-04-30 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bf967ed8-5e89-3e53-958f-871024aa5e88 | -8.89983 | -44.78692 | 2025-04-30 04:55:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4aca335-7f21-3b22-8f87-f21ea2b7065b | -5.79341 | -43.61546 | 2025-04-30 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 279aebb1-07e5-3b40-95bc-29a95dd665ba | -7.08609 | -44.38182 | 2025-04-30 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e40e5c09-76b6-3fac-a886-fc5e820f475a | -8.9403 | -44.23324 | 2025-04-30 04:55:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0d673bb-82a0-3d6d-819a-a0a83523920a | -7.07377 | -44.38833 | 2025-04-30 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 819574ed-defe-3a47-b6be-d0b0a0cbe0a3 | -7.07992 | -44.38511 | 2025-04-30 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f94fbd74-de19-33f2-a1a2-00fea8a69a5d | -8.94664 | -44.23006 | 2025-04-30 04:55:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f9b5ad3-fced-328d-9f8e-0ee3644790b1 | -7.07326 | -44.39206 | 2025-04-30 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20c89db4-b51e-3699-8c08-1d18785ddaff | -7.08098 | -44.37728 | 2025-04-30 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd4c58d0-6daf-3e71-824f-95051a64e9eb | -8.90244 | -44.78251 | 2025-04-30 04:55:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edbf0c6b-3c40-3d3f-85b5-11ba2a950cf5 | 3.14854 | -60.27467 | 2025-04-30 04:55:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7992a413-c9bf-3f13-bb4b-de5e05bf78f6 | -7.07429 | -44.38447 | 2025-04-30 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb6f3e75-9de1-3530-b112-35eddd9a7720 | -7.08663 | -44.37784 | 2025-04-30 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 233302fe-f257-3da1-bd61-c2ef9c430a43 | -8.94083 | -44.22916 | 2025-04-30 04:55:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10177049-4484-364a-97e7-2ab58cf03f5d | -7.06867 | -44.38374 | 2025-04-30 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48d1e8bf-8cd8-3e72-8c70-4e743c77b5d3 | -12.68063 | -58.08937 | 2025-04-30 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35e854aa-b1a2-37aa-a7ce-1cdfae2716c2 | -15.16832 | -52.97526 | 2025-04-30 04:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 674554a3-4051-346d-a94e-e851f0c20a09 | -11.79644 | -47.37505 | 2025-04-30 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c8e0f0a4-aa90-3cb2-a3e1-ea20c6f9d494 | -9.93566 | -59.20848 | 2025-04-30 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9792449-ec38-38db-a52a-76b5357692bd | -16.20844 | -48.98811 | 2025-04-30 04:57:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00ccfb5a-3f44-3e19-aca1-7181730330e1 | -10.50817 | -56.42062 | 2025-04-30 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52ca6b03-cccc-312e-ba4e-60824a82cfeb | -11.39914 | -52.955 | 2025-04-30 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4b3a213-a542-3dd0-a191-f9bad0d78a5a | -11.39972 | -52.95113 | 2025-04-30 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8e6474e-96ef-3793-b180-a85b7b4ae618 | -11.39859 | -52.93505 | 2025-04-30 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87ffb1cd-b918-3167-b082-e04db38a3d23 | -12.66382 | -58.08227 | 2025-04-30 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b907499-8bf7-354a-870b-f39389eb60cd | -12.67648 | -58.09271 | 2025-04-30 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e723606-7f4a-35b9-8abe-5691f85eba14 | -11.58624 | -61.21248 | 2025-04-30 04:57:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3fd0363-3a08-30f7-a87b-1baa11240ffa | -15.07809 | -48.94453 | 2025-04-30 04:57:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b21138f-4c2e-3be4-bcaa-d2474cb8d33e | -12.67779 | -58.08475 | 2025-04-30 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README4.md)
