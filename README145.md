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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd83cd16-85bc-34d2-9361-d1deab5a1e5c | -7.03726 | -45.81611 | 2026-09-28 17:09:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2499ab64-9fc7-397a-a358-b82d4eb652f3 | -8.60736 | -48.35068 | 2026-09-28 17:09:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e198fed2-4d31-35d7-995c-85afc1c5024e | -11.53316 | -47.15715 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d0b057d7-464c-33e5-975f-b249e7d8d141 | -8.48935 | -49.60145 | 2026-09-28 17:09:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| bf4158e9-ce78-3840-9ae0-838ba8744322 | -9.77055 | -44.82832 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6f45ee4f-c12e-31b6-818d-92229098200f | -9.03151 | -45.98084 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f0b7dbf8-13c4-3ffd-8a59-e0c6881874b9 | -11.07364 | -46.08445 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df36bf4e-ee06-3637-a256-c067054e288a | -7.49458 | -45.96686 | 2026-09-28 17:09:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d9857492-63ae-3972-a8f9-7a696d5a7f88 | -12.8031 | -54.0056 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 70610fe0-5476-3d19-8412-692ad8039376 | -6.15741 | -52.82713 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5e260007-8489-3292-be0c-756b64cea41d | -7.28101 | -55.57173 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6c085ff3-c011-346f-895f-11f6cdcc6328 | -11.51349 | -47.39272 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 17f3be93-8b52-3a9e-ba27-a844ab30d846 | -6.01663 | -44.29501 | 2026-09-28 17:09:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8df1f23-aa94-3e5c-a526-71f05ed948bd | -5.88943 | -49.98732 | 2026-09-28 17:09:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a8dac935-ee85-3365-b02c-ecd3958d97b2 | -8.51834 | -48.10981 | 2026-09-28 17:09:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 577d0e83-03f6-38af-9fce-45a64e13735b | -4.31595 | -45.27662 | 2026-09-28 17:09:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 11322c4e-eac8-3f1d-8ec7-cb0df4094738 | -10.88737 | -54.03653 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6a6853ed-e4bb-3c67-a5ed-cf5e6a1ca151 | -7.18226 | -52.66016 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfbc813a-2c02-31a1-9154-75eeec2a5f01 | -10.45888 | -47.48905 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 8c8b2af7-16ea-3379-8389-ab37d75a170c | -11.09744 | -51.37478 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 4aa34fa7-792d-393d-9c82-8306aa635cef | -10.2902 | -49.9634 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 5787bb4f-bd69-3a18-992c-d622ebf0065b | -8.63759 | -49.48268 | 2026-09-28 17:09:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 86b333e8-b436-3337-bf1e-290d2630300e | -10.27358 | -44.62528 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 69a97f32-5d6b-386c-8678-1f2e1cca5416 | -8.97315 | -50.97404 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 07b143be-2af2-3e62-90c0-9fce38288846 | -7.37622 | -44.76955 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 5bf612a4-dab0-30fb-a393-7647ea255ad8 | -6.14875 | -51.56867 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 910f2dc8-af1f-330f-a59b-9935d958045b | -7.29199 | -44.31115 | 2026-09-28 17:09:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 13356b35-34f0-3c80-b478-3fcae534f233 | -10.7488 | -48.77308 | 2026-09-28 17:09:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 72b84245-ce2a-3121-afdd-cfd7e900f687 | -7.45324 | -64.33211 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| fafe8df0-01e3-3163-a14d-8ee4aa24bec4 | -11.08405 | -46.08517 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 8a48b2fe-2da4-328a-a5b7-32d0721a689b | -7.67743 | -54.7388 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2d9526fc-60de-3184-befa-e44c870506de | -5.79157 | -46.08995 | 2026-09-28 17:09:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a66a17f8-51a7-3cc4-9742-2131ffba8fb1 | -8.94544 | -63.2849 | 2026-09-28 17:09:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b2a0c679-d344-3405-930a-303bdb326892 | -6.23505 | -46.55487 | 2026-09-28 17:09:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f538b301-c105-3215-8694-d33c413800a8 | -10.00553 | -50.11754 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| afe9d52e-12b0-3c8b-9d5a-6fa702d6aba8 | -10.21805 | -50.01497 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 6acec936-0419-315b-aa58-4e72f8af8ba4 | -9.39985 | -46.38813 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 14aaeb60-51f5-3ee3-acdf-08300055f6c6 | -10.82472 | -57.22066 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| c6a35296-fdf5-3d3e-afb4-c49c42673d28 | -10.81701 | -57.19005 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 21612fca-207b-3572-9557-3ccc27091a0b | -10.95471 | -50.68522 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c6f9d94e-e334-32d7-b1b8-615ee667f177 | -9.43355 | -46.54687 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 6be35a3a-fb2c-3e1e-9259-f7bf4dfec305 | -11.03231 | -49.70387 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| da80093e-ea01-3758-a747-aa8d34bab3ea | -7.44973 | -64.34602 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 426991be-7396-37ee-a9ec-3a203e376191 | -8.63461 | -49.476 | 2026-09-28 17:09:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f1948199-0f9b-3142-ab8b-0a603ae89f9d | -6.14255 | -53.05836 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| acec7aa1-2630-3cf0-b98b-98a21dd61da0 | -9.11104 | -58.90169 | 2026-09-28 17:09:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 33b56da2-1a37-3228-855e-3894f6519ff4 | -11.58873 | -47.02272 | 2026-09-28 17:09:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| e1d7ed42-250e-32be-b67c-a9fc0cf41dea | -10.27301 | -44.62859 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 7c71b493-3cc2-3548-9fdf-b1c490f2ea32 | -11.85304 | -50.85083 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 1c65c62e-0be4-3f49-ac3d-9597819ea23e | -5.54776 | -45.59911 | 2026-09-28 17:09:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 527cdf34-5416-3933-9bc4-0980fec47784 | -10.81996 | -57.18551 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 10ed0c6f-a5f0-3c1c-bf1f-6bd8c2155f14 | -9.16053 | -51.48604 | 2026-09-28 17:09:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8d893917-e2d7-3c4b-ba1f-34cda42ea54e | -7.71979 | -44.88481 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 312a3ea7-e109-303a-abbe-9461c69b7ea5 | -5.33257 | -46.1964 | 2026-09-28 17:09:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5e2c0936-d8f0-3338-8bb1-b98e171af260 | -7.27678 | -45.34018 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c48bd2ac-d370-3e3c-a9dd-a1c26a55b901 | -10.81238 | -57.21021 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 67c14fe5-401b-3001-b5e1-857360ad8443 | -8.87415 | -49.72775 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c86769f-fd71-3f04-9d15-7a54763d9704 | -7.0727 | -41.74377 | 2026-09-28 17:09:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 1833d58c-e14e-38ba-bc33-62d0f5bcfde7 | -3.92949 | -43.13189 | 2026-09-28 17:09:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7c329c18-1512-3008-aa2d-9f2e7719fb1f | -6.81848 | -45.06114 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b00c73c0-8e7e-3e13-85df-8f9de739d965 | -12.21601 | -50.43645 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 9d921cac-0092-3a96-8e7c-64a036d8481d | -7.59847 | -46.66415 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0f868ae6-dd5d-3b6c-9e87-b48d76490bbd | -7.06289 | -55.4785 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 266.0 |
| cf3b7174-ca3b-35b6-9315-75de75977a51 | -12.3181 | -50.30368 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| ab06a541-5911-3a0b-befc-4fce00c69ea2 | -11.07993 | -48.9008 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 7575e450-f10c-3b1c-be93-a1dcff50e416 | -8.03178 | -54.89918 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 05094360-993c-3391-8a47-5637c4c311b8 | -10.0047 | -50.11259 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3d6aca81-512a-31ab-b8f8-9213e7fc6deb | -6.77403 | -55.81455 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 53536791-e76c-3f5d-89d5-565b67314b18 | -7.31467 | -44.59219 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| bcecff1f-fe81-3f68-ba59-0ccfded645b8 | -11.05114 | -45.18764 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f5414e70-231f-3bd7-9ec1-d6c501bae648 | -10.08369 | -50.3824 | 2026-09-28 17:09:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7122455c-e04c-32c8-9c37-b6b458d0aa4d | -6.20287 | -52.90911 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| cceec48a-bd1e-3080-99a4-8bc94b8ddbc8 | -6.19915 | -53.22429 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ca204848-671e-3d18-b3cc-b9382d3aa126 | -9.36967 | -49.17469 | 2026-09-28 17:09:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9089b12b-9ebd-3d0b-9126-c8e4335debed | -7.4565 | -45.81066 | 2026-09-28 17:09:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9a3c1d4d-882e-3340-9a3e-d716e79934cc | -10.8232 | -61.4106 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 13c39942-b4cd-3d39-ac4a-ae28f7dfa48e | -10.75519 | -61.49569 | 2026-09-28 17:09:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 66194115-434d-306e-9811-246359943973 | -8.92217 | -55.16595 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 57094984-8910-35a4-93c9-71d816ea0b8c | -7.25466 | -43.35965 | 2026-09-28 17:09:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 49c887fd-f0a3-37ba-8a7b-06f13f19217f | -7.39444 | -42.63112 | 2026-09-28 17:09:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 7da53b8e-89d8-35d0-bc9b-d7cbc8bbf2e2 | -10.27285 | -44.62132 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 44ef09fe-854b-3a9a-a185-fc64e16d7b0b | -9.44273 | -41.81693 | 2026-09-28 17:09:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 119.1 |
| 647d722c-931f-334b-af71-51328356ae0e | -8.23126 | -45.46453 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0a31d245-aba5-3bf5-ad16-9affe7d2b391 | -11.623 | -46.78541 | 2026-09-28 17:09:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 77e57a06-f061-373a-8484-b8a0371c3466 | -8.92962 | -45.04978 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4aaa4810-9dcd-3292-9f9c-8d605d96101c | -9.52662 | -46.37804 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 892ec505-4355-3894-98bb-f071773dad22 | -10.73292 | -61.57443 | 2026-09-28 17:09:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 1baed8ba-547f-34f3-8153-a7b8a14620ac | -8.86664 | -49.73277 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 8c01ff8f-b106-3901-9223-5a517988a755 | -12.15145 | -50.38122 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| cf434a3c-8229-3570-b8a0-7b3c3414808b | -8.28062 | -54.70276 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ff25e0cd-75a6-32df-9320-32b1c5683b87 | -10.49594 | -49.27591 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b98c29a3-0446-33d2-889d-79659e957ce3 | -6.15279 | -52.88867 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6bbc2a4c-d68d-3f16-b4de-d01871524de6 | -10.26133 | -44.62769 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 14ece650-0189-3a57-b81d-549ca79fdd38 | -9.77896 | -45.97931 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 746d784e-774b-33b3-b147-d6827a9aef7b | -10.93296 | -43.8759 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48a29c6d-f554-3d9e-9261-de72d2e8ac33 | -10.21332 | -50.01065 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| e95de5f5-d228-345d-b7bc-fe7d659948a0 | -11.17433 | -44.79156 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 07b1c673-5c68-3ced-9df6-cd4d65e01c2b | -9.32221 | -46.55978 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 93c01312-398f-3aaa-a3c0-c1ab7c4ff16c | -11.1922 | -46.28218 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5764cc5e-5ed8-3561-acfd-c31727cb2baa | -12.7435 | -52.849 | 2026-09-28 17:09:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README146.md)
