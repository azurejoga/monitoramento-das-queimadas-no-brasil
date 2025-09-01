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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6486e3f5-178c-3283-9521-d73631e70003 | -11.8143 | -46.41528 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 14973ac5-d8a9-3987-be9c-4f147e86986f | -8.84257 | -47.50902 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ab5e3af-25ef-3d53-abb3-121c77f24b13 | -12.57022 | -44.79342 | 2025-09-01 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8ed50405-50a6-3e10-bfda-b0d813701266 | -9.6407 | -46.60274 | 2025-09-01 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d530186-98d9-3717-a85f-ed47486adc43 | -8.8416 | -47.51403 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b83ffa79-2357-35ed-9a42-f9d79a20ce2e | -13.37287 | -46.31826 | 2025-09-01 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a52396c8-7e60-3b37-87a9-c8543aec8085 | -11.89779 | -46.69387 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 862c6451-dcff-34c8-8c8d-5c046ab0f26f | -7.62659 | -44.03465 | 2025-09-01 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7af6f00c-47db-3cad-b417-cbe02e734e4a | -14.2347 | -48.05427 | 2025-09-01 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc3c1968-52e9-3ec0-a76a-bc7f938e0eb6 | -13.38083 | -46.95218 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57ce0532-1c55-35d2-9914-f35da812102b | -11.48578 | -46.81546 | 2025-09-01 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e055d3d7-1f23-3bf3-90e9-8b25b292c110 | -9.23633 | -47.08124 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90afb40d-9e88-3c36-b481-1b7ce0f0bfda | -12.23059 | -50.15969 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec8139db-43ed-39cf-82a0-a206715c0c6f | -11.03485 | -47.06262 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8561ea8a-e440-39e8-915e-1f4cea4c2f0b | -11.03563 | -45.14895 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20d4ce79-7deb-338e-8600-bbc3ce0bbd5c | -14.04797 | -44.56339 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bae52714-2862-343f-b3f7-9ae1021909cb | -11.48656 | -46.81144 | 2025-09-01 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4438e9c9-1600-3fa3-a8f9-3a6aa06b4de7 | -13.68368 | -46.92212 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 851c665a-869a-38c5-a12e-6f131edcdc29 | -12.80391 | -48.08404 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d44491d3-30ad-37b6-a134-b89060d6d329 | -13.38102 | -46.9528 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 37969f54-6ee3-36b7-b2dc-60d073d195f2 | -11.90442 | -46.68222 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63550078-724d-3f45-bdc6-52717210bc6a | -8.84449 | -47.50452 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a2be3145-5b50-385a-948a-9d3dfc4cf36f | -11.28603 | -44.91671 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75a791a2-981e-3f46-97a3-77274b0bca33 | -8.70467 | -47.86838 | 2025-09-01 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 557b6035-f3ff-3870-aed4-2dd120aaa426 | -13.69454 | -46.92683 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| caa89cdd-71c4-30bb-84c2-b2d15420e8ac | -14.94063 | -40.675 | 2025-09-01 03:45:00 | NOAA-21 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| da9f336a-adc2-3e9f-956b-00e191e007b9 | -11.90517 | -46.67844 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4704cb1-ab3e-3261-9d08-188b713a52f1 | -11.20675 | -45.0396 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88c4ec0e-c079-3d9a-b7b7-530071fc8865 | -12.96995 | -48.1179 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3bacde7-119a-3968-afdd-48d187149d9f | -7.87871 | -46.9813 | 2025-09-01 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac867918-780b-386c-bac8-267f372f2308 | -12.30674 | -45.67892 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d1c03cfb-5dc3-34a1-9b50-152cf697e0b2 | -12.39036 | -46.47749 | 2025-09-01 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d340f42f-7ecd-3706-8cae-187ed09ab45f | -7.97798 | -46.41896 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 95874163-e137-361c-b17b-daa0f6144b34 | -14.04526 | -44.55238 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fcd0053d-a10c-32c2-b394-47d3af0f474b | -11.37171 | -43.59512 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 171902e8-074c-3b00-9cd4-e1e0a057d547 | -11.36999 | -43.60468 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50b113e3-ba28-3436-92d1-4b6331a5286f | -9.57952 | -46.00599 | 2025-09-01 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44295698-1679-34db-8b83-d232e72afa0a | -8.8454 | -47.49965 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3dfdf7cc-b0a1-34f4-ba6c-a556f25eb8c0 | -8.46474 | -43.62657 | 2025-09-01 03:45:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc476ad8-1edc-3ddb-aa56-260e878ba471 | -11.89231 | -46.69231 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f2b988e-374c-3c2d-a751-d7e9c6ff6b5f | -12.56754 | -48.22207 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 346820f7-80f5-3f03-9de1-b7547dd38393 | -11.04686 | -46.96951 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99608f71-49fd-3e2d-8f06-64dbaf8b7566 | -11.89354 | -46.73702 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 06d2ff67-c78c-3ae0-b483-f39fdfbeadff | -8.82573 | -47.83187 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efe4de4d-a5b1-368c-916a-1002f3f16078 | -11.89363 | -46.74594 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68858008-6501-3fee-875c-31d22f5c36a8 | -12.95928 | -48.10928 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d2e5b6d-403c-34ee-b067-d8c17c8de800 | -7.88731 | -47.00246 | 2025-09-01 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5732e5b-4ee7-3d09-b608-bd43c6ca86a1 | -13.1625 | -45.27921 | 2025-09-01 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 059be9c8-b55b-3e69-b1b0-28cbdffbe6b8 | -12.33155 | -45.72388 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26aa704b-a716-32e8-bef0-3362feb5f1b3 | -13.32462 | -43.59395 | 2025-09-01 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23bfe412-fcca-3ec1-acb1-dd95e0a47440 | -7.39556 | -45.93625 | 2025-09-01 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 257ee1de-a01d-3777-98d5-afd5474a49c0 | -11.02497 | -47.05164 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71274c1c-6825-3ce5-9e55-dedba2003dca | -7.50288 | -45.83966 | 2025-09-01 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 27bf615d-d64e-3ee9-a93e-0d03a7248331 | -8.84447 | -47.49915 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88386584-d123-38fe-bab1-7988d13229eb | -11.04075 | -45.14987 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| ee7c14c3-e4c9-3791-8b31-36c0cd89bb6d | -9.15819 | -45.21814 | 2025-09-01 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6912f284-5daf-3091-9d02-7a50a1d26fa7 | -14.04794 | -44.57555 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 13d92e6a-7b34-3335-96cd-cc3b82fb8b9d | -12.38954 | -46.4756 | 2025-09-01 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03f4101c-a6b5-3428-9fab-bc2d5112abf8 | -13.49301 | -46.9338 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae521192-2eb5-3e00-b98e-b4c52efbff7d | -13.48579 | -46.99798 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b65931b0-a7c8-3772-a696-3b711a9ab342 | -12.60168 | -48.20913 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9289d916-c9af-31e0-8962-20c704939600 | -12.3085 | -45.67649 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6b13b02e-2849-3527-8361-d379b465b4b3 | -14.0431 | -44.58865 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2dffe28e-823e-3d26-a9e7-3a4dff837971 | -8.88614 | -47.21239 | 2025-09-01 03:45:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| be5e8247-99ec-3d36-ab9f-6e55f0881734 | -11.04984 | -46.92326 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c19195c8-b2dd-3793-9fde-15a75826d1e5 | -11.37742 | -43.61611 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71b0e41b-51ef-377f-b2a7-de302c1a04ff | -12.56145 | -48.22105 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 87a7ba00-f63a-3ddc-b199-05493f7aba80 | -13.48774 | -46.93222 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b7435ad-000d-330b-902b-cc97970744b1 | -13.37084 | -46.94624 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c5b3f157-cc2b-3f7f-94c6-c21dc2ff18e6 | -12.56946 | -48.21278 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1206ef99-f219-3e3b-948e-037ab1b8c8d8 | -9.63881 | -46.60988 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 54673684-e8b6-3ac6-88e0-9672d6858c6f | -13.50927 | -46.99534 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77da15c7-67dd-360d-916e-bc1006de4c3e | -8.81842 | -47.83596 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db2ae6b0-2b8f-3fc3-a7bc-d48b88c9c481 | -11.37508 | -43.57632 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3ba0df6e-cb27-35ab-bea6-9a05a3d92447 | -8.4986 | -44.74434 | 2025-09-01 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19ae7eca-a82a-3698-a1d7-7474d4dbbb69 | -12.87004 | -48.07672 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 04a05f07-96bd-3a2f-917c-669aa1fd0d21 | -12.77806 | -48.08892 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 18965a93-de87-343c-9d14-822e1f8a947a | -13.69032 | -46.91721 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdfa752e-21f1-3947-b8fe-369330532498 | -9.642 | -47.80572 | 2025-09-01 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0260cde0-c2dc-3f44-8237-a542bf3c2579 | -11.48809 | -46.80362 | 2025-09-01 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52c2b86e-be3f-3e67-8822-b244be3276e9 | -8.19591 | -46.78455 | 2025-09-01 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 65d31ccc-020b-3c62-aee2-406f9dbdf78b | -9.23964 | -47.08198 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e1a4a59-e28c-3428-b143-ae8ded18fad7 | -11.38029 | -43.6266 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 28263cd9-1459-338d-876d-a8c39aa9bf4d | -12.5681 | -48.2145 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 994a5615-479c-3a41-be3e-822268fd915f | -12.56109 | -48.21811 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 21a9f57c-9f53-3fef-b9a0-609f1b871f96 | -11.33336 | -43.51985 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fad0fbf-5397-3e18-b3fe-e2472eed7bc8 | -11.32289 | -43.47153 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88b8872a-0398-3758-bae8-87f4c46c7f3c | -12.56717 | -48.21919 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| aec116cb-6328-32c5-82f4-6d9cab79ee20 | -12.57405 | -44.79991 | 2025-09-01 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5489cfa-043e-3652-b288-78d12fdb4afa | -11.81351 | -46.41939 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 52261b5c-a996-3b65-9dbb-0d9aeca77603 | -7.97723 | -46.423 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 778705de-f326-398d-9b3c-fe0e17b1f2df | -7.63165 | -44.03542 | 2025-09-01 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44c68a31-e537-310f-ab2e-df5800beb9cc | -11.48314 | -46.79892 | 2025-09-01 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e73f1717-fa54-314e-915d-616959cde960 | -8.20041 | -46.77784 | 2025-09-01 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 8a3b9232-9481-3407-8fed-f696e81e8426 | -14.04888 | -44.57049 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5ebc4b59-9f8c-3018-9403-3ec7417682de | -9.67034 | -47.05029 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0dabd64-f330-366c-9af1-f0563400f3aa | -11.961 | -45.84674 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31e5b406-9f1d-30c8-a9a7-51f0cc068882 | -8.84629 | -47.49485 | 2025-09-01 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b00809a2-b13f-3ccf-a325-48aa60d93136 | -12.3911 | -46.47377 | 2025-09-01 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7384696f-ac4c-381f-ac50-0066398d4432 | -9.63543 | -47.79717 | 2025-09-01 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README19.md)
