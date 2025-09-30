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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a41762f9-2736-3acb-a6c1-8f685c9ea84f | -9.55629 | -54.63937 | 2025-09-30 04:40:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04e78141-5bdb-393c-8cb4-7e0fe4786b7a | -11.166 | -47.23262 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9144c47c-7622-34a0-964d-5c71e1a00fc7 | -12.84459 | -46.98679 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2288c162-cf4f-3fe3-a7eb-eca8bfffc0d6 | -13.64779 | -48.04607 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9b13fee-20b4-3b95-9e29-8c4cebdda174 | -11.45521 | -44.97871 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a8d0a42e-928a-36c8-80f1-00679791c01f | -11.46124 | -45.00647 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 25278ed7-7a1f-3bc2-b922-ec071c6210d2 | -9.32149 | -49.82695 | 2025-09-30 04:40:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 684ae46a-2635-3855-b5b8-cf0b3c8e2afe | -10.18935 | -44.89851 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 33dc4f63-f1d6-3a2f-bd43-15cbd055ec22 | -11.44873 | -45.03667 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaf7bd3a-1148-3565-ba0e-8598848159c2 | -7.37356 | -47.05064 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8110b5f-daca-381f-946c-8ceb3a1f9877 | -13.83901 | -47.48235 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c8e94bab-1089-30d9-bb7e-ce4da62f6e1a | -12.82392 | -46.99741 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 581f7ffa-6fd9-3b1b-872c-66d8b424fed9 | -12.38178 | -43.89812 | 2025-09-30 04:40:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5830ab6c-d9f8-3114-8234-46ae7a706fea | -7.10827 | -45.5472 | 2025-09-30 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8710fb52-b304-35ea-a7ed-b204cd641fbb | -8.86583 | -46.59084 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6695afe4-4a75-3e4e-8fe8-39ae9b785ef6 | -12.87176 | -46.9575 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6cbf15e0-4eab-3bb3-a583-5c61c52d22e3 | -10.09008 | -46.06773 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8313fcb2-de91-3d0e-ae95-f7d9e5f8f929 | -13.41272 | -47.54118 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1ce87d1-7457-3148-a2e0-159747768728 | -11.25698 | -47.2203 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6dd842d0-344d-3acb-b226-61bbbd7cc0a0 | -9.42386 | -54.72183 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4f211351-5a29-34f1-bb2d-51aa5cb61e47 | -7.92952 | -44.62457 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8e69d90-577e-31ed-b14e-9714bf7d3d52 | -12.87436 | -46.91172 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 51b5176c-eb3b-3f88-ae5c-53da475f21e4 | -11.75193 | -46.8398 | 2025-09-30 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ff198b43-3fc1-3521-a5ee-2551a025d991 | -13.0165 | -49.44982 | 2025-09-30 04:40:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85b20f0b-b0b8-39d7-8392-d0f8df449ebb | -9.93825 | -49.20376 | 2025-09-30 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 715a0313-c33e-3cce-a18f-39ccb1ab0f3a | -7.56253 | -49.84813 | 2025-09-30 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bb92dcd-b95b-3a5b-9454-1f16ce456671 | -13.16104 | -42.35191 | 2025-09-30 04:40:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ffc9ea3-f8f7-33cc-85ca-938153dd4009 | -13.62808 | -48.02986 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1b8c3493-008a-3ac8-bc23-bf9b37b0583f | -13.78905 | -47.94467 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7474ccae-9f07-3b5f-8bc3-918db2bcbe5c | -13.01309 | -44.11372 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c6bbd76d-5e9d-37fb-96c2-b60fa0d8b7cc | -9.75066 | -47.78236 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b866ae93-f328-3ce7-931c-5c47418b0205 | -13.34375 | -47.82016 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63a8d981-eb85-3d27-b556-98d9a64f928d | -10.64064 | -48.57686 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1286449-ee6a-349a-ac06-12cad8898bbc | -11.1528 | -54.11916 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 47827266-fc5e-398a-a8ce-a412a675f683 | -13.39643 | -48.06705 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d5dfa6e9-5a64-35e9-9fff-e5c2fff5da61 | -8.32592 | -50.87926 | 2025-09-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5947d05-ae0f-3463-9040-c52cce8b2ed7 | -13.79829 | -47.87936 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 406da56d-2218-3b60-ae12-8babd96b1f6a | -13.22097 | -50.93797 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbd9d01a-f869-30b9-b403-2faade76b8f5 | -13.81929 | -47.49581 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23ef5961-bbed-353e-94b3-2873cc059517 | -7.22911 | -44.77623 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f267399-99bb-3db1-8bbc-00a7077188f0 | -9.37224 | -47.58274 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3de04e63-77f7-3746-b0bd-ca1aaa9e4d35 | -7.2286 | -44.77972 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f429c319-c1e6-3e2a-81b0-1b8414743388 | -11.723 | -44.44358 | 2025-09-30 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 31603c8b-f8a8-3f41-8ee2-671095ddb891 | -11.74498 | -46.85097 | 2025-09-30 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b8795ad-a2de-3727-8325-22c5ac5c1fec | -9.06241 | -46.70546 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 583b3630-1f52-3897-8b7b-c340259d081b | -13.0156 | -48.76963 | 2025-09-30 04:40:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d128463-659c-366c-b046-a9f9bac846ed | -7.42241 | -45.18699 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36bf9f85-154a-36d0-b10b-779e3d66527b | -10.63297 | -53.69847 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1da44f37-8802-3fdc-8b47-d00526cc2bf6 | -8.2558 | -45.52821 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 511522ba-f040-346d-9247-cdb10c945675 | -7.51541 | -44.29396 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| debbc8ed-a0c8-374c-8120-15b35ee19fdd | -12.89125 | -46.76363 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1eb16924-00ab-3067-ad28-e18866cece87 | -10.40381 | -48.16639 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f936154-0b86-3aba-93c9-b39022d56fc7 | -13.06769 | -47.07656 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35b7b1b5-87fd-33db-86c0-8a911498c9b2 | -10.79485 | -45.36103 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8544d04d-46ea-35ea-aed8-99640053fe60 | -5.98465 | -51.90652 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 91f0bd75-30ba-37d9-b254-13464c60a0ac | -11.20489 | -47.74142 | 2025-09-30 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 59883d28-4465-3a99-be87-95a1d76c264c | -8.94431 | -51.69091 | 2025-09-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 367ddeef-e510-3899-9ed4-6e5c1df35c1e | -13.39167 | -48.07464 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d88315c0-2729-35c6-ab6b-f90aab699237 | -8.06812 | -42.94501 | 2025-09-30 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d2e29e45-404f-3b0a-9139-ae49f45c3053 | -12.86683 | -46.91048 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38ef28a2-fabd-38e0-b7ae-47a631e3d183 | -11.89106 | -48.04741 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 33d1bf62-6ef6-3770-8eb0-84b98feff4b6 | -11.70616 | -44.43681 | 2025-09-30 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9203605b-97dc-305a-b083-a000c707247f | -13.84527 | -47.93852 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef2b9612-e2b9-3a73-adc5-5881bb7a6d64 | -13.81874 | -47.47332 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5c15588-e159-35bf-b0bb-bb49a5d52d86 | -7.91735 | -44.62241 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8ba5f89c-df82-3a7a-9689-8b71bc26ee69 | -7.7686 | -45.71735 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bf8eedf-4c58-3bd0-a5aa-eda3a54b0b2a | -10.39523 | -47.80676 | 2025-09-30 04:40:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d427728-8c9b-31a8-9223-a9c5b35c73f9 | -7.91436 | -44.61436 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a1635d2-8d66-30e3-b553-8064e5626113 | -13.63758 | -48.04064 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 292419aa-9cd6-305d-8cd0-556a63a53828 | -7.11364 | -45.07409 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8468111-df7d-3f61-8017-9cf781c0d136 | -13.79463 | -47.8791 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 97e1145d-c5b5-34d5-817b-2248ad56a3c5 | -8.09586 | -48.00955 | 2025-09-30 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eea1c000-bda2-37d6-bd1c-bb679cfa3ace | -7.29847 | -47.30389 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67a17336-7b8d-3a81-86e9-ec9891787b15 | -11.15208 | -54.12352 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| f3048248-2709-3b3e-b683-db19ad0ea17a | -12.96623 | -46.4243 | 2025-09-30 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 573b55e0-09f6-343f-9592-a7784e6f22c9 | -9.31981 | -49.81599 | 2025-09-30 04:40:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 276717b4-eb51-3b46-813e-78ecbf12f2ac | -13.78105 | -44.24546 | 2025-09-30 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47403469-b4dd-3b34-b8ed-834decdab6b8 | -7.79824 | -48.30538 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c98baf9-13b2-3569-be78-67b543ba5cec | -11.98927 | -46.58091 | 2025-09-30 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c43d3341-b3d3-3916-b5a8-a47b5b816c60 | -13.80797 | -47.88931 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67e2f9a8-27f9-3c31-ad99-d5f1ad5389d4 | -10.02905 | -52.10784 | 2025-09-30 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f16e8bb1-74c2-3022-b95a-e11e22f907c5 | -7.82017 | -46.99147 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dec336a1-ad33-325f-a9ab-8a19a2a2f4a4 | -8.24425 | -45.52618 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 57e865ac-6a6b-3dfa-8935-15050bb3e532 | -13.08588 | -48.26178 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e384d144-4483-3e87-b5c9-ff72abc936f0 | -12.85566 | -46.87991 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb5b3f91-ca7e-3c22-afcf-fc237d885481 | -9.42468 | -54.71687 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 977197ab-8e5e-3766-bbd1-3eccb29822a1 | -7.54261 | -45.29762 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0b4ae36-ec17-3b70-9cef-21a2326a12dd | -11.66808 | -44.28628 | 2025-09-30 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2833afff-7387-352b-a08f-2a848af066b7 | -9.05223 | -46.69638 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 981acbee-d85a-30cf-8ca0-880f9b3ced11 | -10.75804 | -45.38226 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd0a7952-04f5-3bd8-bddc-3867097bf8a8 | -12.83206 | -46.99405 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 747ab72b-9e30-367e-a532-2e2d8ad051ff | -7.86328 | -46.74729 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56ab4595-7ac8-3483-a01c-24ac5eb5bc0a | -13.80896 | -47.9601 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c29361d6-4f91-3191-a611-79077c73789c | -13.73347 | -48.65516 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb6c35da-6553-3b10-84be-b2cc0580dd16 | -12.7919 | -46.89206 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6eba2d5f-1521-3465-bd9b-e4c11fb5c708 | -10.44242 | -49.35177 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49c00d38-ed5e-38e3-9b4b-d11713b5184a | -10.66466 | -53.70825 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02f17144-8e74-3f4a-b518-f8336ff5811c | -10.53399 | -43.64389 | 2025-09-30 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b8f67dd-bed5-35c5-a065-12f79c7ca101 | -11.88636 | -48.02744 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e5e826d-dffe-3e62-a95b-448bc997b858 | -8.28885 | -50.79057 | 2025-09-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README65.md)
