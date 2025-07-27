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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1299737f-846e-393d-842a-333fbb4dfdb5 | -8.29239 | -45.00401 | 2025-07-27 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73033c0c-a287-33d6-aaa1-015469d3c0a2 | -6.41772 | -41.14569 | 2025-07-27 03:45:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4c5b0386-5590-3e9d-8d7f-f7e49bcc36b5 | -8.95655 | -37.19666 | 2025-07-27 03:45:00 | NPP-375D | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8178a538-fb71-3dcc-ba03-9b09b49fab64 | -5.67902 | -43.66671 | 2025-07-27 03:45:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b1889d7-981c-309e-bcfb-157f860f841b | -4.04601 | -42.52434 | 2025-07-27 03:45:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 09a911bd-2701-32e0-ba66-156556736221 | -8.30321 | -45.00614 | 2025-07-27 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ae7f454-e310-306a-b850-9f6e443ec86e | -6.69869 | -43.07333 | 2025-07-27 03:45:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5587b459-99fb-3667-a762-9a811263d4fb | -7.00384 | -42.34769 | 2025-07-27 03:45:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 890e0bfe-bd8f-3524-ad14-7ab4660dc9e4 | -5.60528 | -45.07904 | 2025-07-27 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17002327-8769-32ee-aca7-582862bbdb9c | -5.78027 | -43.61184 | 2025-07-27 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c51648e7-88fd-381b-a31c-f22ba37f8e94 | -5.18702 | -44.95426 | 2025-07-27 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c1f5754-e38b-3e58-b3df-1a09227a137e | -6.55434 | -41.50299 | 2025-07-27 03:45:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e84269ae-5b96-367e-ae56-a63940f45050 | -3.40115 | -47.50318 | 2025-07-27 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc465b06-abeb-3297-a96e-3663a48af161 | -8.17472 | -43.19378 | 2025-07-27 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f746bdf6-1410-3b5c-8336-3c687a9b8d51 | -9.99942 | -44.36942 | 2025-07-27 03:45:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc626be2-96df-36d7-b732-9da02c9dae01 | -6.67447 | -43.96859 | 2025-07-27 03:45:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86aa6f10-4866-39b3-991c-df38e3b0db85 | -3.39543 | -47.49554 | 2025-07-27 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d872c9db-2ff4-30ba-859d-b41968334a5a | -4.1094 | -48.21294 | 2025-07-27 03:45:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7424abaf-fcda-32be-a3a2-650a00950ac1 | -5.67409 | -42.79889 | 2025-07-27 03:45:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 541a84e4-7853-3cd0-98d8-5d79f11df08f | -8.29299 | -45.00789 | 2025-07-27 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49fed508-84c7-37ff-9c17-86d1b6d873f1 | -5.18482 | -44.96003 | 2025-07-27 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 17847de8-273b-3ae5-a0f6-ca6ffb639b10 | -6.89193 | -44.8065 | 2025-07-27 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bd1b0fe-03e5-3007-8a8c-1f2e85a42708 | -7.09599 | -44.04791 | 2025-07-27 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9862555-acd8-3102-9413-fae54721a615 | -5.68422 | -43.66752 | 2025-07-27 03:45:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 503b03e9-5ac6-31be-ac04-c089acee8d25 | -6.89213 | -43.11182 | 2025-07-27 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46ade788-d1e9-34c4-a8c4-8f6ca44d4543 | -4.10932 | -47.94016 | 2025-07-27 03:45:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d813b5b1-b99b-3179-989a-fc2b06c0e169 | -6.23041 | -44.5257 | 2025-07-27 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28f267af-24f2-315e-a212-bc8a8462ae77 | -4.10606 | -48.2078 | 2025-07-27 03:45:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76494485-e451-382a-b55a-edc3490c7183 | -6.01411 | -44.05396 | 2025-07-27 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4af6772a-9739-3eb9-8ec9-bc720f89d3d4 | -6.56607 | -41.51387 | 2025-07-27 03:45:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bcdcd0d1-bfd9-31da-a919-e45d838625c5 | -8.17376 | -43.19904 | 2025-07-27 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ac1e3ff7-6120-3437-9efb-e6e012a814e2 | -6.22934 | -44.52568 | 2025-07-27 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b9bc38cf-49c9-3178-9356-e87a40d56cca | -4.07868 | -42.54126 | 2025-07-27 03:45:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e09571f0-00aa-3263-9987-097708023bce | -6.66872 | -43.97071 | 2025-07-27 03:45:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39bdf5e3-7795-3f69-8b73-e16da8a43e07 | -5.77562 | -43.60803 | 2025-07-27 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 392e9cb1-b52b-30f8-b3d9-44a744061cea | -6.54993 | -41.50227 | 2025-07-27 03:45:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b275d7e5-95e3-3828-9fc9-dfee81aa3019 | -6.23975 | -44.05557 | 2025-07-27 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b18293d8-ace1-3c4d-9211-09e5c78f612e | -9.38558 | -40.26669 | 2025-07-27 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4c59781c-294b-3fbb-b2e0-dc4c3b4dc401 | -8.30923 | -45.01102 | 2025-07-27 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a95d67b0-ec04-3b69-a1ba-d2e397ebc6fd | -7.29291 | -43.08229 | 2025-07-27 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2acaf621-3177-3539-b8bb-1706ba895155 | -6.67503 | -43.96546 | 2025-07-27 03:45:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 921f182d-ddcb-3fd8-b087-1b4b090b21bb | -4.61549 | -43.3239 | 2025-07-27 03:45:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed84e1e6-39e6-3890-8abf-4402b7c8c361 | -4.95938 | -43.73112 | 2025-07-27 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2aecebb8-8fbd-3aa7-8873-9c0eaa465f56 | -6.55949 | -41.49941 | 2025-07-27 03:45:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01657477-8489-3147-86ed-876de804b751 | -5.7751 | -43.61099 | 2025-07-27 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8aed0f87-ec6c-3930-b747-8652f7cf4e93 | -4.95882 | -43.73441 | 2025-07-27 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a5d574a1-b17e-3132-99af-1c9a44344518 | -6.40909 | -41.14426 | 2025-07-27 03:45:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dd10abf5-200e-3932-8e6c-3931a9d5321e | -3.38859 | -47.49435 | 2025-07-27 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62f8e905-b6e2-3c82-9678-ec874d3474ff | -5.2462 | -38.20187 | 2025-07-27 03:45:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a1d6f03d-417e-3d74-9091-9771963e8c18 | -6.5649 | -36.59875 | 2025-07-27 03:45:00 | NPP-375D | CARNAÚBA DOS DANTAS | RIO GRANDE DO NORTE | Brasil | 2402402 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c09b8ee1-19da-3d84-b12c-e1bdfa20b799 | -6.06029 | -42.94096 | 2025-07-27 03:45:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 35ae3a82-cd85-3037-aed1-728300d80cff | -6.67391 | -43.97172 | 2025-07-27 03:45:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19cd4f29-2b6e-3ae6-a24d-97d942a49593 | -6.66816 | -43.97385 | 2025-07-27 03:45:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b1c102a-b006-3d9e-b03d-5a4bfd6bbf4e | -6.86431 | -43.68493 | 2025-07-27 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 404f694d-5fa3-3d0e-9de0-68e2661f6445 | -3.13018 | -47.01504 | 2025-07-27 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 261a53ad-8350-3d0e-ae49-67b1415cfbb8 | -3.12601 | -47.01446 | 2025-07-27 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4669b39b-9647-3290-afbe-7e2be40acc3d | -6.89378 | -43.11385 | 2025-07-27 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19ae22fa-2bad-3424-8d2e-a83263a29c8d | -7.28323 | -43.08052 | 2025-07-27 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 09050dcd-74f1-399d-a84d-c86dc629b593 | -4.05988 | -42.53237 | 2025-07-27 03:45:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b0f97db-fe59-3e41-898c-639571cd3174 | -3.39433 | -47.50187 | 2025-07-27 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 31a93d3f-3720-3c96-9dc7-e7cc6b2b7973 | -8.30445 | -45.00656 | 2025-07-27 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4aecc877-12d0-3c14-9714-bfa692cecd9b | -10.43357 | -44.18628 | 2025-07-27 03:47:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a79c9f90-0a9e-3eaa-ac93-7f40ff532c2f | -21.33907 | -45.6386 | 2025-07-27 03:47:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ddad15e5-3507-30d6-9928-c5fb206bfaf8 | -11.11139 | -45.1232 | 2025-07-27 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e554651a-682b-3352-8429-8ce585d594db | -13.12329 | -47.35873 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49416241-4ece-32d3-8518-ebb9bd1fa2ab | -14.22004 | -43.94913 | 2025-07-27 03:47:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5be9d007-932b-3306-a8f1-f0d709cf3ea3 | -15.03895 | -49.25766 | 2025-07-27 03:47:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e29b33f-d47e-364c-b7aa-ce8e4ee9f9b9 | -13.13604 | -47.3294 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2ec50ac-e851-3733-a22f-f928c9743b02 | -13.49028 | -45.50337 | 2025-07-27 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2f3ae55d-fb58-3879-8cf5-8c76a8bbc2a6 | -17.24575 | -46.90584 | 2025-07-27 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1119172e-c36e-323f-b526-652a782d5d40 | -23.06492 | -49.6713 | 2025-07-27 03:47:00 | NPP-375D | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8124996c-7152-3b23-895d-3315c95b8695 | -12.71785 | -46.27085 | 2025-07-27 03:47:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc4a5871-5011-3095-a8ed-e257b65a9217 | -15.26618 | -43.076 | 2025-07-27 03:47:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fb527bd2-a3b7-3ac0-9ec4-26b6bb317c94 | -12.70889 | -45.02836 | 2025-07-27 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc564e8f-fcd4-3fcd-8c26-5dccfbaa2e41 | -13.48967 | -45.50645 | 2025-07-27 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8a5c0321-d464-3adc-959b-e333f2087972 | -22.98764 | -46.47309 | 2025-07-27 03:47:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 01383db5-61a0-3843-b172-5129644bb311 | -16.09187 | -41.26539 | 2025-07-27 03:47:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bf7a6615-b195-3c08-83b8-f3062165ea6a | -17.20996 | -44.85378 | 2025-07-27 03:47:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4c57f31-b6bf-3c67-a403-ef6aa8a4aee3 | -12.04583 | -45.84793 | 2025-07-27 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 14c0964f-9b6d-3cd7-9078-2657d406018c | -11.96514 | -46.71123 | 2025-07-27 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| adf17845-1df8-3c61-ba4d-c656be641e3c | -12.7118 | -46.27283 | 2025-07-27 03:47:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fc6bf0c-346b-3e68-b71d-7d81a75e7311 | -13.488 | -45.506 | 2025-07-27 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e5dc9012-e18e-3698-8803-9b3a7bda46cf | -20.35002 | -45.99248 | 2025-07-27 03:47:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6d8b2b9-ae55-379d-af04-4d4cdea9c285 | -12.6899 | -47.01469 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e40d85bf-a054-32bb-ba56-0911728b405e | -16.25958 | -47.81988 | 2025-07-27 03:47:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5ef8f3c-3055-332f-9ec6-690c6385a6e5 | -13.13584 | -47.32676 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b82ddd3-5693-38bb-9021-dc323e5d1fa8 | -16.4102 | -48.92743 | 2025-07-27 03:47:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6524eece-6f8f-3bbd-9739-e5ff2f3735f8 | -13.13523 | -47.3335 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4a9b5a43-5cdb-3e36-91b7-847cfc2e09ca | -16.41118 | -48.92285 | 2025-07-27 03:47:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| da85dc0d-04c7-3b20-a459-8b7cd4b3c4d8 | -21.34351 | -45.63958 | 2025-07-27 03:47:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4c564f7a-cd37-347e-b93b-cf0423b70bf6 | -12.68346 | -47.01718 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec3ddadf-7da0-306d-bb85-dd189844485d | -11.9656 | -46.71529 | 2025-07-27 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c42c152-ea04-3d9a-b161-768c2eec98d9 | -13.12364 | -47.36174 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec4de76d-7aa7-3a72-9f10-631ad1efb393 | -12.70754 | -45.02686 | 2025-07-27 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9b348a4-b169-3961-8ef8-5b342e36447c | -12.67942 | -47.0077 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e412122b-f545-3d1f-8d0b-78524891c040 | -15.27038 | -43.07692 | 2025-07-27 03:47:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 36cd7478-79fc-3858-99e9-d9b9ab1beba7 | -13.12043 | -47.34748 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be6f77fc-19af-3aca-9f56-4b540f7809ee | -12.67773 | -47.01613 | 2025-07-27 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8c52bcd-0045-302f-8093-17fc3318ec81 | -14.20838 | -42.01931 | 2025-07-27 03:47:00 | NPP-375D | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 42142133-790a-3376-a2ba-22955347a3b1 | -12.00363 | -45.83606 | 2025-07-27 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README6.md)
