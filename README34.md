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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10ebcc21-a8c6-38f7-bd0d-3cd62ed709e9 | -8.88152 | -49.54557 | 2025-09-12 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cde26087-ec0e-3ddd-a34d-11fa81bd53e9 | -6.53445 | -44.77176 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d59e9df9-2513-3967-a31f-2df44c551b76 | -6.8247 | -45.64563 | 2025-09-12 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| feadc7a5-7bcb-3eeb-9478-e5f0fdad63c9 | -7.75691 | -44.76742 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f6187ae-be41-3cbf-a548-55f88d26a36e | -10.48594 | -49.3739 | 2025-09-12 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53898320-0344-32a4-9a55-13b4509eb643 | -11.36606 | -43.51258 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6854a348-a448-3d0c-81d0-3ce42e791447 | -8.95831 | -46.08682 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83f15469-fc47-3004-842e-27e0e40fb748 | -7.15245 | -39.41967 | 2025-09-12 04:04:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 154e7c7e-ce44-3dde-850c-ad2f1c4828a3 | -8.64449 | -45.72224 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0603c0d-fbbe-3373-9996-42370f8798bd | -8.94844 | -46.06625 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68cef651-46a5-3d12-8b7c-1018c36ce316 | -6.65705 | -44.12767 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4fff3c5f-07a5-389d-b289-ba782d269bf4 | -10.55409 | -51.52983 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f69eb5d6-24a1-3ecc-bb5d-af08564c008c | -11.4266 | -43.53913 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 65311515-f389-309a-b690-3751d1b70226 | -12.12547 | -44.87296 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edb6171d-ca81-3896-a248-300b61be4a8a | -9.97007 | -50.38745 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9366a140-9046-37e3-8509-7c379be8e66e | -9.08389 | -46.95866 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ccb2cb8-61fc-3764-a4c6-e54251d53113 | -7.73685 | -47.42576 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bacd615a-0dc0-3843-ab3a-86c56f2ab976 | -11.66971 | -46.58631 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 959c4ea9-a78d-39bb-ac07-8d5921d727d6 | -8.8969 | -49.94462 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 20037bc9-650f-39db-beb9-b54435241cbe | -10.66979 | -48.6592 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a03a1cb-94e4-320e-bbb6-4523acac3d13 | -10.87525 | -45.56021 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 080ade59-5932-3585-807a-c0a1b0ec1ab1 | -8.43609 | -47.25402 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 206f31a0-01f8-3792-b4ca-597f3c4e094c | -8.87218 | -49.53696 | 2025-09-12 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b39d8cf3-cc56-3d85-8942-cabb67197062 | -9.85855 | -43.12856 | 2025-09-12 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 98e2b104-9c37-3fc2-9fa8-c30214386619 | -11.67628 | -46.54837 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27ad8120-85b6-3250-86ac-70618be6eb71 | -7.51877 | -44.68144 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fac92064-6440-39c1-af39-12ffc09d6807 | -11.29052 | -41.86613 | 2025-09-12 04:04:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1cec9913-5dff-30bc-aa12-4f1a19cb1499 | -11.68043 | -46.53645 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cc4328c-ecf3-3e03-ad4f-46a7dbdfe630 | -5.86495 | -48.15433 | 2025-09-12 04:04:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49596ed6-1931-3877-9d6d-8c58e55210b9 | -5.60474 | -45.78822 | 2025-09-12 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9274711-8238-369f-b3df-de2717543b9a | -5.96532 | -44.7224 | 2025-09-12 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2182e4d-c143-3a17-a923-2f737ebc793b | -6.94887 | -44.78192 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5447e5d-89c5-3f11-927d-d025c53cf133 | -11.1235 | -45.12323 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7fb212aa-071e-3057-9873-ea60d069143c | -8.36195 | -44.83707 | 2025-09-12 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7eb75f5f-7b2e-3b53-ba67-bdf569195914 | -6.10108 | -45.93732 | 2025-09-12 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e85e0f2-50f4-3c50-9abf-056453af64f2 | -11.67148 | -46.56239 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 468055ba-cc8f-3f30-a295-5b2106a697bb | -11.68591 | -46.52968 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7df343a4-9946-3dce-aec7-6882d0a846a7 | -12.1256 | -44.84993 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d38c522a-bef2-3c42-944d-7865b2c166a8 | -6.32612 | -42.21582 | 2025-09-12 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2b65446b-a835-3305-bcb5-d91594e1dfa3 | -10.21731 | -46.2393 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55ed5487-e05e-3554-ad02-51dac2d9bf93 | -6.38311 | -43.5169 | 2025-09-12 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 930adc59-d28e-3d70-972d-caa2bc129947 | -11.66839 | -46.59388 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5ab28f00-dd3c-31fe-ad04-d3d1af400dd2 | -6.84241 | -47.86407 | 2025-09-12 04:04:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 297ce9ac-db73-33bf-bfa0-c806be8346a4 | -9.11544 | -46.96102 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5dd8f4d-50a0-36ed-933f-cc8dc0187d7d | -6.68697 | -44.1374 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0047d1b3-736f-365c-a04f-ab6cb4ab3308 | -6.32488 | -42.22352 | 2025-09-12 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d84a880e-6be7-3295-a89e-ab373001257f | -9.45953 | -47.65018 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d1981fcc-8fbf-3d77-8e72-435a67a4d1df | -9.78213 | -47.84557 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca8e5191-e758-3d40-a9e0-77fbba6ff079 | -12.10809 | -37.97683 | 2025-09-12 04:04:00 | NPP-375D | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| 1f698544-f330-3f65-8568-765f607ab63a | -5.94725 | -42.78888 | 2025-09-12 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 68839452-c05c-39e3-880b-2150aaf259e6 | -11.67431 | -46.61766 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 457a730e-c186-33c5-8924-359f85ed52b2 | -9.89573 | -51.88179 | 2025-09-12 04:04:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd578905-4552-364f-a365-44f84c657d52 | -8.95263 | -46.06693 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a0bd8ce-987a-3420-b007-2793372e97c1 | -10.5515 | -51.53619 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 488f7bd0-f64a-3675-a578-7abe3ae3f502 | -11.67916 | -46.59081 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ab6eda96-6522-3382-900b-07419df70202 | -6.68698 | -44.12602 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f51c6bb-5be0-3b71-9059-f9d2326bdebb | -11.42595 | -43.5431 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 122fd5b4-93f6-3ee4-b026-85220409075e | -5.59574 | -42.90631 | 2025-09-12 04:04:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| c705a1a8-89e4-3a1a-9a44-12bc7922a001 | -6.90172 | -37.70348 | 2025-09-12 04:04:00 | NPP-375D | SÃO BENTINHO | PARAÍBA | Brasil | 2513927 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8e15cf59-d2d9-35bb-8f80-eb476fad73e3 | -12.10922 | -44.85637 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aed0f0c1-d2ac-310e-ac4c-e3b5dd550376 | -9.66904 | -47.5554 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de81fe90-5270-3ef6-ba0f-b1caac161803 | -9.72158 | -43.51623 | 2025-09-12 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9443f645-5563-341b-925e-0fa8258136b7 | -10.54186 | -51.53048 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 39e55fd0-14e4-3f06-89df-6204b4288304 | -8.07536 | -50.17486 | 2025-09-12 04:04:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0806797-c724-3fb0-a450-9591231a755a | -6.56011 | -43.14619 | 2025-09-12 04:04:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4fb9a43-4d5e-3b13-b8ae-e7886eea7540 | -10.11732 | -47.9147 | 2025-09-12 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 761c39e9-e48c-38fa-b3fb-a5f92592e966 | -6.05578 | -43.106 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b2264d7-8768-3bdc-a90b-cbdab9f869b6 | -11.42881 | -43.54765 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a851dcd1-c47b-3f9e-b6b7-91fae1cab4e4 | -11.42244 | -43.54251 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36cd8578-3fc3-395f-bf45-e0c4db75fef2 | -9.64468 | -48.06392 | 2025-09-12 04:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49a4eaf4-3a77-3346-a55f-fe565b148c91 | -10.13127 | -47.91707 | 2025-09-12 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15517f26-93d2-3dba-b1c7-ece3124013e0 | -6.65483 | -44.14114 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 80db1856-c3aa-373a-bbcc-674599742c06 | -7.45235 | -45.00372 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17ac32ab-bc71-3d5c-84ea-9ce6cbd9ed6a | -6.20714 | -41.01812 | 2025-09-12 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f7bcccc4-2836-3339-9754-cab15b418c58 | -10.84344 | -48.16299 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3f85f361-1205-3a8e-b8cf-b61c4d9c1934 | -5.59437 | -42.91463 | 2025-09-12 04:04:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6cf331d5-4a64-38d5-a663-77955bf91f4e | -7.45009 | -44.3967 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88e33815-6b6a-3ac6-82cb-685b53c6a09e | -11.08863 | -48.4106 | 2025-09-12 04:04:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ced11cb-611e-3af2-a77b-eb9ee2f012e9 | -8.00154 | -45.51552 | 2025-09-12 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74e8efed-e504-3171-a7a6-2106f38ba86a | -9.68439 | -47.54869 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71dfc142-f71b-3d0a-9fb3-8a6ce9525ef5 | -11.41592 | -43.70829 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a21b7a0-d9d1-3299-8afa-2d6fb3af12a8 | -9.66905 | -47.55828 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9229de33-9f90-33fb-8762-c80812277f16 | -12.11295 | -44.85686 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0604f170-a421-33cc-9c83-cbd626edb12a | -10.84722 | -48.16879 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1a5f8a1d-2ae2-3fe5-9892-b5e58457762c | -11.37022 | -43.50924 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ad493b5-3217-3f94-b598-6b02ed217489 | -10.5525 | -51.53825 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 77784ba0-8b3d-30a3-8ec9-543f235abe6a | -8.55278 | -48.95498 | 2025-09-12 04:04:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f847a4a-fa20-3bd4-b372-27819da08cb8 | -9.98989 | -51.72262 | 2025-09-12 04:04:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c97d6b6-cdde-3fa1-a41a-22693c2646f2 | -7.46802 | -45.30102 | 2025-09-12 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 422681c1-780e-35ae-bdee-a4cb0fc57a2e | -10.43465 | -50.6228 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a65113f7-f22c-3c74-abf9-7ceec65add03 | -6.1671 | -41.09599 | 2025-09-12 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9086adfa-2a95-3986-a145-094f759f615a | -9.07014 | -47.11693 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0cd6d63-e90f-3539-a02a-e2b8ba55e2c5 | -11.44018 | -43.56457 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1cfee71-af39-39d2-8693-92e74396299d | -6.34106 | -43.04824 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5298fc0-a583-3c94-b628-35955bc7517c | -8.37673 | -44.84475 | 2025-09-12 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dac52cf7-1f08-30ed-9196-c5248634f414 | -10.13671 | -47.91337 | 2025-09-12 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbff91a7-e1fa-317b-93d2-bb0b7b78c0ec | -12.12932 | -44.85047 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfff1c35-d9b7-37e5-8a1f-b1640c3ae57e | -11.67386 | -46.58699 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 472ca5a3-54f5-30e9-93f9-298632f964f0 | -10.5533 | -51.534 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6e75986-1aba-3ac7-938b-13df858ed6f1 | -6.63268 | -44.08468 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README35.md)
