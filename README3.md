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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d45adf2c-4d50-322f-aedc-ff0aea883fd6 | -13.08427 | -42.28014 | 2024-10-23 00:43:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 3924d612-03b7-3e08-a88a-0cef61219fdd | -11.8209 | -47.0887 | 2024-10-23 00:43:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 69e5d9f4-53e7-3f2f-9cff-5cb456022630 | -11.81957 | -47.07838 | 2024-10-23 00:43:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ec536a03-86ce-3533-8078-722caf8c17a8 | -11.81823 | -47.06806 | 2024-10-23 00:43:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 1d9a270b-3d11-3adf-8b82-73b046fbcc3f | -11.81497 | -47.08523 | 2024-10-23 00:43:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 7b0c2261-1d70-3563-85e5-be2b07dbcd06 | -11.81358 | -47.07492 | 2024-10-23 00:43:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 730c4225-210d-39eb-a81b-324ff78dd5b6 | -16.77902 | -41.80155 | 2024-10-23 00:43:00 | TERRA_M-M | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 76a6898a-a9e7-3243-b2f8-bc6a1e0d2622 | -16.02269 | -41.18964 | 2024-10-23 00:43:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 8bb929e4-bab1-3d3b-8d00-a8782547e90c | -16.02107 | -41.17893 | 2024-10-23 00:43:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| e9a83055-c714-31a6-8930-3f5c5a24c117 | -15.85179 | -43.8171 | 2024-10-23 00:43:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b7b99980-9b1e-343e-82cd-6cff002989e4 | -15.84552 | -43.50363 | 2024-10-23 00:43:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f55d6803-d8b4-3ed3-91ca-6035ca530468 | -15.84295 | -43.81845 | 2024-10-23 00:43:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 2d7d6256-6628-3d09-946b-01c086f7417c | -15.52582 | -43.13713 | 2024-10-23 00:43:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 3d2d3ce0-81a5-336d-a5c2-89a2c0a48d59 | -15.5169 | -43.13852 | 2024-10-23 00:43:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 8.0 |
| dc290d09-194d-32a9-8dc5-338b3f124fe8 | -15.49927 | -43.80173 | 2024-10-23 00:43:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4d11a5e5-a93e-3406-b6fd-fc3dab93e64d | -13.60216 | -44.00526 | 2024-10-23 00:43:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ad9db028-770c-3c4d-9d8e-b6c2cddbd95e | -13.60089 | -43.99618 | 2024-10-23 00:43:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| f1d93b70-8722-340c-baf3-efac171c8365 | -13.22187 | -50.46944 | 2024-10-23 00:43:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| bec703ed-c374-30d3-b994-93f0608d4798 | -13.10591 | -43.36365 | 2024-10-23 00:43:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bffbd47b-7279-3c2b-aa79-bae7a80aaba0 | -12.87099 | -41.76607 | 2024-10-23 00:43:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 1cabfeee-8ffa-320a-9fa5-b75e1a8ede3a | -12.24846 | -43.42606 | 2024-10-23 00:43:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 579eff1f-aff6-3be7-81d1-ceeb4942d29b | -11.99668 | -43.08482 | 2024-10-23 00:43:00 | TERRA_M-M | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 971ea264-43b5-3c68-9e8e-2dc0cab369d2 | -11.88246 | -43.38175 | 2024-10-23 00:43:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2af702db-6cc2-31c3-be94-67baf96cdbbe | -11.57256 | -48.72445 | 2024-10-23 00:45:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9b9b67c2-03e5-36a8-a26c-07e5f3b56fc6 | -11.56789 | -48.71933 | 2024-10-23 00:45:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b4716ec0-7b51-3f60-a3f5-04dcb176cef8 | -11.47093 | -47.07727 | 2024-10-23 00:45:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 48195baa-7aa1-3d90-93bc-afd3c5700745 | -11.4696 | -47.06716 | 2024-10-23 00:45:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 07a4e320-dd8b-3723-b5dc-b8135bbbcdde | -11.34099 | -54.36232 | 2024-10-23 00:45:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 7cd47f84-02be-3c82-bf66-8acd5a7f20a3 | -11.3322 | -54.35812 | 2024-10-23 00:45:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| b68ddf88-ca4c-3da7-8304-00f5b2cb5bb9 | -11.32076 | -54.32938 | 2024-10-23 00:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| b7c5b260-2ac1-30e6-af07-22b73978532c | -11.03404 | -48.27811 | 2024-10-23 00:45:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 425bcaf6-8683-3f51-9ba7-c60bedeaf178 | -11.02398 | -48.27942 | 2024-10-23 00:45:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 21e092ed-5564-30ae-aa49-66e2ed875686 | -10.93648 | -47.83871 | 2024-10-23 00:45:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bba06590-59dc-3f1b-8c8b-a136aef3d422 | -10.64118 | -47.6876 | 2024-10-23 00:45:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0e9a753f-3538-3565-aa58-8e642c0949cd | -10.37284 | -51.3955 | 2024-10-23 00:45:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 48242690-f8f7-3f11-8fd4-4345ce11a0fa | -10.00708 | -47.46608 | 2024-10-23 00:45:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8d616ca7-f536-360c-b4ff-cf6a9bc154ef | -10.00571 | -47.45588 | 2024-10-23 00:45:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 115c9598-c17b-3745-b304-43694c21de86 | -9.64408 | -43.91014 | 2024-10-23 00:45:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 7ab2ea60-3423-379d-9db7-76f11adcf713 | -9.5204 | -40.35135 | 2024-10-23 00:45:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 98d7241d-6ec0-39ea-ae36-e2a7c4c1966e | -9.17765 | -44.12994 | 2024-10-23 00:45:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3b0add4f-1e1a-36ea-8f07-1d0b28764e3b | -9.14094 | -40.64978 | 2024-10-23 00:45:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 5b679cfe-c8f0-3839-9d18-874ff221a3e7 | -9.14082 | -40.65551 | 2024-10-23 00:45:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 8e34be81-c506-3dba-8e0b-122a73903396 | -7.6087 | -42.33856 | 2024-10-23 00:45:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| b8756819-0340-34d9-bc88-c9b9df2e1d5b | -7.4981 | -42.90889 | 2024-10-23 00:45:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 47e9734b-c63b-3203-bda7-1a9fc8f6d690 | -7.44678 | -43.6266 | 2024-10-23 00:45:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 64647d14-9679-3ec7-a80a-e0a550d3f80d | -6.90058 | -40.83468 | 2024-10-23 00:45:00 | TERRA_M-M | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 30.7 |
| a5347bb3-de83-3d0f-a9d2-0b8d95c2d306 | -6.71684 | -37.51916 | 2024-10-23 00:45:00 | TERRA_M-M | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 22.2 |
| bb914dfa-dabd-36d7-b88b-c43fd262f8bd | -6.71575 | -37.51292 | 2024-10-23 00:45:00 | TERRA_M-M | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 48e0b4e9-e82a-32ef-a97e-fcbc7f8a2afd | -11.13731 | -44.95629 | 2024-10-23 00:45:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7020478b-436b-3b46-ba09-af429c735b6b | -11.12848 | -44.95758 | 2024-10-23 00:45:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4f9ce567-97fd-333b-9434-4888cafba818 | -10.99565 | -45.26302 | 2024-10-23 00:45:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| dd2eceac-b104-3a8f-b579-c3f4a3ead18f | -10.79235 | -44.53112 | 2024-10-23 00:45:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6d04cf94-63ab-3720-85c5-ba97965c7f88 | -10.76046 | -45.0264 | 2024-10-23 00:45:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b2b650c5-e9c5-3c7a-b365-2a74d1b015f5 | -10.75921 | -45.01746 | 2024-10-23 00:45:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fa398ebb-ee32-3fbe-8a89-515113a7010b | -10.72114 | -45.21132 | 2024-10-23 00:45:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c6979391-030d-3c71-bf72-3907c8911125 | -10.7066 | -44.38443 | 2024-10-23 00:45:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e29d8a68-e29d-3175-965d-4f191fc9c732 | -10.6534 | -40.81203 | 2024-10-23 00:45:00 | TERRA_M-M | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 6abe9f3b-8e2f-3e0f-bb64-0d0f284296c1 | -10.60063 | -44.28599 | 2024-10-23 00:45:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| e3f1ff13-60de-3b7c-bb4b-60cd19f18f77 | -10.59935 | -44.27691 | 2024-10-23 00:45:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| fe5867a7-a005-38b4-a1ff-75a818ba3d96 | -10.58413 | -44.29773 | 2024-10-23 00:45:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e5232800-2ce8-39e7-8ca5-7466291b0973 | -10.58285 | -44.28865 | 2024-10-23 00:45:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6f1ca5fd-fa7f-31bd-bca2-60797c2866a2 | -10.44816 | -44.89846 | 2024-10-23 00:45:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 882d8bfa-4475-35c7-820c-6d82f26376a8 | -10.43933 | -44.89975 | 2024-10-23 00:45:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 30dbb83f-f744-380c-a16a-c7e7a58bf45f | -9.55943 | -46.40348 | 2024-10-23 00:45:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 30b67061-38d4-3674-8600-3137ef13045c | -9.50376 | -47.90079 | 2024-10-23 00:45:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2701324f-cef1-32d5-8b7c-7f9e99917a7e | -9.07558 | -47.98963 | 2024-10-23 00:45:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c14c4cbb-de98-315f-aa8c-fe525c995e46 | -8.74421 | -50.06176 | 2024-10-23 00:45:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 371b9889-48e6-3d59-a4ab-cca0d122d72c | -8.73312 | -50.06322 | 2024-10-23 00:45:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3937d368-0c77-31bb-8510-1b69a33b4b06 | -8.51855 | -45.87231 | 2024-10-23 00:45:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c49675c5-25c2-3d80-85cf-b09f20dfb1f4 | -8.51095 | -45.88251 | 2024-10-23 00:45:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 64ccbad6-3740-3b00-8a1c-d625f659937c | -8.50971 | -45.87361 | 2024-10-23 00:45:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f5fe4ebe-e951-3e0a-84a5-091fb1bcceed | -1.388 | -51.9867 | 2024-10-23 00:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 8ac515e5-2d10-3d82-a968-f48195b8e0ad | -2.5224 | -54.1193 | 2024-10-23 00:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 6958ff02-7695-3989-866b-2f1f50e4fa64 | -2.5225 | -54.0992 | 2024-10-23 00:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 5838e40a-c6aa-3437-9d69-1b416586fcf4 | -2.7589 | -49.3072 | 2024-10-23 00:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d1b41609-70f2-3583-9b56-80c5e11e3d93 | -2.7614 | -54.0338 | 2024-10-23 00:45:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 31149f38-9c2b-38ab-ad0d-67803bf60b3d | -3.0917 | -54.1666 | 2024-10-23 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 91fe967b-3b0f-3d52-b4b4-4d79d9dc8be5 | -3.1101 | -54.1661 | 2024-10-23 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 316a2fd1-8136-38a3-bc3e-aab3f6f1f56a | -3.1102 | -54.146 | 2024-10-23 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| e7b86804-fc2a-331d-8258-eed939227452 | -3.2542 | -50.1799 | 2024-10-23 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 06f7adba-c3f7-3386-ac1f-eead11ad96ae | -3.5307 | -54.7356 | 2024-10-23 00:45:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f0d66228-17f8-335e-aac8-d39811ffa4a0 | -3.549 | -54.7551 | 2024-10-23 00:45:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 9e20e306-e614-31ea-9f78-e4121755db63 | -3.5491 | -54.7351 | 2024-10-23 00:45:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 48622979-91c6-325d-8084-752ae063276b | -3.7068 | -41.6758 | 2024-10-23 00:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| d3145742-c5f8-31ca-850a-b9d023384468 | -3.685 | -45.4078 | 2024-10-23 00:45:27 | GOES-16 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 1b10352d-5b1a-328c-becb-78e9db018ffb | -4.1719 | -47.9894 | 2024-10-23 00:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 68c0c487-f80c-334c-a2e2-2f1f665b5117 | -4.1905 | -47.9885 | 2024-10-23 00:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 8ba24ddc-0989-38a5-bce2-d5ac57d5edb6 | -4.5331 | -46.6369 | 2024-10-23 00:45:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 405ed9a3-6133-3e22-a750-4f4530b34add | -4.6588 | -44.61 | 2024-10-23 00:45:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| dfecf0c4-da0e-347b-81ce-222f8a8264b0 | -4.6775 | -44.6089 | 2024-10-23 00:45:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 191bbbf4-ee1c-3ab7-b3a6-e3f790901a6d | -4.6776 | -44.5861 | 2024-10-23 00:45:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| aa833660-66ab-32a5-90e1-defe7405bf97 | -4.7254 | -45.7363 | 2024-10-23 00:45:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 80b9f4ae-3803-3991-a2ec-2842538c7bfb | -4.7565 | -46.6249 | 2024-10-23 00:45:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 51.8 |
| bee91cee-1344-35f9-90be-98a3d4f83df8 | -5.2305 | -43.1886 | 2024-10-23 00:45:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 311201ec-da52-3d0d-87b3-1b1d2f863c75 | -5.5671 | -43.2576 | 2024-10-23 00:45:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 961de652-22bc-3c6d-86f8-3e0f60d53c1c | -5.5858 | -43.2562 | 2024-10-23 00:45:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 85ca5f1c-3f21-3137-9e3b-3479e77a447e | -6.6765 | -43.0491 | 2024-10-23 00:45:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| a88ba958-ce9f-300e-a037-d09b36082491 | -6.6767 | -43.0255 | 2024-10-23 00:45:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 39ab26ca-0509-3611-a33f-481ada4651ed | -7.161 | -45.153 | 2024-10-23 00:45:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 90d51606-8438-3a71-9d94-a930f8b6780f | -7.1613 | -45.1302 | 2024-10-23 00:45:47 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |


[Clique aqui para ver as próximas entradas](README4.md)
