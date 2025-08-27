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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc671011-76b2-377e-a594-ed7f0e944329 | -8.2572 | -45.11598 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5bedc73-6cbc-3c1c-91df-d74797c9bf3e | -7.64279 | -42.68454 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e7838cfa-d771-36af-a2e2-d94ce908b358 | -6.81591 | -42.81507 | 2025-08-27 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 528037c6-b85d-39ef-b0ae-b7880631c3cc | -8.25631 | -45.12132 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70e8eced-fec1-368f-8ab0-425af48532b4 | -9.08508 | -49.60988 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68bebacc-3fe5-3d2d-befc-b548cb6495e3 | -9.07785 | -49.5703 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99e9a323-2eb3-3e94-9db9-d157914cee55 | -12.90074 | -44.64073 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7cc493a5-bb56-3344-8525-f3f2ab0d6d30 | -11.7703 | -48.99055 | 2025-08-27 04:04:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59a4a05e-e078-3f99-8c11-f067c9391c51 | -13.3974 | -46.91341 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| db817f02-77e0-3942-bdc1-1c11e63bf6a7 | -6.61922 | -53.32877 | 2025-08-27 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0da267ac-aa15-3884-be5e-97defb4c1c5e | -6.62043 | -53.3224 | 2025-08-27 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c4ec257-bb5e-3b5e-9fd8-279aa3a36e60 | -10.7815 | -47.05648 | 2025-08-27 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ffb35cd-b27c-366d-9f21-88ba736d8b17 | -9.08546 | -49.57866 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d59cc90-fcb8-3889-bc9c-8c64cf52afd5 | -11.15493 | -44.79286 | 2025-08-27 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f597d157-ab2d-3c17-8f35-5570a027718b | -9.09795 | -49.57063 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f93cd97a-7b68-3e74-be1b-329489f52432 | -11.80985 | -46.80258 | 2025-08-27 04:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b93f91cc-b400-3a98-8483-0241dc15219a | -12.751 | -48.20168 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b265ca23-4293-3442-b1d2-e2495d1300f1 | -8.90167 | -44.85367 | 2025-08-27 04:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a94e11ca-1dcd-328c-acb5-5dc707466c0f | -8.90062 | -47.32687 | 2025-08-27 04:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19365882-74e8-303d-b214-f527a469cbae | -7.74532 | -50.27871 | 2025-08-27 04:04:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d30e92c7-0d17-3f46-a216-63497879eae5 | -11.20721 | -41.60109 | 2025-08-27 04:04:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 438112e2-b9e5-337e-9b09-e30bd038d2ce | -11.79438 | -51.40641 | 2025-08-27 04:04:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b722188-7980-36a5-8ce2-3acdfef63db9 | -9.86435 | -44.69058 | 2025-08-27 04:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34c0c3a8-056b-38e1-a8f0-fa54e15f6b29 | -9.0765 | -49.6081 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f60e2542-9e8e-3137-9f71-ddd7f180334d | -6.88149 | -44.40263 | 2025-08-27 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0bafe9bc-8a61-3291-8024-db034c347f69 | -9.01537 | -40.33974 | 2025-08-27 04:04:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3d28d6c6-5495-37d1-9636-4f56eeed2a4d | -9.09139 | -49.57631 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bf530bd-99ee-3b49-bdbe-8c59f3a0a65a | -9.1014 | -49.58152 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8167365b-d689-3774-bb83-ac75de7e589d | -12.40991 | -40.46873 | 2025-08-27 04:04:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d367452b-737f-3ed6-99a8-4d5eb7628f89 | -11.76546 | -48.98949 | 2025-08-27 04:04:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5da42dd-3120-32b7-89ad-5c24d033ec05 | -8.89978 | -47.33162 | 2025-08-27 04:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f9eb97c-fa37-3a1e-b5b2-454cee72d474 | -6.49301 | -44.68278 | 2025-08-27 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c1545c1a-9301-3cf9-96de-6546e8e87279 | -7.70654 | -45.7725 | 2025-08-27 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 62125e41-baf5-3e2c-ba8e-58f98bd9e6fc | -13.40656 | -46.88631 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a5b868ab-1122-310f-bf57-f5ad5f13fda6 | -8.86709 | -47.16882 | 2025-08-27 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbca4439-4f5e-3b04-83d8-40d825532193 | -9.09497 | -49.5666 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0788945-69b6-3404-9c15-7d605da63b0e | -8.47215 | -43.65726 | 2025-08-27 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d862462-d06b-37cf-8a57-d803dd55a1f3 | -8.67961 | -47.98828 | 2025-08-27 04:04:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f32507b7-c37a-33d4-9c50-42e5a4ae5ff0 | -13.3981 | -46.90957 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aaccae9a-7db3-3397-a671-bcd98ae4b5a1 | -10.31785 | -46.77414 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 383ac323-9228-3803-943e-e60f929fbb08 | -12.4246 | -46.48481 | 2025-08-27 04:04:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e566ac17-6bb1-379c-86a3-79789477bdfd | -9.09263 | -49.56971 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c580d57f-0e73-35d1-93e7-9cb10452d86c | -12.73099 | -48.18289 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aae6b171-7167-3c55-b6ad-584b05f22b07 | -13.4585 | -46.85733 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2cff183-fb90-3962-a28e-605111151938 | -7.64536 | -42.66884 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a8ace0b8-abb5-3766-90d2-b66a46d4f3a3 | -13.43362 | -46.99735 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1f5f8b5-e16d-3fcc-8d74-0ce825442834 | -7.25969 | -45.35505 | 2025-08-27 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1c6cf166-6f85-32b3-976e-729be4312cdd | -11.82384 | -46.79721 | 2025-08-27 04:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b0098b2-82de-3cd9-9dd1-ed07a15886ee | -13.63732 | -45.70223 | 2025-08-27 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb1aa3f6-0f1e-32cf-b427-0df67d27c34e | -12.76363 | -48.18403 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 90074abf-dbfd-3154-8cc1-a04f57b4552a | -8.27234 | -45.12381 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b32e5d6-bdad-30b6-acbf-61fd9dcd5bc4 | -8.45249 | -43.68497 | 2025-08-27 04:04:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2af5a3a3-d543-3489-84d0-956852c72bba | -9.08788 | -49.57555 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 37d60847-f8d1-3df8-b7b1-84a86ab98b42 | -7.63926 | -42.68397 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 66dd2c16-e607-35d8-aa64-69a11fd57620 | -7.44382 | -46.1306 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8d5e18f-dc08-38f7-b620-8cdd75653aa6 | -13.174 | -45.2951 | 2025-08-27 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5c4e03bc-4fb5-37d5-9630-f5df45e36a64 | -6.71194 | -43.1017 | 2025-08-27 04:04:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f10a3693-cd83-3a05-aac8-4c8fd621d160 | -7.16082 | -43.50257 | 2025-08-27 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9b54f993-9b71-350d-a490-62b88d8cd937 | -7.17367 | -43.84229 | 2025-08-27 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d17106e-63d9-35c1-a0c2-ee7626c03e7d | -13.41461 | -46.86528 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99d6ab18-145c-36b0-8050-9dc03328351b | -12.9014 | -44.65863 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 78b51a1d-0e2b-34ad-b8f7-09bba0abe5e0 | -9.07905 | -49.56371 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c592479b-a941-3076-9557-cabd6c9c6618 | -13.05289 | -46.30281 | 2025-08-27 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f36091ee-ec2b-3f35-a23f-9d7b2d17a681 | -13.43425 | -46.99378 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01e2169a-1ca4-3032-9340-a9d08ce9369e | -13.42377 | -47.00457 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecfe5628-badc-3fc4-8a8d-1e89082e9f54 | -8.55617 | -51.35584 | 2025-08-27 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a33153c1-551b-3813-a136-e0608933b6e1 | -12.42395 | -46.48853 | 2025-08-27 04:04:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d11cfea-cb6b-33e1-9c7c-75b1c3d1591e | -7.47989 | -46.00496 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bcc5ce6-d36f-3247-a7cc-25c79d3f299f | -13.63816 | -45.69743 | 2025-08-27 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f183b5d9-77b0-33c1-92dd-da7be07476bb | -6.87768 | -44.98688 | 2025-08-27 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b6412dd-22e3-39d0-a01d-f40852b4c4d3 | -9.57891 | -45.7328 | 2025-08-27 04:04:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36feefae-9909-3042-a0f7-db3a53fbab4d | -13.67191 | -46.8992 | 2025-08-27 04:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 085ebb79-338f-37a8-bd55-b49f262f7644 | -9.09319 | -49.57652 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bbf61cb0-efdb-3673-b8b5-e3089a284c80 | -8.45974 | -43.664 | 2025-08-27 04:04:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9517d0e2-2f15-3dca-82b7-fc97d1d17045 | -12.79377 | -48.12154 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e7f09b3b-1c9f-3d38-98de-c91b0ca9aa94 | -13.17184 | -45.28517 | 2025-08-27 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 463b7ede-8a11-37af-b469-25be8c6cee35 | -7.01346 | -43.10867 | 2025-08-27 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9c9ace2f-449a-38e3-acf0-86d8d50a56ed | -12.57352 | -43.78834 | 2025-08-27 04:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5730c66-a493-3a73-9ccf-11be55ea0ff8 | -13.38843 | -46.91586 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ead29604-0401-350a-b037-cdda760ca703 | -11.81963 | -46.79643 | 2025-08-27 04:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bdf9f7a5-beac-3c6a-bb6c-1c21c1e1697e | -7.17318 | -43.8444 | 2025-08-27 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62e7a398-fdea-3546-b983-519c6bd7a391 | -13.46817 | -43.74984 | 2025-08-27 04:04:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f25d9233-8a10-31a6-b0f7-a1f69a84ab91 | -6.79439 | -44.35041 | 2025-08-27 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b5f415a-a206-3c24-a1d7-0ba9f73d8bcb | -7.70588 | -45.7764 | 2025-08-27 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3a70d10d-8359-3219-a1a2-cbd1c3761b67 | -9.07726 | -49.57361 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93d1885c-e9eb-3720-bada-d359d10ddcd6 | -9.08076 | -49.58456 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6833f31-edd9-3370-8c1d-54cb8325a2ae | -8.49232 | -44.7387 | 2025-08-27 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a17d90d-2fd9-30ab-b1df-129e531d38fa | -13.45637 | -46.98972 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 017856d5-baaa-3e03-8f0d-6728c12fad05 | -7.12178 | -43.69061 | 2025-08-27 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eaafbdf3-848b-3fa9-803c-c8fcfccee1b3 | -7.44008 | -42.04448 | 2025-08-27 04:04:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4e30641a-2225-314c-beba-bc005615ccf3 | -9.21272 | -46.73204 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39359223-b2fe-3692-92c0-94668d446e02 | -9.09671 | -49.57726 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8cdc3942-25bb-387b-98c4-446b107369f7 | -12.50269 | -47.23806 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ebdf7a1-63f7-3c8f-9f97-3e373c63def6 | -10.7879 | -47.07099 | 2025-08-27 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5f33b89a-323d-39d9-abdd-3dd88c2008d2 | -7.38246 | -47.04191 | 2025-08-27 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7829bcb-2f70-37ef-9cdb-c43ce7d8f9e2 | -12.90429 | -44.6636 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9346bbdf-c5ba-32c9-8d01-1cde382bfbe5 | -7.64858 | -39.0205 | 2025-08-27 04:04:00 | NPP-375D | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a78aa4da-44dc-3ea7-b27c-760b1b16b1c6 | -11.26167 | -44.96141 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e5c811e-0478-3c14-a474-851cb29a7dc1 | -11.58789 | -47.18682 | 2025-08-27 04:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ebe44d6-72b2-3b35-ae08-152c64dcd6c0 | -9.08732 | -49.56877 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README30.md)
