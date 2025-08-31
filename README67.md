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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a9d0b64-6cab-398f-8796-ac4ee53ffa1b | -10.95319 | -50.86047 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 6727d5fb-064a-3db7-9531-714cc9017d84 | -12.39382 | -46.48026 | 2025-08-31 04:51:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f492df8b-91a1-343f-843a-9279a075d24c | -11.21646 | -45.02162 | 2025-08-31 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ba799f1-85d8-3c49-92e5-638e90186f0c | -8.73514 | -62.39319 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4fd2c3e-7ab7-3faa-933c-0cad406f3803 | -13.16588 | -50.58847 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d7bdee8-7065-38bc-9584-00308a117c4d | -12.86167 | -48.08912 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50312f82-3baf-342e-b7a6-ac8cd5e0c140 | -8.33119 | -47.41855 | 2025-08-31 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 515ac687-b9c9-38f8-9e80-e5b93e4c4c1d | -13.02798 | -56.90197 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7f1356b-d8b8-3064-8bf4-ac04769c327c | -11.77761 | -47.39469 | 2025-08-31 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 485f7f62-a38a-3a02-856f-9395a0fe145d | -11.8316 | -46.42406 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 0bf0efd4-8dad-3412-849d-62f12159287a | -14.4093 | -53.44009 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4321e1fd-6984-3175-85aa-4c2f27b77ec3 | -13.02378 | -56.90536 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48ef5d8d-5c7a-3ff0-9a13-4dfb9f404d45 | -8.74863 | -62.38881 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be89613b-dfa8-380e-9310-910a012ac75f | -11.33272 | -43.63282 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 603d9551-63b3-3af1-8eef-c444f5258a7f | -13.0166 | -56.88336 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84ec1190-4c93-3a71-a187-929f10834eab | -9.48861 | -46.70243 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29be78c2-e48e-3658-a166-2e4d9b477f17 | -10.03713 | -46.0227 | 2025-08-31 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb746755-86fe-3102-83f7-78d34061f604 | -11.81451 | -46.43412 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 9c335bb6-f9bf-375f-8cbd-2c98f1c89224 | -13.3285 | -46.86216 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bf7daeef-f8ec-3a4e-9e11-b520cccf379e | -7.71342 | -50.30112 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff25839f-7ab9-324b-8d79-12b3dbb93eb5 | -13.34883 | -51.7554 | 2025-08-31 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ac0e424-8ba0-31f4-a518-af08f02fb54c | -9.45607 | -62.3557 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 21151e48-fa1f-3346-a8fc-9a32244d233b | -8.7423 | -62.3842 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 376cdaa1-8af7-3af4-98c6-7b9ce548d7b7 | -9.58987 | -46.00581 | 2025-08-31 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 513c1136-23e7-39e1-926e-c065405bc89d | -11.87865 | -46.71985 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 131e78fa-b0aa-3c15-b184-d82cabc07c33 | -11.82061 | -46.42471 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 35da8477-fcff-3dbe-9785-d12f5a6232b0 | -10.31081 | -59.20761 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1ea6ec7-2df1-3088-9b68-739af64de37b | -14.35895 | -51.90512 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72421649-fcb8-36a6-bf5f-50fcd9cfaa13 | -9.4468 | -62.34737 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 608c8f62-9a8d-32f0-8cdb-a935f15a93b3 | -9.08027 | -59.48491 | 2025-08-31 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2d0a981-33d0-353f-9aa0-13ca856f5b62 | -11.15842 | -55.04282 | 2025-08-31 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91205556-d28e-3cc9-8540-6cb2e6b43e67 | -13.34711 | -51.76722 | 2025-08-31 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4717badb-c962-3bb9-b7c2-b689303ad9f7 | -14.22591 | -48.07618 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fe29a322-10ce-3a1a-ab56-8cb914abf4cf | -12.63778 | -48.21542 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7779c364-3387-32d5-9ff5-29df8be07869 | -10.60995 | -54.92345 | 2025-08-31 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4212b3fc-976e-332c-81df-5ab48f3d43d0 | -14.34493 | -51.87824 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c247968-8535-3b86-ad12-284a7ee246d9 | -13.46389 | -46.97407 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92b78fcc-5245-3ba2-84b8-7fcb74b16b3b | -12.63408 | -56.99959 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2b9ccc4-045d-3994-8061-2fef09e51607 | -8.84169 | -64.15471 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a81b5489-997e-391c-b45d-389ff676c2f6 | -8.49727 | -44.74288 | 2025-08-31 04:51:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c88c942-00db-3306-bb86-fd7dcadf2977 | -11.83002 | -51.49601 | 2025-08-31 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64b9d37c-9802-3c0b-858f-97ebbe246e06 | -13.33784 | -51.77495 | 2025-08-31 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03c4d98c-ee57-3549-af38-368a2b3b42c8 | -9.47304 | -47.60798 | 2025-08-31 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fff20ed-d857-320f-9da5-8eb624a858e4 | -9.25513 | -47.05857 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bb5ea72-e187-30a1-8de8-6a959550a585 | -11.90699 | -46.40141 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d00bfb6a-c143-32eb-8aa4-8351fe4f45cf | -12.62557 | -57.00655 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1878fb0-8501-313c-bd59-5723b80917a7 | -13.34976 | -46.95496 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0a23e8e-0066-33f0-b2df-ed6ec1e59656 | -11.00347 | -46.94554 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cb785d7-e4ad-3067-8e3e-bc2f3c3ffb69 | -10.77812 | -48.82198 | 2025-08-31 04:51:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ebfa8468-1d1e-3b67-bb47-5f81619c597c | -12.09194 | -44.72727 | 2025-08-31 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e8291a73-4c5a-3968-8be2-14855e58df88 | -8.74511 | -62.3779 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78e4c36c-dd6a-302a-9570-5abf30b57a98 | -11.80882 | -46.45163 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 409c4396-2945-3d75-a215-e244c62e68e6 | -11.36263 | -43.59873 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0a99456-98dd-3b15-ab3c-5d67dcd158b4 | -14.35078 | -51.88739 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de975bb3-168e-345e-959e-d0e0e8fa346d | -11.82156 | -46.42714 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 236a40b3-833d-3f24-a2b9-8916b7a2bb0a | -11.05743 | -52.04915 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19a2e27d-f30d-3e88-a71d-85bb845b5a8e | -14.99735 | -46.70359 | 2025-08-31 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1ab7d1c-ef50-3a6c-b9bc-ce6e8c15e494 | -8.28912 | -46.31377 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c50c17d8-66a5-3447-bb09-3a14c712a78d | -7.95561 | -46.38488 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc52e6ca-6cea-35d9-abba-a61b59d7bee0 | -7.71052 | -50.27209 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2ca4bfb6-3160-3c89-bc07-7fd3365888a5 | -13.36317 | -54.38615 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b7e905d-cce9-3700-b1dc-74e5acc01465 | -8.11823 | -45.00691 | 2025-08-31 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bd04b63-1181-3146-87b7-188f5c28b751 | -9.45441 | -62.33533 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8a74066-ab33-3707-8408-0a322f908c56 | -13.35854 | -46.94293 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8579e6a4-4334-3585-8796-fdddcf06bba6 | -10.75787 | -59.8217 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b1da807-2c5c-39e2-b4be-01e1fb926b43 | -11.94655 | -46.69478 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7ba7a88-69d8-36d2-9b5a-adca3d6fda76 | -11.56439 | -47.61349 | 2025-08-31 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de7dff53-5bfa-32ce-bcae-d8eb2d5dd590 | -11.0119 | -46.95139 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08484290-a729-37d0-baf9-81a4185dc404 | -13.37113 | -46.95635 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f62c75b9-8cd9-3eba-a540-9c3b97a3eee0 | -14.53896 | -51.9835 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82227eaf-3dce-3903-a654-9d0062a108de | -8.30625 | -55.1096 | 2025-08-31 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eb2805dd-63ad-3329-a275-0f7c447febcd | -13.02297 | -56.88861 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54f2edb6-c067-3ac0-a6b6-14318aab9fba | -7.91032 | -63.01017 | 2025-08-31 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00fcf1d2-7c66-3544-b7d6-25c0a63682ae | -10.24072 | -54.97431 | 2025-08-31 04:51:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 279d991a-eb89-346a-a938-4dc272d7a2d8 | -10.9538 | -50.8564 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 35f0240d-56c1-3c10-8116-9142d091fb7d | -8.66341 | -62.83405 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3da0062-f637-3757-84a7-af60d84f0225 | -14.62074 | -48.06721 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59f85e01-56ca-3aef-b0b5-4650d4b26e49 | -12.62719 | -48.19794 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 29631dc1-6969-38d8-9506-4b2579e893c8 | -11.04409 | -50.83168 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f657607-a6c4-3831-9c20-3e8e13efd946 | -10.31429 | -59.21225 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c98cd5b-cf77-3dd6-a66e-3089258209f3 | -10.59689 | -44.32747 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9bbabb98-3f3c-3523-88c3-97b1a9bb8fd3 | -8.88207 | -62.39117 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a7fdc23c-1ff4-33e0-ba5b-871697724967 | -9.4474 | -62.34412 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9ad19b9-2cba-3fa3-a439-138c6035dcd8 | -8.74575 | -62.39509 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33714db9-11de-3587-8119-a96aeb2065db | -12.82351 | -48.08008 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c65c2f72-a7c2-321e-bb89-c8dcb8a23d45 | -13.3579 | -46.94807 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b6ddddc6-b90a-31ba-b0d7-9a0af76bdada | -9.45047 | -60.56282 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a1010da-2901-35d2-87bc-29a9a1a5c421 | -12.60704 | -57.0134 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0a23997-4a1f-3a59-a84a-1ede85e58677 | -14.22699 | -48.06783 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00830a97-d84e-3c2d-900f-dcc6d720e302 | -11.79926 | -51.43895 | 2025-08-31 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bedc0b7d-fd15-3de3-ba04-383e29b54bae | -9.69667 | -47.04081 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a05bcc3f-3515-34b5-bff5-fffec06253c0 | -9.4736 | -47.60404 | 2025-08-31 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc14c373-a7fe-39d1-a626-a00d58d997d6 | -9.67481 | -63.17175 | 2025-08-31 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9425a11-863d-3e95-97eb-c2a09551a034 | -11.36659 | -43.56639 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 627c72e2-461a-3d9f-9b5f-59bbcbb7a81d | -13.36647 | -46.95563 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3f84cad-4e45-3d59-9e25-a685261cbad8 | -11.8034 | -46.45641 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6f0373a8-052b-3596-a279-fc84a9f9b4b8 | -9.06896 | -65.45358 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3b5fd95c-002f-3e47-930d-f42b9f5f7448 | -11.35115 | -43.64545 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d1bc850b-8e37-3a71-b11b-947fa66ffb8d | -10.75359 | -59.82072 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a02e144-59bf-3f49-8577-374f10243b6d | -11.06295 | -44.63979 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README68.md)
