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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b6e3ce3-64a0-39eb-b508-bf68de72418f | -5.6377 | -43.7407 | 2025-07-19 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 9434947d-2d0f-38ff-9daf-f885768799f0 | -5.6569 | -43.6929 | 2025-07-19 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 0030b02d-e3e7-3abc-a48d-7a21230ac97b | -7.4735 | -47.493 | 2025-07-19 00:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| efba11e1-7ebd-30d8-b7ea-69e506f000aa | -7.4733 | -47.5149 | 2025-07-19 00:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 542dff5c-4930-37e3-aec2-0966297673d3 | -5.6567 | -43.7161 | 2025-07-19 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 406.7 |
| 8b0f2d4a-b211-3723-ae40-af7784296f8e | -11.5587 | -47.0966 | 2025-07-19 00:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 79d76ff7-6352-375f-a668-2aeca8a1bdde | -9.7915 | -48.5642 | 2025-07-19 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 81bc4656-f476-3d6c-9c0d-2cea55b25549 | -11.7508 | -48.1825 | 2025-07-19 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| f7a2f68c-c457-3e04-a404-d69c18df22cd | -5.6565 | -43.7393 | 2025-07-19 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 8ea053ee-db43-31fc-84c2-50fb86ebe6d0 | -11.7126 | -48.1874 | 2025-07-19 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 4b8ad978-ddc1-379b-ac36-d0dfcc178fe6 | -11.4789 | -47.3082 | 2025-07-19 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 06159bd5-61f4-3029-a730-fb209e4e3404 | -6.1792 | -48.0494 | 2025-07-19 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 0185b475-daf5-34db-bcfe-63f20316a078 | -6.1604 | -48.0724 | 2025-07-19 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| ab3a783b-b226-3620-aa85-94076fe13c61 | -2.9109 | -48.2325 | 2025-07-19 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 94acb041-8f11-3e92-bd58-282f46cd8244 | -11.4786 | -47.3306 | 2025-07-19 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| f1a17089-aa79-3847-9bfa-621174d86963 | -3.1384 | -47.0068 | 2025-07-19 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 65f8e279-e274-371c-907d-1724aa71572d | -10.6247 | -44.767 | 2025-07-19 00:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 342a72eb-4b2e-39d3-8ff3-a4586b11aae7 | -11.7313 | -48.207 | 2025-07-19 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 2f51b589-c5ad-3e96-94c7-f56dfdca9c1c | -11.4977 | -47.3281 | 2025-07-19 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 0bf6e973-1d5b-38ec-8c0b-52997b91c7a0 | -7.492 | -47.5134 | 2025-07-19 00:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| b87795fe-1282-305a-85f9-b320ff1d6c17 | -5.6379 | -43.7175 | 2025-07-19 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 270.1 |
| aeff1abf-a3eb-3a38-a773-618deb92992f | -4.2614 | -48.5465 | 2025-07-19 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 994bfc2a-6ff6-3e21-80e2-f0bd6c0ee436 | -3.8209 | -47.7444 | 2025-07-19 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| ae9a6c79-cc03-393d-8f87-f435a71109d7 | -9.8104 | -48.5622 | 2025-07-19 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 07a9aca3-5a72-3133-996f-f854763dbaa7 | -7.4923 | -47.4914 | 2025-07-19 00:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 2c769c3d-a0a4-3b56-b5b7-48d3d847b4eb | -11.7317 | -48.1849 | 2025-07-19 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 293.1 |
| af5c767d-943b-3167-abc1-afe0b83ac902 | -3.1198 | -47.0075 | 2025-07-19 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 2e4d7010-5fee-3e6b-9f88-9e74bf8fd615 | -6.1606 | -48.0507 | 2025-07-19 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 297.7 |
| 04512a09-d54a-3057-9be3-2dae4dddf657 | -8.5389 | -47.8368 | 2025-07-19 00:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 9659573e-25b3-3368-a847-768cb944cdba | -2.9108 | -48.254 | 2025-07-19 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| bf863f7b-2600-3a3b-a9ae-0805e9be7d09 | -22.23928 | -43.72714 | 2025-07-19 00:01:00 | TERRA_M-M | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 7b5caeb5-d550-3cdc-a3d4-a89726034bf6 | -15.47992 | -41.76427 | 2025-07-19 00:03:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| f251ad44-3b30-34da-abd0-718fa3e5c255 | -16.04378 | -43.73208 | 2025-07-19 00:03:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 20.8 |
| a915b2c5-8768-3bae-8d00-5c3c6a2df948 | -15.61717 | -41.32936 | 2025-07-19 00:03:00 | TERRA_M-M | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| b6872f08-af1d-37d9-957f-e0df1fdc1fb3 | -14.70588 | -45.06358 | 2025-07-19 00:03:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 93538d39-f1e7-36e7-8570-2ff89ea88e75 | -16.04205 | -43.71704 | 2025-07-19 00:03:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 3c66ed84-bac7-302a-a770-4921058071b6 | -15.92715 | -43.51328 | 2025-07-19 00:03:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 3303e5f8-fbd1-367c-b7f7-d48e91aa6f01 | -11.45606 | -48.16199 | 2025-07-19 00:05:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 59ba49fe-fac6-3289-bbff-6576e09c5203 | -11.41568 | -42.07184 | 2025-07-19 00:05:00 | TERRA_M-M | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| e5795a82-9464-341c-8ce5-dfbf73152202 | -11.73523 | -48.21909 | 2025-07-19 00:05:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| d82f809b-0e59-3749-a755-43ec5a916ae2 | -12.09537 | -44.73379 | 2025-07-19 00:05:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| d62df249-48a3-304b-a9dc-0ea7526819ab | -11.72927 | -48.16949 | 2025-07-19 00:05:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 1d108b74-c08a-3778-ade8-9280f50227c3 | -11.96513 | -47.02856 | 2025-07-19 00:05:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 11d14912-5edd-39e2-bd80-ffc8375added | -10.62305 | -44.76325 | 2025-07-19 00:05:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 2465f5aa-a536-3b9c-a1e8-d7a83353003d | -10.8641 | -47.14624 | 2025-07-19 00:05:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 78cf92b5-ad8d-330f-a82f-fd855b5e7a37 | -12.57967 | -41.29157 | 2025-07-19 00:05:00 | TERRA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 61b05815-74f5-3acf-bffb-afe125e03f27 | -11.47985 | -47.31263 | 2025-07-19 00:05:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 77f135b6-a1b9-32ba-b44a-61e261e4314a | -11.73211 | -48.19096 | 2025-07-19 00:05:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 567.9 |
| 41150ba4-867a-3661-b07b-2a560d416d4b | -11.57407 | -47.10502 | 2025-07-19 00:05:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 76f01c4a-52e6-35e7-9601-3268b09816b5 | -10.65076 | -49.29741 | 2025-07-19 00:05:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 0ce6a1c2-896f-3dc4-8126-bd76be3d480c | -10.72947 | -46.7914 | 2025-07-19 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 33fe807e-6b15-311b-b9f9-774c8dffa9b0 | -12.42319 | -45.37056 | 2025-07-19 00:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 511b6566-2603-331c-b57f-641cdac93817 | -10.63418 | -44.76181 | 2025-07-19 00:05:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 8aaebc62-ee82-3f59-83b1-4bd3e2ce660d | -10.63563 | -45.23975 | 2025-07-19 00:05:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 14e2825c-4f5f-3f93-af21-8ae4dba2f49a | -11.9625 | -47.00544 | 2025-07-19 00:05:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c87984f4-cec9-319b-8d2b-7188463cc567 | -10.72668 | -46.78655 | 2025-07-19 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| b2f616ca-5f4a-3644-9ed1-df120c5f9b91 | -11.95518 | -47.01303 | 2025-07-19 00:05:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 4cb281bd-c113-3edf-b110-04d2b39acb77 | -10.86691 | -47.16925 | 2025-07-19 00:05:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| f5ffa516-dc7e-3dfa-a764-eb02dda5a992 | -13.60337 | -45.64497 | 2025-07-19 00:05:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 69ea5615-f6bc-3930-986c-1b2ed6a1b2d5 | -11.57137 | -47.08235 | 2025-07-19 00:05:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| a6b75967-502b-3290-9e5f-9ee9d7b96883 | -10.64715 | -44.49191 | 2025-07-19 00:05:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ead7c319-eb8f-311d-bf8f-86166ca14957 | -10.63604 | -44.77649 | 2025-07-19 00:05:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 77679c88-7992-3248-aced-273abf7db23b | -11.56773 | -47.09918 | 2025-07-19 00:05:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| dfd19fff-afa5-386b-add1-b9fbbfe0c4d4 | -11.45609 | -48.15657 | 2025-07-19 00:05:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 8658e20d-0f0e-35b0-b4f6-d2277c5239bc | -11.95797 | -47.03613 | 2025-07-19 00:05:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 3a38f98b-f512-3e51-a1ec-b62af2a290a6 | -11.73256 | -48.19737 | 2025-07-19 00:05:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 389.9 |
| 4221083a-9d2b-3984-afed-c4c6ac5b784c | -10.82467 | -49.29448 | 2025-07-19 00:05:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 79512c80-a707-399c-857b-23af497b62ed | -10.86106 | -47.16325 | 2025-07-19 00:05:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c01c80af-faa3-3637-922c-d51222f32a59 | -10.6596 | -49.29105 | 2025-07-19 00:05:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 45a023af-79ed-33f9-affc-1e0b8d5faad1 | -11.82488 | -48.20832 | 2025-07-19 00:05:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 4cc811ec-a20e-360b-bb67-0530d65ebaf2 | -11.82732 | -48.23182 | 2025-07-19 00:05:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 2baaff94-54b4-3e1c-be8f-4b514f395e84 | -11.48262 | -47.33638 | 2025-07-19 00:05:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 0e279b34-6362-3c11-b5cc-e1d0be57d31e | -10.5118 | -42.40312 | 2025-07-19 00:05:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| ac375df9-5422-3601-ab9b-68dec972eebb | -11.55774 | -47.08392 | 2025-07-19 00:05:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 9b30b67b-ed56-3285-8a76-5dcea25553d9 | -10.6249 | -44.77795 | 2025-07-19 00:05:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 50.7 |
| c7d8d4a3-11e0-3de5-8354-96b4fd2ab4b9 | -11.5604 | -47.10649 | 2025-07-19 00:05:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 9872342e-33e8-3c98-a7e6-1f58c72e6059 | -5.80235 | -43.62378 | 2025-07-19 00:07:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6013bb2e-c223-3982-ad42-174c5eb75d0c | -5.91692 | -43.46897 | 2025-07-19 00:07:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 10da651b-0905-3389-989e-3f34d396d748 | -6.15842 | -43.75532 | 2025-07-19 00:07:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f1bc995d-b534-384d-8df6-6ff97ef67640 | -5.74502 | -46.19479 | 2025-07-19 00:07:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7925c69f-c642-3209-b84a-74ebb5092f7d | -5.65258 | -43.73117 | 2025-07-19 00:07:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 33839d4c-49dc-3109-8acd-269234bec4db | -2.90166 | -48.24107 | 2025-07-19 00:07:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 6c33511b-e95e-33d4-82ed-97c728ee0c41 | -4.48063 | -46.07914 | 2025-07-19 00:07:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 11dfb304-8bed-30cc-9d07-fdab88ad0228 | -4.66361 | -41.96416 | 2025-07-19 00:07:00 | TERRA_M-M | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e3263973-01cc-3239-84d5-7c59da839238 | -9.60172 | -43.8638 | 2025-07-19 00:07:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| d763206b-ec35-36bf-bb88-d2a912172f2a | -3.06066 | -40.04442 | 2025-07-19 00:07:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 56748967-9cfe-3048-a80d-8f4de041acdb | -3.12629 | -47.00242 | 2025-07-19 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| ac61ff7f-8c1e-3c0a-94db-37b5348ad65e | -7.49238 | -47.50023 | 2025-07-19 00:07:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 459.6 |
| 96f77c79-3093-3f02-92d8-e3f23055f917 | -3.61177 | -43.54657 | 2025-07-19 00:07:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| b186f092-55c4-3de1-ab81-01d98714648d | -5.64153 | -43.72196 | 2025-07-19 00:07:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 2c51d330-806c-3cc2-ac94-13fdf8741b13 | -9.81623 | -47.74871 | 2025-07-19 00:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 34ce3d91-c353-3e05-93f3-b53866552a5f | -7.48797 | -43.92884 | 2025-07-19 00:07:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e97e4efa-ade9-3eb1-818d-a30ca2f399f7 | -6.13493 | -42.14792 | 2025-07-19 00:07:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| e14a7ae9-5d75-320e-975f-3d2863d817d7 | -3.58959 | -47.53059 | 2025-07-19 00:07:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 6b7b22d3-aa73-3f2e-8553-1f980617624e | -3.13804 | -47.00065 | 2025-07-19 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| f2e86ce1-c902-30fc-bc29-2fa75544ba0d | -9.82131 | -47.7416 | 2025-07-19 00:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| c7b66601-cf24-366e-b543-5170b1e19f81 | -5.53212 | -43.8835 | 2025-07-19 00:07:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 4b04409f-4e28-38f9-ab89-74a46ab959e8 | -9.76903 | -48.75455 | 2025-07-19 00:07:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 7e61d6c2-b403-3901-89e0-363a91c70972 | -6.16796 | -48.06824 | 2025-07-19 00:07:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 181.2 |
| 84fd646b-ba82-30fa-ae50-0a5335e9fdc0 | -4.25154 | -48.56524 | 2025-07-19 00:07:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |


[Clique aqui para ver as próximas entradas](README2.md)
