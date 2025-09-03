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
| eb3e9b0b-9bb4-3742-bd9b-a80df850b4ac | -7.4873 | -44.821899 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3e7e2e2d-c68e-3824-93ce-056376ff1bda | -6.5287 | -42.946499 | 2025-09-03 00:24:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb8b6eaf-ac44-3629-b7ab-efd6a137d4ed | -13.2895 | -46.833698 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1c49d60d-d6ad-311d-8b20-63556fff3eee | -8.3777 | -48.300301 | 2025-09-03 00:24:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c822a21-1972-3fec-b488-faf1775e1ab3 | -11.0342 | -45.061501 | 2025-09-03 00:24:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 66540215-34bd-3578-8cac-2b2819dfb4d7 | -10.5339 | -50.404099 | 2025-09-03 00:24:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ba18942-db3b-38e5-9128-f9cd993db40d | -6.9678 | -44.354401 | 2025-09-03 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75a727e9-bbbc-3413-8ec6-761d79b09e11 | -5.7604 | -45.296799 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 284fba4d-3ce7-3636-ae28-55c92fa26eb1 | -5.7785 | -45.285599 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8fe6c2b2-d5b3-3d03-9f80-939f0c29e8ed | -5.6894 | -45.391899 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 700eb57b-8a4a-34e7-80f9-ef2a66d60247 | -7.7048 | -48.740299 | 2025-09-03 00:24:00 | METOP-C | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5dca5890-e31e-3b84-a9ab-f19f306b0e39 | -6.8461 | -45.5373 | 2025-09-03 00:24:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c81ce401-81f4-31f4-8ceb-e3f09b8ed4ce | -4.6563 | -41.956001 | 2025-09-03 00:24:00 | METOP-C | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 16856e52-ad27-31fd-aa3e-4040998b9145 | -6.8434 | -52.793499 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29c76fa0-a43b-35a9-b532-9606307a6b38 | -12.838 | -48.042198 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ccc223c3-a053-3243-87e5-de09ed8d26d4 | -9.6243 | -47.854801 | 2025-09-03 00:24:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4be8b4ec-fb37-3f00-9162-1415b750ac6d | -13.2681 | -46.8293 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5336fd6f-5f2b-3fe2-a243-565a3af0a777 | -12.8436 | -48.020302 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 391c3d4b-bc68-33a8-8ded-ec6997edb129 | -10.2863 | -47.5028 | 2025-09-03 00:24:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 479afb07-a591-33ff-8996-dc7d98085db7 | -7.4615 | -44.798901 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a2b526e1-f0ac-3172-96c7-6c483bda1c2e | -7.502 | -45.3395 | 2025-09-03 00:24:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f51aac32-9bff-3e93-b771-cf9d1c64fe80 | -13.3001 | -46.931702 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ba2c7796-36bd-3f31-8885-4b679302d7ff | -15.5513 | -48.3936 | 2025-09-03 00:24:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 49b828a7-391c-3426-8915-61b573724a3b | -4.0216 | -49.7645 | 2025-09-03 00:24:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0534caf-f09d-3819-ba9c-6ad158e0cfb6 | -7.715 | -50.2477 | 2025-09-03 00:24:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42396f28-17aa-3654-9480-dfe14381e20f | -13.2877 | -46.8251 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 170da5db-7f8f-341d-b746-88869ec4fcfe | -7.4842 | -44.808102 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d54df254-a1d3-3d51-b7fd-fad0b004ce41 | -15.091 | -48.129799 | 2025-09-03 00:24:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b958ccf4-3c0f-30b9-8c86-d7fa530de72f | -3.2169 | -47.116402 | 2025-09-03 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d6127e2-2d33-3e4a-8688-a0d394fbeb7e | -11.6047 | -52.124298 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd8dc4fb-b8e0-3279-b25a-28682cb5f75f | -6.9579 | -42.972198 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4274a73e-80df-3aaa-82b7-7c0e0a0dec1d | -6.231 | -42.423 | 2025-09-03 00:24:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 00865602-d1bd-3198-b872-300830769e23 | -12.8303 | -48.0541 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83ed5ff1-c831-3a06-b1eb-768ff8a3a1fc | -10.1374 | -46.2589 | 2025-09-03 00:24:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41d227b1-b31d-3f0d-b8cd-e5c15979fb10 | -7.4744 | -44.810299 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 95055415-f3ac-37dd-9908-644a45401150 | -12.8359 | -48.032299 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de0e743d-4040-3d0f-a3b0-15d09dacd179 | -6.1237 | -44.138302 | 2025-09-03 00:24:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0a6c479-94a0-3599-b994-62d46bc351af | -7.9358 | -46.534 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3a7fba9-aeb8-3264-aa30-7ae6048a7319 | -8.3562 | -48.295601 | 2025-09-03 00:24:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a228cef6-ec0d-30d8-b59f-279643022635 | -7.5246 | -47.4576 | 2025-09-03 00:24:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 577c33fc-a1b4-33f0-81c4-b356c1fc5773 | -8.0153 | -44.1092 | 2025-09-03 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fc8aaa5b-8b56-389c-b632-de0cc95fc7fb | -6.9911 | -43.248199 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9b792b46-d74f-37b5-a654-45339dfdc510 | -6.6867 | -44.163898 | 2025-09-03 00:24:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3dd1feb9-30de-3d48-ba98-f928a03fa447 | -6.7983 | -52.820099 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d29fa42f-dcef-35f9-ab9c-45258aaed0fc | -12.9957 | -48.113098 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93fb3eac-1075-335e-bb93-a97c49d63381 | -3.3689 | -47.149799 | 2025-09-03 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 374ce739-b52a-39e5-a59e-27f1e1edc0a4 | -7.5326 | -47.447601 | 2025-09-03 00:24:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ca8bbfd-1bf1-38a5-b16d-632ec16c2c7e | -6.4088 | -43.764099 | 2025-09-03 00:24:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4cbbd86c-a1ac-3104-98bd-2398626d0c61 | -4.7782 | -45.330502 | 2025-09-03 00:24:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75ab1d4a-9a7e-3b82-a36b-de8e5ad77b8b | -13.6992 | -46.882099 | 2025-09-03 00:24:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 95f3e4e9-5aa8-3410-af2f-6822ab9f0d7e | -10.486 | -50.3204 | 2025-09-03 00:24:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f35e735-fba1-3d85-8c7a-0287d5f35771 | -8.4583 | -43.6133 | 2025-09-03 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dd025954-db2d-3dcd-9b3d-25949bb48d21 | -5.792 | -43.239601 | 2025-09-03 00:24:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9f03e79-dc83-3e43-a117-8921d3ccb297 | -6.245 | -42.6152 | 2025-09-03 00:24:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 687a2602-3c30-355e-a44f-b33701c9010a | -13.5123 | -47.015099 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff44d9d5-af2f-3189-8a7d-a645eb26dd12 | -13.6945 | -46.9571 | 2025-09-03 00:24:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9e80f5d5-f56d-3f31-b9f4-fb5ea76db86d | -6.9612 | -44.370399 | 2025-09-03 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53e7006c-6f47-30f1-a244-914ade420837 | -12.8673 | -48.0359 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8bf31bee-b45b-37be-86ff-ceda37a8f73c | -5.8544 | -42.975899 | 2025-09-03 00:24:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 74a3ac01-4503-38e4-a154-9e6b1af666fd | -8.3679 | -48.302399 | 2025-09-03 00:24:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3912facd-f5a8-371d-843a-729950793cd3 | -6.0264 | -46.012001 | 2025-09-03 00:24:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7086842-461e-3fdb-8c64-7917b8fa5432 | -6.8274 | -52.813999 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a8c1d28-09f2-30fd-a633-ee9ef6ec8585 | -9.2385 | -44.4981 | 2025-09-03 00:24:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 58344d78-c885-36bc-b708-bad6f2fb2c54 | -7.921 | -46.467701 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c67481e-e6ab-3c8a-a783-485ffda2dbde | -8.0661 | -45.373299 | 2025-09-03 00:24:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ccb037bc-638a-3fa7-a180-7eb56a2b2605 | -7.9128 | -46.431 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83a468ec-0bfd-3709-8ec2-9157e726eb52 | -15.5559 | -48.4165 | 2025-09-03 00:24:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7f2a4613-b91c-348a-bbf2-f35c22f455b6 | -12.8575 | -48.037998 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27861977-ff1b-34ea-9b34-5190b24d4f0b | -6.7917 | -44.081699 | 2025-09-03 00:24:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05786265-fdac-3f27-8b3e-7317473a66a0 | -8.3796 | -48.3092 | 2025-09-03 00:24:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d10bdfad-a3f5-3bdd-a339-f5700c0197fd | -12.9936 | -48.103001 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45684fbb-d332-36b2-b299-c0e8a89206e8 | -6.7885 | -52.822201 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06f33921-c5cc-3f07-aaab-6f4c5c1dfc3c | -7.1097 | -44.748501 | 2025-09-03 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78ecc60a-1807-354f-b523-e5693a4fc7c5 | -3.3705 | -47.157001 | 2025-09-03 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca101084-2f0e-3f72-962d-56d13921fa96 | -11.3782 | -43.6161 | 2025-09-03 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 91b820ad-e72d-3664-815c-610860b9e69c | -6.8496 | -52.774899 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e7ccdda-d5c1-3134-906c-f2e4d4f3b6cc | -9.1817 | -45.203701 | 2025-09-03 00:24:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c22d0f08-c8f6-3a10-b7a7-cabffade34b6 | -7.9277 | -46.543598 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22082254-f755-346f-9180-bfa1bb4ccd98 | -11.3785 | -43.572102 | 2025-09-03 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17f569b7-eed8-355a-aaff-ca1bca244608 | -4.8862 | -44.947102 | 2025-09-03 00:24:00 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6fc546c-c037-3c2c-b077-e6c40db5a5bd | -2.8979 | -48.294601 | 2025-09-03 00:24:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2f39ac4-fd09-334e-b566-c17a058d5478 | -4.5541 | -40.3433 | 2025-09-03 00:24:00 | METOP-C | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 72a709d0-e12f-3170-a241-b987ae91ba4a | -12.7491 | -47.667198 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0000954-344c-32ea-a737-3cd44aef287d | -8.063 | -45.359402 | 2025-09-03 00:24:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 43d9f78e-9b8d-3b72-82b9-ba3e872e2c2a | -22.7022 | -47.030102 | 2025-09-03 00:24:00 | METOP-C | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8a49790b-f451-3993-9233-53345cbaa920 | -13.3287 | -46.825199 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 441037b1-e108-36ec-a8d4-f0f5be1119ea | -6.7752 | -52.807701 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28aba962-0784-3275-b700-bc0f08c53be4 | -8.8694 | -45.830799 | 2025-09-03 00:24:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bdc89b9f-5127-3371-a6aa-e83aff2699bf | -11.3576 | -43.5256 | 2025-09-03 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4e347ba8-f96c-3751-b849-ef0a10bf4e5f | -12.9015 | -48.101601 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e1f7f4e-c897-336b-81f4-dd50be29bc06 | -8.8662 | -45.816399 | 2025-09-03 00:24:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f28e6e4f-542e-3297-bf55-5531f8e120a1 | -6.6915 | -44.1847 | 2025-09-03 00:24:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18abcbfb-ab35-3fa5-ad20-2b237d6b7551 | -4.8386 | -42.735001 | 2025-09-03 00:24:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 51b808ee-3476-30b5-aab6-6199e206d37a | -3.1941 | -49.102402 | 2025-09-03 00:24:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f6282de-9ca5-3f26-9134-45ef5da20f77 | -11.8539 | -52.413101 | 2025-09-03 00:24:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 778f3138-6f54-3d1f-9c6f-c2f6c33d9a09 | -15.549 | -48.382198 | 2025-09-03 00:24:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 80e671d4-7322-3a85-814e-e6716241b2b3 | -6.4547 | -44.680099 | 2025-09-03 00:24:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9091b54-3209-3585-90c1-95231ab10f44 | -7.005 | -43.531101 | 2025-09-03 00:24:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ba7d4b67-3588-3cea-8daf-84312bbf650d | -9.5031 | -48.907501 | 2025-09-03 00:24:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 324504c7-7cd2-35a8-9f67-5b7803227eeb | -7.9375 | -46.541401 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
