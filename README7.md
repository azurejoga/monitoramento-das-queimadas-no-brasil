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
| b2c0a103-95fa-30e2-abdd-4cda5f0a1762 | -15.4044 | -47.84871 | 2025-06-16 04:27:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dac77360-5754-397a-bf31-caf17dc32b73 | -11.14188 | -53.92945 | 2025-06-16 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0e373efd-18b8-3668-b56c-e8128c109ec7 | -11.0101 | -55.05511 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 98cfefa4-6fd5-375f-8615-afe04521d4a3 | -12.76683 | -44.40813 | 2025-06-16 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3b982f8-f4ad-3f41-a16a-453ee25a9ed7 | -12.17548 | -54.23289 | 2025-06-16 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd70eb94-2e08-38d9-9f7a-20ebaefd6919 | -11.01021 | -55.08185 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8332072f-b740-3253-978a-caf037cf1528 | -14.65449 | -48.05838 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e705fae1-0b0e-301e-af7d-5c93a894bc71 | -13.91111 | -54.61856 | 2025-06-16 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa843dbc-937b-3c2b-ba34-3ab2db3d7a39 | -10.84737 | -53.77686 | 2025-06-16 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70190221-fb7f-3cab-b54d-c12457678810 | -10.09453 | -52.73548 | 2025-06-16 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b378fc0-49d6-3953-b099-4ada37eac736 | -14.83073 | -48.45403 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d1077cf-4918-3a54-9988-06d0493f48eb | -11.00547 | -55.08091 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39191ca5-8b46-3efd-b02c-4419477b56b1 | -12.72658 | -46.28057 | 2025-06-16 04:27:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 624c9592-2ea3-3711-9929-9f96cc837e12 | -11.13431 | -53.9463 | 2025-06-16 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71453f2a-77b5-3c40-97fb-bd1351c5e10d | -14.64679 | -48.06433 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0eb6145-cc25-3b91-bf81-702d921574b4 | -10.01031 | -48.22329 | 2025-06-16 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc18bb86-6f3f-32fa-874e-0bd7b614411c | -12.97956 | -48.64578 | 2025-06-16 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80e7cdd3-8df8-3c02-ac3b-502fdb3a44a3 | -11.00579 | -55.08314 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3b91840-c266-361e-ac1c-e0e4d80fed7c | -9.4153 | -48.43527 | 2025-06-16 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dba897d9-394e-3482-8438-42d9352c3902 | -12.22485 | -43.88213 | 2025-06-16 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71bf4528-39a0-3521-86f2-f0cbdf145945 | -12.08897 | -49.48952 | 2025-06-16 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aeb25f97-ba28-387f-83ca-ea63f5c49948 | -11.98739 | -57.19668 | 2025-06-16 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b1a6dd0-f63c-34ed-a601-72fb547ffc58 | -10.56807 | -52.01765 | 2025-06-16 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b09b2632-e015-39e6-bbec-b4ddbc3a3ee2 | -16.28641 | -52.9329 | 2025-06-16 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0297ec3c-6686-3c5a-a47f-828c5d1972f9 | -22.78834 | -43.75699 | 2025-06-16 04:29:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6c28975b-cfd1-399e-92ad-28fd97831401 | -17.00923 | -49.78045 | 2025-06-16 04:29:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d81127db-bd11-3b7d-a502-814a83f4d82f | -22.71326 | -43.2366 | 2025-06-16 04:29:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2ab49dc7-50a7-3f63-b5be-38032e3de05f | -17.45485 | -48.17527 | 2025-06-16 04:29:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d574242-0e82-3aeb-90a1-5522d89319ad | -20.54522 | -54.12672 | 2025-06-16 04:29:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9b43c6d-fb6c-319c-92c2-7dbeadf0a947 | -19.27396 | -55.14849 | 2025-06-16 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b49d0181-e3b2-3d08-b15d-6f5eef8516d2 | -17.91475 | -45.53807 | 2025-06-16 04:29:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7b4630f-4605-3d31-aad4-c87084b7ccd5 | -16.65973 | -49.34828 | 2025-06-16 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 76a332e3-3b0e-379f-86bf-406bfbebd228 | -20.47861 | -53.6753 | 2025-06-16 04:29:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ef22833-2c10-3af3-b964-bd1aa546201c | -16.29684 | -52.93718 | 2025-06-16 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c6226af0-dbb2-3aff-923d-51b4399ceb6f | -16.44102 | -54.843 | 2025-06-16 04:29:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c29c506-10e3-3aad-bb96-c2d53f2adee9 | -16.2902 | -52.93361 | 2025-06-16 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0178f2f2-afb0-3415-9f4c-6e829d265dcc | -22.85845 | -42.9828 | 2025-06-16 04:29:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d56a7ded-a047-32cb-9cb5-c803fd199de9 | -17.4554 | -48.17165 | 2025-06-16 04:29:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a9f2e31-c2c3-30ee-be21-40bafe28db02 | -22.67765 | -42.85563 | 2025-06-16 04:29:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d23cf384-8687-363c-aba0-07850275c1f4 | -16.29697 | -52.93965 | 2025-06-16 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a440a45a-8c77-397c-999d-6196117410a3 | -16.29399 | -52.9343 | 2025-06-16 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43023aae-bf52-3b45-a339-fba119f14b80 | -20.76629 | -46.76829 | 2025-06-16 04:29:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 22abe1a9-10d2-3f77-b754-70c624f5d9b8 | -20.41625 | -43.55289 | 2025-06-16 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 15180a79-2271-3266-a7ed-b77903eec145 | -16.29317 | -52.93903 | 2025-06-16 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4700e2f5-7fd5-3370-b6e0-6eae15d3bd66 | -11.0115 | -55.0561 | 2025-06-16 04:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| e22872af-081b-3683-819d-8159d2190949 | -23.33788 | -46.77442 | 2025-06-16 04:32:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 32d301b6-c312-3d1f-a269-173ff9eed1f0 | -26.95833 | -49.1642 | 2025-06-16 04:32:00 | NOAA-21 | INDAIAL | SANTA CATARINA | Brasil | 4207502 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d63fbba3-8b02-3aab-ac7c-4f00f7cdec88 | -23.40684 | -46.55902 | 2025-06-16 04:32:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dfd1aa77-e841-3786-823b-cf000f160149 | -23.59389 | -47.43813 | 2025-06-16 04:32:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9178e342-fb0b-3389-8472-94646f5e08da | -23.51612 | -46.474 | 2025-06-16 04:32:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6c2a87a8-2636-38e7-a0b1-6c19b7dc2706 | -23.51475 | -46.47136 | 2025-06-16 04:32:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1e615734-9052-3aac-8ed1-d2ae2613f793 | -23.06469 | -46.64185 | 2025-06-16 04:32:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f68ae702-be81-3427-8164-4e88abbfc05c | -22.54092 | -48.81214 | 2025-06-16 04:32:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cb17bf2-779d-32bd-9caa-ccc73649d11c | -23.98475 | -48.91883 | 2025-06-16 04:32:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2813232e-f014-3511-9c2a-4d3bc781febc | -30.15131 | -52.02625 | 2025-06-16 04:34:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| d8fd4a9c-50e8-3f54-b853-b39866404aab | -11.0115 | -55.0561 | 2025-06-16 04:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ec7de106-eb4a-3e31-915a-6844a3409299 | -11.0115 | -55.0561 | 2025-06-16 04:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 96b8ae7d-3603-38ac-93f3-4ba9611bd2e5 | -6.8693 | -47.23728 | 2025-06-16 04:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f20c5f5-3223-30a1-9344-ea20c5bffa70 | -3.70694 | -53.71128 | 2025-06-16 04:51:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f37c36da-343f-3187-9980-c2e7e9ceebf2 | -2.58637 | -51.92258 | 2025-06-16 04:51:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 443da562-32da-365e-8849-efc44f50cbfe | -11.00239 | -55.07091 | 2025-06-16 04:53:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd41af2c-4c24-34ce-89af-903ec047880d | -9.49334 | -48.3034 | 2025-06-16 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4640e900-4c02-3723-9638-516cafee08be | -9.46157 | -57.84509 | 2025-06-16 04:53:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b07b8251-da47-300a-97fa-c5750e78bc6d | -11.13929 | -53.93073 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a92e9bd1-d2b0-3101-8afa-fbbe6460c261 | -10.38307 | -53.50964 | 2025-06-16 04:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0e2e2e1-7383-33df-aa69-cc0bc00d98c0 | -10.85346 | -53.76909 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0892f77-1663-3be3-b3cf-41e8e54de8b3 | -11.00974 | -55.0684 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4a6b6891-55f9-318f-9f20-dac36f25fb38 | -12.76736 | -44.40369 | 2025-06-16 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34336c16-aff4-34f5-bac5-87b808871ed0 | -11.00536 | -55.05275 | 2025-06-16 04:53:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| b5be2038-7f24-33a1-a998-90810df83596 | -11.14094 | -53.94183 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| dec98e24-84a7-3c67-a9ce-d9152166bfef | -10.22852 | -54.29685 | 2025-06-16 04:53:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1e475bb0-b953-3103-9322-780484b7ceb5 | -12.76692 | -44.40734 | 2025-06-16 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b49c133-f304-3b07-ba00-a9068c878d1a | -9.4046 | -48.43082 | 2025-06-16 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64647a46-1c64-3acc-ba62-f180d68665d5 | -10.7821 | -55.45548 | 2025-06-16 04:53:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c128ddd3-e777-3061-944f-73ca70b3e93c | -12.98192 | -48.64183 | 2025-06-16 04:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2317193d-c9d6-3183-879b-f66f43378fcf | -11.01034 | -55.06475 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a3e22690-569e-351d-b253-bd784730276c | -10.92814 | -56.83522 | 2025-06-16 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51167a8e-4c9a-37e1-8259-38b431f708b0 | -11.13819 | -53.91612 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dff0ce25-35dd-32b2-a12c-1dcce00af3c4 | -9.41244 | -48.43859 | 2025-06-16 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a45bfe7-496d-3607-9d1e-4ce2ab26ec94 | -9.41588 | -48.43782 | 2025-06-16 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88aa80aa-dd15-391b-8808-bf5bcd5ef707 | -11.0285 | -44.6424 | 2025-06-16 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e03c4aea-f8a3-3bdb-afdd-96f91ead1e56 | -12.7614 | -44.40662 | 2025-06-16 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb0247c9-4fc1-3077-814c-6274f755d002 | -12.72143 | -46.2779 | 2025-06-16 04:53:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bfcecd1f-5bd2-384f-a90b-330927e0ad09 | -11.01193 | -55.07624 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3148a9ed-b8da-3774-997c-d967f326bac1 | -9.90437 | -56.05267 | 2025-06-16 04:53:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65464def-394f-3e30-ac30-0e8b0293551b | -11.8828 | -54.67943 | 2025-06-16 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6130c509-2fa0-314e-8f64-6405f509724a | -12.08827 | -49.49117 | 2025-06-16 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee3c0758-6dd8-34e5-bec6-4f700e8a189a | -11.1415 | -53.93831 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1f90e87d-6e37-324d-a342-d93270d6951d | -11.00855 | -55.07568 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bbbd691-42e5-38e1-b91b-5fd940a83cb8 | -11.02277 | -44.64493 | 2025-06-16 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 647fe725-28c8-322f-9418-a2773e9060cb | -9.40059 | -48.43021 | 2025-06-16 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1134cbc-cebd-3ce3-987a-4d472d80eccf | -12.05822 | -48.07906 | 2025-06-16 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b74ee664-1e1f-3e09-a79a-a9ec682e3cae | -11.13373 | -53.94427 | 2025-06-16 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03bfcbbe-a940-35e0-b917-a459ced24524 | -12.17402 | -54.23261 | 2025-06-16 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3d986ca-225e-3d16-b374-9332874e37e4 | -10.92885 | -56.83101 | 2025-06-16 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db7526fb-93d3-3d4e-bb47-dc7623c505a9 | -11.00358 | -55.06364 | 2025-06-16 04:53:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22687653-b44e-3397-b650-bf84c6bcc88a | -11.00696 | -55.0642 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5891f2dd-9006-3d97-a784-360dac723a4b | -10.78272 | -55.45174 | 2025-06-16 04:53:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a902e8e8-e0ef-323c-9e58-e61da47f2365 | -11.00755 | -55.06056 | 2025-06-16 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d331c4f6-b8b3-3efc-a633-a778ca0440db | -9.41186 | -48.43724 | 2025-06-16 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README8.md)
