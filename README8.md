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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 350aff75-080a-3b34-95ce-341e592529e3 | -8.976 | -46.0152 | 2025-09-17 03:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 1ecae8df-ba5b-32ae-b574-016455ce32b5 | -7.581 | -44.566 | 2025-09-17 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| fd1975e1-0fe4-3eb3-998d-7f7faaa990b2 | -7.5807 | -44.589 | 2025-09-17 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 8ee98ac6-f19c-373c-812e-17fcc513a9e3 | -14.8013 | -51.7033 | 2025-09-17 03:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| c2de03e7-9489-31d2-82ae-20e004b63aed | -8.9571 | -46.0172 | 2025-09-17 03:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| a47c711e-7242-3fcb-8f89-00f47ec4a7fe | -7.8259 | -46.153 | 2025-09-17 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 5f133280-e23b-3355-ae01-7097815a82c7 | -7.581 | -44.566 | 2025-09-17 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 39da1354-32dd-31eb-93a1-a5bc70d51f10 | -7.5807 | -44.589 | 2025-09-17 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 196.6 |
| afb680a7-d642-33fe-8c0f-8ea663c86760 | -6.8823 | -43.96492 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 23178a13-0e83-33b5-97ed-bfd44b112cbf | -7.78372 | -35.62901 | 2025-09-17 03:42:00 | NOAA-21 | BOM JARDIM | PERNAMBUCO | Brasil | 2602209 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8e9def1a-72de-3432-a846-ffa119dae7c5 | -6.87266 | -43.96014 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 52e056cd-42e5-3aed-9b5d-0550f3293ca5 | -6.1755 | -41.22965 | 2025-09-17 03:42:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 986acdd3-523d-3637-9d56-e0f3e6aeea4f | -5.77041 | -45.90895 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| dc8b4c4b-f21a-3972-88ce-0b8ee59fb48d | -5.79687 | -43.486 | 2025-09-17 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63dba7c2-4465-3237-8b6d-f31567812ccd | -6.59636 | -44.32334 | 2025-09-17 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb51f001-6805-3bb2-8847-3d569fa79bdb | -6.62095 | -45.57462 | 2025-09-17 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78025ea8-8e0e-331d-a2bc-438dc24c198c | -5.19068 | -35.86601 | 2025-09-17 03:42:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d2b771db-a668-34c2-9a4b-fa6d8e68649b | -7.25752 | -46.60605 | 2025-09-17 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 47f12478-9184-3fdf-b0b6-c9054d60aafb | -7.27125 | -46.58725 | 2025-09-17 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3eb2c470-e3e3-3c8c-8d73-9547210f663d | -6.19706 | -45.1236 | 2025-09-17 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4d81bc82-8184-3427-bd07-d28b83d28f51 | -7.58757 | -44.5881 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1dfca46-e4c8-32e3-a0f2-ec3f3e3e6dbe | -3.78066 | -39.88054 | 2025-09-17 03:42:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9d9a068f-8b61-3f92-8816-205e6c802b59 | -7.58872 | -44.58162 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62c7309e-2f2f-36ca-8d54-6ca622cdda16 | -4.3873 | -38.69065 | 2025-09-17 03:42:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| db0316f5-f209-3abe-8c58-9731699257eb | -7.58636 | -44.5645 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11f13575-a5d6-378b-87d6-73c506ddbdd0 | -2.92169 | -48.29984 | 2025-09-17 03:42:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 223f725b-149f-3ab6-9f15-f07714ccff91 | -6.96613 | -44.55747 | 2025-09-17 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 411f4dfa-a099-3f6a-8574-db2200ea7d33 | -6.95828 | -42.44224 | 2025-09-17 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 770e29ef-3e46-3adf-bb13-171aaa77a980 | -4.66711 | -37.83759 | 2025-09-17 03:42:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c149105-0202-3ae3-bc1f-a2f4a8c94955 | -5.80702 | -45.708 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79703a11-affb-3732-8bb1-8b3954ae6457 | -6.04628 | -43.1363 | 2025-09-17 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 73841d3a-ed67-3c8a-8b64-47f68db53443 | -6.64231 | -38.91463 | 2025-09-17 03:42:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c43e1dc9-e491-3c3a-97b0-bb9c122e120c | -7.57763 | -44.5831 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f073eaad-c9e6-3779-8d30-bce905fac1a7 | -5.77198 | -45.9003 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f47548ff-a25a-38e7-9d4d-a26ccf9f56e1 | -6.87614 | -43.97 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b37f42ca-3b5e-32a0-a87c-b41a21c58b2d | -7.58814 | -44.58486 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c3de392-14e9-3dbc-af0f-cbfc8e0f71a1 | -5.62973 | -44.82954 | 2025-09-17 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 797eda77-79b2-32d2-9c79-6b75b032f945 | -4.389 | -38.68904 | 2025-09-17 03:42:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a923d406-2e8d-3393-b853-d9fa1f9b64be | -6.36616 | -44.40689 | 2025-09-17 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b68186fe-180c-3b7c-8b92-20e45462dfa8 | -7.65201 | -44.47161 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 560f8306-8fcf-344f-a47c-509d6dcb1178 | -5.5991 | -45.35968 | 2025-09-17 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9a713830-c7ac-3ea4-9a5d-e866e01dd626 | -6.87667 | -43.96703 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1957a085-aa58-395a-aa56-2456dbfea0ac | -6.76583 | -43.40177 | 2025-09-17 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f6701ffc-62ef-3f27-bd26-6a03a3086af4 | -6.97918 | -44.45164 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e2585d7-7863-3b18-8584-0dc60ce994e6 | -5.61326 | -42.8989 | 2025-09-17 03:42:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 15628960-5e19-32ba-9c20-da69c2daff0f | -7.5759 | -44.59279 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 5fa78947-9caa-3482-8e4a-99e81dcbf467 | -7.57648 | -44.58956 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 223eab2b-b25f-376e-983a-9bd117987c7b | -7.68386 | -44.47348 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9604b38-01aa-35a2-982f-521c68d60df2 | -7.5852 | -44.571 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 086384ab-3be3-37d3-a556-ecddd62e9f7d | -7.27367 | -46.58609 | 2025-09-17 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9257d85-3640-3b15-98ba-225ea66c74c7 | -7.59339 | -44.58579 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62c1d9b7-e0e1-37a1-bb7d-013fde1aa1b6 | -3.21873 | -47.12677 | 2025-09-17 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6826c675-762e-38f0-8467-8d66a839fe0a | -5.53167 | -42.18173 | 2025-09-17 03:42:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| bf0d9bbd-ba43-36c0-b0be-96a615d6df66 | -3.2355 | -46.79821 | 2025-09-17 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 57fb1872-8246-3f98-b239-de03ee044386 | -3.59916 | -38.95259 | 2025-09-17 03:42:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 32.3 |
| 7f8b0f28-8712-3de3-be97-ae8c341f5d2e | -7.8356 | -43.85535 | 2025-09-17 03:42:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0257fa32-0e6d-383e-bfd6-b3d1742d20a8 | -6.59165 | -44.31932 | 2025-09-17 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28201733-31d0-37a5-9278-5e4bdc335a65 | -6.74005 | -47.00079 | 2025-09-17 03:42:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 651bf01c-95dd-37bd-8e71-0e81173bddea | -6.40723 | -43.35199 | 2025-09-17 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f0e9a3e1-3820-3c89-a49c-e5973acddf35 | -6.29356 | -42.38489 | 2025-09-17 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 43187d97-c5dc-3722-8824-420f48d840a3 | -5.79083 | -43.49095 | 2025-09-17 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d431fffd-71f0-320a-9dd6-f5fddcf4fcf0 | -7.64679 | -44.47078 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a5665a7-f6eb-3710-b0ea-a45fa540b370 | -6.95505 | -44.55841 | 2025-09-17 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cedd3fd-c5b9-3176-8610-2cd028ff06c6 | -6.29189 | -35.20457 | 2025-09-17 03:42:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8c8c8ba8-7b6a-3d96-a9db-972636fe1478 | -6.33378 | -43.32703 | 2025-09-17 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fc573e77-3cbb-34cc-902f-69eafefe53bd | -6.40229 | -43.3512 | 2025-09-17 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 911e8648-1289-3055-99f9-edfccc9ffa05 | -5.81957 | -46.36054 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| efadc6ce-7262-3072-9c1e-8a872ce28b41 | -6.16571 | -43.67476 | 2025-09-17 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52f34ad7-f96b-3293-9e71-d140c6fa8ca7 | -6.87091 | -38.43851 | 2025-09-17 03:42:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6d165a9d-3b5a-3308-a8d1-a8bc6a880213 | -7.09348 | -44.53674 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bd317d08-1c3d-35ec-8490-a63f5898b89b | -6.87159 | -43.9661 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 71b788ef-ce0f-392d-989b-61f939531713 | -3.23731 | -46.78748 | 2025-09-17 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5b7d0f95-f7d2-3467-a344-6acf00c75f20 | -6.18116 | -41.22223 | 2025-09-17 03:42:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 66649352-6723-3ee9-97ff-2b1ef7230355 | -6.5911 | -44.32254 | 2025-09-17 03:42:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 355fb460-9e17-3ed0-ab5a-c33db71686cb | -7.34366 | -44.59092 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 169a166c-8e65-3eb8-8ca9-87603eec4ac7 | -7.57238 | -44.55199 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f58daab1-c010-34cf-bf08-bde182b531a2 | -7.3369 | -39.71445 | 2025-09-17 03:42:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0aa64f12-c94a-326a-a943-360286684e9c | -6.87105 | -43.9691 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cb07a05-56ba-3646-a06b-8d9d589a7d2f | -7.06817 | -44.34546 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 49e01d69-fbd1-321f-9a34-4a4d01090a37 | -6.29519 | -35.20509 | 2025-09-17 03:42:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ea7a0180-4d7f-3098-b4cd-46198f9f6c69 | -7.65605 | -44.47892 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 079c0069-828f-33a0-bb2f-f72e89a1d843 | -6.97592 | -44.53256 | 2025-09-17 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86ae885b-86b2-3ad7-9537-a0bb956f29ee | -3.51177 | -48.4487 | 2025-09-17 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fb13218-1d4d-30e0-aba4-5c9ddf720069 | -5.50114 | -39.70536 | 2025-09-17 03:42:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a37a5649-e226-3c64-9bf4-df0044d7f3ef | -7.58578 | -44.56775 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 016cbd5d-4d7b-36e7-820a-200279725cd8 | -6.67945 | -46.30441 | 2025-09-17 03:42:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| dacac5e6-ad07-3089-8e7e-2cb5c7de27ff | -7.65135 | -44.47052 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8bcc257a-7373-3e63-9813-c1bfa8138954 | -6.88017 | -43.97683 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31adeae5-13cc-3777-bffd-6313c74bf5a0 | -7.32478 | -44.05987 | 2025-09-17 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6af6d68-c7c7-30a5-8af7-94e605b83430 | -6.95367 | -42.44159 | 2025-09-17 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| c7b4f653-92df-3989-b2eb-cd362ab39bf3 | -5.67383 | -43.51067 | 2025-09-17 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8a32d46d-2402-3220-9ee8-b25f32acb6b4 | -7.58347 | -44.58073 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b7e4e3e5-0e4e-3a67-8286-6b520a26694d | -6.22289 | -42.02159 | 2025-09-17 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9769f1e3-397f-3a8b-9ace-3d739a947c9e | -7.6816 | -44.66708 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e47b31e8-4cbc-330a-80e2-014127a27dad | -6.88124 | -43.97088 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1af690ab-4a8b-379a-ad79-dd9b470b4a25 | -7.31092 | -43.96918 | 2025-09-17 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b7e87068-eea7-3195-91f9-328f6d139bae | -7.84158 | -43.85045 | 2025-09-17 03:42:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26cac835-909b-3447-8d0b-f5dc07a4e59d | -7.17174 | -44.34169 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0df6a617-21dd-3f7c-9778-ea2b3671794a | -7.31146 | -43.96608 | 2025-09-17 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f6bc88d3-e38b-3aaf-aaec-7e747aa1640b | -2.92048 | -48.30678 | 2025-09-17 03:42:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |


[Clique aqui para ver as próximas entradas](README9.md)
