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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 593cb6cc-9db2-375e-b663-46c486869b68 | -11.4456 | -43.6697 | 2025-09-10 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 01e72dcf-079f-300a-be18-d094961b8e58 | -11.4097 | -43.5336 | 2025-09-10 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 47662029-fb08-3160-82d5-5c2c351f75c3 | -6.2595 | -43.4129 | 2025-09-10 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 21d7c628-0a1e-3423-bfbb-0caa97b3e42c | -11.4705 | -50.3247 | 2025-09-10 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| e12e3a12-7074-3b54-a8a1-40e29d122562 | -9.7223 | -48.0907 | 2025-09-10 13:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| c3629db3-8239-3dfe-b847-8f08e0a25227 | -15.655 | -53.8771 | 2025-09-10 13:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 88253a06-891a-3132-8c1b-4380c6c1ee9d | -12.1889 | -50.6267 | 2025-09-10 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 037c6e85-67f8-3898-ba88-c461244e7422 | -16.4573 | -50.6773 | 2025-09-10 13:10:00 | GOES-19 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 33a5e460-df1b-343a-984a-e9923642548c | -5.66 | -43.344 | 2025-09-10 13:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 375fd77b-f02b-3db3-8669-cb2d76314d83 | -11.4465 | -43.6224 | 2025-09-10 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 8179133b-3fb2-34cc-b16f-9261b9284ec2 | -11.488 | -50.4298 | 2025-09-10 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 133.9 |
| f2afa9d2-da6d-34de-b2ff-a8d501a5d5bb | -11.4652 | -43.6432 | 2025-09-10 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 56b569bd-dbac-37e2-bb46-bc2bbfc438fc | -15.1021 | -50.1249 | 2025-09-10 13:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 6cab08b2-3320-3001-8e33-15a5001a7927 | -11.3905 | -43.5365 | 2025-09-10 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 5a50e5bd-fe48-3ec2-be66-4ec44b02cec5 | -6.2407 | -43.4144 | 2025-09-10 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| c20a0f55-5e1d-3e03-8927-875f7aca08e6 | -11.1245 | -52.0359 | 2025-09-10 13:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| f86e6ef8-42d5-383c-93e0-90f7e261a882 | -6.2407 | -43.4144 | 2025-09-10 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 162b6b40-30a6-34ee-a4a9-acea4a6f79cc | -10.3885 | -50.5264 | 2025-09-10 13:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 156.7 |
| 88f5ccb2-be93-3bf8-a9bf-6b2994c425c9 | -8.35 | -44.8324 | 2025-09-10 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 8e272a5d-0ddf-36c5-bf23-aa8aebc1ef41 | -12.2287 | -43.8772 | 2025-09-10 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 7114f41b-3563-3576-bf77-baab1b14a255 | -13.0161 | -48.0549 | 2025-09-10 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 7b26c861-0f31-3aa4-be08-acebda25670b | -11.3393 | -46.5193 | 2025-09-10 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.4 |
| b42e1a37-e9da-365f-bdd8-286520b786ac | -6.8521 | -47.9143 | 2025-09-10 13:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 9d9d7cca-6681-3039-93f8-6cea4a4134fc | -10.1467 | -46.1747 | 2025-09-10 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 3230ce0e-55e3-3e0e-80c9-17989ae7a2f1 | -9.0132 | -46.0563 | 2025-09-10 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 2410d391-891b-3d52-8deb-6dd92a43c74c | -8.0794 | -48.6407 | 2025-09-10 13:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 271.8 |
| 68897b3b-b4b0-380f-b0cb-67ca7b50dfdd | -6.8523 | -47.8925 | 2025-09-10 13:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 20b28d88-76e8-3c14-8496-00b60a41f2a4 | -8.49 | -45.6826 | 2025-09-10 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 66da935b-9e07-3c3f-9e2c-1bc7154034e9 | -14.907 | -55.8546 | 2025-09-10 13:20:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 47131a68-fcb3-3ede-b75b-0bdcd3789565 | -5.6788 | -43.3425 | 2025-09-10 13:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 21204a65-f49d-38d8-87b9-a4d5086c9b1f | -9.7223 | -48.0907 | 2025-09-10 13:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| b0376119-ffdb-34ee-99ff-7024bbc6d7f1 | -11.3905 | -43.5365 | 2025-09-10 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 195.5 |
| 278f51c8-13fc-3261-bf4a-e498ef1489ae | -11.1247 | -52.0149 | 2025-09-10 13:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 50d9eb85-9890-3b24-823f-69445ad4b5ff | -10.7224 | -48.2863 | 2025-09-10 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 33b71fe4-7fd7-3549-87a9-ce39dbb9b911 | -16.5294 | -55.1434 | 2025-09-10 13:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| eb54d4b6-1dea-32cc-9806-155f24bdc51b | -9.6821 | -46.8791 | 2025-09-10 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 9ebdcf4c-4ec1-3c63-b745-e85bac736644 | -9.7011 | -46.877 | 2025-09-10 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 693927e2-d5b4-39a0-b206-eb0c2c7fd15f | -9.0579 | -46.9688 | 2025-09-10 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| f480cc4a-09d9-3dcc-bc55-8ae7d9b90cc9 | -11.3389 | -46.5419 | 2025-09-10 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.0 |
| ad54231b-f7ac-3503-b5e6-f9b121fd7e1f | -10.3882 | -50.5477 | 2025-09-10 13:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 308.0 |
| 2a8d5734-c99f-3f8a-9b08-48a3e0e2df7f | -6.2597 | -43.3895 | 2025-09-10 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 3e7c94f5-f58f-3055-b65a-9a4f3711d438 | -6.4179 | -44.4633 | 2025-09-10 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 38a7a738-8a7e-35e2-8b2f-716c52244923 | -6.8519 | -47.9361 | 2025-09-10 13:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 3102f832-489c-3560-ad11-02f0b7bfc297 | -11.488 | -50.4298 | 2025-09-10 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| cf5886c3-ff1e-3baf-9701-8cd6edf3b4e3 | -11.9535 | -51.081 | 2025-09-10 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 1cd1a5d5-6323-3860-b616-90aa1a79b69a | -11.507 | -50.4276 | 2025-09-10 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 30c5d6cf-bd8d-33c1-a306-f263ae8136ef | -8.721 | -45.3181 | 2025-09-10 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 90e90280-c209-3f9f-9e9e-ff89600f93e2 | -13.1367 | -54.9171 | 2025-09-10 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| b32ce6a8-412f-352a-bcb9-5154d854384a | -7.4845 | -48.2349 | 2025-09-10 13:20:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 608cc997-f9bd-3fdf-8162-123294593b9e | -7.8462 | -46.0165 | 2025-09-10 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 8a1a919a-d452-348e-9530-2ecb9557500d | -9.0074 | -49.5278 | 2025-09-10 13:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 409b2753-6e08-3130-8c5e-7b8fd9f9da5b | -9.8263 | -46.0549 | 2025-09-10 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| f2ea035d-6b0c-35a6-baa6-e6e9465df149 | -9.3437 | -46.7603 | 2025-09-10 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 5046f17c-5548-353a-b7c0-2e5151b7d7d7 | -8.994 | -46.0808 | 2025-09-10 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 4d6ccefb-4f44-3513-9d3f-c6780810027a | -9.0262 | -49.5261 | 2025-09-10 13:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 0b587a7d-b311-3cff-86a6-62536ff1f622 | -8.0414 | -48.6873 | 2025-09-10 13:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 0d2296f8-d813-3e59-812c-afefc5d77814 | -6.4176 | -44.4862 | 2025-09-10 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| bee70b46-0304-371b-94e5-a0ec3b914308 | -14.7542 | -45.3156 | 2025-09-10 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 122.3 |
| ab1ed83b-69e6-3089-bcaa-6eced502911c | -12.1889 | -50.6267 | 2025-09-10 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 154.4 |
| da33871d-2421-3d04-ae5b-355e71f20d51 | -7.5409 | -48.2085 | 2025-09-10 13:20:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 860f645a-4bf9-3c64-99e5-474d532e939f | -15.655 | -53.8771 | 2025-09-10 13:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 333c03b1-cf1e-32cf-ab7b-9c4613209c25 | -15.1021 | -50.1249 | 2025-09-10 13:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c7500574-21c0-3827-a5e6-9f57f3cccb8c | -13.0165 | -48.0326 | 2025-09-10 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 6dd29303-b847-3240-8f40-15ffb049b8b0 | -6.5572 | -47.4992 | 2025-09-10 13:20:00 | GOES-19 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1bf799c8-5b26-323a-b9cf-cc2cce23dd39 | -5.9193 | -45.7492 | 2025-09-10 13:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 5edbd543-25ae-3c6b-9213-68f25ae27dd6 | -11.4097 | -43.5336 | 2025-09-10 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 918a03ec-1c43-35b3-8211-e6d89387acee | -6.2595 | -43.4129 | 2025-09-10 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 7af841b2-c2d4-38d3-806b-c4a5586f94cc | -14.7536 | -45.339 | 2025-09-10 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 193.8 |
| b8386c81-d59c-3cbf-83ac-573124a34c1e | -12.1885 | -50.6482 | 2025-09-10 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 81087f50-0ae6-33ef-ba20-ba18e0ac99e3 | -11.1245 | -52.0359 | 2025-09-10 13:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| c33a9577-5b91-3abd-9c2c-a46a49831827 | -10.0155 | -51.7031 | 2025-09-10 13:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 3c66b66f-ee4e-37d4-8791-12ddde34e6e2 | -6.1896 | -41.0398 | 2025-09-10 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| e4fdf916-6c69-3464-945a-d46423a976df | -13.1176 | -54.9191 | 2025-09-10 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 5baeafa4-c593-39ef-ab74-c3c63e16f3a8 | -8.0416 | -48.6656 | 2025-09-10 13:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 1104029e-4230-3cbe-9c07-6e672cd1016b | -14.7737 | -45.312 | 2025-09-10 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 4c23c425-3283-35e3-8128-f356b9621379 | -9.0768 | -46.9668 | 2025-09-10 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 17b72fbe-048c-38af-a2dc-551b3cb5eb0b | -11.3389 | -46.5419 | 2025-09-10 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 072e29b5-52f7-3d68-b302-b20c7f5028ad | -15.2686 | -53.7801 | 2025-09-10 13:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 40016839-970e-309e-83fa-104f66a940de | -8.0774 | -45.5433 | 2025-09-10 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| b3ebb802-3068-3a9c-9bf0-f2867fc5b412 | -9.7223 | -48.0907 | 2025-09-10 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| be774401-287e-3db4-b2a7-172a9ebf5ef8 | -12.1889 | -50.6267 | 2025-09-10 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 183ad96b-9fc9-3804-b607-8cfab64eb852 | -9.0579 | -46.9688 | 2025-09-10 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 33ba1ad2-9036-3fe4-8ffc-768aa6a2eabf | -9.6821 | -46.8791 | 2025-09-10 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 165.8 |
| af9ab703-9a2a-36f2-97d3-1b9bcdf047a7 | -11.4512 | -50.3483 | 2025-09-10 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| f085f91d-1460-3688-8cc5-b585dc33486d | -6.1894 | -41.0641 | 2025-09-10 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| b35c2031-6fb5-35e4-bca5-ea5179afb803 | -12.1885 | -50.6482 | 2025-09-10 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| a749c616-8f59-3f5b-b93f-7ed56cf28a09 | -9.0132 | -46.0563 | 2025-09-10 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 874834c1-8f9d-3d82-931f-ea58a66d46d1 | -8.994 | -46.0808 | 2025-09-10 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 76532e7f-44dc-3aff-a11d-3ed1d0acd0fd | -16.4573 | -50.6773 | 2025-09-10 13:30:00 | GOES-19 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 60ea8de1-95ef-3d9f-a3cd-5d898a75cb6a | -6.2407 | -43.4144 | 2025-09-10 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 095cdd02-9a2a-37ed-9149-22dc788ab1d3 | -15.2877 | -53.7987 | 2025-09-10 13:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| c14df7fe-f367-3d41-b2fd-b3eefe6e516b | -6.8519 | -47.9361 | 2025-09-10 13:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 3eb5ac0a-626f-3bfc-8c5e-07b1820f7766 | -11.1247 | -52.0149 | 2025-09-10 13:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 192.0 |
| fdc38c5d-1a95-3678-aa5a-ba6d04cca28f | -8.5272 | -45.724 | 2025-09-10 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |
| eb3adca2-e86a-3ee0-a3de-22e61da35a40 | -14.5125 | -53.9367 | 2025-09-10 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| c9dd2319-ede5-3f8c-95ac-e6fd2b028ff2 | -16.5099 | -55.1459 | 2025-09-10 13:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 4aac5e9e-380d-3c69-937a-07f454592ca8 | -11.4702 | -50.3461 | 2025-09-10 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 241.4 |
| 88c46608-3392-3db4-9242-cbf571bb97d7 | -15.2881 | -53.7777 | 2025-09-10 13:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b7d31fe3-bca5-3b98-882c-5d16c7347e89 | -6.8523 | -47.8925 | 2025-09-10 13:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| f674482f-6667-3563-a2b2-d284ba91f4ef | -6.5572 | -47.4992 | 2025-09-10 13:30:00 | GOES-19 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |


[Clique aqui para ver as próximas entradas](README110.md)
