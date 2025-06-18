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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b17c2bf-db4d-344f-9246-1b4eb287e497 | -4.69682 | -48.58328 | 2025-06-18 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6ad8bbb-f895-37b7-84d5-3c3fd310085f | -2.91809 | -48.23376 | 2025-06-18 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2ac6f3f5-a0ec-32d3-ad23-4f19b5270176 | -3.46 | -40.72016 | 2025-06-18 04:14:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 85acb93d-13a4-3ac2-909d-af1073479f88 | -4.3832 | -48.07369 | 2025-06-18 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de6a98f7-88e1-317e-a2b6-b0025fa7b371 | -4.54749 | -48.0166 | 2025-06-18 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6002bd8c-0e89-3b88-b24d-41dcb8d4e9d3 | -5.06072 | -43.24783 | 2025-06-18 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10999b41-9134-30e3-87dc-2d9504bf0cbd | -3.22378 | -54.86424 | 2025-06-18 04:14:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cfd9637-9945-3dc0-ac75-1a7d77a9fbf9 | -5.85142 | -43.63726 | 2025-06-18 04:14:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f22277f-3ecb-3f0a-88ff-19c05add1b95 | -4.55693 | -48.01058 | 2025-06-18 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2dd8ad8-7861-3df2-ab30-a8ce5c715dd1 | -17.69013 | -46.81388 | 2025-06-18 04:17:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dbdc487-8cc8-353a-9f67-63a1e3cca0f7 | -9.41769 | -48.4332 | 2025-06-18 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5bcf044f-e9e4-37c4-bb82-320f6d1f17f8 | -17.8417 | -45.98009 | 2025-06-18 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abc8d537-cb47-37dc-ae8b-fcaae094d9ba | -8.72792 | -49.02469 | 2025-06-18 04:17:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42eafd89-274c-3188-8b83-60e4106988ac | -10.85855 | -53.76348 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c95c232-ba38-31a4-8ff3-c147e29e985e | -9.14627 | -48.97191 | 2025-06-18 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e31ffb9b-1ead-3e5d-8206-79c4b7c5fd90 | -16.31092 | -58.24857 | 2025-06-18 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 808b9a87-31e5-3ddc-9748-9627c1d233b4 | -7.60582 | -45.55873 | 2025-06-18 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2d5f406-352b-37a5-a8a4-bcf5ba61d71f | -9.48637 | -56.09 | 2025-06-18 04:17:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f2002a97-3e1b-31cd-b1f8-a974945b6fd9 | -7.25458 | -44.64422 | 2025-06-18 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3a08b88-0128-308a-8870-7814906f548f | -11.62348 | -46.77383 | 2025-06-18 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36d66647-f22f-358c-b67a-888a6fa33a0e | -9.84427 | -44.7016 | 2025-06-18 04:17:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8dd86aad-46ef-3268-b909-717a9a952137 | -7.25516 | -44.64062 | 2025-06-18 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b102491a-a9eb-3cb4-9695-7765ae5c3ac5 | -10.5436 | -48.64686 | 2025-06-18 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6eb42602-0a4a-3027-bb2f-f67c1cb4fd91 | -11.14313 | -53.93371 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 86914ace-ebdc-3413-b4bc-7d16cf7d4728 | -6.41948 | -44.79732 | 2025-06-18 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 281ffde0-430c-382f-8671-5a43f849aaa5 | -7.26249 | -44.63807 | 2025-06-18 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92b59757-d65c-3c2c-8c9b-aa14ffe3a951 | -10.72805 | -49.56533 | 2025-06-18 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d048c42-2e56-30d6-8ac2-e59ddcc2e8fb | -8.22874 | -46.09726 | 2025-06-18 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d0c8ba0-90c3-3ec2-8f24-bfc4f45be7c5 | -7.16686 | -43.47126 | 2025-06-18 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c1f1446-74ed-3a20-a6f0-c6f23b2717c3 | -6.12126 | -42.5262 | 2025-06-18 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2e556fa8-4084-34a1-be56-d4876c46752e | -19.05756 | -48.33787 | 2025-06-18 04:17:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f7ecdc0-f79b-3b7a-86e5-09017af794b2 | -9.26963 | -49.61676 | 2025-06-18 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39112fda-7eee-39cb-8290-c37f7d039128 | -9.25968 | -50.04067 | 2025-06-18 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 48b336fa-5956-30a6-9f93-441b4af2aa1d | -7.25178 | -44.6401 | 2025-06-18 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c934527-86d1-3bf0-8346-5e56cab3324b | -10.65894 | -49.36593 | 2025-06-18 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b3a8165b-a33e-3a01-ac62-a1949b31a9af | -10.85245 | -53.7659 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00a20b51-1f31-3d75-b990-6f74554f354e | -8.32633 | -46.23096 | 2025-06-18 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d40b1864-e6e9-373d-8ff2-b128861f49cc | -6.16292 | -44.41829 | 2025-06-18 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 270f3c20-2e37-3d7c-bf42-ff5d4bbd3723 | -20.34996 | -40.35934 | 2025-06-18 04:17:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d50b578f-0ad9-3c21-852a-5307920843fb | -12.64334 | -44.04712 | 2025-06-18 04:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d8754cd8-85fd-3cda-b9a6-02844f66f7aa | -11.12598 | -53.9343 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ddc8dff7-b25b-3bd7-bd8b-68a9d5d38a13 | -7.21247 | -43.22555 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0332d5d7-2fb1-320f-ae67-ba714cb5e882 | -11.07774 | -55.05255 | 2025-06-18 04:17:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfe745e1-bea6-3d25-9f6a-37374e3a38be | -6.93796 | -47.25509 | 2025-06-18 04:17:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2cfbf8c7-3d19-3c41-8d6d-d2337088e394 | -10.57842 | -49.65251 | 2025-06-18 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9978423-4e2e-382f-a7c8-d91be4755a81 | -10.2992 | -57.14377 | 2025-06-18 04:17:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50633f06-9214-333a-adf2-489b7096ae0a | -6.6638 | -43.18502 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1f06dc53-002f-38cd-9f6b-83f37b45aefa | -8.603 | -48.06112 | 2025-06-18 04:17:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1db4d278-eb9d-3a83-8010-1ceaf87563d3 | -6.67322 | -43.19007 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d8cb0887-60e1-39e2-8b35-a93120462969 | -10.98878 | -45.09937 | 2025-06-18 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff6cab9b-f797-3dbb-a28f-07ade3a71af7 | -10.29242 | -57.1426 | 2025-06-18 04:17:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df1854dc-5235-34dd-b023-70cce2a960fb | -8.07956 | -43.10917 | 2025-06-18 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c0022054-7202-3cae-8c47-3786e2e4568f | -16.30961 | -58.25433 | 2025-06-18 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8ada28dd-435d-38bd-b384-1326b4344785 | -8.07303 | -43.1118 | 2025-06-18 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 34405cdc-6f14-3e42-b53f-50fc1622a0ce | -9.41683 | -48.43819 | 2025-06-18 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45e42383-e1b3-3814-a2cb-dae14857d455 | -10.5791 | -49.64871 | 2025-06-18 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4be086d-1d4a-3e46-bded-ebe740ab3755 | -8.0697 | -43.11127 | 2025-06-18 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4147bbbb-e49f-3211-b746-872bd9a40d95 | -11.33412 | -45.21781 | 2025-06-18 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24304776-b7fa-3db3-8f12-ba4b172581ee | -8.72658 | -49.02173 | 2025-06-18 04:17:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a18fe9bb-e2f4-33be-aa63-3cf0d5818ec8 | -10.6555 | -49.36155 | 2025-06-18 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8bea4932-b317-3e35-a143-5d7eba6e2d3a | -7.14728 | -43.2971 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5644154d-31fd-3d1b-bae8-a9138c1d64fd | -11.14173 | -53.94106 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 11770137-7852-3494-8980-055c9688d7df | -11.5814 | -44.6505 | 2025-06-18 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64e8f98c-c877-381c-955e-23f0aab29d93 | -10.91754 | -56.85039 | 2025-06-18 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ba4a374a-1c67-311b-9013-9e7c88123ce7 | -9.84988 | -44.68796 | 2025-06-18 04:17:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fc1e4e9-1199-30c4-9dc4-160a08a22e83 | -10.24098 | -52.22726 | 2025-06-18 04:17:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f4b57560-7607-31f6-a05d-e7c0f5e9171e | -8.72574 | -47.99896 | 2025-06-18 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5d1eaae-8c2e-3701-8ba7-f1dd6e05fb43 | -11.0856 | -55.06023 | 2025-06-18 04:17:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23654378-9e95-3f92-b972-d4ec295ef6eb | -12.09709 | -48.48413 | 2025-06-18 04:17:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a821d8f2-95f0-3183-8ba9-977e9f63927b | -11.93204 | -44.55137 | 2025-06-18 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 405b997c-a24f-3d1f-b52d-bf28afca2e72 | -10.50962 | -46.43242 | 2025-06-18 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5db1e864-6a78-309b-8aa9-140ee0f70c56 | -6.24284 | -43.36714 | 2025-06-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18f6d3a5-896b-3bf0-bbaf-3686980780f8 | -11.13485 | -53.94732 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0061ef7c-c800-3baa-8e56-6ed9eda628c1 | -10.73218 | -49.56606 | 2025-06-18 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6da2ee86-2a57-3c3f-86a5-01a801c7aa7e | -7.18589 | -43.20346 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e6ef1531-8829-30d8-9df7-c0e6bd0d9c0f | -7.4406 | -44.90011 | 2025-06-18 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9db670a5-4dc2-33a0-9665-41cd4a65ab00 | -9.27388 | -49.61751 | 2025-06-18 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36e3fc61-a89d-3daa-8a92-4e98d67a5f07 | -10.65486 | -49.36521 | 2025-06-18 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cfb2ce6b-2ca7-3edd-8d7f-4b5dcdd85c7e | -9.40112 | -48.43549 | 2025-06-18 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1b02a15-7960-39a4-8fcf-8d19942c1aa1 | -11.65961 | -44.64491 | 2025-06-18 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 035ff977-e28a-34b8-8cd4-d0662fb4c1f3 | -10.50897 | -46.43634 | 2025-06-18 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6da8111-6575-33d7-ae57-c0b0781d2321 | -7.30415 | -44.39905 | 2025-06-18 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a12c3236-bf42-310c-817a-c80ac5cc7ff4 | -8.42762 | -46.91401 | 2025-06-18 04:17:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd2d766f-6c0d-3276-8cde-840ab68a63b9 | -12.00801 | -43.85026 | 2025-06-18 04:17:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09e05348-24f0-3035-9258-a275273d101a | -11.12528 | -53.93792 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 10912578-8f3b-341c-a173-001dbd9e9a9e | -7.54262 | -45.65541 | 2025-06-18 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 061907cd-fae2-38c6-94ab-ecc5676a6fc9 | -9.8437 | -44.70514 | 2025-06-18 04:17:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3838aaa8-0e37-36bf-9e17-dc48865f55b7 | -8.59278 | -51.57 | 2025-06-18 04:17:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58a5eef3-783d-30ee-ac0f-0a4690231470 | -8.01806 | -50.90651 | 2025-06-18 04:17:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa8a84df-c8f8-36c4-b672-f418a1ff5ce9 | -10.11268 | -48.70337 | 2025-06-18 04:17:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c6f46bf-ab5b-312f-98f6-3ff3f92a8907 | -6.12404 | -42.5302 | 2025-06-18 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| cc2b6f52-246d-3633-a51b-759c78fa7fa3 | -8.45473 | -46.90429 | 2025-06-18 04:17:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 995ef197-873a-35ab-afa2-81ea265a246f | -10.70496 | -44.82314 | 2025-06-18 04:17:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edf23b65-49b8-3261-bb16-2f934183eb0d | -7.23216 | -43.10043 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c581e83a-b3fa-312e-aac0-811221c9e331 | -10.98544 | -45.09882 | 2025-06-18 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c485eab-80d6-39b7-aa82-2e10b7949c92 | -6.41608 | -44.79674 | 2025-06-18 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bec3acf-355c-3813-810b-8f5dcc836aa8 | -8.71834 | -49.02028 | 2025-06-18 04:17:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| caccdc47-e763-3d8b-9121-4ea0fd540a5a | -7.54199 | -45.65926 | 2025-06-18 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3ecbf20-f1a5-3afa-a058-49ac03029a12 | -6.68658 | -43.6874 | 2025-06-18 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a77115b3-87a0-3b6c-8aed-7b9139d2e145 | -6.13618 | -42.9736 | 2025-06-18 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README11.md)
