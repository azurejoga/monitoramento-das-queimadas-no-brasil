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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebf0138d-4abe-31c0-9c24-460872fcb320 | -6.91872 | -44.81081 | 2025-09-17 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41d3e7f3-833c-3c59-9fe0-623000696611 | -4.66509 | -46.31793 | 2025-09-17 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f8d0832-9a22-3d56-8525-1455c1bde9e0 | -5.19269 | -35.86673 | 2025-09-17 04:10:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 011eb2c6-8641-319e-83bf-e84f4230536e | -6.26081 | -44.68076 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c72fe53-5c85-3c96-8360-b1b6ac000693 | -8.27505 | -49.78645 | 2025-09-17 04:10:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d493f04-5778-36b0-b233-9e84cbbd86b2 | -2.26468 | -47.8859 | 2025-09-17 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dfc3265b-cfb7-3ffb-958f-4049b0ee813a | -8.1689 | -46.76664 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed791da5-4954-3151-9616-2c88787d644e | -7.67514 | -44.47071 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60dafc43-c2b6-3a44-9aa1-0d00672eb4fb | -9.38107 | -45.38322 | 2025-09-17 04:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1415a004-05f3-3c0c-8e8c-8b319608ab8e | -7.53129 | -44.72162 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d49f8630-807e-3b9e-a4b9-bca46ef06245 | -7.66353 | -45.13746 | 2025-09-17 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce49d4f9-9f90-338d-b8b7-fe9500391f66 | -6.6262 | -45.59192 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 030fb5d3-24b8-308e-87c3-bd4e19f602b9 | -6.18848 | -45.11571 | 2025-09-17 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60804797-8b88-35da-8f2b-47098743b6c5 | -8.90236 | -46.28173 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1df90e1d-0c4c-3157-b8b7-cd48823e7fa1 | -7.32697 | -44.06046 | 2025-09-17 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fbc01547-9a5f-3445-91e2-84af650eb1b3 | -8.98245 | -45.03619 | 2025-09-17 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77eb23cf-01f9-3a0a-ad2f-8d7f9337e58b | -3.50576 | -48.45001 | 2025-09-17 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 42514c4e-7aca-3f17-b767-3dd6e62eb559 | -8.01906 | -45.65496 | 2025-09-17 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 679dd405-92f1-3499-aa69-4107858988ee | -3.23261 | -46.79123 | 2025-09-17 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 31b780eb-62cb-3378-b635-4393d045f4bc | -6.4015 | -43.35627 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 06c4cfd6-9afc-386f-9512-6a270db11c1c | -8.56683 | -46.33896 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 417fe293-5f57-3aad-9ceb-6c45a27bea29 | -6.40134 | -41.79126 | 2025-09-17 04:10:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4dd6452d-c29f-3d34-9239-33ca7e39ec0e | -3.75679 | -38.70204 | 2025-09-17 04:10:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 85eb53a8-34ff-3c76-bcd9-6cc21b07f0d5 | -9.07697 | -50.3143 | 2025-09-17 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42e3adcf-3fd1-3320-ad20-26a2f7f6d31a | -6.28978 | -42.38305 | 2025-09-17 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2cd235b3-8923-3802-98c4-d9080994bfb5 | -4.05591 | -47.49975 | 2025-09-17 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3990d825-88e2-37fc-85d1-6985aa38f3c5 | -6.16256 | -44.52614 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53289058-b407-340e-86b9-42ada4dfb17a | -8.9695 | -44.1914 | 2025-09-17 04:10:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d07f739-32d4-30ad-8948-4c300a94cec0 | -6.87506 | -43.97511 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| feedfc3c-ce02-350c-9353-435b5bd6757b | -6.30092 | -42.39928 | 2025-09-17 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20b2b7e5-bc43-3b09-82b5-8a5846dcb625 | -7.2679 | -46.58359 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9e8bbcc7-c402-3062-a253-01c83e95fd42 | -9.15787 | -47.01513 | 2025-09-17 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1bf4871a-b0cb-30e8-a393-bdd890ce01ee | -9.11019 | -44.85165 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56996cee-b58c-34fc-b100-4b4b8c1fe869 | -3.31005 | -42.16552 | 2025-09-17 04:10:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| dd6dc3f6-e566-3e2c-8871-5fb55f4adbd4 | -8.5699 | -46.34446 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1c3637fb-0bda-396e-9a26-707f2a5ed23a | -3.30948 | -42.1691 | 2025-09-17 04:10:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2a7b56c9-9fe6-3f3b-923f-2a94cd75bd79 | -8.1649 | -46.76602 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0022efaa-11b3-37f4-a2e9-733b8c38e740 | -8.53591 | -48.97354 | 2025-09-17 04:10:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38071484-667f-39f0-bebf-e9825d606fd9 | -7.37658 | -47.04227 | 2025-09-17 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e1cc5f1-a850-3ed9-92d8-2ff093633a96 | -8.9848 | -45.75018 | 2025-09-17 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56c336e4-5522-3016-96cb-c3f71429819a | -7.50601 | -44.35355 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 645c444d-3630-3944-bca0-ae18a5477d2a | -8.66459 | -46.40277 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 865ec84e-a481-3a64-8fce-f7584717b84b | -4.38938 | -38.68901 | 2025-09-17 04:10:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ba41b8a2-fec6-36ba-bff1-37a3a41ec59e | -7.26393 | -46.58272 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2dbef2bd-942e-30af-b0ac-a64a7639957a | -8.96845 | -45.75663 | 2025-09-17 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27e0aaad-883a-349e-a760-879521f9c430 | -7.88765 | -48.16978 | 2025-09-17 04:10:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31d5c4de-5549-3891-aadb-22e58cb6aba9 | -3.17847 | -48.81556 | 2025-09-17 04:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c7e35162-8bfc-387a-a9b0-4cebb61e144f | -6.30036 | -42.40277 | 2025-09-17 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f65b3662-82a4-34cb-8e3c-2ecbdc3830e0 | -8.9267 | -46.2088 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a2e4cb56-5f4d-3a27-ade7-20fdd685101a | -6.34631 | -43.15871 | 2025-09-17 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3c08b84-06bd-3351-8136-0b2f1353e662 | -6.59496 | -44.32372 | 2025-09-17 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7cb7ed6-83b5-3fc6-8906-15d30ac01585 | -5.32999 | -44.99747 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5acbff9c-7b67-3acc-ba48-8e7fcb90d727 | -7.58638 | -44.56727 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4363f405-3324-31ac-886e-6864a64be04a | -5.56854 | -45.0312 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3961e573-a461-36ae-adb2-83b80772d38f | -9.54979 | -46.29591 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d192559-23ef-349f-9429-7244ad98751e | -7.76892 | -44.72829 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83edce87-2a6e-3f3c-ae23-aa619059d6c2 | -3.89778 | -40.92076 | 2025-09-17 04:10:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43113f43-80af-3d24-9588-e9bf1da155ed | -7.31807 | -43.95728 | 2025-09-17 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34472286-ced5-350b-ba34-2795d11a72db | -8.96839 | -46.0104 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55de21cb-738e-3c5d-9a1b-a87bbff1147a | -3.50663 | -48.44479 | 2025-09-17 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59e8b3c3-15f1-309a-b9a2-6af0f87ba63d | -5.61423 | -51.7217 | 2025-09-17 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| de2c6e25-a5fa-3cb8-8a56-288228b801ae | -8.57901 | -46.3432 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1e3f410-279c-35b9-b598-0139467bfa18 | -6.87568 | -43.97125 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3403b32-478b-3252-96bb-beea1e5b5e40 | -9.09829 | -44.9241 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 646b3692-dccb-3778-b9aa-0176c93adb31 | -6.30148 | -42.39578 | 2025-09-17 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 160de690-4b04-3d38-b3c0-1ea4937ce8b6 | -7.60973 | -47.46782 | 2025-09-17 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c180a9e2-16be-356f-897b-04ac8ceaba0d | -6.19893 | -45.12184 | 2025-09-17 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 52ae5714-132c-3f26-a70d-922919d64cab | -5.21767 | -45.42727 | 2025-09-17 04:10:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a48a4f0c-06aa-301e-97cc-1b899efb1db8 | -6.25548 | -43.45982 | 2025-09-17 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7dfb1c3-ee04-3846-80c7-61d59318c271 | -5.49097 | -43.99098 | 2025-09-17 04:10:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 907f3640-011b-344c-ae2e-20858b226f37 | -8.67586 | -46.36209 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca12b3d3-fa64-36fe-a8de-077717803151 | -5.6365 | -43.89078 | 2025-09-17 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 044a599c-0336-39ea-a35a-95b8ec3ee16a | -6.29535 | -42.39117 | 2025-09-17 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 749baa33-172b-3d00-87b3-357058de531d | -5.08617 | -41.16766 | 2025-09-17 04:10:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e3f9f1ae-b944-37b1-bea4-01b4ef79fda7 | -6.76547 | -43.39874 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 46fb9cb3-f28c-3764-bae1-10f88bf9b74e | -8.97591 | -46.01178 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0603830e-e336-3636-9782-b088ca935759 | -6.96819 | -44.55491 | 2025-09-17 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| adde44ef-3f5d-3902-943a-eddb7aafc0a3 | -6.96494 | -44.46296 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c622c31-a199-3a56-bd4c-066d2b9f8214 | -6.24453 | -43.46188 | 2025-09-17 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ae2a92b-abf1-327d-b4df-7651b2cdd739 | -9.15048 | -46.93852 | 2025-09-17 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c205951-9c1a-34ee-8f03-f71fbddadcb9 | -8.16182 | -46.76007 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c701c27-901e-38d7-9a0b-42f665116eab | -7.39933 | -50.00809 | 2025-09-17 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 54620449-ebbe-3482-8a16-ee20f2af0143 | -6.16206 | -45.98895 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64a208e6-aa56-3e4f-80de-3b77b1f0a3ee | -6.96886 | -44.5508 | 2025-09-17 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5526043e-6532-34fa-95f2-723b7062ff86 | -8.57984 | -46.33836 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3ddc7d4-61b3-3f9f-8e79-e73105eafc8e | -4.66099 | -46.31727 | 2025-09-17 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24bb1aeb-5f38-356e-acd5-21988da981e7 | -5.60296 | -44.11784 | 2025-09-17 04:10:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ede3de27-393c-3459-a0cd-e9ce93ed4478 | -2.37771 | -47.63726 | 2025-09-17 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 12ab374b-f608-3463-a7c3-1c20b7a8b830 | -6.21972 | -42.02352 | 2025-09-17 04:10:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e61a3a4a-34fb-3042-9ebc-c9774c57e71b | -6.4267 | -44.37589 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ab7428a-39ee-3e54-9c4b-a2fef86bc3bb | -9.11241 | -44.86033 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 230214f0-29c3-3b93-a1b3-a45341906a3c | -7.66203 | -44.67426 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d003392-91ed-313b-a131-78f08d519c31 | -9.06644 | -44.93964 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c52b4cd-18cb-3f4f-834d-585e6f497669 | -8.54089 | -48.97688 | 2025-09-17 04:10:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fccd3ed-7445-3d61-9aec-e2b9165f493d | -5.99418 | -43.69118 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3976a7b-7d40-3bb0-a091-df0a93a6045a | -6.40424 | -42.66747 | 2025-09-17 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2c55e84c-c5a0-3357-9a9c-aac9f080efd8 | -5.63444 | -51.70888 | 2025-09-17 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c1a8895-d9ae-3d2a-91b9-9ba025b3d41d | -5.47695 | -45.34805 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3586ea83-7bd7-375b-919e-9842a3cac22f | -7.21301 | -44.38221 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0a6b088-526d-3343-bd6e-c642bab7b6cc | -5.63373 | -51.71288 | 2025-09-17 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README22.md)
