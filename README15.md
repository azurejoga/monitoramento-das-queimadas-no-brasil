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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c596c929-c407-3db7-a0e1-4112589f229a | -10.79599 | -50.4242 | 2026-07-21 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd635666-2b7d-3261-9548-d5d2269cdcad | -12.0133 | -50.55316 | 2026-07-21 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d39349a7-c7e6-3f55-9e75-1e46a959bd90 | -8.75148 | -49.08364 | 2026-07-21 05:23:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d8d22a06-1c45-3d71-a451-81b2400d90fa | -10.51547 | -50.29092 | 2026-07-21 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c440850c-fc79-37d0-8d3a-9f54d0ff6aea | -12.65878 | -48.20327 | 2026-07-21 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c3a5289-d17b-318f-9dd8-f455ad38beb9 | -10.51044 | -50.28812 | 2026-07-21 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4a8a542-7aac-3047-ad4b-10a8bfd2ff17 | -7.6825 | -55.36467 | 2026-07-21 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95697a5f-f45e-3f53-8efc-796f90af456c | -9.10071 | -59.40436 | 2026-07-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e658a79a-017c-3bd2-bd48-6b2b48353a65 | -8.75254 | -49.08024 | 2026-07-21 05:23:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e28af2e-7ca2-3a40-8ab1-c2f8b4e5d62a | -10.52793 | -50.28133 | 2026-07-21 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1849006a-6e7b-37aa-8342-ed6dca768540 | -9.10181 | -59.3974 | 2026-07-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13329dd2-7728-32a6-9363-e0aac2644143 | -12.65941 | -48.20028 | 2026-07-21 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8555ead1-bf81-3a9d-ab00-2a61ebf629d1 | -12.45737 | -46.51798 | 2026-07-21 05:23:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04ed9cff-2623-3405-a42b-6aa031e5e5e2 | -17.58262 | -47.4998 | 2026-07-21 05:23:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b0899365-21a1-3440-bf45-bf2fc411be87 | -9.1844 | -58.0627 | 2026-07-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35fd7f00-e6c7-393f-9d47-3b9d482eafec | -8.75732 | -49.08453 | 2026-07-21 05:23:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 23aa99cc-9094-3ac3-86f6-3b143cb6381f | -9.0974 | -59.40384 | 2026-07-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b28b5f74-018e-3796-b01a-668c5e5ddaec | -10.50993 | -50.29022 | 2026-07-21 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5d9e8e0-65e2-3f08-b3c1-07d7330fc683 | -12.13881 | -48.2594 | 2026-07-21 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d79a99c3-3335-3b3a-8727-3b1b804c67e8 | -10.81808 | -50.42654 | 2026-07-21 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a75b568-22d1-37ce-bcfe-a2413fc81ec5 | -10.0619 | -60.49946 | 2026-07-21 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b5c3d9f-ef61-3820-b6ed-df25b4881c15 | -9.09635 | -71.26684 | 2026-07-21 05:23:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 925cf7c6-f250-380b-9663-2f418c61aa3c | -16.80561 | -54.59139 | 2026-07-21 05:23:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ec79525-8fb3-3b75-8c1d-451aec27a6d2 | -12.13734 | -48.26344 | 2026-07-21 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aacdc6c8-7853-303c-a0de-32a19f9b7dc8 | -8.94255 | -47.60551 | 2026-07-21 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a83b03d7-779e-3b69-b8c9-3372f1282ad2 | -17.582 | -47.50717 | 2026-07-21 05:23:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b47eea2-a828-3ddc-862d-ed4907872244 | -6.53844 | -55.15334 | 2026-07-21 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c516674e-5069-3389-8586-95d737f1e196 | -9.08596 | -50.58605 | 2026-07-21 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18c0e0ea-d691-3218-a7b6-6583ff2fdeaf | -10.82355 | -50.42778 | 2026-07-21 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3f034c25-1166-3989-93cb-8a911fc5e102 | -9.12083 | -59.0603 | 2026-07-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b856cad7-19dc-3f58-b87f-65c52a92deca | -6.18989 | -55.38805 | 2026-07-21 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e377e479-425b-3fb5-bf8b-7e9cc2ab8443 | -12.13821 | -48.26476 | 2026-07-21 05:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c1e57d8-e959-33c5-a6b9-1bb14cd4d1ba | -10.55162 | -56.33678 | 2026-07-21 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 675c2560-79e5-3221-8f9b-d96dfa65a372 | -10.5155 | -50.29248 | 2026-07-21 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 034098da-3d7c-3733-97c9-ebc50d9a7b44 | -10.55369 | -56.33421 | 2026-07-21 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8baf4223-8d5a-3b67-9ddb-0172813a5e8b | -7.62726 | -49.75425 | 2026-07-21 05:23:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c90900d6-ad67-331b-9220-0bec69822077 | -8.94163 | -47.60274 | 2026-07-21 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c625793-52c4-3e1c-9186-e012311dcca4 | -20.87132 | -57.488 | 2026-07-21 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fc140307-59b7-363e-a130-0e6ee78a32ef | -11.62998 | -58.28239 | 2026-07-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d2671e1-ff22-3483-b1ec-621d66c24e47 | -18.55202 | -56.81274 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 61607292-1468-3413-961e-d7893985328e | -18.54753 | -56.81581 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 613c7b03-dd35-30ae-a4d2-055938fb01f7 | -13.36891 | -54.31365 | 2026-07-21 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5155c544-3ec8-3ea1-9330-73cee6a8ef92 | -18.5541 | -56.82785 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| a5cf5e13-9d5f-303e-8b1c-70f2de727b48 | -20.8746 | -57.49398 | 2026-07-21 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b5e48faf-49c8-3da1-85fd-0f36be5cccd2 | -18.55459 | -56.82422 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| db6a3bae-e165-3303-a581-06646c84dcab | -20.69955 | -50.52972 | 2026-07-21 05:25:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d1bbc1f2-f4c9-3dbd-8c6d-179f33c91f16 | -18.54658 | -56.82307 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 7e827a3b-9da8-3512-897d-d6f3000eb97c | -18.55507 | -56.82059 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.3 |
| e9935400-09b0-3de4-8d27-9fb97889b234 | -12.98705 | -62.15284 | 2026-07-21 05:25:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6642d6f0-8a4b-3453-8a9f-b3fedc962753 | -18.55058 | -56.82365 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| df71bd56-56f4-3c20-9c4e-777b5715d207 | -11.5991 | -58.50839 | 2026-07-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8dd83a39-b524-38af-95e8-854cd9a6bfe2 | -18.55106 | -56.82001 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 7d3f02aa-c88b-31d6-a66f-d1c75e249a2b | -20.89184 | -57.48548 | 2026-07-21 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5eb6588c-41c2-389d-8db2-24ff8363ea70 | -18.54305 | -56.81886 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 4116b940-d772-309f-88cd-3224516c30a9 | -19.60983 | -47.64719 | 2026-07-21 05:25:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eafbd21b-ccaf-3f78-8e11-c829fa885ff9 | -12.16599 | -59.76075 | 2026-07-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c89351df-7318-35c8-9f16-4d7a1b8be477 | -12.88462 | -58.28778 | 2026-07-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a793049d-d7ab-36cc-a492-882c30fab0fb | -12.99103 | -62.14973 | 2026-07-21 05:25:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeac0a3e-d62f-35a1-97fc-c6219577a8a4 | -18.55154 | -56.81638 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 49cb8f0d-78e8-3abd-a9db-fec5125bc3f9 | -11.63056 | -58.27859 | 2026-07-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc7ceb4f-cfa4-3bda-aff3-711bd0d3b262 | -18.55652 | -56.80967 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 5182cc2c-4333-3a6f-9fea-bcfcc12a8aca | -20.87324 | -57.50478 | 2026-07-21 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 9ead4738-ff3e-360b-8ea4-816747b729ca | -20.87528 | -57.48856 | 2026-07-21 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c54f8ccd-98a8-32cc-929f-2676b1914d04 | -20.88787 | -57.4849 | 2026-07-21 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| dcc190d8-a044-36d5-9220-82e71f88c303 | -19.60752 | -47.64258 | 2026-07-21 05:25:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b773b154-d20f-35de-8128-49e333ad48c4 | -20.47921 | -54.98139 | 2026-07-21 05:25:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 065186e3-129f-3629-8ad4-dc3433044db6 | -19.61039 | -47.63952 | 2026-07-21 05:25:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 53c079ec-15ec-3aa3-b258-816021ca4b3f | -18.54802 | -56.81218 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4e5abe61-ac69-39f2-a1ac-f928c780441c | -18.54353 | -56.81522 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| a3c9c0ff-7d81-3fda-a690-f0fdd6155a15 | -20.89115 | -57.49091 | 2026-07-21 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2040d744-61b7-37ff-aaac-b896d0613c42 | -19.60692 | -47.65012 | 2026-07-21 05:25:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 90663683-e927-3223-ab52-5be262c41e8c | -18.55555 | -56.81695 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 7c44add5-a974-3f99-98ca-e0ca82d5f298 | -11.59853 | -58.51213 | 2026-07-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6444d6ed-af0b-38bb-8e47-44ec279873dd | -18.54706 | -56.81944 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| c060ccb6-1d46-3c2d-88e5-718c9f97ff8c | -11.5957 | -58.50785 | 2026-07-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8f682e5-c387-3499-b376-f05415dfdc77 | -18.55603 | -56.81332 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 0d380e0f-dcfc-3c21-af37-18e37b3d316f | -18.5501 | -56.82727 | 2026-07-21 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 5583e374-46f3-377b-a735-b9ccf5744388 | -13.3221 | -45.1246 | 2026-07-21 05:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| e0b5f3a1-953a-38fe-a557-00200cb279e8 | -18.5671 | -56.8317 | 2026-07-21 05:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 52ee1b62-d01b-3e3d-a0b4-522d95da629b | -18.5675 | -56.8109 | 2026-07-21 05:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 3dcbd5a8-17d2-3891-aa63-9441e9e77dfb | -13.3032 | -45.1045 | 2026-07-21 05:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| aa653365-7665-3cf2-af2e-41ab7476e6e5 | -13.3028 | -45.1278 | 2026-07-21 05:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| a9bfc44d-ec39-3a52-80ad-0e07ac0c75aa | -7.6375 | -49.7507 | 2026-07-21 05:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 3cf2519b-ba81-3acf-bfaa-a0082aec8dd2 | -18.5472 | -56.8343 | 2026-07-21 05:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.6 |
| b07ec16a-7084-3984-815b-906504248845 | -18.5476 | -56.8135 | 2026-07-21 05:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.0 |
| eff9e10b-fc8a-30f1-b8f0-b669be995bf2 | -7.6375 | -49.7507 | 2026-07-21 05:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| d656c950-ebb6-3320-810a-1a4639928717 | -18.5472 | -56.8343 | 2026-07-21 05:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 1b5ab7db-01ca-30fc-8d55-33f989f1e75c | -13.3221 | -45.1246 | 2026-07-21 05:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| c16224b3-3992-399b-9eb6-c382a00d3ac0 | -18.5675 | -56.8109 | 2026-07-21 05:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.3 |
| c236bcb2-9b66-3c2d-97b4-60204a495992 | -13.3028 | -45.1278 | 2026-07-21 05:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 8cee19da-f294-37cb-a685-57f96afbf67a | -18.5476 | -56.8135 | 2026-07-21 05:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 80385249-5f83-3e96-adcf-171dc393f0d2 | -13.3032 | -45.1045 | 2026-07-21 05:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| cd357531-c6c8-341e-a581-d66e39d4b140 | -18.5675 | -56.8109 | 2026-07-21 05:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.4 |
| 7a01cd07-e3d0-3544-90ee-098a2e26508a | -13.3221 | -45.1246 | 2026-07-21 05:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| a20f674c-40d8-302e-9f53-a383eac52e8b | -18.5472 | -56.8343 | 2026-07-21 05:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 35612ea5-d2c4-3eb2-9b98-c4a794fbd6d3 | -13.3028 | -45.1278 | 2026-07-21 05:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| f1f422e0-d2a7-3e04-9548-25c5e05fb162 | -18.5476 | -56.8135 | 2026-07-21 05:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| f48842d4-127e-31c8-b6fb-8519b1f7b2b9 | -13.3032 | -45.1045 | 2026-07-21 05:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 46f113f8-9704-3cc7-b980-90389ea99cb5 | -18.5472 | -56.8343 | 2026-07-21 06:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 00a80b0f-b7b9-331b-a58c-bab6dfd47424 | -13.3032 | -45.1045 | 2026-07-21 06:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |


[Clique aqui para ver as próximas entradas](README16.md)
