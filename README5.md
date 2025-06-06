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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 923b52d4-0663-3278-9d1b-22037ed1eacb | -12.2655 | -55.07546 | 2025-06-06 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99b37ecc-b2da-3854-ba36-45193412b472 | -14.04198 | -55.13959 | 2025-06-06 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cd788b9-03f2-3f58-8407-8fc002d5682d | -12.84142 | -47.3878 | 2025-06-06 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 829338b0-eb01-35d8-8238-80629f405728 | -14.04274 | -55.13582 | 2025-06-06 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ea71173-28d5-39d7-8cdf-3a99da71959b | -14.23515 | -45.48376 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7c6de9d-20f3-318f-b04a-0e7623442fdc | -11.29554 | -53.98353 | 2025-06-06 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| edd43717-68f5-313d-b04a-e6f9b140804f | -10.50211 | -53.65819 | 2025-06-06 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21f01f24-2260-339f-86ce-c7077e8c49f9 | -13.87751 | -47.14411 | 2025-06-06 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb005f6b-f4aa-3ad1-87bc-20cf64bab28a | -13.51478 | -56.56868 | 2025-06-06 04:17:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7c418db0-a03c-3443-98de-d6dd32e484dd | -12.95676 | -46.77799 | 2025-06-06 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f26d4109-e473-3509-b5f3-223c9f742495 | -17.23325 | -46.78927 | 2025-06-06 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28bdfcd8-7faa-37d0-81df-8503afd483b7 | -12.95613 | -46.78184 | 2025-06-06 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 63992c49-220c-3952-9f56-b13e8f6929c6 | -12.83507 | -47.38255 | 2025-06-06 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d1ba1405-f390-3684-97f6-d7ae73c14d37 | -12.05587 | -47.3257 | 2025-06-06 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f63a45bf-99dc-3277-8966-d3c2e480aba3 | -14.22628 | -45.49688 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5db92504-8909-30a6-9fcb-97eb7e22392c | -14.22024 | -45.49223 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0eb98402-9f76-34a5-8cc4-3c2c9a9b4bb8 | -13.88895 | -54.67829 | 2025-06-06 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9da29378-fd49-3212-a719-baaa7663996f | -17.78343 | -42.80936 | 2025-06-06 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 018d4cbd-f652-3a09-8588-044bad73bc56 | -15.14994 | -45.50858 | 2025-06-06 04:17:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db28ef24-3737-32ec-a04c-18b7ad979e61 | -10.48997 | -53.66328 | 2025-06-06 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 59cff992-4a7a-3d7f-89a5-7c112ef6da72 | -12.15358 | -46.59501 | 2025-06-06 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d79e492-6da2-39f7-bf93-cc5b5b609b6c | -14.73544 | -45.0942 | 2025-06-06 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5a02570-5c07-3d2f-80dc-45a3dd1f9689 | -11.57551 | -47.44249 | 2025-06-06 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0325ecaa-6d55-336d-bb27-321e08f72a76 | -16.72515 | -45.74775 | 2025-06-06 04:17:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| afabfca6-b685-3136-aff5-135988abf12a | -14.92692 | -45.96991 | 2025-06-06 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7378b1aa-8027-325d-ab8a-7d63dba2be51 | -11.29483 | -53.98717 | 2025-06-06 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 338a37b7-16f9-3da8-a9de-b73912f4793b | -17.60042 | -48.42165 | 2025-06-06 04:17:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8ba7fad9-b167-385a-abd5-6276c84ac4ae | -12.41102 | -49.67742 | 2025-06-06 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 912cbacb-fa8b-33ad-a30d-4c374938f349 | -11.91917 | -54.82279 | 2025-06-06 04:17:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7424cb04-eb46-355d-8b3f-e14597a6ce9d | -11.29362 | -53.98679 | 2025-06-06 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4549cd93-d99d-30e0-b300-861086b208d9 | -14.70451 | -40.97605 | 2025-06-06 04:17:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c54cf892-d8cc-34ee-8b41-d3fdacb7a5b5 | -13.45327 | -48.21822 | 2025-06-06 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d17834d8-185f-34a7-bd33-a40e68d26d96 | -13.03333 | -44.11707 | 2025-06-06 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 968471ed-5ea1-3f09-adb1-48f7be563a50 | -14.23128 | -45.48677 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8270cc8d-62a2-3d00-9ea7-a16e5c547b47 | -11.79994 | -42.62408 | 2025-06-06 04:17:00 | NOAA-21 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fc7b8567-4b18-36c1-91d7-f79f67316a38 | -12.38103 | -47.31635 | 2025-06-06 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91695ddd-b398-31eb-9eed-e34908bd6fef | -15.14664 | -45.50801 | 2025-06-06 04:17:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93d5bea7-f91c-3613-afd1-708ff4169ece | -12.96766 | -46.77594 | 2025-06-06 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8494c51a-672a-3170-9a1d-12b93ac1a108 | -14.03242 | -55.12956 | 2025-06-06 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfa74440-0d4c-3165-a733-4969a1b25b93 | -12.95739 | -46.77415 | 2025-06-06 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34ddd575-7f0f-31a8-af52-d18c07e18979 | -12.38171 | -47.31233 | 2025-06-06 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e46644cb-4e41-3c10-892f-33ed7da19a20 | -12.83858 | -47.38316 | 2025-06-06 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fd3d0693-e806-384c-992c-3e943d7e28f3 | -14.90573 | -45.99583 | 2025-06-06 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 143d92dc-86b9-36bf-8ea6-4ed9f65fec5b | -13.07683 | -49.24652 | 2025-06-06 04:17:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a47b7012-c181-3d93-89c3-3cfaa1584b64 | -11.53485 | -56.45073 | 2025-06-06 04:17:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7df4de2-83de-31bc-9f30-2b17610f8de3 | -9.52456 | -54.77619 | 2025-06-06 04:17:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 246edb59-f4fe-3d2b-9f33-d8b4db8e4723 | -14.23402 | -45.49087 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76b885ff-a619-3f0f-869e-9cedfbe9ce74 | -13.48421 | -44.03687 | 2025-06-06 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e474e682-46ef-3973-9ff8-34db3dac400c | -14.02534 | -55.13595 | 2025-06-06 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c077b0b0-7562-3dc8-bb0b-73c867b2ff57 | -14.22959 | -45.49743 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbd4769c-d7fb-3303-bfc7-78e3b39c4a6e | -10.49064 | -53.65974 | 2025-06-06 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9afcf019-6ee6-3008-909d-d547b8b2ecda | -14.03722 | -55.13448 | 2025-06-06 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88b7a248-f760-3080-8464-3aecbf5aa245 | -14.49753 | -43.81006 | 2025-06-06 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e4543d1-a801-3f34-aae5-dd16182e540a | -11.92641 | -54.81583 | 2025-06-06 04:17:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 92090ce0-7ed9-3cd6-af31-e6c4c5c090e6 | -13.71412 | -57.48199 | 2025-06-06 04:17:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b90ed6ef-89ef-34db-b516-a8bf294d7cfd | -15.14334 | -45.50746 | 2025-06-06 04:17:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab1e759e-6775-37a9-9c90-1182eced0858 | -12.82305 | -47.368 | 2025-06-06 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 644c8760-8183-379a-94dd-a7212fdd466e | -11.13582 | -54.22129 | 2025-06-06 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e9d9a28-86c4-3e0e-88e2-25bcc8b9010f | -12.05518 | -47.32976 | 2025-06-06 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4982cc44-8218-3c5b-be03-4bf3e2a1235f | -12.53369 | -58.35411 | 2025-06-06 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0690dec9-457e-3d4f-ba4d-b4c3549434b0 | -12.66854 | -58.22446 | 2025-06-06 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f13624dc-d43f-3f4a-97b3-f4036f355367 | -11.11398 | -54.66134 | 2025-06-06 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3deb539a-ae88-366d-af47-515b49954427 | -11.91996 | -54.81875 | 2025-06-06 04:17:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e81b052b-882c-3661-9dbe-f68223e97bdb | -14.23015 | -45.49387 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cd5ba32-c800-36b9-9242-61516747ebe5 | -10.99354 | -49.01913 | 2025-06-06 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f53c9a14-b818-362f-b4b9-320882d96e0f | -15.0808 | -48.94474 | 2025-06-06 04:17:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12f64c30-7b56-36b9-8ef8-d8d3c52ca308 | -13.51578 | -56.56387 | 2025-06-06 04:17:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f4cbecb4-0921-302a-b63a-8aa08f6f73fc | -14.22685 | -45.49332 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1c52f27-3795-3b69-bf21-3ccc334fd38b | -16.46932 | -45.01078 | 2025-06-06 04:17:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eac76610-2ea4-3573-9b71-76b1dfa84bbe | -11.53162 | -56.451 | 2025-06-06 04:17:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c530c5a4-c6ed-3dcd-b802-5e54c63e25db | -13.99429 | -45.24018 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a71d5ca-a0a0-3f1c-a09d-0764a6b27fa0 | -17.93653 | -48.92436 | 2025-06-06 04:17:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 984743ae-af20-3bdf-a923-4db69a624b0c | -22.90104 | -43.75365 | 2025-06-06 04:17:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76cbe9eb-8030-390e-8080-067d4119d963 | -12.66175 | -58.2228 | 2025-06-06 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00a96999-e3e1-3ac6-90c3-ac28fcf0fbba | -11.54007 | -56.4572 | 2025-06-06 04:17:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58bb16d6-817e-3f58-bebe-d1453fa6409c | -14.73325 | -45.08656 | 2025-06-06 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 561c7769-84df-3b6e-83fa-f418cde6f2fb | -17.26681 | -43.63644 | 2025-06-06 04:17:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39afaf4d-d9f7-316a-8f52-7b98d6b8f7ed | -11.71434 | -56.45258 | 2025-06-06 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d4c0eda-1798-3681-9175-6396c5cf36db | -17.09514 | -43.80562 | 2025-06-06 04:17:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 455e8671-8496-31c9-a80b-476f58c66bf5 | -11.53377 | -56.45595 | 2025-06-06 04:17:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4764b30-17e5-3698-bfd6-3d4e1f6a97e4 | -14.01021 | -45.27176 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b5ca479-bcdf-3468-8803-e416a5813665 | -14.28962 | -47.98467 | 2025-06-06 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8050d3ca-20e3-3533-a540-c8f2a7572787 | -14.12351 | -44.83017 | 2025-06-06 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7da8ce28-bdeb-31d6-a0c6-7e9fbdd2cf48 | -13.52291 | -56.56027 | 2025-06-06 04:17:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d5cf5be-f166-33e6-a592-4743f916092b | -10.07527 | -52.75156 | 2025-06-06 04:17:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91308f44-0865-3b02-94c3-a6db61fb5f22 | -15.00472 | -56.06429 | 2025-06-06 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08d73d58-1f53-3b9a-b2dc-9272f59fea0a | -11.13613 | -53.94889 | 2025-06-06 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a00ba1da-ed34-3c2c-be98-06c5447099c9 | -13.5721 | -44.26181 | 2025-06-06 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27038f24-4f3b-3d97-92a0-9daff51e5546 | -13.52094 | -56.56979 | 2025-06-06 04:17:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ebd0c3d8-59e8-3da3-b848-7e3f9f2612f2 | -11.53793 | -56.45216 | 2025-06-06 04:17:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df4ad0a2-8815-3894-9227-58886da58048 | -14.73819 | -45.09829 | 2025-06-06 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06224e8c-661e-3b55-9a3d-5154f2ca0fc8 | -13.93366 | -47.1857 | 2025-06-06 04:17:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0f42d72-c8c3-362a-bc9f-6ce9308dc0e9 | -12.15908 | -43.20668 | 2025-06-06 04:17:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3ba7f342-cbd9-3878-bb48-b8a0a62f8ce8 | -17.60111 | -48.41756 | 2025-06-06 04:17:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 531ac317-f8ee-3046-9855-80b56e451159 | -12.26614 | -55.07901 | 2025-06-06 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7fa43e2-bb8b-3679-9c26-ad90e21fd006 | -12.26696 | -55.07491 | 2025-06-06 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cbf2b52-1813-3ff1-9f27-6dc4b56e5d3a | -12.94702 | -46.53896 | 2025-06-06 04:17:00 | NOAA-21 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 54dbb3c5-3200-3e35-b3f1-0908045ef039 | -11.53688 | -56.45746 | 2025-06-06 04:17:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87913b9b-8b4b-35e3-9344-e63d1b02aac9 | -14.73874 | -45.09474 | 2025-06-06 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a69dfe83-8de1-3515-8317-301fdfdc3fe7 | -12.42649 | -47.1962 | 2025-06-06 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README6.md)
