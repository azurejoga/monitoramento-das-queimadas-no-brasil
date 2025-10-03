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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1d36333-34d8-36ae-810b-1e9765175507 | -6.3775 | -44.6313 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19fe56a9-daf3-3070-a275-0c188de35168 | -7.8013 | -46.02045 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59fac8cf-8751-3eb5-9c71-aba88dd39fda | -6.75907 | -44.80885 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de0e943c-a090-3c4e-bf11-c00af83ad642 | -6.55307 | -44.15323 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5e320b6-5170-3daa-a58e-825568e059fe | -6.97584 | -44.39431 | 2025-10-03 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99262ce9-6f88-3292-a251-d9146b6072ad | -5.79031 | -45.75761 | 2025-10-03 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d73f0eb-057f-3400-97ab-88404ede89d0 | -7.30752 | -45.26506 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2574a143-fc1a-3fb2-a234-2cdada613249 | -6.35047 | -43.95753 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce875f5c-b2b1-3ef5-aa7f-52db4c2e99c9 | -8.33187 | -46.22499 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10a18ea5-c0d9-3e1e-b117-86b34c72f9d1 | -6.38237 | -44.76062 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0c02a0b-cb87-32c1-857f-b7ee4d3c59aa | -4.66123 | -45.80684 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| e23d2d8d-8e58-3ced-8609-0188ed521757 | -5.97584 | -44.1546 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e1d4122-29cb-305d-9a03-65a1f202e719 | -7.05996 | -43.23037 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4678e509-bb0e-3ec0-b843-ab602aa80162 | -6.8739 | -44.5144 | 2025-10-03 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c31661b-2779-33dd-a849-237442ca5319 | -7.25465 | -48.48346 | 2025-10-03 04:10:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ba04b8f-b577-3549-b4fb-6273d972cce9 | -5.54597 | -44.64992 | 2025-10-03 04:10:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 089361bc-6716-39d8-a9fb-3a5851327fb1 | -7.74992 | -46.25698 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f704a6f3-b603-35b0-aa4a-8c4ddb053fb4 | -0.90425 | -47.54795 | 2025-10-03 04:10:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b6ea5b1-c1cb-3745-bec4-442354dc763f | -1.08585 | -53.67963 | 2025-10-03 04:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3041db70-ef07-3e18-aaf0-acd33d2224bf | -6.70787 | -44.61876 | 2025-10-03 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a406350-1b66-3c00-a5b4-0297e6661c58 | -4.94025 | -38.00237 | 2025-10-03 04:10:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 5fd875e8-a087-33db-a2da-fcf5eeaba48a | -5.2625 | -42.9165 | 2025-10-03 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6c1c0697-cd19-3fb1-8449-e6577e016e7c | -3.69837 | -49.01202 | 2025-10-03 04:10:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ecdb451-1147-3d39-928c-0adcd11590a7 | -6.13526 | -44.03659 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f83a7670-496d-3137-ba89-33d7c58440ab | -6.19968 | -39.69727 | 2025-10-03 04:10:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f49b8edd-a4a0-34f0-966a-20f100100173 | -7.25015 | -48.48256 | 2025-10-03 04:10:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1e34d7c0-3b8d-3239-b8a2-9eb21dcd61a2 | -5.54277 | -51.13395 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0152f52b-84b5-3149-87d5-4410ad64fe08 | -7.75318 | -42.5721 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7cb9a944-b1ef-3940-930b-caa461670a8c | -0.89953 | -47.54724 | 2025-10-03 04:10:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dbbe8974-09c5-3c6c-a4af-da51416d593a | -4.66849 | -45.78751 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 416407bf-f0aa-3f48-b63f-67edd7fd00b4 | -6.33601 | -43.03761 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a9d863b-f76d-3379-99d1-13c500d441e9 | -7.77163 | -42.52103 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 96a791dc-9228-373f-bf40-969749bb7d2c | -7.74444 | -42.59172 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9750252d-0190-3b38-a529-714e9c0cdc47 | -7.76701 | -42.61411 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 893d4e91-1ce2-39f1-8121-0fcc78136ab5 | -6.65215 | -42.79187 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b3e965ef-4fce-3582-bfd6-5e281cd3d6b2 | -4.6503 | -47.54787 | 2025-10-03 04:10:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3812a1e7-ee4a-3c9f-a424-bc057f1255f6 | -8.8353 | -44.7994 | 2025-10-03 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 631f0008-d85c-3550-b46d-5850a2f25114 | -6.40916 | -43.83971 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dd8ed80-09c1-35c3-9d9e-5ea17ce0d468 | -4.67559 | -45.7936 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73d8b53e-1fd4-3fdb-9c18-ae04e4837445 | -5.05753 | -40.95268 | 2025-10-03 04:10:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1f07a7ee-a834-3942-849f-78509d7b9158 | -7.56078 | -42.40057 | 2025-10-03 04:10:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7abf95e4-87bc-3164-a56f-a2f7fd4972d5 | -7.00246 | -47.18302 | 2025-10-03 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffef2f4d-b7e9-3047-9cf8-eeed1470bdcf | -6.27129 | -44.04544 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff5bdac8-d31c-30e0-ae39-191d98cc7344 | -5.90543 | -39.14878 | 2025-10-03 04:10:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 850c6fb5-0028-3317-98ff-37286906c175 | -2.92638 | -48.3097 | 2025-10-03 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26f993bf-a44f-39ed-8f5a-8489c9f1acc9 | -8.21989 | -45.54636 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c7fb60e-bf3b-3fb3-a909-1071834052bb | -2.92681 | -48.31195 | 2025-10-03 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 684059d6-a332-35c1-bc1e-86a51605ce7b | -7.76202 | -42.60243 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 663e38f7-208d-3c68-bc7a-acda28820393 | -6.3503 | -43.40509 | 2025-10-03 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56c10eff-19b3-3c97-9e83-b3916c61e24c | -5.63839 | -44.51636 | 2025-10-03 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4fa8580d-050b-3002-8216-f093d02e157d | -7.29158 | -46.00805 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e27dd939-397f-30dc-a3bf-ab50b709a26e | -8.58667 | -41.06285 | 2025-10-03 04:10:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 569595cf-a3dc-380f-b6ca-311069a35b73 | -7.05375 | -43.22561 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ecf90fb7-d08e-364e-b889-a1764b61e236 | -6.59438 | -44.32378 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1e5d416-41f5-398b-8abd-8965ab288e42 | -7.30981 | -45.26456 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03f2ac43-625a-3a39-a827-8ced72dfaea1 | -7.76379 | -46.26957 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 59fd3a4b-2f3e-3f7f-b1ed-f0102336e154 | -5.446 | -44.82294 | 2025-10-03 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1e060c1-9541-3366-b503-4ed4a54c603a | -7.75152 | -42.56103 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| f69358f1-b42f-36da-b061-e609930f8bb4 | -6.61252 | -44.29689 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfd56f40-4389-30dd-ba16-acd84371249b | -4.66687 | -45.79729 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 4ad93791-2515-3f21-aa23-00d6c188e244 | -7.76038 | -42.59131 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2e9ac8a4-0110-36b5-9466-9944532ffc31 | -6.22907 | -44.23783 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67dd5bcd-6585-3a17-9309-be42a8033b50 | -3.82569 | -40.41887 | 2025-10-03 04:10:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e9838a4c-3d60-3dc5-b9e0-2d14849046ea | -5.63743 | -43.90432 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e7cccbb-6d6d-3aba-b7de-844a6bee9447 | -7.76155 | -42.56263 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 55218e1d-d70b-3788-8efa-5e9d9734c9bf | -8.21763 | -45.537 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a6efe52-9f99-3f8a-af76-91acac09a64b | -5.48804 | -52.13633 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16baed21-f40b-35f4-a783-4c1a6c01b6c0 | -6.03015 | -44.63093 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca8b3522-5001-3652-bb80-de33bc5b1fa7 | -7.71611 | -46.19752 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a0141ea-9641-37ff-8d7a-c8f55bc15b58 | -2.24997 | -47.87637 | 2025-10-03 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 72ccfccb-35bf-3c86-a614-a8c69e3c4fd1 | -5.75002 | -44.61059 | 2025-10-03 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 11573a38-58c1-3c5b-a050-56c7a896d736 | -7.79225 | -42.49915 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7e08bf5b-6362-34c3-8307-ff0d263b30f1 | -8.04241 | -44.11305 | 2025-10-03 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59425271-ad5b-3acf-8e11-09beffd66a97 | -5.48856 | -45.40351 | 2025-10-03 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d4917ff-9791-3c69-9fa4-7a19a8b63070 | -7.24976 | -49.41724 | 2025-10-03 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c8e4ed32-c4c1-36b0-bd60-612f78e9f3dc | -7.25157 | -49.40671 | 2025-10-03 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42bc344a-fb05-38ed-b7e7-180059a919a8 | -7.76423 | -42.61004 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 47849afc-a26a-339f-b2c3-a9da24e092ad | -4.32068 | -38.12829 | 2025-10-03 04:10:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c090e173-7604-3ed6-a83e-b7cb7b200075 | -6.55883 | -43.89497 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 791d4a63-5189-3408-ac78-b031dee9daeb | -3.84255 | -41.57491 | 2025-10-03 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a6a95abc-7781-36ce-b19d-70bab2c0f340 | -7.71144 | -46.20157 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 92ee06cb-89fa-3ac9-8859-9db7e98c77c1 | -7.88981 | -47.35003 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1c59bc3-0506-3da5-8f8a-c35cc7adc2d2 | -8.17549 | -47.01464 | 2025-10-03 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4230b122-12ce-3508-94a4-0372775687e8 | -7.77736 | -47.37457 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 89d1d1b8-31b5-34e3-bab9-d0d3fce9047e | -4.26479 | -48.55526 | 2025-10-03 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 139eae47-5697-3950-9350-cc03b0be45bc | -6.70827 | -42.80817 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 27cb9331-b012-3aab-b66f-dc1e27e8ab1d | -4.66533 | -45.78209 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6106a5c-c79a-362a-b45e-51150b781be3 | -6.6667 | -42.80883 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0e5ede0c-0d69-3788-b41b-8d43d7b33b96 | -4.55654 | -50.46994 | 2025-10-03 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c81b99b8-6598-33cc-89f9-c5c51a61bf9a | -6.22677 | -45.35744 | 2025-10-03 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a3b412b2-db1a-3c94-ab7c-00ec8ac63fa9 | -6.33481 | -44.03088 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 105efe5b-259b-3e9e-8e9c-59db76a670fe | -5.78258 | -45.75624 | 2025-10-03 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff8c737b-ba41-3b17-8a13-66bc37287139 | -8.59679 | -44.76057 | 2025-10-03 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b0ed003-1d5b-3c1a-ae43-5a9d42ef4231 | -3.19495 | -51.03192 | 2025-10-03 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1602b8d-99cb-313b-ba43-7d0eef4fad2b | -7.42182 | -40.07099 | 2025-10-03 04:10:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 52ee2765-26fd-3569-b433-ca1d7ae820b4 | -8.24469 | -47.02223 | 2025-10-03 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 672b295e-3c52-3f03-addd-0af3138481f5 | -6.32927 | -43.88711 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17f2684c-6137-3977-8569-f8f25bebfd83 | -7.79778 | -42.5288 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 41c9ba6a-9589-3a93-a5aa-c64d7dbbb0c2 | -5.19669 | -42.78357 | 2025-10-03 04:10:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77837665-f82c-3a92-8191-a48491d3f8f7 | -6.8768 | -44.51913 | 2025-10-03 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README45.md)
