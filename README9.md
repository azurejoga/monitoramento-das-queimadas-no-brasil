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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82f1aae2-156c-310d-b1c7-030e37497348 | -8.6948 | -47.876598 | 2025-09-07 00:45:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07ba2391-55ff-3398-9d2e-2428a2c0a2ea | -10.7275 | -44.357899 | 2025-09-07 00:45:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0cca36c9-e1ce-3a51-bcae-9d5e84122478 | -6.7191 | -50.469799 | 2025-09-07 00:45:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd790660-fcf9-3641-84c6-2f6665e12dfc | -6.5915 | -43.993999 | 2025-09-07 00:45:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0df2689-6238-3c84-8413-05673b7c8ba7 | -6.1614 | -43.195 | 2025-09-07 00:45:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| dafed08e-b5df-3d26-b2d8-a8443b060cb2 | -7.7424 | -50.761299 | 2025-09-07 00:45:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f828766e-a104-3ab3-a8a8-47be3c0eeb2f | -12.812 | -48.021198 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fac98f4f-4459-3744-8e1a-05a18e2f0937 | -19.8722 | -45.036098 | 2025-09-07 00:45:00 | METOP-C | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9fa81dc7-8ff6-31bf-8231-c8808ab8f0c0 | -16.313 | -52.948101 | 2025-09-07 00:45:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 363c45cd-5f58-35ba-be9d-9534d826f669 | -13.8238 | -46.2626 | 2025-09-07 00:45:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d8497480-8015-39a8-b99b-a508492de824 | -7.719 | -50.3363 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 545db563-ceac-3d0b-9442-872e87af9d36 | -11.8439 | -50.524502 | 2025-09-07 00:45:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce064c81-e664-383d-a126-c46bd1deef0c | -20.540701 | -46.4604 | 2025-09-07 00:45:00 | METOP-C | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 53544856-8ce2-368a-aedb-014c42786698 | -11.7997 | -48.239399 | 2025-09-07 00:45:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3edd33db-06f3-3b71-9a57-cf179431383b | -7.0446 | -50.862499 | 2025-09-07 00:45:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31dab9d8-5bb9-3a25-9287-884504bb31a4 | -6.806 | -50.854698 | 2025-09-07 00:45:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0665b8cd-722d-3b5c-8b3d-e4fd33750083 | -9.7343 | -51.070499 | 2025-09-07 00:45:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dad88e2-de67-31b8-ab13-786e6c10b45b | -5.6773 | -45.436298 | 2025-09-07 00:45:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8009ca4-d964-3b54-aafe-d05f9f6defdf | -17.6605 | -43.542099 | 2025-09-07 00:45:00 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c61401aa-2504-39d4-b1e1-0b0249265936 | -9.2316 | -57.062302 | 2025-09-07 00:45:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df835392-0c6b-3dbd-a0f7-ee1b440e2ff8 | -11.5683 | -47.765598 | 2025-09-07 00:45:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6917bda-30be-37f2-8c25-57a5179fc3b8 | -5.9946 | -44.170502 | 2025-09-07 00:45:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c36bce8-d7f3-3323-9fe9-4c16324d0a0b | -11.2092 | -55.023201 | 2025-09-07 00:45:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d64aa5ec-9a47-35f1-a2b4-4594022ceaf6 | -6.7962 | -50.856899 | 2025-09-07 00:45:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6efa8ea8-6e72-337f-9e5c-9141a47c4ebb | -10.3704 | -44.980301 | 2025-09-07 00:45:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67651ca7-ad28-3a6f-a06d-da4f76289d02 | -6.1939 | -43.584999 | 2025-09-07 00:45:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6fa14de5-b3b4-345b-89c0-1b08218852e7 | -7.7092 | -50.338501 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b70768f0-e233-3a02-830d-6a21e2478e34 | -18.0236 | -47.094002 | 2025-09-07 00:45:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8b198aca-e1f9-35e1-aed1-78d393598a80 | -14.5738 | -52.1483 | 2025-09-07 00:45:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c777cfd-94bf-3473-b782-ec89dd2d7c35 | -13.0464 | -48.055401 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d97c6355-c481-3f09-94df-7ad7b19756f6 | -6.6012 | -48.0597 | 2025-09-07 00:45:00 | METOP-C | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 79c743d7-429a-33f7-8329-933237257a83 | -11.58 | -47.186298 | 2025-09-07 00:45:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2285cfff-6094-3a24-9802-17a8117dea3f | -6.8118 | -52.815498 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 995373ee-54c8-3c4c-a61f-456009bd1466 | -7.6322 | -46.768002 | 2025-09-07 00:45:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c411841-ff9f-3b24-b3bd-c4c4e624cdf5 | -2.4247 | -49.319901 | 2025-09-07 00:45:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3901045-6c62-3d86-984e-35e8856264c0 | -2.905 | -48.673801 | 2025-09-07 00:45:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2593e07c-979a-3455-9e5b-cc2bf5abe0c8 | -8.3475 | -52.564602 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4cdd97c-697e-34f9-b545-4de4a2e357f9 | -11.2531 | -46.487801 | 2025-09-07 00:45:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f9c47ff4-2a8c-3e83-9fc2-1802157d8b13 | -11.8351 | -47.578701 | 2025-09-07 00:45:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| afe87128-c1ea-3207-a329-7df530d206eb | -5.9576 | -53.594299 | 2025-09-07 00:45:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b86509d5-89bb-3d4a-9d8b-52a571858d7c | -6.5889 | -43.983002 | 2025-09-07 00:45:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65326c7f-e6c7-33e6-886b-2b1a479aad73 | -6.5941 | -44.004902 | 2025-09-07 00:45:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b4a29bb-8e6f-3a31-90db-57e4875304b0 | -6.5179 | -45.848701 | 2025-09-07 00:45:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61c7c375-a5e2-318e-be48-ae7a1b0a5a5c | -21.479 | -45.5746 | 2025-09-07 00:45:00 | METOP-C | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 39ae486e-6653-31df-931a-9ca15ad9dd1c | -10.8004 | -47.7449 | 2025-09-07 00:45:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d04265a-1521-3d26-a7d6-dd8f5ca435bd | -8.069 | -50.198799 | 2025-09-07 00:45:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22e51e87-9c6e-3e1c-9676-551b824ab8b5 | -11.6077 | -47.172298 | 2025-09-07 00:45:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb527d23-261a-3617-950a-347da16f378b | -11.0318 | -54.163799 | 2025-09-07 00:45:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33d96fd5-aacf-36b6-8df1-aa19469a3f5a | -13.0404 | -47.119801 | 2025-09-07 00:45:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 620fc394-0acd-3981-9f19-75f129f482f5 | -1.9285 | -56.5793 | 2025-09-07 00:45:00 | METOP-C | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17c211a6-2044-3d51-8835-3384a8bb1f06 | -16.282101 | -45.683899 | 2025-09-07 00:45:00 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 33c9a022-64c1-3b18-95f4-81883602aa39 | -11.8375 | -50.542301 | 2025-09-07 00:45:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ca17ceb-90a0-35a7-87fe-9534b1ac58dd | -10.3343 | -44.915901 | 2025-09-07 00:45:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 94bde671-b508-39dd-b731-45394a9505db | -9.8301 | -46.5411 | 2025-09-07 00:45:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5114732e-d064-346a-9ac9-730c87311fee | -7.1992 | -46.199001 | 2025-09-07 00:45:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1787ca60-0350-3500-9ca8-59427a8eafbd | -5.6227 | -51.360699 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c7a86c5-fd70-3ec0-a33a-85c123caf238 | -19.464899 | -47.765202 | 2025-09-07 00:45:00 | METOP-C | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0b2ef237-3f87-31c1-abb3-fedc02734e6b | -6.5791 | -43.985298 | 2025-09-07 00:45:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98136636-1ead-3848-a7b7-03f906199619 | -6.2854 | -51.423401 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93e7d1c8-bdf7-35b2-bc70-515156d70b0b | -16.3228 | -52.946098 | 2025-09-07 00:45:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74b269e3-6ceb-3c50-bf3e-2d6274a82a83 | -8.6843 | -54.692799 | 2025-09-07 00:45:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97b76543-ed65-3a2d-9511-cbb92a9db756 | -18.004299 | -44.910999 | 2025-09-07 00:45:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a41e615c-d136-39eb-8285-a06b9427aec3 | -11.797 | -50.592098 | 2025-09-07 00:45:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d314995-d703-3299-ab01-1cbad596b5c0 | -4.4682 | -48.1171 | 2025-09-07 00:45:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f41a819-f97c-35f4-ad0d-078e2ab2d77d | -13.7661 | -52.787498 | 2025-09-07 00:45:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 69adcaa1-acd6-3600-bfde-eac96113c254 | -13.0021 | -48.0877 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1513c7ec-f506-3a43-842d-e16f85137e9c | -11.7808 | -50.612099 | 2025-09-07 00:45:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e77af8f3-c5e6-3519-9eeb-914121fa4a1c | -12.0052 | -47.781898 | 2025-09-07 00:45:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8dabd0e-70c2-3b5d-b2ef-16089c0b7733 | -13.0202 | -48.076199 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc47f45a-82e5-3c07-b687-4b964820112d | -14.5714 | -48.1036 | 2025-09-07 00:45:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 032dfa41-823d-3265-ae63-7bff818bc100 | -21.695499 | -45.388599 | 2025-09-07 00:45:00 | METOP-C | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47b6022a-8331-340a-9b09-be528f16c489 | -8.3338 | -52.549198 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0784cc1-ac78-3184-abab-107644137ec3 | -5.3994 | -44.8302 | 2025-09-07 00:45:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7896093a-063c-33a1-8809-9613936a29d1 | -8.8702 | -52.046001 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c04d5c4-b289-360e-8e84-74515f6318e5 | -13.0006 | -48.0807 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0994766c-1e9f-3090-8c05-cb616cd6373f | -7.3261 | -48.518902 | 2025-09-07 00:45:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74d570b3-a73c-3028-b48b-2035dd50ab6c | -6.1946 | -53.273899 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df14b4f8-b0e5-3a1d-ba2e-3e6e3ce2b6e8 | -12.9365 | -54.772499 | 2025-09-07 00:45:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3de98cac-0796-36dc-8991-19102f06a1a0 | -5.7009 | -43.934799 | 2025-09-07 00:45:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a092f3a-9d61-31b7-99bf-35aceb0ddfde | -8.6058 | -54.659599 | 2025-09-07 00:45:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a97da78a-1772-3caf-a302-ede0e60fbb14 | -12.9292 | -48.0383 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90c36f97-dcc2-382b-a9b2-2853c01c9961 | -13.814 | -46.264999 | 2025-09-07 00:45:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db2b298f-c92e-34e9-851c-f1bff931b9de | -10.5993 | -44.3405 | 2025-09-07 00:45:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e285c07-6390-3292-b107-2e418278de74 | -11.1349 | -48.398998 | 2025-09-07 00:45:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16dcf75e-081f-3780-b2c2-5137bff6070d | -21.2005 | -44.3395 | 2025-09-07 00:45:00 | METOP-C | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aad25982-5c62-3214-9b86-615a977d431a | -6.6039 | -44.002602 | 2025-09-07 00:45:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33c9b03a-36c6-3597-960e-2554190d5c51 | -6.2623 | -53.4408 | 2025-09-07 00:45:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1d40f38-f4ea-388f-abb7-c9ea274edfa9 | -6.2069 | -46.7649 | 2025-09-07 00:45:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6ddab0c-4088-3db7-ab3a-2f15ccb45817 | -15.1011 | -48.078602 | 2025-09-07 00:45:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bc39b70d-9b4b-3a61-b15c-965f7c0532bd | -14.559 | -43.733101 | 2025-09-07 00:45:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 57d86f7d-ec22-3ac9-b84d-695533687b68 | -9.7021 | -49.492599 | 2025-09-07 00:45:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 056c708d-de75-3cc8-967b-6f4a887dae54 | -7.735 | -48.817402 | 2025-09-07 00:45:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9a0d7da2-926a-349a-bc2a-ce4f4a819da5 | -15.1093 | -48.069199 | 2025-09-07 00:45:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 52ad2771-9657-33b7-b8c1-524fcfab585d | -6.1965 | -43.382099 | 2025-09-07 00:45:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad27b459-2e85-3232-b9a4-e145da4e9afc | -21.4774 | -45.5672 | 2025-09-07 00:45:00 | METOP-C | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b18a79b-8dd8-31ec-8c2b-719b40e64ed9 | -10.5971 | -44.3312 | 2025-09-07 00:45:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0d243f43-c558-30dd-8aea-b53296c4a2a1 | -13.0217 | -48.083199 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6397b261-45a5-3143-8aca-43fdb5378d6d | -5.6697 | -45.447701 | 2025-09-07 00:45:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca72eb5c-1f13-37a4-b9f1-45ad3eb9eae3 | -11.9346 | -46.6656 | 2025-09-07 00:45:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2c7eae7-a952-3c9c-8add-d2b88a35c89d | -9.9721 | -51.640202 | 2025-09-07 00:45:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
