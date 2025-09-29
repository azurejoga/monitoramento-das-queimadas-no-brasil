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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46c27caf-3d06-3960-9f5a-d2dc9429f7c7 | -5.19142 | -43.75948 | 2025-09-29 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bbefa1d7-22ea-35b0-b8f8-f971f2a78be6 | -8.26405 | -45.48139 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59867c6a-9002-3759-9bfa-44666899c508 | -9.78459 | -46.93626 | 2025-09-29 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc97f8ee-74d3-38b5-b8c2-c8cd23ed4727 | -7.73718 | -44.94477 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a050312e-4692-3c14-8349-c53a4bbae2fe | -9.75434 | -47.78887 | 2025-09-29 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48079916-b317-3325-a013-3e3a351706ed | -11.26912 | -47.18475 | 2025-09-29 04:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6ede793f-98e7-37ed-9b44-7a11e811d7cd | -10.80938 | -46.66587 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9fb24b93-c762-331f-a35a-5b053daa544e | -7.70318 | -46.81153 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3afe969a-420d-3390-9bf8-48fb7f343cbf | -6.29864 | -43.46307 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7fbad1e1-74b6-33e5-bccb-da37e206a26c | -10.7981 | -48.91485 | 2025-09-29 04:57:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef984ac1-5423-37ec-a4c7-5dd6ad1211bc | -6.67415 | -44.60342 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80077b53-d755-3f96-901b-b214be8699a5 | -5.93867 | -47.40721 | 2025-09-29 04:57:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 955a85d3-937a-30e7-95cc-57372280aab7 | -6.74278 | -43.3737 | 2025-09-29 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 39317005-0e23-39af-b1cb-de5ea0e0712d | -7.74146 | -46.9957 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6187bd3b-ea46-3fc6-8d41-5e23f6b3eaea | -3.3078 | -51.67121 | 2025-09-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d78c2f9-4895-3570-9230-b7609c46daec | -7.50583 | -45.42765 | 2025-09-29 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0198d44-449a-3919-b1bf-41c107ec47da | -10.83269 | -45.39081 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e7acc812-640f-3525-a94e-60017f2197a9 | -9.31039 | -45.70379 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac0551f6-c718-3f54-8d5a-2429b1799b59 | -6.74385 | -44.75198 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26944ce8-4264-3d53-9080-2ac1a7f25330 | -7.22501 | -44.77792 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 72b02cbe-656d-3a70-bcbc-c4d379978615 | -7.50206 | -45.42299 | 2025-09-29 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 015253bc-ced8-3c7a-9b81-3e5b2a94b16c | -10.80861 | -46.67198 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1cb08cba-09ac-3e3c-8314-bdbe55d59baa | -3.89099 | -52.07726 | 2025-09-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61170681-66c2-3931-a09c-c9e3c28a8b4a | -7.75101 | -46.99721 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0dd44fc7-0a7c-3bf4-9adc-c621f9f57f3e | -6.62233 | -44.9486 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| acbd61ea-0370-3797-8240-e30badf20ff9 | -8.82905 | -46.19764 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05e51537-22e8-31ac-b0d0-5f33ac3e816a | -7.73641 | -46.99435 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f9748df-93a8-3aeb-a731-6c3b216f6299 | -6.27901 | -42.49296 | 2025-09-29 04:57:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e8b4960a-b5e0-353d-b818-b96323917bd9 | -8.66367 | -49.43233 | 2025-09-29 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d34d9117-6ac9-39a2-a898-d51c6d3e3ee2 | -9.41917 | -54.68908 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0683ac46-68c6-3756-9004-4422bf8faf2a | -6.46317 | -44.00434 | 2025-09-29 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a407f58-35bd-37db-ab34-aee39b1ecbef | -9.30163 | -45.72993 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1ee780b-bd8f-322e-a452-c17400cfbd05 | -11.36581 | -45.07777 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57a0e4c0-14b9-38d1-9a1d-ed6c47baef05 | -10.46165 | -48.19677 | 2025-09-29 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b703d4f1-8cef-3590-bd76-b1ea5527eb58 | -5.34881 | -43.69083 | 2025-09-29 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c63fc7c-b4f5-3e9c-847a-47bbef8a170f | -6.31054 | -43.46461 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c92289b-aebf-3bb3-8e84-dc41ce951619 | -10.83274 | -45.39917 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7fd9b9c2-909f-3f1f-9fe5-f91eabd8d31f | -6.82906 | -44.83609 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 52c0993e-aca2-368a-9531-ec9c5945d7a8 | -8.29708 | -45.43748 | 2025-09-29 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea5f7dc3-fa89-3f0a-b455-827ee5a4a90d | -7.89468 | -44.60808 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea1b7e87-c222-36f3-a3a3-27e16641ae6a | -5.86803 | -45.7641 | 2025-09-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e369364-d362-36db-9053-117f6fbc495a | -4.31196 | -48.0933 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b70181f1-9a2a-38e1-8d7f-e36c5624c744 | -6.58342 | -43.42853 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ab28c075-83b0-3062-bb07-5e5e7b98a227 | -9.30205 | -45.72663 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e9c2abe-71d8-356d-a8eb-ce5da49aae92 | -6.80436 | -45.98367 | 2025-09-29 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90707e2a-1cc6-396f-8f3b-118f26d8e331 | -10.04237 | -50.40495 | 2025-09-29 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02ffba81-412a-33de-b57f-bab4866f53e5 | -3.48737 | -51.59986 | 2025-09-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6157552d-91e7-3095-8586-3505920aaddd | -10.19679 | -52.55518 | 2025-09-29 04:57:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9363bf57-5bf3-3557-9602-b79363693d01 | -10.46573 | -48.20132 | 2025-09-29 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ba9d2203-53ca-35eb-b39e-dc4f81fcae2b | -7.54933 | -46.2944 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b879b87f-09d9-3c57-a30c-4974df1b457e | -4.31968 | -47.59821 | 2025-09-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dcbfa38d-ef0a-3204-bdf4-f83014fe1aac | -4.11693 | -48.92443 | 2025-09-29 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6276e297-2449-319a-be96-de346b6734a6 | -4.29362 | -48.27102 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b81cc225-2af1-36e2-878c-583b0b22cdf9 | -11.36123 | -45.06755 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56396e68-b049-3c3b-8629-b41afbe65e7c | -3.29985 | -51.60953 | 2025-09-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23a380eb-d189-3590-9345-adda04cae98d | -6.47114 | -43.94553 | 2025-09-29 04:57:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 740f1917-bd3a-3292-a8df-df15202bc1bc | -9.78334 | -46.93567 | 2025-09-29 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e712bb71-ae71-3181-bbb8-945a99cf89fe | -3.94166 | -49.1309 | 2025-09-29 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c5810666-bbbe-3446-a0ce-157a7e84a0d0 | -9.15958 | -50.55953 | 2025-09-29 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 972297c2-0aba-3959-95d4-8837c99560bb | -9.40906 | -54.70537 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9692b586-5253-3627-a5c8-d329d6d8ac95 | -11.36528 | -45.08208 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 069303f2-277d-36d2-90b2-d8e782d1f781 | -6.46809 | -44.22367 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c32c330f-c735-3756-8cfa-d35227742296 | -3.33117 | -50.25138 | 2025-09-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3337e537-aa42-3aab-8351-76914a78189a | -5.7218 | -42.85954 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c8cc3e37-997d-3566-8862-9b86986eb83a | -10.60173 | -46.27312 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad49cb88-d572-35c4-88e3-ef8a88e07ca0 | -6.8981 | -44.5271 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5605a3a-ae4f-3e33-8416-cb344e7cb68f | -6.83395 | -44.83424 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1b24ea30-ee9a-34b1-a9d3-d09a44270fc6 | -7.75593 | -49.85368 | 2025-09-29 04:57:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc4ad770-c488-3b78-87c7-77bc6f445ec2 | -6.82955 | -44.83239 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 788c9505-36ef-3759-92ee-67c5dcd1b795 | -9.05262 | -46.7136 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8bf9a958-3509-325e-af46-e73caf81ee4a | -9.94221 | -48.79945 | 2025-09-29 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fcb0eb42-e0fe-3aee-a06b-6c947fc6530c | -11.26342 | -47.1899 | 2025-09-29 04:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| dd684b86-b449-3c29-b881-95766aadfaa1 | -8.87294 | -46.60243 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fea542dc-006d-345d-a1ec-3546192806c4 | -5.6752 | -45.29159 | 2025-09-29 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83f30c7b-be4f-3e2d-8248-b9c0de2ff5b2 | -10.91665 | -45.71778 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1306f3aa-87f1-3278-b209-d0425e560e41 | -4.26317 | -48.55375 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d42b9599-0533-3e57-8ef4-2c59a9ec17de | -4.97484 | -44.50876 | 2025-09-29 04:57:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 00cc615c-b5e2-362c-b7d2-9f5df6d7ddee | -8.6683 | -49.42929 | 2025-09-29 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3838d935-1f82-35a8-be7e-b9f4546cfea9 | -9.28103 | -45.73465 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 14dfd051-ff59-3786-86a1-e29d4766f6d1 | -9.05787 | -46.70469 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 140841ea-f25c-34f0-ac08-85af9df4a054 | -8.88804 | -45.04795 | 2025-09-29 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 57742cbd-ea9f-31a1-ab04-b98d7ace3973 | -5.73404 | -42.6727 | 2025-09-29 04:57:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0200e1c2-f034-3d42-a961-9a6b0c7b6050 | -11.48881 | -43.21038 | 2025-09-29 04:57:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5cab1377-c622-31d8-8cc6-12e17e7c10ce | -6.43391 | -42.82429 | 2025-09-29 04:57:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 98bb765d-7109-339a-bf94-73722cb6694b | -5.17485 | -41.26036 | 2025-09-29 04:57:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2fa37932-88b0-351b-b79a-9a930ecae341 | -4.25655 | -48.59706 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e10c0887-7d23-378a-9f0c-2d539f8df4a0 | -10.83068 | -45.40752 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c8c990b-458d-39ac-88ba-d5c040516f58 | -9.41182 | -54.70937 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c34c6d1-a5fe-3449-91ee-542402936821 | -6.62134 | -44.94101 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eda27785-0450-35fd-a198-e58bdf5f6f1a | -6.40839 | -42.82617 | 2025-09-29 04:57:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7778908e-8ea3-3518-8181-004b62ca6995 | -8.71681 | -47.97976 | 2025-09-29 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d37288c5-ad81-3bc3-94ae-ae2a994c003a | -9.40631 | -54.70138 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e42a7fd-50b2-3b58-8c0e-8526006c643b | -10.40253 | -48.14904 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e26d969-16b0-3a3e-b60e-a7efe0efd7db | -3.31177 | -51.66806 | 2025-09-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6513bac0-4921-3c13-9b68-5697f19119f3 | -3.84392 | -50.00694 | 2025-09-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 560228d1-98c0-34cd-a86b-ac89972132ac | -6.06799 | -42.48108 | 2025-09-29 04:57:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fcbc132a-440d-3e14-a98d-c4f7dc5c0987 | -3.2548 | -50.11528 | 2025-09-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ddd08dd4-9243-3dd5-83df-27bc6b1b16f4 | -7.54855 | -46.1107 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0cb7e3e-d3b2-3c8c-92de-2f83a31d8913 | -6.06756 | -42.60822 | 2025-09-29 04:57:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 77a825e1-40b1-3586-9e00-c7f9cc581b82 | -6.69662 | -44.56254 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README59.md)
