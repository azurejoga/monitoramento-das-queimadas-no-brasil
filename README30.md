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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d183600b-a21e-3ee9-9699-46d671adfeed | -8.60973 | -40.31201 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 329ec97f-2545-393d-a8c9-9a0086069210 | -6.24478 | -42.63871 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b11fdf8-cae4-3f23-931a-d7a32142575b | -4.92775 | -43.18 | 2025-09-04 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46833c56-05ac-382d-ac8d-cf4cb083885b | -5.44986 | -42.82039 | 2025-09-04 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e12868d0-b214-362b-8f8b-202948d31b7d | -8.05691 | -44.13261 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e800cc2-0d2c-3428-b075-660aadd92b17 | -6.57998 | -44.55822 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ab1a6a7-b42b-3222-b732-a3402836d76a | -6.76858 | -44.49407 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 994b2d34-ebb1-3c6e-a2cb-b8ed563bc8f0 | -4.07933 | -48.04483 | 2025-09-04 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb91d52c-981f-3161-86b0-fac11ee3d766 | -6.91972 | -45.5536 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82f8535b-c479-33ca-a499-82091ac1b359 | -6.35309 | -43.76344 | 2025-09-04 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33dc802f-32d1-3bd3-9cf8-df42afab5691 | -6.90148 | -43.80005 | 2025-09-04 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1534c8d6-be12-3e4c-90ea-b81be8751969 | -7.72674 | -44.62485 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07a02835-b942-32b6-b011-bdfd52207bf8 | -5.72317 | -45.26716 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f438cd8-f9d8-3083-a3c3-fdb9ef9df61a | -6.8773 | -45.18761 | 2025-09-04 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c26c1459-3d24-3139-ad3b-86555e692d8f | -5.88989 | -43.25706 | 2025-09-04 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9536034-2eeb-3ffe-8cf4-c8f442573c0e | -6.85343 | -44.25959 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 339d94ad-be2b-378f-a237-d277e915a19a | -4.63284 | -42.53028 | 2025-09-04 04:25:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9aa6adcf-35a5-307a-9f46-13d2a41a5414 | -4.83644 | -42.7409 | 2025-09-04 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 49aa2fcc-f4ee-38b3-a25e-0228588a02b7 | -6.87676 | -45.19119 | 2025-09-04 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c9ebc62-8d21-3b00-8fc0-281a324d200b | -7.48144 | -44.78759 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72cc9f9a-f1ac-3edd-944b-b911e182eee6 | -5.39208 | -55.91312 | 2025-09-04 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f3e46c7-72e6-3854-9b46-399f3dd2eb06 | -6.78495 | -44.08873 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| daa4cf5b-7f79-3083-825e-a7400bd95d51 | -5.68822 | -45.60162 | 2025-09-04 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66d03f13-a39d-3588-9388-dbed6822144c | -8.01996 | -44.13925 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6492e3fa-f18c-3a57-bfc2-70fb5c7cf44f | -6.23259 | -42.43873 | 2025-09-04 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4e3ab1f5-3bce-38de-b9a1-5e32dbb368a1 | -6.88463 | -45.56272 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6840a2e-6ec7-384e-b6ca-1253b96fe283 | -4.33605 | -47.95372 | 2025-09-04 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5159e25d-7069-31d0-94ec-9962284bb69a | -7.50955 | -45.36498 | 2025-09-04 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f66e3ae-113b-345c-8cc4-e685f1ca060b | -6.17644 | -43.32181 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be7ae05b-6ef2-38d1-9f2e-2a69373d7ff9 | -6.28788 | -43.59565 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bad3d8e4-2a5d-3ea1-a83f-7d41e199d394 | -6.30781 | -44.38786 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4f57ca1-d864-3de2-8156-c8763e961068 | -7.54025 | -45.34394 | 2025-09-04 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6837066b-2e3a-364a-a9da-e575e407a920 | -6.69994 | -48.41544 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b407f93-aac7-30bb-bbfa-f0902bd7189e | -6.79191 | -44.08978 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| bd2c7c2c-745d-3142-ac46-c896892d1d9e | -5.68953 | -45.17543 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ac8c26f-dd9d-3363-9d13-e197f397c4b5 | -8.0528 | -44.13608 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0fc99ef-645c-3f16-8df6-08debd14a568 | -6.46495 | -43.97924 | 2025-09-04 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3623baa3-c6cc-35c1-94c3-c8d2ba3fae5e | -7.5497 | -45.72351 | 2025-09-04 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c876fa8b-2293-36a6-a705-a7591eefe537 | -5.78069 | -43.83956 | 2025-09-04 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 959fc0c3-f804-39f2-8d90-ea4c5f543aec | -5.73231 | -45.36203 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2e63f8e-e994-3d74-8c54-a0b56af4730e | -6.59589 | -44.31499 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e20ed992-4d31-3b8c-8a1f-8356dfaf767e | -5.89844 | -45.95743 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fb04118-98dc-3c0d-b131-c714ea32b60a | -5.80015 | -49.12815 | 2025-09-04 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d13320ee-8900-392e-baa9-0d310f8c0034 | -2.20157 | -47.99291 | 2025-09-04 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05486bce-7521-37de-88cd-d56032d1c62b | -6.38002 | -43.00742 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef4269c5-130e-34e4-b462-4cfa82cae082 | -6.49051 | -44.1048 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c4092e30-0b97-312a-907a-d2e9d1e842a8 | -5.85325 | -45.65618 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a71d49cf-31e0-3879-9a57-d0e607282db7 | -5.34846 | -45.09365 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7282fdea-ee9d-3edd-a255-9166a98264b3 | -6.30153 | -44.15215 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 36ba8695-ef2d-30fa-9412-3429b09cccda | -8.01298 | -44.03999 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ed8650a-d228-3773-ba6a-5ba0d3d8bad0 | -5.48448 | -45.22688 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a24a34a7-83a4-3b21-8759-3a9d5a126baf | -6.09425 | -43.26853 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4e6b2bbe-7da2-3158-916e-e416a36e8bdb | -5.2824 | -55.95694 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1199f8d2-90a3-3a6a-a800-1e65185dd189 | -6.67759 | -48.40036 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2714ad0f-6e21-34a4-a2f0-192f9db283ea | -5.70546 | -43.40176 | 2025-09-04 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60e98794-b4a6-36a3-bc93-2533eecea638 | -6.74195 | -45.14484 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e637dbc-57ee-3330-8062-2797374a4842 | -6.12721 | -42.94655 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c75fa57f-66d1-3099-8f24-bac28e30297f | -6.69094 | -48.40617 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dac5fb67-2461-3f33-b517-ee94b3a5bfd0 | -2.9615 | -49.3624 | 2025-09-04 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 6aa77167-77a6-3f94-aaab-1e9a8455e44b | -6.21373 | -43.3907 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cf5b775-5c5c-3453-927f-5cc081df5b13 | -6.74008 | -45.92338 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56afa508-5953-3bf9-9c8e-b30091fdcd09 | -6.87621 | -45.19476 | 2025-09-04 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b317b69-802d-349e-886d-553e45620dde | -6.87741 | -45.56527 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f4a7484-2602-3bb9-aaa5-a7fb3013a920 | -6.26726 | -44.51535 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f2873ef3-d32a-3f6d-82dc-a550b90d31f7 | -6.33614 | -45.67798 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce5ab10f-aab0-3a47-aef1-e780a4562086 | -7.48088 | -44.79127 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58e72e14-daaf-39e9-b249-8ff0f05a77ba | -6.49109 | -44.10094 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34f535e7-b6a3-3ff3-8643-9b15055984bb | -5.9503 | -43.02726 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 41086595-194d-3071-9c29-ce2dbad7e3d6 | -6.54555 | -42.952 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b88accab-d23c-3a58-b309-d155ead1b491 | -6.16209 | -43.31972 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| b06adec4-13ef-359d-87a2-cc00f3e34afa | -6.29 | -43.5092 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a80d6d6-24d3-3e57-a182-b95753b7814b | -5.26667 | -50.76099 | 2025-09-04 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c9fdeb2-58dc-302c-9d22-f44bb554117a | -7.72502 | -44.61279 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93987f3a-4994-32e9-b09d-bf40e9074d77 | -6.23359 | -43.54755 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 026bf521-9436-321f-b5f9-c07e33e2588b | -6.13219 | -44.11533 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0aef88fd-657d-3041-bcfd-7ded187ee7fd | -6.68971 | -48.41373 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6ac35de-efac-3165-be57-d447db3f7e65 | -5.69311 | -45.94314 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 160f300d-ae6c-3e38-adff-abd2f937dcac | -6.74604 | -45.93132 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcad747e-4b9b-3fe5-91d1-23f9d3e0f887 | -6.86896 | -44.82382 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec30f509-bdd2-3461-9aa2-288db4ff2f65 | -5.84376 | -45.62979 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01bb1fd3-cd09-36ac-b9f3-1abc86454501 | -5.31093 | -55.8566 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06ac3988-6a61-341f-82f6-7723410cd971 | -5.30265 | -55.97205 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce4082e0-4840-3b11-9583-af878d55daa0 | -3.43037 | -59.5754 | 2025-09-04 04:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0cac2cf9-42ba-3b6f-990b-3668f8a24aea | -5.86273 | -46.12141 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20af1a28-1382-32ad-9e7b-3020831ce328 | -5.98743 | -43.81406 | 2025-09-04 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f92dc53-fc97-3791-a299-b4b73c24a19d | -5.69504 | -45.16183 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fd6a5cb-525c-318c-8c59-585e9893e5d3 | -6.48655 | -43.57387 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9cbef54-e983-3521-86d2-70f40fee6f60 | -5.92375 | -43.20293 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8a3835e2-9d51-340b-a1ef-5f87b21d6436 | -5.67934 | -45.13042 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f73b2674-0bd7-38f0-97cb-6d930ad4d8e7 | -6.68692 | -48.40936 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 31d86350-d82b-3023-b602-baacc773225d | -6.45387 | -43.98173 | 2025-09-04 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9ed4755-4177-3536-afa4-9766b0111b5b | -6.76313 | -45.93047 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a574ea1-63d7-3411-8fb4-053f0d32228a | -7.05192 | -50.8602 | 2025-09-04 04:25:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f7c5c738-969b-3fe7-b586-d9a465cf6060 | -6.78435 | -44.09262 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65bdf9d1-c1be-3c7b-b033-1ae04462dfb1 | -6.30095 | -44.15595 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6aa75200-9b2e-3e6c-816a-4fa9cc68a468 | -6.0834 | -45.53172 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7036f38-f711-3ed3-ab63-866d88a8e90c | -6.85917 | -44.26841 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71ec007c-a285-36a6-9ac5-6e33389ffbd5 | -4.62424 | -41.40142 | 2025-09-04 04:25:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5ae18600-5870-35d7-a037-67f34b87d4ab | -6.23544 | -43.53548 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b90ed25-37b4-3d33-9ffc-77a964273516 | -6.4557 | -42.39645 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README31.md)
