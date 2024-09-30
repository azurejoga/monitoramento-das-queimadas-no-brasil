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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63be83d3-6f08-3d5e-bf59-379015acf9a4 | -17.15854 | -56.25624 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 60f06afc-ff57-3c7e-8193-492487efa408 | -17.14967 | -56.23326 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| bf1d9146-b806-337e-b485-8eb1db65bda0 | -17.14622 | -56.22835 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8d93f806-24c4-3cb4-9b32-f396ea0d3ad8 | -17.14547 | -56.23239 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5aa6a56e-3e6b-3cd0-b59e-d69b349e2b52 | -17.14503 | -56.21124 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 706ddd5e-141e-3814-b10a-a246475dd4fc | -17.14428 | -56.21529 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| dfd5a41c-72e9-36a7-b68f-c807443fdb76 | -17.14158 | -56.20631 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9036bb91-df7e-3442-b8ea-7ee4a2ee47a4 | -17.14126 | -56.23153 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 174aefcf-b2b4-376d-ae51-6b8add7065c8 | -17.14083 | -56.21037 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 9d99078a-9d25-3478-a92c-0e2da8c33308 | -17.14007 | -56.21443 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e11124ff-f4d7-3cdf-a5a6-e532982a2e78 | -17.13932 | -56.21848 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ce262f3d-36fc-380b-a4c9-f9bee96a8339 | -17.1389 | -56.1973 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3b36f9f7-442f-3e93-95e5-4af167b6dfe0 | -17.13738 | -56.20544 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e6f3a108-c2a8-3a08-abb8-2da1bfe37a95 | -17.13663 | -56.2095 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 23071961-ab80-375e-b93c-301ad6fc7c67 | -17.13587 | -56.21356 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2e84567f-43b5-3696-8069-2dd313c9c85d | -17.13394 | -56.2005 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7c792005-34b5-3632-8063-9a481050381f | -17.13318 | -56.20457 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2ea82c18-0021-3a8d-95db-c836f25e2f0e | -17.13243 | -56.20863 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f9e17500-7f42-3f05-9cef-b58792ce6113 | -17.13167 | -56.21269 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b5e53666-ad23-3862-81a3-5b61e6263255 | -17.1305 | -56.19559 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3281f10a-9ada-346d-8ff7-09e66ca7f1bd | -17.12974 | -56.19965 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2db3b114-dcbc-3760-9c78-045614082950 | -17.12898 | -56.20371 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 07915736-9d1e-3a38-9cd2-408e7650186d | -17.12823 | -56.20776 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a3b47f0a-819e-31c9-855a-b1c02ad7a7b1 | -17.12789 | -56.23296 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f3d2b2d0-fc05-347e-a3c1-f11dd83bc037 | -17.12747 | -56.21181 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f44e7ceb-177f-3cd1-9b92-9a4c87bb2f2a | -17.12671 | -56.21586 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f9ad4de1-8e53-3597-881e-54feba6ac0b0 | -17.1263 | -56.19472 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| efa38367-ba9c-3d7b-a522-3fd2e8b4cd59 | -17.12596 | -56.21992 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 693aeb62-71d1-3723-b190-136c949815c4 | -17.12555 | -56.19878 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8485cd11-83bc-3a38-a06a-4d928c067541 | -17.1252 | -56.22398 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4edb8b5a-0755-35e7-9ad0-a5acaa4a29b5 | -17.12444 | -56.22803 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 56efcd77-812e-3a82-be72-6e47b2a239c3 | -17.12403 | -56.20689 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 12d72436-b828-31cb-8032-57384daf1243 | -17.12327 | -56.21093 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9641ff1e-b68a-3810-8224-d3b3e6f6ce3e | -23.49935 | -47.22727 | 2024-09-30 04:36:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d5e25e0e-159b-3d9c-960c-cb143ba8e2d5 | -23.49756 | -47.22485 | 2024-09-30 04:36:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f9fe5733-6df5-337b-9c5a-ffdb81266971 | -23.35314 | -46.98956 | 2024-09-30 04:36:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7f288bf6-c99c-3fec-9113-e666be201f5c | -23.34921 | -46.98933 | 2024-09-30 04:36:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9d20bb7a-01a6-377f-ae9c-541ffa61a0b3 | -23.33966 | -46.77579 | 2024-09-30 04:36:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 863d1a24-4bdf-372a-b03e-243ea503c2c0 | -23.33636 | -46.77419 | 2024-09-30 04:36:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 30aff1a6-54bb-3df7-8ca7-47f4813866df | -23.17603 | -49.58833 | 2024-09-30 04:36:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0360898e-2775-3ba9-9879-d7169289d1d3 | -23.17546 | -49.59233 | 2024-09-30 04:36:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7f739abe-9841-333c-ba66-a59efb9f49fe | -22.99818 | -49.60872 | 2024-09-30 04:36:00 | NOAA-20 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 25e70907-55b6-3ecb-873a-68dbb60dd42f | -22.99761 | -49.61271 | 2024-09-30 04:36:00 | NOAA-20 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dbef7aff-7770-35e8-8698-7cc112b7fb6b | -28.69333 | -50.4134 | 2024-09-30 04:36:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 92ab551e-f411-3397-85f1-5efe07a21239 | -28.6929 | -50.41116 | 2024-09-30 04:36:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bf376d39-6c16-3bf2-b085-0740130931ad | -28.69229 | -50.41562 | 2024-09-30 04:36:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f39f879d-e720-34e0-93a0-37dcad775c52 | -28.68983 | -50.4128 | 2024-09-30 04:36:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 11e00b73-2899-3005-ba0c-39aaa4534480 | -28.51037 | -50.66529 | 2024-09-30 04:36:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 89efda2b-ea31-3b3f-87af-a40a87f50d9b | -28.50978 | -50.66957 | 2024-09-30 04:36:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6ebd6272-e4eb-3beb-8b24-3c4681422d73 | -23.42879 | -51.45015 | 2024-09-30 04:36:00 | NOAA-20 | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e69905aa-fa7b-395e-a73c-37865be0a897 | -23.11165 | -50.41084 | 2024-09-30 04:36:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f094e815-9958-3cc3-bb10-3c44449b1e4c | -23.11108 | -50.41467 | 2024-09-30 04:36:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 26b68e56-0111-38aa-926c-df3e3758b973 | -23.10887 | -50.40638 | 2024-09-30 04:36:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 67c53b8d-f66f-3eef-a521-a52113e534eb | -23.1083 | -50.41023 | 2024-09-30 04:36:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4bf1079b-3c76-3f8e-a910-6b795e5d8f6d | -23.10773 | -50.41407 | 2024-09-30 04:36:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2ab4c77f-80ab-3ba6-8876-03c4908682e2 | -23.10716 | -50.41791 | 2024-09-30 04:36:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c98db0f5-bf5d-322b-8dba-92856504d205 | -24.24164 | -50.7391 | 2024-09-30 04:36:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| acca5ee7-e68e-37b7-92e6-286e9dbc4f1b | -26.74801 | -51.72892 | 2024-09-30 04:36:00 | NOAA-20 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 036bebde-1797-3e12-bc49-16defb000cfb | -25.43826 | -53.98229 | 2024-09-30 04:36:00 | NOAA-20 | SERRANÓPOLIS DO IGUAÇU | PARANÁ | Brasil | 4126355 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6cb7cdbc-dd87-37fc-812d-7b8c41844d44 | -23.60006 | -54.35033 | 2024-09-30 04:36:00 | NOAA-20 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2738831d-c1e9-3d21-bdc8-2e23d42649c3 | -30.14989 | -52.02521 | 2024-09-30 04:38:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| f0310660-9eb5-3a78-89ff-a83d58669c08 | -8.52061 | -44.71037 | 2024-09-30 05:04:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 4bf9c2c2-cb54-3726-9274-9a7194fa8c8d | -8.51912 | -44.71993 | 2024-09-30 05:04:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0dfb205e-f1c2-32ab-a87a-215d3b5b97d2 | -8.51298 | -44.70329 | 2024-09-30 05:04:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 9d227970-34e1-3358-94ed-1f65c5aa133d | -7.92014 | -42.76771 | 2024-09-30 05:04:00 | AQUA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| ad0d80d3-6821-3219-97d8-bd04eddf6358 | -7.91262 | -42.75753 | 2024-09-30 05:04:00 | AQUA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b3f3157d-8a20-384e-ac90-f82cbdc697a5 | -7.9113 | -42.76641 | 2024-09-30 05:04:00 | AQUA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| e4994609-6363-3fef-baa3-e61aa75b6da2 | -7.4789 | -43.85294 | 2024-09-30 05:04:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 054ed377-cb92-3da3-966b-abba59516dc3 | -7.28556 | -42.25245 | 2024-09-30 05:04:00 | AQUA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 208168d0-e961-33eb-8356-b87d4ca71e62 | -3.95678 | -41.4842 | 2024-09-30 05:04:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 954d3cbe-7d23-3084-afd9-39666d10aaa4 | -8.61798 | -46.55409 | 2024-09-30 05:04:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 32eaebd9-00c4-3468-95e7-9312a2096a09 | -8.41632 | -46.33518 | 2024-09-30 05:04:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e1a5e9eb-d7fb-341a-83d3-17093e6682b5 | -7.23953 | -44.9375 | 2024-09-30 05:04:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 105dc9b7-9bdd-349d-ab6e-4ba17b232f52 | -6.38529 | -44.77203 | 2024-09-30 05:04:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 6be4de64-3c0d-3d00-9102-be1f14db2d6e | -6.37963 | -44.77463 | 2024-09-30 05:04:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| def8aaa2-338e-3b7e-b45c-1f612deca2db | -4.27746 | -48.63532 | 2024-09-30 05:04:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| f2f879dd-0f9f-3b48-946e-3adf002a7260 | -4.27429 | -48.65557 | 2024-09-30 05:04:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| ce7829ff-5fab-3fd9-8db2-6f45479cfd24 | -3.58875 | -44.53515 | 2024-09-30 05:04:00 | AQUA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| a4ed2455-4817-33d5-9680-7fad6317daa4 | -3.58715 | -44.5456 | 2024-09-30 05:04:00 | AQUA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| d9a0db64-15ec-3495-9daf-3c3232eb2009 | -3.57917 | -44.53376 | 2024-09-30 05:04:00 | AQUA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 41b4b368-3481-32b6-9483-64b0756cb430 | -3.57757 | -44.54416 | 2024-09-30 05:04:00 | AQUA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 0c900f39-a03c-3bd7-b55a-274cb4a91aca | -3.10821 | -49.37432 | 2024-09-30 05:04:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| cff1d964-c476-3a13-83f0-569bbf376faa | -3.10439 | -49.39838 | 2024-09-30 05:04:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 8556d033-f4ea-312d-99b8-89bc2e7a0c41 | -3.10129 | -49.39033 | 2024-09-30 05:04:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| c804d100-2074-314a-a5f5-9c4a8b25c8c4 | -3.09762 | -49.41458 | 2024-09-30 05:04:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 9013d2d3-2c08-37ac-820d-705ab0168295 | -1.7278 | -47.12032 | 2024-09-30 05:04:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 58bcbfc8-db87-3d26-bbf5-5a9417c19d4b | -16.10799 | -50.36107 | 2024-09-30 05:06:00 | AQUA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3c1a0600-8f07-34ff-b818-adde8547a2d0 | -16.08323 | -50.38589 | 2024-09-30 05:06:00 | AQUA_M-M | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9ef73215-217e-3444-b621-78d24eeb6419 | -16.08148 | -50.37319 | 2024-09-30 05:06:00 | AQUA_M-M | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 121935e4-5b9d-3aa2-9259-44f493451a43 | -16.0783 | -50.39077 | 2024-09-30 05:06:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 6af68746-0a0f-3148-b25b-8e28ed145a8e | -16.07451 | -50.36594 | 2024-09-30 05:06:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 96dd9fdc-e7b0-3fde-b3c3-7278ddf27e76 | -16.07133 | -50.38433 | 2024-09-30 05:06:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 33.1 |
| e72eecfe-8f32-33e5-bf98-a5e985cc080c | -15.88351 | -45.05596 | 2024-09-30 05:06:00 | AQUA_M-M | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1d056337-b751-30c4-b0d0-cd49eaff6969 | -15.32462 | -47.49232 | 2024-09-30 05:06:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 91794ed6-3e13-32d0-833e-232af96e906e | -15.32279 | -47.50357 | 2024-09-30 05:06:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 235.9 |
| 7e44f057-230e-3c66-8dcd-186589034f91 | -15.321 | -47.51456 | 2024-09-30 05:06:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c97e60f8-4075-3239-8245-ddb82054666d | -15.28547 | -47.48695 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4ce6736b-6e35-3f52-bfbf-529737518909 | -15.28368 | -47.49781 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a71703ac-cf1c-3911-b769-3189685fbc2b | -15.28153 | -47.49224 | 2024-09-30 05:06:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b19ded28-a688-3873-aff6-e86ce01e14b3 | -14.75936 | -48.73682 | 2024-09-30 05:06:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |


[Clique aqui para ver as próximas entradas](README58.md)
