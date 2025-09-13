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
| 1a37f72b-a56a-3a1f-9e4c-5666e8c6f771 | -10.74657 | -50.50392 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2f550001-5a4a-36e7-90aa-7d4b3450f4bf | -12.11426 | -44.8474 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a04b9ef2-5e66-3aaf-a2c0-ce30d723978a | -10.51374 | -51.5521 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abae454b-0aaf-34bf-8f57-3d1d651a69de | -10.77279 | -50.52612 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 97f986ce-8b32-37e1-83bc-f09a12a18e98 | -9.86021 | -43.12553 | 2025-09-13 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0d4561bd-6e50-3476-b37e-1fc026a1dca5 | -11.71084 | -46.559 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb7e2455-9313-3325-a264-24453c0b65a3 | -14.17406 | -46.26319 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 73521c0d-233e-3865-bec7-bbd7f60ce158 | -12.12812 | -44.84502 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fd002390-3127-3208-a916-7dabba8d95ed | -11.74427 | -44.21225 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb6210b1-a9b4-3333-9c90-5996365d56a6 | -10.78943 | -45.99424 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fafc55ea-5cff-3d76-9ed4-b1506ddc2e86 | -10.78054 | -50.53907 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b472f4eb-8241-3051-97f1-c20ae165cef3 | -12.44633 | -44.74629 | 2025-09-13 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7f3316c7-8fe7-3caf-b408-c7a5720343f6 | -8.40815 | -47.26846 | 2025-09-13 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 505a927c-f8d0-3bb3-bcc3-999866300c03 | -10.69912 | -54.44764 | 2025-09-13 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e64a6452-4657-31f4-b6e2-f2a1536b5288 | -11.76561 | -51.51493 | 2025-09-13 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a9063423-c0b0-38c8-8235-d4946549f9e0 | -10.7007 | -48.653 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80947d94-314a-3baf-9747-b632d1b95424 | -13.7785 | -46.28807 | 2025-09-13 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a6f5509b-b752-397b-b310-a36c50a1373c | -10.50144 | -51.53387 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd8efbf0-152e-30e4-a775-5b1fd7a45930 | -11.72278 | -46.57926 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4605d7b1-846c-3c3c-8be3-1fc122ce43ee | -11.17331 | -51.41687 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e01f1b6-763e-332c-9801-46536bd405f0 | -14.4335 | -47.33744 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af76d990-bf8e-3a68-87ba-d94c945c8c2b | -11.1028 | -51.44305 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02253136-006f-305e-8b37-2a1ae9377ec0 | -12.99257 | -46.75267 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c61139de-4d8d-30b0-b08c-9217ca3470f9 | -14.16949 | -46.1658 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 93c3d2a6-cc4b-3214-a4dc-9f66981f02c8 | -11.42466 | -50.74833 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 085b3a73-97ae-3505-a394-a5259d36335a | -13.40184 | -46.80257 | 2025-09-13 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 364595b4-c531-3ca1-b368-fe291986bfc2 | -12.79809 | -47.98456 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34c8cee9-c8b8-3a23-8fa3-16a7f1c5e718 | -12.89711 | -47.94727 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f85549cc-0e52-33d9-8c7a-bda29cc71303 | -15.0619 | -48.015 | 2025-09-13 04:08:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc939016-27e8-383b-9bca-a833876d0da9 | -10.359 | -50.50317 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0d5452c-18c2-3607-bd3d-2d51c7d1bc89 | -10.32708 | -48.8265 | 2025-09-13 04:08:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b2251739-69e7-3e95-9ec0-43bd013ca68f | -11.4983 | -43.65144 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 304d5e55-3260-3e33-be53-e9ac8987ae81 | -9.78935 | -48.90511 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea7a7ad6-4b3c-3e51-8cb2-f8e177a8cdc5 | -14.18193 | -46.23877 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 679b2f0e-53bf-33eb-b7e2-f933fa38e4cc | -10.71443 | -48.61228 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70b13e02-f503-31f2-a828-c1bd66467aba | -14.45697 | -47.33586 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb22e076-5c52-3a9d-bfa5-270eb951e4f4 | -11.10102 | -51.45247 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5a7a188-73d5-3c4f-a2da-1a8dd97867ba | -11.43669 | -43.55042 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f772b6e7-4abe-39dd-9b36-c005f38c0a5e | -8.92163 | -46.15662 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f737e378-38c4-320a-a4ed-a99aec6ba44e | -8.94855 | -44.44335 | 2025-09-13 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e860a93-3415-3ebd-b59c-db9e6fa28d0e | -11.06733 | -40.80482 | 2025-09-13 04:08:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a2e23996-2bfb-32a8-ae42-ab9da2d33f84 | -9.4167 | -43.40734 | 2025-09-13 04:08:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6c9ef64e-bd8b-30b5-8738-8c461873671c | -12.84978 | -47.94822 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0c5e277-62b6-38c7-9af2-a5dd08ae2abe | -11.17727 | -51.41555 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a4257df7-4ac6-3dda-bc39-f81752e0e475 | -11.79677 | -51.54708 | 2025-09-13 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2cfafa7b-1320-34a1-be7f-7d2490f85228 | -10.70362 | -50.50583 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af327b99-a610-3331-aff3-aa72d2b7a7ed | -14.22028 | -46.29322 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad6cfb0f-dfc5-3197-86eb-8c04e167e364 | -9.82134 | -48.89655 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a79ebf9-6bd3-3048-89a9-e81dca46bb3b | -11.43932 | -45.62453 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3bd13897-a821-3f60-8a09-79df792301eb | -11.8666 | -46.76377 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f4f163d9-d467-3848-be86-21c332968f81 | -11.9965 | -47.7596 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8b1974c7-ad44-3f5a-8bd9-b7bf7297e6e8 | -13.25535 | -51.71431 | 2025-09-13 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97ba15b0-42f9-31f9-aeab-d83c979821f1 | -11.04711 | -51.47639 | 2025-09-13 04:08:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f52a7322-b56f-3660-92fb-f79bccf95a88 | -14.69294 | -43.66581 | 2025-09-13 04:08:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed145699-1c9c-3b44-8ac8-aed553b70842 | -12.80925 | -47.99129 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 79c1f7fb-e822-328c-a9d5-816b889d0710 | -9.80816 | -48.89323 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c91b139-63ce-3ad8-becf-4fb88e574dc7 | -11.74239 | -46.62902 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c71fe38d-7e9d-3f65-bc43-6867687f20c1 | -14.68962 | -43.66526 | 2025-09-13 04:08:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcbe5f6c-9c99-3c25-b8f9-b9f72fabb9f6 | -10.23203 | -48.62114 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fcc2ddac-6fed-3480-bbd4-62a058489016 | -9.22043 | -46.53967 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a76ba0af-ccfe-3392-afe0-96c556fd9213 | -11.62232 | -46.60446 | 2025-09-13 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d9a4a52-0ca6-30bd-9de1-46e21db32a3c | -10.41489 | -50.62384 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| faad395c-3250-3715-8db0-130c1bc26a28 | -14.17905 | -46.25548 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9deb2e8d-328f-347f-a695-060016e9c909 | -10.71071 | -48.6466 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e8d751a-497f-346d-aa70-817cbedf2686 | -9.74796 | -45.38887 | 2025-09-13 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e19ea3c2-3120-30d7-a24a-8a60191d35c7 | -11.84934 | -50.56487 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f8ee91a2-46cc-3dcb-a505-e1d3dd808083 | -9.72344 | -48.35175 | 2025-09-13 04:08:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67344b7e-037f-3869-b3ef-408771f5dd07 | -9.96531 | -50.29863 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ea5aa986-ab2e-389c-baa2-8b4aab623e02 | -14.27953 | -45.03767 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88dfce1d-372c-3035-994a-a7ac5cbe2df6 | -12.91103 | -54.74989 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 77d9b73b-cda8-3f7b-abb5-afb9cd37a118 | -8.40406 | -47.26774 | 2025-09-13 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72371b08-7a51-3e28-91f5-b2785f08c775 | -15.05976 | -47.98935 | 2025-09-13 04:08:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aaea301b-5591-37ec-a292-eb77fc0b9043 | -9.85072 | -43.14212 | 2025-09-13 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7dfe657d-3acb-38c9-bc58-f0b23d11d242 | -10.37822 | -50.49156 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8862547f-3e63-35ce-a81b-a70324115bbc | -9.02573 | -47.04613 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1804a0bc-5f04-3ba5-b323-6bd43d576d85 | -10.35558 | -45.40349 | 2025-09-13 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3498369d-b31f-3d13-bb83-5d3c62e0fd02 | -10.51438 | -51.54872 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 191557ac-a313-389a-92ba-ec3775d37f92 | -9.78709 | -48.90811 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6060dd92-a73f-3b1e-ae72-0a6815ece0d5 | -11.43335 | -43.54988 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52ac1abd-c375-3f3a-8eeb-7c9c28aa45e2 | -11.14549 | -45.3188 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07f2ee62-9f71-31cc-a287-11efc160a877 | -14.22515 | -41.97657 | 2025-09-13 04:08:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 71e659ee-bda4-34db-aaa1-16172f86b5ec | -11.43726 | -43.67518 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcd589ae-9de5-3710-9f94-0d7da14161e0 | -8.50795 | -47.31939 | 2025-09-13 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2859be45-4d83-33ee-bed8-f5c85347a5b7 | -14.46288 | -47.3242 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a85fd066-8020-38a7-afad-13790db237fb | -10.34099 | -48.82462 | 2025-09-13 04:08:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b1555750-4482-33d9-83f0-43f4d1b24998 | -12.57924 | -45.70088 | 2025-09-13 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2f9cbb7-c2ee-36b5-bab1-5249405f8aa8 | -9.52132 | -54.63952 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| e03c254e-2931-3d5f-b2f6-829ac07e3209 | -13.29096 | -43.76486 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21ee2c01-bc75-3901-b44a-35565c0bf8c2 | -11.18296 | -48.35104 | 2025-09-13 04:08:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da10c360-8eee-3e04-aa92-288cc880b256 | -8.95358 | -44.45613 | 2025-09-13 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a65926f-ecca-3e8b-b4e8-24ca8f425f15 | -10.77853 | -50.55016 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d427efc-7ffc-36a6-b215-7fbed3f0d797 | -12.12469 | -44.84449 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1e62a213-67ce-339c-8056-56b633cfddab | -11.15528 | -45.23756 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd48670f-57c9-3eb0-a7f8-31a49b2eac47 | -14.19962 | -46.24237 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 36a4a352-b37e-372a-993a-865708c032df | -10.55972 | -43.65966 | 2025-09-13 04:08:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d82e57da-b2a0-36bf-ad1b-a0706b1b1d68 | -11.44222 | -45.62921 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 594abbf6-3032-31fd-9001-7060dce67a23 | -12.3831 | -40.39569 | 2025-09-13 04:08:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2053c79c-d41a-3e2c-b9fb-a2fbdc5aa7af | -7.91033 | -44.86912 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02b6b16b-39e2-36bb-8b45-a5a196ecaf48 | -12.12316 | -44.83248 | 2025-09-13 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9822b2f5-4780-372b-a527-c9e65e1cb763 | -13.14292 | -47.13582 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README58.md)
