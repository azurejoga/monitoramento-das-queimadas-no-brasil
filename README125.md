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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62931170-c472-3efa-b70d-fcfd513e09a1 | -5.99434 | -43.47639 | 2024-10-10 05:14:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 058d815b-44ad-3b10-ad1d-e0934c29b519 | -5.99299 | -43.48541 | 2024-10-10 05:14:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1739f600-8360-3f9c-bc18-8a813fef355f | -6.44007 | -44.26186 | 2024-10-10 05:14:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4980ea6a-c06f-31d9-ad81-2ced8727c46a | -6.20626 | -44.10679 | 2024-10-10 05:14:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e794d15c-d65b-3aee-99be-3df016742931 | -6.07099 | -44.63987 | 2024-10-10 05:14:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 98189afe-0194-3baf-8d5b-8e4d7dab3783 | -6.06966 | -44.64871 | 2024-10-10 05:14:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 89a24d3d-01cb-3386-84f5-c919ac4f57f4 | -5.70668 | -44.78752 | 2024-10-10 05:14:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b06a9d1f-e88a-36b5-b40b-c160b7ee8be0 | -7.20902 | -43.99717 | 2024-10-10 05:14:00 | AQUA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3b35fb97-58c2-3169-a047-ecf0e8e7df97 | -7.31478 | -44.9649 | 2024-10-10 05:14:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9410c98f-6671-3e5c-81a3-22f60ec0b01e | -7.31345 | -44.97376 | 2024-10-10 05:14:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| bfb61033-6657-3a4f-b183-008f22726bd1 | -7.3046 | -44.97244 | 2024-10-10 05:14:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 2c2bc4c4-8ee1-3448-95ae-2cebc253c5bb | -7.30327 | -44.9813 | 2024-10-10 05:14:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 90367359-f25f-3f45-a662-bc5e197c7689 | -6.94226 | -44.6078 | 2024-10-10 05:14:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fd1a339e-c18c-3f5f-80a0-c545fe299231 | -6.51205 | -44.3414 | 2024-10-10 05:14:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e7f66456-b49d-3bc7-9c96-efc5fecafd65 | -7.63 | -45.26398 | 2024-10-10 05:14:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6bf3b224-0255-3f40-971f-3fb5d4390a76 | -7.61648 | -44.85653 | 2024-10-10 05:14:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dfcffca3-2979-3c9c-b490-b120b6c7072a | -8.36396 | -44.11773 | 2024-10-10 05:14:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 08fdc0b8-e602-3ca7-a28d-e863f83a7f6d | -8.36263 | -44.12676 | 2024-10-10 05:14:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 92c6b5f7-d355-3380-9cf4-1aeece6aed7b | -8.35904 | -44.08933 | 2024-10-10 05:14:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 63c57b1e-041e-346f-a508-8e24c186fb00 | -8.33988 | -44.09575 | 2024-10-10 05:14:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 5cbf0216-cdd0-3f84-84c5-762a81986ecc | -8.00433 | -44.36731 | 2024-10-10 05:14:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 38a30061-1f3f-31e0-a6d7-2f458098d48e | -8.00301 | -44.37622 | 2024-10-10 05:14:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| faf87429-9c56-3bfa-ad4e-3e3d1bbd675c | -12.98612 | -46.23732 | 2024-10-10 05:14:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 686800ed-3443-3c47-b3d3-3a865499c97a | -12.98474 | -46.2464 | 2024-10-10 05:14:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f456cb45-01b3-32aa-99bd-49dbf8473b94 | -12.97997 | -46.20288 | 2024-10-10 05:14:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 46ba84b3-d8bd-3d22-a4fe-ffe4065e849e | -12.97861 | -46.21194 | 2024-10-10 05:14:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 01e4617d-51ef-33c5-8930-db6dff46a03b | -12.97589 | -46.23003 | 2024-10-10 05:14:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 99988199-d8b8-31f5-8ed3-290e32886951 | -12.71229 | -45.46368 | 2024-10-10 05:14:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 7ab911cf-f54f-304b-8308-dced1e3a5ef2 | -5.91787 | -45.41221 | 2024-10-10 05:14:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7e7daeae-01a3-3612-9f5b-01e7835a6366 | -5.91649 | -45.4213 | 2024-10-10 05:14:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 45a5d2e6-af2b-3333-885f-8b195e931685 | -5.90752 | -45.41996 | 2024-10-10 05:14:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 49cc419b-cef3-362d-ac09-3a3460ba3dcc | -6.96294 | -45.27686 | 2024-10-10 05:14:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 990dca6b-8644-378e-bb49-1c499b2ed9ab | -6.96159 | -45.28577 | 2024-10-10 05:14:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 4493073a-25ed-3015-92a1-27d63c525a26 | -6.84706 | -46.21839 | 2024-10-10 05:14:00 | AQUA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 312c2c0e-8293-3fba-81cb-c95d015dc6d8 | -7.58867 | -46.80515 | 2024-10-10 05:14:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 3da4d82b-3860-33db-866a-6531488794ed | -10.27665 | -46.73759 | 2024-10-10 05:14:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c44a4e31-f037-3f15-9589-8b4118df7459 | -12.21022 | -46.72044 | 2024-10-10 05:14:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b3a290b6-d5d2-3669-ad03-c35ef435ed26 | -12.2088 | -46.72967 | 2024-10-10 05:14:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 78065cdf-58fd-3221-8827-efddcf34afd6 | -12.19985 | -46.72826 | 2024-10-10 05:14:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b5974d36-6841-3552-a383-ea5cd4c2b20c | -11.80024 | -47.39237 | 2024-10-10 05:14:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| eb7bcf46-e6b8-3804-b7be-6b7aaf6374d6 | -5.84256 | -47.41552 | 2024-10-10 05:14:00 | AQUA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 8a863013-203b-378b-b142-31e0c2d1c3bd | -7.02819 | -47.37469 | 2024-10-10 05:14:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9c7b91bb-ae8f-341b-b6d8-5c93df2fc51a | -7.01296 | -47.21992 | 2024-10-10 05:14:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 32b4804a-bad1-3ce8-bcbe-7657064821d8 | -7.01127 | -47.23062 | 2024-10-10 05:14:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e5b23451-eabf-30ec-a84a-343e427e1274 | -7.00934 | -47.22355 | 2024-10-10 05:14:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 29865749-038c-39dd-b2c3-c1b3612f0a8b | -6.98764 | -47.37992 | 2024-10-10 05:14:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2840173a-e23a-361c-a93c-583ef82f85aa | -6.98653 | -47.37306 | 2024-10-10 05:14:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cf94ff77-f3e0-379d-bc72-f575c1243b7d | -6.98489 | -47.38375 | 2024-10-10 05:14:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4d4d81cc-505b-3fee-8df7-2c0bf950973a | -6.93498 | -47.71112 | 2024-10-10 05:14:00 | AQUA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1b06e23c-be63-3aa7-af45-42589251dd6a | -6.93416 | -47.71564 | 2024-10-10 05:14:00 | AQUA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 907aee0a-265f-3c04-ad0b-5d428de66e48 | -6.93321 | -47.72223 | 2024-10-10 05:14:00 | AQUA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5000d9d3-b532-3a9f-9a66-6954cf65d830 | -6.93245 | -47.7268 | 2024-10-10 05:14:00 | AQUA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 37164bce-566b-3228-9ba0-85a6c4e99564 | -8.50166 | -48.63705 | 2024-10-10 05:14:00 | AQUA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 57c4e1ac-7ef3-310f-9cd6-bba848bb0b47 | -9.3671 | -48.80043 | 2024-10-10 05:14:00 | AQUA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 416e5aee-f6e3-33fa-b29f-875aaa8e1e8e | -10.60835 | -47.70405 | 2024-10-10 05:14:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 366e8500-d4fc-31f5-af8e-3c92adeee6af | -10.58066 | -48.02689 | 2024-10-10 05:14:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 20134a0c-42ff-32dc-9b2a-47414491b4af | -10.57871 | -48.01998 | 2024-10-10 05:14:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5c7bbaa1-925a-36c2-885d-db42a0742689 | -10.57708 | -48.03044 | 2024-10-10 05:14:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 482efb4c-c5bd-350b-b145-aa6647cce762 | -10.01735 | -48.84807 | 2024-10-10 05:14:00 | AQUA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| aeab8606-f506-3190-a771-6aa072189395 | -10.00711 | -48.84655 | 2024-10-10 05:14:00 | AQUA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6befc413-bc47-3e6a-a5ea-e7d3307714c4 | -10.98377 | -47.87918 | 2024-10-10 05:14:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fd1cbac1-b3c5-335b-91c0-87b1e84adc91 | -14.21361 | -49.74293 | 2024-10-10 05:14:00 | AQUA_M-M | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| a611b3ef-8f84-36a5-a306-faa6b0e9e909 | -14.21158 | -49.75513 | 2024-10-10 05:14:00 | AQUA_M-M | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| de82c6b7-85f9-36da-9b3b-0a3575d05f85 | -9.62518 | -48.98828 | 2024-10-10 05:14:00 | AQUA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d81164e7-3545-337d-98e1-b3c0f9bb18be | -4.82887 | -50.78176 | 2024-10-10 05:14:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 43b074ba-f23b-38aa-bc5e-772d58a55a8d | -6.31401 | -49.98613 | 2024-10-10 05:14:00 | AQUA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e8d4703e-1d6a-328e-afdd-c5f3d27859ae | -10.36272 | -55.8676 | 2024-10-10 05:14:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 22bc923b-0f20-39b2-928a-3683114093d5 | -10.36172 | -55.87588 | 2024-10-10 05:14:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 4b27745e-985b-354c-b8ae-632eb1fda4d5 | 3.29965 | -51.35722 | 2024-10-10 05:33:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52faab3a-a81f-3414-bd4c-714ffd6e832e | 3.29397 | -51.35823 | 2024-10-10 05:33:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18861e03-8d79-349a-af0d-d37cdb98fd48 | -2.46982 | -50.2433 | 2024-10-10 05:33:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ec86d74-fbba-3f9f-998e-99ccf35be086 | -2.95243 | -49.20122 | 2024-10-10 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e0b115f6-99a6-304e-9840-4c829d8ad2b8 | -2.95139 | -49.20816 | 2024-10-10 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c1a43560-7be2-33db-bc7b-400d4c9e9c82 | -2.95035 | -49.21506 | 2024-10-10 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| be74d571-b4d1-3e34-9ff2-fabeb72b36de | -2.7237 | -49.54603 | 2024-10-10 05:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 96afa547-ecd8-3d8b-a0f6-1892f67f281e | -2.60205 | -49.79441 | 2024-10-10 05:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f066f4e3-f4e8-3fbe-bfb5-bf4a8e01320f | -2.60112 | -49.80066 | 2024-10-10 05:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a39ab3d1-2d1d-3433-9865-8bb491af2a90 | -2.47645 | -50.24441 | 2024-10-10 05:33:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bcc0052d-9917-3d9f-8e4e-19087cee5ed5 | -2.47557 | -50.2502 | 2024-10-10 05:33:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b660d78-f3dd-39f8-8c6a-46c35cd16d0f | -2.474 | -50.24329 | 2024-10-10 05:33:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a9f91fe7-ace1-3baf-ae3c-b822885b0ab3 | -2.47316 | -50.2491 | 2024-10-10 05:33:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 690795c8-aaee-352a-ae53-6877a8b77569 | -2.8158 | -51.59905 | 2024-10-10 05:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4bc3cc6c-1586-34f5-b420-daf12032420f | -2.81578 | -51.59896 | 2024-10-10 05:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cd377056-48e2-3b72-a26e-cf1de0c5ee2d | -0.38976 | -52.05407 | 2024-10-10 05:33:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 746795cd-eb05-3fa2-b54d-965cc57e54c4 | -0.38884 | -52.05269 | 2024-10-10 05:33:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05165281-3632-33f7-96f5-d2323daba56d | -0.38818 | -52.05678 | 2024-10-10 05:33:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3aab3ca3-3f02-3b0f-b93c-d756cdbdf13f | -1.65626 | -53.33763 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1af5b3ad-56e8-30bb-9adf-459864386fdb | -1.65086 | -53.33687 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 662dd4fe-fbc5-32f3-8155-7c941249ac24 | -1.5348 | -52.9521 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c42c2df1-03dd-37e1-9641-9eedc0c5e3dd | -1.52928 | -52.95125 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f13ab2b1-762c-3e51-8d59-5295f486f460 | -2.25262 | -53.47412 | 2024-10-10 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dff8304-c8bb-3d72-9458-6ebac07a4518 | -1.92181 | -54.58104 | 2024-10-10 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33024573-b589-3cc0-93c7-4f159a5b1100 | -1.92138 | -54.58395 | 2024-10-10 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af2065a5-affe-36e7-b63c-fa5d6c394486 | -1.9207 | -54.58225 | 2024-10-10 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 288d6a38-95fe-303f-b74c-2da01c58f651 | -1.74243 | -54.24216 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4b268ca3-dc08-3a2a-8ee3-e8d80c1438a0 | -1.74198 | -54.24505 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f7f7451-a8a9-3052-83cb-4db6ffae4902 | -1.74152 | -54.24803 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 12c8c823-0205-31df-b7ff-b1b9a209caa7 | -1.70967 | -54.38708 | 2024-10-10 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff2eea9f-0324-3638-a34a-c2d6ca0463d3 | -1.70923 | -54.38995 | 2024-10-10 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 206c94ea-6864-3619-a928-e320fa6d9752 | -1.69457 | -54.38497 | 2024-10-10 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README126.md)
