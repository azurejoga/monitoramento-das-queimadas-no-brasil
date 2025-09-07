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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1a4b085-8c1e-3939-af71-beab5767fcdb | -5.43732 | -42.80961 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7cdf2d28-1da8-3b8c-8f0a-282d2ca6a346 | -5.43675 | -42.81327 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3815ca73-2567-3a1a-ad4e-1cea5bd629e9 | -5.03887 | -45.31972 | 2025-09-07 04:17:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0897b27e-0fd3-3161-8a09-f29d0aa6e589 | -5.30868 | -42.78262 | 2025-09-07 04:17:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59d5ecbd-8532-387e-90e0-71fc7e9ff9a9 | -5.3782 | -45.97475 | 2025-09-07 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 254cc105-1c39-376c-add5-b87424d9e011 | -5.44619 | -42.8029 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b14196f3-454c-38d8-9a72-52244747d432 | -6.39245 | -38.90975 | 2025-09-07 04:17:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fcd83819-2fbd-39bc-aaaf-a7fe24bb448d | -5.04035 | -45.45662 | 2025-09-07 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6381bc6-9c88-321e-9c05-956469e0ce4d | -5.72831 | -43.89838 | 2025-09-07 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0473a722-da8c-392b-bab3-ad076ac6e91e | -5.76026 | -43.12532 | 2025-09-07 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a4bbe6e2-9f68-332a-b70b-1eb87cb95a1e | -5.24862 | -42.72097 | 2025-09-07 04:17:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e9969b04-5127-3536-a5b6-492bb9920dee | -5.46148 | -42.81652 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ae54b16e-c837-3c60-97cf-4f9eb0648f6d | -5.52901 | -43.08235 | 2025-09-07 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf96335c-c727-3e07-b733-c2b09bddd19e | -5.21697 | -43.69345 | 2025-09-07 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 070a194a-ee59-3b65-b8be-b6a598e66ab1 | -5.52845 | -43.08595 | 2025-09-07 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cd04005-c29e-3bb6-87cd-cac925a6c36c | -3.24207 | -50.80791 | 2025-09-07 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2a54454e-823b-3cb7-8d50-6f9cf1e80e34 | -4.80397 | -43.05622 | 2025-09-07 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8c22f862-9ad5-3c70-8915-43e5fb3f986e | -4.48185 | -48.11828 | 2025-09-07 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 25d0be4f-55e0-3673-8700-77403e1bb120 | -5.37721 | -42.63505 | 2025-09-07 04:17:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3d233d87-3122-30dd-ae55-ee44ce001bbd | -4.17152 | -42.02762 | 2025-09-07 04:17:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e05fe2fc-aaba-31c8-9477-f8539549d002 | -5.75744 | -43.12119 | 2025-09-07 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 29de4d8e-111d-34cf-ad60-a014f45802e1 | -3.35295 | -39.27737 | 2025-09-07 04:17:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 69ecd581-ffb8-34a5-9291-e132c7441986 | -5.43636 | -42.65934 | 2025-09-07 04:17:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9a3e0761-3ec6-3735-8067-43a787fa2020 | -5.75382 | -43.7128 | 2025-09-07 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33581646-c889-33ac-b1e2-23f921fea58b | -5.45865 | -42.81235 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f9c21594-a726-348a-8993-97120a1322b5 | -3.88053 | -43.16331 | 2025-09-07 04:17:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7c92fee-a359-3997-9302-1264d41a5ba6 | -5.73224 | -43.91682 | 2025-09-07 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcdd15df-9529-3680-acb0-3d8616392e62 | -5.21642 | -43.69695 | 2025-09-07 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 67cea697-7b0a-3cd4-bfd0-4fb5f3283cd9 | -5.83407 | -37.99862 | 2025-09-07 04:17:00 | NOAA-20 | SEVERIANO MELO | RIO GRANDE DO NORTE | Brasil | 2413607 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 08024ba8-f6a2-3b9e-9f38-c9cb9ddf341b | -5.8617 | -42.42056 | 2025-09-07 04:17:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 03fb7f02-d7b7-39ec-b21e-f04758d19356 | -5.3723 | -45.98117 | 2025-09-07 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0e2de0c-bb41-3c0e-b8e8-12839f462fcd | -2.43305 | -49.30919 | 2025-09-07 04:17:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a91b69e9-6d2b-3791-80e0-a85c8538ef98 | -3.82299 | -54.12682 | 2025-09-07 04:17:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0434eec-b93c-3b07-b35b-1a7cdb9a4532 | -3.81738 | -54.12572 | 2025-09-07 04:17:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52233641-f326-3d63-a547-ac2a83e3bdcf | -6.1857 | -42.63818 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7c96fa36-452d-3392-b260-e0706be8bc1a | -7.59308 | -44.69686 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4096144e-58ed-3e41-8352-ed2471f2c15d | -7.17665 | -46.18935 | 2025-09-07 04:19:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 887c53d7-43ab-3fbb-a861-7623d71f42fd | -6.60361 | -48.05523 | 2025-09-07 04:19:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9f09005f-748d-308f-870c-000da43222c3 | -7.71249 | -50.33448 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 34dc7835-afbe-38b9-a0f7-54546fadf4ae | -6.25537 | -43.50158 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5aa9076c-973d-3ecf-b1b1-fae788f47358 | -6.32246 | -42.19764 | 2025-09-07 04:19:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7ff9b19a-ccd9-3109-a212-07f6cc92f442 | -9.81589 | -46.01967 | 2025-09-07 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 268e8c89-1b92-398c-8421-f4ce1385848e | -11.14784 | -48.38896 | 2025-09-07 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 455fdf9d-28bf-3508-baf9-f08e7b5c2746 | -7.40204 | -44.96114 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bf48a31-da4c-3569-bf68-ba66ab17559a | -11.15685 | -48.37809 | 2025-09-07 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37947ef7-8e31-3aae-b2e4-749b00a13121 | -7.71779 | -44.72366 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd3d3397-2671-34ac-a4d5-76e42c4211bd | -11.58938 | -47.72983 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddeac628-07e6-3d49-baa1-26f40e94664f | -5.96836 | -53.59423 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 533d0b9c-ab77-3820-80cc-f6f266ccb106 | -11.21317 | -55.01511 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc7a3961-142b-3f29-9d19-a962bc08acb5 | -6.19754 | -45.03924 | 2025-09-07 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94ff2452-3e6b-3cdb-bbf3-547b4fc4fcdd | -11.40895 | -43.60706 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49cd293b-ea49-3188-bcfe-0c43032c3985 | -11.40263 | -43.6258 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fe9933b4-61f3-3a74-8aaf-528baa709920 | -7.26133 | -47.44723 | 2025-09-07 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7b02264-7876-3726-b996-467acff0a48b | -6.55248 | -42.93956 | 2025-09-07 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a799d2b1-dd79-3bd1-a995-ae833065d1fc | -7.84473 | -44.93186 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63905573-fc2a-3f4f-9c83-312380f62f3e | -11.37451 | -43.53879 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ea4e2c6-dcc6-347f-98dc-9f1dfbd9c46f | -7.0161 | -44.97431 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a18f2406-f82b-39db-9836-bcc1e671e00f | -7.59362 | -44.6934 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fa097f9-d0a7-3c43-b7a9-2495d4a03fb0 | -7.76439 | -50.76028 | 2025-09-07 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 30a17343-d977-31cf-9208-d7bbbdd259b5 | -6.18429 | -43.37003 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6f52d3e-7ef3-3691-a132-695e1de3716a | -8.44167 | -47.30503 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f273ff5-8448-30be-928e-a31b142dc2f7 | -6.87819 | -45.54351 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b242bbb4-c336-3567-8dd2-8a6433e8b35d | -6.13948 | -44.24382 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4701e90e-7dbb-3cce-8983-4418a2c63a1e | -6.73156 | -50.45524 | 2025-09-07 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fa947bc-a439-38b3-82e6-025d5773eee9 | -6.18766 | -45.4227 | 2025-09-07 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2a3ceba2-6b57-36c6-bd84-def7a3673eef | -7.34435 | -44.31193 | 2025-09-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b331c986-2b7b-32ba-9587-b27960d157ba | -7.40207 | -44.98245 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0c70d21-2b99-34cc-9b6b-0255a0e9a63c | -12.00982 | -47.77615 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 913ffafb-18c0-3413-93b3-25b48bde872f | -8.02888 | -43.81403 | 2025-09-07 04:19:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dfa6f2a5-c75a-382d-92cb-960e4a943672 | -11.90122 | -46.64099 | 2025-09-07 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1294cbca-9fc6-3ed7-a5d3-8f44791a5bae | -6.18322 | -45.42916 | 2025-09-07 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e39e1277-d47f-31a1-8c6e-eae6b8f85247 | -7.21767 | -43.99088 | 2025-09-07 04:19:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 201685c2-96db-3390-b7a9-abec11ad5db3 | -9.83357 | -46.5474 | 2025-09-07 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ada6c3ce-7b37-375f-8e01-ff58b181ce20 | -9.06243 | -50.45231 | 2025-09-07 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b5dc39b-efdd-3407-916c-9c11a086bba6 | -5.86735 | -51.95156 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 45ec8b55-79a3-38ae-b964-26ae0c63c0ab | -5.95376 | -53.80074 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2400e50-9da3-3a42-a253-65dd74357af7 | -11.57328 | -47.74256 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28791709-4549-3a53-bc00-363a6e7952c8 | -10.7391 | -44.35363 | 2025-09-07 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 153482c6-42d0-3c0b-8370-59aeb7001fc6 | -7.72772 | -44.72523 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e88a8a93-0485-3e96-8777-5f881dbcac31 | -6.21433 | -42.635 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e68cf55e-ef35-39ca-b77a-0bf35f77364d | -10.78257 | -47.72881 | 2025-09-07 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89bdbd9f-b026-3bd7-ae47-7e65a69ca9eb | -10.78351 | -47.7445 | 2025-09-07 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f0a79ed-4a33-3124-b236-d44e2a3033cc | -11.15835 | -48.39092 | 2025-09-07 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8eb88e9d-ca57-3ed5-801a-747cd1451b54 | -6.38332 | -42.98987 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c8e2bc9-9a11-31f2-9da9-bd66b0c2b80d | -7.99297 | -44.50638 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43fb1e91-83d1-3208-8c87-b38451843c3d | -9.87211 | -53.81457 | 2025-09-07 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6779760c-c564-3c0d-a8a8-6c8cfaada271 | -6.20552 | -44.19034 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62e7a9ad-73a0-3616-946c-02c6ea9016a5 | -9.75 | -51.05888 | 2025-09-07 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a1174d4a-f27f-3ac4-9183-e145a9c78662 | -9.84687 | -48.84031 | 2025-09-07 04:19:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f8a75d0-eefa-33b8-b482-c503679480ad | -8.45432 | -45.02895 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd8ef484-8486-3e2c-aebb-33f151a2f510 | -5.56058 | -52.07939 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cc6b90f-b826-3431-8c97-2340e5735eab | -8.11025 | -45.31608 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d94686f6-0f44-355b-b220-8f9b47ea4aa0 | -11.5887 | -47.17062 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9339cca9-3c1f-3a68-a899-7922dce11017 | -11.20853 | -55.0108 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a90db48f-c003-362a-82c0-3b4fad21f239 | -11.40664 | -43.59877 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a69e944-298e-3602-922b-1acf054df4c9 | -11.58534 | -47.17007 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5120f8d2-1fda-35bf-92eb-b10bf8af0e4c | -10.74341 | -48.18201 | 2025-09-07 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 388a4bc2-cc35-382e-9bd3-c2cd8849dca5 | -11.40438 | -43.63785 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af384602-4fe2-3e3d-9913-de99438bd268 | -8.88557 | -47.90879 | 2025-09-07 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50252526-2c4f-3e7b-9fff-fa1b960167fc | -8.6886 | -54.66808 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README42.md)
