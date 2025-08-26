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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbaa287e-e3e0-3dd0-9642-4369ded9bac9 | -9.40656 | -48.24772 | 2025-08-26 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 513921a5-809f-3f23-89a8-3459d12d70c3 | -5.79194 | -43.88284 | 2025-08-26 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e246e828-dba8-398f-ada2-0b1eb7f4c640 | -7.59346 | -43.95889 | 2025-08-26 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b77060f6-ab46-31da-98f4-db609a6dbbf0 | -8.33266 | -50.57226 | 2025-08-26 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fad894fd-c0f9-3ffd-b335-8089b01933e2 | -7.53689 | -36.73742 | 2025-08-26 03:55:00 | NOAA-21 | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 70e88302-b69b-3a4f-be6b-804593bf2910 | -10.81241 | -48.31596 | 2025-08-26 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d49bacb0-4bda-399c-adcb-b7c01f583ff2 | -11.15392 | -44.768 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 6a419d87-a6e0-3c99-a1fb-6902d3ecabba | -6.76114 | -42.98782 | 2025-08-26 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| d2ab3f9c-675c-3c7d-84b7-39ac29751134 | -12.42243 | -46.81024 | 2025-08-26 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6add8167-b9d3-337f-8f43-51dc7858b747 | -11.53972 | -50.45757 | 2025-08-26 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f47965a8-d25f-3312-9f3d-6b14de3b9c7f | -8.31277 | -47.24352 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea117ab2-6577-3f51-8ca3-e1eaa5e5fc8a | -8.26885 | -47.22972 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 904f5dd2-76a0-3db5-8647-0c746b3deb33 | -5.82792 | -46.35579 | 2025-08-26 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9e26ab5-69af-3dc8-b667-0072d434d8a2 | -7.17438 | -45.15467 | 2025-08-26 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8555f8b-e6d7-3e83-90f3-9cf76b64f46a | -7.57052 | -47.47561 | 2025-08-26 03:55:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c9b4659-c06c-361e-8237-f30bb4a3e08e | -8.11126 | -47.12828 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d514fa5-c135-3714-9d63-f52cfa230612 | -11.0847 | -44.77856 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f4baef2-3826-3687-91ae-e15c6c030706 | -6.69863 | -48.38296 | 2025-08-26 03:55:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ebd54051-9d29-3229-bbda-61194e3c4b04 | -7.29859 | -44.53635 | 2025-08-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 817f9481-8057-3396-a121-a4124d9d293e | -6.89342 | -45.65781 | 2025-08-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f765e06-8538-34c7-89ff-666131a3d9c9 | -5.40041 | -45.14872 | 2025-08-26 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73994408-bd71-336e-9146-a17ef4493bbd | -12.3928 | -45.00703 | 2025-08-26 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ab59561-3c92-3a2c-a86c-aca1220d19f9 | -11.26469 | -44.99527 | 2025-08-26 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ee09b98-cb70-3ac2-b49e-0bc1b24922d3 | -11.64176 | -46.19609 | 2025-08-26 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b49ce3d0-8960-3725-bdeb-cf8f9f06c6b2 | -8.38057 | -48.02768 | 2025-08-26 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e79f0300-5c97-3724-b69c-b0a79837ac42 | -11.4405 | -47.32915 | 2025-08-26 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b0b90e6b-4486-3cf0-a95a-3d3892be2534 | -8.31335 | -47.24174 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c759b9de-af9c-3b2f-8ada-5ebd1e1ed867 | -8.33211 | -50.56931 | 2025-08-26 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 8662faeb-eb8e-3688-ba96-2a16af8b8d19 | -11.1192 | -44.7473 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba9fd11e-e3e0-3b11-9245-a2bf33ee2174 | -8.07432 | -47.30669 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5ac16fb-22b2-31ba-81e8-b4db9be7366e | -8.16062 | -45.05524 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f8eac4b-713e-3976-9d7b-bf32312dbac1 | -5.87262 | -42.40896 | 2025-08-26 03:55:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d87fd42-a1d2-358e-8256-f8f71884cd31 | -9.57826 | -48.63181 | 2025-08-26 03:55:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ad35c58-f569-388c-a8e1-e6b730403884 | -6.32223 | -37.75583 | 2025-08-26 03:55:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 58d4be3b-bfba-30ab-90c2-24eb45cb08fe | -10.77766 | -46.38812 | 2025-08-26 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 318629c7-42d2-3c2f-ac26-84033fd8746a | -7.65017 | -42.67898 | 2025-08-26 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 430deae9-025e-35be-b8cf-ad4cd5266121 | -6.89442 | -44.43406 | 2025-08-26 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98e6829a-d079-3b50-ab31-dfc387afc0a7 | -5.41424 | -49.19865 | 2025-08-26 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee53ca17-c396-3b6d-907c-4c186242b102 | -8.28941 | -47.22995 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c34fed61-e475-33ab-bc91-ece5ca488509 | -9.1667 | -40.60462 | 2025-08-26 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c88a83fe-205d-3333-bd8e-266764057103 | -8.36373 | -49.56032 | 2025-08-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acc3396a-94b9-30bd-9f12-f3ff12390868 | -6.40006 | -43.51908 | 2025-08-26 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a76c968d-8250-3b37-baa7-0e2386c9e6a8 | -9.21124 | -40.56362 | 2025-08-26 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 882c8aba-913a-3edc-a11d-186b598e1f55 | -6.87055 | -45.65337 | 2025-08-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5aabb6ea-e27f-3df3-aadf-9dc9bce81e16 | -11.25848 | -44.98263 | 2025-08-26 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3dc026f-2160-30d6-8f43-7cfc9e2b52e7 | -12.42113 | -43.49273 | 2025-08-26 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5a5cf9d-75ae-3bcc-8917-c586218e6d79 | -7.53419 | -44.93303 | 2025-08-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d64ea729-3e42-37f4-b8b7-f6461ad77222 | -6.34307 | -43.66146 | 2025-08-26 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64667a0c-b693-33ec-a651-a7a85475b473 | -11.1592 | -44.76166 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| fc0febd0-aa8c-38e5-be0c-ec714e95d4f3 | -7.29925 | -44.53246 | 2025-08-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d32a428-2673-3204-8b2f-814469741a1b | -11.15303 | -44.74953 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 509bf592-fb9b-373e-a10c-d428bca3ea96 | -11.63616 | -46.40142 | 2025-08-26 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3ebafcc-cdec-3992-a4cc-84d37e2cd6f6 | -8.32557 | -50.576 | 2025-08-26 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e7833421-48b8-3ac5-a4ca-87e1e7aebb17 | -7.96184 | -42.62867 | 2025-08-26 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 401ea58b-305e-3ab0-9da2-568687ec9428 | -6.797 | -44.34163 | 2025-08-26 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f6fb6f4-408d-3415-943b-df0a87b8e7c0 | -7.65612 | -42.66615 | 2025-08-26 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 34c19b89-71c9-3ebc-abac-ac1b58e6dde6 | -11.16448 | -44.75523 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 3793d9bc-8fd5-3651-8a75-9a289cd4c37f | -12.38941 | -45.00272 | 2025-08-26 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 991bf9ff-46c6-31c0-8793-bceb5ccbd482 | -6.90406 | -44.40269 | 2025-08-26 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27d83f89-95f4-35de-807f-093190d6ce8c | -6.94632 | -44.17721 | 2025-08-26 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70679487-3472-350b-af47-94fdcc12d03b | -12.56149 | -44.42708 | 2025-08-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a331b5c0-b005-330c-8415-092587ab18e2 | -7.22465 | -44.40825 | 2025-08-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84c76bb4-031d-3455-a1eb-9fb6679df505 | -11.03625 | -49.14555 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 252f27d2-6810-3877-9f5f-ff46d67d9dbb | -8.48108 | -43.67095 | 2025-08-26 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0707b108-97f1-3ba6-b51e-1a6033481a78 | -12.3888 | -45.00624 | 2025-08-26 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 808c7c99-eb25-3277-9312-01a2d4398a05 | -11.10525 | -44.75593 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c5daeac-e649-308a-86e0-c000b387d46d | -7.15587 | -44.17294 | 2025-08-26 03:55:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92898c84-b2b2-3420-b6e1-0f0ac967e098 | -7.46997 | -45.01321 | 2025-08-26 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14828aeb-67ea-39fe-92be-08e17f1afcfe | -8.30499 | -47.23112 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a1063ccf-3718-3995-9ea7-e3e903aaf3aa | -8.36295 | -49.5645 | 2025-08-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5bca671-0b24-3808-b836-94329d210fd0 | -8.90373 | -45.72049 | 2025-08-26 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c85da8a-a60a-317e-98f7-8dcf53599868 | -11.15732 | -44.77229 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f1a9d797-2f9d-3ca0-b922-a47972eb841d | -8.24675 | -45.10824 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7f53e02-4f5a-3ab6-a874-ffd337d2b7eb | -11.16385 | -44.75881 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| dcc31b5e-f5a9-34fb-875c-066becd9fff0 | -8.32404 | -50.57793 | 2025-08-26 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7c73677e-2591-393e-844e-f5141edc46ec | -7.21437 | -44.41795 | 2025-08-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 153ecabd-3076-39c9-8839-e3f3b9a18c9a | -4.93114 | -47.5546 | 2025-08-26 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c84361dc-5eff-3831-b50f-e62c60c14166 | -8.07416 | -47.31165 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cbf9641-cb85-37d3-be31-9edb505ffffc | -6.31501 | -41.89358 | 2025-08-26 03:55:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 7af962c5-d85d-3c13-b724-0bf5a48c7f09 | -7.5833 | -47.49331 | 2025-08-26 03:55:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26a38537-7a8d-3084-8e90-112c940bda00 | -6.94697 | -44.17334 | 2025-08-26 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2c1201c-ba16-32ec-9b78-dbf1a17c752f | -7.16909 | -45.15891 | 2025-08-26 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1958a2f5-1353-3dae-99e3-3f896788c67b | -5.81311 | -42.29798 | 2025-08-26 03:55:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5b8a4b52-4b31-3dda-97b3-93ed9014c351 | -4.93656 | -47.5554 | 2025-08-26 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b381412c-f010-345f-9875-23c92c858e68 | -7.8525 | -46.73546 | 2025-08-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 040a0cde-d6df-3a37-ad2f-6e855fa89ea2 | -12.37333 | -46.56187 | 2025-08-26 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac4dcc32-1d6d-307d-a525-b54fd9afca96 | -11.62548 | -46.21196 | 2025-08-26 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0aaf921-fb9c-3eeb-8a6f-9b542baff00f | -8.33356 | -50.56744 | 2025-08-26 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d4ead707-5536-3ea6-9cef-34714c9d8add | -11.64183 | -46.19638 | 2025-08-26 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0ab80b6-79d7-35d1-839a-9fe3aa431b30 | -8.23848 | -45.12008 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 468fd646-80a0-31d6-a09f-dc34656c08d4 | -10.53924 | -46.79715 | 2025-08-26 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2e73323-d697-3f50-b8fb-82e986a3b52f | -11.1567 | -44.77584 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 42913d12-19be-39db-b115-9f83b699f740 | -10.14544 | -38.51211 | 2025-08-26 03:55:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d518287d-b5ad-3764-b416-a9af3e98e36f | -7.47065 | -45.00919 | 2025-08-26 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab00535d-d05c-3437-9bde-84827f4d9a4f | -11.15365 | -44.74598 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2bda6f7-6c06-3ee3-a411-f6468907605e | -11.08874 | -44.77925 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2aadcca6-a84e-3b93-b55e-35e314a20b46 | -8.27386 | -47.23051 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6ffc9b68-3bc2-3c8c-8af1-4d794f0d44d7 | -8.31735 | -47.65544 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd0649d2-fa07-3dd5-b57d-3828cdf6a8c1 | -7.29501 | -44.53181 | 2025-08-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1aabcc3f-1765-39cf-8af1-663082535bce | -7.96555 | -42.62931 | 2025-08-26 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README29.md)
