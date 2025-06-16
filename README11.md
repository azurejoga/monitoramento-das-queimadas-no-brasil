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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90f3d39d-436c-37e0-99d2-9126e2027166 | -7.14819 | -47.27803 | 2025-06-16 12:04:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| ad171ab8-a510-3c8f-acbd-473373d0af69 | -6.66305 | -43.1939 | 2025-06-16 12:04:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 42.7 |
| 56bfe258-56dd-3f02-9dd4-a2da3684df6e | -7.11889 | -44.03548 | 2025-06-16 12:04:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 0f1e9e03-f214-3225-99cf-f6bc617ef694 | -7.13652 | -43.29951 | 2025-06-16 12:04:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| a62121c7-fc13-3c82-b9c9-adb43fc80e64 | -7.19333 | -43.60131 | 2025-06-16 12:04:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 41.9 |
| c0cee5ba-732f-3623-9b7b-f8e0ae9be062 | -6.67343 | -43.18594 | 2025-06-16 12:04:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 28.9 |
| bcc59c8e-d89e-3ec2-a99a-b2b2711219bb | -7.20247 | -43.60257 | 2025-06-16 12:04:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 513958e9-1857-3615-9ad8-0c7b0ad16b03 | -7.18627 | -43.21218 | 2025-06-16 12:04:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 318fe56a-1591-3105-86f4-64d69d907de1 | -7.22818 | -44.72716 | 2025-06-16 12:04:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| ba531c04-e087-34ab-9c96-2cc84c94ac8f | -7.19528 | -43.21348 | 2025-06-16 12:04:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 1abc8026-1212-371e-adc4-fdea10f684c5 | -7.04455 | -43.42264 | 2025-06-16 12:04:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 3a15df25-eabd-397a-bb45-fb127b2d3982 | -6.21922 | -43.32449 | 2025-06-16 12:04:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e8aa2354-a48c-3d8d-80a9-a619c5c6d451 | -7.01518 | -44.06895 | 2025-06-16 12:04:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d3b59c50-b6bb-31ce-aaf1-2f92fb8d7820 | -7.02182 | -44.06631 | 2025-06-16 12:04:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3bbeb105-5923-3471-9d21-97c26cbcfd8e | -6.6617 | -43.20319 | 2025-06-16 12:04:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a56b4051-7d14-3d2b-8f43-9322ba0ee499 | -6.93962 | -43.7612 | 2025-06-16 12:04:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 166341d2-77b4-3beb-94c1-8a60401563c6 | -7.3452 | -44.01039 | 2025-06-16 12:04:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3d28bac0-94de-3dc0-8b0d-0ac222120896 | -5.29698 | -37.08525 | 2025-06-16 12:04:00 | TERRA_M-T | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 18d96372-cd22-34e9-af38-0812646f0d25 | -5.07092 | -43.72835 | 2025-06-16 12:04:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| fb911f9e-bcdc-307f-b1e7-160892f53b4b | -6.97203 | -42.91046 | 2025-06-16 12:04:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 901585a2-1e15-31c4-8d50-01f4467935f2 | -6.63979 | -43.91846 | 2025-06-16 12:04:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8c2c1e48-baf5-3f6d-84ac-ab626db2c2d1 | -5.07241 | -43.71833 | 2025-06-16 12:04:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 636b69de-ad19-3005-b0ec-59466a1bb447 | -6.31517 | -43.74549 | 2025-06-16 12:04:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 17984d0e-9f00-3d4c-8a29-df377eeaf571 | -7.19191 | -43.61083 | 2025-06-16 12:04:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 5fd5f91b-8429-3a7c-a509-381bf909200c | -7.02031 | -44.07635 | 2025-06-16 12:04:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 407da7de-a772-34ef-accd-5f2587721a03 | -6.09693 | -45.56704 | 2025-06-16 12:04:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 964cb7c1-2a61-3af6-9357-e7bd09c60840 | -7.1174 | -44.04538 | 2025-06-16 12:04:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| c1245aab-03cf-3d9a-980c-4a092343e665 | -7.12037 | -44.02564 | 2025-06-16 12:04:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| bcfb6659-f1a2-31ed-a591-0bd72f03ae89 | -6.6644 | -43.18467 | 2025-06-16 12:04:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 18.9 |
| ff6eb903-58ac-3cc0-be10-06f39c2c9327 | -8.11986 | -43.13793 | 2025-06-16 12:04:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 79b2ba55-389a-3daa-9aa1-2e3d59945e23 | -6.21782 | -43.3339 | 2025-06-16 12:04:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 414b018c-e488-3e06-8624-dede7ed253f8 | -10.81758 | -46.96186 | 2025-06-16 12:06:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| e2854c0c-7c9d-33f0-b044-1a39fc35ab6c | -14.00941 | -46.18752 | 2025-06-16 12:06:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a2ef82a4-a917-3cab-8561-029e986849fb | -9.40489 | -48.41896 | 2025-06-16 12:06:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 005072fd-dfb2-3707-8552-4226dd0d1aa6 | -8.47437 | -47.48039 | 2025-06-16 12:06:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5dc72c58-fe67-3da2-8c61-72b7ff94e195 | -12.70797 | -43.17904 | 2025-06-16 12:06:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c54ac89b-92af-3b66-b2dc-03ba46906038 | -11.48721 | -48.53764 | 2025-06-16 12:06:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 965f9bc3-36a5-3965-89fe-d4bdfcfc733c | -8.74219 | -47.16937 | 2025-06-16 12:06:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 156311b4-5267-3858-b434-a6fb9c732db2 | -11.4725 | -48.55298 | 2025-06-16 12:06:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d3d3df50-5775-3ad9-87fd-d0bc4d35f158 | -8.79005 | -45.09878 | 2025-06-16 12:06:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 71dba42a-21a1-3c63-8133-0195f151b0eb | -8.64609 | -45.44598 | 2025-06-16 12:06:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9a37ffd6-289c-352f-b0c3-ee28f232c8b7 | -8.78198 | -45.08649 | 2025-06-16 12:06:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d6ccbafa-f0e6-304e-9fd1-2e843219cdef | -14.21314 | -45.46898 | 2025-06-16 12:06:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ed6c590c-df69-3fc0-8ec9-d7cdf2fa1d3b | -14.01111 | -46.17664 | 2025-06-16 12:06:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9715a440-e98f-3280-abf9-fb09ba69eb0e | -15.39376 | -47.8553 | 2025-06-16 12:06:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cd005534-ebe4-30ca-af9f-fc39ceaa368f | -8.8992 | -44.23536 | 2025-06-16 12:06:00 | TERRA_M-T | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e53b960f-c9a1-32cd-be6c-7abbd010166c | -15.40643 | -47.84404 | 2025-06-16 12:06:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4f7235aa-4f64-3c99-ad59-557cd534278e | -8.6478 | -45.43458 | 2025-06-16 12:06:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d7414e5f-9aef-32e4-9b81-67f61cf07e4e | -12.22655 | -44.19711 | 2025-06-16 12:06:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| be71319f-7b39-3f87-a5c1-498522ae853c | -12.23416 | -44.20776 | 2025-06-16 12:06:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e43e4dda-eae2-3b65-b624-6bb3be515206 | -12.23553 | -44.19845 | 2025-06-16 12:06:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 2c40764e-3741-3b14-910e-86f5dbba87d9 | -12.22518 | -44.20641 | 2025-06-16 12:06:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0259ddeb-02a5-3299-be89-4990ca7a9c37 | -8.79167 | -45.08791 | 2025-06-16 12:06:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 090883c0-6435-3fce-bab1-da50b2f8b17f | -11.89103 | -47.44942 | 2025-06-16 12:06:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e6c3837e-52a8-3ce0-b00f-74d85b14ceb9 | -11.47527 | -48.53573 | 2025-06-16 12:06:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| f44c2887-3ab5-3b22-80ba-1b27ab3d8ed6 | -14.19634 | -45.40868 | 2025-06-16 12:06:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e613f8b3-a0ce-3346-b0fa-09653fae305e | -11.88878 | -47.46347 | 2025-06-16 12:06:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 47ec5e39-6fbf-3b0e-b843-85fd9c423fb2 | -11.48036 | -48.54336 | 2025-06-16 12:06:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| dce0bae6-0996-3ebf-a25a-9e2335eaf5f2 | -19.98795 | -47.18819 | 2025-06-16 12:08:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 56b5ec72-605b-3434-8e54-3f541eaf72fa | -20.81872 | -44.53067 | 2025-06-16 12:08:00 | TERRA_M-T | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 13cf7fee-4884-3a88-9866-6b4c4fd6ce0d | -20.82005 | -44.52124 | 2025-06-16 12:08:00 | TERRA_M-T | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 5cb4f69b-274a-3db1-9533-d2cf334ba041 | -16.88398 | -43.88102 | 2025-06-16 12:08:00 | TERRA_M-T | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9aab77a1-9977-363d-b62d-612c5819bfce | -19.98963 | -47.17751 | 2025-06-16 12:08:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e2df0414-e95d-321c-a6e6-7988065ed47e | -13.9471 | -54.4386 | 2025-06-16 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 555b3061-bae2-3fbd-9385-504dd8f108c3 | -13.9471 | -54.4386 | 2025-06-16 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| f12b6f0a-36c0-3171-8676-8a0d12326371 | -6.675 | -43.1899 | 2025-06-16 12:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 7049c9d4-c95a-3682-afde-278ccb7d3d04 | -6.675 | -43.1899 | 2025-06-16 12:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 565fe254-40ad-353f-8794-64c827c7dfec | -6.675 | -43.1899 | 2025-06-16 12:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 103.7 |
| c9bbee9f-12c2-34f7-8aa2-f86abf34def6 | -13.9471 | -54.4386 | 2025-06-16 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 80e06f02-404b-3a58-b50a-3c5c13949cae | -10.8696 | -54.2947 | 2025-06-16 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| acfea422-28fe-37e2-a714-617854053e82 | -10.8696 | -54.2947 | 2025-06-16 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| d96ac574-a052-36cc-ac1a-7d2d431ea56b | -6.675 | -43.1899 | 2025-06-16 13:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 52cbb320-f69d-340e-849b-41adbc751e75 | -12.2224 | -44.2073 | 2025-06-16 13:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 59abe1df-026b-3a20-af9a-e9bface7ca96 | -10.8696 | -54.2947 | 2025-06-16 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 89a0ac3f-bccd-3585-b0f2-c76e34542bf9 | -7.1969 | -43.6087 | 2025-06-16 13:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 498fcf93-8c16-3151-8504-11ef44c7c78e | -6.675 | -43.1899 | 2025-06-16 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 109.3 |
| 3edcfe0e-6899-3fc0-a0f6-96c356c30793 | -11.8963 | -47.4537 | 2025-06-16 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| a0b587af-dd12-359f-bfee-27c2db084033 | -11.8963 | -47.4537 | 2025-06-16 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| dbf5c20e-a0c4-32c2-9e2a-6924466fa3f1 | -12.2224 | -44.2073 | 2025-06-16 13:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 2e0d91e2-4686-3e7e-b7ae-5b2d63e6fc6d | -6.2228 | -43.3226 | 2025-06-16 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| cfa44841-36b6-38e2-8f6d-1de86db574f0 | -6.675 | -43.1899 | 2025-06-16 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 95.7 |
| b2be7b05-b859-3eac-aacc-dd869c28b04a | -10.8696 | -54.2947 | 2025-06-16 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 5ed6827f-4c2f-37bb-b8d7-b19d40556910 | -6.6562 | -43.1916 | 2025-06-16 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 14a32675-44c0-3514-8354-4e8def45b01a | -6.2226 | -43.3459 | 2025-06-16 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |
| afe35f58-cd4d-3194-b8ef-12415a4ac68f | -12.2417 | -44.2042 | 2025-06-16 13:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 393ce0ba-8352-310e-bfe9-4bb0d9292a0d | -9.3972 | -48.4305 | 2025-06-16 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 437483d1-154a-39cc-9bf4-939e4e353909 | -6.675 | -43.1899 | 2025-06-16 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 108.1 |
| e8100af8-2137-3601-b73d-94acfab237fb | -6.2228 | -43.3226 | 2025-06-16 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 4877f3e3-9b71-34d5-bdb1-dff276e4d312 | -10.8696 | -54.2947 | 2025-06-16 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| b394738e-05a0-339d-b4ba-0c3acc671a72 | -11.896 | -47.476 | 2025-06-16 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 8f31bb32-3f56-3be2-805b-7d18b8b42ae3 | -6.2226 | -43.3459 | 2025-06-16 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 0a174fba-1fb6-3881-8409-30f0d1d50d21 | -6.2228 | -43.3226 | 2025-06-16 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 156.3 |
| e38b42dc-e08f-3ad3-a7f7-22097da2e2d5 | -12.2224 | -44.2073 | 2025-06-16 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 50efd1f9-b66d-365f-9f85-7143295c5a09 | -10.8696 | -54.2947 | 2025-06-16 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 1f56efdc-2ab2-3410-8fdb-a9ba302bee10 | -6.675 | -43.1899 | 2025-06-16 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 114.1 |
| 49a2bed5-7fc1-341e-84b2-6a7d63eb3f84 | -11.896 | -47.476 | 2025-06-16 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 27436c76-e7fd-3d9d-8f69-a27580668701 | -11.8963 | -47.4537 | 2025-06-16 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| dcd89243-808d-3d1a-9a49-e1b0bd76e9ea | -9.4161 | -48.4286 | 2025-06-16 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| ba64ccab-0890-331b-8199-0fc6ea0a17f8 | -11.8963 | -47.4537 | 2025-06-16 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 623ecabe-a90d-3078-a9a6-a4a0ce9a3056 | -10.8696 | -54.2947 | 2025-06-16 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |


[Clique aqui para ver as próximas entradas](README12.md)
