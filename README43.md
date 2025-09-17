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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61cf72df-1aea-3584-8e8c-ce599abc19a9 | -6.40264 | -43.35578 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8693acff-2b43-328f-9431-3a390615ee47 | -7.25757 | -46.60659 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a58fab48-dd9f-3dd2-b3bf-0220981aae1c | -6.16305 | -43.67339 | 2025-09-17 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4d6baeb-0cbb-3bef-8f6c-3e7466aec7ee | -9.12248 | -44.88577 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85a5692a-14a2-3b9c-9691-2e222fb42d79 | -10.55706 | -51.47345 | 2025-09-17 04:32:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2b48dc3f-29c0-3550-b938-509ba8940998 | -10.6759 | -46.50539 | 2025-09-17 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23e915cc-c075-34ba-a1ab-2d93d6c1ad53 | -6.88163 | -43.96235 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20c632a2-1fa8-31c5-b241-0b7ff6aa5c5e | -9.58829 | -45.66833 | 2025-09-17 04:32:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c95af565-c6da-39b6-af69-7f43582324de | -6.48273 | -45.99965 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0d30e7c-c063-380e-95c6-6e2394970567 | -5.04931 | -46.00757 | 2025-09-17 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bc46696-f8ce-39d5-9dfd-879a3bf582a8 | -8.24907 | -44.83462 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8c5d4ac5-ba14-3702-b1d5-029912f7ea70 | -5.77635 | -42.7733 | 2025-09-17 04:32:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| abb6b031-a7bc-3c81-963c-826a44646a0a | -7.82488 | -46.15083 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83e4c7a4-31b0-3f31-834f-0213336315f9 | -9.38124 | -45.38317 | 2025-09-17 04:32:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b481eaea-ed1e-3bcd-b86d-5ee38205340c | -7.41355 | -49.98728 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81d82e81-cd7b-315f-bc0d-f3744609f96b | -7.337 | -39.71622 | 2025-09-17 04:32:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cd66c77c-0ef3-334d-a7b8-df8822880a01 | -5.76963 | -45.90038 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b2698bc-a5ee-3963-bae5-8b92b660f550 | -5.75929 | -43.71063 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0c2474a-37e4-3761-bae8-443941979b47 | -8.68568 | -46.40512 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edbde19a-3403-3e01-b09c-90cb10ecc065 | -6.39558 | -43.34965 | 2025-09-17 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8fac315c-679e-3479-981b-8e82b6ca6b71 | -8.88375 | -46.18731 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2336764-9e63-36e4-9253-300e31b50dbd | -5.78835 | -43.4671 | 2025-09-17 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 506f37c4-4810-33ab-bfce-47e0aad8bfb7 | -8.6828 | -46.37792 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 618acad3-d447-303e-b6f7-5395d3bb70a4 | -10.63139 | -44.22406 | 2025-09-17 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37af332e-b0fa-347a-99a7-a0f98544ab81 | -10.77467 | -50.71585 | 2025-09-17 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07d3fcf2-0055-3893-9a13-13f5da3201df | -9.06532 | -44.94608 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a9da46d-eda0-3bdb-8d8b-368b3baec447 | -7.41578 | -49.99529 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5270cddf-6412-36b0-8ec6-9b00a663050d | -9.00478 | -49.78015 | 2025-09-17 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 28198bc6-5721-3992-a7c3-620d3b2b55ff | -6.88335 | -43.97678 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81757f43-8620-3506-9874-b1df9dc81222 | -8.57955 | -46.34283 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa886ba5-531f-3faf-bdf1-6224f2cb16e9 | -7.067 | -44.34981 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 26c7c0f9-bc4a-35e9-827d-7cce59d5607c | -8.68169 | -46.4083 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca0abb4e-6032-39ab-b16e-72542611bb55 | -5.79987 | -43.46875 | 2025-09-17 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa4763a1-83c0-38fe-9a23-2f4428763daf | -5.60081 | -45.36129 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 41ccd9eb-7fd0-35e2-8ef1-d87157d00ec4 | -9.15973 | -47.01118 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b66f8fe-2ed0-31aa-be17-b73490565fc1 | -6.91439 | -44.78825 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3813a789-fdeb-34ed-ba3f-5d5d497f537b | -11.50536 | -43.70713 | 2025-09-17 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47d30fc1-e9de-3cb9-89cc-adcb5c4f726c | -6.70737 | -43.29832 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d8f28245-f3ad-34a9-905d-cf18a95f7616 | -5.39938 | -46.52874 | 2025-09-17 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b411627-c863-356f-9d0e-eac0643669c5 | -5.66876 | -51.35767 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06ab651a-2cf2-349f-84eb-f7370dd9ab08 | -6.86614 | -38.43665 | 2025-09-17 04:32:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 44a2c282-c534-34d6-9382-5e049be4d734 | -7.57716 | -44.58309 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0560f22d-fc7e-3912-beec-3e045dd0236f | -7.87458 | -48.15588 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce07106a-c620-38c1-ae3e-6804845b65e4 | -4.0463 | -49.07524 | 2025-09-17 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34ff9d78-d896-30b2-8139-883605b9f0ee | -9.08743 | -46.93358 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d717ee38-cd33-3c47-b248-39bb3b7bf15b | -7.81225 | -46.11808 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ac19e5e-9843-3128-959b-0e775a0ef269 | -10.42682 | -50.65517 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc706e78-3d4b-3aae-b159-be53f61c97a1 | -10.79742 | -50.72716 | 2025-09-17 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 24239c9c-6e5d-3db9-bf82-11d10e554d23 | -5.87455 | -45.8785 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8a05da5-36c9-3009-9158-00da9e6a8f50 | -6.95782 | -44.55284 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57dd0df4-28d8-3eef-ab3f-e31b31cf5efc | -7.60273 | -49.33337 | 2025-09-17 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 703d1e1a-7ebc-36d7-82fa-14d574cce85b | -6.40857 | -42.65868 | 2025-09-17 04:32:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| beea4b21-b16e-3250-9672-14bc634c032c | -9.07632 | -44.94783 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c757edc-37cf-37df-8437-b50ce16b93eb | -5.21585 | -45.42509 | 2025-09-17 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bc80b66-0aa0-3b1c-abf6-f7a1d5d5a00f | -8.96088 | -46.32328 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0b7b6fd-3998-3c11-85fc-4d3ddebe0262 | -8.67595 | -46.35368 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 148a1cfb-1878-3bf2-af72-05b16f8f272d | -5.65958 | -45.04899 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4866643-02ef-385b-a661-08f7acc51323 | -7.52767 | -44.73818 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4782b24c-a1f9-3d98-9560-90357ad43186 | -6.12324 | -47.8251 | 2025-09-17 04:32:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16b0d694-bb99-38f8-8ee6-1f6686fd0009 | -9.06482 | -44.87428 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a5c556a-b0cd-3654-9296-04e06a03bfe7 | -4.06205 | -46.93824 | 2025-09-17 04:32:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4aaa987-55f2-3409-9522-4c731a4905d9 | -5.61401 | -51.71917 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d8312b3e-6400-3b78-bb30-723a54d3d72f | -9.15005 | -46.93913 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa65585b-6fdb-3213-bd0d-14a00541a1c0 | -6.16235 | -43.67813 | 2025-09-17 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 576b5cea-58e1-3e84-828d-37e77813df25 | -6.10381 | -49.84566 | 2025-09-17 04:32:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8178cbe1-4168-308f-8baa-05bcb1f01de3 | -4.66492 | -46.31786 | 2025-09-17 04:32:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57088bf4-820a-3542-a418-583784e398cb | -8.15437 | -46.7468 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8707e1a8-3121-3046-b068-52aef8111822 | -8.96315 | -46.33144 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85a8942e-8801-3755-bf1d-650e355bb226 | -6.6247 | -45.57478 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b01960f0-54bf-3149-b369-142f20d00abb | -3.80153 | -47.57808 | 2025-09-17 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6c0aa043-dbaf-384a-bf3f-018717ec2edd | -10.67473 | -46.51307 | 2025-09-17 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ecbfd9db-9374-33fd-8c80-d9aa64ea8fd3 | -8.0042 | -45.65545 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 369b1b89-8cd1-35b3-8adc-b42e82722ec0 | -10.63345 | -48.75091 | 2025-09-17 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5682b3e5-99d2-3bf2-921e-644bb9199700 | -6.35568 | -43.15847 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d7f05934-6a25-3896-9323-f9ebc42e6f35 | -8.01181 | -45.65255 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7232a58-2fea-3135-9fef-ca7d9f217ee6 | -8.8931 | -46.14954 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 797051d9-6c49-3acd-9012-6c98350f7bc0 | -6.9298 | -44.76817 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fcceca7-88a7-38a7-a28b-44bbb3d711e2 | -10.63069 | -48.74688 | 2025-09-17 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57212192-d495-389a-b6d2-1e9f0c6054fb | -4.11188 | -51.08953 | 2025-09-17 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04409236-052f-3dfc-a4dc-2eabfe7efcb5 | -8.99332 | -46.26564 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2aa1a38-123e-3f66-b6ce-99bd6aca2651 | -5.78932 | -43.48665 | 2025-09-17 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0c685d1-ad3d-3f8b-848d-60fb21342401 | -11.46961 | -43.57343 | 2025-09-17 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b0c4308-de37-3c37-bcb3-140ed1c641dd | -8.63266 | -46.43132 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 715d5953-cdca-318e-a9ad-867b14f4752c | -6.34486 | -42.9557 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79a244bc-2a54-369a-af95-906db40e949f | -7.07644 | -44.56022 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cac25938-e24e-3fac-8aba-96c8d1e6f9e9 | -8.63202 | -46.4352 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99fab709-7e1e-32a4-8728-ac1774c4fb58 | -8.16395 | -46.75198 | 2025-09-17 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75c079b6-221d-3089-afc2-87d37b8381a6 | -8.63605 | -46.40907 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7daa2fe-af71-31d4-977c-3d81e2e215d0 | -10.32506 | -46.62535 | 2025-09-17 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc42a17a-193c-308d-b7eb-c23ab1b35afb | -8.95869 | -46.26852 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a10e77b-5898-3a02-b1c5-9b2a0b5bab7b | -8.01881 | -45.65368 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 910d1f85-0dae-3e50-8708-9e7562be62d0 | -7.88894 | -48.17238 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b81c028-397d-3fde-9659-9be071c07f52 | -9.0481 | -44.88531 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 51bbee31-9cfc-3201-9ba9-337dc9068e8c | -5.46187 | -44.68575 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15232c07-c4d3-3480-a50a-8484b6405966 | -9.07603 | -44.94639 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f433143-36b6-35f4-a4ab-0408f744c61e | -7.07071 | -44.35033 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a97a9c78-7273-3754-8e2b-d4221132ff55 | -6.99877 | -44.57904 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fdb6b38-9744-3fb6-94cf-802b51565943 | -7.87789 | -48.15641 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6316860f-0c6d-368e-b5c1-c4672328615a | -11.12169 | -45.11406 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| feda8aba-9262-3f82-b7eb-3afa78bf8f2a | -10.62738 | -48.74635 | 2025-09-17 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README44.md)
