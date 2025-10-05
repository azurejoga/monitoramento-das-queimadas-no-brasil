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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c1949ac-2d38-324d-83a9-f1fe089d8e9a | -10.40411 | -45.39788 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c2dc750-903f-3c79-85a1-77f0178f81c7 | -6.40899 | -43.05546 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8c182b1b-746c-3f5a-bea5-a9c8e8c87f13 | -10.19478 | -45.53322 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 335ac374-f846-3db5-9583-4493fca937cb | -5.83212 | -43.35687 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1091c9d0-1f28-314a-bf0b-15e99a486700 | -8.18565 | -44.14658 | 2025-10-05 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f965da6-c9b2-346c-9872-c2e540914fd9 | -7.81426 | -44.53825 | 2025-10-05 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 71429ec0-472f-33bf-9399-24d81a2f98e2 | -6.76383 | -42.23816 | 2025-10-05 03:53:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7fd5bc63-0c87-319c-9fac-a5c5a580f2d6 | -8.56209 | -46.26464 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7d9fdc83-f7b2-3d5c-8711-53e06bd252a1 | -5.46796 | -42.79194 | 2025-10-05 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| df3624cf-e159-3e03-a5e8-42804a34c54c | -5.89039 | -42.91161 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 37.7 |
| 3de74e94-8d13-3ab0-ae41-831c27686185 | -5.58543 | -43.40749 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5ec9de7-6d4f-39dd-bf39-3153099e5702 | -5.64694 | -43.91599 | 2025-10-05 03:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 83404225-b8d9-3762-8daa-32fb89e119e2 | -7.69363 | -42.57357 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dc0b96f7-cf09-349d-b5c3-c61ea3696904 | -7.05324 | -42.76397 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9b29d415-dc5d-3edf-a200-5ec3b2fae147 | -7.64656 | -45.42586 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f832f56a-cecd-34db-b3b3-6d5d5c341ac6 | -6.61363 | -43.71877 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e261208b-69fe-3f1d-8595-4cabae223647 | -6.40414 | -43.05996 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d7159a93-96c6-3783-9f71-3bf86ad918ba | -5.97824 | -44.36335 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf63b8b5-e279-3bda-bc15-0340dabcb56a | -6.74236 | -44.00416 | 2025-10-05 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3708d459-5496-3369-a683-d5e957a69d23 | -5.66454 | -42.70076 | 2025-10-05 03:53:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 91681750-91a3-3f9c-9de3-3a14e9d51e1f | -5.97534 | -44.35409 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b142679-19f7-3cee-a836-73281a1fae46 | -8.55582 | -47.27069 | 2025-10-05 03:53:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b77cced-30b4-30d5-afab-d559b8f69a86 | -6.20896 | -44.07664 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13f45529-5e39-3c27-9522-96a1bf20c31a | -5.21212 | -46.18052 | 2025-10-05 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c9858df-92bf-307a-b0de-753fed86fa44 | -10.19026 | -45.5331 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5bdc4f70-9859-33a0-90ad-2e919bd522b6 | -10.19041 | -45.5073 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d59fb07-c1a5-358d-a1d9-d3ceef90ad30 | -5.0008 | -47.21326 | 2025-10-05 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11f4b39f-35d9-3334-b1d1-b890734f6f52 | -6.05788 | -42.53679 | 2025-10-05 03:53:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e70b2a2c-a6a5-36e6-a0b0-a96f460faad7 | -7.47103 | -42.62778 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a54e8d28-e200-3c85-9309-c7d0efc112e8 | -8.93448 | -48.66427 | 2025-10-05 03:53:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e372ceec-cc9e-3627-98f4-5029a9805d34 | -6.55858 | -44.16672 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b753a8e4-3c0c-316c-89a8-89496c7450fd | -8.53835 | -46.31438 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6f5233a1-6da6-304f-b3a7-e972c87b8bee | -5.10982 | -45.46886 | 2025-10-05 03:53:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed182b1a-ac40-32ff-90db-5ceca7c8dd79 | -6.3393 | -43.46663 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9959c709-c82c-367b-a702-275d3d4ee548 | -8.23505 | -46.81868 | 2025-10-05 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dbbc1cb5-85d9-3ea3-8f0d-538f57891a99 | -7.79172 | -44.13659 | 2025-10-05 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b56df63e-d25b-3ce4-8aa2-403a7aa8f857 | -6.70845 | -42.83018 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 102db098-d00b-3b12-9714-b5bfabfdf7a0 | -4.31913 | -48.09223 | 2025-10-05 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 44ecb962-57c1-30d6-b5a8-fd7c2aba97ab | -6.78223 | -41.58781 | 2025-10-05 03:53:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0bf05180-4853-314b-bc8e-de680ad9727a | -6.18755 | -42.72266 | 2025-10-05 03:53:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 08ab0223-f9a0-3e66-b307-42e4a0a39147 | -8.56124 | -46.32402 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3f33da2-72b8-35af-aa33-759ec0779c55 | -8.16723 | -43.34357 | 2025-10-05 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 19501bc9-099c-34d0-aa51-8278f6662f14 | -7.31195 | -45.56169 | 2025-10-05 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1a716cc5-44d2-3384-8cad-7c381ffbfb8f | -6.40553 | -42.69292 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1fd4406f-1b0f-3588-8918-2e61e94ae9cd | -6.2425 | -43.04622 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a1d2154-78fd-3cc2-94c2-073466c58396 | -7.64282 | -45.42036 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 62cddbcf-a233-30a2-9b1f-f479a9b45620 | -5.78089 | -42.94084 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6322a112-a1f3-3bc4-a031-38e804cf35c2 | -5.22677 | -43.70538 | 2025-10-05 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61aea7f6-453e-36c9-9191-047ba675ef8f | -7.52293 | -41.27232 | 2025-10-05 03:53:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 63ed8b7b-b59b-32af-aef8-2fe0226f251b | -6.25876 | -42.77755 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2e9ea8ef-d37e-3f4f-8e94-632185326aa3 | -5.30117 | -43.1124 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94c47e18-d111-3aa4-ac78-b8036ef22032 | -5.91285 | -42.53361 | 2025-10-05 03:53:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 186590ba-d11e-3b07-9efd-84785032b6de | -5.27859 | -42.92068 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7a8d47b1-5ee1-393f-be59-12950cc5116c | -8.54711 | -46.32038 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 992c7a3c-1473-3be5-8272-3e10d4ceeaa1 | -7.01098 | -40.31794 | 2025-10-05 03:53:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c98d7046-b1dc-32fe-afae-acfb8c691873 | -7.4657 | -43.04107 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7bffff48-7dea-383d-bbf1-05b3b6540f02 | -5.49178 | -42.79572 | 2025-10-05 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 41128676-a2e0-3a3b-bd6f-1bbb2920e194 | -5.35979 | -45.95442 | 2025-10-05 03:53:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d542073c-e744-3254-8344-696c50121739 | -5.49091 | -42.80093 | 2025-10-05 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| e76d6a7b-9f19-3cb5-afbc-e34b95a00934 | -8.34222 | -49.5031 | 2025-10-05 03:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4333044-73ee-3217-a0b9-c620be568742 | -6.70673 | -42.16054 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8e798b45-a512-371f-a4a8-e51aec2fdfa4 | -7.31659 | -45.98741 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 057c25d1-5f66-3eeb-9db7-0d2544b7bece | -6.32499 | -41.63313 | 2025-10-05 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 67ea0d9e-890c-335e-8fa5-a19ecc5c1891 | -6.14771 | -44.61317 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ddd4dda-74be-30ea-a9c2-003fcf438e22 | -10.39326 | -45.40859 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3d167a2b-523e-3c9f-be4f-0683e542a5cf | -7.76172 | -46.31273 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80d47f2a-07c6-3ad8-a43c-2a8b9423fa8f | -6.29581 | -44.05524 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8e31100-5eb0-39d7-9080-7d9bd3a6ce0a | -10.35047 | -48.1635 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67ed82bf-4665-3972-9828-708b45ddf92a | -7.78449 | -42.58649 | 2025-10-05 03:53:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c37d2e14-cef3-3491-85b4-9cd68d816a64 | -8.63123 | -44.91032 | 2025-10-05 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 460a67cb-c523-3294-bb58-0920658e80be | -7.42713 | -41.12564 | 2025-10-05 03:53:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4b5ab13a-3fa8-3ad4-9188-b3f1e10f069a | -6.35422 | -43.91494 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c4f4951b-339f-3214-a585-cb05673de3a4 | -6.98883 | -44.21397 | 2025-10-05 03:53:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 89bd136b-ec29-3205-95a5-c46f00be9cd9 | -10.63588 | -46.35035 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 578539dc-8d9c-319c-a0fa-2aba3d0982c4 | -6.94337 | -47.04764 | 2025-10-05 03:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65034a9d-4049-3428-ba1c-5b8d87e7eee8 | -5.66969 | -42.74368 | 2025-10-05 03:53:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 743345ec-a0f3-30e0-8975-d90e6232045e | -6.87224 | -47.23637 | 2025-10-05 03:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73e1db47-c586-383c-9054-20ff83e44a9f | -5.76848 | -45.78439 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 21b8fabe-a3b7-3e06-892c-589e8240c736 | -8.13695 | -44.09652 | 2025-10-05 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 592bbb3d-7292-3d25-9c90-42f0fbd94849 | -7.25093 | -44.89926 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4100c81-897f-368d-95c6-0a10af9883ec | -7.20303 | -46.85995 | 2025-10-05 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4996b0d-037d-3b17-b9f1-e94ba94b0717 | -7.60654 | -45.46584 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ed16e82-4b25-3f84-911c-c8c2f1aba143 | -8.14046 | -44.10096 | 2025-10-05 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb8a4359-c460-3840-a2db-033de28f0cef | -8.57556 | -46.3266 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 7721addf-8b88-3196-bc37-61f03b750505 | -5.43198 | -42.93242 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ddb5f556-c5dc-3ca7-ac86-6571081ddbb4 | -6.45969 | -44.58577 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 89ef77fd-efa5-37c2-9a64-9bd7275a3159 | -7.45952 | -43.05415 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8d0c81ed-c5b7-301b-9ff9-699701a709f0 | -9.56844 | -46.12221 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| dff93157-087d-3d0a-8e1b-a348bff9fd60 | -6.01946 | -44.01872 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e94e4a2b-64e6-3066-8df3-de4688e753d9 | -6.40314 | -43.6056 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b823a95-4845-3b61-a516-6b2e43443050 | -10.01331 | -48.29431 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 343203c6-a1c7-3d9e-a543-a9cbdf9a1f0d | -5.74293 | -42.54343 | 2025-10-05 03:53:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b5eed3fd-f1a5-32c7-b3d3-dbba93851cd2 | -6.14092 | -43.50575 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c8dc936-5e6c-3e9c-86b2-c5e834df0617 | -10.35868 | -43.73185 | 2025-10-05 03:53:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbe311ea-d82e-3add-8a5b-740f7cd36422 | -7.24871 | -44.88541 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7635613-c8b3-36ca-95c7-54513895af71 | -7.65629 | -45.45095 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ae141b9-6219-30e3-ae76-2ce0c238a45e | -5.9559 | -43.51775 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4cd99295-9d03-349c-9fb3-22cbb79e386f | -5.94226 | -43.52328 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16124340-3ee7-3885-ad5c-196bf85c9f9e | -8.18281 | -44.13837 | 2025-10-05 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68c81fcc-bd1f-3795-8d8c-3669f5947ea3 | -6.32998 | -43.90244 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README41.md)
