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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dea14476-25b6-3e11-9d11-291fcf331b85 | -11.86739 | -46.7591 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 921c9114-7580-34e9-9e58-ae852a5f65f5 | -9.90344 | -51.88771 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d5c8275a-5c7d-31a0-b32f-bd6ef979423f | -11.74559 | -46.61043 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b00fe51-4305-3c09-8032-ea82994e3dd2 | -9.96398 | -50.40514 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bb5e40c-aee3-36a6-816c-68fe8948cab3 | -13.0 | -46.74139 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2a4a86af-2263-3394-8848-9f5d8bf60363 | -13.73158 | -45.44396 | 2025-09-13 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c59b5ba-3d06-303b-8b23-f6128b112610 | -10.69545 | -54.45006 | 2025-09-13 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1df390c-1ce4-3e19-9b9d-7d49e2185bb0 | -13.13428 | -47.14118 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 631e0bca-7410-332b-b179-2f49e5613528 | -15.24085 | -44.04265 | 2025-09-13 04:08:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddc44bf1-8080-3061-9d10-73815734bab8 | -13.92248 | -48.27515 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b6ffff3e-f6ae-3eaf-9118-99d68f258f98 | -10.56307 | -43.66022 | 2025-09-13 04:08:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ac27391-56f4-30d1-b8b1-66fda28fc1d0 | -9.89451 | -51.86736 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b96ed93a-252b-389a-afe5-945afbe8ae44 | -11.74769 | -46.62058 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e750a9eb-9cee-3484-a199-1bf69bce3948 | -14.17478 | -46.25904 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 72a59583-3fe7-321d-80e5-98cc5e506bd4 | -9.81153 | -48.3919 | 2025-09-13 04:08:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72561338-b2e8-3f7f-99d3-819f4d819266 | -13.67719 | -42.50091 | 2025-09-13 04:08:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 40c1b512-816a-333a-ab29-56524061de6f | -11.43669 | -43.67877 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 539d3b31-42df-319e-a48e-7af035d4c9ab | -9.89516 | -46.64032 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bdc4bb67-ef49-308f-854b-0ad4ae9aa33c | -11.71467 | -46.56704 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 33f6eb94-7458-302b-b4d8-5d1ed0181046 | -14.18476 | -46.26498 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f9fc6200-54b7-3f8e-9575-2378b4d77888 | -14.2482 | -44.38585 | 2025-09-13 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6af71cf-bc54-3355-9a88-b6d6d23b9a8f | -9.0819 | -46.94566 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0f38f5bf-1ccf-3569-8486-c9005b22d557 | -9.90753 | -51.88814 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 16b14575-e6fc-366c-9561-ec40a0bef09a | -13.2648 | -43.76031 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 704069c3-cb8c-3b14-9adc-824a9a91427f | -11.79849 | -51.54788 | 2025-09-13 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f8af241-db14-3452-b0e8-fc1473951e9a | -10.07552 | -48.17609 | 2025-09-13 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3845be6c-2072-331c-8c31-6a4ef26bbc32 | -12.11761 | -47.59618 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01d394d4-26e7-3d8c-928c-b9d243037126 | -10.70553 | -50.50744 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b631b74-4739-3909-8f44-3d3f875fc2c6 | -11.87138 | -50.58028 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| b9331f57-b60c-3c8d-8045-f6cf69cfc4ac | -8.09426 | -50.17751 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 29157682-396c-3b87-b586-ba9adab0befb | -10.50489 | -51.54471 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9099b81-5b98-321f-ab28-1aec31ee0b47 | -9.00698 | -45.78288 | 2025-09-13 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86cc3c74-4d29-372a-a29f-bed52be02979 | -13.9111 | -48.28408 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12c879be-5e5f-3024-ac16-2a9ba7fcced8 | -9.05455 | -47.03305 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 95ce21d6-8e6b-3a79-8323-3cb6a63c42aa | -14.16316 | -46.15998 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5026226a-17df-3db2-898c-357ea83db627 | -10.74047 | -50.53706 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f378a51-73b3-37f7-8bc6-72986e65adf5 | -14.22313 | -46.29805 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 08725ba2-5a40-3384-8087-0cb303e4994e | -10.33641 | -54.32098 | 2025-09-13 04:08:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef9a8fc4-a647-3fac-a8d6-f6de8118b139 | -13.66873 | -44.22517 | 2025-09-13 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 057ff228-c217-34d9-89ba-c63de483a09a | -13.00662 | -44.11466 | 2025-09-13 04:08:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3397d9f7-9fc0-38cb-8f3d-20b86b1627cf | -9.24203 | -51.24131 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16bb2aa9-7039-3a1f-ae46-0a587424f96e | -11.44326 | -43.57344 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81483074-14f3-3ad0-841c-e45d0badcf66 | -12.80391 | -47.97506 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 23b251d9-ecd9-3d82-9e12-50ecd5fce2de | -11.17669 | -51.41868 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1233c125-69c5-365a-a527-b4780fcb6935 | -12.13156 | -44.84557 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1cfcb4c-d66b-31d1-bce4-ed1c3e5cd5b3 | -9.41612 | -43.41093 | 2025-09-13 04:08:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 63682024-7c93-3656-9453-8d32a0730f2b | -9.49471 | -50.89298 | 2025-09-13 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb315ce2-e739-3850-b730-823f8f991f46 | -9.96633 | -50.29315 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 07bb0c03-e7a4-31e0-9579-d396b56027db | -11.417 | -43.71596 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2249887f-f201-314d-a4d5-1e295fdafe6b | -12.72204 | -45.07736 | 2025-09-13 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7df90891-e277-33bd-b1d8-9d034b282e8f | -10.33665 | -48.82356 | 2025-09-13 04:08:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e28c39ed-f419-338f-bec8-b541f97a3f26 | -14.21384 | -46.26643 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f161e881-056a-3d4a-a59b-4c6a3fbf8466 | -14.43137 | -47.32767 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79d4f96f-908e-3d8f-87fc-de1901f31808 | -12.80854 | -47.97217 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 32c8a0d1-de1d-392d-b47a-f22a07140b1d | -8.09164 | -44.51664 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 164ebb64-3edf-3875-8cb2-d8c66a415755 | -10.77756 | -44.78127 | 2025-09-13 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aba7b560-8eca-3f14-b736-0d909a764b73 | -8.10189 | -50.19262 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be897477-f416-3633-af9c-ad9c21014ee4 | -7.95065 | -46.9113 | 2025-09-13 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95c58ed1-9804-3136-b3eb-e19efc93e823 | -9.48452 | -55.9752 | 2025-09-13 04:08:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 229cda33-237f-3248-913a-9b7d55096413 | -11.72538 | -46.616 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d95346f-c672-3ea6-be10-c4f4d388a1d4 | -11.86363 | -46.75844 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68460ee6-d87c-336c-8d21-9ee237b1e03f | -8.36462 | -47.57441 | 2025-09-13 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9c97ed9-803c-36f5-9a5f-5e4f951ebb2d | -13.89601 | -48.25288 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 05b5046e-3536-3798-b7d8-9412538a01ae | -14.43437 | -47.33254 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 79080590-178c-3eed-a028-cf18d04e53ec | -12.18271 | -40.40672 | 2025-09-13 04:08:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0a62ea3a-0ea8-32e4-a06e-86f09e5adf49 | -11.47346 | -43.61428 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22081f3a-416e-3343-b991-e3ca73564e39 | -11.3591 | -43.50115 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6c436ad-b379-354e-93e9-dc785046cf6f | -10.40598 | -50.58891 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fbf63a96-4a04-382a-bf73-5548de01b295 | -9.70294 | -47.53334 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e9defd3-f7e9-3454-bb00-ade8d2821afc | -11.1568 | -51.3824 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66a09523-3bbc-37ef-a8e4-760da142b0ea | -11.86075 | -50.57914 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| fd27db3f-6ee0-3c65-8f3b-7bef640e3e8c | -11.08126 | -48.43496 | 2025-09-13 04:08:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 590a5170-223a-3f0b-bbee-75502a0945a7 | -14.2054 | -46.27289 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 772be067-3c8b-38fa-b62b-0875acc6db9f | -14.18263 | -46.23469 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ce96f6c-62b4-33a3-9247-232850af9202 | -11.72695 | -46.60696 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0e261010-d779-3522-bf44-3da1ed1c185d | -10.38007 | -48.57437 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f7ec805-90da-3edf-b51f-cc99cb28a1dc | -13.26713 | -51.70749 | 2025-09-13 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f72252d-d7e0-3da6-b8c5-8ebf21d68163 | -12.0968 | -44.8679 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64b1ac1a-56cf-36e2-99d9-c887c8fc875a | -14.19118 | -46.24889 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fbdfdf3f-9dd5-339f-840e-ce274c8a4cb9 | -8.47525 | -47.26459 | 2025-09-13 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6fc9e77d-6674-3838-a9bb-52e15abaae86 | -11.20812 | -48.40713 | 2025-09-13 04:08:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2dc5bfb-3537-3bf2-88a8-ebc0c867c3c8 | -9.49985 | -50.89382 | 2025-09-13 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7992380f-9169-38c6-b76c-ae53a5043f9e | -12.99025 | -46.754 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c71edb1-1bc4-354d-8350-163cf18eb899 | -9.25703 | -51.24411 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3155ad61-fc41-3cad-b1a3-3d08cfb5ee20 | -12.56568 | -45.67345 | 2025-09-13 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28284ac6-9299-33cf-88ed-7ee65fd0f1e6 | -10.73683 | -50.50204 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d6154487-f418-378e-a401-d81067696de7 | -8.50956 | -45.14459 | 2025-09-13 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44f1111f-29bd-3636-ac62-00364de036eb | -14.19541 | -46.24558 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 523ed894-4ad9-314e-9694-df8c5186c21f | -11.4095 | -43.65586 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1cfcb1a-7b21-35f9-9ef9-bec170d9ac02 | -12.7186 | -45.07677 | 2025-09-13 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e69c070-072e-3cbd-ab53-0f0337bfdab2 | -11.83297 | -50.57272 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbdf85d8-7732-310b-902b-23654a66ebd0 | -13.9214 | -48.27237 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 083567c4-aa09-330a-b66e-26f9ee2effc5 | -10.75043 | -50.51037 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 07e149ed-e24e-348e-a9a6-3eb4114d87e8 | -11.86275 | -50.57303 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 73adb236-6382-3dfc-9dde-19c52f516e02 | -11.44164 | -43.56221 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a432aa48-97b4-30ac-94f0-6656fe1bebe9 | -9.51907 | -54.65099 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab3d35aa-ce0c-378d-bf16-4d5bfdb6d823 | -8.09806 | -50.18511 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 92701924-6130-3cbe-8239-c2849c13db0c | -8.66355 | -40.18101 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7c6a7bd7-6a7c-37ad-9d0b-0ade514f285e | -13.4026 | -46.79811 | 2025-09-13 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cc41eae-c61e-3bf3-b09a-147f85fcaad8 | -9.80721 | -48.39123 | 2025-09-13 04:08:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README56.md)
