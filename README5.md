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
| 4aa83825-303f-30c0-a9ae-9f382ba97c76 | -2.32956 | -47.2075 | 2026-07-25 04:49:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36995052-44e7-3511-bc12-1177f8eb154a | -2.48069 | -47.08829 | 2026-07-25 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a8f8cc7-d8b2-35fc-bf6f-747e4795842d | -2.43456 | -51.85192 | 2026-07-25 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2ca5bbe-f5e9-3c16-a322-7dc8ad36914b | -4.43784 | -40.92568 | 2026-07-25 04:51:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b564fc56-4a41-30ad-9625-758392d7fd32 | -4.00074 | -50.85783 | 2026-07-25 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3db9a1d-1a49-3491-aa72-e7f0cdc986bd | -9.08412 | -59.48046 | 2026-07-25 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70b44805-0c08-397a-b029-a4f7a6911229 | -4.18333 | -48.58121 | 2026-07-25 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6d0e437-2643-3568-82ba-9808f0a20ed7 | -9.99885 | -51.4739 | 2026-07-25 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a16778c4-499c-3922-8294-0f3df26ec6a8 | -9.18724 | -58.06382 | 2026-07-25 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 789afe9e-55a7-3d85-94e2-7ec89db466aa | -11.00249 | -47.4786 | 2026-07-25 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0fdc268-256c-33f1-8a87-aec0920f6ddf | -8.83413 | -47.08339 | 2026-07-25 04:51:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1bba682-81c8-3ea2-8efc-d8e44c15c1b6 | -7.01434 | -45.42836 | 2026-07-25 04:51:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a0bdf277-7314-3869-812d-8340bb17c257 | -9.19119 | -58.0645 | 2026-07-25 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5402344b-920f-3318-8d03-6cc5406d5ca6 | -7.01584 | -45.43128 | 2026-07-25 04:51:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 079cc28c-bb95-35d5-82ca-ae191bac5142 | -3.82117 | -50.63359 | 2026-07-25 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3348425-d54e-399b-bd73-cf4abe2c8d1e | -4.37371 | -47.76948 | 2026-07-25 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fb85b126-7b56-35ba-a25d-1082b4a0be8a | -4.0002 | -50.86137 | 2026-07-25 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7e298d3-cdfd-326c-aeab-ec93419ab858 | -10.27243 | -46.74215 | 2026-07-25 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02eac81a-ee94-372a-a957-c18fdd851594 | -4.18268 | -48.5856 | 2026-07-25 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b01eb168-9acf-3763-8532-f9e66d9283b7 | -7.01516 | -45.43626 | 2026-07-25 04:51:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 77efe488-ff98-352a-9de2-2745b334275e | -2.90189 | -54.55895 | 2026-07-25 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01545605-305e-3af8-8bd0-82f48ffbe772 | -3.80015 | -51.18674 | 2026-07-25 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e99a27f-5755-35a9-aaa4-f9ea47095e96 | -8.67736 | -47.84003 | 2026-07-25 04:51:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 753d541e-cb0d-3129-a82c-ef5b82f2c111 | -9.99543 | -51.47337 | 2026-07-25 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53a2e2ed-5f56-38de-a5e3-f1bd78847000 | -9.16449 | -58.32251 | 2026-07-25 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fa36949-1d92-3afc-ae56-67f12c0f2f07 | -8.68144 | -47.84066 | 2026-07-25 04:51:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a733290b-e21e-3ba9-a908-8c9dafca1de4 | -4.06093 | -43.24744 | 2026-07-25 04:51:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7f099b8-cd71-3d1c-8c15-3f80116380d1 | -9.08338 | -59.48464 | 2026-07-25 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50b07846-fbe5-33cb-8f79-94db90cc7541 | -4.18305 | -48.58696 | 2026-07-25 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77c71d37-108c-3c58-8c59-c58179bc9882 | -8.38387 | -48.21228 | 2026-07-25 04:51:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ae9ffd85-3621-3eef-8756-d8a070ed6d08 | -8.38314 | -48.21742 | 2026-07-25 04:51:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bbb12fa2-8cfb-3392-82a0-d604c94ab039 | -9.47877 | -57.31855 | 2026-07-25 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b6c7438b-3f25-321b-9c7a-8a151b499e74 | -5.96721 | -51.39893 | 2026-07-25 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37825e48-0bf7-3d66-9389-1f60dcfa391a | -8.8918 | -60.59987 | 2026-07-25 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 075bee3e-62a4-3863-88bd-a6fcdb479d7e | -7.01905 | -45.42896 | 2026-07-25 04:51:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 47775d4b-7466-37ac-8980-e55e1648b1ad | -3.95982 | -48.1263 | 2026-07-25 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e76aa3f6-368e-3d32-bf15-98926bef62ab | -10.68007 | -46.35176 | 2026-07-25 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| db33d04d-7d1c-337d-abde-bf55aeb0dc90 | -11.00306 | -47.47438 | 2026-07-25 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 672aa499-5781-3a30-a683-b5201a4d1bb7 | -8.28487 | -49.60638 | 2026-07-25 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8da8d5cc-6550-3961-a41d-dc4c76501a77 | -3.80068 | -51.18328 | 2026-07-25 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fc726977-0d23-30a6-ac12-af603b0c9347 | -5.09057 | -47.94534 | 2026-07-25 04:51:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 887543f7-ae4d-3684-90c1-509ba0f16d14 | -5.09128 | -47.94056 | 2026-07-25 04:51:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d72c23d-f66d-339b-9db5-ed9906aeada8 | -2.81878 | -52.28852 | 2026-07-25 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f040331-5c3c-3ef4-8064-4a2c8281d2bc | -9.16498 | -58.32648 | 2026-07-25 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a978ee65-5d27-3f75-8d8a-fc09996592fb | -10.27314 | -46.73693 | 2026-07-25 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a71d2240-8ce1-351e-96c7-9a998dbc5b43 | -4.18373 | -48.58258 | 2026-07-25 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4e858c3-f579-3785-a562-54caba5e7375 | -9.15987 | -58.32544 | 2026-07-25 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b4141b3-6b7c-33c0-8ccf-17549c55fb7d | -4.28438 | -48.23441 | 2026-07-25 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cd4addf-5dcc-3937-b7ea-ddb3a17c9ba6 | -7.01652 | -45.42626 | 2026-07-25 04:51:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 332aa7bf-bec8-3c38-ba31-54c5a1c9db32 | -3.48482 | -47.67579 | 2026-07-25 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c55a443-6cfe-3e67-8bb5-59d6b94b7c6c | -3.99755 | -43.2802 | 2026-07-25 04:51:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df3c6f6d-ebee-3003-9d45-94b35357785f | -2.91444 | -54.16236 | 2026-07-25 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c8225e7-03cc-35e0-aa45-5079cf829eee | -4.36985 | -47.76888 | 2026-07-25 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 79603bce-4030-30aa-af33-e18aa439f4d8 | -4.05569 | -43.24673 | 2026-07-25 04:51:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 690bcd4e-2ae9-35af-9b13-64f8913fc191 | -10.0057 | -51.47495 | 2026-07-25 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 528c6d62-3924-3ea9-b3b3-f5aa709efa36 | -3.79736 | -51.18277 | 2026-07-25 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddd581f7-ae17-39d8-90cb-7e754a101cdb | -3.99628 | -43.28226 | 2026-07-25 04:51:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c70957c-7eb4-341a-9909-b36c258b49d0 | -8.28121 | -49.60585 | 2026-07-25 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03e063bb-4b7a-3172-9fc5-00e385d6251a | -4.94215 | -48.23951 | 2026-07-25 04:51:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e91b94a9-aad7-36ef-b6c1-c7a700b9adba | -2.91307 | -52.72966 | 2026-07-25 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df2ecd37-a5d3-3355-8c97-d96331100f45 | -9.99829 | -51.47765 | 2026-07-25 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5499c415-e747-3f48-8470-da59c04211c1 | -3.99581 | -43.28543 | 2026-07-25 04:51:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fb4c6d1-46f8-31a4-9c84-d03042983ba8 | -4.06665 | -43.24488 | 2026-07-25 04:51:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d120fa8c-6541-3a32-bc59-c1bca6181d75 | -10.00284 | -51.47066 | 2026-07-25 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3e0f176-cb08-3f6b-8f88-97a1f8e0d76b | -8.72071 | -54.53806 | 2026-07-25 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 920572ed-3479-34ec-9cea-4177dc55d189 | -7.01506 | -45.42333 | 2026-07-25 04:51:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| aa54cac8-78d8-39cc-a9df-4c9a162baa6b | -9.88612 | -49.98281 | 2026-07-25 04:51:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ebdff65-2913-3c58-b69f-8eb48d80b9d1 | -10.00513 | -51.4787 | 2026-07-25 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0f19d54-61f8-39ce-aef1-abe71de928a2 | -3.99676 | -43.27909 | 2026-07-25 04:51:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| defcd6fe-ecbd-39da-90f9-ba026521ee5b | -4.37057 | -47.7641 | 2026-07-25 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4ec19efc-90f5-360a-9413-3a6868fe31c0 | -7.0118 | -45.42564 | 2026-07-25 04:51:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| deb14082-682e-364b-96b4-bd43248dd075 | -8.72128 | -54.53446 | 2026-07-25 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59e8fbac-0565-3512-ada8-21cda05be91f | -9.16389 | -58.32611 | 2026-07-25 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7dc82f13-e12e-308c-96c2-1670e4543ce1 | -4.43788 | -40.92622 | 2026-07-25 04:51:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5282d023-6461-3541-80a9-a0d632f76841 | -3.9971 | -43.28337 | 2026-07-25 04:51:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c959827e-aaa5-3b6f-9965-3bd9f698bc67 | -7.01113 | -45.43065 | 2026-07-25 04:51:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 114e9a82-41f0-3774-bb06-3791760f1d7e | -3.7329 | -49.27206 | 2026-07-25 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea2d332d-476f-3425-b553-8c0ea8926113 | -7.01292 | -45.43829 | 2026-07-25 04:51:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6a13e59b-c21f-3b45-b48a-73f046d8db1c | -10.26351 | -46.74014 | 2026-07-25 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cde31e5-b8ad-30b6-bce3-0deb13b12ec5 | -9.17427 | -58.32065 | 2026-07-25 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2141b795-1ea8-3313-8e72-010ad648b2c2 | -3.67377 | -58.73875 | 2026-07-25 04:51:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a09266ca-ce79-3f65-848e-1b41488eb021 | -7.01363 | -45.43333 | 2026-07-25 04:51:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e10accf8-ca1a-3d3a-a068-01b0fe938ecc | -9.1656 | -58.3229 | 2026-07-25 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f4e5f0d-d4e1-3193-a62c-6ad1d99b49b5 | -7.16915 | -59.32191 | 2026-07-25 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1f2bc22-d2a4-3af2-b9d1-400d993232b3 | -9.17828 | -58.32134 | 2026-07-25 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db63e5fa-0af6-38c4-a301-3eee5d902ae9 | -9.16046 | -58.32186 | 2026-07-25 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cc58a7d-05ba-331b-8ef4-76cbb364aca9 | -4.27313 | -48.23262 | 2026-07-25 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ec398ad-2cd2-3fdb-936e-a12bb0a47394 | -8.28425 | -49.61066 | 2026-07-25 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 988264b7-cf21-3fa8-b31e-b2403099d94c | -3.72937 | -49.27154 | 2026-07-25 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b084789-671d-34ab-b0d1-f235babbbd55 | -4.18006 | -48.582 | 2026-07-25 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2e93940-3e8b-3f76-8be4-704196837284 | -4.18606 | -48.59186 | 2026-07-25 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47c7be79-b09a-319b-be87-1fb4a4f42cbf | -9.88247 | -49.98226 | 2026-07-25 04:51:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20aeee71-04ad-372a-8061-7df4c2cfa386 | -4.18571 | -48.59053 | 2026-07-25 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb36a6ad-9a59-3098-af87-1c6472f42a8e | -8.8933 | -60.60231 | 2026-07-25 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eb9251d1-cda0-3df8-ab0d-f4c92b8732a9 | -2.81548 | -52.28801 | 2026-07-25 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee8bfd9d-184a-3384-b1dc-ab1d1347473b | -10.26865 | -46.73617 | 2026-07-25 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec872a81-0cc4-3279-8625-e997e849a4bc | -11.80344 | -47.09006 | 2026-07-25 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| bf400b22-8698-3b45-be61-e4b0e04c5b92 | -11.64688 | -49.46803 | 2026-07-25 04:53:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5590409-9b18-3029-87fd-97f2546ec5fb | -11.92827 | -47.64017 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64d88be2-97d5-3903-9919-c429924e0a0b | -10.83328 | -49.39307 | 2026-07-25 04:53:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README6.md)
