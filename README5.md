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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce8677d4-12e6-325c-bfab-9ca2869bdc3b | -12.4896 | -45.3278 | 2026-08-11 03:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| a5fea2b3-246a-3997-a807-d38793458b72 | -4.2635 | -48.1799 | 2026-08-11 03:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| d1ede64a-9edc-3e1e-b452-8ee095eb04d4 | -7.59388 | -42.77147 | 2026-08-11 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0592972b-2d73-3d79-bfd9-df3d2c85f1ef | -9.38323 | -47.49221 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 64c92e17-c2e0-306a-a4ed-bfe6f511b859 | -10.58189 | -44.78135 | 2026-08-11 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc73ec1b-0e70-3c62-b903-1c86df397a95 | -6.94794 | -44.22754 | 2026-08-11 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d902761f-56f0-3e75-bffa-1ca4a9d93191 | -9.73748 | -37.94773 | 2026-08-11 03:47:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3546d745-b42a-3356-90bc-1a93227e2f43 | -9.48512 | -40.30893 | 2026-08-11 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb4494d3-498c-33d3-b77c-469fba412c6a | -7.59167 | -42.76519 | 2026-08-11 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 02d07fe8-32b2-3f7e-accc-df766032a881 | -8.63992 | -45.85783 | 2026-08-11 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3871885a-b761-39b9-a71f-bddfcffca67f | -8.36527 | -46.3882 | 2026-08-11 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7833285c-436a-37ba-bcf0-d74b676095c7 | -7.65967 | -44.38784 | 2026-08-11 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7914f42-fdd8-38ce-92ab-2ce7f104d80f | -6.9474 | -44.23059 | 2026-08-11 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f0e61e9-b326-3cbe-80b5-88519c578d78 | -9.39569 | -47.46015 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 062b62cc-2187-31d8-8249-79d1993c913d | -8.53532 | -49.69527 | 2026-08-11 03:47:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87e46323-737d-3027-be0c-511de2c2e7fc | -10.23707 | -45.86058 | 2026-08-11 03:47:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85f369fd-315d-3883-9108-e34672bad33a | -4.97718 | -37.2333 | 2026-08-11 03:47:00 | NOAA-20 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b696018f-427e-372b-a89e-c842d19c3f7c | -8.6355 | -45.86018 | 2026-08-11 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de4e4b43-e86b-3bc3-a74d-daf73320f687 | -9.13677 | -46.39222 | 2026-08-11 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08a61c57-58d7-3a05-b658-fc146036d015 | -8.53233 | -49.69638 | 2026-08-11 03:47:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c86d22f0-16a9-314e-8a44-16949ea34a96 | -9.37258 | -47.51472 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| dbec0087-f0e4-3b91-8d08-5c13d252cb9b | -9.38436 | -47.45324 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c46eab1a-1349-369e-a7ae-c85a0c160e9a | -10.21917 | -45.86598 | 2026-08-11 03:47:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0dba4e29-bee8-3b31-9e6a-b56e96085490 | -7.61065 | -42.78458 | 2026-08-11 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d838beee-1de2-397b-a6d9-d626206fae6a | -11.23483 | -39.41076 | 2026-08-11 03:47:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5c06cd20-d166-3c5e-af35-498d88e80563 | -9.3735 | -47.50994 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 0a1ff9a5-6397-3727-af08-24417a311531 | -7.61616 | -42.78036 | 2026-08-11 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| aaed6c3d-93d9-3365-9463-3584f1ef0153 | -7.59563 | -42.76164 | 2026-08-11 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 231804f5-c96e-350d-a876-7e89dbbf6a90 | -9.63648 | -45.51513 | 2026-08-11 03:47:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b86038b-fdce-3ebe-bec8-d9611538b1e9 | -7.62339 | -42.76637 | 2026-08-11 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cefd5623-60bd-37c3-8114-3fcb94862643 | -7.389 | -42.86728 | 2026-08-11 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fed5061d-7daa-3f9b-ba62-b7fb9609211d | -10.23151 | -45.86021 | 2026-08-11 03:47:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9b8aa705-69fc-3a73-b397-0220014a87d8 | -9.38144 | -47.50157 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9ee1322c-f496-34c5-a0e3-811c0df8a85e | -9.39049 | -47.45425 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae0292ee-82b7-3a06-8766-a163ba07a0fe | -8.29995 | -46.38589 | 2026-08-11 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e27b82e8-03ed-3f7c-8ac8-0659f2601ddd | -9.37073 | -47.52439 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| df355dc7-f661-311e-85a1-63e13799ee70 | -9.39386 | -47.46972 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc90dd74-aeb3-360d-8069-ae67320ff76d | -8.23491 | -46.25244 | 2026-08-11 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 338ec2d1-f9b0-3783-ba88-7ab289e076ba | -8.63933 | -45.86097 | 2026-08-11 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06272f2c-1a28-3908-a69e-293e3232f2d2 | -4.64444 | -42.46649 | 2026-08-11 03:47:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4aba5e3f-785f-3fc5-a3c1-2e8b9932d636 | -10.23649 | -45.86368 | 2026-08-11 03:47:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58d74953-267d-3ad1-9cad-5fe09f0ed2aa | -8.36452 | -46.3922 | 2026-08-11 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bf92089-1f44-303f-b195-8cfcaf9205ee | -9.13602 | -46.3962 | 2026-08-11 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6a31f73-e2ce-3454-b19c-db893a18b96e | -3.02335 | -39.9768 | 2026-08-11 03:47:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ca400a62-7dd1-35ee-8879-9498284ced5a | -10.23593 | -45.86664 | 2026-08-11 03:47:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ad80e9d-7672-3702-8654-0b8b67a62b0f | -10.23328 | -45.82088 | 2026-08-11 03:47:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c83fa3c4-db94-3b9b-99a3-31af5b136748 | -8.30508 | -46.39063 | 2026-08-11 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22fc543c-ccdf-37dc-99f3-e9bed771a68f | -9.37167 | -47.51952 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 852ad805-2b51-34a2-95b3-989efbeff2c6 | -8.29917 | -46.39012 | 2026-08-11 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 322324c5-dc07-32d9-945b-22b6b9ad57ea | -9.39201 | -47.47943 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0d6892b0-5f2d-3f75-90a5-f63c118e43f8 | -9.39022 | -47.48882 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2f78d6ff-88e8-3afb-89fc-f3070aa49794 | -9.38934 | -47.49342 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| be7b066c-3041-36d7-ae0d-2657d6c156de | -4.97657 | -37.23709 | 2026-08-11 03:47:00 | NOAA-20 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2f3ab42e-a344-3009-8c98-5bf42a7d3dd9 | -7.38052 | -42.86068 | 2026-08-11 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b436e9e1-636b-3ac5-b2fa-e6be5aece82b | -7.62253 | -42.77127 | 2026-08-11 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3241baa8-9693-3865-8dcc-06c69d112aa5 | -10.23872 | -45.82178 | 2026-08-11 03:47:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d200a7f4-6f8c-3b1a-ab0e-15cdce83da41 | -8.62926 | -45.86272 | 2026-08-11 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 816e6cda-c891-3438-b2a6-e1a0938b3203 | -9.36462 | -47.52317 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b7f1ed5d-d6f5-3771-91e8-1c053f143616 | -8.23568 | -46.24826 | 2026-08-11 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f87a4d47-344e-3143-a3e7-ce9d7c28f45e | -10.22315 | -45.81503 | 2026-08-11 03:47:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 88b21622-9b96-3ee8-9e28-e508c72912df | -10.11015 | -46.19894 | 2026-08-11 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 11ae5a2a-0cd4-3fda-97dd-aebf43a567ca | -9.37963 | -47.51107 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5c2013ea-b959-3d98-beaa-cc8ab3aa0e25 | -10.58122 | -44.77997 | 2026-08-11 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0582f766-1ae5-35e1-b142-9935291528a5 | -10.58065 | -44.78297 | 2026-08-11 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e88a81ee-2217-3be7-9e2e-239a8bdb979b | -10.23767 | -45.85737 | 2026-08-11 03:47:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 167e01df-de36-3655-8948-ecafdf7b2707 | -10.24339 | -45.85682 | 2026-08-11 03:47:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 14aa3591-d70b-3134-bb2f-2d8faf1a1d77 | -9.38524 | -47.44867 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3265b39b-e434-3512-be74-bd3f666692e7 | -10.57685 | -44.78045 | 2026-08-11 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a2a7928-17db-3bbf-8855-551a10fcffe5 | -9.38234 | -47.49688 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 8290410b-c9c4-3a4c-9291-9868f42ac04a | -8.55807 | -45.35475 | 2026-08-11 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e586d50-b4c8-3916-a0e0-14035bfa8156 | -8.31284 | -44.77969 | 2026-08-11 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d3b867a-d22e-3cf7-81c5-f898fd488131 | -8.23544 | -46.25089 | 2026-08-11 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21a4e5b7-d8bd-3c4b-a023-8b56ad25e857 | -8.29327 | -46.38951 | 2026-08-11 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f34f154-eef1-35cf-9feb-5f12300dbeb6 | -7.38519 | -42.86155 | 2026-08-11 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 24e8facc-e9e8-3dd4-88e2-465f5a07674e | -10.24275 | -45.86026 | 2026-08-11 03:47:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 34acc083-02a3-37b0-b010-a34cc0a1b22a | -10.22246 | -45.81868 | 2026-08-11 03:47:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa3830af-c12f-3450-9e03-00946e9860b2 | -8.64168 | -45.85801 | 2026-08-11 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64d8cbe3-e30f-308b-92d7-d7fb09ef6f9b | -7.59013 | -42.76574 | 2026-08-11 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c370a724-a540-3570-83a6-06b4453f9489 | -7.38814 | -42.87218 | 2026-08-11 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 940d084a-c35c-311d-a00c-195cb6d950d1 | -9.38957 | -47.45908 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83f4af6f-3a2f-311d-b25b-dfb7e92fb5d4 | -8.30585 | -46.38649 | 2026-08-11 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7011d87d-ea6d-30c8-89e0-5ff7217147cd | -9.39293 | -47.47458 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98650bb0-954d-37b3-9768-f7f9e8521b7e | -9.39111 | -47.48415 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fdda6627-f396-35fb-8730-8b836ba7c915 | -8.63371 | -45.86008 | 2026-08-11 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be693651-1c22-378b-a15e-e60298233498 | -4.70272 | -37.81055 | 2026-08-11 03:47:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 38d0ca0d-15db-3792-892f-3ab9b56464ba | -10.21849 | -45.86963 | 2026-08-11 03:47:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe473e45-d917-3f34-ac3d-6a010ab84c83 | -9.3787 | -47.51591 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1717f8a5-fe63-305a-9ddf-aeb8dbfa8b1b | -11.23553 | -39.40663 | 2026-08-11 03:47:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b9ca2d8d-c782-36b5-bb05-c05ff778b8da | -9.38054 | -47.5063 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 15482051-94d2-3d5f-acd5-448db6d6a830 | -8.52831 | -49.69374 | 2026-08-11 03:47:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c5a9b21-da31-3c88-ba8f-d3ffbde302fa | -9.39477 | -47.46494 | 2026-08-11 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9b9c630-18a8-3d01-8bd4-d2e75bb85b1b | -10.2309 | -45.86345 | 2026-08-11 03:47:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ef2124e-bdc1-3077-81e4-2b4bb058f779 | -5.25748 | -36.69275 | 2026-08-11 03:47:00 | NOAA-20 | PENDÊNCIAS | RIO GRANDE DO NORTE | Brasil | 2409902 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 040618fd-c107-3c91-95a7-60cc3a9e58ef | -8.31349 | -44.77599 | 2026-08-11 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fb91e98-4f3d-3f61-8283-d6e7480d1c4d | -10.58135 | -44.78434 | 2026-08-11 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52d19ce9-875d-3bad-8362-2ec9edbc8ea0 | -8.55333 | -45.35013 | 2026-08-11 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82e857d5-d510-35b4-8212-5ac890d6ad3d | -7.61529 | -42.78532 | 2026-08-11 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c44913a0-284f-31d4-8040-2c89cb0c8813 | -10.10947 | -46.20249 | 2026-08-11 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f72b9cc8-fa3f-3ab9-ae58-034b807f3a5d | -8.29404 | -46.38533 | 2026-08-11 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bf9083d-bdaa-31f4-915e-f216c3b4a667 | -13.59332 | -46.24797 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README6.md)
