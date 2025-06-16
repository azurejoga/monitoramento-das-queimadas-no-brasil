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
| 820a6698-a130-302b-be2c-8a13950f1644 | -7.1167 | -44.0571 | 2025-06-16 00:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 4694039c-29eb-3ee6-93f5-a5da0c68f89c | -10.0972 | -52.7376 | 2025-06-16 00:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 81f17585-4902-39e8-b136-00a3d9a2d8f9 | -11.1379 | -53.9429 | 2025-06-16 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 268.0 |
| bb95446d-e107-3cd4-954d-fb1cf5a13344 | -11.0117 | -55.0358 | 2025-06-16 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 74a9b91e-4cb7-3009-b7e9-940bddad938d | -11.1571 | -53.9206 | 2025-06-16 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 6807d711-7b9d-333d-8b5f-0427531797ed | -4.7707 | -47.2624 | 2025-06-16 00:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| ac58dafb-03cb-386c-b16f-d3ecce71f3fd | -11.0115 | -55.0561 | 2025-06-16 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 349.3 |
| 8af7f8c7-0d12-30d9-9be9-e98b177189f4 | -7.1357 | -44.0322 | 2025-06-16 00:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 42.2 |
| f6a332de-254e-3b47-a929-ec093644166e | -11.1382 | -53.9223 | 2025-06-16 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 8edbf3bb-3f46-3116-a118-e84442301e48 | -11.1568 | -53.9411 | 2025-06-16 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 158.9 |
| 9da2b0f1-cbb7-3460-a71c-5044d52a2bf7 | -7.1172 | -44.0108 | 2025-06-16 00:00:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 4154b5ae-5e44-351a-813f-fa68e7f8de38 | -10.9926 | -55.0577 | 2025-06-16 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 8bb4f23d-bb0b-3c82-bb72-424c8b66c6d2 | -11.0113 | -55.0764 | 2025-06-16 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 8f040e9d-dd45-3719-87f2-9c50958615fe | -7.1169 | -44.0339 | 2025-06-16 00:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 146.5 |
| f21611af-291d-3ca0-b14f-1fcc9eef75a3 | -11.0113 | -55.0764 | 2025-06-16 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 73583484-017f-3cd9-a903-54533b6a53cc | -10.9929 | -55.0374 | 2025-06-16 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b3294cca-a351-31d3-ace6-08eccc0be2aa | -11.1571 | -53.9206 | 2025-06-16 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 0bb80a75-a96f-3848-8df2-bef6c63880be | -11.0115 | -55.0561 | 2025-06-16 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 259.9 |
| 775592fd-dd72-32bf-8e37-1cd44261fc72 | -11.0304 | -55.0545 | 2025-06-16 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 8a84e685-dc37-3303-a42d-df5f446925b3 | -11.0117 | -55.0358 | 2025-06-16 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 3f2f0eee-45fc-3b2c-a608-c837f5a72570 | -11.1379 | -53.9429 | 2025-06-16 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 230.5 |
| 73fdf1f1-ff61-34b0-97d4-aefd852c7d69 | -11.1382 | -53.9223 | 2025-06-16 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| e6f602a4-1c44-3692-824f-b74740b13357 | -10.9926 | -55.0577 | 2025-06-16 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 21ed3378-c696-3756-a988-5d363a3366f0 | -11.1568 | -53.9411 | 2025-06-16 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 06903648-54d1-3359-bef0-fa2040589482 | -10.0736 | -52.726501 | 2025-06-16 00:10:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c5f22d9-c08f-3d92-b7e1-283ea7019ed6 | -12.762 | -44.394299 | 2025-06-16 00:10:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6717e283-65a8-39e0-ba3d-ca2cd74c786d | -11.4069 | -47.623402 | 2025-06-16 00:10:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22269a5a-1a84-3939-a0a9-a36e8824e7e9 | -12.9869 | -48.636002 | 2025-06-16 00:10:00 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6addd095-4737-3903-b5e4-d814e246dbff | -15.4041 | -47.852299 | 2025-06-16 00:10:00 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 026a2ef3-cd35-3ff1-9245-726584e911d0 | -12.7652 | -44.408699 | 2025-06-16 00:10:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d8eb069e-703f-3374-b41f-1ed3a5819185 | -12.0564 | -48.065498 | 2025-06-16 00:10:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eedc19c7-7ac6-350a-b972-7bea2232b940 | -13.9181 | -54.598301 | 2025-06-16 00:10:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d36ab40-cde3-3733-9b40-f49c2f67fb84 | -11.144 | -53.914101 | 2025-06-16 00:10:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bcb34d32-8216-3f59-af08-ebc79e20b9ac | -4.78 | -47.253101 | 2025-06-16 00:10:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c7304054-b4c3-3669-adf1-113d3ce37c19 | -11.0032 | -55.053501 | 2025-06-16 00:10:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f38ae23-d756-3516-aa6d-6270849d4c4e | -12.7636 | -44.401501 | 2025-06-16 00:10:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3741cbc2-61fc-36d3-b297-1d0a3c83e28b | -11.176 | -47.7906 | 2025-06-16 00:10:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d8f659e-ad8e-36a8-a3c6-b8d7b400cf78 | -8.7475 | -47.172199 | 2025-06-16 00:10:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3712206c-0289-35e7-af0c-667aa8b234d0 | -11.0251 | -44.6474 | 2025-06-16 00:10:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c7904b4-1a62-3135-8f0c-c2bb21ac4e0a | -22.6737 | -42.848499 | 2025-06-16 00:10:00 | METOP-B | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f7a33ac5-fd92-355f-9581-4d0f0be48c34 | -10.0931 | -52.7225 | 2025-06-16 00:10:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c296289c-6187-3931-a101-2e4ef9b63c6f | -11.0052 | -55.012001 | 2025-06-16 00:10:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 13a8adbd-d252-38c8-a5a4-850db215e856 | -10.0904 | -52.709301 | 2025-06-16 00:10:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d52ad4a-58fe-330d-9fcb-37b1adb09891 | -7.1055 | -44.015701 | 2025-06-16 00:10:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 571e91eb-343c-3dc2-9c00-60d6422aa810 | -12.9771 | -48.6381 | 2025-06-16 00:10:00 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c69483f-9338-315e-8fda-9d2bfa0f2015 | -11.1343 | -53.9161 | 2025-06-16 00:10:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a236407-1e44-3de8-95cb-74b93a7220b8 | -10.0152 | -48.217098 | 2025-06-16 00:10:00 | METOP-B | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86709eb5-3894-3104-82d0-095971cfd35a | -7.1073 | -44.023701 | 2025-06-16 00:10:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c86fb776-7a6a-3229-a8c3-94dbbd748cb4 | -10.9994 | -55.033699 | 2025-06-16 00:10:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 99f2cf43-eb33-3039-8b66-2c4d0507cd6d | -15.4023 | -47.844101 | 2025-06-16 00:10:00 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 53ed8e50-56e6-393d-9ca2-1a13f537b491 | -4.7785 | -47.2463 | 2025-06-16 00:10:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2626d911-bb2c-33fc-b34e-28abf2035f5f | -7.119 | -44.0294 | 2025-06-16 00:10:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6d5fe7b7-89e0-3353-a5d8-47f55c9bffc2 | -5.3232 | -49.273399 | 2025-06-16 00:10:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17a5ef8b-c44a-3dd3-beac-c334e68ceb5f | -7.9281 | -47.794399 | 2025-06-16 00:10:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca00b66d-0a64-367f-97ef-cabddb075461 | -9.4022 | -48.421902 | 2025-06-16 00:10:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e56dbfdc-39d3-3efa-8a16-62f52a4f9bca | -11.1407 | -53.897499 | 2025-06-16 00:10:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c65e889-7164-33ca-bffb-b041e2c42e4b | -7.1288 | -44.027199 | 2025-06-16 00:10:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| db9b466f-0600-3a83-bc94-3015534e3ee2 | -15.419 | -47.874901 | 2025-06-16 00:10:00 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a17dcc22-c3f8-36ac-8365-7df0ba33058c | -9.1675 | -45.321701 | 2025-06-16 00:10:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6469bc34-6306-3a28-8b54-fe51c249c019 | -11.1473 | -53.930801 | 2025-06-16 00:10:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01d95b18-ce44-32fe-b11d-423649526078 | -7.1092 | -44.0317 | 2025-06-16 00:10:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2a934c24-db68-3dc7-a7f5-d1584ec05568 | -5.3249 | -49.2808 | 2025-06-16 00:10:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 346feedc-5e7c-371b-89f0-02f6f181c5a9 | -11.0235 | -44.640202 | 2025-06-16 00:10:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c7f704d1-06b3-3981-8a0c-c8cfe63014af | -22.675301 | -42.8559 | 2025-06-16 00:10:00 | METOP-B | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7f66f7dd-0243-3ea3-990b-46dd141a2968 | -11.1776 | -47.798 | 2025-06-16 00:10:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55be3d3f-892e-35f8-96c4-9c7b4ae49c58 | -7.111 | -44.0397 | 2025-06-16 00:10:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f8dc5c8-08ef-39c3-9632-055fa6db67a8 | -11.1375 | -53.932701 | 2025-06-16 00:10:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33cf2786-8785-3e2d-b9d3-e1aafc6a9fa5 | -7.9297 | -47.801498 | 2025-06-16 00:10:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7881733-61f8-38f3-9ed5-55f19df39b5c | -7.1208 | -44.037399 | 2025-06-16 00:10:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d81cd7a8-e090-39fb-967f-a93945fda965 | -12.0883 | -49.479301 | 2025-06-16 00:10:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 962813b4-18c1-3473-842d-17b14c26424b | -9.4137 | -48.427299 | 2025-06-16 00:10:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 672da364-fc03-399b-9cb2-f8a3c066c24f | -7.1171 | -44.0214 | 2025-06-16 00:10:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aa50864a-8c7e-3762-aae8-149477141a3c | -10.8287 | -46.951302 | 2025-06-16 00:10:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38afd8fe-cf7d-3e4b-babd-9ebfade6ac59 | -10.1029 | -52.720501 | 2025-06-16 00:10:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0541243-c5b3-389b-ad4a-57c8b8d72230 | -12.058 | -48.0732 | 2025-06-16 00:10:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1d25a33-9baf-3831-b427-d141a42c4323 | -10.9955 | -55.013901 | 2025-06-16 00:10:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0474554-97d1-3914-8d8b-100dfc2f9e5b | -11.0333 | -44.638 | 2025-06-16 00:10:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c3826fd1-4b72-36c5-b1fe-f21b5582b3cd | -10.0958 | -52.735802 | 2025-06-16 00:10:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 995f56be-801a-39c1-8837-b8d8dae6270b | -11.0129 | -55.051601 | 2025-06-16 00:10:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 542f6903-0ca5-365e-b432-297dd93f01fe | -11.1382 | -53.9223 | 2025-06-16 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| d573d643-b0c7-3ab9-8cfa-e395496686bc | -11.1568 | -53.9411 | 2025-06-16 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 54466521-3a72-3509-a0c9-74480615dcc5 | -10.0972 | -52.7376 | 2025-06-16 00:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 7a6874d4-1e65-3f45-ab30-768a5f52a56c | -11.0117 | -55.0358 | 2025-06-16 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 34eb3b6c-231e-3679-a1e7-64523918620a | -10.9926 | -55.0577 | 2025-06-16 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| b614d853-7a1f-33d1-8c61-15466782bd73 | -11.0113 | -55.0764 | 2025-06-16 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 9d357742-7f33-33a7-9c24-848839704f13 | -11.1379 | -53.9429 | 2025-06-16 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 248.4 |
| 0e958e87-f446-3b0d-a1c0-9d20a695b180 | -11.0304 | -55.0545 | 2025-06-16 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 88c502cd-add0-3847-a871-d5b7a1fde706 | -11.0115 | -55.0561 | 2025-06-16 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 257.3 |
| 8058d539-5ac1-3733-ba97-f483464a99e6 | -11.1379 | -53.9429 | 2025-06-16 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 03f5af10-3b92-3bfa-8e26-ff5272bfd436 | -11.0115 | -55.0561 | 2025-06-16 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 209.6 |
| 759f007a-f174-317a-ab29-e2f92e7955e4 | -11.0117 | -55.0358 | 2025-06-16 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| dda73ad7-e7b1-3662-9179-a65a587675bf | -7.1357 | -44.0322 | 2025-06-16 00:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 43.9 |
| ba2e9243-6c8f-37d4-b3e3-dbee2e4723c4 | -10.9926 | -55.0577 | 2025-06-16 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 8ad247f6-fd1a-3c3e-afb1-4e2afd6bb9c9 | -7.1169 | -44.0339 | 2025-06-16 00:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| c3484ea3-544f-3774-b584-93c7dc3be6cc | -11.0113 | -55.0764 | 2025-06-16 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 62d49212-538b-37d7-b0d6-53c85c05f44a | -17.4596 | -48.1613 | 2025-06-16 00:30:00 | GOES-19 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 3c12a4f0-889a-30fa-8c94-175087cc0544 | -11.1568 | -53.9411 | 2025-06-16 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| a26197bb-e15b-3a1c-a11f-f492a3a7e002 | -11.1382 | -53.9223 | 2025-06-16 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| f785812b-ec9b-370b-a27e-213ce5acd09e | -7.1172 | -44.0108 | 2025-06-16 00:30:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 2ebb026c-20c0-359c-9728-0bcabcb4d400 | -10.0972 | -52.7376 | 2025-06-16 00:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |


[Clique aqui para ver as próximas entradas](README2.md)
