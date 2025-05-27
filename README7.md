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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f75ad28-b3f8-30aa-99af-ec06fcfa4c22 | -17.53348 | -52.11902 | 2025-05-27 04:04:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ceff729e-94c9-3aed-b3ad-fad3584f2f6a | -16.58914 | -45.88008 | 2025-05-27 04:04:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69884f2b-c527-3ecd-8d54-fe40fa77ae07 | -18.8401 | -53.59331 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddaa56f1-5522-3788-b190-1347ed93bfab | -18.85047 | -53.59983 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e455c115-b44b-3a3a-a82a-4458c9c6b348 | -14.14973 | -45.47675 | 2025-05-27 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3774d72-3d37-343f-bfc8-d587bfe2523b | -14.14314 | -45.47094 | 2025-05-27 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 404175dc-ce03-3738-a4cf-50ff35ba8624 | -18.83731 | -53.60588 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 041b61a6-017d-31bf-a43f-38fbecb75fa1 | -18.84676 | -53.61662 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 27.6 |
| ebe3fbcd-e2c9-3ed5-82cc-e14d4d54accb | -18.85614 | -53.60094 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c96976e-6727-31a1-83d8-be2135457d42 | -18.85146 | -53.62212 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 23.2 |
| f60fdb32-08a5-3c72-a3d0-79dbabbb986a | -14.04075 | -55.13635 | 2025-05-27 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2a54c5ff-78b2-30b7-9d9e-7b74d4d0113b | -18.8529 | -53.60344 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b2a785f-8ef0-3126-bb27-e8db7026620e | -12.11701 | -54.66525 | 2025-05-27 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a80597a7-b899-3c14-9b8c-763f027f7100 | -18.84015 | -53.61975 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 3f326969-23c2-3480-8435-0f3ab01e87a0 | -18.84543 | -53.61081 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 25fdea65-233d-3c1e-96f5-bb723a4b26b1 | -17.37756 | -42.48506 | 2025-05-27 04:04:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51b9f1f8-3ac1-3baa-b310-530a4bd4021a | -17.53272 | -52.1226 | 2025-05-27 04:04:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82f20564-2446-3ec1-b2ff-f7a48e1334f8 | -14.24185 | -45.66431 | 2025-05-27 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc7a47ea-270e-3d91-8c5b-59ee9be74f32 | -19.05492 | -53.45911 | 2025-05-27 04:04:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1fb2ab56-811d-37c6-ada1-6c5b6dcc2e25 | -18.8571 | -53.62336 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 6eaf7272-95b5-3bf6-993c-2015979c8dca | -14.59148 | -48.35355 | 2025-05-27 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36c21c09-4502-3ba2-a688-f04e37a8ac20 | -12.64444 | -54.08499 | 2025-05-27 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ec9c26a-c2d0-32fa-aded-8cd5c3943ac7 | -19.97304 | -47.18746 | 2025-05-27 04:04:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 173a49de-dcf7-3098-8360-605aff059643 | -18.83594 | -53.59998 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d34ac1f-f5dc-37c6-8db8-6c3b309ffadf | -18.84109 | -53.6155 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 9f57759d-4c5a-3c0a-980f-01a63325781e | -14.01156 | -54.4822 | 2025-05-27 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9f21017-0038-3e70-a780-e775d1758d8e | -15.89098 | -43.46035 | 2025-05-27 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 25b27b9e-3abd-3492-ac51-7a5c8279a6ff | -13.78311 | -54.31815 | 2025-05-27 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5762efd-4ad7-3b7e-87d0-3603fa92c01f | -13.09879 | -52.29062 | 2025-05-27 04:04:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 217fec19-52fc-338c-845a-460504703115 | -18.85432 | -53.60918 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 60410716-d665-36f2-8c05-595b405a351a | -14.65958 | -45.08945 | 2025-05-27 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 321f280b-f6ea-3766-8c53-eea4f3351aa5 | -12.17039 | -54.26295 | 2025-05-27 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5bc372d6-46f3-35fb-90fa-65a94c59edc0 | -14.03752 | -55.13025 | 2025-05-27 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f7b2f331-7668-3913-87e7-f4522420de6b | -18.84632 | -53.60662 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 934a6e5b-ea3b-317c-8aac-eb8966d7e8fc | -15.08083 | -48.94713 | 2025-05-27 04:04:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a57b5786-40f6-3576-b35e-169cff90f39c | -14.02736 | -55.13318 | 2025-05-27 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a23fd8b3-5121-3fc1-8d3b-510d3c1ca262 | -17.0959 | -43.80448 | 2025-05-27 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27637462-3c02-34a0-894a-041c94d3e74a | -12.12379 | -54.66658 | 2025-05-27 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 874ff472-db36-3f21-8d1d-7f7f41e27cac | -18.8549 | -53.62175 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 3c5cfc55-e949-3dea-90b5-29705000ba72 | -18.83638 | -53.6101 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7843f349-9e6f-3e40-86a8-e52f70375ca2 | -21.18065 | -43.98164 | 2025-05-27 04:04:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ad1cc8a7-21e9-3a41-aa82-e73d05a3fae2 | -14.0152 | -55.12438 | 2025-05-27 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91fac6ef-c152-3112-b547-b85e82badb3d | -17.73954 | -43.06015 | 2025-05-27 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b607cd94-eafa-34e7-a97d-6de6570ee4bc | -17.53722 | -52.12738 | 2025-05-27 04:04:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33063856-b4a2-30f2-8535-458d7d1893de | -14.26024 | -45.69127 | 2025-05-27 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b84ada71-9c98-3e52-b961-2b12264d1e02 | -18.85201 | -53.60764 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bc58d4f9-acbc-39c9-b765-5ec86cd09254 | -18.8427 | -53.62358 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1449c5a-16f7-3469-acd9-ee0bc53e3c25 | -14.63315 | -47.94331 | 2025-05-27 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b98cbaf4-41c5-3c3c-8d22-a091088a0bf5 | -15.88429 | -43.45921 | 2025-05-27 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ae22f517-257f-382a-99c0-1dfb607629cd | -18.84204 | -53.61126 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 57e91624-da38-3b27-87df-cfb447291941 | -12.6551 | -52.43568 | 2025-05-27 04:04:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8076fdf9-14f5-3d9f-9ae6-789c6b592678 | -18.8477 | -53.61237 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c027b79f-52dd-321c-ac18-5b9e39c7c217 | -14.65168 | -45.09242 | 2025-05-27 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f138640f-dff3-3693-8ac1-f61c8ca23739 | -18.85214 | -53.6347 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0576c3a0-e7ea-359a-a93d-620d750d6a62 | -15.88764 | -43.45978 | 2025-05-27 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 704186a7-4e42-3a51-a7bd-270c111e5873 | -19.09091 | -43.97534 | 2025-05-27 04:04:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9d85e5c-ebd1-39a8-89a9-abb22fc15db2 | -15.88704 | -43.46346 | 2025-05-27 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 34f83369-a0d1-3912-b37d-8287e7f2a1d0 | -18.84452 | -53.61504 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 21.7 |
| aa197e56-4e8a-380d-a5bd-0d0b6162e048 | -19.05405 | -53.46318 | 2025-05-27 04:04:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 728ff123-bab5-304e-bb4d-8f2e48ece983 | -25.19025 | -49.32864 | 2025-05-27 04:06:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 60b63d45-970f-3409-ba73-be2a5bd5908d | -21.26761 | -48.61103 | 2025-05-27 04:06:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 4515936a-2d70-398f-8911-e8cc19915e8e | -21.22323 | -48.60712 | 2025-05-27 04:06:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f21363ed-40e3-30b9-a1ba-030b8231a061 | -22.90104 | -47.08301 | 2025-05-27 04:06:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 32a92608-cdb7-36c0-9095-f4e0a4aac0f8 | -22.67848 | -42.85478 | 2025-05-27 04:06:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 27125de6-da49-35bb-9767-e3ca4c602211 | -21.26265 | -48.61568 | 2025-05-27 04:06:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b079be30-4bb7-30af-add5-3ef95a029817 | -23.5999 | -49.00502 | 2025-05-27 04:06:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d8f58a7-96ad-319b-8dd9-ea50d511e16e | -23.42775 | -46.76117 | 2025-05-27 04:06:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9461c669-2586-3545-9507-3db06beba046 | -23.60222 | -54.76301 | 2025-05-27 04:06:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9d5e04e6-1531-3af7-9c43-4a5410ba0798 | -23.60772 | -54.76429 | 2025-05-27 04:06:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d7f812bf-132d-37ed-8e6f-bceb6c057a00 | -23.27351 | -47.05945 | 2025-05-27 04:06:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c74d2347-4f64-3159-9ed0-38f906ffe649 | -22.54196 | -48.81285 | 2025-05-27 04:06:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4073014-7638-3505-9e1a-da7144c3c15e | -19.79048 | -53.84445 | 2025-05-27 04:06:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f2a620f-e14f-3485-97b5-15a3888e1b3d | -23.33849 | -46.77071 | 2025-05-27 04:06:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 118d9394-296f-3a7d-9220-44f265285d8d | -23.63046 | -46.42598 | 2025-05-27 04:06:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 79ff066a-7106-379d-91ca-9bc7157f8ca2 | -22.51868 | -47.7222 | 2025-05-27 04:06:00 | NOAA-21 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c222e782-9636-3bbc-9deb-9135e0c2b007 | -22.52235 | -47.72305 | 2025-05-27 04:06:00 | NOAA-21 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b0430a0f-f1b9-3a5e-92dc-8814c4135a77 | -23.42849 | -46.75691 | 2025-05-27 04:06:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 579be610-0f79-3f78-b9a8-95522a97b445 | -23.41557 | -47.26275 | 2025-05-27 04:06:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a9f72266-4e85-3d55-817b-bd6ecdd8ffa0 | -25.19412 | -49.32938 | 2025-05-27 04:06:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f5a2e882-b903-35af-bb3c-046bfcd2345e | -22.42963 | -48.44152 | 2025-05-27 04:06:00 | NOAA-21 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d025bb41-438f-3b1f-9dfd-4772b1ef37eb | -21.51981 | -48.77468 | 2025-05-27 04:06:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8fb2d087-9428-383e-a7e6-52ff7efaae3f | -25.19333 | -49.32729 | 2025-05-27 04:06:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 49ccf988-e2c3-3a75-93ba-b00d9a40cf1d | -25.32712 | -51.48258 | 2025-05-27 04:06:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8f5adcd8-1268-3d3c-9656-541939da0a5d | -23.60391 | -49.00776 | 2025-05-27 04:06:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6d39a91-6335-368c-acde-c8504006d25f | -23.40579 | -46.55711 | 2025-05-27 04:06:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e6fdb351-828c-3fb4-b391-7f0bd706b086 | -21.2666 | -48.61647 | 2025-05-27 04:06:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 30503ed6-2985-3fda-a9d4-e2ba72f35bda | -18.8679 | -53.6218 | 2025-05-27 04:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 136.8 |
| d292ff47-92ee-3b01-8fee-2e7d2e0a803f | -7.2025 | -43.1171 | 2025-05-27 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.7 |
| 7a7d4a86-5d7b-34f3-b06f-15bac6a361f2 | -18.8684 | -53.6003 | 2025-05-27 04:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 107.6 |
| d8c0931b-2e01-319c-9171-10fd3406b162 | -18.8484 | -53.6035 | 2025-05-27 04:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 320.5 |
| e559b81c-e856-3f12-ac25-11c39a918d23 | -18.8479 | -53.6251 | 2025-05-27 04:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 248.7 |
| 5bb87392-2f97-35b6-97e3-92443d299d66 | -18.8284 | -53.6067 | 2025-05-27 04:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 65.4 |
| bf2baee2-321d-34c2-ae63-1896877941af | -18.8679 | -53.6218 | 2025-05-27 04:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 62.3 |
| a7f14246-876b-310a-bec5-b9d4fd439e74 | -18.8484 | -53.6035 | 2025-05-27 04:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 125.4 |
| f8291431-4a87-3cd4-96d9-be1d38244af5 | -18.8479 | -53.6251 | 2025-05-27 04:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 112.2 |
| d3516310-3e98-39e7-a768-8a62f402d435 | -3.42358 | -43.1657 | 2025-05-27 04:25:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f766524f-ddde-33af-a74a-ae0d1403af77 | -12.27203 | -44.59909 | 2025-05-27 04:27:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73343da6-4073-302c-9b78-c26760b699af | -7.19694 | -43.11594 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| fca01e80-b616-3e35-9005-0b4805ef9b98 | -6.86594 | -47.8351 | 2025-05-27 04:27:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce3a4e00-2866-3de1-957f-b53c6326ab3d | -7.35639 | -43.41417 | 2025-05-27 04:27:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README8.md)
