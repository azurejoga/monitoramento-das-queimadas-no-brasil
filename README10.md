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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e0f80be-6efb-38a2-b402-b893bf886d56 | -4.94381 | -44.59465 | 2025-10-06 03:34:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f4ba0f3-66a1-3dac-a906-f02e4b7f1844 | -5.50087 | -42.2357 | 2025-10-06 03:34:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a6c7b07c-4f6b-36f1-86b3-97052ae8934c | -7.80459 | -42.57489 | 2025-10-06 03:34:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cec283df-b276-3bbd-83fc-f9cc227a74bf | -7.551 | -44.93636 | 2025-10-06 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3887412e-369f-3aca-87b0-f8fbd02b5bf7 | -7.71213 | -42.3997 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fc9d0905-d9c5-3290-9241-b9749ef1273f | -7.78337 | -42.60358 | 2025-10-06 03:34:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 922980b1-836d-3bbf-a938-5d4304532bda | -5.0375 | -44.45759 | 2025-10-06 03:34:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d07fce98-3209-3bd6-b045-d932c369ea10 | -6.32178 | -41.62084 | 2025-10-06 03:34:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d9f9694d-fd8c-3ed3-b69e-da6fcd944ab8 | -6.0556 | -44.08597 | 2025-10-06 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 088319b3-eefb-3596-baab-0f9a717a4ce2 | -5.32127 | -43.37146 | 2025-10-06 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db740589-128d-3d96-8316-aeab98acc905 | -5.4823 | -43.26441 | 2025-10-06 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b11cba4e-99b8-379f-acf6-835cf8b6d4e3 | -5.53297 | -35.78915 | 2025-10-06 03:34:00 | NOAA-20 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 582d6015-5649-3ccf-867e-ecd5cb7e87e2 | -4.74465 | -44.4407 | 2025-10-06 03:34:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 217fe090-a211-331c-9a44-90f500bf0c6e | -6.18856 | -42.71598 | 2025-10-06 03:34:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| efac6fa2-c8b8-3689-8879-c144feab1740 | -7.46374 | -43.0406 | 2025-10-06 03:34:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8cea8227-1b0e-32fd-85af-543ba51a03c1 | -5.33259 | -43.37382 | 2025-10-06 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afecccdd-ad9d-377a-9254-5941b91c94a3 | -5.50884 | -43.46149 | 2025-10-06 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ad3aa9a5-ecfc-33c8-a451-159aa31d0f90 | -6.04005 | -42.55151 | 2025-10-06 03:34:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d25a68e3-27b2-3f46-8d2c-a95b81a3e371 | -7.41994 | -41.13755 | 2025-10-06 03:34:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 82bc6e95-d1cc-3da5-b6ff-69f6e14d8394 | -7.42176 | -41.1271 | 2025-10-06 03:34:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9ce98d62-76ef-3fdb-b1a0-3bb5dda3ecd3 | -6.64721 | -41.96838 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7e136bd4-0d9d-349e-a6ec-5c1c5100c583 | -7.01603 | -42.29988 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| df91f9ad-1ef8-3a84-9b67-273a405abcd9 | -6.99648 | -42.83746 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 50543bd0-afef-3f3c-a533-834071c24f84 | -7.46433 | -43.03727 | 2025-10-06 03:34:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 532c3629-6a88-38cb-953b-80394a05f5b3 | -6.85078 | -45.48332 | 2025-10-06 03:34:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 880ae160-25cf-34d2-8fd0-45b55c79afa9 | -6.22846 | -44.39133 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9809599-6b5b-3d83-80aa-c1c84537a35f | -7.35866 | -45.22948 | 2025-10-06 03:34:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 098b5e9d-cd35-3fbd-b5d6-25f948d57677 | -7.73424 | -42.39437 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1737e9a7-a016-33ff-9475-3b896a1ad501 | -6.04804 | -42.55628 | 2025-10-06 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 18bd01b8-8807-35a3-91c6-46e6580a7b79 | -6.10029 | -43.53382 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e45c24a5-69e7-30af-a71d-29d4a7e83871 | -6.99587 | -42.84088 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 237ba768-5cd7-3216-8d91-459ba2b208f3 | -7.01431 | -42.79923 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 108c964f-47f5-3858-a3dd-66d3453a4bef | -7.21704 | -34.95705 | 2025-10-06 03:34:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e781869b-c7fd-3f92-b161-1db6e84011d1 | -6.0658 | -42.54905 | 2025-10-06 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ebdf6c26-b2f4-378f-bee3-2255a84e9337 | -7.79831 | -42.58006 | 2025-10-06 03:34:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0454faca-111e-3290-94a0-5af2f4e54280 | -6.04152 | -42.56203 | 2025-10-06 03:34:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 50f870ab-252c-3e43-8e5c-b7ecbaa70f19 | -6.04743 | -42.55969 | 2025-10-06 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3b6fde88-81ea-3f69-acf6-79a8f689511b | -5.79681 | -35.59977 | 2025-10-06 03:34:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a65dc238-5951-3751-84a7-efdebc0730a3 | -6.6467 | -41.97132 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ba417b4c-d2ed-3575-9923-310a616aa1bd | -6.07172 | -43.48443 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 343cf136-5d69-39e5-aa53-2694f161388d | -6.24787 | -44.26647 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7adcd83f-5c6d-3471-a266-c91ff648b8c8 | -5.27013 | -37.92329 | 2025-10-06 03:34:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2bdfa096-2ed0-37ee-99cc-bc497821966c | -6.04271 | -42.55536 | 2025-10-06 03:34:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4c3b1dfd-fe41-3a80-ab0c-80540526e62a | -6.40395 | -43.60897 | 2025-10-06 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29a63a3e-47a0-33fa-9f86-66f454edc256 | -7.45837 | -43.03963 | 2025-10-06 03:34:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f74da29f-f31e-38fc-bb1a-e9f387a575fa | -6.69659 | -42.15424 | 2025-10-06 03:34:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1da33a2f-9dbc-37ee-8344-d98c86d21f32 | -7.42266 | -41.12191 | 2025-10-06 03:34:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 61a1d7b6-e863-35b7-8328-8e21ba0118e8 | -6.6406 | -41.97635 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ccc8be1d-1fd1-35ec-8838-feee59ee3b38 | -6.10039 | -43.50066 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| db3d5fe0-3a04-3829-a7dd-257f9e34ec2f | -6.24875 | -44.26171 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbc7f024-8677-3338-a3f4-ecc2b6b6c16a | -4.89678 | -41.50749 | 2025-10-06 03:34:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ffa4e985-8e5c-372e-87db-4cd6628d2e49 | -4.31663 | -46.81358 | 2025-10-06 03:34:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4973d67-4957-3a3e-a01f-c7b09da7fc82 | -7.36205 | -45.23852 | 2025-10-06 03:34:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cdddbd4-2fe2-3e23-8af2-e04ec51e0c24 | -5.32901 | -47.29189 | 2025-10-06 03:34:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 88df3d21-60bd-368b-b938-b94854df08f4 | -7.77982 | -42.62325 | 2025-10-06 03:34:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c82b705c-b30c-3b5c-8125-43b1b4f7741b | -6.05276 | -42.56064 | 2025-10-06 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 64a33208-e88d-32ae-894e-6c97469bfe7e | -5.46011 | -42.79649 | 2025-10-06 03:34:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6c0fe4ef-40ec-3edf-ac7d-b2532654c200 | -6.05884 | -43.49137 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ffea97bb-ceb0-369f-920a-aacf17d6f6a4 | -7.01784 | -42.8103 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cadc7500-bcf0-3ca6-b12e-beb76c8b6b1f | -7.35685 | -45.23935 | 2025-10-06 03:34:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e5e8aa1-0f57-39b0-bc7c-ff3c39d7bd14 | -3.79316 | -44.47598 | 2025-10-06 03:34:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f428c4c7-ecb7-3960-a313-412c83803dbc | -5.95554 | -43.53362 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6684e93d-bf08-31ce-8926-30d297946714 | -5.45953 | -42.79993 | 2025-10-06 03:34:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e004785f-230d-31d5-ba69-661be48f0573 | -7.68239 | -42.59464 | 2025-10-06 03:34:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0fef36a0-5d79-337b-8857-2ae40bd06a99 | -5.41278 | -41.06584 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b959df1c-bb9d-3ddb-a591-34718c9aff3c | -7.51687 | -35.22709 | 2025-10-06 03:34:00 | NOAA-20 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7f2415ed-a487-3590-92d3-3d8554927ee4 | -5.45894 | -42.8034 | 2025-10-06 03:34:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 29b1cd1e-45cd-32cc-a886-c8f2de944989 | -5.95755 | -43.53388 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4348517e-b29c-3243-ae1e-132158a2a9e2 | -5.33461 | -43.37424 | 2025-10-06 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80ca8554-686a-39d2-a30a-a85aae2a8134 | -6.64515 | -41.98026 | 2025-10-06 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3dfe4f99-04ff-3d72-aa0e-93427a232295 | -5.45888 | -42.80758 | 2025-10-06 03:34:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2686ac27-1fb6-3ad5-a098-6b2144403f5c | -7.0161 | -42.78917 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5a9235a8-a021-3a37-af46-c670ecb45f78 | -6.78795 | -38.76175 | 2025-10-06 03:34:00 | NOAA-20 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9744045b-be93-3137-9462-427a7469d95a | -5.45834 | -42.80693 | 2025-10-06 03:34:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 08fe1062-5de8-3e0d-ad8a-439c843ab4b3 | -7.47119 | -42.62762 | 2025-10-06 03:34:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3de6b809-3b6a-3000-ab9a-a6d42fc0ddf4 | -5.41033 | -41.06685 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 53388cd9-7382-3b34-8cda-49721b86f92a | -5.47597 | -43.26746 | 2025-10-06 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c8cdeb7-5c33-393d-8ad1-d8c77ee6cb4e | -6.11306 | -43.52789 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bee3a2aa-e32e-3368-8ea0-1f241abe6bcd | -5.41178 | -41.34909 | 2025-10-06 03:34:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5ddbb305-85cd-3c80-ac42-18536b67e384 | -6.25132 | -44.26223 | 2025-10-06 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8e7d79b0-37a3-35f5-93f2-583edfd919cb | -7.71626 | -42.55503 | 2025-10-06 03:34:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 946dee10-51d9-35a7-86b8-1800a4fb38e7 | -6.25595 | -43.89754 | 2025-10-06 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c95be87f-2b31-37f4-883a-b860387e7010 | -7.71157 | -42.40279 | 2025-10-06 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 21629dec-ed4d-3cec-8cb8-04933495350c | -6.69444 | -42.1665 | 2025-10-06 03:34:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f0fb345f-cb34-3b0d-9e40-9e4b9d81fad0 | -5.46073 | -42.79716 | 2025-10-06 03:34:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e93288d8-dc9a-3270-9c59-6ea9fa11d7b6 | -5.45951 | -42.80404 | 2025-10-06 03:34:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2f50af20-0ca4-3939-84c9-3d2fc0cec795 | -6.77524 | -41.58873 | 2025-10-06 03:34:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 98633bfe-938b-33fb-b395-7a800f648b61 | -5.19413 | -46.15892 | 2025-10-06 03:34:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5d3c017d-2197-31ce-afec-bcbfc869f816 | -7.68359 | -42.58799 | 2025-10-06 03:34:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 57ace364-dc50-3ec0-a548-d994c1e540c1 | -7.79774 | -42.58325 | 2025-10-06 03:34:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f5c66f65-d451-3774-aac8-9b0db27a15a2 | -7.01549 | -42.79256 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1b4176bf-8d8f-3a2c-b89a-12416149ca39 | -7.7891 | -42.60152 | 2025-10-06 03:34:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9282ab17-131c-3608-bda1-dd206ef0415a | -6.6995 | -42.16782 | 2025-10-06 03:34:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| db359482-e392-3c12-b82b-0985ee193ca8 | -7.02563 | -42.76641 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e712b48d-d4ef-3fd8-b43b-5cd051776171 | -6.72658 | -42.16431 | 2025-10-06 03:34:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 63122a6b-4a5a-3447-9741-4ea1bc1e56da | -6.06529 | -43.48786 | 2025-10-06 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02bf27da-6627-3035-aece-51fdd3fbea7f | -6.66262 | -40.91253 | 2025-10-06 03:34:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d7aaad8a-ff81-3e1c-a122-b1c22292bbf2 | -5.64033 | -37.79647 | 2025-10-06 03:34:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3f0138c3-0207-3c62-b43b-9eaff346478e | -6.05749 | -42.56499 | 2025-10-06 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ee055ece-7240-3b1b-88a5-68fcc1618ba9 | -7.02733 | -42.78777 | 2025-10-06 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README11.md)
