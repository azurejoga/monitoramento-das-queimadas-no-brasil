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
| 742138c3-d926-31cb-8bf5-5327c839d28f | -6.72009 | -44.32991 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0aaad154-1b17-3c22-9e41-5e4000eb57e8 | -3.38778 | -47.49217 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbf391a8-45b1-3422-a087-1fc784cb591b | -3.38416 | -47.48019 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 71c76547-a08f-398b-b708-16b2b8db7310 | -7.05606 | -43.51349 | 2025-07-17 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c93aee39-9817-3d76-96bd-4f3fa62a1a3a | -7.89392 | -44.49487 | 2025-07-17 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e8dd37f-5586-3c4d-b1a7-0e9c530e7e81 | -9.38236 | -40.61913 | 2025-07-17 03:53:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 866f1d4f-9dd5-371e-921e-15d15cdecf2d | -6.97473 | -42.8116 | 2025-07-17 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8f3fd5df-66a1-3124-9b2c-99bd97092d30 | -8.53463 | -47.85401 | 2025-07-17 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93d08346-1a90-335e-a8e1-fbf6c5190b93 | -3.39255 | -47.50139 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fb96c90-5b7e-3d48-9ac3-a1f53eef15a8 | -5.49749 | -43.67537 | 2025-07-17 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2454e70-1a25-3015-ac64-7ff44843824f | -6.72873 | -44.3294 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 28197127-6d3f-337c-9afc-58b15ceb2a23 | -5.98085 | -43.60449 | 2025-07-17 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d32efc0-fa7c-3c93-bdae-8a440fd8f9c0 | -4.45155 | -48.99675 | 2025-07-17 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21456780-e4ed-3a18-8241-029a65d1b1ba | -7.61543 | -37.82836 | 2025-07-17 03:53:00 | NOAA-20 | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d1c313a8-df81-3091-8ee1-bc5cd47cb166 | -6.85106 | -42.05337 | 2025-07-17 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f3a51db4-b8e0-339f-95e2-fc5ff48e069a | -5.06882 | -37.71548 | 2025-07-17 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7737be44-c178-37b9-9d8e-03c9bcdc0a6c | -4.10536 | -48.20609 | 2025-07-17 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 834e3307-f59c-3a9b-8648-3d20a6e1d3e4 | -4.30226 | -48.10496 | 2025-07-17 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 91f86473-8355-38c4-b0e6-9c2abbcef195 | -10.9661 | -46.48404 | 2025-07-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4c92d415-a1c8-3373-975a-e240e13c4f01 | -14.5195 | -47.67589 | 2025-07-17 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e36fc547-5ec3-3d70-8b22-49421a9ac0a2 | -12.9918 | -44.86014 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0b3016b-ce7b-3bed-a702-399cb2519362 | -10.96665 | -42.17797 | 2025-07-17 03:55:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f270c5cd-e618-3198-aa70-06d11309224f | -12.47833 | -46.91792 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1bfb0301-0a7c-3f11-aaa0-6d8e102c36c7 | -12.42143 | -50.04485 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2effdbf-357b-3caa-839d-44137ce22207 | -9.3101 | -44.84771 | 2025-07-17 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55db32c6-01eb-315a-96e8-427e0e040678 | -9.88785 | -47.81277 | 2025-07-17 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdbc176f-d69d-3253-add0-67823a0072bc | -12.41943 | -50.03743 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 73caa34d-9d7c-3cbf-bb22-94c7b65b420d | -11.35864 | -48.72761 | 2025-07-17 03:55:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46fbd396-7ff3-3605-abf9-b92f66dcc191 | -12.47222 | -46.92373 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa475aa4-3c36-30cd-8b98-c606702517e2 | -12.49653 | -46.9214 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48ccaabb-d5bc-3f02-9f8d-a58db245ad6b | -12.4116 | -50.04791 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d690356d-454e-33c7-b739-843c9bcc1c42 | -11.67039 | -43.76817 | 2025-07-17 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2726a818-61d6-3b9d-ab4e-b06a459da3ed | -13.00182 | -44.87271 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41854ba7-bd25-3cad-938f-c63ff1d6fa10 | -11.35803 | -48.73091 | 2025-07-17 03:55:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00323fbb-56f7-38c6-b14e-615dbe6e8425 | -13.00575 | -44.87352 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bde72ec-6487-34d8-8b4b-9e614382fe68 | -13.05578 | -47.80851 | 2025-07-17 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c9173ce-8c77-398d-97db-5d1282588c49 | -12.48743 | -46.91966 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa5db90d-1b50-37e7-9d9d-f4d7ca141682 | -11.94512 | -48.4274 | 2025-07-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d6d3a67-9976-3d0a-953a-eba9c442db8c | -11.49416 | -48.07636 | 2025-07-17 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88be0dcf-ecc2-3e41-8c9d-e2f278db47e0 | -10.10242 | -40.9185 | 2025-07-17 03:55:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 03f65d6d-7ac0-3221-b86e-4bafd0a97881 | -11.11125 | -48.86489 | 2025-07-17 03:55:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a06c399-bba8-339e-ad20-942d21e4ca80 | -10.96534 | -49.25163 | 2025-07-17 03:55:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ded89fb1-cdf5-38d6-a473-ac2265580340 | -12.48377 | -46.91404 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0cd2b522-137a-375d-bdc5-fb7fc87e408a | -10.9624 | -46.47855 | 2025-07-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a14575bb-d2a3-3848-adc4-e5d0b1644eb4 | -11.47372 | -47.32385 | 2025-07-17 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2524101c-3d82-3797-a859-3043ec134bf5 | -12.71192 | -46.80669 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 586acb18-4ad4-3ffb-815e-978d6be7f0f9 | -11.94118 | -48.4203 | 2025-07-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6975aba-7e76-3619-86df-3900911f9915 | -12.10186 | -48.19625 | 2025-07-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ddff5a5-04b1-3339-b651-6c2c591d8606 | -12.37779 | -50.38117 | 2025-07-17 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 267e7b31-e924-3619-8538-3487820bb7b1 | -11.10276 | -48.8809 | 2025-07-17 03:55:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08a03469-bea9-3b28-bf02-9d22fc2d68b0 | -9.80838 | -47.74105 | 2025-07-17 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58b7a93a-c7ea-3d8c-8f08-1c46dcb33312 | -12.42351 | -50.04642 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0137f9f1-f9f4-36bc-912f-05b79d9937bc | -12.37698 | -50.38522 | 2025-07-17 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8973365c-2d7d-3741-b65e-a70b5eff5ef8 | -14.2036 | -45.34428 | 2025-07-17 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa721baf-0919-3b6e-a5cf-cb10054a4ce8 | -12.47922 | -46.91318 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fc4ba682-ccdc-3b98-ab06-7b91f513ec4a | -10.66065 | -49.47792 | 2025-07-17 03:55:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69ea222e-8088-3d85-8a5f-2a40fbfa9cb7 | -12.41069 | -50.48607 | 2025-07-17 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2d39ef6f-f6ca-35c5-ac94-686870662752 | -15.88023 | -44.823 | 2025-07-17 03:55:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f5a0e67-5476-3957-83e3-271161a81f1b | -12.3786 | -50.37712 | 2025-07-17 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7c58dfdf-c235-3b52-9273-1f296b077030 | -11.94175 | -48.41728 | 2025-07-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13f57c78-0e0d-3aa5-9279-8d49c8ace9ec | -11.50387 | -48.96127 | 2025-07-17 03:55:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65a289e0-aeab-33db-a396-6014ad3e8e6b | -14.31995 | -48.6473 | 2025-07-17 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0aa90b58-b807-32dc-99f9-a4a0a883225a | -11.10808 | -48.8819 | 2025-07-17 03:55:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93576477-10de-358b-8964-e93237f6e282 | -9.88286 | -47.81145 | 2025-07-17 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92399ccc-8fbd-326b-b2af-015e5e2c81a8 | -11.23639 | -49.49787 | 2025-07-17 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b9f8d7e-982c-397c-874d-e954a503b7f4 | -12.42221 | -50.04096 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6bffbf1e-6616-3ee2-ac48-1103c9ab5371 | -10.6551 | -49.47677 | 2025-07-17 03:55:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8db6160-dcf8-3440-84dd-a626319ba96c | -11.94569 | -48.42437 | 2025-07-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb7243ee-de6b-3625-ab23-fad57b461e06 | -11.23566 | -49.50158 | 2025-07-17 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6dd6df90-5758-3355-a02d-4281852fd106 | -11.52698 | -48.95528 | 2025-07-17 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9407e048-6e44-342a-871b-515c7f1f60d5 | -12.49741 | -46.91666 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d664e3db-4150-3cb1-bc61-055d472ff4ec | -12.41585 | -50.04369 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d52e1302-a3f9-3ffd-8de1-fb2783cabd3e | -9.24111 | -48.56209 | 2025-07-17 03:55:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ae8f73a9-0fea-31d1-9f31-1f9a84046f85 | -12.70829 | -46.8012 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bad7b6e3-1eff-3258-b8aa-3d6d77d6c96f | -8.88621 | -50.15308 | 2025-07-17 03:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6c1c134-b0bd-37a7-85e0-fa5caaeef449 | -11.45897 | -48.15785 | 2025-07-17 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 041219a8-91f9-3fb2-86be-9f421b9e8541 | -13.24133 | -43.66837 | 2025-07-17 03:55:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73157545-40e0-3175-a765-49ce06e48910 | -9.4091 | -48.41987 | 2025-07-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcf18352-87ca-3e24-9965-f75b959c5929 | -8.91417 | -47.35469 | 2025-07-17 03:55:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92267c89-32e2-3fde-943d-59d609627510 | -9.60191 | -43.85253 | 2025-07-17 03:55:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d994e8a0-db08-325f-8682-6bae7b42f521 | -14.20758 | -45.34505 | 2025-07-17 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3d6b1c0-3093-3cbf-a865-202def9e60e7 | -14.46767 | -46.97133 | 2025-07-17 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15c71c03-a320-32fc-8dff-033d85b0b972 | -8.88536 | -50.15759 | 2025-07-17 03:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a07d615a-d630-3600-820a-5866d45b03c2 | -11.56958 | -47.09166 | 2025-07-17 03:55:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6edb788d-c0ec-30bd-a4e9-bfe388bf8e57 | -14.02151 | -51.22495 | 2025-07-17 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2d4b5a04-ee11-3adb-8eab-754208720d80 | -8.91389 | -47.35653 | 2025-07-17 03:55:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c48d9e9e-06c4-36cd-b0ac-ff993ef139f5 | -13.01813 | -45.06096 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1d93788-913b-3ce6-aef2-213ff8938dff | -11.49432 | -48.07862 | 2025-07-17 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdc95833-b97d-3f9d-bfe5-5f6624dbf118 | -10.56492 | -49.1427 | 2025-07-17 03:55:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bb29da6-39d6-3cf4-bdcb-724771825283 | -11.56491 | -47.09075 | 2025-07-17 03:55:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af20bd30-6893-38d1-be7f-6d2de8cab499 | -12.99575 | -44.86087 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 050d31d1-6af6-363b-a9fc-ee49dd67b5f9 | -9.41501 | -48.41764 | 2025-07-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3393283-9cf7-3e7f-986d-429133d2ef40 | -13.01983 | -45.06063 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c279756-bfd0-3b69-a439-6920087f81ee | -12.41179 | -45.37466 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 575f765e-7902-34c3-a12c-cc88fe7ef7ea | -8.70887 | -50.05033 | 2025-07-17 03:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3edd205-a5e7-353a-8627-c2812a99121c | -11.49487 | -48.07564 | 2025-07-17 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 602c38c2-32b2-3442-ab56-7e134041aa18 | -12.40988 | -50.4902 | 2025-07-17 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 40526ec2-b489-3b6d-9bb3-504fa923c670 | -12.42501 | -50.03864 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4bc34858-be76-3575-9bee-b84fcb391473 | -13.61327 | -42.5143 | 2025-07-17 03:55:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5498a194-4548-300e-8488-70902dbbd8ad | -13.01584 | -45.05988 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README16.md)
