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
| 9016de4f-5897-320b-8c1a-0433a5e52f9c | -12.86677 | -46.06731 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8782738d-f25d-3150-9634-120e1c1fbc84 | -12.86895 | -46.07516 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a119f00-c517-349c-bdd3-88b0bfa17d4a | -13.01422 | -42.32436 | 2025-08-17 04:14:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| b5298630-7f9d-3069-97fb-e8938680ce67 | -11.181 | -44.5273 | 2025-08-17 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58add47f-23b8-3de5-bce8-a7d6f92f00ed | -12.61774 | -46.91486 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f72e929-d293-37a0-902c-591958176941 | -9.69424 | -46.26004 | 2025-08-17 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffab9842-5dd4-38c2-9c9b-544c3e246e92 | -13.43218 | -45.8927 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae78acd0-a968-3ae9-ab68-3f7718dd9838 | -11.89593 | -43.42757 | 2025-08-17 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f6ec288-a4f6-358f-bb68-2a60ab6f42ed | -8.10753 | -42.35616 | 2025-08-17 04:14:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| deb91a45-8acc-3ebc-a13d-1e088dc66bf9 | -8.0378 | -47.67174 | 2025-08-17 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e1d45798-f448-3858-bdbf-0316a861736f | -7.60492 | -44.93792 | 2025-08-17 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38dc3401-b525-30dd-a798-1672c0224d4c | -6.19104 | -45.44146 | 2025-08-17 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9df81d2-e90b-3230-9d83-c5e9159a237e | -8.50018 | -44.73935 | 2025-08-17 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11108749-d05d-3e79-87f3-c30237481322 | -12.69784 | -45.09281 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1cc9077a-d3eb-3f4b-a214-d0d29ef67b98 | -10.8395 | -45.34621 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 139e5a75-7bf3-348b-a0ec-3df687901270 | -10.85403 | -45.34125 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d29549e7-9ce3-3323-854e-b0dcc09c3f25 | -10.82335 | -45.33987 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaa5c4d2-ae33-38be-a618-7f57b9ae63e8 | -12.88751 | -46.13099 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85d53b2d-65b7-38ef-b3ca-19562c1d7e85 | -6.99162 | -45.58287 | 2025-08-17 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84997e07-b7bb-3dfd-9561-06dc6e4f5a2d | -6.52997 | -44.54855 | 2025-08-17 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e887bccc-1232-3509-944e-764531d76ea4 | -10.8425 | -45.30623 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 609648a3-a67f-32d1-ace4-c7556f1dca2f | -7.87898 | -43.86329 | 2025-08-17 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34a40537-6642-3bb9-ac06-8942a55be09f | -12.89267 | -46.1206 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0db8b7ee-119d-324e-97d2-6f3eb49d4a63 | -12.85631 | -46.04676 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85bca0ac-f41a-3e71-900c-dda4a33f0ea6 | -12.86342 | -46.06671 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 682ff874-2d12-33df-8674-fdec28d0cf7d | -12.77255 | -45.93533 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5776cf1-d5c0-3989-a99b-e3e0474d7ee5 | -6.18126 | -45.43587 | 2025-08-17 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fcce77e3-0913-348b-9cd6-133bf193b896 | -12.86401 | -46.06307 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bc116ff-e158-3ec5-bab3-df1403a76e34 | -12.54128 | -46.93526 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98df01d7-348b-3d32-9140-c0a92ac75cd9 | -7.19583 | -43.97141 | 2025-08-17 04:14:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ed5cbeb-083d-3d0f-9604-c5dab6722aad | -7.19252 | -43.97087 | 2025-08-17 04:14:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c35b84d-2e45-3900-a6c6-cd8342a9452b | -8.90402 | -47.33912 | 2025-08-17 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f30e0126-2623-34cf-8d97-5f5d8dbb27c9 | -7.19992 | -46.21787 | 2025-08-17 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6fd03c4-077d-3894-9f77-536d8dc5835d | -12.57459 | -47.04421 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27809372-d63c-3b95-b309-30cd4a7d498c | -10.84169 | -45.35392 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b75d0367-aad3-3d65-aeea-ad51a3be1bcb | -7.19307 | -43.9674 | 2025-08-17 04:14:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d5097105-3d70-3dde-872e-f5e783675305 | -8.08098 | -47.69373 | 2025-08-17 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 263827be-e5cd-3982-b7e5-894dcb028745 | -10.83467 | -45.31227 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b070307c-a56c-3df5-b78f-810718fc313a | -8.49742 | -44.73525 | 2025-08-17 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31235093-2336-3b38-b6cd-d3df8223cb6d | -7.93924 | -48.18277 | 2025-08-17 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 560eb61f-6d74-36b8-afc2-95b9ea1956fe | -8.73104 | -44.0388 | 2025-08-17 04:14:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a56de62c-4f6a-389d-8765-c58915bc3544 | -12.83301 | -46.00914 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c633a1a-99eb-3a17-b9f4-f5e9094dc361 | -6.25673 | -45.55444 | 2025-08-17 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c105671-da9d-371c-8431-d97c7dfbc148 | -5.57129 | -52.04865 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95c830d6-e7f2-3216-97bf-cfa07806556d | -10.31557 | -54.16265 | 2025-08-17 04:14:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 208bc728-8e98-342b-9ebe-7b9752d20d38 | -7.02284 | -44.24881 | 2025-08-17 04:14:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 594d1526-2733-3a38-ae4e-cb20c01bca20 | -13.44062 | -45.883 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35c71aa2-8ef0-366e-9523-234817f6cf78 | -10.844 | -45.33957 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b2909f7-08c7-3169-8444-1d234a39a3d1 | -7.02617 | -44.24935 | 2025-08-17 04:14:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 375aa7bf-4a7b-3f91-a7e7-d3fae501808f | -6.61784 | -44.46413 | 2025-08-17 04:14:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af791534-2c38-3619-9f3a-d859d38fb997 | -10.83776 | -45.35697 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c4ef86f-6a95-3667-83da-b761030083d3 | -7.19528 | -43.97489 | 2025-08-17 04:14:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b208952-e67a-38cd-b1de-64931bbe1c1f | -12.54213 | -48.4957 | 2025-08-17 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7315aae-0fe0-3d54-abb8-430d353eb62c | -6.50547 | -45.44769 | 2025-08-17 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ceaabd6b-dbb0-3b9e-b737-4adef5f3fe78 | -11.09157 | -44.81169 | 2025-08-17 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 445d60db-daa0-3377-9ca6-ba1fbaa51930 | -7.61121 | -43.83806 | 2025-08-17 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb404f03-7279-3310-b94b-f8a7df9ae3ba | -12.44958 | -47.00445 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 854be01d-723b-3011-89d8-74f671888f14 | -8.70447 | -49.41353 | 2025-08-17 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53f78b20-a12c-3084-bdd3-25c898f712b7 | -7.70401 | -47.43922 | 2025-08-17 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08430160-e155-3fa2-976b-6f5676070e1c | -7.14313 | -44.6428 | 2025-08-17 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c321944-bc68-3cbc-ae2d-bf0c55b9b465 | -6.55126 | -43.02012 | 2025-08-17 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c1736db1-2b94-3911-a222-f8a52d0ec53d | -11.36454 | -55.42012 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a5a70af-68e6-35e9-aa7e-244d112787c6 | -12.18951 | -47.24017 | 2025-08-17 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0820f438-a704-3535-becd-a6b47b082c67 | -12.89326 | -46.11695 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 146e93f1-4313-390c-942c-4902be29a8c2 | -6.18472 | -45.43645 | 2025-08-17 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 14ee54b6-1101-3b6f-a554-4829199c3d65 | -9.27756 | -44.55351 | 2025-08-17 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d04369b1-f334-3931-97eb-43322a4d5135 | -10.85576 | -45.3305 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a604d865-8c59-31fe-993b-eb1ca9daab42 | -12.83797 | -46.0212 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2dd5bbb-9b5a-3b0d-97ba-1536cfd7c096 | -8.51078 | -44.73741 | 2025-08-17 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 247fed8b-b798-3a76-82dd-0c4b9aabcbbf | -8.74759 | -44.04143 | 2025-08-17 04:14:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d65685a2-275a-33ee-a099-fa5f2401c664 | -8.51021 | -44.74096 | 2025-08-17 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a48a9c0-fdf2-38a4-a61a-520bad1563e9 | -8.01724 | -43.33078 | 2025-08-17 04:14:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 25065841-3799-32b9-bf07-939f794b950d | -13.56559 | -46.97771 | 2025-08-17 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b56d5fa7-4eb9-343d-ab20-bc11c788e834 | -10.82843 | -45.32963 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18105a2f-4a76-3951-875d-c72a232ce0b1 | -12.4461 | -47.0038 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2cb3386e-e291-34bc-9c2e-ee970d5525eb | -5.95312 | -46.15806 | 2025-08-17 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57104d9e-db2e-3e01-a201-938ef29eb84d | -12.8899 | -46.11635 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2dd825d-7258-3ce5-9299-ec3247bdb2e4 | -6.78218 | -44.3517 | 2025-08-17 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5efeb096-7eff-3a8e-a985-0ce4eba92d47 | -13.43336 | -45.88549 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3cd0fd0e-8e81-38ba-9b17-869e22d66e77 | -6.72538 | -44.04704 | 2025-08-17 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a875d24-7389-3d86-9b3a-4ef659926d0f | -12.83738 | -46.02485 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63a567e1-3db7-3b01-9ed4-3f9b9d9a5b24 | -12.8336 | -46.00552 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c8d298d-638c-3a9a-9ced-160818e91b90 | -10.31629 | -54.15879 | 2025-08-17 04:14:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 192ebe60-d685-39f8-a40a-b1e8fd90dc54 | -9.69708 | -46.26447 | 2025-08-17 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74405dba-26ed-3d4d-adbc-062e35c59ace | -8.03479 | -47.66645 | 2025-08-17 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66b7e55b-fbd8-3166-ab2e-0c5ee407af4b | -11.88801 | -50.95037 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4bc8fd0-82e1-3bc2-994d-64ebcfc1f971 | -11.35616 | -55.39974 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff8485b5-3eab-3fd0-bd3b-a3668946a2b9 | -12.61552 | -46.90681 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3b0ca55-1a6a-3a98-8608-1f0e9d9ead31 | -12.19304 | -47.24075 | 2025-08-17 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19a951e6-ae1a-34ba-b069-ca421a5a20b1 | -7.89775 | -42.11808 | 2025-08-17 04:14:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 90a1af7c-48b0-36bd-8093-883f5840848d | -13.44396 | -45.88357 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c196a3b8-2eeb-3f0a-9659-d5cdd33eacca | -11.35529 | -55.40419 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9d618e0-4821-32e1-9ca0-1d983b2e9548 | -12.88811 | -46.12732 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 895318a1-1896-363b-bdc1-7ca75d16e1a4 | -6.54632 | -43.02998 | 2025-08-17 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ce51ec0-1a4f-3ebf-90bf-2f320f49004f | -12.2023 | -47.25059 | 2025-08-17 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3a80ec7-fbb9-3118-843a-3a5f292821f8 | -13.3446 | -44.19881 | 2025-08-17 04:14:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50fdeee4-d708-3547-9267-794274e056f9 | -10.31987 | -54.15965 | 2025-08-17 04:14:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 262782f5-5ebb-332c-a26c-46f4c124d8a5 | -12.20601 | -47.25039 | 2025-08-17 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c80a252-8d82-3a48-a193-7b0cbfb5f5c5 | -9.10395 | -44.7059 | 2025-08-17 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3359648d-9d71-355e-bdf0-0cdd025c3307 | -7.62502 | -44.96352 | 2025-08-17 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README19.md)
