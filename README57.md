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
| a0ff9560-7d1d-34bb-a6e4-29743a82703c | -11.39981 | -50.99734 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7cac73bd-6b08-3bc4-bdbb-643ea79d27fe | -13.43196 | -43.8121 | 2026-09-30 04:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| cd1bee18-58d5-329e-b354-874bcf28a825 | -11.32798 | -50.98229 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd442c14-43fa-3b34-bd8f-85a662174453 | -11.84246 | -50.47649 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2663d96d-9012-35f5-b67c-f6c1b0e186c3 | -11.35605 | -50.97927 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9dbed2f-199e-3e48-a51d-de7476e509a7 | -11.86031 | -50.98246 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45278301-14a0-3675-bb82-667bd0c5924f | -13.43156 | -43.81535 | 2026-09-30 04:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 2e05fa9d-27a7-35aa-a8ba-ed6498ca3a9f | -11.79592 | -50.43951 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9a3fc40c-404e-3c4f-99c1-64d892d62bd0 | -11.30104 | -50.97804 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9ed06678-4f13-3b1a-a311-c01c83fd2dc8 | -11.81937 | -46.89441 | 2026-09-30 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8538567e-9c7f-3393-868f-f32a7cb6142d | -12.78193 | -54.00119 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0edb0481-3a7d-3945-bbdc-caaa80832185 | -12.77834 | -54.02304 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d03c91c7-49d4-3b4a-82bb-89891c0fac2b | -11.38525 | -50.96896 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a8b273b0-7584-313c-8c4d-592dcedf5651 | -11.33308 | -51.03886 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cc4d27a-cdb6-370f-8833-db914eb7e54f | -19.96791 | -47.90929 | 2026-09-30 04:55:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a81a890-8e4d-3ecb-9d62-f6de31d6456d | -10.0736 | -63.08384 | 2026-09-30 04:55:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 349d05bb-9e06-3a05-a7c2-3d422409cefd | -11.93811 | -44.80482 | 2026-09-30 04:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b884f655-3fdd-3f0f-ac47-0e79ee0d7455 | -11.84246 | -50.42988 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38e48f97-20a3-3ce7-99cb-3823d27d77d8 | -11.82127 | -50.43048 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cfbcbf2c-f652-3e52-861d-46e47c219abe | -12.78924 | -53.9987 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| deda76b8-ffe1-3257-a3f5-4c6e5f018bb3 | -13.37901 | -46.82944 | 2026-09-30 04:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7cf5be75-18c4-324f-9dbb-1e45bb0011f3 | -18.50283 | -45.14695 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 517d019f-04ac-35a7-9d1a-7412edc86012 | -11.40147 | -50.98643 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f89e741e-55f7-340c-85fe-16ce2e9cab39 | -18.48843 | -45.13613 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84eb93d5-16fd-31ac-b467-e2be20438583 | -11.82015 | -50.46138 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 101ba919-0c0f-30b8-870e-54268670e884 | -11.38694 | -51.01392 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ee04067-5c00-3636-881f-1de234b20591 | -19.3864 | -44.70486 | 2026-09-30 04:55:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bad0be50-06c5-3520-9901-d098e5d042b5 | -11.81271 | -50.4641 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c50509f-c5f9-36e4-94ef-e4b1a86d2b1b | -11.84227 | -50.96459 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1277071-a2ab-30f4-a0be-72e13aef8106 | -11.39422 | -51.01135 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3cacd9ce-217c-3f74-8b3d-0e74f10f1fb7 | -10.06769 | -63.08253 | 2026-09-30 04:55:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7b650e6a-dec4-32d1-bf55-59b3beaf7cf1 | -11.81442 | -50.45272 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a49d868-6d67-38b8-be81-37797c50aff3 | -11.34875 | -50.98184 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a306e7a-8db8-3ed1-b6b6-7c3af3acbd83 | -14.2213 | -44.53299 | 2026-09-30 04:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca7f768b-5938-3b32-a120-00075eab5145 | -11.38188 | -50.96843 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c354f084-4bde-3c05-971d-d813ef3bc1df | -12.79081 | -54.01018 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bedfb7a4-cb52-31d7-aeae-cd7de649302f | 1.79983 | -55.64781 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cee35c3f-38bb-3228-96c9-2fa55b5d361c | 2.51489 | -60.99625 | 2026-09-30 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5eeb2b6-f5b8-38a7-aab4-0b9da2ce992c | 4.35016 | -59.70419 | 2026-09-30 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 938ceae3-003d-385f-a410-128710400ec4 | 4.0768 | -59.93272 | 2026-09-30 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e9f3bc4a-2389-371d-a56c-0135f42980d4 | 1.80726 | -55.6378 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f92fd74-77c2-3247-82dd-17e4134468b0 | 4.34794 | -59.71212 | 2026-09-30 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0768b2db-fcea-38e9-91e1-24f1f4741504 | 1.80299 | -55.63599 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51d49d98-45b1-30d6-a946-429b6ecd799c | 2.54655 | -61.3072 | 2026-09-30 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57542f1e-5ec7-3b6f-a2e9-7174c688381d | 4.08865 | -59.94211 | 2026-09-30 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4dacde5d-57d3-3d2b-a16a-2678018a1437 | 1.68273 | -55.90345 | 2026-09-30 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58a0dfa0-4caf-3573-a2c4-13d0fe176157 | 1.81027 | -55.62843 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c73c1bf9-3284-3b00-a6d6-cd9dcda8cb22 | 1.8522 | -55.63545 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a01ef3e4-bb94-365c-bf4b-6ae09f7f1881 | 1.85963 | -55.6252 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| db7d394d-de84-388b-8639-190a5943503e | 1.86394 | -55.56653 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7c5f23e-31b3-3d96-89f2-1972ac1108b8 | 3.28258 | -60.61793 | 2026-09-30 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25535081-43a9-3d2b-a41a-104a4602bb81 | 1.79992 | -55.64534 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d33bb349-24b9-3592-809b-ddfcc413c2cc | 1.81469 | -55.62771 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83341642-3162-3c4a-8349-33a851f41ed4 | 1.6814 | -55.89506 | 2026-09-30 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fdd9973c-056a-3993-80cd-8b01846bad7d | -2.57912 | -50.786 | 2026-09-30 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c49fe4f4-bff6-366c-9e44-94f9b1d07dd4 | 1.70472 | -55.92981 | 2026-09-30 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbdf2d10-f93e-3e93-8c7d-ba20c4ad3e4b | 1.81911 | -55.627 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 002de284-8087-335a-9e0c-628b16932910 | 4.08921 | -59.94567 | 2026-09-30 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b68c0752-2de7-3fbd-b5c4-ff00c5e083af | 4.07737 | -59.93636 | 2026-09-30 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 660165ee-ee22-34cd-991a-e796c1d5f9a2 | -2.57833 | -50.79155 | 2026-09-30 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 53568657-040c-394a-a719-40d904795317 | 1.80434 | -55.64465 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57a7e960-c167-38d2-9e68-491296697716 | 1.68073 | -55.89088 | 2026-09-30 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a9602d4-d3c0-3719-bfa3-f5a336c3bce9 | 4.08019 | -59.93227 | 2026-09-30 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9eca61ed-cccc-3b30-8354-82d7f0f5eddf | 1.85882 | -55.56293 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4151456-8fa4-36ab-a7e1-dd9f496d1c40 | 1.80355 | -55.6428 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb79e38e-969e-3595-bbc2-5da626e36030 | 0.13674 | -60.40463 | 2026-09-30 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11f12da5-f165-3c40-b5d7-8ef7f9e082f3 | 2.54325 | -61.30771 | 2026-09-30 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a774fc7d-cea3-35d7-8d3d-648b688e1e8c | 1.67838 | -55.90414 | 2026-09-30 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d0ff021-94bf-373e-93b0-77063739de89 | 4.08414 | -59.93543 | 2026-09-30 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d1dc4ae-75af-3b6e-8c46-2c0c88bdf950 | -0.66853 | -49.25087 | 2026-09-30 05:33:00 | NOAA-21 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ea5dbbd-1a4c-3dfc-89fb-c7bbc1154d8e | 4.08471 | -59.93905 | 2026-09-30 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42b78058-cdc2-34c6-98cb-e43aa4fab38e | 1.32314 | -60.71188 | 2026-09-30 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4ef43cf-9421-3e79-a636-908cb8e02253 | 1.86031 | -55.62949 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0d722e01-08a2-3803-979c-0a3f75115be7 | -0.67548 | -49.25203 | 2026-09-30 05:33:00 | NOAA-21 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d325b8da-fa00-3282-ac3a-bf21bb5b9d9f | 1.80367 | -55.64032 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f898d0b8-8c0e-3c26-a764-63213241c1e2 | 1.86101 | -55.63388 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fca5d59a-254d-36fe-b73c-363c73a76eda | 1.81117 | -55.63026 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d57413cb-7191-3ebb-b2bd-f857b8c5133f | 1.9295 | -60.84313 | 2026-09-30 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 438ef216-2468-341e-9944-74ea0a68d400 | -1.66189 | -53.69485 | 2026-09-30 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c2f584d-4738-3fc6-bf8d-91da30efaf83 | 1.81098 | -55.63278 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 873cd0f6-c236-3d38-8f11-ab8a490c22e5 | 1.80284 | -55.63848 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b59922e-0bb4-35ee-9a1c-bc81cb6a74f3 | 4.34736 | -59.70845 | 2026-09-30 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68f28805-403a-376c-bd87-5c86041a8be1 | 4.08809 | -59.93856 | 2026-09-30 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 44263e4c-dfc4-391e-b79c-b1370de07f34 | 1.8569 | -55.60807 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 72539382-2f8c-3a7b-a8f8-bf54408f7e63 | 0.91194 | -59.62896 | 2026-09-30 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eca53ad3-6242-3791-b169-271d510281f3 | 1.85618 | -55.60356 | 2026-09-30 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f32e55c8-7f79-33d6-baa3-0cfe473f8b71 | 1.6834 | -55.90763 | 2026-09-30 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ce8cf17-6c99-37f6-9fec-aa49777c1f58 | -3.83515 | -52.26249 | 2026-09-30 05:36:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f508b1ec-f08f-33bb-a336-7e857e08ee9d | -3.10045 | -50.28048 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bd821817-7289-33bb-bf14-94df384a9bf7 | -3.01038 | -51.06687 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68c2b5af-8c0c-3b17-b637-f80f4cd88d8a | -8.11992 | -54.85247 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 111635b4-3085-395e-a52c-9988a711744f | -7.49939 | -55.0361 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bf5fe5b-a782-31c4-802f-840a94e138be | -5.72413 | -53.46201 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b444c39e-82f9-3ed6-9906-e8f0549c9d64 | -5.17362 | -55.99617 | 2026-09-30 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c52574ba-b083-3d27-beea-1e30954205f6 | -6.69841 | -59.96631 | 2026-09-30 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 460cb27e-8be3-3c77-9ae8-3e9392af4a29 | -3.25258 | -50.11781 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d84daf11-db89-3fb4-9885-d79d364b177e | -7.55181 | -55.03815 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0d821ca-b7ff-380a-95e3-152f3b0c1bd6 | -7.43121 | -55.18323 | 2026-09-30 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3020b7e3-8fcc-321c-97f7-e3564195b95b | -7.17677 | -55.40642 | 2026-09-30 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f7bddde-688a-3a48-99dc-8233fb004d16 | -6.23454 | -55.651 | 2026-09-30 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README58.md)
