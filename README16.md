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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 070ec417-d256-3143-ab56-fc3a95d7b209 | -3.87462 | -42.96017 | 2026-06-24 05:08:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c52936c-6764-39d6-9e40-61f1f267621a | -9.22118 | -45.33786 | 2026-06-24 05:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef5e5276-5fdc-3427-99ae-25a40f2e8263 | -9.21277 | -47.93008 | 2026-06-24 05:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a6f1c8b3-222b-365f-9121-555b42ad401c | -3.50528 | -48.03925 | 2026-06-24 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 800ee9cd-3ea8-38c8-b1fe-f3612a376ec9 | -6.5109 | -42.22161 | 2026-06-24 05:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 115dea95-cb72-31f5-a3d0-30b747340c20 | -8.60594 | -45.99966 | 2026-06-24 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d61d0ad3-dbf4-3b57-9452-950d62c2a271 | -8.07365 | -46.38977 | 2026-06-24 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90aee598-34f4-3540-9fd3-9178cdc7ab22 | -9.36439 | -50.54609 | 2026-06-24 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c9c69150-0375-36f6-a54f-8beb20ea41d8 | -7.37517 | -42.80534 | 2026-06-24 05:08:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9382ae96-66d8-32c2-a7ba-40ebeaf621a1 | -8.60637 | -45.99657 | 2026-06-24 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3e31bc73-2e90-3bec-91ef-81f3bc60b8ce | -4.66267 | -43.12467 | 2026-06-24 05:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67227f1d-48fd-3d2a-87da-0c0a6c066fec | -4.67573 | -48.15615 | 2026-06-24 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f667cfd1-19ef-3342-9689-83f3151744f7 | -4.66284 | -43.2237 | 2026-06-24 05:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a140e58c-776e-3ced-9715-3eb56122639c | -7.9222 | -48.29243 | 2026-06-24 05:08:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 809109e4-0e23-3c77-bfbc-4975eeee9c7d | -12.8354 | -44.3657 | 2026-06-24 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 295.3 |
| a8648f8c-1b6c-3067-b648-7d586cbb5942 | -12.8552 | -44.3389 | 2026-06-24 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 77374d16-f28d-3365-ae2e-d515caab0e9e | -13.0635 | -53.3546 | 2026-06-24 05:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 48bb47ae-8347-3059-a174-24bc1a9e1674 | -12.8359 | -44.3422 | 2026-06-24 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| b99fcf7b-6f24-388e-b902-031456735c11 | -12.8349 | -44.3892 | 2026-06-24 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 2a3abf59-5635-3082-a95a-1495af85e511 | -12.8543 | -44.386 | 2026-06-24 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.6 |
| b3a02746-693b-3a1c-a8e8-7dd463a77b80 | -12.8548 | -44.3625 | 2026-06-24 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 265.4 |
| 55cb914e-3d63-352b-80cd-220614f05b44 | -10.90587 | -54.13832 | 2026-06-24 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 159129d5-cf0b-3873-aca3-0aa43ad92d9c | -11.62465 | -48.49125 | 2026-06-24 05:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae48baec-8836-3281-bbf9-858d2faf2088 | -12.67961 | -54.58146 | 2026-06-24 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b34516a-8a77-3603-abe4-64d976e8fc8f | -9.18711 | -58.06746 | 2026-06-24 05:10:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 700aad4c-52fd-390a-8732-36ec20a975e9 | -10.1581 | -56.60973 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6cca39a6-6014-3593-896e-83b532b4b969 | -10.87306 | -49.40166 | 2026-06-24 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5eab5df-60b6-3012-abb2-aca20daa642c | -11.75875 | -47.07862 | 2026-06-24 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62a487f9-a53a-32a6-a539-930b6541779b | -9.60658 | -56.92709 | 2026-06-24 05:10:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3471fa23-267c-3ae1-b017-635ae87dfddd | -12.85119 | -44.35787 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 894ec663-5d3b-3dc6-94e5-8c93d950cf04 | -12.84707 | -44.35876 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 09620cc9-74c6-35aa-80d3-d265b07045b4 | -11.26104 | -43.36403 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 80862c1f-eaa8-3fc2-8115-f46065c2f1a7 | -11.29716 | -43.33045 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 157863b1-e729-3659-b342-baf9efaff49e | -11.27768 | -55.7947 | 2026-06-24 05:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c50100f1-629e-3eff-b561-04dddccd3205 | -12.6791 | -54.57796 | 2026-06-24 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de7533b6-ce7f-3f08-85de-2a94b96ed047 | -10.87682 | -49.40639 | 2026-06-24 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 875b7ae3-c3cf-340f-b4c2-c98e912b4584 | -11.30428 | -43.32585 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 65774188-2102-3130-b4aa-8d6ee0dad3b0 | -14.75712 | -48.18555 | 2026-06-24 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8e6f8ae-fabc-3031-861a-b76c37ad5b9f | -15.75791 | -43.23423 | 2026-06-24 05:10:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 300f3c1e-9ae8-33bc-9063-969f025496a4 | -11.94342 | -57.70343 | 2026-06-24 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b7be77e-e78a-3990-9f0a-07497aa5e574 | -10.76734 | -54.10945 | 2026-06-24 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab3573dd-bc77-397d-ae22-38629f351940 | -11.75914 | -47.07555 | 2026-06-24 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fc128726-c0b5-3490-b708-ed60a111f8d2 | -10.15912 | -56.62483 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d17e5370-d75d-3627-ba0c-885ed781a448 | -12.77509 | -44.43818 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c586ed91-605d-316a-bfd7-2fcd1dbd3865 | -11.51441 | -56.13057 | 2026-06-24 05:10:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dcf2651-50c0-39d3-a3d1-15a5279faa1a | -10.15574 | -56.62427 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f6378a2-39a6-38f3-9d94-12255f05ce36 | -13.77656 | -53.07495 | 2026-06-24 05:10:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e48a3a68-f443-3fb4-9290-f3001ae9e96b | -9.38037 | -58.20865 | 2026-06-24 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d7fab31-fe19-394a-bfc3-1cd176298830 | -9.78866 | -56.94979 | 2026-06-24 05:10:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcc130e0-ba01-37e2-ab4b-9a2e0be99a2f | -12.8465 | -44.36362 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 50b8bc4a-cd56-3f10-ab94-0be6dd04a49c | -14.52988 | -49.11487 | 2026-06-24 05:10:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe9f5a9f-8140-3977-9f58-2a139265777b | -12.21768 | -57.28704 | 2026-06-24 05:10:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7b1dd3f-1ec8-3010-9dca-e4572d4d2cf6 | -12.68017 | -54.57779 | 2026-06-24 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1b9d928-6af1-3e01-bc07-b200770cb86d | -10.1625 | -56.62539 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec7b131d-d95a-3c79-ac4c-41cceee974b9 | -10.27408 | -60.54721 | 2026-06-24 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f281c54b-ac9f-3922-ad38-6664c82efc47 | -12.06353 | -48.42544 | 2026-06-24 05:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c5a15f6-dbc7-31ac-aad0-0acee9e0ae46 | -11.23765 | -43.33921 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3fbb32ac-7697-3eae-a7e5-a03da604b67f | -10.12521 | -52.11015 | 2026-06-24 05:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42803890-0260-32ec-99da-fc06ddeece45 | -12.78072 | -44.44379 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b3c4723-cba7-3afc-9942-fa0cfbe6c9a5 | -12.83918 | -44.37241 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 68c21dc6-e953-3f0c-8fd5-b40ed692e3cb | -12.82789 | -44.3611 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ead4498a-548e-3d6d-ad6f-a8ac67c799bc | -12.67853 | -54.58162 | 2026-06-24 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a9e9904-c534-3c9c-92dc-1e4dd6486d51 | -12.77454 | -44.443 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7b8cfc01-61cf-3b03-89ae-75f04a40ce4e | -14.75711 | -48.18724 | 2026-06-24 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbe327b5-a580-3e8f-8a4c-8a91e1d2fd2a | -12.86876 | -44.36986 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adf26e0d-628c-35e5-afb3-9f5b03becc94 | -12.85214 | -44.36922 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 005f4184-7467-3eb2-a07c-361e60537497 | -10.5421 | -53.73684 | 2026-06-24 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfefa612-514d-3870-9b22-735cc608ee21 | -10.15794 | -56.6321 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66a5b213-e7d5-3cc7-a217-af6366c32061 | -11.29867 | -43.32484 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 137187bb-7739-38bb-9824-544459f2a0c9 | -12.85065 | -44.36275 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e6c74c7b-cb7f-3fde-a08d-bc23de571043 | -12.774 | -44.44782 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e2e8dfa0-5235-32c6-9eee-eed3e6e3f8b0 | -13.12039 | -53.53247 | 2026-06-24 05:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a40114b9-64cf-3470-a1ba-aa654a8ec3b7 | -10.2794 | -60.54068 | 2026-06-24 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 058ed51c-025f-37f4-8a0b-536286db33cf | -11.54251 | -52.78117 | 2026-06-24 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f040956-8c12-31c2-80ca-a44105effd11 | -12.83353 | -44.36678 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 41c9006d-e1b1-3cdb-992c-840b44a059a0 | -12.8403 | -44.3628 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| ef8218fb-2e49-3b83-bfc3-e33757f57c4c | -11.30518 | -43.3255 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4a4a1956-882e-3b98-9c7e-8d25b7007ae2 | -12.19619 | -47.96856 | 2026-06-24 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33a21035-5fa6-31ab-a9cf-0e43f462d5c8 | -14.52461 | -49.10569 | 2026-06-24 05:10:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a1db50c-9718-377d-abcf-3280bf973690 | -16.8461 | -45.42489 | 2026-06-24 05:10:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcef6afa-66ad-3835-bdb4-e8973ff58ca6 | -12.7858 | -44.45412 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 292a14a9-9f8e-36d0-aa92-6c39bea795dc | -12.86821 | -44.37473 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3eb8747-458f-342a-a243-cc7197785eec | -11.23704 | -43.34435 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 123327cf-2ac0-3c6d-955a-97aff78713c6 | -17.61231 | -46.69743 | 2026-06-24 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aab13da3-f68a-3ecf-8aba-2adf05fb3971 | -13.07133 | -53.35405 | 2026-06-24 05:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e44b48bc-7979-306a-b639-390a593add85 | -10.69884 | -49.6143 | 2026-06-24 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b003e4f-c267-3336-bdee-22d0537da847 | -10.12457 | -52.11436 | 2026-06-24 05:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 586edb44-6b23-363c-a161-56e21044bc6a | -9.17701 | -58.06151 | 2026-06-24 05:10:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80bb5304-da52-3ff0-a11d-a010bc14fa86 | -11.29803 | -43.3301 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f1cc4f2e-6bba-37fa-8418-dc1c4d62346f | -9.18284 | -58.07098 | 2026-06-24 05:10:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7aa21f3-648e-3889-849c-ddc522dee44f | -17.25897 | -46.32283 | 2026-06-24 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc6135ae-ed3f-3066-8fc0-ed3400695a8b | -12.83409 | -44.36195 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| a1c57700-159c-38ce-b711-0b659cdbc9b5 | -11.30765 | -54.72066 | 2026-06-24 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efc13361-05ef-34a1-ae59-b3949ed5daf9 | -12.8574 | -44.35863 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bf1aa1d6-7a10-3eb0-8645-be62e3476dd8 | -11.20802 | -54.33357 | 2026-06-24 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| df7fa104-e253-3f8d-990e-c1d5ad205e79 | -11.62 | -48.49059 | 2026-06-24 05:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 948225fb-aafe-32e9-a5f1-685cacb388cc | -10.80039 | -48.56158 | 2026-06-24 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f5256b9-b5a7-303b-ba70-e3a760a13291 | -13.06075 | -53.35241 | 2026-06-24 05:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e9e17bd-23e8-33e0-9f66-68cbf41af467 | -10.15971 | -56.62119 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f1011a1-bd27-3921-a94b-18a93f4238c0 | -11.30096 | -54.71959 | 2026-06-24 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README17.md)
