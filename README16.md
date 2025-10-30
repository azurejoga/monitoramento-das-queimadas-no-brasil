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
| 66411a15-d065-36fb-950b-4eda85a436c5 | -6.14211 | -41.69208 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 13aa39c2-767f-36cb-80c2-ef7ae785e744 | -10.51059 | -44.79255 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6145995b-f648-38c4-98bd-07c0715bd304 | -6.02206 | -41.97379 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| baa3623a-4c0e-393d-a780-44deef87a592 | -8.92514 | -37.28354 | 2025-10-30 03:36:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a9535417-932c-3b71-8110-8db8c0362e9f | -10.85676 | -47.87477 | 2025-10-30 03:36:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e86debfe-145d-35bc-ad94-4fbde6cb5611 | -5.40896 | -46.01246 | 2025-10-30 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0d87ed6d-7545-3c75-9268-33717d640734 | -6.08997 | -41.78334 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0d09c8c9-c67e-3308-8806-b2e9b5ba40f9 | -7.96049 | -46.72139 | 2025-10-30 03:36:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 62867f23-363c-3939-bf77-c9ecb92ea54f | -6.13866 | -41.59349 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1853c7a6-9984-354c-9538-bcc1c835d335 | -10.26473 | -44.57646 | 2025-10-30 03:36:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a0f18620-4238-3ec1-aff7-c9b89da10d28 | -7.39185 | -42.46629 | 2025-10-30 03:36:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cd75d27c-4fad-3c02-a662-edddd794c711 | -6.12788 | -41.8648 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| af2498d9-f474-3564-aa56-25704ab44bca | -9.91118 | -47.91523 | 2025-10-30 03:36:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 69f0b4c9-d785-3b2c-a890-8acd359cb2b3 | -11.63806 | -44.04653 | 2025-10-30 03:36:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 624aa1fa-78f5-3be4-9e00-7266251b7ec6 | -6.2171 | -41.82344 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0fc106b4-8bda-3eb9-a778-0fc960b175a5 | -11.71879 | -41.66023 | 2025-10-30 03:36:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| aeabf0ad-8447-3769-844d-80aaa24ec7c4 | -9.81346 | -47.58448 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a266238d-7d83-31e9-bb4e-085855dafd0c | -7.14099 | -40.46062 | 2025-10-30 03:36:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 29f7d42b-c306-3b83-9f8c-1449f4133c40 | -8.49948 | -40.95697 | 2025-10-30 03:36:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0f4b778f-e033-3c4d-9335-79b068ca72cc | -7.30243 | -45.6665 | 2025-10-30 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e6416493-ecc4-3c42-ae63-f74b39f4f0b9 | -6.12405 | -41.70691 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8a02c14f-2c84-306f-88cd-7ab7992a8784 | -7.34396 | -39.33386 | 2025-10-30 03:36:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d070819a-df5e-3479-a244-139155f64537 | -6.05767 | -44.15426 | 2025-10-30 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cfd264e9-5751-378e-bd3f-6ce6455acae2 | -8.16411 | -37.61638 | 2025-10-30 03:36:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cf704225-0104-33d0-ba03-a439646a5e47 | -7.50738 | -44.07574 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4208d18-7835-3a07-81be-bbe6a2d5de12 | -8.3217 | -45.3818 | 2025-10-30 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a534ce60-7e23-306f-ae4d-853064681ca8 | -8.03343 | -42.51144 | 2025-10-30 03:36:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74ce37ba-3e13-3139-bbb5-040a3bebc34b | -7.61837 | -43.57445 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5b66649-c5c0-3e70-bb7b-4d5b9ee41a3a | -9.49949 | -40.37775 | 2025-10-30 03:36:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 618da98a-f409-330a-a545-916ede6ac617 | -5.72363 | -44.4063 | 2025-10-30 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 55227103-9dac-3685-9f52-480ab8c72549 | -10.27668 | -44.5751 | 2025-10-30 03:36:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 19f8449d-ef1b-34bc-b7ce-ce2bc7b5df03 | -5.60969 | -47.12241 | 2025-10-30 03:36:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9ed0cfe4-9de8-3aaf-a521-b6b72f943395 | -10.86546 | -47.61798 | 2025-10-30 03:36:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3798aa3-5298-3714-a196-85670fb997d7 | -7.61561 | -43.58953 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 29456204-272d-3252-bbc8-27adb08501b4 | -6.95023 | -40.91646 | 2025-10-30 03:36:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 25a96f61-cd01-314e-b63a-ec03ac57225d | -8.33151 | -47.92435 | 2025-10-30 03:36:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 05706256-eb2e-35a3-8cb1-ca437b5f54ff | -7.62407 | -43.60594 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f4506d31-fdac-38e6-841f-edc3ad0161ef | -10.27818 | -44.56718 | 2025-10-30 03:36:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34e5ff0c-2cf6-389e-aa87-42c18eb3161d | -7.16537 | -38.53341 | 2025-10-30 03:36:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b0590e50-851d-36d2-9f97-d1ca993c3bf4 | -8.40792 | -39.95665 | 2025-10-30 03:36:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 696fe0ec-1ea9-3966-a3ff-a6da7365ef54 | -7.95682 | -46.7229 | 2025-10-30 03:36:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7939a16e-67bf-3ce2-bc76-3c40f02135db | -11.17348 | -45.22385 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c88411d7-7531-3fc4-b5d3-350bcc1c9bec | -7.6638 | -43.91667 | 2025-10-30 03:36:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d8e6829-35ca-3ef5-b6d0-f2e974ad80f7 | -6.13219 | -41.57191 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fad891b7-9ae2-3c55-a389-7d3eb83f3fe3 | -6.11351 | -41.70815 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9bc14036-139d-3a36-bb01-6e256b72a536 | -6.1511 | -41.66988 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0c007a9e-dad3-3e57-b975-645fdf361d26 | -6.12839 | -41.8618 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5ab6e21f-28db-3afb-af10-b427761924df | -7.86963 | -44.22785 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74d2b165-75fc-3138-b93c-966ec72853ab | -6.69726 | -39.69009 | 2025-10-30 03:36:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4e1bf31c-0f4e-3577-a23c-af4e746085e5 | -7.27028 | -46.88358 | 2025-10-30 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 77d58321-d6df-3f74-8e5f-423cee2431db | -5.41242 | -46.01163 | 2025-10-30 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9053d79d-97fd-3f4b-b4c7-3ebbd7c40837 | -6.13242 | -41.86876 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1a67bb68-cf59-3589-857f-5d08a778fbf6 | -7.86386 | -44.22691 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9fde2176-e3df-3667-9870-d57da6c5968a | -7.79847 | -46.41689 | 2025-10-30 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 27e51086-a854-3401-9f96-8fe921542c94 | -6.11201 | -41.7167 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4aea722c-2e30-32ed-83bb-137e992e6fd2 | -6.11042 | -41.72578 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2b4ae1b5-b7a8-301a-a95b-b8b7a958e984 | -7.64815 | -42.24473 | 2025-10-30 03:36:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 36bfd936-7bbb-3062-9346-fb704e407248 | -6.14457 | -41.58898 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b9f83479-c425-3f9f-bafa-b46cf91e404c | -6.02102 | -41.97989 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 14b9e3ca-ec5d-3849-8600-7749a0011fd3 | -10.74924 | -44.74897 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 87e8036a-f6fb-3692-b88f-29d8619a7f18 | -9.84466 | -44.89118 | 2025-10-30 03:36:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c514c27a-28d3-3a38-a69a-d3ae58efff02 | -5.43387 | -45.33468 | 2025-10-30 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 6efc66a1-ed05-3f97-9a73-2901264086a8 | -6.15845 | -41.59753 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 542df176-1089-3e72-a38d-51a5535b9af2 | -7.0756 | -44.9366 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| feb9c5a6-477c-30e6-bc7e-0de29a839203 | -11.16693 | -45.22629 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef98d23e-334b-335b-bb1b-78fbcc97414b | -9.90336 | -47.91417 | 2025-10-30 03:36:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3d995205-e5e9-30f7-87ae-d7006c53f475 | -7.617 | -43.58197 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ac1b994-9774-3b3f-8388-45c5c1010b43 | -7.50255 | -37.20865 | 2025-10-30 03:36:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 866991b7-2173-31af-a526-e47f8e65d08b | -9.50024 | -40.37351 | 2025-10-30 03:36:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| b98cb120-85fe-3337-a469-ce9c648f9d14 | -6.13717 | -41.57267 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cb9fd7c6-5cba-3281-9fbb-0c4580f68997 | -9.89134 | -47.44463 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c5c5364e-94b1-36b2-9740-54c9d81ba0f2 | -6.11304 | -41.71085 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4ace4ae5-f508-3dea-9e9e-a530454cc593 | -7.3406 | -39.71422 | 2025-10-30 03:36:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| c64baf52-6476-3816-b927-36f9aaecfd57 | -8.33008 | -47.93166 | 2025-10-30 03:36:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| cb1910ef-6a40-31c4-a45f-cf1bbbbc7546 | -7.65271 | -42.24847 | 2025-10-30 03:36:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa1198b3-9000-3d3f-a35d-dfa7f5dc12e6 | -6.70774 | -38.2144 | 2025-10-30 03:36:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bae2b730-2d5b-3dcd-a533-4de2e4641722 | -10.43468 | -40.502 | 2025-10-30 03:36:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3bbf6dc4-8df9-3708-92a3-5acfac9ee4b1 | -10.48735 | -45.04473 | 2025-10-30 03:36:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f3c8621f-c393-3127-837b-534f324d0712 | -6.09788 | -42.44353 | 2025-10-30 03:36:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c161f794-814e-3fd5-a7de-38958603272c | -6.69297 | -39.68918 | 2025-10-30 03:36:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e5847d54-e563-3f9a-8fa2-99c1ff3e9dcb | -9.84716 | -47.69607 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| acf92d99-6dde-3ea5-8386-42503e7b3357 | -7.29527 | -45.66977 | 2025-10-30 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eec641f6-3e2c-3f43-8918-ceb086283f71 | -10.04427 | -36.14601 | 2025-10-30 03:36:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 94.2 |
| bdfeccee-615e-36d2-a256-0a0883f95f3d | -7.92271 | -39.71768 | 2025-10-30 03:36:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b0516645-7f9a-33dd-8822-cc38273e04b6 | -7.40044 | -43.93914 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 14ae30ce-0a17-3604-a6ca-3fa3cf4ead59 | -6.69071 | -38.19576 | 2025-10-30 03:36:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 97ba9a42-120d-3c96-a880-e321feca54a1 | -10.35578 | -47.27463 | 2025-10-30 03:36:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6e52c282-d6f7-3e17-a419-e918d1c0947e | -7.38019 | -47.62554 | 2025-10-30 03:36:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bd38da2c-582b-3408-a4b0-3ad51d0d14c1 | -8.90843 | -47.63904 | 2025-10-30 03:36:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 3af289fc-e140-3f90-a525-7fb667433559 | -9.84547 | -44.88683 | 2025-10-30 03:36:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 340c325e-4e63-348e-87de-24adcd0d0d63 | -5.72766 | -44.40855 | 2025-10-30 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47911eab-b969-399f-83b1-535470844ec8 | -10.75724 | -44.73799 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cdde8368-9832-39e7-a482-27e8f8c312a3 | -6.517 | -46.90834 | 2025-10-30 03:36:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 54fece84-58ad-362a-9bfa-900cca92e1f3 | -9.91251 | -47.90847 | 2025-10-30 03:36:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2f825cd4-1980-3f94-9fdd-82176ebeca5b | -6.13417 | -41.67841 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1520e28a-aedd-3194-ad0b-139fd41db360 | -6.88354 | -45.55284 | 2025-10-30 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a6ceba0-da03-35ce-9d6b-5ec13b3bc444 | -6.01641 | -41.97599 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f9f0360f-497c-3671-88b0-b0a6c21433a4 | -13.85483 | -48.49966 | 2025-10-30 03:38:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fa50f4b-d8bf-3e4c-8a28-f7282b2a3f06 | -14.90481 | -43.10141 | 2025-10-30 03:38:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 13caf9a7-627e-392a-a646-213fbdcc704a | -13.61323 | -47.58891 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README17.md)
