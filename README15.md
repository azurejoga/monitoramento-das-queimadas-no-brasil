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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21066c4d-ca32-3edf-8bf8-079aec8d39fe | -7.60194 | -44.7278 | 2025-07-14 12:29:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f8c23e07-337d-39ad-9faf-2f11da1c0223 | -11.5856 | -47.34426 | 2025-07-14 12:29:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 27091abf-03ee-3f2a-b81f-25a073865f7b | -6.13615 | -44.08552 | 2025-07-14 12:29:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0fea616d-4592-320a-92d3-18cb6c17fc43 | -8.81804 | -44.55585 | 2025-07-14 12:29:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ed61dc63-0c10-38f6-a954-65726b14efcd | -8.81455 | -44.54958 | 2025-07-14 12:29:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 9e1ef2d5-950b-3fc7-8255-f6126749de71 | -6.36602 | -43.64177 | 2025-07-14 12:29:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fcedb79b-2c07-3b1e-ab7d-1d67175a1661 | -6.83219 | -47.85462 | 2025-07-14 12:29:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7355cef6-0c2c-3009-9057-646f3d4ae648 | -9.80777 | -47.74698 | 2025-07-14 12:29:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4c153ffd-57de-32a3-a95f-629176fc37f3 | -8.91365 | -47.3512 | 2025-07-14 12:29:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b638c90c-bb31-3021-b9a8-4bb57235d008 | -11.58831 | -47.32421 | 2025-07-14 12:29:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 49da1fb0-8a17-3c1d-bc77-5f143d4d4042 | -6.1468 | -44.08738 | 2025-07-14 12:29:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| bd2a6515-feec-36f2-a9fa-26fb84100694 | -7.26878 | -45.31308 | 2025-07-14 12:29:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| d769cd68-82c9-3b82-aefa-d4b59f58a0e6 | -6.3858 | -44.74529 | 2025-07-14 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 19c7757e-dd6a-3d5e-bf84-a1a6b22da512 | -9.63207 | -48.27511 | 2025-07-14 12:29:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 22b79b11-47d9-318a-9772-152ce5af1e27 | -6.48041 | -44.86786 | 2025-07-14 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2e8fd56d-d13e-3037-be83-a0e4882c29bb | -7.92969 | -42.89418 | 2025-07-14 12:29:00 | TERRA_M-T | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 3aa23ae1-a569-3487-ad66-104ac1a0d3e1 | -11.47303 | -47.30618 | 2025-07-14 12:29:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4cc8b0c6-5992-3ee3-870b-62d9eef8362a | -7.58387 | -44.73185 | 2025-07-14 12:29:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 76371884-00db-389a-a2de-811ea2952a4f | -5.03535 | -47.97052 | 2025-07-14 12:29:00 | TERRA_M-T | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e1d6b442-e81a-32f7-977e-fdfc5bb47cf1 | -11.57899 | -47.32299 | 2025-07-14 12:29:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6ddc7237-b292-351d-8a11-172d63085538 | -8.19253 | -47.56151 | 2025-07-14 12:29:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d7b04427-1c92-3006-beff-ff755ab627a3 | -6.27359 | -43.39616 | 2025-07-14 12:29:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b3b4ece1-5bb8-39ab-bd7f-036024e4acad | -4.86214 | -43.22375 | 2025-07-14 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| c0e763b6-47eb-3f9e-90ab-78231f0badce | -11.78199 | -47.39365 | 2025-07-14 12:29:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| efba8e51-5f25-3e34-8c5e-3eb4b9ee17b6 | -10.69669 | -48.31456 | 2025-07-14 12:29:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5a675b70-40e2-3b9b-a4b4-b94856454a14 | -11.48005 | -47.30332 | 2025-07-14 12:29:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 36b84558-c037-3606-b345-007c329b427f | -8.04161 | -44.50735 | 2025-07-14 12:29:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 92cb4719-c7bd-355a-8196-7131f9fbaf4f | -7.92518 | -42.88791 | 2025-07-14 12:29:00 | TERRA_M-T | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 61806993-5345-376f-99e2-a928f39c0b9f | -7.27033 | -45.30164 | 2025-07-14 12:29:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e464cc75-6184-3acb-b141-4d1f50972859 | -8.60578 | -47.31266 | 2025-07-14 12:29:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3f6a936a-88c3-3f3d-abd1-67529d456bac | -6.40277 | -44.83905 | 2025-07-14 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 42b5a991-4ef8-3819-8d4c-e57370131566 | -5.02656 | -47.9693 | 2025-07-14 12:29:00 | TERRA_M-T | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 14593913-bfe9-3e7e-8f15-3774a8d6da0e | -11.58696 | -47.33424 | 2025-07-14 12:29:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 274.0 |
| 7389a08a-884a-3724-8123-b77ce14175fd | -12.20806 | -50.31149 | 2025-07-14 12:29:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8018d5c6-3195-3635-88b4-ff2bd99d2683 | -8.8198 | -44.54216 | 2025-07-14 12:29:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| d289fffa-2976-36ea-9d77-8af7a00cda4f | -10.71847 | -46.69863 | 2025-07-14 12:29:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4431f307-c668-3ba7-b501-5f13e434764b | -12.46098 | -46.91599 | 2025-07-14 12:29:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9fcc597a-7118-38fb-a982-ef10e46b0962 | -6.47126 | -45.3802 | 2025-07-14 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 2ac01124-e6cb-3dc2-89d0-54f00e7ee0c7 | -6.4012 | -44.8507 | 2025-07-14 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 52f52a57-fa5c-3482-8dce-21a7f02606f4 | -7.26914 | -43.50104 | 2025-07-14 12:29:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| ce7f753a-30c7-3d30-8176-070114f7e27f | -4.86273 | -43.21737 | 2025-07-14 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 08696674-307e-373a-a51c-4aca6323f025 | -5.39092 | -47.92265 | 2025-07-14 12:29:00 | TERRA_M-T | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 95a301e2-b9ef-3ffa-a0c1-efef7d215c20 | -9.87825 | -46.78192 | 2025-07-14 12:29:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cfd404f1-6a7d-3c4f-89a5-e1a63a7c6754 | -12.47061 | -46.91727 | 2025-07-14 12:29:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 15fa7ca1-a671-3488-b581-195c7f76d772 | -10.64813 | -49.42932 | 2025-07-14 12:29:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6bf29f5f-d696-3041-840e-c09087f6eab4 | -2.9095 | -48.23827 | 2025-07-14 12:29:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 402ad01a-48a3-31bb-b5bd-c5f838b091a8 | -11.71627 | -47.05688 | 2025-07-14 12:29:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 153359a9-500c-32cb-be4b-0dd73e2225b1 | -11.71904 | -47.03614 | 2025-07-14 12:29:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4c8e6de3-3318-366c-84e4-12842fb2fc06 | -6.14152 | -43.96258 | 2025-07-14 12:29:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e21867e9-4573-3c36-a6b6-374b35b41b6f | -7.60022 | -44.74084 | 2025-07-14 12:29:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4b6d860c-7b47-3640-afbb-5f697597cfa9 | -8.46453 | -49.58512 | 2025-07-14 12:29:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0be90f69-7e2d-346f-b17b-eee1bd4ae63b | -8.59539 | -47.32082 | 2025-07-14 12:29:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| fae80ab2-fe41-3cb8-82db-2f65eccb7c25 | -8.8746 | -46.89918 | 2025-07-14 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 815f6f67-545a-3c8b-83f0-ca55363889bb | -11.57764 | -47.333 | 2025-07-14 12:29:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 06a6791c-af59-3456-9145-8600547799f6 | -11.6316 | -48.54564 | 2025-07-14 12:29:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1d1b61e-313a-3650-824d-cd56a0f0e15f | -3.58621 | -47.51084 | 2025-07-14 12:29:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1ec21e34-5a70-38cb-983e-e7e88385e228 | -6.27154 | -43.41133 | 2025-07-14 12:29:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| ca8b1b69-9e61-34e2-a423-5f1218779252 | -4.86741 | -45.29989 | 2025-07-14 12:29:00 | TERRA_M-T | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 1182ef90-ac88-3aea-a69a-74c6b0726c7a | -5.69646 | -43.66894 | 2025-07-14 12:29:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 742051dc-5971-34bd-ad4c-fe39d284c73c | -12.10344 | -46.44304 | 2025-07-14 12:29:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9b7224c6-eab0-30d4-9d66-fb40865a2a81 | -7.52734 | -45.36638 | 2025-07-14 12:29:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7be4c80e-6232-3f46-a930-fd7e3d1385c5 | -11.03539 | -47.07197 | 2025-07-14 12:29:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c45f6772-46cf-3f8a-bf82-fa684a4ca07f | -12.20052 | -50.30109 | 2025-07-14 12:29:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 701b3a3b-9080-3f62-bf1d-65e74d79aee6 | -8.5118 | -43.30238 | 2025-07-14 12:29:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| d6dc717c-e9d7-3245-893b-bf93d9892095 | -8.86938 | -46.86841 | 2025-07-14 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3c35e400-b1e5-39eb-af1a-0d10ac7c3509 | -7.58563 | -44.7191 | 2025-07-14 12:29:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8199bbb9-2678-3965-a826-2198bfb426cb | -12.47204 | -46.90647 | 2025-07-14 12:29:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 09cb6ed0-fb6c-3db8-abe5-28ea223245ea | -10.39516 | -46.68943 | 2025-07-14 12:29:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 94e8e11b-5c04-3ccd-bdfb-203b15e27d39 | -6.97864 | -47.0812 | 2025-07-14 12:29:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4554d0ab-5744-314f-a495-1364aa5fcb7b | -12.4624 | -46.90515 | 2025-07-14 12:29:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| a705c455-4221-3130-96f6-f7c14e13965c | -7.66899 | -45.96865 | 2025-07-14 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| b8a3accd-5c52-3c74-a249-bcfa9dde1509 | -10.39375 | -46.69987 | 2025-07-14 12:29:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 83ac762f-fc57-3ed1-a916-f63a9d7ddc32 | -8.43843 | -45.80221 | 2025-07-14 12:29:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b98b2d7f-9b09-3b22-91a5-6e9466459149 | -3.58495 | -47.5196 | 2025-07-14 12:29:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 91930556-4de5-3a18-a512-f57f6240e397 | -6.46151 | -45.37859 | 2025-07-14 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 46463dbc-49d5-35d5-b234-c7d57aebcf87 | -6.83345 | -47.84576 | 2025-07-14 12:29:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d53f02fe-b492-3893-8d3a-915c6982510b | -7.02915 | -44.35956 | 2025-07-14 12:29:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 85165a5e-274e-33c9-b5f8-32e95dd6d3db | -7.25967 | -46.986 | 2025-07-14 12:29:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0e3e8366-87e4-33bf-b7e8-98f4f45ba264 | -6.12708 | -42.53228 | 2025-07-14 12:29:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 45c2ccd6-2c63-3b7f-a304-f96263877d0f | -10.3857 | -46.6855 | 2025-07-14 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| beda22be-4962-3313-a1c4-41e66aaa8dfd | -15.2328 | -46.9489 | 2025-07-14 12:32:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 67f9edf5-b558-371d-8a3e-a2b811d94914 | -16.06671 | -53.74731 | 2025-07-14 12:32:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ec05fee6-ae4f-3d21-83e2-9fcdfdbe9ee9 | -18.53436 | -44.66503 | 2025-07-14 12:32:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 26.9 |
| cd1dbd8c-b4b5-36fe-9582-6dd3a7209d3d | -18.40393 | -44.18901 | 2025-07-14 12:32:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5f7a721f-af80-3465-ba62-9b53e8b12a66 | -17.50358 | -42.3618 | 2025-07-14 12:32:00 | TERRA_M-T | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 21.1 |
| d05fad2b-87eb-30b2-88dc-14105cc5a790 | -14.68406 | -52.68806 | 2025-07-14 12:32:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 80afbebd-93b1-3ae1-aa86-8bcc5886984b | -19.7375 | -47.43167 | 2025-07-14 12:32:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 10664397-e15e-3386-8a9a-ea4c04fbc527 | -14.52694 | -58.92459 | 2025-07-14 12:32:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 35.5 |
| bd0af0a8-4c6f-3280-a857-2023439771d9 | -14.52423 | -58.93005 | 2025-07-14 12:32:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 30.8 |
| b1bf9e34-4451-3208-a591-b79e7a6dbe04 | -16.06744 | -53.74088 | 2025-07-14 12:32:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f34f7907-a221-39bf-b069-1903b3d3b5fd | -16.30338 | -48.26701 | 2025-07-14 12:32:00 | TERRA_M-T | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 41f7b69c-85b3-3187-8491-49867e9407cc | -21.70214 | -56.14436 | 2025-07-14 12:34:00 | TERRA_M-T | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f624c162-2ed9-35c8-875f-5e25edf5cf10 | -20.5578 | -54.12673 | 2025-07-14 12:34:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 33.1 |
| ccbbe6b3-5954-3f69-a4d5-5e985e891b17 | -12.4608 | -46.9045 | 2025-07-14 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 398537ce-93ec-319c-a296-7018c993e754 | -11.5929 | -47.3379 | 2025-07-14 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| d71277da-eed0-3c5e-92e6-85eea90ef70b | -12.4121 | -45.3628 | 2025-07-14 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 70a3f064-85b4-37c2-8654-eb709894710c | -12.3928 | -45.3658 | 2025-07-14 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 18121410-8e3a-3d1d-b176-215299168442 | -10.3857 | -46.6855 | 2025-07-14 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 813e27a8-dd14-326f-91be-45e65166cf16 | -12.4121 | -45.3628 | 2025-07-14 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 8a1dc4e2-be30-31f2-ade8-ab42a5258381 | -11.712 | -47.0538 | 2025-07-14 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |


[Clique aqui para ver as próximas entradas](README16.md)
