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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d832c0e-6942-3bfb-8e83-73cc2a089ea0 | -7.27415 | -43.38637 | 2024-10-01 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 447011b0-6cb5-35e3-bb3f-776d322a4591 | -6.70184 | -43.04657 | 2024-10-01 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ee2851af-0ecc-3cea-bea5-2bcbb88ab2f6 | -6.70076 | -43.05236 | 2024-10-01 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 35bd6c02-55b3-37b7-b385-074927c34274 | -6.69527 | -43.04536 | 2024-10-01 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d9f3e09b-e2ab-33d0-9956-36b1c793ed4c | -6.69419 | -43.05111 | 2024-10-01 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a97e65e4-4ffa-3ed6-8827-aa090b56afa6 | -6.68524 | -43.54563 | 2024-10-01 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e52f9858-e2ad-3cee-a5d7-4dfa225a79c1 | -6.54373 | -43.0378 | 2024-10-01 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 97112dde-ebd5-3fe9-a71d-9476a6da966e | -6.5427 | -43.04343 | 2024-10-01 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cc3ee88f-f0cf-30c4-8f55-8e55b4d9674f | -6.54182 | -43.03852 | 2024-10-01 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| b48930ab-bb99-3059-83b5-b617fc1f8b1d | -6.54075 | -43.04414 | 2024-10-01 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| af53f8ad-58fe-34f6-a13c-043d71a13855 | -6.53711 | -43.03679 | 2024-10-01 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 18ca825d-037e-3b08-a7bc-471e3bca4ab1 | -6.53607 | -43.04244 | 2024-10-01 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8b8b9a22-2b10-3e7f-840a-efdba1700c8c | -6.5063 | -43.63169 | 2024-10-01 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ff126ab7-7b99-39a5-8d07-2870bf842030 | -5.89085 | -43.72537 | 2024-10-01 03:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c07122fa-d52a-3500-8275-e4a50f08e918 | -5.89008 | -43.72588 | 2024-10-01 03:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 168082ab-6cfe-352f-8e59-fd1990fe8013 | -5.88512 | -43.71754 | 2024-10-01 03:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 34b18b85-94de-3da1-aa62-68c533ed694a | -5.88438 | -43.71814 | 2024-10-01 03:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 581a6962-ef84-35d1-995b-ff11c723364a | -5.8839 | -43.72424 | 2024-10-01 03:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 878f96a3-1eeb-363a-8982-130688864281 | -6.2518 | -44.14792 | 2024-10-01 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1247a65e-888a-3e6e-8e8d-00c8ce3b4f94 | -6.25047 | -44.15486 | 2024-10-01 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 18f7386d-c143-310b-a010-ea27a6fbea47 | -6.24819 | -44.14322 | 2024-10-01 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c3d73236-a8f0-3671-acdd-180e924dcae2 | -6.24688 | -44.15033 | 2024-10-01 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| d5545965-067a-3ded-ac2b-11d49684b611 | -6.24602 | -44.13995 | 2024-10-01 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 11b98371-c134-3f25-bc63-018dc60a27f3 | -6.24473 | -44.1467 | 2024-10-01 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 36319103-cd0f-329e-af5b-f4c6ac4977dc | -6.24227 | -44.1358 | 2024-10-01 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d3ac1b3e-cee9-3966-b2d3-94e0a66f8b4c | -6.24105 | -44.14239 | 2024-10-01 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5b2cf6ae-8eb0-39d7-a9a8-bae1fd81a544 | -6.23884 | -44.13937 | 2024-10-01 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d321fdd1-7b7b-3a0b-84d0-d0ce2a25d4ea | -7.81199 | -44.19181 | 2024-10-01 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2070f8e6-7902-329b-b217-260770e98b19 | -7.81075 | -44.19828 | 2024-10-01 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8ef65c2-3627-39ed-ba41-875a98b9be37 | -8.53129 | -44.70906 | 2024-10-01 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a33780d6-33eb-3364-9d1d-266bfc86d37a | -8.52851 | -44.72311 | 2024-10-01 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8fc5bbe1-c715-3a0e-90c4-7de8bfff8643 | -8.52423 | -44.70794 | 2024-10-01 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a215063-8c02-381c-900e-5557ede487ec | -6.0916 | -35.11024 | 2024-10-01 03:23:00 | NOAA-21 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 8e8c52fa-5b56-343e-83eb-e607293b4b72 | -7.53382 | -35.20801 | 2024-10-01 03:23:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 04624c76-9978-3ec6-a3ef-49eb61a20bf2 | -7.33524 | -35.18974 | 2024-10-01 03:23:00 | NOAA-21 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4bc6264f-b4ad-3b95-a84d-62139a7e1a18 | -5.2627 | -36.19105 | 2024-10-01 03:23:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b8524bb2-daa5-3a1e-b186-875e8be2afbd | -5.25839 | -36.19035 | 2024-10-01 03:23:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 56f9efaf-7c6d-3b14-b029-59f411bf483c | -5.10235 | -37.66759 | 2024-10-01 03:23:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 86eab184-96d9-39dd-9235-d4684ce4697d | -7.07465 | -39.14384 | 2024-10-01 03:23:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 112f974d-6474-3411-b61a-f3b483011a1d | -7.07409 | -39.14697 | 2024-10-01 03:23:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e2bbdbd4-2faf-3786-ad80-5d3d334bdac7 | -7.06955 | -39.14292 | 2024-10-01 03:23:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f9d01a24-62bd-3ed5-907c-f95a98ffe95b | -6.79255 | -40.14254 | 2024-10-01 03:23:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4d4ef9d0-f91e-3b1c-a24b-a15921f54e14 | -9.25724 | -40.81882 | 2024-10-01 03:23:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f889c795-6f8c-3ab2-ab7e-80204534b2d0 | -9.25106 | -40.82145 | 2024-10-01 03:23:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 808ca011-3ec8-3e87-a6e9-faf3c26c7f1a | -9.25036 | -40.82514 | 2024-10-01 03:23:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a573718d-9bd8-3ebf-b5b2-afd9e4d8a211 | -9.24967 | -40.82883 | 2024-10-01 03:23:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 86612c5f-8afd-3edd-aa36-1020f1c6957c | -9.01862 | -40.56918 | 2024-10-01 03:23:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9a9c414b-1ae4-3b20-ad4e-bb1fcb34a338 | -9.01798 | -40.57268 | 2024-10-01 03:23:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5ed0ea07-54ce-3dd4-8e1e-0011bfe621a3 | -9.56754 | -40.34902 | 2024-10-01 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 55d76aeb-b874-3a6b-a8c4-205cfa5de6f1 | -9.46727 | -40.39441 | 2024-10-01 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ab7b6aec-290c-350d-98b2-5beb1a543fe4 | -17.72585 | -42.34951 | 2024-10-01 03:25:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24aafefc-5a57-3de4-b50c-70d3618754df | -17.7252 | -42.34903 | 2024-10-01 03:25:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cf19245-de2f-393a-8ead-79d87bff8622 | -17.72456 | -42.3522 | 2024-10-01 03:25:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed3619ab-5369-3440-8285-b8e3070a4cc2 | -11.56111 | -42.18293 | 2024-10-01 03:25:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1c11971a-08ea-30f4-921f-43bf23db6e4d | -11.56073 | -42.18175 | 2024-10-01 03:25:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 486af8e3-8abf-3f20-88a5-d58b5aece5cd | -16.34769 | -43.69798 | 2024-10-01 03:25:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b8d3325-6232-3107-91b6-c80855921ab1 | -17.28248 | -43.1926 | 2024-10-01 03:25:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85c328ec-db94-34dd-9a5e-ededda32c3f6 | -17.28169 | -43.19638 | 2024-10-01 03:25:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17bbd44d-bf70-3a1f-b5d4-7ab8ca1d736b | -17.28081 | -43.20054 | 2024-10-01 03:25:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a1b8d73-2cf4-3ba0-95d3-5ffae3ae703a | -17.25673 | -43.17809 | 2024-10-01 03:25:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 838a020f-0257-3884-8c00-6e0ada505477 | -11.25548 | -43.38111 | 2024-10-01 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d5971ef1-149f-3047-a9a3-2d707015ee15 | -11.25446 | -43.38618 | 2024-10-01 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 01d78c4c-8b0d-3afd-840a-588df4944276 | -11.25343 | -43.39125 | 2024-10-01 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6b80be18-97ce-3138-b970-c4a36d6474b2 | -11.24926 | -43.37989 | 2024-10-01 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 478ea506-87bc-3d31-aa58-9fb18b5d7680 | -11.24823 | -43.38494 | 2024-10-01 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| aca66843-dde4-3ab0-9749-4e2ea1e35541 | -11.24721 | -43.39 | 2024-10-01 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 7cc59ef2-3ef4-396f-9870-99c1b2759c11 | -13.45021 | -43.77751 | 2024-10-01 03:25:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 50a32178-ecd6-36ec-931f-aecf3e48f3b8 | -14.49976 | -45.0745 | 2024-10-01 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 23047a5e-d057-340b-a62b-d80220147d9e | -14.49237 | -45.23567 | 2024-10-01 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6534223c-f674-319b-ac37-ab6315d8ba73 | -14.4913 | -45.23347 | 2024-10-01 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4251740-5a6a-3b39-a84f-55a998bad6bb | -14.48997 | -45.23945 | 2024-10-01 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f1d9d2e-c6ce-3f7b-b91e-ec86fd4bee90 | -14.48468 | -45.23237 | 2024-10-01 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4ef44ec-ef4c-3fce-ad0c-3eaa08e0ad38 | -10.87236 | -44.79853 | 2024-10-01 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65b55bce-640b-3051-a59e-e2960a66698a | -10.87107 | -44.80481 | 2024-10-01 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a7472f06-bd38-3a1c-b975-e06eeaf53b07 | -10.86556 | -44.79717 | 2024-10-01 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b950359-2544-3d5b-b5b5-493459143212 | -10.85875 | -44.79589 | 2024-10-01 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0cfd444-dcd3-3d84-8c6b-2502fb34a258 | -12.07135 | -44.95905 | 2024-10-01 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2a4857c8-5604-3ac6-b63e-90b7ab3e05c6 | -12.06663 | -44.95928 | 2024-10-01 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3843d211-1f58-3c00-a2be-1c8ef8636be7 | -11.26439 | -45.65471 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e220d7a4-58e5-30eb-a7c9-1196ebedc571 | -11.26281 | -45.66206 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2879299f-8792-35ab-a42b-ea5b8d0622e0 | -11.26116 | -45.6697 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c5f0477d-a597-36bc-a7bc-91f671110a42 | -11.26068 | -45.65423 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1f00ac70-6afc-3af2-8022-8d14dfc77e63 | -11.25911 | -45.66173 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7070d291-b870-37ae-8c3c-28e424d0bce9 | -11.25749 | -45.66949 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8cc2e39f-17c0-3875-a085-eff9840296e4 | -11.14105 | -45.6776 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 887af574-cbcf-3349-b90c-f96a27ab887f | -11.13957 | -45.68469 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5efc7450-30b3-359c-9bae-978960ae38fc | -11.12423 | -45.65188 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3fa8f98d-94b8-37ff-8b78-9b653cadd2e9 | -11.12157 | -45.62936 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 61a3e0d8-4688-30c0-b91a-bdcdaf0c4ece | -11.12012 | -45.63627 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 0150113b-e075-3737-b66f-5708d71adf47 | -11.11865 | -45.64325 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a9046850-6619-39a7-af10-bfaf154c561e | -11.11717 | -45.65028 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3e2399d2-677e-37b3-b3bc-1f3e0e9553b5 | -11.11675 | -45.63483 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3cf6c901-78b0-3588-92b0-b2897e35cca0 | -11.11532 | -45.64182 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 627e335d-ac0d-3172-82ea-929996ea0eb2 | -11.1111 | -45.67904 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b0c78e91-5feb-34ba-b9ff-0ecfabdaf199 | -11.10944 | -45.67058 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 200e3460-3e6a-35ad-a091-5161871bb3d7 | -11.10548 | -45.67056 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 48298795-e4a4-3d64-b779-1c04adbe9875 | -11.10391 | -45.678 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c188b948-f5dc-3ebb-a822-956b8c46c8ae | -11.10228 | -45.6694 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9f1fa994-1177-39df-99f0-ed3544f8574e | -11.0983 | -45.66946 | 2024-10-01 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 58af35aa-7483-356f-bdb0-70ff2484f04e | -14.43982 | -45.71798 | 2024-10-01 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README36.md)
